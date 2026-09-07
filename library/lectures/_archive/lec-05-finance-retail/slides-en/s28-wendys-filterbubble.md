---
id: s28
type: case_study
section: "Section 5. Recommendations"
duration_min: 3
assertion: "Recsys/pricing optimizes a proxy (click, margin), not the goal (trust); Wendy's surge-pricing backlash 02.2024 — fairness is a constraint; the failure is quiet"
learning_goal: "Filter bubble + Wendy's #G + criterion proxy ≠ goal (one class across the chapter); price discrimination (CQ return 5)"
chapter_ref: "§5.5"
visual_brief: "Left — the root proxy ≠ goal + the Wendy's case. Right — a counter-weight mini-diagram «why the failure is quiet» (proxy metric ↑ vs true goal → they diverge; dashboard green, trust falls) + a compact criterion. Gold — «proxy ≠ goal». (The right-side emptiness is removed.)"
interaction: think_pause
verify_day_of: false
---

# Visible content

## Title bar
The system reports success by its own metric — while destroying what did not make it into the metric.

## Body
[Left — Ocean rounded box, root]

**The root — proxy ≠ goal**
the system optimizes what is measurable in the moment (**proxy**: clicks, time, conversion, margin) ≠ the true goal (trust, well-being, diversity of choice). When the proxy diverges from the goal → **filter bubble, dark patterns, homogenization**.

**Case G — Wendy's, February 2024**
~$20 million into digital menu boards with dynamic pricing → the media read it as surge pricing → #BoycottWendys, a competitor beat it in an ad → rollback within days. Money invested, the technology available — what failed was **ignoring that perceived fairness = a constraint, not a variable**.

[Right — teal callout, criterion]
- a proxy metric ≠ the goal → build in **serendipity** (a deliberate share of the unexpected) + explainability + a discrimination audit
- pricing policy — a decision of a **human within a legal frame**, NOT the output of an optimizer

[Gold callout, bottom]
One class across the whole lecture: accuracy deception, scoring proxy bias, Klarna, filter bubble — **proxy ≠ goal**. The more powerful the optimizer, the more costly the divergence. The failure is quiet — the graphs rise, the harm accumulates.

## Speaker notes

The central question returns sharply for the fifth and last time. The failure of this AI type is subtler than the previous ones, and precisely for that reason it is easy to underestimate. The root — a proxy instead of the goal. A recommender system optimizes what is measurable in the moment: clicks, viewing time, conversion. But this is a proxy, not the true goal — the long-term value and well-being of the user, their trust, the diversity of choice. When the proxy diverges from the goal, the system honestly maximizes the proxy and gets pathologies: a filter bubble, dark patterns, homogenization.

The case — Wendy's, February 2024. The fast-food chain announced an investment of around twenty million dollars in digital menu boards with a dynamic-pricing capability. The media interpreted this as surge pricing — the price rises during peak hours, as with taxis; a public scandal erupted, a competitor beat it in an ad. Within a few days the company was forced to publicly roll back the wording. The money had been invested, the technology was available — what failed was not IT but the ignoring of the fact that the perception of price fairness is a constraint, not an optimizable variable. Technically, surge pricing is a solvable optimization task: the model maximizes revenue by adjusting price to demand. If you frame the task that way, the optimizer will honestly solve it — and lead to exactly what caused the boycott. The error is not in the model but in the framing: fairness and loyalty were implicitly discarded because they are poorly measurable.

Compare it with the filter bubble — the same mechanism: there the proxy is the click, the goal is long-term value; here the proxy is revenue per shift, the goal is trust in the brand over years. And in both cases the pathology does not look like a malfunction: the model works perfectly by its metric, the graphs rise, the failure is visible only if you look at what did not make it into the metric. This is one class of error across the whole lecture — deception by an accuracy metric, scoring proxy bias, Klarna, the bubble: the optimizer maximizes a proxy that diverges from the goal. The criterion: build in a deliberate share of unexpected recommendations and explainability, an audit for discrimination; pricing policy is a decision of a human within a legal frame. Think for thirty seconds: where in a service familiar to you have you noticed a bubble or an unfair price — and what was the proxy, and what was the goal?
