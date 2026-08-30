---
id: s27
type: assertion_visual
section: "Section 5. Recommendations"
duration_min: 3
assertion: "Hybrid = composition (most industrial systems); filter bubble — a narrowing of diversity without malicious intent; dynamic pricing — fairness is a constraint, not a variable"
learning_goal: "INTRODUCTION FROM SCRATCH: hybrid + filter bubble + dynamic pricing; Amazon/Netflix historical estimate (fact discipline)"
chapter_ref: "§5.2, §5.3, §5.4"
visual_brief: "Left — hybrid + 2 readable stat cards Amazon ~35% / Netflix ~75% (instead of the invisible c27-bar; explicit caveat «historical McKinsey estimate, as a number not a graph-fact»). Right — filter bubble + dynamic pricing. Gold — «filter bubble without malicious intent». Footer — caveat."
interaction: none
verify_day_of: false
---

# Visible content

## Title bar
A hybrid softens the weaknesses — but without explicit diversity it does not cancel the bubble.

## Body
[Left — Ocean rounded box]

**Hybrid recommender**
collaborative + content-based + context (time, device, session). The content part closes cold-start, the collaborative part breaks over-specialization. Not a «third algorithm» — an engineering composition of the first two. **Most industrial systems are hybrids.**

[c27 — Amazon ~35% / Netflix ~75% bar chart]

[Right — Ocean rounded box]

**Filter bubble**
showed the similar → the user interacts with the similar → the model learns to show even more similar. A narrowing of diversity — **not malicious intent, but a consequence of optimizing for short-term relevance**.

**Dynamic pricing**
automatic adjustment of price to demand/time/context. The perception of fairness and the law are **constraints of the task, and NOT optimizable variables**.

[Gold callout, bottom]
A filter bubble arises without any intent — a direct consequence of «guess what you'll buy now». A hybrid does NOT automatically cancel this narrowing.

[Footer]
*Amazon ~35% / Netflix ~75% — a historically cited estimate (traces back to McKinsey ~2013), NOT a fresh verified metric; Ozon/WB — the companies do not disclose the exact share.*

## Speaker notes

The third approach — a hybrid recommender system. Most real industrial systems are hybrids: a collaborative and a content part plus context such as time, device, session history, combined so that the strengths of one compensate for the weaknesses of the other. The content part closes cold-start, the collaborative part breaks over-specialization. This is not a third separate algorithm but an engineering composition of the first two for a specific product.

Let us introduce from scratch two pathology-concepts. The filter bubble is an effect in which a recommender system, optimizing relevance to already manifested preferences, narrows the diversity of what the user sees: the model shows the similar, the user interacts with the similar, the model learns to show even more similar. This is not malicious intent but a direct consequence of optimizing for short-term relevance. Dynamic pricing is the automatic adjustment of price to demand, time, competitor, context. Let us fix the engineering-and-ethical boundary right away: the perception of price fairness and regulatory constraints are constraints of the task, not optimizable variables; an attempt to optimize price head-on, ignoring them, is the classic error «proxy instead of goal».

And separately — with the fact-checking discipline that the previous section taught. It is widely cited that around thirty-five percent of Amazon's revenue comes from recommendations, and about seventy-five percent of Netflix's views. These figures must be presented correctly: they are historically cited classic estimates, both tracing back to one source around 2013, not fresh verified metrics. Using them as a current fact today is exactly the error the previous section warned against. In Russia Ozon and Wildberries actively use recommendations, but the specific share of revenue from them could not be confirmed against a primary source — so the Amazon figure cannot be transferred here; the correct wording: recommendations are a key driver of conversion, the companies do not disclose the exact share.
