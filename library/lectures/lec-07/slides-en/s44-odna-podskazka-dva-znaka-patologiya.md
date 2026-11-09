---
# СХЕМА ДОБАВЛЕНА (п. 11 наряда, §11.3: «схема обязательна у каждого кадра типа `case`»).
# Замер прожарки: схема нашлась у 5 кадров `case` из 12 в разделе, и не было её ровно у семи
# самых тяжёлых по тексту — то есть там, где она нужнее всего. §10.3: схема решения несёт
# инженерное содержание, текст — пояснение к ней, не замена; поэтому вместе со схемой из тела
# СНЯТО то, что она теперь показывает сама (п. 12 наряда, плотность: чинить схему и объём
# вместе, а не по очереди).
id: s44
local_id: s3-08
section: "3. Постановка диагноза"
type: case
title: "Example 2: pathologists read slides — with a suggestion and without"
assertion: "Здесь патолог сильнее модели, и пара поэтому выше обеих сторон — но прибавка на группе незначима, а в разрезе правоты подсказки шансы верного ответа растут вчетверо при верной и падают вчетверо при неверной, одинаково на всех уровнях опыта: отчёт о внедрении с одним числом показал бы «эффекта нет» там, где эффект велик в обе стороны"
source: "Kiani et al., npj Digital Medicine 2020 — https://doi.org/10.1038/s41746-020-0232-8"
media: ""
media_needed: "рисунок с эффектом подсказки из первоисточника — добыть (журнал открытого доступа, переиспользование законно при атрибуции — она идёт в assets/*.url, НЕ на кадр: О17). Одна на слитый кадр: s44a иллюстрации не требовал"
media_note: "иллюстрация не добыта"
blocks:
  - {label: "Share of correct findings: model alone · pathologist alone · the pair", value: "0.842 · 0.898 · 0.914", note: "intervals of 0.875–0.916 for the pathologist and 0.893–0.930 for the pair; the pair's gain over the pathologist at the group level is NOT robust — odds ratio 1.281. The model's accuracy is on its own independent test set", key: true}
  - {label: "The same pair broken out by whether the suggestion was right: correct → incorrect", value: "≈0.94 → ≈0.50", note: "converted from odds ratios of 4.289 and 0.253, both robust, from a baseline of eight correct out of ten: the study publishes odds, the shares here are illustrative", key: true}
  - {label: "In sum", value: "the average is the same, the spread grew"}
pol_slov: 205   # О20 (#229): переобъявлен по собранному PDF. Прежние 204 называли состав ДО снятия p-значений: «отношение шансов 1,281, p = 0,184» стало «на группе НЕ устойчива — отношение шансов 1,281», а «(p < 0,001)» — «устойчивых в обе стороны». Цифры ушли с экрана, слов стало на одно больше, и это весь прирост. Сами уровни значимости с интервалами внесены в заметки, где их прочтёт лектор: прежде в них не было ни одного.
# ПЕРВЫЙ БЛОК ПЕРЕВЕДЁН В ЦИФРЫ, как владелец и просил: он назвал пять величин — базовая точность, с верной подсказкой, с неверной, точность модели, точность пары, — и все пять в работе есть. Стоят они на двух плашках, и разведены по тому, что ИЗМЕРЕНО и что ПЕРЕСЧИТАНО: «0,842 · 0,898 · 0,914» напечатаны работой с интервалами, а «≈0,94 → ≈0,50» — пересчёт из отношений шансов 4,289 и 0,253 от базы восемь верных из десяти, и работа печатает шансы, а не эти доли. Поставить все пять в один ряд значило бы выдать пересчёт за замер.
# ЧТО СНЯТО по п. 38: «Устроено. Вход — оцифрованный срез, выход — один из двух диагнозов; точность модели на независимом наборе 0,842» — блок владелец велел убрать, и число 0,842 переехало на плашку точностей, где оно и сравнивается; «Шансы верного ответа: модель права → неправа — вчетверо вверх → вчетверо вниз» говорило то же, что «≈0,94 → ≈0,50» рядом, только в шансах — осталась одна плашка, шансы ушли в её подпись; «Дало → потребовало: прибавку при верной → равную потерю при неверной» — тот же факт третьим разом; «Что переехало» переименовано в «Стоимость» (п. 38).
# ЧЕМ ЗАНЯТЫ СЛОВА: цена ошибки сжата в экспозицию одной строкой, как велел владелец. И встала связь с разбором-сводом, которой кадр не имел: «здесь патолог сильнее модели — и пара выше обеих сторон, это ровно то подмножество свода, где так и бывает» (18 слов). Без неё кадр читается исключением из правила раздела, а он — его вторая половина: свод даёт +0,46 там, где сильнее человек, и этот опыт стоит именно в том подмножестве. Прежде раздел предъявлял только половину «модель сильнее», и правило выглядело приговором паре.
# ЦЕНА (замер по собранному PDF): четыре плашки → три, тело 15,0 пт — выше пола на три пункта, блокирующих нет. Слов 145 → 204: вес куплен пятью числами, которые владелец перечислил поимённо, и связью с подмножеством свода.
scheme:
  caption: "Half the cases with a suggestion, half without; the sign-off is the pathologist's either way"
  arrows: true
  rows:
    - {label: "Without the model", steps: ["slide on screen", "pathologist decides", "sign-off"]}
    - {label: "With the model", steps: ["slide on screen", {text: "the model's suggestion", ai: true}, "pathologist decides", "sign-off"]}
timing_min: 1.1
in_bucket: true
method_steps: ["①цена ошибки", "②классические режимы", "③модель против них", "④как это устроено", "⑤что переехало", "пара дало–потребовало"]
form: ["сетка", "форма 7", "[VFY]"]
vfy: true
status: собран
---

## Visible slide text
**11 pathologists of varying experience** distinguished two types of liver cancer across 80 digitized slides. **The cost of error cuts both ways:** mistaking one tumor type for the other means different treatment; re-checking means a specialist's time.

**Here the pathologist is stronger than the model, and the pair beats both sides.** At the same time, the model's error becomes the physician's error: the sign-off is theirs.

**"No effect" in a one-number report:** the group-level gain isn't significant, even though the effect runs fourfold in both directions.

## Speaker notes

Pathologists read specimens with a single suggestion from the model, and in half the cases the suggestion was wrong. What's measured here is the same thing as in the eye-tracking studies, but at the level of the decision rather than eye movement: the same tool shifts the result fourfold in both directions — up with a correct suggestion and down with an incorrect one.

Significance levels for these figures. For the group as a whole, the pair's gain over the pathologist didn't reach significance: odds ratio 1.281 at p equal to 0.184 — that's exactly what produces "no effect" in a one-number report. But both fourfold shifts are robustly significant: odds ratio 4.289 with a correct suggestion (interval from 2.360 to 7.794), and 0.253 with an incorrect one, p less than one thousandth in both directions. The pair reads together: no effect at the group level, and fourfold in each direction individually.

The design of the study, which determines how the rung is marked. Eleven pathologists of varying experience — three gastrointestinal subspecialists, three specialists in other fields, three residents, and two whose specialty wasn't specified — distinguish two types of liver tumor from digitized slides. The set is eighty slides; the model's own accuracy on an independent test set is zero point eight hundred forty-two. The same pathologist read the same set twice, in separate sessions: half the cases with a suggestion, half without, with the assignment flipped in the second session and a washout period of at least two weeks. The comparison runs between sessions: a first and second look at the same case are never compared against each other here.

The baseline is reading a slide without a suggestion. When the suggestion is correct, the odds of a correct answer rise roughly fourfold; when it's wrong, they fall by roughly the same factor. This held at every level of experience and across cases of every difficulty alike: a subspecialist's own field gave them no protection, and that matters more than the size of the effect itself.

How to read "fourfold" without getting the direction wrong. Odds are the ratio of the probability of a correct answer to the probability of an incorrect one. If, without a suggestion, the pathologist answered correctly in eight cases out of ten, odds grown fourfold come out to about ninety-four out of a hundred, while odds fallen fourfold bring it down to about fifty. Symmetry in the odds produces asymmetry in the shares, because high accuracy has a long way to fall and almost nowhere to rise.

The second classical mode — a subspecialist second opinion — is named and not counted: it wasn't measured on this set, and plugging in a number from a different study would be exactly the kind of pooling of mismatched samples this course warns against.

The average gain and the sign-flip are one observation read two ways, and they come from the same sample. At the group level, without splitting cases into those where the model is right and those where it's wrong, the gain doesn't reach significance. That's the price of this case study, and it's organizational in nature, with nothing clinical about it: a deployment report carrying a single number would show no effect exactly where the effect was fourfold in both directions. There's exactly one decision such a report leads to — "works about the same as before, keep it" — and it gets made blind.

What shifted. One form: the cost of error moved. The steps, the amount of work, and the performer stayed the same — the pathologist looks at the same slide for the same amount of time. What changed is the consequence: the model's error became the physician's error, because the sign-off on the report is theirs. The shift is measured in both directions, and that's rare: usually only the loss or only the gain gets measured.

The pair that closes out this case study reads straight off the plates. Gave — a gain with a correct suggestion. Cost — an equal loss with an incorrect one. In sum — the average is the same, the spread grew. For the procedure, that's the worst possible outcome: the average gives no reason to step in, while the spread means some patients got a worse decision than they would have before.

Alongside this, in a different genre and weaker in strength of evidence, sits a review of clinical decision-support systems: a wrong suggestion raises the risk of a wrong decision by twenty-six percent, drawn from a review covering seventy-four studies out of thirteen thousand eight hundred twenty-one screened. A caveat on the review is mandatory: that body of work includes many rule-based systems, with trained models making up only part of it. So this figure stands as a mention; it doesn't work as an argument here.

**Sources.** The study doesn't publish its training set either. [Kiani A. et al., Impact of a deep learning assistant on the histopathologic classification of liver cancer, npj Digital Medicine 2020, PMC7044422](https://doi.org/10.1038/s41746-020-0232-8). Study design: eleven pathologists of varying experience — three gastrointestinal subspecialists, three specialists in other fields, three residents, and two with unspecified specialty; eighty slides, two readings, suggestion assignment flipped in the second session, a washout period of at least two weeks. A mention removed from the slide as the weakest in strength of evidence: [Goddard K., Roudsari A., Wyatt J., Automation bias: a systematic review of frequency, effect mediators, and mitigators, JAMIA 2012;19(1):121–127](https://doi.org/10.1136/amiajnl-2011-000089).
