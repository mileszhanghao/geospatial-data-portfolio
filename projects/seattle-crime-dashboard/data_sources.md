# Public Data Sources

This workflow is designed around public civic data rather than private course files.

| Layer | Source | Use |
| --- | --- | --- |
| Seattle public safety incidents | `https://data.seattle.gov/resource/tazs-3rd5.json` | Point events for incident category, date, and location analysis |
| Seattle neighborhoods | `https://services.arcgis.com/ZOyb2t4B0UYuYNYH/arcgis/rest/services/nma_nhoods_sub/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson` | Polygon layer for point-in-polygon summaries |
| Seattle police beats | `https://services.arcgis.com/ZOyb2t4B0UYuYNYH/arcgis/rest/services/Current_Beats/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson` | Optional operational boundary overlay |

The script keeps endpoints configurable so the same pattern can be reused for other Socrata or ArcGIS FeatureServer datasets.
