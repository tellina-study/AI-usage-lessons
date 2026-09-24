---
id: s36
type: failure_vignette
duration_min: 3
assertion: "By default memory is read as trusted context rather than as data — and turning memory on does not necessarily improve the result"
learning_goal: "The failure/limitation of case 2.1, two layers of a different nature: memory poisoning (SpAIware) and the measured \"memory exists\" ≠ \"memory helps\""
visual:
  pattern: failure_vignette
  primary: "Top half — the story of memory poisoning with a date and the mechanics in three steps. Bottom half — three measurements that run against intuition: 46.0% versus 57.6% on the same task set; losing to a flat file by 25-67 points; 17% write refusals."
---

# Memory can lie, and memory can get in the way

## Assertion

By default memory is read as trusted context rather than as data — and turning memory on does not necessarily improve the result.

## Visual

Top half — **memory poisoning**. SpAIware (Johann Rehberger, September 2024, the ChatGPT desktop app for macOS). The mechanics in three steps:

external text with an embedded instruction → **long-term memory** → activation in later sessions, exfiltration of the conversation

Caption: the exfiltration vector was closed in version 1.2024.247 (September 2024); the structural principle remained.

Scale, with a baseline for comparison: **≈48%** of all subsequent memory retrievals captured (MemoryGraft, 2025; before poisoning — **0%**), and it held until a manual cleanup; in an adjacent experiment **5** planted documents are enough to steer the output in more than 90% of cases.

Bottom half — **"memory exists" ≠ "memory helps"**:

| Measurement | Value | Baseline for comparison |
|---|---|---|
| A popular memory system on a long-term memory benchmark | **46.0%** with memory versus **57.6%** without | the same system, memory switched off |
| Six memory systems versus "the whole session text in one file" | losing to the flat file by **25–67** points | the same flat file |
| Write discretion | **17%** (4 tasks out of 24) — the model refused to write down the fact that was needed | the same 24 tasks |

## Speaker notes

Two layers of a different nature, and they must not be merged: the first is about security, the second about effectiveness.

Poisoning — told as a story, with a date: September 2024, the ChatGPT desktop app for macOS, researcher Johann Rehberger. The agent read an external text — and an instruction was embedded inside it. That instruction went not into the conversation but into long-term memory. The conversation ended, the memory stayed. The vendor closed that specific leak channel the same month. Nobody closed the principle: by default the agent reads the contents of memory as trusted context, not as data.

The scale — with an explicit baseline: a dozen poisoned templates captured on the order of half of all subsequent memory retrievals, against zero before the poisoning; in an adjacent experiment five planted documents were enough to steer the output in more than nine cases out of ten.

The practical conclusion — as it applies to our file: today we wrote down our own decision, and here everything is fine. But the moment the agent starts writing into memory conclusions drawn from someone else's issue, someone else's page or someone else's ticket — that is already a different level of trust.

The second layer does not hit your paranoia, it hits your intuition. An independent run of one popular memory system: with memory — forty-six percent, without memory — fifty-seven point six, the same system, the same benchmark. In a live comparison of six memory systems against the trivial "put the whole session text into one file", some of the systems lost to that flat file by twenty-five to sixty-seven points. An honest caveat about the conditions: the corpora there are small, they fit into the context in full — but a small corpus is exactly our case today.

And a third detail: on twenty-four tasks, on four of them — seventeen percent — the model flatly refused to write down the fact that was needed. This is not a bug — by construction the model decides for itself what is worth writing down. The conclusion for an engineer: completeness of memory is not guaranteed, and if a fact is critical — you write it by hand.
