---
id: n22
type: case_divider_quote
duration_min: 0.5
assertion: "The base's chunks that the previous case worked with were not ten lines of FAQ, but real, multi-page regulations"
learning_goal: "Case 2's divider. Form — a fact from practice (canon §8.2: the entry form differs for every case). Names the problem (A2), not the solution."
visual:
  pattern: case_divider_quote
  primary: >
    Dark background, one action line large. Below it, the track of four
    cases for the session, the second one highlighted.
  backup: >
    The case title — "Splitting a Document into Chunks", by task, matches
    case_track. The transition fact — from SETKA-KEYSOV.md Case 2, "Entry
    form": the base's chunks aren't ten lines, they're real documents.
---

# Case 2. Splitting a Document into Chunks

## Assertion

The store doesn't swallow a document whole — and a three-page regulation doesn't fit into one chunk.

## Visual

> Case 1 decided where the base would live once it grew — in a separate store, outside the prompt. But the store doesn't swallow a document whole: a three-page regulation doesn't fit into one chunk in a way that lets search later point precisely at the right spot.

## Speaker notes

The previous case decided where the growing knowledge base would live — in a separate store, where chunks of text and their numeric representations of meaning get written, outside the prompt. But this solution carries a silent assumption we haven't checked yet: the store doesn't swallow a document whole in one chunk. The ten lines of FAQ we worked with in the previous case fit into a single store fragment without any trouble. A real three-page training-center regulation does not.

The document first needs to be cut into chunks — and where that cut falls decides whether the answer to a specific question stays intact inside one chunk or ends up torn between two neighbors. If the answer to a client's question sits exactly on the cut's boundary, part of that answer lands in one chunk, part in another, and search will later find only half of it.

This isn't a hypothetical configuration detail — it's a decision that directly determines how many answers reach the requester intact, and how many fall apart in half. Let's look now at how this gets checked in practice.

This problem arises precisely because the previous case ended with a specific decision — putting the base into a separate store. While the whole base lived in the prompt, the question of where to cut didn't exist at all: the model read the entire text at once, and the boundary between neighboring regulations never touched it. The moment a store with separate chunks appears, a new point of failure appears too, one that wasn't there before — and this point of failure needs its own analysis; the silent assumption that it will somehow just work out doesn't hold here.

It's worth picturing the scale right away: a training center's three-page regulation is, by rough estimate, several thousand characters of text. Cutting it into chunks of one hundred eighty characters each gives a couple dozen fragments from a single document. Every boundary between neighboring fragments is a potential spot where one fact ends and the next begins, and any of those boundaries could by chance land exactly where the answer to a future client question sits.
