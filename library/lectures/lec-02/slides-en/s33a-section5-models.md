---
id: s33a
type: section_divider
section: "Section 5. Model Types and Sizes"
duration_min: 0.5
assertion: "Section 5 — Model Types and Sizes: what they run on and what they can do"
learning_goal: "Section divider for section 5 — a new course section: classifying models by size and deployment location, the 2026 landscape, benchmark critique"
learning_outcomes: [LO1, LO6]
chapter_ref: "§5.x (chapter-part3.md) [for-slide-s33a]"
visual_brief: "v3.1 (#183 round 3): 2-column composition (unified pattern) — left text: 'Section 5' (92pt gold), 'Model Types and Sizes', frame phrase, tag '4 case studies'. Right — real photo of a set of Russian matryoshka dolls (Wikimedia Commons, CC-BY-SA) in an Ocean rounded box, ≈25% of slide area, with attribution — a metaphor for models of different sizes nested within their classes. Bottom, full width — pipeline progress bar: the whole strip muted gold (the section sits logically 'above' the pipeline)."
---

# Visible content

## Title bar
(none — section divider slide)

## Body
[Large "Section 5" centered in the upper half — 140pt gold]

[Below it — sub-title]
**Model Types and Sizes**

[Caption — the section's meaning in one line]
"What models of different sizes run on — and what each class can do"

[Tag line, small]
4 case studies

[Pipeline progress at the bottom — the same pipeline diagram as on s04b]

[Small matryoshka illustration — corner of the slide]

## Speaker notes

The pipeline across four sections — tokenization, embeddings, attention, sampling — is the same regardless of the size of the model running it. But the model's size determines where and how you deploy it, and that's a separate practical question worth addressing explicitly.

Four case studies in this section. First, classification by size: small models that fit on a laptop or smartphone, medium models on a single gaming GPU, large models on a server with several cards, and giant models that physically exist only in the cloud or on a cluster — with examples of specific models as of September 2026 and what each class can do in terms of multimodality. Next, deployment location as a separate axis from size: the same question from a different angle, the criterion for choosing between local deployment and a cloud API. After that, a map of the terrain: the landscape of specific models as of September 2026, the frontier and open weights, pricing. And the section closes with a hard conversation about why you can't take benchmark numbers at face value when choosing a model.

This is the last substantive section before the lecture's finale — after this we'll assemble the entire pipeline and every mechanism we've covered into one picture.
