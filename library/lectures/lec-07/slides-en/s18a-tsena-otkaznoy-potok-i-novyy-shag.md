---
# ЧИСЛО ПРИВЕДЕНО К ЧИСЛУ ГЛАВЫ (переделка раздела 2, п. 6 наряда; канон
# `storozha-i-priyomka.md` §14, строка «число на слайде = число в главе»).
# БЫЛО «5 снимков из ста» на той же самой выборке, на которой тело главы
# (`chapter-part1b.md:245`) и её самопроверка (`:275`) говорят **0,9 процента —
# 910 из 101 710 визитов, прошедших валидацию**. Это не урезанная база, а ДРУГОЕ
# ЧИСЛО на том же знаменателе: расхождение впятеро.
# ОТКУДА ОНО ВЗЯЛОСЬ — найдено, а не угадано: перечень источников главы
# (`chapter-part1c.md:255`, пункт 10) называл «5 процентов снимков негодны по
# качеству», противореча телу той же главы. Дека брала число из перечня
# источников, тело главы его не подтверждало. Строка источника исправлена тем же
# кругом; иначе сторож вернул бы пятёрку на кадр при следующей сверке.
# РАЗДЕЛЁН ИЗ s18 (#229, сессия содержания, с явного разрешения оркестратора): склейка s18+s19
# не держала текст при поле кегля 12 пт — тело садилось на 10,5. Резать форму (схему «без модели /
# с моделью») запрещено доводом владельца о системной ошибке, резать обязательное по §5.13 —
# нарядом. Поэтому разбор разложен на два кадра по образцу деки («Пример 2, цена: вычитка другого
# рода», s63a): на s18 — явка, цена обеих ошибок, устройство; здесь — что переехало и чего это стоило.
# ДОПОЛНЕНО (issue #270): появился третий кадр разбора, `s18b` (архитектура EyeArt,
# пост-маркетинговое обновление, германское измерение чувствительности к популяции) — только поле
# `razbor_part` обновлено, чтобы назвать все три части; видимый текст и заметки этого кадра не трогались.
id: s18a
local_id: s1-08a
section: "1. Первичный скрининг и отбор на обследование"
type: case
title: "Example 3, cost: the reject stream and a new step"
assertion: "Решение «направить или нет» перешло к допущенному устройству целиком, и вместе с ним переехала ответственность за пропуск; производной формой появился шаг, которого у офтальмолога не было вовсе, — добыть годный снимок, — а цена этого шага измерена, но на другом материале, и с явкой в одну бухгалтерию не складывается"
source: "US regulator decision DEN180001, 2018 — https://www.accessdata.fda.gov/cdrh_docs/pdf18/DEN180001.pdf"
media: ""
media_needed: "иллюстрация не нужна: кадр держат две плашки и четыре строки"
media_note: "—"
razbor_part: "2 из 3 (issue #270 добавил третью часть, s18b, — поле обновлено, содержание этого кадра не трогалось); ①цена ошибки, ②классические режимы, ③модель против них и начало ④как устроено (вход/выход, три исхода порога, обучающая выборка) — на s18; продолжение ④как устроено (архитектура EyeArt, пост-маркетинговое обновление) и честно поименованный ⑤обучение/обновление/дрейф (германское измерение, явно отделённое от дрейфа во времени) — на s18b; здесь — ⑤что переехало и пара дало–потребовало"
scheme:
  arrows: true
  rows:
    - {label: "Before", steps: ["The ophthalmologist reads it", "The same person answers for it"]}
    - {label: "Now", steps: [{text: "The device reads it", ai: true}, "Responsibility rests with the device", "New step: a gradable image"]}
blocks:
  - {label: "Ungradable for quality", value: "0.9 out of 100", note: "910 of 101,710 visits, 404 clinics, adults"}
  - {label: "Stream the specialist never sees at all", value: "75.7 out of 100", note: "previously, normal cases reached him and he could check them", key: true}
pol_slov: 178   # #229, вторая половина разбора s18 после разделения. Чем заняты слова: мост на s18 одной строкой · две названные формы словаря (сменился исполнитель — по документу, единственный такой случай лекции; появился шаг, которого не было) · оговорка о несводимости с явкой, без которой две плашки читаются как цена того же опыта · пара дало–потребовало. Обязательное по §5.13 для этой половины — ⑤что переехало и пара — стоит целиком; ①–④ остались на s18 и названы полем razbor_part. Пол взят по замеру собранного PDF после разделения, тело кадра выше пола 12 пт ЗАМЕР ПОСЛЕ РАЗДЕЛЕНИЯ (render_sec.py 0 1, 15 страниц): 178 слов на этом кадре; тело кадра набрано не ниже пола 12 пт, блокирующих 0. До разделения склейка весила 237 слов и держала тело на 10,5 пт
timing_min: 0.75
in_bucket: true
method_steps: ["⑤что переехало", "пара дало–потребовало"]
form: ["форма 5", "форма 3"]
vizforma: "плашки"
vfy: false
status: собран
---

## Visible slide text

Imaging at the appointment delivered attendance. Now — what it cost, and to whom.

**The performer changed on paper** — the only such case in this lecture: responsibility for a missed finding moved from the physician to the device.

**The ophthalmologist never had this new step:** he adjusted the imaging conditions himself.

**Both figures come from a different program and a different device, in adults.**

**delivered** on-the-spot access · **required** a new step and a stream nobody reviews · **net**: access bought at the cost of a reject stream.

## Speaker notes

The same fundus imaging at the appointment, now counted from the cost side. The decision to refer or not moved from the ophthalmologist to a device authorized by the regulator in full, and responsibility for a missed finding moved along with it: previously it rested on the physician's decision, now it rests on the device. This is the only case in the entire lecture where the performer changed on paper: the first authorization for autonomous diagnosis without physician interpretation was granted in 2018.

Hence a new step that did not exist in the old order: obtaining a gradable image. The ophthalmologist had no such operation, because he adjusted the imaging conditions himself, on the spot. Now a nurse takes the image, and its gradability has become a separate task with its own defect rate.

How much this step costs has been measured — but on different material. On a mature stream, with a different manufacturer's device and in adult patients, nine-tenths of a percent of images are ungradable for quality: 910 of 101,710 visits that passed validation, across more than 400 clinics. And more than 75 percent of the stream the specialist never sees at all. Against attendance of 22 out of 100, these figures do not add up into one ledger: two different programs, two different devices, two different age groups. Combining them into one "delivered — required" pair would be exactly the splicing of samples this lecture is dissecting — which is why the reject stream gets its own slide with an explicit caveat, instead of sitting inside the payoff count.

What happened to the ophthalmologist. He sees roughly a fifth of the stream, and it is the part the model selected. Previously it was the specialist who decided what was normal; now the normal cases never reach him — and he cannot check whether they really were normal. This is the move named precisely: the work did not disappear, it moved to a different performer, and the ability to check it moved along with it. Seventy-five percent is exactly the size of that move, named in units of work rather than in words.

How this case differs from the Swedish screening program, where a model was "deployed" too: there, the model split the stream, but the finding for each study still came from a human — the order of work changed. Here the device issues the finding — the performer changed. The two deployments cannot be described in the same words, even though they often are.

Add the two halves together. Delivered: examination on the spot, at the same visit, without a separate trip to a specialist who may not exist in the area. Required: a new step with its own defect rate, and a stream nobody reviews. Net, this is access bought at the cost of a reject stream — and both halves have to be named together, because each one alone sounds like a conclusion on its own.

The criterion that carries forward: autonomy transfers responsibility and does not eliminate work — it shifts the work onto a different step and a different person. A deployment that did not count this step is cheaper than it actually is. For an engineer, two questions follow: who retakes an ungradable image, and on whose time; and who reviews the part of the stream the model classified as normal. Neither question is about the model's accuracy, and both are settled when designing the workflow, not when choosing the device.

The strength of evidence differs between the two halves of this breakdown, and they should not be equated. Attendance was measured by a randomized trial — the top rung of the evidence ladder, though with a small sample, one device, and a narrow age group; there is not a single replication. The figures on this slide did not come from a trial at all: they are a retrospective count from clinic records.

**Sources.** [US regulator decision DEN180001, 2018](https://www.accessdata.fda.gov/cdrh_docs/pdf18/DEN180001.pdf)
