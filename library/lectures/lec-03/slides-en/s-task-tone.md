---
id: s-task-tone
type: assertion_visual
section: "Section 1. The prompt and its limits"
assertion: "Text in a given tone is few-shot with 3–5 samples; the judgment boundary — AI detectors can't be trusted as evidence (some under 80% accurate, +30% more false positives on non-native writers)"
learning_goal: "Task pattern 2: few-shot style transfer; the on-point failure — unreliable detectors"
learning_outcomes: [LO7, LO4]
chapter_ref: "§1.10 [for-slide-task-tone]"
interaction: none
---

# Visible content

## Title bar
«Text in a given tone: few-shot from samples»

## Body
[Setup]
You need text in a specific voice, style, or register: a brand-voice email, a support reply, a draft that reads "like a human wrote it."

[Architecture: few-shot style transfer]
3–5 samples of the author's writing as examples → generation in the same style. Models copy public personas well but struggle with an ordinary author's individual style.

[Gold callout — failure]
AI detectors can't be trusted as evidence: some are under 80% accurate, non-native writers' texts get flagged up to +30% more often, and accuracy drops after paraphrasing.

## Speaker notes

The second class is generating text in a given tone, style, or register: a marketing email "in our brand voice," a support reply in the company's signature tone, a draft that reads "like a human wrote it." The right architecture here is few-shot style transfer: give three to five samples of the author's writing wrapped in examples, and ask for generation in the same style. This is the most reliable lever for tone and voice, and it's exactly where a persona role works the way people usually assume it does — it shapes tone, not facts.

But the boundaries of this class matter more than the technique itself, and there are two of them. First: models copy public figures and fictional characters reasonably well, but struggle with an ordinary author's individual style — personal style doesn't reduce to a handful of sliders. Second, and sharper: AI detectors are unreliable as sole evidence. Vendors themselves admit this in their documentation. Independent studies put some detectors' accuracy below eighty percent; texts by non-native speakers get flagged as machine-written noticeably more often — the baseline here is the false-positive rate relative to native speakers — and accuracy drops sharply after simple paraphrasing.

As with the previous class, let's name the parameters and validation so this is a recipe, not just advice. Parameters: formality (from "academic" to "friendly"), emotional coloring, a specific persona, the number and quality of style samples, and explicit prohibitions — no bureaucratic phrasing, no emoji, no superlatives. Validation is harder here because style is weakly formalizable: teams use an LLM judge for tone match, checks against concrete markers (sentence length, presence or absence of specific vocabulary), and spot-check human review. A typical failure with fine-grained multi-attribute control: the attributes conflict — "formal, but warm, but brief, but detailed" pull in different directions, and the model underperforms on some dimensions; on long dialogues, persona drift adds on top.

The engineering conclusion is twofold. Generating human-like text is technically possible, but passing it off as your own is an ethical and academic risk. And a detector can't be trusted either as a shield to prove a text is AI-written, or as a sword to reliably hide its AI origin. This is the same lesson as the whole chapter — observable doesn't equal guaranteed — applied to detection.
