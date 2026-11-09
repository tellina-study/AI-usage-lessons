---
id: s36
local_id: s3-02
section: "3. Постановка диагноза"
type: norm
title: "Diagnosis: the stage's seven steps, and the three where the model operates"
assertion: "Стадия постановки диагноза состоит из семи действий — собрать данные, выписать список объясняющих болезней, назначить различающую проверку, вычеркнуть опровергнутое, прочесть вторым независимо, разрешить расхождение третьим, подписать заключение, — и без обученной модели каждое из семи делает человек по записанному правилу"
source: "Singh et al., BMJ Quality & Safety 2014 — https://doi.org/10.1136/bmjqs-2013-002627"
media: "rework/deck/assets/s35a-priem-vrach-slushaet-rasskaz.jpg"
media_needed: "реальный снимок рабочего места, где составляют список: кабинет приёма с экраном карты. Кадра нет, нужен поиск; запасной вариант — собственная схема сужения списка"
media_note: "основной адрес этого файла — здесь (решение 2026-10-14): на снимке врач слушает рассказ пациента, за ним второй врач, в камеру никто не смотрит и не улыбается — ровно то, чего поле требовало. Экрана карты в кадре нет; выдавать снимок за «рабочее место, где составляют список», нельзя. Имя файла начинается с s35a и не переименовано намеренно — на него ссылаются .url и реестр. Права — assets/s35a-priem-vrach-slushaet-rasskaz.url"
blocks:
  - {label: "Frequency of diagnostic error: adult outpatient visits", value: "5.08 out of a hundred visits", note: "identified via a trigger — an unusual patient return, an abnormal result with no follow-up workup; so only part of the errors is counted; the share itself was extrapolated to the US adult population; the authors call this an underestimate: the true frequency may be noticeably higher than five percent", key: true}
opyt_net: "заземление стадии: собственного замера за 5,08 приёма из ста нет вовсе — это экстраполяция на взрослое население США, сведённая из трёх ретроспективных работ, а способ выявления триггером назван подписью плашки. Размеров тех трёх выборок в нашем материале нет. Своего замера у стадии нет; измеренные опыты раздела — s41, s44, s47, s49b"
scheme:
  caption: "How the list narrows: the stage right after the workup"
  arrows: true
  rows:
    - {label: "The workflow", steps: ["gather the data", "list candidate diseases", "order a differentiating test", "cross out what's ruled out"]}
    - {label: "Occupied by the model", steps: ["composing the list", "the second reading", "the sign-off"], arrows: false}
timing_min: 0.85
in_bucket: false
method_steps: ["заземление"]
form: []
vizforma: "ряды"
pol_slov: 130   # О20 (#229): объявлен ВПЕРВЫЕ по п. 33 владельца, по собранному PDF. Тело 13,5 пт — замерено: 51 слово прозы давало 11,0 пт, 44 держат 13,5. Вес кадра почти весь в обязательной оговорке плашки о частоте врачебной ошибки — решение О21.
# «ДОКИНУТЬ СТАДИЮ ИССЛЕДОВАНИЯ» (п. 33) исполнено подписью схемы: «как сужается список: стадия сразу за исследованием». После слияния разделов 2 и 3 саму стадию исследования несёт s22a со своими шестью действиями, поэтому дублировать её здесь значило бы сказать одно дважды через четыре кадра; на этом кадре нужен был МОСТ, и он стоит (§5.22).
# «РАСКРЫТЬ, КАК И НА КАКИХ ЭТАПАХ РАБОТАЕТ ИИ» (п. 33) — встала строка «модель стоит на трёх из семи действий: состав списка, второе чтение, подпись», и каждое из трёх дальше разбирается своим кадром: состав списка — s38, второе чтение — s37, подпись — весь раздел. Прежде кадр называл только добавленное действие («решить, верить ли подсказке») и не называл занятых.
# ЧАСТОТА ВРАЧЕБНОЙ ОШИБКИ (решение О21) стоит плашкой с полной оговоркой: выявление триггером, перенос доли на население, собственное признание авторов о занижении. Кадр s35a снят владельцем (п. 32), и число пришло сюда — ровно как предлагал оркестратор, чтобы снять устройство кадра, а не требование.
# КАРТИНА РАБОТЫ сохранена и сжата: один приём с тремя жалобами и четырьмя болезнями — это та «одна картина работы», которой CLAUDE.md требует вместо перечня шагов; перечень действий стоит схемой, а не прозой.
vfy: false
status: собран
---

## Visible slide text

**One visit:** a cough for three weeks, an evening fever, a four-kilogram weight loss. Of four candidate diseases, the X-ray and blood test ruled out two — two remained, indistinguishable on the image.

**The model occupies three of the seven steps:** composing the list, the second reading, the sign-off. **And it added one — deciding whether to trust the suggestion.**

## Speaker notes

The stage has been named, and now step by step. It has seven steps: gather the data, list the diseases that could explain it, order a differentiating test, cross out what's been ruled out, have a second independent reading, resolve any disagreement with a third reader, sign the report. The diagram shows the first four — the ones that narrow the list; the fifth, sixth, and seventh come after it and are covered on the next slide. Here is what matters about each of the seven.

Gather the data. Complaints, the physical exam, whatever was already measured at the previous stage. That is everything the physician has going in.

List the candidates. Diseases that could explain what's observed: prolonged bronchitis comes first as the common cause, tuberculosis because the picture is classic and missing it is costly, lymphoma because the same two signs can be read differently, an autoimmune condition less often, but it still belongs on the list.

Order a differentiating test. The X-ray and the blood test come first for a reason: start with what's cheap and rules out a lot. The clinical version of hypothesis elimination is harsher than the engineering one in one respect — some tests are themselves risky or expensive, so the order of testing becomes a separate decision that has to be justified.

Cross out what's ruled out. Bronchitis is ruled out by the image: bronchitis doesn't produce changes in the upper lobe. The autoimmune condition is ruled out by calm inflammatory markers. Two diagnoses remain that the image can't distinguish, and a sputum culture decides between them — three weeks of waiting, part of the price the patient pays.

Have a second, independent reading. A second opinion is a report on the same case made by someone who hasn't seen the first one; the whole point of that definition rests on the second half.

Resolve the disagreement. A third reader sees both reports and steps in only where the two disagreed.

Sign the report. The signature is the point where responsibility becomes attached to a name.

Picking the wrong item off the list is an error that gets noticed: a test result comes back and doesn't match expectations. Failing to put on the list something that should have been there is an error that leaves no trace: no one orders a test for it, the case leaves with a different diagnosis, and it comes back a year later.

And the same field with the model, named before the case studies. Of the seven steps, the trained model occupies three. The second — the suggestion edits the composition of the list, adding a line a tired physician wouldn't have come up with, or dropping one that should have been there. The fifth — it becomes the second, independent reader. The seventh — the sign-off, and at the fourth rung of involvement it's given without looking. One step gets added — deciding whether to trust the suggestion — and the physician never had that operation before at all. Three places where it doesn't work are named for what breaks: independence — the suggestion is visible before the physician's own conclusion forms, and the model's error is the same for every reader, so it doubles instead of averaging out; selectivity — not a single group managed to disbelieve the suggestion exactly where the model was wrong; explainability — a simplified explanation of an incorrect recommendation drops the result below working without a model at all.

A question for the room, while the list is on screen. Which of your own hypotheses have you failed to write down — and how did you find out it was missing? We're after a short answer, one sentence: most often you find out the same way as in the clinic — a result comes back that no one expected, because you don't order a test for something that was never written down. Someone will mention an incident review, someone else a debugging session where the cause turned out to be outside the list under consideration. It's the same mechanism, and it's needed here so the second row of the diagram reads not as an improvement but as a shift in where the error sits: the model edits the composition of the list — that is, it intervenes in exactly the step whose failure leaves no trace.

And one last thing worth pausing on in the second row of the diagram. Of the seven steps, the trained model occupies three — composing the list, the second reading, the sign-off — and it added a fourth on its own: deciding whether to trust the suggestion. The physician never had that operation before, no one is trained for it, and the visit norms set aside no time for it. The rest of the section measures exactly this: how a person's attempt to tell a correct suggestion from an incorrect one turns out. Three places where it doesn't work are named for what breaks. Independence — the suggestion is visible before the physician's own conclusion forms, and the model's error is the same for every reader, so it doubles instead of averaging out. Selectivity — not a single group we'll examine managed to disbelieve the suggestion exactly where the model was wrong. Explainability — a simplified explanation of an incorrect recommendation drops the result below working without a model at all.
