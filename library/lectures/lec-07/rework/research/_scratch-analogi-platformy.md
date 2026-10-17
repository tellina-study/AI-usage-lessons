# Аналоги: чему и как учат про ИИ в медицине на массовых платформах и во врачебных обществах

Черновик-разведка для переработки Лекции 7. **Не коммитить.**

Дата сбора: **2026-10-14**. Всё ниже получено **прямым чтением страниц**, если прямо не сказано иное.

## Как читалось и чему верить

| Пометка | Что значит |
|---|---|
| **прочитано** | страница открыта и разобрана целиком, перечень модулей скопирован с неё |
| **прочитано (архив)** | живая страница закрыта защитой от роботов (Cloudflare) или входом; читался снимок Wayback, дата снимка указана |
| **только сниппет** | перечень виден лишь в выдаче поиска, самой страницы открыть не удалось — такой перечень к доказательствам не относится |
| **не открылось** | названа причина, домысла нет |

Инструменты: прямой запрос страницы с вырезанием сценариев и оформления; при отказе — снимок Wayback через `timemap` (служебный ответ «снимков нет» оказался ложным минимум трижды: `timemap` отдавал снимки там, где `archive.org/wayback/available` возвращал пустоту — см. § «Чего стоило чтение»).

**Разведка разрезана на три части по лимиту 600 строк (CLAUDE.md § Document Size Limit).**

- **Часть 1 (этот файл):** как читалось · сводные таблицы · A. Coursera · B. edX и университетские курсы
- **Часть 2:** [`_scratch-analogi-platformy-part2.md`](_scratch-analogi-platformy-part2.md) — C. Врачебные ассоциации, издатели, коллегии и государственные службы
- **Часть 3:** [`_scratch-analogi-platformy-part3.md`](_scratch-analogi-platformy-part3.md) — D. Перечни компетенций · сквозная раскладка по рубрикам · **что системно есть / чего системно нет** · чего не удалось прочитать · заметки о приёме

---

## Сводка прочитанного

**Прочитано: 26 учебных программ + 19 нормативных, консенсусных и обзорных документов.** Отдельно перечислено 10 позиций, которые открыть не удалось или которых не существует (§ «Чего не удалось прочитать»).

### Учебные программы

| № | Программа | Кто | Год/версия | Кому | Объём | Деньги | Кредиты | Пара человек+модель |
|---|---|---|---|---|---|---|---|---|
| A1 | AI in Healthcare Specialization | Stanford Online (Shah, Lungren, Yeung, Cho, Baker, Hernandez-Boussard) | выпуск 10.08.2023, кредиты до 09.08.2029 | врачи **и** инженеры, начальный | 5 курсов, 60 ч | подписка, есть финпомощь | **54,5 AMA PRA Cat. 1** | **1 видео, 5 мин = 0,15% программы** |
| A2 | AI for Medicine Specialization | DeepLearning.AI (Rajpurkar, Shyu, Kiani) | действует на 2026-10-14 | инженеры со знанием нейросетей | 3 курса, 10 недель, 72 ч | подписка | нет | **нет ничего** |
| C11 | AI Series: Fundamentals of AI and ML in Healthcare | Stanford Center for CME | действует | врачи и руководители | перечень за входом | платно | CME | не читано |
| B1 | MITx 6.871Jx Machine Learning for Healthcare | MITx (Sontag) | снимок 2023-05-28, помечен «archived» | продвинутые инженеры | 15 недель, 8–12 ч/нед | $49 / бесплатно | нет | **раздел «Human Factors», 3 недели; «Learning to Defer» + домашняя работа** |
| B2 | 6.S897/HST.956 Machine Learning for Healthcare | MIT OpenCourseWare (Szolovits, Sontag) | Spring 2019 | выпускники с базой ML | 25 занятий | бесплатно | нет | **нет** (появилось позже, в версии edX) |
| B3 | Applications of AI in Healthcare | HBKUx (Hamad Bin Khalifa University) | снимок 2025-02-16 | медработники без техбазы | 9 модулей, свой темп | $119 / бесплатно | нет | «AI Mistrust and Explainable AI» — про **недоверие**, не про якорение |
| B4 | Introduction + Advanced Principles in AI & ML in Healthcare | MGH Institute of Health Professions | действует | от начального к среднему | 5 + 4 недели | платно | нет | **нет** (перечень из вторичного источника) |
| B5 | AI in Healthcare. Hype or Help? | KU Leuven (De Vos, Claes) | действует, код B-KUL-E0J85A | врачи-специалисты, последипломные программы | 4 ECTS, 8 тем | $80 | ECTS, не CME | «How to coexist with AI» — 1 тема из 8 |
| B6 | Artificial Intelligence in Health Care | MIT Sloan Executive Education | набор 11.11.2026 | руководители здравоохранения | 6 недель, 6–8 ч/нед | **$3 250** | нет | **нет**; регуляторики и этики тоже нет |
| B7 | AI in Medicine: Foundations and Applications | Harvard Medical School (HMX) | действует | клиницисты, исследователи | 11 единиц | $495 | не указаны | **нет**; зато 3 единицы из 11 — регуляторика |
| B8 | BIODS220 Artificial Intelligence in Healthcare | Stanford (Yeung), зачётный | Fall 2022–23 | выпускники CS/биомед | 14 лекций | плата за обучение | нет | **нет**; прозрачность+справедливость+этика = 1 лекция |
| C1 | Artificial Intelligence in Health Care Series | AMA ChangeMedEd + University of Michigan DATA-MD | снимок 2025-11-19 | **студенты-медики**, также резиденты и практики | 7 модулей | **бесплатно** | **4,0 CME** | отдельного модуля нет |
| C2 | Practical Applications for AI in Health Care | AMA Ed Hub (JAMA и др.) | снимок 2025-05-29 | врачи, студенты, медработники | 29 материалов | смешанно | **26,75 CME** | «Augmented Decision-Making **Opportunities**» — 1 материал из 29 |
| C3 | Artificial and Augmented Intelligence in Health Care | AMA Ed Hub | снимок 2026-07-25 | врачи, студенты, специалисты | 18 материалов | смешанно | **22,75 CME** (было 16 на снимке 2024-05-11) | **нет модуля**, но во вводном абзаце прямо названа чрезмерная опора |
| C5a | RSNA Imaging AI Foundational Certificate v2.0 | RSNA | v2.0, выпуск с 15.07.2026 | радиологи, физики, резиденты | 6 модулей (открыто 3) | $425–725 | **CME не предлагается** | модули 4–6 не опубликованы |
| C5b | RSNA Advanced Certificate | RSNA | действует | радиологи | 6 модулей | $555–855 | **нет** | «the human side of AI» в модуле этики |
| C5c | RSNA Emergency Certificate | RSNA | действует | резиденты и радиологи приёмного покоя | 6 модулей + практикум | $480–780 | **нет** | **да, модуль 6: «consequences of overreliance on automated systems for human readers»** |
| C5d | RSNA Chest Certificate | RSNA | действует | радиологи грудной клетки | 6 модулей | $480–780 | **нет** | **да, учебная цель: «Explain how overreliance on AI can affect human interpretation and diagnostic accuracy»** |
| C6 | ACR AI-LAB | ACR Data Science Institute | платформа 2.7 | радиологи-разработчики | 22 единицы + конвейер | **бесплатно** | нет | «What can go wrong?» — только заголовок |
| C10 | 3-дневный курс для резидентов-радиологов | UMC Groningen (проект B3CARE) | 2024 | старшие резиденты (3–5 лет) | 24 ч за 3 дня | — | — | нет; **есть измеренный результат курса** |
| C12c | Каталог «Artificial intelligence» + рамка способностей | NHS Learning Hub / Цифровая академия NHS | рамка 2023 | весь персонал NHS | 5 областей + 6-я полка | **бесплатно** | не CME | через отчёты C12a/C12b |
| C12d | An introduction to AI for healthcare professionals (занятие 48) | NHS e-learning for healthcare | 27.10.2023 | медработники, программа Clinical Imaging | 1 занятие | **бесплатно** | не указаны | перечень экранов не опубликован |
| C15a | AiM-PC: AI/ML in Primary Care | STFM, одобрено AAFP | действует | студенты, резиденты, практики первичного звена | 5 модулей × 60 мин | **бесплатно** | 5,0 AAFP Prescribed | нет; модули 2–4 дословно повторяют домены Russell |
| C15b | Revealing AI Use Cases in Family Medicine | AAFP (Waldren) | действует | семейные врачи | 1 материал | **бесплатно** | AAFP Prescribed | **нет** |
| C16 | AI Resource Hub | ACP | действует | врачи-интернисты | 5 разрозненных позиций | членам бесплатно | по позициям | **нет**; 2 из 5 — тренажёры, где модель играет пациента |
| C12b | Developing healthcare workers' confidence in AI (предложенная программа) | Health Education England + NHS AI Lab | октябрь 2022 | весь персонал NHS, 5 ролей | 113 стр.: базовая + продвинутая части | **бесплатно** | не CME | **да, полнее всех: раздел §4.3 «The risk of deskilling» + искажения в базовой части** |

### Нормативные, консенсусные и обзорные документы

| № | Документ | Кто | Год | Жанр | Якорение дословно | Износ навыка дословно | Числа |
|---|---|---|---|---|---|---|---|
| C4 | Augmented intelligence in medicine (страница) | AMA | обновлено 01.04.2025 | рамка + опрос | нет | нет | **да: 68% / 65%, 38% → 66%** |
| C3a | AI in medical education (страница) | AMA | снимок 2026-10-05 | рамка | нет | нет | нет |
| C7 | Teaching AI for Radiology Applications: a Multisociety-Recommended Syllabus | AAPM + ACR + RSNA + SIIM | 2025–2026 | силлабус по 4 лицам | **да: «Risks of automation bias and methods of mitigation»** | нет | нет |
| C8 | What the radiologist should know about AI — ESR white paper | ESR | 2019 | позиция общества | нет термина; есть цитата про доверие машине | **да, развёрнуто** | нет |
| C9 | Training opportunities of AI in radiology: a systematic review | Schuur, Rezazade Mehrizi, Ranschaert | 2021 | систематический обзор | **0 упоминаний** | **0 упоминаний** | **да, про сам рынок обучения** |
| C13 | AI deployment fundamentals for medical imaging | Royal College of Radiologists | ноябрь 2024 | руководство для служб | **да, прямо, с мерой: «своё мнение первым»** | нет | нет |
| C14 | Topol Review: Progress on the recommendations | HEE / NHS | 2019 / февраль 2023 | государственное поручение | нет | нет | нет |
| C12a | Understanding healthcare workers' confidence in AI | HEE + NHS AI Lab | май 2022 | основание для программы | **да, с таксономией 5 искажений** | нет | **нет** |
| C17 | Artificial Intelligence (позиция) | RCGP | январь 2026 | позиция + перечень руководств | нет | нет | **да: 28% применяют, 57% записи, 28% решения, 89% препятствие** |
| C19 | NEJM AI | NEJM Group | с 2023 | **журнал, не обучение** | — | — | — |
| D0 | AI competencies | **AAMC** | **не выпущено; обещано осенью 2026** | — | — | — | — |
| D1 | AI Competencies for Medical Educators | CGEA Faculty Development SIG | май 2025 | консенсус рабочей группы | **да: «Identify automation bias and preserving skills»** | **да, в той же строке** | нет |
| D2 | Augmented Intelligence Development, Deployment, and Use in Health Care | AMA House of Delegates | принята 12.11.2024 | принятая политика | по смыслу: «human in the loop… intervening or overriding» | **по смыслу, жёстко: «able to provide the same medical service without the aid of AI»** | нет |
| D3 | Политика по грамотности в ИИ для медобразования | AMA House of Delegates | ноябрь 2026 | политика (поручение себе) | нет | нет | нет |
| D4 | Competencies for the Use of AI–Based Tools by Health Care Professionals | Russell et al., Academic Medicine | 2023 | 15 экспертных бесед | нет; есть «exercise judgment in applying AI-generated recommendations» | нет | нет |
| D5 | AI in medical education curriculum: an e-Delphi study | Çalışkan, Demir, Karaca, PLoS ONE | 2022 | трёхкруговой Delphi, 60 экспертов | **0** | **0** | да, про сам опрос |
| D6 | Developing a Canadian AI medical curriculum | Singla et al., npj Digital Medicine | 2024 | Delphi, 18 экспертов, привязка к CanMEDS | нет; есть «user biases» и «shared decision-making with AI» | нет | да, про сам опрос |
| D7 | Guidance on large multi-modal models | **ВОЗ** | 2024 | руководство | **да, многократно + поручение министерствам и вузам** | **да: «moral de-skilling», «Skills degradation»** | нет |
| D8 | Ethics and governance of artificial intelligence for health | **ВОЗ** | 2021 | руководство, 165 стр. | **да, 6 раз** | нет термина | нет |

---

## A. Coursera

### A1. AI in Healthcare Specialization (Stanford Online)

- Страница специализации: `https://www.coursera.org/specializations/ai-healthcare` — **прочитано 2026-10-14**
- Записано слушателей на день чтения: **97 392**; оценка 4,7 по 2 645 отзывам
- Уровень: «Beginner level. No prior experience required»
- Объём: «4 weeks to complete at 10 hours a week», сумма по курсам — 60 часов
- Кому: дословно — «This specialization is designed for both healthcare providers and computer science professionals, offering insights to facilitate collaboration between the disciplines»
- Деньги: входит в подписку Coursera Plus, есть финансовая помощь
- Кредиты: **54,5 кредита AMA PRA Category 1** на всю специализацию — прочитано в разделе частых вопросов каждого курса 2026-10-14. По курсам: Introduction to Healthcare — **12,00**; Introduction to Clinical Data — **11,00**; Fundamentals of Machine Learning for Healthcare — **11,00**; Evaluations of AI Applications in Healthcare — **9,50**; AI in Healthcare Capstone — **11,00**. Дата первого выпуска **10.08.2023** (у выпускного курса 16.11.2023), срок годности кредитов — **09.08.2029**. Формулировка дословно: «The Stanford University School of Medicine designates this enduring material for a maximum of 11.00 AMA PRA Category 1 Credits™. Physicians should claim only the credit commensurate with the extent of their participation in the activity.» На страницах курсов — совместная аккредитация ACCME + ACPE + ANCC (врачи, провизоры, медсёстры).

  **Это и есть наша главная цифра по рубрике (ж).** Крупнейшая врачебная программа по ИИ в медицине, выпущенная медицинским факультетом Стэнфорда и дающая врачу **54,5 зачётных кредита**, отводит якорению на подсказке **5 минут** — одно видео «Death by GPS and Other Lessons of Automation Bias». Это **0,15% программы**. Падению квалификации — ноль минут: такого заголовка нет ни в одном из 5 курсов.
- Что обещают на выходе, дословно: «Identify problems healthcare providers face that machine learning can solve» · «Analyze how AI affects patient care safety, quality, and research» · «Relate AI to the science, practice, and business of medicine» · «Apply the building blocks of AI to help you innovate and understand emerging technologies»

Пять курсов: «Introduction to Healthcare» (12 ч) · «Introduction to Clinical Data» (12 ч) · «Fundamentals of Machine Learning for Healthcare» (14 ч) · «Evaluations of AI Applications in Healthcare» (11 ч) · «AI in Healthcare Capstone» (11 ч).

#### Курс 1. Introduction to Healthcare

`https://www.coursera.org/learn/intro-to-healthcare` — **прочитано 2026-10-14**. 7 модулей. Преподаватели: Nigam Shah, Mildred Cho, Laurence Baker.

Модули дословно:

1. **Overview of Health Care Systems and Key Challenges They Face** (2 ч, 12 видео)
2. **Physicians, Physician Practices, and Physician Payment** (2 ч, 12 видео)
3. **Hospitals, Other Provider Organizations, and Related Payment Systems** (2 ч, 13 видео)
4. **Intermediaries, Health Insurance Plans, and Health Care Financing** (2 ч, 15 видео)
5. **Health Care Products and Prescription Drugs, and Quality Measurement and Improvement** (2 ч, 13 видео)
6. **Ethics** (1 ч, 4 видео) — подзаголовок «Ethics in Healthcare System»
7. **Course Wrap Up** (1 ч) — «Course Summary», «Final Assessment Note», «Claim CME Credit», «Full Study Guide», «Final Assessment • 60 minutes»

Содержание модуля 6 дословно: «Overview of AI applications in delivery of health care services and ethical issues» (5 мин) · «Ethical frameworks for health care and for AI» (5 мин) · «AI and incentives in health care delivery and payment structures» (6 мин) · «More examples of AI and incentives in health care delivery and payment structures» (6 мин).

Наблюдение, важное для нас: **в каждом из модулей 1–5 последнее содержательное видео называется «Lessons for AI and Data» / «Lessons for Innovators» / «Innovation and Data in Quality Improvement» и длится 1–4 минуты.** То есть весь первый курс специализации — это 12 часов про устройство американского здравоохранения и оплату труда врача, к которым ИИ подшит одной минутой в конце каждого раздела. Это ровно тот порядок, который мы в Лекции 7 ставим первым шагом раздела: сначала показать работу, в которую ИИ вмешивается. Stanford отдаёт на это **целый курс из пяти**, то есть пятую часть программы.

#### Курс 2. Introduction to Clinical Data

`https://www.coursera.org/learn/introduction-clinical-data` — **прочитано 2026-10-14**. 8 модулей. Преподаватели: Nigam Shah, Steven Bagley, David Magnus.

1. **Asking and answering questions via clinical data mining** (1 ч, 12 видео)
2. **Data available from Healthcare systems** (2 ч, 16 видео)
3. **Representing time, and timing of events, for clinical data mining** (1 ч, 12 видео)
4. **Creating analysis ready datasets from patient timelines** (2 ч, 18 видео)
5. **Handling unstructured healthcare data: text, images, signals** (2 ч, 19 видео)
6. **Putting the pieces together: Electronic phenotyping** (1 ч, 11 видео)
7. **Ethics** (1 ч, 7 видео)
8. **Course Conclusion** (1 ч)

Внутри модуля 2 — отдельная связка про то, как система здравоохранения сама портит данные: «Actors with different interests» · «Strengths and weaknesses of observational data» · «Bias and error from the healthcare system perspective» · «Bias and error of exposures and outcomes» · «How a patient's exposure might be misclassified» · «How a patient's outcome could be misclassified». Модуль 3 заканчивается кадром **«Clinical processes are non-stationary»** — то есть сдвиг данных подан не оговоркой, а названным свойством клинической работы.

Модуль 7 дословно: «Introduction to Research Ethics and AI» (5 мин) · «The Belmont Report: A Framework for Research Ethics» (7 мин) · «Ethical Issues in Data sources for AI» (7 мин) · «Secondary Uses of Data» (9 мин) · «Return of Results» (6 мин) · **«AI and The Learning Health System»** (10 мин) · «Ethics Summary» (3 мин).

#### Курс 3. Fundamentals of Machine Learning for Healthcare

`https://www.coursera.org/learn/fundamental-machine-learning-healthcare` — **прочитано 2026-10-14**. 8 модулей. Преподаватели: Matthew Lungren, Serena Yeung. Соавтор Geoffrey Angus; редакторы Mars Huang, Jin Long, Shannon Crawford, Oge Marques.

Кому, дословно: «The course will empower those with non-engineering backgrounds in healthcare, health policy, pharmaceutical development, as well as data science with the knowledge to critically evaluate and use these technologies».

1. **Why machine learning in healthcare?** — «Why machine learning in healthcare?» · «History of AI in Medicine» · «Course Overview» · «Why Healthcare Needs Machine Learning» · **«Machine Learning Magic»** (9 мин) · «Machine Learning, Biostatistics, Programming» · **«Can Machine Learning Solve Everything?»** (6 мин)
2. **Concepts and Principles of machine learning in healthcare part 1** — термины и жаргон (2 части), «How Machines Learn» (2 части), «Supervised Machine Learning Approaches: Regression and the "No Free Lunch" Theorem», «Other Traditional Supervised Machine Learning Approaches», «Support Vector Machine (SVM)», «Unsupervised Machine Learning»
3. **Concepts and Principles of machine learning in healthcare part 2** — «Introduction to Deep Learning and Neural Networks» · «Deep Learning and Neural Networks» · «Cross Entropy Loss» · «Gradient Descent» · «Representing Unstructured Image and Text Data» · «Convolutional Neural Networks» · «Natural Language Processing and Recurrent Neural Networks» · «The Transformer Architecture for Sequences» · «Commonly Used and Advanced Neural Network Architectures» · «Advanced Computer Vision Tasks and Wrap-Up»
4. **Evaluation and Metrics for machine learning in healthcare** — «Introduction to Model Performance Evaluation» · «Overfitting and Underfitting» · «Strategies to Address Overfitting, Underfitting and Introduction to Regularization» · «Statistical Approaches to Model Evaluation» · «Receiver Operator and Precision Recall Curves as Evaluation Metrics»
5. **Strategies and Challenges in Machine Learning in Healthcare** — «Introduction to Common Clinical Machine Learning Challenges» · «Utility of Causative Model Predictions» · «Context in Clinical Machine Learning» · «Intrinsic Interpretability» · «Medical Data Challenges in Machine Learning Part 1 / Part 2» · «How Much Data Do We Need?» · **«Retrospective Data in Medicine and "Shelf Life" for Data»** · **«Medical Data: Quality vs Quantity»**
6. **Best practices, teams, and launching your machine learning journey** — «Clinical Utility and Output Action Pairing» · «Taking Action - Utilizing the OAP Framework» · «Building Multidiciplinary Teams for Clinical Machine Learning» · «Governance, Ethics, and Best Practices» · **«On Being Human in the Era of Clinical Machine Learning»** (8 мин) · **«Death by GPS and Other Lessons of Automation Bias»** (5 мин). Плюс чтение «Recommended Reading for Ethics» (15 мин)
7. **Foundation models (Optional Content)** — «Introduction to Foundation Models» (13 мин) · «Adapting to Technology» · «General AI and Emergent Behavior» · «How Foundation Models Work» (22 мин) · «Healthcare Use Cases for Text Data» · «Healthcare Use Cases for Non-textual Unstructured Data» · **«Challenges and Pitfalls»** (14 мин) · «Conclusion». **Помечено как необязательное и без зачётных заданий.**
8. **Course Conclusion**

**Это единственное место во всех 26 прочитанных учебных программах, где якорение на подсказке названо своим именем в заголовке учебной единицы.** Называется дословно **«Death by GPS and Other Lessons of Automation Bias»**, длится **5 минут**, стоит шестым видео в шестом модуле третьего курса из пяти — то есть примерно на 36-м часе из 60. Чисел по страницы не видно: формат — 5-минутное видео, построенное, судя по названию, на небедицинской истории про навигатор. Измерений человеко-модельной пары в медицине здесь ждать не стоит; проверить содержимое без подписки нельзя — **помечаю как «название прочитано, содержимое не читано»**.

#### Курс 4. Evaluations of AI Applications in Healthcare

`https://www.coursera.org/learn/evaluations-ai-applications-healthcare` — **прочитано 2026-10-14**. 8 модулей. Преподаватели: Tina Hernandez-Boussard, Mildred Cho.

1. **AI in Healthcare** (10 видео) — «Common Definitions» · «Why AI is needed in Healthcare» · «Examples of AI in Healthcare» · «Growth of AI in Healthcare» · «Questions Answered by AI» · «AI Output» · **«Think beyond area under the curve»** (1 мин)
2. **Evaluations of AI in Healthcare** (15 видео) — «Recap: Framework» · «Stakeholders» · «Clinical Utility» · **«Outcome: Action Pairing, An Overview»** · «Lead Time» · «Type of Action» · «OAP Examples» · **«Number Needed to Treat»** · **«Net Benefits»** · **«Decision Curves»** · «Feasibility overview» · «Implementation Costs» · «Clinical Evaluation and Uptake»
3. **AI Deployment** (19 видео) — «The Problem» · «Practical Questions Prior to Deployment» · «Deployment Pathway» · «Design and Development» · «Stakeholder Involvement» · «Data Type and Sources» · «Settings» · «In Silico Evaluation» · **«Net Utility & Work Capacity»** · «Statistical Validity» · **«Care Integration, Silent Mode»** · «Clinical Integration, Considerations» · «Technical Integration» · «Deployment Modalities» · «Continuous Monitoring and Maintenance» · «Challenges of Deployment» · **«Sepsis Example»**
4. **Downstream Evaluations of AI in Healthcare: Bias and Fairness** (18 видео) — «Real World Examples of AI Bias» · «Historical Bias» · «Representation Bias» · «Measurement Bias» · «Aggregation Bias» · «Evaluation Bias» · **«Deployment Bias»** · «What is algorithmic Fairness» · «Anti-classification» · «Parity Classification» · «Calibration» · «Applying Fairness Measures» · «Lack of Transparency» · «Minimal Reporting Standards» · «Opportunities and Challenges»
5. **The Regulatory Environment for AI in Healthcare** (18 видео) — «International Definitions Used for Regulatory Purposes» · «Definition Statement & Risk Framework» · «Valid Clinical Association» · «Analytical Evaluation» · «Clinical Evaluation» · «General Control» · «de novo Notifications» · «Software Modification» · «TPLC» · **«Locked vs Adapted AI solutions»** · «Examples» · «Non-Regulated Products» · «EU Regulations» · «Chinese Guidelines» · «OMB Guidelines»
6. **Best Ethical Practices for AI in Health Care** — только 3 чтения, без видео: «Problem Formulation» · «Identifying Conflicts of Interest» · «Mitigating Conflicts of Interest»
7. **AI and Medicine (Optional Content)** (9 видео) — «Navigating the Intersections of AI and Medicine» · «Life Cycle of AI» · «A Deep Dive into Historical and Societal Dimensions» · «Race-Based Medicine and Race-Aware Approach» · «Bias Mitigation Strategies» · «Exploring Potentials and Ethical Quandaries» · «Dismantling Race-Based Medicine» · «Deploying AI into Healthcare Settings»
8. **Course Wrap Up** — «Final Exam • 60 minutes»

Три кадра из этого курса ближе всего к нашему разделу про переезд нагрузки:

- **«Net Utility & Work Capacity»** (2 мин, модуль 3) — единственная во всех 26 прочитанных программах учебная единица, в заголовке которой стоит **рабочая ёмкость**. То есть мысль «модель перекладывает нагрузку, и ёмкость смены конечна» в мировой практике существует — но ей отведено **две минуты**.
- **«Care Integration, Silent Mode»** (3 мин) — тихий режим как ступень внедрения, то есть модель сначала считает, не показываясь врачу.
- **«Number Needed to Treat»** + **«Net Benefits»** + **«Decision Curves»** (3+3+4 мин) — цена обеих ошибок в одних единицах. Это ровно наша рубрика, и здесь она присутствует **как метод, а не как предостережение**: курс учит считать чистую пользу, а не говорить «будьте осторожны».

#### Курс 5. AI in Healthcare Capstone

`https://www.coursera.org/learn/ai-in-healthcare-capstone` — **прочитано 2026-10-14**. 5 модулей. Преподаватели: Matthew Lungren, Nigam Shah (всего 5).

Сквозной случай, дословно: «the journey of a patient who develops some respiratory symptoms and given the concerns around COVID19 seeks care with a primary care provider». Набор данных — обезличенный, созданный специально для специализации, «spans EHR as well as image data».

1. **Getting Started, Phase 1: Data Collection** — 2 проекта + 2 взаимных проверки
2. **Phase 2: Model Training Part 1**
3. **Phase 3: Model Training Part 2**
4. **Phase 4: Model Evaluation**
5. **Phase 5: Model Deployment and Regulation, Wrap Up**

Обещание курса дословно: «We will review how the different choices you make -- such as those around feature construction, the data types to use, how the model evaluation is set up and how you handle the patient timeline -- affect the care that would be recommended by the model». То есть выпускная работа — про то, как решения разработчика меняют рекомендацию модели. **Про то, как рекомендация модели меняет решение врача, в выпускной работе нет ничего.** Асимметрия ровно в одну сторону.

### A2. AI for Medicine Specialization (DeepLearning.AI)

- Страница: `https://www.coursera.org/specializations/ai-for-medicine` — **прочитано 2026-10-14**
- Преподаватели: Pranav Rajpurkar, Eddy Shyu, Amirhossein Kiani (+1)
- Уровень: Intermediate. Дословно: «a working knowledge of deep neural networks, particularly convolutional networks, and proficiency in Python programming at an intermediate level will be essential»; и отдельно — «No prior medical expertise is required!»
- Объём: «2 months to complete at 10 hours a week»; по курсам 20 + 30 + 22 = 72 часа
- Деньги: подписка. **CME нет** — это инженерная программа, не врачебная
- Три курса: «AI for Medical Diagnosis» · «AI for Medical Prognosis» · «AI For Medical Treatment»

#### Курс 1. AI for Medical Diagnosis (3 недели)

`https://www.coursera.org/learn/ai-for-medical-diagnosis` — **прочитано 2026-10-14**

- **Week 1. Disease Detection with Computer Vision** (9 ч, 20 видео). Дословно часть названий: «Medical Image Diagnosis» · «Eye Disease and Cancer Diagnosis» · «Building and Training a Model for Medical Diagnosis» · «Training, Prediction, and Loss» · «Image Classification and Class Imbalance» · «Binary Cross Entropy Loss Function» · «Impact of Class Imbalance on Loss Calculation» · «Resampling to Achieve Balanced Classes» · «Multi-Task» · «Multi-task Loss, Dataset size, and CNN Architectures» · «Working with a Small Training Set» · «Generating More Samples» · «Model Testing» · **«Splitting Data by Patient»** · «Sampling» · **«Ground Truth and Consensus Voting»** · «Additional Medical Testing». Практика: «Chest X-Ray Medical Diagnosis with Deep Learning» (180 мин) + лаборатории «Data Exploration & Image Pre-Processing», «Counting Labels and Weighted Loss Function», «Densenet», **«Patient Overlap & Data Leakage»**
- **Week 2. Evaluating Models** (5 ч, 10 видео): «Sensitivity, Specificity and Evaluation Metrics» · «Accuracy in Terms of Conditional Probability» · «Sensitivity, Specificity and Prevalence» · «PPV, NPV» · «Confusion Matrix» · «ROC Curve and Threshold» · **«Varying the Threshold»** · «Sampling from the Total Population» · «Confidence Intervals» · «95% Confidence Interval»
- **Week 3. Image Segmentation on MRI Images** (7 ч, 10 видео): «Medical Image Segmentation» · «MRI Data and Image Registration» · «Segmentation» · «2D U-Net and 3D U-Net» · «Data Augmentation for Segmentation» · «Loss Function for Image Segmentation» · **«Different Populations and Diagnostic Technology»** · **«External Validation»** · **«Measuring Patient Outcomes»** (3 мин)

#### Курс 2. AI for Medical Prognosis (4 недели)

`https://www.coursera.org/learn/ai-for-medical-prognosis` — **прочитано 2026-10-14**

- **Week 1. Linear Prognostic Models** (8 ч, 11 видео): «Medical Prognosis» · «Examples of Prognostic Tasks» · «Atrial Fibrillation» · «Liver Disease Mortality» · «Risk of Heart Disease» · «Risk Score Computation» · «Evaluating Prognostic Models» · «Concordant Pairs, Risk Ties, Permissible Pairs» · «C-Index»
- **Week 2. Prognosis with Tree-based Models** (7 ч, 15 видео): «Decision Trees for Prognosis» · «Dividing the Input Space» · «Building a Decision Tree» · «How to Fix Overfitting» · «Survival Data» · «Different Distributions» · «Missing Data Example» · **«Missing Completely at Random»** · **«Missing at Random»** · **«Missing Not at Random»** · «Imputation» · «Mean Imputation» · «Regression Imputation» · «Calculate Imputed Values»
- **Week 3. Survival Models and Time** (6 ч, 16 видео): «Survival Models» · «Survival Function» · «Valid Survival Functions» · «Collecting Time Data» · **«When a Stroke is Not Observed»** · «Heart Attack Data» · **«Right Censoring»** · «Estimating the Survival Function» · «Died Immediately, or Never Die» · «Somewhere in-between» · «Using Censored Data» · «Chain Rule of Conditional Probability» · «Deriving Survival» · «Calculating Probabilities from the Data» · «Comparing Estimates» · «Kaplan Meier Estimate»
- **Week 4. Build a Risk Model Using Linear and Tree-based Models** (8 ч, 24 видео): «Hazard Functions» · «Hazard» · «Survival to Hazard» · «Cumulative Hazard» · «Individualized Predictions» · «Relative Risk» · «Ranking Patients by Risk» · «Individual vs Baseline Hazard» · «Smoker vs Non-smoker» · «Effect of Age on Hazard» · «Risk Factor Increase Per Unit Increase in a Variable» · «Risk Factor Increase or Decrease» · «Intro to Survival Trees» · «Survival Tree» · «Nelson Aalen Estimator» · «Comparing Risks of Patients» · «Mortality Score» · «Evaluation of Survival Model» · «Permissible and Non-Permissible Pairs» · «Possible Permissible Pairs» · «Example of Harrell's C-Index» · «Example of Concordant Pairs»

#### Курс 3. AI For Medical Treatment (3 недели)

`https://www.coursera.org/learn/ai-for-medical-treatment` — **прочитано 2026-10-14**

- **Week 1. Treatment Effect Estimation** (8 ч, 12 видео): **«Absolute Risk Reduction»** · **«Randomized Control Trials»** · **«Causal Inference»** · «Average Treatment Effect» · «Conditional Average Treatment Effect» · «T-Learner» · «S-Learner» · «Evaluate Individualized Treatment Effect» · **«C-for-benefit»** + «C-for-benefit Calculation»
- **Week 2. Medical Question Answering** (7 ч, 10 видео): «Medical Question Answering» · «Handling Words with Multiple Meanings» · «Define the Answer in a Text» · «Automatic Label Extraction for Medical Imaging» · «Synonyms for Labels» · «Is-a Relationships for Labels» · «Presence or Absence of a Disease» · «Evaluating Label Extraction» · «Precision, Recall and F1 Score» · «Evaluating on Multiple Disease Categories»
- **Week 3. ML Interpretation** (8 ч, 9 видео): «Drop Column Method» · «Permutation Method» · «Individual Feature Importance» · «Shapley Values» · «Combining Importances» · «Shapley Values for all Patients» · «Interpreting CNN Models» · «Localization Maps» · «Heat Maps»

**Итог по A2, он же главный наш довод.** Три курса, 10 недель, 72 часа, 164 видео — и **ни одной учебной единицы про то, что происходит с врачом, когда он видит вывод модели.** Ни якорения на подсказке, ни падения квалификации, ни арбитража спорных случаев, ни измеренной человеко-модельной пары. Ближайшее к клиническому исходу — **«Measuring Patient Outcomes», 3 минуты** в последней неделе первого курса; ближайшее к цене ошибки — «Absolute Risk Reduction» и «C-for-benefit», и это метрики испытания, а не метрики смены. Курс объявляет это сам: он для тех, кто «already familiar with some of the math and coding behind AI algorithms», и «No prior medical expertise is required». Самая известная в мире программа «ИИ для медицины» — **программа для инженеров, в которой врача нет как действующего лица.**

---

## B. edX и университетские курсы

Общая оговорка по методу: страницы edx.org — одностраничные приложения на сценариях, прямое чтение отдаёт только навигацию. Поэтому читались либо снимки Wayback **самих страниц edx.org**, либо официальные страницы университетов. Там, где пришлось опереться на сторонний каталог, это сказано прямо.

### B1. MITx: Machine Learning for Healthcare (6.871Jx)

`http://web.archive.org/web/20230528194750/https://www.edx.org/course/machine-learning-for-healthcare` — **прочитано (архив), снимок 2023-05-28**. На edX помечен «This course is archived».

- Уровень Advanced. Предварительные требования дословно: «6.86x or equivalent machine learning course; 6.00.1x or proficiency in Python programming; 6.431x or equivalent probability theory course; College-level single-variable calculus; Vectors and matrices»
- Объём: 15 недель, 8–12 часов в неделю, по расписанию. Цена: $49 за подтверждённый результат, прослушивание бесплатно. CME нет.

Полный перечень дословно:

**Unit 1: Overview of Clinical Care & Data (2 weeks)** — «Introduction: What Makes Healthcare Unique?» · «Translating Technology Into the Clinic» · «Overview of Clinical Care» · «Deep Dive Into Clinical Data»

**Unit 2: ML for Risk Stratification & Diagnosis (3 weeks)** — «Risk Stratification» · «Survival Modeling» · **«Learning from Noisy Labels»** · **«Detecting and Mitigating Dataset Shift»**

**Unit 3: ML with clinical text, imaging, and physiological data (2 weeks)** — «Guest Lecture on Machine Learning for Pathology» · «Physiological Time-Series» · «Guest Lecture on Machine Learning for Mammography» · «Clinical Natural Language Processing»

**Unit 4: Understanding disease and its progression (2 weeks)** — «Differential Diagnosis» · «Precision Medicine» · «Disease Progression Modeling and Subtyping»

**Unit 5: Human Factors (3 weeks)** — **«Learning to Defer»** · «Guest Lecture on Machine Learning for Cardiology» · «Interpretability» · «Fairness» · «Regulation of ML / AI in the US» · **«Automating Clinical Workflows»**

**Unit 6: Causal Inference & Reinforcement Learning (3 weeks)** — «Causal Inference from Observational Data» · «Off-Policy Reinforcement Learning»

Домашние работы дословно: «Predicting In-hospital Mortality for Intensive Care Unit patients» · «Fundamentals of Learning from Changing Data» · «Fundamentals of Learning from Noisy Labels» · «Identifying and Using Clinical Terms Found in Clinical Notes» · «Deep Learning to De-Identify Clinical Notes» · «Interpreting Deep Models for Chest X-Ray Diagnosis» · **«Fundamentals of Learning to Defer to Human Experts»** · «Fundamentals of Causal Inference from Observational Data»

**Это единственная из 26 прочитанных программ, где раздел целиком называется «Human Factors» — три недели из пятнадцати, то есть 20% курса.** И единственная, где есть и лекция, и **домашняя работа** про передачу решения человеку: «Fundamentals of Learning to Defer to Human Experts». Но жанр надо назвать точно: «Learning to Defer» — это **алгоритмическая** постановка (как обучить модель отказываться от ответа и передавать случай человеку), а не измерение того, что происходит с врачом у подсказки. Чисел про якорение в перечне нет.

### B2. MIT 6.S897/HST.956 Machine Learning for Healthcare (OpenCourseWare, Spring 2019)

`https://ocw.mit.edu/courses/6-s897-machine-learning-for-healthcare-spring-2019/pages/syllabus/` и `.../pages/calendar/` — **прочитано 2026-10-14** (открытый доступ, без помех). Преподаватели: Peter Szolovits, David Sontag. Выпускной уровень, 2 занятия в неделю по 1,5 часа. Оценка: домашние 40% / проекты 40% / участие 20%.

25 занятий дословно: «Introduction: What Makes Healthcare Unique?» · «Overview of Clinical Care» · «Deep Dive into Clinical Data» · «Risk Stratification, Part 1» (обсуждающий Leonard D'Avolio) · «Risk Stratification, Part 2» · «Physiological Time-Series» · «Natural Language Processing (NLP), Part 1» (Katherine Liao) · «NLP, Part 2» · «Translating Technology into the Clinic» (Adam Wright) · «Machine Learning for Cardiology» (Rahul Deo) · «Machine Learning for Differential Diagnosis» · «Machine Learning for Pathology» (Andy Beck) · «Machine Learning for Mammography» (Connie Lehman, Adam Yala) · «Causal Inference, Part 1 / Part 2» · «Reinforcement Learning, Part 1» (Fredrik Johansson) · «Reinforcement Learning, Part 2» (Barbra Dickerman, «Evaluating Dynamic Treatment Strategies») · «Disease Progression & Subtyping, Part 1 / Part 2» · «Precision Medicine» · **«Automating Clinical Workflows»** · «Regulation of ML/AI in the US» (Andy Coravos, «Human Subjects Research»; Mark Shervey) · «Fairness» · «Robustness to Dataset Shift» · «Interpretability»

**Находка сравнением двух версий одного курса.** В версии 2019 года **лекции «Learning to Defer» нет**. Она появилась при переносе на edX. То есть раздел про передачу решения человеку — **позднее приобретение** в самом инженерно-сильном курсе мира по ИИ в медицине: сперва научили строить модели и считать сдвиг данных, а мысль «а когда модель должна отступить» дописали после.

### B3. HBKUx: Applications of AI in Healthcare (Hamad Bin Khalifa University, Катар)

`http://web.archive.org/web/20250216130535/https://www.edx.org/learn/computer-science/hamad-bin-khalifa-university-applications-of-ai-in-healthcare` — **прочитано (архив), снимок 2025-02-16** (на снимке «© 2024»).

Уровень Introductory, без предварительных требований. Кому дословно: «healthcare workers and other non-technical professionals interested in AI applications in healthcare». Подтверждённый результат $119, прослушивание бесплатно.

Девять модулей дословно:

1. **Overview of AI in Clinical Environments** 2. **Automatic Diagnosis of Respiratory Disease With AI** 3. **Automatic Segmentation Analysis of Medical Images** 4. **Automatic Enhancements of Medical Images** 5. **AI in Histology** 6. **AI Mistrust and Explainable AI** 7. **Mental Health and AI** 8. **The Challenges of AI in Healthcare** 9. **The Future of AI in Healthcare**

Что обещают, дословно: «…**Mitigate challenges related to the clinical use of AI, such as AI mistrust, and legal and ethical considerations**.»

По рубрике (ж): модуль 6 называется **«AI Mistrust and Explainable AI»** — и это редкий случай, когда в заголовке стоит **недоверие**, а не чрезмерное доверие. Повёрнуто ровно в обратную сторону от якорения: курс учит, как **преодолеть** недоверие врача к модели, а не как уберечь врача от излишней опоры на неё. Чисел нет.

### B4. MGH Institute of Health Professions: две части (edX, входят в MicroMasters)

Страницы edx.org не отдали тело ни напрямую, ни через архив. Метаданные читались в стороннем каталоге OpenCourser (`https://opencourser.com/course/xsi0ja/introduction-to-ai-machine-learning-in-healthcare` и `.../e4hl3u/advanced-principles-topics-in-ai-machine-learning-in-healthcare`) — **это не страница edX, а сторонний пересказ её каталожных данных; отношу к «перечень из вторичного источника», не к прямому чтению.**

Курс 1 «Introduction to AI & Machine Learning in Healthcare», 5 недель, 2–4 часа на модуль, порог 80%: **Overview of AI and its Impact on Healthcare** · **AI Legal and Ethical Considerations including Privacy Concerns** · **Basics of Data & Healthcare** · **Basic Machine Learning Algorithms** · **Case Studies of AI & ML in Healthcare**

Курс 2 «Advanced Principles & Topics in AI & Machine Learning in Healthcare», 4 недели: **Advanced Machine Learning Techniques** · **Implementation and Operation of AI Systems** · **Evaluating Machine Learning Models** · **Special Topics in AI in Healthcare**

По рубрике (ж): **ни одного модуля.** Ближайшее — «Implementation and Operation of AI Systems», и это про эксплуатацию систем, не про врача.

### B5. KULeuvenX: AI in Healthcare. Hype or Help?

`https://onderwijsaanbod.kuleuven.be/syllabi/e/E0J85A` — **прочитано 2026-10-14** (официальная страница учебного плана KU Leuven, код B-KUL-E0J85A). На ней дословно: «All course materials are available at the edX platform.» Координатор Maarten De Vos, содокладчик Peter Claes. **4 ECTS**, второй семестр. Входит в настоящие дипломные программы: «Master in de specialistische geneeskunde», «Postgraduaat in de acute geneeskunde», «Postgraduaat technologie in de zorg». Входные требования дословно: «There is no specific prior knowledge required for this course.»

Содержание дословно:

> «Welcome to the course» · «Breaking the (A)Ice» · «First AId kit» · «Inside the AI engine. Search problems and optimization» · «Inside the AI engine. Learning from data» · «Inside the AI engine. Artificial Neural Networks» · **«How to coexist with AI»** · «AI in action»

Цели дословно: «Learners can explain the key enabling factors and limitations of AI tools from the past and present, and foresee its growing impact in the future… Learners can identify the added value and risks of AI in healthcare applications… Learners can define healthcare data requirements, and can identify related societal, ethical, and legal regulations… **Learners can critically analyse, question, and embrace the added value of AI in healthcare**.»

Оценка: половина — проверки на платформе (проверки знаний 10%, зачёты по модулям 30%, итоговый экзамен 60%), половина — задание в Toledo.

По рубрике (ж): тема **«How to coexist with AI»** — прямое попадание по названию, одна из восьми. Чисел нет; по устройству оценки (выбор ответа и зачёты) содержание скорее обсуждение, чем измерение. Длительность 10 недель и цена $80 — **по поиску, прямым чтением страницы edX не подтверждено**, помечаю.

### B6. MIT Sloan Executive Education: Artificial Intelligence in Health Care

`https://executive.mit.edu/course/artificial-intelligence-in-health-care/a056g00000URaaTAAT.html` — **прочитано 2026-10-14**. Та же программа идёт и через edX Executive Education (доставка GetSmarter). На день чтения следующий набор — 11.11.2026 – 26.01.2027, и ещё шесть наборов расписаны до 2028 года.

6 недель, 6–8 часов в неделю (4–5 обязательных + 2–3 необязательных). **$3 250.** Сертификат MIT Sloan, зачитывается в Executive Certificate. **CME нет** — это управленческая программа. Кому дословно: «leaders in both business and medical roles… Professionals working for health care providers will learn to identify the types of problems that AI techniques can help solve». Преподаватели: Regina Barzilay, Dimitris Bertsimas, Tommi Jaakkola, Dina Katabi, David Sontag, Collin Stultz.

Модули дословно: **Orientation Module** «Welcome to your Online Campus» · **1** «AI and Machine Learning - Applications and Foundations» · **2** «Using AI for Disease Diagnosis and Patient Mentoring» (в оригинале, по-видимому, опечатка вместо Monitoring) · **3** «Natural Language Processing and Data Analytics in Health Care» · **4** «Interpretability in Machine Learning - Benefits and Challenges» · **5** «Patient Risk Stratification and Augmenting Clinical Workflows» · **6** «Taking an Integrated to Hospital Management and Optimization» (в оригинале пропущено слово Approach)

По рубрике (ж): отдельного модуля нет. Ближайшие — модуль 4 (доверие к модели через прозрачность) и модуль 5 («Augmenting Clinical Workflows»). Регуляторика и этика **отдельными модулями не вынесены вовсе** — это редкость даже среди инженерных программ.

### B7. Harvard Medical School (HMX): AI in Medicine: Foundations and Applications in Medical Practice and Research

`https://learn.hms.harvard.edu/programs/ai-medicine-foundations-and-applications-medical-practice-and-research` — **прочитано 2026-10-14** (прямой запрос упирался в Cloudflare, страница открылась средствами загрузки с разбором). Это собственная платформа HMX медицинского факультета Гарварда, не edX. **$495**, самостоятельный темп. Кому дословно: «Clinicians and health care professionals; researchers in biomedicine and technology sectors; and professionals across health care fields.» На странице указано «3-4 Hours», что не вяжется с одиннадцатью единицами — **расхождение фиксирую, не домысливаю**. CME на странице не упомянуты.

Одиннадцать единиц дословно:

> «Key Technical Concepts in Machine Learning: Supervised Learning» · «Generative Modeling and Self-Supervised Learning for Text Generation» · «Generative Modeling with Diffusion Models for Image Generation» · «Deep Dive: Model Architectures» · **«Pre-market Evaluation of Machine Learning Models»** · «Deep Dive: Evaluation Metrics for Classification Models» · «Applications of AI in Diagnosis» · **«Applications of AI to Improve Clinical Workflows»** · «The Role of AI in Biomedical Research» · **«Post-market Surveillance of Medical AI»** · **«Conversation: Regulatory Aspects of AI in Medicine»**

**По регуляторике это самая насыщенная программа из всех 26: три единицы из одиннадцати** — до выпуска, после выпуска, и отдельный разговор про правовую сторону. Этика и справедливость отдельной единицей **не вынесены** (в описании курса есть общая фраза «discussions of bias and ethics», в перечне единиц — нет). По рубрике (ж) — **ни одной единицы**: ни про доверие, ни про износ навыка, ни про арбитраж.

### B8. Stanford BIODS220: Artificial Intelligence in Healthcare (зачётный курс, не edX)

`https://biods220.stanford.edu/` и `https://biods220.stanford.edu/syllabus` — **прочитано 2026-10-14**. Версия Fall 2022–2023. Ведёт Serena Yeung (она же — преподаватель курса 3 специализации A1). Очно. Требуется Python, математический анализ, линейная алгебра, статистика, знакомство с машинным и желательно глубоким обучением.

14 лекций дословно: «Course Introduction» · «Medical Images: Classification» · (разбор) «Review: Deep Learning Fundamentals» · «Medical Images: Advanced Vision Models (Detection and Segmentation)» · «Medical Images: Advanced Vision Models (3D and Video)» · «Electronic Health Records: Introduction» · «Electronic Health Records: Advanced Topics» · «Electronic Health Records: More on Text Data and Representations» · (гость Gabriel Brat) «Strategies for Interdisciplinary Projects in AI and Healthcare» · «Multimodal Data, Multimodal Models, Weakly and Self-Supervised Learning» · «More on Transformers and Multimodal Models» · «Genomics: Introduction» · «Special Topics: AI for COVID-19» · промежуточный экзамен · «Unsupervised Learning and Reinforcement Learning» · (гость Barbara Engelhardt) лекция по геномике · **«Interpretability, Fairness, and Ethics»** · (гость Jonathan Chen) · «Distributed Learning, Security, and Privacy» · заключение и гостевая лекция Zach Harned, JD · итоговый проект

По рубрике (ж): отдельной лекции нет. Прозрачность, справедливость и этика сведены в **одну** лекцию из четырнадцати.

### B9. Отрицательные находки по разделу B — проверено прямым чтением, а не отсутствием в выдаче

- **Doane University**: курса или сертификата «Artificial Intelligence in Healthcare» от Doane на edX **не существует**. Проверялся сам `doane.edu` (каталог, DoaneX, Health Sciences, Extended Learning) плюс несколько заходов поиска. У Doane есть несвязанный «Thinking and Writing with AI Certificate» на кафедре английского языка — не про медицину. **Задание исходило из того, что такой курс есть; его нет.**
- **UC Berkeley / BerkeleyX**: отдельного курса про ИИ в медицине не найдено ни поиском по `edx.org/school/`, ни общими запросами. Единственный близкий — общий `CS188.1x: Artificial Intelligence` без медицинской направленности.
- **Microsoft «AI for Healthcare Professionals» (edX)**: название в выдаче есть, страницу открыть не удалось ни прямым чтением, ни через архив (запрос снимков вернул пустой список). **Перечень модулей сознательно не приводится** — считаю курс «найден, но не прочитан».
- **Stanford Online «не Coursera»**: такой версии не существует. Официальная страница `online.stanford.edu/programs/artificial-intelligence-healthcare` (прочитана через снимок `http://web.archive.org/web/20251002120517/...`; живая отбивает запрос защитой AWS) сама пишет: «Delivery Methods: **100% Online, on-demand, Coursera**», подписка **$79 в месяц**. То есть витрина Стэнфорда ведёт на ту же специализацию A1.
