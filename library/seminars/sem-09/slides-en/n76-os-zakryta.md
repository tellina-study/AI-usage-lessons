---
id: n76
type: recap_table
duration_min: 3.0
assertion: "The six rows of the axis are filled in with measurements: in four of the six case studies, the run was green, and the answer still could not be sent"
learning_goal: "Closing the session's axis. Every right-hand cell is a number from a run the room has already seen. The session's throughline gets its count here: six cases, eight measured runs on the live rig, 1461 calls that reached the model, four cases of a green run with an answer unfit to send, and, named separately, 75 discarded calls — 45 from Case 4's withdrawn setup, 30 from the photo-reading run with the leaked prompt."
visual:
  pattern: recap_table
  primary: >
    The same table that opened the session, now with the right-hand column
    filled in. Below it, two tally cards (the calls that count, and the
    discarded ones separately) and a short line about the two case studies
    that didn't make it into the count of green runs.
  backup: >
    The left column is verbatim the same as on n04. The right column is
    assembled from the "generalization" and "nuances" beats of the six
    cases in `SETKA-KEYSOV-S9.md` and `SETKA-KEYSOV-S9-part2.md`; every
    number is our own rig run with a protocol (`stend/zamery-k1-k3/`,
    `stend/zamery-k2/`, `stend/zamery-k2-kesh/`, `stend/zamery-k3-smes/`,
    `stend/zamery-k4-novyy/`, `stend/zamery-k5-k6/`,
    `stend/zamery-k5-povtorno/`, `stend/zamery-k6-edinyy/`), or outside
    figures from `CHISLA-SVERENO.md`. Nothing is taken from `research/*`.
    `stend/zamery-k4/` is the history of Case 4's withdrawn setup and does
    not serve as a source for any figure currently in use.

    THE THROUGHLINE'S COUNT is assembled by addition over each rig's own
    README, not invented: eight measured runs, 1461 calls that reached the
    model — 268 (`zamery-k1-k3`) plus 84 (`zamery-k2`) plus 119
    (`zamery-k2-kesh`) plus 92 (`zamery-k3-smes`) plus 693
    (`zamery-k4-novyy`, Case 4 was entirely redefined 2026-10-29, issue
    #303) plus 85 (`zamery-k5-k6`, Measurement 4.1 honestly re-measured
    after a prompt leak) plus 90 (`zamery-k5-povtorno`, counting single
    few-shot and description on two scenarios plus their combination) plus
    30 (`zamery-k6-edinyy`). Separate from this sum: 75 discarded calls —
    45 held by Case 4's withdrawn setup (`zamery-k4/`), 30 held by the
    first, leaked run of Measurement 4.1 in `zamery-k5-k6`, replaced by an
    honest rerun on the fixed prompt (those 30 honest calls are already
    counted in the 85 above). The full table of where every number comes
    from is `BRIEF-PROIZVODSTVO.md`, section "Where the call count comes
    from." The same number gets corrected, in the same round, in
    `BRIEF-PROIZVODSTVO.md`, in `rendered/deck-config.yaml`, and in
    `rendered/svodka-tekst.yaml`. "Green run, can't send" is credited to
    four cases — 1 (6 of 15 confidently wrong), 4 (11 of 64 wrong
    decisions on honest requests even under the best defense), 5 (10 of
    10 wrong at the threshold), 6 (0 of 15 wrong dates caught by format
    validation). Case 3 is deliberately NOT counted among these four —
    there, the added check rejected CORRECT answers, and nothing unfit
    ever went out — the opposite defect, named in its own line.

    Case 2 (renamed K2-1, revision 2026-10-29: "Prompt Optimization") has
    no run of its own for THIS claim in the table (a dip in the middle of
    the list on its own knowledge base's short items) — this is stated
    outright, with no rounding up to "all six." Case 2 does have its own
    runs on five directions of prompt structuring (84 calls,
    `zamery-k2/`) and on the cost and mechanics of caching (119 calls,
    `zamery-k2-kesh/`), and these are counted in the total sum above —
    they don't cancel this row's own caveat, which is about READING, not
    about COST.

    The right-hand cells are held to a short fact for the sake of height:
    six rows is this table's limit, and the detail for each row lives in
    the notes.
---

# Six Rows of the Axis: What It Turned Out to Be

## Assertion

The room saw every right-hand cell on screen before it was ever spoken aloud.

## Visual

| Looks solid | What it turned out to be |
|---|---|
| the model will say so itself if it doesn't know the answer | admitted it 3 of 3 times where the topic isn't in the knowledge base at all; answered confidently and wrongly **6 of 15** times where the topic is there but the detail is different |
| if the knowledge base grows, we'll just add a new item at the end — order doesn't matter | a knowledge base pasted whole into the prompt has a physics of position: the start and the end of the list read better than the middle, and what reads worse is a topic that **is** in the knowledge base |
| asking the model to re-read its own answer — an extra check can't hurt | the judge model falsely rejected **5 of 5** correct answers, approved what the code had already rejected **0 of 6** times, and on one question changed its verdict only on the third attempt at nearly the same text; the cost is 2 model calls per attempt against 1 |
| three classic defenses against injection — so text manipulation is a closed problem | the best combination holds **0 successful attacks out of 34**, but of 64 decisions, **11 are still wrong** — and all 11 are on requests with not a single manipulation in them: the model gets the 30-day rule's arithmetic wrong. The same rule in code: **64 of 64**, 0 model calls |
| the same model settings — the same behavior on the same question, every time | at zero temperature: **3 different outcomes out of 10** on a recalculation, **10 of 10** identically and wrongly at the 3000-ruble threshold, **10 of 10** consistently self-contradictory on two knowledge-base items |
| a formally correct answer (valid JSON, every field present) means the document was read correctly | the amount is correct **25 of 30** times, and breaks at 53×64 pixels; a date set in smaller type breaks earlier — at 2.9 pixels of the character's own glyph height, and format validation caught **0 of 15** wrong dates, while a cross-check against an independent value caught **15 of 15** |

> **Six cases. Eight measured runs on the live rig — 1461 calls that reached the model. In four of the six, the run was green, the log was clean, and the answer still could not be sent: "Answer or Stay Silent," "Defense Against Injection and Manipulation," "Answer Reproducibility," "Reading a Photo."**

> **Separately, 75 calls were discarded: 45 went to Case 4's withdrawn setup, 30 to the first run of photo reading, where the prompt itself handed over the finished amount instead of letting the model read it. I found the leak by staring at an unreadable crop of a receipt and asking how that could possibly have been recognized at all — exactly what this whole session has been about all evening: a run can be green when the answer still can't be sent.**

> The two remaining case studies differ. "Checking the Answer": the added check rejected correct answers 5 of 5 — nothing unfit went out, but fit answers didn't either. "Prompt Optimization": this row's reading effect rests on an outside source, though the case did measure caching's own cost and mechanics separately.

## Speaker notes

We're back at the table we started with. The right-hand column isn't empty anymore, and it wasn't my narration that filled it in — you saw every cell as a number on screen.

First row. The model will say so itself if it doesn't know: where the topic isn't in the knowledge base at all, it admitted that all three times. Where the topic is there, but the question is about a neighboring detail, the exact same setting answered confidently and wrongly six times out of fifteen — the decision "I answer myself, or I hand this to a human" was living inside the text of the answer, where it can neither be checked nor shown to anyone.

Second row. Adding an item at the end. A knowledge base that sits whole inside the prompt has a physics of position: the start and the end of a list read better than the middle, and what breaks is the answer about something that actually is in the knowledge base. On reading — this is the only row of the table with no run of our own; we did already measure, in this same case, the cost of that same text through caching, ourselves.

Third row. One more look can't hurt. It hurt: the judge model rejected five correct answers out of five, and approved what code had already rejected zero times out of six. On one question it rejected, rejected again, and only approved nearly the same text on the third attempt — two model calls per attempt against one for the code-based check.

Fourth row. The three classic defenses handled the direct task: the best combination let through none of the thirty-four attacks. But of sixty-four decisions, eleven are wrong on nothing but honest requests: the model kept getting the thirty-day rule's arithmetic wrong, naming the course's correct date and still drawing the wrong conclusion from it. The same rule in plain code: sixty-four out of sixty-four, with not a single model call.

Fifth row. Zero temperature promises the same behavior every time. On a question where the answer is looked up directly in the knowledge base, that's exactly what happens. Where the answer has to be composed, we got three different outcomes out of ten. At the three-thousand threshold, the answer was identical all ten times — and wrong all ten times. On two knowledge-base items at once, the answer held steady all ten times, and contradicted itself in two adjacent sentences all ten times.

Sixth row. A formally correct answer. The amount read correctly twenty-five times out of thirty: no errors on five resolutions out of six, and it breaks cleanly on the smallest one — fifty-three by sixty-four pixels. The date on the same receipt is printed smaller and breaks earlier, at two point nine pixels of the character's own glyph height. Format validation caught zero wrong dates out of fifteen; a cross-check against an independent value caught all fifteen.

Now the count. Six cases, eight runs on the rig — one thousand four hundred sixty-one calls. In four of the six, the run was green, the log was clean, and the answer could not be sent. Separately: seventy-five calls discarded — forty-five on Case 4's withdrawn setup, thirty on the photo-reading run where the prompt handed over the finished amount; I caught the leak while staring at an unreadable crop of a receipt. The two remaining case studies didn't make it into the count: in the third, the check rejected fit answers; in the second, there's no run of its own for this at all.
