---
id: s25
type: case_study
section: "Section 3. Attention Mechanism"
duration_min: 3.5
assertion: "Verbatim-insertion retrieval is nearly solved — but without lexical overlap, 11 of 13 models lose more than half their accuracy already at 32,000 tokens"
learning_goal: "Updating lost-in-the-middle: needle is solved, NoLiMa exposes the boundary; the formula '1M window ≠ 1M of reasoning'"
learning_outcomes: [LO6]
chapter_ref: "§3.7 (chapter-part2.md) [for-slide-s25]"
visual_brief: "Two side-by-side panels in Ocean rounded boxes. Left, 'Finding a verbatim phrase — solved': teal checkmark, 'single-needle: 99% on the full 1M window (Gemini Deep Think).' Right, 'Understanding by meaning — no': a NoLiMa bar chart — 13 model bars, 11 of them fall below the dashed '50% of the model's own baseline accuracy' line, x-axis marker '32K = 3% of the advertised 1M window' (gold). Bottom, a wide gold callout formula 'A 1M window ≠ 1M tokens of reasoning.'"
---

# Visible content

## Title bar
"Verbatim-insertion retrieval is solved. Understanding long context is not"

## Body
[2 side-by-side panels, Ocean rounded boxes]

**Finding it verbatim (needle-in-a-haystack) — nearly solved** ✓
- Finding an inserted phrase by literal match: flagships reach up to 99% on the full 1-million-token window
- "Find where the contract mentions the amount" — works almost as advertised

**Understanding by meaning (NoLiMa, 2025) — collapse**
- The benchmark removed literal word overlap between the question and the hidden fragment
- **11 of 13 models fall below 50% of their own accuracy on short context**
- Already at **32,000 tokens** — that's ~3% of a flagship's advertised window

[Gold callout — formula]
**A 1M window ≠ 1M tokens of reasoning. The window is how much the model can read; the usable length is how many tokens out it can still connect facts across.**

[Practical line at the bottom]
Put critical instructions at the start or end of the prompt · targeted retrieval of 5–10 fragments beats "dump everything into the window" · test at your task's working length

## Speaker notes

You probably know the classic 2023 result "Lost in the Middle": a fact buried in the middle of a long context is retrieved worse than one at the edges — a U-shaped accuracy curve. That knowledge needs a 2026 update — in both directions.

The good news: literal "needle in a haystack" search — finding a verbatim inserted phrase — is essentially solved by the flagships: up to 99% on the full million-token window. If the task is to find where the contract mentions the amount, a large window works almost as advertised.

The bad news came from the NoLiMa benchmark, which removed the main crutch of such tests — literal lexical overlap between the question and the hidden fragment. When you have to find something by meaning rather than by matching words, the picture collapses: eleven of thirteen tested models fall below half of their own accuracy on short context — note the baseline: it's the model compared against itself, not some absolute threshold. And this happens already at 32,000 tokens — not at a million, but at three percent of a flagship's advertised window. The U-curve didn't disappear — it hid behind high scores on tests that measure retrieval, not reasoning.

A formula worth remembering: a million-token window doesn't equal a million tokens of reasoning. The window is how much the model can read; the usable length is how many tokens out it can still connect facts across without literal cues, and the second quantity is many times smaller than the first. Consequences: put critical instructions at the start or the end, not in the middle; "dump the whole knowledge base into the window" loses to good retrieval of five to ten targeted fragments — more on that next lecture; and when choosing a model for long documents, don't ask "what window size" but "what results on benchmarks without lexical overlap" — and test at your task's actual working length: half an hour of stress-testing on real documents tells you more than any leaderboard.
