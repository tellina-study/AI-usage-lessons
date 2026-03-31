"""Shared ontology loader — parses TTL files from ontology/data/ into nodes + edges.

Used by viz-ontology.py and viz-ontology-table.py.
"""

import glob
import os
import sys
import tempfile
from rdflib import Graph, Namespace, RDF, RDFS

AUL = Namespace("https://ai-usage-lessons.local/ontology#")

# Entity types we care about (instances, not the class definitions themselves)
ENTITY_TYPES = {
    str(AUL.Document): "Document",
    str(AUL.Topic): "Topic",
    str(AUL.Lecture): "Lecture",
    str(AUL.SlideDeck): "SlideDeck",
    str(AUL.Diagram): "Diagram",
    str(AUL.Requirement): "Requirement",
    str(AUL.Task): "Task",
    str(AUL.Section): "Section",
}

# Relationships to extract as edges
RELATIONS = [
    "cites", "depends_on", "covers", "supersedes",
    "belongs_to_topic", "illustrates", "tracked_by",
]


def _find_latest_ttl(base_dir="."):
    """Find the latest graph-*.ttl file in ontology/data/."""
    pattern = os.path.join(base_dir, "ontology", "data", "graph-*.ttl")
    ttl_files = sorted(glob.glob(pattern), reverse=True)
    if not ttl_files:
        return None
    return ttl_files[0]


def _parse_ttl(path):
    """Parse a TTL file with rdflib, handling common issues."""
    g = Graph()

    # First attempt: parse as-is
    try:
        g.parse(path, format="turtle")
        return g
    except Exception:
        pass

    # Fallback: clean common issues (missing trailing period, tabs)
    with open(path, encoding="utf-8") as f:
        content = f.read()

    content = content.rstrip()
    if not content.endswith("."):
        content += " ."

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".ttl", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(content)
        tmp_path = tmp.name

    try:
        g.parse(tmp_path, format="turtle")
    except Exception as e:
        print(f"ERROR: Cannot parse {path}: {e}", file=sys.stderr)
        return g
    finally:
        os.unlink(tmp_path)

    return g


def load_ontology(base_dir="."):
    """Load ontology from latest TTL file. Returns (nodes, edges, ttl_path).

    Each node is a dict with keys: id, label, type, and optional:
        url (source_url), status, updated_at, owner, source_system, title.

    Each edge is a dict with keys: source, target, relation.
    """
    ttl_path = _find_latest_ttl(base_dir)
    if not ttl_path:
        print("ERROR: No ontology TTL files found in ontology/data/", file=sys.stderr)
        return [], [], None

    g = _parse_ttl(ttl_path)
    if len(g) == 0:
        return [], [], ttl_path

    # --- Extract nodes ---
    nodes = []
    node_ids = set()

    # We need to skip class/property definitions (those typed as rdfs:Class or rdfs:Property)
    skip_types = {
        str(RDFS.Class),
        "http://www.w3.org/2000/01/rdf-schema#Class",
        "http://www.w3.org/2000/01/rdf-schema#Property",
    }

    for s, _p, o in g.triples((None, RDF.type, None)):
        o_str = str(o)
        if o_str in skip_types:
            continue
        etype = ENTITY_TYPES.get(o_str)
        if not etype:
            continue

        sid = str(s).split("#")[-1]
        if sid in node_ids:
            continue
        node_ids.add(sid)

        # Extract attributes
        label_vals = list(g.objects(s, RDFS.label))
        label = str(label_vals[0]) if label_vals else sid

        node = {"id": sid, "label": label, "type": etype}

        url_vals = list(g.objects(s, AUL.source_url))
        if url_vals:
            node["url"] = str(url_vals[0])

        status_vals = list(g.objects(s, AUL.status))
        if status_vals:
            node["status"] = str(status_vals[0])

        updated_vals = list(g.objects(s, AUL.updated_at))
        if updated_vals:
            node["updated_at"] = str(updated_vals[0]).split("T")[0]

        owner_vals = list(g.objects(s, AUL.owner))
        if owner_vals:
            node["owner"] = str(owner_vals[0])

        system_vals = list(g.objects(s, AUL.source_system))
        if system_vals:
            node["source_system"] = str(system_vals[0])

        title_vals = list(g.objects(s, AUL.title))
        if title_vals:
            node["title"] = str(title_vals[0])

        nodes.append(node)

    # --- Extract edges ---
    edges = []
    for rel_name in RELATIONS:
        rel_uri = AUL[rel_name]
        for s, _p, o in g.triples((None, rel_uri, None)):
            s_id = str(s).split("#")[-1]
            o_id = str(o).split("#")[-1]
            if s_id in node_ids and o_id in node_ids:
                edges.append({"source": s_id, "target": o_id, "relation": rel_name})

    return nodes, edges, ttl_path
