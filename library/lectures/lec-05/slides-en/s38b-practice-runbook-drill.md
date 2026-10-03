---
id: s38b
type: process
section: "Section 5. Support and operations"
duration_min: 2
assertion: "A failure drill in support repeats the make-up of a fire drill: the part of the fire is played by a plan, and what gets tested is the detector, the siren, the exit and the time standard — in IT that is the alert threshold, paging the on-call engineer, rolling the version back and four measured times; AI works inside the drill — it proposes scenarios, generates a flow of tickets, assembles the timeline and a draft postmortem, and a human signs the postmortem off"
learning_goal: "The section's practice: what a failure drill is, how its elements map onto an IT system, what work AI takes on inside it, and where that help ends"
learning_outcomes: [LO1, LO2]
chapter_ref: "§5.3"
verify_day_of: true
partial_out_strict_in: true
interaction: none
protected: true
revision: >
  issue #212, owner-review 2026-10-01: "slide 39 is excellent, only the link between the fire
  alarm and IT systems and the role of AI in it needs stating more sharply, and let us look
  here at the use of AI in such tests rather than at AI degradation". The structure of the
  card and the diagram of the four times are kept unchanged — the owner accepted the slide.
  Added: (1) a phrase-by-phrase mapping of the elements of a fire drill onto the elements of
  an IT system, right inside the "what it is" block — smoke, detector, siren, exit, evacuation
  time standard; (2) the role of AI named inside each step of the mechanism, with the names of
  2026 tools; (3) the subject of the drill moved from degradation of the AI component to the
  use of AI as an instrument of the drill, with the boundary in the gold panel rewritten for
  that subject. Style rule: the contrastive "not X, but Y" format is removed in full — the
  card had eight of them.
meme_or_visual: >
  schema_matrix, a single practice card. In the "what it is" block, as a second paragraph, the
  mapping line "smoke → ... · detector → ... · siren → ... · exit → ... · time standard → ...".
  In HOW IT WORKS, on the right, the labelled diagram of the four time marks is kept, with the
  numbers of one drill filled in.
source: "§5.3 of the chapter. Tools that assemble a timeline and a draft postmortem from the records of an incident (incident.io, Rootly, PagerDuty) — vendor claims; there is no independent measurement"
note: >
  issue #212: the card form is one and the same across all twelve practices in the deck. The
  numbers in the diagram of the four times come from one drill that was actually run, and the
  slide says so in the caption. The vendors' claim about time saved on the postmortem is not
  carried into the visible layer: there is no measurement of our own behind it, and in the
  notes it is named as a vendor claim.
---

# Visible content

## Title bar
The failure drill: is there anything here that would notice degradation

## Body
[what it is → how it works → with AI and without → where it breaks]

**WHAT IT IS**

A fire drill tests the building and the people in it: the detector went off, the siren sounded, the exit was clear, everyone got out within the time standard. There is no fire — the part of the fire is played by a plan. A drill in support is built the same way: the quality of answers is spoiled deliberately and under control, in order to see whether detection fires.

**Element of the drill → element of the system:** smoke → a substituted model prompt · detector → a threshold on a proxy metric · siren → paging the on-call engineer · exit → rolling the version back and a path to a human · evacuation time standard → four measured times.

**HOW IT WORKS**

1. One **class of failure** is chosen and a date is set. **AI:** proposes scenarios drawn from past postmortems; a human chooses.
2. Quality is degraded **under control**: the model prompt is swapped for a weak one, the guardrails are loosened. **AI:** generates a flow of tickets to the scenario, so that the on-call engineer sees the load.
3. **Four times** are measured and written down as numbers — your own, from this drill.
4. The postmortem. **AI:** assembles the timeline and hands over a draft; the findings and the edits to the procedures are signed off by a human.
5. A drill that changed not a single procedure was too easy.

[Labelled diagram on the right, the column "minutes from the start": noticed — 4 · a human arrived — 9 · automation stopped it — 12 · restored to how it was — 21; the caption "the numbers come from one drill that was run; at the next one they are filled in afresh"]

**WITH AI AND WITHOUT**

| WITHOUT AI — the classic failure drill | WITH AI — what it is busy with inside the drill |
|---|---|
| A service is killed, a resource taken away: you watch whether the system comes back up and whether the on-call engineer turns up. The scenario, the timeline and the postmortem are a human's work. | AI proposes the scenarios from past postmortems, generates the flow of tickets itself, assembles the timeline from the records and hands over a draft postmortem. The 2026 tools: incident.io, Rootly, PagerDuty. |

[Gold callout — WHERE IT BREAKS]
AI proposes variations on what has already been lived through: a class of failure that has not happened yet, it will not invent. A draft postmortem is plausible **even when it names the cause wrongly**. **A drill once a quarter gives you detection with a quarter-wide window.**

## Speaker notes

The second practice is shorter than the first, and it tests the thing without which the first one stays on paper: whether detection actually works.

What it is. Think back to a fire drill. There is no fire, the part of the fire is played by a plan, and what gets tested is the building and the people: did the detector go off, did the siren sound, was the exit clear, did everyone get out within the time standard. A drill in support is built in exactly the same way, and let us say the mapping out element by element, because a metaphor is useful only while it is accurate. The smoke that is not there is the model prompt, substituted for a deliberately weak one. The smoke detector is the alert threshold on a proxy metric of quality. The siren is the page to the on-call engineer. The fire exit is rolling the version back and the path to a live human. The evacuation time standard is the four times we measure. And what we are testing is ourselves: is there anything here that would notice degradation, and will anyone get there in time.

The mechanism has five steps, and in each of them AI has work of its own. First: one class of failure is chosen and a date is set. AI goes through past tickets and postmortems and proposes a list of plausible scenarios; a human picks from it. Second: quality is degraded under control — the prompt is substituted, the guardrails are loosened. AI generates a flow of tickets to the scenario, so the on-call engineer sees a real load: one invented ticket is not enough. Third: four times are measured. How long until it was noticed. How long until a human arrived — that is a separate time, because an alert nobody walked towards is of no use. How long until the automation stopped what was happening on its own. How long until things were restored to how they were, restored and not patched over. The numbers on the slide come from one drill that was run; at the next one they are filled in afresh. The fourth step is the postmortem. The timeline from the records and the draft postmortem are assembled by AI — that is what incident.io, Rootly and PagerDuty are for; the time saving they promise is substantial, but it is a vendor claim with no measurement of our own behind it. The findings and the edits to the procedures are signed off by a human. Fifth: a drill that changed not a single procedure was too easy.

The boundary is honest. AI proposes scenarios drawn from what has already happened, so it gives you variations on what has been lived through; a class of failure you have not had yet remains a human's work. A draft postmortem always looks plausible, including when the cause named in it is the wrong one. And a drill once a quarter gives you detection with a quarter-wide window.
