---
id: n01
type: hero_cover
duration_min: 0.5
assertion: "The process that, until today, only wrote to the table and to Olga starts answering the person who reached out"
learning_goal: "Cover slide. Names the session's topic and its rung on the arc — answering a human (rung 3), not new tool mechanics."
visual:
  pattern: hero_cover
  primary: >
    Dark Ocean gradient, a large title centered on the canvas, a subtitle
    line in the middle of the open band. No session number on screen.
  backup: >
    The title is verbatim from `ARCHITECTURE.md` (the `title` field) and from
    the "Session topic" in `SETKA-KEYSOV-S9.md`: the process answers the
    client itself. The session number is not printed on the cover — owner
    decision, `sem-06/qa/oblozhka-bez-nomera.md`, the same device as S8's
    cover. There is deliberately no figure on the cover: the arc ladder
    (`lestnitsa-dugi.png`) sits one screen later, on n03, and repeating it
    here would show the rung before the gap is named. The session's axis
    question is also not placed on the cover: it is asked on n04 and
    repeated verbatim on n77, and a third spot would throw off the count
    between those two.
---

# The Process Answers the Human

## Assertion

Until today, our process wrote a row to the table and told Olga about the request. Today its answer gets an addressee outside the company.

## Visual

> Large-language-model workflows: the third session of the arc.

## Speaker notes

Two sessions in a row, we built a process with exactly one reader — us. The form took in the request, the model pulled out the topic and the urgency, the knowledge base normalized the values to a fixed list, the row landed in the table, and Olga got a notification. Everything the process produced stayed inside: in the table, in the execution log, in the message to the coordinator. A mistake in a row like that is caught by the person who actually works with that row, and gets fixed before it goes anywhere.

Today we lift that restriction. The process starts writing to the person who reached out to us: answering a question about rescheduling a class, naming a refund amount, explaining how a retake works. From the outside this looks like a small step — the same process, the same model node, just the result going somewhere else. On the inside, what changes is the main thing: the answer now has a reader who knows nothing about how the process works, nothing about the fact that the answer came from a model, and who will take what's written as the training center's own position.

That's what the whole day is about. We'll add the process the ability to answer, piece by piece: what to answer with and when to stay silent, where to keep the knowledge base, who checks the answer before it goes out, what to do with text the client wrote themselves, why the same question gets different answers, and how to read a photo of a document. Six case studies, and each one rests on a measurement — a run on our own rig, or outside work checked against its primary source.

The main difference from the last two sessions is the question we put to every new step. Last time we asked: does the model do this work, or does code? Today the question is harder, because the cost is different. The process wrote something to a human — and now we have to answer who is responsible for what got written, and what can back that up. A green run is not that backing, and by the end of the session we'll have counted this across six case studies — a count worth remembering.
