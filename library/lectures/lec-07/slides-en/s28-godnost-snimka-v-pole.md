---
id: s28
local_id: s2-06
section: "2. Инструментальная и лабораторная диагностика"
type: case
title: "Example 3: Thailand — fundus reading in a primary-care office"
assertion: "В поле решение о годности снимка переходит от человека к устройству, двадцать один снимок из ста устройство отклоняет само, и каждому из этих людей достаётся повторный визит, а технику — работа добиться годного снимка, которой у офтальмолога не было"
source: "Beede et al., CHI 2020 — https://doi.org/10.1145/3313831.3376718"
media: ""
media_needed: "Поиск: реальная фотография ретинальной камеры для скрининга диабетической ретинопатии в кабинете первичного звена — медсестра или фельдшер делает снимок глазного дна пациенту. Нужен подлинный снимок, не рендер и не постановочная иллюстрация с актёрами."
media_note: "#283, задача 2: лента из трёх настоящих негодных снимков глазного дна (была на кадре) СНЯТА — бюджет высоты кадра занят схемой `без модели / с моделью`, которую отдельно потребовал бриф (чек-лист инженерной глубины, §2 obzor-stran-i-glubina-razbora.md), и боковая колонка не умещается ни при какой ширине до пола 2,60\" при схеме+двух плашках на кадре (замерено `fit_media`). Снимок не мок и не слабая картинка — он уступил место содержанию, которое бриф назвал обязательным; права и источник (Skevas и соавт., BMC Ophthalmology 2024, рис. 3, CC BY 4.0) остаются в `deck/images.md` §3.3 для восстановления, если бюджет кадра когда-нибудь расширят"
blocks:
  - {label: "The cost of both errors", value: "vision loss · a visit to an ophthalmologist who does not exist", note: "no monetary estimates exist for this country"}
  - {label: "Image rejected for quality → a repeat visit", value: "21 out of 100", note: "393 of 1,838 over the first six months", key: true}
scheme:
  arrows: true
  rows:
    - {label: "Without the model", steps: ["referral to a specialist", "waiting for the visit", "specialist reading"]}
    - {label: "With the model", steps: ["image taken by a nurse/technician", {text: "autonomous reading", ai: true}, "refer / negative / rejected for quality"]}
pol_slov: 193   # О20 (#229): объявлен ЗАНОВО — кадр перестроен по п. 25 владельца целиком. Прежние 159 оплачивали строку «Как наблюдали».
# ЧТО СНЯТО по п. 25: лозунг из заголовка («точность приехала, а снимки не прошли» — оценка, не предмет; стоит «чтение глазного дна в кабинете первичного звена», §5.18); плашка «Дало → потребовало» — именно её владелец назвал пустой содержанием («не видно что дало как наблюдали и что переехало — убрать»), и её содержание переехало в сами числа: «21 из ста → повторный визит» и есть «что переехало», названное человеко-центрично; текстослоп внизу («У техника появилась работа… появился шаг — повторный визит каждому из 21 из ста») говорил то же, что подпись плашки, — осталась подпись.
# ЧЕМ ЗАНЯТЫ СЛОВА: «было → стало» в единицах людей, чего кадр не имел вовсе (п. 25). Было — классический режим «направить к специалисту», до которого доходят 22 из ста направленных; стало — результат получают все обследованные, но 21 из ста уходит на повторный визит. Обе половины с оговоркой о разных выборках прямо на кадре: явка измерена в другой стране и на другой возрастной группе, сопоставляются порядки.
# ЧЕГО В ЕДИНИЦАХ ВЛАДЕЛЬЦА СДЕЛАТЬ НЕЛЬЗЯ, и это названо, а не обойдено: «количество отклонённых vs стоимость» денежного ответа не имеет — глава прямо говорит, что денежных оценок для этой страны в открытых источниках нет, а американские сюда не переносятся (chapter-part1c.md:138). Поэтому стоимость названа в той единице, которая измерена: повторный визит каждому из 21 из ста и новая работа техника. Выдумывать денежную оценку было бы ровно тем, что раздел учит ловить.
# ЦЕНА (замер по собранному PDF): плашек четыре → три, тело 14,0 пт — выше пола на два пункта, блокирующих нет. Слов 158 → 193: проза срезана, но «было → стало» в людях и оговорка о разных выборках прибавили больше, чем ушло. Иллюстрация на месте (лента трёх настоящих негодных снимков), и она часть ответа: отказ по качеству показан самим явлением.
timing_min: 1.1
in_bucket: true
method_steps: ["①цена ошибки", "②классические режимы", "③модель против них", "④как это устроено", "⑤что переехало", "пара дало–потребовало"]
form: ["сетка", "форма 4", "форма 3", "[VFY]"]
vfy: true
status: собран
---

## Visible slide text

**Fundus reading in a primary-care office.** Six months, eleven clinics in Thailand: nurses and technicians took the images, the system read them on the spot in under a minute and rejected unusable ones itself.

**How it's built.** Trained on images already selected for quality; in the field, that selection is made by a human with no rule. The system's name is not given. **Reasons for rejection:** lighting, a slow connection.

**The deployment failed, the reading worked.** *A field observation, measured once; orders of magnitude are compared, not samples.*

## Speaker notes

Eleven clinics in Thailand, the first six months of deployment: primary-care nurses and technicians take the fundus image, the system reads it on the spot in under a minute and rejects an unusable one itself. It rejected twenty-one images out of a hundred — 393 of 1,838. The cost of both errors here is counted in outcomes and in visits; there are no monetary estimates for this country.

A missed fundus lesion in a person with diabetes means irreversible vision loss: up to the late stages it is asymptomatic, the person feels nothing and does not come in on his own. A false alarm is a referral to an ophthalmologist who may not exist in the area at all, and a line where those who actually need the referral have to wait. There are no monetary estimates for this country in open sources, and American ones do not carry over here, so the cost is named in outcomes and visits.

The classical regime is named in words, with no number: once a year, a person with diabetes visits an ophthalmologist, who takes and reads the image himself. There is no count for this regime on the same Thai sample in the source, and plugging in attendance from a different trial — a different country, a different age group — would mean splicing two samples into one. There is no second classical regime for this task at all: double reading of fundus images never happens in primary care — there is nobody there to do it.

The model against this regime: autonomous reading of two fundus images right in the primary-care office, a result in under a minute, no ophthalmologist. Input — two images, output — the same label a specialist would assign. It was trained on a lab dataset of images that had already been selected for quality, and this is exactly where the whole breakdown lies: in the field, this selection is made by a human given no rule for it. The study names no name for the system — there is nothing to name it with, and this is a refusal, not an omission.

The source is silent on the size and composition of the training set, on how often it is retrained after deployment, and on any drift-monitoring protocol: this is an observational deployment study, describing the setting and its problems, not the model's engineering.

And here is what the field showed. Over the first six months of deployment across eleven clinics, 21 images out of a hundred were rejected for quality — 393 of 1,838 taken. Both named causes are about the setting, not the model: the lighting in the room where the image was taken, and a slow connection that kept the image from making it to processing in time. Neither cause is visible on the lab dataset.

Twenty-one out of a hundred is the share of ungradable images, and it must not be confused with a no-show rate: attendance was measured by a different breakdown, on a different sample, in a different country.

The lab accuracy of the predecessor model is published, but it does not enter this breakdown: it has no named group and no named prevalence. The section's rule applies even to a number that would flatter the breakdown.

Now for what moved in the work, and this is the case's leading change. The workload grew in the same place. The place and the hand are the same — the primary-care technician, the same camera — but the volume of work is larger: he has gained the job of obtaining a gradable image. The ophthalmologist never had this operation at all, because he compensated for the imaging conditions himself: adjusted the position, retook the shot, looked at the result with his own eyes. Alongside it, a step appeared that did not exist in the classical order: a repeat visit for anyone whose image did not pass. That is 21 people out of every hundred examined, and each of them has to come back a second time.

The pair that closes this breakdown. Delivered: a result right in the primary-care office, with no referral and no waiting for a specialist. Required: a gradable image under conditions the system was never tested against. Net: at the start of deployment, the result came in worse than the lab measurement, and the gap is explained by the mechanics of the setting, not the mechanics of the model.

The lesson worth taking from this breakdown as a whole. The deployment failed — the reading worked. The model arrived ready; the setting for it was not, and nobody measured that very setting before deployment. Neither of the two named changes is about the model: both are about the setting.

And an honest caveat on the strength of the evidence. This is a field observational deployment study: eleven clinics, the first six months. Measured once, with no direct replication.

**Sources.** [Beede et al., CHI 2020](https://doi.org/10.1145/3313831.3376718) · illustration — [Skevas et al., BMC Ophthalmology 2024, fig. 3](https://pmc.ncbi.nlm.nih.gov/articles/PMC10832120/)
