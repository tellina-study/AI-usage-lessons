---
id: s07
type: process
duration_min: 4
assertion: "70 years of AI: discoveries, winters, the 2017 turning point"
learning_goal: "A compressed AI timeline; the AI Effect through examples"
learning_outcomes: [LO1]
references: [vaswani-2017-attention, mccorduck-2004, dhar-2024-paradigms]
visual:
  pattern: horizontal_timeline_grouped_panels
  primary: "3 full-width tinted panels (Ocean light/mid/deep tint) with a group «tab» badge on top instead of a left text column; a timeline on each panel + a gold pill/oval badge on 2017 + a Vaswani callout (8 authors, self-attention, 160K+ citations)"
---

# 70 years of AI: discoveries, winters, the 2017 turning point

## Assertion

70 years of AI: discoveries, winters, the 2017 turning point.

## Visual

**Redesign issue #155 Round 2 (owner comment #176)** — replaces the former layout
«3 lines + a left text column with a range of years» (which duplicated the years
already shown as dots on the line). New layout: each of the 3 groups sits on
its own full-width tinted Ocean panel (light/mid/deep tint
background, growing in intensity toward 2017 — visually reinforcing the narrative
of approaching the turning point). The group name — white bold text in a
rounded «tab» badge in the group's color, «riding astride» the top edge of the
panel (not a separate column on the left, no duplication of years). 3 key
events on the line inside each panel: «Discoveries» (Turing 1950 — the test for
thinking, ELIZA 1966 — Weizenbaum, expert systems 1980s); «Winters and
breakthroughs» (1st winter 1974 — the Lighthill report, Deep Blue 1997 — 200M pos/sec,
AlexNet 2012 — GPU + DL); «Turning point and explosion» (Vaswani 2017 ★, ChatGPT 2022 —
1M in 5 days, DeepSeek R1/Claude Code 2025–26). All labels are on one line
(em-dash separator), rendered in English (Turing rather than Imitation Game
per the owner's explicit request; Weizenbaum/Lighthill — standard English
spellings, aligned with the wording in this slide's speaker notes).
«Attention Is All You Need» is left verbatim — the exact title of the paper in
quotes, a legitimate citation, not an anglicism.

The 2017 turning point — a large gold pill (1.35"×0.44", DEEP text 22pt) +
a gold oval over the line, read together as a single badge/pin marker —
the most prominent element of the slide. **WCAG fix found during the visual
loop:** gold TEXT COLOR on a light tint background gives ~1.6:1 contrast (fail
WCAG AA); in this palette gold works only as a FILL with dark text
on top (~6.9:1) — so both the ordinary and the pivot event labels are now DEEP,
not gold-colored, and the «wow» effect comes from the shape (pill+oval), not from text color.

The callout at the bottom — a Vaswani deep-dive (unchanged): 8 co-authors (Vaswani,
Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin) introduced
self-attention; as of May 2026 the paper has over 160,000 citations. Additional
events (1956 Dartmouth, the XCON/MYCIN expert systems, MCP 2024)
are covered by voice, not shown on the axis, for readability.

5 iterations of Generate→Convert→Inspect→Fix, with 3 substantially different
compositions tried (full trace — `rendered/iteration-log-issue155.md`,
the «s07 Round-2 redesign» section):
(a) a thin full-width panel + a left colored accent bar + a pill badge inside
the panel on the left; (b) an `ocean_box` card with an explicit outline + the group heading
as separate text at the top-left (which created empty «dead» space
between the heading and the line); (c)/(d) a compact panel + a tab badge
«riding astride» the top edge — chosen as the final one: the most
distinctive composition («a real gem», not banal), a clear separation of the 3 eras
by panel color, no duplication of years.

## Speaker notes

The history of AI as an engineering discipline is about seventy years. To keep twenty factoids from blurring together, let's split the chronology into three thematic groups.

The first group — discoveries and the first practice, from the fifties to the eighties. In nineteen fifty, Turing publishes his paper on the imitation game. In fifty-six — the Dartmouth conference, where McCarthy, Minsky, Rochester, and Shannon introduce the very term «artificial intelligence». In sixty-six — Weizenbaum creates ELIZA, a simple psychotherapist program, and discovers that users ascribe understanding to it. In the eighties — the commercial boom of expert systems: the rule-based systems XCON, MYCIN, and the Japanese «Fifth Generation» project.

The second group — winters and breakthroughs, from the seventies to the early tens. The first winter, after the Lighthill report to the British government and cuts in DARPA funding. The second — the collapse of the market for specialized AI machines from Symbolics in the late eighties. And the breakthroughs between the winters: in ninety-seven, IBM's Deep Blue defeats Kasparov, evaluating two hundred million positions per second. In twelve — AlexNet wins ImageNet, proving that deep convolutional networks trained on GPUs beat hand-crafted features.

The third group — the turning point and the explosion. In seventeen, Vaswani and seven co-authors publish «Attention Is All You Need», introducing the Transformer architecture. As of May 2026, the paper has more than one hundred sixty thousand citations on Google Scholar. In twenty-two — OpenAI launches ChatGPT; a million users in five days. In twenty-four through twenty-six — the explosive growth of reasoning models and agentic systems.

The two winters matter as a methodological lesson. When promises fail to materialize en masse, the field loses resources. Today's wave is the fourth in AI's history. So far it avoids a winter because some of the promises really are being fulfilled. But history teaches us: not all of them will be, and an engineer must be able to tell what already works now from what is promised for the thirties.
