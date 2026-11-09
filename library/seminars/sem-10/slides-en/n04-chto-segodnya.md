---
id: n04
type: content
duration_min: 1.5
assertion: "Four cases in a row and one concept interlude; each case rests on a run of its own rig on real data"
learning_goal: "Session overview. Names the four cases by task (not by thesis) and the interlude, without revealing findings. Matches the Lec-N-1 pattern of the 'what's covered today' section, adapted for a seminar."
visual:
  pattern: content
  primary: >
    A short five-item list (four cases + the interlude), each one a single
    line naming the task, with no spoiler of the finding.
  backup: >
    Source — rework/section-0-otkrytie.md, section "What's covered today,"
    recast into a compact list. The case names follow the task (design
    canon §1), matching case_track in the config verbatim. The nuance
    about Case 4's honest failure (rework/section-0, "A nuance the opening
    is obligated to name directly") is deliberately NOT carried onto this
    slide: a finding-spoiler here would violate A1/C2 (the result before
    the case itself). It's named at the start of Case 4 (n60), not here.
---

# Four Cases and One Interlude

## Assertion

Storage, splitting, search, and images — four parts of the same question, and as a closing note, a warning about what search on its own doesn't guarantee.

## Visual

1. **Knowledge Base Storage** — what happens to the answer's accuracy and cost as the base grows from ten items to hundreds of documents.
2. **Splitting a Document into Chunks** — once the knowledge base turns from ten lines into real documents, they first need to be cut up; whether the answer to a question stays intact depends on where the cut falls.
3. **Choosing a Search Method** — once there are many chunks in the base, the search method (by words or by meaning) isn't interchangeable.
4. **Image Search** — the same storage-and-search task, only for the scans and photos the training center receives in requests.

> Interlude: a system can find a topically relevant chunk and still give a wrong answer. "Found" and "correct" are different things.

## Speaker notes

Today's session rests on four cases in a row, and after them — one concept interlude, before the session closes.

The first case — knowledge base storage: what happens to the answer's accuracy and cost as the base grows from ten items to a couple hundred documents, and whether there's any point in taking it out of the prompt before the model stops coping with the volume.

The second — splitting a document into chunks. Once the knowledge base turns from ten lines into real documents — regulations, multi-page instructions — before you put it anywhere, the document needs to be cut up. Whether the answer to a question stays intact inside one chunk, or ends up split across two, depends on where the cut ran.

The third — choosing a search method. Once there are many correctly cut chunks in the base, the method used to search them — by words or by meaning — is meant for different cases: one doesn't substitute for the other. Each method has its own zone where it wins, and combining both turns out to be a working solution.

The fourth — image search. The same storage-and-search task, only for the scans and photos Olga's training center has been receiving in requests since the previous session. This continues a line that started two sessions ago: the session before last showed the basic limits of handing an image to the model, the last one showed that the model can read it. Today we add the last step — learning to find that image among other, similar ones.

After the four cases — a concept interlude about how a system can find a topically relevant chunk and still give a wrong answer. "Found" and "correct" are different things, and none of this session's four cases is automatically insured against that substitution just by the fact that it uses search.

All four cases rest on a run of the same rig — the same n8n you've been working with since the seventh session — on real open datasets with a known correct answer. There will be no eyeballed numbers in today's breakdown.
