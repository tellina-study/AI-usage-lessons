---
id: s37
type: assertion_visual
duration_min: 3.5
assertion: "A 5-question checklist before using AI in a creative project."
learning_goal: "Action checklist — the main takeaway of the lecture"
learning_outcomes: [LO5]
chapter_ref: "§5.1 — 5-question checklist"
references: []
visual:
  pattern: pipeline
  primary: "5-question flowchart in an Ocean rounded box + decision tree"
---

# 5-question checklist before AI in creative work

## Assertion

Before using AI in a creative project — 5 questions. If any one is "no/risk," reconsider the approach.

## Visual

On top, title 28pt deep blue: "5-question checklist before AI in creative work." Below the title — a large Ocean rounded box with 5 numbered questions vertically (each — a separate sub-card with a number and the question + a chip of examples): 1. "Training-data licensing on the tool?" (Firefly = yes; Stable Diffusion / Midjourney = risks). 2. "Output-similarity check for protected content?" (NYT verbatim-citation risk). 3. "Voice/likeness consent if applicable?" (ScarJo, SAG-AFTRA, Korea). 4. "IP-clean tools for commercial use?" (Adobe Firefly vs scraped models). 5. "Brand-trust risk — legacy/flagship campaign?" (Coca-Cola, Toys R Us, SI). To the right of the questions — a gold-highlighted decision branch: "If 'no/risk' on at least one → human alternative OR structural mitigation." Below — an anchor: "Apply BEFORE the start, not after."

## Speaker notes

This is the final takeaway of the lecture — a five-question action checklist. Apply it before the start of any creative project with an AI component, not after. Question one — training-data licensing on the tool. Adobe Firefly — yes, a licensed corpus (Adobe Stock plus licensed). Stable Diffusion — no, web-scraped data, Andersen-class risk. Midjourney — debatable, there are risks. This is the first filter. If you build a commercial product on a foundation model — choose a tool with documented licensed training, otherwise you have structural legal debt. Question two — output-similarity check for protected content. The product must have a technical control that tracks whether the model's output verbatim or substantially reproduces a copyright-protected source. The NYT v. OpenAI verbatim-citation theory is no longer a theoretical risk, it is an active lawsuit. If you do not have such a control — you have the verbatim-citation risk personally. Question three — voice and likeness consent if applicable. If the product uses the voice or face of specific people — explicit consent is needed. ScarJo, SAG-AFTRA Digital Replicas, the Korea schoolgirl crisis — all cases show that without a consent-acquisition infrastructure you have exposure to risks. This includes the use of selfies, uploaded photos, voice samples — any recognizable real person. Question four — IP-clean tools for commercial use. This is the integration of questions one and two: for commercial deployment you must have an end-to-end IP-clean pipeline — a licensed training corpus plus an output-similarity check plus disclosure. Adobe Firefly Foundry presents this as a product. Models on scraped data are "cheap to start, expensive to bring to release." Question five — brand-trust risk, legacy and flagship campaigns. If you deploy AI for a category where the audience expects human creative direction — a flagship seasonal campaign, by-line trust, an original brand voice — this is structurally spending brand capital. Coca-Cola Christmas, Toys R Us Cannes, SI by-line — all show a measurable cost. If on any of the five questions the answer is "no" or "risk identified" — your choice must be one of three. Option A — a non-AI alternative, do not use AI. Option B — structural mitigation: a licensing layer, a similarity check, a consent infrastructure, brand-aware design. Option C — accept the risk explicitly, with a documented business decision and a calibrated mitigation. Do not make an implicit acceptance — that is the most expensive mistake. If you apply this five-question diagnostic to any creative task with an AI component, you will have a protective layer that ensures deliberate engineering judgment. This is the main takeaway of this lecture.
