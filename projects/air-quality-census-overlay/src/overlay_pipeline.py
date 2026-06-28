"""Area-weighted overlay for census geography and PM2.5 polygons."""

from __future__ import annotations

import argparse
from pathlib import Path

import geopandas as gpd
import pandas as pd


CENSUS_GEOJSON = (
    "https://gisdata.kingcounty.gov/arcgis/rest/services/OpenDataPortal/"
    "census___base/MapServer/2884/query?outFields=*&where=1%3D1&f=geojson"
)
PM25_GEOJSON = (
    "https://services8.arcgis.com/rGGrs6HCnw87OFOT/arcgis/rest/services/"
    "PM25_Concentration_v2/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"
)


def pick_column(frame: gpd.GeoDataFrame, candidates: list[str]) -> str:
    lookup = {column.lower(): column for column in frame.columns}
    for candidate in candidates:
        if candidate.lower() in lookup:
            return lookup[candidate.lower()]
    raise KeyError(f"None of these columns were found: {candidates}")


def load_layers(census_url: str = CENSUS_GEOJSON, pm25_url: str = PM25_GEOJSON) -> tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]:
    census = gpd.read_file(census_url)
    pm25 = gpd.read_file(pm25_url)
    return census.to_crs("EPSG:3857"), pm25.to_crs("EPSG:3857")


def area_weighted_overlay(census: gpd.GeoDataFrame, pm25: gpd.GeoDataFrame) -> pd.DataFrame:
    census_id = pick_column(census, ["geoid", "geoid10", "objectid", "name"])
    pm25_value = pick_column(pm25, ["pm25", "pm_25", "gridcode", "value", "concentration"])

    keep_census = census[[census_id, "geometry"]].copy()
    keep_pm25 = pm25[[pm25_value, "geometry"]].copy()
    keep_pm25[pm25_value] = pd.to_numeric(keep_pm25[pm25_value], errors="coerce")
    keep_pm25 = keep_pm25.dropna(subset=[pm25_value])

    intersections = gpd.overlay(keep_census, keep_pm25, how="intersection")
    intersections["overlap_area_m2"] = intersections.geometry.area
    intersections["weighted_pm25"] = intersections[pm25_value] * intersections["overlap_area_m2"]

    summary = (
        intersections.groupby(census_id, as_index=False)
        .agg(overlap_area_m2=("overlap_area_m2", "sum"), weighted_pm25=("weighted_pm25", "sum"))
        .assign(pm25_area_weighted=lambda df: df["weighted_pm25"] / df["overlap_area_m2"])
        .sort_values("pm25_area_weighted", ascending=False)
    )
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("outputs/pm25_census_overlay.csv"))
    args = parser.parse_args()

    census, pm25 = load_layers()
    summary = area_weighted_overlay(census, pm25)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(args.output, index=False)
    print(f"Wrote {len(summary):,} census exposure rows to {args.output}")


if __name__ == "__main__":
    main()
