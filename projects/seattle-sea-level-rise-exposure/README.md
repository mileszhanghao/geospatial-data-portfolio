# Seattle Sea-Level-Rise Residential Exposure

This project models a 1 meter sea-level-rise scenario for Seattle and estimates which residential zoning areas intersect the modeled exposure zone.

## Methods

- Used a USGS SRTM DEM as the elevation surface.
- Applied an ArcGIS Pro raster threshold to classify cells at or below 1 meter elevation.
- Converted the inundation raster into polygon geometry.
- Intersected the exposure polygon with Seattle single-family and multifamily residential zoning.
- Summarized exposed residential land area and mapped low-lying shoreline patterns.

## Result

The analysis identified 288 residential zones intersecting the modeled 1 meter exposure area, totaling about 7,924,389 square feet, or roughly 0.736 square kilometers. The most exposed areas were concentrated near low-lying shoreline and waterway zones such as the Duwamish Waterway, South Park, and Georgetown.

## Artifact

- [Project report](report.pdf)
