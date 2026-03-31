#!/usr/bin/env python3
"""Generate interactive ontology visualization with attribute panel and neighbor highlighting.

Usage:
    python3 scripts/viz-ontology.py [output_path]

Default output: catalog/exports/viz/ontology-graph.html

Requires: pip install pyvis
"""

import sys
import os
import json
from pyvis.network import Network

OUTPUT = sys.argv[1] if len(sys.argv) > 1 else "catalog/exports/viz/ontology-graph.html"

# Color map by entity type
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

TYPE_SHAPES = {
    "Document": "dot",
    "Topic": "diamond",
    "Lecture": "box",
    "SlideDeck": "triangle",
    "Diagram": "star",
    "Requirement": "square",
    "Task": "triangleDown",
}

RELATION_COLORS = {
    "supersedes": "#E74C3C",
    "depends_on": "#3498DB",
    "cites": "#2ECC71",
    "covers": "#F39C12",
    "belongs_to_topic": "#9B59B6",
    "illustrates": "#1ABC9C",
    "tracked_by": "#95A5A6",
}

# Node data with links and attributes
NODES = [
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
    {"id": "lec_1", "label": "Лекция 1: Введение", "type": "Lecture", "status": "draft",
     "url": "https://docs.google.com/document/d/1TsPeWdhgje3pj4yXMQrA9MDFb-hD9Ljed4hao7n-Ft8/edit",
     "updated_at": "2026-03-31"},
    {"id": "deck_1", "label": "Слайды Л1", "type": "SlideDeck", "status": "draft",
     "url": "https://docs.google.com/presentation/d/1BviVqnn7vtHGg09h22UzfUTyQswTHfvSXqol_JaRTyM/edit",
     "updated_at": "2026-03-31"},
    {"id": "deck_old", "label": "ИИ и мир (old)", "type": "SlideDeck", "status": "archived",
     "local_path": "catalog/exports/slides/ii-i-mir.pptx"},
    {"id": "diag_roadmap", "label": "Семестровый план", "type": "Diagram", "status": "active",
     "local_path": "diagrams/lecture-flows/semester-roadmap.drawio",
     "git_url": "https://github.com/tellina-study/AI-usage-lessons/blob/main/diagrams/lecture-flows/semester-roadmap.drawio"},
]

EDGES = [
    {"source": "doc_v2", "target": "doc_v1", "relation": "supersedes"},
    {"source": "doc_rpd_new", "target": "doc_rpd_old", "relation": "supersedes"},
    {"source": "doc_v2", "target": "doc_rpd_new", "relation": "depends_on"},
    {"source": "doc_fos", "target": "doc_rpd_old", "relation": "depends_on"},
    {"source": "doc_fos", "target": "doc_rpd_old", "relation": "cites"},
    {"source": "deck_1", "target": "lec_1", "relation": "depends_on"},
    {"source": "diag_roadmap", "target": "doc_v2", "relation": "illustrates"},
    {"source": "doc_v2", "target": "t_sw", "relation": "belongs_to_topic"},
    {"source": "doc_v2", "target": "t_fin", "relation": "belongs_to_topic"},
    {"source": "doc_v2", "target": "t_med", "relation": "belongs_to_topic"},
    {"source": "doc_v2", "target": "t_mfg", "relation": "belongs_to_topic"},
    {"source": "doc_v2", "target": "t_gov", "relation": "belongs_to_topic"},
    {"source": "doc_v2", "target": "t_cre", "relation": "belongs_to_topic"},
    {"source": "doc_v2", "target": "t_eth", "relation": "belongs_to_topic"},
    {"source": "doc_v2", "target": "t_prm", "relation": "belongs_to_topic"},
    {"source": "doc_rpd_old", "target": "t_rec", "relation": "belongs_to_topic"},
    {"source": "doc_rpd_old", "target": "t_exp", "relation": "belongs_to_topic"},
    {"source": "doc_fos", "target": "t_rec", "relation": "belongs_to_topic"},
    {"source": "doc_fos", "target": "t_exp", "relation": "belongs_to_topic"},
    {"source": "lec_1", "target": "t_sw", "relation": "covers"},
    {"source": "lec_1", "target": "t_eth", "relation": "covers"},
    {"source": "lec_1", "target": "t_prm", "relation": "covers"},
]

# Build node lookup for JS
NODE_DATA = {}
for n in NODES:
    NODE_DATA[n["id"]] = {k: v for k, v in n.items() if k != "id"}


def build_graph(nodes, edges):
    net = Network(height="100vh", width="100%", directed=True, bgcolor="#fafafa", font_color="#333")
    net.barnes_hut(gravity=-4000, spring_length=180, damping=0.5)

    for node in nodes:
        color = TYPE_COLORS.get(node["type"], "#cccccc")
        shape = TYPE_SHAPES.get(node["type"], "dot")
        size = 30 if node["type"] == "Document" else 25 if node["type"] == "Lecture" else 20
        border_color = "#666" if node.get("status") == "archived" else color
        net.add_node(
            node["id"], label=node["label"], color={"background": color, "border": border_color,
            "highlight": {"background": "#FFD700", "border": "#FF8C00"}},
            shape=shape, size=size, borderWidth=2,
            font={"size": 12, "color": "#333", "strokeWidth": 2, "strokeColor": "#fff"},
        )

    for edge in edges:
        color = RELATION_COLORS.get(edge["relation"], "#999")
        net.add_edge(
            edge["source"], edge["target"],
            label=edge["relation"], color={"color": color, "highlight": "#FF8C00", "opacity": 0.8},
            arrows="to", width=2, font={"size": 9, "color": color, "strokeWidth": 0},
            smooth={"type": "curvedCW", "roundness": 0.15},
        )

    return net


def build_html(net):
    """Generate the HTML with custom attribute panel and neighbor highlighting."""
    net.set_options(json.dumps({
        "physics": {
            "barnesHut": {"gravitationalConstant": -4000, "springLength": 180, "damping": 0.5}
        },
        "interaction": {
            "hover": True, "tooltipDelay": 100, "hideEdgesOnDrag": True,
            "multiselect": True, "navigationButtons": True
        },
        "edges": {"smooth": {"type": "curvedCW", "roundness": 0.15}},
    }))

    net.save_graph(OUTPUT)

    with open(OUTPUT, "r") as f:
        html = f.read()

    # Inject custom CSS + JS for attribute panel and neighbor highlighting
    custom_css = """
<style>
  html, body { margin: 0; padding: 0; height: 100%; overflow: hidden; font-family: 'Segoe UI', sans-serif; }
  #mynetwork { position: absolute; left: 0; top: 0; right: 300px; bottom: 0; min-height: 600px; border-right: 1px solid #ddd; }
  #panel { position: absolute; right: 0; top: 0; width: 300px; bottom: 0; overflow-y: auto; background: #fff; padding: 16px; box-sizing: border-box; }
  #panel h3 { margin: 0 0 8px 0; color: #333; font-size: 16px; }
  #panel .type-badge { display: inline-block; padding: 2px 8px; border-radius: 4px; color: #fff; font-size: 11px; font-weight: bold; margin-bottom: 8px; }
  #panel .attr { margin: 6px 0; font-size: 13px; }
  #panel .attr-label { color: #888; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; }
  #panel .attr-value { color: #333; word-break: break-all; }
  #panel a { color: #4A90D9; text-decoration: none; }
  #panel a:hover { text-decoration: underline; }
  #panel .relations { margin-top: 12px; border-top: 1px solid #eee; padding-top: 8px; }
  #panel .rel { margin: 4px 0; font-size: 12px; }
  #panel .rel-arrow { color: #999; }
  #panel .empty { color: #999; font-style: italic; padding: 40px 0; text-align: center; }
  #legend { padding: 12px 0; border-bottom: 1px solid #eee; margin-bottom: 12px; font-size: 12px; }
  #legend b { font-size: 13px; }
  .leg-item { margin: 2px 0; }
  .leg-dot { display: inline-block; width: 10px; height: 10px; border-radius: 50%; margin-right: 4px; vertical-align: middle; }
  .leg-line { display: inline-block; width: 20px; height: 2px; margin-right: 4px; vertical-align: middle; }
  #type-toolbar { position: fixed; top: 0; left: 0; right: 300px; height: 40px; background: #fff; border-bottom: 1px solid #ddd; display: flex; align-items: center; gap: 8px; padding: 0 16px; z-index: 10; box-sizing: border-box; }
  #mynetwork { top: 40px !important; }
  .type-btn { border: none; padding: 5px 14px; border-radius: 20px; font-size: 12px; font-weight: 600; cursor: pointer; color: #fff; opacity: 0.7; transition: opacity 0.15s, box-shadow 0.15s; }
  .type-btn:hover { opacity: 0.9; }
  .type-btn.active { opacity: 1; box-shadow: 0 0 0 2px rgba(0,0,0,0.25); }
</style>
"""

    filter_types = ["Document", "Topic", "Lecture", "SlideDeck", "Diagram"]
    toolbar_buttons = '<button class="type-btn active" data-type="All" style="background:#666" onclick="filterByType(\'All\', this)">All</button>'
    for t in filter_types:
        c = TYPE_COLORS.get(t, "#999")
        toolbar_buttons += f'<button class="type-btn" data-type="{t}" style="background:{c}" onclick="filterByType(\'{t}\', this)">{t}</button>'

    custom_panel = """
<div id="type-toolbar">""" + toolbar_buttons + """</div>
<div id="panel">
  <div id="legend">
    <b>Ontology Graph</b><br>
    <div style="margin-top:6px"><b>Entities</b></div>
    <div class="leg-item"><span class="leg-dot" style="background:#4A90D9"></span>Document</div>
    <div class="leg-item"><span class="leg-dot" style="background:#F5A623"></span>Topic</div>
    <div class="leg-item"><span class="leg-dot" style="background:#7ED321"></span>Lecture</div>
    <div class="leg-item"><span class="leg-dot" style="background:#9B59B6"></span>SlideDeck</div>
    <div class="leg-item"><span class="leg-dot" style="background:#1ABC9C"></span>Diagram</div>
    <div style="margin-top:6px"><b>Relations</b></div>
    <div class="leg-item"><span class="leg-line" style="background:#E74C3C"></span>supersedes</div>
    <div class="leg-item"><span class="leg-line" style="background:#3498DB"></span>depends_on</div>
    <div class="leg-item"><span class="leg-line" style="background:#2ECC71"></span>cites</div>
    <div class="leg-item"><span class="leg-line" style="background:#9B59B6"></span>belongs_to_topic</div>
    <div class="leg-item"><span class="leg-line" style="background:#F39C12"></span>covers</div>
    <div class="leg-item"><span class="leg-line" style="background:#1ABC9C"></span>illustrates</div>
  </div>
  <div id="details">
    <div class="empty">Click a node to see details</div>
  </div>
</div>
"""

    node_data_json = json.dumps(NODE_DATA, ensure_ascii=False)
    edges_json = json.dumps(EDGES, ensure_ascii=False)

    custom_js = """
<script>
const NODE_DATA = """ + node_data_json + """;
const EDGES = """ + edges_json + """;
const TYPE_COLORS = """ + json.dumps(TYPE_COLORS) + """;

const REPO = "https://github.com/tellina-study/AI-usage-lessons/blob/main/";

// Wait for vis network to initialize
setTimeout(function() {
  var network = Object.values(document.getElementById('mynetwork'))[0]
    || window.network;

  // Try to find the network instance
  var frames = document.querySelectorAll('iframe');
  if (!network) {
    // pyvis stores network on the window of the iframe or directly
    network = window.network;
  }

  if (!network) return;

  var allNodes = null;
  var allEdges = null;

  try {
    allNodes = network.body.data.nodes;
    allEdges = network.body.data.edges;
  } catch(e) {}

  // Click handler — show attributes panel
  network.on("click", function(params) {
    var panel = document.getElementById("details");
    if (params.nodes.length === 0) {
      panel.innerHTML = '<div class="empty">Click a node to see details</div>';
      resetHighlight();
      return;
    }

    var nodeId = params.nodes[0];
    var data = NODE_DATA[nodeId];
    if (!data) {
      panel.innerHTML = '<div class="empty">No data for ' + nodeId + '</div>';
      return;
    }

    var color = TYPE_COLORS[data.type] || "#ccc";
    var html = '<h3>' + data.label + '</h3>';
    html += '<span class="type-badge" style="background:' + color + '">' + data.type + '</span>';

    // Attributes
    if (data.status) html += '<div class="attr"><div class="attr-label">Status</div><div class="attr-value">' + data.status + '</div></div>';
    if (data.updated_at) html += '<div class="attr"><div class="attr-label">Updated</div><div class="attr-value">' + data.updated_at + '</div></div>';
    if (data.owner) html += '<div class="attr"><div class="attr-label">Owner</div><div class="attr-value">' + data.owner + '</div></div>';

    // Links
    html += '<div class="attr" style="margin-top:12px"><div class="attr-label">Links</div></div>';
    if (data.url) html += '<div class="attr"><a href="' + data.url + '" target="_blank">📄 Open in Google Drive</a></div>';
    if (data.local_path) html += '<div class="attr"><a href="' + REPO + data.local_path + '" target="_blank">📁 View in GitHub</a></div>';
    if (data.git_url) html += '<div class="attr"><a href="' + data.git_url + '" target="_blank">📁 View in GitHub</a></div>';

    // Relations
    html += '<div class="relations"><div class="attr-label">Relations</div>';
    var outgoing = EDGES.filter(e => e.source === nodeId);
    var incoming = EDGES.filter(e => e.target === nodeId);

    outgoing.forEach(function(e) {
      var targetData = NODE_DATA[e.target] || {label: e.target};
      html += '<div class="rel"><span class="rel-arrow">→</span> <b>' + e.relation + '</b> ' + targetData.label + '</div>';
    });
    incoming.forEach(function(e) {
      var sourceData = NODE_DATA[e.source] || {label: e.source};
      html += '<div class="rel"><span class="rel-arrow">←</span> <b>' + e.relation + '</b> ' + sourceData.label + '</div>';
    });
    if (outgoing.length === 0 && incoming.length === 0) html += '<div class="rel" style="color:#999">No relations</div>';
    html += '</div>';

    panel.innerHTML = html;

    // Highlight connected nodes
    highlightNeighbors(nodeId);
  });

  function highlightNeighbors(nodeId) {
    if (!allNodes || !allEdges) return;

    var connectedNodes = new Set([nodeId]);
    var connectedEdges = new Set();

    allEdges.forEach(function(edge) {
      var edgeData = allEdges.get(edge.id);
      if (edgeData.from === nodeId || edgeData.to === nodeId) {
        connectedNodes.add(edgeData.from);
        connectedNodes.add(edgeData.to);
        connectedEdges.add(edge.id);
      }
    });

    // Dim non-connected nodes
    var updates = [];
    allNodes.forEach(function(node) {
      if (connectedNodes.has(node.id)) {
        updates.push({id: node.id, opacity: 1.0, font: {color: "#333"}});
      } else {
        updates.push({id: node.id, opacity: 0.15, font: {color: "#ccc"}});
      }
    });
    allNodes.update(updates);

    // Dim non-connected edges
    var edgeUpdates = [];
    allEdges.forEach(function(edge) {
      if (connectedEdges.has(edge.id)) {
        edgeUpdates.push({id: edge.id, hidden: false, width: 3});
      } else {
        edgeUpdates.push({id: edge.id, hidden: true});
      }
    });
    allEdges.update(edgeUpdates);
  }

  function resetHighlight() {
    if (!allNodes || !allEdges) return;
    var updates = [];
    allNodes.forEach(function(node) {
      updates.push({id: node.id, hidden: false, opacity: 1.0, font: {color: "#333"}});
    });
    allNodes.update(updates);

    var edgeUpdates = [];
    allEdges.forEach(function(edge) {
      edgeUpdates.push({id: edge.id, hidden: false, width: 2});
    });
    allEdges.update(edgeUpdates);
  }

  // Type filter logic — exposed globally so onclick can call it
  window.filterByType = function(type, btnEl) {
    // Update active button
    document.querySelectorAll('.type-btn').forEach(function(b) { b.classList.remove('active'); });
    if (btnEl) btnEl.classList.add('active');

    if (!allNodes || !allEdges) return;

    if (type === 'All') {
      resetHighlight();
      return;
    }

    // Find nodes of selected type
    var selectedIds = new Set();
    allNodes.forEach(function(node) {
      if (NODE_DATA[node.id] && NODE_DATA[node.id].type === type) {
        selectedIds.add(node.id);
      }
    });

    // Find directly connected nodes (one hop)
    var visibleIds = new Set(selectedIds);
    allEdges.forEach(function(edge) {
      var edgeData = allEdges.get(edge.id);
      if (selectedIds.has(edgeData.from)) visibleIds.add(edgeData.to);
      if (selectedIds.has(edgeData.to)) visibleIds.add(edgeData.from);
    });

    // Show/hide nodes
    var nodeUpdates = [];
    allNodes.forEach(function(node) {
      if (visibleIds.has(node.id)) {
        nodeUpdates.push({id: node.id, hidden: false, opacity: 1.0, font: {color: "#333"}});
      } else {
        nodeUpdates.push({id: node.id, hidden: true});
      }
    });
    allNodes.update(nodeUpdates);

    // Show edges only between visible nodes
    var edgeUpdates = [];
    allEdges.forEach(function(edge) {
      var edgeData = allEdges.get(edge.id);
      if (visibleIds.has(edgeData.from) && visibleIds.has(edgeData.to)) {
        edgeUpdates.push({id: edge.id, hidden: false, width: 2});
      } else {
        edgeUpdates.push({id: edge.id, hidden: true});
      }
    });
    allEdges.update(edgeUpdates);
  };

}, 1000);
</script>
"""

    # Inject into HTML
    html = html.replace("<head>", "<head>" + custom_css)
    html = html.replace("</body>", custom_panel + custom_js + "</body>")

    # Fix pyvis container to fill the viewport properly
    html = html.replace('style="width: 100%; height: 100vh;"', 'style="width: 100%; height: 100vh;"')
    # Ensure the canvas div also fills height
    html = html.replace('#mynetwork {', '#mynetwork { min-height: 600px; ')

    return html


if __name__ == "__main__":
    os.makedirs(os.path.dirname(OUTPUT) or ".", exist_ok=True)
    net = build_graph(NODES, EDGES)
    html = build_html(net)

    with open(OUTPUT, "w") as f:
        f.write(html)

    print(f"Ontology visualization saved to: {OUTPUT}")
    print(f"Nodes: {len(NODES)}, Edges: {len(EDGES)}")
    print(f"Open in browser: file://{os.path.abspath(OUTPUT)}")
