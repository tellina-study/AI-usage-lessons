---
# НОВЫЙ КАДР (круг 6, 2026-10-19) — шаг «что переехало» для Примера 1.
# Отдельным кадром, а не строкой на `s27a`: разбор не обязан помещаться в слайд,
# дробить его ради экономии места запрещено (CLAUDE.md § «Строение раздела»,
# «Один кейс может занимать несколько слайдов»). Та же пара, что у `s30`/`s30a`.
# Деньги считаются ПРОТИВ НАЗВАННОГО КЛАССИЧЕСКОГО РЕЖИМА в его собственных
# рублях, а не от нуля: выигрыш, посчитанный от нуля вместо классического
# режима, правилами курса не принимается (CLAUDE.md § «Строение раздела», п. 3).
id: s27b
local_id: s2-05b
section: "2. Инструментальная и лабораторная диагностика"
type: case
title: "Example 1, cost: it got cheaper only because nobody reads half of it"
assertion: "Чтение одного снимка стало ДОРОЖЕ — 155,62 рубля против 132,98 прежних; экономия 43,7 процента берётся целиком из тех 55 снимков из ста, которых не читает никто, а 290 пропусков нашлись только потому, что в исследовании «норму» перечитывали люди — в штатной работе этого слоя нет"
source: "Vasilyev et al., Digital Diagnostics 2025;6(1):5–22 — https://doi.org/10.17816/DD641703"
media: ""
media_needed: ""
media_note: "кадр числовой: три плашки и схема потока денег; иллюстрация здесь заняла бы место у чисел, ради которых кадр стоит"
blocks:
  - {label: "Human reading of one image: before → now", value: "132.98 → 155.62 RUB", note: "got more expensive on every image still read by a human; the model's finding — 6.9 RUB", key: true}
  - {label: "Over five months: without the model → with the model", value: "76.5 → 43.1 million RUB", note: "−43.7 percent, savings of 33.4 million RUB under mandatory health-insurance tariffs"}
  - {label: "Half the stream is people aged 18–44, and they have more misses", value: "12 versus 7 per 10,000", note: "155,898 of 315,491 \"normals\""}
scheme:
  arrows: true
  rows:
    - {label: "Where the savings come from", steps: ["45 out of 100 is read by a physician — pricier than before", "55 out of 100 is read by nobody", "net −43.7%"]}
    - {label: "What had to be done beforehand", steps: ["amending the mandatory health-insurance tariff agreement", "four new service codes", "without it, there is nothing to pay for the model's finding with"]}
pol_slov: 192   # замер по собранному sec-2.pdf, круг 6: шаг «что переехало»: три плашки с парами «было → стало» и схема происхождения экономии
timing_min: 1.1
in_bucket: true
method_steps: ["⑤что переехало", "пара дало–потребовало"]
form: ["форма 3", "форма 7"]
vfy: true
status: собран
---

## Visible slide text

**The benefit is not that reading got cheaper.** One image read by a human got **more expensive**: 155.62 RUB against 132.98. The savings come entirely from those 55 images out of 100 that nobody reads.

**The layer that found the 290 misses will not exist in routine operation:** all the "normals" were re-read by humans under the study's own protocol. The share will remain; the way to see it will not.

**Delivered:** −33.4 million RUB over five months. **Required:** 290 missed findings, and amending the tariff agreement before the work could even start.

## Speaker notes

The first thing that moved — a layer that caught the error disappeared. In routine operation, not one of the 290 misses would have been found by anybody. They were found only because the study's protocol required humans to re-read all 315,491 "normals". Once the study ends, this layer will not exist, and the share of misses will stay exactly what it is. In other words: the number we just praised the model with was obtained by means that do not exist in its routine operation.

Second: reading got more expensive per image. The tariff for reading a fluorography image classified as "not normal" is 155 rubles 62 kopecks, against 132 rubles 98 kopecks for the old blanket reading. An X-ray is 157 rubles 56 kopecks. Every image a human still reads got more expensive. The model's autonomous finding, meanwhile, costs 6 rubles 90 kopecks for a fluorography image and 8 rubles 80 kopecks for an X-ray — more than twenty times cheaper than human reading.

That is why the savings arithmetic looks exactly the way it looks. Over five months, tariff spending came to 43 million 89 thousand rubles, against a modeled 76 million 537 thousand under the old regime — minus forty-three point seven percent, a saving of 33 million 448 thousand. And it does not come from reading getting cheaper: reading got more expensive. It comes from the fact that nobody reads more than half the stream.

Third: before any work could happen, the regulatory base had to be amended. Four new service codes were added to the 2024 mandatory health-insurance program's tariff agreement. Without this amendment, the model could not operate at all — there was nothing to pay for its finding with. This is worth an engineer noting: the system's technical readiness and the ability to actually switch it on turned out to be two different things here, and the second was settled outside the technical plane entirely.

Fourth: the burden of misses fell unevenly. Half the stream is people aged eighteen to forty-four, 155,898 of 315,491 people, and they carry the largest share of misses: twelve per ten thousand against seven in the older groups. For men, the odds ratio for a clinically significant discrepancy is 1.32, with an interval of 1.04 to 1.66. The average share across the stream — five per ten thousand — describes none of these groups.

The pair that closes this breakdown. Delivered: 33 million 448 thousand rubles over five months, and half the stream taken off the radiologist's plate. Required: 290 missed clinically significant findings, not one of which will be found under ordinary operation.

And the lesson in full, because this is the first case in the section where autonomous use of the model did not fail. It is built honestly: the task is narrow — triage into "normal" and "not normal", not a diagnosis; the trigger threshold is set against the asymmetry of cost; the benefit is counted against a named classical regime in its own rubles; the cost is named with a number and an address. And it also shows what this rests on: the share of misses is known exactly because it was measured, and in routine operation there is nothing left to measure it with.

**Sources.** [Vasilyev et al., *Digital Diagnostics* 2025;6(1):5–22](https://doi.org/10.17816/DD641703)
