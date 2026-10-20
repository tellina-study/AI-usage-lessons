---
id: n41
type: question_with_option_cards
duration_min: 1.0
assertion: "The model was calibrated correctly, yet the decision was bypassed thousands of times in a row — the question is what was missing from the loop, not from the model itself"
learning_goal: "Zillow's question: bare action cards, no arguments or verdicts (canon §5). The cards are a design choice, not a claim about the model."
visual:
  pattern: question_with_option_cards
  primary: >
    The question in a gold frame, four equal-width cards underneath, no
    explanations and no highlighted correct option.
  backup: >
    Cards are a literal rendering of SETKA-KEYSOV-S8-part2.md, section
    "Zillow", with no rephrasing. All four are actions that could be built
    into the decision loop (or explicitly are not such an action — the
    fourth card), not claims about the model's properties.
---

# What was missing from Zillow's decision loop

## Assertion

The model was calibrated correctly. The decision still bypassed the rule thousands of times in a row. The question isn't about the model — it's about what surrounds it.

## Visual

> **What was missing from the decision loop?**

`calibrate the model more precisely` · `set up runtime drift monitoring with an automatic stop threshold` · `tie the purchase decision above a given risk amount to a specific human underwriter` · `know in advance that the housing market would behave unpredictably`

## Speaker notes

We just saw the diagram: valuation, purchase with no mandatory gate, the error visible only from the quarterly report. The question is what should have been in that loop and wasn't.

Zillow Offers bought homes by algorithmic valuation and resold them. The model priced the home, the purchase decision was made almost automatically, and this happened thousands of times in a row, for as long as the market behaved as usual. When the housing market in 2021 turned out more volatile than history had assumed, the model's error rate jumped sharply, and the decision loop failed to catch it in time.

The question: what was missing from the decision loop?

Four cards. The first comes back to the accuracy of the algorithm itself — calibrate the model more precisely. The second is about watching the model in real time rather than once a quarter: set up runtime drift monitoring with an automatic stop threshold. The third is about who ultimately answers for a decision with a large stake: tie a purchase above a given risk amount to a specific human underwriter. The fourth is about the market itself, not the decision loop: know in advance that the housing market would behave unpredictably.

Notice that all four cards sound like reasonable engineering steps, and that's deliberate: the point isn't to tell a silly option apart from three serious ones, but to work out which one actually changes the decision loop and which one only rephrases what was already there. Resist guessing from the wording which option is the "odd one out."

Fifteen seconds to choose, then we vote by raising hands.

One more thing to consider before voting. All four options sit on the same diagram we just saw: valuation, purchase, execution, no checking interval, quarterly report. Don't think abstractly about "what sounds reasonable" — think concretely about which of the four options would add a new node or a new stopping point to that diagram, and which would just rephrase what's already drawn on it. A card that only restates a step already on the diagram, in slightly different words, is not the one that closes the gap.
