---
id: s33b
type: comparison
section: "Section 6. Delivery · Operations · Documentation"
duration_min: 3
assertion: "The AI multiplier works both ways inside one and the same phase: BT Group and Azure cut response times by orders of magnitude on top of a mature SRE practice, while the same class of AI simultaneously generates infrastructure-as-code that is insecure by default — restricting privileges does not protect against unsafe content inside the artifact"
learning_goal: "Going deeper into operations: where an AI copilot genuinely works (a mature platform) — and the symmetrical failure (IaC secure-by-default has not moved in 2 years)"
learning_outcomes: [LO1, LO7]
chapter_ref: "§6.1 [for-slide-s33b]"
references: [bt-group-incidentio, azure-triangle-ms, iac-insecurity-2026]
in_bucket: false
verify_day_of: true
visual_brief: >
  comparison, two columns. Left (gold accent, icon gauge) — "where the AI copilot works": BT Group MTTR
  ~2h→85s (~97% reduction) through alert correlation + automatic remediation from a runbook; Azure Triangle
  time-to-engage −91%, triage accuracy 97% — both on top of an ALREADY mature SRE practice. Right (warning
  accent, icon shield-alert) — "the same multiplier, the other side": AI-generated IaC (Terraform/K8s) secure
  by default ~55% (barely moved in 2 years, while syntactic correctness is >95%) · a 2026 benchmark of 6
  frontier models — 8.4% on security-checked tasks (a SEPARATE measurement, not the same trend — label it
  explicitly, otherwise the two adjacent numbers read as a contradiction).
  Round-6 (owner: "the security problems on this slide are not connected to the multiplier at all — what is the
  problem? more rollouts? more issues?"): the previous version put two facts side by side under a shared banner
  and never named the MECHANISM. Both columns now answer the same pair of questions in identical white insets —
  "what AI multiplies" and "where the gate is" / "there is no gate" — so it is visible that the multiplier is
  ONE AND THE SAME (volume × speed) and only the maturity of the gate differs. On the left what gets multiplied
  is an already-verified step (the runbook defines the permitted actions, telemetry shows the result); on the
  right it is an unverified artifact (the pipeline checks syntax, not security → more configurations → less
  attention on each → the unsafe one reaches production). Gold callout — "the problem is not that there are more
  rollouts but WHAT exactly is being multiplied".
interaction: none
---

# Visible content

## Title bar
The multiplier is volume: a mature gate multiplies what is verified, a missing gate multiplies what is unsafe

## Body
[Left — where the AI copilot works]

**BT Group** — **MTTR ~2h → 85s (~97% reduction)**
*MTTR (mean time to repair) — the average time to restore service after an incident*

**Microsoft Azure "Triangle"** — **time-to-engage −91%, triage 97%**
*time-to-engage — the time until the on-call engineer is engaged*

**What AI multiplies:** alert correlation and steps from a runbook written in advance.

**Where the gate is:** the runbook (a ready-made remediation script) defines the permitted actions, telemetry shows the result of every step. What is multiplied is work already verified — on top of an **ALREADY mature** operations practice (SRE).

[Right — the same multiplier, the other side]

**AI-generated IaC** (infrastructure-as-code) — **~55% secure by default**
*the share of tasks where the generated Terraform / Kubernetes code is secure out of the box, with no human edits; over 2 years the figure has barely moved. Syntactic correctness >95%.*

**A separate 2026 benchmark, a different measurement: 8.4%** on security-checked tasks.

**What AI multiplies:** the generation of configurations — many times more artifacts, and faster.

**There is no gate:** the pipeline checks syntax, not security. More configurations → less attention on each → the unsafe one reaches production.

[Gold callout]
The problem is not that "there are more rollouts" but **WHAT exactly is being multiplied**: BT multiplies a verified step, IaC generation multiplies an unverified artifact. The multiplier is the same; only the **maturity of the gate** differs.

## Speaker notes

These two examples widen the picture of the operations phase and, above all, show the mechanism behind the phrase "the multiplier works both ways".

Start with the positive pole. At BT Group, adopting an AI copilot for alert correlation and automatic incident remediation from runbook scripts written in advance cut the mean time to repair, MTTR, from roughly two hours to eighty-five seconds — about a ninety-seven percent reduction. In Microsoft's internal Azure "Triangle" system the time until the on-call engineer is engaged fell by ninety-one percent, with triage accuracy at ninety-seven. Both companies introduced the copilot on top of an already mature operations practice.

Now the mechanism itself, because without it the two columns look like nothing more than two facts standing next to each other. The multiplier is volume and speed: AI does the same work more often and faster. The question is what exactly falls under that multiplication. At BT it is alert correlation and steps from an already written runbook: the set of permitted actions is fixed in advance, and telemetry shows the result of each step. What is multiplied is work that has already been verified — hence the positive result.

The other side belongs to the same phase. AI-generated infrastructure-as-code is insecure by default: only about fifty-five percent of tasks yield secure code out of the box, and over two years that figure has barely moved, even though syntactic correctness exceeds ninety-five percent. In a separate 2026 benchmark, six models passed security-checked tasks in only eight point four percent of cases. Here what falls under the multiplier is the generation of configurations — many times more artifacts, and faster — but there is no gate on their security: the pipeline checks syntax, not safety. More configurations means less attention on each one, and the unsafe configuration reaches production. Restricting the agent's privileges does not protect against this: it limits what the agent may do, not what the artifact itself contains.
