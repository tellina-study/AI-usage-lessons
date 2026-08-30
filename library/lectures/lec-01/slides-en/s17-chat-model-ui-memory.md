---
id: s17
type: case_study
duration_min: 2
assertion: "Chat = model + interface + dialog memory"
learning_goal: "Chat as a layer; a corporate-chat case for making sense of a normative document"
learning_outcomes: [LO1, LO4, LO6]
references: [vciom-2025-oct, dam-2024-llm-chatbots]
visual:
  pattern: case_card_with_production_disclaimer
  primary: "Eyebrow pill «CHAT» at the top; a corporate-chat case on the left + a caveat for production systems on the right («pure chats are almost never used in production — almost everywhere they are extended into agents, at least for memory and RAG»)"
---

# Chat = model + interface + dialog memory

## Assertion

Chat = model + interface + dialog memory.

## Visual

Eyebrow pill «CHAT» in the top-left corner — the same pattern as s15/s16/s18/s19/s19a. On the left, an Ocean rounded box with a case: «An engineer receives an incomprehensible normative document and asks the chat to build a checklist for their own work». An illustration of the dialog, 2-3 lines in small type. On the right, a gold-tinted Ocean rounded box with a caveat for production systems: «Pure chats are almost never used in production. Almost everywhere they are extended into agents — at least for long-term memory and search over a corporate knowledge base (RAG). We'll break down the agent architecture on the next slide». At the bottom, a gold callout: «Choosing chat is choosing a point on the interaction scale, not the one right option».

## Speaker notes

Chat is a model wrapped in a text interface with dialog memory within a session. The user writes a message, the model answers, and the history of both messages is included in the context of the next request. This creates the feeling of a conversation and lets you refine the task step by step, which radically changes the usage pattern.

Today's chats are first and foremost LLM chats, though multimodal ones also exist: with the ability to pass images, audio, and files. You know the canonical products: ChatGPT, Claude, Gemini, DeepSeek Chat, GigaChat, YandexGPT, Mistral Le Chat. The differences between them are in quality for various tasks, in context-window length, in cost, in the availability of modalities — but the basic interaction pattern is the same.

Let's take a concrete example. An engineer receives an incomprehensible normative document — say, a technical spec from an adjacent department, full of references to standards and complicated wording. The task is to make sense of it and build a checklist for their own work. This is a typical case for chat: a one-off task that requires dialog, with clarifications along the way. Here you don't need a separate specialized model, because there is no stream of similar tasks. You don't need an agent, because there is no requirement to automatically open files and APIs. And there is no specialized application. Chat is the optimal tool.

An important caveat for production systems. Pure chats in the form they come «out of the box» — that is, just an LLM plus a UI plus a short session memory — are almost never found in a corporate environment. Almost everywhere real deployment is involved, the chat is extended into an agent: at least to store long-term memory across sessions, or to search for an answer in a corporate knowledge base via RAG (retrieval-augmented generation). The agent architecture — exactly what gets added to the chat — we'll break down on the next slide.

Choosing chat is an engineering decision about a point on the interaction scale: where the type of interaction with the AI is chosen correctly, the system works predictably.
