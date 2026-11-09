---
id: s16
local_id: s1-07
section: "1. Первичный скрининг и отбор на обследование"
type: case
title: "Example 2: a first-line chatbot replaces a call to the practice"
assertion: "Сервис первой линии встал на место звонка в свою практику: вход стал мгновенным и бесплатным, обращений на человека стало больше при том же подушевом платеже, заказчик доплатил за год больше, чем весь платёж за этот список, и кончилось банкротством; качество сортировки при этом не измерил никто, а экзаменационным баллом обосновали выход в открытый поток"
source: "Royal College of GPs, 2018 · independent service evaluation, 2019"
media: ""
media_needed: "настоящий снимок: страница приложения или публичного события 2018 года, где заявлена оценка. По убыванию: архив страниц сайта компании (веб-архив, дата видна) · иллюстрации к расследованию в деловой прессе · снимок страницы публичного заявления коллегии врачей"
media_note: "стилизованную карточку с дословным заголовком вместо настоящего снимка не ставить ни при каких обстоятельствах"
blocks:
  - {label: "Extra the commissioner paid in a year", value: "£10.5 million", note: "a panel of 49,000; the whole capitation payment for it is £7.6 million", key: true}
scheme:
  caption: "The practice is paid £155 per person a year, not tied to the number of contacts"
  arrows: true
  rows:
    - {label: "Before", steps: ["Complaint", "Call to the practice", "Visit by triage"]}
    - {label: "After", steps: [{text: "Complaint in the app", ai: true}, "The model issues the route", "Contacts 4.0 → 4.3"]}
razbor_part: "1 из 2; ①цена обеих ошибок, ②классические режимы, ③экзамен как основание и арифметика канала, ⑤пара дало–потребовало — здесь. Три свидетельства о внутреннем устройстве ПОРОЗНЬ (Харви — бывший сотрудник; Уоткинс — врач со стороны, писал регулятору; собственная публикация компании), ④как это устроено и честно названный пробел в контуре обратной связи — на s16a. Разведение Харви и Уоткинса стоит там, а не здесь, потому что там же стоит третье свидетельство, и все три сравниваются в одном месте: глава называет их смешение отдельной ошибкой атрибуции"
pol_slov: 259   # #270 (issue #270, инженерная глубина): добавлена мостовая фраза «Что опубликовала сама компания — кадром следом» после строки про дерево «если-то» — готовит разряд свидетельства второй половины разбора (s16a) без того, чтобы путать его со словами участника здесь. Остальное содержание кадра НЕ ТРОНУТО: #229 п.16 (владелец: экспозиция в названии и первом блоке; «от качества бота нам ни горячо ни холодно — показать, на что влияет, или убрать»; «явно: внедрение бота повысило/понизило обращения → такие потери/экономия → итог для отрасли»). Что сделано и чем заняты слова. ЭКСПОЗИЦИЯ: заголовок называет случай и что в нём делали («чат-бот первой линии вместо звонка в практику»), первый блок — «Что за случай» целиком. ЦЕПОЧКА стоит четырьмя плашками в порядке, который требовал владелец: обращений 4,0 → 4,3 на человека в год · платёж практике 155 фунтов, от числа обращений не зависящий · доплата заказчика 10,5 млн фунтов за год при том, что весь подушевой платёж за этот список — около 7,6 млн (контрфакт из chapter-part1b.md:182, счётом 155 × 49 000) · оценка 4,2 млрд → активы 500 тысяч. КАЧЕСТВО БОТА больше не висит само по себе: экзамен 81 против 72 назван тем, на что он повлиял, — им обосновали выход в открытый поток, тогда как качество сортировки не измерил никто. ИТОГ ДЛЯ ОТРАСЛИ назван словами главы (chapter.md:466, chapter-part1b.md:224): сортировка обращения словами после этого случая стоит на месте. Снято как сказанное дважды: «список около 49 тысяч» стоял трижды — в заголовке, в теле и в подписи плашки, где он и есть база числа 10,5 млн; в теле снят. ЗАМЕР ПО СОБРАННОМУ PDF полосы Входа и раздела 1 (render_sec.py 1, 2026-10-18, 11 страниц): 259 слов на этом кадре после добавления мостовой фразы (было 252); медиана полосы 177, максимум 286 (`s13a`), блокирующих 0 (`build_lec07.py --only s16,s16a`). Поле выставлено ПО ЗАМЕРУ, не по оценке.
timing_min: 1.1
in_bucket: true
method_steps: ["①цена ошибки", "②классические режимы", "③модель против них", "④как это устроено (слова участника)", "⑤что переехало", "пара дало–потребовало"]
form: ["форма 1"]
vfy: true
status: собран
---

## Visible slide text

**What kind of case this is.** A first-line service in England: a person describes a complaint, and the model issues the route. The second classical order of work — a phone triage line — is named, but not counted.

**The cost of both errors:** missing someone who needs help now · tying up an appointment · the cost of the channel.

**Exam: 81 for the app against 72 for doctors.** This is what justified the move into the open flow; nobody measured the quality of the triage itself.

**What it gave:** round-the-clock triage · **what it cost:** a loss on every patient · **net result: worse off** — bankruptcy in 2023.

## Speaker notes

A first-line service in England: a person describes their complaint in an app, and the model issues the route — where to go right now. The service took the place of a call to one's own practice, and it ended in bankruptcy in August 2023. The cost of both errors in triaging contacts: missing someone who needs help right now costs an outcome; tying up an appointment for someone who didn't need it costs a doctor's time and someone else's delayed visit. There's a third cost, usually not counted at all: triage costs money for whoever funds it, and the payment structure decides whether it survives.

What was claimed. In June 2018 it was publicly announced that the app scored eighty-one percent against seventy-two on licensing exam questions for trainee doctors — against the average score of practicing doctors. The Royal College of General Practitioners publicly called these claims questionable.

The device and the service go by their own names: the app is Babylon, the first-line service built on it is "GP at Hand." The input was a complaint in free text; the output was a route — "where to go right now." What it was trained on is unknown, and that lack of knowledge is itself telling. Two people spoke about the internal construction, and they are different people with different standing to speak — folding them into one "same thing" would be exactly the mistake this section teaches you to catch. Hugh Harvey worked at the company in 2016–2017 as head of regulatory affairs for clinical AI: by his own public claim, there was nothing to train — inside sat a decision tree of "if-then" rules in an ordinary table. David Watkins is a general practitioner who never worked at the company: since February 2017 he's documented misses and written to the regulator about them, escalating the complaint to "critical" by 2018. The first is words from a person inside about the construction; the second is letters from a person outside about the system's behavior. Neither is a check, and treating either as an established fact would be exactly the mistake this case is examined to catch. They're examined separately further on, alongside what the company itself published.

The participant's words aren't the last thing found about the chatbot's construction: the company has its own technical publication, and it can be trusted differently — I examine it separately, so the two different testimonies don't blur into one fact. The scale of the pilot, for context: with the National Health Service it started in January 2017 and was available to roughly 1.2 million residents of north London; one case in the chat took about two minutes.

Why the exam metric doesn't hold up as a foundation. An exam question arrives already formulated and contains the relevant features. A live contact arrives with no formulation: the person says "I feel awful," not "chest pain radiating to the left arm." The exam metric measures performance with a ready-made formulation — exactly the part of the task that doesn't exist in the open flow. And the right comparison existed and was ignored: a year before the demonstration, an independent comparison of three apps on the same tasks put this app in last place — it recognized typical illnesses worse than any of the others.

Now the other half of the case — the cost, and here the classical regime is counted in money. The practice is paid about one hundred fifty-five pounds per registered person a year by the National Health Service, and that amount doesn't depend on the number of contacts. A classical contact rate is four times a year for people 25 to 44 and three and a quarter for people 15 to 24. This is the base chosen, rather than the national average, because more than eighty percent of the service's panel were under forty, and the average would have understated the difference. In the service, contacts came to four point three per person a year.

The arithmetic plays out as division, and that's where all the bite is. On top — a fixed sum per person per year. On the bottom — a grown number of contacts. Every extra contact is free for the patient and gets paid for out of the same payment, divided by a bigger number of contacts. The load moved from triage to the appointment, and nobody was left to pay for it. The engine of this move is the accessibility of the channel — the model's quality has nothing to do with it. Entry became instant and free, and the number of contacts grew.

What it gave and what it cost. It gave round-the-clock triage and a low threshold for reaching out. It cost: an economics that ran at a loss on every patient, more than ten million pounds of extra expense for the commissioner in a year with a panel of about forty-nine thousand people, and a documented case where symptoms resembling a heart attack weren't recognized. Net result: a valuation at exit through a merger of more than four billion dollars, bankruptcy in August 2023, assets sold for five hundred thousand pounds.

Caveats to the slide's figures. The ages used aren't national averages — the reason is named above. The contact rate in the service is an estimate from an independent report over twelve months of data, with personal contacts counted from the single month the report was given access to count; it's an estimate with a trend extrapolation, and the report says so itself. The last plate carries two different quantities in two different currencies, not one quantity at two points in time, and that's exactly why there's no arrow between them: the company's valuation was figured in dollars at the merger, the revenue from the asset sale in pounds at bankruptcy, and in some reports the same sum is given as $620,000.

What these figures don't prove: whether the rise in contacts was unmet need or demand the service itself created — the report honestly says it doesn't know. Whether the decision tree itself sorted poorly, there's no data for that either: what's measured here is a restructuring of the channel's economics, not the quality of the triage.

The case is still worth taking as it is: this is a failure of the condition, and the cost of claiming a model where there was none is its content. The lesson is a checkable criterion: a demo metric is not grounds for release into the open flow, and the question to ask is what material it was obtained on.

This regime doesn't distinguish rare from common in the open flow. Dictating a visit note into it is accepted — the record-keeping section examines that; sorting a contact, after this case, is not.
