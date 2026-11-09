---
# Frame obtained by splitting frame s92 while fixing the first render (10/27/2026):
# everything that stood on one frame did not fit into a 5.36" body at any point size.
# Numbers, plates, columns, schemes, and map cells were carried over UNCHANGED; the minutes are
# taken from frame s92's own budget (1.3 → 0.7 + 0.6), the section total is untouched.

id: s92a
local_id: "s92a"
section: "6. Wrap-up"
type: assertion_visual
title: "Why criteria get written before work begins"
assertion: "Inside the circle of tasks the model pulls, 758 consultants with it did 12.2% more tasks and 25.1% faster at higher quality, while on one task outside that circle the share of correct calls fell from 84.5% without the model to 60% and 70% in two conditions with it — nineteen percentage points; the task looked no different from the other eighteen, which means the boundary of applicability cannot be seen from inside the task"
source: "Dell'Acqua et al., \"Navigating the Jagged Technological Frontier,\" SSRN 4573321, 09/18/2023 (field study with Boston Consulting Group)"
chapter_ref: "chapter-part4.md §§ 6.3–6.4"
media: ""
media_needed: ""
scheme:
  kind: shkala
  unit: "percent correct on one and the same task"
  base: "a task outside the circle; 758 consultants, three conditions"
  from: 50
  to: 90
  marks:
    - {value: "60", label: "with the model", key: true}
    - {value: "70", label: "with the model and prompt training"}
    - {value: "84.5", label: "without the model"}
blocks:
  - {label: "Inside the model's circle of tasks", value: "12.2% more tasks and 25.1% faster", note: "a large win by the standards of experiments, without the model"}
  - {label: "The gap on this task", value: "19 percentage points", note: "a difference of SHARES of correct calls, not percent of percent", key: true}
  - {label: "The rule this gives", value: "criteria get written before work begins", note: "the boundary cannot be seen from inside the task; measured with a stopwatch and a share of correct calls"}
timing_min: 0.6
in_bucket: true
method_steps: ["refusal criteria", "the measurement that requires them"]
form: []
vfy: false
status: собран
---

## Visible slide text

**The harm comes from the invisibility of the boundary — the quality of the tool has nothing to do with it.** The task outside the circle looked no different from the other eighteen.

## Speaker notes

And here is what makes these four rules actually work: they are written down before work begins.
The reason is measured. Seven hundred fifty-eight consultants were randomly assigned to three
conditions — without the model, with the model, and with the model plus introductory training on
working with prompts — and given real working tasks. Inside the circle of tasks the model pulls,
participants with it completed twelve and two-tenths percent more tasks and twenty-five and
one-tenth percent faster, at significantly higher quality. But on one complex managerial task,
specifically chosen outside that circle, the share of correct decisions fell: eighty-four and a
half percent without the model against sixty and seventy percent in the two conditions with it.
The difference is nineteen percentage points, and the unit has to be said out loud here, because
the phrasing "19 percent less often" would describe an entirely different quantity. The task
looked no different from the other eighteen. The boundary of the model's capability is jagged:
neighboring tasks of similarly looking difficulty fall on different sides of it. The harm comes
from the invisibility of that boundary: the quality of the tool itself has nothing to do with it.
Since it cannot be seen, there is exactly one way to manage it: write the criteria down in advance
and measure the result.

The numbers from this study are worth repeating with their units, because they are easy to mix up
with each other. Inside the circle of tasks the model pulls: participants with it did 12.2 percent
more tasks and 25.1 percent faster, at higher quality. This is a large win by the standards of
field experiments in consulting, and there is no reason to deny it.

On one task outside the circle: the share of correct decisions was 84.5 percent without the
model against 60 and 70 percent in the two conditions with it. The difference is nineteen
percentage points, and the unit has to be said out loud here: this is a difference of shares, not
a relative drop. "19 percent less often" would describe a different quantity.

What matters in this study is not the size of the failure but its invisibility. The task outside
the circle looked no different from the other eighteen: same format, same volume, same subject
area. Participants could not tell they had crossed the boundary, because the boundary does not
show up inside the task — it shows up only in the result, and only if the result is compared
against something.

From this comes the conclusion that makes the four criteria workable. Criteria of applicability
get written down before work begins, not at the moment something goes wrong — because at the
moment something goes wrong, you will not notice it. And the result is measured by two things: a
stopwatch and a share of correct decisions, not by how participants felt. The next frame will
speak separately about participants' own feelings, and it will say something unpleasant.

And one last remark on how to read this study without reading more into it than is there. Seven
hundred fifty-eight consultants are consultants, not engineers and not doctors; the tasks were
real working tasks, ranging from creative to analytical, but they are consulting tasks. The
percentages cannot be carried over to another profession. What can be carried over is the
structure of the result: a win inside the circle, a failure outside it, with the boundary
invisible from inside the task. It is exactly this structure that reproduces itself in other
subject areas, and each one has its own specific numbers, which have to be measured on their own.

Separately — on the phrase "the harm comes from the invisibility of the boundary." The quality of
the tool itself has nothing to do with it: the same model, on tasks inside the circle, gave a
large win. What is dangerous is not the model, but the lack, in the person doing the work, of any
way to tell which side of the boundary they are currently on.
