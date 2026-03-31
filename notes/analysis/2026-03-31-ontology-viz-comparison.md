# Ontology Visualization Tool Comparison — 2026-03-31

## Tools Tested

### 1. pyvis (Python + D3.js) — SELECTED as primary
- **Install:** `pip install pyvis` (requires networkx, jinja2)
- **How it works:** Python script reads ontology data, builds network graph, outputs standalone HTML
- **Test result:** Successfully generated interactive graph with 19 nodes, 22 edges
- **Output:** `catalog/exports/viz/ontology-graph.html` (12KB self-contained)
- **Features:**
  - Conditional formatting (color by type, size by importance, shape by category)
  - Interactive (drag, zoom, hover for metadata)
  - Self-contained HTML (works offline, can be hosted on GitHub Pages)
  - Legend support (custom HTML overlay)
  - Physics simulation (force-directed, Barnes-Hut)
  - No server required
  - No saved views (requires regeneration with different filters)
  - Requires Python script to generate (not one-click)
- **Verdict:** Best balance of features, flexibility, and simplicity. Can be automated via a skill.

### 2. OntoSpy (Python CLI) — BROKEN
- **Install:** `pip install ontospy`
- **Test result:** FAILS on Python 3.12 — `SafeConfigParser` removed in 3.12
- **Error:** `ImportError: cannot import name 'SafeConfigParser' from 'configparser'`
- **Verdict:** Dead on current Python. Not usable.

### 3. WebVOWL (hosted web)
- **URL:** https://service.tib.eu/webvowl/
- **How it works:** Upload OWL/TTL file, get VOWL visualization
- **Test result:** Page loads, accepts file upload via drag-and-drop
- **Features:**
  - No install required
  - Standard VOWL notation (well-known in semantic web community)
  - Export to TTL
  - Requires OWL2VOWL conversion (our TTL may need preprocessing)
  - External dependency (hosted service may go down)
  - No conditional formatting beyond VOWL defaults
  - No automation possible (manual upload each time)
- **Verdict:** Good for one-off schema visualization. Not suitable for daily use with instance data.

### 4. isSemantic RDF Visualizer (web)
- **URL:** https://issemantic.net/rdf-visualizer
- **Test:** Not tested (paste-based, no automation)
- **Verdict:** Too manual for regular use. Good for quick ad-hoc checks.

### 5. VisGraph3 (web)
- **URL:** https://visgraph3.github.io/
- **Test:** Not tested
- **Verdict:** Similar to isSemantic — browser-based, manual paste.

### 6. OWLGrEd Online (web)
- **URL:** https://owlgred.lumii.lv/online_visualization
- **Test:** Not tested
- **Verdict:** More of an ontology editor than visualizer. Overkill for our needs.

### 7. open-ontologies MCP
- **Test:** Checked all 43 tools — no visualization output (SVG/HTML/image)
- **onto_stats:** Returns counts only
- **onto_query:** Returns JSON/table data that can be fed to pyvis
- **Verdict:** Not a visualizer, but good data source for pyvis script

### 8. draw.io (fallback)
- **How:** SPARQL query -> build Mermaid/XML -> mcp__drawio__open_drawio_xml -> save .drawio
- **Pros:** Already integrated, editable diagrams, version-controlled
- **Cons:** Manual layout, doesn't auto-update from ontology, not interactive
- **Verdict:** Good for presentation-quality static diagrams. Not for exploration.

## Decision

| Context | Tool | Format |
|---------|------|--------|
| **Local exploration** | pyvis (Python script) | Interactive HTML |
| **Web/git sharing** | pyvis output (static HTML) | Host on GitHub Pages or commit HTML |
| **Presentation export** | draw.io (via diagram-refresh skill) | .drawio -> PNG/SVG |
| **Schema visualization** | WebVOWL (one-off) | Upload to hosted service |

### Implementation Plan
1. Create `scripts/viz-ontology.py` — reads graph TTL, generates pyvis HTML to `catalog/exports/viz/`
2. Add to diagram-refresh skill as an optional step
3. For web sharing: the HTML file is self-contained, can be served from anywhere

## What pyvis gives us that others don't
- **Conditional formatting:** nodes colored by type, sized by importance — built into the script
- **Attribute display:** hover shows metadata (type, label, URI)
- **Automation:** Python script can be run from CLI or via skill
- **Self-contained output:** single HTML file, no server needed
- **Customizable:** change colors, physics, layout by editing the script
