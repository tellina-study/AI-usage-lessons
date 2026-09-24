---
id: s07
type: assertion_visual
duration_min: 22
assertion: "Who has a story — did it help or let you down?"
learning_goal: "A plenary scaffold for an open exchange of experience across the whole audience"
learning_outcomes: []
references: []
visual:
  pattern: failure_category_grid
  primary: "6 AI failure category icons in an Ocean rounded box grid (2×3), larger and without the top invitation block"
  round4b_note: "owner follow-up 2026-08-29 — category 6 renamed from 'Too generic advice — not for your situation' to 'An answer that doesn't fit your specific situation' (target); 6 personal instructor stories added to the speaker notes (one per category), see below"
---

# Who has a story — did it help or let you down?

## Assertion

Who has a story — did it help or let you down?

## Visual

Round-2: removed the top invitation block "Who has a story — raise your hand"
+ the GOLD `hand` icon — the freed-up space goes to the category grid (larger
cards, better visual mass balance). The hand-raising invitation mechanic
itself stays in the speaker notes. A grid of 6 Ocean rounded box cards (2×3,
icons enlarged to 96px), each with an icon and a short label for an AI failure
category: "Hallucinated fact" (`x-circle`), "Outdated data" (`clock`), "A task
solved only on the surface — looks right, but dig in and it's not" (`layers`,
round-2 rename from "Code that looked correct" — this broadens the category
beyond code alone), "Lost context in a conversation" (`rotate-ccw`),
"Mismatched tone" (`smile`), "Too generic advice — not for your situation"
(`target`, round-2 replacement for "Data leaks" — an unlikely student
experience; generic boilerplate advice is a far more recognizable one). No
mention of groups or teams, no methodology text anywhere in the slide's
visible area — the whole audience together, and the success/failure
alternation stays exclusively in the speaker notes.

## Speaker notes

Now — an open exchange of experience in front of the whole audience. In turn, whether by volunteering or by my calling on you, you'll tell one story out loud where AI genuinely helped, and one where AI let you down or made a mistake. Together, on the board, we'll find common patterns in the stories we collect.

Whoever has a story where AI genuinely helped — raise a hand. If no one volunteers right away, that's fine, I can call on someone directly. We'll alternate: one success story, then a failure, then a success again — that way we keep the balance and don't let the conversation slide into one tone.

Six categories of AI failure that come up most often: a hallucinated fact — AI confidently makes up a fact or source that doesn't exist; outdated data — AI answers with information that was correct at training time but is now stale; a task solved only on the surface — the result looks like the right answer, but on inspection the substance isn't actually solved (this is broader than just code: the same pattern shows up in text and in calculations too); losing context in a long conversation, where AI forgets the conditions set at the start; a mismatched tone or style in the response; and too-generic advice — AI gives an answer that's correct in general but nonspecific, and it doesn't account for your particular situation. When you tell a failure story, try to guess for yourself which category it belongs to — we'll pin it down together. Failure stories in particular are valuable today: they help reveal AI's real limits, not just its impressive examples. This same term — hallucination — will come back with a precise definition later, in the quickfire quiz.

— Instructor's personal stories (to tell in this block, one per category) —

1. Hallucinated fact. Last year, while I was writing an article for a conference, a model gave me several citations to research papers that don't exist — and some of the citations pointed to real papers, but on a completely different topic than claimed. It looked confident and plausible, so every citation had to be checked by hand.

2. Outdated data. This is especially noticeable in development: a model pulls in outdated library versions and, worse, outdated approaches. For example, you ask for a React component — and it writes it as a class with componentWillMount instead of hooks; or it suggests moment.js, which hasn't been actively developed in years, instead of date-fns or the built-in Temporal. The code is formally working, but the approach is from the day before yesterday.

3. A task solved only on the surface. This happens with almost every product I build: the first AI prototype looks a lot like what's needed — screen, buttons, responses — but dig in, and often it either doesn't work or fakes working (data is hardcoded, error handling is drawn but not wired up). A finished product on the outside, a stage set on the inside.

4. Lost context. In a long refactoring conversation, after a couple dozen messages, the model forgets what we agreed on at the start: say, I explicitly said "no pulling in external dependencies" and we renamed a module — and twenty replies later it's suggesting a third-party library and the old name again, as if the conversation never happened. The context has drifted out of the window, and the conditions have to be restated.

5. Mismatched tone. The example is right in front of you — these lectures. I prepare them with heavy AI involvement, and there are still odd turns of phrase and tone on the slides and in the notes that I haven't cleaned up. This is an honest example that a model's tone has to be edited by hand.

6. An answer that doesn't fit your situation. The same story keeps coming up for me — a model's paranoid "information security" on dev and test environments: it resists saving or showing the logins and passwords for test users because "that's not secure," even though we're talking about deliberately fake test accounts on a local environment, which is exactly where that's needed. The advice is correct in general — just not for my particular situation.
