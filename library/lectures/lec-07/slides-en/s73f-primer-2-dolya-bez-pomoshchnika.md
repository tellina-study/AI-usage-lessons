---
id: s73f
local_id: s5-04
section: "5. Профессиональная квалификация: поддержание и износ"
type: case
title: "Example 2: the rate fell without the assistant"   # был «Пример 1» — перенумерован под новый порядок раздела (#293, Этап B): разбор на разработчиках встал первым
assertion: "Когнитивное искажение «износ навыка», третье из шести, предъявленных на входе вечера, разобрано до дна: в четырёх центрах внедрили помощника, подсвечивающего образование на видео в реальном времени, а затем посмотрели, что стало с теми же врачами без него: 28,4 против 22,4 из ста процедур, минус 6,0 процентного пункта; помощник повышает результат, пока включён, и это состояние не бесплатно — исполнитель тот же, но стал хуже"
source: "Budzyń et al., Lancet Gastroenterology & Hepatology 2025 — https://doi.org/10.1016/S2468-1253%2825%2900133-5 · Bastani et al., PNAS 2025 — https://doi.org/10.1073/pnas.2422633122"
media: ""
media_needed: "реальный снимок подсветки образования системой обнаружения (рамка на видео)"
media_note: "снимок добыт (s92-ramka-na-obrazovanii.jpg), в слайд НЕ вкручен — замерено: полоса плашек при суженном теле роняет слайд с 13,5 до 10,8 пт, и 12 пт здесь не достигается НИ ПРИ КАКОЙ ширине слота, вплоть до предельных 2,6\". Вторая причина: ровно этот сюжет — экран процедуры с рамкой системы на образовании — стоит кадром раньше, на s73d, где он стоит слайду 1,8 пт вместо 2,7. Разбор и права — deck/images.md §3.3 и §7. Кадр сложен из двух: прежний «Пример 1, цена: исполнитель тот же, но стал хуже» (s73g) стоял отдельным кадром на шаг формы — свёртка круга диеты, решение О6"
scheme:
  caption: "Where the assistant sits, and where the physician was measured without it"
  arrows: true
  rows:
    - {label: "With the assistant", steps: ["the stream of frames", {text: "a box on the region", ai: true}, "the physician decides for himself"]}
    - {label: "What was measured", steps: ["the same physicians", "procedures WITHOUT the assistant"]}
blocks:
  - {label: "Before the assistant", value: "284 procedures with a finding per 1,000", note: "226 of 795"}
  - {label: "After three months", value: "224 per 1,000", note: "145 of 648"}
  - {label: "Resulted in", value: "minus 60 findings per 1,000", note: "19 physicians, average 28 years of experience", key: true}
pol_slov: 171   # О13 (#229): +3 слова на подпись единицы («28,4 → 22,4 ПРОЦЕДУРЫ из ста»; оговорка — находки на процедуры). О13 (#229): +16 слов на переворот единицы («без находки были 71,6 процедуры из ста, стали 77,6» — дополнение к доле обнаружения 28,4 → 22,4, глава §10.5-10.6). О13 (#229): +14 слов на описание работы («Что делали»: эндоскопист ведёт колоноскопию и ищет образования глазами на видео, помощник подсвечивает находку рамкой). Веса и кегля здесь нет нарочно: их печатает прогон на любой момент, а записанные прозой они устаревают молча — пол живёт в файле месяцами, вес меняется каждой правкой (О20, #229). Прежний пол 140 — О10 (#229): пара дало–потребовало с названной формой, сила свидетельства названа вместе с выводом, источник рукояткой
timing_min: 1.1
in_bucket: true
method_steps: ["③модель против них", "④как это устроено", "⑤что переехало", "пара дало–потребовало"]
form: ["форма 8"]
vfy: true
status: собран
---
## Visible slide text
**What was done.** At four centers in Poland, endoscopists were given an assistant that boxes a finding. Three months later, the same physicians' procedures were compared **without** it.

**This is a cognitive distortion — skill decay, the third of the six presented at the opening of the evening.** In a person it shows up like this: the same physicians, without the assistant, find less.

**Gave:** they find more while it's on. **Required:** the skill of searching on your own. **Net:** the performer is the same — the place, the volume, and the hand are unchanged — but got worse.

**The publication does not name its own system.**

## Speaker notes

Four centers in Poland: endoscopists were given an assistant that boxes a finding on video, right during the procedure. Three months later the same nineteen physicians' procedures were examined without it — findings dropped from 28.4 to 22.4 out of 100 procedures, minus six percentage points. This is what skill decay looks like, the third of the six distortions presented at the opening of the evening: the assistant lifts the result while it's on, and that state is not free — the skill of searching on your own gets drained.

The strength of the evidence and the full shape of the dispute. The study is retrospective and observational, not randomized; it does not prove causality, and the authors make no such claim. The windows are short, there is one region, one assistant system, and not a single replication. A correction, three letters to the editor, and the authors' reply have been published around this work — the dispute is open, and it cannot be hidden behind the word "measured." There are three substantive objections: secondary outcomes did not drop (mean adenomas per procedure 0.54 against 0.43, advanced ones 0.062 against 0.063, both not significant); withdrawal time was not measured in the study at all, meaning the finding lacks the behavioral link that would make it checkable; and workload over the same period nearly doubled — from 795 procedures to 1,382.


Anchoring — the first of the six — is absent here entirely: what gets looked at are procedures WITHOUT the assistant, where there is no cue and nothing to anchor on. Anchoring works while the model is there; erosion is visible once it's removed.

And it was not the procedures with the assistant that were examined, but the procedures without it: the drain on skill is visible only where the tool isn't.

Composition. Nineteen endoscopists — sixteen gastroenterologists and three surgeons, each with more than two thousand colonoscopies performed, average 28 years of experience. Two three-month windows, with the assistant deployed between them. The main comparison included 1,443 procedures without the assistant: 795 in the early window and 648 in the later one. These are not residents or novices, and that is half the strength of the observation: the drop happened among people who had held their form for two decades.

The result. The detection rate in procedures without the assistant was 28.4 percent before deployment, that is 226 findings out of 795 procedures, and 22.4 percent after, 145 findings out of 648. The absolute difference is minus 6.0 percentage points, at an interval of minus 10.5 to minus 1.6, and significance 0.0089. In a multivariable model, having worked alongside the assistant gives an odds ratio of 0.69 at an interval of 0.53 to 0.89; patient age sixty and above gives 3.60 in the same model — that is, it predicts detection noticeably more strongly. The ratio between these two figures is not stated: dividing a ratio above one by a ratio below one compares nothing. The six points lie in the same range where effects from patient mix live, and that sets the scale of the finding without canceling it out.

A caveat about the denominator, without which the number 795 reads as something it is not. In the early window, the assistant was not yet at the centers, so 795 means "procedures without the assistant" and "procedures in total" at the same time; in the later window they diverge — 648 without the assistant, 1,382 in total. The comparison of 226 of 795 against 145 of 648 is done honestly, by one column, and the rise in overall workload explains part of the drop just as well as skill decay does. This is exactly what the three letters to the editor take aim at.

The mechanics of the assistant: input is the stream of frames during the procedure, output is a box on the suspicious area in the same second. The publication does not name its own system, and manufacturers do not publish what systems of this class are trained on. The mode has names, and they are verifiable: GI Genius by Medtronic, CAD EYE by Fujifilm, ENDO-AID CADe by Olympus; the difference between them in pooled comparisons is small, and that matters more than the names.

The pair that closes the breakdown. Gave: with the assistant on, physicians find more, and the gain in detection rate in randomized trials is measured and replicated many times over. Required: the skill of searching on your own. The drain is visible within three months, even among physicians with an average of twenty-eight years of experience: this is a trained skill that is held up by volume of performance, and the drop ran exactly along centers, not individual physicians. Net: the assistant raises the result while it's on, and that state is not free. Nobody has done a count in one currency — how much the assistant on added against how much was lost while off — and it must not be presented as measured.

The eighth glossary form: the performer is the same, but got worse. The place of work, the volume, the order of steps, and the hand are unchanged; what changed is the condition of the hand itself. The neighboring forms don't check out: the fifth requires the hand to have changed, and the comparison here is built inside the same nineteen physicians; the form about operation volume misses too — procedure volume is unchanged, it's the finding rate that fell. The reverse case stands in the glossary as an empty slot: it has a name, and not a single measurement.

The same phenomenon is measured by randomization outside the clinic — among high-school students, in math: an exam with no model available turned out 17 percent worse than the control for the group with free access, while the group with teacher-set guardrails came out about at the control's level. A remedy against erosion was found there, and it consists in the design of access, not the amount of practice. This is not a replication of the clinical finding: a different study, different people, a different task.

**Sources.** [Budzyń et al., Lancet Gastroenterology & Hepatology 2025](https://doi.org/10.1016/S2468-1253%2825%2900133-5) · [a published correction to the same work, 2025;10(11):e12, and three letters with the authors' reply, 2025;10(12):1060–1062](https://doi.org/10.1016/S2468-1253%2825%2900294-8) · [Bastani et al., PNAS 2025](https://doi.org/10.1073/pnas.2422633122) · the original article: 2025;10(10):896–903
