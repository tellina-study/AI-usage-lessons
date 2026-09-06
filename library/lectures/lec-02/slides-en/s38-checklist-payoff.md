---
id: s38
type: summary
section: "Section 6. Wrap-up"
duration_min: 3
assertion: "Let's wrap up: for each mechanism — the boundary and what to do about it in practice"
learning_goal: "Summary table of 'mechanism → boundary → what to do' across every topic covered in the lecture; self-check"
learning_outcomes: [LO7]
chapter_ref: "§5.4 (chapter-part3.md) [for-slide-s38]"
visual_brief: "A table of rows in an Ocean rounded box: 'mechanism' column (tokenization, attention/role, KV-cache and prompt caching, determinism, context window, sampling/reasoning, structured output, benchmarks, model sizes), 'boundary' column, 'what to do — one line' column. Rows compact, ≤2 lines of text per cell. At the bottom, a wide gold callout 'Knowing a tool means knowing its limits'."
---

# Visible content

## Title bar
"Let's wrap up: mechanism → boundary → what to do"

## Body
[Summary table, Ocean rounded box]

| Mechanism | Boundary | What to do |
|---|---|---|
| Tokenization | The model sees tokens, not letters; a viral fix (strawberry → cranberry) doesn't generalize to the task class | Test "your own domain's cranberry"; hand off counting and arithmetic to a tool |
| Attention and role | A role is tokens that get weighted like any other; it shifts style and focus, not factual quality | Use role as a tone/focus control, not an "intelligence booster"; supply data for facts |
| KV-cache and prompt caching | The cache only saves on a repeated prefix; one changed token near the start breaks everything after it | Put stable content first in the prompt, variable content last; check the cache hit rate in API responses |
| Context window | The advertised window ≠ usable window: without lexical cues, 11 of 13 models lose half their accuracy by 32K already | Choose a model based on non-lexical-match benchmarks, not the number on the model's spec sheet |
| Determinism at T=0 | Inference kernels are not batch-invariant: someone else's load on the server changes your answer | Don't build tests on bit-for-bit comparison; strict determinism is a separate infrastructure problem |
| Reasoning tokens | Billed as output, with no natural ceiling on volume | Budget for reasoning separately; control effort/verbosity explicitly |
| Structured output | Token masking guarantees validity by construction, but not substantive quality | Don't over-constrain the schema — excess strictness sometimes lowers answer quality |
| Benchmarks | Data contamination, overfitting of public versions, models cheating on tests | Build your own small eval set; treat leaderboards as a guide, not a guarantee |
| Model sizes | Open weights no longer means "runnable locally": MoE giants only fit in the cloud | Choose a model class by task scale and available hardware, not by the weight license |

[Gold callout]
**Knowing a tool means knowing its limits. Every mechanism works — but not without bound.**

## Speaker notes

Let's wrap up. Over an hour and a half we walked the inference pipeline from text to answer, and at every stage — alongside the mechanism — we saw its boundary. Tokenization: the model sees tokens, not letters; a viral fix on one word doesn't generalize to the task class — test your own analogue of cranberry. Attention and role: a role in the prompt is tokens that get weighted like everything else; it shifts the style and focus of the answer, but doesn't raise factual quality — it's a tone-control tool, not an intelligence booster.

Caching: KV-cache and prompt caching only save money on a matching prefix, and one token changed near the start wipes out the savings for everything after it — stable content goes first, variable content goes last. Context window: the number on the model's spec sheet is intake capacity, not a guarantee of quality reasoning across the whole length; without lexical cues, models degrade already at a small fraction of the advertised window. Determinism: zero temperature doesn't give bit-for-bit reproducibility, because compute kernels change the order of summation depending on someone else's load on the server — build your tests on semantic comparison.

Reasoning tokens are billed as output and have no built-in ceiling on volume — budget for them separately. Structured output guarantees validity by construction, but not substantive quality — don't over-constrain the schema. Benchmarks can't be taken at their word: data contamination and overfitting of public versions are commonplace, your own eval set is more reliable than someone else's leaderboard. And model sizes: open weights have long stopped being synonymous with "runnable locally" — the choice between a small model and a giant comes down to task scale and available hardware.

The common denominator: knowing a tool means knowing its limits. Every one of these mechanisms works and delivers value — but not without bound; and in every row there's a point where an engineer must be able to say "no" to an unsuitable use. None of these "no"s mean "don't use models" — they all mean "use them with precise knowledge of what's guaranteed to you and what isn't."

A one-minute self-check: close the table and reconstruct the "boundary → what to do" pair for any three rows. If you can — the main content of the lecture is yours to keep.
