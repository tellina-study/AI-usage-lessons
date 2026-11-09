---
# Frame obtained by splitting frame s80 during the fix for the first render (2026-10-27):
# everything that stood on one frame did not fit the 5.36" body at any point size.
# Numbers, plates, columns, diagrams and map cells carried over UNCHANGED; minutes taken
# from the budget of frame s80 itself (1.2 → 0.8 + 0.4), the section's total untouched.
#
# CONSOLIDATION (#301, Section 5 overhaul): merged with the former s80b ("How this went by date") —
# that frame carried a single `timeline` form of four milestones and was split into a separate
# file by the same splitting as this one. A full re-merge of all three fragments
# (s80+s80a+s80b) into one frame was NOT done: s80 carries `vynoski` (breakdown on the image),
# and that form takes over the whole frame and allows no diagram, timeline, plates, or body prose
# alongside it (confirmed by build: `--only s79` with media+blocks+diagram gave [height]/[width],
# and the `vynoski` engine is even stricter — measurement in `deck/build_lec08_v5.py` §"vynoski
# takes over the whole frame"). The scroll image cannot be dropped, so `vynoski`
# stays on its own frame, `s80`; here is the mechanism and chronology together — that's two
# frames out of the former three, not three. Dates from s80b carried over UNCHANGED; minutes
# added (0.4+0.4=0.8). The old `s80b` was removed as a separate file.
id: s80a
local_id: "s80a"
section: "5. Recognition and Provenance"
type: analitika
title: "How an unrolled scroll is read — and on what dates"
assertion: "The input is X-ray tomography of the charred cylinder; the machine does two things: it mathematically flattens the spiraling surface into a plane and finds traces of carbon ink on it, which by density are almost indistinguishable from the charred base; the Greek text is then read by people. The task was solved by an open competition with cash prizes, not a staff laboratory: the first word from inside an unrolled scroll was read by a twenty-one-year-old participant in October 2023, coherent passages took the grand prize in February 2024, and on June 25, 2026, scroll PHerc. 1667 was read in full"
source: "Vesuvius Challenge and EduceLab, Prof. Brent Seales, University of Kentucky, in collaboration with the National Library of Naples; https://scrollprize.org/"
chapter_ref: "chapter-part3d.md § 5.7"
media: ""
media_needed: "the breakdown's illustration sits on the companion frame of the same pair (`s80`, `vynoski`): next to the diagram and timeline it would squeeze both into unreadability. The tiers of sourcing were already gone through there"
scheme:
  caption: "The machine answers one question — where is the ink here; both of its tasks have a checkable answer"
  arrows: true
  rows:
    - label: "How the scroll is read"
      steps:
        - "X-ray tomography of the scroll: layer-by-layer scanning"
        - {text: "digital unrolling: the spiral is flattened into a plane", ai: true}
        - {text: "ink search: carbon on the charred base", ai: true}
        - "a flattened image with the ink revealed"
timeline:
  unit: "milestone in decoding the scroll"
  caption: "How this went by date"
  stages: ["First word", "Coherent passages", "Works identified", "Scroll in full"]
  marks:
    - at: 0
      head: "Oct. 2023"
      text: "ΠΟΡΦΥΡΑϹ, 'purple' — $40,000 prize, participant aged 21"
    - at: 1
      head: "Feb. 2024"
      text: "coherent passages of a scroll, grand prize $700,000"
    - at: 2
      head: "2024–2025"
      text: "PHerc. 172 'On Vices'; PHerc. 139 'On Gods'"
    - at: 3
      head: "2026-06-25"
      text: "PHerc. 1667 read in full — for the first time in two millennia"
timing_min: 0.8
in_bucket: false
method_steps: ["①cost of both errors", "②no classical mode, reason named", "③what the machine did", "④how it works", "⑤what moved downstream", "chronology"]
form: []
vfy: false
status: собран
# Overhaul (#301): a diagram + timeline on one frame — two heavy forms, and the first
# measurement showed a −1.12" overflow with a full prose body on top of them;
# after dropping `itog` and the one-line body, a −0.16" overflow remained — the diagram and
# timeline already fill the body on their own, each form's own caption names the subject,
# and there is no room left for a third line in the visible layer.
# Both short phrases that stood here were carried into the notes without loss.
---

## Visible slide text

## Speaker notes

The mechanism. The input is X-ray tomography of the charred scroll: layer-by-layer scanning that yields a three-dimensional density field. The machine does two things. The first — digitally unrolling the layers: within the volume, the surface of the papyrus, winding in a spiral, is located, and it is mathematically flattened into a plane. The second — detecting ink traces with machine learning: ancient ink is carbon-based, and on charred papyrus it is almost indistinguishable by density from the base, and the recognizer is trained to see a difference that the human eye cannot distinguish on a tomogram. The output is an image of the flattened surface with the ink revealed. The Greek text is read by people.

Let's break this down into steps, because every step here is a separate engineering task with a checkable answer, and not one of them is generation. Step one: scanning. The scroll is placed under an X-ray source and many projections are taken from different angles; from them a three-dimensional density field is reconstructed — the same thing a medical CT scanner does, only at far higher resolution. Step two: digital unrolling. The surface of the papyrus winds in a spiral inside the volume; it has to be located, traced, and mathematically flattened into a plane. This is a geometry task, and it has a checkable criterion: the flattened surface must not tear and must not intersect itself. Step three — the one for which a trained model was needed. The eye cannot see the difference between ink and the base on a tomogram; the recognizer is trained to see it — not to guess at letters, but to answer the question "is there ink at this point or not." The answer is checkable: where sections could be cross-checked, the prediction matched reality. Step four: the image of the flattened surface with the ink revealed is handed to people. Philologists read the Greek text. The machine does not restore what is lost, does not guess at endings, and does not fill in damaged parts by inferring meaning.

I'll name the one specific gap in this breakdown directly: the volume and composition of the training set for the ink recognizer are not disclosed in the publications available. It is precisely the training set that determines whether the method transfers to scrolls of a different state of preservation.

It's useful to compare this task with generation, because on the surface they look alike: in both, a trained model outputs an image that is not in the source data. The difference is where the content of the output comes from. In generation, it comes from the statistics of the training corpus, and there is nothing to check it against but plausibility. Here, the content comes from measurement: the ink is physically present on the tomogram, the model only separates it from the base, and the answer has a ground truth — sections that could be independently cross-checked. From this comes a general rule for tool choice: before applying a trained model to the restoration of anything at all, ask what the result will be checked against. If there is a ground truth or an independent way to cross-check, the task is restorative, and a model is appropriate for it. If there is no ground truth and the only criterion is plausibility, the task is artistic, and the result should be called that.

What the machine did is known by date. October 2023 — the first word from inside an unrolled scroll is read: ΠΟΡΦΥΡΑϹ, "purple"; found by twenty-one-year-old Luke Farritor, prize forty thousand dollars. February 2024 — several coherent passages of one scroll are read, grand prize seven hundred thousand dollars, three people: Youssef Nader, Luke Farritor, Julian Schilliger. Next, works are identified: PHerc. 172 — Philodemus, "On Vices," Book One, the first title found; PHerc. 139 — Philodemus, "On the Gods," Book Eight. And on June 25, 2026 — for the first time in history, a scroll is read in full, from start to finish, without being unrolled. This is PHerc. 1667: about a meter and a half of papyrus, about twenty-two columns of Greek text, a philosophical treatise on ethics with Stoic themes.

A separate detail for an engineering audience: the task was solved by an open competition with cash prizes, not a staff laboratory. Most of the team that finished reading the scroll in 2026 are former competition participants. It's worth understanding why this worked here specifically, because it won't work everywhere. The task had a checkable criterion: the word read either forms Greek text that philologists recognize, or it doesn't. Where the criterion is checkable and announced in advance, an open competition gathers more attempts than any laboratory and honestly selects the best one from among them. Where there is no criterion and the result is judged by taste, the same format produces noise.

From this chronology, engineering practice should take away two things. First: milestones were announced in advance and formulated checkably — not "improve reading quality" but "read a word," "read a coherent passage," "read the scroll." Formulating a goal in checkable terms is half the success of such a format, and it is also what internal projects most often lack. Second: money here was paid for a result, not for an attempt. Forty thousand dollars for the first word and seven hundred thousand for coherent passages — sums trivial by the standards of a scientific program, and they gathered work that the program had not gathered in two hundred and fifty years.

And finally — how this recognizer differs from the ones that will appear later in the section. Here the task has ground-truth labeling: sections where it is known where the ink is, against which the method is checked. So the answer has a number, and that number is checkable by a third party. Later in the section there will be a recognizer that also has a number, but whose checkability slips away as soon as the material's origin changes — and it's useful to compare these two cases.
