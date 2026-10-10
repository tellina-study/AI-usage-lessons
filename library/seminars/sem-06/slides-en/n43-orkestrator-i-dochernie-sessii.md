---
id: n43
type: mechanics_map
duration_min: 1.5
assertion: "Alongside the working session people bring up an orchestrator session, which launches full-blown child sessions: you can walk into a child session by hand, and it launches subagents of its own — so there come to be three tiers; the cost is the scaffolding, and the fact that the orchestrator learns a child's result only when it goes and checks"
learning_goal: "A third move alongside the two already examined. A subagent and a child session answer one request — do the pieces at the same time — and diverge on two properties that decide the choice: whether you can walk in by hand, and whether you can go one tier further down. The criterion is named by the size of the piece, the cost is named in three lines"
visual:
  pattern: mechanics_table
  figure: subagent-n43-tri-yarusa.png
  primary: "At the top — a diagram of three tiers: the working session, the orchestrator session, the child sessions and the subagents beneath them; the child session is marked as one you can walk into by hand, the subagent as one that only sends back a result. Under the diagram — a table in two substantive columns: what a child session gives and what it costs. The slide is closed by a criterion line in gold: a small piece to a subagent, a large one to a child session. The line about whose practice this is lives in the diagram's caption."
  backup: "The source is the course author's own working practice, told at both of the classes this deck was delivered in (transcripts: `qa/rasshifrovki/gruppa-1.txt`, 32:33; `qa/rasshifrovki/gruppa-2.txt`, 43:34, 52:02-53:36, 55:38). It was not in the materials, and the author said so directly: \"didn't put it into this lecture\" (group 1, 39:54). Added under section B of the delivery breakdown (`qa/RAZBOR-PROVEDENIYA.md`) — the practice test: what gets added off the cuff twice is what the material is missing.

    Verbatim supports. The move itself: \"I bring up a session that acts as the orchestrator, and I bring up other working sessions for myself as well\" (group 1, 32:33). The two advantages over a subagent: \"you can walk into a child session, first, to look at something or write something, and second, it can spawn subagents of its own, so you get a deeper nesting of the hierarchy, and as a result you can solve more complex tasks that way\" (group 1, 32:33); the same in group 2 — \"what I like about the parallel-session option is that we build a more complex structure here, one that can solve a more complex task\" (43:34). The cost: \"it needs some minimal scaffolding around it\" (group 1, 31:57), \"the main session finds out that the child has done something only when it checks periodically\" (group 2, 52:52). The criterion: \"if the little tasks are small, then subagents; if they're big, then sessions\" (group 2, 55:38).

    The three ways of doing the scaffolding were named by him as well (group 2, 52:26-53:36): an off-the-shelf control layer; an imitation via the issue tracker (called bad — precisely because the result is visible only when you check); a terminal window manager, in whose panes the sessions are brought up and which you can walk into. The names of the tools are deliberately not put on the screen: the author's own development was mentioned by him without a name, and the window manager is a detail of one configuration that has nothing to do with the fact of three tiers.

    What is not on the screen and why. Figures for \"how many sessions to keep\" are not brought up here: they stand on the next screen together with the configuration they were measured on. The limit of a person's attention, which he named on the spot (\"3-5 is enough for me\"), is not carried over in any form: in the same breath he worked out himself that leaning on \"seven plus or minus two\" is supported by nothing (group 2, 51:22), and introducing a number the author called made up in front of the room would be swapping one unsupported support for another. The check is closed (`qa/fact-check-7-plus-minus-2.md`, 2026-10-10): Miller's original source is real and the number in it is measured rather than invented, but what it measures is something else — the limit of discrimination along a single dimension and the span of immediate memory, which Miller himself keeps apart and whose coincidence he calls \"a pernicious, Pythagorean coincidence\"; modern work (Cowan, 2001) gives about four for working memory. The decision after the check — **do not bring it in either as a support or as a debunking**: the number has nothing to do with the composition of the context or with the boundary of a subagent, and the question \"how many sessions to keep\" is already answered by the material's own measurement of machine memory on the next screen.

    Terminology: the slide was written on \"subagent\" from the start — the word \"role\" does not appear in it (the renaming across the whole deck is being done by the neighboring session of the same round)."
---

# The orchestrator and child sessions

## Assertion

Alongside the working session people bring up an orchestrator session, which launches full-blown child sessions. You can walk into a child session by hand, and it launches subagents of its own.

## Visual

| What a child session gives | What it costs |
|---|---|
| you can walk into it by hand: see what it has got through, add to the task, correct the direction | the orchestrator does not learn the result by itself — it learns it when it goes and checks |
| it launches subagents of its own: there come to be three tiers, and the work can be taken on in bigger pieces | scaffolding is needed: sessions do not come up alongside, and do not get polled, by themselves |
| its context is entirely its own, as in any ordinary run | and it costs what an ordinary run costs — in the token bill and in machine memory |

> **A small piece to a subagent. A large piece, one you will have to walk into by hand, to a child session.**

## Speaker notes

Alongside the two moves already examined stands a third, and up to now it has not appeared in the seminar's materials. The course author uses it constantly in his work: alongside the working session another one is brought up, which is called the orchestrator, and it launches child sessions. The child sessions are full-blown, with their own context and their own terminal; this is an ordinary run of the same tool the person works in.

The request this move answers is the same as the subagent's: do the independent pieces at the same time. The two moves diverge on two properties, and both of them decide the choice.

The first property is reachability by hand. You cannot walk into a subagent: only the calling session can talk to it, and the person sees the result once the subagent has finished. You can walk into a child session: open it, read what it has got through, add to the task, turn it around halfway. For a piece that gets discussed as the work goes on, that settles everything.

The second property is depth. A child session launches subagents itself, because it is an ordinary session and can do exactly what yours can. There come to be three tiers: you, the orchestrator with its child sessions, and the subagents under each of them. Hence the point of the move — the work is taken on in bigger pieces than fit into one tier: the orchestrator is given a top-level task, it breaks that into child sessions, and each of those breaks its part into subagents.

The cost of the move is named in three lines, and the first of them weighs more than the others. The orchestrator does not learn the result of a child session by itself — it learns it when it goes and checks. That inverts the order of work: instead of waiting for an answer, there appears a round of visits and polling. From this it also follows why an imitation via the issue tracker works badly: the orchestrator sees the child session's entry when it next looks into the tracker, and the speed is lost on the looking-in itself.

The second line is the scaffolding. Sessions do not come up alongside, and do not get polled, by themselves: somebody has to set them up, give each one a task, be able to list them and walk into them. There are three ways of doing it. An off-the-shelf control layer that can do this out of the box. An imitation via the issue tracker — examined above and called weak. A terminal window manager: the sessions come up in its panes, the panes are listed and opened, and you can walk into each one by hand.

The third line is the cost of an ordinary run. A child session's context is entirely its own, and it is paid for as in any session: a separate bill for tokens and separate machine memory. On one or two tiers that goes unnoticed; on a dozen sessions it becomes an expense you count in advance, and it is counted next.

The criterion that comes out of this is simple, and the author named it with the same sentence at both classes: a small piece goes to a subagent, a large one to a child session. "Large" here has a checkable sign: it is a piece you will have to walk into by hand at least once. If the result is enough, a subagent is cheaper and does not multiply tiers. If, as the work goes on, you are going to need to look and add something, a subagent will not give you that, and the saving will turn into rework.
