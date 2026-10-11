---
id: n44
type: mechanics_map
duration_min: 1.0
assertion: "Sessions cost machine memory: by the course author's own measurement, on a cloud VM with 16 GB the work starts stumbling at twenty concurrent sessions and gives out at thirty to forty — which puts the order of magnitude at 1-2 GB per session; the tool's cap of twenty concurrent subagents may be overtaken by the hardware sooner"
learning_goal: "The cost of the previous move, named in units that can be checked on your own machine. The measurement is presented as one person's measurement on one configuration with a named baseline (16 GB), not as an industry norm: the reader gets an order of magnitude and a way to re-measure it for themselves. Two separate caps are kept apart — the concurrency of subagents inside a session, and machine memory for sessions"
visual:
  pattern: mechanics_table
  primary: "At the top — a line saying whose measurement this is and on what machine. Below — a table in two substantive columns: what was measured and what follows from it, three rows. Under the table — a short line about the difference made by the language the agent itself is written in. The slide is closed by a line in gold: the order of magnitude, which is worth re-measuring for yourself."
  backup: "The source is the course author's measurement on his own machine, named at both of the classes this deck was delivered in (transcripts: `qa/rasshifrovki/gruppa-1.txt`, 34:31; `qa/rasshifrovki/gruppa-2.txt`, 53:36-55:38). Added under section B of the delivery breakdown (`qa/RAZBOR-PROVEDENIYA.md`), item 2.

    Verbatim supports. The baseline and the threshold: \"I've got a 16-gig VM in the cloud, at 20 sessions it starts feeling unwell\" (group 1, 34:31); \"I've got a VM, my cloud one, it starts somewhere from 20, and at 30-40, depending on how big they are, it dies\" (group 2, 54:03). The per-unit consumption: \"you need at least 2 gigs per session\" (group 1, 34:31), \"roughly, very roughly, you have to budget somewhere around 1-2 gigs of RAM per session, even when they're just sitting idle\" (group 2, 54:03) — the 1-2 GB range was taken into the material as the later and more cautious wording of the same measurement, with the caveat \"at rest\". The surprise: \"you'd think it's a thin client that just shuttles text back and forth... it's too early for us to give up good laptops with good memory\" (group 1, 34:58).

    The agent's language: \"one's sort of written in JS, the other... one of them is written in Rust, and it's like 10 times lighter\" (group 2, 54:42). The multiple is NOT put on the screen: in the same sentence the author was getting confused about which of the two tools was written in which language, and he named the multiple by eye. The screen says \"noticeably lighter\", and the notes say outright that the multiple was named by eye and the units were not recorded. The names of the two tools are not given for the same reason. [FACT-CHECK: which language each of the common agent clients is written in, and what the real gap in memory is — NOT brought into the material; bringing it in requires a measurement, not an impression]

    The baseline for the figures (CLAUDE.md, § \"Baseline / Counterfactual Mandate\"): the 16 GB is named outright, and the 1-2 GB range agrees with it — 16 / 20 ≈ 0.8 GB per session at the lower threshold. The counterfactual is named in the notes: one or two sessions on a machine like that create no expense at all, the cost only appears at a dozen.

    Keeping the two caps apart is this round's own finding, not the author's words: the cap of twenty concurrent subagents (`n42`, the environment variable) applies to concurrency INSIDE one session, whereas the 1-2 GB applies to the number of SESSIONS themselves. The coincidence of both numbers at twenty is accidental, and that needs saying, or the reader will add two different caps into one.

    Terminology: the slide was written on \"subagent\", the word \"role\" does not appear in it.

    Literary editing (issue 225, qa/pravki-nahodok-svedeniya.md item 5): the headline \"The cost in
    hardware\" was a nominal phrase among headlines that state things and headlines that set scenes. It became
    \"Sessions cost machine memory\" — the same thing the slide's `assertion` says in its very first clause.
    The number twenty is deliberately NOT put in the headline: two slides earlier, on `n42`, twenty
    means a different cap, and this very slide keeps the two caps apart in a direct line — a headline
    repeating the number would fold them back together. The content, the table, the caveats and the open
    `[FACT-CHECK]` above are untouched. The slide's file name is left as it was: by the seminar canon
    (§1) the file, the manifest and the frontmatter agree by numbers and minutes, not by the wording of the headline."
---

# Sessions cost machine memory

## Assertion

Sessions cost machine memory: by the course author's measurement, a cloud VM with 16 GB starts stumbling at twenty concurrent sessions and gives out at thirty to forty.

## Visual

> The course author's measurement on his own machine: a cloud VM, 16 GB of memory, ordinary sessions with no heavy runs inside them.

| What was measured | What follows from it |
|---|---|
| from twenty concurrent sessions on, the machine starts stumbling | the order of magnitude is 1-2 GB per session, and that is at rest, without what a session will launch itself |
| at thirty to forty, depending on their size, it stops responding | a dozen sessions on a machine like that is the working limit, and it is counted before launching |
| bringing up one more session costs the same as bringing up the first | the tool's cap is twenty subagents at once inside one session; machine memory is counted by the number of sessions themselves and may run out sooner |

> The language the agent itself is written in shows here: a client built in Rust is noticeably lighter than its counterpart in JavaScript. The author estimated the multiple by eye.

> **This is one person's measurement on one configuration. The order of magnitude is worth re-measuring for yourself — on your own memory, your own number of sessions and your own agent.**

## Speaker notes

The previous move has a cost the machine shows, and the token bill does not. There is one measurement here and it belongs to the course author: a cloud VM with sixteen gigabytes of memory, ordinary sessions with no heavy runs inside them.

The measurement looks like this. From twenty concurrent sessions on, the machine starts stumbling: responsiveness drops, launches take longer. At thirty to forty, depending on how much each session has managed to accumulate, it stops responding altogether. Hence the order of magnitude — from one to two gigabytes per session, and that is at rest: a session that has launched a build or a test run itself will eat noticeably more.

The sixteen gigabytes are named here not for completeness: without a baseline the "1-2 GB" range means nothing. The division works out — sixteen over twenty gives about eight tenths of a gigabyte, which is to say the lower edge of the range is exactly the edge at which the machine starts stumbling. The counterfactual matters just as much: one session, two, three cost such a machine nothing noticeable. The expense appears at a dozen and becomes decisive closer to twenty.

The surprise the author voiced at this point is worth repeating, because it throws many people off. By the look of it an agent session is a thin client: it shuttles text in both directions, and it is not the one doing the computing anyway. Yet it uses as much memory as a full-blown application, and it goes on holding its context, its open files and its child processes in memory. The conclusion the author drew from this was direct: it is too early to give up a machine with good memory.

The difference made by the language the agent's client itself is written in becomes visible at this scale. A client built in Rust is noticeably lighter than its counterpart built in JavaScript. The multiple here was named by eye, the units were not recorded, and putting a number on it would be inventing precision. The observation has practical sense all the same: on one or two sessions the difference goes unnoticed, at twenty it decides whether the twenty-first will start.

Two caps that are easy to fold into one are worth keeping apart, all the more so because both equal twenty. The cap of twenty concurrent subagents is the tool's cap, it stands inside one session, and it is changed by an environment variable. The cap of twenty sessions is the machine's memory cap, and no variable changes it: it is changed by buying memory. The coincidence of the numbers is accidental. You can run into either of the two, and confusing them is expensive: having raised the subagent cap, you will have learned nothing about whether the machine will take another five sessions.

How to check this for yourself, if the move with child sessions looked useful. Look at the memory use of one session right after launch and again after an hour's work — those two numbers give you your range. Divide the free memory by the higher of them, subtract an allowance for what the sessions launch themselves, and you get your own number of concurrent sessions. It will be different for you: different memory, a different agent, different tasks inside. The course author's measurement gives an order of magnitude and a way of counting; checking it is worth doing on your own machine.
