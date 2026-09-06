---
id: s01
type: hook
section: "Section 0. Introduction"
duration_min: 2.5
assertion: "temperature=0 means the answer is always identical, right? Yes. → But no."
learning_goal: "Meme hook: two-panel meme about temperature=0, no checklist and no voting — hook with a question, the answer unfolds in the sampling section"
learning_outcomes: [LO7]
chapter_ref: "§Введение [for-slide-s01]"
visual_brief: "v3.1 (#183 round 3, owner mandate 'use real memes and pictures from the internet'): a real, recognizable meme template 'Well yes, but actually no' (imgflip, a still frame from 'The Pirates! Band of Misfits', Aardman) — ≥40% of slide area. In the template's empty top field — custom large-font text: 'temperature=0 means the answer is always identical, right?'. The meme's built-in caption 'Well yes, but actually no' already answers the question literally. Below — a small gold-colored gloss line: 'Yes, formally deterministic. But no — not in practice. Why — today's topic.'. Source: imgflip.com (see rendered/assets/web/attribution.md). No checklists, no assertions, no lists, no hands-raising interaction."
---

# Visible content

## Title bar
(none — poster-meme slide)

## Body
[Large two-panel meme composition, hero illustration ≥40% of area]

**Panel 1**
"temperature=0 means the answer is always identical, right?"
**Yes.**

**Panel 2** *(gold)*
**→ But no.**

[Small caption at the bottom]
*why — today's topic*

## Speaker notes

A simple warm-up question: if you set temperature to zero, will the model's answer to the same query be identical every single time? Intuition says "yes" — zero randomness, always pick the most likely token, what could possibly go wrong.

And the intuition is almost right. Almost — because in engineering practice, "almost" costs money: tests that rely on bit-for-bit reproducibility at T=0 occasionally fail for no apparent reason, and the cause isn't in your code. Today we'll unpack where this "but no" comes from — along with a few more places where intuition about models holds nine times out of ten, and breaks in the tenth in a predictable, explainable way. We'll walk the inference pipeline from text to answer, and at every stage look at where intuition built from observation stops being a reliable map.
