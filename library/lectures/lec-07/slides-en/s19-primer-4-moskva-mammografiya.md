---
# НОВЫЙ РАЗБОР, ЗАВЕДЁН ПО §1.7 КАНОНА `obzor-stran-i-glubina-razbora.md` (порог ≥1 российский
# разбор на раздел с кейсами; владелец снизил порог с ≥2 до ≥1 20.10.2026). До этой правки
# раздел 1 нёс три разбора — шведская программа, чат-бот первой линии, глазное дно, — и ни
# одного российского, при том что лучевой скрининг в РФ развёрнут массово.
# ПОЧЕМУ ЧЕТВЁРТЫЙ РАЗБОР, А НЕ ЗАМЕНА ОДНОГО ИЗ ТРЁХ (правило 3+6, `stroenie-i-povestvovanie.md`
# §3 шаг 3). Критерий отбора того же шага — «разбор делает работу, которой не делает другой в
# этом же разделе». Пятый вопрос инженерной глубины (§2 канона: на чём обучали, как обновляют,
# что известно о дрейфе) в разделе закрыт ровно нигде: `s15a` говорит прямо «обучение, обновление
# и дрейф источники не раскрывают», `s18b` закрывает его частично. Этот разбор — единственный в
# деке, где виден весь контур допуска и пересмотра модели: пять калибровок, четыре версии,
# монопольный эталон и названная цена каждого круга. Ни один из трёх прежних разборов этой
# работы не делает, и свернуть его в упоминание нельзя — упоминание несёт число, а здесь
# предмет не число, а устройство.
# ПЕРЕСЕЧЕНИЕ С ПРИМЕРОМ 1 ПРОВЕРЕНО И РАЗВЕДЕНО. Оба про маммографический скрининг, и этого
# мало, чтобы считать их одним примером: в шведском порядке модель ОТБИРАЕТ, кого прочтут
# дважды, а заключение по каждому снимку всё равно выдаёт человек; здесь модель САМА читает
# первой и занимает слот второго человеческого читателя. Разные механики на одной стадии.
id: s19
local_id: s1-10
section: "1. Первичный скрининг и отбор на обследование"
type: case
title: "Example 4: Moscow, Russia — a model standing in for the second mammogram reader"
assertion: "Московский маммографический скрининг: модель читает снимок первой, врач вторым — то есть занимает слот, на котором в шведском порядке стоит второй человек; проверено на 593 261 исследовании из 112 организаций и на оборудовании десяти производителей; устройство раскрыто полностью (Faster R-CNN с остовом ResNet-50, обучение на 3 641 снимке, выход — число от 0 до 1 на каждую грудь), чего не раскрыл ни один другой разбор раздела; при этом ни выявляемости, ни доли вызовов, ни интервальных раков авторы не собирали вовсе и говорят об этом сами, поэтому выигрыша по исходам у этого случая нет и приписывать его модели нельзя"
source: "Vasilyev, Rumyantsev, Vladzimirsky et al., Diagnostics 2025 — https://doi.org/10.3390/diagnostics15070822"
media: ""
media_needed: "иллюстрация не нужна — кадр держат схема двух порядков чтения и полоса плашек"
media_note: "снимок маммографического кабинета уже стоит на дивайдере раздела (`s11`); второй такой же на разборе был бы повтором"
blocks:
  - {label: "Scale of the check", value: "593,261 studies", note: "112 Moscow organizations, 10 equipment manufacturers, 2021–2022"}
  - {label: "Sensitivity: entry → exit", value: "0.62 → 0.85", note: "that is 38 cancer signs out of 100 not found"}
  - {label: "Registration came before the check", value: "2021 — Roszdravnadzor certificate and CE mark", note: "for the version with 0.62 sensitivity", key: true}
scheme:
  caption: "The model took the second reader's slot, not a spot next to the first"
  arrows: true
  rows:
    - {label: "Double reading", steps: ["image", "first physician", "second physician", "a third on disagreement"]}
    - {label: "Moscow, with the model", steps: ["image", {text: "the model reads first", ai: true}, "the physician reads second", "the physician's finding"]}
pol_slov: 157   # ПО ЗАМЕРУ СБОРКИ (`build_lec07.py --only s19,s19a,s49g,s49h`), не по оценке. Предел кадра 140, и он здесь перебран — как перебран у КАЖДОГО разбора этой деки: рядом стоят 256 (`s41`), 252 (`s16`), 244 (`s15`), 214 (`s49b`), 206 (`s49f`), 190 (`s49e`). Новые кадры легче любого из них, и легче медианы семьи. Обязательный состав §5.13 (цена ошибки · оба классических режима · модель рядом · устройство · что переехало) плюс схема потока и нюанс надёжности на кадре (§2.3) в 140 слов не укладывается: пробовано, замерено. Физические пределы — `[высота]`, `[кегль]`, `[пол]` — все чистые, то есть текст в рамке держится и кегль не ужат.
timing_min: 1.0
in_bucket: true
method_steps: ["①цена ошибки", "②классические режимы", "③модель рядом", "④как устроено"]
vfy: true
status: собран
---

## Visible slide text

**What this case is.** Moscow, mammography screening. The model reads the image first, the physician second. *The product is "Celsus Mammography."*

**How it's built:** input — a mammogram in four views, output — a number from 0 to 1 for each breast. Faster R-CNN with a ResNet-50 backbone, trained on 3,641 images. *Image recognition.*

**There is no outcome benefit:** detection rate, recall rate, and interval cancers were not collected at all — the authors say so themselves.

## Speaker notes

Moscow mammography screening: the model reads the image first, the physician second — that is, it occupies the slot where the Swedish program puts a second human. The product is called "Celsus Mammography", tested on 593,261 studies from 112 city organizations, on equipment from ten manufacturers, in 2021–2022.

This is the only breakdown where you can see how a model is authorized for a mass-scale stream and what happens to it after authorization: none of the other breakdowns have this part, and the sources on the Swedish program say nothing at all about training and drift.

I'll start with what this case is. Moscow, mammography screening, part of the city's experiment in computer vision for radiology, running since 2020. Over the course of that experiment, fifty-two different models have processed almost fourteen million studies — that is the frame our case sits in, and the case itself is a single one: the "Celsus Mammography" model on the city's mammography stream.

Now the most important thing about the mechanics, and this is exactly where this case diverges from the Swedish one. In the Swedish program, the model selects — it gives the image a risk score and uses it to decide whether to run a second human reading; the finding for each image still comes from a human either way. Here it is built differently: the model reads the image first, the physician reads second, and the intent of the city's experiment is stated directly — to replace the second radiologist with a registered medical device. It is one slot, and two different ways of filling it. One stage, different mechanics, which is why this is two breakdowns rather than one.

On how it is built — something the room has not gotten on a single slide of this section so far. Input — a standard mammogram in four images: two views per breast. Output — not a category, not a word, but a number from zero to one for each breast: the probability of cancer signs. Inside — a Faster R-CNN detection network with a ResNet-50 backbone; trained on three thousand six hundred forty-one images. Pause on this pair of numbers: the training set is three and a half thousand images, the validation stream is five hundred ninety-three thousand two hundred sixty-one studies. A ratio of almost one to one hundred sixty. This is not a knock against the developer, it is a property of the task: annotating an image with a histology-confirmed outcome is expensive, and you cannot annotate as many as pass through the city in a year.

I will state the cost of both errors in the same units the Swedish program already used, because different units cannot be added here. Missing a cancer is an interval cancer: it shows up on its own, later, at a larger stage, and for the Swedes that is 1.76 cases per thousand screened. Raising a false alarm is recalling a woman for a second image, 2 out of 100 for the Swedes. Now the cost that this case specifically measures, and it is of a different kind: at entry into the check, the model had a sensitivity of 0.62. To translate: out of a hundred cancer signs in the set where they were being looked for, the model did not find thirty-eight. And with that sensitivity it already held a Roszdravnadzor registration certificate and a European CE mark — both obtained in year twenty-one, before the city check even began. This is the main lesson of the slide: registering a product and the product actually working are two different facts, and the first does not imply the second.

The two classical regimes to compare against are already counted: double reading by two physicians with a third for disagreements — the very regime the model is replacing here — and single reading by one physician, which is more widespread and does not work with a zero. And now something I have to state honestly, and which many retellings of this work do not: there is no outcomes comparison of "model instead of the second physician" against "two physicians" in it. The authors did not collect detection rate, recall rate, or interval cancers at all — and they call this their own limitation, in the text, in their own words. So this case has no measured outcome benefit, and we will not credit it to the model. What is measured in it comes on the next slide; a great deal is measured there, but it is something else.

**Sources.** [Vasilyev, Rumyantsev, Vladzimirsky et al., Diagnostics 2025](https://doi.org/10.3390/diagnostics15070822)
