---
id: s19
type: assertion_visual
duration_min: 3
assertion: "«Excessive automation at Tesla was a mistake. Humans are underrated» — Musk, апрель 2018. Канонический урок automation paradox."
learning_goal: "Tesla 2018 canonical case + Bainbridge 1983 + Toyota alternative"
learning_outcomes: [LO2, LO8]
chapter_ref: "§2.4 Tesla 2018 deep-dive"
failure_bucket: strict_in
references: [musk-2018-tweet, bainbridge-1983, imd-tesla-case]
visual:
  pattern: timeline_with_quote
  primary: "Timeline Q1 2018 + цитата Маска + IMD root cause"
---

# Tesla 2018 — канонический урок automation paradox

## Что произошло (Q1 2018)

**Target:** 2 500 Model 3 per week.

**Реально:** 2 020 per week.

**13 апреля 2018, твит Маска:** «Yes, excessive automation at Tesla was a mistake. To be precise, my mistake. Humans are underrated.»

CBS interview тот же день: «We had this crazy complex network of conveyor belts and it was not working, so we got rid of that whole thing.»

## Что не сработало

Conveyor system Model 3 — «we got rid of that whole thing».

Робот-«fluffer» для fiberglass mats.

Over-automated battery module assembly.

## Корневая причина (IMD case)

Tesla заменял людей **там, где variability — feature, не bug.**

Сборка автомобиля — это miles of edge cases: разные конфигурации, разные ракурсы установки, разные допуски. Человек справляется с variability через judgment. Робот — через жёсткие spec, где variability ломает программу.

## Структурный урок: automation paradox (Bainbridge 1983)

**Чем больше автоматизация, тем критичнее остающиеся операторы.** В нештатной ситуации они должны быстро среагировать — но если 99% времени они только наблюдают, навык атрофируется.

Tesla 2018 — практическая иллюстрация Lisanne Bainbridge «Ironies of Automation», 1983.

## Альтернатива

Toyota Production System + Jidoka — augment, не replace. **Работает с 1950-х** на том же типе продукта.

## Speaker notes

Tesla 2018 — это канонический урок для этой лекции и для всей карьеры в industrial AI. Запомните детали.

Q1 2018. Tesla обещал миру 2500 Model 3 в неделю — это был ориентир, по которому Wall Street оценивал Tesla. Реально производили 2020 в неделю, и компания горела деньгами. Маск спал на заводе во Fremont. Это называлось «production hell».

13 апреля 2018 года, твит Маска: «Yes, excessive automation at Tesla was a mistake. To be precise, my mistake. Humans are underrated». Я переведу: чрезмерная автоматизация в Tesla была ошибкой. Если точнее — моей ошибкой. Людей мы недооценили.

В CBS интервью тот же день Маск рассказал конкретику: «у нас была crazy complex network of conveyor belts, и она не работала, мы избавились от неё целиком». Они физически демонтировали конвейерную систему сборки Model 3, потому что робот-конвейер не справлялся с разнообразием конфигураций машины. Демонтировали также робота-«fluffer», который раскладывал fiberglass-маты на battery module — этот робот лучше справлялся в видео, чем на конкретном узле.

Что было корневой причиной. IMD Business School разобрал этот случай как case study. Корневая причина: Tesla заменял людей там, где variability — это feature, а не bug. Сборка автомобиля — это десятки тысяч edge cases. Разные конфигурации, разные ракурсы установки, разные допуски на конкретной партии деталей. Человек справляется с variability через judgment — увидел странность, оценил, скорректировал. Робот справляется через жёсткие spec — если variability выходит за spec, программа ломается.

И вот структурный урок: automation paradox. Это концепция Лизан Бейнбридж из 1983 года, статья «Ironies of Automation». Бейнбридж сказала: чем больше автоматизация, тем критичнее остающиеся операторы. В нештатной ситуации они должны быстро вмешаться. Но если 99 процентов времени они только наблюдают, не действуя — навык атрофируется. Когда нештатная ситуация случается, оператор не готов. И тогда автоматизация, которая должна была повысить надёжность, становится источником нового класса отказов.

Bainbridge написала это в 1983 году про авиацию и атомные станции. Tesla 2018 — практическая иллюстрация ровно того же принципа в новом контексте.

Альтернатива — Toyota Production System и Jidoka, о которых мы говорили на предыдущем слайде. Toyota работает с 1950-х годов на том же типе продукта, дёт Camry, RAV4, Corolla. Toyota не пыталась заменить рабочих целиком. Toyota дополняет рабочих. И Toyota построил завод в Texas, который собирает почти столько же машин в год, сколько Tesla, но с другой парадигмой.

Это не идеологическая дискуссия. Это инженерное наблюдение: где variability — feature, replace не работает. Augment — работает.
