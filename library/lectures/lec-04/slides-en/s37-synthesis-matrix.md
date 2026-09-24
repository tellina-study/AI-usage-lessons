---
id: s36
type: schema_matrix
section: "Section 7. Synthesis — discipline by phase"
duration_min: 3
assertion: "The lecture's matrix: phase × leading practice × failure mode × where the human is required — with no vendor column, because the vendor illustrations were already named in prose across sections 1–6 and a fifth column would make the table read as a ranking of tools"
learning_goal: "SYNTHESIS matrix (round-3 edit §7.1): phase × leading practice × failure mode × where the human — 4 columns, the vendor column removed entirely"
learning_outcomes: [LO1, LO4, LO7]
chapter_ref: "§7.1 [for-slide-s36]"
verify_day_of: true
visual_brief: >
  schema_matrix 8 rows (phases) × 4 columns (round-3 edit §7.1: the vendor column is removed entirely so the
  table cannot read as a ranking of tools — the vendor illustrations were already named in prose across
  sections 1–6). Columns: Phase · Leading practice (Primary mid, dominant, wider) · Failure mode · Where the
  human is required (gold-accent column).
  Fill >=75% (every cell filled, <=2 lines, font >=12pt axis / >=14pt cell). Single language EN.
  An anchor icon per phase (Lucide) in the first column. Gold — the "where the human" column + the caption
  "the vendor names from sections 1–6 are replaceable; the practice / failure mode / human in this summary are
  durable, because they rest on the character of the phase's complexity". Every cell is DERIVED from the section
  covered, not assigned. Source references — inline right at the material, NOT in a bottom footer; small and
  muted.
interaction: none
---

# Visible content

## Title bar
The lecture's matrix: the practice leads — no vendor column

## Body
[schema_matrix — 8 phases × 4 columns; the vendor illustrations were already named in prose across sections 1–6 and are deliberately not repeated here]

| Phase | Leading practice | Failure mode | Where the human is required |
|---|---|---|---|
| Requirements | spec-driven: spec before code | prompt-and-pray; "spec = truth" | **deciding what to build** |
| Architecture | ADR + fitness functions + architecture-as-code | poisoned context without management | **choosing the forks under trade-off** |
| Implementation | explore→plan→code→commit + harness | the 70% problem; "almost right" | **reviewing the diff + merge** |
| Testing | TDD: test-as-spec + a deterministic gate | "all green" lies; coverage != defects | **what the test asserts** |
| Review + Security | fresh-context; least-priv+sandbox+egress+SAST against the Lethal Trifecta | complacency; vulnerable code + false confidence | **a second pass + threat modeling** |
| Delivery (CI/CD) | headless + a risk-calibrated prod gate (DORA-first) | AI consumes, does not own | **the prod gate (hard on the irreversible)** |
| Operations | human-owned telemetry + on-call | no system / runtime context | **owning the system model** |
| Documentation | docs-as-context (code = truth) | cognitive debt; setup hallucinations | **generation pace <= comprehension pace** |

[Gold callout]
The vendor names from sections 1–6 are **replaceable**; the leading practice, the failure mode and the human's point in this summary are **durable** — they rest on the character of the phase's complexity, not on product names. Every cell is **derived** from a section covered, not assigned — the vendor column is deliberately not repeated so that the table cannot read as a ranking of tools.

## Speaker notes

This is the lecture's main summary table, and it holds the key idea of the whole course on reliable AI development. The rows are the lifecycle phases in order. But the columns are arranged in a principled way: the leading column here is not "AI's strength" and not a vendor name, but each phase's leading methodical practice. Next come the phase's characteristic failure mode and the point where the human is required. There is no vendor column in this summary at all — not because vendors do not matter, but because they have already been named in prose in the corresponding sections of the chapter, and a fifth column would read as a ranking of tools. The frame of the matrix is the phase skeleton, where each phase has a human-owned artifact and a human gate [2].

Let us walk through how to read a row with an example. Requirements: the leading practice is spec-driven, spec before code; the failure mode is prompt-and-pray and the overclaim "spec equals truth"; the human is required where it is decided what to build. Architecture: the practice is ADR plus fitness functions plus architecture-as-code; the failure is poisoned context in the absence of management; the human is at the choice of forks under trade-off. And so for each phase up through documentation.

Why the matrix is built exactly this way — because it will outlive the change of any vendor. In a year or two the vendor names given in prose in sections one through six will change, but the leading practice, the failure mode and the point of the required human will remain, because they rest not on products but on the character of the phase's complexity: where essential complexity dominates, there the human leads, and that does not go out of date. The matrix is ordered by the load-bearing DORA lens — "AI amplifies what is already there" [1]: the tool multiplies the existing practice rather than replacing it. And another point important for trust: each cell is not assigned from above but derived from the section covered — the matrix folds what has already been proven into one screen, with which an engineer names, for any dev task, its phase, the appropriate practice, and the point where one cannot do without a human.
