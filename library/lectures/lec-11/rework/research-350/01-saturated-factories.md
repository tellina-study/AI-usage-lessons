# Исследование: заводы, насыщенные автоматизацией и ИИ (issue #350)

Собрано для Лекции 11 (ИИ в производстве). Формат по объекту: таблица «показатель | год | значение | база/знаменатель | источник | self-report/независимый». Числа без URL первоисточника не включались. Где агенты-исследователи сами не смогли прочитать первоисточник напрямую (403/платный доступ) — это помечено explicitly как «не проверено прямым чтением», а не выдано за подтверждённый факт.

---

## 1. Siemens Electronics Works Amberg (EWA), Германия

### Дефекты на миллион (DPM)

| показатель | год | значение | база | источник | тип |
|---|---|---|---|---|---|
| DPM на старте | 1989 | «~500 dpm» | — | не нашёл первичного документа Siemens с этой цифрой; встречается только в пересказах | **неподтверждено** |
| Качество | 2015 | 99,9988% (≈12 dpm) | — | [factsheet-amberg-en.pdf](https://assets.new.siemens.com/siemens/assets/api/uuid:6b67972d-4992-4cd0-b202-8a698fae046a/factsheet-amberg-en.pdf) (press release 23.02.2015) | self-report |
| DPM, интервью Büttner | ~2018-2019 | 12 dpm, сравнение «типичный человеческий показатель ~500 dpm» (общий бенчмарк, не «1989 vs сейчас») | — | [us-tech.com интервью Prof. Dr. Büttner](https://www.us-tech.com/RelId/1334566/pagenum/26/ISvars/default/Prof_Dr_Buttner_Showcases_Siemens_Digital_Factory.htm) | self-report (интервью) |
| Качество | н/д | 99,99885% (≈11,5 dpm), 12 млн SIMATIC PLC/год | — | [automationworld.com](https://www.automationworld.com/products/control/blog/13315384/siemens-positions-itself-as-an-industry-40-example) | self-report/пересказ прессы |
| Качество | н/д (без года) | **99,9999%** (≈1 dpm) — цитата Dr. Gunter Beitinger, SVP Manufacturing | — | [capgemini.com интервью](https://www.capgemini.com/insights/research-library/discussion-with-siemens/) | self-report |

**Противоречие:** 12 dpm (2015, первичный документ) vs 1 dpm (цитата без даты) — разница в 10×. «500 dpm в 1989» нигде не подтверждено первичным источником — вероятно смешение исторической базы с общим бенчмарком «человеческая ошибка ~500 dpm».

### Рост объёма производства при почти неизменном штате

| показатель | год публикации | значение | базовый год/штат | источник | тип |
|---|---|---|---|---|---|
| Множитель роста выпуска | ~2016-2017 | **9×** | с 1989, штат 1300 | [industryweek.com](https://www.industryweek.com/technology-and-iiot/automation/article/22019249/embattled-german-industrials-pursue-the-factory-of-the-future) | независимый |
| Множитель роста выпуска | 23.02.2015 | **8×** | штат ~1200 | [factsheet-amberg-en.pdf](https://assets.new.siemens.com/siemens/assets/api/uuid:6b67972d-4992-4cd0-b202-8a698fae046a/factsheet-amberg-en.pdf) | self-report |
| Множитель роста выпуска | н/д | **13×** | с 1990 | [navvis.com case study](https://www.navvis.com/resources/case-studies/siemens) | self-report/вендор-кейс |
| Множитель роста выпуска | н/д | **13×** | с 1991(!), штат 1250 | [industrie40award.com](https://www.industrie40award.com/the-winners/siemens-ag-elektronikwerk-amberg/) | независимый (премия) |
| Множитель роста выпуска | 2024 (по сниппету) | **14×** | с 1990 | controleng.com — **fetch не удался (403), не проверено напрямую** | не проверено |

**Противоречия (важны для лекции — пример «две меры разошлись»):**
- Год основания плавает: **1989** (большинство, включая Siemens) vs **1991** (Industrie 4.0 Award).
- Множитель НЕ монотонно растёт по времени публикации: 9× (2016) → 8× (2015, раньше, но меньше) → 13× → 14× — Siemens сам в разные годы называл разные базовые точки без пересчёта методики.
- Штат плавает: 1150-1200 / 1250 / 1300 — всё в пределах заявленного диапазона ~1150-1400, но не одно число.

### Доля автоматизации ~75%

Подтверждено несколькими self-report источниками, устойчиво повторяется:
- «Machines and computers handle 75 percent of the value chain on their own; a quarter of the work is done by people» — [factsheet-amberg-en.pdf](https://assets.new.siemens.com/siemens/assets/api/uuid:6b67972d-4992-4cd0-b202-8a698fae046a/factsheet-amberg-en.pdf), self-report.
- Dr. Gunter Beitinger: «75% of the value chain handled independently by machines and robots» — [capgemini.com](https://www.capgemini.com/insights/research-library/discussion-with-siemens/), self-report.
- Подтверждается независимо: [smartindustry.com](https://www.smartindustry.com/benefits-of-transformation/advanced-control/article/11290138/a-factory-of-the-futurein-amberg).

**Почему не 100% — прямой цитаты про экономику предельной ступени (diminishing returns) НЕ НАЙДЕНО.** Büttner формулирует автоматизацию как «систему поддержки персонала», не как экономический предел — это описание мотивации, не объяснение «почему именно 75%». Для лекции: если нужен тезис про diminishing returns на этом кейсе — это будет интерпретация лектора, не задокументированный факт Siemens.

### ИИ vs классическая автоматика — подтверждённый ML-кейс

- **Рентген-контроль плат**: Schmitt, Bönig, Borggräfe, Beitinger, «Predictive model-based quality inspection using Machine Learning and Edge Cloud Computing», *Advanced Engineering Informatics*, 2020. [ResearchGate](https://www.researchgate.net/publication/341530592_Predictive_model-based_quality_inspection_using_Machine_Learning_and_Edge_Cloud_Computing). Авторы — инженеры Siemens, peer-reviewed журнал → гибридный источник.
  - Метод: supervised ML (бинарная классификация) на уровне solder joint, обучена на исторических данных SPI + параметрах процесса; модель предсказывает, нужен ли рентген-контроль конкретной зоны.
  - Результат: **29% среднее снижение объёма рентген-инспекций** без потери точности обнаружения дефектов.
  - **Это настоящая обученная модель** (вероятностное предсказание, переобучается на новых данных) — не ПЛК-правило.
- **Предиктивное обслуживание шпинделя**: упоминается связка edge computing + AI (скорость вращения + ток привода коррелируют с простоями) — вероятный источник [blog.siemens.com, Dominik Bittner](https://blog.siemens.com/2019/11/beyond-the-hype-a-practical-use-case-on-the-edge/), но полный текст не извлечён. **Статус: не подтверждено прямым URL с текстом.**
- Академический разбор культурного конфликта AI/lean: van Giffen et al., «The Culture Clash of AI Adoption in Lean Quality Management… Amberg», *Information Systems Journal*, 2025/2026, DOI 10.1111/isj.70006, [Wiley](https://onlinelibrary.wiley.com/doi/10.1111/isj.70006) — abstract открыт, полный текст платный. Соавтор из Siemens → гибридный источник.

**Явно НЕ использовать без доп. проверки** (похожи на AI-generated SEO-контент с правдоподобными, но неподтверждёнными числами): `agentvictoria.ai` («12-36 часов предсказания отказа», «up to 30% fewer X-ray tests», «6000 operator hours freed»), `millennial.ae` («−60% defect rate», «−20% energy»), `bright-amber.com` («€200k/год экономии на PCB-резке»), фраза про «4500 сотрудников... AI process stewardship, digital twin validation, autonomous fleet coordination» (похоже на AI-сгенерированный текст).

### Инвестиции

| сумма | год | цель | источник | тип |
|---|---|---|---|---|
| **>€200 млн** | 2025/2026 анонс | новая «фабрика будущего» в Амберге, к 2030 | [press.siemens.com](https://press.siemens.com/global/en/pressrelease/siemens-invest-over-eu200-million-build-factory-future-amberg-germany) | self-report |

Распространённую цифру «€150 млн, 2017» — **не нашёл подтверждения**, не использовать без проверки.

### Что делают оставшиеся ~1200-1400 человек

Self-report (2015): «человеческие руки касаются платы только в начале процесса — укладка непропаянной платы» ([factsheet](https://assets.new.siemens.com/siemens/assets/api/uuid:6b67972d-4992-4cd0-b202-8a698fae046a/factsheet-amberg-en.pdf)). Остальные роли (программирование линий/ПЛК, обслуживание роботов, SPC-контроль качества, логистика) — только агрегированный поисковый синтез без единого первичного документа на каждую роль; не числовые, не строго цитируемые.

### WEF Lighthouse-статус

Amberg — один из первых заводов Siemens в WEF Global Lighthouse Network (2021), позже получил статус «Sustainability Lighthouse». Заявление «+140% факторного выпуска при двукратной сложности продукта без роста энергопотребления» подтверждено в [WEF_GLN_2021_Reimagining_Operations_for_Growth.pdf](https://www3.weforum.org/docs/WEF_GLN_2021_Reimagining_Operations_for_Growth.pdf), стр.31 (см. раздел 6). Это полу-независимая верификация — WEF/McKinsey профили строятся на данных, предоставленных компанией.

---

## 2. FANUC, Oshino (Яманаси, Япония) — lights-out производство

### С какого года и сколько длится безлюдный режим

| показатель | год | значение | база | источник | тип |
|---|---|---|---|---|---|
| Начало lights-out режима | **2001** | запуск полностью безлюдного ночного режима | — | [Wikipedia: Lights out (manufacturing)](https://en.wikipedia.org/wiki/Lights_out_(manufacturing)), цитирует CNN Money (Null & Caulfield), 01.06.2003; оригинал money.cnn.com недоступен для fetch (503) | Пресса (независимый), не прочитано напрямую |
| Цитата FANUC | 2003 (опубл.) | «Not only is it lights-out, we turn off the air conditioning and heat too» — Gary Zywiol, VP FANUC | — | та же статья | self-report через прессу |
| Более ранний прообраз (другой завод/эпоха) | **январь 1981** | робот-завод, 16 ч/сутки (не 24/7), штат 100 чел. на ~100 роботов/мес, «в 5× меньше» штата обычного завода | 500 чел. на обычном заводе того же объёма | [CSMonitor, 15.04.1981](https://www.csmonitor.com/1981/0415/041542.html) (fetch 403, восстановлено через поиск); подтверждается [Fortune/CNN 1987](https://money.cnn.com/magazines/fortune/fortune_archive/1987/05/25/69060/index.htm) | Пресса, не прочитано напрямую |
| Длительность автономной работы | 2001 (репортаж 2003) | **до 30 дней подряд** без людей | — | CNN Money 2003 via [Wikipedia](https://en.wikipedia.org/wiki/Lights_out_(manufacturing)), [standardbots.com](https://standardbots.com/articles/lights-out-manufacturing) | Пресса |
| Та же цифра в часах | лето 2002 | «720 часов» непрерывной работы (=30 дней) | отдельный полностью автоматизированный завод в Ошино | [encyclopedia.com](https://www.encyclopedia.com/social-sciences-and-law/economics-business-and-labor/businesses-and-occupations/fanuc-ltd) (403, через сводку) | вторичный пересказ |

**Не нашёл:** статистику по числу цехов именно lights-out («более 20 дней/заводов» из брифа) — такой цифры нигде не встретилось, вероятно искажение/смешение с «30 дней».

### Производительность

| показатель | год | значение | база | источник | тип |
|---|---|---|---|---|---|
| Темп сборки роботов роботами | 2001-2003 | **~50 роботов/24ч смену** | — | CNN Money 2003 via Wikipedia, [andrewtobias.com](https://andrewtobias.com/building-robots-in-the-dark/) | Пресса |
| Темп на заводе 1981 г. | 1981 | ~100 роботов/мес, штат 100 чел. | ≈1 робот/мес на человека vs ≈0.2 на обычном заводе | CSMonitor 1981 | Пресса |
| Мощность цеха роботов (self-report) | текущее (~2023-2025) | ROBOT Factory: **6000 роботов/мес** | один из цехов кампуса 1,78 млн м² | [fanuc.eu/fanuc-factories](https://www.fanuc.eu/eu-en/fanuc-factories) | self-report |
| Другие цеха того же кампуса | текущее | CNC/контроллеры — 25 000/мес; сервомоторы — 150 000/мес; сервоусилители — 84 000/мес; ROBOSHOT — до 600/мес; ROBOCUT — до 150/мес | — | [fanuc.eu/fanuc-factories](https://www.fanuc.eu/eu-en/fanuc-factories) | self-report |
| Общая мощность японских заводов FANUC | 2021 | факт ~8000 робот/мес, мощность до 11 000/мес | все японские заводы, не только Ошино | найдено через поиск, URL не зафиксирован отдельно | **слабо подтверждено** |
| Юбилей | 2021 (pesmedia) / 2023 (fanucamerica, заголовок) | 750-тысячный промышленный робот FANUC | кумулятивно с 1970-х | [pesmedia.com](https://www.pesmedia.com/fanuc-robot-manufacturing-05072021); [fanucamerica.com](https://www.fanucamerica.com/news-resources/fanuc-america-press-releases/2023/12/11/global-automation-leader-fanuc-announces-production-of-750-000th-robot) | self-report, **дата между двумя источниками противоречит** |

### Штат

| показатель | год | значение | источник | тип |
|---|---|---|---|---|
| Штат автоматизированного завода | 1981 | 100 чел. вместо ~500 | CSMonitor 1981 | Пресса |
| Штат завода «720 часов» | 2002 (вторичный пересказ) | 100 чел. вместо ~500 — та же формулировка, что 1981 г. (подозрение на дублирование) | encyclopedia.com | вторичный пересказ, не первоисточник |
| Персонал FANUC Corp. | на 31.03.2024 | 4689 чел. (вся компания) | финдокументы FANUC | self-report, не именно Ошино |
| Персонал FANUC Group | на 31.03.2024 | 9970 чел. (группа) | финдокументы FANUC | self-report, не именно Ошино |
| Разбивка день/ночь смена для Ошино | — | **не нашёл** | — | — |

### ИИ vs классическая автоматика — строгое разделение

- **Lights-out сборка (50 роботов/смену, 30 дней)** — классическая автоматика: ЧПУ-станки, промышленные роботы по жёстким программам, автоматический склад. Независимый разбор [andrewtobias.com](https://andrewtobias.com/building-robots-in-the-dark/) прямо отмечает: «source material does not mention AI, deep learning, or machine learning».
- **FANUC AI Bin Picking** — реальный ИИ: deep reinforcement learning, робот учится брать детали из бункера (~8ч обучения → >90% точность). Партнёрство с Preferred Networks начато 2015, демо на International Robot Exhibition Tokyo (дек. 2015), коммерческий релиз «AI Bin Picking FIELD» (апрель 2018). [MIT Technology Review](https://www.technologyreview.com/2016/03/18/161519/this-factory-robot-learns-a-new-job-overnight/); [Preferred Networks pr](https://www.preferred.jp/en/news/pr20180417). **Нет подтверждения, что это стоит именно на заводе в Ошино** — демо проходило в офисе в Токио.
- **Вывод: миф «роботы FANUC в Ошино делают роботов с помощью ИИ» некорректен** — lights-out история (2001-2003) = классическая автоматика без ML; реальный deep learning продукт (2015-2018) — отдельный проект, не привязанный источниками к Ошино.

### Инвестиции

| сумма | год | цель | источник | тип |
|---|---|---|---|---|
| ¥12 млрд | завершено к сент. 2019, работа с 2020 | новый цех обработки деталей сервомоторов в Ошино, 55 200 м² | seisanzai-japan.com (через поиск) — требует прямой проверки URL | self-report |
| ¥18,6 млрд | FY2021 | капвложения FANUC | FANUC Annual Report 2021 | self-report |
| ¥40,136 млрд | FY2022 | капвложения FANUC, включая ZEB-здание Central Technical Center | FANUC convocation documents | self-report |
| $7,3 млн | 2015 | инвестиция в Preferred Networks (инфраструктура для AI Bin Picking) | через поиск, не найден отдельный пресс-релиз-URL | требует проверки |

### Противоречия (важные для лекции)

1. **Конфляция 1981 и 2001/2002**: цифра «500→100 работников» впервые — из репортажей 1981 г. про завод в Яманаси. Та же цифра всплывает у encyclopedia.com применительно к «2002 году» с добавлением «720 часов». Первоисточник CNN 2003 (который ввёл «50/смену, 30 дней») этой цифры НЕ содержит — разные метрики из разных десятилетий сливаются вторичными обзорами в один абзац. **Не писать «500→100» и «50/смену» в одном предложении как одно измерение.**
2. «Oshino» vs «Yamanashi/Fuji plant» (статьи 1981-87) — нет явного подтверждения, что это буквально то же здание, а не более поздняя пристройка того же кампуса.
3. Дата юбилея 750-тысячного робота: июль 2021 (pesmedia) vs декабрь 2023 (fanucamerica заголовок) — не развёдено, два разных юбилея или дублирование.
4. Первоисточник CNN Money 2003 не прочитан напрямую (503/archive.org недоступен инструментам) — все цифры восстановлены через цитирование в Wikipedia/блогах. **Самое слабое место — рекомендуется независимая проверка до публикации в главе.**
5. Нет данных, что режим «30 дней без людей» действует и сегодня (2020-е) — современные self-report страницы FANUC говорят обобщённо, без конкретной цифры дней.
6. **Независимый контрапункт**: Assembly Magazine (независимый) прямо пишет, что **72% операций производства по-прежнему выполняют люди**, и сам FANUC (VP Chris Blanchette, Joe Gazzarato) признаёт: lights-out «не практично для каждого применения» из-за короткого жизненного цикла продукта и mass customization, экономически сложно оправдать для high-mix производства. [assemblymag.com/articles/94982](https://www.assemblymag.com/articles/94982-lights-out-automation-fact-or-fiction). Это прямо противоречит образу «норма, а не нишевая демонстрация».
7. Фраза «более 20 заводов/дней» из брифа — не подтверждена ни одним источником.

---

## 3. Xiaomi, Чанпин (Пекин) — «dark factory» смартфонов

### Важно: минимум 3-4 разных завода Xiaomi путают под одной фразой

1. **Чанпин, смартфоны, 2021-2024** — объект запроса, ниже.
2. **Циюйчжуан (亦庄), Xiaomi Auto, электромобили** — «машина каждые 76 секунд», ~2000-2200 чел. **Другой завод, другой продукт.**
3. **Завод бытовой техники (кондиционеры), запуск ~окт. 2025** — свои цифры: 100% автоматизация цехов литья/металла, 161 AMR, 94% «умной логистики», 6,5 сек/кондиционер.
4. **Более ранний «黑灯工厂» (2020)** — ~1 млн телефонов/год, по словам Лэй Цзюня — «сверхбольшая экспериментальная лаборатория для проверки технологий», НЕ production-сайт. Критиковался в фьюде с Gree/Дун Минчжу как «PR без производственной значимости».

Это сам по себе материал для лекции: один бренд, одна фраза «dark factory» — 3-4 разных объекта с разными числами, которые статьи сливают в одно.

### Таблица — Чанпин (смартфоны)

| показатель | год | значение | база | источник | тип |
|---|---|---|---|---|---|
| Начало стройки Phase 2 | 2021 (14.07.2021) | объявлено Лэй Цзюнем | — | [beijing.gov.cn](https://www.beijing.gov.cn/ywdt/gqrd/202303/t20230307_2930560.html), [gamersky.com](https://www.gamersky.com/tech/202107/1406118.shtml) | гос. источник + пресса |
| Инвестиции в здание Smart Factory | анонс 2021, запуск 2024 | **2,4 млрд юаней (~$330 млн)**, 81 000 м² | — | [propakistani.pk](https://propakistani.pk/2024/07/09/xiaomis-smart-factory-can-run-24-7-without-people/), IR-документ Xiaomi | self-report |
| Инвестиции во ВЕСЬ Phase 2 комплекс | 2021-2023 | **12,1 млрд юаней**, 141 100 м² (здание + R&D-центр + индустриальный парк) | в ~5× больше «2,4 млрд» — другая база счёта | [baike.baidu.com](https://baike.baidu.com/item/%E5%B0%8F%E7%B1%B3%E6%99%BA%E8%83%BD%E5%B7%A5%E5%8E%82%E4%BA%8C%E6%9C%9F/60020996) | китайская пресса/справочник |
| Дата запуска производства | расходится: февр. 2024 vs июль 2024 | «тихий запуск» (投产) в феврале vs публичный анонс Лэй Цзюня в июле | — | [news.qq.com (февр.)](https://news.qq.com/rain/a/20240219A092OL00) vs [news.qq.com (июль)](https://news.qq.com/rain/a/20240709A04FJ900) | self-report/пресса |
| Заявленная мощность | 2024 | **10 млн флагманских смартфонов/год** | 81 000 м², 11 линий | [trendforce.com](https://www.trendforce.com/news/2024/07/09/news-featuring-mix-fold-4-xiaomis-smart-factory-opens-with-10-million-annual-flagship-smartphone-capacity/) | self-report |
| Заголовочный темп «1 тел/сек» | 2024 | растиражировано как «1 телефон в секунду» / «60 тел/мин» | — | [bgr.com](https://www.bgr.com/2087200/xiaomi-dark-robot-smart-phone-factory/), [itc.ua](https://itc.ua/en/news/xiaomi-s-new-smart-factory-will-operate-24-7-without-people-and-produce-60-smartphones-per-minute/) | маркетинг, подхвачено без проверки |
| **Честный пересчёт того же темпа** | 2024 | при 10 млн/год это **1 тел. каждые ~3,15 сек**, не 1 сек | 10 млн/год как база | [slashgear.com](https://www.slashgear.com/2144548/xiaomi-smartphone-robot-dark-factory-how-works-makes-phones-fast/) — явно пересчитал | редкий случай арифметической проверки |
| Фактический наблюдаемый темп на месте | 2026 (апрель) | ~600 тел/час (1 шт/~6 сек) | при мощности 10 млн/год это **≈52% от заявленной мощности** (600×24×365≈5,26 млн vs 10 млн) | [euronews.com](https://www.euronews.com/2026/04/24/inside-xiaomis-beijing-factory-the-machine-behind-a-smartphone-made-every-6-seconds) | репортаж на месте — **нэймплейт ≠ реальная загрузка** |
| Степень автоматизации линии | 2024-2026, устойчиво | **81%** | вся производственная линия | euronews.com (выше), [notebookcheck.net](https://www.notebookcheck.net/Factory-visit-at-Xiaomi-A-look-at-the-highly-automated-smartphone-production-in-Beijing.1231066.0.html) | self-report, независимо процитировано на 2 визитах |
| Автоматизация «ключевых процессов» | 2024 | 100% заявлено | — | propakistani.pk, IR Xiaomi | self-report, доля «ключевых» от «всех» не проверена |
| Доля самостоятельно разработанного оборудования/ПО | 2024 | 96,85% оборудования, 100% ПО | — | [vnexpress.net](https://e.vnexpress.net/photo/enterprises/inside-xiaomis-near-fully-automated-factory-that-assembles-a-smartphone-in-6-seconds-5003325.html) | self-report |
| **Штат линии** | 2024-2026 | **~220 чел. на линии 310 м** — инспекция, реагирование на сбои, работа там, где точность незаменима (чистка объективов камер под микроскопом) | Xiaomi сравнивает: «обычная линия 600 м / 300 устройств/ч / ~450 чел.» | notebookcheck.net, euronews.com | смешанный: факт «220, не 0» подтверждён визитом журналиста; база «обычная линия=450» — цифра самой Xiaomi, не проверена независимо |
| Этапы производства | 2024-2026 | >200 операций сборки, 49 собственных тест-станций, 3-этапное тестирование | — | notebookcheck.net | репортаж на месте |
| AI/ML-функции (платформа HyperIMP) | 2024 | заявлены: машинное зрение для дефектов, «цифровой двойник» каждой машины, predictive maintenance по порогу износа | — | [newatlas.com](https://newatlas.com/robotics/xiaomi-dark-robotic-factory), [interestingengineering.com](https://interestingengineering.com/innovation/xiaomi-human-less-self-improving-robot-factory-to-make-10-mn-phones-yearly) | **чистый self-report/пресс-ретеллинг** — независимой технической проверки точности моделей не нашёл |

### Противоречия / разоблачения

1. **«1 тел/сек» арифметически неверно** при собственной заявленной мощности: 10 млн/год ÷ (365×24×3600) ≈ 1 раз в 3,15 сек, не в 1 сек. Только slashgear.com явно пересчитал; остальные повторили заголовок без проверки.
2. **Нэймплейт-мощность ≠ реальная загрузка**: заявлено 10 млн/год, независимый репортаж (апр. 2026) фиксирует фактический темп ~600 шт/час — около половины заявленной мощности.
3. **«Полностью безлюдный» vs 220 человек на линии** — заголовки («no workers») прямо противоречат и собственному признанию Xiaomi, и репортажу Notebookcheck («люди вмешиваются там, где точность незаменима»). Реальность — «largely lights-out», не «fully lights-out».
4. **База «обычная линия=450 человек»** — цифра самой Xiaomi, предъявленная как self-serving контраст к своим 220; независимого стороннего бенчмарка не нашёл.
5. **2,4 млрд vs 12,1 млрд юаней** — разные базы счёта (одно здание vs весь комплекс Phase 2), статьи почти всегда цитируют только первую цифру без оговорки.
6. Дата запуска плывёт между «тихим вводом в строй» (февр. 2024) и публичным PR-анонсом (июль 2024).
7. **Фотосъёмка внутри завода запрещена** даже допущенным журналистам (Notebookcheck явно пишет об этом) — даже «репортаж с места» во многом опирается на материалы, отобранные самой Xiaomi.
8. Цифры других заводов Xiaomi (авто: 76 сек/авто, ~2000 чел.; бытовая техника: 6,5 сек/кондиционер, 161 AMR) регулярно просачиваются в статьи про Чанпин, создавая ложные комбинации.
9. Более ранний «黑灯工厂» (2020) критиковался в китайской прессе как PR-витрина без реальной производственной значимости — контраст к нынешней волне восторга 2024 года.

**Не нашёл:** прямого покрытия от SCMP/The Verge/Nikkei Asia именно про завод в Чанпине; независимого технического аудита точности ML-моделей машинного зрения; видео-тура блогеров именно по смартфонному заводу (съёмка запрещена).

---

## 4. Philips Drachten (Нидерланды) — сборка бритв, adaptive robotics

| показатель | год | значение | база | источник | тип |
|---|---|---|---|---|---|
| Роботов на линии | 2012 | 128 роботизированных рук (Adept Technology) | — | [NYT, Markoff, 18.08.2012](http://www.nytimes.com/2012/08/19/business/new-wave-of-adept-robots-coming-to-factory-floors.html) (платный доступ; [PDF-зеркало](http://www.as.utexas.edu/astronomy/education/spring13/wheeler/secure/Robots_NYT.pdf)) | независимый (репортаж NYT с места) |
| Персонал на смену | 2012 | «several dozen workers per shift» (несколько десятков чел.) — **≈1/10** от штата смены на заводе в Чжухае (КНР) | база — штат смены Zhuhai | тот же NYT | независимый |
| Расширенная конфигурация роботов | ~2016-2017 | >120 роботов: Adept Viper (6-осевые) + Adept Cobra (SCARA); 9 линий × 5-8 ячеек; 40 систем AnyFeeder | — | [Assembly Magazine](https://www.assemblymag.com/articles/90173-automation-profiles--robots-help-philips-shave-assembly-costs-), [Assembly Magazine 2017](https://www.assemblymag.com/articles/93686-philips-future-proof-assembly-concept-for-high-end-shavers) | независимый отраслевой |
| Vision-guided роботы | 2012-2017 | ~50 роботов получили vision guidance (AdeptSight) на новых линиях | — | Assembly Magazine (выше) | независимый |
| Число роботов (self-report) | 2022 | «не менее 300 роботов» + AGV для межцеховой перевозки | — | [philips.nl, 16.09.2022](https://www.philips.nl/a-w/about/news/archive/standard/about/news/articles/2022/20220916-werken-bij-philips-drachten-een-van-de-slimste-fabrieken-van-europa.html) | self-report |
| Точность сборки | 2022 | 70 микрометров для компонентов бритвы | — | philips.nl (выше) | self-report |
| Объём данных на единицу | 2000 vs 2022 | в 2000 — 4 КБ/головку бритвы; сейчас — ≥500× больше | база — 2000 год | philips.nl (выше) | self-report |
| Год основания завода | 1950 | Royal Philips Electronics открыла завод | — | NYT (выше) | независимый |
| Инвестиции именно в роботизацию Drachten | — | **не нашёл** | — | — | — |

**Технология — классика vs ИИ.** Роботы Adept Viper/Cobra с AdeptSight — машинное зрение по камерам для позиционирования/захвата деталей (классическое servo+vision управление, не обученная нейросеть). NYT прямо: «Video cameras guide them». 2022 self-report Philips упоминает «алгоритмы» для предиктивного обслуживания на основе накопленных данных — ближе к реальной аналитике/ML, но без конкретики (нет названия модели, метода обучения, метрик). **Нельзя подтвердить до уровня «точно обученная модель».**

**Роли людей:** инженер управляет линией; присмотр за роботами (роботы в стеклянных клетках — по соображениям безопасности), квалифицированное обслуживание и репрограммирование.

**Противоречия:**
1. **«9 рабочих на контроль качества»** (встречается во вторичных источниках типа standardbots.com) — **не подтверждено первоисточником**. NYT говорит «several dozen workers per shift», а не 9. Похоже на искажённую компиляцию.
2. **Нет подтверждения полного переноса производства из Китая в Drachten** — по Wikipedia (Philishave), Drachten и Zhuhai оставались параллельными площадками (премиум — Drachten, остальное — Zhuhai), не было полного переноса. Bloomberg-оригинал (19.01.2012) заблокирован (403), не проверено напрямую.
3. Цифра «€50 млн инвестиций Philips в AI/robotics/imaging в Нидерландах» относится к **медицинским технологиям**, НЕ к заводу Drachten/бритвам — явно предупреждаю, не путать.

---

## 5. Hyundai Metaplant America (HMGMA), Джорджия, США

| показатель | год | значение | база | источник | тип |
|---|---|---|---|---|---|
| Инвестиции в сборочный завод | 2024-2025 | **$7,59 млрд** (иногда $7,6 млрд) | — | [Newsweek](https://www.newsweek.com/hyundai-metaplant-america-georgia-factory-2050288), [Hyundai Motor Group pr](https://www.hyundaimotorgroup.com/en/news/hyundai-motor-group-metaplant-america-celebrates-grand-opening-powering-us-economic-growth) | self-report + независимые совпадают |
| Общие инвестиции в Джорджию | — | **$12,6 млрд** (завод $7,59 млрд + батарейный JV $4,3 млрд с LG Energy Solution + доп.) | — | Newsweek, Wikipedia | смешанный |
| Батарейный завод (JV с LG) | — | $4,3 млрд, 30 ГВт·ч | обеспечивает ≈360 000 авто/год при 84 кВт·ч/пак | [Wikipedia: HMGMA](https://en.wikipedia.org/wiki/Hyundai_Motor_Group_Metaplant_America) | независимый |
| Доп. инвестиции в США (широкий план) | 2025 | $21 млрд к 2028, из них $6 млрд на инновации/робо-партнёрства (вкл. Boston Dynamics) | — | [Drives&Controls](https://drivesncontrols.com/hyundai-plans-to-buy-tens-of-thousands-of-robots-in-21bn-us-plan/), [Robotics 24/7](https://www.robotics247.com/article/hyundai-to-deploy-boston-dynamics-humanoids-quadrupeds/) | независимый, со ссылкой на self-report анонс |
| Производственная мощность (цель) | план | до 500 000 EV/HEV/год (иногда 580 000 как «future target») | — | [CleanTechnica](https://cleantechnica.com/2025/03/27/hyundai-kia-genesis-plant-that-can-produce-500000-electric-hybrid-vehicles-opens-in-georgia/), IEEE Spectrum | смешанный |
| Начальная мощность (факт) | 2024 | 300 000 авто/год изначально | из плана 500 000 = 60% | CleanTechnica | независимый |
| Штат — план | план | 8500 рабочих мест (завод+батарея+поставщики) к 2030/2031 (дата финиша расходится) | — | [Statesboro Herald](https://www.statesboroherald.com/local/as-metaplant-rises-in-ellabell-regional-officials-expect-a-5-to-7-year-hire-up-to-the-hyundai-motor-groups-8500-jobs-and-suppliers-nearly-6000/) | независимый (местное СМИ) |
| Штат — факт | окт. 2024 | ~1400 чел. | из плана 8500 = ~16% | Wikipedia | независимый |
| Штат — факт | окт. 2025 | 3200+ чел. | из плана 8500 = ~38% | [Yahoo Finance/Hyundai update](https://finance.yahoo.com/news/hyundai-motor-group-metaplant-america-090314317.html) | смешанный |
| Средняя зарплата | — | $58 100/год, на 35% выше среднего по округу Bryan County | база — средняя по округу | IEEE Spectrum | независимый |
| Первый выпуск авто | 03.10.2024 | первый Ioniq 5 с конвейера | — | Wikipedia, Hyundai press | self-report + независимый совпадают |
| Старт Ioniq 9 | март 2025 | — | — | CleanTechnica | смешанный |
| Boston Dynamics Spot | 2024-2025 | **подтверждено официально**: используется для внешнего контроля качества в weld shop | — | [Boston Dynamics pr, 03.04.2025](https://bostondynamics.com/news/boston-dynamics-hyundai-motor-group-expand-collaboration-drive-mobility-manufacturing-innovation/) | self-report (сам Boston Dynamics) — надёжно |
| Число Spot на заводе | — | по одному источнику «2 робота» | — | [Automotive Manufacturing Solutions](https://www.automotivemanufacturingsolutions.com/smart-factory/hyundai-reshapes-vehicle-production-at-metaplant-america/2677700) | не перепроверено другим источником |
| Atlas (гуманоид) | план 2026-2030 | **НЕ развёрнут в производстве**: пилот с 2026, parts sequencing план на 2028, сборка — план на 2030 | — | Boston Dynamics pr, [tech.yahoo.com](https://tech.yahoo.com/ai/meta-ai/articles/hyundai-motor-group-plans-deploy-210317930.html) | self-report анонс — независимые СМИ пересказывают, не подтверждают реальное внедрение |
| Сварочные роботы (6-осевые) | — | 500 или 600 (расхождение между источниками) | — | Automotive Manufacturing Solutions | противоречиво |
| AGV/AMR | — | расхождение: 161 / 300 / «более 500» | — | Automotive Manufacturing Solutions, Assembly Magazine | взаимно противоречащие пересказы |
| Общее число роботов | — | «1000+» или «850» в разных пересказах | — | разные пересказы той же статьи | внутренне противоречиво |
| AGV-поставщик | — | Hyundai Wia (AMR до 1,5 т; парковочные роботы до 3,4 т) | — | Automotive Manufacturing Solutions | независимый отраслевой |
| Computer vision для QC кузова | — | заявлено: детекция дефектов панелей (отверстия, трещины), vision-based one-kit sequencing, AI-камеры flush-alignment на дверных станциях | — | Automotive Manufacturing Solutions, Assembly Magazine | self-report, пересказанный прессой — независимого техн. подтверждения архитектуры нет |
| Водородные грузовики логистики | — | 21 машина Hyundai Xcient | — | IEEE Spectrum | независимый |
| Рейд ICE | сент. 2025 | ~450-475 задержанных; Hyundai заявила, что ни один не её сотрудник (субподрядчики LG) | — | [CNN](https://www.cnn.com/2025/09/11/business/hyundai-raid-plant-delay-ceo), [Wikipedia](https://en.wikipedia.org/wiki/2025_Georgia_Hyundai_plant_immigration_raid) | независимый |
| Задержка батарейного завода из-за рейда | 2025 | минимум 2-3 месяца (слова CEO Жозе Муньоса) | — | CNN, InsideEVs, Axios | смешанный, перепроверено несколькими СМИ |

**ИИ vs классика:** 500-600 сварочных роботов и AGV/AMR по заданным маршрутам — классическая автопром-робототехника (навигация lidar+QR, не обучение на лету). Заявленный реальный ИИ — vision-детекция дефектов панелей (вероятно CNN-based computer vision) и Atlas-партнёрство (реальная ИИ-платформа, упоминается сотрудничество с Google DeepMind для управления) — но **Atlas на линии пока не работает**, только анонс/пилот 2026+.

**Противоречия:**
1. Число роботов/AGV расходится в 2-3× между пересказами одной статьи — рекомендация: прочитать первоисточник вручную перед использованием точного числа в лекции.
2. $7,59-7,6 млрд (только завод) vs $12,6 млрд (завод+батарея+доп.) — не противоречие, а разный охват; нужно явно указывать при цитировании.
3. Штат: план 8500 к 2030 vs 2031 (целевой год расходится); факт на окт. 2025 (3200+) подтверждён и совпадает между источниками.
4. Spot подтверждён официальным пресс-релизом Boston Dynamics (надёжно); Atlas — только анонс, независимого подтверждения реальной работы на линии нет. **Хороший пример «анонс ≠ внедрение».**
5. Мощность: заявлено «до 500 000/год», факт 2024 — 300 000 (60% от цели) — это начальная, не текущая мощность.
6. Рейд ICE: self-report-дистанцировка Hyundai («не наши сотрудники») не отменяет реальной задержки производства на 2-3 месяца, подтверждённой независимо.

---

## 6. WEF Global Lighthouse Network

### Кривая роста числа «маяков» — два ряда чисел, которые НЕ совпадают

**А. «Живые» цифры — что WEF объявлял в момент каждого анонса:**

| дата анонса | накопительно | новых | источник | тип |
|---|---|---|---|---|
| Давос, янв. 2018 | **16** (запуск) | — | [WEF_Global_Lighthouse_Network_2023.pdf](https://www3.weforum.org/docs/WEF_Global_Lighthouse_Network_2023.pdf), стр.2 — прочитано прямо | self-report |
| дек. 2019/янв. 2020 | **44** | +28 в 2019 (14 из них E2E) | WEF_Global_Lighthouse_Network.pdf — не проверено прямым чтением, только через сводку | self-report, не перепроверено |
| сент. 2020 | **54** | +10 в Q3 2020 | [WEF_GLN_2020_Four_Durable_Shifts.pdf](https://www3.weforum.org/docs/WEF_GLN_2020_Four_Durable_Shifts_In_Manufacturing.pdf) — прочитано прямо | self-report |
| март 2021 | **69** | +15 | [WEF_GLN_2021_Reimagining_Operations_for_Growth.pdf](https://www3.weforum.org/docs/WEF_GLN_2021_Reimagining_Operations_for_Growth.pdf) — прочитано прямо | self-report |
| янв. 2023 | **132** | +29 в 2022 + 7 sustainability | [WEF_Global_Lighthouse_Network_2023.pdf](https://www3.weforum.org/docs/WEF_Global_Lighthouse_Network_2023.pdf), стр.5 — прочитано прямо | self-report |
| конец 2023 | **153** | +21 в 2023 | [weforum.org/stories](https://www.weforum.org/stories/2024/01/advanced-tecnologies-manufacturing-factories-scaling-innovations/) — не проверено прямым чтением | self-report, не перепроверено |
| 08.10.2024 | **172** | +22 (19 Fourth IR + 3 Sustainability) | weforum.org/media (403 при fetch, через сводку) | self-report, не перепроверено |
| 14.01.2025 | **189** | +17 (13 Fourth IR + 5 Sustainability) | [WEF_Global_Lighthouse_Network_2025.pdf](https://reports.weforum.org/docs/WEF_Global_Lighthouse_Network_2025.pdf) — прочитано прямо: «the GLN has expanded from 16 to 189» | self-report, подтверждено прямым чтением |
| 15.01.2026 | заявлено **223** | +23 новых в этом раунде (заголовок пресс-релиза) | weforum.org/media (403 при fetch, через сводку) | self-report, не перепроверено |

**Б. Ретроспективная диаграмма из white paper янв. 2026 (Figure 1, cumulative) — ДРУГИЕ числа для тех же лет**, прочитано прямо из [WEF_Global_Lighthouse_Network_2026.pdf](https://reports.weforum.org/docs/WEF_Global_Lighthouse_Network_2026.pdf), стр.6:

| год | накопительно (диаграмма 2026) |
|---|---|
| 2018 | 16 |
| 2019 | 26 |
| 2020 | 54 |
| 2021 | 93 |
| 2022 | 124 |
| 2023 | 170 |
| 2024 | 201 |
| 2025 | 223 |

Текст того же отчёта: «Having expanded from 16 factories to **223 sites**... In 2025, GLN proudly welcomed an additional **34** Lighthouses».

### Противоречия между отчётами WEF (пойманы при прямом чтении PDF, не гипотетические)

1. **Диаграмма 2026 почти не совпадает с собственными «живыми» пресс-релизами WEF**, кроме концов ряда:
   - 2019: диаграмма — 26, white paper дек.2019 — 44. Разница 18.
   - 2021: диаграмма — 93, white paper март 2021 (прочитан прямо) — 69. Разница 24.
   - 2022: диаграмма — 124, white paper янв.2023 (прочитан прямо) — 132 как итог именно 2022 года. Разница 8 (диаграмма даёт МЕНЬШЕ).
   - 2023: диаграмма — 170, оценка «конец 2023» — 153. Разница 17.
   - 2024: диаграмма — 201, январский 2025 white paper (прочитан прямо, ближайший по времени документ) — «from 16 to 189». Разница 12.
   Единственные совпадающие точки — старт (16) и последний итог (223). Вероятная причина: WEF задним числом пересчитал исторический ряд по новой методологии категорий (Sustainability lighthouse — с 2020, customer-centricity/talent — с 2025), и новая разбивка не стыкуется со старыми пресс-релизами. **Пример для лекции: одна и та же организация даёт разные числа для одного года в разных документах — важна дата публикации, а не только дата события.**
2. **Несовпадение внутри ОДНОГО релиза 2026 года**: пресс-релиз 15.01.2026 — «23 new sites»; white paper того же месяца — «In 2025, GLN welcomed an additional 34 Lighthouses». Арифметика: 189+23=212, а заявлено 223 (разрыв 11). Вероятное объяснение (подтверждается структурой отчёта 2025 — «evaluated in two cohorts, reflecting two application waves... Wave 12/Wave 13»): 34 = сумма двух волн 2025 года, из которых публично анонсирована громко только последняя партия (23). Публично WEF это не проговаривает явно.

### Конкретные примеры с измеренными эффектами и базой

| завод | год | что измерено | база → результат | источник | тип |
|---|---|---|---|---|---|
| **Unilever, Tinsukia (Индия)** | 2025 (E2E, Wave 13) | период «заморозки» планирования для e-commerce | **с 14 дней до 1 дня** (−92%), за счёт ML-driven planning + AI-enabled changeovers | [WEF_Global_Lighthouse_Network_2025.pdf](https://reports.weforum.org/docs/WEF_Global_Lighthouse_Network_2025.pdf), стр.43-44 — прочитано прямо | self-report, абсолютная база дана |
| **GE HealthCare, Пекин** | 2025 (Factory) | цикл производства, брак, жалобы клиентов — через AI defect detection + deep learning vision | цикл −66%, брак −66%, жалобы −73% — **абсолютная база НЕ дана**, только %% | WEF_Global_Lighthouse_Network_2025.pdf, стр.36 — прочитано прямо | self-report, **classic «missing denominator»** |
| **Johnson & Johnson Consumer Health, Хельсингборг (Швеция)** | профиль в white paper март 2021 | CO₂-выбросы завода | **с 5000 т (2010) до 0 т (2017)**, удержано с 2017; энергопотребление −25% (18 п.п. из них — от 4IR); OEE +14% (робототехника); себестоимость −20% (цифровой двойник) | [WEF_GLN_2021...pdf](https://www3.weforum.org/docs/WEF_GLN_2021_Reimagining_Operations_for_Growth.pdf), стр.24 — прочитано прямо | self-report, абсолютная база дана |
| Novo Nordisk, Хиллерёд (Дания) (доп., без детальной базы) | 2021 | «statistical twin» ML предсказывает настройки станков | OEE +10 п.п., простой −40…85% (диапазон) | WEF_GLN_2021...pdf, стр.19-20 | self-report |

### Классическая автоматизация/digitalization vs реальный ML/AI в сети «маяков»

Ключевой факт из прямого чтения отчёта 2025 (стр.11, Figure 5): доля «analytical AI» среди топ-5 кейсов маяков выросла с ~62% (2023) до 77% (2024), доля GenAI — всего 9% (2024). **Даже в «ИИ-маяках» бо́льшая часть изменений — не генеративный ИИ, а более старая analytical AI/IoT-аналитика.**

**Явный реальный ML/AI:**
- Computer vision/deep learning: Emirates Global Aluminium (ОАЭ) — «deep learning video supervisor» + online inspection качества электродов; GE HealthCare Пекин — AI vision inspection; Hisensehitachi Циндао — computer vision для flexible automation (все — [2025 white paper](https://reports.weforum.org/docs/WEF_Global_Lighthouse_Network_2025.pdf), стр.17, 36, 43).
- Predictive maintenance как настоящая модель: Agilent Penang (ML для 3D-печати); Jubilant Ingrevia (Индия) — predictive maintenance −85% незапланированных часов ремонта; ReNew Power (Индия, 2021) — advanced analytics/ML снизили простой ветро/солнечных активов на 31%.
- GenAI с измеренным эффектом: Hisensehitachi — GenAI-ассистент для пересменки → OEE +16%; Aramco North Ghawar — AI asset failure prediction c LLM → OEE +77%, GenAI co-pilot → training cost −75% (2025 wp, стр.13, 40).

**Классическая автоматизация/lean БЕЗ обученной модели (часто маскируется под «4IR»):**
- Siemens Амберг — +140% выпуска без роста энергопотребления, но драйверы — роботизированная логистика и upskilling, а не ML-модель как таковая.
- J&J Хельсингборг — «smart energy management integrated with automated systems and sensors», advanced controls, робототехника, цифровой двойник — классическая digitalization/connectivity, не обученная модель.
- AstraZeneca, Уси (Китай) — «IoT-based smart andon integrated with skill matrixes» → OEE +31% — правило-ориентированная логистика, не ML.
- Danone/Cipla/Midea (кейсы масштабирования, white paper 2023) — вообще не про конкретную AI-модель, а про организационные практики (transformation office, agile squads); цифры в диапазонах (20-80%) без единой базы.

**Общий вывод для лекции:** абсолютная база присутствует редко — явно найдено только 2 случая с чистой абсолютной базой (Unilever Tinsukia, J&J Хельсингборг) из десятков разобранных кейсов. Это системная проблема первоисточника WEF/McKinsey, а не недосмотр фактчека — хороший материал для слайда «даже у авторитетного источника большинство цифр без базы».

---

## Что НЕ подтвердилось / противоречия источников (сводно)

1. **Siemens Amberg**: «500 dpm в 1989» — не подтверждено первичным документом. Множитель роста выпуска (8×/9×/13×/14×) и год основания (1989/1991) расходятся между публикациями самого Siemens. DPM «12» vs «1» (10× разница) в двух self-report цитатах без датировки второй. Прямая цитата про экономику «почему 75%, не больше» — не найдена.
2. **FANUC Oshino**: «500→100 работников» — конфляция данных 1981 г. (другой завод/эпоха) с описанием 2002 года у вторичных источников. Нет подтверждения, что миф про AI relates именно к Ошино — реальный deep learning-продукт (AI Bin Picking) демонстрировался в офисе в Токио, не на этом заводе. Первоисточник CNN 2003 не прочитан напрямую (403/503) — все цифры восстановлены через цитирование третьими сторонами. Независимый контрапункт: по Assembly Magazine 72% операций производства по-прежнему делают люди, lights-out «не практично для каждого применения» по признанию самого FANUC.
3. **Xiaomi Чанпин**: «1 телефон в секунду» — арифметическая ошибка маркетинга (на деле 1/3,15 сек при заявленной мощности); независимый репортаж фиксирует фактическую загрузку ~52% от заявленной мощности. «Полностью безлюдный» прямо противоречит собственному признанию Xiaomi (220 человек на линии). Съёмка внутри завода запрещена даже журналистам — ограничивает независимость любой проверки. Легко спутать с 3 другими заводами Xiaomi (авто, бытовая техника, более ранний экспериментальный «黑灯工厂» 2020 г.).
4. **Philips Drachten**: «9 рабочих на контроль качества» — не подтверждено первоисточником (NYT говорит «несколько десятков», не 9). Нет подтверждения полного переноса производства из Китая — Drachten и Zhuhai оставались параллельными площадками.
5. **Hyundai Metaplant**: число роботов/AGV расходится 2-3× между пересказами одной статьи (требует ручной проверки первоисточника). Atlas — анонс, не внедрение (реальный статус — пилот с 2026). Мощность «500 000/год» — цель, факт 2024 — 300 000 (60%).
6. **WEF Lighthouse Network**: ретроспективная диаграмма 2026 г. не совпадает почти ни в одной промежуточной точке (2019-2024) с собственными историческими пресс-релизами WEF — разница от 8 до 24 сайтов на точку. Внутри одного релиза января 2026 число «новых сайтов» (23) не складывается с заявленным приростом за год (34) — разрыв 11, вероятно из-за двух необъявленных явно «волн» подачи заявок. Абсолютная база эффектов дана лишь в 2 из разобранных кейсов (Unilever, J&J) — остальные (включая GE HealthCare) дают только %% без знаменателя.

---

## Оценка надёжности по объектам

| объект | надёжность | причина |
|---|---|---|
| **WEF Lighthouse Network** | Средняя-высокая для прямо прочитанных PDF (2020/2021/2023/2025/2026 — все открыты и процитированы напрямую); низкая для сверки между годами — сам первоисточник внутренне непоследователен (см. противоречия выше). Эффекты в кейсах — self-report WEF/McKinsey, независимой проверки нет. |
| **Siemens Amberg** | Средняя. Ключевые цифры (75% автоматизации, DPM~12 за 2015, факт инвестиций 2025/2026) подтверждены первичными документами Siemens. Множитель роста и год основания — противоречивы между собственными публикациями Siemens. Единственный железно подтверждённый ML-кейс — рентген-инспекция (peer-reviewed, 29% снижение). Много low-quality контента в поисковой выдаче (AI-generated SEO-сайты) — явно исключён. |
| **Hyundai Metaplant** | Средняя. Крупные цифры (инвестиции, даты запуска, штат, рейд ICE) подтверждены независимой прессой (Reuters/CNN/Axios/Newsweek) и совпадают с self-report. Детальные операционные цифры (число роботов/AGV) — противоречивы между пересказами одной отраслевой статьи, не перепроверено на первоисточнике. Atlas — чистый анонс, явно помечен как неподтверждённое внедрение. |
| **Philips Drachten** | Средняя-низкая. Базовый факт (128 роботов, 2012, NYT) надёжен — независимый репортаж с места. Но данные устарели (последний self-report — 2022, в основном общие цифры без деталей по технологии). Популярная цифра «9 рабочих» — не подтверждена, вероятно ошибка компиляции. |
| **FANUC Oshino** | Низкая-средняя. Исторический миф (2001-2003) не прочитан на первоисточнике (CNN недоступен), восстановлен только через пересказы. Современные self-report цифры (fanuc.eu) надёжны для производственной мощности, но не для самого «lights-out»-режима сегодня. Высокий риск конфляции данных из разных десятилетий — явно зафиксирован. Независимый контрапункт (Assembly Magazine, 72% операций руками) — единственный по-настоящему независимый и скептический источник среди всех собранных. |
| **Xiaomi Чанпин** | Низкая. Почти все цифры — self-report/маркетинг, подхваченный прессой без проверки (кроме единичного честного пересчёта slashgear.com и репортажа euronews.com на месте). Съёмка на объекте запрещена — фундаментальное ограничение независимости любой проверки. Высокий риск путаницы с другими заводами Xiaomi под той же фразой «dark factory». |

---

## Методологическая заметка

Для WEF-источников потребовался прямой `curl`-фетч PDF с `weforum.org` (стабильно отдававшего 403 через стандартный WebFetch) — подтверждает известное ограничение «WebFetch ненадёжен», уже зафиксированное в `notes/mcp-limitations.md` проекта. Для нескольких других источников (CNN Money 2003, CSMonitor 1981, money.cnn.com, Bloomberg 2012, Wiley ISJ 2025/2026, HBS 518-054) первичный текст остался недоступен (платный доступ/403/archive.org недоступен инструментам) — везде, где это так, это явно помечено «не прочитано напрямую» рядом с цифрой, а не скрыто.
