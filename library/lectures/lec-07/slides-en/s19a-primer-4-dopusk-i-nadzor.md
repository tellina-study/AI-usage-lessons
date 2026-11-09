---
# ВТОРАЯ ПОЛОВИНА ЧЕТВЁРТОГО РАЗБОРА (см. головной кадр `s19`). Здесь стоит то, ради чего разбор
# заведён: контур допуска и пересмотра модели — пятый вопрос инженерной глубины (§2 канона
# `obzor-stran-i-glubina-razbora.md`), который в разделе не закрыт больше нигде.
# НЮАНС НАДЁЖНОСТИ СТОИТ НА КАДРЕ, А НЕ В ЗАМЕТКАХ (§2.3 того же канона, требование дословное:
# «нюанс — видимая строка на кадре, не абзац, который требует открыть главу»). Их здесь два, и
# оба названы в видимом теле: точность считана на ста исследованиях калибровочного набора, а не
# на 593 261, и эталоном служило заключение того самого врача, которого модель замещает.
# МЕХАНИЗМ НАЗВАН ТЕРМИНОМ ВВЕДЕНИЯ (§2.4 того же канона, введено владельцем 20.10.2026):
# 1 745 несогласий из 8 406 ответов — это «Несогласие», пятый из шести механизмов кадра `s01ae`.
# Свободного пересказа «ИИ меняет доверие врача» здесь нет намеренно: словарь курса уже введён
# во Введении, и разбор обязан им пользоваться, а не изобретать термин заново.
id: s19a
local_id: s1-10a
section: "1. Первичный скрининг и отбор на обследование"
type: case
title: "Example 4, authorization: two years and nine months to insurance payment"
assertion: "Контур допуска и пересмотра московской модели: пять калибровок, четыре версии, две первые придирки вообще не про точность (нет пометки «только для исследований», подсветка нарисована цветом и на монохромном маммографическом мониторе не различается); после переделки архитектуры площадь под кривой поднялась с 0,73 до порога 0,81 и далее до 0,94, технические отказы упали с 9 до 1 из ста, но большая их часть оказалась не моделью, а настройкой аппарата, параметрами техника и сбоями архива; порог допуска 0,81 назначен как нижняя граница доверительного интервала самого радиолога; эталон измерения — заключение врача, выше которого модель измерена быть не может, а точность считана на 100 исследованиях калибровочного набора, не на 593 261"
source: "Vasilyev, Rumyantsev, Vladzimirsky et al., Diagnostics 2025 — https://doi.org/10.3390/diagnostics15070822"
media: ""
media_needed: "иллюстрация не нужна — кадр держат полоса плашек и схема круга пересмотра"
media_note: "второй кадр разбора; снимок на дивайдере раздела"
blocks:
  - {label: "Technical failures", value: "9 → 1 out of 100", note: "most are not the model: device setup, technician parameters, archive failures"}
  - {label: "What accuracy was measured against", value: "100 studies, not 593,261", note: "the benchmark is the finding of the very physician the model replaces: it cannot be measured above him", key: true}
  - {label: "The physician disagreed with the model", value: "1,745 times out of 8,406", note: "33 radiologists; this is \"Disagreement\" — the fifth mechanism from the opening slide"}
scheme:
  caption: "The review cycle: a report goes to the developer every month"
  arrows: true
  rows:
    - {label: "Check", steps: ["output requirements", "calibration on 100", "stream and failures", "review by an expert physician"]}
    - {label: "Response", steps: ["report to the developer", {text: "new model version", ai: true}, "re-calibration", "insurance payment"]}
pol_slov: 151   # ПО ЗАМЕРУ СБОРКИ (`build_lec07.py --only s19,s19a,s49g,s49h`), не по оценке. Предел кадра 140, и он здесь перебран — как перебран у КАЖДОГО разбора этой деки: рядом стоят 256 (`s41`), 252 (`s16`), 244 (`s15`), 214 (`s49b`), 206 (`s49f`), 190 (`s49e`). Новые кадры легче любого из них, и легче медианы семьи. Обязательный состав §5.13 (цена ошибки · оба классических режима · модель рядом · устройство · что переехало) плюс схема потока и нюанс надёжности на кадре (§2.3) в 140 слов не укладывается: пробовано, замерено. Физические пределы — `[высота]`, `[кегль]`, `[пол]` — все чистые, то есть текст в рамке держится и кегль не ужат.
timing_min: 1.0
in_bucket: true
method_steps: ["④как устроено", "⑤что переехало"]
vfy: true
status: собран
---

## Visible slide text

**The first two objections were not about accuracy:** the finding was highlighted in color, and mammography monitors are monochrome.

**Area under the curve: 0.73 → 0.81 → 0.94.** *Scale: 0.5 is a coin flip, 1.0 is no misses. The 0.81 threshold is the lower bound of the radiologist's own confidence interval.*

## Speaker notes

What was done with the Moscow mammography model after registration and before the city began paying for its work out of insurance funds. The whole cycle took two years and nine months: five calibrations and four versions of the product.

The first check is functional, and it stops the model on two points, neither of which is about accuracy. First: the output document and the additional set of images lacked the "for research use only" label. Second, and worth remembering: the model highlighted the finding in color — and mammography monitors are monochrome, so the colored highlight cannot be distinguished on them. The model could have been arbitrarily accurate; its answer was physically unreadable on the equipment actually sitting in the room. This is exactly the engineering work no metric can substitute for: until someone sits down at a real monitor, you cannot see it.

The second check is the calibration check, on a hundred studies with confirmed annotation, and here the model failed on area under the curve: as a reminder of the scale, 0.5 is a coin flip, 1.0 is no misses. The threshold was set at 0.81, and it was not pulled out of thin air: it is the lower bound of the confidence interval that the radiologist himself gives on the same task. In other words, the requirement is framed as: be no worse than the least plausible human. The model scored 0.73 and was sent back.

What the developer rewrote over the following month is a list worth stating out loud, because it answers the question "what actually happens when a model fails". They expanded the training set. They reworked image preprocessing. They added a separate channel with brightness-window selection and histogram equalization. They added a head that scores the quality of the input image. They swapped the network backbone from ResNet-50 to ResNeSt. They replaced a coarse resizing of the region with a precise one. They changed the activation function. After that the area under the curve became 0.81 — exactly the threshold, not above it — and the model was let into the stream. Two more reviews followed: at month nine they added a fibrocystic-change class and annotation on the international breast-imaging reporting scale, added at the radiologists' direct request; at month fifteen, two more finding classes, an image-quality score, and a quadrant split, and the network was moved to a different architecture. By the fourth version, the area under the curve reached 0.94, and before authorization for payment there was a fifth calibration, where the figure came in slightly below the peak. Revisions do not only go up.

Technical failures are a separate story, and probably the most useful one for an engineer. They fell from nine percent to one, and that is a genuine improvement in robustness. But look at the composition: most of the failures are images the system did not process in full — cases where the model handled one, two, or three frames out of four — and the causes are named directly: incorrect mammograph setup, study parameters set by the technician, and failures in the city archive itself. In other words, a substantial share of what the report counts as a model defect is not a model defect at all. Without this breakdown, the figure "failures dropped ninefold" would read as credit to the network.

And two nuances that change the reliability of everything I have named; both are stated on the slide. First: accuracy was measured on the hundred studies of the calibration set — not on the five hundred ninety-three thousand. A stream of that size measured failures, physician agreement, and expert review, not accuracy; the authors name this as a limitation themselves. Second: in the prospective part, the benchmark was the physician's own finding — the very physician the model replaces. Measured this way, the model cannot turn out better than the human even in theory, and a shared miss by both is never visible at all. I'll add a third, smaller one: the clinical review was run by one expert physician at a time, and at month fifteen that physician changed — meaning the measuring instrument itself changed partway through the measurement, and the authors note this themselves.

What moved. The decision "is the model's output acceptable" moved from the developer to a city-level tester: output requirements are published, calibration is mandatory, and a report goes to the developer every month. And the physician gained a step that did not exist before: over the observation period, thirty-three radiologists pressed "disagree" one thousand seven hundred forty-five times out of eight thousand four hundred six responses — roughly every fifth time. This is "Disagreement", the fifth of the six mechanisms we named at the opening: a discrepancy with the model is worked through as a separate step, and that step is paid for in working time. In January of year twenty-three, the city introduced a separate paid service — mammography description and interpretation using the model. Two years and nine months from the start of testing to the tariff.

**Sources.** [Vasilyev, Rumyantsev, Vladzimirsky et al., Diagnostics 2025](https://doi.org/10.3390/diagnostics15070822)
