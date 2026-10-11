---
id: n32
type: problem_scenario
duration_min: 1.5
assertion: "The developer found all four places where the limit on members is checked, having read forty files in the same session the edit had already been explained in — and when it came to the edit itself, the agent re-asked what had been explained that morning: the context is taken up with reading for something else, and half an hour went on the repeat"
learning_goal: "The hook of the case: the volume of reading needed for a short conclusion has no relation to the size of the conclusion, and the result of that reading is needed in the same place the work sits. A recognizable working situation (a new plan and a limit that has spread across the codebase), not one constructed for the sake of a moral — the owner outright rejected \"examples pulled out of thin air\". Round 5 (issue 225): the scene was replaced entirely. The previous one was about an unrelated question from the technical director, and the room justifiably asked why the protagonist had not opened a second session for it; the seminar did not answer that question. Now the reading serves an edit that sits in this same session, and the result of the reading has to come back here — a second session gives an answer but does not return it into the work. And the scene presents the opening's second miss in full (\"what was needed fit inside and crowded the work out\", n04, the second row). The solution is not named"
visual:
  pattern: problem_scenario
  primary: "Five steps as a numbered list: the task of the day, fifteen minutes of explaining it to the agent, why a search is needed before the edit, where the limit actually lives (four places) and how many files have to be opened, and what happened when it came to the edit itself. At the bottom, a highlighted line: the cost — half an hour on repeating the explanation, and a direct reference to the opening's second miss."
  backup: "Round 5 (issue 225, ZADANIE-KRUG-5.md, verbatim: \"it is not clear why he did not raise a second session for an unrelated question. we need something more lifelike and logical\"). It was: the technical director asked in the chat about the limit on the free plan, the protagonist read forty files and answered \"yes, but…\", and the edit the session had been opened for was deliberately NOT connected to the question — and along with that lack of connection went the reason to read precisely here. It became: the reading and the edit are one piece of work. The protagonist is editing the limit, and in order to edit it he needs a list of the places where the limit is checked; the list is needed by the agent that is doing the editing, that is, in this session. The turn of the case was not touched (a subagent does not read any faster, what is saved is room in the context) — all that changed is why the reading cannot be moved out. The class of the scene is exactly the one the owner named a round earlier: \"work out where some behavior lives in the project, and read dozens of files in order to do it\". The detail (a limit on members scattered across middleware / the config / the migrations / the client) is an ordinary situation in any product with pricing plans; the seminar's demo repository is too small for an honest forty-file scene, so the scene runs in the protagonist's working product, and that is said on the screen in the very first line. The cost was recalculated from an hour to half an hour: fifteen minutes of explaining, spent twice, plus the return into interrupted work — an hour with twenty minutes of reading read as a stretch. THE DAY OF THE WEEK IS DELIBERATELY NOT NAMED: the opening (n04) calls this miss Wednesday, while the scene of the MCP section's first case (n10) stands on a Tuesday — a different episode; a third instance of a day of the week would have cemented the confusion."
---

# Found all four places. Started the edit over

## Assertion

To edit the limit, you have to know where it is checked. The search cost forty opened files — and when it came to the edit itself, the agent re-asked what it had been told that morning.

## Visual

1. The same developer who set up the hook and the skill here. A different scene: the product he works in every day — plans, members, two years of migrations. The task of the day is to set up a "Team" plan: twenty members instead of five.
2. The session has been open since the morning. For some fifteen minutes he explains the task to the agent: what the plan is called, who can get it, what to do with old accounts, which cases to check. They are making the edit right here.
3. Before editing, a list is needed of the places where the limit on members is checked at all. Miss one, and the new plan will pass the config and run into a check nobody remembers any more.
4. The agent searches and finds four: the middleware when a member is added, the plans config, a separate migration for accounts created before the pricing tiers were changed, and a client-side component with the same check for the case where the server is unavailable. There are fifteen migrations over two years, and the limit changed in three — all of them have to be paged through. More than forty files opened, some twenty minutes of reading.
5. "Now edit it per this list" — and the agent re-asks what it had been told that morning: what the plan is called and how many members are in it. The explaining has to be done a second time.

> **Half an hour went on saying what had already been said and getting back to where he had stopped. The list, meanwhile, is correct, and the reading went quickly: what was needed fit into the context whole and crowded out the work the session had been opened for. This is the second miss from the start of the class, presented in full.**

## Speaker notes

The protagonist is the same one who set up the hook and the skill here over two classes in a row. The scene is a different one: the product he works in every day — plans, members, two years of migrations. The task of the day is an ordinary one: set up a "Team" plan, twenty members instead of five.

In the morning he opens a session and spends some fifteen minutes explaining the task: what the plan is called, who can get it, what to do with old accounts, which cases to check. They are going to do the editing right here — the whole count that follows rests on that.

Before editing, a list is needed: where the limit on members is checked at all. Miss one place, and the new plan will pass the config and run into a check nobody remembers any more.

The agent searches and finds four places: the middleware when a member is added, the plans config, a separate migration for accounts created before the pricing tiers were changed, and a client-side component with the same check for the case where the server is unavailable. There are fifteen migrations over two years, and the limit changed in three — all fifteen have to be paged through. More than forty files opened, some twenty minutes of reading.

He says: now edit it per this list. And the agent re-asks what it had been told that morning: what the plan is called and how many members are in it.

It is worth examining what has been paid for here. The list is correct, the reading went quickly, and there was not one mistake. Forty files fit into the context whole and crowded out the task the session had been opened for. This is the second miss from the start of the class, presented in full: what was needed fit inside and crowded the work out.

The cost is half an hour, although the reading was twenty minutes, and the difference between those numbers matters. Twenty minutes were spent on the work itself: the list was needed, and without it the edit comes out incomplete. Half an hour went on saying what had already been said again and getting back into interrupted work. That is the only part of the day that did not have to be spent.

Next, the objection that comes up here first: why did he not open a second session and ask there? The answer rests on where the edit sits. The editing will be done by this session, and the list is needed by the agent that is doing the editing. A second session will give the answer and keep it to itself: it has no channel into the working session. You do the carrying over, in your own retelling, and the agent edits by that retelling. The condition about the old accounts is the first thing to fall out of a retelling — it is long, dull, and at the moment of carrying over it looks secondary. That option is broken down in full two screens from now, together with four others.

The second objection: then move the whole of the work into a second session? That is the same count, paid in advance. The task was explained here — those very fifteen minutes; explaining it a second time in a new session means paying exactly the loss we are counting. Moving house does not save anything, it shifts the expenditure to the beginning.

The third: could he not have known where to look straight away? In a product where a rule has been changed over years by small edits — he could not. Documentation that would hold all four points in one place has never existed here. Setting it up after the fact costs more than reading forty files once.

What remains is to say why the scene does not run in the seminar's demo repository. It has fewer than ten files, and a forty-file scene there would have been fitted to the conclusion; it would not have made the conclusion any more correct. The protagonist is the same, the project is different, and that is said on the screen in the first line.
