---
title: "Лекция 8 (trust-recognition) — внешне верифицированные кейсы, волна 2, issue #349"
type: research
issue: "#349"
date: 2026-11-20
---

# Лекция 8 — trust-recognition: 30 внешне верифицированных кейсов, волна 2 (2018–2026)

## Подход к поиску

Та же отрасль, что в волне 1 (`verified-cases/lec-08-verified.md`, 23 кейса) — биометрия
лица/голоса/радужки, дипфейки, доверенные системы идентификации — но с явным заданием **не
повторять** 23 кейса волны 1 (список исключений дан в задаче: US CBP, CLEAR Plus, Changi FAST,
NIST FRTE/FATE, Mastercard/Payface, Apple Optic ID, NEC Зимбабве, World ID/Orb, Reality Defender,
Ferrari, IRS/ID.me, Rite Aid, Детройт/Woodruff, фейк «взрыв у Пентагона», Worldcoin/Кения,
Lloyds Voice ID, Arup, робоколл Байдена, Южная Корея/Telegram, Meta DFDC, индикт $129М, Met Police,
Clearview BIPA-расчёт) и **закрыть провал волны 1 по годам 2018–2021**, которые в волне 1 были
покрыты слабо (волна 1 — окно 2022–2026 почти целиком).

Поиск вёлся сериями `WebSearch` по под-темам: (а) ранние (2018–2021) дипфейк-мошенничества
голосом — первые документированные случаи клонирования голоса CEO; (б) ранние wrongful-arrest
кейсы распознавания лиц в США (Parks, Williams, Reid — отдельно от уже использованного в волне 1
Woodruff); (в) ранние регуляторные/судебные прецеденты против Clearview AI по юрисдикциям,
отличным от иска BIPA (UK ICO, Италия, Швеция, Канада, Австралия, Франция — каждый с собственной
датой, суммой и типом исхода); (г) муниципальные запреты распознавания лиц в США (Сан-Франциско,
Портленд); (д) академические/активистские тесты точности и предвзятости (ACLU×Amazon Rekognition
2018, Gender Shades 2018); (е) политические и корпоративные дипфейки 2020–2024 (BJP/Тивари,
Зеленский, WPP, Словакия, Tom Hanks, школа Pikesville); (ж) производственные биометрические
системы с заявленной статистикой (Москва Face Pay, India Digi Yatra, Intel FakeCatcher);
(з) обход liveness-проверки в Китае (налоговая система, 2018–2021).

Бюджет `WebSearch` в этой сессии был исчерпан (200/200) после 24 серий запросов — следующие
несколько запланированных тем (HSBC Voice ID, Amazon One, Barclays voice biometrics, Facewatch UK,
Dubai Smart Tunnel) пришлось закрывать точечными `WebFetch` по известным URL, а не полнотекстовым
поиском. Два найденных таким образом кандидата — Amazon One (запуск 2020 → 500+ точек к 2023 →
полное закрытие сервиса в 2026) и дипфейк-порно против журналистки Rana Ayyub (2018) — **сознательно
исключены** из итоговой таблицы: единственным доступным источником по ним после исчерпания
бюджета оказалась Wikipedia (агрегатор, прямо запрещённый заданием), а попытки дотянуться до
первоисточника (HuffPost-статья Ayyub, статья The Verge/CNBC про остановку Amazon One) вернули
404 без возможности повторного поиска замены. Решено не включать два кейса со слабым
источником вместо того, чтобы штамповать Wikipedia-ссылку — то же правило, которым волна 1
руководствовалась, отбраковывая Aadhaar при разошедшихся цифрах.

**Покрытие по годам — все восемь лет 2018–2026 присутствуют, перекос в сторону 2018–2022 —
намеренный** (это была явная цель задания): 2018 — 2 кейса (ACLU×Rekognition, Gender Shades);
2019 — 3 (UK voice-дипфейк, Parks, запрет Сан-Франциско); 2020 — 6 (банк ОАЭ, Williams, Facebook
BIPA, запрет Портленда, BJP/Тивари, Guo Bing); 2021 — 6 (TikTok BIPA, Москва Face Pay, Шанхай,
Швеция/IMY, Канада, Австралия/OAIC); 2022 — 7 (Reid-арест, Clearview UK, Clearview Италия,
Зеленский, Google BIPA, Intel FakeCatcher, Франция/CNIL); 2023 — 4 (Digi Yatra, Retool, Словакия,
Tom Hanks); 2024 — 2 (WPP, Pikesville). 30 кейсов, ноль совпадений с волной 1 по названию/компании/
инциденту (сверено построчно против списка исключения из задачи).

**Честная оговорка №1 — кластер из шести юрисдикций против Clearview AI (кейсы 6, 7, 26–29).**
Это не искусственное раздувание счёта одним и тем же инцидентом: UK ICO, Италия, Швеция, Канада,
Австралия и Франция — шесть **разных** регуляторов, с разными датами, разными суммами (от €0
штрафа в Канаде/Австралии — только предписания без денежного штрафа — до €20+5,2 млн во Франции),
и, что важнее для осей курса, **разным итоговым исходом для одного и того же базового нарушения**:
британский штраф был впоследствии **отменён** трибуналом по вопросу юрисдикции (Clearview выиграла
апелляцию), тогда как французский штраф **эскалировал** (к первому €20 млн добавили ещё €5,2 млн за
неисполнение). Это прямое продолжение наблюдения волны 1 про Worldcoin/Кению: один и тот же
технический продукт и одно и то же нарушение дают принципиально разные институциональные исходы
в разных юрисдикциях — `external_driver` здесь решает исход сильнее, чем сама технология, причём
теперь это видно не на двух, а на шести независимых точках данных.

**Честная оговорка №2 — «техническая работа получилась, цель не достигнута» (кейсы 13, 22).**
И индийский дипфейк BJP/Тивари 2020, и словацкий аудио-дипфейк 2023 — это случаи, где сама
генеративная технология сработала (убедительный липсинк, убедительный клон голоса, широкое
распространение), но партия, в пользу которой был создан дипфейк, **проиграла** выборы (BJP — с
разгромным счётом 8 против 62 мест AAP в Дели; Progressive Slovakia — узко Smer-SD Фицо).
Размечено как `outcome=partial`, а не `success`/`failure` в чистом виде: технический успех
генерации ≠ успех заявленной цели использования. Для словацкого кейса отдельно учтена академическая
статья (Harvard Kennedy School Misinformation Review), прямо ставящая под вопрос причинно-следственную
связь между дипфейком и результатом выборов — отсюда `confidence=low`, а не `medium`: это тот же
паттерн «две оценки разошлись», что Metropolitan Police в волне 1.

**Честная оговорка №3 — качество источников неоднородно по кейсам.** Судебные/регуляторные
решения (ICO, Garante, CNIL, IMY, OAIC, Privacy Commissioner Canada, FTC-аналог здесь не нужен,
суд Фуяна/Ханчжоу) — высокая надёжность, решение есть зафиксированный факт. Академические работы
(Gender Shades, статья HKS про Словакию) — высокая надёжность методологии, но для Словакии прямо
оспорен причинный вывод. Корпоративные самоотчёты про продакшн-масштаб (Москва Face Pay — цифры
департамента транспорта Москвы; India Digi Yatra — цифры PIB, то есть пресс-служба правительства
Индии; Intel FakeCatcher — 96% точность — единственная цифра во всём файле, взятая из
пресс-релиза вендора без упоминания независимого продакшн-деплоя или третьей стороны) размечены
`confidence=medium` или `confidence=low` сообразно.

## Таблица

| case_name | year | source_url | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| UK-энергокомпания — голосовой дипфейк «немецкого CEO» вынудил перевести €220 тыс. ($243 тыс.) венгерскому поставщику | 2019 | [Sophos — Scammers deepfake CEO's voice](https://news.sophos.com/en-us/2019/09/05/scammers-deepfake-ceos-voice-to-talk-underling-into-243000-transfer/) | extreme | U1 | seconds-minutes | F-C | deep-learning | no | medium | no | failure | medium |
| Банк в ОАЭ — «deep voice»-клон голоса директора компании, перевод $35 млн на подтверждение несуществующей сделки | 2020 | [Futurism — Bank robbers deepfaking voice](https://futurism.com/the-byte/bank-robbers-deepfaking-voice) | extreme | U1 | hours-days | F-C | deep-learning | no | catastrophic | no | failure | medium |
| Детройт — Robert Williams, ошибочный арест по распознаванию лиц (DataWorks Plus), $300 тыс. урегулирование в 2024 | 2020 | [Reason — Faulty facial recognition tech $300,000 payout](https://reason.com/2024/07/23/faulty-facial-recognition-tech-got-him-arrested-now-hes-getting-a-300000-payout/) | high | U3 | hours-days | F-A | deep-learning | no | high | no | failure | high |
| Нью-Джерси — Nijeer Parks, арест по размытому фото из распознавания лиц, 10 суток в СИЗО | 2019 | [ACLU-NJ — Face recognition landed one innocent man in jail ten days](https://www.aclu-nj.org/news/how-face-recognition-technology-landed-one-innocent-man-new-jersey-jail-ten-days/) | high | U3 | hours-days | F-A | deep-learning | no | high | no | failure | high |
| Джорджия/Луизиана — Randal Reid, арест по единственному совпадению распознавания лиц в штате, где он никогда не был, $200 тыс. урегулирование | 2022 | [BiometricUpdate — wrongful arrest $200K settlement](https://www.biometricupdate.com/202506/wrongful-arrest-in-us-linked-to-facial-recognition-error-leads-to-200k-settlement) | high | U3 | hours-days | F-A | deep-learning | no | high | no | failure | high |
| Clearview AI — штраф ICO Великобритании £7,5 млн за биометрию британцев без согласия, позже отменён трибуналом по вопросу юрисдикции | 2022 | [TechCrunch — UK fines Clearview for privacy breaches](https://techcrunch.com/2022/05/23/clearview-uk-ico-fine/) | unclear | none | season-years | F-A | deep-learning | no | high | mixed | partial | medium |
| Clearview AI — штраф итальянского Garante €20 млн за незаконный биометрический мониторинг граждан | 2022 | [Engadget — Italy fines Clearview AI €20 million](https://www.engadget.com/italy-slaps-facial-recognition-firm-clearview-ai-with-20-million-euro-fine-212500675.html) | moderate | none | season-years | F-A | deep-learning | no | high | yes | failure | high |
| Facebook — $650 млн по иску BIPA Иллинойса за автотэггинг лиц в «тэгах» без согласия | 2020 | [ABA — Historic Biometric Privacy Suit Settles for $650 Million](https://www.americanbar.org/groups/business_law/resources/business-law-today/2021-february/historic-biometric-privacy-settlement/) | moderate | none | season-years | F-A | deep-learning | no | high | no | failure | high |
| Сан-Франциско — первый в США запрет распознавания лиц городскими службами и полицией | 2019 | [NPR — San Francisco first US city to ban facial recognition](https://www.npr.org/2019/05/15/723466452/san-francisco-is-first-u-s-city-to-ban-facial-recognition-technology) | moderate | none | weeks-months | F-A | unclear | no | medium | yes | failure | high |
| Портленд — самый широкий в США запрет распознавания лиц, включая частный бизнес в общественных местах | 2020 | [TechCrunch — Portland passes expansive ban](https://techcrunch.com/2020/09/09/facial-recognition-ban-portland-oregon/) | moderate | none | weeks-months | F-A | unclear | no | high | yes | failure | high |
| ACLU×Amazon Rekognition — 28 членов Конгресса США ошибочно сопоставлены с базой мугшотов, расовый перекос | 2018 | [ACLU — Amazon's Face Recognition Falsely Matched 28 Members of Congress](https://www.aclu.org/press-releases/amazon-facial-surveillance-technology-falsely-identifies-28-members-congress-mugshots) | high | U3 | seconds-minutes | F-C | deep-learning | not-applicable | medium | no | failure | high |
| Gender Shades (Buolamwini/Gebru) — ошибка классификации пола до 34,7% у темнокожих женщин против 0,8% у светлокожих мужчин (IBM, Microsoft, Face++) | 2018 | [MIT News — Study finds gender and skin-type bias](https://news.mit.edu/2018/study-finds-gender-skin-type-bias-artificial-intelligence-systems-0212) | high | U3 | season-years | F-A | deep-learning | not-applicable | medium | no | failure | high |
| BJP/Manoj Tiwari — липсинк-дипфейк на хариянви разослан через 5000+ групп WhatsApp ~15 млн зрителям; партия всё равно проиграла выборы в Дели | 2020 | [ThePrint — Why the Manoj Tiwari deepfakes should worry India](https://theprint.in/tech/why-the-manoj-tiwari-deepfakes-should-have-india-deeply-worried/372389/) | high | U1 | weeks-months | F-B | deep-learning | no | medium | mixed | partial | medium |
| Дипфейк «сдачи» Зеленского — распространён после взлома телеканала, удалён Meta/YouTube в течение дня из-за явных артефактов | 2022 | [NPR — Deepfake video of Zelenskyy](https://www.npr.org/2022/03/16/1087062648/deepfake-video-zelenskyy-experts-war-manipulation-ukraine-russia) | high | U1 | seconds-minutes | F-C | deep-learning | yes | high | no | failure | high |
| Google — $100 млн по иску BIPA за биометрию в Face Grouping Google Photos (2015–2022) | 2022 | [Engadget — Google settles Photos facial recognition lawsuit](https://www.engadget.com/google-photos-bipa-lawsuit-settlement-161237789.html) | moderate | none | season-years | F-A | deep-learning | no | high | no | failure | high |
| TikTok — $92 млн по иску BIPA за биометрию лиц пользователей, включая несовершеннолетних | 2021 | [Variety — TikTok agrees to pay $92 million](https://variety.com/2021/digital/news/tiktok-privacy-lawsuit-payment-92-million-1234915736/) | moderate | none | season-years | F-A | deep-learning | no | high | no | failure | high |
| Московское метро Face Pay — 122 тыс. пользователей и 12,7 млн поездок оплачено биометрией к концу первого года | 2021 | [BiometricUpdate — Face biometric payments launch at scale in Moscow Metro](https://www.biometricupdate.com/202110/face-biometric-payments-launch-at-scale-in-moscow-metro) | low | none | seconds-minutes | F-C | deep-learning | yes | low | not-applicable | success | medium |
| India Digi Yatra — биометрический посадочный контроль в аэропортах, 1 млн пользователей к июню 2023 | 2023 | [PIB India — Digi Yatra passenger benefit update](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1901737&reg=48&lang=2) | low | none | seconds-minutes | F-C | deep-learning | yes | low | not-applicable | success | medium |
| Intel FakeCatcher — детектор дипфейков по сигналу кровотока в пикселях, заявлена точность 96% в реальном времени | 2022 | [Intel Newsroom — Intel Introduces Real-Time Deepfake Detector](https://newsroom.intel.com/artificial-intelligence/intel-introduces-real-time-deepfake-detector) | extreme | none | seconds-minutes | F-C | hybrid | not-applicable | unclear | not-applicable | success | low |
| Retool/Fortress Trust — голосовой дипфейк коллеги + SMS-фишинг обошли MFA, кража $15 млн у клиента-криптокомпании | 2023 | [IBM — How a new wave of deepfake-driven cyber crime targets businesses](https://www.ibm.com/think/insights/new-wave-deepfake-cybercrime) | extreme | U1 | seconds-minutes | F-C | deep-learning | no | catastrophic | no | failure | high |
| WPP — попытка дипфейк-атаки на гендира (Teams-встреча, голосовой клон, YouTube-видео) сорвана без потери денег | 2024 | [DesignRush — WPP CEO addresses deepfake scam attempt](https://www.designrush.com/news/wpp-ceo-addresses-deepfake-scam-attempt) | extreme | U1 | seconds-minutes | F-C | sensor-fusion | yes | low | no | success | high |
| Словакия — аудио-дипфейк лидера партии о подкупе голосов распространён за 48 часов до выборов; партия проиграла, причинный эффект оспорен академически | 2023 | [HKS Misinformation Review — Beyond the deepfake hype: the Slovak case](https://misinforeview.hks.harvard.edu/article/beyond-the-deepfake-hype-ai-democracy-and-the-slovak-case/) | high | U1 | hours-days | F-B | foundation-model | no | high | mixed | partial | low |
| Tom Hanks — несанкционированная реклама стоматологического плана с дипфейк-видео актёра | 2023 | [Deadline — Tom Hanks warns fans it's not him](https://deadline.com/2023/10/tom-hanks-warns-fans-that-its-not-him-pitching-a-dental-plan-in-ai-created-video-1235561184/) | moderate | U1 | hours-days | F-C | deep-learning | no | medium | no | failure | high |
| Шанхай — обход liveness-проверки налоговой системы Китая дипфейк-видео по купленным фото, фиктивные счета на ¥500 млн | 2021 | [SCMP — Chinese government-run facial recognition system hacked by tax fraudsters](https://www.scmp.com/tech/tech-trends/article/3127645/chinese-government-run-facial-recognition-system-hacked-tax) | extreme | U1 | season-years | F-A | deep-learning | yes | high | no | failure | high |
| Guo Bing v. Hangzhou Safari Park — первый в Китае суд по распознаванию лиц, зоопарк обязан удалить биометрию посетителя | 2020 | [CGTN — Chinese court finds for plaintiff in first facial recognition lawsuit](https://news.cgtn.com/news/2020-11-22/Chinese-court-finds-for-plaintiff-in-first-facial-recognition-lawsuit-VCxkZY4gOA/index.html) | moderate | none | season-years | F-A | deep-learning | no | medium | yes | failure | high |
| Швеция — штраф полиции €250 тыс. за нелегальное применение Clearview AI без оценки воздействия на защиту данных (DPIA) | 2021 | [ComputerWeekly — Swedish police fined for unlawful use of facial-recognition app](https://www.computerweekly.com/news/252496545/Swedish-police-fined-for-unlawful-use-of-facial-recognition-app) | moderate | none | season-years | F-A | deep-learning | no | medium | yes | failure | high |
| Канада — комиссары по приватности признали сбор биометрии Clearview AI «массовым слежением» за канадцами | 2021 | [OPC Canada — Clearview AI's unlawful practices represented mass surveillance](https://www.priv.gc.ca/en/opc-news/news-and-announcements/2021/nr-c_210203/) | moderate | none | season-years | F-A | deep-learning | no | high | yes | failure | high |
| Австралия OAIC — приказ Clearview AI уничтожить биометрию австралийцев, решение подтверждено апелляцией в 2023 | 2021 | [OAIC — Clearview AI breached Australians' privacy](https://www.oaic.gov.au/news/media-centre/clearview-ai-breached-australians-privacy) | moderate | none | season-years | F-A | deep-learning | no | medium | yes | failure | high |
| Франция CNIL — штраф Clearview AI €20 млн, затем ещё €5,2 млн за неисполнение приказа об удалении данных | 2022 | [Hunton — CNIL fines Clearview AI 20 million euros](https://www.hunton.com/privacy-and-cybersecurity-law-blog/cnil-fines-clearview-ai-20-million-euros-for-unlawful-use-of-facial-recognition-technology) | moderate | none | season-years | F-A | deep-learning | no | high | yes | failure | high |
| Балтимор/Pikesville — завхоз школы создал ИИ-аудио «расистской тирады» директора из мести, разоблачён ФБР за 3 месяца, осуждён | 2024 | [Washington Post — Baltimore AI voice audio framing principal](https://www.washingtonpost.com/dc-md-va/2024/04/26/baltimore-ai-voice-audio-framing-principal/) | high | U1 | weeks-months | F-A | deep-learning | no | high | no | failure | high |

**Итог по счёту:** 30 кейсов, из них **4 success** (Москва Face Pay, India Digi Yatra, Intel
FakeCatcher, WPP), **3 partial** (Clearview AI/ICO UK, BJP/Тивари, Словакия), **23 failure** —
4 + 3 + 23 = 30. Перекос в сторону `failure` —
не артефакт подбора, а честный портрет найденного материала: в этой волне целенаправленно искались
ранние (2018–2021) судебные/регуляторные прецеденты и wrongful-arrest кейсы, которые по своей
природе — зафиксированные провалы (это и есть событие, которое попадает в новости и в судебные
архивы), тогда как «тихие» успешные биометрические деплои 2018–2021 года (банковский Voice ID,
Amazon One и т.п.) либо не публикуют независимо проверяемых цифр, либо источник оказался
аггрегатором без первоисточника (см. «Честная оговорка №3» и исключённые Amazon One/Rana Ayyub
выше) — это зафиксировано как пробел, а не скрыто.

## Что это добавляет к рамке осей (контрпримеры и подтверждения — названы прямо)

- **Подтверждение «гейт — сильнейший предиктор», третий и четвёртый независимый кейс.** WPP
  (success, `axis4_gate=yes` — цель насторожилась и не перевела денег/данные) против банка ОАЭ,
  UK-энергокомпании, Retool/Fortress Trust и Шанхая (все `failure`, `axis4_gate=no` или гейт
  присутствовал технически, но был обойдён) — тот же паттерн Ferrari/Arup из волны 1, теперь на
  пяти новых кейсах голосовых и видео-дипфейков подряд, от 2019 до 2024 года: наличие гейта
  предсказывает исход лучше, чем качество самого дипфейка.
- **Юрисдикционный кластер Clearview AI (6 кейсов) — институциональный контекст решает исход
  сильнее техники, на бóльшей выборке, чем Worldcoin/Кения в волне 1.** Один и тот же продукт,
  одно и то же нарушение (сбор биометрии без согласия) — но Канада и Австралия ограничились
  предписаниями без штрафа, Швеция/Италия/Франция — штрафы разного размера, Франция —
  эскалирующий штраф, а Великобритания — штраф, который был полностью **отменён** на апелляции по
  вопросу юрисдикции. `external_driver=yes/mixed` здесь не формальность: один и тот же
  `axis1`–`axis3` профиль даёт шесть разных `outcome`/`axis4_blast_radius` в зависимости от
  юрисдикции — не от модели.
- **«Техническая удача ≠ успех цели» — новый, не встречавшийся в волне 1 паттерн (BJP/Тивари,
  Словакия).** В обоих кейсах генеративная технология выполнила заявленную техническую задачу
  (убедительный липсинк/голос, широкое распространение), но политическая цель использования —
  провалена (проигранные выборы в обоих случаях). Это ось, которую текущая разметка `outcome`
  не разделяет явно — технический успех и успех намерения здесь разошлись, и это стоит отдельно
  проговаривать на лекции при разборе дипфейк-кейсов: «сработало» и «добилось цели» — не одно и
  то же.
- **Ранние (2018) кейсы предвзятости — U3 без единого инцидента-жертвы, через агрегированный
  тест.** В отличие от большинства `U3`-кейсов (конкретный пострадавший — Williams, Parks, Reid),
  ACLU×Rekognition и Gender Shades — это **намеренные контролируемые тесты**, а не случайные
  инциденты: `axis4_gate=not-applicable`, потому что ставки теста нулевые (никого не арестовали
  по результатам), но именно эти два теста 2018 года задали доказательную базу для всех
  последующих городских запретов (Сан-Франциско 2019, Портленд 2020) и судебных урегулирований
  (Facebook/Google/TikTok BIPA) в этом же файле — причинно-следственная цепь «академический тест
  → муниципальный запрет → судебное урегулирование» прослеживается по датам (2018 → 2019–2020 →
  2020–2022) внутри одной этой таблицы.
- **Самый дешёвый с точки зрения вычислений и самый дорогой с точки зрения доказанности провал —
  Шанхай.** Обход liveness-проверки стоил мошенникам смартфона за 1650 юаней и готового
  face-swap-приложения, но принёс ¥500 млн фиктивных счетов за три года, прежде чем был
  обнаружен — `axis2_bucket=season-years`, `F-A`: обратная связь была крайне медленной
  (институциональный аудит, а не немедленный технический алерт), что подтверждает вывод волны 1
  про «потолок попытки ≠ потолок успеха» уже не для детекции дипфейков, а для систем
  anti-spoofing/liveness, которые именно для такого сценария проектировались и всё равно не
  сработали три года подряд.
