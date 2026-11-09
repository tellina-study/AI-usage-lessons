---
id: n41
type: answer_breakdown_table
duration_min: 1.0
assertion: "Task class: a model re-checking its own answer with no external correctness criterion is, with high probability, a degradation; code is more reliable than a judge exactly to the degree that the criterion itself is reliable"
learning_goal: "The case's generalization — a portable wording with no tool name. The second statement must stand right next to the first: without it, the case reads as 'code is always right,' which the measurement itself didn't show."
visual:
  pattern: answer_breakdown_table
  primary: >
    Two statement banners, one under the other, each a full sentence;
    below them a task-class line, highlighted in gold, and a short line on
    what follows from this for building a process.
  backup: >
    Both wordings follow SETKA-KEYSOV-S9.md, section "Case 3," subsection
    "Generalization," portable, with no orchestrator name and no node
    names.

    The second statement ("code is more reliable exactly to the degree
    that the criterion itself is reliable") stands here not as a softening,
    but as a mandatory half of the conclusion: our own measurement gave
    code one false rejection out of six, and a generalization that doesn't
    mention this would disagree with the case's own measurement.

    A separate line names what follows from the conclusion for building a
    process: the checker gets checked with the same care as the generator.
    That's the portable part — it doesn't depend on the tool or the model.

    Numbers aren't repeated on this frame: they were already presented in
    beats n37, n38, n39, and n40, and a generalization that retells the
    numbers eats the space where the wording itself needs to stand.
---

# Task class

## Assertion

The checker gets checked with the same care as whoever writes the answer.

## Visual

> **Rereading one's own answer with no external correctness criterion more often makes it worse, not better.** The second call knows exactly what the first one knew: no new data, no ground truth, no way to find out it's wrong. It looks like insurance, and it works like an extra loop.

> **Code is more reliable than a judge model exactly to the degree that the criterion itself is reliable.** Nobody here has absolute reliability: a formal check is reproducible and explainable, but it fails where the criterion is written carelessly — and it fails silently.

> **Task class.** A check before sending is built around a criterion that can be written down and read — and that's when code becomes the checker. Where no such criterion can be written, there is no checker in the process at all, and that needs to be known before building it.

> **What follows from this for building a process.** The checker is as much a part of the process as the generator, and deserves the same breakdown: who renders the verdict, what it's based on, whether it repeats tomorrow, and what each attempt costs.

## Speaker notes

Let's fold the case into wordings that can be carried over and applied to your own process, without recalling a single node name.

First. Rereading one's own answer with no external correctness criterion more often makes the result worse, not better. The reason is simple and has nothing to do with the model's quality: the second call knows exactly what the first one knew. It has no new data, no ground truth, no way to notice it's wrong right now. A self-review like this looks like insurance, and it works like an extra loop — our own measurements and other people's say the same thing, equally.

Second, and it must stand right next to the first. Code is more reliable than a judge model exactly to the degree that the criterion itself is reliable. We saw both ends today: the judge was wrong five times out of six and invented reasons, but code was also wrong once out of six — it didn't recognize the needed word in a different grammatical case. The difference isn't that one is always right. The difference is that code's mistake is visible in the code and repeats identically, while the judge's mistake is visible nowhere and never repeats at all.

From this comes the task class. A check before sending is built around a criterion you can write down in words and read with your eyes: length, a required word, an allowed set of numbers, language. Where no criterion can be written down, there is no checker in the process — and that has to be known before building it, before the first month of running quietly with no complaints.

And what follows from this in practice. The checker is as much a part of the process as the generator, and deserves the same breakdown. Who renders the verdict. What that verdict is based on. Whether it repeats tomorrow on the same text. And what each attempt costs. Four questions worth asking your own process before it runs for a month with no complaints.
