---
id: s63
local_id: s5-07b
section: "4. Ведение медицинской документации"
type: case
title: "Example 2: the discharge summary"
assertion: "Документ модели готов раньше, короче и связнее человеческого; он менее полон и несёт больше уникальных ошибок при том же потенциале вреда одной ошибки — а по эпикризу назначают"
source: "A blinded comparison of 100 hospitalizations, JAMA Internal Medicine 2025 — https://doi.org/10.1001/jamainternmed.2025.0821"
media: ""
media_needed: "реальный снимок обезличенного выписного документа крупно; стилизованная карточка не подходит"
media_note: "иллюстрация не добыта"
scheme:
  caption: "Assembling the discharge document, two orders of work"
  arrows: true
  rows:
    - {label: "Without the model", steps: ["Chart and progress notes", "The physician assembles it himself", "Reviewing his own work", "Attending physician's signature"]}
    - {label: "With the model", steps: ["Chart and progress notes", {text: "The model assembles it", ai: true}, "Reviewing someone else's work", "Attending physician's signature"]}
blocks:
  - {label: "At least one error in the document", value: "9 of 11 machine-written summaries", note: "of 19 fabrications, 10 were major", key: true}
  - {label: "Completeness: human → model", value: "4.13 → 3.72", note: "a five-point reviewer scale"}
  - {label: "Unique errors per document", value: "1.82 → 2.91", note: "human → model"}
  - {label: "Potential harm of a single error", value: "1.34 → 1.35", note: "out of seven; not distinguishable"}
pol_slov: 137  # ПЕРЕОБЪЯВЛЕН ПО СОБРАННОМУ sec-3.pdf в круге #285 (раздел «Ведение документации»): вес 133 + запас 4. Прежнее значение ставилось до правок этого круга и к нынешнему кадру не относится. Канон: мера берётся с вывода, а не со входа (storozha-i-priyomka.md §11)
timing_min: 1.05
in_bucket: true
method_steps: ["②классические режимы", "③модель против них", "④как это устроено", "⑤что переехало", "пара дало–потребовало"]
form: ["форма 7"]
vfy: true
status: собран
---

## Visible slide text

*Text generation: the medical record goes in, a draft of the narrative section comes out.*

**How it was measured.** 100 hospitalizations, 22 reviewers: each document was read blind by two of them.

**Shorter and more coherent, but less complete.** The study names neither the model nor its training data.

**The cost of error shifted:** the same person writes it, but the reader pays.

## Speaker notes

A discharge summary written by the model: the medical record and the hospitalization's progress notes go in, a draft of the document's narrative section comes out. 100 hospitalizations, 22 reviewers, each document read blind by two of them. The tool is the same one as in the previous breakdown, but the document carries more weight: treatment elsewhere gets prescribed off the discharge summary.

I'll name the classical modes before the measured result. Of the stage's four modes, two apply to this document. The physician writes the summary himself — this mode is counted, and it is the baseline for every comparison of the work. A resident's draft signed off by the attending physician — named but not counted: the blinded comparison took the attending physician's document, not the resident's, and a number from a different study cannot be substituted in here. The other two modes of the stage do not apply here: the live scribe writes the visit note, not the discharge summary, and carrying forward a previous note does not transfer to a hospitalization's final document.

How it was measured is the main point of the breakdown, and the design of the measurement is worth stating slowly. 100 hospitalizations lasting three to six days. 22 attending-physician reviewers. Each document was examined independently by two of them, and none of the reviewers knew which text was machine-written and which human. Blinding here is not a formality: a self-report from physicians who chose the tool themselves is evidence of a quite different strength, and most of the enthusiastic publications about this stage rest on exactly that.

Now the numbers. Overall quality is comparable: 3.67 for physicians against 3.77 for the model — slightly higher for the model. The model's document is shorter and more coherent. And yet it is less complete: completeness is 4.13 for the human against 3.72 for the model. Unique errors per document: 1.82 for the human against 2.91 for the model — the model has more errors. And the potential harm of a single error is 1.34 against 1.35 on a scale from zero to seven: both ratings are low and not distinguishable from each other.

These four numbers have to be read as a whole, or you end up with one of two falsehoods. You can say "the model writes better" by leaning on overall quality. You can say "the model writes dangerously" by leaning on the error count. The true statement is the third one: the model's document is ready sooner, reads more easily, contains less of what is needed and more of what isn't, and none of its individual errors is scarier than a human one.

How it works: input is the medical record and the hospitalization's progress notes, output is a draft of the document's narrative section. The study names neither the model nor the composition of its training data, and that is a limitation of the publication.

And what moved. The steps and performers on the slide are the same: assembled, reviewed, signed. The cost of error shifted. One person writes the document, but a missed line costs another person — the one who will prescribe treatment off this document a month later, at a different institution. This is the glossary form named here explicitly, and it is the most unpleasant of all: none of the participants feels the deterioration, because the deterioration lands on someone else.

Why blinding in the measurement matters deserves its own word. Almost all the enthusiastic literature about this stage rests on self-reports from physicians who chose the tool themselves and rated the result themselves. Such a report measures satisfaction with the choice, not the quality of the document. Here the design is different: documents are de-identified, the reviewer does not know which one is machine-written, and each document is examined independently by two people. This is more expensive and slower, and that is exactly why there are so few such studies.

Separately, about what the study does not say — and this has to be stated, not skirted. The publication names neither the model nor the composition of its training data. So you cannot repeat the measurement on your own document, and you cannot carry the result over to another product of the same mode either: we saw in the previous breakdown that two products of the same mode gave different results under one trial design.

And last, what carries on down the line. The document is assembled, reviewed, and signed. The signature on it is human, but the basis of the decision came from outside — from text that the person did not write. What that signature means, and who checks that the signer is capable of pushing back against the machine, is the whole of the next section.

**Sources.** [a blinded comparison of 100 hospitalizations, JAMA Internal Medicine 2025, DOI 10.1001/jamainternmed.2025.0821](https://doi.org/10.1001/jamainternmed.2025.0821)
