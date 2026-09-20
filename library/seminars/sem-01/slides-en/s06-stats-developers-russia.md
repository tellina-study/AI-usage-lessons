---
id: s06
type: assertion_visual
duration_min: 11
assertion: "Used more, trusted less — and that's not a paradox"
learning_goal: "Stack Overflow 2025 + VCIOM as the first two independent data points; the comparison with the audience's own numbers is delivered verbally (speaker notes), without separate visible live cards on the slide"
learning_outcomes: []
references: [stackoverflow-developer-survey-2025, vciom-neiroseti-2025-2026]
visual:
  pattern: triple_bignumber_usage_tools_trust
  primary: "Round-4 (comment #247): unreadable bar charts removed, replaced with 3 big-number Ocean cards — USAGE (84%, 76%→84%), WHAT THEY USE (ChatGPT 82% / Copilot 68% / Gemini 47% / Claude 41% — mini bars) and TRUST (29%, was 40%, 46% don't trust it, 3% fully trust it). At the bottom — a gold strip 'Russia · VCIOM 2026': 78% over the year (was 73%), 58% weekly (was 51%), 64% believe it's beneficial. Sources: SO Dev Survey 2025 (N=49,009) + VCIOM."
  round4_note: "comment #247 — 'the text is completely unreadable, replace the charts with big numbers'; fresh data checked online (SO 2025/2026: 84% use, 29% trust, tool breakdown; VCIOM 2026)"
  charts_removed: [assets/charts/s06-stackoverflow-v2.png, assets/charts/s06-vciom-v2.png]
---

# Used more, trusted less — and that's not a paradox

## Assertion

Used more, trusted less — and that's not a paradox.

## Visual

Point-fix rebuild (the course owner hand-edited the charts after round-2; the
current render — 2 full-height Ocean rounded box panels side by side, filling
the entire content area of the slide; the bottom strip with 4 live poll cards
("Your audience"), present in the round-2 version, has been removed from the
final render — the "fill in the numbers verbally" mechanic remains only in the
speaker notes, with no separate visible cards on this slide).

Panel 1 — Stack Overflow Developer Survey 2025 (MID bold headline). Inside: a
horizontal bar chart (`s06-stackoverflow-v2.png`) on the left — "use or plan to
use AI": 76%→84% (+8 pp, 2024→2025), "trust the accuracy of the output":
40%→29% (−11 pp). To the right of the chart — a text block: "76% → 84%
(+8 pp)" in large type; "40% → 29% (−11 pp) · 46% explicitly distrust the
accuracy (was 31%) · 3% fully trust it"; a small-print methodology line
"N=33,244 (67.8% of the sample) · among developers with 10+ years, 'somewhat/
highly distrust' is 47% vs 37% for newcomers with 1–5 years." At the bottom of
the panel — a source line: "Stack Overflow · self-selected online sample."

Panel 2 — VCIOM, "Neural Networks in Our Lives" (MID bold headline). Inside: a
bar chart (`s06-vciom-v2.png`) on the left — 2025 vs 2026 ("used it over the
past year" 73%→78%, "at least once a week" 51%→58%). On the right — an Ocean
rounded box callout: "2026: 64% believe AI is beneficial · 67% — only in
certain areas" (small, bold) above "Over the year: 73% → 78% (+5 pp)" and
"Weekly: 51% → 58% (+7 pp)" (larger, bold); a methodology line "N=3,209, 18+,
25–27.06.2026 · ≤±1.7%." At the bottom of the panel — a source line: "VCIOM ·
a representative sample of Russians."

## Speaker notes

The first source — the Stack Overflow Developer Survey 2025. Eighty-four percent of developers use or plan to use AI tools in development — up from seventy-six percent in 2024. At the same time, only twenty-nine percent trust the accuracy of what AI produces — down from forty percent a year earlier.

How is that possible — using a tool more, but trusting it less? It's not a paradox: the tool is used as a draft that always gets checked — a sign of mature use. An important methodological detail: this is a self-selected online survey — the respondents are people who came to the Stack Overflow site themselves, so the audience skews toward English-speaking developers.

The second source — VCIOM, "Neural Networks in Our Lives." In 2025, seventy-three percent of Russians had used neural networks over the past year, and fifty-one percent at least once a week; the 2026 figures grew to seventy-eight and fifty-eight percent. VCIOM surveys Russians in general, not just an engineering student audience.

The bottom strip — your own numbers from the poll a minute ago, across all four questions. Fill in (verbally, out loud, I'll write it on the slide or record it on the board) the results: which AI tool was named most often, how often the group uses AI, the average trust score on the 1–5 scale, and how many people raised a hand for "AI let me down." How does your group compare with the two outside sources — higher or lower on trust, using it more or less often?
