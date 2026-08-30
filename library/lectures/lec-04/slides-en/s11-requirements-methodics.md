---
id: s11
type: assertion_visual
section: "Section 1. Requirements — the first artifact"
duration_min: 3
assertion: "How to run requirements: STRUCTURE (stories+criteria, EARS, functional/non-functional, requirements→design→tasks) and PROCESS (interrogatory LLM, sign-off gate, versioning, syncing) — the tools are secondary"
learning_goal: "Recommendations for running requirements: structure (how to write) + process (how to maintain); the human owns \"what to build\""
learning_outcomes: [LO7, LO4]
chapter_ref: "§1.2 [for-slide-s11]"
references: [spec-kit, ears, fowler-intent, fitness-fn, adr, anthropic-playbook]
verify_day_of: true
visual_brief: "Two columns in an Ocean rounded box: STRUCTURE (stories+acceptance criteria [3]; EARS [7]; functional/non-functional [6]; requirements→design→tasks [3]) and PROCESS (interrogatory LLM [4]; review/sign-off [1]; versioning in the repo [3]; syncing like an ADR [9]). Each item with a [N] marker. A bottom numbered clickable ref list. Gold judgment: EARS+decomposition+requirements-as-check+sign-off are durable; the hype — \"a command pipeline = requirements discipline\"."
interaction: none
---

# Visible content

## Title bar
How to run requirements: structure (how to write) + process (how to maintain)

## Body
[Two columns in an Ocean rounded box — STRUCTURE on the left, PROCESS on the right]

**STRUCTURE — how to write requirements**
- **User stories + acceptance criteria** [3] — "As a <role>, I want <goal> so that <benefit>" + verifiable criteria for each story.
- **EARS notation** [7] — "WHEN <trigger>, the system SHALL <response>" (Mavin, 2009): removes "should/may", makes the requirement verifiable and AI-readable.
- **Functional vs non-functional** [6] — behavior separately from characteristics (latency / cost / security); the non-functional ones are enforced by fitness functions.
- **requirements → design → tasks** [3] — the enforced order of three files (Kiro / Spec-Kit); Definition of Done — small independently-testable units.

**PROCESS — how to maintain requirements**
- **Elicitation: the interrogatory LLM** [4] — the model ASKS you questions (Fowler, "Interrogatory LLM"), surfacing unstated assumptions, rather than "prompt-and-pray".
- **Review and sign-off BEFORE code** [1] — requirements are reviewed and signed off by a human before generation; accept/reject of the spec = "the merge".
- **Versioning next to the code** [3] — requirements are diffable Markdown in the repository, not in a wiki/chat; a durable artifact, not a fleeting prompt.
- **Syncing on change** [9] — keep them current like an ADR; the human owns "what to build", AI helps with structure and completeness.

[Judgment plate, gold]
Durable pattern: EARS + decomposition + requirements-as-check + human sign-off will outlive any tool. The hype: "our command pipeline = requirements discipline".

## Speaker notes

The "requirements before code" discipline is not "write a bigger document." The methods have concrete recommendations of two kinds: how to structure requirements and how to run them over time. Let's gather them as a practice, not as a set of commands of a particular tool.

First, structure. First — user stories with verifiable acceptance criteria: "as such-and-such a role, I want such-and-such a goal so as to get such-and-such a benefit." Second — Mavin's EARS notation of 2009, "Easy Approach to Requirements Syntax": five templates, the key one being "WHEN trigger, the system SHALL response"; EARS removes vague "should/may" and makes the requirement both verifiable and readable for the model [7]. Third — explicitly separate functional requirements (what the system does) and non-functional ones (latency, cost, security); the non-functional ones are then enforced by fitness functions, which get a separate discussion in architecture [6]. Fourth — the enforced order of three files: requirements, then design, then tasks, with versioning next to the code [3], and the Definition of Done is framed as small independently-testable units: not "do authentication", but "create a registration endpoint that validates the email format".

Now the process. Requirements elicitation: instead of one vague prompt, let the model interview you — Fowler calls this the "Interrogatory LLM": the model asks questions and surfaces unstated assumptions [4]. Next — review and sign-off: requirements are reviewed and signed off by a human before code generation, and it is exactly this accept/reject that plays the role of "the merge" [1]. Versioning: requirements live as diffable Markdown right in the repository next to the code, not in a wiki or chat [3]. And syncing: requirements are kept current the same way as an ADR — an outdated requirement silently rots [9]. The through-line thesis: the human owns "what to build", AI helps with structure and completeness; the tools that execute all this are replaceable, while the load-bearing thing is these recommendations.
