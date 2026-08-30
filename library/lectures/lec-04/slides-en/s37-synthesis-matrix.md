---
id: s36
type: schema_matrix
section: "Section 7. Synthesis — discipline by phase"
duration_min: 3
assertion: "The lecture's matrix: phase × leading practice × failure mode × where the human is required; the vendor is the last, secondary, replaceable column — this removes the vendor catalog"
learning_goal: "SYNTHESIS matrix reframed (#264): phase × leading practice × where the human; vendor is a secondary column"
learning_outcomes: [LO1, LO4, LO7]
chapter_ref: "§7.1 [for-slide-s36]"
verify_day_of: true
visual_brief: >
  schema_matrix 8 rows (phases) × 5 columns. The KEY pivot #264: the leading column is "Leading practice", NOT the vendor.
  Columns: Phase · Leading practice (Primary mid, dominant) · Failure mode · Where the human is required (gold-accent column) · Vendor (LAST, muted, "secondary/replaceable").
  Fill >=75% (every cell filled, <=2 lines, font >=12pt axis / >=14pt cell). Single language EN. The vendor column is visually muted/compressed (light) — to emphasize its secondary status.
  An anchor icon per phase (Lucide) in the first column. Gold — the "where the human" column + caption "only the illustration column will be replaced; practice/failure mode/human are stable".
  Each cell is DERIVED from the section covered, not assigned. Source references — inline right at the material (definition/claim/recommendation), NOT in a bottom footer; small and muted: vendor names volatile; practices stable.
interaction: none
---

# Visible content

## Title bar
The lecture's matrix: the practice leads, the vendor is a replaceable column

## Body
[schema_matrix — 8 phases × 5 columns; the leading column = practice, the vendor last and muted]

| Phase | Leading practice | Failure mode | Where the human is required | Vendor (secondary) |
|---|---|---|---|---|
| Requirements | spec-driven: spec before code | prompt-and-pray; "spec = truth" | **deciding what to build** | Kiro, Spec-Kit, plan mode |
| Architecture | ADR + fitness functions + architecture-as-code | poisoned context without management | **choosing the forks under trade-off** | (no product; ADR/Structurizr) |
| Implementation | explore→plan→code→commit + harness | the 70% problem; "almost right" | **reviewing the diff + merge** | Cursor, Junie, Codex/Jules/Copilot |
| Testing | TDD: test-as-spec + a deterministic gate | "all green" lies; coverage != defects | **what the test asserts** | AWS Q /test, Qodo, hook gate |
| Review + Security | fresh-context; least-priv+sandbox+egress+SAST against the Lethal Trifecta | complacency; vulnerable code + false confidence | **a second pass + threat modeling** | Copilot review; GitHub SAST; Big Sleep |
| Delivery (CI/CD) | headless + prod gate (DORA-first) | AI consumes, does not own | **the production gate** | (Actions; `gh`/CLI) |
| Operations | human-owned telemetry + on-call | no system/runtime context | **owning the system model** | AWS Q CloudWatch |
| Documentation | docs-as-context (code = truth) | cognitive debt; setup hallucinations | **generation pace <= comprehension pace** | Confluence AI, Q /doc |

[Gold callout]
Only the **illustration** column will be replaced. The leading practice, the failure mode, and the human's point are **stable** — they rest on the character of the phase's complexity, not on product names. Each cell is **derived** from the section covered, not assigned.

## Speaker notes

This is the lecture's main summary table, and it holds the key idea of the whole course on reliable AI development. The rows are the lifecycle phases in order. But the columns are arranged in a principled way: the leading column here is not "AI's strength" and not a vendor name, but each phase's leading methodical practice. Next come the phase's characteristic failure mode and the point where the human is required. And only as the last, secondary, deliberately muted column comes the vendor illustration. The frame of the matrix is the phase skeleton, where each phase has a human-owned artifact and a human gate [2].

Let us walk through how to read a row with an example. Requirements: the leading practice is spec-driven, spec before code; the failure mode is prompt-and-pray and the overclaim "spec equals truth"; the human is required where it is decided what to build; the vendors — Kiro, Spec-Kit, plan mode — come last and are interchangeable. Architecture: the practice is ADR plus fitness functions plus architecture-as-code; the failure is poisoned context in the absence of management; the human is at the choice of forks under trade-off; and characteristically, there is no specialized product here at all. And so for each phase up through documentation.

Why the matrix is built exactly this way — because it will outlive the change of any vendor. In a year or two the names in the last column will change, but the leading practice, the failure mode, and the point of the required human will remain, because they rest not on products but on the character of the phase's complexity: where essential complexity dominates, there the human leads, and that does not go out of date. The matrix is ordered by the load-bearing DORA lens — "AI amplifies what is already there" [1]: the tool multiplies the existing practice rather than replacing it. And another point important for trust: each cell is not assigned from above but derived from the corresponding section covered — the matrix is a folding of what has already been proven into one screen, with which an engineer names, for any dev task, its phase, the appropriate practice, and the point where one cannot do without a human.
