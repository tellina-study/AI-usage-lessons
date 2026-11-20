---
title: "Лекция 8 (trust-recognition) — внешне верифицированные кейсы, расширение реестра issue #349"
type: research
issue: "#349"
date: 2026-11-20
---

# Лекция 8 — trust-recognition: 23 внешне верифицированных кейса (2022–2026)

## Подход к поиску

Отрасль — биометрия (лицо/голос/радужка), детекция дипфейков, доверенные системы идентификации.
Задача: не передокументировать кейсы лекции (`razmetka/lec-08.md`, `lec-08-os4.md` — уже 22 строки
в каноническом реестре), а найти **новые**, независимо проверяемые кейсы с реальным URL,
конкретной цифрой, датой и именованным инструментом/продуктом. Поиск вёлся сериями
`WebSearch` по под-темам: (а) биометрия на границах/в аэропортах/в рознице/в банках —
production-деплои с заявленной точностью; (б) провалы распознавания лиц правоохранительными
органами (wrongful arrest, FTC-дела); (в) дипфейк-мошенничество (видео-звонки, робоколлы,
голосовой клон против банка); (г) академические/бенчмарк-работы о генерализации детекторов
дипфейков; (д) институциональные провалы (суды, регуляторы, банкротства/расчёты).
Несколько находок добавлены WebFetch-проверкой даты/цифр напрямую на первоисточник, когда
summary поисковика было недостаточно точным (пример: HSBC VoiceID — первый найденный пресс-релиз
оказался за 2020/2019 год и был **отбракован** как вне окна 2022–2026, а не использован с чужой
датой).

**Покрытие по годам — все пять лет закрыты с обеих сторон.** Успех: 2022 (Mastercard/Payface),
2023 (Changi, NIST FRTE/FATE), 2024 (CLEAR, Apple Vision Pro, NEC/Зимбабве, Ferrari), 2025 (World
ID/Orb, Reality Defender), 2026 (CBP — веха октября 2026). Провал: 2022 (IRS/ID.me), 2023 (Rite
Aid дело началось в декабре 2023 по нарушениям 2012–2020; Detroit/Woodruff; Пентагон-фейк;
Worldcoin/Кения; Lloyds/голосовой клон), 2024 (Arup; робоколл Байдена; Южная Корея/Telegram;
Metropolitan Police), 2025 (Clearview-settlement; коллапс точности детекторов дипфейков), 2026
(индикт на $129М голосового клонирования). Ни один год не закрыт искусственно слабым кейсом —
слабых мест в покрытии не осталось.

**Честная оговорка по качеству источников.** Цифры успеха у частных компаний (CBP, CLEAR,
Mastercard/Payface, Apple, NEC/Zimbabwe, World/Worldcoin, Reality Defender) — **самоотчётные**,
взяты из пресс-релизов или вендорских/околовендорских публикаций (biometricupdate.com,
idtechwire.com), без независимого аудита точности в духе NIST. Отдельно НЕ включён кейс Aadhaar
(UIDAI) — предварительный поиск дал **несовпадающие** цифры неуспеха аутентификации (6,5% в одних
источниках, до ~30% в других за январь–апрель 2025 по face-auth) без ясной методологической
сверки баз — ровно та ситуация «две цифры разошлись», когда безопаснее не включать кейс, чем
штамповать спорное число. Это осознанный пробел, не упущение. Провальные кейсы, где источник —
суд/регулятор (FTC, FCC, суд Illinois по BIPA) — качественно надёжнее: решение/штраф — это и есть
зафиксированный исход, а не чьё-то измерение.

## Таблица

| case_name | year | source_url | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US CBP — биометрическое сравнение лиц на границе (1 млрд+ пассажиров, >98% точность, вехa) | 2026 | [idtechwire — CBP 1 Billion Travelers](https://idtechwire.com/cbp-says-facial-biometrics-have-verified-more-than-1-billion-travelers/) | low | none | seconds-minutes | F-C | deep-learning | yes | medium | not-applicable | success | medium |
| CLEAR Plus — биометрическая идентификация в аэропортах (43,5 млн участников, +30% г/г) | 2024 | [ID Tech — CLEAR 43.5M Members](https://idtechwire.com/clear-reaches-43-5-million-members-as-q2-revenue-rises-27-percent/) | low | none | seconds-minutes | F-C | deep-learning | yes | low | not-applicable | success | high |
| Changi Airport FAST (IDEMIA) — биометрический выезд без паспорта, 25с→10с | 2023 | [IDEMIA — Changi FAST](https://www.idemia.com/singapores-changi-airport-terminal-4-idemia-fast-and-seamless-travel) | low | none | seconds-minutes | F-C | deep-learning | yes | low | not-applicable | success | high |
| NIST FRTE/FATE Feb 2023 — Idemia 99,88% на 12 млн лиц (1:N mugshot) | 2023 | [NIST IR 8491](https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8491.pdf) | moderate | none | seconds-minutes | none | deep-learning | not-applicable | unclear | not-applicable | success | high |
| Mastercard / Payface — «pay by smile», пилот 5 супермаркетов Сан-Паулу | 2022 | [biometricupdate — Mastercard Brazil pilot](https://www.biometricupdate.com/202205/mastercard-launches-retail-biometrics-program-with-brazil-pilot) | low | none | seconds-minutes | F-C | deep-learning | yes | low | not-applicable | success | medium |
| Apple Vision Pro Optic ID — радужка, заявлен FAR 1 к 1 000 000 | 2024 | [Apple — Face ID/Optic ID security](https://support.apple.com/guide/security/face-id-touch-id-optic-id-and-passwords-sec067eb0c9e/web) | low | none | seconds-minutes | F-C | deep-learning | yes | low | not-applicable | success | medium |
| NEC NeoFace Watch — полиция Зимбабве опознаёт и задерживает подозреваемую с фальшивым паспортом | 2024 | [IntelligentCIO — NEC XON NeoFace Watch, Zimbabwe](https://www.intelligentcio.com/africa/2024/05/13/facing-justice-zimbabwes-police-nail-criminal-syndicate-with-nec-xons-neoface-watch/) | moderate | none | hours-days | F-A | deep-learning | yes | medium | not-applicable | success | medium |
| World ID / Worldcoin Orb — 16,9 млн верифицированных людей, 1500+ Orb в 23 странах | 2025 | [PR Newswire — Eightco/World 16.9M verified humans](https://www.prnewswire.com/news-releases/eightco-holdings-inc-orbs-announces-16-9-million-verified-world-humans-adding-1-9-million-since-launching-worldcoin-treasury-just-3-weeks-ago-302569218.html) | moderate | none | seconds-minutes | F-C | deep-learning | unclear | unclear | not-applicable | success | medium |
| Reality Defender — банк в проде: 2,4 млн+ звонков, ~1010 синтетических голосов пойманы | 2025 | [Reality Defender — AI Voice Fraud financial institutions](https://www.realitydefender.com/insights/ai-voice-fraud-is-targeting-financial-institutions) | high | none | seconds-minutes | F-C | deep-learning | yes | medium | not-applicable | success | medium |
| Ferrari — руководитель распознал дипфейк-видеозвонок «CEO» вопросом о книге, сделка не прошла | 2024 | [Carscoops — Ferrari exec foils deepfake CEO call](https://www.carscoops.com/2024/07/ferrari-ceo-impersonator-uncovered-by-colleague-in-deepfake-call/) | high | none | seconds-minutes | F-C | sensor-fusion | yes | high | not-applicable | success | medium |
| IRS / ID.me — обязательное распознавание лиц для доступа к налоговому аккаунту отменено | 2022 | [Washington Post — IRS abandons ID.me face scans](https://www.washingtonpost.com/technology/2022/02/07/irs-idme-face-scans/) | moderate | none | weeks-months | F-A | deep-learning | no | medium | yes | failure | high |
| Rite Aid — запрет FTC на лицевое распознавание на 5 лет (ложные обвинения в кражах, расовый перекос) | 2023 | [FTC — Rite Aid press release](https://www.ftc.gov/news-events/news/press-releases/2023/12/rite-aid-banned-using-ai-facial-recognition-after-ftc-says-retailer-deployed-technology-without) | high | U3 | season-years | F-B | deep-learning | no | high | no | failure | high |
| Детройт — Porcha Woodruff, ошибочный арест беременной женщины по распознаванию лиц | 2023 | [AP via WHEC — Woodruff lawsuit](https://www.whec.com/ap-top-news/woman-wrongly-accused-of-carjacking-loses-lawsuit-against-detroit-police-who-used-facial-tech/) | high | U3 | hours-days | F-A | deep-learning | no | high | no | failure | high |
| Фейковое фото «взрыва у Пентагона» (ИИ) — вирусный хайп, краткая просадка рынка ~$500 млрд | 2023 | [NPR — fake viral Pentagon images AI](https://www.npr.org/2023/05/22/1177590231/fake-viral-images-of-an-explosion-at-the-pentagon-were-probably-created-by-ai) | high | U2 | seconds-minutes | F-C | foundation-model | no | high | no | failure | medium |
| Worldcoin / Кения — приостановка сканирования радужки регулятором (350 000+ уже зарегистрированы) | 2023 | [TechCrunch — Kenya suspends Worldcoin scans](https://techcrunch.com/2023/08/02/kenya-suspends-worldcoin-scans-over-security-privacy-and-financial-concerns/) | moderate | none | weeks-months | F-A | deep-learning | no | medium | yes | failure | high |
| Lloyds Bank Voice ID обойдена клонированным голосом (ElevenLabs, журналист VICE) | 2023 | [VICE/Motherboard via Futurism — journalist clones voice, breaks into bank](https://futurism.com/the-byte/journalist-clones-voice-break-into-bank) | extreme | U1 | seconds-minutes | F-C | foundation-model | no | high | no | failure | high |
| Arup — дипфейк-видеозвонок «CFO» + коллеги, 15 переводов, $25 млн, Гонконг | 2024 | [CNN — Arup deepfake scam](https://www.cnn.com/2024/05/16/tech/arup-deepfake-scam-loss-hong-kong-intl-hnk) | extreme | U1 | seconds-minutes | F-C | sensor-fusion | no | catastrophic | no | failure | high |
| Робоколл с клонированным голосом Байдена (Нью-Гэмпшир) — штраф FCC $6 млн | 2024 | [NPR — FCC fines deepfake Biden robocall](https://www.npr.org/2024/05/23/nx-s1-4977582/fcc-ai-deepfake-robocall-biden-new-hampshire-political-operative) | high | U1 | weeks-months | F-A | foundation-model | no | high | no | failure | high |
| Южная Корея — Telegram-скандал с дипфейк-порно в школах/вузах, 781 жертва за 2024 (рост ×11 к 2018) | 2024 | [ABC News (AU) — South Korea deepfake pornography Telegram](https://www.abc.net.au/news/2024-09-08/south-korea-deepfake-pornography-telegram-app-sex-crimes/104314174) | high | U3 | season-years | F-B | deep-learning | no | high | mixed | failure | high |
| Metropolitan Police — живое распознавание лиц: внутренний 0,0003% ложных vs внешние «1 из 40» и 231 арест на 160 000 сканов | 2024 | [Hyphen — StopWatch: Met LFR ineffective](https://hyphenonline.com/2024/10/23/live-facial-recognition-used-by-met-police-is-ineffective-says-monitoring-group/) | unclear | unclear | hours-days | F-C | deep-learning | yes | medium | no | partial | low |
| Clearview AI — расчёт по иску BIPA: 23% акций вместо денег, 125 000 участников класса | 2025 | [The Record — Clearview AI $50M settlement](https://therecord.media/clearview-ai-illinois-class-action-lawsuit-settlement) | unclear | none | season-years | F-A | deep-learning | no | high | mixed | partial | high |
| «Fit for Purpose?» (2025) + Meta DFDC — детекторы дипфейков: 95–98% в лаборатории → до 65% вживую, топ-коммерческий ошибается 1 раз из 5 на материале 2024 | 2025 | [arXiv 2510.16556 — Fit for Purpose? Deepfake Detection in the Real World](https://arxiv.org/abs/2510.16556) | extreme | U2 | season-years | F-B | deep-learning | not-applicable | unclear | no | failure | high |
| Индикт на $129 млн — голосовой/видео-клон CEO/юристов против больниц, банка, фонда, 18 месяцев | 2026 | [Resemble.ai — $129M AI voice cloning fraud scheme incident](https://www.resemble.ai/learn/deepfake-incident-database/incidents/three-men-charged-in-alleged-dollar129-million-ai-voice-cloning-fraud-scheme) | extreme | U1 | season-years | F-B | sensor-fusion | no | catastrophic | no | failure | medium |

**Итог по счёту:** 10 успехов, 12 провалов, 1 частичный (`partial` — Metropolitan Police) +
1 частичный (`partial` — Clearview settlement) = 23 кейса, из них 10 success / 12 failure / 2
partial. Оба минимума (≥10 success, ≥10 failure) выполнены без натяжек.

## Что это добавляет к рамке осей (контрпримеры и подтверждения — названы прямо)

- **Подтверждение «гейт — сильнейший предиктор».** Ferrari (success, гейт=yes — внешний
  контрольный вопрос) против Arup и индикта на $129М (оба failure, гейт=no — решение принято внутри
  самого скомпрометированного канала без независимой проверки) — тот же паттерн, что и
  KnowBe4/«Famous Chollima» внутри самой лекции 8 (`razmetka/lec-08.md`), теперь с тремя новыми
  независимыми внешними кейсами на обе стороны.
- **Контрпример-напряжение внутри одной технологии.** Один и тот же продукт (Worldcoin/World ID,
  иридодиагностика через Orb) — `success` в глобальной метрике масштаба 2025 года и `failure` в
  Кении 2023 года **для того же базового механизма сканирования**. Разница — не в точности
  распознавания радужки, а в институциональном контексте (согласие, регулирование) — это прямо
  иллюстрирует, что `external_driver` иногда решает исход сильнее, чем сама техническая ось.
- **«Две цифры разошлись» — живой пример внутри реестра, не только в заметках памяти.**
  Metropolitan Police: сам департамент считает 0,0003% ложных срабатываний (знаменатель — все лица,
  увиденные камерой), независимые наблюдатели считают «1 из 40» (знаменатель — только
  сработавшие алерты) — при этом гейт формально есть (`axis4_gate=yes`, офицер проверяет алерт
  перед остановкой), а исход всё равно спорный. Помечено `outcome=partial`, `confidence=low`
  осознанно, а не притянуто к одной стороне.
- **Подтверждение «потолок попытки ≠ потолок успеха» для foundation-model/deep-learning на
  экстремальной неопределённости.** «Fit for Purpose?» (2025) — прямое количественное
  подтверждение паттерна L08-004 этой же лекции (XceptionNet 0,997→0,482 AUC на новом
  генераторе): детекторы дипфейков **пытаются** работать вплоть до extreme-неопределённости
  (это и есть их заявленное назначение), но генерализация вне обучающего распределения
  обваливается — ровно механизм U2, теперь подтверждённый вторым независимым источником 2025 года,
  а не только академической статьёй 2022–2023 годов, уже использованной в самой лекции.
- **Низкая неопределённость + узкая задача verification (1:1) держит высокую заявленную точность
  устойчиво по всем годам 2022–2026** (CBP, Changi, NIST, Mastercard, Apple) — контраст с
  identification/detection-задачами (1:N watchlist, детекция дипфейка, «узнать голос без
  предупреждения») уровня high/extreme, которые либо провалились (большинство новых failure-кейсов
  этого файла), либо держатся только при явном гейте (Ferrari, Reality Defender с человеком в
  контуре).

---

## Батч 2 (третья волна, 2026-11-20) — добавлено 28 кейсов: V08-024…V08-051

Полные таблицы с осями, описаниями и источниками — `../verified-cases-batch2/lec-08-verified-batch2.md` (файл provenance; локальные номера там — S1/F1/B2-S1 и т.п., НЕ финальные ID). Консолидация в `reestr-reshenij-verified.csv` — скриптом `build_verified_batch2.py` (дедуп + enum-валидация), разбор дублей — файл 18 §1.

Исключены при консолидации как дубли: Retool/Fortress Trust (то же событие, что V14-013); WPP дипфейк-атака (то же событие, что L14-071).

| final_id | case_name | year | outcome |
|---|---|---|---|
| V08-024 | UK-энергокомпания — голосовой дипфейк «немецкого CEO» вынудил перевести €220 тыс. ($243 тыс.) венгерскому поставщику | 2019 | failure |
| V08-025 | Банк в ОАЭ — «deep voice»-клон голоса директора компании, перевод $35 млн на подтверждение несуществующей сделки | 2020 | failure |
| V08-026 | Детройт — Robert Williams, ошибочный арест по распознаванию лиц (DataWorks Plus), $300 тыс. урегулирование в 2024 | 2020 | failure |
| V08-027 | Нью-Джерси — Nijeer Parks, арест по размытому фото из распознавания лиц, 10 суток в СИЗО | 2019 | failure |
| V08-028 | Джорджия/Луизиана — Randal Reid, арест по единственному совпадению распознавания лиц в штате, где он никогда не был, $200 тыс. урегулирование | 2022 | failure |
| V08-029 | Clearview AI — штраф ICO Великобритании £7,5 млн за биометрию британцев без согласия, позже отменён трибуналом по вопросу юрисдикции | 2022 | partial |
| V08-030 | Clearview AI — штраф итальянского Garante €20 млн за незаконный биометрический мониторинг граждан | 2022 | failure |
| V08-031 | Facebook — $650 млн по иску BIPA Иллинойса за автотэггинг лиц в «тэгах» без согласия | 2020 | failure |
| V08-032 | Сан-Франциско — первый в США запрет распознавания лиц городскими службами и полицией | 2019 | failure |
| V08-033 | Портленд — самый широкий в США запрет распознавания лиц, включая частный бизнес в общественных местах | 2020 | failure |
| V08-034 | ACLU×Amazon Rekognition — 28 членов Конгресса США ошибочно сопоставлены с базой мугшотов, расовый перекос | 2018 | failure |
| V08-035 | Gender Shades (Buolamwini/Gebru) — ошибка классификации пола до 34,7% у темнокожих женщин против 0,8% у светлокожих мужчин (IBM, Microsoft, Face++) | 2018 | failure |
| V08-036 | BJP/Manoj Tiwari — липсинк-дипфейк на хариянви разослан через 5000+ групп WhatsApp ~15 млн зрителям; партия всё равно проиграла выборы в Дели | 2020 | partial |
| V08-037 | Дипфейк «сдачи» Зеленского — распространён после взлома телеканала, удалён Meta/YouTube в течение дня из-за явных артефактов | 2022 | failure |
| V08-038 | Google — $100 млн по иску BIPA за биометрию в Face Grouping Google Photos (2015–2022) | 2022 | failure |
| V08-039 | TikTok — $92 млн по иску BIPA за биометрию лиц пользователей, включая несовершеннолетних | 2021 | failure |
| V08-040 | Московское метро Face Pay — 122 тыс. пользователей и 12,7 млн поездок оплачено биометрией к концу первого года | 2021 | success |
| V08-041 | India Digi Yatra — биометрический посадочный контроль в аэропортах, 1 млн пользователей к июню 2023 | 2023 | success |
| V08-042 | Intel FakeCatcher — детектор дипфейков по сигналу кровотока в пикселях, заявлена точность 96% в реальном времени | 2022 | success |
| V08-043 | Словакия — аудио-дипфейк лидера партии о подкупе голосов распространён за 48 часов до выборов; партия проиграла, причинный эффект оспорен академически | 2023 | partial |
| V08-044 | Tom Hanks — несанкционированная реклама стоматологического плана с дипфейк-видео актёра | 2023 | failure |
| V08-045 | Шанхай — обход liveness-проверки налоговой системы Китая дипфейк-видео по купленным фото, фиктивные счета на ¥500 млн | 2021 | failure |
| V08-046 | Guo Bing v. Hangzhou Safari Park — первый в Китае суд по распознаванию лиц, зоопарк обязан удалить биометрию посетителя | 2020 | failure |
| V08-047 | Швеция — штраф полиции €250 тыс. за нелегальное применение Clearview AI без оценки воздействия на защиту данных (DPIA) | 2021 | failure |
| V08-048 | Канада — комиссары по приватности признали сбор биометрии Clearview AI «массовым слежением» за канадцами | 2021 | failure |
| V08-049 | Австралия OAIC — приказ Clearview AI уничтожить биометрию австралийцев, решение подтверждено апелляцией в 2023 | 2021 | failure |
| V08-050 | Франция CNIL — штраф Clearview AI €20 млн, затем ещё €5,2 млн за неисполнение приказа об удалении данных | 2022 | failure |
| V08-051 | Балтимор/Pikesville — завхоз школы создал ИИ-аудио «расистской тирады» директора из мести, разоблачён ФБР за 3 месяца, осуждён | 2024 | failure |
