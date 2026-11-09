---
id: s37
local_id: s3-03
section: "3. Постановка диагноза"
type: norm
title: "A second opinion: what holds it up, and when it stops being second"
assertion: "Второе мнение держится на независимости двух чтений и на третьем, который разбирает расхождение; когда вывод модели стоит на экране до того, как человек составил своё мнение, независимости нет по построению, и цена этого измерена — 8,9 пункта по решениям к действию"
source: "Goh et al., a continuation of the same trial — https://doi.org/10.1001/jamanetworkopen.2024.40969"
media: ""
media_needed: "собственная схема: два чтения с перегородкой между ними и третий арбитр, к которому идёт только расхождение"
media_note: "—"
scheme:
  caption: "Two opinions: when they're independent, and when they no longer are"
  arrows: true
  rows:
    - {label: "Independent", steps: ["the first reading", "the second doesn't see the first", "disagreement — a third decides"]}
    - {label: "No longer", steps: ["the suggestion is on screen", "one reading on top of it", "nothing left to disagree with"]}
pol_slov: 123   # О20 (#229): объявлен ВПЕРВЫЕ по п. 34 владельца, по собранному PDF. Было 75 слов, стало 123; тело 15,0 пт — выше пола на три пункта.
# СХЕМА ПЕРЕДЕЛАНА (п. 34, «важный, но нечитаемый; переделать схему»): прежние два ряда были «два чтения» и «разошлись» — то есть один и тот же порядок, разрезанный на две строки, и сломанного случая на кадре не было вовсе. Теперь ряды противопоставлены: «независимо» и «уже нет», и §5.12 («сопоставление без ИИ / с ИИ читается с одного взгляда») выполняется буквально.
# РЕАЛЬНАЯ МЕТРИКА ВСТАЛА (п. 34, «дать реальные метрики, в идеале не из примеров дальше»): 8,9 пункта за порядок предъявления подсказки, 70 врачей, 254 случая. Это прямой замер того самого механизма, которым держится кадр, и он НЕ из семи разборов раздела — отдельная работа той же команды. Прежде это число стояло на видимом слое s49b, где к разбору хирургов отношения не имело; здесь оно на своём месте, и дважды дека его больше не говорит.
# ЖЕНЩИНА С ПИСЬМОМ ЗАМЕНЕНА ЭТОЙ МЕТРИКОЙ — дословное требование владельца («женщину заменить на эти метрики»). Строка «Снимок женщины с письмом прочтёт тот, у кого подсказка на экране» снята: линия женщины идёт через всю лекцию и держится другими кадрами, а здесь она занимала место измеренного числа.
timing_min: 0.6
in_bucket: false
method_steps: ["заземление"]
form: ["вопрос залу"]
vizforma: "ряды"
vfy: false
status: собран
---

## Visible slide text

**Held up by independence:** the second reader is denied access to the first report, and a third reader resolves any disagreement.

**A second opinion from the model that suggested the first one is no longer a second opinion:** the error is shared, and it doubles instead of averaging out.

**The order of presentation has been measured.** A suggestion shown before the person formed their own opinion, versus a suggestion shown after — **8.9 points** in decisions to act. *70 physicians, 254 cases.*

**Which of you has asked a model for a second opinion on a decision you'd already made yourself? What did you do when it disagreed?**

## Speaker notes

A second opinion is a report on the same case made by someone who hasn't seen the first one. The whole weight of that definition rests on the second half.

The mechanism exists because a single reading misses things, and it misses them for any reader: attention is limited, the image is large, a sign can be small and sit where it wasn't expected. What makes a second opinion useful is a single observation: the two readers' misses don't coincide. The first missed a density because they were distracted by calcifications in the center; the second was distracted by something else. If both systematically failed to see the same thing, a second reader would add nothing but cost. The gain from double reading comes from the mismatch between errors and nothing else — it doesn't double the strength of the first reader.

Independence is built by the organization's own hands: a separate reading queue, a hidden report field, sometimes a separate shift or institution. It doesn't rely on a reader's diligence. There's exactly one checkable sign — could the second reader physically have seen the first report at the moment of reading; access rights give the answer, and a written policy is not proof here. The partition costs money, and it's the first thing cut when someone looks for savings. Formal independence looks the same and works differently: the rate of disagreement falls, and management reads that as growing consistency.

Arbitration is a third reader who sees both reports and steps in where the first two didn't match. Their workload is set by the number of disagreements, meaning it can be estimated in advance and is governed by a threshold. A case conference works differently: several specialists discuss a case while seeing each other's opinions, and independence is deliberately given up there — the value lies in exchanging arguments. That's why the screening stream is never read by case conference.

The model's suggestion breaks independence from two sides. It's visible before the person's own opinion has formed. And it's the same for every reader: the trained system's miss is identical for everyone, so its error doubles across two readers rather than averaging out; the averaging that a second reader was set up to achieve never happens. From this comes the conclusion the section rests on: "add a second opinion from the model" and "add a second physician" are different changes to the process, even though they look like the same block on a diagram.

And one measurement the lecture doesn't take on board — named out loud, because otherwise you can't see how its own rule works. On anchoring in the reverse direction — that is, on how a physician's text moves the machine — there's a figure: the model's agreement with the physician's reasoning fed into it rises from 65.8 to 93.5 percent. On its subject, this figure is precious — it strikes right at the independence of the second opinion from the machine's side — but it's measured in a preprint where there are zero live physicians: the physician reasoning in it is simulated by other models. A lecture that treats strength of evidence as its own rule doesn't say that number from the stage: it's more honest here to say there's no measurement.

For the woman with the letter, the partition between the two readers is exactly what her program rests on: the gain from double reading comes from the mismatch between two people's errors, and that mismatch only occurs between people who haven't seen each other's work. Both readers see the model's suggestion, and the partition stops being a property of the procedure: both readers are now answering the question "do I agree," and that's a different task with a different error rate. Arbitration by a third reader still happens, but now it has to resolve a disagreement between two opinions that shared a common source.

And one check on this diagram. The partition in it isn't a rule of conduct but a mechanism: there's exactly one checkable sign — could the second reader physically have seen the first report at the moment of reading. Access rights give the answer, and a written policy is not proof here. That's why "add a second opinion from the model" and "add a second physician" are two different changes to the process, even though they're drawn as one block on the diagram.
