---
id: n30
type: base_and_edge
duration_min: 2.0
assertion: "The agent works in your session and talks to you; a subagent is a separate worker whom the agent calls for one task, with a context of its own, and back into your session the subagent returns only the result — by itself, without you being involved"
learning_goal: "The base of the tool at the start of the rung, before its first case (the round-3 consolidation: the base and the one-pager stand at the start of the section, in the same order as n07/n09 in the MCP section). Round 5 (issue 225, ZADANIE-KRUG-5.md): the slide was reassembled for the owner's three direct requirements — separate \"agent\" from \"role\", remove the word \"window\", and show in a diagram what comes into the context at start-up and from where. The diagram's third box (a second session) answers the room's question \"why not open a second session\" BEFORE the question is asked: up to round 5 the answer lay only in the reference material of the scene, and the case read as unexplained"
visual:
  pattern: mechanics_with_figure
  figure: subagent-n30-kontekst-i-subagenty-en.png
  backup: "Round 5 (issue 225, ZADANIE-KRUG-5.md, the remark on case 4: \"the terminology of agents and roles gets confused, a little diagram with the agents is needed… window is a so-so term as well… it is context, surely. And we need to show what comes into it at start-up and from where\"). It was: a table \"BASE / WHAT DECIDES THE OUTCOME\" in three rows plus a paragraph on portability — the base_and_edge device, the word \"window\" fifteen times on the slide, and no diagram at all. It became: a diagram in two tiers. The upper one — the four sources of the context at start-up, with \"from where\" named for each (the system part from the harness, the project's instruction files, the definitions of the connected servers, the conversation itself); the shares are deliberately NOT drawn as segments of one scale — the seminar has no measured share, the standing cost for the servers is measured separately and it alone (n18), and a scale with invented proportions would be a number with no base. The lower one — three contexts side by side: the session with the agent, the subagent the agent called, and a second session; the difference between the latter two is held by the grammar of the arrows, not by words (a solid gold \"the result by itself\" from the subagent into the session, a dashed \"through you\" from the second session). The facts of the previous table are not lost: \"only the result comes back\" is on the diagram as an arrow and a caption; \"a call by name or by description\" and \"the tool list\" are blocks 2 and 5 of the n31 one-pager, which comes as the next screen; portability is on the bottom line of the canvas itself (the slide's `## Visual` is empty: with text blocks beside it the diagram runs into the ceiling of `deck_kit.FIG_NATURAL_H` and gets squeezed). The device was changed from `base_and_edge` to `mechanics_with_figure`, because `g_base_edge` does not draw a diagram at all; the `type` was left as it was — the slide on the subagent in the section is still the base. The point size was measured in points, not by eye (the same mistake happened twice with the one-pagers n09 and n31): a canvas of 2400×1170 px sits on a slide 11.92″ wide, that is 201.4 px per inch, the smallest text at 23 px is about 8.22 pt against the deck's threshold of 7.5 pt, and the main body at 24–27 px is about 8.6–9.7 pt. The slot went 1.25 → 2.0 min; the compensation is n36 (1.0 → 0.75) of the same zone, with the count in qa/krug5-subagent-keys1.md.
    Separating the contradictions (issue 225, 2026-10-07, qa/n30-sostav-konteksta.md): the third line of tier 1 (\"the definition of every tool in full, across all servers, before your first question\") was the deck's one place asserting that connected servers put full schemas into the context unconditionally — after n09/n18/n24/n25 moved on the same day to \"the tool names and the server's instructions\", that became an open contradiction in the section coming straight after the case about the context overflowing. It was replaced by \"the tool names and the server's instructions\" / \"across all servers, before your first question\" — the same wording as on n09 and n18, and the same thing n25 confirms separately (names + the server's instructions, both items). The condition \"by default\" was not added: as on n18, this is a lower bound, true under any mode — the deferral only adds full schemas to it rather than cancelling the very fact of the name and the instructions being present. The figures and `duration_min` did not change.
    An edit after two delivered classes (issue 225, qa/RAZBOR-PROVEDENIYA.md §A1): the term
    \"role\" was replaced across the whole deck by \"subagent\" — the lecturer stumbled over it aloud
    in both groups, and round 5 got it wrong by separating two names instead of taking one. The
    quotation of the owner's instruction above is left as it was said. The canvas's middle box now
    reads \"A SUBAGENT CALLED BY THE AGENT\" with the caption \"a separate worker for one task\" (the
    previous caption, \"in the documentation — a subagent\", added nothing after the unification),
    and the canvas was renamed to `subagent-n30-kontekst-i-subagenty.png`. The figures, the tiers
    of the diagram and `duration_min` did not change."
---

# The agent, the subagent and the context of each

## Assertion

The agent works in your session — it is the one you talk to. A subagent is a separate worker whom the agent calls for one task: its own context, its own reading, and only the result back. And that result comes back by itself, to the place the work sits in.

## Visual

## Speaker notes

Two words stand side by side from here on all the time, and they are worth separating right away. **The agent** is what works in your session and what you talk to. **A subagent** is a separate worker whom the agent calls for one task. The third word is **context**: what the agent or the subagent holds with it while it works.

The upper tier of the diagram answers the question the whole count begins with: what gets into the context at start-up and from where. There are four sources.

The first is brought by the harness — the environment the agent works in: the system part, which states what tools there are, how to answer and what is forbidden. The second is brought by the repository: the project's instruction files, `CLAUDE.md` and `AGENTS.md`, at every level — from the root down to the folder the work is going on in. The third is brought by the connected servers: the tool names and the server's instructions, across all the servers, before your first question. That is the very standing cost the seminar's previous section measured in tokens. The fourth source is the conversation: the task, the agent's answers, and the contents of every file it has read.

Three of the four sources arrive before your first line. You did not write them and did not choose them; they have already taken up the room. Of the four only the last one grows — with every file the agent has opened. Hence a property that looks strange in the work: the context runs out earlier than the length of the conversation would suggest.

The bars of the four sources are drawn the same width, and that is a decision, not styling. The seminar has no measured share for each: the standing cost of the connected servers is measured in tokens and as a share of the context, while the other three sources nobody has measured over a sample. A scale with proportions set by eye would read as a measurement that never happened.

The lower tier is who holds that context. There are three boxes here, and the comparison between them carries the whole breakdown.

On the left, the session the work sits in: that same agent you talk to, and its context — all four bars from above. The edit sits here, and the result of the reading is needed here too: otherwise there is nothing to carry the edit on with. Read forty files here, and the fourth bar will crowd out the task you explained to the agent.

In the middle, the subagent the agent called. Its context is its own: the same three upper bars, and in place of the conversation, one task sent as text. Your correspondence is not there. The forty files land there and close along with the subagent, and only the result goes back — and it goes back without you being involved, into the same session the edit sits in. That is the solid gold arrow on the diagram.

On the right, a second session, which you opened: its own agent, its own context. The forty files land there, and the working context stays clean — exactly the same thing a subagent gives. But the answer stays there: there is no channel into the working session. You carry it over yourself, by hand and in your own retelling, and the agent making the edit sees only that retelling. That is why the way back is drawn as a dashed line and leads through you. A second session frees up the context and stops at that: it does not carry the work on.

Hence three differences between a subagent and a second session, and all three stand on the diagram. The result comes back by itself, into the context the work sits in. A subagent's behavior is set by a file, so the second call repeats the first. And a subagent's permissions can be trimmed down by a list — a second session has no permissions list at all.

Several questions arise right here, and the answers to them are short. The agent calls as many subagents as are needed; it is itself single while doing so, and the limit on the number of subagents is broken down in the rung's second case. A subagent does not remember a previous call: every call raises its context from zero, and nothing is carried over between calls. That is the same property read from the other side: the context is single-use and therefore clean, and the rung's first case takes its benefit from precisely that. How to call a subagent — by name or by letting the model choose itself — takes up the whole of the next screen.

The bottom line of the canvas is about the portability of the technique: a separate worker with a context of its own exists in several products for working with code, each one's notation is its own, and not one of them has a shared specification. What is portable is the skill, not the syntax.

Out of the whole diagram, the count in the next breakdown rests on the gold arrow: the result comes back by itself, to the place the work sits in.
