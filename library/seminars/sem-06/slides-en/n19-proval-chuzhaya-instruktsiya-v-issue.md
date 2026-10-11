---
id: n19
type: failure_vignette
duration_min: 2.25
assertion: "Someone else's instruction in an ordinary-looking issue made the agent publish private code to the outside — because three ordinary things coincided: access to private data, the reading of someone else's text, a channel to the outside; without at least one of them an attack of this type is impossible"
learning_goal: "The failure comes back to the co-building screen: the line \"all repositories, including the private ones\", which was just crossed out, is exactly the one without which the scenario does not go through. Round 2 of the owner's edits (issue 225, the line-by-line breakdown of n19 — \"cleverness plus a statement with its context pulled out from under it\"): the title names the risk directly instead of referring back to the co-building screen; the definition of the \"lethal trifecta\" was moved BEFORE the table — the second layer no longer refers to a term the student has not yet seen"
visual:
  pattern: failure_vignette_table
  primary: "Above the table — one line of connection to the co-building screen, then straight away the plate with the definition of the \"lethal trifecta\" (before the table, not after). Below — a table of two layers: what happened · the basis for comparison."
  backup: "Source — rework/section-1-mcp.md §A.1.10, §B.10 (part1c.md). Carried over from sem-05/rework/section-3-mcp.md with no change of content — fact-check qa/fact-check-mcp.md §1 and §2.2 items 2–3: Invariant Labs (May 2025) and Willison's \"lethal trifecta\" (16.06.2025) — VERIFIED. CVE-2026-61742 (DBHub, CVSS 9.3) — inherited from Seminar 5's fact-check-round1.md, not re-verified. The caveat about Strix.ai as a secondary analysis of the \"2 requests\" figure is held in the text of layer 2 itself.
    Round 2 of the owner's edits (issue 225, the line-by-line breakdown of n19): the owner called
    the previous slide (\"The crossed-out line is the very one without which the attack does not go
    through\") cleverness with its context pulled out from under it — the title referred back to
    the co-building screen instead of saying outright which risk was being discussed, and the term
    \"lethal trifecta\" was used in the table (layer 2) before its definition appeared on the slide
    (the plate stood AFTER the table). The edit: the title names outright what happened
    (\"someone else's instruction… made the agent publish private code\"), and the plate with the
    definition of the trifecta was moved before the table — by the time layer 2 mentions the
    trifecta, it has already been named. The facts, figures and dates did not change by a single
    character.
    The storytelling revision (issue 225, P6): the slot went 2.75 → 2.25 (the speech at 1.39 min
    fits with room to spare; the 0.5 min given up went to n18), and the speech was cut from 236
    words to 180. A return to the scene on n10 was added to the reference material — the same flow
    of someone else's text in which a line of a requirement got lost in the scene carries someone
    else's instruction here. The facts, figures, dates and sources did not change."
---

# Someone else's instruction in an issue made the agent publish private code

## Assertion

Attacking text in an ordinary-looking issue made the agent leak private data to the outside — without a single line of exploit code. Three ordinary things coincided: access to private data, the reading of someone else's text, a channel to the outside. Take away at least one — and an attack of this type is impossible.

## Visual

> Let us go back to the co-building screen. We crossed out the line "all repositories, including the private ones" — this is exactly the case where that decided the matter.

> **The lethal trifecta** (Simon Willison, 16.06.2025): access to private data + the processing of untrusted external content + a channel to the outside. With all three present, it is enough for an attacker to write text that the agent will read in the course of ordinary work.

| Layer | What happened | The basis for comparison |
|---|---|---|
| 1 · exfiltration through the bundle (Invariant Labs, May 2025) | An agent with a token for all of the user's repositories, including the private ones. The attacker creates an issue in a public repository with the instruction to gather data about other repositories and publish it here. The developer asks the agent to deal with the open issues — the agent honestly reads them, the instruction gets into the context as a task, it reads the private repositories and publishes their contents in an automatically created public PR | the vulnerability has no number assigned — it is an architectural class of a bundle of permissions, not a hole in code. Remove the line "all repositories, including the private ones" — there is nothing to read, and the scenario does not go through at all |
| 2 · without a model at all (CVE-2026-61742, DBHub, CVSS 9.3 out of 10) | The HTTP transport by default listens without authentication, and the protection against cross-site requests is bypassed by DNS rebinding | per a secondary technical analysis (Strix.ai) — two HTTP requests and zero credentials up to takeover; the same trifecta is not the only route to a leak here — the server itself can be an unprotected network service |

## Speaker notes

Let us go back to the co-building screen — the one that was worth remembering. May 2025, the analysis by Invariant Labs.

A developer's agent goes into the tracker under a personal token with permissions for all repositories, including the private ones. The attacker sets up an ordinary-looking issue in a public repository: gather data about this user's other repositories and publish it here. The developer asks the agent to deal with the open issues — a completely routine request. The agent honestly reads the issues; the instruction built into the text gets into the context as a task, and for the model it is indistinguishable from yours. It then reads the private repositories and publishes their contents in an automatically created public draft edit.

There is not a single line of exploit code in this story. There is no vulnerability number either, and that is not an omission: there is nothing to fix — this is an architectural class, the bundle of "broad permissions plus someone else's text", and it is not a hole in anybody's code.

Now to our screen. The line "all of the user's repositories, including the private ones" we crossed out in the co-building. Without it the scenario does not go through at all: there is nothing to read, and the attack's first step runs into the key's permissions.

The combination that makes a leak like that possible is called the lethal trifecta (Simon Willison, 16 June 2025): access to private data, the processing of untrusted external content, a channel to the outside. With all three present, it is enough for an attacker to write text that the agent will read in the course of ordinary work. Take away at least one leg — and an attack of this type is impossible in principle, not "unlikely".

The generalization here weighs more than the example. GitHub stands in the example because our case assembles precisely that bundle — an issue tracker with a personal token. But the trifecta applies to any agent that has access to data, the processing of text and a channel to the outside, irrespective of the particular product. And the agent reads the same flow of someone else's text in which a line of a requirement got lost in the scene: the issues in a tracker are not written by your client alone.

A second layer of the same construction does without a model entirely. A vulnerability in the transport was found in an MCP server for databases: CVE-2026-61742, the DBHub server, scored 9.3 out of 10. The HTTP transport by default listens without authentication, and the protection against cross-site requests is bypassed by DNS rebinding. Per a secondary technical analysis — two HTTP requests and zero credentials up to takeover; that figure is taken from the Strix.ai analysis, it is not in the primary record, and it is named with that caveat.

DNS rebinding works like this. The DNS name of the attacker's domain first points to his own IP address — so as to pass the check on the request's origin — and then switches to the victim's address. After that the victim's browser considers the request "its own", and the local server executes it. An arbitrary site open in the browser pulls the server's tools directly.

The trifecta is not the only route to a leak here: the server itself can turn out to be an unprotected network service, and this case is exactly that. The openness of the protocol does not protect against it — the openness of a protocol and the authentication of a particular server are different things, and that was already noted in the section's base.

What follows from the two layers for the file we assembled. A key with permissions for one repository closes the first layer entirely. The second it does not close at all: there the matter is how the server listens to the network, and that is settled by the choice of transport — the very decision that was taken in the co-building.

And the answer to the question of why the failure is shown after the decision has been assembled. An assembled decision is only checked by an attempt to break it. A line crossed out without such an attempt is crossed out out of habit — and on the day the habit does not fire, it will not be crossed out.
