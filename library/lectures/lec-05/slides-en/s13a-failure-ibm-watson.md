---
id: s13a
type: case_study
section: "Section 1. Discovery"
duration_min: 2.5
assertion: "IBM Watson for Oncology: $62 million spent — without a single treated patient; trained on hypothetical cases from a handful of doctors"
learning_goal: "On-point failure #3: IBM Watson for Oncology (LO2/LO6) — high-stakes discovery on unverified data"
learning_outcomes: [LO2, LO6]
chapter_ref: "§1.9 [for-slide-s13a]"
in_bucket: true
interaction: none
verify_day_of: false
note: "cascade-safe suffix ID (s13a) — Discovery's 3rd failure, added per course-curator LO3 sign-off; does not shift the s14+ numbering"
meme_or_visual: >
  case_study: a "scales" icon — on one pan $62 million (a stack of coins), on the other — zero
  (an empty pan, a patient symbol crossed out). Contrast "synthetic cases from a handful of
  doctors" (a small group of icons) vs "real outcomes of thousands of patients" (a large crowd of
  icons, crossed out — not used).
source: "STAT News leak (25 July 2018); MD Anderson partnership termination (Sept 2016)"
---

# Visible content

## Title bar
$62 million — and not a single treated patient

## Body
[Scales: $62M in coins on the left vs an empty pan on the right]

**IBM Watson for Oncology, since 2012**
- MD Anderson partnership terminated (2016): $62M, 0 patients
- Internal documents: recommendations called "unsafe and incorrect"
- Trained on hypothetical cases from a handful of MSK oncologists, not real outcomes

[Gold callout]
Criterion: a high-stakes domain + only synthetic/hypothetical data behind the recommendation = the product isn't ready, however impressive the demo

## Speaker notes

IBM Watson for Oncology was developed starting in 2012 in partnership with Memorial Sloan Kettering Cancer Center. The MD Anderson Cancer Center partnership was terminated in 2016 after sixty-two million dollars in spending — without a single treated patient. Internal IBM documents, leaked to the press in 2018, showed the system produced unsafe and incorrect recommendations — for example, prescribing a drug to a hypothetical patient with active bleeding even though the drug carries an explicit warning against such use. In 2022, IBM sold the division for roughly a billion dollars.

The mechanism, tied specifically to the Discovery phase: the failure sits exactly at the data-source-selection step — the very core of discovery as evidence-gathering. The system was trained not on real patient data or validated clinical guidelines, but on a small number of synthetic, hypothetical cases labeled by a handful of oncologists. The product inherited the personal preferences of a few doctors instead of a representative clinical base. This is the same class as the synthetic-users failure before it: a synthetic source, unanchored to real outcomes, was accepted as a sufficient basis — but here the stakes aren't a failed feature, they're patient safety.

The lesson: the discovery phase of an AI product in a high-stakes domain must verify the representativeness of its training data before demonstrating capabilities to customers; a marketing demo is not validation. The criterion: if the entire available dataset is small-N synthetic cases from a narrow group of experts, not real outcomes across large samples, that's a signal it's too early for the product — a separate phase of data collection and validation is needed. The alternative: evidence-based systems built on structured clinical guidelines with transparent source traceability, or a supervised pilot with a human in the loop. The section's three failures are one class: a synthetic source accepted as a validated basis for a decision — only the cost of the mistake changes.
