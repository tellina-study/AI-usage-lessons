---
title: "Лекция 10 (agriculture) — независимо верифицированные кейсы, волна 3 (добор до 1000+ строк)"
type: research
issue: "#349"
date: 2026-11-20
lecture_num: 10
industry: agriculture
wave: 3
---

# Лекция 10 (agriculture) — верифицированные кейсы, волна 3 (не дублирует волну 1 и реестр)

## Подход к поиску

Задача — найти ≥25 новых, независимо верифицированных кейсов «ИИ в сельском хозяйстве»,
**не пересекающихся** с 20 кейсами волны 1 (`verified-cases/lec-10-verified.md`) и, по
возможности, с 54 кейсами основного реестра лекции (`razmetka/lec-10.md`). Перед началом работы
прочитаны оба файла целиком; список из ~74 уже использованных названий вендоров держался под
рукой на всё время поиска, чтобы не задвоить случайно совпавшее имя.

Поиск вёлся кластерами: (1) вертикальные фермы/закрытия 2022–2025 за пределами уже известных
восьми банкротств, (2) автономная техника и прополка/спрей за пределами See & Spray/Carbon
Robotics/Verdant, (3) virtual fencing и датчики для КРС за пределами Allflex/CattleEye/DeLaval,
(4) ИИ-платформы для агродата/почвы/урожайности за пределами Climate FieldView/TerraMind, (5)
точечное закрытие пробела 2018–2021 годов, который волна 1 явно не закрыла.

**Критический сбой инфраструктуры в процессе работы.** Бюджет `WebSearch` на сессию (200
вызовов) оказался **общим на весь CAO-терминал**, а не на этот вызов агента — он был исчерпан
другой работой до того, как эта задача успела сделать больше 15 запросов (тот же симптом волна 1
уже зафиксировала в своём файле). После этого:
- Прямые `WebFetch` по угадываемым URL пресс-релизов срабатывали примерно в половине случаев
  (вторая половина — HTTP 404, URL не совпал с реальным).
- `curl` на `lite.duckduckgo.com` и `html.duckduckgo.com` отрабатывал несколько запросов, затем
  упёрся в анти-бот CAPTCHA («Select all squares containing a duck») и не восстановился до конца
  сессии.
- `bing.com` и `google.com` через `curl`/`WebFetch` либо требуют JS-рендер, либо показывают
  EU-cookie-consent редирект, либо отдают нерелевантную выдачу — не дали ни одного пригодного
  результата.
- Рабочим резервным каналом оказался прямой `WebFetch` по официальным сайтам компаний,
  Wikipedia-страницам (когда они существуют) и GitHub-зеркалам документации (сработало для даты
  ретайринга Azure Data Manager for Agriculture).

Это означает: охват этой волны **уже' не настолько широк, как при полном бюджете WebSearch** —
часть кандидатов (список ниже, раздел «Отброшено») не дотянута до verified-статуса и честно не
включена, а не притянута силой.

## Качество источников — по уровням, не усреднённо

- **Первичные регуляторные/корпоративные документы** (SEC 8-K/10-Q/424B3 — Kalera, AgEagle,
  Local Bounti; BusinessWire press release от самой компании — Benson Hill; официальная
  Microsoft-документация retirement notice) — самый сильный класс в этой волне.
- **Деловая/отраслевая пресса с прямым цитированием** (AgFunderNews, TechCrunch, FarmProgress,
  The Robot Report, Just-food, WPXI, TechCabal/Weetracker) — высокое качество, вторичные, но с
  именованными фактами и датами.
- **Вендорский PR / собственный сайт без независимого аудита** (ecoRobotix PRNewswire,
  Greeneye/Semios/smaXtec — цифры эффекта от самой компании или партнёрского «research»-блога) —
  понижено до `confidence: medium`.
- **Единственный источник, тем более тускло вторичный** (Jones Food Company — только
  англоязычная Wikipedia, без независимого прямого фетча оригинальной статьи о закрытии;
  Harvest CROO Robotics — спонсируемый вендором материал Nutanix, который **противоречит**
  собственному выводу основного реестра лекции о категории «робот-сборщик клубники» как
  структурном провале) — понижено до `confidence: low`, с явной оговоркой в примечании, а не
  тихой заменой confidence.
- **Слабая AI-специфичность продукта** (Smallhold — источник подтверждает климат-контроль, но
  не называет его ИИ/ML явно; Local Bounti — SEC-факты о долге железные, но сам продукт описан
  как «CEA greenhouse», не как ИИ-система) — помечено в примечании отдельно от confidence самого
  факта банкротства/долга, который в обоих случаях high.

## Честный недобор кандидатов (отброшено, не дотянуто до verified)

Проверялись, но **не включены** из-за недостатка первичной верификации после отказа поисковых
движков (не потому, что кейсов не существует):

- **DOT Technology Corp** — оказался тем же `Raven/CNH`-деревом, что уже даёт волна 1 (F9,
  ребрендирован в OMNi/OMNiPOWER тем же Raven Industries) — не новый кейс, а тот же, под другим
  именем на промежуточном этапе.
- **IBM Watson Decision Platform for Agriculture** — анонс экспансии 2019 года найден, но ни один
  источник не подтвердил дату/факт сворачивания напрямую.
- **Gamaya** — проверка показала, что компания **не** свернула агро-направление (противоречит
  исходной гипотезе), включать как «провал» было бы ложью; как «успех» — недостаточно цифр.
- **Pivot Bio, Connecterra, XAG, Resson, Babylon Micro-Farms, Dream Harvest, FarmDroid, Bear Flag
  Robotics** — угаданные URL первичных источников не открылись (404), а резервный поиск был
  заблокирован CAPTCHA/JS-стеной до того, как успели найти рабочую ссылку. FarmDroid отдельно
  отброшен и по содержательной причине: собственный сайт прямо говорит «no camera needed», т.е.
  это GPS-точность, не ИИ — не подходит под тему задачи вовсе.

## Таблица кейсов

### Провал (9)

| # | case_name | year | outcome | confidence | axis1_level / mechanism | axis2_bucket / mechanism | axis3_class | axis4_gate / blast_radius | external_driver | Что произошло (цифры) | source_url |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F1 | Kalera — Chapter 11 | 2023 | failure | high | low / none | season-years / none | hybrid | not-applicable / medium | mixed | Подала на Chapter 11 4 апр. 2023 (Южный округ Техаса) после снятия CEO 29 марта; >200 кредиторов; в июне 2023 продала все активы кредитору Sandton Capital Partners; в нояб. 2023 суд одобрил ликвидационный траст для необеспеченных кредиторов. | [SEC 8-K](https://www.sec.gov/Archives/edgar/data/1909152/000149315223010745/ex99-1.htm), [Bloomberg Law](https://news.bloomberglaw.com/bankruptcy-law/vertical-farmer-kalera-gets-liquidating-bankruptcy-plan-approved), [Produce Grower](https://www.producegrower.com/news/kalera-chapter-11-bankruptcy-protection/) |
| F2 | Fifth Season — закрытие | 2022 | failure | high | low / none | season-years / none | hybrid | not-applicable / medium | yes | Robotics-вертикальная ферма (Питтсбург) закрылась 28 окт. 2022, ~100 сотрудников; привлекла $35M (Drive Capital и др.); причина по цитате бывшего VP — исключительно неудачное время по отношению к доступности venture-капитала, не технический провал робота. | [WPXI](https://www.wpxi.com/news/local/vertical-farming-robotics-startup-fifth-season-shuts-down/Z6VV32XUWNGFRGEKDZZJCZR3FI/), [AgFunderNews](https://agfundernews.com/robotic-vertical-farming-startup-fifth-season-shuts-down) |
| F3 | Gro Intelligence — крах | 2024 | failure | high | moderate / U3 | weeks-months / F-B | classical-ml | not-applicable / medium | mixed | Сократила 60% штата в марте 2024, закрылась в мае 2024, сменив CEO/основателя Sara Menker по пути; привлекла $117M за всю историю; по показаниям бывших сотрудников — выручка была сконцентрирована на одном клиенте, бизнес-модель съехала в bespoke-консалтинг вместо повторяемого продукта (это и трактуется как U3 — структурный разрыв между заявленной data/AI-платформой и фактической моделью поставки). | [TechCabal](https://techcabal.com/2024/06/02/kenya-data-analytics-gro-intelligence-shuts-down/), [Weetracker](https://weetracker.com/2024/06/02/why-gro-intelligence-shutdown/) |
| F4 | Abundant Robotics — закрытие | 2021 | failure | high | moderate / U1 | season-years / none | hybrid | not-applicable / medium | mixed | Остановила сбор яблок робота-вакуумного харвестера и продала IP/активы 29 июня 2021 (куплены Wavemaker Labs в октябре); причина явно по источнику — хронические проблемы с вакуумной системой на мокрых плодах и разной архитектуре деревьев (сенсорный/механический шум = **U1**) + невозможность поднять раунд во время пандемии. | [The Robot Report](https://www.therobotreport.com/abundant-robotics-shuts-down-fruit-harvesting-business/), [TechCrunch](https://techcrunch.com/2021/07/08/robotics-roundup-19/) |
| F5 | Benson Hill — Chapter 11 | 2025 | failure | high | moderate / unclear | season-years / none | hybrid | not-applicable / medium | mixed | Семенная ИИ/data-science компания (соя) подала на Chapter 11 20 марта 2025; $137,5M активов против $110,7M долга, >200 кредиторов; получила ~$11M DIP-финансирования; 22 мая 2025 суд одобрил продажу активов Confluence Genetics (S2G Investments/ProAgInvest). Причина по источнику — «комбинация отраслевых трудностей и финансовых ограничений», без конкретного технического провала модели. | [BusinessWire](https://www.businesswire.com/news/home/20250320235229/en/Benson-Hill-Files-Voluntary-Chapter-11-Petitions), [World Grain](https://www.world-grain.com/articles/21184-soybean-innovator-benson-hill-files-for-bankruptcy) |
| F6 | Upward Farms — прекращение операций | 2023 | failure | high | low / none | season-years / none | hybrid | not-applicable / medium | mixed | Аквапоника+вертикальная ферма (рыба+зелень) остановила все операции 30 марта 2023, на пороге открытия «крупнейшей в мире» фасилити; собственная цитата компании — «vertical farming почти бесконечно сложна»; развитие пенсильванского объекта 250 000 кв. футов остановлено. | [WVIA](https://www.wvia.org/news/news-briefs/2023-04-04/vertical-farm-shuts-down-operations), [just-food](https://www.just-food.com/news/upward-farms-throws-in-towel-ten-years-after-founding-vertical-farming-business/) |
| F7 | Smallhold — Chapter 11 | 2024 | failure | high | unclear / unclear | season-years / none | unclear | not-applicable / medium | mixed | Вертикальная грибная ферма подала на Chapter 11 18 февр. 2024; 81 сотрудник затронут (закрыты Техас и Нью-Йорк, Лос-Анджелес продолжил работу «как мост»); Monomyth Group получила 90,77% доли. Причина по источнику — спад венчурного финансирования + «флэт» категория свежих грибов, а не явный провал технологии. **Важная оговорка**: источник подтверждает только «патентованный климат-контроль», не называет его ИИ/ML явно — axis3_class оставлен `unclear`, а не `hybrid`, именно по этой причине. | [AgFunderNews](https://agfundernews.com/mushroom-vertical-farming-company-smallhold-files-for-bankruptcy-firm-in-worse-financial-shape-than-previously-disclosed) |
| F8 | Microsoft Azure Data Manager for Agriculture — ретайринг | 2025 | failure | high | not-applicable / none | not-applicable / none | unclear | not-applicable / medium | no | Microsoft объявил 22 авг. 2025 о выводе из эксплуатации (retirement) превью-сервиса Azure Data Manager for Agriculture с датой отключения 1 сент. 2025 — данные клиентов удаляются через 30 дней после этой даты; сервис позиционировался как универсальный data-layer для построения ИИ-решений в АПК поверх Azure (аналог инфраструктурного слоя, как `TerraMind`/`Tract` в основном реестре — не модель сама по себе, а платформа). Решение внутреннее, стратегическое — не внешний шок. | [GitHub/Microsoft docs](https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/data-manager-for-agri/includes/public-preview-notice.md), [Microsoft Learn overview](https://learn.microsoft.com/en-us/azure/data-manager-for-agri/overview-azure-data-manager-for-agriculture) |
| F9 | Jones Food Company — administration | 2025 | failure | low | unclear / unclear | season-years / none | unclear | not-applicable / medium | unclear | Крупная UK-вертикальная ферма (Глостершир, открыта 2024, работала на возобновляемой электроэнергии) была помещена в administration (аналог банкротства) в апреле 2025. **Источник — только Wikipedia (`Vertical farming`), независимый прямой фетч оригинальной статьи о закрытии не удался** (404 на угаданные URL BBC/vertical farm daily, бюджет WebSearch исчерпан до повторной попытки) — confidence понижен до low именно по этой причине, не по сомнению в самом факте. | [Wikipedia: Vertical farming](https://en.wikipedia.org/wiki/Vertical_farming) |

### Успех (9)

| # | case_name | year | outcome | confidence | axis1_level / mechanism | axis2_bucket / mechanism | axis3_class | axis4_gate / blast_radius | external_driver | Что произошло (цифры) | source_url |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S1 | GUSS Automation — автономные опрыскиватели садов | 2024 | success | high | moderate / none | season-years / F-A | sensor-fusion | yes / low | not-applicable | >250 машин развёрнуто по миру, 2,6M акров обработано, 500 000 автономных часов на момент отчёта; John Deere в 2024 полностью выкупил GUSS Automation и представил электрическую версию опрыскивателя на World Ag Expo 2024. | [Electrek](https://electrek.co/2024/02/20/meet-guss-an-electric-autonomous-sprayer-from-john-deere/), [AgDaily](https://www.agdaily.com/news/autonomous-sprayer-brand-guss-fully-mergers-into-john-deere/) |
| S2 | Greeneye Technology — brand-agnostic precision spray | 2022 | success | medium | moderate / none | season-years / F-A | deep-learning | yes / low | not-applicable | Первая компания, коммерчески запустившая precision-spray технологию в США (2022) — 120-футовые алюминиевые бумы с 24 камерами (5000 изображений/сек каждая), устанавливаются на любой бренд опрыскивателя (Hagie/Case/New Holland/John Deere), конкурент, не партнёр See & Spray; заявленная экономия гербицидов >80% (цифра вендора, не аудирована независимо). | [FarmProgress](https://www.farmprogress.com/farming-equipment/greeneye-spray-booms-are-here-but-hard-to-get), [Greeneye press](https://www.greeneye.ag/press-releases/greeneye-technology-precision-spraying-system-now-available-for-cotton) |
| S3 | Semios — сеть умных ловушек-предикторов вредителей | 2020 | success | medium | moderate / none | hours-days / F-B | sensor-fusion | yes / low | not-applicable | >1 млн сенсоров в работе на момент публикации (сент. 2020); выручка росла двукратно год к году с 2015; раунд $99M объявлен в том же году; ключевой baseline/counterfactual явно назван источником — традиционный мониторинг требовал обхода поля раз в 12-14 дней, система даёт ежедневные данные. | [Research2Reality](https://research2reality.com/energy-environment-nature/natural-resources/semios-weather-forecasting-farming-almanac-agriculture/) |
| S4 | Vence — приобретена Merck Animal Health | 2022 | success | high | moderate / none | hours-days / F-B | sensor-fusion | yes / medium | not-applicable | Merck Animal Health подписала соглашение о приобретении Vence (virtual fencing для КРС — GPS-ошейники + звук/вибрация вместо физического забора) в сентябре 2022; сделка явно названа частью растущего портфеля «интеллектуальных» продуктов identification/traceability/monitoring Merck. | [DTN/Progressive Farmer](https://www.dtnpf.com/agriculture/web/ag/livestock/article/2022/10/17/merck-acquires-new-virtual-fencing), [Drovers](https://www.drovers.com/news/industry/merck-animal-health-acquire-vence) |
| S5 | Halter — virtual fencing (Новая Зеландия) | 2024 | success | high | moderate / none | hours-days / F-B | sensor-fusion | yes / medium | not-applicable | Solar-powered GPS-ошейники для КРС + приложение; >1000 ферм-пользователей в Новой Зеландии (1 из 10 ранчо NZ), 207 000 км виртуальных заборов выставлено за 2024 год; Series D на NZ$165M в нояб. 2024 по оценке $1B. | [Wikipedia: Halter (company)](https://en.wikipedia.org/wiki/Halter_(company)), [BusinessWire (Series E, 2026, контекст истории раундов)](https://www.businesswire.com/news/home/20260324036414/en/Halter-Raises-$220M-in-Series-E-to-Accelerate-Global-Expansion-of-Virtual-Fencing) |
| S6 | ecoRobotix ARA — коммерческий запуск в ЕС | 2023 | success | medium | moderate / none | season-years / F-A | deep-learning | yes / low | not-applicable | ARA (швейцарский high-precision опрыскиватель, AI-based распознавание растений для point-and-shoot внесения) анонсирован как «коммерчески доступен и используется по ЕС» в февр. 2023; полевые испытания — экономия гербицидов 70-95%, заявленный общий эффект 80-95%, потенциальный прирост урожайности ~5%+. Цифры эффекта от самой компании, независимого аудита нет — отсюда `confidence: medium`. | [PRNewswire](https://www.prnewswire.com/news-releases/ecorobotixs-ara-ultra-high-precision-sprayer-a-game-changer-for-sustainable-crop-protection-301757183.html) |
| S7 | OneSoil — расширение распознавания культур по спутнику | 2026 | success | medium | moderate / none | season-years / F-A | classical-ml | yes / low | not-applicable | Бесплатное спутниковое приложение расширило распознавание культур с 12 до 28 культур (объявлено 27 окт. 2026); точность 90-95% в проверенных регионах; доступно в >45 странах (Европа, США, Канада, Аргентина, Бразилия, ЮАР, Австралия, Казахстан); обучено на собственном датасете ~2 млн полей, накопленном с 2016 года. | [Farmers Review Africa](https://farmersreviewafrica.com/onesoil-global-analytics-now-identifies-up-to-28-crops-from-satellite-imagery-up-from-12/) |
| S8 | Blue River Technology — ранний See & Spray (до «Ultimate») | 2019 | success | medium | moderate / U2 | season-years / F-A | deep-learning | yes / low | not-applicable | John Deere купил Blue River Technology за $305M (сент. 2017); к 2018-2019 коммерческие развёртывания селективного опрыскивания на базе CV+нейросетей на хлопке и сое в США цитируются источниками как сокращение расхода гербицида «на две трети или больше». **Это другая, более ранняя и узкая по домену генерация той же продуктовой линии**, чем See & Spray Ultimate (волна 1, 2025 год, 5M акров) — см. явную оговорку о пересечении ниже. | [AgFunderNews](https://agfundernews.com/breaking-exclusive-john-deere-acquires-see-spray-robotics-startup-blue-river-technology-305m), [The Robot Report](https://www.therobotreport.com/startup-blue-river-technology-sells-deere-305-million/) |
| S9 | smaXtec — бolus-сенсор + ИИ для здоровья КРС | 2026 | success | medium | moderate / none | hours-days / F-B | sensor-fusion | yes / low | not-applicable | Рубцовый болюс-сенсор (внутренняя температура ±0,01°C) + «ИИ-анализ данных» на непрерывном потоке; >1 млн подключённых коров по миру, 256+ млрд точек данных/день; именованные case study-фермеры: инволюнтарный убой снижен с ~5,5% до ~2% (650 голов, Камбрия), антибиотики сокращены на ~60% (350 голов, Типперэри), интервал между отёлами снижен на >30 дней за 12 мес (70 голов, Дамфрис); средний payback <9 месяцев; совместный продукт SmartCalving получил Gold на EuroTier Innovation Award 2026 — частично независимая проверка (отраслевая награда), цифры эффекта в остальном с собственного сайта вендора. | [smaXtec](https://www.smaxtec.com/en/) |

### Частичный результат / неопределённо (7)

| # | case_name | year | outcome | confidence | axis1_level / mechanism | axis2_bucket / mechanism | axis3_class | axis4_gate / blast_radius | external_driver | Что произошло (цифры) | source_url |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U1 | AgEagle Aerial Systems — going concern | 2023 | partial | high | unclear / unclear | weeks-months / unclear | sensor-fusion | not-applicable / medium | mixed | Публично торгуемая drone+ML-аналитика (MicaSense/senseFly мультиспектральные сенсоры, Measure Global аналитика, платформы HempOverview/Ground Control) заявила «существенное сомнение в способности продолжать деятельность» в SEC-отчётности; за первые 6 мес. 2023 — выручка $7,3M (-20% г/г), чистый убыток $(9,9)M, кэш $4,2M, накопленный дефицит $(126,4)M. К 2024 убыток сократился до $12,6M с $39,2M (2023) — компания выжила, но не вышла из зоны риска. | [SEC Form 424B3](https://www.sec.gov/Archives/edgar/data/8504/000149315224008249/form424b3.htm) |
| U2 | Local Bounti — реструктуризация долга под угрозой going concern | 2025 | partial | medium | low / none | season-years / none | unclear | not-applicable / medium | mixed | CEA-теплицы (не чисто вертикальная ферма) с «существенным сомнением в способности продолжать деятельность»; в 2025 реструктурировала $197M долга, получила $25M нового финансирования, усилена поддержка Cargill (март 2025); продажи выросли на 27-38% г/г, но долг $483M и проценты съедают весь gross margin. **ИИ-специфичность продукта в найденных источниках не детализирована** (CEA greenhouse software, не названо явно ИИ/ML) — отсюда axis3_class `unclear`, а не `hybrid`. | [SEC Form 424B3](https://www.sec.gov/Archives/edgar/data/1840780/000162828025055865/localbounti-final424b3nov2.htm), [Morningstar/PR Newswire](https://www.morningstar.com/news/pr-newswire/20251112dc22104/local-bounti-announces-third-quarter-2025-financial-results) |
| U3 | Root AI (Virgo) — приобретена AppHarvest | 2021 | partial | high | moderate / U1 | unclear / none | deep-learning | not-applicable / low | mixed | CV+ИК-лазерный робот-харвестер Virgo (идентифицирует >50 сортов томата плюс перец/огурцы) куплен AppHarvest за $60M (апр. 2021, ~$10M наличными + акции); 19 сотрудников Root AI перешли в AppHarvest, сооснователь стал CTO. **На момент сделки — явный успех** (валидированная технология, экзит); но сама AppHarvest (не повторяется здесь, это кейс волны 1 F7) подала на Chapter 11 в 2023 — отсюда `outcome: partial`, а не чистый success, чтобы не скрывать итоговую судьбу материнской компании. | [The Robot Report](https://www.therobotreport.com/root-ai-acquired-by-appharvest-for-60m/), [AgFunderNews](https://agfundernews.com/appharvest-acquires-root-ai-to-add-ai-powered-harvesting-robots-to-its-workforce) |
| U4 | Aigen — solar-powered автономный полевой робот (Element) | 2023 | partial | medium | moderate / unclear | season-years / F-A | hybrid | yes / low | not-applicable | $12M Series A (нояб. 2023, итого $19M с учётом seed 2022); пилотные испытания с клиентами в Северной Дакоте в течение сезона 2023; план развёртывания на >20 000 акров анонсирован на апрель 2024 — т.е. на момент самого раунда это ещё пилотный, не доказанный в масштабе кейс, отсюда `partial`, не `success`. Экипажи из 5 роботов покрывают 200 акров за сезон; автономная работа до 14 часов без подзарядки от сети. | [AgFunderNews](https://agfundernews.com/aigen-raises-12m-to-scale-its-fleet-of-solar-powered-autonomous-robots-to-more-than-20000-acres), [GeekWire](https://www.geekwire.com/2023/aigen-a-seattle-startup-that-sells-a-solar-powered-weed-thumping-robot-lands-12m/) |
| U5 | Four Growers — Series A, ИИ-робот для теплиц | 2024 | partial | medium | high / unclear | weeks-months / unclear | deep-learning | not-applicable / low | not-applicable | YC-backed стартап привлёк $9M Series A (нояб. 2024) на масштабирование автономного робота-харвестера томатов для теплиц, явно позиционированного как ответ на дефицит рабочей силы; на момент раунда — ранняя стадия, публичных цифр промышленного масштаба развёртывания не найдено, поэтому `outcome: partial`, не `success`. | [TechCrunch](https://techcrunch.com/2024/11/20/yc-backed-four-growers-builds-robots-to-help-solve-greenhouse-labor-shortages/), [The Packer](https://www.thepacker.com/news/packer-tech/four-growers-secures-9m-scale-production-harvesting-robot) |
| U6 | Trace Genomics — ДНК-секвенирование почвы + ML | 2018 | partial | medium | moderate / none | season-years / F-A | classical-ml | yes / low | not-applicable | $13M Series A (нояб. 2018, итого $19M); протестировано >150 000 акров почвы для фермеров 70+ культур фруктов/овощей, пропускная способность 1000+ образцов/неделю; именованный пример клиента — экономия $100/акр за счёт отказа от ненужного фунгицида plus видимый прирост урожайности в следующем сезоне. Единичный клиентский анекдот, не широкая выборка — отсюда `partial`, не `success`. | [Global AgInvesting](https://globalaginvesting.com/trace-genomics-raises-13m-scalable-ai-enabled-soil-microbiome-technology/) |
| U7 | Harvest CROO Robotics — B8 «pick-to-pack» клубничный харвестер | 2025 | undetermined | low | extreme / U1 | season-years / F-A | deep-learning | unclear / unclear | unclear | Платформа из 16 роботов, Nvidia-процессоры, заявлена «индустрией первое pick-to-pack решение»; вендорский/спонсируемый материал (Nutanix) заявляет, что «>70% индустрии выращивания клубники в США инвестировали» в систему. **Это прямо противоречит** собственному выводу основного реестра лекции (`razmetka/lec-10.md`, s21) о категории «робот-сборщик клубники» как затянувшемся, коммерчески не состоявшемся pilot после 10-15 лет R&D — противоречие не разрешено независимой проверкой (бюджет WebSearch исчерпан), отсюда `outcome: undetermined`, `confidence: low`, а не принятие более благоприятной вендорской версии. | [Nutanix / The Forecast](https://www.nutanix.com/theforecastbynutanix/profile/ai-robots-and-strawberries-advance-ag-tech) |

## Итог по годам

| Год | Провал | Успех | Частичный/неопр. | Комментарий |
|---|---|---|---|---|
| 2018 | — | — | 1 (Trace Genomics) | Закрывает часть заявленного пробела 2018-2021 волны 1 |
| 2019 | — | 1 (Blue River, ранний See & Spray) | — | Та же цель — ранняя точка до пробела |
| 2020 | — | 1 (Semios) | — | |
| 2021 | 1 (Abundant Robotics) | — | 1 (Root AI) | |
| 2022 | 1 (Fifth Season) | 2 (Greeneye, Vence) | — | |
| 2023 | 2 (Kalera, Upward Farms) | 1 (ecoRobotix) | 2 (AgEagle, Aigen) | |
| 2024 | 2 (Gro Intelligence, Smallhold) | 1 (GUSS Automation) | 1 (Four Growers) | |
| 2025 | 3 (Benson Hill, Jones Food Company, Microsoft ADMA) | — | 2 (Local Bounti, Harvest CROO) | Самый плотный год по провалам в этой волне |
| 2026 | — | 2 (OneSoil, smaXtec) | — | Оба — реально датированные 2026-события (не выводная дата, в отличие от S7 волны 1) |
| **Итого** | **9** | **9** | **7** | **25** |

**Пробел 2018-2021 волны 1 — частично закрыт.** Волна 1 честно констатировала отсутствие
верифицированного успеха за 2022 год и неуверенность в дате 2026-кейса; эта волна добавляет три
новых года (2018, 2019, 2020) и по одному дополнительному кейсу на 2021 и 2022 — итоговая выборка
по годам 2018-2021 всё ещё тоньше, чем 2022-2025 (характерно для доступности верифицируемых
AgTech-материалов в интернете, которые смещены к недавним новостям), но больше не пустая.

## Пересечение с волной 1 и основным реестром — явные оговорки

- **S8 (Blue River Technology, 2019) — та же продуктовая линия, что F-кейс волны 1 и s07
  основного реестра («See & Spray Ultimate», 2025).** Это не задвоенный кейс: цифры, год, домен
  (хлопок/соя vs. 2025-масштаб 5M акров любых культур) и даже риск-профиль (в 2025-версии явно
  задокументирован domain shift в Cerrado, которого в 2018-2019 версии источники не упоминают,
  потому что она не развёртывалась за пределами США) — разные. Включено как содержательно иная,
  более ранняя и более узкая точка той же эволюционной линии, с этой явной оговоркой.
- **U3 (Root AI, 2021) — связан с AppHarvest (волна 1, F7, Chapter 11 2023) как материнская
  компания.** Сам Root AI как отдельная сделка не повторяет F7 волны 1 (разные даты, разные
  цифры, разный тип события — M&A vs. банкротство), но итоговая судьба материнской компании —
  причина, по которой это помечено `partial`, а не `success`.
- **U7 (Harvest CROO Robotics) — прямо пересекается по смыслу (не по имени) с генерик-категорией
  основного реестра** («Робот-сборщик клубники (категория, DailyRobotics и др.)», s21,
  `razmetka/lec-10.md`) **и даёт противоположный вывод** (вендор утверждает >70% проникновение
  индустрии против вывода реестра о структурном провале категории). Решение — не выбирать более
  удобную версию, а оставить противоречие явным и понизить confidence, а не confidence одной из
  двух сторон произвольно.
- Все остальные 22 кейса — проверены построчно против списка 20 кейсов волны 1 (из постановки
  задачи) и построчно против 54 названий `razmetka/lec-10.md` — текстовых совпадений вендоров не
  найдено.

## Что это даёт линии #349

25 новых кейсов, из них 9 провалов / 9 успехов / 7 частичных-неопределённых — более сбалансированное
распределение исходов, чем у волны 1 (10 провалов/7 успехов при честном недоборе), и три новых
года покрытия (2018-2020), которых не было ни в волне 1, ни в быстро прочитанных строках основного
реестра. Готово к сведению в общий companion-реестр тем же способом, что волна 1 и сделанные ранее
12 кейсов (см. `15-itogovaya-svodka-linii-349.md` при будущем объединении).
