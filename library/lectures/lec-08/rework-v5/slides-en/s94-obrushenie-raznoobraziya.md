---
# Source: chapter/chapter-part4b.md §§ 6.6 and 6.7.
# Departure from DECK-KARTA: the map's title promises "loss of commonality" unconditionally. The
# fact-check correction (critique/FACTCHECK-OTKRYTYE-15.md, incidental finding C and "What to cut
# from the frame" §6) removes that unconditionality, and the title is brought back to what the
# primary source actually shows. The condition matters more than the effect itself: it is the one
# thing on the frame an engineer can apply tomorrow, so it stands in the title and in the right-
# hand column, on equal footing with the effect.
#
# TWO FACT-CHECK CORRECTIONS, both mandatory:
#  (1) "+50%" is the increase PER PARTICIPANT ("50% more ads per worker"). It cannot be carried
#      over to a team's total output without recalculation.
#  (2) Noy and Zhang: the JOURNAL pair goes on the frame (453 participants, time −40%, quality
#      +18%), because the citation is to Science. The MIT working-paper numbers (444
#      participants, 27 → 17 minutes, −37%, 3.79 → 4.54) do NOT go on the frame. The 25/50/25
#      time split and the 0.49/0.25 correlations are checked against the working paper and are
#      attributed to IT, not to the journal.
id: s94
local_id: "s94"
section: "6. Wrap-up"
type: analitika
title: "The collapse of diversity: Ju and Aral, 2,234 participants — and the mode in which it doesn't happen"
assertion: "Cheaper trials can narrow the spread of results, and this is measured on a creative task; but the same study, by the same count, also showed a mode of working in which the narrowing does not happen at all; the human chooses the mode, and that gives an engineer a lever"
source: "Noy S., Zhang W., Science 381(6654):187–192, 07/14/2023, doi:10.1126/science.adh2586 (MIT working paper — 03/02/2023) · Ju H., Aral S., \"Collaborating with AI Agents,\" arXiv:2503.18238, MIT IDE"
media: ""
media_needed: "no photograph. Checked: neither study has photographs of the experimental setup under a usable license; a search of Wikimedia Commons for \"Stable Diffusion sample grid\" turned up a grid of variants for one prompt (File:Image grid to show correlations between CFG and Sampling Steps - Original.png) — it would show the sameness vividly, but its subject is different, a comparison of two settings, and a frame about that already exists in the deck. Putting it here would tell the room the wrong subject. The frame's visible content is two condition columns and a band of numeric plates"
scheme:
  kind: dorozhki
  caption: "Two studies on the same cheapening of trials: in the lab on standard texts, and in the field on a creative task"
  rows:
    - label: "Lab — 453"
      steps:
        - "time per assignment down 40%, quality up 18%"
        - "the draft stage shrank by half, editing doubled"
        - "a preregistered randomized study"
    - label: "In the field, 2,234"
      steps:
        - "11,024 ads, checked on real impressions"
        - "50% more ads per participant"
        - "text wins, image loses"
blocks:
  - {label: "Productivity in the field study", value: "50% more ads PER PARTICIPANT", note: "the unit is named: this number does not carry over to a team's total output without recalculation", key: true}
blocks_per_row: 1
timing_min: 0.7
in_bucket: true
method_steps: ["effect", "condition of the effect", "what moved"]
form: []
vfy: false
status: собран
---

## Visible slide text

**The same cheapening of trials, two modes of a human working with a model.** The lab study measured time and quality by judges' ratings; the field study measured the behavior of a real audience, with no judges at all. Both found the boundary between parts of the work equally jagged: the text part wins for teams with the model, the image part loses.

## Speaker notes

The two measurements on this frame stand side by side for a reason: the first confirms the
evening's axis in the lab, the second names its own price and the condition under which that
price does not arise.

Start with the confirmation. A preregistered randomized study: four hundred fifty-three
professionals with higher education, assignments were standard working texts in their own
fields — press releases, short reports, analytical memos. Half were randomly given access to the
model. Time per assignment fell by forty percent, quality rose by eighteen. These are the numbers
of the published paper; its own earlier manuscript had a sample nine people smaller, and the
headline numbers there are different. A good reason to remember: numbers move between preprint
and publication, and you have to cite them by whichever document you took them from.

But the weight of this study lies elsewhere: in what shifted inside the work. Before the
intervention, participants spent roughly a quarter of their time on conception, half on drafting,
and a quarter on editing. Afterward, the draft share fell by more than half, and the editing share
more than doubled. The authors put it this way in their own abstract: the tool substitutes for
worker effort rather than complementing worker skill, and restructures the task toward idea-
generation and editing, away from writing a draft. This is the evening's own axis, said in someone
else's words about someone else's material: execution shrank, selection and finishing took up the
space it left behind.

A third result from the same study is more unexpected than the rest: the existing inequality
between strong and weak participants shrank by about half. In the control group, a participant's
score on the first assignment predicted their score on the second noticeably better than in the
group with the model. In plain terms, those who wrote worse win more. For the creative industries
this explains the pattern observed across the board: the lower segment of orders — greeting
cards, social-media layouts, small-business banners — is shrinking, because the client closes the
task themselves; the upper segment holds and gets more expensive, because that is where people pay
for what the model does not pull up to standard.

Now the second half of the frame — a limitation that shows up only on creative tasks and is
absent both in customer support and in programming. The field study: two thousand two hundred
thirty-four participants produced eleven thousand twenty-four ads, and the result was checked on
real impressions, that is, by the behavior of a real audience with no judges' ratings at all.
Teams with the model produced fifty percent more ads per participant — the unit has to be held
onto here, because this number does not carry over to a team's total output without
recalculation. Quality split by part of the work: the text part is better for teams with the
model, the image part is worse. This is the same jagged boundary, seen inside one task.

The engineering formulation worth taking away. A cheap trial shifts the distribution of results
toward the center, and shifts it the more strongly, the more of the work a human hands over to
the model wholesale. If the value of the work lies in hitting the center of expectations — a
standard banner, a product card, a technical illustration — this property works in your favor. If
the value lies in deviating from the center, over-sampling through delegation destroys it, and
restoring it takes the old methods: different people, different tools, a deliberate step outside
whatever the model offers first — exactly the task-oriented mode in which the study saw no
collapse. The human chooses the mode, and that is the whole lever.

And a short formulation worth taking away from this frame whole: a cheap trial shifts the
distribution of results toward the center of expectations. The winner is whoever needs a
reliable average result. The loser is whoever's value lies in deviating from the average — and
they lose unnoticed, because every single piece of work gets better at the same time.
