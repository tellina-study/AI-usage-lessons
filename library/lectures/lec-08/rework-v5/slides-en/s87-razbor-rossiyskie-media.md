---
# Source: chapter/chapter-part3e.md §§ 5.10 and 5.20; REESTR-RAZBOROV-part3.md line 5.3.
# Second-step column — (a), and this breakdown is stronger than the previous one: both halves
# are measured by ONE method on ONE sample, not borrowed from a neighboring study.
# "Column (a)" is the registry's working language, not surfaced on the frame (form §6.3).
# The cumulative map is brought to the canonical form of BRIEF-DEKA.md §12. Here it is filled
# in for the last time: the fifth column, "Recognition" — after this, Wrap-up reads it.
grafa: "a — both classical modes counted in the same unit as the model, by one method on one sample"
id: s87
local_id: "s87"
section: "5. Recognition and Provenance"
type: analitika
title: "Breakdown: Russian media — 18% of articles carrying traces of generation"
assertion: "In the second quarter of 2026, signs of generation are present in 18 percent of articles from a sample of 254,610 pieces across 174 Russian outlets, and the counterfactual here is measured on the spot, not borrowed: in newsrooms with a share of machine-made articles above 20 percent, experts per thousand words fell by 22 percent against their own 2020–2022 level, while in newsrooms with almost no machine-made articles, the figure rose by 6 percent over the same period; what moved downstream was not text quality but the work of gathering evidence — a newsroom that switches to generation stops calling people"
source: "Kirill Pshinnik, co-founder of Zerocoder, published October 16, 2026"
chapter_ref: "chapter-part3e.md § 5.10"
media: "assets/charts/s87-dolya-statey-po-kvartalam.png"
media_needed: ""
media_note: "a chart built by the QuickChart service from the breakdown's own numbers: the quarterly series for the share of articles carrying traces of generation, 0.08 → 0.88 → 5.7 → 14 → 18 percent. A screenshot of the primary source could not be sourced — six tiers were gone through, details in images-log-s88-s97.md; a self-built series with a named denominator was used instead of decoration. No source caption on the frame"
# Overhaul of forms (#301, Section 5): `piktogrammy` was TRIED — the 18% share with an area
# denominator rather than a line. Built and measured: [height] s87/body — no room left
# (-1.82", "primitives ate the frame"). The frame already carries the quarterly series chart
# (media) + 2 counterfactual plates + visible text; the chart STAYS ("a frame keeps its
# illustration" rule) — it shows the TREND across quarters, which pictograms can't do (the
# form holds one share, not a series). Pictograms could only be added by dropping something
# already accepted (the −22%/+6% counterfactual, or the trend itself) — the overhaul does not
# do that, so `piktogrammy` is not placed on this frame: the frame is already full.
blocks:
  - {label: "Newsrooms with a share of machine-made articles above 20%", value: "experts per 1,000 words −22%", note: "against their own 2020–2022 level"}
  - {label: "Newsrooms with almost no machine-made articles", value: "+6% over the same period", note: "same corpus, same procedure, same years — this counterfactual is what makes the breakdown the strongest one", key: true}
blocks_per_row: 1
timing_min: 0.8
in_bucket: true
method_steps: ["①cost of both errors", "②both modes on one scale on one sample", "③the share curve", "④how it was measured", "⑤what moved downstream", "map"]
form: []
vfy: true
status: собран
---

## Visible slide text

**The unit — density of live evidence per thousand words.** Both halves obtained by one procedure on one corpus: 254,610 articles from 174 outlets, from 2020 through Q2 2026.

**Why 18% is a lower bound:** recognizers don't generalize to an unfamiliar model. Alongside: 13% growth in machine-like vocabulary among humans, and 27% of the corpus with partial signs.

## Speaker notes

The second case with both sides counted, and it's stronger than the previous one for one reason: both halves are measured by the same method on the same sample, not borrowed from a neighboring study with a different methodology.

The unit is the density of live evidence per thousand words. The cost of "publishing machine text" is measured: direct quotes are 2.1 times fewer, expert comments 2.6 times fewer, average length 773 words against 1,090. The cost of "not publishing on time" is absent, as in the previous breakdown: the throughput norm for a second-tier newsroom is not in the selection.

Both modes are counted on the same scale, on the same corpus. In newsrooms with a share of machine-made articles above twenty percent, experts per thousand words fell by twenty-two percent against their own 2020–2022 level. In newsrooms with almost no machine-made articles — up six percent over the same period. Both halves were obtained by the same procedure on the same corpus, so they can be placed side by side without rigging, and that is exactly what makes this the strongest breakdown in the whole lecture's cost layer: the counterfactual is measured right here, on the spot.

The share curve by year: zero through the end of 2022 — more precisely, from zero to eight hundredths of a percent, and these are false positives from the recognizers themselves; eight tenths of a percent at the end of 2023; five point seven at the end of 2024; fourteen at the end of 2025; eighteen in the second quarter of 2026. By outlet tier: federal outlets around ten percent, the second tier — topical, lifestyle, large regional — twenty-three to twenty-five, local and niche outlets seven point nine. By topic, home, food, and health are most affected; politics and breaking news least, no more than two point eight percent.

The methodology matters more than the result here — it's why this case was chosen. The sample is two hundred fifty-four thousand six hundred ten articles from one hundred seventy-four Russian outlets, from 2020 through the second quarter of 2026. The tool is two open recognizers; an article counts as machine-made at an average score of at least one half; with an additional cross-check by a third recognizer. The author is Kirill Pshinnik, co-founder of the online university Zerocoder, published on October 16, 2026.

The method's limitation has to be stated outright, all the more so because it was examined earlier in this same lecture through measurement: recognizers of generated content don't generalize to an unfamiliar model. Here this is softened by three recognizers and a large sample, but the absolute share still reads as a lower bound, not an exact value. And a nuance that changes the scale of the conclusion: thirteen percent growth in machine-like vocabulary in texts written by humans, and twenty-seven percent of the corpus with partial signs of generation, against eighteen percent fully machine-made. People are starting to write alike, and that influence is broader than the share of machine-made articles.

What moved downstream. The call to an expert moved: a newsroom that switches to generation stops calling. This is said with a number, not an estimate — quotes 2.1 times fewer, experts down twenty-two percent, while neighbors in the same sample over the same period are up six percent.

And the third half of the count, the one that's easy to lose. The cost of "publishing machine text" is measured in the same unit as everything else: direct quotes in such newsrooms' texts are 2.1 times fewer, expert comments 2.6 times fewer, average material length 773 words against 1,090. These are not stylistic observations: each of the three figures counts the presence in the text of live evidence — that is, exactly what the newsroom should have gone to a person for.

Breaking the sample down by outlet tier shows the share is unevenly distributed: around ten percent for federal outlets, twenty-three to twenty-five for the second tier, seven point nine for local and niche outlets. By topic, home, food, and health are most affected; politics and breaking news least — there, no more than two point eight percent. The higher the cost of an error in a topic, the less often a newsroom trusts it to a machine, and this distribution on its own reads as the industry's own risk assessment.

One more detail about the counting methodology is worth knowing. An article was counted as machine-made when the average score of two open recognizers was at least one half, with an additional cross-check by a third recognizer. This is a reasonable procedure, and it has exactly the same limit examined one frame earlier: a recognizer trained on one family of generators performs worse on an unfamiliar one. So eighteen percent is a lower bound, not an exact value.
