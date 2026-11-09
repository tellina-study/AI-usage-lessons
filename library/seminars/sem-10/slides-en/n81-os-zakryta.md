---
id: n81
type: recap_table
duration_min: 2.0
assertion: "The axis's four rows are filled in with measurement: in each one, the intuition wasn't foolish — it was an incomplete picture, which the run completed"
learning_goal: "Closing of the session's axis. Every right-hand cell is a number from a run the room has already seen. The session's question returns verbatim, the same text as on n03."
visual:
  pattern: recap_table
  primary: >
    The same table that opened the session (n03), now with the right
    column filled in. Below it — the session's question, the same text.
  backup: >
    The left column is verbatim the same as on n03. The right one is
    assembled from the four cases' "generalization" and "nuances" beats,
    the numbers from the current version of SETKA-KEYSOV.md (an
    additional pass on 2026-11-01, Case 1's question set rebuilt on
    2026-11-02): this slide uses only the final, rebuilt numbers.
---

# Four Rows of the Axis: What They Turn Out to Be

## Assertion

The room saw every right-hand cell as a number on screen before it was ever spoken here.

## Visual

| Looks reliable | What it turns out to be |
|---|---|
| if the base has grown — just list it all in the prompt, like on S9 | Accuracy holds at one level (~0.7 at 10/50/200) with no warning sign, while cost grows ×17.0 over the same range — and at 500 documents the request is physically rejected (HTTP 400, context exceeded); keyword search holds recall@1=0.8 at every size, vector search holds 1.0 at 10/50/200 and 0.9 at 500, at ~$0.00005 regardless of size |
| you can cut a document into pieces any way you like, as long as the chunk ends up in storage | Fixed-size chunking tears the answer apart in 2.8–12.5% of cases; sentence-boundary chunking stays almost always within 0–1.4%; a chunk size that merely "looks convenient" guarantees no quality without checking it against your own data |
| semantic search (vector) finds the same thing as keyword search anyway, just smarter | On a hard corpus, vector search beats keyword search on recall@1 (0.86 vs. 0.74) — but combining the two signals doesn't win on every metric at once; a reranker raises recall@1 to 0.96 at the cost of a separate model call and its own mistakes |
| if we know how to search text, we'll find an image the same way, just by captioning it in words | A caption loses what's visible in the image; direct image comparison technically doesn't work on this rig — the model answers without an error, but returns the same vector for different images |

> **Where does the process get its facts, and why does it consider them true?**

## Speaker notes

We're back at the table we opened the session with. The right column is no longer empty, and it wasn't my narration that filled it in — you saw every cell as a number on screen, in its own case.

The first row. If the base has grown — just list it all in the prompt. Accuracy here gives no warning sign whatsoever: it holds at one level, around 0.7, at ten, at fifty, and at two hundred documents alike — while cost keeps growing the whole time, seventeen times over across that same range, with no connection to accuracy at all. And at five hundred documents, what happens isn't a gradual "a bit worse" — it's an instant structural failure: the request is physically rejected because it exceeds the model's context. Search behaves differently: keyword search finds the right document eight times out of ten at any base size — and that neither improves nor worsens as the base grows, so the cause isn't scale; semantic search holds ten out of ten at the three smaller sizes and only dips to nine out of ten at five hundred documents.

The second row. You can cut a document into pieces any way you like, as long as the chunk ends up in storage. Fixed-size chunking by character count tears the answer to a question apart in anywhere from two point eight to twelve and a half percent of cases, depending on the chosen chunk size. Sentence-boundary chunking almost always stays within zero to one point four percent. And a separate finding: a chunk size that merely "looks convenient" guarantees nothing on its own without checking it against your own data — version 1's dependence on size is non-monotonic.

The third row. Semantic search finds the same thing as keyword search anyway, just smarter. On a deliberately hardened corpus, semantic search really does beat keyword search on the share of correct top results — eighty-six percent against seventy-four. But combining the two signals doesn't win on every metric at once: pure vector search's share of correct top results is even higher than the hybrid's. And having the model re-rank the order raises that share to ninety-six percent — at the cost of a separate model call, which is itself not insured against making mistakes.

The fourth row. If we know how to search text, we'll find an image the same way, just by captioning it in words. A caption loses what's visible in the image itself — that's expected. But the real finding is elsewhere: direct image comparison technically doesn't work on this rig — the model answers without a single error and still returns the same vector for completely different images.

And here's today's main question, the one everything started with: where does the process get its facts, and why does it consider them true. The four cases gave it a full, detailed answer, and the interlude we just worked through added a warning to it: even a perfectly built search doesn't guarantee that what's found is correct.
