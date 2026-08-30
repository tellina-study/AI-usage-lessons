---
id: s16
type: process
duration_min: 2
assertion: "How chat works: the 6 steps of the cycle"
learning_goal: "Remove the magic of chat + control via the system prompt + the context-window limit"
learning_outcomes: [LO1, LO4]
references: [anthropic-2024-effective-agents]
visual:
  pattern: dialog_cycle_compact
  primary: "Eyebrow pill «CHAT» at the top; compact diagram of the dialog cycle: USER on the left in two roles (sender and receiver), in the middle two horizontal blocks (Message → LLM → Response → USER), on top — System prompt merging into the Message via a gold arrow pointing down. Below the Response — a growing «history» block labeled «the whole text again on every step». On the right, two gold callouts: «Control via the system prompt» and «Limit — the context window (128k–1M tokens)». At the bottom — a takeaway without the «not magic» tail."
---

# How chat works: the dialog cycle

## Assertion

How chat works: the dialog cycle.

## Visual

Eyebrow pill «CHAT» in the top-left corner — the same pattern as s15/s17/s18/s19/s19a. A compact diagram of the dialog cycle. In the left column — a user icon in two roles (sender on top, receiver below). In the center — two horizontal blocks: «Message» (user input) and «Response» (model output), one above the other. On the right, a large blue block «LLM / model». From the «System prompt» at the top, a gold arrow points down and merges with the «Message» — visually showing that the prompt is attached to every request. Arrows: USER → Message → LLM (rightward), LLM → Response → USER (leftward). Below the Response — a cumulative visual «history» block (a growing bar with several segments) with an explicit label «the whole text again on every step» — clearly showing that the model reads the entire history in full, not just the increment. In the right column, two gold callouts: «Control via the system prompt — the developer's engineering lever» and «Limit — the context window: 128k–1M tokens; the old stuff drops out». At the bottom, a takeaway in italics: «Chat is a "gather → feed → append → show" pipeline» (without the «not magic» tail).

## Speaker notes

Chat is convenient to discuss on an everyday level: you ask a question, you get an answer. But behind that simple experience sits a very concrete technical cycle. Understanding this cycle removes the magic and gives you two practical skills: how to control the chat via the system prompt, and how to explain why chat «forgets» old messages.

The six steps of the cycle. First — the user types text into the chat window: a question, an instruction, a fragment of data.

Second — the system takes the entered text and attaches it to the system prompt. The system prompt is a set of instructions defined in advance by the developer: «You are the corporate assistant of company X. Answer in Russian. Do not give legal advice. If you don't know — say "I don't know".» In addition, the entire current chat history from the start of the session is mixed in.

Third — the full assembled package, that is the system prompt plus the history plus the new message, is sent to the LLM as one large piece of text. The model does not «remember» the previous conversation — it receives it anew each time as part of the input.

Fourth — the model generates the response token by token, based on the probability distribution over the next token given the context.

Fifth — the model's response is appended to the chat history on the system side. From this point on it is part of the context for every subsequent request in this same session.

Sixth — the response is shown in the chat interface. The user reads it, replies, and the cycle repeats from step one. But now the history is already larger, and on the next request the LLM will receive the whole set: the system prompt plus the previous question-answer pairs plus the new message.

Two practical consequences follow from this cycle. First — the system prompt is an engineering lever. Through it the developer sets the frame of the chat: tone, role, constraints, mandatory response formats. The very same ChatGPT behaves differently in the role of a corporate assistant versus a general-purpose helper precisely because of the system prompt.

Second — every model has a context window: the maximum number of tokens per request. For modern models this is tens and hundreds of thousands of tokens. When the chat history stops fitting into the window, the old messages drop out. That is why chat «forgets» details from the beginning of a long conversation.
