---
id: s05c
type: assertion_visual
section: "Section 1. The prompt and its limits"
duration_min: 3
assertion: "The protocol roles system/user/assistant ≠ a persona role; the priority of system is a tendency (~63.8%), not a boundary; STI forges a role"
learning_goal: "Separate the persona role from the protocol roles; show that the priority of system is a statistical habit, not a defense, and name a concrete vulnerability (STI)"
learning_outcomes: [LO7]
chapter_ref: "§1.2 [for-slide-s05c]"
verify_day_of: true
---

# Visible content

## Title bar
"Protocol roles: not a persona, but dialogue markup"

## Body
[Top bar — the distinction]
**Persona role** ("you are a lawyer") — text inside a message, affects tone
**Protocol role** `system` / `user` / `assistant` — markup for "who is speaking," the structure of the dialogue

[Left — why they are needed + priority]
Dialogue structure · behavior control · **learned priority** of the system role
GPT-4o respects the priority in ≈ **63.8%** of cases; special tuning raised it 84.1%→94.1% — but **not 100%**

[Right — mechanics + vulnerability]
The model receives **one flat stream of tokens**; roles are special tokens of the chat template (ChatML, Llama, Anthropic — each has its own format)
**Special Token Injection (STI):** a forged role string in external content → ChatInject: ASR on AgentDojo 5.18%→32.05%, up to 88.3% on Llama-4

[Gold callout, bottom]
**The priority of the system role is a tendency, not a security boundary.** Defense: escape special tokens in incoming content + check the chat template of a local model.

## Speaker notes

In prompting the word "role" has two independent meanings. A persona role — "you are a lawyer" — is text in a message and affects tone. The protocol roles system/user/assistant are markup for the structure of the dialogue; not text but markup for "who is speaking." The first answers "in what tone," the second "whose turn this is."

Protocol roles exist so the model can tell the developer's instruction apart from the user's input and from its own answers. The model is trained to treat the system role as more authoritative — but this is a statistical habit, not an architectural guarantee. A study showed that GPT-4o obeys the priority of the system instruction in only 63.8% of cases. Special training raised this to 94.1% — but not 100%. Priority is a tendency, not a security boundary.

Physically the model receives a stream of tokens with role markup. The list of messages is assembled by a chat template, which wraps every message in special tokens. Hence the vulnerability: if external content — a web page, a file, a letter — contains text resembling role markup, the model may interpret it as its own turn. This is the Special Token Injection attack: a forged string imitating the start of an assistant turn is inserted into external content. A study on agent scenarios showed the attack success rate rising several-fold, and that asking the model "do not give in" barely protects it. Real defense is escaping special tokens in incoming content and checking the chat template for local models.

Special Token Injection is a particular case of prompt injection. The full treatment of injection as a class of attacks on an agent comes in the section on agents (agent security) — together with defense measures at the architecture level.
