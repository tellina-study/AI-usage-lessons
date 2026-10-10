---
id: n47
type: research_evidence
duration_min: 1.25
assertion: "The two subagents from the previous scene — the one that set up the lookup list and the one that configured the form — have no third one checking them against each other for consistency; and by a measurement over 1600+ traces of multi-agent systems, misalignment between agents accounts for 37% of failures, almost level with the specification of the task itself"
learning_goal: "Scale, not a single case: the evidence base of this boundary is research, not a demonstration on a student's machine. The slide stands at a low-energy minute of the seminar — the headline and the first line name our two subagents straight away, not an abstract percentage; the explicit caution about the striking \"79%\" figure goes into the notes, it does not hang on the screen as a plate of its own. The honest gap is named directly"
visual:
  pattern: evidence_table_with_gap
  primary: "A short plate at the top, BEFORE the table: the lookup-list configurer and the form configurer work with no third subagent checking them for consistency — that is what the table below is about. A table of two rows in three columns: source · claim · strength of evidence, with the bibliography compressed to the author and the arXiv number. Under the table — a single honest-gap plate; the warning about \"79%\" goes into the speaker notes and does not hang there as a second plate."
  backup: "The sources are section-2-subagent-part1a2.md §A.2 \"Evidence\" + \"Caution with the count\" + \"An honest gap\", section-2-subagent-part1c.md n46, verbatim in substance; the numbers did not change (owner's round 3, issue 225 — the material is carried over without altering the wording or the sources). The attribution \"Kim, Gu, Park et al.\" is a fact-check round-2 correction (2026-10-05), kept as it is. The second roast (issue 225, student simulator): the slide stands at minute ≈64-65, the most vulnerable point of the seminar for attention, and it led with abstract percentages, with the tie to our two subagents as a third plate at the bottom in small type. Three stacks under the table (subagents / caution with the count / honest gap) overloaded exactly the point where density ought to have been coming down. The edit: the tie to the subagents was moved INTO THE HEADLINE AND THE OPENING of the slide (assertion + a plate before the table, not after it), and \"caution with the count\" was taken off the visible layer into the speaker notes (the warning is spoken aloud, it does not hold a frame of its own on the screen) — from three visible blocks after the table down to one. The numbers and facts did not change, only the order of presentation and the number of visible blocks. Storytelling revision (P6): the screen is untouched to the character — the numbers, the sources, the plate tying it to the two subagents and the honest gap are the same. The speech was trimmed (205 words → 170) and tied by one sentence to the turn of the case: dependency between steps costs more than parallelism saves. The warning about \"79%\" was moved out of the speech into the notes entirely — it is spoken where it belongs and takes up no slot. Owner's round 5 (issue 225, ZADANIE-KRUG-5.md): the screen, the numbers, the sources and the attributions are untouched to the character. Slot 1.5 → 1.25 (a quarter minute given to the n39 exercise), the speech was trimmed 170 → 155 words to fit the slot; the tie to the turn is preserved verbatim. Revisions after the classes were held (issue 225, qa/RAZBOR-PROVEDENIYA.md §A3): the numbers, the sources, the attributions and the honest gap are untouched to the character — all that changed was the tie to the scene, which was rewritten around the facilitator's example (the lookup list and the form). After that replacement the MAST row about the specification of the task itself works on the scene more directly than before: it is exactly its absence that breaks the scene.

    Note on the quoted category: \"task and role specification\" is MAST's own category vocabulary, cited as the taxonomy names it. It is NOT this seminar's vocabulary — the term \"role\" was retired across Seminar 6 in favor of \"subagent\", and this row is the one place where the external source's word is kept because altering it would misrepresent the source."
---

# Scale, not a single case

## Assertion

The two subagents from the previous scene have no third one checking them against each other for consistency. By a measurement over 1600+ traces, misalignment between agents accounts for 37% of failures — almost level with the specification of the task itself.

## Visual

> **For our two subagents.** The one that set up the lookup list and the one that configured the form are working with no third subagent checking them for consistency. Here is what a measurement at scale, rather than on a single case, says about that.

| Source | Claim | Strength of evidence |
|---|---|---|
| Cemri et al., "MAST", arXiv:2503.13657 (NeurIPS 2025 D&B) | From 41 to 87% of annotated traces (depending on the framework) are failures; three categories of cause: task and role specification ≈42%, misalignment between agents ≈37%, verification of the result ≈21% | strong: manual annotation of 1600+ traces across 7 frameworks, inter-rater agreement κ=0.88 |
| Kim, Gu, Park et al. (Google Research), arXiv:2512.08296 | On a sequential task the scheme loses to the single-agent version of the same task by 39-70%; with no coordinator the number of errors is amplified 17.2× relative to a single-agent system at the input, with centralized checking — 4.4× | strong: a controlled experiment, 260 configurations, 6 benchmarks, 5 architectures |

> **An honest gap.** There is nothing with which to test the misalignment of two parallel subagents on the course repository or on a student's machine — none of the seminar's checkability supports demonstrates this. The claim is backed by research, not by a command run in class.

## Speaker notes

The two subagents from this story have no third one checking them against each other for consistency. The case looks particular — until you look at what a measurement at scale says about it.

The first source is a taxonomy of failures in systems made of several agents, Cemri and others, the paper "MAST", arXiv:2503.13657, accepted at NeurIPS 2025 into the Datasets and Benchmarks track. More than 1600 traces were annotated by hand across seven different frameworks, with agreement between the annotators on the kappa scale at 0.88. Failing traces run from 41 to 87% depending on the framework. The causes fall into three categories: task and role specification accounts for about 42%, misalignment between agents for about 37%, verification of the result for about 21%. Misalignment between agents stands as the second cause by weight, almost level with the description of the task itself. That is the gap from our story, counted over a sample.

The second source is a controlled experiment about the cost, Kim, Gu, Park and others, Google Research, arXiv:2512.08296. Two hundred and sixty configurations, six sets of tasks, five architectures. On a sequential task a scheme made of several subagents loses to a single-agent one on the same task by 39 to 70%, and the number of errors is amplified 17.2 times relative to a single-agent system at the input. With centralized checking the amplification falls to 4.4 — it falls, but it stays an amplification. There is the figure under the turn of this case: where the steps are dependent, splitting them into subagents costs more than everything the parallelism could have saved.

About inter-rater agreement, it is worth saying why that figure is looked at at all. A kappa of 0.88 means high agreement: the categories were told apart by different people and they converged with each other. That is what makes the taxonomy fit to cite — the annotation here is not arbitrary.

The second source does not publish an absolute number of errors, and it is honest to say so directly. Only the relative amplification is given — how many times more than for a single subagent on the same task. "Seventeen times more" with no base value speaks about direction and says nothing about size, and you cannot supply the base yourself.

The spread "from 41 to 87%" looks so wide that one wants to discard it, and that is not worth doing. The spread runs across frameworks: different systems fail differently. One thing in it matters — nowhere did the share of failing traces turn out to be small.

Separately, about the figure "79% of failures are a specification problem", which has gone around the internet and turns up in retellings of this work. It is the sum of MAST's first two categories, 42 and 37, retold as though it were a separate measurement. If you meet it, it is worth checking whether the same thing is being counted twice under different captions.

Do these figures carry across to two subagents directly? No, and that has to be said before somebody arms themselves with a seventeen-fold amplification in a conversation about a pair of workers. Both studies measured systems made of many agents; the direction carries across, the order of magnitude does not. For two subagents it is more honest to speak of the risk of a gap, which is measured as the second cause of failure by weight.

And the honest gap, because in class it is named directly. There is nothing with which to test the misalignment of two parallel subagents on the course repository or on your machine: none of this seminar's checkability supports demonstrates such a thing. The claim rests on research, not on a command you can type into a terminal. The seminar's other supports are checkable by hand; this one is not.
