---
id: n47
type: measured_outcome_table
duration_min: 1.0
assertion: "Two models from two different families — the deciding model and a filter cheaper and weaker than it — both named and configured here, before a single result number"
learning_goal: "The owner's strict rule C5: wherever there's a model, its name and settings are stated — both in the implementation and in the results. A dedicated beat, not a line inside another slide, so the name doesn't get lost among the numbers."
visual:
  pattern: measured_outcome_table
  primary: >
    Two model cards side by side — the deciding model and the filter —
    each with a name, three call settings, and a price per million
    tokens. Below them, a line on why the filter is taken from a
    different family of models.
  backup: >
    Numbers and names — verbatim from `stend/zamery-k4-novyy/README.md`,
    section "Models and settings"; the same figures — `korpus...sborka.py`
    (constants `MODEL_RESHENIE`, `MODEL_KLASSIFIKATOR`, `TEMP_*`,
    `MAX_TOKENS_*`).

    The deciding model — `qwen/qwen-2.5-7b-instruct`, temperature 0, a
    300-token answer limit, $0.10 / $0.20 per million tokens in/out. The
    same model as Cases 1, 2, and 5 of this session — Case 4's numbers
    are comparable to theirs exactly because of this.

    The filter — `meta-llama/llama-3.1-8b-instruct`, temperature 0, a
    120-token answer limit, $0.05 / $0.08 per million tokens. Taken from
    a DIFFERENT model family and half the price of the deciding model —
    the justification on the slide: a guard of the same breed as the
    model it guards tends to trip over the same things.

    Both models are called through the rig's own `OpenRouter account`
    credential, via an HTTP Request node to
    `POST https://openrouter.ai/api/v1/chat/completions`. Prices were
    checked against `GET /api/v1/models` on the day of the run.
---

# Models and settings of the measurement

## Assertion

The deciding model is the same one used by three other cases in the session. The filter is from a different model family and half its price.

## Visual

> **The deciding model — `qwen/qwen-2.5-7b-instruct`.** Temperature 0, a 300-token answer limit, $0.10 / $0.20 per million tokens (in/out). The same model as Cases 1, 2, and 5 of this session.

> **The entry filter — `meta-llama/llama-3.1-8b-instruct`.** Temperature 0, a 120-token answer limit, $0.05 / $0.08 per million tokens. Taken from a different family and half the price of the deciding model.

> **Why the filter isn't from the same family.** A guard of the same breed as the model it guards tends to trip over the same things — this assumption is checked further on, against the measurement's result, not taken on faith.

## Speaker notes

Before we look at the results, let's name the models outright — this session's rule has no exceptions: wherever a model sits in a diagram, its name and its settings appear on the slide, both in the description of the device and right next to the result numbers.

The deciding model is the one that reads the request, the client list, and the rule, and makes the final decision: refund, decline, or manager. It's `qwen-2.5-7b-instruct`, called at temperature 0 with a 300-token answer limit. The very same model that Cases 1, 2, and 5 of this session run on — and that's not an accident: Case 4's numbers can be set alongside those cases' numbers precisely because the model underneath is one and the same.

The entry filter is the model the classifier defense calls, before the deciding model ever sees the request. It's `llama-3.1-8b-instruct`, also at temperature 0, but with a shorter answer — 120 tokens, it only needs to say "yes" or "no." And its price per million tokens is half the deciding model's.

Worth saying why the filter is taken from a different model family while the deciding model stays in its own. The logic is simple: if a guard is built the same way as the model it's guarding, they share the same blind spots — a technique that fools one is likely to fool the other too. A different model family is an attempt to split those blind spots at least by architecture, with no guarantee it works. How well that attempt actually held up in practice, we'll see next: the filter has its own separate story, and it isn't the most convincing one.

Both models are called through the same single channel on the rig — an HTTP request to OpenRouter, billed the same way — and from here on these two names will keep appearing next to every results table in the deck: not named once here and forgotten.
