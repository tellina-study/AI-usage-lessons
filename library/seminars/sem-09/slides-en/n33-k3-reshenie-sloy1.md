---
id: n33
type: mechanism_node_graph
duration_min: 1.0
assertion: "A check before sending is a loop with three mandatory parts: who decides, how many attempts, and what happens when the loop never converges"
learning_goal: "Layer 1 of the 'our solution' beat (case-design canon §2): an architecture with not a single node name and not a single tool name. Names both parts that get forgotten most often: the retry limit and the 'not converged' branch."
visual:
  pattern: mechanism_node_graph
  figure: k3-shema-tsikl-en.png
  primary: >
    A two-row schema, TWO sequential forks of identical shape (redrawn
    2026-10-29, owner edit): "Converged?" — yes, right to "Send to client,"
    no, down to "Limit exhausted?" — yes, right to "Hand to Olga," no, left
    to "Retry," which loops back to the generator. A separate banner states
    the limit: three attempts. Ocean palette, font size no smaller than
    7.5 pt.
  backup: >
    EN figure `k3-shema-tsikl-en.png`, generated for this EN track (issue
    #172/#319) — same layout as the RU `k3-shema-tsikl.png`, labels
    translated: "Converged?" / "Send to client" / "Limit exhausted?" / "Hand
    to Olga" / "Retry."

    The loop's design follows SETKA-KEYSOV-S9.md, section "Case 3,"
    subsection "Solution," layer 1, and `stend/zamery-k1-k3/README.md` (the
    code-check scenario: generator, checker, fork, up to three attempts, an
    explicit "not converged" branch).

    REDRAWN 2026-10-29 (issue #303). The owner read the earlier version
    (one T-shaped crossbar feeding both forks) as a "matrix," not a chain:
    "handing the client's send to Olga, it's at the bottom, that's turned
    into a matrix... let's close the chain instead: converged — yes, right,
    send to client; converged — no, down, limit exhausted — yes, right, to
    Olga; no, left, into a retry." The new figure is exactly this chain, two
    forks of mirrored shape ("yes" always goes right, an exit from the
    loop; "no" always goes to the next step). The text below is TRIMMED:
    what's now visible on the diagram itself (the straight path, the "not
    converged" branch, the limit) is not retold in prose — saying the same
    thing twice was eating space the figure didn't have to spare (THE
    SCHEMA WAS CRAMPED, 42% of the area before the fix).

    No node names, no orchestrator name, and no Latin script appear on the
    schema on purpose: canon §2 requires layer-1 wording that survives a
    change of tool. The real canvas and the real settings panel come on
    later screens, n34 and n35.

    About "anchors" from the grid. The grid describes a node that
    accumulates already-passed checks between attempts. On the rig this is
    done simpler and stricter: on every attempt, the checker re-checks ALL
    five requirements from scratch, so a retry can't fix one thing while
    quietly breaking another. The schema says exactly this — there's no
    separate accumulator node on the frame, because there isn't one on the
    rig either.

    A FINDING, FLAGGED TO THE ORCHESTRATOR AS A REPORT, not silently fixed:
    the figure `k3-shema-tsikl.png` already carries a measured number in
    its bottom banner ("an exact substring match wasn't enough to recognize
    a semantically correct answer in a different grammatical case — 1 case
    out of 6"). That's the result of beat n37 and the caveat of beat n42,
    and at the solution beat it stands earlier than the measurement has
    been presented. The visible text of this slide carries no number;
    removing it from the already-drawn figure is the orchestrator's call,
    not the slide author's (figures are outside this session's scope).
---

# The "write — check — retry" loop

## Assertion

A loop must have three things: who decides, how many attempts, and what happens when it never converges.

## Visual

> **A detail the schema doesn't show.** A retry re-checks **all five requirements again**, including the ones already passed — otherwise a second attempt can fix one thing while quietly breaking another.

> **What's still undecided here.** Who the checker is — code or a model — the schema doesn't say. The difference appears next, and it's measured.

## Speaker notes

Look at the design with not a single node name: if someone else builds this tomorrow with a different orchestrator, not one line here would change.

The forward path is simple. A question arrives, the generator writes an answer, the checker verifies the listed requirements, and a fork decides: good enough — it goes out to the client.

The path back is more interesting. If it's not good enough and attempts remain, the answer is written again, and the generator is told exactly what failed. Here's the important detail that's easy to lose: on the second attempt, all five requirements are checked again, including the ones that passed the first time. The reason is direct — a retry changes the whole text. Shorten the answer, and the model can easily drop the needed detail along with the extra length, and if you only check length, you'll accept a text that got worse on a different requirement.

The limit. Three attempts, and the counter is set by hand. This isn't excess caution: the loop doesn't stop on its own. It stops only when the checker says "good enough" — and if the checker is stubborn, or wrong, that might never happen at all.

And the "not converged" branch — the part people forget most often. Attempts run out, and the answer still hasn't passed the check. What then? The answer doesn't go to the client, the question is handed to Olga, and she answers by hand. Without this branch there are exactly two bad outcomes left: the process spins until someone stops it, or it sends the person a text it has already rejected itself.

Notice what the schema doesn't say. It says "the checker verifies the requirements" — and not a word about who that checker is. Code and a model look identical on it; both builds fit the same drawing. That's exactly why the choice between them isn't made from the schema. Next we'll build the real loop on the rig, open the checker's actual settings panel, and run both variants on the same six questions.
