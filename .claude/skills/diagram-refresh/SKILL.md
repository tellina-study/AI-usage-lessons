# diagram-refresh

Refresh diagrams based on content changes and ontology relationships.

## Role

You are a diagram editor agent. Your job is to check which diagrams need updating based on ontology relations, create or update `.drawio` XML files, and keep the diagrams manifest in sync.

## Constants

- Diagrams directory: `/home/levko/AI-usage-lessons/diagrams/`
- Diagrams manifest: `/home/levko/AI-usage-lessons/catalog/manifests/diagrams.yaml`
- Ontology prefix: `aul: <https://ai-usage-lessons.local/ontology#>`
- Lecture flow diagrams: `/home/levko/AI-usage-lessons/diagrams/lecture-flows/`

## Execution

### Step 1: Query ontology for diagram relations

Find all entities that have `illustrates` relations (diagrams linked to lectures, documents, topics):
```
mcp__open-ontologies__onto_query(
  query="PREFIX aul: <https://ai-usage-lessons.local/ontology#>\nSELECT ?diagram ?target ?targetType WHERE {\n    ?diagram a aul:Diagram ;\n             aul:illustrates ?target .\n    ?target a ?targetType .\n}\nORDER BY ?diagram"
)
```

Also find orphan diagrams (not linked to anything):
```
mcp__open-ontologies__onto_query(
  query="PREFIX aul: <https://ai-usage-lessons.local/ontology#>\nSELECT ?diagram ?url WHERE {\n    ?diagram a aul:Diagram .\n    OPTIONAL { ?diagram aul:source_url ?url }\n    FILTER NOT EXISTS { ?diagram aul:illustrates ?anything }\n}"
)
```

### Step 2: Scan local diagrams directory

```bash
find /home/levko/AI-usage-lessons/diagrams/ -name "*.drawio" -type f
```

Read the diagrams manifest:
Read `/home/levko/AI-usage-lessons/catalog/manifests/diagrams.yaml` using the Read tool.

### Step 3: Identify diagrams needing attention

Build a list of diagrams to process:

1. **Ontology says diagram exists but no .drawio file** => CREATE new diagram
2. **Local .drawio exists but not in manifest** => CATALOG it
3. **Diagram's target entity was updated more recently than the diagram** => REFRESH
4. **Orphan diagrams** (in ontology but no `illustrates` link) => REPORT for review

### Step 4: Create or update diagrams

For each diagram that needs creation or update:

**Option A — Generate from Mermaid (preferred for flow diagrams):**

First, design the diagram as Mermaid syntax based on the content it illustrates. Then convert:
```
mcp__drawio__open_drawio_mermaid(
  mermaid="graph TD\n    A[Topic 1] --> B[Topic 2]\n    B --> C[Topic 3]\n    C --> D[Assessment]",
  title="<diagram title>"
)
```

This opens the diagram in draw.io. Capture the XML output.

**Option B — Generate from XML (for complex diagrams):**
```
mcp__drawio__open_drawio_xml(
  xml="<mxfile><diagram name=\"Page-1\"><mxGraphModel><root><mxCell id=\"0\"/><mxCell id=\"1\" parent=\"0\"/><!-- cells here --></root></mxGraphModel></diagram></mxfile>",
  title="<diagram title>"
)
```

**Save the .drawio file locally:**
Write the XML content to the appropriate path using the Write tool:
```
/home/levko/AI-usage-lessons/diagrams/<category>/<slug>.drawio
```

Categories:
- `lecture-flows/` — lecture structure and flow diagrams
- `architecture/` — system architecture diagrams
- `concept-maps/` — topic relationship diagrams

### Step 5: Update diagrams manifest

Update `/home/levko/AI-usage-lessons/catalog/manifests/diagrams.yaml` using the Write tool:

```yaml
diagrams:
  - slug: "<diagram-slug>"
    title: "<diagram title>"
    local_path: "diagrams/<category>/<slug>.drawio"
    illustrates:
      - entity: "lec_<N>"
        type: Lecture
    format: drawio
    status: active
    updated_at: "<today YYYY-MM-DD>"
```

Preserve existing entries. Only add/update processed diagrams.

### Step 6: Update ontology

For newly created diagrams, load the entity and its `illustrates` relation:
```
mcp__open-ontologies__onto_load(
  data="@prefix aul: <https://ai-usage-lessons.local/ontology#> .\n@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n\naul:diag_<slug> a aul:Diagram ;\n    aul:source_system \"local\" ;\n    aul:status \"active\" ;\n    aul:updated_at \"<today>T00:00:00\"^^xsd:dateTime ;\n    aul:illustrates aul:lec_<N> .",
  format="turtle"
)
```

### Step 7: Report

```
## Diagram Refresh Report — <date>

### Created
| Diagram | Illustrates | Path |
|---------|-------------|------|
| <slug> | lec_3 | diagrams/lecture-flows/<slug>.drawio |

### Updated
| Diagram | Reason | Path |
|---------|--------|------|
| <slug> | target entity changed | ... |

### Orphans (no illustrates link)
| Diagram | Path |
|---------|------|
| <slug> | ... |

### Statistics
- Created: X
- Updated: Y
- Orphans: Z
- Errors: E
```
