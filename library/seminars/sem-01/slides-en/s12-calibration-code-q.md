---
id: s12
type: comparison
duration_min: 1.3
assertion: "Who wrote it — code: AI or human?"
learning_goal: "Calibration 3/5 — code, focused on the measurable payoff"
learning_outcomes: []
references: [requests-library-psf]
visual:
  pattern: two_code_voting_cards
  primary: "2 code-block Ocean rounded box cards (monospace font): a real function from the requests library + an AI-generated equivalent"
---

# Who wrote it — code: AI or human?

## Assertion

Who wrote it — code: AI or human?

## Visual

Round-2: removed the "hand+camera" voting badge and the AI/human pill buttons
under the cards (we vote by raising hands, explained on s05) — the code cards
now take up the full height of the block. 2 Ocean rounded box cards with a
monospace font (JetBrains Mono / Courier New fallback), dark code-block
background. Code A:

```python
def prepare_method(self, method):
    """Prepares the given HTTP method."""
    self.method = method
    if self.method is not None:
        self.method = to_native_string(self.method.upper())
```

Code B: an AI-generated small function of a similar scope (for example,
normalizing an HTTP header name).

## Speaker notes

The third category — code. Two small functions, roughly the same scale. Let's vote: which was written by a human, which by AI.

Here too, it's not just about authorship: what's the measurable difference in productivity between "get a function from AI" and "use a proven library"? We'll discuss this in the reveal.

After the vote, ask: what tipped you off — the variable-naming style, the docstring, the structure of the conditional check?
