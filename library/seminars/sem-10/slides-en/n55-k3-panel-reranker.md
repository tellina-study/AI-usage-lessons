---
id: n55
type: mechanism_node_graph
duration_min: 0.75
assertion: "The reranker's request body is an ordinary chat-completions call: the model openai/gpt-4o-mini and a system prompt in Russian that directly names the task — 'a search-result reranker'"
learning_goal: "Layer 2 of Case 3, beat 3 of 3: a real configuration panel of the reranker node's request body, EXPANDED view. This system instruction is the direct cause of why the reranker sometimes spoils an already-correct result (a bridge to n57)."
visual:
  pattern: mechanism_node_graph
  figure: case3-n8n-reranker-panel-real.png
  primary: >
    A real screenshot of the expanded JSON field of the "LLM reranker
    (gpt-4o-mini)" node: `model: 'openai/gpt-4o-mini'`, system role —
    "You are a search-result reranker. You are given a question and N
    candidate excerpts..."
  backup: >
    Source of the frame: `stend/n8n-screenshots-raw/case3-reranker-
    panel.png` (an HTTP Request node → chat/completions, Body field →
    JSON), captured by `stend/n8n_shots.py` in the EXPANDED view. Crop —
    `rendered/compose_case3_n8n_shots.py`: the upper Method/URL/
    Authentication/Credential Type fields are NOT taken into the frame —
    this same HTTP Request node, pointed at the same OpenRouter
    credential, was already shown once and named in text on the panels of
    Case 1 (n16/n17/n18); a repeat breakdown would add nothing new, just
    the same thing again. The single substantive piece taken is "Specify
    Body: Using JSON" → the JSON field, where the MODEL'S NAME and the
    start of the system prompt are visible.

    FULL TEXT OF THE SYSTEM PROMPT (not fully visible on the frame,
    clipped by panel height; verbatim in the original —
    `stend/measure/case3_rerank_measure.py::rerank_llm`): "You are a
    search-result reranker. You are given a question and {N} candidate
    excerpts, numbered 1..{N}. Reorder the candidate numbers from most
    relevant to the question to least relevant. Reply with STRICTLY a
    JSON array of numbers — a permutation of all the numbers, with no
    explanations. Example answer: [3,1,4,2,5,6,7,8,9,10]" — with N=10
    (the merge node's TOP_N, n54). The user message —
    "Question: {question}\n\nCandidates:\n{numbered list of texts}".
    TRANSLATOR'S FLAG: the real stend run actually sent this prompt to
    gpt-4o-mini in RUSSIAN, not in this English rendering — the glossary
    note on this point (glossary.en.yaml "notes" list) says to translate
    quoted prompt content like any other text but flag that the real run
    used Russian; this note is that flag, the English above is the
    natural EN equivalent for the slide, not a claim about what was
    actually transmitted to the model.

    THE MODEL IS NAMED EXPLICITLY (C5): `openai/gpt-4o-mini` — visible
    right in the JSON body on the frame, with no call settings beyond the
    required ones (no explicit temperature). THE COST OF THE STEP,
    COMPUTED (not an abstract percentage): ~$0.00033 per call — more
    expensive than the entire keyword/vector search-and-answer pipeline
    of Case 1 (~$0.00005) — stend/raw/case3-rerank-results.json, n51.

    BRIDGE TO n57: the prompt asks the model to return a STRICT
    permutation of the numbers — it neither adds nor removes candidates,
    only rearranges the ten already given. This is the direct reason why
    the reranker physically cannot raise a document that wasn't among the
    top-10 candidates before it (the nuance about the question with
    vector at 26th place, n57), and why it sometimes moves an
    already-correct result to the wrong place (the nuance about the
    question "An example of water barriers?", n57): the model reads only
    those ten texts and decides anew, not knowing that one of them was
    already right.
---

# The real panel: the reranker's request body

## Assertion

"You are a search-result reranker" — a system role in Russian, right inside the body of an ordinary chat-completions request.

## Visual

> "You are a search-result reranker. You are given a question and 10 candidate excerpts, numbered 1..10. Reorder the candidate numbers from most relevant to the question to least relevant. Reply with STRICTLY a JSON array of numbers..."

## Speaker notes

Here's the expanded request-body field of that same rerank node we just saw from the outside, on the canvas. The "Body Content Type" field is set to JSON, and inside is an ordinary `chat/completions` call body, which we've already seen several times today, only with a different model and different content.

The first thing literally visible on the frame is the model's name right in the request body: `openai/gpt-4o-mini`. There's no separate "rerank" parameter here at all — this is the exact same call form as any ordinary chat request, it's just that the system role describes the task differently than in the answering node.

And here's that role, visible on the frame: "You are a search-result reranker. You are given a question and ten candidate excerpts, numbered one through ten. Reorder the candidate numbers from most relevant to the question to least relevant." Next comes a strict requirement for the answer's format: strictly a JSON array of numbers, with not a single word of explanation, with an example of what the answer should look like. This requirement isn't decorative — a model that starts explaining its choice in words instead of returning a clean array of numbers will break the parsing done by the next node, and for exactly that case the rig has an honest fallback: if the answer can't be parsed, the order of the candidates stays as it was, unchanged, and no error is raised.

An important detail worth carrying forward from this frame. Exactly ten candidates are put into the model's input — exactly the ten that the previous merge node selected: not the whole corpus, not some arbitrary number. And it's asked to return a STRICT PERMUTATION of these same ten numbers: adding and removing nothing, only rearranging the order within the set already given. This directly explains the boundary of what the rerank can do, which we'll break down a bit further on: if the needed document wasn't among these ten candidates, the reranker physically cannot bring it in — it only works with what it was shown, and knows nothing about documents outside that list.

The cost of this call is a concrete figure: you can't call it an abstract percentage. About a third of a thousandth of a dollar per question — that's more expensive than the entire search-and-answer pipeline of the first case of this session combined. How this cost and this same strict permutation play out on specific questions — we'll break down in the nuances beat.
