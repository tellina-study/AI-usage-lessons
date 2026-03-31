# Ontology Visualization

Interactive views of the AI-usage-lessons knowledge graph.

## Views

### [index.html](index.html) — Combined viewer
Tabbed interface switching between graph and table views.

### [ontology-graph.html](ontology-graph.html) — Graph View
Interactive force-directed graph (pyvis/vis.js).

**Features:**
- Color-coded nodes by type (Document, Topic, Lecture, SlideDeck, Diagram)
- Type filter toolbar — click to show only one type + its connections
- Click node → right panel shows attributes, status, Drive/GitHub links
- Neighbor highlighting — unrelated nodes fade out on selection
- Drag, zoom, physics simulation

### [ontology-table.html](ontology-table.html) — Table View
Sortable entity table with connected objects.

**Features:**
- Type/Name/Status/Links/Connected Objects columns
- Sort by clicking column headers
- Search box filters by text
- Type filter buttons (same as graph)
- Click row → highlights connected rows
- Connected object names are clickable (scrolls to that row)

## Regeneration

Views are auto-regenerated on every commit via pre-commit hook.

Manual regeneration:
```bash
python3 scripts/viz-ontology.py                    # → ontology-graph.html
python3 scripts/viz-ontology-table.py              # → ontology-table.html
```

## Data Source

Generated from hardcoded node/edge data in the Python scripts. To update after ontology changes:
1. Query ontology via `mcp__open-ontologies__onto_query`
2. Update NODES and EDGES lists in both scripts
3. Re-run scripts (or just commit — hook does it)

Future: auto-read from `ontology/data/graph-*.ttl` files.
