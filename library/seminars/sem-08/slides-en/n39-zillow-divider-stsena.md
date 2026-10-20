---
id: n39
type: section_divider_macro
duration_min: 2.0
assertion: "Zillow shut down its algorithmic home-buying business and wrote off hundreds of millions of dollars — the same ungated decision threshold as in the 'Refund Approval' case, just at the scale of an entire company"
learning_goal: "EN mirror of the third wave (BRIEF-PROIZVODSTVO.md §0/§4): Zillow written up as a full business case, not a shortened filler. Divider and scene stay merged into one screen (carried over from the previous wave), but the business context — what iBuying is and how Zillow Offers worked — is now explicit on screen, not only in the notes. The CEO quote leads."
visual:
  pattern: section_divider_macro
  primary: >
    A dark macro-divider. The CEO's quote large, in quotation marks, the
    attribution underneath. Below it — a short business context: what iBuying
    is and how Zillow Offers worked, plus a table-strip of five numeric tiles.
    No case track on this screen — Zillow sits outside the case track.
  backup: >
    Numbers checked word for word against SETKA-KEYSOV-S8-part2.md, section
    "Концептуальный разбавитель — Zillow", and library/lectures/lec-05/
    chapter-part3.md §5.4 — unchanged from the previous wave. The business
    context (the iBuying paragraph) is new text from this wave, per the
    brief's own §4 requirement ("business context: what iBuying is, how it
    worked"), drawn from the same SETKA part2 section, with no details added
    beyond the source.
---

# Zillow Offers: algorithmic home buying

## Assertion

The company's own CEO announces the shutdown of an entire line of business and a write-off of hundreds of millions of dollars — at the same ungated decision threshold we just examined on a single customer refund.

## Visual

> "We've determined that the unpredictability in forecasting home prices far exceeds what we expected… the error rate we observed turned out to be far more volatile than we ever thought possible."
> — Rich Barton, CEO of Zillow, November 2, 2021, announcing the shutdown of the Zillow Offers business

> Zillow is the largest real-estate listings aggregator in the US. Since 2018 the company ran a line of business called Zillow Offers, also known as iBuying: the algorithmic Zestimate model priced a home from public data, the company bought it almost instantly at that price, did minimal repairs, and resold it quickly — earning on the spread between the purchase and the sale.

> Inventory write-down — **$304.4 million** for Q3 2021, $407.9 million for the full year. Workforce cut — **~25%, about 2,000 people**. In that same quarter Zillow bought **9,680** homes and managed to sell only **3,032** — the average loss per home sold came to **~$80,000**.

## Speaker notes

This quote belongs not to an analyst but to the company's own CEO, announcing the shutdown of an entire line of business himself.

Zillow is the largest real-estate listings aggregator in the US, and since 2018 the company had a separate line of business, Zillow Offers, also called iBuying. It worked simply: the algorithmic Zestimate model priced a home from public data, the company bought the home almost instantly at that price, did minimal repairs, and resold it quickly, earning on the spread between the purchase and the sale. The scheme worked for as long as the housing market behaved the way the model, trained on historical data, assumed it would.

In the fall of 2021, Zillow announced it was shutting the business down entirely. The numbers on screen are not journalists' estimates but direct figures from its SEC filings: the write-down on home inventory came to $304.4 million for a single quarter and $407.9 million for the full year, the workforce was cut by roughly a quarter, about two thousand people. In the third quarter of 2021 alone, the company bought 9,680 homes and managed to sell only 3,032 — the average loss per home sold came to about $80,000.

We take up this case right after "Refund Approval" on purpose. There, the rule about the refund-amount threshold lived in the prompt's text, not in the code's condition, and the model bypassed it in a measured share of runs — right at the edge of that condition. At Zillow the shape of the gap was the same: the risk threshold above which it would have been worth halting the automatic purchase or handing the decision to a person existed not as a mandatory condition in the loop, but as an expectation that the model would manage, because it had managed before. The only difference is scale: there, it's one conversation with a customer; here, it's buying a house with real money, and thousands of such decisions were made in a row.

On the next screen is a diagram of how that loop was actually built: without a mandatory gate and without a short checking interval. And the question we'll ask after it isn't whether the market's volatility could have been predicted in advance. It's about what was missing from the decision loop itself.
