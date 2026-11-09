---
id: s105
local_id: s9-02
section: "7. Закрытие"
type: comparison
title: "The device gets recalled; the decisions stay"
assertion: "Необратимы не изделия — необратимы решения, принятые по ним до отзыва"
source: "Lee et al., JAMA Health Forum 2025, cutoff November 2024 — https://doi.org/10.1001/jamahealthforum.2025.3172"
media: "rework/deck/assets/s105-hero-uvedomlenie-ob-otzyve-izdeliya-verkh.png"
media_hero: true
media_document: true   # О18 (#229): на кадре снимок ЗАПИСИ РЕГУЛЯТОРА — предъявленный документ, а не фотография-иллюстрация: зал по подписи проверяет саму запись Z-2111-2021, на которой стоит число кадра. Поле требует подпись об источнике и включает её отрисовку
# ЗАГОЛОВОК НАРОЧНО В ДВЕ СТРОКИ, и сборка об этом предупреждает. Рядом с
# обязательным hero в 7,58" колонка заголовка — 4,31", и `titles.fit_title`
# на ней даёт: 46 знаков → 23,0 пт в две строки, 35 знаков → 16,0 пт в одну.
# То есть «починка» предупреждения укорочением роняет строку-удар с 23 до 16
# пт — она становится мельче подписи плашки рядом. Названный предупреждением
# вред (золотая черта под второй строкой подчеркнёт одно слово) на снимке не
# наступает: черта ставится по НАСТОЯЩЕМУ низу заголовка во всю свою ширину
# (`heading`, «ЗАЖИМА СВЕРХУ БОЛЬШЕ НЕТ»), проверено глазами на PDF 13 октября
# 2026. Предупреждение оставлено как есть — глушить его нечем, и врать ему
# нечего.
blocks:
  - {label: "What gets recalled", value: "the device", note: "the recall procedure exists — the regulator's record sits alongside"}
  - {label: "What stays", value: "the decisions made during its year in service", note: "a procedure can't be redone, a year of follow-up can't be replayed", key: true}
media_caption: "FDA device recall database, record Z-2111-2021, October 2026"
media_needed: "настоящий снимок: публичное уведомление об отзыве медицинского изделия — страница регулятора с датой. Настоящая страница, не стилизованная карточка"
media_note: "добыта: снимок записи FDA об отзыве Caption Interpretation Automated Ejection Fraction Software — изделие из той же выборки, что и число слайда (допуск 22 июля 2020, отзыв начат 19 мая 2021 — внутри первых двенадцати месяцев). На слайд идёт верхняя часть снимка, полностраничный оригинал лежит рядом. Права и сверка — deck/images.md §1"
pol_slov: 130   # ПОДНЯТ со 115 (#229): единственное число кадра — 43,4 процента отзывных событий первого года — ушло вместе с разбором надзора (s71), и примитив `figure` снят целиком. Кадр переписан на утверждении «изделие отзовут, решения останутся», которое держится механизмом, а не долей. Освободившееся место занимает САМО противопоставление кадра двумя плашками («что отзывается — изделие» · «что остаётся — решения за год его работы»), без единого заимствованного числа. ЗАГОЛОВОК ВОЗВРАЩЁН двухстрочный: прежний круг укоротил его, чтобы погасить предупреждение, не прочитав стоящую тут же записку о том, что две строки здесь НАРОЧНО; замерено — короткий даёт 19,0 пт в одну строку против 23,0 пт в две, то есть «починка» стоила закрытию четыре пункта заголовка. 113 → 126 по собранному PDF
opyt_net: "кадр закрытия: своего замера не ставит. Число 43,4 процента отзывных событий первого года и его база стояли здесь и ушли вместе с разбором надзора (s71), который снят; кадр говорит это прямо. Утверждение «изделие отзовут, решения останутся» держится механизмом, а не долей: отзыв как процедура существует, снимок записи регулятора стоит на кадре, а обратного хода у принятых решений нет"
timing_min: 1
in_bucket: true
method_steps: ["⑤что переехало"]
form: ["[VFY]"]
vfy: true
status: собран
---
## Visible slide text
"In medicine everything is irreversible" is a claim wider than any measurement. **Devices get recalled: the regulator's record sits right here.** Decisions made on a device during its year in service don't get recalled along with it.

**What happened to the woman with the letter, nobody measured.** The same question for your own loop: what in it gets recalled, and what stays.

**Next — an industry where an error can almost always be undone:** the dispute there is over who owns the result; the cost of error barely gets a mention.

## Speaker notes

The last lecture ended with a line said to the room: a batch can be recalled, a decision about a person cannot. This lecture has worked that claim over with measured material — the claim holds, and there's an amendment that makes it stronger.

The first half holds literally, and even wider than it was stated: not only a batch of parts gets recalled, but a device with a trained model inside it too. The count that confirmed this sat in the oversight section and was cut along with it; what remains here is the checkable half itself — it is specifically the model-equipped device that gets recalled, and a record of such a recall sits right on the slide.

The second half is confirmed by two of the lecture's breakdowns. Decisions made on a device before its recall: they are not recalled along with the device. Technique that degraded in procedures done without the assistant — those procedures have already happened, and they can't be redone.

The amendment worth stating out loud: the recall exists, works, and has been counted. The device gets recalled — what's irreversible are the decisions made on it before the recall. Forty-three percent of recalls fall in a device's first year in service, and that year's decisions stay as they are. The phrasing "in medicine everything is irreversible" is wider than any measurement, and there's nothing to check it against. The phrasing "there's a gap between a device's reversibility and a decision's irreversibility, and it's measured" is checkable, and it can be applied to your own working loop: ask what in it gets recalled, and what stays after a recall.

And an honest caveat about scope: both remaining breakdowns sit inside a medical loop, where the decision was made by the person accountable for it. A third one, where irreversibility concerned a treatment decision about a specific person made by someone other than a doctor, was cut by the course owner's decision along with the topic it belonged to, and there's nothing to strengthen that pillar with in its place. From here the course moves into an industry where an error can almost always be undone, and the dispute there is over who owns the result rather than over the cost of error: that's the shift, and the change in question is exactly that.

And about the woman the evening began with. What happened to her, nobody measured: not a single measurement of a person's long-term outcome after a decision made with the model's involvement turned up — not in her program, not in any other. Where a sixth step on the path should stand, there's nothing, and that was stated at the start. This is exactly the difference between a device recall and a decision about a person: the first is counted, the second isn't even tracked.

**Sources.** [Lee et al., JAMA Health Forum 2025, device recalls](https://doi.org/10.1001/jamahealthforum.2025.3172)

The number behind this measurement is no longer on the slide: the oversight breakdown that counted it and worked out its denominators was cut along with its own section. If you want to say the share out loud — it was a share of recall EVENTS, not a share of devices, and the two must not be confused; but there's nothing left here to present it with on a slide, and it shouldn't be passed off as shown.

"In medicine everything is irreversible" is a claim wider than any measurement, and it has to be checked the same way we check anyone else's claims. The recall exists as a procedure, and the regulator's record of one sits right on the slide: a device can be taken out of circulation. What's irreversible is something else — the decisions made on that device during its year in service. They aren't recalled along with it, nobody revisits them, and the person something was done to, on their basis, usually isn't notified of the recall at all.

So the question to your own loop is put exactly this way: what in it gets recalled, and what stays. A device, and a batch, can be recalled; a decision made before the recall, and a procedure already carried out, cannot be undone.

And the transition to the next lecture. From here the course moves into an industry where an error can almost always be undone: roll back a version, rewrite the code, restore data from a backup. The dispute there is over who owns the result — who's the author, whose work, whose rights — and the cost of error is barely heard in it. This comparison is worth stating plainly: not "it's easier there," but "the asymmetry is different there, and it makes different things expensive."

How often this happens, this one hasn't counted.
