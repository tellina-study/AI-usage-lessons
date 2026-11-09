---
# НОВЫЙ КАДР-УДАР, прожарка сторителлинга #293, Этап C (П3, раздел 2). Место — МЕЖДУ `s27` и
#   `s27a`: доля потока названа ударом, и только потом идёт разбор того, как она получилась.
#   П3 дословно: «открыть s27a с конца — кадр „55 из 100 — не прочтёт никто" одним числом во
#   весь экран, потом разбор».
# НОМЕР `s27_1` — подномер между `s27` и `s27a` (`deckkit/slidefile.py::order_key`): буквенный
#   хвост этого места не даёт, `s27a` уже занят разбором, а переименовывать разбор значило бы
#   двигать три ссылки на него в `s99`, `s103` и реестре.
# ПОЧЕМУ ЭТОГО ЧИСЛА НЕТ ВО ВХОДЕ. Удар Входа (`s01_1`) берёт английские 2,8 млн, и московские
#   55 из ста туда НЕ взяты намеренно — об этом прямо сказано во фронтматтере `s01_1`: это удар
#   своего раздела, и предъявить его дважды значит потратить впустую.
# ПЛАШКА СНЯТА С `s27a`, А НЕ ПРОДУБЛИРОВАНА: та же пара «55 из ста · 315 491 из 575 549»
#   стояла там третьей плашкой из трёх. Два написания одного числа на соседних кадрах — это
#   §5.12 («пара — ОДНА плашка, не два числа на разных кадрах»). Побочный выигрыш замерен:
#   `s27a` — самый тяжёлый кадр деки, единственный с блокирующим `[кегль]`, и плашкой меньше
#   он дышит.
id: s27_1
local_id: s2-04_1
section: "2. Инструментальная и лабораторная диагностика"
type: udar
title: "Moscow, the preventive stream: how many images no human opens"
assertion: "Доля потока, которую после автономной сортировки не читает ни один врач, — 55 из ста: 315 491 снимок из 575 549 за пять месяцев 2024 года; дальше разбирается, как эта доля получилась и чем за неё заплачено"
source: "Vasilyev et al., Digital Diagnostics 2025;6(1):5–22 — https://doi.org/10.17816/DD641703"
media: ""
media_needed: "иллюстрация не нужна и запрещена замыслом: кадр держит одну величину во весь экран"
media_note: "кадр-удар на БЕЛОМ фоне, не на тёмном. Тёмных кадров в деке два — удар Входа `s01_1` и пауза закрытия `s102_1`, — и оба стоят на швах вечера. Третий тёмный посреди раздела обесценил бы оба: смена экрана работает, пока она редкая"
figure:
  value: "55 out of 100"
  unit: "preventive chest images that no physician opens"
  base: "315,491 of 575,549 over five months of 2024, Moscow"
  note: "the model's finding goes straight into the electronic chart"
timing_min: 0.3
in_bucket: true
method_steps: ["заземление"]
form: []
vfy: true
status: собран
---

## Visible slide text

## Speaker notes

Fifty-five preventive images out of a hundred in Moscow go into the medical chart without ever passing through a human. The share is computed on a published sample — England has two such shares, the United States has none at all.

Fifty-five images out of a hundred. More precisely — fifty-four point eight percent: from May to September of year twenty-four, the model received five hundred seventy-five thousand five hundred forty-nine preventive chest images, fluorography and X-ray scans, and classified three hundred fifteen thousand four hundred ninety-one of them as normal. The finding on them went straight into the electronic chart. Not a single physician opened these images.

I'll state the denominator separately, because without it the number reads wrong. Five hundred seventy-five thousand is not the city's entire radiology stream, and not all chest images. It is the preventive stream: images taken on healthy people by plan, not by complaint. Six hundred forty-two thousand six hundred eighty-one studies were sent into the system; five hundred seventy-five and a half thousand went into the analysis. On a complaint-driven stream the share would be different, and the two cannot be compared.

And right away, a distinction without which this hit turns into a slogan. Fifty-five out of a hundred is volume, and only volume. It says neither that this is good nor that it is bad. It says that the decision "a human will not see this image" is made in the city three hundred fifteen thousand times over five months, that is, roughly two thousand times a day, and it is not a human making it. What has been paid for this is the next slide, and the payment there is counted: two hundred ninety clinically significant misses, and minus forty-three point seven percent of tariff revenue.

Why this is a standalone hit, not a line in the breakdown. The whole evening rests on one question: what does the human do after the model. At the third tier of participation — "looks only at what's in dispute" — the answer turns out to be literal: on half the stream, he does nothing, because that half never reaches him. The number stands as its own slide so the room hears it before it starts working through the trigger threshold and the tariffs: scale of the decision first, its mechanics second.

One note on the technique itself, in case anyone asks why it was tuned this way. Sensitivity is set to one deliberately: an alarm is raised on anything even remotely resembling an abnormality, and specificity is declared not significant. This is exactly why forty-five images out of a hundred go to a human and fifty-five do not. The breakdown of this decision is on the next slide; what matters here is only that the trigger threshold is not a default setting — it is an adopted and recorded decision.

**Sources.** [Vasilyev et al., *Digital Diagnostics* 2025;6(1):5–22](https://doi.org/10.17816/DD641703)
