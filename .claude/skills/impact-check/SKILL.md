# impact-check

Analyze impact of recent changes across the knowledge base using ontology queries.

## Role

You are an issue-manager agent. Your job is to query the ontology for recently updated entities, trace dependency chains to find cascading impacts, generate an impact report, and create GitHub Issues for any unresolved impacts.

## Constants

- Manifests directory: `/home/levko/AI-usage-lessons/catalog/manifests/`
- SPARQL queries directory: `/home/levko/AI-usage-lessons/ontology/queries/`
- Pre-built queries:
  - `find_docs_for_lecture.rq` — find documents related to a lecture
  - `impacted_by_requirement_change.rq` — find entities impacted by requirement changes
  - `orphan_diagrams.rq` — find unlinked diagrams
- GitHub repo: `tellina-study/AI-usage-lessons`
- Ontology prefix: `aul: <https://ai-usage-lessons.local/ontology#>`

## Execution

### Step 1: Read pre-built SPARQL queries

Read these files using the Read tool:
1. `/home/levko/AI-usage-lessons/ontology/queries/find_docs_for_lecture.rq`
2. `/home/levko/AI-usage-lessons/ontology/queries/impacted_by_requirement_change.rq`
3. `/home/levko/AI-usage-lessons/ontology/queries/orphan_diagrams.rq`

### Step 2: Find recently updated entities

Query the ontology for all entities updated in the last 7 days (or since the last impact check):
```
mcp__open-ontologies__onto_query(
  query="PREFIX aul: <https://ai-usage-lessons.local/ontology#>\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\nSELECT ?entity ?type ?updated ?status WHERE {\n    ?entity aul:updated_at ?updated ;\n            a ?type .\n    OPTIONAL { ?entity aul:status ?status }\n    FILTER (?updated >= \"<7_days_ago_ISO>\"^^xsd:dateTime)\n}\nORDER BY DESC(?updated)"
)
```

Replace `<7_days_ago_ISO>` with the actual date 7 days before today in `YYYY-MM-DDT00:00:00` format.

If no date-filtered results, fall back to listing all entities:
```
mcp__open-ontologies__onto_query(
  query="PREFIX aul: <https://ai-usage-lessons.local/ontology#>\nSELECT ?entity ?type ?updated WHERE {\n    ?entity aul:updated_at ?updated ;\n            a ?type .\n}\nORDER BY DESC(?updated)\nLIMIT 20"
)
```

### Step 3: Trace dependency chains

For each recently updated entity, find everything that depends on it:

**Forward impact (what depends on the changed entity):**
```
mcp__open-ontologies__onto_query(
  query="PREFIX aul: <https://ai-usage-lessons.local/ontology#>\nSELECT ?dependent ?depType ?relation WHERE {\n    {\n        ?dependent aul:depends_on aul:<changed_entity> .\n        BIND(\"depends_on\" AS ?relation)\n    } UNION {\n        ?dependent aul:cites aul:<changed_entity> .\n        BIND(\"cites\" AS ?relation)\n    } UNION {\n        ?dependent aul:covers aul:<changed_entity> .\n        BIND(\"covers\" AS ?relation)\n    } UNION {\n        ?dependent aul:illustrates aul:<changed_entity> .\n        BIND(\"illustrates\" AS ?relation)\n    }\n    ?dependent a ?depType .\n}"
)
```

**Reverse impact (what the changed entity depends on — check if those are still valid):**
```
mcp__open-ontologies__onto_query(
  query="PREFIX aul: <https://ai-usage-lessons.local/ontology#>\nSELECT ?dependency ?depType ?status WHERE {\n    aul:<changed_entity> aul:depends_on ?dependency .\n    ?dependency a ?depType .\n    OPTIONAL { ?dependency aul:status ?status }\n}"
)
```

### Step 4: Run requirement impact check

Use the pre-built query for any changed requirements:
```
mcp__open-ontologies__onto_query(
  query="PREFIX aul: <https://ai-usage-lessons.local/ontology#>\nSELECT ?entity ?type ?url WHERE {\n    ?req a aul:Requirement .\n    {\n        ?entity aul:covers ?req .\n    } UNION {\n        ?entity aul:cites ?req .\n    } UNION {\n        ?entity aul:illustrates ?req .\n    } UNION {\n        ?entity aul:depends_on ?req .\n    }\n    ?entity a ?type .\n    OPTIONAL { ?entity aul:source_url ?url }\n}\nORDER BY ?type ?entity"
)
```

### Step 5: Check for orphans

Run orphan checks:

**Orphan diagrams:**
```
mcp__open-ontologies__onto_query(
  query="PREFIX aul: <https://ai-usage-lessons.local/ontology#>\nSELECT ?diagram ?url WHERE {\n    ?diagram a aul:Diagram .\n    OPTIONAL { ?diagram aul:source_url ?url }\n    FILTER NOT EXISTS { ?diagram aul:illustrates ?anything }\n}"
)
```

**Untracked entities (no GitHub issue tracking them):**
```
mcp__open-ontologies__onto_query(
  query="PREFIX aul: <https://ai-usage-lessons.local/ontology#>\nSELECT ?entity ?type WHERE {\n    ?entity a ?type .\n    FILTER (?type IN (aul:Document, aul:Lecture, aul:SlideDeck, aul:Diagram))\n    FILTER NOT EXISTS { ?entity aul:tracked_by ?task }\n    FILTER NOT EXISTS { ?entity aul:status \"archived\" }\n}"
)
```

### Step 6: Cross-check with manifests

Read all manifests to verify ontology data matches local state:
1. `/home/levko/AI-usage-lessons/catalog/manifests/documents.yaml`
2. `/home/levko/AI-usage-lessons/catalog/manifests/lectures.yaml`
3. `/home/levko/AI-usage-lessons/catalog/manifests/decks.yaml`
4. `/home/levko/AI-usage-lessons/catalog/manifests/diagrams.yaml`

Check for:
- Entities in ontology but not in manifests (stale RDF data)
- Entities in manifests but not in ontology (missing RDF data)

### Step 7: Create issues for unresolved impacts

For each impacted entity that does NOT already have an open tracking issue:

First check for existing issues:
```
mcp__github__search_issues(
  query="repo:tellina-study/AI-usage-lessons is:open <entity identifier>",
  sort="updated",
  order="desc"
)
```

If no existing issue, create one:
```
mcp__github__issue_write(
  method="create",
  repo="tellina-study/AI-usage-lessons",
  title="[Impact] <affected entity> needs update due to <source change>",
  body="## Impact Assessment\n\n**Source change:** <what changed>\n**Affected entity:** <entity> (<type>)\n**Relation:** <depends_on|cites|covers|illustrates>\n\n## Cascade Chain\n\n1. <source> was modified\n2. <entity> <relation> <source>\n3. <downstream> depends on <entity>\n\n## Required Actions\n\n- [ ] Review <entity> for accuracy\n- [ ] Update content if needed\n- [ ] Run affected skill (<update-lecture|build-deck|diagram-refresh>)\n- [ ] Verify downstream dependencies\n\n## Detected by\n\nimpact-check skill — <today's date>",
  labels=["impact", "needs-review"]
)
```

### Step 8: Report

```
## Impact Check Report — <date>

### Recently Updated Entities
| Entity | Type | Updated |
|--------|------|---------|
| <entity> | Document | <date> |

### Cascading Impacts
| Changed Entity | Affected Entity | Relation | Has Issue? |
|----------------|-----------------|----------|------------|
| doc_X | lec_3 | covers | Yes (#42) |
| doc_X | deck_lec_3 | depends_on | Created (#45) |

### Orphans
| Type | Entity | Issue |
|------|--------|-------|
| Diagram | diag_X | No illustrates link |

### Manifest-Ontology Mismatches
| Entity | In Manifest | In Ontology |
|--------|-------------|-------------|
| <entity> | Yes | No |

### Statistics
- Entities checked: X
- Impacts found: Y
- Issues created: Z
- Orphans: W
```
