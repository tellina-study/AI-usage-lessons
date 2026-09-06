---
id: s23b
type: summary
section: "Section 4. Agents"
duration_min: 3
assertion: "A catalog of 10 CLASSES of failure as a table: class→case→lesson (188 of 344 — the agent broke it itself)"
learning_goal: "The learning unit is the failure class, not the individual case; the scale of the 'agent broke it itself' class"
learning_outcomes: [LO7]
chapter_ref: "§4.10 [for-slide-s23b]"
interaction: none
---

# Visible content

## Title bar
"Failure catalog: 10 classes"

## Body
[Scale panel, top]
Of **7,246** documented AI incidents — **344** are enterprise-relevant; of those, in **188 (≈55%)** an autonomous system did the harm **itself, without an attacker**

[Class table — compact, 10 rows]

| Class | Case | Lesson |
|---|---|---|
| Destruction + over-privilege | PocketOS | The system prompt is not a security control |
| Zero-click injection | EchoLeak | The "triad": data+content+egress |
| Runaway cost | $48k/14h, $1.3M/30d | No success criterion → it will not terminate |
| Supply chain (hallucination) | Slopsquatting 19.7% | Do not trust package names without verification |
| MCP rogue server | postmark-mcp | MCP = supply chain without an inventory |
| Multi-agent cascade | 61% from upstream | Where it broke ≠ where it showed up |
| Legal liability | OLG Hamm, Air Canada | "The bot answered" is not a defense |
| Loop without a budget | $4,200/63h | Without a limit — it is executed literally |
| Error accumulation | reliability compounding | p^n, not averaging |
| Multi-agent fragility | Cognition | Worse than a single linear agent on dependencies |

[Gold callout, bottom]
**The learning unit is the CLASS of failure, not a date or a sum.** On meeting a new incident — name its class, the class determines the countermeasure.

## Speaker notes

The agent loop plan-act-check-repeat has four points of failure, and next we work through these modes in dated cases — each with a lesson and an alternative. But before going through the cases, it is important to fix the way to read the whole catalog: the learning unit here is the failure class, not the individual incident; the concrete cases are illustrations of a class, not material for memorizing dates and sums. On meeting a new incident in practice, the useful skill is to name which failure class exactly it belongs to, because the class determines the countermeasure: restricting privileges, isolating untrusted content, validation between steps.

The scale is set by the anchor number: of seven thousand two hundred forty-six publicly documented AI incidents, three hundred forty-four are selected as relevant to business systems, and already among those, in one hundred eighty-eight — about fifty-five percent — an autonomous system did the harm right in production without any attacker in the chain: the agent broke everything itself, with no one else's malice. This changes the intuitive picture of the risks of agent systems: most often the danger comes not from an external attack but from the agent's own logic meeting a situation no one anticipated.

The ten classes from the table cover the whole failure map of the section: a destructive action combined with excessive privileges, injection via untrusted content without a single click by the victim, uncontrolled cost growth, delivery of malicious code through hallucinated package names, an untrusted MCP server, a cascade of errors in a multi-agent system, the company's legal liability for the words of its own bot, a loop without budget limits, the mathematical accumulation of errors along a chain of steps, and the general fragility of multi-agent architectures on dependent subtasks. Each of them will be worked through separately with a concrete case, but keep in mind the key point: the goal is to recognize the class, not to remember the numbers by heart.
