---
# СВЁРТКА (#229) СВЕДЕНА ПО СМЫСЛУ сессией содержания: вторая половина пришла из s19 (файл в slides/_snyato/) и больше не стоит отдельным куском — обе половины собраны в одну форму §5.13.
# ДОБАВЛЕНО (issue #270, доработка инженерной глубины разбора §2 obzor-stran-i-glubina-razbora.md).
# Два новых факта из chapter-part1b.md §1.6: (1) устройство порога — три взаимоисключающих исхода,
# не два, заменило прежнюю упрощённую «метку» в «Устроено»; (2) обучающая выборка нашлась (порядка
# 25 000 обследований, University of Iowa/EyeCheck) — заменила прежнюю «производитель не публикует»
# в обоих местах заметок, с той же осторожной формулировкой «порядка», что и в главе: первоисточник
# числа не вскрылся, точнее не утверждается. Остальной новый материал главы (пост-маркетинговое
# обновление 510(k) K213037, германское измерение чувствительности к популяции, архитектура EyeArt)
# на этот кадр не поместился бюджетом — он на новом `s18b`, см. `razbor_part` ниже.
#
# РАЗРЕШЕНО (issue #270, круг доводки R3): владелец повторил старую пометку
# «глазное дно не скрининг» — читая «скрининг» как «скрининг здоровых
# незаинтересованных людей». По первоисточнику (Wolf и соавт., Nature
# Communications 2024, DOI 10.1038/s41467-023-44676-z) заголовок статьи сам
# называет протокол screening («...increases screening and follow-up for
# diabetic retinopathy in youth...»), а собственное определение стадии этой
# деки на `s11a` (строка 43) явно включает «предшествующий диагноз» в список
# группирующих признаков наряду с возрастом и полом. Выборка этого кейса —
# диагностированные диабетики, бессимптомные ПО ОТНОШЕНИЮ К ЦЕЛЕВОМУ
# СОСТОЯНИЮ (ретинопатии): это целевой/группоспецифичный скрининг осложнения
# у группы риска, а не популяционный скрининг диабета у здоровых. Кейс НЕ
# снят (резать разделы запрещено нарядом, замены равной силы в research/ не
# нашлось) — вместо этого title/assertion/первая строка тела переквалифицируют
# случай явно, без слова «методически».
id: s18
local_id: s1-08
section: "1. Первичный скрининг и отбор на обследование"
type: case
title: "Example 3: the fundus is photographed at the appointment"
assertion: "Это целевой скрининг осложнения — диабетической ретинопатии — у уже диагностированных диабетиков (группа риска по предшествующему диагнозу, см. s11a), а не популяционный скрининг диабета у здоровых; само испытание называет протокол screening в заголовке статьи (Wolf и соавт., «…increases screening and follow-up for diabetic retinopathy…», Nature Communications 2024). Выигрыш измерен явкой, а не точностью чтения: до теста у специалиста доходили 22 человека из ста, со съёмкой на приёме — все сто, а до офтальмолога после отклонения — 64. Что это стоило — кадром следом"
source: "Wolf and co-authors, Nature Communications 2024 — https://doi.org/10.1038/s41467-023-44676-z"
media: ""
media_needed: "Фотография ретинальной камеры для скрининга диабетической ретинопатии в кабинете первичного звена."
media_note: "СНИМОК СНЯТ С КАДРА (#229, сессия содержания) — два довода, оба проверяемые. Первый физический: сборка говорит «боковая иллюстрация не умещается ни при какой ширине до 2.60\" — кадру нечего ей отдать» и при ней же даёт блокирующую [высота] («примитивы съели кадр», тела 0.12\"); кадр несёт схему порядка работы, полосу плашек и обязательный состав §5.13, и ужать их ради снимка значило бы снять измеренное. Второй содержательный, и он уже стоял в этом же поле ниже: на снимке кабинет ОФТАЛЬМОЛОГА (справа щелевая лампа) на кадре, который называется «без офтальмолога». Файл и его проверка сохранены ниже: если владелец предпочтёт вернуть снимок, резать придётся содержание, и это его решение, не моё. ПРЕЖНЯЯ ЗАПИСЬ ПОЛЯ: ПРОВЕРЕНО ГЛАЗАМИ (#229, класс О12): по предмету СООТВЕТСТВУЕТ — настоящая ретинальная камера Topcon TRC-NW8, на мониторе рядом настоящий снимок глазного дна с диском зрительного нерва. ОДНО РАСХОЖДЕНИЕ С ЗАКАЗОМ: заказан кабинет ПЕРВИЧНОГО ЗВЕНА, а на снимке кабинет офтальмолога — справа щелевая лампа, это оснащение специалиста. Тихое противоречие с текстом рядом: заметка в двух строках от картинки говорит «без офтальмолога — доходят сто из ста». Ложного утверждения в заметке НЕТ (она про снимок глазного дна у пациента, не про иллюстрацию), поэтому правка не срочная; решать сессии раздела 1"
razbor_part: "1 из 3; ①цена обеих ошибок, ②оба классических режима в явке, ③модель против них — здесь; ④как устроено ЦЕЛИКОМ (вход/выход, три исхода порога, имя изделия, обучающая выборка) переехало на s18b, чтобы не стоять двумя кусками на двух кадрах; продолжение ④как устроено (архитектура EyeArt, пост-маркетинговое обновление 510(k) K213037) и честно поименованный ⑤обучение/обновление/дрейф (германское измерение чувствительности к популяции и навыку оператора, явно отделённое от дрейфа во времени) — на s18b; ⑤что переехало и пара дало–потребовало — на s18a"
blocks:
  - {label: "Step 1 — reached the exam", value: "22 → 100 out of 100", note: "81 versus 83, by randomization", key: true}
  - {label: "Step 2 — reached the ophthalmologist", value: "16 people out of 25", note: "that is 64 out of 100; in the control, the same 22"}
scheme:
  arrows: true
  rows:
    - {label: "Without the model", steps: ["Referral", "Waiting for the visit", "Specialist reading"]}
    - {label: "With the model", steps: ["Image taken by the nurse", "Autonomous reading", "On-the-spot decision"]}
pol_slov: 222   # ЗАМЕР ПОСЛЕ R3 (issue #270, круг доводки 3): владелец повторил «глазное дно
  # не скрининг» — title переквалифицирован в «целевой скрининг осложнения у
  # диабетиков», первая строка тела явно называет это целевым скринингом осложнения
  # (ретинопатии) у диагностированных диабетиков, не скринингом диабета у здоровых, и
  # отмечает, что сами авторы называют протокол screening; assertion получил ту же
  # классификацию с опорой на s11a и DOI первоисточника. +12 слов от правки R2.
  # ЗАМЕР ПО СОБРАННОМУ PDF раздела 1 (render_sec.py 1, 2026-10-19, 14 страниц): 222
  # слова на этом кадре; медиана полосы 156, максимум 259 (`s16`), блокирующих 0
  # (`build_lec07.py --only s15,s15a,s16,s16a,s18,s18a,s18b`). Поле выставлено ПО
  # ЗАМЕРУ, не по оценке.
  # ПРЕЖНЕЕ ЗНАЧЕНИЕ (#229 пп.17–18, владелец: «это не отбор — перенести в диагностику или убрать; если оставить — убрать лишний текст и явно показать эффект»; «объединить с 17»). Склейка СВЕДЕНА ПО СМЫСЛУ, а не сложением: из четырёх плашек прежние три были словами без чисел («Дало», «Потребовало», «В сумме») и дублировали строку пары дало–потребовало в теле — сняты, а их место заняли измеренные величины со своими базами: явка 22 → 100 из ста (81 против 83, жребий), второй шаг того же пути 22 → 64 из ста (из 25 отклонений дошли 16), негодных 5 снимков из ста (101 710 визитов, 404 клиники). ОТВЕТ НА «ЭТО НЕ ОТБОР» стоит на кадре строкой: выигрыш измерен явкой, а не точностью чтения, — то есть мерится «кого вообще посмотрели», вопрос этой стадии. Перенос в диагностику не делался: резать разделы этой сессии запрещено нарядом. ЭФФЕКТ показан явно тремя числами и отказным потоком 75,7 процента. Добавлена цена обеих ошибок, которой на видимом слое НЕ БЫЛО вовсе при объявленном method_steps ①. Чем заняты слова: цена обеих ошибок · схема двух порядков работы · три плашки с базами · устройство с именем изделия и типом задачи · отказной поток с оговоркой о несводимости · пара дало–потребовало. ЧТО ОСТАЛОСЬ НЕ ЗАКРЫТО И НАЗВАНО ЧИСЛОМ: тело набрано 10,5 пт при поле 12 — блокирующих нет, но пол видимого слоя не взят. Замерено три состояния: со снимком и прежним телом — блокирующая [высота] (тела 0,12 дюйма, «примитивы съели кадр»); снимок снят, тело сжато — 10,5 пт без блокирующих; снять ещё и схему порядка работы — 12 пт и чисто. Схема оставлена сознательно: она единственная даёт сопоставление «без модели / с моделью» одним взглядом, а его отсутствие владелец называл системной ошибкой. Выбор между 10,5 пт и снятой схемой — за владельцем ЗАМЕР ПО СОБРАННОМУ PDF полосы Входа и раздела 1 (render_sec.py 0 1, 2026-10-15, 14 страниц): 189 слов на этом кадре; медиана полосы 142,5, максимум 263, блокирующих 0. Поле выставлено ПО ЗАМЕРУ, не по оценке: прежнее число в этой строке называло состав до правки по замечаниям владельца и после неё было бы разрешением на чужой вес. ЗАМЕР ПОСЛЕ РАЗДЕЛЕНИЯ (render_sec.py 0 1, 15 страниц): 189 слов на этом кадре; тело кадра набрано не ниже пола 12 пт, блокирующих 0. До разделения склейка весила 237 слов и держала тело на 10,5 пт. ЗАМЕР ПОСЛЕ ISSUE #270 (render_sec.py 1, 13 страниц раздела 1): 210 слов на этом кадре — рост на 21 слово от правки «Устроено» (три исхода порога вместо одной метки, пункт 1 наряда); медиана полосы 210, максимум 286 (`s13a`), блокирующих 0 (`build_lec07.py --only s18,s18a,s18b`). Обучающая выборка (пункт 2 наряда) правилась только в заметках — на счёт тела не повлияла
timing_min: 0.95
in_bucket: true
method_steps: ["①цена ошибки", "②классические режимы", "③модель против них", "④как это устроено"]
form: ["сетка"]
vizforma: "ряды"
vfy: false
status: собран
---

## Visible slide text

**What this case is.** Adolescents aged 8–21 with diabetes: once a year they are checked for a complication — fundus damage. This is a check of an at-risk group, not screening of healthy people.

**The cost of both errors:** a miss — asymptomatic until vision loss · a false call — a visit to a specialist who may not exist in the area · and they lose people to no-shows.

**Both classical regimes are counted in attendance:** to the ophthalmologist once a year — 22 out of 100 · not screening at all — zero.

## Speaker notes

Adolescents from eight to twenty-one years old with diabetes: once a year they are checked for a complication — fundus damage. In a randomized trial, the image is taken by a nurse or a primary-care technician right at the visit, and the decision to refer or not is issued by the authorized device on the spot, in under a minute, without an ophthalmologist. Attendance at the exam rose to one hundred people out of one hundred, against twenty-two. This is a check of an at-risk group with an existing diagnosis, not screening of healthy people for diabetes.

The cost of both errors is stated before any accuracy figure. Missing fundus damage in a person with diabetes means reaching vision loss: up to the late stages it is asymptomatic, the person feels nothing and so does not come in. An unnecessary referral costs a visit to a specialist who may not exist in the area. And a third quantity decides everything: they lose people to no-shows. A test that a person never reached has zero sensitivity, whatever it measures in the lab.

Both classical regimes are counted in one unit — attendance. The first: once a year, a person with diabetes goes to an ophthalmologist, who takes the image and reads it himself; twenty-two people out of one hundred reach the test. A separate visit to a separate specialist on a separate day, often in another city, while the person feels nothing — the regime loses people along the way. The second regime is unpleasant to name, and it is more widespread than the first: not screening at all. Its attendance is zero, and that figure comes from definition, not measurement. This is how monitoring works where there is no ophthalmologist in the area; without naming this regime, the gain in attendance reads only against a visit to the specialist, when it was also obtained against nothing at all.

The comparison base: eighty-one people against eighty-three, randomized, one device. The device's sensitivity does not enter into this breakdown — the sources give no prevalence of the lesion in these samples, and accuracy cannot be read without the group and the prevalence.

The second step of the same path is counted within the same trial: of twenty-five people whose result came back abnormal, sixteen reached the ophthalmologist — sixty-four out of one hundred, against twenty-two in the control. The criterion this breakdown leaves behind: autonomy transfers responsibility and does not eliminate work — it shifts it onto a different step and a different person. If this step was not counted, the deployment is cheaper than it actually is. Here it was counted, which is why the breakdown holds up: sixty-four percent were carried through to the specialist, not one hundred.

Not everything is known about how the device is built, and both halves are worth naming. Input — two fundus images taken by a nurse or technician in a primary-care office; output — a "refer or not" label. The system was trained on roughly 25,000 complete exams (University of Iowa and the EyeCheck project); the primary source of this figure did not come up in full text, so it is not claimed more precisely than "roughly", and it must not be rounded into a certainty when retold. The publication does not name the device that operated in this trial. The regime does have names, and they are checkable: the first authorization in history for autonomous diagnosis without physician interpretation was granted in 2018 to the IDx-DR system, which is called LumineticsCore today; the retrospective stream of one hundred and one thousand visits discussed further on was captured on an EyeArt device.

How far this evidence can be trusted: the allocation to groups is random — evidence does not get stronger than that — but the sample is small, there is one device, the age group is narrow, and there is not a single replication.

**Sources.** [Wolf et al., Nature Communications 2024](https://doi.org/10.1038/s41467-023-44676-z)
