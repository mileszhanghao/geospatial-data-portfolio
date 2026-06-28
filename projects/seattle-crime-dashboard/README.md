# Seattle Public Safety Dashboard Workflow

This project summarizes a Python workflow for exploring Seattle public safety incidents and translating raw public records into spatial dashboard views.

## Portfolio Files

- `src/build_incident_map.py`: public-data pipeline that fetches Seattle incident records, converts them to geospatial points, joins them with neighborhood polygons, and writes a Folium HTML map.
- `data_sources.md`: public API and FeatureServer endpoints used by the workflow.

## Methods

- Queried the City of Seattle Socrata/SODA API with date filters on `report_date_time`.
- Cleaned returned JSON records with pandas.
- Converted latitude/longitude records into a GeoDataFrame with `EPSG:4326`.
- Joined incident points with Seattle neighborhood polygons.
- Compared incident categories across time windows.
- Built a campus-centered buffer view to focus on nearby incidents.
- Used Folium-style interactive mapping to inspect spatial clusters and popup details.

## Result

The dashboard workflow showed how incident categories and concentrations can be compared across periods and neighborhoods. A 750 meter campus-adjacent buffer made the analysis more actionable than a citywide aggregate by focusing on high-foot-traffic corridors and nearby commercial areas.

## Product Value

This work demonstrates public API ingestion, geocoded event cleaning, point-in-polygon analysis, buffer-based spatial filtering, and interactive map communication.

## Portfolio Boundary

The original notebook export is not published because it contained course scaffolding. The public version keeps the reusable engineering pattern: API ingest, geometry normalization, spatial join, campus buffer filtering, and dashboard-ready output.
