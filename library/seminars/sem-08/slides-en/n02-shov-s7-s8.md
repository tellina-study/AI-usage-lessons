---
id: n02
type: mechanism_node_graph
duration_min: 2.5
assertion: "We have a workflow that classifies incoming requests — six nodes, the same ones that were working at the end of last session"
learning_goal: "Seam S7→S8: the workflow is shown as a real screenshot, not retold or redrawn. Today's cases exist not because these six nodes are bad, but because the chain is about to get new steps that have not faced this question yet."
visual:
  pattern: mechanism_node_graph
  figure: shov-s7-obzor-klassifikatsii-en.png
  primary: >
    A real screenshot of the live n8n canvas from last session (not a
    diagram): six nodes left to right, each numbered, with a short one-line
    key to the numbers below the shot. The failure branch is not shown in
    this particular shot — the notes cover it separately.
  backup: >
    The owner's edit, 2026-10-20 (issue #274): "let's not show that scary
    diagram — let's show a screenshot from n8n that already exists, with a
    short caption underneath — not the same workflow that one person will
    remember and another won't, but a note saying we have a workflow for
    classification." The shot is sem-07/rendered/figures/obzor-k1.png, a
    real frame from the live rig with marked labels
    (sem-07/rendered/annotate_shots.py, function annotate, the obzor-k1.png
    call: labels are placed over the real frame, the interface itself is
    not redrawn), copied unchanged into
    sem-08/rendered/figures/shov-s7-obzor-klassifikatsii.png. The earlier
    programmatic diagram (make_figures_n02.py, shov-s7-s8.png) was accurate
    in node composition but drawn by code, not captured from the screen —
    it is left in the repository as a record of the decision; the slide no
    longer uses it. The failure branch (3-attempt retry → a separate
    status=not_parsed row → its own screen) did not make it into the frame
    itself — it is described in words in the notes, not invented: the
    composition is confirmed by reading sem-07/stend/student.json directly.

    EN track note (this file, issue #172/#274): the figure is re-annotated
    with English captions from the same underlying screenshot
    (sem-07/rendered/figures/n8n-holst-stage1.png, read-only — sem-07's own
    folder is never edited) and the same label coordinates as obzor-k1.png
    — see sem-08/rendered/make_figures_n02_en.py. The numbered circles
    (1–6) carry no language; only the caption band below them is
    translated.
---

# Starting state: the workflow from last session

## Assertion

We have a workflow for classifying incoming requests. Six nodes that were working at the end of last session. Today not one of them changes.

## Visual

> This is a real n8n canvas, not a diagram. We have a workflow for classifying incoming requests — six nodes, the same order, the same names as at the end of last session.

## Speaker notes

We have a workflow for classifying incoming requests — here it is, on screen, a real screenshot of the canvas, not a drawn diagram. The exact same six nodes you saw at the end of last session, in the same order, with the same names. Not one node has been renamed, deleted, or changed — if you opened the workflow file at home, today's rig starts from that same file.

Quick reminder of how it is built, because from here on we will refer to these steps by name. The form takes the request as free text — the person writes however is convenient, no format required. Extraction is a separate model step that pulls the topic, urgency, and contact out of that text, if a contact is mentioned in the text at all. The lookup list is not a model but a deterministic check: a value is either from the given list, or it becomes "other" or "not specified" — there are never empty cells after this step. Write puts the finished row into the table, and the results screen shows the requester every step at once, as a single sheet.

Separately — the failure branch, which you cannot see in this particular shot: if extraction cannot parse the text even after three attempts, the request does not disappear — it goes into the same table with its own marker, and it gets its own screen.

Why look at this again at all. Not because there is anything to pick at here — there are no complaints about these six nodes today. It is because today's four cases are exactly the steps this chain is about to pick up: a notification channel, a check for a repeat request, a decision on the refund amount, delivery of an image. Not one of them has had the question "is this the model's job or code's job" asked of it yet. We are starting from a clean, already-working foundation and building onto it, case by case, with this one question.
