---
# НОВЫЙ КАДР (круг 6, 2026-10-19), заказ владельца дословно: «в исследованиях
# почему нет российских примеров? у нас же куча рентгенологии, флюорографии и
# других примеров. найди и дай что-то прям массовое, еще технически интересное
# и с доказанным эффектом… и не меньше 2х российских».
# Это первый из двух. Массовый — 575 549 исследований. Технически интересный —
# порог срабатывания выставлен на чувствительность 1,0 СОЗНАТЕЛЬНО, специфичность
# объявлена незначимой, и больше половины потока после этого не читает человек.
# С измеренным эффектом — доля пропусков и деньги посчитаны, не заявлены.
# Глава несёт разбор целиком: `chapter-part1c.md` §2.5б (написан тем же кругом,
# book-first: кадр выведен из главы, а не глава дописана под кадр).
id: s27a
local_id: s2-05a
section: "2. Инструментальная и лабораторная диагностика"
type: case
title: "Example 1: Moscow — preventive images that no human reads"
assertion: "Чувствительность выставили на единицу, специфичность объявили незначимой — и больше половины профилактического потока перестал читать человек; за пять месяцев это 290 клинически значимых пропусков на 575 549 снимков и минус 43,7 процента расходов по тарифам"
source: "Vasilyev et al., Digital Diagnostics 2025;6(1):5–22 — https://doi.org/10.17816/DD641703"
media: ""
media_needed: "Поиск: настоящая фотография флюорографического кабинета городской поликлиники — человек стоит у флюорографа, рентгенолаборант за пультом. Нужен подлинный снимок (пресс-фото департамента здравоохранения, фотобанк с указанием места съёмки), не постановка с актёрами и не рендер."
media_note: "иллюстрации пока нет; бюджет высоты кадра занят схемой `без модели / с моделью` и тремя плашками. Пустое поле здесь честнее слабой картинки (§ «Форма подачи слайда»: картинку лучше не ставить вовсе, чем ставить слабую)"
blocks:
  - {label: "The cost of both errors", value: "the disease is found a year later · an unnecessary follow-up exam", note: "the asymmetry is extreme — the trigger threshold was derived from it"}
  - {label: "Clinically significant misses", value: "5 per 10,000 images", note: "290 of 575,549 is 0.05 percent; a human on the same kind of image gets 3–4 percent, but on a different stream", key: true}
scheme:
  arrows: true
  rows:
    - {label: "Without the model", steps: ["image", "the radiologist reads every one", "finding goes into the chart"]}
    - {label: "With the model", steps: ["image", {text: "triage: normal or not", ai: true}, "normal → into the chart without a physician · not normal → the radiologist"]}
pol_slov: 179   # замер по собранному sec-2.pdf, круг 6: разбор по форме §5.13: три плашки со знаменателями, схема «без модели / с моделью», порог срабатывания на кадре. #293 Этап C: плашка «55 из ста» уехала на кадр-удар `s27_1`, кадр стал легче — пол переобъявляется по собранному PDF этапа
timing_min: 1.3
in_bucket: true
method_steps: ["①цена ошибки", "②классические режимы", "③модель против них", "④как это устроено", "⑤что переехало"]
form: ["форма 3", "форма 4"]
vfy: true
status: собран
---

## Visible slide text

**How this 55 out of 100 came about.** Chest images, Moscow, May–September 2024: 575,549 fluorography and X-ray scans, three services.

**How it's built.** Sensitivity was set to **1.0**, specificity was declared **not significant**. 45 images out of 100 go into "not normal" — the radiologist reads these. The rest go into the chart without him.

**What was missed:** infiltrate or opacity — 266 of 290 cases.

## Speaker notes

Moscow, May–September 2024: 575,549 preventive chest fluorography and X-ray scans, three registered services. Sensitivity was set to one, specificity was declared not significant — and a human stopped reading more than half of this stream. The breakdown has to start with the cost of both errors, because the entire engineering decision for this case was derived from it.

A preventive chest image is taken on a person with no complaints. A missed infiltrate on such an image means tuberculosis or a tumor that will be caught on the next cycle, a year later, and the cost of the miss is measured by the stage at which the disease is caught. An unnecessary alarm on a preventive image is incomparably cheaper: the person just gets called in for a follow-up exam. The asymmetry here is extreme, and it is exactly what set the trigger threshold.

The classical regimes, counted in the same unit. The first: a radiologist reads every preventive image. The share of clinically significant misses for a human on a chest X-ray is three to four percent, and that figure comes from the same center that ran the study, on a sample of 8,815 images and 403 specialists. The second regime is double reading, two radiologists per preventive image. It is not used at mass scale, and not for methodological reasons: there are not enough readers even for a single reading. The first regime's cost is also named, and named by the mandatory health insurance tariff: a human reading one preventive chest X-ray costs 132 rubles 98 kopecks.

Now the model against these regimes, and the mechanics matter more than the result here. The trigger threshold was set as follows: sensitivity 1.0 with a confidence interval from one to one, specificity ruled not significant. This is an engineering decision, not a property of the model. With this setting, the system is bound to raise an alarm on anything even partly resembling an abnormality, and the price it pays for that is that almost half the stream ends up in "not normal."

From there the stream splits in two. Images classified as "not normal" go to a reference-center radiologist — 260,058 of them, forty-five out of a hundred. Images classified as normal are read by nobody: the model's finding goes straight into the electronic chart. There are 315,491 of them, fifty-five out of a hundred, and that is the entire benefit of this case.

It was checked in a way routine practice never checks and never will. All 315,491 "normals" were re-read by radiologists from a federal academy — an organization not involved in the deployment. They raised 942 suspicions. A thoracic radiologist confirmed 411 of them, and the remaining 531 turned out to be false alarms from the checking physician himself — and that number is worth holding onto: the human doing the checking here was wrong more often than the machine being checked. Of the 411 confirmed, 290 were clinically significant, 121 were not.

The outcome in one line: 290 clinically significant misses out of 575,549 images, that is, five per ten thousand, with a confidence interval of four to six per ten thousand. The triage was correct in 99.95 percent of cases.

These five per ten thousand cannot be compared directly with the human three to four percent, tempting and devastating as the comparison looks. The human share is computed over the entire stream, including the hard images. The model's share is computed only over the subset it itself selected as easy. The two numbers do not share a denominator, and a sixtyfold difference does not follow from them.

What exactly was missed is worth naming item by item. Infiltrate or consolidation — 188 of 290 cases. An area of opacity — 78. Widened mediastinum — nine, pleural effusion — five, a break in the integrity of a bone plate — three, atelectasis — three, dissemination — two, a cavity — two. The first two items account for ninety-two percent of all clinically significant misses, and these are exactly the findings a preventive image is taken to catch.

The cost of this benefit — the money, the regulatory change, and the vanished layer of review — is broken down on the next slide.

**Sources.** [Vasilyev et al., *Digital Diagnostics* 2025;6(1):5–22](https://doi.org/10.17816/DD641703)
