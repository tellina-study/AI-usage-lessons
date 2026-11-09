---
id: n16
type: mechanism_node_graph
duration_min: 0.75
assertion: "The store node is named Simple Vector Store, and there's no stock 'embedding via OpenRouter' node in n8n at all — this step is built with a plain HTTP Request"
learning_goal: "Layer 2 of Case 1, beat 1 of 3: a real screenshot of the rig's live canvas (not a drawn diagram — the live UI was captured by `stend/n8n_shots.py`, the workaround for [#233-8] lifted on 2026-10-20). The two nodes' panels come as the next two beats (n17, n18)."
visual:
  pattern: mechanism_node_graph
  figure: case1-n8n-canvas-real.png
  primary: >
    A real screenshot of the live rig's n8n canvas: Question + corpus with
    vectors (formTrigger) → Embed query (OpenRouter) → Simple Vector Store
    (cosine top-1) → Answer (RAG) with a model node hanging below it →
    Result screen.
  backup: >
    A REAL SCREENSHOT REPLACES THE DRAWN DIAGRAM in this edit
    (`proektirovanie-keysa-i-voprosa.md` canon §2, README §8.4: the
    "layer unreachable" finding gets fixed not with a substitute genre but
    with a new capture). The previous diagram, `case1-n8n-vector-
    scheme.png` (`make_figures_sem10.py::case1_scheme`), was legitimate at
    the time it was made — the live canvas was unreachable
    (`notes/mcp-limitations.md` [#233-8]) — but that limit was lifted on
    2026-10-20 (an update to the same issue number), and `stend/README.md`
    records: "live screenshots taken, the earlier conclusion was a
    mistake." The earlier generator file was NOT deleted (it stands as a
    record of the earlier solution's build), but the slides no longer
    reference it.

    Frame source: `stend/n8n-screenshots-raw/case1-canvas.png`, captured
    by `stend/n8n_shots.py` on the live `n8n.lessons.tellian.io`. Crop —
    `rendered/compose_case1_n8n_shots.py` (Pillow, the same effect as
    `convert -crop`; ImageMagick isn't available in this working
    environment) — only the dangling "+" connector to the right of Result
    screen was removed; the canvas itself wasn't reassembled or redrawn by
    even one pixel.

    THE MODEL IS NAMED BY NAME (C5): `gpt-4o-mini` (the answer) and
    `text-embedding-3-small` (the question's embedding) —
    `stend/harness2.py`, `CHAT_MODEL`/`EMBED_MODEL`, with no explicitly
    set call settings (parameters such as temperature left at default).
    On the canvas both are visible only by a generic node name ("Embed
    query (OpenRouter)," "Model (answer on retrieved chunk)") — the
    model's own name isn't labeled in the interface (it lives inside the
    HTTP request body / the node's credential), so it's named in the
    slide's text, not on the frame.

    A DEMO RUN, NOT A REPEAT OF THE MAIN MEASUREMENT: the question "At
    what pressure were helium crystals obtained?" — a separate small
    corpus (10 documents) belonging to this demo scenario (workflow
    `JNXhpgEoOC937W5g`), not one of the 10 SberQuAD questions from the
    main measurement on n09/n10. The frame's purpose is to show the
    canvas's mechanics, not to repeat the measurement's numbers
    (`stend/README.md` § "What each demo screen confirmed," execution
    `2112`).
---

# The real canvas: a vector store in n8n

## Assertion

The store node is named Simple Vector Store — its stock name, not "In-Memory," as it's sometimes mistakenly called.

## Visual

> Both the embedding step and the final model call are built with a plain HTTP Request node carrying a pre-set credential type — there's no stock "embedding via OpenRouter" node in n8n's catalog at all.

## Speaker notes

On screen is a real screenshot of the rig's live canvas — the same interface the process was built in last session too: a live-captured n8n frame, with no drawing and no diagram.

Reading left to right gives the main path. The form takes in the question and holds the document corpus, with vectors already computed. Next, the "Embed query (OpenRouter)" node computes this question's embedding the same way the corpus was prepared — the caption under the node right on the canvas shows exactly where the request goes: `POST: https://openrouter.ai/...`. The next node is the store, and its name is Simple Vector Store: that's the node's stock name in n8n. "In-Memory" is a name sometimes used by mistake, but it's not on this canvas. Inside the node is the search code: cosine similarity between the question's embedding and each document's embedding, top-1 candidate. After that comes the answer node, Answer (RAG), with a separate round model node hanging below it: in this interface the model is an external entity, connected to the node from outside, which is why it's drawn separately on the canvas.

Both models that actually do the work here are named in text, because the canvas itself only shows a generic node name — which specific model sits inside isn't readable from the frame: the embedding is computed by `text-embedding-3-small`, the answer is formed by `gpt-4o-mini`, both calls with no specially set settings, parameters left at default.

There's no separate stock "embedding via OpenRouter" node on this canvas. The version of n8n running on the rig has no such ready-made node — OpenRouter as a provider isn't on the list of ready integrations for the embedding step. So both the embedding step and the final model call are built the same way: with a plain HTTP Request node carrying a pre-set credential type. This isn't a workaround and it isn't an unfinished shortcut — it's how a step that has no ready-made node in the catalog actually gets built in n8n today: the parameters are set right in the HTTP request body — the address, the model, the prompt — while n8n substitutes the credential itself on its own side, with no manual handling of the key.

The run on this frame is a demonstration, on a separate small corpus of ten documents: we've already seen the main measurement across four base sizes as a number, there's no need to repeat it here. The question "at what pressure were helium crystals obtained?" went through this whole chain: the question's embedding found the right document with a similarity score of 0.590 among ten candidates, and the model answered correctly, quoting the condition from the found chunk — "at a pressure above 35 atm." How both nodes are set up inside — real configuration panels, next two frames.
