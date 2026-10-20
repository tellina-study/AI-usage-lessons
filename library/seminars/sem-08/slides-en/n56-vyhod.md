---
id: n56
type: outcome_artifact
duration_min: 2.0
assertion: "What leaves the session is a continuation of student.json with four fixes: a template instead of a model for the notification, two-tier deduplication, a code condition instead of a text rule, a size check before sending the image"
learning_goal: "The session's output presented as an artifact: what got added and what to do with it at home. Carries the through-line S7→S9."
visual:
  pattern: outcome_artifact
  primary: >
    A file card: what it is, how to install it, what's needed, what to do
    at home. The same form as in the closing of Seminar 7.
  backup: >
    AN HONEST NOTE ON THE ARTIFACT'S STATE as of writing this slide: each
    of the four fixes has been built and confirmed by its own real runs on
    the rig (stend/stage-1-after.json, stage-2.json, stage-3b-code.json,
    stage-4.json — see SETKA-KEYSOV-S8.md "Rig state"). Combining all four
    into ONE file for handing to students (by analogy with
    sem-07/stend/student.json) is ABSENT from the repository as of this
    slide — stend/sborka.py has no function equivalent to student_file() in
    sem-07/stend/sborka.py. This is an open item of the production phase,
    not a hidden gap: the slide describes the contents of the file that
    will be assembled for the handout, not a claim that the combined file
    already sits in the repository.
---

# What we're taking from the session

## Assertion

Four fixes, one file — a continuation of the same scenario you finished last session with.

## Visual

| | |
|---|---|
| **file** | a continuation of `student.json`, the one you finished last session with |
| **what's new** | coordinator notification by template, not by model · duplicate check in two tiers · refund decision by a condition in code, not a rule in text · image delivery with a size check before sending |
| **how to install** | same import as last time: workflow menu → Import from File |
| **what you need** | your own n8n and a model provider key, same as before, plus a Telegram bot and token for the notification and the image |
| **what to do** | run a few requests, including a repeat and an oversized image, and see where any of the four decisions behaves differently from what's on screen |

## Speaker notes

Let's gather what got added today to the workflow you're already working with at home.

It's the same file, a continuation of student.json, the one you left last session with: the form, field extraction, the lookup list, writing to the table, the results screen, plus retry and the failure branch. Today four decisions got added to it, and each one replaces something that looked like it worked with something you can answer for.

The notification to the coordinator is now assembled by substituting values into a ready-made template, not by a separate model call: the same text, with no risk that the model adds a detail to the message that wasn't in the request. Before the request is written, there's now a two-tier duplicate check: cheap and instant for cutting literal repeats, and a meaning-based question for whatever's left. The refund decision is now made by a condition in code, not a text rule inside a request to the model: the same amount threshold, but without the chance of getting it wrong right at the edge. And delivery of the image to Telegram now checks the file size before sending, instead of trusting that it'll just work out.

Install it the same way as last time: workflow menu — import from file. You need the same things last session needed — your own n8n and a model provider key — plus, additionally, a Telegram bot and token, if you want to check the notification and the image on your own data.

The homework request is the same as last time: run a few requests on your own version, including a repeat request and an image noticeably larger than usual, and see which of the four decisions behaves differently for you than it did here on screen.

And a separate request, because today's session was denser than the last one: don't check all four decisions in one evening. Take one — whichever is closer to your own work — and get it to a state where you can explain to a colleague why it's built exactly that way; the other three can wait until next week.
