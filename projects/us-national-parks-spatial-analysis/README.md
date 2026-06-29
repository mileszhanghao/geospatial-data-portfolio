# US National Parks Spatial Analysis

ArcGIS Pro case study analyzing two complementary views of national park access and conservation coverage: city proximity to parks and state-level park area as a share of total land area.

## Decision Questions

- Which cities have the strongest proximity to multiple national parks within a 100 km travel-planning radius?
- Which states have the highest normalized share of land area occupied by national parks?
- How do cartographic choices change the story when one map emphasizes local access and another emphasizes statewide coverage?

## Methods

- Built 100 km buffers around city locations and counted intersecting national park features.
- Used ArcGIS Pro geoprocessing tools to summarize park area within state boundaries.
- Normalized park area by total state land area to avoid over-weighting physically large states.
- Resolved coordinate reference system and unit issues by using ArcGIS Pro shape-summary attributes instead of area values calculated in decimal degrees.
- Designed two complementary layouts: graduated symbols for city proximity counts and a choropleth for state-level park coverage.
- Used Alaska and Hawaii inset maps so national-scale context remained readable without shrinking the contiguous United States.

## Findings

- Bishop, California emerged as the city with the highest number of national parks within the 100 km proximity threshold, reflecting its location near the Sierra Nevada and parks such as Yosemite, Kings Canyon, and Sequoia.
- Alaska, Hawaii, and California ranked highly for percentage of state land area covered by national parks.
- The proximity map emphasized regional clustering around the Sierra Nevada, while the normalized choropleth shifted attention toward statewide conservation intensity.

## Technical Lessons

The main GIS issue was unit reliability. Early area calculations produced anomalous values because geometry was being interpreted in geographic coordinates rather than projected metric units. The corrected workflow used ArcGIS Pro's shape-summary attributes inside the summarization step, producing reliable square-kilometer area values and reinforcing the importance of CRS checks before quantitative spatial analysis.

## Skills Demonstrated

- ArcGIS Pro geoprocessing
- Buffer analysis and spatial intersection
- Summarize Within workflows
- CRS and measurement-unit validation
- Choropleth and graduated-symbol cartography
- Inset map layout design
- Public-facing spatial analysis writing

## Portfolio Boundary

This public case study summarizes the analysis workflow and results without publishing course scaffolding, private assignment files, or restricted data links.
