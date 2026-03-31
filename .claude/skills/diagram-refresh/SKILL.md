# diagram-refresh

Refresh diagrams based on content changes.

## Steps
1. Check which diagrams are affected (via Oxigraph `illustrates` relations)
2. Read current .drawio source from `diagrams/`
3. Update diagram content via drawio-mcp
4. Validate via draw-mcp
5. Export to PNG/SVG in `diagrams/exports/`
6. Update `catalog/manifests/diagrams.yaml`
7. Run orphan diagram check
