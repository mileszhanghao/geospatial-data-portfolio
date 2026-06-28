"""Build a Seattle public-safety incident map from public data APIs.

The script keeps the portfolio version independent from private notebook
exports. It shows the reusable pattern: fetch civic API records, normalize
geometry, spatially join events to neighborhoods, focus the view with a campus
buffer, and publish an interactive Folium map.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import folium
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point


INCIDENTS_URL = "https://data.seattle.gov/resource/tazs-3rd5.json?$limit=5000"
NEIGHBORHOODS_URL = (
    "https://services.arcgis.com/ZOyb2t4B0UYuYNYH/arcgis/rest/services/"
    "nma_nhoods_sub/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"
)
UW_CAMPUS = {"name": "University of Washington", "lat": 47.6553, "lon": -122.3035}


def pick_column(frame: pd.DataFrame, candidates: list[str]) -> str:
    lookup = {column.lower(): column for column in frame.columns}
    for candidate in candidates:
        if candidate.lower() in lookup:
            return lookup[candidate.lower()]
    raise KeyError(f"None of these columns were found: {candidates}")


def load_incidents(url: str = INCIDENTS_URL) -> pd.DataFrame:
    return pd.read_json(url)


def incident_points(frame: pd.DataFrame) -> gpd.GeoDataFrame:
    lat_col = pick_column(frame, ["latitude", "lat", "y"])
    lon_col = pick_column(frame, ["longitude", "lon", "lng", "x"])
    category_col = None
    for candidates in (
        ["offense_parent_group", "offense", "event_clearance_group"],
        ["crime_against_category", "initial_type_description"],
        ["type", "category"],
    ):
        try:
            category_col = pick_column(frame, candidates)
            break
        except KeyError:
            continue

    clean = frame.copy()
    clean[lat_col] = pd.to_numeric(clean[lat_col], errors="coerce")
    clean[lon_col] = pd.to_numeric(clean[lon_col], errors="coerce")
    clean = clean.dropna(subset=[lat_col, lon_col])
    clean["portfolio_category"] = clean[category_col] if category_col else "Incident"
    geometry = [Point(xy) for xy in zip(clean[lon_col], clean[lat_col])]
    return gpd.GeoDataFrame(clean, geometry=geometry, crs="EPSG:4326")


def join_neighborhoods(points: gpd.GeoDataFrame, neighborhoods_url: str = NEIGHBORHOODS_URL) -> gpd.GeoDataFrame:
    neighborhoods = gpd.read_file(neighborhoods_url).to_crs(points.crs)
    return gpd.sjoin(points, neighborhoods, how="left", predicate="within")


def campus_buffer(points: gpd.GeoDataFrame, meters: int = 750) -> gpd.GeoDataFrame:
    projected = points.to_crs("EPSG:3857")
    campus = gpd.GeoSeries([Point(UW_CAMPUS["lon"], UW_CAMPUS["lat"])], crs="EPSG:4326").to_crs("EPSG:3857")
    mask = projected.geometry.within(campus.buffer(meters).iloc[0])
    return projected.loc[mask].to_crs("EPSG:4326")


def write_map(points: gpd.GeoDataFrame, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    m = folium.Map(location=[UW_CAMPUS["lat"], UW_CAMPUS["lon"]], zoom_start=14, tiles="cartodbpositron")
    folium.Circle(
        location=[UW_CAMPUS["lat"], UW_CAMPUS["lon"]],
        radius=750,
        color="#1f77b4",
        fill=False,
        tooltip="750 meter campus analysis buffer",
    ).add_to(m)

    for _, row in points.head(1000).iterrows():
        folium.CircleMarker(
            location=[row.geometry.y, row.geometry.x],
            radius=3,
            color="#d62728",
            fill=True,
            fill_opacity=0.6,
            tooltip=str(row.get("portfolio_category", "Incident")),
        ).add_to(m)

    folium.LayerControl().add_to(m)
    m.save(output)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents-url", default=INCIDENTS_URL)
    parser.add_argument("--buffer-meters", type=int, default=750)
    parser.add_argument("--output", type=Path, default=Path("outputs/seattle_incident_buffer_map.html"))
    args = parser.parse_args()

    incidents = load_incidents(args.incidents_url)
    points = incident_points(incidents)
    joined = join_neighborhoods(points)
    focused = campus_buffer(joined, args.buffer_meters)
    write_map(focused, args.output)
    print(f"Wrote {len(focused):,} mapped incidents to {args.output}")


if __name__ == "__main__":
    main()
