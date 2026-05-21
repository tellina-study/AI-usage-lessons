# Slide Deck: {{title}}

## Metadata
- Lecture: {{lecture_number}}
- Google Slides URL: 
- Last updated: 

## Slide Sequence

### Slide 1 — Title (hero_cover, ENFORCED [[hero-images-required]])
- Hero image ≥40% area (real, via 6-tier acquisition)
- media:
    pattern: hero_cover
    primary: <description of hero illustration — foreshadow keystone OR domain identity>
    acquisition_tier: <1-6>  # per [[no-mock-fallbacks]] (1=og:image, 2=Wikipedia, 3=press release, 4=YouTube thumb, 5=Wayback, 6=Google Images)
    source_url: <URL>  # actual source for traceability
    attribution_label: <text on slide>  # e.g. "CNN · 16 мая 2024", "Wikimedia · CC-BY-SA"
    fallback: <static PNG path>  # if Tier 6 fails — custom data-viz hero, NOT plain text card

### Slide 2 — Agenda
- 

### Slide 3 — {{topic}}
- Key points:
- Diagram: 
- media:
    pattern: <pattern_name>  # e.g. real_screenshot, generated_chart, schema_layered, schema_quadrant
    primary: <description>
    acquisition_tier: <1-6>  # per [[no-mock-fallbacks]] — for real_screenshot patterns
    source_url: <URL>
    attribution_label: <text on slide>
    fallback: <static PNG path>
- Notes:

### Slide N — Summary / Closing (hero_closing, ENFORCED [[hero-images-required]])
- Hero image ≥40% area (real, via 6-tier acquisition)
- media:
    pattern: hero_closing
    primary: <description — bridge к Lec-N+1 OR emotional payoff OR iconic case visual>
    acquisition_tier: <1-6>
    source_url: <URL>
    attribution_label: <text on slide>
    fallback: <static PNG path>
- Key takeaways
- Next lecture preview
