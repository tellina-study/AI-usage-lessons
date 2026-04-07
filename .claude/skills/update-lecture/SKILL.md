# update-lecture

Create or update a lecture document in Google Docs based on the course plan.

## Role

You are a course-curator agent. Your job is to take a lecture number, extract that lecture's content from the V2 course plan, and create or update a Google Doc with structured lecture content following the lecture outline template.

## Arguments

This skill expects a lecture number as argument. Example invocation: `/update-lecture 3`

If no argument is provided, ask which lecture number to process.

## Constants

- Google account: kzlevko@gmail.com
- Course plan (V2): `/home/levko/AI-usage-lessons/catalog/exports/docs/ai-v-raznyh-industriyah.md`
- Course plan (V1, reference): `/home/levko/AI-usage-lessons/catalog/exports/docs/ai-v-tsikle-sozdaniya-po.md`
- Lecture template: `/home/levko/AI-usage-lessons/templates/lecture-outline.md`
- Lectures manifest: `/home/levko/AI-usage-lessons/catalog/manifests/lectures.yaml`
- Google Drive folder ID: `1-f2hpJrlUbfnMcxhR-6vF3xCsXZUI6am`
- Ontology prefix: `aul: <https://ai-usage-lessons.local/ontology#>`

## Execution

### Step 1: Read source materials

Read these files using the Read tool:
1. `/home/levko/AI-usage-lessons/catalog/exports/docs/ai-v-raznyh-industriyah.md` — the V2 course plan
2. `/home/levko/AI-usage-lessons/templates/lecture-outline.md` — the template
3. `/home/levko/AI-usage-lessons/catalog/manifests/lectures.yaml` — current lectures manifest

### Step 2: Extract lecture content from course plan

Parse the V2 course plan and find the section for lecture N (the argument).
Extract:
- Lecture title
- Topics covered
- Key concepts and content points
- References to normative documents
- Practical examples mentioned

If the course plan uses a numbered list of lectures/topics, map the argument number to the corresponding section.

### Step 3: Query ontology for related documents

Find documents related to this lecture's topics:
```
mcp__open-ontologies__onto_query(
  query="PREFIX aul: <https://ai-usage-lessons.local/ontology#>\nSELECT ?doc ?url ?status WHERE {\n    ?lecture a aul:Lecture ;\n             aul:covers ?topic .\n    ?doc a aul:Document ;\n         aul:belongs_to_topic ?topic ;\n         aul:source_url ?url ;\n         aul:status ?status .\n    FILTER (?status != \"archived\")\n}\nORDER BY ?doc"
)
```

Also use RAG to find relevant content:
```
mcp__local-rag__query_documents(query="<lecture title and key topics>", limit=5)
```

### Step 4: Compose lecture document

Using the template structure, compose the lecture content:

```markdown
# Lecture <N>: <Title>

## Topics Covered
- <topic 1>
- <topic 2>

## Prerequisites
- Lecture <N-1>: <previous lecture title>

## Normative References
- <document title> — <source_url>

## Materials
- Slides: <to be created>
- Diagrams: <to be created>

## Learning Objectives
1. <objective based on course plan>
2. ...

## Outline
### Part 1 — <subtopic>
<detailed content>

### Part 2 — <subtopic>
<detailed content>

### Part 3 — <subtopic>
<detailed content>

## Assessment
- <assessment criteria from course plan>
```

### Step 5: Check if lecture already exists

Read the lectures manifest. If lecture N already has an entry with a Google Doc ID:

**Update existing doc:**
```
mcp__workspace-mcp__modify_doc_text(
  document_id="<existing_doc_id>",
  edits=[{"type": "replace_all", "find": "<old content marker>", "replace": "<new content>"}]
)
```

If the doc needs a full rewrite, it may be simpler to clear and re-insert. Use `mcp__workspace-mcp__batch_update_doc` for complex structural changes.

**Create new doc (IMPORTANT — use import, not create_doc):**
```
mcp__workspace-mcp__import_to_google_doc(
  user_google_email="kzlevko@gmail.com",
  file_name="Лекция <N>: <Title>.md",
  content="<full markdown content composed in Step 4>",
  source_format="md",
  folder_id="1-f2hpJrlUbfnMcxhR-6vF3xCsXZUI6am"
)
```

This preserves markdown formatting (headings, bold, lists, tables) as native Google Docs styles.
Do NOT use `create_doc` — it inserts raw text without formatting.

Save the returned document ID.

### Step 6: Update lectures manifest

Update `/home/levko/AI-usage-lessons/catalog/manifests/lectures.yaml` using the Write tool:

```yaml
lectures:
  - number: <N>
    title: "<lecture title>"
    doc_id: "<google_doc_id>"
    source_url: "https://docs.google.com/document/d/<doc_id>/edit"
    topics:
      - "<topic 1>"
      - "<topic 2>"
    prerequisites:
      - <N-1>
    status: draft
    updated_at: "<today YYYY-MM-DD>"
```

Preserve existing lecture entries. Only add/update the one being processed.

### Step 7: Update ontology

Load lecture entity and its relations:
```
mcp__open-ontologies__onto_load(
  data="@prefix aul: <https://ai-usage-lessons.local/ontology#> .\n@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n\naul:lec_<N> a aul:Lecture ;\n    aul:source_url \"https://docs.google.com/document/d/<doc_id>/edit\" ;\n    aul:source_system \"google_drive\" ;\n    aul:status \"draft\" ;\n    aul:owner \"kzlevko@gmail.com\" ;\n    aul:updated_at \"<today>T00:00:00\"^^xsd:dateTime ;\n    aul:covers aul:topic_<topic_slug_1> ;\n    aul:covers aul:topic_<topic_slug_2> ;\n    aul:depends_on aul:lec_<N-1> .",
  format="turtle"
)
```

### Step 8: Report

```
## Lecture Update Report — <date>

- Lecture: <N> — <title>
- Action: <created|updated>
- Google Doc: https://docs.google.com/document/d/<doc_id>/edit
- Topics: <topic list>
- References used: <count> documents
- Ontology: lecture entity + <count> relations loaded
```

### Step 9: Trigger compile-wiki

After creating/updating lecture content, remind the user to run `/compile-wiki` to ingest new research notes and papers into RAG and update wiki indexes.
