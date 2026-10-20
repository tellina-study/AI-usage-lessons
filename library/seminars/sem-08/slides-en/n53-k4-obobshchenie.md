---
id: n53
type: answer_breakdown_table
duration_min: 2.0
assertion: "Binary data is a separate data model from JSON fields, and the same contract that broke on text in «Notifications» breaks here on format and size; this session introduces them at the level of «one file, one limit, one send,» no deeper"
learning_goal: "Case 4 wrap-up + an explicit boundary on the introductory level of binary data. Storing and searching many files is Seminar 10, not here."
visual:
  pattern: answer_breakdown_table
  primary: >
    A short wrap-up and below it a two-column table — what's enough for
    this session and what's deliberately left out of frame until
    Seminar 10.
  backup: >
    The text is a direct unfolding of "Wrap-up" from
    SETKA-KEYSOV-S8-part2.md, section "Card in Telegram," including
    the sentence "An explicit boundary of the introductory level,"
    folded into the table.
---

# The binary-data contract and the boundary of the introductory level

## Assertion

The same broken contract we saw on text happens here on format and size — and binary data doesn't go any further than this session.

## Visual

> **Binary data in n8n is a separate data model, not just another field value.** The contract between steps that broke on text in "Notifications" (the node didn't fail, the result was just quietly wrong) breaks here on format and size — for the same reason: a formally successful run says nothing about whether the result reached the recipient.

| Enough at this level | Next level — Seminar 10 |
|---|---|
| one file, one known limit, one send | storing and searching among many files |
| checking size and format before sending | processing a file's content with a model (searching images by meaning) |
| an explicit condition in the chain at every step touching binary data | a vector store and indexing attachments |

## Speaker notes

Let's wrap up what we broke down in this case, and name right away where it ends.

Binary data in n8n is a separate data model from text JSON fields, not just another value in a request. A text field has content. A file has content, and it also has a size and a format, and it's exactly these last two properties that decide whether the result reaches the recipient.

The contract between steps that broke in the "Notifications" case on text — the node didn't fail, the result just quietly turned out wrong — breaks here on the format and size of a binary attachment, for the exact same reason: a formally successful run says nothing about whether the result reached the recipient in the shape expected. This is one and the same lesson on two different data types within a single session, and that's not a coincidence — it's one and the same systemic property of any chain: a step's success measures the step itself, not what happens after it.

Now the explicit boundary this case deliberately doesn't cross. We introduced binary data at the level of "one file, one known limit, one send": fetch the file, check its size and format, send it. Storing many files, searching among them, and processing their content with a model — a vector store, searching by image, answering based on picture content — is a next-level task, and it's deliberately untouched here. Seminar 10 completes exactly what's left out of frame today: it doesn't introduce binary data from scratch, it continues from the level we left it at today.

The difference between the two levels isn't about the tool's complexity, it's about the question being asked at all. Today's question was "will this specific file arrive on this specific run" — and the answer is fully known ahead of time, from two numbers: the file's size and the channel's limit. At the next level, the question is different — "which of many files answers the meaning of the request" — and it no longer has an answer you can compute from two numbers before the run.
