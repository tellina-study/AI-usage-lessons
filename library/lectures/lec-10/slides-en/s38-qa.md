---
id: s38
type: qa
duration_min: 1
assertion: "Q&A. Backup questions about vertical farming thermodynamics, agentic AI scope, ITELMA vs Cognitive Pilot, foundation models by 2030."
learning_goal: "Dedicated Q&A slide with 3 backup prompts"
learning_outcomes: []
chapter_ref: "Q&A backup + §9 Part 3"
references: []
visual:
  pattern: cover_distinct_qa
  primary: "Huge Q&A typography + Lucide message-circle-question icon + 3 backup prompts small at the bottom"
---

# Q&A

## Assertion

Q&A.

## Visual

The main composition — a huge headline «Q&A?» centered 120pt bold Primary deep, below it — the icon `message-circle-question` Lucide 96px Primary mid.

Below this — 3 backup prompts in a horizontal row in an Ocean rounded box (small font 14pt italic Primary light, as hints for the lecturer and student):

1. **«Vertical farming — Oishii survived and raised $150M in 2026. Is this an exception or a turnaround?»** (chapter B7)
2. **«ITELMA vs Cognitive Pilot — is it really a replacement or do they solve different tasks?»** (chapter B6)
3. **«Foundation models — how accessible are they to smallholders by 2030?»** (chapter B14)

At the bottom — a small course-contact card (~10pt italic Primary light) with the course contact.

## Speaker notes

Let's open the Q&A. I have three typical questions in reserve that may come up — in case the room is quiet.

The first — about vertical farming. "Oishii survived and raised a Series C of one hundred fifty million in May 2026. Is this an exception or a turnaround for the category?" The answer is short. Oishii is an exception that proves the rule, not a reversal of the category's collapse. Oishii sells premium strawberries at ten-plus dollars per package in Whole Foods in New York. Their unit economics work precisely because they don't try to compete with the open field on leafy greens. Tortuga AgTech, acquired by Oishii in March 2025, showed technical success — fifty percent reduction in harvest expenses — but within a collapsed category. This is a business-model lesson, not a technical robotics lesson. The premium segment in vertical farming can survive; commodity leafy greens can't, because of LED thermodynamics versus free sunlight.

The second — about Cognitive Pilot and ITELMA. "Is it really a replacement of one by the other or do they solve different tasks?" They solve different tasks. Cognitive Pilot is a CV stack answering the question "what do I see" — recognizing visual features in the field: the uncut edge, obstacles. ITELMA Kvadro is sensor-fusion AI on multi-GNSS, answering the question "where am I" — precise navigation with two-to-five-centimeter accuracy. The correct solution for a modern autonomous combine is a combination of both: GNSS navigation as primary plus CV as secondary for nonstandard situations. The "one is better than the other" comparison is a false simplification. This is an example of AP-two-a — an architectural choice within the AI domain.

The third — about foundation models. "How accessible are TerraMind and Prithvi-EO 2.0 to smallholders by 2030?" The answer depends on three factors. First — compute. Fine-tuning a foundation model requires a significant GPU cluster. For smallholders in Africa or Asia, direct access to H100 / A100 — no. The alternative — fine-tune-as-a-service from large providers. Second — local data. A foundation model for agriculture covers geographies unevenly — the US, EU, Brazil are data-rich; sub-Saharan Africa, Russia outside the southern regions — underrepresented. This means fine-tuning requires local data collection — which is hard for smallholders without an external partner. Third — the interface. A smallholder doesn't work with a Hugging Face API; they need a mobile app in their national language. This means there must be a UX layer between the foundation model and the farmer, which hasn't been built yet. By 2030 I expect: foundation models will become accessible to large AgTech startups serving smallholders via UX layers (like Plantix, but with a RAG-grounded architecture); direct smallholder access to the models — no.

Open to your questions.

## Sources

- Chapter v3.1 §9 Part 3 — Q&A backup.
