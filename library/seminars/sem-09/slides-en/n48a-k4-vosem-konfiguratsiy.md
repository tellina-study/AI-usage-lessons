---
id: n48a
type: test_structure_table
duration_min: 1.0
assertion: "Each defense is tested alone, in pairs, and all three together — eight configurations on one and the same corpus, with a no-defense baseline for comparison"
learning_goal: "Beat 1 of the measurement's exposition (C2), continued: the measurement's design. Eight configurations — a separate rig canvas for each, not a flag inside one process. No results on this frame."
visual:
  pattern: test_structure_table
  primary: >
    A four-step ladder diagram: no defenses → one defense (three
    variants) → a pair of defenses (three variants) → all three.
  backup: >
    The design — the owner, verbatim (42:17): "each of the three options
    separately… and then their combination by twos and all three… the
    tools separately, in pairs and what comes of that, and all together."
    Source — `stend/zamery-k4-novyy/README.md`, section "Design — doubled."

    The `0` baseline isn't directly named in the owner's own brief —
    it's added because without it the other seven have nothing to
    compare against (Baseline / Counterfactual Mandate, CLAUDE.md).

    Eight SEPARATE scenarios on the rig, not one process with switches —
    the owner's own justification (41:47, "a canvas per decision"): a
    canvas that physically has no mechanical-check node is an honest
    picture of the "no mechanical check" configuration.

    512 decisions (8 configurations × 64 requests) — a number for the
    next beat, here it already appears on the slide as the plan's size,
    not as a result: there isn't a single figure on this screen about
    what came out of it.
---

# Eight configurations: alone, in pairs, all three

## Assertion

Three defenses, eight ways to turn them on — from "nothing at all" to "all three together" — and each way gets its own canvas on the rig.

## Visual

> **The measurement's design.** Each defense is tested on its own (`p`, `r`, `c`), then all three pairs (`pr`, `pc`, `rc`), then all three together (`prc`) — plus a no-defense baseline (`0`) for comparison. Eight configurations on the same corpus of 64 requests — **512 decisions**.

| Step | Configurations |
|---|---|
| no defense | `0` |
| one defense | `p` — prompt · `r` — mechanical check · `c` — classifier |
| a pair of defenses | `pr` · `pc` · `rc` |
| all three | `prc` |

> **Before we look at the result — a prediction.** Of the three defenses covered on the previous frame, which one stops the most attacks on its own? The answer is on the next frame, as a number.

## Speaker notes

The measurement's design is doubled, exactly the way the course owner put it: test each defense on its own, then every combination of them by twos, then all three together. Eight configurations come out of a straight enumeration: a no-defense baseline, the three defenses alone, the three possible pairs, and one triple.

The no-defense baseline wasn't part of the direct request — it's added because without it the other seven configurations have nothing to compare against. A number with no baseline doesn't read, and here the baseline is exactly "what happens with no defense at all."

Eight configurations means eight separate canvases on the rig, each with its own set of nodes. The configuration with no mechanical check has no mechanical-check node on its canvas at all — the canvas is built without it. This is more honest than a toggle: a toggle can sit in the wrong position unnoticed, a missing node is visible at once.

Each of the eight configurations runs the whole corpus — all 64 requests. Eight times sixty-four is five hundred and twelve decisions. This number can already be named — it's about the size of the plan, not the outcome: how many decisions we're about to get, not what turned up in them.

Worth also saying what's not in this plan. There's no repeat of any single request within one configuration — each request runs through each configuration exactly once. That's a deliberate choice in favor of coverage: better to go through 64 different wordings once each than ten wordings ten times apiece. The stability of the answer itself is a separate question, and it gets its own check further along in the breakdown too — for a less than obvious reason.

Before we look at what came out — a prediction. We've already gone through the three defenses: prompt reinforcement, the mechanical check, the classifier at the entry. Which one do you think stops the most attacks on its own? Hold your answer in your head — we'll check it against the number on the next frame.
