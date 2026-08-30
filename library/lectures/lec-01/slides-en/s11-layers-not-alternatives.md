---
id: s11
type: assertion_visual
duration_min: 1.5
assertion: "Ways to build AI systems: not alternatives, but layers"
learning_goal: "A layered mental model for Section 3"
learning_outcomes: [LO1, LO4]
references: [anthropic-2024-effective-agents, weng-2023-agents]
visual:
  pattern: nested_layers_bottom_aligned
  primary: "4 nested layers sharing a common bottom edge (Model → Chat → Agent → Application). Component labels in the top strip of each layer on a teal-tinted background for better visibility."
---

# Ways to build AI systems: not alternatives, but layers

## Assertion

Ways to build AI systems: not alternatives, but layers.

## Visual

Four nested Ocean rounded boxes, aligned to a common bottom edge (each outer layer extends upward). Each layer contains, in its top strip on a teal-tinted background, a name + a list of the components it adds to the previous one (12pt italic, legible from a projector):

- Center — **Model**: stateless: input → model → output.
- Layer 2 — **Chat**: + dialogue UI · message-history memory.
- Layer 3 — **Agent**: + tools (API, retrieval, code) · planning · vector DB.
- Outer — **Application**: + AI inside the product · forms, buttons, integrations · prompts hidden from the user.

To the side — a compact text block («Each next layer includes the previous») and a gold callout «Choosing a layer is an engineering decision, not an alternative».

## Speaker notes

Before we walk through each of the four types of builds, it's important to lock in the key idea: these are not four alternative technologies, but four ways to build the same task with a layered structure. Each next level includes the previous one and adds new components.

The model is the most basic layer. Stateless inference on a single task. Data goes in, a prediction comes out. No interface, no memory, no tools.

Chat is the next layer. The same model, but wrapped in a text interface with dialogue memory within a session. The user writes a message, and the history of both messages is included in the context of the next request.

The agent is another layer. To chat we add the ability to call external tools — retrieval, the file system, an API, code execution — and the logic for planning a sequence of actions.

The application is the outer layer. From the outside it's an ordinary product with its own forms, buttons, and integrations. The AI works inside as one of the components. The user doesn't write prompts, doesn't talk to the model directly.

This nesting matters because many practical misunderstandings arise from trying to choose between the levels as though they were alternatives. In reality each successive wrapping is an engineering decision that adds capabilities and, at the same time, complexity, cost, and the potential for errors. The higher the level of the wrapping, the more room there is for bugs between the AI component and its surroundings.

Throughout the course we'll return to this layered model many times. When we look at a YOLO detector on a conveyor line, we stay at the model level. When we use ChatGPT for analytics — at the chat level. When we build an agent that reads two hundred PDFs — at the agent level. When we talk about Notion AI or YandexGPT in Search — about applications in which AI is just one of the components.
