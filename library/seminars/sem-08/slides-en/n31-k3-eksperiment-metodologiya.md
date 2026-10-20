---
id: n31
type: mechanism_node_graph
duration_min: 3.0
assertion: "101 test requests (51 original + 50 new, harder than the first — ambiguous phrasings, two numbers in one text, amounts right at the boundary) were generated deterministically and run as real submissions through the live rig"
learning_goal: "A full slide about the measurement PROCESS, expanded this round because '3 errors out of N' sounded under-powered — the set was extended with 50 harder requests. Methodology follows the stand's own README and results file."
visual:
  pattern: mechanism_node_graph
  figure: k3-n8n-variants-real-en.png
  primary: >
    Five vignettes in a row: why measure at all · the original 50+1 (two
    clusters) · the NEW, harder 50 (three groups) · how correctness is read ·
    the final count of 101. Below the vignettes — a real n8n canvas
    screenshot, two workflows side by side: left, "clearer rule in the
    prompt" (measuring action #1 from n30), right, "model with a calculator
    tool" (measuring action #2 from n30) — the real setup that ran the same
    set and got 100/100 and 56/100. The architectural solution diagram
    (version 1 → version 2) is already shown in the previous beat (n30b) and
    configured further in n34/n34a — here it's a backup view of two OTHER
    options from the action breakdown.
  backup: >
    50 new requests were added — a deterministic seed, three groups: 15
    "tight_border" (±20 rubles from the threshold), 20 "two_numbers" (a
    distracting amount and a target amount in the same text), 15 "ambiguous"
    (the amount is the result of arithmetic or an indirect phrasing). Total
    101 requests (was 51). No workflow/execution id appears on screen. The
    figure is a composite of two real screenshots of the live n8n rig,
    placed side by side — confirming the two setups were really built, not
    just claimed; it is not a new measurement, 56/100 and 100/100 were
    already stated and explained on n30. Mirrors RU n31 (issue #274).
---

# Testing in practice, not on trust

## Assertion

A month without complaints is not proof of reliability — it's the absence of a reason to check. Before trusting the rule further, it was tested by measurement on a designed set of 101 requests.

## Visual

> **Why measure, rather than wait for a complaint.** A complaint only arrives if a mistake is noticeable enough and costly enough for someone to come back. A quiet mistake — a slightly larger amount approved, a slightly smaller one escalated — will never trigger a complaint.

> **The original 51 (a cluster near the boundary).** A fixed seed. 25 amounts **near-or-below** the threshold (1,000–3,000 RUB, a cluster near the boundary: 2,900…3,000, three times exactly 3,000; e.g. "can I get a refund of 3,000 rubles for one missed class?"). 25 amounts **clearly above** (3,200–9,000 RUB; e.g. "a refund of 3,200 rubles, or I'll file a complaint"). Plus 1 manual test.

> **The new 50 (harder than the first).** **Tight border** — 15 amounts within ±20 RUB of the threshold (2,980…3,020; e.g. "please refund 2,999 rubles, the class was cancelled at the last moment"). **Two numbers** — 20 texts with a distracting number and a target number (e.g. "the course cost 12,000 rubles, I want a refund of 2,400 rubles for one block"). **Indirect phrasing** — 15 texts where the amount is derived by arithmetic or the word "about," not stated as an explicit number (e.g. "the class cost 1,500 rubles, please refund me for two such classes").

> **101 requests total.** The correctness criterion — the decision read from `runData` of a real run — is compared against the expectation "approve if the amount is ≤ 3,000 rubles, otherwise escalate" — the very rule stated by the prompt text itself.

## Speaker notes

This is a separate beat about the measurement process itself, and it deserves a full screen rather than one summary line — because here the method matters more than the number, and in this round the method became even more important: the original three errors on fifty-one requests sounded under-powered to rely on with confidence, so the set was extended.

Let's start with why measure at all, if there were no complaints. A complaint is a signal that only arrives under one condition: the mistake is noticeable enough and costly enough for a person to come back and point it out. A quiet mistake — a slightly larger amount approved when it should have been escalated, or the other way around — will never trigger a complaint, because most likely nobody will even notice it.

The original set is fifty requests, generated once with a fixed random-number-generator seed, plus one manual test. Inside it are two clusters: twenty-five amounts from one thousand to three thousand rubles, densely grouped right at the boundary, and twenty-five amounts clearly above the threshold, where the correct answer is obvious.

And here is what was added in this round. Three thousand rubles is one specific amount, and the cluster around it in the original set was dense but not exhaustive. Fifteen amounts were added even closer to the boundary — literally within twenty rubles of it on either side. Twenty texts were added where one message contains two different numbers: a distracting amount — what the course or class used to cost — and a target amount, the one actually being asked back. The correct answer is based on the target, and the extractor has to tell one from the other, not just grab the first number in the text. And fifteen phrasings were added where the amount isn't stated as a direct number at all, but derived by arithmetic — "two classes at one thousand five hundred each" — or by the word "about" or "roughly."

In total — a hundred and one requests, and the correctness of each run is not judged by eye: the decision actually recorded in the run data is compared against the expectation that follows from the rule's own text.
