# build-deck

Build or rebuild a Google Slides presentation for a lecture.

## Role

You are a deck-editor agent. Your job is to take a lecture number, read the lecture content and related materials, and create a Google Slides presentation with structured slides following the slide outline template.

## Arguments

This skill expects a lecture number as argument. Example invocation: `/build-deck 3`

If no argument is provided, ask which lecture number to process.

## Constants

- Google account: kzlevko@gmail.com
- Lectures manifest: `/home/levko/AI-usage-lessons/catalog/manifests/lectures.yaml`
- Decks manifest: `/home/levko/AI-usage-lessons/catalog/manifests/decks.yaml`
- Slide template: `/home/levko/AI-usage-lessons/templates/slide-outline.md`
- Diagrams directory: `/home/levko/AI-usage-lessons/diagrams/`
- Google Drive folder ID: `1-f2hpJrlUbfnMcxhR-6vF3xCsXZUI6am`
- Ontology prefix: `aul: <https://ai-usage-lessons.local/ontology#>`

## Execution

### Step 1: Read source materials

Read these files using the Read tool:
1. `/home/levko/AI-usage-lessons/catalog/manifests/lectures.yaml` — find lecture N entry
2. `/home/levko/AI-usage-lessons/catalog/manifests/decks.yaml` — check if deck already exists
3. `/home/levko/AI-usage-lessons/templates/slide-outline.md` — slide structure template

If lecture N has a `doc_id` in the manifest, read the lecture Google Doc:
```
mcp__workspace-mcp__get_doc_as_markdown(document_id="<lecture_doc_id>")
```

If no doc_id, read the course plan instead:
Read `/home/levko/AI-usage-lessons/catalog/exports/docs/ai-v-raznyh-industriyah.md` and extract lecture N content.

### Step 2: Find relevant diagrams

Check for diagrams related to this lecture:
```bash
ls -la /home/levko/AI-usage-lessons/diagrams/
```

Also query the ontology for diagrams that illustrate this lecture's topics:
```
mcp__open-ontologies__onto_query(
  query="PREFIX aul: <https://ai-usage-lessons.local/ontology#>\nSELECT ?diagram ?url WHERE {\n    aul:lec_<N> aul:covers ?topic .\n    ?diagram a aul:Diagram ;\n             aul:illustrates ?topic .\n    OPTIONAL { ?diagram aul:source_url ?url }\n}"
)
```

### Step 3: Design slide structure

Based on the lecture content and template, plan the slides:

1. **Title slide**: Lecture number, title, date
2. **Agenda slide**: List of topics to cover
3. **Content slides** (one per major topic/subtopic):
   - Heading
   - 3-5 bullet points of key content
   - Speaker notes with detailed explanation
   - Diagram reference if applicable
4. **Summary slide**: Key takeaways
5. **Next lecture preview**: What comes next

Aim for 12-20 slides depending on content density.

### Step 4: Check if deck already exists

Read the decks manifest. If lecture N already has a deck entry with a `presentation_id`:

**Update existing deck** — use batch_update to modify slides:
```
mcp__workspace-mcp__get_presentation(presentation_id="<existing_presentation_id>")
```
Review existing slides, then update:
```
mcp__workspace-mcp__batch_update_presentation(
  presentation_id="<existing_presentation_id>",
  requests=[
    {"deleteObject": {"objectId": "<slide_id>"}},
    ...
  ]
)
```

**Create new presentation:**
```
mcp__workspace-mcp__create_presentation(
  title="Лекция <N>: <Title>",
  folder_id="1-f2hpJrlUbfnMcxhR-6vF3xCsXZUI6am"
)
```

Save the returned presentation ID.

### Step 5: Populate slides

Use `mcp__workspace-mcp__batch_update_presentation` to add slides with content.

For each slide, create a request batch. Example for adding a new slide with content:
```
mcp__workspace-mcp__batch_update_presentation(
  presentation_id="<presentation_id>",
  requests=[
    {
      "createSlide": {
        "slideLayoutReference": {"predefinedLayout": "TITLE_AND_BODY"},
        "insertionIndex": <index>
      }
    }
  ]
)
```

Then get the presentation to find the new slide's object IDs:
```
mcp__workspace-mcp__get_presentation(presentation_id="<presentation_id>")
```

Insert text into the slide placeholders:
```
mcp__workspace-mcp__batch_update_presentation(
  presentation_id="<presentation_id>",
  requests=[
    {
      "insertText": {
        "objectId": "<placeholder_object_id>",
        "text": "<slide content>",
        "insertionIndex": 0
      }
    }
  ]
)
```

Add speaker notes:
```
mcp__workspace-mcp__batch_update_presentation(
  presentation_id="<presentation_id>",
  requests=[
    {
      "insertText": {
        "objectId": "<notes_object_id>",
        "text": "<speaker notes>",
        "insertionIndex": 0
      }
    }
  ]
)
```

### Step 6: Update decks manifest

Update `/home/levko/AI-usage-lessons/catalog/manifests/decks.yaml` using the Write tool:

```yaml
decks:
  - lecture_number: <N>
    title: "Лекция <N>: <Title>"
    presentation_id: "<google_slides_id>"
    source_url: "https://docs.google.com/presentation/d/<id>/edit"
    slide_count: <number>
    diagrams_used:
      - "<diagram filename>"
    status: draft
    updated_at: "<today YYYY-MM-DD>"
```

Preserve existing entries. Only add/update the one being processed.

### Step 7: Update ontology

```
mcp__open-ontologies__onto_load(
  data="@prefix aul: <https://ai-usage-lessons.local/ontology#> .\n@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n\naul:deck_lec_<N> a aul:SlideDeck ;\n    aul:source_url \"https://docs.google.com/presentation/d/<id>/edit\" ;\n    aul:source_system \"google_drive\" ;\n    aul:status \"draft\" ;\n    aul:owner \"kzlevko@gmail.com\" ;\n    aul:updated_at \"<today>T00:00:00\"^^xsd:dateTime ;\n    aul:covers aul:topic_<topic_slug> ;\n    aul:depends_on aul:lec_<N> .",
  format="turtle"
)
```

### Step 8: Report

```
## Deck Build Report — <date>

- Lecture: <N> — <title>
- Action: <created|updated>
- Google Slides: https://docs.google.com/presentation/d/<id>/edit
- Slides: <count>
- Diagrams included: <list>
- Ontology: deck entity + <count> relations loaded
```
