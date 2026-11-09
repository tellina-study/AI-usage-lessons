---
id: n29
type: case_divider_quote
duration_min: 0.5
assertion: "The model composes the answer, and it is also the only one who reads it before it is sent"
learning_goal: "Case 3 divider. Text form — QUESTION (BRIEF §4a: every case in the session gets its own divider form, rule P3). Names the problem (A2), gives away no measured result."
visual:
  pattern: case_divider_quote
  primary: >
    Dark background, the question large across two lines. Below it, the
    six-case track of the session, the third one highlighted.
  backup: >
    The "question" form was assigned to this divider by BRIEF-PRODUCTION
    §4a: the forms "scene," "number," "quote," "contrast," and "stakes" went
    to the other five cases, so six dividers in a row don't read in one
    grammar (illness §4.1 No. 7, rule P3).

    The setup follows SETKA-KEYSOV-S9.md, section "Case 3," "Input form" and
    "Setup": the answer goes out to the requester right after the model has
    written it.

    What's deliberately NOT shown: not a single measured number. Not "0 of
    6," not "5 of 5," not three verdicts on one text — all of that lives in
    beats n37 and n38. A divider that gave away the outcome would zero out
    both the question and the breakdown (BRIEF §4a).

    The case's name — "Checking the Answer" — by function, matching the
    case track in `rendered/deck-config.yaml` (`case_track`). The
    alternative "you can't trust a judge model" was rejected: the case's
    name must not let anyone guess how it ends.
---

# Case 3. Checking the Answer

## Assertion

The model composes the answer — and it is also the only one who reads it before it is sent.

## Visual

> The answer goes out to the requester the moment the model has written it. Let's put a check in place before it's sent — and if the checker is also a model, who checks the checker?

## Speaker notes

The process has learned to decide whether to answer at all, and to put that decision into a field code can verify. But nothing has been said yet about the text of the answer itself. It's composed by the model and goes out to the person exactly as it was born: nobody opens it between those two events.

The training center does have requirements for a text like this, and they're the usual ones for a short reply to a client: not too long, to the point, nothing extra. What exactly belongs on that list — we'll break it down point by point on the next screen. One thing is worth naming right now: the answer has to be entirely in Russian — that sounds like a minor detail right up until the moment a fragment of Chinese characters turned up in the middle of a Russian text, in the previous case.

Checking all of this by eye is Olga's job, and that's exactly the job the process is supposed to free her from. So the check has to go inside the process. And that's where the fork appears that this whole case is about: the check can be written in code, or it can be handed to a model — the same one, or a second one. The second option looks more attractive: code has to be written and then maintained, while a model just needs to be told, in words, what counts as a good answer — the same words you'd use to explain it to a person.

Which is where the question that opens the case — and the one it closes with — comes from. If the checker is also a model, how is it different from the generator? It composes text the same way, it can be wrong the same way, and it isn't obligated to be wrong the same way twice in a row. A check exists so you can lean on it. You can lean on something that behaves predictably. Next we'll build both on the real rig, run them on the same questions, and see which of the two checkers deserves the trust it's given up front.
