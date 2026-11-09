---
id: n18
type: mechanism_node_graph
duration_min: 0.75
assertion: "The answer node's prompt explicitly forbids the model from going beyond the found chunk: 'Answer ONLY from the text below. If the answer isn't there — write \"no information\"'"
learning_goal: "Layer 2 of Case 1, beat 3 of 3: a real prompt panel for the Answer (RAG) node, EXPANDED view. This system instruction is the direct cause of the 'no information' answers we'll break down in the next beats (a bridge to n11)."
visual:
  pattern: mechanism_node_graph
  figure: case1-n8n-answer-panel-real.png
  primary: >
    A real screenshot of the expanded "Prompt (User Message)" field of the
    Answer (RAG) node: "Answer ONLY from the text below. If the answer
    isn't in the text — write "no information." Text: {{ $json.chunk }}".
  backup: >
    Frame source: `stend/n8n-screenshots-raw/case1-answer-panel.png` (the
    HTTP Request → chat/completions node, the Prompt (User Message)
    field), captured by `stend/n8n_shots.py` in EXPANDED view. Crop —
    `rendered/compose_case1_n8n_shots.py`: the top "Save time with an
    example" block and the prompt-source selector field were removed, as
    were the Require Specific Output Format / Enable Fallback Model
    toggles at the bottom (not used in this node). The prompt's own text
    wasn't changed by even one character — it's verbatim from
    `stend/harness2.py::llm_answer`, the call's system message.

    THIS INSTRUCTION IS THE SAME FOR ALL THREE ACTIONS (a C5 corollary):
    prompt-stuffing gets this same system instruction on top of the
    entire base's text, keyword and vector get it on top of a single
    found chunk (`{{ $json.chunk }}`). The difference between actions
    isn't in the model's instruction — it's in what text gets substituted
    into `{{ $json.chunk }}`: the whole knowledge base or one chunk.

    BRIDGE TO THE NEXT BEAT: it's exactly this line — "if the answer isn't
    in the text — write 'no information'" — that's the direct cause of
    why prompt-stuffing, at large base sizes, answers literally "no
    information" several times (n11/n10): not because the model isn't
    trying, but because it's explicitly allowed and instructed to say so
    if it can't find the fact. At a small base there's plenty to search
    through; at a large one, as the number of similar distractor
    documents grows, correctly locating its own fact inside a wall of text
    doesn't always succeed — and that's exactly when this instruction
    kicks in.
---

# The real panel: the answer node's prompt

## Assertion

The prompt is identical for all three actions: "answer only from the text below." The difference is what text actually gets substituted in.

## Visual

> "Answer ONLY from the text below. If the answer isn't in the text — write "no information." Text: `{{ $json.chunk }}`"

## Speaker notes

Here's the expanded prompt field of the same answer node we just saw on the canvas. Two lines of instruction and one variable — that's the entire text that goes out to the model together with the question.

The first line is a hard constraint: answer only from the text below. The second is explicit permission for an honest refusal: if the answer isn't in the text, the model must write "no information" — it isn't allowed to make up a plausible-sounding answer from general knowledge. This isn't an accidental phrasing or a stylistic choice — it's a direct defense against exactly the behavior people fear most in systems that answer from a knowledge base: a confident but invented answer.

The variable `{{ $json.chunk }}` is where the actual text the model must answer from gets substituted. And here's what matters: this variable is named the same way and holds the same shape of place for all three actions we're comparing. The instruction is identical everywhere; the difference between prompt-stuffing and search is in what exactly gets substituted into `chunk`. For prompt-stuffing, `chunk` ends up holding the entire knowledge base's text, however many documents are in it. For search by word and search by meaning, only one found document goes in there — the very one the previous node found, which we saw on the last panel.

This second line goes on to work directly: when we break down exactly what happens to prompt-stuffing as the base grows, several answers there will read literally like this — "no information" — even though the needed fact is physically present somewhere in that text. That isn't the model being lazy or not trying: this instruction kicks in exactly when, amid a grown mass of text, the model can't reliably identify the needed fact among dozens of similar ones — and it honestly says so, exactly as instructed. The breakdown of this — next beats, on the measurement itself.
