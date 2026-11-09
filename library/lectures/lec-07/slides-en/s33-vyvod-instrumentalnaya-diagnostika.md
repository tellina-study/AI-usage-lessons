---
# ВОЗВРАЩЁН ИЗ `_snyato/` (переделка раздела 2 по канону PR #286). Снят он был не по содержанию,
# а как следствие слияния разделов: у слитого раздела вывод был один — `s50`, — и он закрывал
# «две стадии и один случай сверх них». Слияние отменено, значит каждая стадия снова получает
# свой вывод: этот закрывает инструментальную и лабораторную диагностику, `s50` — постановку
# диагноза, и ни один из двух больше не считает чужие места.
# КАРТА СТАДИИ ОТДЕЛЬНЫМ КАДРОМ НЕ ВОЗВРАЩАЕТСЯ — решение круга R6 действует (семь карт сняты,
# довод: обзор во входе `s01a`/`s01b` называет то же в одном месте и один раз, накопительная
# сетка собирается в «Итогах» на `s99` — прежде она стояла на `s101`, слитом туда в #293
# Этап B; правка одного имени в этом примечании, чтобы ссылка не висела на снятом номере).
# Вместо кадра-матрицы занятые клетки названы ЗДЕСЬ
# словами, последней строкой: тип задачи и модальность у каждой — это то, что карта несла
# содержательно, без её формы, которую зал уже отверг (§5.17 закрывается по существу).
# ЧЕТВЁРТАЯ КЛЕТКА НАЗВАНА ПУСТОЙ ОТ МОДЕЛИ, А НЕ ПРОПУЩЕНА: «измерение · сигнал прибора» —
# клетка без обученной модели, и честная пустая клетка лучше выдуманной занятой.
# СТРОКА О ШЕСТИ ИСКАЖЕНИЯХ ВЫНЕСЕНА ОТДЕЛЬНЫМ АБЗАЦЕМ (владелец 2026-10-20, «ок»). Стояла
# хвостом плотного перечня занятых клеток («Где модель стоит…») и там тонула: единственный в деке
# честный отказ — раздел не встретил ни одного механизма — читался как приписка к списку модальностей.
# ЦЕНА НАЗВАНА И ПРИНЯТА ВЛАДЕЛЬЦЕМ: отдельный абзац стоит кадру 0,5 пт кегля тела — замерено
# частичной сборкой, 11,0 → 10,5 пт (сторож `[пол]` мягкий, его число изменилось вместе с кеглем).
# Новых предупреждений нет: блокирующее одно и то же (`[плотность]` 194), прочих два и те же.
# Поднять кегль обратно можно было бы только срезав текст кадра — это уже не правка читаемости
# одной строки, и без отдельного решения владельца здесь не делается.
id: s33
local_id: s2-09
section: "2. Инструментальная и лабораторная диагностика"
type: comparison
title: "Section conclusion: the reading itself failed once out of five"
assertion: "В трёх разборах из пяти провалилось не чтение, а место, состав набора и определение цели; в четвёртом автономное чтение разрешили и посчитали его цену, в пятом запретили — и различает их не качество модели, а цена ложной тревоги. Модель на этой стадии даёт постоянство, поток и воспроизводимость и не умеет назначить порог срабатывания, переснять и увидеть смещение собственного входа; взамен нагрузка выросла на том же месте, появился повторный визит, сменился исполнитель и сместилась цена ошибки, а держат эту нагрузку порог срабатывания под цену обеих ошибок и контроль годности измерения — и ни одна процедура не проверяет, что система считает своей целью"
source: "—"
media: ""
media_needed: "иллюстрации нет: противопоставление столбцами и строка занятых клеток держат кадр сами"
media_note: "прочерк стоит последней строкой правого столбца — в нём сам вывод; полужирным его НЕ набирать: `columns` разметку не читают и выводят звёздочки как текст (поймано личным просмотром PNG 2026-10-19, ни одна проверка сборки этого не видит)"
columns:
  left:
    head: "What works"
    items:
      - "consistency: the ten-thousandth image reads like the first"
      - "throughput: \"normal\" does not occupy the specialist"
      - "reproducibility: a discrepancy can be worked through"
  right:
    head: "What does not work"
    items:
      - "setting the trigger threshold: a cost of both errors stands behind it"
      - "ordering a retake: measurement gradability stays with the human"
      - "seeing that the input itself is biased: no procedure can do this"
blocks:
  - {label: "The setting, the dataset, and the target failed", value: "3 of 5", note: "Thailand · skin · program selection", key: true}
  - {label: "The reading failed as a reading", value: "1 of 5", note: "hemorrhage: 293 false alarms against 4 on 3,409 scans"}
  - {label: "Autonomy was granted and withheld in the same city", value: "decided by the cost of an alarm", note: "preventive stream — a follow-up exam · emergency path — a crew"}
pol_slov: 203   # ПЕРЕОБЪЯВЛЕН ПО ЗАМЕРУ в круге #285 §2.4 (механизмы искажений проведены в разделы 1–5): вес 199 по собранному PDF одиннадцати правленых кадров (parts-sec/krug285.pdf, pymupdf постранично) + запас 4. Не оценка по файлу кадра: мера берётся с вывода, а не со входа (storozha-i-priyomka.md §11).
timing_min: 0.75
in_bucket: true
method_steps: ["вывод раздела"]
form: ["форма 4", "форма 3", "форма 5", "форма 7"]
vfy: false
status: собран
---

## Visible slide text

**You can go wrong in three places without the model itself being wrong:** a device measures the input, a human assembles the dataset, a variable sets the target.

**Autonomy is decided by the cost of a false alarm, not the quality of the model.**

**Where the model stands.** *Image classification* — fundus, skin lesion. *Image recognition* — triaging the stream on X-ray and CT. *Forecasting on structured data* — a risk score in the chart. *Measurement · device signal* — **no model, and still bias.**

**Of the six distortions named at the opening, this section ran into none: the stream is read by the model alone.**

## Speaker notes

The outcome of this stage: the reading itself failed once out of five. In three breakdowns, what let things down was the setting, the composition of the training set, and the definition of the target — that is, it was possible to go wrong without the model itself being wrong. The benefit here is real and measurable, and a specialist will take it: consistency of reading and relief for the stream. The system reads the ten-thousandth image like the first, and resolving a discrepancy gains a reproducible side — you can ask the machine again, you cannot ask yesterday's version of yourself.

There is one boundary, and it is the same one the section opened with. Shares are computed on a group, and the meaning of the output changes along with the group. The same "sick" signal means different things in a general-population stream and in a specialized department, and the gap between them is nearly tenfold — eight out of a hundred against seventy-nine.

Let's state the risk so it sticks. A device measures the input. A human assembles the dataset. A variable sets the target. You can go wrong in three places without the model itself being wrong — and three breakdowns in this section are exactly that: in fundus reading, the deployment failed; in skin assessment, the composition of the training set; in program selection, the definition of the target. In none of these three did the reading itself fail, and what got confirmed instead was that nobody measured the setting for the model, the data for it, or its target before deployment.

And the two domestic breakdowns add something the first three do not have. In the intracranial-hemorrhage task, the model alone produced 293 false alarms against four from the physician on the same 3,409 scans, and missed forty-five hemorrhages: here the reading itself failed. And right next to it — the same city, the same circle of products, the preventive stream, where that same generosity with alarms turned out to be a benefit: a human stopped reading more than half the images, and that saved 33 million rubles over five months. From the same property of the model, one task got permission to work without a human, and the other got a ban on it. What tells them apart is the cost of a false alarm and whether there is time: on the preventive stream, a false alarm costs one follow-up exam; on the emergency path, it costs a deployed crew, and there is no time to check it. This is exactly what an engineer should take from this section, instead of the question "is the model good."

What happened to the work. The workload grew in the same place: the primary-care technician gained the job of obtaining a gradable image, which the ophthalmologist never had, because he compensated for the imaging conditions himself. A step appeared: a repeat visit for anyone whose image did not pass. The performer changed: program selection used to be done by the treating physician, now a single score does it. And the cost of an error shifted — twice, by two different mechanisms: in the skin breakdown it was shifted by the composition of the training data, in the selection breakdown by the choice of the target variable.

What holds this workload up. A trigger threshold, set against the cost of both errors by the protocol, not by the developer. Measurement quality control — a procedure written in the room's own instructions. And recomputing a share for one's own prevalence before applying someone else's number at home. There is one dash here, and it is set in bold not for decoration: nobody checks the system's target. None of the three procedures asks what exactly the algorithm treats as its target — and in the third breakdown that is exactly what let things down.

And one encouraging observation worth stating, because otherwise this section reads as hopeless. The one fix actually measured in this section came from data composition: fine-tuning on a representative set closed the skin-tone gap, and even flipped it, while three named algorithmic bias-correction methods did not shrink it significantly. This is the part of the work that genuinely sits in an engineer's hands — not the choice of method, but collection and labeling.

Now about the cells of the course's own grid occupied by this stage — there are four, and the fourth is the most interesting. Image classification: autonomous fundus reading and skin-lesion assessment, and both classes of devices bypass the specialist and both only produce a "show to a physician or not" triage. Image recognition: detection and triage of the stream on X-ray and CT — this is what the platforms from the country-by-country overview are doing. Forecasting on structured data: a risk score inside the medical chart, bought by an administrator or a payer, meaning the decision of who gets taken under watch is made wherever the money is counted. And the fourth cell — measurement and device signal — is occupied with no trained model at all: the blood-saturation device's bias arrives before any model does. The full grid will come together in the summary, across all sections at once.

Further down the cycle, everything this section read lands with a human who will make the decision and sign for it. What happens to that human is the subject of the next section.

So three out of five failed, and in the fourth place — the reading itself — the fifth one failed.
