---
id: s35b
type: assertion_visual
section: "Section 6. Delivery · Operations · Documentation"
duration_min: 3
assertion: "The documentation toolchain mechanically repeats the 'bright spot' thesis: AI retells what already exists in the code or the thread — visible both in the SaaS layer (Confluence AI, AWS Q /doc) and in the code-first alternative through an installed skill with no vendor lock-in"
learning_goal: "What docs-as-context looks like in practice: the 3 capabilities of Confluence AI, AWS Q /doc (input = code, not prompt), the code-first alternative through a skill"
learning_outcomes: [LO1, LO7]
chapter_ref: "§6.3 [for-slide-s35b]"
references: [eesel-confluence-ai, aws-q-doc]
verify_day_of: true
visual_brief: "Two Ocean rounded boxes: left — the SaaS vendor layer (Confluence AI: summarization / generation / Q&A search; AWS Q /doc: input = code, diagrams from IaC, closed loop code→diff). Right — the code-first alternative (an installed skill: README/ADR/inline comments from the project structure; a community pattern, not an official one). Icons: bot (Confluence AI), file-code (AWS Q /doc + skill). Gold — the vendor layer illustrates the mechanics of the 2026 stack, it is not a recommendation; the same pattern is available through a skill without SaaS."
interaction: none
---

# Visible content

## Title bar
The documentation toolchain in practice: the input is code, the output is a retelling of what was already said

## Body
[Left — the SaaS vendor layer, Ocean rounded box]

**Confluence AI (Atlassian Intelligence).** Three capabilities: **summarizing** a long thread into a short digest; **generating and transforming** a draft from a prompt; **Q&A search** over the knowledge base in natural language (a RAG-like pattern over the corporate base).

**AWS Q Developer `/doc`.** A mature feature (announced December 2024): the agent analyzes the **codebase** rather than retelling the prompt. It can build infrastructure diagrams from IaC files (Terraform/CDK) — a direct link to the already-introduced principle of architecture-as-code. A closed loop: the code changed → a diff in the documentation is proposed.

[Right — the code-first alternative, Ocean rounded box]

**The code-first alternative is the coding agent itself.** An installed **skill** ("Code Documentation Skill", "README Generator") analyzes the project structure, the dependencies and the code patterns, and generates README / ADR / inline comments.

*Honestly: this is a community pattern, not a single official skill from the Anthropic repository. Onboarding documentation is a good skill candidate by the heuristics already introduced: a repeated instruction + it needs progressive disclosure.*

[Gold callout]
The vendor-specific layer (Confluence AI/Rovo, AWS Q `/doc`) illustrates the mechanics of the current 2026 stack; it is not a recommendation of one vendor: the same pattern is available through an installed skill on top of the coding agent you already use, with no SaaS lock-in.

## Speaker notes

We have already named the documentation vendors — Confluence AI, AWS Q slash-doc, JetBrains — but not the mechanics. Let us look at what happens inside each of them, and at the code-first alternative, which sits closer to the practice of this course.

Confluence AI, the general AI layer over Atlassian's products, offers three capabilities. Summarization: a long thread is folded into a short digest. Content generation and transformation: a draft page from a prompt, or a rewrite of existing text in a different tone. Q&A search over the knowledge base: a question in natural language instead of keywords, with the answer assembled from scattered pages — the same RAG-like pattern over a corporate base, including decoding the company's internal jargon.

AWS Q Developer with the slash-doc command is a mature feature, announced in December 2024, not a fresh experiment. The agent analyzes the codebase and generates documentation from it — the input is the code itself, not a retelling of the prompt. It can create infrastructure diagrams if the project contains infrastructure-as-code files — a direct link to the already-introduced principle of architecture-as-code: the agent reads the infrastructure-as-code that already exists and derives a diagram from it rather than inventing an architecture from a description. It can also review new code and propose documentation updates — a closed loop: the code changed, a diff in the documentation is available.

The code-first alternative: instead of SaaS, the same job is done by the coding agent through an installed skill — a pattern we have met before. A skill such as "Code Documentation Skill" analyzes the project structure and code patterns and generates README, ADR and inline comments. The honest caveat: this is a community pattern, not an official skill from the Anthropic repository — "the pattern exists" does not mean "a built-in feature out of the box". Onboarding documentation is a good skill candidate on two heuristics at once: one instruction gets copied to a new developer again and again, and the material is not needed at every step.

The durable pattern is the very fact that documentation, as accidental complexity, has an input that already exists — code, a thread, a decision — and AI retells what was said rather than inventing intent. The vendor-specific layer illustrates the current stack; it is not a recommendation.
