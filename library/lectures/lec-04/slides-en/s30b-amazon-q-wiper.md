---
id: s30b
type: case_study
section: "Section 5. Review + Security — the discipline of skepticism"
duration_min: 3
assertion: "A third, mechanically separate failure class: trust is needed not only in what the agent produces or reads, but in what the agent itself is made of — an unaudited contributor merged a malicious system prompt straight into an official Amazon Q Developer release"
learning_goal: "The supply-chain risk of the AI tool itself (not only of its output or its input) — a third failure mechanism next to slopsquatting and CamoLeak"
learning_outcomes: [LO1, LO7]
chapter_ref: "§5.6 [for-slide-s30b]"
references: [amazon-q-wiper]
in_bucket: true
verify_day_of: true
visual_brief: >
  case_study: left — an Ocean rounded box with the chronology (icon package-x): July 2025, an unaudited outside
  contributor merged a PR carrying a "system cleaner" system prompt (aws s3 rb, stopping EC2, deleting IAM users)
  into the official VS Code extension release v1.84.0, ~1 million developers; patched in v1.85.0; the attack failed
  technically (formatting broke execution) — luck, not control. Right — a "third class" panel (icon layers):
  slopsquatting = trust in a package name · CamoLeak = trust in someone else's untrusted text in the context ·
  Amazon Q = trust in the supply chain of the tool ITSELF. Gold callout — "review is needed not only for the code
  your agent writes, but for the code the agent itself is made of".
interaction: none
---

# Visible content

## Title bar
Trust is also needed in what the AI tool itself is made of

## Body
[Left — the chronology]

**July 2025.** An unaudited outside contributor merged into the open repository of the **Amazon Q Developer extension for VS Code** a pull request carrying a "system cleaner" system prompt: delete local files, wipe cloud resources (`aws s3 rb`, stopping EC2, deleting IAM users).

The prompt passed review and shipped in release **v1.84.0** — reaching roughly **1 million** developers — before the **v1.85.0** patch.

The attack failed technically (the prompt's formatting broke command execution, no customers were affected) — that is **luck, not control**.

[Right — the third class]

**Three mechanically different fronts of one phase:**

**Slopsquatting** — trust in the **package name** that AI advice recommended.

**CamoLeak** — trust in **someone else's untrusted text** (a PR comment) inside the agent's context.

**Amazon Q** — trust in the **supply chain of the tool itself**: not in what the agent produces or reads, but in what it is made of.

[Gold callout]
Review is needed not only for the code your agent writes, but for the code the AI tool itself is made of — which includes trusting its own contribution-intake process, invisible to you.

## Speaker notes

A third example of the same family, separate in mechanism — neither prompt injection during the agent's work nor a hallucinated package name, but an untrusted contribution to the product itself. In July 2025 an unaudited outside contributor merged into the open repository of the Amazon Q Developer extension for VS Code a pull request carrying a system prompt instructing the model to behave as a "system cleaner": delete local files and wipe cloud resources — remove S3 buckets, stop EC2 instances, delete IAM users.

The prompt passed the vendor's review and shipped in official release 1.84.0, reaching roughly one million developers — the extension's entire audience — before it was found and patched in version 1.85.0. The attack itself failed technically: the prompt's formatting broke command execution, and no customer systems were harmed. But that is luck, not control — the vendor's review process let a malicious PR from an unaudited contributor through, straight into an official release of an AI tool used by a huge number of developers.

It is worth naming this explicitly as a third, mechanically separate class next to slopsquatting and CamoLeak, which we just went through. Slopsquatting exploits trust in a package name that AI advice recommended. CamoLeak exploits trust in someone else's untrusted text that reached the agent's context. Amazon Q is trust in the supply chain of the tool itself: not in what the agent produces, and not in what it reads, but in what it is made of. The lesson for an engineer using third-party AI extensions: trusting the tool also means trusting its own contribution-intake process, which is invisible to you; review is needed not only for the code your agent writes, but for the code the agent itself is made of.
