# GeoPandas Urban Analysis Workflows

This page summarizes Python geospatial workflows built with GeoPandas. Raw notebook exports are kept private; this page preserves the portfolio-safe analysis patterns and technical substance.

## Workflows Represented

- Reading public GeoJSON and shapefile data into GeoDataFrames.
- Checking and aligning coordinate reference systems.
- Creating choropleth maps from numeric and categorical attributes.
- Using dissolve and aggregation to summarize spatial units.
- Running spatial joins between point events and polygon boundaries.
- Using overlay operations such as intersection, union, and difference.
- Comparing wildfire point datasets across time windows after CRS alignment.
- Interpreting raster-derived terrain change from LiDAR data.

## Tools

Python, pandas, GeoPandas, Shapely, Matplotlib, Jupyter, public GeoJSON, Natural Earth data, MTBS wildfire points, and raster analysis concepts.

## Product Value

These workflows demonstrate a reusable geospatial data science pipeline: ingest data, normalize geometry/CRS, join or overlay layers, aggregate results, visualize patterns, and write a plain-language interpretation.
