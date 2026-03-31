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

# Node data (same as graph script)
NODES = [
    # Original documents (5)
    {"id": "doc_v2", "label": "AI в разных индустриях (V2)", "type": "Document", "status": "active",
     "url": "https://docs.google.com/document/d/1k0ASel9hqLeBhtaDjS8k83Kpf640WFe8lln_MaV-OFY/edit",
     "local_path": "catalog/exports/docs/ai-v-raznyh-industriyah.md",
     "updated_at": "2026-03-06", "owner": "kzlevko@gmail.com"},
    {"id": "doc_v1", "label": "AI в цикле создания ПО (V1)", "type": "Document", "status": "archived",
     "url": "https://docs.google.com/document/d/1UliavdtqqZAyHu-JYDOGPFCbJZ44Enhju5TwmqV99Xg/edit",
     "local_path": "catalog/exports/docs/ai-v-tsikle-sozdaniya-po.md",
     "updated_at": "2026-02-23", "owner": "kzlevko@gmail.com"},
    {"id": "doc_rpd_old", "label": "РПД (original)", "type": "Document", "status": "archived",
     "url": "https://docs.google.com/document/d/18AFEqywR2utCu6a99zPuNa0MrIKYGmFd5ZWqKbu-6YE/edit",
     "local_path": "catalog/exports/docs/prog-otraslevoe-primenenie-AI.md",
     "updated_at": "2026-03-30", "owner": "kzlevko@gmail.com"},
    {"id": "doc_rpd_new", "label": "РПД (updated)", "type": "Document", "status": "active",
     "url": "https://docs.google.com/document/d/1zgAWfdyWlJBFMElmtKpmjgxySUCRccF9lNT-tj7J4fU/edit",
     "local_path": "catalog/exports/docs/prog-otraslevoe-updated-formal.md",
     "updated_at": "2026-03-31", "owner": "kzlevko@gmail.com"},
    {"id": "doc_fos", "label": "ФОС", "type": "Document", "status": "active",
     "url": "https://docs.google.com/document/d/1adJu0mKKIRgNHKRVNwVSdTI6sVdSykay/edit",
     "local_path": "catalog/exports/docs/fos_otraslevoe_primenenie_AI.docx",
     "updated_at": "2026-03-30", "owner": "kzlevko@gmail.com"},
    # New documents from Drive restructure (11)
    {"id": "doc_course_structure", "label": "Структура курса", "type": "Document", "status": "active",
     "url": "https://docs.google.com/document/d/1djdHRpBFFK_4rvH7nl3L4V5hM1glN1G04_HPem9JDes/edit",
     "local_path": "catalog/exports/docs/course-structure.md"},
    {"id": "doc_course_narrative", "label": "Нарратив курса", "type": "Document", "status": "active",
     "url": "https://docs.google.com/document/d/1ii8GbnjYGSoyadnBO_S5SKXVptq1QYz4QcDOGQ3DknI/edit",
     "local_path": "catalog/exports/docs/course-narrative.md"},
    {"id": "doc_ai_cheatsheet", "label": "AI Cheat Sheet", "type": "Document", "status": "active",
     "url": "https://docs.google.com/document/d/1RODql_LKx_MSH7C6TINpvH9HxXJoDowHhgyBHhSM5qU/edit",
     "local_path": "catalog/exports/docs/ai-cheatsheet.md"},
    {"id": "doc_prompt_library", "label": "Библиотека промптов", "type": "Document", "status": "active",
     "url": "https://docs.google.com/document/d/1o1ctSpLqtTMRyaIyjPcMRItFMMohKWQbkl9KlrEMcFY/edit",
     "local_path": "catalog/exports/docs/prompt-library.md"},
    {"id": "doc_stats_general", "label": "Статистика AI — обзор", "type": "Document", "status": "active",
     "url": "https://docs.google.com/document/d/1i5T6naIAt-K4cFPJixN5i4w7WzHgumCsTu_v3G9ufTM/edit",
     "local_path": "catalog/exports/docs/stats-overview.md"},
    {"id": "doc_stats_finance", "label": "Статистика — Финансы", "type": "Document", "status": "active",
     "url": "https://docs.google.com/document/d/1hY0mSFGrR5Gn3CR3Ah8SHQyJUL4oLeFchYlue7Sd4Nc/edit",
     "local_path": "catalog/exports/docs/stats-finance-retail.md"},
    {"id": "doc_lec01_plan", "label": "План лекции 1", "type": "Document", "status": "active",
     "url": "https://docs.google.com/document/d/1UX671dOrhfQ8OgnadD_8ce4dhVJ9wDVrFqPq6p9S9uo/edit",
     "local_path": "catalog/exports/docs/lec-01-plan.md"},
    {"id": "doc_sem01_task", "label": "Семинар 1 — задание", "type": "Document", "status": "active",
     "url": "https://docs.google.com/document/d/1KyTg-h3S8v_NOK1SL6SMN-wDvCo0lsebBKHLpwrVJWU/edit",
     "local_path": "catalog/exports/docs/sem-01-task.md"},
    {"id": "doc_sem01_guide", "label": "Семинар 1 — руководство", "type": "Document", "status": "active",
     "url": "https://docs.google.com/document/d/1n3aW30ZANDQITh0c-BuHnWfB82wUKiuqIvh1xVg9BV4/edit"},
    {"id": "doc_exam1", "label": "Промежуточный контроль 1", "type": "Document", "status": "active",
     "url": "https://docs.google.com/document/d/1AMnpH0C05cGMbIfAUqT166JhBSXFk2bztuiCDTtzOpc/edit",
     "local_path": "catalog/exports/docs/sem-05-midterm-1.md"},
    {"id": "doc_final_exam", "label": "Итоговый экзамен", "type": "Document", "status": "active",
     "url": "https://docs.google.com/document/d/1Rr6niV4SHQr1IwH14Pzn-8ziTxZlFj4gbmfWc0AT8B4/edit",
     "local_path": "catalog/exports/docs/sem-17-final-exam.md"},
    # Topics (10)
    {"id": "t_sw", "label": "AI в ПО", "type": "Topic"},
    {"id": "t_fin", "label": "AI в финансах", "type": "Topic"},
    {"id": "t_med", "label": "AI в медицине", "type": "Topic"},
    {"id": "t_mfg", "label": "AI в производстве", "type": "Topic"},
    {"id": "t_gov", "label": "AI в госуправлении", "type": "Topic"},
    {"id": "t_cre", "label": "AI в креативе", "type": "Topic"},
    {"id": "t_eth", "label": "Этика AI", "type": "Topic"},
    {"id": "t_prm", "label": "Промптинг", "type": "Topic"},
    {"id": "t_rec", "label": "Рек. системы", "type": "Topic"},
    {"id": "t_exp", "label": "Эксп. системы", "type": "Topic"},
    # Lecture (1)
    {"id": "lec_1", "label": "Лекция 1: Введение", "type": "Lecture", "status": "draft",
     "url": "https://docs.google.com/document/d/1TsPeWdhgje3pj4yXMQrA9MDFb-hD9Ljed4hao7n-Ft8/edit",
     "updated_at": "2026-03-31"},
    # Decks (2)
    {"id": "deck_1", "label": "Слайды Л1", "type": "SlideDeck", "status": "draft",
     "url": "https://docs.google.com/presentation/d/1BviVqnn7vtHGg09h22UzfUTyQswTHfvSXqol_JaRTyM/edit",
     "updated_at": "2026-03-31"},
    {"id": "deck_old", "label": "ИИ и мир (old)", "type": "SlideDeck", "status": "archived",
     "local_path": "catalog/exports/slides/ii-i-mir.pptx"},
    # Diagram (1)
    {"id": "diag_roadmap", "label": "Семестровый план", "type": "Diagram", "status": "active",
     "local_path": "diagrams/lecture-flows/semester-roadmap.drawio",
     "git_url": "https://github.com/tellina-study/AI-usage-lessons/blob/main/diagrams/lecture-flows/semester-roadmap.drawio"},
]

# Edge data (same as graph script)
EDGES = [
    # Original relations
    {"source": "doc_v2", "target": "doc_v1", "relation": "supersedes"},
    {"source": "doc_rpd_new", "target": "doc_rpd_old", "relation": "supersedes"},
    {"source": "doc_v2", "target": "doc_rpd_new", "relation": "depends_on"},
    {"source": "doc_fos", "target": "doc_rpd_old", "relation": "depends_on"},
    {"source": "doc_fos", "target": "doc_rpd_old", "relation": "cites"},
    {"source": "deck_1", "target": "lec_1", "relation": "depends_on"},
    {"source": "diag_roadmap", "target": "doc_v2", "relation": "illustrates"},
    # V2 topic links
    {"source": "doc_v2", "target": "t_sw", "relation": "belongs_to_topic"},
    {"source": "doc_v2", "target": "t_fin", "relation": "belongs_to_topic"},
    {"source": "doc_v2", "target": "t_med", "relation": "belongs_to_topic"},
    {"source": "doc_v2", "target": "t_mfg", "relation": "belongs_to_topic"},
    {"source": "doc_v2", "target": "t_gov", "relation": "belongs_to_topic"},
    {"source": "doc_v2", "target": "t_cre", "relation": "belongs_to_topic"},
    {"source": "doc_v2", "target": "t_eth", "relation": "belongs_to_topic"},
    {"source": "doc_v2", "target": "t_prm", "relation": "belongs_to_topic"},
    # Old program topics
    {"source": "doc_rpd_old", "target": "t_rec", "relation": "belongs_to_topic"},
    {"source": "doc_rpd_old", "target": "t_exp", "relation": "belongs_to_topic"},
    {"source": "doc_fos", "target": "t_rec", "relation": "belongs_to_topic"},
    {"source": "doc_fos", "target": "t_exp", "relation": "belongs_to_topic"},
    # Lecture covers
    {"source": "lec_1", "target": "t_sw", "relation": "covers"},
    {"source": "lec_1", "target": "t_eth", "relation": "covers"},
    {"source": "lec_1", "target": "t_prm", "relation": "covers"},
    # New: course_structure topic links
    {"source": "doc_course_structure", "target": "t_sw", "relation": "belongs_to_topic"},
    {"source": "doc_course_structure", "target": "t_fin", "relation": "belongs_to_topic"},
    {"source": "doc_course_structure", "target": "t_med", "relation": "belongs_to_topic"},
    {"source": "doc_course_structure", "target": "t_mfg", "relation": "belongs_to_topic"},
    {"source": "doc_course_structure", "target": "t_gov", "relation": "belongs_to_topic"},
    {"source": "doc_course_structure", "target": "t_cre", "relation": "belongs_to_topic"},
    {"source": "doc_course_structure", "target": "t_eth", "relation": "belongs_to_topic"},
    {"source": "doc_course_structure", "target": "t_prm", "relation": "belongs_to_topic"},
    # New: cheatsheet & prompt library topic links
    {"source": "doc_ai_cheatsheet", "target": "t_prm", "relation": "belongs_to_topic"},
    {"source": "doc_prompt_library", "target": "t_prm", "relation": "belongs_to_topic"},
    # New: stats topic links
    {"source": "doc_stats_finance", "target": "t_fin", "relation": "belongs_to_topic"},
    {"source": "doc_stats_general", "target": "t_sw", "relation": "belongs_to_topic"},
    {"source": "doc_stats_general", "target": "t_fin", "relation": "belongs_to_topic"},
    {"source": "doc_stats_general", "target": "t_med", "relation": "belongs_to_topic"},
    {"source": "doc_stats_general", "target": "t_mfg", "relation": "belongs_to_topic"},
    {"source": "doc_stats_general", "target": "t_gov", "relation": "belongs_to_topic"},
    # New: depends_on relations
    {"source": "doc_lec01_plan", "target": "lec_1", "relation": "depends_on"},
    {"source": "doc_sem01_task", "target": "lec_1", "relation": "depends_on"},
    {"source": "doc_sem01_guide", "target": "doc_sem01_task", "relation": "depends_on"},
    {"source": "doc_exam1", "target": "lec_1", "relation": "depends_on"},
    {"source": "doc_course_structure", "target": "doc_v2", "relation": "depends_on"},
    {"source": "doc_course_narrative", "target": "doc_v2", "relation": "depends_on"},
]


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
