VERDICT: APPROVE-CLEAN

# Fact-Checker Report — Семинар 7 (собранная дека) — 2026-10-11

Независимый фактчек Фазы 6, проведён по **собранной деке** — `library/seminars/sem-07/rendered/snapshots/iter-01..34.png`
(визуальный слой) сверен построчно с `library/seminars/sem-07/slides/n01..n34-*.md` (фронтматтер +
заметки), а не по исходникам `rework/*.md`. Каждый факт перепроверен заново через прямой `curl`/`WebFetch`/
`WebSearch` по правилу §8.7 канона семинаров (отрицательный ответ не повод считать источник
недоступным — два источника в этом проходе сначала дали 403/451/DNS-отказ через `WebFetch` и были
подтверждены прямым `curl` или `WebSearch`).

## Severity counts

- P0 (false fact / broken citation / direction inversion / misquote): **0**
- P1 (missing source / suspicious number without caveat / freshness expired): **0**
- P2 (cite format / minor nuance): **2**

Сам проход этой сессии производства уже поймал и исправил один случай неподтверждённых цифр
(Zillow «~65%/$500M+» → заменено на проверенные $304,4 млн/$407,9 млн, задокументировано в
`rework/section-1-chaining-otchet.md` §3) — этот проход его не повторяет, независимо перепроверяет
итоговые цифры и не находит новых аналогичных случаев ни в одном из шести кейсов.

## Кейс 1 — Zillow Offers (n13–n15)

| Факт | Источник на слайде | Проверка | Вердикт |
|---|---|---|---|
| $304,4 млн списание за 3кв2021 | CNN 9 нояб. 2021 | SEC 8-K (`sec.gov/.../exhibit993.htm`): «recorded a $304.4 million write-down of inventory... third quarter 2021» — дословное число, точнее, чем округлённые «$304 million» в тексте самой CNN-статьи (подтверждено прямым `curl` CNN, HTTP 200, текст: «$304 million inventory write-down in the third quarter») | VERIFIED |
| $407,9 млн за весь 2021 год | форма 10-K перед SEC | SEC 10-K (`sec.gov/.../z-20211231.htm`): «write-down to inventory totaling $407.9 million» для года, закончившегося 31.12.2021 | VERIFIED |
| 2000 рабочих мест / 25% штата | CNN | CNN (прямой `curl`): «plans to cut 2,000 jobs, or 25% of its staff» — дословное совпадение | VERIFIED |
| Закрытие объявлено 2 нояб. 2021 | — | CNN текст статьи от 9 нояб. подтверждает «announced last week»; SEC 8-K датирован 02.11.2021 | VERIFIED |
| Цитата Рича Бартона | CNN | CNN дословно: «"unpredictability in forecasting home prices" that "far exceeds" what the company had expected» — ровно то же усечение, что на слайде | VERIFIED (точная цитата, не искажена) |
| Остин: 27%/год (Zillow, 4 года) vs ~6%/год (Case-Shiller) | Fortune 3 нояб. 2021 | Fortune напрямую (`curl`, HTTP 200): «homes have appreciated by an average of 6% per year... according to... Case-Shiller» vs «Zillow had paid... represented a 27% annual price increase... looking back over a four-year period» — точное совпадение чисел и периода | VERIFIED |
| Похожий разрыв >20%/год — Сакраменто, Портленд, Цинциннати, Тампа, Феникс, Денвер | Fortune | Fortune дословно называет те же шесть городов тем же порядком: «In Sacramento, Portland, Ore., Cincinnati, Tampa, Phoenix, and Denver... a run-up of more than 20% per year» | VERIFIED |
| Листинг +5% / скидка в среднем −6% / чистый убыток ≈2% | Fortune | Fortune дословно: «list its houses at an average 5% markup»; «discounts, averaging about 6%»; «a 2% loss if it managed to sell... at... current listing prices» | VERIFIED |
| Callback к Лекции 5 §5.4 (рамка мониторинга жизненного цикла, multiwindow burn-rate, отсутствие быстрого circuit breaker) | — | Сверено с `library/lectures/lec-05/chapter-part3.md` §5.4: та же пара чисел $304,4 млн / $407,9 млн, тот же диагноз («у Zillow не было ни короткого, ни длинного окна», отсутствие быстрого слоя часы-дни с автоматическим порогом остановки). Описание того, что было в Лекции 5, на слайде n14 не искажено | VERIFIED |

Полная сверка — ни один из первоначально отвергнутых чисел («~65%», «$500 млн+») не просочился в
видимый слой или в живое утверждение заметок; обе строки, где встречается «65%», — внутри backup-поля
фронтматтера n13/n14, и это запись о том, какая цифра была отклонена Фазой 3, а не используемый факт
(см. §8.10 канона — запись о прошлом, не живое утверждение).

## Кейс 2 — Octomind / LangChain (n16–n18)

| Факт | Проверка | Вердикт |
|---|---|---|
| «We could just code» | Блог через Wayback Machine (прямой `curl`, `octomind.dev` не резолвится из песочницы — сетевое ограничение, не признак отсутствия источника): дословно «We could just code.» | VERIFIED (точная цитата) |
| 1 класс/1 вызов (прямой API) vs 3 класса/4 вызова (LangChain) | Блог дословно: «This is simple code... containing a single class and one function call»; «We now have three classes and four function calls» | VERIFIED |
| Три новых понятия — шаблон промпта, парсер вывода, «цепочка» (переопределяет `\|`) | Блог дословно: «three new abstractions: Prompt templates... Output parsers... Chains: LangChain's "LCEL syntax" overriding Python's \| operator» | VERIFIED |
| LangChain в проде «до середины 2024» | Блог: «used LangChain in production for over 12 months, starting in early 2023 then removing it in 2024» — точного «mid-2024» в тексте нет, но HN-обсуждение поста датировано 20 июня 2024 (середина года) — формулировка слайда согласуется, не противоречит | VERIFIED (с уточнением: «mid-2024» — разумная интерпретация даты публикации/обсуждения, не прямая цитата блога) |
| HN: 480 очков, 297 комментариев, 20 июня 2024 | Прямой `curl` на `news.ycombinator.com/item?id=40739982` (WebFetch вернул 403, подтверждено §8.7): «480 points by ma_za on June 20, 2024... 297 comments» | VERIFIED |
| Цитата «пять слоёв абстракции...» (комментарий HN) | HN-страница дословно: «you have to go through 5 layers of abstraction just to change a minute detail» | VERIFIED |
| Anthropic, Building Effective Agents (2024): «найди простейшее решение» | Anthropic Dec 2024: «we recommend finding the simplest solution possible, and only increasing complexity when needed» — смысл передан верно; русская фраза в кавычках — перевод, не дословная выписка английского оригинала | P2: формат цитаты — переведённая фраза в «» рядом с несколькими словами перевода без кавычек создаёт лёгкую двусмысленность (см. ниже) |

## Кейс 3 — Jev / TypeSafe AI (n19–n23, vfy_day_of)

| Факт | Проверка | Вердикт |
|---|---|---|
| Decision-модель / «System One» | Simon Willison (simonwillison.net/2026/Sep/21/jev/, WebFetch успешно): «their inaugural "System One model"»; Wikipedia «Jev (AI model)»: «the first "System One model"» | VERIFIED |
| Запуск 15.09.2026 (в backup/frontmatter, не на видимом слое) | Wikipedia: «released Jev on "September 15, 2026"»; Willison (опубликовано 21.09.2026): «unveiled last week» (≈14 сент.) — расхождение в 1 день между «14» и «15» сентября, не влияет на видимый слой (дата там не показана студентам) | VERIFIED (минорная 1-дневная неточность в источниках друг против друга, не на слайде) |
| Эксперимент Bay Area: Купертино выше всех, Восточный Пало-Альто ниже всех | Willison дословно: «Cupertino scored highest while East Palo Alto ranked lowest» | VERIFIED |
| Формат ответа Jev — число, не причина; риск скрытой предвзятости | Willison: «Unlike traditional LLMs that can explain reasoning, Jev returns only floating-point numbers... warns against using it for hiring decisions» | VERIFIED |
| $0,042/млн входных токенов (упомянуто в задании фактчека, НЕ присутствует на видимом слое и НЕ в заметках ни одного слайда sem-07) | Willison: «Input costs $0.042 per million tokens, with free output» — само число подтверждено, но на слайдах n19–n23 оно не используется вовсе (грепом по всей деке — ноль вхождений `0,042`/`0.042`) | VERIFIED как факт-источник, но **на деке отсутствует** — нечего фактчекать на видимом слое |
| «Kev» — открытый клон на Qwen 3.5, модели 0.8B/4B/9B (только в `vfy_day_of_note`, backup-поле n22, НЕ часть истории для студента) | Подтверждено WebSearch: реальный проект (`github.com/jaredpalmer/kev`), «family of small decision models built on Qwen3.5 and Qwen3.8»; размеры моделей в источниках указываются по-разному (0.8B/4B/9B в одних описаниях, 0.8B–27B в других) — ядро утверждения («Kev» существует, построен на Qwen3.5, open-source клон Jev) подтверждено | VERIFIED (флаг `vfy_day_of` остаётся корректным и актуальным на 11.10.2026 — расстановка не изменилась настолько, чтобы требовать правки видимого слоя) |

Ничего из кейса Jev не искажено на видимом слое. `vfy_day_of` флаг (n22/n23) отработал как задумано:
production-сессия уже сверила оба источника напрямую `curl` 2026-10-11 и получила контент с обеих
страниц (без ложного «источник недоступен»).

## Кейс 4 — Optum/UnitedHealth, Obermeyer et al. (n25–n28)

| Факт | Проверка | Вердикт |
|---|---|---|
| Obermeyer, Powers, Vogeli, Mullainathan, Science, 2019, DOI 10.1126/science.aax2342 | science.org метаданные через WebSearch: «Science, 25 October 2019, Volume 366, Issue 6464» — DOI совпадает буквально | VERIFIED (на деке дата не уточняется до дня — только «Science, 2019», что не противоречит точной дате 25.10.2019) |
| 17,7% → 46,5% (доля чёрных пациентов, направленных в программу усиленного наблюдения, после исправления алгоритма) | UC Berkeley пресс-релиз (news.berkeley.edu, через WebSearch): «increase the percentage of Black patients receiving additional help from 17.7 to 46.5%» — дословное совпадение обоих чисел | VERIFIED |
| ≈200 млн человек/год | IEEE Spectrum (WebFetch): «these types of algorithms are making health decisions for 200 million people per year» | VERIFIED |
| Алгоритм — продукт Optum (подразделение UnitedHealth) | WebSearch (STAT News/healthcarefinancenews/Berkeley): «reporters quickly identified it as Impact Pro, sold by Optum, a subsidiary of UnitedHealth Group» | VERIFIED |
| Прошлые расходы как прокси потребности → искажение из-за неравного доступа к медицине у чёрных пациентов | Подтверждено всеми источниками (Berkeley, Chicago Booth, Lancet) | VERIFIED |

## Кейс 5 — IRS audit-selection (n29–n32)

| Факт | Проверка | Вердикт |
|---|---|---|
| 2,9–4,7× чаще аудит чернокожих налогоплательщиков | Stanford SIEPR напрямую (WebFetch) + WebSearch по рабочей статье «Measuring and Mitigating Racial Disparities in Tax Audits»: «Black taxpayers have their tax returns audited between 2.9 to 4.7 times the rate of non-Black taxpayers» — точное число, не округление | VERIFIED |
| EITC — главный драйвер разницы | SIEPR/WebSearch подтверждают: «Earned income tax credit (EITC) claims were identified as the main driver of this disparity» | VERIFIED |
| IRS сама подтвердила результат, объявила об исправлении | SIEPR (WebFetch): письмо комиссара IRS Danny Werfel от 15.05.2023: «an initial review of its auditing process confirms the results of a Stanford study»; «pledged to implement changes before the next tax filing season» | VERIFIED |
| Механизм: дешевизна проверки + отношение возврата к доходу (не раса впрямую) | Соответствует описанию исследования во всех источниках | VERIFIED |
| «Совместным исследованием Stanford и самой IRS, 2023» (формулировка на слайде n32) | Фактически: Stanford провёл независимое исследование (возможно, с доступом к анонимизированным данным IRS по соглашению), январь 2023; IRS подтвердила результат отдельно в мае 2023, после совместной проверки с исследователями | P2: формулировка «совместное исследование» слегка опережает хронологию источников — точнее было бы «исследование Stanford, подтверждённое IRS после совместной проверки» (разница не меняет само число 2,9–4,7×, не искажает факт признания IRS) |

## Кейс 6 — Внутренние cross-references (Лекция 3, Лекция 5)

| Ссылка | Где на слайде | Проверка | Вердикт |
|---|---|---|---|
| Workflow vs Agent — та же таксономия, что в Лекции 3 §4.3, со ссылкой на Anthropic Building Effective Agents (2024) | n07 | `library/lectures/lec-03/chapter-part3.md` §4.3 содержит ровно то же различение теми же терминами и той же ссылкой на Anthropic (2024) | VERIFIED |
| Атрибуция формулировки «Nate Herk» (только в frontmatter `learning_goal`/`backup`, НЕ на видимом слое — видимый текст говорит обезличенно «у создателей контента об автоматизации на базе ИИ») | n07 (backup-поле) | Nate Herk — реальный автор контента про n8n/AI-автоматизацию (подтверждено WebSearch: `builtwithagents.ai`, `agnt.gg` цитируют его framework «deterministic logic when reliability matters... reserve "agent" for judgment-heavy steps»). Имя не выдумано, атрибуция правдоподобна, хотя прямого источника с точной формулировкой не найдено — сама production-сессия уже честно пометила это как непроверенное в backup-поле | VERIFIED как «имя реально, не халлюцинация» (само поле уже помечено производственной сессией как не до конца проверенное — это корректная практика, P0 не присваивается, т.к. поле не достигает студента) |
| Правило лестницы («справится ли один промпт или один вызов + RAG — так и сделайте»), глава Лекции 3 | n06 | `lec-03/chapter-part3.md`/`chapter-part4.md`: «лестница архитектур (промпт → RAG → workflow → агент → мульти-агент)» — то же правило, та же логика | VERIFIED |
| Callback к Лекции 5 §5.4 — Zillow разбирался «через рамку мониторинга жизненного цикла модели» | n14 | Сверено выше (кейс 1) — описание механизма Лекции 5 не искажено | VERIFIED |

## Числа на слайдах вне списка задания — отдельная проверка

Полный греп по всем 34 файлам слайдов на числовые паттерны (`%`, `млн`, `млрд`, `$`, `×`) не выявил
ничего вне шести перечисленных кейсов. Единственное замеченное число вне прямого фокуса задания —
«65%» внутри backup-поля n13/n14 — разобрано выше как запись об отклонённой цифре, не факт.

На видимом слое и в заметках **нет** отдельного упоминания цены Jev ($0,042/млн токенов) — пункт из
брифа фактчека, по которому прямо сказано «если есть на слайде»: его нет, поэтому нечего верифицировать
на уровне деки (сам факт как таковой подтверждён в ходе проверки источника).

## Render vs source — выборочная сверка (канон §7: «проверка на язык не видит того, что нарисовано»)

Сверены визуальные снимки iter-14, iter-17, iter-22, iter-23, iter-28, iter-32 (соответствуют n14,
n17, n22, n23, n28, n32 по порядку `deck.yaml`) против markdown источников построчно — PNG-слой
совпадает с фронтматтером slide-файлов дословно, расхождений рендера с источником не найдено.

## DISPUTED / FALSE facts

Нет. Ни один факт в шести кейсах не оказался ложным или инвертированным по направлению.

## NEEDS-CITATION

Нет пропущенных источников — каждая цифра в шести кейсах имеет явную атрибуцию на слайде и
подтверждённый первоисточник.

## UNVERIFIABLE

Нет. Все источники, по которым `WebFetch` изначально вернул отказ (CNN — 451, HN — 403, Science.org
DOI — 403, Octomind — DNS-отказ в песочнице), были успешно прочитаны напрямую `curl`/`WebSearch`/
Wayback Machine по правилу §8.7 — ни один факт не остался непроверенным из-за инструментальной
ошибки.

## P2 — минорные замечания (не блокируют)

1. **n18** — цитата Anthropic «найди простейшее решение» дана в кавычках как короткий перевод
   английской фразы «finding the simplest solution possible», с продолжением без кавычек. Технически
   это соответствует духу правила цитирования (переведённая прямая цитата не обязана быть
   побуквенным аналогом английского оригинала), но стоит удостовериться при литературной редактуре
   (Фаза 7), что граница «это цитата / это пересказ» читается однозначно.
2. **n32** — формулировка «подтверждено совместным исследованием Stanford и самой IRS, 2023»
   слегка опережает фактическую хронологию (независимое исследование Stanford, январь 2023 →
   отдельное подтверждение IRS, май 2023, после совместной проверки данных). Сама цифра 2,9–4,7× и
   факт признания IRS — верны; формулировка «совместное» можно уточнить при желании, не обязательно.

## Топ-N правок до публикации

Правок, требующих действия перед показом, **нет**. Оба P2 — стилистические наблюдения, не искажающие
факт, фиксируются для возможной правки на усмотрение литературного редактора (Фаза 7), не для
возврата на доработку содержания.
