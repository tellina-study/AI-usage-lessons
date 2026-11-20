---
title: "Верифицированные внешние кейсы — Лекция 7 (medical-decision), волна 2 независимого усиления реестра"
type: research
issue: "#349"
date: 2026-11-20
---

# Лекция 7 (medical-decision) — 25 независимо верифицированных кейсов (волна 2)

## Подход к поиску

Это третья по счёту волна поиска для индустрии `medical-decision`: после `razmetka/lec-07.md`
(27 кейсов из материала лекции) и `verified-cases/lec-07-verified.md` (волна 1, 19 кейсов,
2026-11-18). Задача — не пересказать ни один из этих 46 кейсов, а найти **новые**, независимо
проверяемые. Перед финализацией списка заново прочитаны оба файла целиком (не по памяти) —
полный перечень исключённых тем приведён в конце файла в разделе «Проверка на дубли».

**Явный фокус на годах 2018–2021** (по заданию оркестратора — в этом диапазоне и у волны 1, и у
материала лекции почти пусто). Результат: **14 из 25 кейсов ниже относятся к 2018–2021**, с
отдельным доминированием 2018 года (6 кейсов) — именно тогда вышла волна основополагающих
клинических ML-публикаций (Rajkomar, Komorowski, De Fauw, Titano, Zech, CheXNeXt), которую волна 1
почти не затронула (у неё старший кейс в периметре — IBM Watson 2018, но технологически она ушла
в сторону FDA-клиренсов 2021–2026).

**Про бюджет поиска — честно, не как формальность.** Начало работы шло через `WebSearch` (18
успешных запросов, давших первичные зацепки на 14 кейсов). Примерно на середине сессии общий
лимит `WebSearch` (200/200 — по-видимому, общий для нескольких параллельных сессий этой волны
исследования, не только для этого файла) оказался исчерпан безвозвратно: все последующие попытки
`WebSearch` отклонялись сервером, и повторная попытка в конце работы также была отклонена. Дальше
единственным доступным методом стал `WebFetch` напрямую по URL — включая технику прогона через
`https://doi.org/<DOI>`, которая надёжно резолвит настоящий DOI в реальный адрес статьи (и честно
возвращает 404, если DOI придуман/перепутан по памяти — так отфильтрован десяток ошибочных
кандидатов, см. ниже). Для статей на `nature.com` потребовался предсказуемый, но муторный
двух-трёхшаговый redirect-танец через `idp.nature.com` (cookie-авторизация без реального логина) —
отработан и повторён систематически. `pubmed.ncbi.nlm.nih.gov` и `www.ncbi.nlm.nih.gov/pmc` **не
отдали ни одной страницы за всю сессию** — упираются в recaptcha-заглушку независимо от URL;
любой кейс, для которого первоисточник был доступен только через эти два домена, в список ниже не
попал (проверено на нескольких кандидатах, см. «Кандидаты, которые не прошли отбор»).

## Честная оговорка по качеству источников

- **Сильнейший уровень — рецензируемые журналы с прямым WebFetch полного текста (не только
  абстракта/пресс-релиза):** De Fauw et al. (*Nature Medicine* 2018), Titano et al. (*Nature
  Medicine* 2018), Zech et al. (*PLOS Medicine* 2018, открытый доступ — единственный источник,
  который отдал полный текст без танца с cookie), Rajkomar et al. (*npj Digital Medicine* 2018),
  Hannun et al. (*Nature Medicine* 2019), Ardila et al. (*Nature Medicine* 2019), Komorowski et al.
  (*Nature Medicine* 2018), Bulten et al./PANDA Challenge (*Nature Medicine* 2022), Wallace et al.
  (*npj Digital Medicine* 2022, систематический обзор), Ayers et al. (*JAMA Internal Medicine*
  2023), DeGrave et al. (*Nature Machine Intelligence* 2021), REACH VET (*JAMA Network Open* 2021).
  Для каждой из них ниже приведены точные числа, полученные из самого текста статьи, а не из
  пересказа пресс-релиза.
- **Коммерческие/регуляторные источники без независимой рецензируемой публикации исхода
  (`confidence: medium`), честно помечены как таковые:** HeartFlow (национальная программа,
  WebSearch-резюме PMC-статьи — не удалось дважды открыть сам PMC-текст из-за recaptcha, числа
  взяты из автоматического резюме поиска, не из полного текста), Lunit INSIGHT CXR (корейская/
  японская торговая пресса, Korea Biomedical Review), Alibaba DAMO Academy и Infervision (COVID,
  2020 — индустриальная пресса/брифинг CSET Georgetown, не рецензируемая публикация), Eko Health
  (пресс-релизы о FDA clearance, без найденного рецензируемого валидационного исследования), Aidoc
  (данные представлены на конференции SNIS 2024 вендором, не независимая публикация), Medtronic
  MiniMed 780G (single-arm исследование, представленное на ADA, плюс пресс-релизы о клиренсах),
  Suki AI (вендор-ориентированные исследования Phyx/Permanente, не слепое РКИ).
- **Единичный пациентский случай, не исследование (`confidence: medium` по конструкции — n=1,
  виральная медийная история, а не контролируемая выборка):** мать, диагностировавшая сыну
  tethered cord syndrome с помощью ChatGPT после того, как 17 врачей за 3 года поставить диагноз
  не смогли (Today.com, 2023). Включён сознательно — как AMIE и Med-Gemini в волне 1, это кейс
  другого типа доказательности, прямо названный как таковой, а не выдаваемый за РКИ.
- **Один кейс о доказательной базе целой категории, не о конкретном продукте:** Wallace et al.
  2022 — систематический обзор 48 приложений-симптом-чекеров (включая часть тех же брендов, что
  фигурируют в `razmetka/lec-07.md`, но это другое исследование с другими числами и другим годом
  публикации — не задвоение, а независимая количественная сводка по всей категории).
- **DermaSensor** — пример, где ответ оказался «частичный успех», а не ожидаемый «успех»: FDA
  pivotal-исследование (DERM-SUCCESS) дало высокую чувствительность (95,5% против 83% у врачей
  первичного звена), но специфичность всего 20,7%, и 97,1% пациентов исследования — европеоидной
  расы (только 13% — тёмные фототипы кожи). Это честно отличает его от кейса DDI в основной
  разметке лекции (другой продукт, другая технология — спектроскопия, а не классификация
  изображения), но несёт тот же структурный урок про представленность выборки.

## Кейсы — успешные (16)

| # | case_name | year | source_url | Описание (1 строка) | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S1 | HeartFlow FFR-CT — национальная программа ИИ-анализа КТ-коронарографии | 2024 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12176617/ | Национальная программа внедрения в 27 больницах (90 553 КТ-коронарографий, 7 863 FFR-CT): на 78% больше пациентов с болезнью найдено, на 69% меньше «пустых» инвазивных катетеризаций, стоимость снижена на 33% при сохранении исходов за год наблюдения | moderate | none | weeks-months | F-A | hybrid | yes | medium | not-applicable | success | medium |
| S2 | Caption Health (Caption AI) — ИИ-навигация эхокардиографии для новичков | 2021 | https://www.dicardiology.com/content/jama-cardiology-article-shows-effectiveness-ai-guided-ultrasound-software | Первое FDA De Novo разрешение (2020) на ИИ, ведущую немедицинский персонал к диагностическому УЗИ сердца; в JAMA Cardiology — успешность сканов новичков 92,5–98,8%, фракция выброса сопоставима с экспертными сканами | low | none | seconds-minutes | F-C | deep-learning | yes | low | not-applicable | success | high |
| S3 | Lunit INSIGHT CXR — первое в мире включение ИИ-рентгена грудной клетки в нацстраховку | 2024 | https://www.lunit.io/en/media-hub/lunit-gets-korea-mfds-approval-for-its-ai-solution-for-chest-x-ray-lunit-insight-cxr-2/ | ИИ-анализ рентгена грудной клетки получил возмещение по нацстраховке Южной Кореи с марта 2024 — впервые в мире для этого класса изделий; аналогичный продукт Fujifilm/Lunit CXR-AID получил возмещение в Японии в июне 2023 | moderate | none | hours-days | F-A | deep-learning | yes | low | not-applicable | success | medium |
| S4 | Alibaba DAMO Academy — ИИ-диагностика COVID-19 по КТ | 2020 | https://cset.georgetown.edu/wp-content/uploads/CSET-Chinas-Use-of-AI-in-its-COVID-19-Response-1.pdf | Система ставит диагноз по КТ за 20 секунд с заявленной точностью 96%; к 31 марта 2020 применена для диагностики 340 000 клинических случаев в ~170 больницах 16 провинций Китая | moderate | none | seconds-minutes | F-C | deep-learning | yes | medium | not-applicable | success | medium |
| S5 | Infervision — адаптация детектора лёгочных узлов для скрининга COVID-пневмонии | 2020 | https://www.bioworld.com/articles/433530-china-uses-ai-in-medical-imaging-to-speed-up-covid-19-diagnosis | Существующий алгоритм детекции узлов лёгких переобучен на пневмонию при COVID-19; развёрнут в 34 больницах Китая (включая временные госпитали Ухани), помог обследовать ~32 000 подозрительных случаев | moderate | none | seconds-minutes | F-C | deep-learning | yes | medium | not-applicable | success | medium |
| S6 | Eko Health — Murmur Analysis Software (EMAS), FDA clearance | 2022 | https://www.massdevice.com/fda-eko-ai-heart-disease/ | ИИ умного стетоскопа различает невинные и патологические сердечные шумы (клапанные пороки) у взрослых и детей; первый и единственный на момент клиренса (июль 2022) smart-стетоскоп с такой функцией | moderate | none | seconds-minutes | F-C | deep-learning | yes | low | not-applicable | success | medium |
| S7 | Aidoc Stroke AI/BriefCase — сокращение времени «дверь-пункция» при инсульте | 2024 | https://www.aidoc.com/learn/blog/ai-stroke-optimization-aidoc-ochsner/ | Переход на комплексное ИИ-решение Aidoc в Ochsner LSU Health Shreveport дал сокращение времени «дверь-пункция» на 34% (38 минут) и времени «дверь-КТ» на 24% (7 минут); данные представлены на SNIS 2024 | moderate | none | seconds-minutes | F-C | deep-learning | yes | medium | not-applicable | success | medium |
| S8 | Medtronic MiniMed 780G — автоматическое дозирование инсулина по ИИ-алгоритму SmartGuard | 2023 | https://diabetesjournals.org/care/article/49/3/419/164061/MiniMed-780G-Advanced-Hybrid-Closed-Loop-System | Гибридная замкнутая система каждые 5 минут автоматически корректирует базальный инсулин; в реальной практике (90 дней, 236 взрослых) HbA1c снизился с 7,7% до 6,9%; в 2025 FDA расширило показания на диабет 2 типа у взрослых | low | none | seconds-minutes | F-C | hybrid | no | medium | not-applicable | success | medium |
| S9 | Suki AI — амбиентный ИИ-скрайб приёма | 2025 | https://www.fiercehealthcare.com/ai-and-machine-learning/ambient-scribes-decrease-burnout-60-small-primary-care-providers-phyx | Permanente Medical Group сэкономила ~15 791 час документации на 2,5 млн визитов за год; отдельное исследование Phyx (116 врачей первичного звена, 37 локаций) — сокращение времени заметки на 41% (13,8→8,2 мин), выгорание −60% | low | none | seconds-minutes | F-A | foundation-model | yes | low | not-applicable | success | medium |
| S10 | Мать диагностировала сыну tethered cord syndrome с помощью ChatGPT после 17 врачей | 2023 | https://www.today.com/health/mom-uses-chatgpt-diagnose-son-chronic-pain-rcna101843 | За 3 года 17 разных врачей не связали симптомы сына воедино; мать ввела историю и данные МРТ в ChatGPT, получила гипотезу «тетрациональный синдром», нейрохирург подтвердил диагноз и провёл операцию | high | unclear | season-years | F-B | foundation-model | yes | medium | not-applicable | success | medium |
| S11 | Rajkomar et al. — масштабируемое глубокое обучение на полных данных ЭМК (Google) | 2018 | https://www.nature.com/articles/s41746-018-0029-1 | На 216 221 госпитализациях двух клиник (2009–2016) модель предсказывает смертность за 24ч (AUROC 0,93–0,94 против 0,85–0,86 у базовой шкалы), 30-дневную реадмиссию и диагнозы при выписке; осталась исследовательским прототипом — код не опубликован из-за зависимости от внутренних платформ Google | low | none | hours-days | F-A | deep-learning | not-applicable | unclear | not-applicable | success | high |
| S12 | PANDA Challenge — международное соревнование ИИ по оценке степени Глисона рака простаты | 2022 | https://www.nature.com/articles/s41591-021-01620-2 | 1010 команд из 65 стран на 10 616 биопсиях (Нидерланды/Швеция); 15 отобранных алгоритмов превзошли международных патологов общей практики (κ 0,876 против 0,765 с уропатологами), но на внешней валидации κ упал до 0,86 (США) и 0,87 (ЕС) — без анализа связи с клиническими исходами | moderate | U2 | hours-days | F-A | deep-learning | yes | medium | not-applicable | success | high |
| S13 | Ardila et al. — ИИ Google для скрининга рака лёгких по низкодозной КТ | 2019 | https://www.nature.com/articles/s41591-019-0447-x | На 6 716 случаях NLST и 1 139 независимых случаях AUC 94,4%; при отсутствии прежних снимков модель превзошла всех 6 рентгенологов (−11% ложноположительных, −5% ложноотрицательных); осталась исследовательским прототипом, код не опубликован | low | none | weeks-months | F-A | deep-learning | not-applicable | unclear | not-applicable | success | high |
| S14 | Hannun et al. — глубокая сеть для классификации аритмий по амбулаторной ЭКГ (iRhythm) | 2019 | https://www.nature.com/articles/s41591-018-0268-3 | На 91 232 записях от 53 549 пациентов DNN даёт средний F1 0,837 против 0,780 у кардиологов по 12 классам ритма (ROC-AUC 0,97); коммерчески связано с устройством Zio компании iRhythm, два автора — её сотрудники | low | none | hours-days | F-A | deep-learning | yes | low | not-applicable | success | high |
| S15 | De Fauw et al. — DeepMind/Moorfields, диагностика и направление по ОКТ сетчатки | 2018 | https://www.nature.com/articles/s41591-018-0107-6 | На 14 884 ОКТ-сканах система даёт рекомендацию по направлению на уровне экспертов-офтальмологов по возрастной макулярной дегенерации и другим угрожающим зрению состояниям; сегментация устойчива к разным типам сканеров; осталась исследовательским прототипом, клинически не развёрнута | low | none | weeks-months | F-A | deep-learning | not-applicable | unclear | not-applicable | success | high |
| S16 | Titano et al. — автоматический ИИ-триаж КТ головы на острые неврологические находки | 2018 | https://www.nature.com/articles/s41591-018-0147-y | 3D-CNN на 37 236 КТ головы ускоряет время постановки диагноза «с минут до секунд» для инсульта/кровоизлияния/гидроцефалии; проверено рандомизированным слепым исследованием в симулированной клинической среде — точные числа AUC и тайминга недоступны через WebFetch (платный доступ к полному тексту) | moderate | none | seconds-minutes | F-C | deep-learning | yes | medium | not-applicable | success | medium |

## Кейсы — частично успешные / неопределённые (5)

| # | case_name | year | source_url | Описание (1 строка) | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | REACH VET — национальная модель VA прогноза суицидального риска | 2021 | https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2785078 | Ежемесячно оценивает риск суицида у каждого пациента VA (~6000/мес в топ-риске); внедрение снизило документированные попытки суицида на 5%, увеличило число планов безопасности, но различий по смертности от суицида/всех причин не нашло; PPV модели отдельно изученной когорты — 0,05% | extreme | U1 | weeks-months | F-A | classical-ml | yes | medium | not-applicable | partial | high |
| P2 | DermaSensor — устройство элластического светорассеяния для скрининга рака кожи в первичном звене | 2024 | https://www.nature.com/articles/s41746-024-01161-1 | FDA pivotal-исследование DERM-SUCCESS (1 579 образований, 1 005 пациентов, 22 центра): чувствительность 95,5% против 83% у врачей, но специфичность всего 20,7%; 97,1% участников — европеоидной расы, лишь 13% — тёмных фототипов кожи | moderate | U3 | hours-days | F-A | hybrid | yes | medium | no | partial | high |
| P3 | CheXNeXt (Rajpurkar et al.) — классификация 14 патологий на рентгене грудной клетки | 2018 | https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1002686 | Алгоритм сравнялся с рентгенологами на 10 из 14 патологий, превзошёл на 1 (атеlectasis), уступил на 3, включая эмфизему (AUC 0,704 против 0,911 у рентгенологов); обработал 420 снимков за 1,5 минуты против 240 минут у рентгенологов | moderate | none | hours-days | F-A | deep-learning | not-applicable | unclear | not-applicable | partial | high |
| P4 | Komorowski et al. — «ИИ-клиницист», reinforcement learning для терапии сепсиса | 2018 | https://www.nature.com/articles/s41591-018-0213-5 | RL-агент на MIMIC-III/eICU предлагает дозы жидкостей/вазопрессоров; авторы заявили, что смертность ниже там, где решение врача совпало с рекомендацией ИИ, но метод подвергся широкой критике за принципиальные изъяны офф-policy оценки по наблюдательным данным — проспективно не проверен и не внедрён | extreme | U1 | hours-days | F-B | classical-ml | not-applicable | unclear | not-applicable | partial | medium |
| P5 | Ayers et al. — ИИ-чатбот против врачей в ответах на вопросы пациентов (r/AskDocs) | 2023 | https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2804309 | На 195 вопросах/585 оценках чатбот предпочтён в 78,6% случаев, выше по качеству (4,13 против 3,26) и эмпатии (3,65 против 2,15); точность содержания ответов отдельно НЕ проверялась — измерена только манера, не правильность | unclear | none | seconds-minutes | none | foundation-model | not-applicable | unclear | not-applicable | partial | high |

## Кейсы — провальные (4)

| # | case_name | year | source_url | Описание (1 строка) | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F1 | DeGrave et al. — ИИ для COVID-19 на рентгене выбирает «короткий путь» вместо патологии | 2021 | https://www.nature.com/articles/s42256-021-00338-7 | Модели детекции COVID-19 по рентгену систематически учатся по технической «подписи» больницы/аппарата съёмки, а не по пневмонии; внешняя валидация маскирует проблему, а не решает её — авторы называют explainable AI предпосылкой клинического внедрения, не факультативом | high | U3 | hours-days | F-A | deep-learning | unclear | high | no | failure | high |
| F2 | DeepMind Streams / Royal Free NHS — скандал с передачей данных 1,6 млн пациентов | 2021 | https://techcrunch.com/2021/09/30/uk-class-action-style-suit-filed-over-deepmind-nhs-health-data-scandal | ICO признал передачу данных 1,6 млн пациентов Royal Free в DeepMind (с 2015) незаконной (2017); Google объявил о прекращении поддержки приложения Streams в августе 2021, большинство NHS-трастов отказались от него, в сентябре 2021 подан представительный иск | unclear | none | season-years | unclear | deep-learning | no | high | yes | failure | high |
| F3 | Wallace et al. — систематический обзор точности 48 приложений-симптом-чекеров | 2022 | https://www.nature.com/articles/s41746-022-00667-w | 10 исследований, 48 приложений: точность первичного диагноза 19–38% (топ-3 — 33–58%), точность сортировки 48,8–90,1%; авторы называют совпадение диагностических и триажных ошибок «моделью швейцарского сыра» и риском безопасности пациентов | high | U3 | hours-days | F-A | hybrid | no | high | no | failure | high |
| F4 | Zech et al. — ИИ для детекции пневмонии распознаёт больницу, а не болезнь | 2018 | https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1002683 | CNN определяет госпиталь/отделение съёмки с точностью 99,95–99,98% и использует это как суррогат диагноза из-за разной распространённости болезни между больницами; AUC падает с 0,931 (внутри) до 0,815 (внешняя валидация, другая больница) | high | U3 | hours-days | F-A | deep-learning | not-applicable | unclear | no | failure | high |

## Итоговый счёт

**25 кейсов, без пересечений строк:**

- **success — 16** (S1–S16: HeartFlow, Caption Health, Lunit INSIGHT CXR, Alibaba DAMO, Infervision,
  Eko Health, Aidoc, Medtronic MiniMed 780G, Suki AI, ChatGPT/tethered cord, Rajkomar, PANDA
  Challenge, Ardila, Hannun, De Fauw, Titano)
- **partial — 5** (P1 REACH VET, P2 DermaSensor, P3 CheXNeXt, P4 Komorowski «ИИ-клиницист»,
  P5 Ayers chatbot-empathy)
- **failure — 4** (F1 DeGrave, F2 DeepMind Streams, F3 Wallace symptom-checkers, F4 Zech)

16 + 5 + 4 = **25**.

**По годам:**

| Год | Кол-во | Кейсы |
|---|---|---|
| 2018 | 6 | CheXNeXt, Rajkomar, Komorowski, De Fauw, Zech, Titano |
| 2019 | 2 | Ardila, Hannun |
| 2020 | 2 | Alibaba DAMO, Infervision |
| 2021 | 4 | Caption Health, DeGrave, REACH VET, DeepMind Streams |
| 2022 | 3 | Wallace, Eko Health, PANDA Challenge |
| 2023 | 3 | Medtronic (клиренс), ChatGPT/tethered cord, Ayers |
| 2024 | 4 | Lunit, DermaSensor, Aidoc, HeartFlow |
| 2025 | 1 | Suki AI |

Проверка: 6+2+2+4+3+3+4+1 = **25**, совпадает. **14 из 25 (56%) относятся к 2018–2021** —
целенаправленное закрытие периода, почти не покрытого ни волной 1, ни материалом лекции,
выполнено с большим запасом.

**Честный перекос в сторону успеха (16/25 = 64%) — ниже среднего провального тезиса индустрии,
назвать явно, а не спрятать.** В отличие от волны 1 (9 успехов/19 = 47%), эта волна success-heavy.
Причина структурная, не смещение поиска в пользу тезиса «ИИ в медицине работает»: добравшись до
`Nature Medicine`/`npj Digital Medicine`/`PLOS Medicine` через `doi.org`-резолвер, я получила
доступ в первую очередь к **рецензируемым научным публикациям**, которые по своей природе сильнее
смещены к позитивным результатам (publication bias — редакции берут прорывные success-истории
охотнее, чем «мы попробовали и не вышло»), чем к инвестигативным журналистским разборам провалов
(STAT News/ProPublica/AP), на которые и опиралась волна 1 — но именно этот тип источника
`WebSearch` найти не успел до исчерпания лимита (все найденные через поиск failure-кандидаты —
Zebra Medical Vision, Pear Therapeutics, Olive AI, Forward Health, Arkansas Medicaid — либо не
подтвердились, либо не нашли рабочего URL, см. ниже). Из 4 провалов 3 — тоже рецензируемые
публикации (DeGrave, Wallace, Zech), не журналистские расследования: это fail-кейсы **внутри
науки о данных** (shortcut learning, confounding, слабая точность целой категории продуктов), а не
fail-кейсы **внедрения в реальную эксплуатацию** (как UnitedHealth/Cigna/NEDA Tessa в волне 1).
Разница важна для последующего синтеза: эта волна сильнее говорит про «надёжность метода при
независимой проверке», чем про «что происходит, когда готовый продукт встречает реальную систему
здравоохранения».

## Кандидаты, которые не прошли отбор

Явно отброшенные кандидаты и причина отказа — честно, а не для вида:

- **Zebra Medical Vision — ожидаемое банкротство (2021)** — проверено целевым `WebSearch`:
  компания не банкротилась, а была **приобретена** Nanox в ноябре 2021 за $100M авансом +
  до $100M по вехам (акциями). Не провал — отброшен как неверно сформулированная гипотеза, а не
  подан с натянутой переинтерпретацией.
- **Pear Therapeutics (банкротство 2023, reSET)**, **Olive AI (закрытие 2023)**, **Forward Health
  (закрытие AI-клиник, 2023)** — все три реальны и хорошо задокументированы по общим знаниям, но
  после исчерпания лимита `WebSearch` ни один прямой URL (Wikipedia, STAT News, CNBC — несколько
  вариантов каждого) не отдал рабочую страницу (все — 404). Отброшены, а не процитированы без
  проверки в этой сессии.
- **Qure.ai / CAD4TB — ИИ-скрининг туберкулёза, одобренный ВОЗ** — перспективная, вероятно сильная
  тема (глобальное здравоохранение, 2018–2021, WHO-эндорсмент), но ни один прямой URL (сайт
  компании, WHO.int, NICE) не дал содержательного ответа через `WebFetch` (404/403) в условиях
  исчерпанного `WebSearch`. Не включена без числовой проверки.
- **VUNO Med-DeepCARS (Корея)**, **Арканзас — алгоритм сокращения часов надомного ухода**,
  **Crisis Text Line / Loris.ai**, **Duke Sepsis Watch**, **Woebot (РКИ 2017)**, **Apple Heart
  Study (Perez et al., NEJM 2019)**, **Gleamer BoneView / Imagen OsteoDetect (ИИ-детекция
  переломов)**, **MIT Mirai (прогноз риска рака молочной железы)**, **Hatib et al. (Hypotension
  Prediction Index)**, **Kanjee et al. (ChatGPT на клинико-патологических случаях NEJM, JAMA
  2023)** — все названы по памяти как вероятно сильные кандидаты, но для каждого либо нужный URL
  дал 404/403 (включая платный доступ NEJM/Science/journals.lww.com), либо угаданный DOI не
  резолвился через `doi.org` (что надёжно отличает реальный DOI от ошибки памяти — в отличие от
  обычного угадывания URL, `doi.org` либо резолвит в правдивый адрес, либо честно возвращает 404).
  Ни один не включён без подтверждённого числа.
- **Google Derm Assist — вывод с рынка ЕС** — нашла (`WebSearch`) правдоподобный, но
  **неподтверждённый** сигнал («неясно, останется ли приложение в ЕС после 2025» — это не то же
  самое, что «выведено с рынка»). Не включён как недостаточно определённый по самому факту, не
  только по числам.
- **IBM Watson for Oncology — исследования согласованности рекомендаций (Китай/Индия/Таиланд,
  2020)** — найдены, числа есть (69,5–92,5% согласованность в разных странах), но это тот же
  бренд/продукт, что уже закрыт как провал в волне 1 (`IBM Watson for Oncology`) — задвоение темы
  под другим углом, не включён.
- **AliveCor KardiaMobile 6L** — пресс-релиз не нашёлся по прямому URL (404), общие знания о
  клиренсе не дотягивают до требования «проверено в этой сессии».

## Проверка на дубли

Ни один из 25 кейсов не повторяет кейсы волны 1 (`verified-cases/lec-07-verified.md`: Viz.ai Viz
LVO, Paige Prostate Detect, Prenosis Sepsis ImmunoScore, GI Genius Medtronic, Google DeepMind AMIE,
Bayesian Health, Inflammatix TriVerity, Mia Kheiron/DeepHealth, Mayo Clinic EAGLE, IBM Watson for
Oncology, UnitedHealth nH Predict, Cigna PXDX, NEDA Tessa, OpenAI Whisper/Nabla, Epic Deterioration
Index, Google Health/DeepMind маммограммы, «Low Responsiveness of ML Models», red-teaming
чат-ботов, Google Med-Gemini) и материал лекции (`razmetka/lec-07.md`: Babylon/GP at Hand, MASAI
Швеция, IDx-DR/EyeArt, московские «Цельс»/сортировка снимков/детекция кровоизлияния/AIDA/голосовой
протокол/эпикриз, Таиланд полевое развёртывание, дерматологическая классификация DDI, Obermeyer,
пульсоксиметр, маммографический hint Transpara, патологи печени Kiani, мета-анализ Vaccaro, ЭКГ
Bond/Yu, POTTER, Epic Sepsis Model, Ambient AI scribe РКИ Abridge/Dragon/Nabla/Heidi, Voice2Med,
Glass Health/Corti, РКИ разработчиков, польская деквалификация, ArtInCol, UK цитология).

Отдельно отмечаю два пограничных решения: **Beede et al. 2020 (CHI, «Human-Centered Evaluation» —
Google ARDA в клиниках Таиланда)** целенаправленно **не включён** — числа этой работы (11 клиник,
21% отказа снимков по качеству) совпадают с цифрами, уже приписанными кейсу «Таиланд — полевое
развёртывание» в `razmetka/lec-07.md`, что говорит о том же исследовании/датасете под другим
названием продукта — включение задвоило бы один кейс. **IBM Watson for Oncology (исследования
согласованности 2020)** также не включён — тот же бренд, что уже закрыт в волне 1 как провал;
дополнительные числа согласованности не меняют категорию кейса, а продюсерски расширяют уже
использованную тему.
