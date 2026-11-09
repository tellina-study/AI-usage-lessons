---
id: n19
type: content
duration_min: 1.0
assertion: "The requester sees no difference — Olga sees what each next answer costs as the base grows"
learning_goal: "Case 1's result and generalization: what the requester sees vs. what Olga sees, and the principle that carries over to any orchestrator (not just n8n)."
visual:
  pattern: content
  primary: >
    Two tiles side by side: "to the requester," "to Olga" — then a
    formula tile with the transferable principle.
  backup: >
    Text — SETKA-KEYSOV.md Case 1, "Result and generalization," verbatim.
---

# What Olga sees, and what the requester sees

## Assertion

On the outside, the answer doesn't change. On the inside, what changes is what each next answer costs as the base grows.

## Visual

To the requester this is invisible entirely — they get an answer that's the same quality or better. Olga sees something different: at the current base size (while it's still small) the difference is barely noticeable, but it's exactly this choice that decides what each next answer will cost once the base grows.

> **The principle carries over to any orchestrator: n8n here is just an example. A prompt that holds the entire knowledge base grows in cost linearly with the base's size and doesn't guarantee rising accuracy — an external store, from which only the needed chunk gets pulled on every question, keeps the cost and the prompt's volume constant no matter how many documents have piled up.**

## Speaker notes

Let's separate what the requester sees from what Olga sees — these are two different observers of the same solution, and they shouldn't be mixed up.

To the requester, the person who wrote in to the training center, the difference between prompt-stuffing and a separate store is entirely invisible. They get an answer — the same quality or, as we just saw in the numbers, even better — and it doesn't matter to them which method the process used to put that answer together. From the outside, the solution looks the same regardless of what's happening inside.

Olga sees something different — over time. While the base is small, the difference between the two approaches is barely felt — we'll see that as a number in the next beat, on the boundary of applicability. But it's exactly which approach gets chosen that decides what each next answer will cost as the base grows. This isn't a difference in whether the process works or not today — it's a difference in how it will behave six months from now.

And here's the principle worth taking away from this case as a whole — n8n here is just an example. A prompt that holds the entire knowledge base grows in cost linearly with the base's size, and it doesn't guarantee rising accuracy along with it — we saw the opposite, accuracy falling. An external store is built differently: only the needed chunk gets pulled from it on every question, which is why the cost and the prompt's volume stay constant regardless of how many documents have piled up in that store. This observation is about architecture; the specific tool has nothing to do with it. It will stay true if the same task gets built tomorrow in any other process orchestrator.

One more thing that's easy to lose behind the numbers. The decision to move the base out into a separate store gets made once, in advance, and doesn't get revisited every time the base grows. That means: the price of this decision is paid once, up front — on preparation: splitting the documents, computing embeddings, setting up the search node. After that, the process works with any volume of base equally cheaply, with no hidden tax on every call, and that's exactly what distinguishes an architectural decision from a temporary patch that would have to be redone at every next round of growth.
