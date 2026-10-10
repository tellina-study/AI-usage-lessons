---
id: n10
type: problem_scenario
duration_min: 1.5
assertion: "On Tuesday the developer copied the issue into the chat in the morning, the client added a line to it in the afternoon, and the edit went out without one requirement: an hour of rework, an email of explanation, and a client who now double-checks whether what he wrote made it through"
learning_goal: "The hook of the case. The storytelling revision (issue 225, P2): the scene stops being a description of a state (\"the client keeps his tasks in a tracker\") and becomes an episode in which a specific person missed and the cost is named in terms the room understands — an hour lost, a requirement skipped, an explanation owed to the client. It is that episode which makes the base's thesis (\"a snapshot will be out of date by lunchtime\") checkable rather than declarative, and the case's failure comes back to it"
visual:
  pattern: problem_scenario
  primary: "At the top — the lead-in: how the client moved to a tracker and what the developer does by hand. Below — one Tuesday in four steps as a numbered list, with the miss on the third step. Under them, a highlighted line with the cost and with the nature of a tracker as a live system, separate from the repository."
  backup: "Source — rework/section-1-mcp.md §A.1.4, §B.3 (part1c.md). Carried over from sem-05/rework/section-3-mcp.md §A.2; the content of the case (five ways of getting access, the mechanics, the failure, the criterion) did not change — four rounds of edits and a fact-check were completed in the previous class.
    Round 2 (issue 225, part B.3) changed the frame: the scene is presented as \"the client keeps a tracker\", not \"the data is not in the repository\".
    The storytelling revision (issue 225, P2) changes the genre of the scene while leaving the
    facts: instead of the cycle \"I copy — I paste — I copy back\", repeating in general, it shows
    one Tuesday on which that cycle broke down. The miss is named (the morning snapshot was
    copied), and the cost is named in terms the room understands (an hour, an email, lost trust
    in the transfer). The frequency \"a few times a week\" and the fact that \"the tracker changes
    without the developer\" are kept — n11, n12 and n20 rest on them.
    The task \"the form does not submit from a phone\" is the same as in the previous edition of
    the scene; the second line of the requirement (\"and from a tablet\") was added by this
    revision as the subject of the miss."
---

# The Tuesday the transfer by hand failed

## Assertion

On Tuesday morning the developer copied the issue into the agent's chat. In the afternoon the client added one line to that same issue. In the evening the edit went out without it: an hour of rework, an email of explanation — and a client who now double-checks whether what he wrote made it through.

## Visual

> The site is in its third month. For a month now the client has been keeping his tasks in a tracker — the developer suggested it himself, so that edits would stop getting lost in a messenger. The transfer between the tracker and the agent's chat the developer does by hand, a few times a week.

1. Tuesday morning: opened the issue "the form does not submit from a phone", copied the text into the agent's chat, went off to make the edit.
2. In the afternoon the client added a line to that same issue: "and from a tablet too".
3. The developer did not see it — what he had in the chat was the morning's snapshot. In the evening the edit went out to the client.
4. In the morning, in the issue: "what about the tablet?". An hour on a second edit and an email explaining why a requirement from the issue did not make it through to the work.

> The hour lost is the smaller part of the cost. The larger part is that the client now double-checks whether what he wrote reached the work. The tracker lives in a separate system and changes every day without the developer: a snapshot taken in the morning is already inaccurate by evening.

## Speaker notes

The site is in its third month. For a month now the client has been keeping his tasks in a tracker — the developer is the one who suggested it to him, so that edits would stop getting lost in the correspondence. The transfer between the tracker and the agent's chat the developer does by hand, a few times a week: open the issue, copy the text, paste it into the chat, copy the finished answer back into the issue. That is where those two requests the agent did not find on Monday were lying.

Tuesday of the same week. In the morning the developer opens the issue "the form does not submit from a phone", copies the text into the agent's chat and goes off to make the edit. In the afternoon the client adds one line to that same issue: "and from a tablet too". The developer does not see it: what he has in the chat is the morning's snapshot of the issue, and a snapshot does not know how to update itself. In the evening the edit goes out to the client. In the morning a question appears in the issue: "what about the tablet?".

The cost is an hour on a second edit and an email explaining why a line from the issue did not make it through to the work. The hour is the smaller part here. The larger part is that the client now double-checks whether what he wrote arrived: a habit he picked up precisely because one time it did not. Getting that trust back costs more than redoing the form.

It was not the agent that made the mistake here. The mistake was in the transfer by hand: by construction it hands the agent the issue's past state, and no amount of care changes that property.

Discipline — re-reading the issue before you send — looks like a solution and works right up to the day there are three issues and five sessions. The cost of that discipline grows linearly with the number of issues and sessions, and a forgotten line goes from being an exception to being the norm. Asking the agent to "keep an eye" on the tracker will not work either: the agent works within one session, it does not carry on acting between requests, and it has no way of its own to reach an external system without access being granted. A tracker open next to you in a browser changes the form of the transfer while leaving the transfer itself: a paste stays a paste, and the morning's snapshot stays the morning's.

It is worth noting what is not in this scene. There is no careless developer in it: he suggested the tracker himself, he carries issues over a few times a week, and that Tuesday he did everything he always did. Nor is there a broken tool in it: the tracker worked, the agent worked, the edit went out on time. What broke down was the link between them — the one place nobody designed and which therefore nobody is responsible for. Places exactly like that are what collect the cost: they have no owner, and people start fixing them after the first email of explanation.

This mistake has a mirror image, and it is more expensive. The developer pastes the agent's answer about a different issue into an issue — the client reads somebody else's requirement as his own and plans work he never asked for.

The detail of the scene is needed for the choice that is coming next: it depends on two of the scene's properties — the frequency of the transfer and the liveness of the source. A source is called live here if its answer depends on the time of the request. A specification file in the repository is not live in that sense: it changes by a commit, and the commit is visible. The tracker changes without a commit and without a notification — and it is this Tuesday that shows which of the two cases we are facing.
