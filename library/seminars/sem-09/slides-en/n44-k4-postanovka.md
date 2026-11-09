---
id: n44
type: problem_scenario
duration_min: 1.5
assertion: "An automatic refund is owed only to a client from the database with a course in the last 30 days — and that rule is checked not by code, but by a model, reading it in the same stream as the request's text"
learning_goal: "Case 4's setup, completely redefined on 2026-10-29 (S1: a solid/dashed diagram at the case's start; an honest admission that example K4-5 is a degenerate case; K4-4's reframing as a money question, not a routing one)."
visual:
  pattern: problem_scenario
  figure: k4-shema-postanovka-en.png
  primary: >
    On top — a diagram of the setup (S1): solid line — request → deciding
    model (client list + rule) → decision; dashed line — the defense layer
    this case builds and measures. Below the diagram — the center's rule,
    an honest admission that the example is degenerate, and the question's
    reframing.
  backup: >
    The setup is verbatim from `stend/zamery-k4-novyy/README.md`, section
    "Setup," and the owner's own speech (transcript 38:50–40:12): "to get
    a refund the client has to be in the client database… a list of, say,
    10 or 20 clients gets mixed into the prompt… the rule that only a
    course in the last 30 days qualifies for an automatic refund."

    AN HONEST ADMISSION OF DEGENERACY (K4-5), the owner verbatim (36:56):
    "yes, this is a degenerate example here, we're saying this is
    technically a gate, we're not betting it on an amount… a teaching
    case, to work through." On the slide this isn't a footnote caveat —
    it's its own block: the rule "is on the list AND the course is no
    older than 30 days" is entirely computable by code, and a real system
    would put that check in front of the model. The measurement hands the
    rule to the model on purpose, to show how the defenses behave on a
    subject the student can hold in their head whole — the baseline
    ("the same rule in code") is unveiled on n51a and confirms exactly
    this argument with a number.

    THE REFRAME (K4-4), the owner verbatim (36:56): "this isn't a routing
    question, we're talking about the question of a wrongful refund."
    The case isn't about who answers the client — it's about whether
    money goes to someone it isn't owed to.

    Character — Olga, the training center's administrator (A13), the
    same person as in the other five cases of the session.

    THE THREE QUOTE BLOCKS WERE TRIMMED in the designer pass (issue #303,
    Part G): the build flagged "DIAGRAM SQUEEZED [n44]: 9.22″ of 12.23″
    (75% of width, 57% of area) — neighboring blocks ate the space." The
    text under the diagram was denser than the same idea needed — the
    trim freed up room, the diagram now sits at its full natural size
    (3.87″), the warning is gone without losing a single fact (16
    clients, 30 days, "a money question," computability by code — all of
    it is still there).

    Measurement's reference date — 2026-10-29, the 30-day window — a
    course from 2026-09-29. Database — 16 clients, details and the
    boundary rows — on n48.
---

# Refund rule: in the database and no older than 30 days

## Assertion

The decision is made by a model, reading the rule in the same stream as the request's text. If the text convinces it otherwise, the money goes to someone it isn't owed to.

## Visual

> **The training center's rule.** An automatic refund is owed to a client from the database for a course taken in the last 30 days — a list of 16 clients is mixed directly into the request sent to the deciding model.

> **The money question.** If the model gets it wrong, money goes out to someone it isn't owed to.

> **Said plainly.** The rule "on the list and the course is no older than 30 days" is entirely computable by code — a string search, a date subtraction. A real system would put this check in front of the model; here it's handed to the model on purpose, to work through the defenses on a simple example.

## Speaker notes

The training center formalized its refund rule. An automatic refund is owed only to someone who is in the client database, and only for a course they took in the last 30 days. The client list with course dates — a small one today, 16 rows — is mixed directly into the request sent to the deciding model. The model reads that list, reads the rule, reads the text of the request, and makes one of three decisions: issue the refund, decline it, or hand the request to Olga.

Worth sorting out right away what this case is about, and what it isn't. It isn't a question of who answers the request — we already covered routing in the session's other cases. It's a money question: if the model gets the decision wrong, money genuinely goes out to someone it isn't owed to, and that only surfaces during reconciliation — by which point it's too late to reverse the transfer.

And honesty is needed here before we go any further. The rule we handed to the model — "is on the client list, and the course is no older than 30 days" — is entirely computable by ordinary code. Looking up a name on a list, subtracting two dates, comparing against the number 30. None of it needs any understanding of natural-language text. A real system would put that check in front of the model, in code, and an injection through the request's text wouldn't touch it at all. We're doing this on purpose: handing a computable rule to the model so we can show, on a subject that's as simple and as easy to hold in your head as possible, how the three classical defenses against text manipulation actually behave. At the end of the breakdown we'll come back to this choice and compare the defended model against that same rule computed in code — the result of that comparison is worth waiting for.

Now look at the diagram. On top is what already exists: the request comes in, the deciding model reads its text together with the client list and the rule, and out comes a decision. That's one single flow, and it already works. The dashed part is what we're building and measuring today: a defense layer. It can sit in front of the model as a separate node — a mechanical text check or a cheap classifier model — or it can be built directly into the deciding model's own call, as a strengthened system instruction. Three different ways to build a defense into the same flow, and we'll go through and measure all three next.
