---
id: s73g
local_id: s5-05
section: "5. Профессиональная квалификация: поддержание и износ"
type: case
title: "Example 3: ArtInCol, Russia — an assistant on the same procedure"   # был «Пример 2» — перенумерован под новый порядок раздела (#293, Этап B): разбор на разработчиках встал первым
assertion: "Многоцентровое рандомизированное испытание в России меряет ту же величину на той же процедуре и даёт прирост 413 → 472 процедуры с находкой из тысячи; оно сильнее польского по разряду свидетельства, называет и вход, и выход, и обучающий архив, и ложные срабатывания — и при этом периода наблюдения после снятия помощника у него нет, что авторы говорят сами"
source: "Achkasov S.I., Shelygin Yu.A. et al. Efficacy of the ArtInCol artificial-intelligence system in the diagnosis of neoplasms during colonoscopy: results of a multicenter randomized study. Koloproktologiya, 2025; 24(3):12–21 — https://doi.org/10.33878/2073-7556-2025-24-3-12-21"
media: ""
media_needed: "реальный снимок рабочего места эндоскописта с подключённым отечественным ИИ-ассистентом либо рисунок 1 из публикации (рамка детекции на мониторе); права на рисунок из «Колопроктологии» не проверены — до проверки кадр держат схема и плашки"
media_note: "иллюстрация НЕ поставлена, и причина названа честно, а не спрятана: рисунок 1 публикации (рамка детекции на мониторе) — ровно то, чего просит поле, но лицензия журнала «Колопроктология» на переработку рисунка не проверена, а выдавать за него кадр из чужой зарубежной работы нельзя — именно это и есть подмена, которую лекция разбирает у других. Снимок с рамкой того же класса уже стоит на s73d, и ставить второй такой же рядом незачем. Эскалация по §11.4: если владелец считает иллюстрацию обязательной, нужно решение — запрашивать права у журнала или снимать рабочее место эндоскописта самим"
scheme:
  caption: "Where the system sits in the workflow"
  arrows: true
  rows:
    - {label: "Mechanics", steps: ["video stream from the scope", "a computer by the cart", {text: "a box on the monitor", ai: true}]}
    - {label: "Trained on", steps: ["the archive of the National Medical Research Center of Coloproctology", "annotation by its own endoscopists"]}
blocks:
  - {label: "Without the assistant", value: "413 procedures with a finding per 1,000", note: "547 patients"}
  - {label: "With the Russian assistant", value: "472 procedures per 1,000", note: "581 patients", key: true}
  - {label: "What the trial lacks", value: "a measurement after the assistant is removed"}
pol_slov: 165   # ПЕРЕОБЪЯВЛЕН вторично, круг 2 (#285), со 150: глава закрыла четвёртый шаг формы разбора у §10.5а, и форма словаря обязана быть НАЗВАНА на кадре, а не лежать в поле фронтматтера. Поставлены обе: «сменился исполнитель» (часть поиска делает допущенное устройство) и «нагрузка выросла на том же месте» (1,23 ложного срабатывания там, где их ноль). Довод против формы «шаг появился» — время осмотра замерено и не изменилось — уведён в заметки, на кадре ему места нет. Высоту под это дала схема: подпись и первый шаг укорочены, бокс стал ниже. Замер по PDF: 164 слова. ПРЕЖНЯЯ ПРИЧИНА ПОЛА (со 138): добавлена строка названного пробела по России (§3 состояние 2): внедрение крупнейшее в мире по заявленным числам — и замера последствий нет. Обе половины обязаны стоять на кадре вместе, иначе строка читается либо похвальбой, либо попрёком. Плюс страна названа СТРАНОЙ вместо «Москвы и Уфы» и «отечественного» (замер круга 1: слово «Росси*» встречалось в видимом слое всех восьми страниц раздела ровно один раз, в подвале источника). Цена рамки переехала с тела на плашку по §5.12 («ключевое число вне абзаца»). Замер по PDF: 148 слов. ПРЕЖНЯЯ ПРИЧИНА ПОЛА: НОВЫЙ КАДР 2026-10-19 (раздел 5, прожарка под канон #285). Заведён по §1.7 (≥2 российских кейса в разделе с подробным разбором) — в разделе их было НОЛЬ, а глава закрывала это одной фразой «отечественных измерений нет тоже», которая по этому предмету неверна: измерение есть, оно рандомизированное и в той же единице. Все числа сверены ПО ПЕРВОИСТОЧНИКУ (PDF журнала «Колопроктология», DOI 10.33878/2073-7556-2025-24-3-12-21), не по пересказу в прессе: ADR 47,2% (95% ДИ 43,1–51,2) против 41,3% (95% ДИ 37,3–45,5), величина эффекта 5,9%, p = 0,048; среднее число аденом 0,97 (0,85–1,09) против 0,79 (0,67–0,92), p = 0,01; 1 128 пациентов, 4 учреждения, август–декабрь 2024; РУ № РЗН 2024/23409; ложные срабатывания 1,23 на исследование (35 случайно отобранных колоноскопий, срабатывание = рамка не короче 3 секунд); время осмотра на выходе 9 (7;12) против 8 (7;11) минут, p = 0,54. Доли переведены в «процедуры из тысячи» единой единицей раздела (§5.19/§12): 413 → 472. Ограничения взяты из раздела ограничений самой статьи, а не домыслены: нет ослепления, нет периода наблюдения, исключены 1 центр и 5 эндоскопистов за нарушение критериев включения, оборудование экспертного класса. Кадр закрывает и §2 «инженерной глубины»: вход, выход, обучающий архив, порог и ложные срабатывания — всё названо, чего у польского разбора нет вовсе
timing_min: 1
in_bucket: true
method_steps: ["③модель против них", "④как это устроено", "⑤что переехало"]
form: ["форма 5", "форма 4"]
vfy: true
status: собран
---
## Visible slide text
**What was done.** At four institutions in Russia — Moscow and Ufa — 1,128 patients were split by lottery: colonoscopy as usual, and with a Russian assistant that boxes a region.

**Two glossary forms.** The performer changed: part of the search is done by the authorized device. The load grew at the same spot: 1.23 false alarms per study where there used to be zero — that many times the physician looks at an empty spot.

**The Russian deployment is the largest in the world by claimed numbers, yet there is no measurement of the consequences:** the physician was not measured here after the assistant was removed.

## Speaker notes

Four institutions in Russia — Moscow and Ufa: 1,128 patients were split by lottery between ordinary colonoscopy and colonoscopy with the Russian assistant ArtInCol, which boxes a region on video. Procedures with a finding became 472 per 1,000, against 413.

This trial measures the same quantity on the same procedure as the Polish study, and is built more strongly: multicenter, randomized. Its result does not cancel out or replicate the Polish finding: they measure different things.

Composition. August–December 2024, four medical institutions: the Ryzhikh National Medical Research Center of Coloproctology, Botkin Hospital, Pirogov Russian National Research Medical University in Moscow, and the Republican Clinical Oncology Dispensary in Ufa. 1,128 patients, split by lottery: 547 for colonoscopy without the assistant, and 581 with it.

The result, in the same unit the whole section counts in. Procedures with a finding became 472 per 1,000 against 413 — that is, the adenoma detection rate was 47.2 percent against 41.3, effect size 5.9 percent at significance 0.048. The mean number of adenomas found per procedure was 0.97 against 0.79, and this difference is more robust than the main one: significance 0.01.

Now something the Polish breakdown lacked entirely, and the reason this slide is especially needed for an engineering audience: the mechanics is named in full. The system is vendor-neutral, carries a Roszdravnadzor registration certificate, and connects to standard endoscopic equipment. Input is the video stream during the procedure, which goes to a compact industrial computer next to the cart. Output is a detection box on the monitor, in real time, on areas where the probability of a growth is high. It is trained on the coloproctology center's own archives, annotated by the endoscopists of its own endoscopic diagnostics and surgery department. Before refinement, the prototype gave an accuracy of 83.2 percent and a sensitivity of 77.2 on the test set.

And the cost of attention, stated as a number — something most publications don't even look for. The mean number of false alarms came to 1.23 per study. This was measured on thirty-five randomly selected colonoscopies, and an alarm was counted as a box appearing for no less than three seconds. More than once per procedure, the physician shifts attention to a spot where there's nothing. This is the answer to the question the room asks about its own work: a model deployed in an acceptance loop always has a figure like this, and if the vendor doesn't name it, it wasn't measured.

The limitations are named from the article itself, not invented. There was no blinding in the study: the endoscopists knew they were working with the assistant and that their results were being compared, and the authors explicitly name this a possible source of bias. One center and five endoscopists from different institutions were excluded from the final analysis for protocol violations — inflating the inclusion criteria and, as a result, abnormally high detection rates. The equipment was expert-grade, the staff were trained, and the authors separately note that in resource-limited regions, deployment will run into a shortage of technical support and trained staff.

And for this section's axis — a gap, named exactly where it is. The trial has no observation period: the authors say so themselves, in a separate line in the limitations. That is, the Russian study measured exactly half the pair — what the assistant gives while it's on — and did not measure the other half: what becomes of the same physicians when it's switched off. The Polish study measured exactly that second half, and was weaker in strength of evidence. There is no clinical study anywhere, in Russia or elsewhere, that has measured both halves on one sample; the second half has only been measured by lottery in the developer study the section opened with — and that measurement is not clinical. This is the honest answer to the question "what about us": the gain is measured better than theirs, and the drain is not measured at all.

And the slide's line about the country has to be said in both halves, or it comes out as either boasting or reproach. First: the radiological AI project deployed in Russia is the largest in the world by claimed numbers. Second: we looked for a measurement of what this deployment did to physicians' skill — through deployment-program publications, specialty journals, and operational reports — and found not a single one. Scale of deployment and scale of measuring its consequences are two different things, and the first says nothing about the second.

And one remark about withdrawal time, because it closes the second objection to the Polish study. Here this quantity was measured: a median of nine minutes against eight, a difference that is not significant. That is, in the Russian trial the gain is not explained by withdrawing the scope more slowly with the assistant. The Polish study had no such measurement, and that is exactly why its finding cannot be checked all the way through.

And the last step of the breakdown — what moved. There are two forms here, and both have to be stated.

The performer changed: part of the search at this spot is now done by an authorized device — a Roszdravnadzor certificate, a video stream in, the system itself marking areas out. This is the case the glossary sets apart from the Polish study and keeps for the loop's switched-on state. The form's tally: 413 procedures with a finding per 1,000 against 472.

And the load grew at the same spot: every cue costs seconds of attention to the same physician at the same workplace, and the seconds are counted — 1.23 false alarms per study where there are zero without the system.

Why it's not "a step appeared" here, even though that form suggests itself first. A new step would have had its own cost in time: where that cost has been counted in the lecture, arbitration cost two minutes twelve seconds against forty-eight seconds of reading. Here, examination time was measured and did not change — a median of nine minutes against eight, no significance. So the box lands inside a step that already exists, without creating a new operation. The form was rejected by the measurement, and it's worth saying that to the room directly.

**Sources.** [Achkasov, Shelygin et al., Koloproktologiya 2025; 24(3):12–21](https://doi.org/10.33878/2073-7556-2025-24-3-12-21)
