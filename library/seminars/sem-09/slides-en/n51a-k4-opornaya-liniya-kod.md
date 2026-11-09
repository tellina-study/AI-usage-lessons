---
id: n51a
type: measured_outcome_table
duration_min: 1.5
assertion: "The same rule, computed by ordinary code, gets 64 correct decisions out of 64 and not a single model call; the best defended model gets 53 out of 64 at 65 calls"
learning_goal: "The baseline required by the Baseline/Counterfactual Mandate for the case's main finding: a computable rule shouldn't be decided by a model at all. Directly tied to the AI-Failure & Judgment Content Rule — when AI isn't the right tool."
visual:
  pattern: measured_outcome_table
  primary: >
    Two tiles side by side: "the rule in code — 64 of 64, 0 calls" and
    "the best defended model — 53 of 64, 65 calls." Below them, one line
    about what the code can't do, and one about what that means for the
    choice of tool.
  backup: >
    Numbers — `stend/zamery-k4-novyy/README.md`, section "Baseline — the
    same rule, computed by code": function `gate_v_kode` in `svod.py`,
    a name lookup on the list plus a date subtraction, no model in it
    at all.

    THE CAVEAT, mandatory to show (honesty about the code itself, not
    only the model): the name match is character-for-character, and a
    client who wrote "Smith, J." instead of their full name would be
    rejected by this gate. The corpus has no variant-spelling cases — this
    is an untested spot in the code, not a proven reliability.

    Ties to CLAUDE.md § AI-Failure & Judgment Content Rule: this is
    exactly the "AI isn't needed here" example — the task is entirely
    computable, and the right engineering choice isn't "defend the model
    against injection," it's "don't hand the model something it never
    needed to be handed."
---

# Baseline: the same rule in code

## Assertion

Ordinary code on this same rule doesn't err once and doesn't make a single model call.

## Visual

> **The rule in code: 64 of 64 correct decisions, 0 model calls.** A name lookup on the client list plus subtracting two dates — exactly the same rule we handed to the model.

> **Best defended model: 53 of 64, 65 calls.** Three classical defenses, eight configurations, and even the best of them doesn't reach what a dozen lines of ordinary code deliver.

> **The code's own caveat, told honestly too.** The name match in the code is character-for-character: a client who wrote their surname with initials instead of a full name would be rejected by this code. This is an untested spot, not a proven reliability.

## Speaker notes

This finding has a direct baseline, and we're obligated to show it, not just say "code would have been better."

The rule we handed to the model for the whole case — "the client is on the list and their course is no older than thirty days" — is entirely computable. Look up the surname on the client list, take the course date, subtract it from today's date, compare against thirty. This was computed directly, without a single call to any model: ordinary code on this same corpus of 64 requests gives 64 correct decisions. Not one error. Not one model call, and therefore not a kopeck spent on calls and not a second of latency.

Set that next to the best result from the defended model — 53 out of 64 at 65 calls. Eight configurations, three classical defenses, hundreds of model decisions — and the best outcome falls short of a dozen lines of ordinary code.

That doesn't mean code is smarter than a model in general. The code has its own weakness here, and it has to be named just as plainly: the name match runs character-for-character, and a client who wrote "Smith, J." in their request instead of their full name would be rejected by this code as nonexistent. We didn't test this on the corpus — there are no variant spellings of a name in it, and this is an honest untested spot, not a proven reliability.

But the point of the comparison isn't that the code is flawless. The point is that a task that's entirely computable, with no need to understand natural language, shouldn't be handed to a language model at all. The three defenses we went through today lower the cost of that mistake — but the right engineering choice sits one step earlier than any of them: don't defend the model against injection where the model never belonged in the first place.
