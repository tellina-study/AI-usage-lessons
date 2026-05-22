---
id: s29
type: assertion_visual
duration_min: 3.5
assertion: "Cruise: 10 миллиардов сожжено, менее 500 миллионов выручки. От 2 октября 2023 (incident SF) до 11 декабря 2024 (GM exit) — 14 месяцев краха."
learning_goal: "Cruise centerpiece — timeline 4-уровневого failure pattern"
learning_outcomes: [LO2, LO7]
chapter_ref: "§3.6 — Cruise GM exit: канонический провал robotaxi 2024"
failure_bucket: strict_in
references: [cnbc-cruise-exit, npr-gm-retreats]
visual:
  pattern: schema_timeline_with_lessons
  primary: "Timeline 2016 → Dec 2024 с точками incident / DMV suspension / mass layoffs / GM exit + блок 4 уровней failure"
---

# Cruise GM exit: centerpiece раздела

## Timeline (2016 → декабрь 2024)

- **2016** — GM покупает Cruise за $1+ миллиард.
- **2018-2022** — extensive funding, рост ODD от Phoenix → Phoenix + Сан-Франциско → multi-city.
- **2 октября 2023** — incident SF. Cruise robotaxi после столкновения пешехода с другим автомобилем протянул пострадавшую около 20 футов вместо немедленной остановки.
- **24 октября 2023** — California DMV отозвал лицензию Cruise.
- **Late 2023** — mass layoffs, freezing operations.
- **Декабрь 2024** — GM объявляет полный exit. $10+ миллиардов operating losses, <$500M cumulative revenue.

## Числа

- **$10+ миллиардов** operating losses 2016-2024.
- **<$500 миллионов** cumulative revenue за всю историю.
- **Соотношение 20:1** — на каждый доллар выручки сожжено 20 капитала.

## Четыре уровня failure pattern

- **Technical:** Cruise Observe-стек сработал (увидел пешехода), но Decide дал инструкцию «pull over», которая в контексте «пешеход под машиной» оказалась катастрофической. Это **provал второй стадии OODA-цикла**.
- **Business model:** capital intensity без commercial revenue. $10B vs <$500M — провал unit economics.
- **Regulatory / trust:** Cruise нарушила собственные правила прозрачности с DMV — представила инцидент менее severely, чем он был. DMV отозвал лицензию не за инцидент, а за coverup.
- **Cultural / organizational:** GM-Cruise hybrid culture — Cruise хотела двигаться fast, GM хотела квартальный отчёт. Misalignment затрудняло crawl-walk-run discipline.

## Lesson — survivor pattern vs Cruise pattern

- **Waymo:** crawl-walk-run, conservative ODD expansion, formal safety case.
- **Cruise:** rapid ODD expansion ради IPO timeline, нарушение transparency с регулятором.
- **Один dragging incident + DMV trust violation = killing program.**

## Speaker notes

Cruise GM exit — это centerpiece раздела три. Я хочу остановиться на три с половиной минуты, потому что этот кейс собирает все уроки лекции в одном месте.

Timeline. В 2016 году GM купила Cruise за миллиард+ долларов. С 2018 по 2022 — extensive funding, рост ODD от Phoenix к Phoenix плюс Сан-Франциско, потом multi-city. Cruise делал driverless ночные смены в SF к 2023 году, хотя только в очень ограниченной географии.

Второго октября 2023 года произошёл incident в Сан-Франциско. Cruise robotaxi после столкновения пешехода с другим автомобилем — не Cruise — протянул пострадавшую около двадцати футов, вместо немедленной остановки. Это технический failure — Cruise Observe-стек сработал, увидел пешехода, но Decide-логика дала инструкцию «pull over», и в контексте «пешеход под машиной» эта инструкция оказалась катастрофической. Это provал второй стадии OODA-цикла из Лекции 9.

Двадцать четвёртого октября 2023 — California DMV отозвал лицензию Cruise. Важно: DMV отозвал лицензию не только за сам инцидент, а за coverup. Cruise представила инцидент DMV менее severely, чем он был. DMV это обнаружил позже через independent investigation.

Late 2023 — mass layoffs, freezing operations. Cruise сократил большую часть персонала и заморозил most operations.

Декабрь 2024 — GM объявила полный exit. Десять+ миллиардов operating losses кумулятивно за восемь лет. Менее пятисот миллионов revenue. Соотношение двадцать к одному.

Цифры. Десять+ миллиардов сожжено. Менее пятисот миллионов выручки. На каждый доллар выручки сожжено двадцать долларов капитала. Это unit economics failure высочайшего порядка.

Четыре уровня failure pattern. Технический — provал второй стадии OODA. Business model — capital intensity без revenue. Regulatory and trust — нарушение transparency. Cultural and organizational — GM-Cruise hybrid culture misalignment.

Lesson. Это не «один инцидент уничтожил Cruise». Это «один инцидент плюс DMV trust violation» уничтожил Cruise. Если бы Cruise были honest с DMV, то incident мог быть остаточным происшествием, после которого Cruise мог бы recover. Но coverup был последней капля.

Survivor pattern vs Cruise pattern. Waymo делает crawl-walk-run. Cruise делала rapid ODD expansion ради IPO timeline и нарушение transparency с регулятором. Один dragging incident плюс trust violation = killing program. Это lesson инженерной этики, а не алгоритмическая ошибка.

Это lesson для вас — будущих инженеров. Когда вы работаете в технологической компании с regulator interaction — transparency с регулятором это не PR-вопрос. Это структурный survival вопрос. Cruise могла бы быть жива, если бы её leadership понимал это.
