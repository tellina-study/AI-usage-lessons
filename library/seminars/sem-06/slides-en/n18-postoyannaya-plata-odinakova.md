---
id: n18
type: mechanics_map
duration_min: 1.25
assertion: "The standing cost is set by the number of connected servers and the number of their tools — your own server, somebody else's locally and somebody else's remotely all pay it identically; the cost of a connection as named describes the mode without deferred loading and gives the upper bound of the worst case"
learning_goal: "The mechanics of the cost: what actually gets into the context at the start of a session, what the deferred loading of tool schemas depends on, and where the upper bound of the worst case runs. Round 2 of the owner's edits (issue 225, part A9): the standing cost and the cost of a call are already separated on n09 (block 5), and here is the comparison across ways of getting access promised there, resting on the same evidence base rather than on an invented estimate. A candidate for compression if time runs short"
visual:
  pattern: mechanics_table
  figure: mcp-n18-dolya-konteksta.png
  primary: "The share of the context is shown as a proportion (a filled bar, 21% of 200K), not listed as a number in a table; beside it — the comparison of 1,365 against 44,026 tokens by the same device (two bars, captioned with the absolute numbers, with the 32-fold difference in gold). Above the checking line — a short comparison of the access variants by their effect on the context."
  backup: "Source — rework/section-1-mcp.md §A.1.9, §B.9 (part1c.md). The 21% share of the context was added during the stitch-up (qa/chetvyortaya-stena-otchet.md item 4, source getunblocked.com) — the same source and scenario, with no recalculation. A second measurement, different in method (zhang-liz, 13.1%), exists and is not brought onto the visible layer — the divergence is explained by the different composition of servers in the measurement, not by an error in carrying it over. Fact-check: VERIFIED on ENABLE_TOOL_SEARCH (qa/fact-check-mcp.md §2.2 item 10).
    The visual session (issue 225): the two-row table was replaced by a diagram (rendered/
    make_figures_mcp.py) — the share of the context is drawn as a proportion (a filled bar on a
    0..200K scale) rather than named as a number in a cell; the comparison of 1,365/44,026 is two
    bars on a shared scale rather than a pair of figures in a row. The closing caveat about
    ENABLE_TOOL_SEARCH remains a text block under the diagram — it is a checking command, not part
    of the proportion.
    Round 2 of the owner's edits (issue 225, part A9, the line-by-line breakdown of n18): the owner
    asked for the standing cost and the cost of a call to be separated (done on n09, block 5) and
    for the access variants from the breakdown (n12) to be compared by their effect on the context,
    resting on research rather than on an invented estimate. One line was added above the checking
    command — it introduces no new figures but explains why 1,365/44,026 is an apt comparison here:
    the standing cost depends only on how many servers are connected and how many tools they have
    (mechanics-5-mcp.md §2.1–§2.3) — the transport (local/remote) and the authorship (your own /
    somebody else's) have no effect on it; the only thing that does not pay it is something that is
    not an MCP server at all.
    The storytelling revision (issue 225, P1 by its second half and P5): that line was the second
    overturning of the obvious — the cost of a connection depends neither on the transport nor on
    the authorship — but it stood as an addendum above the checking command. It was raised into the
    title and into the assertion; the previous title (\"A connection costs tokens — but that is the
    cost of the worst case\") is preserved in sense in the assertion and in the speech. P5 — a
    block \"To yourself\" was added: the one question in this section of the seminar addressed to the
    room's own project (how many servers are connected right now and how many tools they describe).
    The diagnostic commands (`claude mcp list`, `/mcp`) are deliberately not named on this screen —
    n17 introduces them, and here they would be a repeat of the neighboring screen.
    The slot went 0.75 → 1.25 (compensated by n13 1.5 → 1.25 and n19 2.75 → 2.25, the section's
    total unchanged); the speech was cut from 208 words (1.60 min against a slot of 0.75) to 156
    (1.20 min). The figures 21%, 1,365, 44,026, 55,000, $3.20/$55.20 and the sources did not change.
    Separating the contradictions (issue 225, 2026-10-07): \"The name and short instructions of every connected server\" on the visible layer and in the notes was replaced by the tool names and the server's instructions — the same as what n24 and n25 print, and the same thing the measured 42–55 thousand tokens for 93 definitions agree with. The length of the visible line was held to the previous number of lines (the \"DIAGRAM SQUEEZED\" guard was firing on the longer wording). The figures 21%, 1,365, 44,026, 55,000 did not change."
---

# The standing cost is the same: your own, somebody else's, local, remote

## Assertion

The standing cost is set by the number of connected servers and the number of their tools: your own server, somebody else's locally and somebody else's remotely all pay it identically. The cost of a connection as named describes the mode without deferred loading — it is the upper bound of the worst case.

## Visual

> **The standing cost is set by the number of tools.** The tool names of every server and the instructions about it hang in the context always. Your own server, somebody else's locally, somebody else's remotely all pay it identically: the transport and the authorship make no difference. Free of it are a direct API call and a command like `gh` — they have no list of capabilities hanging in the context between calls.

> **To yourself.** How many servers do you have connected right now and how many tools do they describe? You pay that cost in every session — including the one in which the agent did not go to a single one of them all day.

> To check at your own place: whether `ENABLE_TOOL_SEARCH=false` is set, and what the card of a particular server actually shows in a session — the command does not go out of date, unlike the figure itself.

## Speaker notes

Now the figure that is often spoken of inaccurately. "A connection costs so many tokens" is a statement about the mode without deferred loading. By default, at the start of a session what gets into the context is the tool names and the server's short instructions, without the full schemas.

The worst case has been measured: a bundle of five servers with no deferral — on the order of fifty-five thousand tokens, about twenty-one percent of a context of two hundred thousand. That is the upper bound. For comparison: one and the same action by an ordinary command in the terminal is one thousand three hundred and sixty-five tokens, by a server's tool it is forty-four thousand and twenty-six. A thirty-two-fold difference for one answer.

What exactly that cost is paid for is worth taking apart piece by piece — otherwise the numbers look arbitrary.

The standing cost is the names of all the tools of every connected server and the server's short instructions about itself: what, under deferred loading, lands in the context at start-up. They hang in the context the whole time, from the first second of the session, regardless of whether the agent uses the server or not. Two numbers set it: how many servers are connected and how many tools each one describes. That cost depends neither on the place where the server runs nor on who wrote it — your own, somebody else's, local, remote all pay identically. The transport has no effect on those two numbers: a remote server describes its tools with the same names and the same instructions as a local one, and the same description gets into the context. The authorship has no effect either: your own server written for three operations pays for three descriptions — exactly as much as somebody else's with three operations would pay. What you pay for is the list of capabilities, and the list does not know where it arrived from.

The cost of a call is a separate line item: it is every answer the server returned. That is where the comparison of one thousand three hundred and sixty-five tokens against forty-four thousand belongs: one and the same action, the same result, a thirty-two-fold difference in how much room getting it took up.

Free of the standing cost are a direct API call and a command like `gh`. They have no list of capabilities hanging in the context between calls: until a call is made, there is nothing about them in the context.

Hence the question to your own project, worth asking yourself right now: how many servers do you have connected and how many tools do they describe? You pay that cost in every session — including the one in which the agent did not go to a single server all day.

The mode can be checked at your own place by two actions: look at whether the variable `ENABLE_TOOL_SEARCH=false` is set, which turns deferred loading off, and look at what the card of a particular server actually shows in a session. That check does not go out of date, unlike the figure itself.

Why the figure is named at all, then: it remains correct as the order of magnitude of the worst case — for platforms without deferred loading, or for a session that really did pull in almost all the definitions through the internal search. The same effect has been independently confirmed by another team of researchers, and in money: three dollars twenty cents against fifty-five dollars twenty cents for ten thousand operations of one kind a month, a seventeen-fold difference, a different method.

The conclusion from this is not "connecting a server does not pay". What makes it pay is the thing the cost was paid for: the agent sees the list of operations itself and picks the one it needs. Where there is one operation and it is known in advance, there is no point paying for the list — and that is exactly the criterion the case closes with.

What remains is to explain why the full schema is not pulled in straight away. There are many schemas, and only a handful of them will be needed. Deferred loading is the default behavior on current models; it is switched off by an environment variable, and it is sometimes found switched off in somebody else's ready-made settings.
