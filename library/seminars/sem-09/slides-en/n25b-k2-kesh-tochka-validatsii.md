---
id: n25b
type: content
duration_min: 2.5
assertion: "The cache reads from the start of the prompt up to the first point of change -- and at Anthropic, where that boundary actually falls is decided not by the edit itself, but by how the text before it is split into blocks"
learning_goal: "Beat S2-3 (breakdown by group, review 2026-10-29): the case's main correction -- the old claim that 'appending to the end busts the whole cache' was true only for ONE layout and wrong as a general rule (K2-15). Replaces the dropped n26 (the word 'trap' removed, K2-14) and carries the owner's own testimony on hit rate (K2-13) with an explicit caveat."
visual:
  pattern: content
  figure: k2-shema-kesh-lovushka-en.png
  primary: >
    The caching condition in three lines (no word "trap"). Next, two
    columns with the same edit applied: one block of text (the cache
    burns) and four blocks with the breakpoint moved (the cache survives),
    same model, same edit, a 9.8x difference in price. At the bottom, an
    inset carrying the owner's own testimony on hit rate, with a caveat.
  backup: >
    THE OLD "CACHE TRAP" SLIDE WAS DROPPED (K2-14: remove "trap" from the
    first two condition blocks). The word is removed everywhere on this
    frame: the condition is named in its plain form, with no trap metaphor.

    THE MAIN CORRECTION (K2-15). The old claim ("appending an item to the
    end busts the whole accumulated cache") was doubted by the owner as
    right in substance and wrong in one word: he asked whether the cache
    always reads up to the point of divergence. The answer breaks into
    three parts (`stend/zamery-k2-kesh/README.md`, "A direct answer to the
    owner's question"): (1) at Anthropic, caching is NOT on by default --
    with no `cache_control`, nothing is cached at all (Table 5, the series
    with no breakpoint -- 0/0/0 on every call); (2) "reads up to the point
    of divergence" is correct, and that's the behavior of providers with
    automatic caching (Gemini, OpenAI); (3) "there's no invalidation if the
    addition comes after the breakpoint" is correct, but ONLY when the
    breakpoint is set correctly. The proof is Table 5: the same appended
    item, the same model, two different outcomes depending on how the text
    is split into blocks -- one block: 0 read, 3834 written, a price of
    1.271x (the cache burned); four blocks with the breakpoint on the new
    block: 3762 read, 68 written, a price of 0.129x (the cache survived).
    A 9.8x difference in the price of the same call. Anthropic's own
    documentation names the mechanics directly: "Cache writes occur only
    at your breakpoint... The system does not write entries for any
    earlier position"; the hash is "cumulative", so "changing any block at
    or before the breakpoint produces a different hash" -- in the
    one-block layout there simply is no record behind the breakpoint left
    to find.

    HOW THE BREAKPOINT IS ACTUALLY SET (a direct answer to "how is this
    breakpoint set in the first place", K2-15): an explicit
    `cache_control: {"type": "ephemeral"}` field on a content BLOCK (not
    at the level of the whole prompt), no more than four breakpoints per
    request. If the knowledge base is sent as one text block with a
    breakpoint at its end, any edit inside that block changes the whole
    block, and there's no record left behind it. If the knowledge base is
    split into several blocks (say, "the old 10 items" as one block, a new
    11th item as its own), and the breakpoint is moved to the NEW last
    block, the old blocks stay findable by hash, and only the appended
    part burns. The rule for the frame: not "appending is safe", but
    "appending is safe if the breakpoint sits on the new block, not inside
    the old one".

    THE OWNER'S OWN TESTIMONY (K2-13), with a caveat (README, section "The
    owner's own testimony on a 98-99% hit rate"): this is NOT our own
    measurement -- the rig makes single calls, not agentic runs, and a hit
    rate can't be measured this way. The arithmetic checks out: at the
    measured 0.107x read multiplier and a 98-99% hit rate, the input bill
    drops to 0.12-0.13 of the original -- 87-89% savings, which agrees with
    the owner's "up to 90%". The published range on real agentic traces is
    more honest and wider: 92.2-98.6% (TurnCost 98.6%, TraceLab 95.7% on
    average and 97.9% on tool steps, vLLM 92.2%), and naming this range
    stands next to the testimony, not in its place.

    THE REVERSE CASE stays unchanged in substance (the cache lives for
    minutes, an hour for some providers; a knowledge base edited more
    often than that doesn't save money, it overpays 1.25x instead of 1x).

    The figure `k2-shema-kesh-lovushka.png` needs its generator edited for
    this correction (the word "trap" in the docstring of
    `rendered/make_figures_k2.py`, a separate step in this same session,
    not here).

    EN FIGURE NOTE (Bilingual Production Rule, issue #172/#319): the EN
    slide uses k2-shema-kesh-lovushka-en.png, a direct English-text redraw
    of the same schema (same layout, same colors, same numbers), generated
    by running `python3 make_figures_k2.py --lang en` -- the same
    `kesh()` function, driven by the shared `fig_strings_en.py` dictionary
    (`tools/seminar-build/fig_toolkit.py`), not a second, hand-written
    `_en()` function. The word "trap" doesn't appear on the EN redraw
    either, matching the same K2-14 removal applied to the RU figure.
---

# The Condition Under Which the Cache Reads -- and What Decides the Breakpoint

## Assertion

The cache reads from the start of the prompt up to the first point of change. At Anthropic, where that boundary falls is decided by the block layout, not the edit itself.

## Visual

> **Condition.** If the start of the prompt up to the breakpoint matches the previous request character for character, it reads from the cache; if not, the cost starts at the point it diverges.

| Layout | Read | Written | Price |
|---|---|---|---|
| 1 block, breakpoint at the end | 0 | 3834 | **1.271x** -- burned |
| 4 blocks, breakpoint on the new one | 3762 | 68 | **0.129x** -- survived |

## Speaker notes

There's one caching condition, and it's stated with no metaphors. The start of the prompt up to the breakpoint has to match the previous request character for character. If it matches, we read from the cache starting where the match ends. If it doesn't match from the very first point of change, we pay as for new text starting there.

Now the main reason we're back here. This session's earlier claim used to go: "appending an item to the end busts the entire accumulated cache." That turned out not to always be true, and a difference of nine point eight times in the price of the same call with the same edit depends not on what we appended, but on how the text was split into blocks BEFORE the edit. We sent the knowledge base as one chunk of text with a breakpoint at its end, and the appended item landed inside that same chunk: the chunk's content changed, and there was no record left behind the breakpoint to find. Zero tokens read, the whole text written again. We sent the same knowledge base as four blocks, with the new, eleventh item as its own, fifth block, and moved the breakpoint onto it -- and three thousand seven hundred sixty-two tokens from the old blocks read from the cache; only the new sixty-eight-token block gets written.

Here's how this breakpoint actually gets set: an explicit field on a content block, not on the text as a whole, up to four breakpoints per request. Writing happens only at the breakpoint itself -- Anthropic's documentation says so directly -- and the hash used to look up a match is cumulative: any change at or before the breakpoint changes the hash entirely. Hence the rule: appending to the end is safe if the breakpoint is moved onto the new, just-appended block. If it stays inside the old one, there's no safety.

And separately, something the owner named from his own experience: in agentic tasks, where the same start of the prompt repeats from step to step, the cache hit rate reaches ninety-eight to ninety-nine percent, and the savings reach ninety. This isn't our own run: our rig makes single calls, it can't measure an agentic series. But the arithmetic checks out: at our measured multiplier, a hit rate like that gives savings of around ninety percent. Published measurements on real agentic traces name a range from ninety-two to ninety-eight and a half percent -- more honest than one narrow figure, and still impressive.

And the reverse case, which hasn't gone anywhere: the cache lives for minutes, around an hour for some providers. A knowledge base edited more often than the cache can pay for itself doesn't save anything -- it overpays.
