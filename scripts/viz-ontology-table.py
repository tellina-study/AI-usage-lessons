#!/usr/bin/env python3
"""Generate table view of ontology entities.

Usage:
    python3 scripts/viz-ontology-table.py [output_path]

Default output: catalog/exports/viz/ontology-table.html

No external dependencies — uses only Python standard library.
"""

import sys
import os
import json

# Add scripts dir to path so we can import ontology_loader
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ontology_loader import load_ontology

OUTPUT = sys.argv[1] if len(sys.argv) > 1 else "catalog/exports/viz/ontology-table.html"

# Color map by entity type (same as graph script)
TYPE_COLORS = {
    "Document": "#4A90D9",
    "Topic": "#F5A623",
    "Lecture": "#7ED321",
    "SlideDeck": "#9B59B6",
    "Diagram": "#1ABC9C",
    "Requirement": "#E74C3C",
    "Task": "#95A5A6",
    "Section": "#F39C12",
}

STATUS_COLORS = {
    "active": "#27ae60",
    "archived": "#95a5a6",
    "draft": "#f1c40f",
}

REPO_BASE = "https://github.com/tellina-study/AI-usage-lessons/blob/main/"

# Load nodes and edges dynamically from ontology TTL
NODES, EDGES, _ttl_path = load_ontology(base_dir=".")

if not NODES:
    print("ERROR: No nodes loaded from ontology. Check ontology/data/ for graph-*.ttl files.")
    sys.exit(1)


def build_node_lookup():
    """Build a dict from node id to node data."""
    return {n["id"]: n for n in NODES}


def get_connections(node_id, lookup):
    """Get all connections for a node as a list of (direction, relation, target_id, target_label)."""
    connections = []
    for e in EDGES:
        if e["source"] == node_id:
            target = lookup.get(e["target"], {})
            connections.append(("out", e["relation"], e["target"], target.get("label", e["target"])))
        if e["target"] == node_id:
            source = lookup.get(e["source"], {})
            connections.append(("in", e["relation"], e["source"], source.get("label", e["source"])))
    return connections


def esc(text):
    """Escape HTML entities."""
    return (text
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#39;"))


def build_links_html(node):
    """Build the Links cell content."""
    parts = []
    if node.get("url"):
        parts.append(f'<a href="{esc(node["url"])}" target="_blank" class="link-badge link-drive">Drive</a>')
    if node.get("git_url"):
        parts.append(f'<a href="{esc(node["git_url"])}" target="_blank" class="link-badge link-github">GitHub</a>')
    elif node.get("local_path"):
        gh_url = REPO_BASE + node["local_path"]
        parts.append(f'<a href="{esc(gh_url)}" target="_blank" class="link-badge link-github">GitHub</a>')
    return " ".join(parts) if parts else '<span class="no-links">--</span>'


def build_connections_html(node_id, lookup):
    """Build the Connected Objects cell content."""
    conns = get_connections(node_id, lookup)
    if not conns:
        return '<span class="no-links">--</span>'
    parts = []
    for direction, relation, target_id, target_label in conns:
        arrow = "&rarr;" if direction == "out" else "&larr;"
        parts.append(
            f'<span class="conn-item">'
            f'{arrow} <b>{esc(relation)}</b>: '
            f'<a href="#{esc(target_id)}" class="conn-link" data-target="{esc(target_id)}">'
            f'{esc(target_label)}</a>'
            f'</span>'
        )
    return "<br>".join(parts)


def generate_table_rows(lookup):
    """Generate HTML table rows for all nodes."""
    rows = []
    for node in NODES:
        nid = node["id"]
        ntype = node.get("type", "")
        color = TYPE_COLORS.get(ntype, "#ccc")
        status = node.get("status", "")
        status_color = STATUS_COLORS.get(status, "#ccc")

        row = (
            f'<tr id="{esc(nid)}" class="onto-row" '
            f'data-type="{esc(ntype)}" '
            f'data-name="{esc(node["label"])}" '
            f'data-status="{esc(status)}" '
            f'data-id="{esc(nid)}">'
            f'<td><span class="type-badge" style="background:{color}">{esc(ntype)}</span></td>'
            f'<td class="name-cell">{esc(node["label"])}</td>'
            f'<td>'
            + (f'<span class="status-badge" style="background:{status_color}">{esc(status)}</span>'
               if status else '<span class="no-links">--</span>')
            + f'</td>'
            f'<td>{build_links_html(node)}</td>'
            f'<td class="conn-cell">{build_connections_html(nid, lookup)}</td>'
            f'</tr>'
        )
        rows.append(row)
    return "\n".join(rows)


def get_unique_types():
    """Get sorted unique types from NODES."""
    types = sorted(set(n["type"] for n in NODES))
    return types


def generate_filter_buttons(types):
    """Generate type filter buttons HTML."""
    buttons = ['<button class="filter-btn active" data-filter="All">All</button>']
    for t in types:
        color = TYPE_COLORS.get(t, "#ccc")
        buttons.append(
            f'<button class="filter-btn" data-filter="{esc(t)}" '
            f'style="--btn-color:{color}">{esc(t)}</button>'
        )
    return "\n".join(buttons)


def generate_html():
    lookup = build_node_lookup()
    types = get_unique_types()

    # Build connection map for JS (node_id -> list of connected node_ids)
    conn_map = {}
    for node in NODES:
        nid = node["id"]
        connected = set()
        for e in EDGES:
            if e["source"] == nid:
                connected.add(e["target"])
            if e["target"] == nid:
                connected.add(e["source"])
        conn_map[nid] = list(connected)

    conn_map_json = json.dumps(conn_map, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ontology Table</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
  font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
  background: #f5f6fa;
  color: #333;
  padding: 20px;
  min-height: 100vh;
}}
h1 {{
  font-size: 22px;
  margin-bottom: 16px;
  color: #2c3e50;
}}
.toolbar {{
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  align-items: center;
  margin-bottom: 12px;
}}
.filter-btn {{
  padding: 5px 14px;
  border: 2px solid #ddd;
  border-radius: 20px;
  background: #fff;
  cursor: pointer;
  font-size: 13px;
  font-weight: 500;
  color: #555;
  transition: all 0.15s;
}}
.filter-btn:hover {{
  border-color: #aaa;
  background: #f0f0f0;
}}
.filter-btn.active {{
  border-color: var(--btn-color, #4A90D9);
  background: var(--btn-color, #4A90D9);
  color: #fff;
}}
.search-box {{
  margin-bottom: 12px;
}}
.search-box input {{
  width: 100%;
  max-width: 400px;
  padding: 8px 14px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
  outline: none;
  transition: border-color 0.15s;
}}
.search-box input:focus {{
  border-color: #4A90D9;
  box-shadow: 0 0 0 2px rgba(74,144,217,0.15);
}}
.table-wrap {{
  overflow-x: auto;
  border-radius: 8px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.08);
}}
table {{
  width: 100%;
  border-collapse: collapse;
  background: #fff;
  font-size: 14px;
}}
thead th {{
  background: #2c3e50;
  color: #fff;
  padding: 10px 14px;
  text-align: left;
  font-weight: 600;
  font-size: 13px;
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
  position: sticky;
  top: 0;
  z-index: 2;
}}
thead th:hover {{
  background: #34495e;
}}
thead th .sort-arrow {{
  margin-left: 4px;
  font-size: 10px;
  opacity: 0.5;
}}
thead th.sorted .sort-arrow {{
  opacity: 1;
}}
tbody tr {{
  transition: background 0.1s;
}}
tbody tr:nth-child(even) {{
  background: #fafbfc;
}}
tbody tr:hover {{
  background: #eef3f9;
}}
tbody tr.highlighted {{
  background: #fff9e6 !important;
}}
tbody tr.connected-highlight {{
  background: #f0f7ff !important;
}}
tbody tr.hidden-row {{
  display: none;
}}
td {{
  padding: 8px 14px;
  border-bottom: 1px solid #eee;
  vertical-align: top;
}}
.type-badge {{
  display: inline-block;
  padding: 2px 10px;
  border-radius: 12px;
  color: #fff;
  font-size: 12px;
  font-weight: 600;
  white-space: nowrap;
}}
.status-badge {{
  display: inline-block;
  padding: 2px 10px;
  border-radius: 12px;
  color: #fff;
  font-size: 12px;
  font-weight: 600;
  white-space: nowrap;
}}
.name-cell {{
  font-weight: 500;
  min-width: 180px;
}}
.link-badge {{
  display: inline-block;
  padding: 2px 10px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
  text-decoration: none;
  margin-right: 4px;
}}
.link-drive {{
  background: #e8f0fe;
  color: #1a73e8;
}}
.link-drive:hover {{
  background: #d2e3fc;
}}
.link-github {{
  background: #f0f0f0;
  color: #333;
}}
.link-github:hover {{
  background: #e0e0e0;
}}
.no-links {{
  color: #ccc;
  font-size: 13px;
}}
.conn-cell {{
  font-size: 13px;
  line-height: 1.6;
  min-width: 250px;
}}
.conn-item b {{
  color: #666;
  font-weight: 500;
}}
.conn-link {{
  color: #4A90D9;
  text-decoration: none;
  cursor: pointer;
}}
.conn-link:hover {{
  text-decoration: underline;
}}
.count-info {{
  margin-bottom: 8px;
  font-size: 13px;
  color: #888;
}}
@media (max-width: 768px) {{
  body {{ padding: 10px; }}
  td, thead th {{ padding: 6px 8px; font-size: 13px; }}
  .name-cell {{ min-width: 120px; }}
  .conn-cell {{ min-width: 180px; }}
}}
</style>
</head>
<body>

<h1>Ontology Table</h1>

<div class="toolbar">
{generate_filter_buttons(types)}
</div>

<div class="search-box">
  <input type="text" id="search-input" placeholder="Search by name, type, status...">
</div>

<div class="count-info">Showing <span id="visible-count">{len(NODES)}</span> of {len(NODES)} entities</div>

<div class="table-wrap">
<table id="onto-table">
<thead>
<tr>
  <th data-col="type">Type <span class="sort-arrow">&#9650;&#9660;</span></th>
  <th data-col="name">Name <span class="sort-arrow">&#9650;&#9660;</span></th>
  <th data-col="status">Status <span class="sort-arrow">&#9650;&#9660;</span></th>
  <th>Links</th>
  <th>Connected Objects</th>
</tr>
</thead>
<tbody>
{generate_table_rows(lookup)}
</tbody>
</table>
</div>

<script>
(function() {{
  const CONN_MAP = {conn_map_json};

  // --- Sorting ---
  const table = document.getElementById('onto-table');
  const thead = table.querySelector('thead');
  const tbody = table.querySelector('tbody');
  let sortCol = null;
  let sortAsc = true;

  thead.querySelectorAll('th[data-col]').forEach(function(th) {{
    th.addEventListener('click', function() {{
      const col = th.getAttribute('data-col');
      if (sortCol === col) {{
        sortAsc = !sortAsc;
      }} else {{
        sortCol = col;
        sortAsc = true;
      }}

      // Update header styles
      thead.querySelectorAll('th').forEach(function(h) {{ h.classList.remove('sorted'); }});
      th.classList.add('sorted');

      const rows = Array.from(tbody.querySelectorAll('tr.onto-row'));
      rows.sort(function(a, b) {{
        let va = a.getAttribute('data-' + col) || '';
        let vb = b.getAttribute('data-' + col) || '';
        va = va.toLowerCase();
        vb = vb.toLowerCase();
        if (va < vb) return sortAsc ? -1 : 1;
        if (va > vb) return sortAsc ? 1 : -1;
        return 0;
      }});

      rows.forEach(function(row) {{ tbody.appendChild(row); }});
    }});
  }});

  // --- Filtering by type ---
  let activeFilter = 'All';
  const filterBtns = document.querySelectorAll('.filter-btn');

  filterBtns.forEach(function(btn) {{
    btn.addEventListener('click', function() {{
      filterBtns.forEach(function(b) {{ b.classList.remove('active'); }});
      btn.classList.add('active');
      activeFilter = btn.getAttribute('data-filter');
      applyFilters();
    }});
  }});

  // --- Search ---
  const searchInput = document.getElementById('search-input');
  searchInput.addEventListener('input', function() {{
    applyFilters();
  }});

  function applyFilters() {{
    const query = searchInput.value.toLowerCase().trim();
    const rows = tbody.querySelectorAll('tr.onto-row');
    let visible = 0;

    rows.forEach(function(row) {{
      const type = row.getAttribute('data-type');
      const name = row.getAttribute('data-name').toLowerCase();
      const status = row.getAttribute('data-status').toLowerCase();
      const text = name + ' ' + type.toLowerCase() + ' ' + status;

      const typeMatch = (activeFilter === 'All' || type === activeFilter);
      const searchMatch = (!query || text.indexOf(query) !== -1);

      if (typeMatch && searchMatch) {{
        row.classList.remove('hidden-row');
        visible++;
      }} else {{
        row.classList.add('hidden-row');
      }}
    }});

    document.getElementById('visible-count').textContent = visible;
  }}

  // --- Row click highlighting ---
  let selectedId = null;

  tbody.addEventListener('click', function(e) {{
    // If clicking a connection link, scroll to that row
    const connLink = e.target.closest('.conn-link');
    if (connLink) {{
      e.preventDefault();
      const targetId = connLink.getAttribute('data-target');
      highlightRow(targetId);
      const targetRow = document.getElementById(targetId);
      if (targetRow) {{
        targetRow.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
      }}
      return;
    }}

    // Otherwise highlight clicked row and its connections
    const row = e.target.closest('tr.onto-row');
    if (!row) return;
    const rowId = row.getAttribute('data-id');

    if (selectedId === rowId) {{
      clearHighlights();
      selectedId = null;
      return;
    }}

    highlightRow(rowId);
  }});

  function highlightRow(nodeId) {{
    clearHighlights();
    selectedId = nodeId;

    const row = document.getElementById(nodeId);
    if (row) row.classList.add('highlighted');

    const connected = CONN_MAP[nodeId] || [];
    connected.forEach(function(cid) {{
      const cRow = document.getElementById(cid);
      if (cRow) cRow.classList.add('connected-highlight');
    }});
  }}

  function clearHighlights() {{
    tbody.querySelectorAll('tr').forEach(function(row) {{
      row.classList.remove('highlighted', 'connected-highlight');
    }});
  }}
}})();
</script>

</body>
</html>"""

    return html


if __name__ == "__main__":
    os.makedirs(os.path.dirname(OUTPUT) or ".", exist_ok=True)
    html = generate_html()

    with open(OUTPUT, "w") as f:
        f.write(html)

    print(f"Ontology table saved to: {OUTPUT}")
    print(f"Nodes: {len(NODES)}, Edges: {len(EDGES)}")
    print(f"Open in browser: file://{os.path.abspath(OUTPUT)}")
