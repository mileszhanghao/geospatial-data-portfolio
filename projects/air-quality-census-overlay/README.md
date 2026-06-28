# Air Quality and Census Overlay

Environmental exposure workflow that combines census geography with PM2.5 concentration polygons from public ArcGIS FeatureServer endpoints.

## Product Goal

Which populated census areas should be prioritized for air-quality screening when a city team needs a quick environmental exposure view?

## Public Workflow

- Load King County census geography from a public ArcGIS REST GeoJSON endpoint.
- Load PM2.5 concentration polygons from a public ArcGIS REST GeoJSON endpoint.
- Normalize both layers to a projected CRS before measuring overlay area.
- Intersect census and PM2.5 polygons.
- Calculate area-weighted exposure values by census area.
- Export a ranked CSV that can feed a dashboard, static map, or policy memo.

## Portfolio Files

- `src/overlay_pipeline.py`: cleaned GeoPandas pipeline for area-weighted environmental overlay.

## Stack

Python, GeoPandas, Shapely, ArcGIS FeatureServer, GeoJSON, area-weighted aggregation.

## Why It Matters

This is the kind of geospatial backend logic that sits behind an environmental justice dashboard: not just drawing a map, but turning multiple public layers into a decision-ready exposure table.
