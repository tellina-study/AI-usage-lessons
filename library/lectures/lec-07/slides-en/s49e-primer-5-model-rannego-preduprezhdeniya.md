---
# ПЛАШКИ РАЗГРУЖЕНЫ ПОД СХЕМУ (пп. 11-12 наряда). Схема заняла бюджет высоты, и кадр перестал
# держать прежний набор плашек: сборка давала [высота] s49e/тело: не укладывается даже при масштабе 0,58 — 1,03 против 0,61 дюйма. Снято по двум правилам, не на глаз.
# §7.1 — оговорка о НАДЁЖНОСТИ замера уходит в заметки целиком, знаменатель остаётся на кадре.
# §5.15 — упоминание из ДРУГОЙ работы на кадре разбора есть библиография, а не разбор; его место
# в заметках, и там оно уже стоит целиком. Ни одно измеренное число не потеряно: снятое
# перечислено поимённо ниже и читается вслух.
# СНЯТО С КАДРА: хвосты подписей у двух плашек цены (о ведущей причине внутрибольничной смерти и об антибиотике «на всякий случай») — это объяснение цены, которое лектор произносит; сами обе цены на кадре остались
# СХЕМА ДОБАВЛЕНА (п. 11 наряда, §11.3: «схема обязательна у каждого кадра типа `case`»).
# Замер прожарки: схема нашлась у 5 кадров `case` из 12 в разделе, и не было её ровно у семи
# самых тяжёлых по тексту — то есть там, где она нужнее всего. §10.3: схема решения несёт
# инженерное содержание, текст — пояснение к ней, не замена; поэтому вместе со схемой из тела
# СНЯТО то, что она теперь показывает сама (п. 12 наряда, плотность: чинить схему и объём
# вместе, а не по очереди).
# ИМЯ ВЕЛИЧИНЫ СВЕДЕНО ПО ВСЕЙ ДЕКЕ (п. 13 наряда, §5.20 сквозная ревизия): здесь величина
# звалась «различением», на s30 · s41 · s49b · s102 — «площадью под кривой». Одна величина не
# может стоять на одних кадрах под одним именем, на других под другим; шкала «0,5 монетка,
# 1,0 без промаха» при этом сохранена — она и есть объяснение, которое §5.20 требует.
# ПРЕФИКС СТАДИИ ПЕРЕПИСАН (переделка раздела 2 по канону PR #286, `storozha-i-priyomka.md` §14).
# Было `s4-05` — префикс стадии «динамическое наблюдение и клинические тревоги». Стадия эта
# самостоятельным разделом деки не является: владелец снял её по имени 2026-10-15 («раздел
# наблюдение убираем, пример из него в диагностику» · «пример в диагностику в виде 1-2
# слайдов», запись — `_snyato/README.md`), и этот разбор стоит здесь по его указанию. Пока
# то решение не отменено письменно, кадр принадлежит разделу «Постановка диагноза» —
# и префикс обязан это говорить, иначе сторож «один раздел — один префикс стадии» ловит
# расхождение, которого по существу нет. Материал разбора при этом остаётся материалом
# стадии наблюдения, и заметки кадра это называют; на видимый слой такая оговорка не идёт (§7.1).
id: s49e
local_id: s3-17
section: "3. Постановка диагноза"
type: case
title: "Example 5: an early-warning model for sepsis"
assertion: "Модель сепсиса, встроенная в медицинскую карту, заменила балльную шкалу, которую считали руками; независимая проверка дала различение 0,63 против заявленных 0,76–0,83, подтверждается 12 тревог из ста поднятых против 8 у шкалы, опережения клинического решения нет вовсе — и разбор тревоги стал новой статьёй рабочего времени той же смены"
source: "Wong, Otles et al., JAMA Internal Medicine 2021, with an erratum in the same journal — https://doi.org/10.1001/jamainternmed.2021.2626 · a comparison of scoring scales, JAMIA Open 2021 — https://doi.org/10.1093/jamiaopen/ooab062 · Ostermayer et al., JAMIA Open 2024 — https://doi.org/10.1093/jamiaopen/ooae133 · claims for the second version and a prospective validation — https://doi.org/10.1001/jamanetworkopen.2026.0181"
media: ""
media_needed: "иллюстрация не нужна — кадр держат две цены и полоса плашек"
media_note: "свёрнут из шести кадров снятого раздела наблюдения; снимок сестринского поста и экран прикроватного монитора ушли вместе с ними в _snyato"
blocks:
  - {label: "The cost of a miss", value: "hours until the ICU", note: "not measured in money"}
  - {label: "The cost of a false alert", value: "after a hundred of these — dismissing without reading", note: "time taken from another patient"}
  - {label: "Confirmed out of alerts raised: scale → model", value: "8 → 12 out of a hundred", note: "scale: 45,776 patients, sepsis in 3.3 out of a hundred · model: 38,455 admissions, 6.6 out of a hundred"}
  - {label: "Claimed → measured by an independent validation", value: "0.76–0.83 → 0.63", note: "area under the curve: 0.5 is a coin flip, 1.0 is no misses. Caught 33 cases out of a hundred — missed 1,709 out of 2,552", key: true}
pol_slov: 230   # СВЁРТКА 4→2 (#229, владелец: «пример сильно сокращаем до 2х слайдов», уточнение «в виде 1-2 слайдов»). 227 по собранному PDF. Чем заняты слова — обязательным по §5.13, и каждый пункт пришёл со своего снятого кадра: цена ОБЕИХ ошибок плашками (с `s55`) · классический режим с базой 45 776 и подписью про две другие шкалы (с `s56`) · имя изделия и класс модели (с `s57`) · заявленное против измеренного со шкалой различения · «как проверяли». ОДИН КАДР ПРОБОВАЛСЯ И ЗАМЕРЕН: всё обязательное вместе даёт блокирующее `[высота] −0,88"`, а после снятия столбцов и схемы — тело 9,5 пт при поле 12,0. Поднять кегль можно было только срезав измеренное, что наряд запрещает; два кадра — результат замера, а не оценки. Вес в семье разборов этой деки обычный: рядом стоят 256 (`s41`), 252 (`s16`), 244 (`s15`), 214 (`s49b`)
scheme:
  caption: "The classical mode isn't zero, it's a scale tallied by hand"
  arrows: true
  rows:
    - {label: "Scale by hand", steps: ["points from a table", "the sum", "the threshold", "the assigned action"]}
    - {label: "Model in the record", steps: ["vitals and notes, continuously", {text: "risk score", ai: true}, "alert with orders", "the shift reviews it"]}
timing_min: 1.1
in_bucket: true
method_steps: ["①цена ошибки", "②классические режимы", "③модель рядом", "④как устроено"]
vfy: true
status: собран
---

## Visible slide text

**The Epic sepsis model** inside the medical record. *A forecast from structured data: penalized logistic regression, no deep network.*

**The comparison has to be against the scale, not against zero.** *Retrospective, 27,697 patients.*

## Speaker notes

An early-warning model for sepsis, built into the medical record, replaced a scoring scale that had been tallied by hand before it. You have to start with how the scale is built: without it, there's nothing to compare against. An early-warning scoring scale is a table where every value measured at the bedside gets points for deviating from normal: a respiratory rate from twelve to twenty scores zero, twenty-one to twenty-four scores two, twenty-five and above scores three. The points are summed, the sum falls into a band, and the band assigns an action: continue observing, increase the frequency of measurements and call the on-call physician, or call the resuscitation team immediately. The weights in this table were set by a consensus committee of a professional society and printed on the chart that sits on the ward. Hence a property the model doesn't have: an error in the scale is handled as an error in a document — a committee convenes, revises the table, issues a new edition, and anyone who disagrees knows exactly who to object to and on which point.

I'm naming the cost of both errors before any numbers, and on the slide it stands as two plates. Missing a deterioration: sepsis is a leading cause of in-hospital death, and the clock here runs in hours until the ICU, not in money. Raising a false alert: an antibiotic given "just in case," time taken from another patient, and — after a hundred such alerts — the habit of dismissing a notification without reading it. The same shift pays for both errors, and the choice between them gets made many times a night.

Now the numbers, starting with what the model is compared against. For the scale, eight alerts out of a hundred are confirmed: the remaining ninety-two were raised for nothing, and that's the cost of the classical mode, before any machine learning at all. The measurement was taken on forty-five thousand seven hundred seventy-six patients, sepsis in three and three tenths out of a hundred, one sample covering all three scales at once; the other two scales in the same measurement came in at twelve and eighteen. A figure that circulates alongside this in the literature is eighty-eight and eight tenths — the false-alarm rate of a bedside monitor — and it can't be added to ours: that's a device at the bedside, with a threshold set by hand, with no trained model inside it at all. It's a different task and a different baseline; I'm saying this here so the slide doesn't carry two shares the room will add together.

What the developer claimed, and what an independent validation measured. For the first version of the model, an area under the curve of 0.76 to 0.83 was claimed. An external validation across 38,455 admissions measured 0.63 — discrimination only a bit better than a coin flip. The model caught 33 sepsis cases out of a hundred: it missed 1,709 out of 2,552. The developer released a new version after this, and what matters here isn't that the first fell short of what was claimed, but that this was learned from the outside: there was no internal validation that would have shown the same thing.

The two denominators on the slide are different, and confusing them is the main place where case studies like this lie. Eighteen out of a hundred is the share of admissions that received at least one alert: six thousand nine hundred seventy-one alerts across thirty-eight thousand four hundred fifty-five admissions. Twelve out of a hundred is the share of already-raised alerts that were confirmed. They're counted from different things. From this comes an arithmetic worth saying slowly: to find one case of sepsis, the shift has to review eight alerts. An earlier version of this case study said fifteen — that figure was retracted by an erratum in the same journal, and I'm naming this out loud, because this lecture is about how numbers live longer in retellings than in the original sources.

A second validation, by different authors and in different hospitals, adds something the first didn't measure — time. In the emergency department, it's the physician who recognizes sepsis: they examine the patient, order labs, start treatment. The validation compared the timing of the alert against the timing of that decision, across one hundred forty-five thousand eight hundred eighty-five visits to two departments in 2023. The median lead time was zero minutes; in roughly half the cases, physicians were already managing sepsis before the model spoke up. The authors' conclusion, verbatim: "adds little to what physicians are already doing." For the current version, validated prospectively across two hundred twenty-seven thousand ninety-one admissions in four systems, discrimination rose to a band of zero point eighty-two to zero point ninety-two, while confirmation stayed low — thirteen to twenty-six out of a hundred.

What shifted. The alert now exists and runs without a human — around the clock, across every patient at once, from data that already sits in the record in machine-readable form. That's a real gain, and a specialist will take it. But reviewing and dismissing an alert became a separate line item of working time that didn't exist before this was deployed, and at some hospitals this step has its own staff now. The vocabulary form here is the fourth — the load grew at the same spot: same place, same hand, more reading and dismissing. And the form "a step appeared" — about the review of the alert itself: with the scale, there was nothing to dismiss, since it computed its own threshold.

**Sources.** [Wong, Otles et al., JAMA Internal Medicine 2021, with erratum](https://doi.org/10.1001/jamainternmed.2021.2626) · [a comparison of scoring scales, JAMIA Open 2021](https://doi.org/10.1093/jamiaopen/ooab062) · [Ostermayer et al., JAMIA Open 2024](https://doi.org/10.1093/jamiaopen/ooae133) · [a prospective validation of the current version, JAMA Network Open 2026](https://doi.org/10.1001/jamanetworkopen.2026.0181) · [alert volume during the epidemic, JAMA Network Open 2021](https://doi.org/10.1001/jamanetworkopen.2021.35286)
