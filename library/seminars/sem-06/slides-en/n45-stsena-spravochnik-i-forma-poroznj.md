---
id: n45
type: problem_scenario
duration_min: 1.25
assertion: "A lookup list and the form that leans on it go to two subagents at the same time; there is no shared description of the task. Both jobs are done honestly and fast, and together they do not work: the fields in the lookup list are one thing, on the form another — and reconciling them takes longer than the configuring itself did"
learning_goal: "A test of the turn on a negative example — on two pieces that lean on each other. The parallelism here was real and cost nothing; what was missing was a shared description of the task that both workers read before starting. The scene is a working one, from a configurable platform: parallelizing is especially tempting there, because it is not code"
visual:
  pattern: problem_scenario
  primary: "Two rectangles side by side — the lookup list (the composition of the fields) and the form (which fields it shows and checks), with an arrow \"leans on\" between them and a narrow zone with no owner: there is no shared description of the task. At the bottom — the outcome: the fields diverged, the jobs were reconciled by hand."
  backup: "Revisions after the classes were held (issue 225, qa/RAZBOR-PROVEDENIYA.md §A3). The former scene —
    a diff reviewer and a tester on one indivisible piece, two honest `PASS`es and a gap in front of the
    domain — was rejected out loud by the facilitator in both groups: \"didn't come up with a good example...
    I couldn't come up with a nice example off the top of my head\" (group 1, 41:06), \"that's not a very good example there, just
    a pretty picture\" (group 2, 56:27). Both times he substituted his own, a working one, and both times the same
    one: on a configurable platform a lookup list and the form that leans on it are configured in parallel;
    there is no shared description of the task, the fields diverge, reconciling takes a long time (group 1, 43:36;
    group 2, 56:54-57:39). The scene was rewritten around it. The evidential part of the case is untouched: the numbers
    and sources of n47 (MAST, 1600+ traces, 37%, Google Research, Cognition's reversal of position)
    stayed as they were — what changed was the scene, not the evidence. The example from a student in group 1 (breaking work up
    in testing and code analysis lowers quality and lets problems through, group 1, 41:51-42:12) and
    the former diff-reviewer/tester pair are kept in the notes as a second and third variety of the same divergence.
    The tie to the n39 exercise remains, but at the level of the lesson rather than the piece: there the condition was named out loud,
    here nobody wrote it down. The 1.25 slot did not change.
    Literary editing (issue 225, qa/pravki-nahodok-svedeniya.md item 3): the setting of the scene
    came onto the screen as one bold paragraph in a gold bracket — six lines of bold, in which bold
    weight was no longer emphasizing anything. The text of the scene is untouched, not by a word: the setting
    was moved into the box in ordinary weight, and one thought was left in gold — the outcome the
    scene is told for. The scene was NOT rewritten as numbered steps: the owner deferred that edit
    to himself (finding F3 of the consolidation pass), the example belongs to the facilitator."
---

# A week later: the lookup list and the form, configured separately

## Assertion

Two pieces, and one leans on the other. There are two workers and no shared description of the task. Both jobs are honest and fast, and together they do not work.

## Visual

- A week later — different work: a configurable platform, the kind where lookup lists, forms, access permissions and scripts are set up by configuring. Parallelizing is especially tempting there, because every piece looks like a self-contained screen.
- Two pieces go to two subagents at the same time: one sets up the lookup list, the second configures the form that shows and checks that lookup list. Nobody writes a shared description of the task — it seems superfluous, since the pieces are right there on the screen.

> Both come back with the job done, and both are right: the lookup list is set up, the form is configured. Together they do not work — the fields in the lookup list were named and composed by one of them, the form expects something else. This has to be reconciled by hand, and reconciling takes longer than the configuring itself did.

## Speaker notes

Let us test the conclusion on a negative example. For that, let us take platform configuration: this miss shows up more cleanly there than in code.

A configurable platform: lookup lists, forms, access permissions, scripts are set up by configuring rather than by programming. Parallelizing work like that is doubly tempting — every piece looks like a separate screen you can open and fill in without looking at anyone else. A week later the developer does exactly that: the lookup list goes to one subagent, the form that leans on that lookup list goes to a second, at the same time. He does not write a shared description of the task: the pieces are right there, what is there to describe.

Both come back with the job done, and both are right. The lookup list is set up: the fields are named, the composition is assembled, the values are filled in. The form is configured: the fields are shown, required flags are set, validation is in place. There is no complaint against either of the two — each did exactly what they were given, and did it fast.

Together they do not work. The lookup list's fields were named and composed according to one understanding of the task, the form expects another: some fields do not match by name, some by composition, somewhere a required flag has diverged. The result is two fast and entirely unconnected pieces of work, which then take a long time to reconcile by hand. The reconciling takes more time than the configuring did, and it eats exactly the parallelism the whole thing was started for.

What has been repeated here is the number of workers. The condition under it was not there: the pieces are not independent, one leans on the other. The parallelism, meanwhile, was real, and the harness gave it for free; it is not what let them down. What let them down is that nobody knew the whole task: breaking it up narrowed each worker's context, and a shared description in which the composition of the fields is named once for both did not exist for either of them.

The same miss looks different in code and is built the same way. Split a check into separate independent runs — each one green, and the problem you can only see on the task as a whole gets found by none of them: breaking up lowers quality exactly where it lowered the context. In our landing page a pair of the same kind sits right in the layout: the new field with its validation and the map of error messages live in one file, and the message keys are exactly the lookup list the form leans on.

It is worth clearing the workers themselves of suspicion separately. Neither of the two made a mistake or was lazy: each read their own setup and honestly carried it out. Both reports are correct within their own bounds, and that is precisely why the divergence surfaces late — two green jobs add up to a picture of readiness that does not exist. The pair of checkers is built the same way, if one reads the code line by line and the second runs through scenarios: both report honestly, and neither names the case that fell between their zones.

The link to Friday is direct here, and it is about one word. In the layout the condition was named out loud: which pieces are independent and why got said. Here nobody wrote it down.
