---
id: n46
type: answer_breakdown_table
duration_min: 1.5
assertion: "The three defenses pay differently: through an instruction with no extra calls, through calls removed, or through calls added — and the most expensive by far is the defense that calls the model twice"
learning_goal: "Breakdown right after the question (A1), the 4-column form 'action · how it works · advantage · drawbacks' (A5) plus a fifth column (C6, a numeric column). The numbers here are the architectural cost in model calls, measured on this same corpus; attack catch rates and honest errors come after the measurement's exposition (C2), in n50–n52."
visual:
  pattern: answer_breakdown_table
  primary: >
    A table: action · how it works · advantage · drawbacks · cost in
    model calls. Three rows, no verdict column — what holds and what
    doesn't is settled by the result beats further on.
  backup: >
    DESIGNER-PASS DECISION (issue #303, Part B): there is NO new "where
    each method sits in the pipeline" diagram on this frame — deliberately,
    not by omission. All three defenses in this table are already shown
    with their place in the flow on n44 (`k4-shema-postanovka.png`: three
    labeled cards — mechanical check, entry classifier, prompt
    reinforcement, each with a dashed arrow into the deciding model). A
    second diagram with the same three places on this frame would be
    cross-slide redundancy (anti-pattern §5.5,
    `tools/presentation-build/README.md`) — duplicating the visual two
    screens down with no new information.

    The breakdown's text is from `stend/zamery-k4-novyy/README.md`,
    section "Three defenses," and the owner's own speech.

    THE FIFTH COLUMN — per requirement C6 (`forma-keysa-s-zamerom.md`
    §12, collision 2: "a fifth column inside form A5, or a number as a
    tile next to the table" — resolved in favor of the column, pending
    an explicit owner decision). The numbers in it are an ARCHITECTURAL
    fact (how many times a configuration calls the model across the
    whole 64-request corpus), not a catch-rate result: this is
    deliberate, so as not to break C2 (test structure before results,
    beats n48–n48a come later). Source of the numbers — Table 1 of
    `stend/zamery-k4-novyy/README.md`: configuration `0` (no defenses) —
    64 calls to the deciding model; `p` (prompt reinforcement) — also 64,
    the prompt neither removes nor adds calls; `r` (the mechanical check)
    — 33, half the requests are stopped before the model; `c` (the
    classifier) — 123, the classifier is called on all 64 plus the
    deciding model on whatever it let through.

    Models and settings — to be named on the next frame (C5, n47); here
    is the defense's construction, not the call contract.
---

# Three defenses: how they're built and what they cost

## Assertion

Prompt reinforcement doesn't change the number of calls. The mechanical check removes half of the deciding model's calls. The classifier nearly doubles their number.

## Visual

| Action | How it works | Advantage | Drawbacks | Cost in model calls (64 requests) |
|---|---|---|---|---|
| **Prompt reinforcement** | the system part of the request declares the client's text data, the client list the only source of facts about course dates | adds no node, doesn't change the flow — only the content of the request to the same model | only protects what the instruction itself names; it reacts unevenly to overtly official-looking text (notes, format overrides) | **64** — the deciding model is called on every request, same as with no defense |
| **Mechanical check** | a code node in front of the model checks the request's text against a set of templates for known techniques; a match — the request goes to the manager, the model is never called | stops a request before the model ever sees it — and removes a call | only catches a technique expressed as recognizable phrasing; a technique expressed through meaning with no telltale words slips past | **33** — the model isn't called on requests already stopped by the mechanical check |
| **Classifier model at the entry** | a separate, cheap call to a different model decides whether the text contains an attempt to influence; "yes" — the request goes to the manager without the deciding model | also closes the "cheap model at the entry, straight to the manager" option with one decision | the classifier is called on ALL 64 requests, and the deciding model on everything it let through; the cost grows, it doesn't fall | **123** — nearly twice as many as with no defense at all |

## Speaker notes

The three defenses are built differently, and the difference already shows in how they change the number of model calls on the same corpus of 64 requests — before we even look at what each one catches.

Prompt reinforcement doesn't touch the flow at all. It's a change to the text of the system part of the request: the deciding model gets called exactly as it would with no defense, 64 times on 64 requests. The advantage is in its simplicity — not one new node, not one new setting. The drawback is that the defense only works where its own instruction directly names the technique: how it holds up against different wordings of the same manipulation, we'll see next, on the measurement's results.

The mechanical check changes the flow noticeably. A code node steps in front of the deciding model and checks the request's text against a set of templates — telltale phrasings of known techniques. A match — the request goes straight to the manager, the deciding model never even sees it. On our corpus this drops its number of calls from 64 to 33: half of the requests are stopped earlier. The cost of that saving is paid in who the request goes to — a separate conversation, further on, on the measurement's results. The technique's own drawback: it catches phrasing, not meaning — a wording with no recognizable words will slip past the template.

The classifier model at the entry is the most expensive of the three by construction alone. It's called on all 64 requests without exception, and the deciding model on everything the classifier didn't flag as suspicious. That's 123 calls in total instead of 64: a defense meant to lower risk here increases the cost nearly twofold. This is exactly the answer to the "cheap model at the entry, straight to the manager" question — it's cheap by model, not by the number of calls to a model at all.

What among this is worth what it costs — we'll see next. First let's name the models and their settings, then the structure of the test itself, and only after that — the result.
