---
id: s08
type: case_study
section: "Section 1. Tokenization"
duration_min: 3
assertion: "The patch race: 'strawberry' got fixed in April, 'cranberry' not until July; the underlying task class stays unsolved"
learning_goal: "Letter-blindness mechanism (fast — the meme is familiar) + 2026 diagnosis: point patches instead of a skill + jagged intelligence"
learning_outcomes: [LO6, LO7]
chapter_ref: "§1.4 [for-slide-s08]"
visual_brief: "Left, compact — the mechanism: strawberry → [st][raw][berry], the model sees 3 tokens, not 10 letters. v3.1 (#183 round 3): under the mechanism — a real ChatGPT screenshot (OpenAI forum, 2024, \"There are two 'r' characters in the word 'strawberry'\") with a small attribution caption 'screenshot: ChatGPT, OpenAI forum, 2024'. Right — patch-race timeline: GPT-5.2 (Dec 2025) strawberry ✗; GPT-5.5 (Apr 2026) strawberry ✓ / cranberry ✗; GPT-5.6 (Jul 2026) cranberry ✓ (gold) [VFY-day-of]; StrawberryBench — 847 questions, 7 levels. Bottom callout with the explanation: 'jagged intelligence' — skill level is set by training data, not by 'general intelligence': the model wins Olympiad gold and fails letter counting. Below it, a 'What to do' line: test your own domain's cranberry; a viral pass ≠ a skill."
interaction: retrieval_live_attempt
verify_day_of: true
---

# Visible content

## Title bar
"The patch race: they fixed strawberry, then cranberry — one word at a time"

## Body
[Left — the mechanism, compact, Ocean rounded box]

`strawberry` → `[st][raw][berry]` — the model sees **3 tokens**, not 10 letters

[Right — patch race timeline]

**GPT-5.2** (Dec 2025): "there are two r's in strawberry" ✗

**GPT-5.5** (Apr 2026): strawberry ✓ / **cranberry ✗** — "two r's" instead of three

**GPT-5.6** (Jul 2026): cranberry ✓ (gold) — but the task class isn't closed

**StrawberryBench**: 847 questions, 7 difficulty levels — systematic testing instead of one viral question

[Callout at bottom — with the mechanism explanation]
**"Jagged intelligence": skill level is set by training data, not by "general intelligence" — the same model wins Olympiad gold and fails letter counting.**

[Bottom line, "What to do"]
**What to do:** test your own domain's "cranberry" — obscure cases nobody hyped about; going viral ≠ having the skill.

## Speaker notes

You know the "how many r's in strawberry" meme; you probably also know that current models answer it correctly now. The conclusion "so they've learned to count letters" is wrong, and here's why.

The mechanism is letter blindness. A word arrives at the model as three tokens, not ten letters. Inside the learned token vector there's no field saying "contains an r at position N" — there's contextual statistics instead. Character-by-character counting requires reasoning on top of the tokenized representation — spelling the word out or calling code; a single forward pass doesn't reliably get you there. This is a structural property of the pipeline.

Now look at the 2026 patch race. GPT-5.2, in December 2025, still answered "two r's" for strawberry. GPT-5.5, released in April 2026, passes strawberry — but on "how many r's in cranberry" it answered "two"; the correct answer is three. Only GPT-5.6, in July 2026, finally fixed cranberry too [VFY-day-of] — check the current model right now. Notice the pattern: each viral case gets patched individually, one at a time, rather than through a single skill-level improvement — otherwise fixing strawberry would have immediately closed cranberry too. To test the task class systematically, StrawberryBench appeared — 847 questions across seven difficulty levels; it's there, not on one viral word, that you see character counting remains a genuine weak spot.

The phenomenon has a name: "jagged intelligence" — a capability profile with sharp dips right next to peaks. The reason is that skill level is set by training data, not by "general intelligence": wherever a skill is richly represented in the data, there's a peak; wherever the word's representation hides the needed structure, there's a dip. The same model solves Olympiad-level math and fails letter counting; on multiplication, GPT-4 without tools scored around 59% on three-digit numbers, 4% on four-digit numbers, and 0% on five-digit numbers. The lesson carries over to practice: if a model passes your test, check it against "your domain's cranberry" — a structurally analogous but unhyped example nobody tested on: going viral is not a skill. And for character-level operations and arithmetic — use an external tool, not a direct forward pass.
