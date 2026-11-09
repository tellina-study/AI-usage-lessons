---
# ВОЗВРАЩЁН ИЗ `_snyato/` (переделка раздела 2 по канону PR #286, `storozha-i-priyomka.md` §14).
# ЭТО НАХОДКА, КОТОРАЯ ДЕРЖИТ ВСЮ ТАБЛИЦУ СТОРОЖЕЙ §14: несущая выкладка §2.2 главы — «одна
# система, две группы, доля верных тревог почти в десять раз выше при смене группы» — была
# объявлена на дивайдере `s22` в поле `assertion` и НИ РАЗУ не встретилась на 21 кадре показа:
# ни числом, ни словом «десятикратно». Кадры, её несшие (`_snyato/s24`, `_snyato/s25`), сняли
# раньше без замены. Канон на это: «снять кадр, несущий содержание дивайдера, без переноса
# содержания — то же самое, что соврать дивайдеру».
# ПРИЧИНА СНЯТИЯ УСТРАНЕНА, А НЕ ПРОИГНОРИРОВАНА. Снимал владелец, п. 23 своего разбора:
# «внезапный, ни перехода, ни экспозиции — убрать». Довод был верен: кадр открывался строкой
# «Как считали» без имени случая и без моста с предыдущего кадра. Исправлено ровно это и
# адресно: §5.18 — заголовок и первый блок называют, что за случай и что в нём делали (одну
# опубликованный порог срабатывания применили к двум группам по десять тысяч); §5.22 — первой
# строкой стоит мост с `s22a`, где стадию уже назвали производящей величины. Содержание выкладки
# при этом не урезано: четыре знаменателя на месте.
# `s25` НЕ возвращается: он пересказывал ту же арифметику второй раз (три способа поднять долю
# и имя доли). Три способа уехали в заметки этого кадра, имя доли стоит на кадре строкой.
id: s24
local_id: s2-03
section: "2. Инструментальная и лабораторная диагностика"
type: norm
title: "How accuracy is counted: one trigger threshold on two groups of ten thousand"
assertion: "Одни и те же доли чувствительности и специфичности дают на разных группах почти десятикратно разную долю верных тревог, и поднимают её тремя способами, из которых ни один не состоит в улучшении модели"
source: "Rajpurkar et al., CheXNet 2017 — https://arxiv.org/abs/1711.05225"
media: ""
media_needed: "Схема: одна система посередине, от неё две стрелки к двум группам людей разного размера — поголовный поток и профильное отделение, с проявленными числами верных тревог в каждой."
media_note: "иллюстрация не добыта; схему-конвейер кадр несёт сам, две группы разведены подписями рядов"
blocks:
  - {label: "Finds in 100 sick people · falsely alarms in 100 healthy people", value: "94 · 11", note: "one published setting, applied to both groups unchanged"}
  - {label: "Out of 100 alarms turned out to be disease: stream → department", value: "8 → 79", note: "94 of 1,183 versus 2,820 of 3,590; two groups of 10,000 people each", key: true}
scheme:
  caption: "One system, one trigger threshold; what differs is the share of sick people in the group"
  arrows: true
  rows:
    - {label: "General population stream", steps: ["1 sick out of 100", "1,183 alarms", "8 correct out of 100"]}
    - {label: "Specialized department", steps: ["30 sick out of 100", "3,590 alarms", "79 correct out of 100"]}
timing_min: 0.75
in_bucket: true
method_steps: ["заземление"]
form: ["сетка"]
vfy: false
status: собран
---

## Visible slide text

**The properties of a measurement are computed on a group.** One **trigger threshold** — the value beyond which the system declares "sick" — was applied to two groups of ten thousand people, differing only in the share of sick people.

**The difference is nearly tenfold, and not one line changed inside the system.** This share has a name — **positive predictive value**: what fraction of alarms turned out to be disease. This is what the physician at the visit actually sees, not sensitivity.

**The woman with the letter stands in the general-population stream: for her it is 8 out of 100.**

## Speaker notes

One trigger threshold — the value beyond which the system declares "sick" — is applied to two groups of ten thousand people, which differ in exactly one thing: the share of sick people among those examined. The system catches 94 sick people out of 100 and falsely alarms 11 healthy people out of 100. The count is short. These two figures illustrate the method, taken from a published trigger threshold for a chest-image reading model; they do not serve as a characteristic of a specific product, and no procurement decision should be based on them.

Apply it to both groups with not a single change inside.

General population stream: ten thousand people in a row, disease in one out of a hundred, that is 100 of 10,000. Correct alarms 94, false alarms 1,089, total 1,183. Specialized department: the same ten thousand, but here people have already been selected by complaint or referral, disease in thirty out of a hundred, that is 3,000. Correct 2,820, false 770, total 3,590.

Now for what this count is actually for. The physician at the visit does not see sensitivity at all — he sees what share of the alarms that reached him turned out to be disease. In the first case that is 94 of 1,183, that is, 8 out of 100. In the second, 2,820 of 3,590, that is, 79 out of 100. The difference is nearly tenfold, and not one line inside the system changed: only the group changed, and the share of sick people in it was set by whoever decided who to call in for examination — not the developer. This is a selection decision, made for everyone before anybody even looked at accuracy.

This share has two names, because two professions name it differently. An engineer knows it as precision on the positive class. In clinical work it goes by the name positive predictive value, and it depends on prevalence — the share of sick people in the examined group. Prevalence is not a property of the device.

What this means for the physician. Explaining to a patient one false alarm out of ten and nine false alarms out of ten are two different jobs, and those conversations are built differently. What this means for the engineer. Carrying a system over from a specialized department to general-population screening changes the meaning of its output: the same signal of "sick" is an almost certain finding in the first case, and in the second, a reason for further examination that will end in the word "normal" nine times out of ten.

And from here, three ways to raise the share of correct alarms, none of which consists of improving the model. Raise the threshold: there will be fewer false alarms, more missed cases, and the exchange rate here is set by the cost of both errors. Change the group: examine people in whom the disease occurs more often. Add a second, confirmatory test and declare "sick" only on both — this is exactly how the two tiers of screening programs are built: the first is tuned not to miss, its output is not a diagnosis but an invitation to further examination, and its share of correct alarms is low by design. A program where the first tier declares the diagnosis loses the second tier entirely.

Hence the rule this section hands off to the whole lecture: a stated accuracy figure without a named group and a named prevalence does not mean anything. The right pair of questions to ask of any accuracy claim is: which two shares, and on what group; and what is the prevalence where you are planning to apply this.

One clarification of usage that this rule makes visible. "Six cases detected per thousand examined" and "prevalence six per thousand" are different statements. The first speaks to the outcome of the program's work on the examined group, the second to a property of the population. Substituting the second for the first turns up constantly in retellings and breaks the whole count, because a value nobody measured gets plugged into the denominator.

Now about the woman with the letter, because this arithmetic is about her. She came in with no complaints, by age alone, and stands in that very general-population stream, where there is roughly one sick person per hundred. So the share of correct alarms for her group is the left-hand one, eight out of a hundred, not the right-hand one. If she gets a call inviting her for further examination, there is an eight-in-a-hundred chance the finding will be confirmed, and ninety-two that it is a false alarm, and each of those ninety-two people will live their weeks with an open question. Not one line inside the system changes.

**Sources.** [Rajpurkar et al., CheXNet 2017](https://arxiv.org/abs/1711.05225)
