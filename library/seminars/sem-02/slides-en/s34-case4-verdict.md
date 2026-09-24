---
id: s34
type: case_study
assertion: "The task narrowed down to a template — a local 7-8B-parameter model handles it"
learning_goal: "Breaking down intro 2 — exactly what the engineer dug up about small models; a double lesson on complexity and sensitivity"
learning_outcomes: [LO1, LO7]
references:
  - "T-lite/T-pro: https://habr.com/ru/companies/tbank/articles/928956/"
visual:
  pattern: single_card_plus_dual_lesson
---

# Sales calls — breakdown

## Assertion

Hard for a human doesn't mean hard for a model

## Visual

A schema: "free-form conversation" → "extracting fields on a fixed
template" → "local model, 7-8 billion parameters, 4-bit quantization" →
"data doesn't leave the company perimeter." Next to it — a list of open
7-8B-class models: Qwen3, Llama, Gemma, Mistral, T-lite, T-pro. At the
bottom — two takeaway lines. No row of moves under the diagram.

## Speaker notes

The task actually narrowed down: it doesn't need a free-flowing
conversation, it needs a structured summary against a fixed template of a
few fields — that's extracting fixed fields against a template, not a
free conversation requiring context understanding. Here's exactly what
the engineer dug up while looking into this: this class of task is well
covered by current open models in the 7-8 billion parameter range —
Qwen3, Llama, Gemma, Mistral, as well as the Russian T-lite and T-pro,
built by T-Bank under the Apache 2.0 license, based on Qwen. 4-bit
quantization — compressing the model's weights down to 4 bits per
parameter — lets you fit such a model into 4-6 gigabytes of memory and
run it on an ordinary server with no GPU farm, using tools like Ollama or
llama.cpp. If you need to fine-tune the model more precisely for the
output format, you can fine-tune it with LoRA, an economical fine-tuning
method that doesn't touch all of the model's weights, and do it on a
single GPU. Let's spell out two lessons explicitly. First — "hard for a
human" doesn't mean "hard for a model": a free-form conversation looks
like a hard input, but extracting structured fields against a template is
a task of moderate complexity that a small model handles reliably.
Second — data sensitivity isn't visible in the initial task statement; it
has to be uncovered by asking questions about the content of the input
data, not assumed from the wording.
