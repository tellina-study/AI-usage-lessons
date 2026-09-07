---
id: s24
type: assertion_visual
section: "Section 4. Agents"
duration_min: 2.5
assertion: "A data map per feature: ZDR does NOT cover third-party/MCP; least-privilege is mandatory"
learning_goal: "ZDR does not cover the whole data chain of an agent system; the data map as a mandatory design step"
learning_outcomes: [LO7]
chapter_ref: "§4.8 [for-slide-s24]"
verify_day_of: true
---

# Visible content

## Title bar
"ZDR does not cover everything"

## Body
[Left — the ZDR boundary]
**ZDR** (zero data retention) covers the main model calls
**Does NOT cover:** Files API, batch, code-execution containers, the MCP connector, third-party integrations, consumer plans
An agent = model **+ tools** — and the tools are often exactly third-party/MCP

[Right — a legal precedent]
**NYT v. OpenAI (2025):** the court ordered ALL ChatGPT logs preserved as evidence
The contractual "30 days" policy proved **powerless** against a third-party court order

[Gold callout, bottom]
**"We have ZDR" ≠ "the data is protected across the whole chain."** The more agentic the architecture, the more data passes through uncovered links.

[Panel — the rule]
A data map per feature BEFORE production: which data, through which link, with what retention, which links are third-party. Regulated data — only ZDR/BAA or on-prem.

## Speaker notes

"We have ZDR turned on, so the data is protected" — a typical and dangerous oversimplification when designing an agent system. ZDR, zero data retention, is a mode in which the provider does not store the content of requests and responses after processing, but it covers far from the whole chain. At leading vendors, ZDR extends to the main model calls but does not cover a whole set of adjacent capabilities: the Files API, batch processing, code-execution containers, the MCP connector, third-party integrations, and consumer pricing plans. Here lies the trap specifically for agent systems: an agent is by definition a model plus tools, and the tools are again and again exactly third-party services or MCP servers — precisely the links that ZDR does not cover. The more "agentic" the architecture becomes, the more data passes through links that live outside the protection of zero retention.

The second fact, which breaks naive confidence in a contractual retention policy, is the New York Times v. OpenAI case. In the course of the litigation, a federal court ordered OpenAI to preserve absolutely all ChatGPT logs as potential evidence, regardless of what was written in the company's own policy. The provider's stated policy of "we delete after thirty days" proved wholly powerless before a court order in a dispute entirely external to the client. Hence the practical conclusion: data that has left your perimeter starts to live by rules you do not control, and a provider's promise is a description of normal conditions, not a guarantee for every case.

The design rule that follows from both facts: before releasing a feature into production you need to build a data map — which data exactly passes through which link of the chain, what the link's real retention policy is, and which links belong to a third party at all. For regulated or highly sensitive data the only reliable option is to work only through links with ZDR or a signed data-processing agreement, or to deploy the model on your own infrastructure. "We turned ZDR on" is not a project checkbox but one item from a map you need to build in full.
