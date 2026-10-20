---
id: n11a
type: mechanism_node_graph
duration_min: 1.5
assertion: "The settings panel of the 'Compose notification (LLM)' node: the real prompt text, exactly as it stands on the rig right now — not a paraphrase"
learning_goal: "New slide (n11a), inserted between n11 and n12, answering the owner's standing note for all cases: a general canvas frame must be followed by a real screenshot of the node's own open settings panel, not a prose paraphrase of the prompt. The prompt text is read verbatim from the screenshot and cross-checked word for word against `stend/stage-1-before.json` — both sources agree."
visual:
  pattern: mechanism_node_graph
  figure: k1-n8n-versiya1-nastroyka-llm.png
  primary: >
    A real screenshot of the "Compose notification (LLM)" node's settings
    panel (Parameters tab): the "Prompt (User Message)" field with the full
    prompt text, and the "Require Specific Output Format" / "Enable
    Fallback Model" toggles — both off. On the left, the list of fields
    available to this node from the "Write row" node.
  backup: >
    **This screenshot is real, and its prompt text is in Russian on
    purpose — read this before anything else.** The live rig is a real
    training-center automation whose coordinator is Russian-speaking, so
    the prompt the facilitator actually wrote instructs the model to
    address a Russian-speaking person, in Russian: "Напиши короткое
    дружелюбное уведомление координатору учебного центра в Telegram о
    новой многотемной заявке…" ("Write a short, friendly Telegram
    notification to the training center's coordinator about a new
    multi-topic request…"). This is NOT re-drawn or re-translated for the
    EN deck — doing so would misrepresent what is actually configured in
    the live system (see `glossary.en.yaml`'s mirror-check note). The
    visible body and these speaker notes state explicitly, in English,
    that the screen is real and why its text is in Russian.

    Prompt text visible on the frame, read in full up to the word
    "упомянуто: {{ $('Vocabulary check').item.json.extra_to…" — the field
    then scrolls out of frame (an honest limit of the n8n scroll box, not a
    crop on our part). The full value is confirmed verbatim by
    `stend/stage-1-before.json`: "Напиши короткое дружелюбное уведомление
    координатору учебного центра в Telegram о новой многотемной заявке.
    Имя заявителя: {{ $('Request form').item.json['Имя'] }}. Основная
    тема: {{ $('Vocabulary check').item.json.topic }}. Также в заявке
    упомянуто: {{ $('Vocabulary check').item.json.extra_topics }}. Пиши
    по-человечески, одно-два предложения." — the visible part of the
    frame matches this text verbatim up to the scroll cutoff, no
    discrepancies.

    This replaces the earlier form of presenting this: previously the same
    prompt text (paraphrased closely but in prose, not quoted in full) sat
    next to a canvas crop that showed neither the panel nor the text —
    forcing the reader to take the slide's word for it. Now the text and
    its source are on the same frame.

    The field list on the left (received_at, name, contact, request_text,
    topic, urgency, contact_from_text, status, extra_topics, id,
    createdAt, updatedAt) are the real fields available to this node from
    "Write row" (visible on the panel as a tag list), not invented for
    illustration.
---

# Node settings: the prompt of the model version

## Assertion

Here is the actual settings panel — not a paraphrase. The screen below is real, and its prompt is in Russian on purpose: the live bot addresses a Russian-speaking coordinator. The prompt's source is "Define below"; the model is handed three ready values and asked to write the notification freely, with no fixed form.

## Visual

> **Node "Compose notification (LLM)", Parameters tab.** The **Prompt (User Message)** field (real screen, text in Russian — see Assertion above): «Напиши короткое дружелюбное уведомление координатору учебного центра в Telegram о новой многотемной заявке. Имя заявителя: `{{ $('Request form').item.json['Имя'] }}`. Основная тема: `{{ $('Vocabulary check').item.json.topic }}`. Также в заявке упомянуто: `{{ $('Vocabulary check').item.json.extra_topics }}`. Пиши по-человечески, одно-два предложения.» — in English, what this instructs: "Write a short, friendly Telegram notification to the training center's coordinator about a new multi-topic request. Requester's name: {{ … }}. Main topic: {{ … }}. The request also mentioned: {{ … }}. Write it the way a human would, one or two sentences."

> The **Require Specific Output Format** and **Enable Fallback Model** toggles — both off: no fixed answer structure, no fallback model if the call fails.

## Speaker notes

Here's the actual settings panel — what opens if you double-click the "Compose notification (LLM)" node on the canvas from the previous screen. Before anything else: this screen is real, and the prompt is in Russian because the live bot genuinely addresses a Russian-speaking coordinator — we are not re-drawing or re-translating it, because that would misrepresent what's actually configured. The prompt's source is "Define below": the text is set right here, not pulled from a separate system prompt somewhere else.

The model is handed three already-ready values — the requester's name, the main topic, and the extra topics, all extracted earlier, at previous steps of the chain — plus one instruction: write a short, friendly Telegram notification to the coordinator, one or two sentences, the way a human would. No fixed phrase structure, no "answer in exactly this form" — this is exactly the freedom we talked about on the architecture diagram: a meaning-level task with no fixed response structure.

Notice one detail already, before we see the result: there's nothing in the instruction like "address the coordinator by name" or "insert the recipient's name." The model simply was never told the coordinator's name — because the text Olga receives doesn't need it. This detail becomes important two screens from now, when we see the real runs.

The two toggles under the prompt field are also part of the real configuration, not invented for the breakdown. "Require Specific Output Format" is off: the answer isn't constrained in structure at all. "Enable Fallback Model" is off too: if the primary model doesn't respond, there's no fallback here.

The finished text from this node goes straight into the node that sends the message to the coordinator — no check in between; you can already see that on the previous, general frame, from the direct arrow between the two nodes.

The configuration itself looks tidy and gives no hint of a future problem: the prompt is short, clear, with no obvious wording mistakes. Worth keeping in mind going forward — if the next screens turn up a finding, it won't be about the quality of how the prompt was written. It will be that any text a model composes freely from a naturally worded instruction can accidentally drag along a scrap of the very form it was working from — and no format check will catch that, because the resulting text is syntactically fine.
