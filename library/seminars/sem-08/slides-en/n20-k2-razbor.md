---
id: n20
type: answer_breakdown_table
duration_min: 3.0
assertion: "Measured, not assumed: on 20 test pairs the classic vector approach (13/20) turned out worse than plain hashing (15/20), the cheap judge model scored 17/20, and the external service (jev) scored 20/20 with zero errors — and each scheme has its own price"
learning_goal: "A breakdown on a real measurement, not verdicts (canon §6 — a realistic contrast case: the classic vector approach is measured as a full candidate, not a strawman). The twist: a heavier non-language tool isn't just a non-improvement over hashing — it can be measurably worse; a narrow specialized service measurably beats the cheap judge model here — but one measurement on 20 pairs isn't reason enough to change an already-built and demonstrated architecture. A fifth column (cost and speed) was added, and the raw jev numbers were removed from the visible layer (2026-10-20 voice edit)."
visual:
  pattern: answer_breakdown_table
  figure: k2-n8n-test-stend-real.png
  primary: >
    A 4-row, 5-column table: scheme · correct out of 20 · what it caught ·
    what it missed · cost and speed. Below it — a condensed honest finding
    about the threshold and the best result. No raw jev numbers on the
    visible layer. Below the finding — a real screenshot of the live n8n
    rig, the test workflow: not an illustration of the point but the actual
    process these numbers were measured on (ADDED 2026-10-20, issue #274,
    owner's voice edit: "did you even look at the screenshots yourself? the
    last section has almost none, and not many in the others either").
    CHANGED in the same round: the intro line "20 test pairs: ..." was
    dropped from the visible layer (the slide's height budget doesn't fit
    intro + table + finding + figure at once — see backup), and the "Honest
    finding" was compressed by half. Neither edit loses facts: the test-set
    composition (10 duplicates, 10 different, close topics) already reads
    from the table's columns, and all three findings of the quote are kept,
    just shorter.
  backup: >
    The table and the finding are from SETKA-KEYSOV-S8.md, Case 2, section
    "Measurement Result". The numbers are final and real, re-measured
    2026-10-19 on a NEW set of 20 pairs (the original set from the first
    measurement wasn't preserved anywhere — the first pass's temporary
    workflow was deleted; this pass's generator and set are
    stend/_gen_duplicate_check_pairs.py and
    stend/duplicate-check-test-pairs.json, full log —
    stend/duplicate-check-results.json): hash 15/20, TF-IDF-cosine 13/20,
    LLM judge 17/20 — see BRIEF-PROIZVODSTVO.md §3. The fourth scheme (jev,
    TypeSafe Decisions API, endpoint POST
    https://openrouter.ai/api/alpha/decisions, model typesafe/jev-1.13) was
    measured 2026-10-20 on the same set of 20 pairs via the production
    workflow stage-2-duptest.json (id gs5uhluV74yu045D): 20/20,
    classification threshold 0.5 (jev_noul >= 0.5 => duplicate), a clean
    split — jev_noul 0.70–0.97 on all 10 duplicates, 0.02–0.08 on all 10
    different questions (the raw numbers were removed from the visible layer
    and from the notes per the 2026-10-20 voice edit — "unclear to the
    viewer without context" — and are kept only here, replaced on the
    visible layer with the wording "a clean split, no overlap between
    duplicates and different questions"). The blocker previously described
    as a credential access restriction was a WRONG diagnosis: the actual
    cause was a plain authoring mistake on the node "Jev decision (noul)" —
    the credential wasn't attached in the workflow's node.credentials (the
    field was null), even though nodeCredentialType was set; fixed by the
    orchestrator via PUT /workflows/gs5uhluV74yu045D, with no need to touch
    the owner or their credential. The full log and the honest caveat about
    this being a single measurement — stend/duplicate-check-results.json,
    section jev_measured.

    The "Cost and speed" column is new (2026-10-20 voice edit). Hash and
    TF-IDF are pure mechanics with no model call — cost and latency are
    negligible by construction and weren't measured separately, because
    there's nothing to measure. The LLM judge (gpt-4o-mini) — public pricing
    from OpenAI's price list on the production date: $0.15 per 1M input
    tokens, $0.60 per 1M output tokens — an estimate from the public price
    list, NOT an exact fact about this test's specific runs (token count per
    call wasn't measured separately). jev — $0.042 per 1M input tokens, $0
    for output, OpenRouter Decisions API, model typesafe/jev-1.13 — the same
    caveat: an estimate from OpenRouter's public price list, not a measured
    fact about this run.

    RECALCULATED FOR THE CASE'S VOLUME (2026-10-20 voice edit, issue #274):
    the owner separately required that "the cost estimate for model calls
    must be given for our own case, not just the price list" — bare pricing
    without volume says nothing about the real budget. A strictly
    illustrative calculation, with explicit assumptions at every step:

    Volume — from n18 (`slides/n18-k2-stsena.md`): Olga estimates repeats at
    "about 10 times a day" — her own estimate, not measured statistics (the
    overall daily-request denominator isn't measured). This calculation's
    assumption: the expensive step fires on ALL of these ~10 daily cases (in
    practice part of them should be caught by the free hash step first — see
    n20/n21 — so this is a ceiling on spend, not a measured fact) → ≈300
    calls per month (10 × 30).

    Message length per call — NOT a measured fact, an illustrative
    assumption based on the typical message length in the test set
    (stend/duplicate-check-test-pairs.json, 40 texts, average length 39
    characters, range 26–66). The judge model's prompt — the verbatim text
    of the node "Same question, reworded? (LLM)" from stend/stage-2.json
    ("This is a new message: «...». A recent message from the same
    contact: «...». Is this the same question, just phrased differently?
    Answer strictly «yes» or «no».") without the two messages — 145
    characters; plus two messages at ~39 characters each — ≈223 characters
    per call in total. The jev request body (verbatim on n23: instructions
    185 characters, criteria.true 92, criteria.false 66, JSON structure
    model/keys/punctuation ≈80) without the two messages — ≈420 characters;
    plus two messages — ≈500 characters per call in total (the jev request
    is longer: it has an explicit instruction and both criteria, which the
    judge model's prompt doesn't).

    Characters → tokens — an illustrative assumption of ≈2 characters per
    token for Russian text (NOT a measured fact, a rough counting rule —
    this tokenizer specifically wasn't checked): the judge model ≈110 input
    tokens, a short output ("Да." / "Нет." — see llm_judge_raw in
    duplicate-check-results.json) ≈5 tokens; jev ≈250 input tokens, $0
    output by pricing (the Decisions API returns a probability, not text).

    Cost per call: judge model ≈110×$0.15/M + 5×$0.60/M ≈ $0.0000197; jev
    ≈250×$0.042/M ≈ $0.0000105. At ≈300 calls a month: judge model
    ≈$0.006/month, jev ≈$0.003/month — BOTH under a cent a month at this
    volume. The honest conclusion of this recalculation: the price
    difference between the two expensive schemes is practically
    unnoticeable in money here — at Olga's volume, what decides isn't call
    cost but accuracy (17/20 vs. 20/20). This doesn't cancel the
    per-million-token price comparison (it still shows which scheme is
    cheaper AT SCALE), but it directly answers the owner's question — "what
    does this mean for our case" — and for our case it means "under a cent
    a month, price isn't the argument".

    ADDED (2026-10-20 voice edit, issue #274, the owner after looking at the
    deck — "did you even look at the screenshots yourself? the last section
    has almost none, and not many in the others either"): the figure
    k2-n8n-test-stend-real.png is CONFIRMATORY (the fig_after device,
    deck-config.yaml, the same one used for n31 — drawn AFTER the table and
    the honest finding, not instead of them). Source — a real screenshot of
    the live n8n rig (Playwright, taken 2026-10-20,
    https://n8n.lessons.tellian.io, see notes/mcp-limitations.md [#233-8]),
    file stend/n8n-screenshots-raw/case2-test-4schemes.png (1900×1100), crop
    (230, 340, 1740, 810) → 1510×470, with no redrawing, assembled in
    rendered/make_figures_k2.py by the function test_stend_real(), saved as
    library/seminars/sem-08/rendered/figures/k2-n8n-test-stend-real.png.

    The frame shows the canvas of the workflow "C8 · Case 2 — dedup test
    (rig, 4 schemes)", the very test process these numbers in the table
    above were measured on (hash 15/20, TF-IDF 13/20, LLM judge 17/20, jev
    20/20). The text on the frame reads literally, line by line: the node
    Test pair (webhook) (trigger, output label POST) leads by two arrows —
    to the node Jev decision (noul) (type httpRequest, label POST:
    https://openrouter.ai/...) and to the node LLM judge (input Input 2,
    zigzag icon); a separate node Judge model is connected to LLM judge by a
    dashed line labeled Model (the mandatory model sub-node, a chat-model
    link type, not a direct data flow). Both nodes — Jev decision (noul) and
    LLM judge — converge on the node Combine (labeled combine, two labeled
    inputs Input 1 / Input 2), then Combine → Shape result (curly braces —
    a transform node) → Respond (returns the webhook response). Hash and
    TF-IDF are NOT drawn as nodes on this canvas — these two schemes don't
    call an external model and were computed by a local script
    (stend/_gen_duplicate_check_pairs.py + string/cosine comparison), not on
    the live rig; the canvas shows exactly the two nodes that actually call
    a model (the LLM judge and jev) — exactly what needed confirming with a
    screenshot, unlike hash and TF-IDF, which have nothing to screenshot.
    The crop cuts out the canvas header (the line with the workflow's
    name), the Published badge, the Editor/Executions/Evaluations tabs, the
    left column of app icons, the right floating zoom/search panel, the
    "Execute workflow" button, and the bottom Logs panel — there's no
    workflow/execution id anywhere on the final frame (canon §2–§3,
    tools/seminar-production/README.md).

    HEIGHT BUDGET (same round of edits): the slide was already at the
    ceiling — the 5-column table at 10.5 pt already took 2.79″ out of the
    allotted 2.81″ before the figure even entered (build.py, measured
    before the edit). With the figure (natural height ~3.81″ at the current
    crop), the sum of the four blocks' natural heights (intro line 1.08″ +
    table 3.81″ + finding 2.63″ + figure 3.81″ — DEBUG measurement from
    tools/seminar-build/roles.py:compose()) was four times the allotted
    5.89″, and proportional shrinking pushed the table below stage 2's
    floor (9 pt, 2.30″) — build.py returned OVERFLOW (×3) and PAST THE
    CANVAS EDGE (the composition ended at 7.42″ against a 7.50″ canvas
    height, with the bottom block not visible). The intro line "20 test
    pairs: ..." was dropped entirely (its facts — the 10/10 composition, 3
    close topics — are already duplicated in the table's columns, see the
    TF-IDF row "2 false positives on close topics"); the "Honest finding"
    was compressed from 3 expanded sentences to 3 compact ones — all three
    findings (TF-IDF doesn't save the threshold, jev beat the judge model,
    both paid schemes cost under a cent) are kept, at ~47% of the original
    text length. After both edits — no OVERFLOW and no PAST THE CANVAS
    EDGE: the table sits on stage 2's floor (9 pt, "AT THE FLOOR OF THE
    SIZE" — the device can't go lower, but the 2.29″ budget is practically
    equal to the needed 2.30″, within rendering tolerance) — the same level
    of compression already accepted on n46 of this same deck, not a new
    precedent. The render was checked visually (pdftoppm of page n20) and
    by the overlap checker (check_text_overlap_pdf.py — 0 overlaps on n20):
    the text doesn't run over, the table, the finding, and the figure all
    read in full, without cropping.
---

# What Each Scheme Caught

## Assertion

Before calling the model, we measured a more serious non-language alternative — instead of taking it on faith. The result on the same set of 20 pairs was unexpected: the classic vector approach (13 out of 20) is worse than plain hashing (15 out of 20), not on par with it, while the narrow specialized service scored 20 out of 20, with zero errors.

## Visual

| Scheme | Correct out of 20 | What it caught | What it missed / got wrong | Cost and speed |
|---|---|---|---|---|
| **Hash (exact match)** | **15/20** | all 5 repeats, all 10 different ones | all 5 rephrasings (0/5) | cheap and instant — no model call |
| **TF-IDF + cosine** (threshold 0.3) | **13/20** — worse than hash | repeats, some of the different questions | the same 5 rephrasings + 2 false positives on close topics (hash doesn't make this mistake) | cheap and instant — no model call |
| **Judge model** (gpt-4o-mini) | **17/20** | all 10 duplicates | 3 false positives, including a pair with no shared words | ~$0.15/M in · $0.60/M out — for the case (≈300/mo) ≈$0.006/mo (price-list estimate) |
| **jev service** | **20/20** | all 20, zero errors | clean split, no overlap | $0.042/M in, $0 out — for the case ≈$0.003/mo (price-list estimate) |

> **Honest finding.** TF-IDF misses every rephrasing, adds 2 false positives where hash never errs. jev scored best — accurate, cheap — but one 20-pair run can't justify replacing a working architecture. At this case's volume (≈10/day) both paid options cost under a cent a month: accuracy decides.

## Speaker notes

We're breaking down the five actions from the previous screen — on a measurement taken before deciding anything.

Exact match, action one, catches 15 out of the 20-pair set: all 5 literal repeats and all 10 deliberately different questions, but none of the 5 rephrasings — zero out of five. Cost and speed aren't counted separately here: it's string comparison, either free and instant or it isn't there at all.

Action two, the classic vector approach — TF-IDF plus cosine similarity, threshold 0.3 — looks more serious: a similarity measure, a tunable threshold, a realistic engineering choice, not a weak alternative for contrast. The result on the same set, the same method — 13 out of 20, worse than hash. The same five rephrasings are missed for the same reason: the Russian words for "payment" and "to pay" are different inflected forms of one verb, and the Russian words for "course" and "class" are different words for one meaning, and a word-based measure is blind to that in principle. But two false positives on a close topic got added — "a Python course" and "a data-analytics course" share almost all their words, and the 0.3 threshold counted them as the same question. Hash never makes that mistake on the same pair — different strings don't match by definition. The more serious tool paid for the old failure with a new category of error, also free — the price isn't in money but in missed and false answers.

Action three, the cheap judge model: a direct question — "is this the same question, just phrased differently?" — model gpt-4o-mini. The result: 17 out of 20, all 10 real duplicates caught. But three of its own false positives, and not all from word overlap: the pair "how long does one class run" and "tell me about the continuing-students group" shares no words at all, and the model still said "yes" — an error of judging meaning, not words. And here, for the first time, a money cost appears: by gpt-4o-mini's price list, at the case's volume (~300 calls a month) — about $0.006 a month, under a cent; a price-list estimate, not a measured fact.

Action four — the specialized external service jev, a narrow Decisions API, measured by the same method. The result: 20 out of 20, zero errors — a clean split between all the duplicates and all the different questions, with the 0.5 threshold clearing it comfortably. The best result of the four schemes — and this is the very service that used to carry the label "not measured": the cause wasn't an access problem but a plain node configuration mistake that was found and fixed. By pricing, it's not just more accurate than the cheap judge model but also cheaper — about $0.003 a month at the same volume; also a price-list estimate, not a measured fact.

The main honest finding: the best result didn't come from the most obvious candidate — the narrow service beat the general-purpose judge model and cost less. But one measurement on 20 pairs of one topic isn't reason enough to immediately rewrite an architecture already demonstrated on the rig: the same discipline that kept us from taking jev on faith earlier keeps us from blindly trusting this number now. And one more thing: both sums here are under a cent a month — price isn't the argument.

Action five, ordering — cheap first, expensive only on what's unresolved — settles both tasks on price: 5 literal repeats get caught for free by hash, and the expensive step is called only on what's left. What this looks like architecturally — on the next screen.
