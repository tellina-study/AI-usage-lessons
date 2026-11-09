---
# Frame obtained by splitting frame s94 while fixing the first render (10/27/2026):
# everything that stood on one frame did not fit into a 5.36" body at any point size.
# Numbers, plates, columns, schemes, and map cells were carried over UNCHANGED; the minutes are
# taken from frame s94's own budget (1.3 → 0.7 + 0.6), the section total is untouched.

id: s94a
local_id: "s94a"
section: "6. Wrap-up"
type: analitika
title: "Two modes of a human working with a model, and the spread collapses in only one of them"
assertion: "The collapse of diversity happens where the human delegates the work to the model wholesale and talks to it as to a conversational partner; under task-oriented interaction — set the task, review the result, set the next one — no collapse is observed in the study at all, and both productivity and quality are higher across every measure at once"
source: "Noy S., Zhang W., Science 381(6654):187–192, 07/14/2023, doi:10.1126/science.adh2586 (MIT working paper — 03/02/2023) · Ju H., Aral S., \"Collaborating with AI Agents,\" arXiv:2503.18238, MIT IDE"
media: ""
media_needed: ""
scheme:
  kind: dorozhki
  caption: "The same cheapening of trials, two modes of a human working with a model"
  rows:
    - label: "The spread collapses"
      steps:
        - "the human delegates the work wholesale and talks to the model as to a conversational partner"
        - "the outputs come out noticeably more alike"
        - "if the value lies in deviating from the center of expectations, this mode destroys it"
    - label: "It doesn't collapse"
      steps:
        - "the human sets the task, reviews the result, sets the next one"
        - "no collapse of diversity is observed in the study at all"
        - "both productivity and quality are higher, across every measure at once"
timing_min: 0.6
in_bucket: true
method_steps: ["effect", "condition of the effect", "what moved"]
form: []
vfy: false
status: собран
---

## Visible slide text

**The human chooses the mode. That is the only lever on this frame.** The first mode is called delegation, the second task-oriented interaction. What distinguishes them is who holds the decision; the tool in both cases is the same one.

**The authors' own measure of diversity:** seventy thousand variants from one model are less diverse than seventy variants from seventy different people.

## Speaker notes

And the observation itself: the outputs came out noticeably more alike. The mechanism is clear
from how it is built — the model is trained on what came up more often, and under equal
conditions it produces what came up more often. Seventy thousand variants obtained one way from
one model are less diverse than seventy variants obtained from seventy different people.
Oversampling widened the number of trials and narrowed their spread.

But here begins the reason the frame belongs in Wrap-up, and the condition matters more than the
effect itself. The authors observed the narrowing in teams where the human handed the work to the
model wholesale and communicated with it in an interpersonal style, as with a conversational
partner. Under task-oriented interaction — the human sets the task, reviews the result, sets the
next one — the same study, by the same count, recorded higher productivity, higher quality across
every measure at once, and no collapse of diversity. Both halves are measured on the same
material.

Let's lay the two modes out by name, because what distinguishes them is not the tool and not the
task, but how the human behaves inside that pairing.

Mode one — delegation. The human hands the work to the model wholesale and talks to it as to a
conversational partner: formulates, receives, accepts. This is where the narrowing of the spread
sets in: the outputs come out noticeably more alike, because they all arrive from one
distribution, shifted toward the middle of what is expected. Seventy thousand variants generated
by one model are less diverse than seventy variants from seventy different people — and this is a
measured property. Wherever the value of the work lies precisely in deviating from the center of
expectations, this mode destroys it.

Mode two — task-oriented. The human sets the task, reviews the result, sets the next one. The
decision about what counts as good stays with the human, and the distribution is shaped by their
own selection, not by the model's distribution. In this mode no collapse of diversity is observed
in the study at all — and both productivity and quality are higher, across every measure at once.

This is the frame's practical conclusion, and it is rare in its form: the effect has a switch, and
the switch is in the human's hands. Not the model provider's, not a regulator's, not the next
version's — the person sitting in front of the screen, deciding whether to hand the work over
wholesale or carry it forward step by step. The condition here matters more than the effect
itself: the narrowing of the spread is not a property of the technology, but a property of one of
the two ways of using it.

For practice, this gives a checkable requirement on the process, not on the tool. If you are
introducing a trained model where dissimilarity of outputs is valued — in design-option
exploration, in ad copy, in the search for engineering solutions — write into the process that the
human sets the task and reviews the result, rather than accepting what comes out wholesale. This
is not a matter of taste and not discipline for discipline's sake: the difference between the two
modes is measured on over two thousand participants and eleven thousand ads, and verified by the
behavior of a real audience, not by judges' ratings.

And here is what sets this study apart from most: quality here was measured not by judges'
ratings but by the behavior of a real audience on real impressions — eleven thousand twenty-four
ads, two thousand two hundred thirty-four participants. A judge's rating measures what the judge
likes; an impression measures what worked. For the conclusion about diversity this matters a
great deal: a judge is precisely inclined to rate work shifted toward the center of expectations
more highly.
