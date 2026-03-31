# Ontology Mapping Rules

## Document → RDF

When a document is cataloged, create a triple:

```turtle
<doc:{id}> a aul:Document ;
    aul:source_url "{google_drive_url}" ;
    aul:source_system "google_drive" ;
    aul:updated_at "{iso_datetime}"^^xsd:dateTime ;
    aul:status "active" ;
    aul:owner "{owner_email}" .
```

## Lecture → RDF

```turtle
<lecture:{number}> a aul:Lecture ;
    aul:covers <topic:{topic_id}> ;
    aul:depends_on <lecture:{prev_number}> ;
    aul:tracked_by <task:{issue_number}> .
```

## Diagram → RDF

```turtle
<diagram:{filename}> a aul:Diagram ;
    aul:illustrates <lecture:{number}> ;
    aul:source_system "local" ;
    aul:source_url "diagrams/{path}" .
```

## General Rules

1. IDs are derived from filenames or Google Drive file IDs
2. All `updated_at` timestamps use ISO 8601 with timezone
3. Relations are bidirectional in queries but stored as forward edges
4. Orphan check: every Diagram and SlideDeck should have at least one `illustrates` or `covers` relation
