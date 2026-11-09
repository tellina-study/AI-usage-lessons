---
# ПЕРЕЕХАЛ ВПЕРЁД И СТАЛ ПЕРВЫМ РАЗБОРОМ РАЗДЕЛА, Этап B прожарки сторителлинга (#293, П3).
# Был `s73ga`, стоял предпоследним разбором — между ArtInCol и сводом режимов. Прожарка §2.3 и
# П3 назвали это дефектом порядка, а не состава: «Раздел 5: начать с s73ga (разработчики,
# 52 инженера) — „это про вас“ как вход, зеркалом; потом врачи. Сильнейший ход раздела сейчас
# стоит предпоследним». Содержание разбора не менялось: те же числа, тот же разряд, тот же
# отказ присвоить форму словаря. Менялись три вещи — место, мосты и нумерация примеров.
#
# НОМЕР ВЫБРАН ПРОВЕРКОЙ СОРТИРОВКИ, А НЕ НА ГЛАЗ. Место кадра нужно было между `s73ca` и
# `s73d`, то есть хвост имени обязан лежать строго между `ca` и `d`. Вставка-подномер Этапа A
# (`s01` → `s01_1` → `s01a`) здесь НЕ РАБОТАЕТ: `deckkit.slidefile._ORDER` читает подномер
# только СРАЗУ за цифрами (`^s(\d+)(?:_(\d+))?([a-z]*)`), поэтому `s73ca_1` разобрался бы как
# `(73, 'ca', 0)` — тот же ключ, что у `s73ca`, то есть молчаливое совпадение двух кадров на
# одном месте. Взят буквенный хвост `cb`: `ca` < `cb` < `d`, проверено на самом `order_key`.
# `s73cb` свободен и в `slides/`, и в `_snyato/` — ни один снятый номер не переиспользован
# (занято снятыми: `s73a`, `s73e`, `s73g` прежней редакции, `s73h`, `s73ha`, `s73`).
#
# НУМЕРАЦИЯ ПРИМЕРОВ РАЗДЕЛА ПЕРЕСОБРАНА ПОД НОВЫЙ ПОРЯДОК (сплошным проходом, не по памяти):
# разработчики — Пример 1 (был 3), доля без помощника в Польше — Пример 2 (была 1), ArtInCol —
# Пример 3 (был 2). Дивайдер `s73b` перечисляет их в новом порядке и дословно новыми
# заголовками (§5.16).
#
# МОСТЫ ПЕРЕПИСАНЫ, И ЭТО ГЛАВНАЯ ПРАВКА СОДЕРЖАНИЯ. Прежний кадр печатал «Вторую половину
# пары измерили жребием — чего нет у соседних разборов»: формулировка верна только тогда,
# когда соседние разборы ЗАЛУ УЖЕ ПОКАЗАНЫ. Став первым, кадр обещает вперёд, а не
# оглядывается: сказано, что у двух врачебных разборов дальше так эту половину не измерит ни
# один, — то есть зал получает мерку прежде, чем ею мерить. Это же и причина ставить случай
# первым: он задаёт разряд свидетельства, которым дальше читаются оба клинических разбора.
#
# ЗАМЕНЁН ЗАПРЕЩЁННЫЙ ОБОРОТ. Прежние `assertion` и заметки называли способ обращения с
# помощником «рычагом» — слово из §6.3 списка протечек рабочего языка, запрещённое в ОБОИХ
# слоях, видимом и заметках. Написано то, что оно значило: способ обращения с помощником, и
# что именно он решает.
#
# МАТЕРИАЛ НЕ ДОБЫВАЛСЯ ЭТОЙ СЕССИЕЙ — он сверен оркестратором и лежит в
# `rework/krug2/SVERENNYE-CHISLA.md` §2; все числа взяты оттуда дословно, своего веб-поиска не
# велось.
#
# ФОРМА СЛОВАРЯ НЕ ПРИСВОЕНА, И ЭТО НАЗВАННЫЙ ОТКАЗ С ПРИЧИНОЙ (§4 шаг 5 допускает такой
# исход наравне с присвоением). Восьмая форма — «исполнитель тот же, но стал хуже» — здесь
# не подходит: у польской работы сравнение построено ВНУТРИ тех же девятнадцати врачей, а
# тут сравниваются две разные группы, и мерится не падение у работавшего, а то, что у
# входящего в работу навык не сложился. Такой графы словарь не ведёт, и дописывать её ради
# зачёта нельзя. Счёт форм на s97 этот кадр поэтому НЕ меняет — проверено.
#
# ПРАВИЛО 3+6: подробных разборов в разделе ровно три (разработчики · Польша · ArtInCol) —
# предел, не больше. Упоминаний с числом на кадре одно — цитология Великобритании, и она
# здесь намеренно: это альтернативный инструмент БЕЗ всякой модели, снявший навык той же
# механикой, и вывод из него несущий для раздела. Став первым, кадр подаёт этот вывод как
# рамку для двух следующих разборов, а не как оговорку в конце.
id: s73cb
local_id: s5-02c
section: "5. Профессиональная квалификация: поддержание и износ"
type: case
title: "Example 1: developers on an unfamiliar library"
assertion: "Пятьдесят два инженера распределили жребием: половина писала с ИИ-помощником, половина руками, и сразу после работы всех проверяли без него — 50 верных из ста против 67, размер эффекта 0,738 при значимости 0,01; выигрыша по времени нет, разрыв шире на заданиях «найди ошибку», а способ обращения с помощником назван и измерен: кто спрашивал только про понятия, держался выше 65 из ста, кто отдавал задачу помощнику целиком — ниже 40"
source: "Shen and Tamkin, arXiv:2601.20245, 2026 — https://arxiv.org/abs/2601.20245 · Heudel et al., ESMO Real World Data and Digital Oncology 2026 — https://doi.org/10.1016/j.esmorw.2026.100693"
media: ""
media_needed: "иллюстрация не нужна структурно: предмет кадра — устройство сравнения двух групп, и оно на кадре схемой"
media_note: "иллюстрация не поставлена, и причина названа прямо. У работы нет ни одного снимка, который показывал бы предмет: это опыт на людях, пишущих код, и единственный «снимок» такого опыта — экран редактора, то есть иллюстрация-подделка, а не свидетельство. Снимок рабочего места разработчика из стока показал бы то, что зал видит каждый день, и не сказал бы ничего о замере. По правилу «слабую картинку лучше не ставить вовсе» кадр держат схема сравнения и полоса плашек"
scheme:
  caption: "What was compared with what"
  arrows: true
  rows:
    - {label: "Half by lottery", steps: ["a task on an unfamiliar library", {text: "the assistant alongside", ai: true}, "tested without it"]}
    - {label: "The other half", steps: ["the same task", "documentation and working it out themselves", "the same test"]}
blocks:
  - {label: "Wrote by hand: correct on the test", value: "67 out of 100", note: "the gap is wider on \"find the bug\" tasks"}
  - {label: "With the assistant: the same test", value: "50 out of 100", note: "effect size 0.738, significance 0.01; no gain in time", key: true}
  - {label: "Asked only about concepts", value: "above 65 out of 100", note: "7 people; those who handed the task over whole — four of them — below 40 out of 100"}
pol_slov: 225   # ОБЪЯВЛЕН ЗАНОВО (#293, Этап B): кадр переехал первым разбором раздела и получил мост с кадров стадии, а оглядка на соседние разборы заменена обещанием вперёд. 221 слово замером по собранному PDF + запас 4. ПРЕЖНЯЯ ПРИЧИНА ПОЛА: НОВЫЙ КАДР, разбор. Замер по собранному PDF: 200 слов — схема сравнения, три плашки, состав опыта и упоминание цитологии. Пол объявлен под четыре слагаемых, и каждое стоит на кадре потому, что без него разбор перестаёт быть разбором. (1) Состав опыта — кто и сколько, что делали, чем мерили: это три части описания опыта, которые прогон `zamer_opisaniya_opyta.py` считает отдельно, и уводить их в заметки значит сдать кадр без того, чем он доказывает. (2) Разряд свидетельства словом «жребием» — у двух следующих разборов он другой, и без него зал не поймёт, зачем случай стоит первым. (3) Способ обращения с помощником тремя числами — ради него случай и взят: он единственный в разделе называет не только расход, но и как его не платить. (4) Ограничения самих авторов — §2.3 требует нюанс, меняющий надёжность показателя, ВИДИМОЙ строкой, не в заметках. Веса и кегля здесь нет нарочно: их печатает прогон на любой момент, а записанные прозой они устаревают молча
timing_min: 1.1
in_bucket: true
method_steps: ["②классические режимы", "③модель против них", "④как это устроено", "⑤что переехало"]
form: ["—"]
vfy: true
status: собран
---

## Visible slide text
**Skill is spent in silence — and so is skill that hasn't formed yet.** What was done: 52 participants — junior engineers unfamiliar with an asynchronous-programming library — were split by lottery: half with the assistant, half by hand. Everyone was tested without the assistant.

**The subject being measured here is programming, not medicine.** The second half of the pair — the result without the assistant — is measured by lottery: neither of the two physician breakdowns that follow will measure it this way.

**What is measured here is a skill that never formed:** nobody knew the library, so there is nowhere for erosion to come from; the glossary has no form for a case like this.

**The same drain happens with no model at all.** In UK cytology, the volume of reading dropped 80–85 out of 100 after the switch to human papillomavirus testing, and the number of centers fell to 8 out of 45. **It is the handed-off volume of work that drains skill, not the model.**

## Speaker notes

Fifty-two junior engineers, unfamiliar with an asynchronous-programming library, were split by lottery: half wrote code with an AI assistant, half by hand. Right after the work, everyone was tested with no assistant. Those who had written with the assistant got 50 correct tasks out of 100; those who wrote by hand got 67. Effect size 0.738 at significance 0.01; there is no gain in time at all, and the gap is wider on "find the bug" tasks. The subject being measured here is programming, not medicine.

Behind this breakdown stands a yardstick for the two clinical ones that follow, and each of them has its own hole. The Polish study measures exactly what's needed — the result for the same physicians without the assistant — but it is observational, looking backward through an archive, and the authors make no claim of causality. The Russian trial is stronger in grade of evidence, it is randomized, but it has no observation period after the assistant is removed at all, and the authors say so themselves. One study measures the right thing by a weak method, the other measures the wrong thing by a strong method. Here the second half of the pair is measured by lottery, and this is the only place in the section where that happens.

The second reason to put it first, and it is the more important one. It is taken on the very work the room itself does. About physicians, you can always say: they have their own specifics, it's not like that for us. About junior engineers writing against an unfamiliar library, you cannot say that — this is exactly what half the audience was doing this week. The section is about what happened to the person who decides, and it begins with the person sitting in the room.

And right away, a distinction that cannot be glossed over. The Polish study, which comes next, measured EROSION: the same nineteen physicians were in form and got worse. Here what's measured is FORMATION: nobody knew the library, and the question was whether the skill formed at all. The eighth glossary form, "the performer is the same, but got worse," cannot be assigned here: the same performer is not being compared against anything here. There is no form in the glossary for a case like this, and it is more honest to call it a refusal than to force a fit.

The design of the experiment. Fifty-two participants, mostly junior engineers; each has written in this language for at least a year, is familiar with AI assistance, but is not familiar with the specific asynchronous-programming library — and this matters, because what is being measured is exactly the formation of a new skill, not work with one already held. The task: write two features using this library. Split by lottery: half were given an AI assistant, half were not. Right after the work, everyone was tested with no assistant, with four types of tasks: find a bug in code, read someone else's code, write code, explain a concept.

The result. The group that wrote by hand scored 67 correct out of 100; the group with the assistant scored 50. Cohen's effect size of 0.738 at significance 0.01. That's about a two-grade difference — the kind you'd see on an exam. The gap is wider on "find the bug" tasks — and this is worth pausing on: finding a bug in someone else's code is exactly the work the assistant takes over first, and afterward there is nothing left to train that skill on. There is no gain in time here: the group with the assistant finished about two minutes earlier, a difference that is not significant. So they paid in understanding and didn't buy speed.

Now the reason this case is more valuable than the two that follow: it names not only the drain, but also a way not to pay it. The authors broke down exactly how people dealt with the assistant, and identified six approaches. Three of them preserve retention. Those who asked only about concepts and worked out the bugs themselves — seven people — stayed above 65 out of 100. Those who asked for code together with an explanation — three of them — did too. And those who handed the task over to the assistant whole — four of them — were the fastest of all and below 40 out of 100. These numbers are small, and they cannot be presented as a measured regularity; they can be presented as a direction, because it matches what we already saw with schoolchildren: there, guardrails removed the effect; here, the way the assistant is used removes it. In both cases the cure is the design of access, not the amount of practice.

I name the limitations as the authors themselves do. The sample is small. What was tested was immediate understanding right after the work, not skill over months — that is, this measurement has no long horizon, unlike the Polish study, where three months passed between windows. The work is code only. And there is no comparison against help from a live person — a mentor, a colleague — at all, and that absence matters: we don't know whether any kind of help produces the same effect, or specifically help from a model.

And the slide's last line, which frames the whole section if said properly. The same loss of skill happens with no trained model at all. In the UK, cytology switched to primary human papillomavirus (HPV) testing — that is a laboratory assay, with no model in it at all. The volume of cases for reading dropped 80 to 85 out of 100, the labs were cut down from 45 centers to 8, and the review itself names the consequence directly: there was nothing left to train on. The conclusion from this carries weight, and it runs exactly against an easy reading of the whole section, which has only just begun. It is the handed-off volume of work that drains skill, not the trained model as such. Blaming AI specifically for deskilling would be an error of the same class as crediting the model with the classical mode's win — and this is the error the lecture has spent all evening catching others in. So the right question sounds like this: how much work have we taken away from the person, and where is he getting it now. And it's with that question that we'll go to the physicians.

The grade of evidence for the cytology mention has to be named: this is a consolidated review of deskilling, not the primary source of the program itself. In that same review sit two more numbers worth saying out loud: in web-reading experiments, more than thirty out of a hundred participants abandoned their own correct conclusion under an incorrect model cue, under time pressure; and in an experiment with twenty-seven radiologists, incorrect cues raised the false-call rate by up to plus twelve percentage points, including among experienced ones. Both numbers are taken from the review, not from the full texts of the experiments themselves — and that is exactly how they should be cited. And that same review has its own error, exactly on our subject: it calls the Polish study, which comes next, a randomized multicenter trial, when it is observational. A peer-reviewed review got the grade of evidence wrong. We will not get a better illustration today of why we spend the whole evening looking at how a measurement is built, rather than at the word "measured."
