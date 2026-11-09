---
id: n25
type: measured_outcome_table
duration_min: 2.0
assertion: "Five providers, five series of calls, 119 requests -- the design of the caching measurement, before a single result number shows up on screen"
learning_goal: "Beat S2-1 (measurement structure, review 2026-10-29): the corpus, the groups, and the expectation for each group -- BEFORE the result. Replaces the dropped n25 (K2-9, the old frame with theoretical multipliers and no run of our own) and opens the re-run caching measurement (K2-19, Z2). The model and its settings are named (C5)."
visual:
  pattern: measured_outcome_table
  primary: >
    A five-row table of groups: what was checked · on what · how many
    calls · what was expected from the provider's own documentation. No
    results on the frame -- not a single outcome number. On top, a banner
    with the model names and the calling method.
  backup: >
    THE OLD n25 WAS DROPPED (K2-9: "bust it -- doesn't work"). The
    previous frame carried the multipliers 1.25x/2x/0.1x and an outside
    ProjectDiscovery example with not a single number of our own; the
    owner rejected it as not working. In its place: the structure of a
    real, re-run measurement of our own (K2-19, Z2, from
    `qa/kommentarii/RAZBOR-2026-10-29.md`).

    MODELS AND SETTINGS (C5), all five through the same broker, OpenRouter,
    an `httpRequest` node on `/v1/chat/completions`, the request body
    assembled entirely on the python side, parameters unchanged for every
    model except the explicit `cache_control` field wherever it's being
    tested: `anthropic/claude-haiku-5.5` (served by Anthropic, caching
    threshold 512 tokens), `google/gemini-2.5-flash` (served by Google AI
    Studio, threshold 2048), `openai/gpt-4.1-mini` (served by OpenAI,
    threshold 1024), `deepseek/deepseek-chat` (served by DeepInfra),
    `qwen/qwen-2.5-7b-instruct` (served by Phala, the session's own rig
    model).

    FIVE SERIES, 119 CALLS -- `stend/zamery-k2-kesh/README.md`, section
    "How to rebuild" and Tables 1-8: S1 -- 20 calls, which of the five
    models returns caching metrics at all; S2 -- 36 calls, where to append
    a knowledge-base edit (no edit / at the end / in the middle / at the
    start) on the automatic-caching providers; S3 -- 27 calls, how
    Anthropic's breakpoint is set (one text block against four blocks);
    S4 -- 24 calls, a threefold repeat of S2's borderline cases; S5 -- 12
    calls, the session's real knowledge base (10 items, not padded
    synthetic text).

    THE EXPECTATION FOR EACH GROUP comes from provider documentation,
    named by primary source, NOT from our own earlier guess: Anthropic
    documents an explicit `cache_control` ("Opt in with cache_control");
    Gemini and OpenAI document automatic caching with no parameter
    ("enabled by default"); Anthropic's own documentation also states that
    writing happens "only at the breakpoint" and that the hash is
    "cumulative" -- hence the expectation that block layout should matter.
    Each of the three expectations is checked by a separate group, and
    they aren't all confirmed the same way -- that's the outcome beat, not
    this one.

    Our own measurement is tied to the session's real text: the base is
    `stend/zamery-k2-kesh/baza.py`, Case 2's 10 real items (the same ten
    as on n23) plus 50 synthetic ones for the series where caching needs
    to be observed on text above the threshold (a padded base is a
    condition for OBSERVING the effect, not a property of our own task --
    see beat n25a).

    NOT A SINGLE RESULT ON THE FRAME (C2): not "turned on", not "worked",
    not a percentage. The test's structure in full, and it stops here.
---

# Measurement Structure: How Caching Was Checked Across Five Providers

## Assertion

Five models, five series, 119 live calls through the same broker. Not a single result on this frame -- only the design.

## Visual

> **Models and calling method.** `claude-haiku-5.5` (Anthropic) · `gemini-2.5-flash` (Google) · `gpt-4.1-mini` (OpenAI) · `deepseek-chat` (DeepSeek) · `qwen-2.5-7b-instruct` (the session's own model). All five through OpenRouter, one `httpRequest` node, parameters unchanged.

| Group | What was checked | Calls | What provider documentation led us to expect |
|---|---|---|---|
| S1 -- who returns metrics | each of the five models, the same 3790+-token prompt, with a breakpoint and without | 20 | not every provider publishes a caching field in the response; Qwen and DeepSeek -- the price is in question |
| S2 -- where to append the edit | Gemini and OpenAI: no edit · appended at the end · inserted in the middle · edited at the start | 36 | automatic caching matches by prefix -- the end should survive, the start and the middle should invalidate |
| S3 -- Anthropic's breakpoint | one whole text block against four blocks with the breakpoint on the new one | 27 | documentation says writing happens "only at the breakpoint" and the hash is "cumulative" -- block layout should change the outcome |
| S4 -- repeating the borderline cases | a threefold repeat of S2's most unexpected outcomes | 24 | a repeat checks that the finding isn't a fluke of one call |
| S5 -- the real knowledge base | the session's 10 real items (not padded synthetic text), three models | 12 | short text risks not reaching the caching threshold for any provider |

## Speaker notes

Before looking at the result, let's take apart the measurement itself. We didn't check one model with one call -- we ran five different providers through the same broker, OpenRouter, with the same node, with the same call parameters, changing nothing except exactly what each specific series is testing.

Five series, a hundred nineteen calls. The first series is twenty calls, the same model, the same long text, and a single question: does this model even return caching numbers in the response, and does caching work with a breakpoint and without one. The second series is thirty-six calls on the automatic providers, Gemini and OpenAI: we edit the same knowledge base in four different spots and see what survives from the accumulated cache. The third is twenty-seven calls, Anthropic only, and this is the main series: its cache isn't automatic, you have to set an explicit breakpoint, and we're checking whether the outcome depends on how the text is split into blocks around that breakpoint. The fourth repeats the third's most contested outcomes, so we don't take one random call's word for it. The fifth is our session's real ten items, not a padded test text, sent exactly the way they'll actually go to the model on the live rig.

Each group had an expectation, and it's taken from each provider's own documentation, not out of thin air: Anthropic states directly that caching only works on explicit request; Gemini and OpenAI state that caching is always on and nothing needs configuring; and separately, Anthropic states that writing happens exactly at the breakpoint, no earlier, and that any change to the text before the breakpoint changes the match check entirely.

On this screen, I'm deliberately not saying what got confirmed. The test's structure isn't the outcome yet, and looking at a number before understanding what was measured and why is a sure way to misread what it means. Next screen -- the round-up.
