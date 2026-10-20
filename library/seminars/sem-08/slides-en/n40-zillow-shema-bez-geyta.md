---
id: n40
type: mechanism_node_graph
duration_min: 1.0
assertion: "The algorithmic valuation decided on the purchase with no mandatory gate and no short monitoring period — the error became visible only in quarterly SEC filings, a historical archive, not a control period"
learning_goal: "Zillow's no-gate decision diagram — layer 1, system-neutral (canon §2), the same device as the 'with LLM / without LLM' diagram in the 'Notifications' case, at a different scale. Short caption under the figure, no prose retelling of the diagram's content (BRIEF-PROIZVODSTVO.md §2) — the full unpacking lives in the notes."
visual:
  pattern: mechanism_node_graph
  figure: zillow-shema-bez-geyta-en.png
  primary: >
    A one-row diagram: Zestimate → purchase with no gate above the risk
    threshold → no monitoring period → the error is visible only in the
    quarterly report.
  backup: >
    EN mirror of the figure, generated from the same script
    (make_figures_zillow.py --lang en) via the fig_strings_en.py dictionary,
    the established pattern from sem-06. Content is a direct unpacking of
    "Схема решения, как оно работало" from SETKA-KEYSOV-S8-part2.md, section
    "Zillow", with no details added.
---

# How the buying decision actually worked

## Assertion

No mandatory gate stood between the valuation and the purchase, and no short checking interval stood between the purchase and discovering the error.

## Visual

> Zestimate (algorithmic valuation) → purchase decision with **no mandatory gate** above the risk threshold → the purchase executes → **no short accuracy-monitoring period** (hours to days) → the error accumulates unnoticed → visible only in the quarterly SEC filing.

## Speaker notes

The diagram on screen is the same device we already used to compare how the decision was built in the "Notifications" case: there, one row showed the chain with an LLM node, the other without it. Here, one row shows how Zillow's actual loop for deciding to buy a home was built.

The first step is the algorithmic Zestimate valuation: the model names a home's price from public data. The second step is the purchase decision, and here is the first gap: the decision was made with no mandatory gate above a given risk threshold. Any valuation, no matter how far it strayed from a reasonable range, moved on through the loop with no mandatory stop.

The third step is the purchase executing: the money goes out, the home becomes a company asset. And here is the second gap, a costlier one: after the purchase there was no short accuracy-monitoring period — hours or days in which one could notice that the actual resale price was systematically diverging from the forecast. No such period existed at all.

Because of this, the error wasn't caught right away — it accumulated unnoticed, purchase after purchase, quarter after quarter. The only point where it became visible was the quarterly SEC filing — that is, a historical archive that confirms what happened, not a control period that could have stopped it.

The difference between an archive and a control period isn't a stylistic nuance. An archive tells the truth only after the cost of the error has already been realized. A control period could have halted buying in a segment while the loss was still small. Zillow had only the archive.

On the next two screens are the question and the breakdown, and after that — a diagram of the same loop, but with the gate that was missing here.

Notice that not one of the five steps on this diagram looks like a mistake on its own. Pricing from public data is standard practice. Buying at the computed price is standard practice. Minimal repairs and a quick resale are standard practice too. The mistake isn't in any single step — it's that between the steps there's no point where the process could stop and ask, "is this valuation actually reliable right now?" That exact missing stopping point is what we'll go looking for in the next breakdown.
