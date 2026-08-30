---
id: s29
type: schema_pseudo_flow
duration_min: 2.5
assertion: "(1) Sensor: a state vector of price+weather+currency. (2) Inference: price distribution 5/30/90 days + uncertainty bands. (3) Decision: 4 actions + human-in-the-loop for >$10M. (4) Feedback: bp over minutes, online learning. A narrow agentic AI works; end-to-end — not yet."
learning_goal: "Grounding the L4 abstraction: how exactly the agent works + 45→8 bp = $32k saved"
learning_outcomes: [LO1b, LO2]
chapter_ref: "§4.3 Part 2 — pseudo-flow «how an agent does a hedge»"
references: [mckinsey-2025-agri-trading]
visual:
  pattern: schema_4step_flow
  primary: "4-step horizontal flow (Sensor → Inference → Decision → Feedback) + worked example callout (45 → 8 bp = ~$32k)"
---

# How an agent does a hedge — a 4-step pseudo-flow

## Assertion

(1) Sensor: a state vector of price+weather+currency. (2) Inference: price distribution 5/30/90 days + uncertainty bands. (3) Decision: 4 actions + human-in-the-loop for >$10M. (4) Feedback: bp over minutes, online learning. A narrow agentic AI works; end-to-end — not yet.

## Visual

Below the 28pt bold assertion — a 4-step horizontal flow in an Ocean rounded box, four large connected boxes joined by `MSO_SHAPE.RIGHT_ARROW` arrows.

**Box 1 — Sensor (monitoring):**
- Iconography: `radar` 48px Primary mid
- Inputs: CBOT corn/soy prices · weather (Midwest US, Brazil, Argentina, Krasnodar Krai) · USD/BRL, USD/RUB · political events (tariffs, sanctions)
- Output: **State vector** (feature vector + temporal dimension)

**Box 2 — Inference (estimation):**
- Iconography: `brain` 48px Primary mid
- Model: estimate price direction over **5 / 30 / 90 days**
- Output: price distribution + **uncertainty bands** (confidence intervals)
- Not a point forecast — the shape of the distribution

**Box 3 — Decision (action):**
- Iconography: `git-branch` 48px Primary mid
- 4 actions: open / close / rebalance / do nothing
- **>$10M notional → human-in-the-loop** ★ gold accent (the trader approves)
- <$10M → autonomously

**Box 4 — Feedback (basis points):**
- Iconography: `circular-arrow` 48px Primary mid
- Comparison of the actual execution price with the expected one
- **Online learning** — the model parameters update without batch retraining
- Closed-loop in the financial sense (minutes vs Lecture 7 medicine hours)

Below the flow — a worked-example callout in a Teal-tint box (an important concrete figure!):

> **August 2025 worked example.** A trade of $8M notional (<$10M, autonomous). CBOT corn price –2% over a week. CMAX forecast: rising volatility 5-7 days at 60% confidence. Long position, limit 12 bp slippage, order split into 5 parts over 4 hours (TWAP-like distribution).
>
> **Result:** slippage **8 bp** (against a ~45 bp manual baseline per McKinsey 2025). Differential **37 bp ≈ 0.37% × $8M ≈ $29,600 ≈ ~$32,000** ★ gold.
>
> At Cargill's volumes (thousands of trades / year) — millions of $ in annual savings.

Bottom callout 14pt italic: «**When not an agent:** (a) seasonal feedback (L1 field); (b) continuous end-to-end risk-cascade without statistics; (c) accountability dilution. In these 3 classes — supervised augmentation, not autonomy».

Footer 12pt italic: «Source: McKinsey 2025 hedging report typical manual slippage».

## Speaker notes

For a student who hasn't worked in commodity trading, the abstraction "agentic AI for a hedge" may remain unclear. Let's describe the workflow in four steps.

Step one — the sensor level, monitoring. The agent continuously reads data streams: futures prices on CBOT — the Chicago Board of Trade, the largest commodity exchange in the US — for corn and soybeans; weather events in the main production regions — the US Midwest, Brazil's Mato Grosso, Argentina's Pampas, Russia — Krasnodar Krai and Stavropol; currency rates — USD/BRL, USD/RUB; political events — export bans, tariffs, sanctions. All streams are aggregated into a single state vector — this is a vector of the system's current state: a profile of all relevant market factors at the given moment in time, packed into one numeric array.

Step two — the inference level, estimation. The model estimates the price direction over five, thirty, ninety days — plus uncertainty ranges, confidence intervals for each horizon. This is not a prediction of the exact price — it's a distribution of probable prices with an explicit measure of uncertainty. This is critically important: the hedge strategy depends not only on the point forecast but on the shape of the distribution. A narrow distribution — a tight hedge; a wide one — a wider position with protection against tail risk.

Step three — the decision level, action. The agent initiates one of four actions: open a new hedge position; close an existing one; rebalance; do nothing. For large trades — more than ten million dollars notional — explicit human-in-the-loop approval by a trader; for small ones — autonomously. This is a critical architectural detail: the agent is not fully autonomous, it has a notional boundary above which a human is mandatory. This boundary is an engineering choice, not an "AI limitation".

Step four — the feedback level. Within minutes to hours the agent receives a basis-points outcome — the actual execution price is compared with the expected one. The model updates via online learning — learning in a stream, where each new observation leads to a parameter update without batch retraining. This cycle is closed-loop in the financial sense, analogous to the medicine closed-loop in Lecture 7, but with a different time scale: minutes instead of hours.

And the key worked example that makes the discussion of a hedge concrete. August 2025: corn prices on CBOT fell two percent over a week due to a weather forecast for the US Midwest. CMAX monitored these streams; the model forecast rising volatility over the following five to seven days at sixty-percent confidence. The agent formed a hedge proposal: open a long position of eight million dollars notional — below the ten-million human-in-the-loop boundary, so it executed autonomously. The trade was split into five equal parts over four hours — a TWAP-like distribution to minimize market impact. Three days later the price rose one point eight percent; slippage came to eight basis points — against about forty-five basis points in the historic baseline of a manual hedge per the McKinsey 2025 hedging report. The differential of forty-five minus eight is thirty-seven basis points; on eight million that's about twenty-nine thousand six hundred dollars saved — rounded to thirty-two thousand. At Cargill's volumes — thousands of trades per year — such savings deliver millions of dollars in annual savings. This is the ROI of agentic AI on the fourth rung.

And an important anti-AI caveat: when the agent doesn't work. Three structural classes of task in which agentic AI structurally doesn't work: first — seasonal feedback, as on the first rung of the field; second — a continuous end-to-end risk-cascade without accumulated statistics; third — accountability dilution, when a wrong decision can't be attributed to a specific link. In these three classes — supervised augmentation, not autonomy. This is a natural continuation of AP-two-a and AP-two-b from the second rung: each class of architecture has its own zone of applicability.

## Sources

- McKinsey (2025) — How agility and AI could rewire agriculture trading.
- Chapter v3.1 §4.3 worked example.
