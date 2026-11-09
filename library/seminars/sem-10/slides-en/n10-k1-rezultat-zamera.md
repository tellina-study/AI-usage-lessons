---
id: n10
type: measured_outcome_table
duration_min: 1.5
assertion: "At 500 documents, prompt-stuffing doesn't get gradually more expensive — it holds accuracy at one level for three steps in a row and then physically refuses to answer: the request exceeds the model's context"
learning_goal: "Beat S2 (summary) — a direct continuation of n09 (structure). The headline finding is pulled out into its own gold tile (rule A11). Tables are kept apart per S6: accuracy is a share, cost is dollars, recall is its own tile, not mixed into one cell."
visual:
  pattern: measured_outcome_table
  primary: >
    Two compact 4×3 tables (base size · whole prompt · keyword · vector) —
    one for accuracy only, one for cost in dollars only — and a golden
    tile with the headline failure number at 500 documents.
  backup: >
    Numbers — SETKA-KEYSOV.md Case 1 / stend/raw/case1-results.json, 10
    SberQuAD questions × 4 base sizes (10/50/200/500, 500 added by an
    extra pass on 2026-11-01 per the owner's comment "the current
    measurement is too easy") × 3 options. The questions were rebuilt a
    second time on 2026-11-02 (issue #311) with lexical_gap/exact_match/
    neutral stratification (Case 3's methodology) — the old 10 questions
    were almost all "exact match," which trivially gave keyword
    recall@1=1.0 and didn't test what was claimed. "Accuracy" = strict
    substring containment of the gold short answer — this understates the
    absolute numbers EQUALLY for every option (methodological disclaimer —
    in the notes, not on screen). The HTTP 400 error text is verbatim from
    the `exec_id: "2483"` field, the run of this rebuild.

    TWO TABLES INSTEAD OF ONE (rule S6 — "one column, one dimension,"
    canon `forma-keysa-s-zamerom.md` §6): accuracy (a share) and cost
    (dollars) in separate tables. Recall@1 gets its own tile, because
    keyword and vector behave differently on it (keyword holds 0.8 across
    all four sizes without change; vector holds 1.0 on three of four and
    dips to 0.9 at 500) — that's no longer one fact shared by both, but
    two separate observations, and mixing them into one sentence would be
    wrong.
---

# What the run showed at four base sizes

## Assertion

Prompt-stuffing holds accuracy at one level across three sizes in a row — then simply refuses to answer, with no warning dip.

## Visual

| Accuracy | Whole prompt | Keyword → answer | Vector → answer |
|---|---|---|---|
| 10 docs | 0.7 | 0.5 | 0.6 |
| 50 docs | 0.7 | 0.5 | 0.7 |
| 200 docs | 0.7 | 0.4 | 0.6 |
| 500 docs | **HTTP 400 ERROR** | 0.5 | 0.7 |

| $/question | Whole prompt | Keyword → answer | Vector → answer |
|---|---|---|---|
| 10 docs | $0.000189 | $0.0000484 | $0.0000486 |
| 50 docs | $0.000809 | $0.0000484 | $0.0000482 |
| 200 docs | $0.003204 | $0.0000501 | $0.0000481 |
| 500 docs | — rejected | $0.00005 | $0.000049 |

> Retrieval recall@1: keyword — **0.8 across all four sizes without change**; vector — **1.0 at 10/50/200, 0.9 at 500**. **At 500 documents, prompt-stuffing needs around 160,000 tokens — more than gpt-4o-mini's context (128,000); OpenRouter rejects the request with HTTP 400 before the model ever answers.**

## Speaker notes

Ten questions from SberQuAD — an open question-answering dataset built on Russian Wikipedia articles with gold-standard labeling of which text fragment holds the correct answer — were run through the real rig at four base sizes and three actions, in exactly the structure we just laid out. The numbers in both tables are the direct result of calls to `gpt-4o-mini` and to the `text-embedding-3-small` embedding through the rig's already-configured access: there's no eyeballed estimate here.

Prompt-stuffing — appending the whole base to the prompt in full — behaves differently from what you might expect at first glance. Accuracy doesn't fall gradually from size to size — it holds almost at one level, 0.7, at ten documents, at fifty, and at two hundred. There's no visible warning signal at all. Meanwhile the cost of a single question keeps growing the whole time: from $0.000189 to $0.003204 — a seventeen-fold increase across that same range, with no connection at all to what's happening to accuracy.

Then comes a jump: not gradual degradation — an instant, complete failure. At five hundred documents, the raw SberQuAD corpus weighs around a hundred and sixty thousand tokens — noticeably more than `gpt-4o-mini`'s context accepts, a hundred and twenty-eight thousand. OpenRouter rejects such a request with error code 400 before the model has had a chance to read anything: "This endpoint's maximum context length is 128000 tokens. However, you requested about 159914 tokens (159914 of text input). Please reduce the length of either one, or use the context-compression plugin to compress your prompt automatically." That's not a metaphor and not our own assumption — that's the literal text of the server's response, and that's exactly why the accuracy table carries a separate error mark on that row instead of a number: there's nothing to compute the accuracy of a refused answer from. Accuracy gave not even a hint, on any of the three previous steps, that the system would simply fail on the next one: 0.7 held steady, and then — a cliff.

Meanwhile, both options with separate search — whether by keyword or through a vector store — keep the prompt constant, around 270 tokens, at a cost of thousandths of a cent at any of the four sizes. But their recall@1 behaves differently, and it matters not to smear that into one sentence. Keyword's recall@1 equals 0.8 at all four sizes without a single exception — no better, no worse as the base grows, and already below one at the very smallest size, ten documents, where there are no distractors at all. Vector's recall@1 equals one at 10, 50, and 200 documents, and dips only to 0.9 at 500. Why exactly — separately, next beat: behind these two numbers are two different and perfectly concrete reasons — there's no general degradation here.

A methodological disclaimer, honestly: accuracy here is strict substring containment of the gold short answer inside the model's answer. This understates the absolute numbers equally for all three actions — the model often answers correctly in substance but in a different wording or grammatical form of the word — and this metric doesn't distort the comparison between actions. What exactly is behind these two separate recall dips — next beat.
