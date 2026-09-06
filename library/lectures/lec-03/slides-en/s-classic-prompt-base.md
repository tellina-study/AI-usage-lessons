---
id: s-classic-prompt
type: assertion_visual
section: "Section 1. The prompt and its limits"
duration_min: 2
assertion: "Before the prompt, a task was stated as a precise specification and a deterministic program; the prompt is stating a task to a probabilistic system in natural language"
learning_goal: "Classical baseline §1.0: precise task statement as the starting point for the prompt"
learning_outcomes: [LO7]
chapter_ref: "§1.0 [for-slide-s-classic-prompt]"
visual_brief: "Three classical-baseline cards (formal specification / requirements spec; imperative vs declarative; interface contract) + gold callout \"what to keep from the classics\" + a bridge to the prompt at the bottom."
interaction: none
new_in_v5b: "#185 WP8 — classical baseline of Section 1"
---

# Visible content

## Title bar
"How a task was stated before the prompt — and what that changes"

## Body
[Three classical-baseline cards, Ocean rounded box]

**Precise specification / requirements spec** — pre- and post-conditions, invariants, acceptance criteria (Z-notation, TLA+, Design by Contract). The result is deterministic and checkable.

**Imperative vs declarative** — "how to do it" (a step-by-step algorithm) versus "what to obtain" (SQL/Prolog describes the result, the engine decides how).

**Interface contract** — a precise input/output agreement (type signatures, OpenAPI, Protobuf). A single correct meaning + a way to verify it.

[Gold callout — what to keep from the classics]
**What to keep: the discipline of precise statement — a precise prompt = the same requirements spec in natural language. For anything deterministic and verifiable (arithmetic, schema validation, rule-based routing) — classical code, not a prompt.**

[Bridge, bottom]
The prompt is stating a task to a probabilistic system in natural language: hence its power (no need to formally specify the unspecifiable) and its limit (no single meaning, no determinism).

## Speaker notes

Before we talk about the prompt, let us fix a starting point — the way an engineer made a system do what was needed before large language models appeared, a way that has not gone anywhere. The classical answer to "how do I get exactly what I need from a machine" rests not on phrasing a wish in natural language but on a precise specification and a deterministic program. Let us reconstruct this way from scratch, because the prompt is its direct opposite along one key axis, and that axis is only visible next to the classics.

The classical discipline of task statement relies on several named tools. A formal specification describes what a system must do in a language with no double reading: pre- and post-conditions, invariants, and in the limit machine-checkable specifications (Abrial's Z-notation, Lamport's TLA+, contract programming in the Design by Contract style). A requirements spec fixes the requirements, boundaries, and acceptance criteria — the basis on which the work is later accepted. An interface contract is a precise agreement about what a method or service accepts on input and guarantees on output (type signatures, OpenAPI, Protobuf). The common trait: the result is deterministic and verifiable.

The same discipline distinguishes two styles of stating a task. The imperative answers "how to do it" — the program lists the steps. The declarative answers "what should result" — a SELECT query does not say how to search; it describes the wanted result, and the planner decides how to obtain it. In both cases the statement had a single correct meaning and a way to check it.

Now the bridge to the rest of the section. The prompt is stating a task to a probabilistic system in natural language. Herein lies both the power and the limit. The power: no need to formally specify what cannot be specified — "rewrite this letter more politely." The limit: natural language has no single correct meaning, and the executor has no determinism. Hence the practical seam rule: use a prompt for what cannot be formally specified; leave everything that can be specified to the classics.
