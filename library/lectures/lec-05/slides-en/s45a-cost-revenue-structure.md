---
id: s45a
type: assertion_visual
section: "Section 6. Governance"
duration_min: 2.5
assertion: "Cost splits by type — people, hardware, model calls — and that split has been measured; a breakdown by feature is something few have, and a decision about a feature needs both, including the line that cannot be closed"
learning_goal: "The structure of cost and revenue in two cuts — by type and by feature — and the mechanics of a decision about a single feature, together with the boundary beyond which the decision is not taken"
learning_outcomes: [LO1, LO2, LO6]
chapter_ref: "§6.1 + §6.1a (the token arithmetic stayed in the chapter)"
verify_day_of: true
partial_out_strict_in: true
interaction: none
protected: true
note: >
  issue #212, edit following owner remark 2 ("slide 46: remake it out of this format into an
  ordinary presentation slide and show, from some research, the structure of costs and
  revenues broken down both by type (people, hardware, AI) and by feature/module, + ideally
  show how introducing one feature grows revenue and another grows cost and we take a
  decision, but with some caveat and an example of a loss-making feature you cannot give up").
  The slide has been TAKEN OUT OF THE PRACTICE-CARD FORM (it was WHAT IT IS / HOW IT WORKS /
  WITH AI AND WITHOUT / WHERE IT BREAKS) and assembled as an ordinary presentation slide: two
  cuts of the structure side by side. Its previous content — the token arithmetic, routing a
  request to a cheap model, the 15x of a multi-agent scheme — stayed in the chapter, §6.1a; on
  the slides its only trace is the counter on the chart on s45.
  RECONCILED (issue #212, 2026-10-01), point by point against the earlier discrepancy:
  (1) the file was renamed to s45a-cost-revenue-structure.md — the name describes the content,
  and the word "practice" was dropped because the slide is out of the card form; the reference
  in deck-part2.yaml was corrected, and the old name was checked by grep across the repository
  and remains nowhere; (2) deck-part2.yaml was brought into line with the frontmatter: type
  assertion_visual, and the slide is no longer counted among the cards of one form; (3) the
  tally of the band was corrected — eleven cards plus this slide.
  REMAINS WITH THE ORCHESTRATOR: (4) the ICONIQ, CloudZero and EU AI Act sources are not yet
  listed in the chapter and need back-filling into §6.1.
  Editorial rule: the "not X, but Y" turn is not used in the new text (tools/editorial).
meme_or_visual: >
  assertion_visual, two cuts side by side. On the left, "by type": two horizontal stacked bars
  one under the other — before launch and at scale — five shares in colour, labelled with a
  legend; beneath them a line about revenue and gross margin. On the right, "by feature": a
  table of four rows (feature / revenue / cost / decision), the fourth row in gold — the one
  that cannot be closed. At the bottom, in gold, the caveat with the example of a compulsory
  loss-making feature.
source: "ICONIQ Capital — State of AI 2026 (approximately 305 executives, Q2 2026); CloudZero (June 2026, n=260); the EU AI Act, articles 12 and 19"
---

# Visible content

## Title bar
The structure of cost and revenue: by type it is measured, by feature you do it yourself

## Body

**BY TYPE — WHAT HAS BEEN MEASURED**
*shares of what a product costs: before launch → at scale*

[Two stacked bars: "before the product launches" 32 · 20 · 16 · 6 · 26 and "at scale" 26 · 23 · 17 · 6 · 28]

- **people** — 32% → 26%
- **model calls** — 20% → 23%
- **hardware and cloud** — around 17%, unchanged
- **data storage and processing** — 6%
- **everything else** — model training, regulatory compliance

*ICONIQ Capital, State of AI 2026: around 305 executives of companies that build products with AI, a survey of the second quarter of 2026. The first four shares come from the report; the last one closes the sum to 100%*

On the revenue side: model calls eat around **23% of revenue**. Gross margin on products with AI was **45%** in 2025, and **53%** is expected for 2026; on a classic software product it holds above 70%.

**BY FEATURE — AND HOW THE DECISION IS TAKEN**
*worked through on the illustrative numbers of one catalogue: a breakdown like this is something few can build*

| Feature | Revenue | Cost | Decision |
|---|---|---|---|
| Suggestions in catalogue search | +8% to paid orders | +₽0.9 per query | we expand it |
| An AI agent on the first line of support | 0 directly | −40% of the agent's time per ticket | we keep it: it pays in savings |
| Review summaries on the product card | within the margin of error | +₽1.4 per view | we close it |
| **A decision log and a way out to a human** | 0 | constant, grows with volume | **cannot be closed** |

*Every number in this breakdown stands against one baseline: the same catalogue without that feature, over the same month. A breakdown by feature is something few can build: 22% of finance leaders can connect AI spend to money, and 60% agree that they spend more on AI than they can justify — CloudZero, June 2026, 260 respondents, more than half of them chief financial officers*

[Gold callout]
A caveat: a loss-making line cannot always be closed. A decision log and a way out to a human are required for a high-risk system by the EU AI Act: from 2 August 2026 events are recorded automatically, and the logs are kept for no less than six months. Revenue zero, cost constant, switching it off not allowed. The same class — a feature that loses money on its own line and holds revenue on somebody else's: the free tier, support, data export.

## Speaker notes

Now the structure: where the money goes and where it comes from. Two cuts, and in quality they are not comparable.

The first is by type, and it has been measured. ICONIQ this year surveyed around three hundred and five executives of companies that build products with artificial intelligence. Before launch the largest share goes on people — thirty-two percent; on model calls, twenty. At scale the picture shifts: people fall to twenty-six, model calls rise to twenty-three. Hardware and cloud hold at around seventeen and barely move; data storage and processing, six.

Look at the character of that shift. People are an almost constant cost: the team is the same whatever the number of users. Model calls tick with volume. As the product grows, the share of predictable cost falls and the share that depends on load rises — exactly the mechanics you saw as steps on the previous slide.

On the revenue side: model calls eat around twenty-three percent of revenue. Gross margin on products with artificial intelligence was forty-five percent in the year twenty twenty-five, and for twenty twenty-six fifty-three is expected. On a classic software product it holds above seventy. The gap is narrowing, but it is there.

The second cut is by feature, and here let me be honest: almost nobody has a breakdown like this. CloudZero in June surveyed two hundred and sixty finance leaders, more than half of them chief financial officers. Twenty-two percent can connect AI spend to money. Sixty agreed with the statement "we spend more on AI than we can justify with a measurable result".

That is why the table on the right is worked through on illustrative numbers, and every number in it stands against one baseline: the same catalogue without that feature, over the same month. Suggestions in search grow paid orders and cost ninety kopeks per query: we expand it. Review summaries move nothing and cost a rouble forty per view: we close it. The agent in support brings in no revenue at all and pays for itself with the agent time it saves.

And the fourth row is the one the caveat is here for. A decision log and a way out to a human: revenue zero, cost constant, closing it is not allowed. Since August of this year that is a requirement of the EU AI Act for a high-risk system. The same class — the free tier and support: loss-making on their own line, holding revenue on somebody else's.
