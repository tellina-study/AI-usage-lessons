---
# ВСТАВКА (issue #270, доработка инженерной глубины разбора по §2
# obzor-stran-i-glubina-razbora.md). Продолжение разбора s18/s18a («Пример 2: глазное дно
# снимают на приёме, а не у офтальмолога»), не новый кейс — отмечено полем `razbor_part`.
# Третья часть того же разбора: s18 несёт ①-④(начало), s18a несёт ⑤что переехало, здесь —
# продолжение ④как устроено (архитектура, обновление) и честно поименованный ⑤обучение/
# обновление/дрейф, которого на первых двух кадрах не было вовсе.
#
# local_id ПРОВЕРЕН перед присвоением (grep по всему `library/lectures/lec-07/rework/`,
# включая `slides/_snyato/` и оба плана `plans/block-01-otbor*.md` и `SLIDE-PLAN.md`):
# `s1-08b` и `s1-08c` нигде не встречаются и нигде не зарезервированы под другое содержание —
# в отличие от `s1-07a` (занят историей `_snyato/s17-arifmetika-kanala.md`, см. `s16a`) и
# `s1-04a` (зарезервирован в `plans/block-01-otbor-part2.md` под другое содержание, см. `s15a`).
# Единственный сосед по плану в этой зоне — `s1-10` («Чем эти клетки заняты сегодня», матрица
# сетки), и это другой адрес и другое содержание, коллизии нет. Взят первый свободный суффикс
# `s1-08b`. `id: s18b` — адрес показа: сортировка имён файлов (`order_key` в
# `tools/presentation-build/deckkit/slidefile.py`, пара (номер, буквенный хвост)) даёт
# `s18` → `s18a` → `s18b` → `s20` (кадра `s19` в деке нет вовсе) — кадр встаёт ровно туда,
# куда просил наряд: сразу после `s18a`, перед `s20` (вывод раздела).
id: s18b
local_id: s1-08b
section: "1. Первичный скрининг и отбор на обследование"
type: case
title: "Example 3, mechanics: training, updates, and a different population"
assertion: "Германское стационарное измерение (875 пациентов, 2026) на том же приборе, что дал пивотальные 87,2/90,7 процента, — другая популяция, не дрейф во времени: 26,1 процента снимков непригодны для анализа, чувствительность падает с тяжестью болезни (94,4 → 60,9 процента), а доля непригодных снимков у одного оператора падает с практикой (46,9 → 0 процентов за четыре дня); отдельно — допуск не замораживает устройство (заявка 510(k) K213037 обновила классификатор качества с версии 2.1.1 до 2.3.0), а у прибора другого производителя (EyeArt) отказ по качеству встроен в тот же механизм, что ставит диагностическую находку"
source: "German study of IDx-DR, 2026 — https://pmc.ncbi.nlm.nih.gov/articles/PMC12864748/ · submission K213037"
media: ""
media_needed: "иллюстрация не нужна структурно: кадр держат три плашки с измеренными величинами и их базами и схема «до допуска / после допуска» (с issue #270 r3 заменила словесное объяснение пути выборка→допуск→обновление в теле)"
media_note: "—"
razbor_part: "3 из 3 (продолжение s18/s18a, не новый кейс); на s18 — ①цена ошибки, ②классические режимы, ③модель против них и начало ④как устроено (вход/выход, три исхода порога, имя изделия, обучающая выборка «порядка 25 000»); на s18a — ⑤что переехало (сменился исполнитель, появился шаг) и пара дало–потребовало; здесь — продолжение ④как устроено (архитектура EyeArt, пост-маркетинговое обновление 510(k) K213037) и честно поименованный ⑤обучение/обновление/дрейф: германское измерение чувствительности к популяции и навыку оператора, явно отделённое от дрейфа во времени — вопрос, которого на первых двух кадрах разбора не было вовсе"
blocks:
  - {label: "Ungradable images at the hospital", value: "26 out of 100", note: "875 patients, same device, different population"}
  - {label: "Detects: severe → moderate form", value: "94 → 61 out of 100", note: "at authorization, the same device gave 87 and 91", key: true}
  - {label: "Image defect rate: day 1 → day 4", value: "47 → 0 out of 100", note: "the same operator throughout"}
scheme:
  arrows: true
  rows:
    - {label: "Before authorization", steps: ["≈25,000 exams", {text: "Model training", ai: true}, "Regulator authorization, 2018"]}
    - {label: "After authorization", steps: ["Different population", "Detects worse, rejects more", "Protocol update"]}
pol_slov: 157   # ЗАМЕР ПОСЛЕ R3 (issue #270, круг доводки 3): title и первая строка тела
  # названы по случаю (диабетическая ретинопатия, IDx-DR), добавлена схема «до
  # допуска / после допуска» (2 ряда × 3 шага, явный `ai: true` на шаге «Обучение
  # модели»: в этой деке `ai_by_word=False`, золото угадыванием не ставится), тело
  # прозы сокращено с 130 до 41 слова — больше половины: первый проход на 81 слове
  # упёрся в блокирующее [кегль] (0.66/0.69 рабочего кегля — схема+3 плашки+тело не
  # укладывались), сняты caption схемы и часть детали EyeArt из тела (осталась в
  # заметках). ЗАМЕР ПО СОБРАННОМУ PDF раздела 1 (render_sec.py 1, 2026-10-19, 14
  # страниц): 157 слов на этом кадре; медиана полосы 156, максимум 259 (`s16`),
  # блокирующих 0 (`build_lec07.py --only s15,s15a,s16,s16a,s18,s18a,s18b`). Поле
  # выставлено ПО ЗАМЕРУ, не по оценке.
  # ПРЕЖНЕЕ ЗНАЧЕНИЕ (issue #270, новый вставной кадр (третья часть разбора s18/s18a)). ТРИ ПЛАШКИ несут
  # числа с базами (непригодность 26,1% на 875 пациентах · чувствительность 94,4%→60,9% по
  # тяжести болезни · непригодность 46,9%→0% по дням практики одного оператора), тело — четыре
  # коротких абзаца БЕЗ повторения этих чисел (та же дисциплина, что `s15a` применила к своим
  # четырём плашкам): германская выборка явно подписана «другая популяция, не дрейф» ·
  # разведение двух разных эффектов (тяжесть болезни vs навык оператора) · пост-маркетинговое
  # обновление сжато до одного предложения с номером документа (510(k) K213037, версии
  # классификатора) · архитектура EyeArt сжата до одного предложения с механизмом (две
  # свёрточные сети на общих слоях). Четвёртая плашка (версии классификатора v2.1.1→v2.3.0)
  # сознательно НЕ заведена — осталась одним предложением в теле, чтобы не раздувать полосу
  # плашек ради детали, которая сама по себе не числовой выигрыш/цена, а факт механизма.
  # ЗАМЕР ПО СОБРАННОМУ PDF раздела 1 (render_sec.py 1, 13 страниц, 2026-10-18): 222 слова на
  # этом кадре; медиана полосы 210, максимум 286 (`s13a`), блокирующих 0
  # (`build_lec07.py --only s18,s18a,s18b`). Поле выставлено ПО ЗАМЕРУ, не по оценке.
timing_min: 0.85
in_bucket: true
method_steps: ["④как это устроено (архитектура EyeArt, пост-маркетинговое обновление)", "⑤обучение и дрейф к популяции"]
form: []
vfy: true
status: собран
---

## Visible slide text

**How it's built:** input — two fundus images; output — one of three outcomes: refer to an ophthalmologist · normal, repeat in a year · image is ungradable. IDx-DR (now LumineticsCore) was the first authorized, in 2018. *Image classification.*

**Authorization does not freeze the device:** the quality classifier was updated through a submission.

**These are two different effects:** disease severity versus skill at holding the camera.

## Speaker notes

The EyeArt reject stream was measured on different material — a different device and a different program, named on the previous slide with an explicit caveat about non-comparability. What follows is what is known about the training of the IDx-DR/LumineticsCore device itself, how it is updated after authorization, and what a separate measurement on a new sample showed.

A German study at a tertiary diabetes hospital (Karlsburg, 2020–2021, 875 patients, average age 52, range 8 to 92) tested the same device, IDx-DR, which gave the pivotal 87.2 and 90.7 percent sensitivity and specificity on the registration sample. In this German sample, the system itself flagged 26.1 percent of images as unfit for analysis — against 96.1 percent gradable at the pivotal study. This is not proof of drift over time: the German sample consists of hospitalized, older, and more severe diabetics, with a higher likelihood of cataracts and constricted pupils, rather than the US primary-care target population for which the device was authorized in 2018. The correct reading is a measurement of how sensitive the result is to the composition of those examined, not a deterioration of the device over the years.

Sensitivity on this same German sample turned out to differ by severity of the lesion rather than being a single number: 94.4 percent for severe diabetic retinopathy — close to the pivotal figures — and only 60.9 percent for the moderate form. Exact agreement with the ophthalmologist's severity grading was only 54.2 percent of cases. The spread is wide enough that a single sensitivity number for this device simply does not exist: it is tied to exactly who is being examined.

The same study found a separate and strong effect — operator training on the camera, not a change in the algorithm: the share of ungradable images for one and the same examiner fell from 46.9 percent on the first day of working with the camera to 0 percent on the fourth day of practice. The model's decision did not change at all here — what changed was the hand of the person holding the camera.

The 2018 authorization does not fix the device forever. At registration, a change-control protocol was agreed: technical modifications capable of affecting the false-positive rate require a new notification to the regulator before deployment, not a quiet update. A concrete example of this mechanism in action is 510(k) submission number K213037, which updated the image-quality classifier from version 2.1.1 to 2.3.0. The full text of the submission did not come up as readable text on direct access to the document, but the fact of filing and the document number are confirmed on the regulator's site — this is exactly the second of the three states of a gap: searched in good faith, found the document, but not its contents.

The device from a different manufacturer, EyeArt — the very one that produced the reject stream and the more-than-75-percent stream on the previous slide — is built differently, judging from patent documents: two convolutional networks on shared layers, one segmenting retinal structures, the other assessing the quality of the image itself. Here, rejection for quality is not a separate filter ahead of diagnosis but is built into the same mechanism that produces the finding. The sources do not disclose the details of the training sample for the certified version of the device — there is only an adjacent validation dataset of different origin, and it cannot be equated with the training set.

The five engineering-depth questions for this case are closed unevenly, and it is worth saying so plainly: input-output and the threshold are fully closed; training only to an order of magnitude; the update is a fact of mechanism without the content of the change itself; and drift is not this same device on the same population at all, but someone else's sample of the same device. The gap between "closed" and "partially closed" here is not a reason to drop the breakdown — it is the honest answer to a question that most medical-AI material does not ask at all.

**Sources.** [Scientific Reports / PMC12864748, "Real-world performance of the AI diagnostic system IDx-DR in the diagnosis of diabetic retinopathy and its main confounders", 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC12864748/) · [FDA 510(k) K213037, accessdata.fda.gov](https://www.accessdata.fda.gov/cdrh_docs/pdf21/K213037.pdf)
