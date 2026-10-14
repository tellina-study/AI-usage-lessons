# Аналоги в университетах: ФАКТИЧЕСКИЕ структуры курсов «ИИ в медицине / ML для здравоохранения»

**Назначение файла.** Черновик-разведка для переделки Лекции 7. Задача — не пересказ, а
**дословные перечни лекций** реальных курсов, прочитанные на страницах, а не по памяти,
с URL и датой чтения. Главный вопрос, под который собирался материал: **есть ли в этих курсах
хоть одна лекция про взаимодействие человека и модели** — искажение решения под подсказкой,
якорение, падение квалификации, переезд нагрузки на арбитраж.

**Дата сбора:** 2026-10-14. Все URL открывались в этот день.

**Как читать пометки достоверности:**
- `[ПРОЧИТАНО]` — страница открылась целиком, перечень скопирован с неё.
- `[PDF ПРОЧИТАН]` — PDF скачан и расшифрован локально (PyMuPDF), текст в руках.
- `[ТОЛЬКО СНИППЕТ]` — видно лишь в выдаче поиска, полный текст не открылся. Доверять нельзя.
- Пустая клетка означает «не нашли», а не «нет». Выдуманных названий в файле нет.

---

## Сводная таблица

Рубрики содержания: **(а)** обзор применений · **(б)** устройство моделей/методы ML ·
**(в)** работа с данными · **(г)** регуляторика · **(д)** этика/справедливость ·
**(е)** измеренные клинические исходы и испытания · **(ж)** взаимодействие человека и модели.

Счёт — по числу лекций/модулей, отнесённых к рубрике целиком (смешанные не считаются).
Сначала полная карта всех программ по главному вопросу, затем разложение по рубрикам
для тех курсов, у которых перечень занятий опубликован целиком.

### Полная карта: все 26 прочитанных программ и рубрика «ж»

| § | Курс / программа | Версия | Кому | Лекция про взаимодействие человека и модели |
|---|---|---|---|---|
| 1 | MIT 6.S897/HST.956 | Spring 2019 | EECS + HST | **нет** |
| 2 | MIT 6.871/HST.956 | Spring 2022 | EECS + HST | **да** — «Human-AI interaction» (Mozannar), **без чтения** |
| 3 | MIT 6.7930/HST.956 | Spring 2021 | EECS + HST | **да** — «Cooperative Decision Making», раздел «Human Factors, Integration, & Deployment» |
| 4 | MIT 6.7930/HST.956 | Spring 2023 / 2024 | EECS + HST | **да** — «Human-AI Collaboration in Clinical ML»; в 2024 чтение задано |
| 5 | MIT 6.7930/HST.956 | **Spring 2025** | EECS + HST | **да** — «Human-AI collaboration in decision making»; **чтение закомментировано** |
| 6–7 | Stanford BIODS 220 / CS 271 / BIOMEDIN 220 | Autumn 2020-21, 2022-23 | смешанно, нужен DL | **нет** (проверено по деке лекции по этике: `clinician` = 0 на 57 слайдах) |
| 8 | **AAPM + ACR + RSNA + SIIM**, силлабус для радиологов | **2025** | радиологи, 4 роли | **нет лекции, но ЕСТЬ пункт** «Risks of automation bias and methods of mitigation» + «Asymmetric costs of different error types» |
| 9 | MIT HST.953 / 6.8850 | Fall 2024 | **2/3–3/4 медики** (HMS, HSPH) | **нет** |
| 9 | MIT HST.953 | Fall 2018, Fall 2020 | смешанно | **нет** |
| 10 | MIT Critical Data, дататоны + учебник (30 глав) | 2014–2019, 2016 | смешанно | **нет** (программы дататонов не публикуются вовсе) |
| 11 | Harvard BMI 702 (Zitnik) | Spring 2024 | магистранты HMS | **нет** |
| 11 | Harvard AIM 2 = BMIF 203 / BMI 702 | **Spring 2026** | PhD-трек AIM | **нет** («Human-AI evaluation loops» — один пункт внутри занятия по NLP) |
| 11 | Harvard BMIF 202 «AI in Medicine I» | Fall 2026 | семинар HMS | **плана нет** — пустая клетка, не отрицание |
| 11 | Harvard BMIF 204 | — | PhD-трек AIM | **нет** |
| 12 | ETH Zürich 261-5120-00L | **Spring 2026** | только инженеры | **нет** (план опубликован на 7 недель из 14) |
| 13 | Technion 336546 (BME) | силлабус 2022 | биоинженеры | **нет** |
| 14 | Technion 97248 (Shalit, иврит) | Spring 2023/24 | магистры-технари | **плана нет**; но лучшая цель «когда не надо» |
| 15 | TU München IN2403 | версия 21W, действует 2025W | информатики | **нет** |
| 16 | Imperial College 70014 | без даты | информатики | **нет** |
| 17 | Karolinska 2QA338 | действует с осени 2022 | **медики И инженеры** | **нет**; но есть «Medical image analysis without AI» |
| 18 | NUS MDG5256 и др. | **2025-2026** | медики | **плана нет**; но цель — «safety and efficiency of clinician-AI interactions» |
| 19 | Toronto LMP1210 | Winter 2024 | **Health Sciences** | **нет**; но есть предупреждение о чрезмерном доверии — про студентов |
| 20 | UCL CHME0035 (+ перечни модулей) | снимок 2026 | Health Data Science | **нет**; UCL перечней занятий не публикует по устройству |
| 21 | University of Arizona, «AI, AI literacy and Medicine» | март 2024 | **старшекурсники-медики** | **нет** |
| 22 | Stanford «AI in Healthcare», Coursera (5 курсов) | 2023, 97 392 чел. | провайдеры + информатики | **нет модуля**; 1 видео 5 мин «Death by GPS and Other Lessons of Automation Bias» |
| 23a | JHU Bloomberg, каталог (15 курсов по ИИ) | **2026-27** | общественное здоровье | **нет** — 0 вхождений по всему каталогу |
| 23b–e | JHU Coursera · EP EN.705.617 · Malone · ExecEd | 2025–2026 | смешанно | **нет** |
| 23f | **JHU + Great Learning «AI and Agentic AI in Healthcare»** | набор 2026 | без требований | **ДА, единственная с модулем про переезд нагрузки** — «WEEK 10: CHANGE MANAGEMENT AND THE SHIFT TO AGENT SUPERVISION» |
| 24 | Michigan DATA-MD | 2024, CME | **врачи, ординаторы, медсёстры** | **нет модуля**; 4 коротких позиции (2–8 мин) |
| 25 | DeepLearning.AI «AI for Medicine» (3 курса) | без даты | инженеры | **нет** — 0 по всем шаблонам |
| 26 | Сеченов, ДПО «Специалист по ИИ в медицине», 256 ч | **2025/26** | медики | **нет**; «Этические аспекты и роль человека» — 6 ч из 256, содержание не раскрыто |
| 27 | Сеченов, магистратура 09.04.02 | набор 2020 | технари | **нет** |
| 28 | ВШЭ, «Большие данные и МО в медицине» | 2023/24 | технари | **нет** |
| 29 | ВШЭ, «Информационно-аналитические технологии в здравоохранении» | 2024 и 2025 | **управленцы, медики** | **нет** |
| 30 | ВШЭ, «Анализ данных в биологии и медицине» | 2026/27 | смешанно | **нет** |
| 31 | ВШЭ, «Управление и экономика здравоохранения» | 2026/27 | управленцы | **нет** |
| 32 | ИТМО, «Биоинформатика и системная биология» | набор 2026 | смешанно | медицинской **нет**; общий «Культура ИИ» |

### Разложение по рубрикам — там, где перечень занятий полный

| Курс | Лекций | а обзор | б методы ML | в данные | г регуляторика | д этика/справедливость | е измеренные исходы | **ж человек и модель** |
|---|---|---|---|---|---|---|---|---|
| MIT 6.S897, 2019 | 25 | 4 | 13 | 3 | 1 | 2 | 0 | **0** |
| MIT 6.871, 2022 | 24 | 3 | 12 | 2 | 1 | 2 | 1 | **1** (4%) |
| MIT 6.7930, 2021 | 23 | 3 | 12 | 2 | 1 | 1 | 0 | **1** |
| MIT 6.7930, 2025 | 25 | 4 | 11 | 2 | 1 | 2 | 1 | **1** (4%) |
| Stanford BIODS 220, 2022-23 | 14 | 2 | 9 | 1–2 | 0 | 1 | 0 | **0** |
| MIT HST.953, 2024 | ~20 | 3 | 6 | 5 | 1 | 2 | 0 | **0** |
| Harvard BMI 702, 2024 | 14 | 2 | 9 | 1 | 1 (нед. 12) | 1 (нед. 5) | 0 | **0** |
| Harvard AIM 2, 2026 | 13 | 1 | 9 | 1 | 1 (нед. 12) | 1 (нед. 7) | 0 | **0** |
| TU München IN2403 | 14 | 2 | 9 | 2 | 0 | 1 | 0 | **0** |
| Technion 336546 | 26 | 1 | 23 | 2 | 0 | 0 | 0 | **0** |
| Toronto LMP1210 | 12 | 2 | 9 | 0 | 0 | 0 | 0 | **0** |
| Karolinska 2QA338 | 4 модуля | 1 | 2 | 0 | 0,5 | 0,5 | 0 | **0** |
| Сеченов ДПО (часы) | 256 ч | 12 ч | 92 ч | 38 ч | 0 | **6 ч** | 0 | **0** |
| ВШЭ Medical Informatics | 13 | 4 | 4 | 4 | 0 | 0 | 0 | **0** |
| ВШЭ Инф.-аналит. технологии | 15 | 6 | 2 | 3 | 1 | 0 | 0 | **0** |

**Главный счёт по таблице:** из 26 программ **рубрика «ж» есть у трёх** — MIT MLHC (одна
лекция из 24–25, то есть около 4% курса, и только для информатиков), профессиональный
силлабус радиологов (один пункт программы, без лекции) и сертификат JHU + Great Learning
(одна неделя из десяти, подана как управление изменениями).
**Рубрика «е» — измеренные клинические исходы и испытания — почти везде нулевая.** Курсы учат
**строить** модель и **оценивать её метрики**, а не **читать отчёт о том, что вышло в клинике**.



---

## 1. MIT 6.S897 / HST.956 «Machine Learning for Healthcare», Spring 2019

**Прочитанные страницы** (все `[ПРОЧИТАНО]`, 2026-10-14):
- силлабус: https://ocw.mit.edu/courses/6-s897-machine-learning-for-healthcare-spring-2019/pages/syllabus/
- расписание: https://ocw.mit.edu/courses/6-s897-machine-learning-for-healthcare-spring-2019/pages/calendar/
- конспекты: https://ocw.mit.edu/courses/6-s897-machine-learning-for-healthcare-spring-2019/pages/lecture-notes/
- литература: https://ocw.mit.edu/courses/6-s897-machine-learning-for-healthcare-spring-2019/pages/readings/
- зеркало курса: https://mlhc19mit.github.io/

**Версия:** Spring 2019. **Читают:** Peter Szolovits, David Sontag.
**Кому:** магистранты и аспиранты EECS (Electrical Engineering and Computer Science) и
HST (Health Sciences and Technology) — то есть **смешанная аудитория инженеров и медиков**.
**Требования:** «at least an undergraduate level of machine learning», закрывается курсами
6.036, 6.862, 6.867 «or similar offerings in machine learning, statistical learning, NLP,
or artificial intelligence».
**Оценка:** Homework 40%, Course Projects 40%, Participation 20%.

### Полный перечень лекций (дословно, со страницы Lecture Notes)

| № | Название (дословно) |
|---|---|
| 1 | Introduction: What Makes Healthcare Unique? |
| 2 | Overview of Clinical Care |
| 3 | Deep Dive into Clinical Data |
| 4 | Risk Stratification, Part 1 |
| 5 | Risk Stratification, Part 2 |
| 6 | Physiological Time-Series |
| 7 | Natural Language Processing (NLP), Part 1 |
| 8 | Natural Language Processing (NLP), Part 2 |
| 9 | Translating Technology into the Clinic |
| 10 | Machine Learning for Cardiology |
| 11 | Machine Learning for Differential Diagnosis |
| 12 | Machine Learning for Pathology |
| 13 | Machine Learning for Mammography |
| 14 | Causal Inference, Part 1 |
| 15 | Causal Inference, Part 2 |
| 16 | Reinforcement Learning |
| 17 | Evaluating Dynamic Treatment Strategies |
| 18 | Disease Progression & Subtyping, Part 1 |
| 19 | Disease Progression & Subtyping, Part 2 |
| 20 | Precision Medicine |
| 21 | Automating Clinical Workflows |
| 22.1 | Regulation of ML/AI in the US |
| 22.2 | Human Subjects Research |
| 23 | Fairness |
| 24 | Robustness to Dataset Shift |
| 25 | Interpretability |

Приглашённые (из календаря): Leonard D'Avolio (4), Katherine Liao (7), Adam Wright (9),
Rahul Deo (10), Andy Beck (12), Connie Lehman + Adam Yala (13), Fredrik Johansson (16),
Barbra Dickerman (17), Andy Coravos + Mark Shervey (22).

### На чём стоит содержание

- **(б) устройство моделей и методы — 13 лекций** (4–8, 14–20, 24–25): стратификация риска,
  временные ряды, NLP, причинный вывод, обучение с подкреплением, модели прогрессирования,
  устойчивость к сдвигу, интерпретируемость. Это больше половины курса.
- **(а) обзор применений — 4** (10–13: кардиология, дифдиагноз, патология, маммография).
- **(в) данные — 3** (2, 3, частично 21).
- **(г) регуляторика — 1** (22.1 + 22.2).
- **(д) этика/справедливость — 2** (23 Fairness, 22.2 Human Subjects Research).
- **(е) измеренные клинические исходы — 0 отдельных лекций.** Ближайшее — лекция 9
  «Translating Technology into the Clinic», но у неё в обязательном чтении ничего нет,
  а в необязательном — опыт Veterans Health Administration и «Clinical Decision Support
  for Early Recognition of Sepsis».
- **(ж) взаимодействие человека и модели — 0. Лекции про это НЕТ.**

### Обязательное чтение

Reading list опубликован целиком и разложен по занятиям (обязательное + необязательное).
**Работ про automation bias, deskilling, human-AI team performance в нём нет ни одной.**
Проверено по полному списку. Самое близкое:
- Caruana et al., «Intelligible Models for HealthCare» (KDD 2015) — занятие 5, необязательно;
- Amland & Hahn-Cover, «Clinical Decision Support for Early Recognition of Sepsis» — занятие 9,
  необязательно;
- Oakden-Rayner, «Exploring the ChestXray14 Dataset: Problems» — занятие 12, необязательно
  (про качество разметки, не про человека рядом с моделью);
- Gawande, «A Life-Saving Checklist» (The New Yorker) — занятие 21, необязательно.
  Единственный текст курса про поведение людей в клинике — и он публицистический.

**Проверка отрицания сделана сплошным поиском, а не на доверии к пересказу.** Я скачал
страницу литературы целиком (1728 слов, около шестидесяти работ) и прогнал по ней поиск
по словам. Числа точные:

| Искомое | Вхождений в полном списке литературы курса |
|---|---|
| `automation bias` | **0** |
| `deskill` / `skill` (любая форма) | **0** |
| `reliance` / `over-reliance` | **0** |
| `human-AI` | **0** |
| `human factor` | **0** |
| `alert fatigue` | **0** |
| `trust` | **0** |
| `workload` | **0** |
| `workflow` | **0** |
| `collaborat` | **0** |
| `adoption` | **0** |
| `second opinion` | **0** |
| `physician` | **0** |
| `anchor` | 1 — и это **«Anchor and Learn Framework»**, приём разметки, а не якорение решения |
| `clinician` | 2 — и **оба раза это название модели**, не человек |

**Последняя строка таблицы — находка, которую стоит произнести со сцены.** В списке литературы
курса-эталона MIT 2019 слово «врач» (`clinician`) встречается дважды, и оба вхождения — это
заголовок работы Komorowski, Celi et al., «**The Artificial Intelligence Clinician** learns
optimal treatment strategies for sepsis in intensive care» (Nature Medicine, 2018) и отклик
на неё. То есть на шестьдесят работ курса про машинное обучение в здравоохранении слово «врач»
приходится ровно два раза — и оба раза **врачом назван алгоритм**. Живого врача в списке
литературы нет.

**Это важная находка.** Курс-эталон 2019 года, с которого списаны почти все остальные,
про взаимодействие человека и модели не говорит вообще.

---

## 2. MIT 6.871 / HST.956, Spring 2022 — рубрика «ж» появляется

**Прочитано:** https://mlhcmit.github.io/2022/index.html `[ПРОЧИТАНО]` 2026-10-14.

**Читают:** David Sontag, Madhur Nayan. Ассистенты: Zeshan Hussain, Intae Moon.
**Уровень:** graduate, 4-0-8 единиц; зачитывается как AUS2, AAGS, II subject; EECS AI TQE.
**Требования:** 6.036/6.862 или 6.867, или 9.520/6.860, или 6.806/6.864, или 6.438, или 6.034.
**Обязательные рецитации** по пятницам — разборы статей и погружение в медицинские данные.

### Полный перечень (дословно, по разделам курса)

**Unit 1: Overview of Clinical Care & Data**
| № | Дата | Название |
|---|---|---|
| 1 | Tue, Feb 1 | Introduction: What makes healthcare unique? |
| 2 | Thu, Feb 3 | Overview of Clinical Care |
| 3 | Tue, Feb 8 | Overview of Clinical Data Science |

**Unit 2: ML with Clinical Text, Imaging, Physiological, and Administrative Data**
| № | Дата | Название | Приглашённый |
|---|---|---|---|
| 4 | Thu, Feb 10 | Risk Stratification from Structured Health Data | — |
| 5 | Tue, Feb 15 | Physiological Time-Series | — |
| 6 | Thu, Feb 17 | Intro to Clinical NLP | Monica Agrawal |
| 7 | Thu, Feb 24 | Clinical NLP for oncology & AI-driven documentation | Kenneth Kehl (DFCI), Monica Agrawal |
| 8 | Tue, Mar 1 | Intro to ML for medical imaging: algorithms & mammography | Adam Yala |
| 9 | Thu, Mar 3 | ML for pathology | Andy Beck, MD/PhD (PathAI CEO) |

**Unit 3: Causal Inference**
| № | Дата | Название |
|---|---|---|
| 10 | Tue, Mar 8 | Causal graphs, potential outcomes, covariate adjustment |
| 11 | Thu, Mar 10 | Assumptions for causal inference, inverse propensity weighting |
| 12 | Tue, Mar 15 | Policy learning, sensitivity analysis, instrumental variables |
| 13 | Thu, Mar 17 | Dataset shift |

**Unit 4: Methods for ML in Healthcare**
| № | Дата | Название | Приглашённый |
|---|---|---|---|
| 14 | Tue, Mar 29 | Critical appraisal of applying ML in healthcare | — |
| 15 | Thu, Mar 31 | Weak supervision & learning from noisy labels | — |
| 16 | Tue, Apr 5 | Survival modeling | — |
| 17 | Thu, Apr 7 | Fairness | Irene Chen |
| 18 | Tue, Apr 12 | Interpretability | — |
| 19 | Thu, Apr 14 | **Human-AI interaction** | **Hussein Mozannar** |
| 20 | Tue, Apr 19 | Disease subtyping & progression modeling | — |
| 21 | Thu, Apr 21 | Privacy | Fei Wang (Weill Cornell Medicine) |

**Unit 5: Off-policy Reinforcement Learning & Regulation**
| № | Дата | Название | Приглашённый |
|---|---|---|---|
| 22 | Tue, Apr 26 | Intro to off-policy reinforcement learning and dynamic treatment regimes | — |
| 23 | Thu, Apr 28 | *(название в таблице не указано)* | Susan Murphy (Harvard) |
| 24 | Tue, May 3 | Regulation of AI in healthcare | — |
| 25 | Thu, May 5 | Project poster session |
| 26 | Tue, May 10 | Final exam review |

### Рубрика «ж»

**Есть: занятие 19, «Human-AI interaction», читает Hussein Mozannar.** Одна лекция из 24
содержательных — около **4% курса**.

Отдельно стоит занятие 14 «Critical appraisal of applying ML in healthcare» с обязательным
чтением **TRIPOD-AI и PROBAST-AI** (руководства по отчётности и оценке риска смещения
в прогностических моделях) — это ближе всего к «как читать отчёт о модели», но не про человека
рядом с ней.

**Отдельная находка про чтение к этой лекции.** В итерации 2022 у занятия 19
«Human-AI interaction» в таблице стоят **только слайды и НИ ОДНОЙ работы** — ни обязательной,
ни необязательной (проверено по разметке строки: `slides/lecture19_human_AI_interaction.pdf`
и пустые клетки чтения, тогда как у соседних занятий 14, 17, 18 чтение прописано). Работа
Tschandl появляется в этой лекции только к итерации 2024. То есть лекция про человека рядом
с моделью три года держалась **без единого обязательного текста** — при том что у лекции
про справедливость обязательное чтение было с самого начала.

Для сверки, чтение соседних занятий 2022 (дословно):
- занятие 14 «Critical appraisal of applying ML in healthcare» — обязательно: «Protocol for
  development of a reporting guideline (TRIPOD-AI) and risk of bias tool (PROBAST-AI)»
  (BMJ Open 11(7):e048008);
- занятие 17 «Fairness» — обязательно: «Dissecting racial bias in an algorithm used to manage
  the health of populations» (Science); необязательно: «Fairness and Machine Learning:
  Limitations and Opportunities» (fairmlbook.org);
- занятие 18 «Interpretability» — необязательно: Molnar, «Interpretable Machine Learning»;
- занятие 24 «Regulation of AI in healthcare» — необязательно: «Butterfly rescinds features
  from handheld ultrasound device, working with FDA to re-enable» (MobiHealthNews).

Обязательное чтение к занятию 17 (Fairness): «Dissecting racial bias in an algorithm used to
manage health of populations» (Obermeyer et al.) — это **измеренный провал внедрённой модели
на 200 млн человек**, полезный пример для нас, но про смещение данных, а не про смещение
решения врача.

---

## 3. MIT 6.7930 / HST.956, Spring 2021 — целый раздел «Human Factors»

**Прочитано:** https://mlhcmit.github.io/2021/index.html `[ПРОЧИТАНО]` 2026-10-14.

Единственная из прочитанных итераций, где человеческий фактор вынесен в **название раздела**:

**Unit 4: Human Factors, Integration, & Deployment**
| № | Дата | Название |
|---|---|---|
| 13 | Tuesday Apr 6 | **Cooperative Decision Making** |
| 14 | Thursday Apr 8 | Interpretability |
| 15 | Tuesday Apr 13 | Fairness |
| 16 | Thursday Apr 15 | Guest Lectures: Regulation (FDA) |
| 17 | Thursday Apr 22 | Guest Lectures: Deployment (Viz.ai) |

Полный перечень остальных разделов (дословно):
**Unit 1: Overview of Clinical Care & Data** — 1 Introduction: What makes healthcare unique?;
2 Overview of Clinical Care; 3 Deep Dive into Clinical Data.
**Unit 2: ML for Risk Stratification & Diagnosis** — 4 Differential Diagnosis;
5 Risk Stratification; 6 Learning with Noisy and Censored Labels (survival modeling);
7 Guest Lecture: Prof. Jenna Wiens (UMich); 8 Detecting & Mitigating Dataset Shift.
**Unit 3: ML with Clinical Text, Imaging, & Physiological Data** — 9 Physiological Time-Series;
10 Clinical NLP Part 1; 11 Clinical NLP Part 2; 12 Imaging.
**Unit 5: Causal Inference & Reinforcement Learning** — 18 Causal inference: potential outcomes
& covariate adjustment; 19 Causal inference: matching, propensity scores; 20 Guest lecture
(Noa Dagan and Noam Barda, Clalit Health Services); 21 Dynamic treatment regimes & off-policy
reinforcement learning.
**Unit 6: Understanding Disease and its Progression** — 22 Precision Medicine;
23 Disease Progression Modeling.
Далее 24–25 Presentations #1/#2, Final Exam (Monday May 24).

**Рубрика «ж»:** занятие 13 «Cooperative Decision Making» — и сама рамка «Human Factors,
Integration, & Deployment» как раздел. Это самая сильная по нашей рубрике итерация **по
структуре**, хотя содержательно (см. §5) материал в 2025-м богаче.

---

## 4. MIT 6.7930 / HST.956, Spring 2024

**Прочитано:** https://mlhcmit.github.io/2024/index.html `[ПРОЧИТАНО, выборочно по рубрике «ж»]`
2026-10-14. Полную таблицу по этой итерации я не выписывал — она близка к 2025-й.

Относящаяся к делу строка, дословно:

> **17 | Thu, Apr 11 | Human-AI Collaboration in Clinical ML; guest lecture by Hussein Mozannar**
> Reading: *Human-computer collaboration for skin cancer recognition*

Та же работа Tschandl и тот же лектор, что в 2022 и 2025. Линия устойчивая, не разовая.

Для полноты: в итерации **Spring 2023** (https://mlhcmit.github.io/2023/index.html,
`[ПРОЧИТАНО, выборочно]`) та же лекция стоит под номером **11, Thu, Mar 16 —
«Human-AI Collaboration in Clinical ML»**.

---

## 5. MIT 6.7930 / HST.956, Spring 2025 — самая свежая прочитанная итерация

**Прочитано:** https://mlhcmit.github.io/ `[ПРОЧИТАНО целиком, включая весь список чтения]`
2026-10-14.

**Читают:** Peter Szolovits, David Sontag.
**Требования:** один из курсов 6.3900, 6.7900, 9.520/6.7910, 6.8611/6.8610, 6.4102/6.4100
или равноценный.

### Полный перечень лекций с обязательным чтением (дословно)

| № | Дата | Лекция | Обязательное чтение |
|---|---|---|---|
| 1 | Tue, Feb 4 | Introduction: What makes healthcare unique? | AI in health and medicine |
| 2 | Thu, Feb 6 | Overview of Clinical Care | Machine Learning in Medicine |
| 3 | Tue, Feb 11 | Overview of Clinical Data Science | — |
| 4 | Thu, Feb 13 | ML for Risk Stratification: focus on structured EMR data | **Factors Driving Provider Adoption of the TREWS Machine Learning-Based Early Warning System and its Effects on Sepsis Treatment Timing** |
| 5 | Thu, Feb 20 | Risk Stratification and Physiological Time-Series (в этот же слот — «Cautionary Tales; Discussion of Project Ideas», гость Dr. Leo Anthony Celi, BIDMC & IMES-LCP) | Constrained transformer network for ECG signal processing and arrhythmia classification |
| 6 | Tue, Feb 25 | LLMs 1: differential diagnosis, question answering, treatment planning | Towards Expert-Level Medical Question Answering with Large Language Models |
| 7 | Thu, Feb 27 | LLMs 2: information extraction and summarization | Retrieval-Augmented Generation–Enabled GPT-4 for Clinical Trial Screening; **необязательно: Manual vs AI-Assisted Prescreening for Trial Eligibility Using Large Language Models — A Randomized Clinical Trial** |
| 8 | Tue, Mar 4 | Guest Lecture by Leo Celi: From AI Bias to AI by Us, For All of Us | ClinicalBERT: Modeling Clinical Notes and Predicting Hospital Readmission |
| 9 | Thu, Mar 6 | Survival Analysis, Censoring, Proportional Hazard Models | Deep Cox Mixtures for Survival Regression |
| 10 | Tue, Mar 11 | Causal inference 1: Causal graphs, potential outcomes, covariate adjustment | Using Big Data to Emulate a Target Trial When a Randomized Trial Is Not Available |
| 11 | Thu, Mar 13 | Causal inference 2: Assumptions for causal inference, inverse propensity weighting | Use of Machine Learning to Assess the Management of Uncomplicated Urinary Tract Infection |
| 12 | Tue, Mar 18 | Causal inference 3: Policy learning and dynamic treatment regimes | Guideline-Based Physical Activity and Survival Among US Men With Nonmetastatic Prostate Cancer |
| 13 | Thu, Mar 20 | Dataset and temporal shift: detection and mitigation | Large-Scale Study of Temporal Shift in Health Insurance Claims |
| 14 | Tue, Apr 1 | Multi-modal modeling of text and imaging data | Learning Transferable Visual Models From Natural Language Supervision |
| 15 | Thu, Apr 3 | Guest lecture: Faisal Mahmood (Computational Pathology) | A multimodal generative AI copilot for human pathology |
| 16 | Tue, Apr 8 | Interpretability & explainability | Interpretable Machine Learning (Molnar), главы 5 и 9 |
| 17 | Thu, Apr 10 | Regulation of AI in healthcare | Skating the Line Between General Wellness Products and Regulated Devices |
| 18 | Tue, Apr 15 | **Human-AI collaboration in decision making** | **чтение ЗАКОММЕНТИРОВАНО в разметке — в 2025 не задавалось** (см. ниже) |
| 19 | Thu, Apr 17 | Fireside chat with Brian Anderson (CEO of Coalition for Health AI) | A Nationwide Network of Health AI Assurance Laboratories; The CHAI Applied Model Card |
| 20 | Tue, Apr 22 | Privacy: differential privacy, federated learning, synthetic data | Federated learning for predicting clinical outcomes in patients with COVID-19 |
| 21 | Thu, Apr 24 | Guest lecture: Nathan Silberman (CTO, Artera AI) | необязательно: Are Open Source Pathology Foundation Models ready for the clinic?; Discrepancy Ratio: Evaluating Model Performance When Even Experts Disagree on the Truth |
| 22 | Tue, Apr 29 | Disease subtyping & progression modeling | Cluster Analysis and Clinical Asthma Phenotypes |
| 23 | Thu, May 1 | Guest Lecture: Marzyeh Ghassemi (The Pulse Of Ethical Machine Learning) | Ethical machine learning in healthcare |
| 24 | Tue, May 6 | Guest Lecture: Jim Collins (Machine Learning Approaches to Antibiotic Discovery) | A Deep Learning Approach to Drug Discovery |
| 25 | Thu, May 8 | Guest Lecture: Manolis Kellis | Good Machine Learning Practice for Medical Device Development: Guiding Principles |
| 26 | Tue, May 13 | Student Project Presentations | — |
| — | Fri, May 16 | Final Exam | — |

### Три работы из этого списка, которые прямо относятся к нашей рубрике «ж»

1. **Занятие 4, обязательное чтение:** «Factors Driving Provider Adoption of the TREWS
   Machine Learning-Based Early Warning System and its Effects on Sepsis Treatment Timing».
   Это **измеренное внедрение**: что заставляет врача принять подсказку системы раннего
   предупреждения и как это сдвинуло время начала лечения сепсиса. Стоит не в лекции про
   человека и модель, а в лекции про стратификацию риска.
2. **Занятие 7, необязательное:** «Manual vs AI-Assisted Prescreening for Trial Eligibility
   Using Large Language Models — A Randomized Clinical Trial». **Рандомизированное испытание
   на переезд нагрузки**: ручной отбор против отбора с моделью.
3. **Занятие 18 — и тут поправка, которую я внёс после сплошной проверки разметки.**
   Работа Tschandl et al., «Human–computer collaboration for skin cancer recognition»
   (Nature Medicine 26.8 (2020): 1229–1234) в версии 2025 года **в разметке страницы
   закомментирована** — лежит внутри `<!-- Reading: … -->` и студентам не задаётся.
   Проверено по исходному HTML, не по отрисованной странице.

   **Хронология этой лекции по итерациям — её стоит прочесть целиком, она говорящая:**
   - **2022** (занятие 19, «Human-AI interaction», Mozannar) — чтения нет вовсе, только слайды;
   - **2023** (занятие 11) — только слайды;
   - **2024** (занятие 17, гость Mozannar) — Tschandl **задан по-настоящему**, ссылка живая;
   - **2025** (занятие 18) — Tschandl **закомментирован**, то есть чтение убрали обратно.

   Итого: за четыре итерации лекция про человека рядом с моделью имела обязательное чтение
   **один раз**. У лекции про справедливость обязательное чтение было во все годы. Это не
   придирка к вёрстке: обязательное чтение — единственное, что в этом курсе заставляет
   студента прочесть первоисточник, и именно у этой темы его чаще всего нет.

---

## 5a. Что именно читают на лекции 18 (разбор слайдов)

Это самый ценный фрагмент всей разведки: **дека лекции открыта и расшифрована целиком**,
51 слайд.

**URL:** https://mlhcmit.github.io/slides/lecture18_Human-AI%20interaction.pdf
`[PDF ПРОЧИТАН]` 2026-10-14 (3,7 МБ, 51 слайд; расшифрован локально PyMuPDF — WebFetch
не смог, вернул бинарный поток).

На титуле дека подписана иначе, чем в расписании: **«Lecture 17: Human-AI Collaboration in
Healthcare», David Sontag, "Acknowledgement: slides adopted from Hussein Mozannar"**.

### Структура лекции (дословно со слайда 4)

> **Today's Lecture**
> 1. How do we combine humans and AI? • Modes of human-AI interaction
> 2. How do people think about AI? • Mental Models
> 3. How do we interact with generative AI? • AI-assisted reading and writing

### Ход разбора и измеренные числа

**Заход через задачу.** Ателектаз по рентгену грудной клетки: модель ResNet-34 на CheXpert
(>200 тыс. снимков), тест — 500 снимков, разметка по большинству из 5 радиологов, сверка
с 3 другими. **Модель AUC = 0,91, обходит всех трёх радиологов** (Rad1 0,21/0,80;
Rad2 0,18/0,71; Rad3 0,31/0,92). Дальше ставится вопрос слайда 9: *«How do we integrate the
AI into the current pipeline?»*

**Разбор 1 — диабетическая ретинопатия, Таиланд.** Модель снижает долю пропусков (FNR)
на 23%, но повышает ложные тревоги (FPR) на 2% (Ruamviboonsuk et al., NPJ Digital Medicine
2019). Внедрение: **8 площадок, 1,5 года, 7600 пациентов, 200 пациентов в день, 5 часов
ожидания, 90 секунд на осмотр глаза.** Проспективное наблюдение — Beede et al., CHI 2020.

**Результат внедрения (слайд 14) — это измеренный переезд нагрузки:**
- модель **отказалась давать ответ на 20% снимков** — нечитаемые для неё;
- причины: плохое освещение, старые камеры, мало времени на позиционирование пациента;
- слова медсестёр, дословно: *«Some images are blurry, and I can still read it, but the system
  can't»*, *«it's good but I think it's not as accurate. If [the eye] is a little obscured,
  it can't grade it»*;
- **и главное:** те, чей снимок не прошёл, **теперь должны были ехать к офтальмологу**, вместо
  того чтобы просто дождаться прочтения снимка на месте.

Вывод слайда 15, дословно: *«Eliminating the ophthalmologists from the system removes safety
checks against model failure (e.g., distribution shift) and input issues»* и *«Can do better
by combining model and ophthalmologists then each alone!»*

**Разбор 2 — передача решения (deferral / learning to defer).** Слайды 16–24: система
«отклонитель» r(X) выбирает между моделью m(X) и врачом h(Z). Показан провал наивного
подхода: если порог ставить только по уверенности модели, **внутри области передачи модель
делает 3 ошибки, а человек — 5** (слайд 17), то есть передавать человеку бессмысленно.
Работы: Raghu, Blumer, Corrado, Kleinberg, Obermeyer, Mullainathan, «The Algorithmic
Automation Problem: Prediction, Triage, and Human Effort» (2019); Mozannar & Sontag,
«Consistent Estimators for Learning to Defer to an Expert» (ICML 2020); Mozannar et al.,
«Who Should Predict? Exact Algorithms For Learning to Defer to Humans» (AISTATS 2023).

**Разбор 3 — модель как второе мнение, рак кожи (Tschandl et al., Nature Medicine 2020).**
Это главный измеренный случай лекции:
- **155 оценивающих**, каждый классифицировал 28 случайных изображений в одну из 7 категорий;
- точность и **время** измерялись сначала **без** модели, затем **с** подсказкой и объяснением;
- **форма объяснения решает всё** (слайд 28): многоклассовые вероятности дали
  **+13,3% точности и −1 секунду времени**; похожие изображения дали **~0% прироста точности
  и +10 секунд времени**. То есть одна из двух форм подсказки — чистый проигрыш: время
  потратили, точность не выросла;
- **зависимость от опыта (слайд 29), дословно:** *«Inexperienced raters benefit hugely from
  the regular AI, but are harmed the most from a bad AI model. Experienced rater benefit the
  least from regular AI, and are harmed the Least by a bad AI model. The difference is how
  sound their mental model of the AI is.»*

**Часть 2 — мысленные модели.** Определение (слайд 32), два пути складывания: через опыт и через
«onboarding». Разбор Cai et al., «"Hello AI": uncovering the onboarding needs of medical
practitioners for human-AI collaborative decision-making» (CSCW 2019): **21 патолог**, задача
про риск рака простаты, замер до / во время / после. Что патологи хотят знать о модели:
объём и разнообразие обучающих данных, доступные модели модальности (*«Does the AI assistant
have access to information that I don't have?»*), шаги анализа, источник эталона, **фаза
калибровки человека и модели на пограничных случаях** (*«I know what my friend... will
call… what would AI call it?... I'm treating it as a peer»*), точность **по подкатегориям
известных человеческих ловушек** (*«Maybe it has really good accuracy except for perineural
invasion. If you see perineural invasion… Don't fall for that»*). Инструменты: Data Cards,
Model Cards. Плюс Mozannar et al., «Effective Human-AI Teams via Learned Natural Language
Rules and Onboarding» (NeurIPS 2024) — правила на естественном языке вида *«Rely on the AI
for patients under the age of 40»*, *«Ignore on the AI whenever x-ray shows a pigtail
catheters»*, *«Rely on AI whenever AI score is above 95%»*.

Слайд 42 ставит вопрос дословно: *«What can happen if people have inaccurate mental models?»*

**Часть 3 — порождающие модели.**
- Чтение клинических записей пациентом с помощью GPT-4 (Mannhardt, Bondi-Kelly, Lam,
  O'Connell, Asiedu, Mozannar, … Sontag, 2024, arXiv:2401.09637): **n = 200**, участники
  отвечали на вопросы по записи с интерфейсом и без. **На 20% точнее с интерфейсом** — и тут же,
  дословно: *«However, GPT-4 definitions and answers often contained serious errors!»*
- Черновики ответов пациентам (Garcia et al., «Artificial Intelligence–Generated Draft Replies
  to Patient Inbox Messages», JAMA Network Open 7.3 (2024): e243201): **врачи использовали
  20% черновиков.**
- Слайд 49 — «Guidelines for Human AI Interaction» Microsoft, 18 правил по четырём фазам
  (INITIALLY / DURING INTERACTION / WHEN WRONG / OVER TIME).

### Итоги лекции (дословно, слайды 50–51)

> • Figure out what mode of Human-AI interaction is appropriate for your problem
> • Human's mental model of the AI determines the success of the system
> • Design onboarding stages to allow the human to form an accurate mental model of the AI
> • **Design AI and AI explanations with human in mind to avoid over-reliance**
> • **Allow for updates over time to interface and model to avoid under-reliance**
> • Integrate and evaluate LLMs to help patients/clinicians in their tasks

### Чего в этой лекции НЕТ (важно для нас)

Притом что это **лучшая найденная лекция по рубрике «ж» во всей разведке**, в ней нет:
- **слова и темы «падение квалификации» / deskilling / skill decay** — ни одного слайда.
  Опыт входит только как модификатор сиюминутной выгоды от подсказки (слайд 29), а не как
  величина, которая со временем меняется;
- **измеренного случая, где пара «человек + модель» хуже каждой стороны по отдельности.**
  Ближайшее — слайд 17 (внутри области передачи человек ошибается чаще модели) и слайд 29
  (новички страдают от плохой модели сильнее всех). Но прямого «пара хуже обоих» нет;
- **якорения на подсказке как названного искажения** — вместо него работает понятие
  «мысленная модель» и пара «over-reliance / under-reliance» в выводах. Механизм назван,
  но как ошибка проектирования интерфейса, а не как искажение решения человека;
- **цены обеих ошибок в одних единицах.** Ложные тревоги и пропуски обсуждаются
  (FNR −23% против FPR +2%), но в одну денежную или временную шкалу не сводятся;
- **переезд нагрузки назван, но один раз и не посчитан:** 20% отказов модели и поездка
  к офтальмологу — это качественное наблюдение из статьи CHI, без арифметики
  «сколько человеко-часов переехало куда».

---

## 6–7. Stanford BIODS 220 / CS 271 / BIOMEDIN 220 «Artificial Intelligence in Healthcare»

**Прочитанные страницы** (`[ПРОЧИТАНО]`, 2026-10-14):
- действующий сайт (Fall 2022-2023): http://biods220.stanford.edu/ и
  https://biods220.stanford.edu/syllabus.html
- архив Autumn 2020-21: https://web.stanford.edu/class/archive/biods/biods220/biods220.1204/syllabus.html
- архив Autumn 2022-23: https://web.stanford.edu/class/archive/biods/biods220/biods220.1232/syllabus.html
- каталог Stanford ExploreCourses (XML API, `view=xml-20200810`): курс значится как
  **«Artificial Intelligence in Healthcare (BIOMEDIN 220, CS 271)», 2024-2025 Autumn, 3 единицы**;
  в выдаче за **2025-2026 BIODS 220 отсутствует** — в этом году на месте профильного курса
  Serena Yeung значится «Advanced Topics in Computer Vision and Biomedicine» (CS 286 / BMDS 276).

**Читает:** Serena Yeung. Ассистенты (2022-23): Jeffrey Gu, Ali Mottaghi, Yuhui Zhang.
**Кому:** смешанная аудитория («students from diverse backgrounds»), но планка техническая.
**Требования (дословно):** владение Python «or significant experience with a different
programming language and ability to self-learn»; матанализ (Math 19/41), линейная алгебра
(Math 51 или EE 103/CME 103), вероятность и статистика (CME 106 или CS 109); знакомство
с машинным обучением и опыт обучения модели; **«Familiarity with deep learning is highly
recommended»**.

### Autumn 2022-23, полный перечень (дословно, включая гостей и секции)

| Тип | Дата | Название |
|---|---|---|
| Lecture 1 | Sep 26 (Mon) | Course Introduction |
| Lecture 2 | Sep 28 (Wed) | Medical Images: Classification |
| Section | Sep 30 (Fri) | Review: Deep Learning Fundamentals |
| Lecture 3 | Oct 3 (Mon) | Medical Images: Advanced Vision Models (Detection and Segmentation) |
| Lecture 4 | Oct 5 (Wed) | Medical Images: Advanced Vision Models (3D and Video) |
| Section | Oct 7 (Fri) | Numpy/TensorFlow Review Session |
| Lecture 5 | Oct 10 (Mon) | Electronic Health Records: Introduction |
| Lecture 6 | Oct 12 (Wed) | Electronic Health Records: Advanced Topics |
| Lecture 7 | Oct 17 (Mon) | Electronic Health Records: More on Text Data and Representations |
| Guest Speaker | Oct 19 (Wed) | Strategies for Interdisciplinary Projects in AI and Healthcare: Dr Gabriel Brat |
| Lecture 8 | Oct 24 (Mon) | Multimodal Data, Multimodal Models, Weakly and Self-Supervised Learning |
| Lecture 9 | Oct 26 (Wed) | More on Transformers and Multimodal Models |
| Lecture 10 | Oct 31 (Mon) | Genomics: Introduction |
| Lecture 11 | Nov 2 (Wed) | Special Topics: AI for COVID-19 |
| Midterm | Nov 7 (Mon) | Midterm Exam |
| Lecture 12 | Nov 9 (Wed) | Unsupervised Learning and Reinforcement Learning |
| Guest Speaker | Nov 14 (Mon) | Genomics Guest Lecture: Dr. Barbara Engelhardt |
| Lecture 13 | Nov 16 (Wed) | Interpretability, Fairness, and Ethics |
| Guest Speaker | Nov 28 (Mon) | Guest Lecture: Dr. Jonathan Chen |
| Lecture 14 | Nov 30 (Wed) | Distributed Learning, Security, and Privacy |
| Conclusion | Dec 5 (Mon) | Course Conclusion and Guest Lecture: Zach Harned, JD (Zoom) |
| Project | Dec 14 (Wed) | Poster Session |

### Autumn 2020-21, полный перечень (дословно)

1 Course Introduction · 2 Deep Learning Fundamentals · 3 Medical Images: Classification ·
4 Medical Images: Advanced Vision Models (Detection and Segmentation) · 5 Medical Images:
Advanced Vision Models (3D and Video) · 6 Electronic Health Records: Introduction ·
7 Electronic Health Records: Advanced Topics · 8 More on Text Data and Representations ·
9 Genomics: Introduction · 10 Multimodal Data, Multimodal Models, and Weakly Supervised
Learning · 11 Special Topics: AI for COVID-19 · 12 Unsupervised Learning and Reinforcement
Learning · 13 Interpretability, Fairness, and Ethics · 14 Distributed Learning, Security,
and Privacy.

### На чём стоит содержание

- **(б) методы — 9 из 14** (2–4, 8–9, 12 и фундаменты): классификация, детекция, сегментация,
  3D/видео, трансформеры, многомодальность, слабый и самонадзорный режим, обучение
  с подкреплением. Курс по существу — **прикладной курс глубокого обучения на медицинских
  данных**.
- **(в) данные — 1–2** (5–7 про электронные медицинские записи, с уклоном в модели).
- **(а) обзор применений — 2** (10 геномика, 11 COVID-19).
- **(д) этика/справедливость — 1** (13, и там же интерпретируемость — то есть одна лекция
  на три больших темы сразу).
- **(г) регуляторика — 0 лекций.** Правовая тема заходит один раз гостем в последний день:
  **Zach Harned, JD**.
- **(е) измеренные клинические исходы — 0.**
- **(ж) взаимодействие человека и модели — 0. Лекции про это НЕТ ни в одной из двух
  прочитанных итераций.**

### Обязательное чтение

В таблице силлабуса есть столбец **«Suggested Readings»** — то есть чтение **рекомендованное,
а не обязательное**, и в прочитанной версии страницы он не заполнен содержательно.
Работ про automation bias, deskilling, human-AI team performance в силлабусе **не обнаружено**.
Оговорка о достоверности: столбец мог заполняться по ходу курса в закрытой части (Canvas),
поэтому точная формулировка — «на открытой странице силлабуса таких работ нет», а не
«их не читали никогда».

Отдельно: материалы лекций лежат открыто (`lecture1.pdf` … `lecture14.pdf` по пути
https://web.stanford.edu/class/biods220/lectures/), слайды Autumn 2021-22 — отдельной
ссылкой со страницы силлабуса.

---

## 7a. Проверка Стэнфорда по существу: вскрыта дека единственной «этической» лекции

Утверждение «у Стэнфорда рубрики „ж“ нет» я не оставил на уровне чтения расписания, а проверил
по содержанию — потому что единственное место, где тема могла бы спрятаться без упоминания
в названии, это лекция 13 «Interpretability, Fairness, and Ethics».

**Прочитано:** https://web.stanford.edu/class/biods220/lectures/lecture13.pdf
`[PDF ПРОЧИТАН]` 2026-10-14 (3,9 МБ, **57 слайдов**, расшифрован локально PyMuPDF).

Поиск по полному тексту деки. Числа точные:

| Искомое | Вхождений |
|---|---|
| `trust` | **5** |
| `automation bias` | 0 |
| `deskill` / `skill` (в любой форме) | **0** |
| `reliance` / `over-reliance` / `over-relian` | **0** |
| `human-AI` / `human AI` | **0** |
| `clinician` | **0** |
| `workflow` | **0** |
| `workload` | **0** |
| `anchor` (якорение) | **0** |
| `complacen` | 0 |
| `second opinion` | 0 |
| `reader study` | 0 |

**И самое существенное — на что потрачены эти пять вхождений `trust`.** Все пять сидят в одном
повторяющемся слайде, который дословно называется:

> **«When can we trust the model?»**
> – Notion of uncertainty: models can be more or less confident about a given prediction. Model
> confidences are also sometimes more trustworthy than at other times. Interpretability and
> explainability of the model gives indications of how the model arrived at its conclusion.
> – Notion of robustness: models may behave differently under different settings (e.g. shift in
> the distribution of patient population / data). We may not be able to trust the model's outputs
> in the same way under some of these. Can we quantify how the model may perform under different
> settings, and make it «robust» under different settings that we care about?

**Это ровно та подмена, которую нам стоит показать в Лекции 7.** Вопрос «когда можно доверять
модели» задан — но он целиком про **свойство модели**: её калибровку, её устойчивость, сдвиг
распределения. Слово «врач» (`clinician`) в деке про этику и доверие не встречается **ни разу**.
Вопрос «что делает человек, когда модель права, и что он делает, когда она неправа» не задан.
Доверие разобрано как метрика модели, а не как поведение пары.

Слово `clinician` = 0 на 57 слайдах лекции по этике прикладного ИИ в здравоохранении — это
не придирка к формулировке, это и есть устройство курса.

---

## 8. Профессиональный силлабус: AAPM + ACR + RSNA + SIIM, «Teaching AI for Radiology Applications», 2025

Это не университетский курс, а **согласованный силлабус четырёх профессиональных обществ**
(Американская ассоциация физиков в медицине, Американская коллегия радиологии, Радиологическое
общество Северной Америки, Общество информатики в медицинской визуализации). Для нас он ценнее
многих университетских курсов по двум причинам: он свежий (2025) и он **единственный
найденный документ, где и «искажение решения под подсказкой», и «несимметричная цена разных
ошибок» названы отдельными пунктами программы**.

**Прочитано:** полный текст через Europe PMC `[ПРОЧИТАНО целиком, 6196 слов]`, 2026-10-14:
https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13481610/fullTextXML
(статья: PMC13481610, DOI 10.1007/s10278-025-01485-8, Journal of Imaging Informatics
in Medicine, © The Author(s) 2025, лицензия CC BY 4.0).
Та же работа напечатана параллельно в Medical Physics (DOI 10.1002/mp.17779, PMC12485864)
и в Radiology: Artificial Intelligence (DOI 10.1148/ryai.250137 — там закрыто).
Оговорка: страница Springer (https://link.springer.com/article/10.1007/s10278-025-01485-8)
через WebFetch отдала переадресацию на вход, поэтому читался открытый экземпляр в PMC.

**Первый автор:** Felipe Kitamura; последний — Neil Tenenholtz. Среди авторов — Linda Moy,
Roxana Daneshjou, Judy Gichoya, Keith Dreyer, Matt Lungren, Charles E. Kahn Jr., Maryellen Giger.

**Устройство документа.** Вместо одного перечня лекций — **четыре роли (personas)**, у каждой
своя программа:
1. **User** — «Interacts with AI Algorithms in Their Clinical Workflow»;
2. **Purchaser / Clinical Owner** — «Makes purchasing decisions and is responsible for deployed
   algorithms»;
3. **Physician Collaborator** — «Works alongside model developers to define and evaluate
   algorithms»;
4. **Developer** — «Creates new AI algorithms to improve patient care and/or clinical workflows».

### Полная программа роли «User» (дословно, приложение)

- **Properties of AI algorithms**
  - Complexity, nonlinearity, and frequent opacity of AI algorithms
  - Algorithm outputs that mirror the training distribution
- **Using AI algorithms effectively**
  - Identification of approved regulatory claims and the implications of supplying data from
    alternative workflows
  - Differentiating between model predictions and information derived from these predictions
  - Evaluating AI output in the context of patient history
- **Limitations of AI**
  - Lack transparency in their predictions
  - Inheritance of biases from training datasets
  - Unpredictable, nonhuman failure modes
  - Potential brittleness with out-of-distribution data, including unseen scanners, protocols,
    and patient populations
- **Safe use of AI**
  - Inclusion criteria for algorithm use
  - Identification of failure modes
  - **Risks of workflow modification**
  - **Risks of automation bias and methods of mitigation**
- **Importance of user feedback**
  - Communication of feedback on algorithm performance
  - Identification of opportunities for improvement
  - Participation in initiatives (e.g., national registries) to share experiences and insights

### Полная программа роли «Purchaser / Clinical Owner» (дословно)

- **Pre-engagement Product / Vendor Evaluation:** Metrics of assessment (including measures of
  bias) · Review of data used for training and evaluation · FDA AI/ML Action Plan
- **Pre-deployment Site Compatibility / Suitability Evaluation:** Integration into the clinical
  workflow (standard vs bespoke integration) · Interoperability of the AI software and
  associated standards · Need for explainability or interpretability of AI results · Platform
  requirements · Hardware requirements (CPU, GPU, memory, storage) · On-premise vs cloud
  deployments · Data security / privacy · Data Use Agreements · **Training users in appropriate
  use** · **Established definition of errors and subjective difference in opinion**
- **Pre-deployment Performance Evaluation:** Testing with local datasets for early detection of
  failure modes · Shadow/canary deployment with acceptance criteria · Evaluation on relevant
  patient population and clinical environment · Detection of potential biases in observed results
- **Post-deployment Monitoring / Evaluation:** Collection and evaluation of user feedback ·
  Sources of data drift and their impact (Scanners · Protocols · Patient Population · Collection
  process) · Concept drift · Monitoring to ensure appropriate access and detect potential
  intrusions · Execution of backup strategy as part of a broader disaster recovery plan
- **Model Value Assessment:** Vendor billing models · Provider billing models ·
  **Quantitative measures of improvements in efficiency** · Alternate revenue streams / discounts

### Полная программа роли «Physician Collaborator» (дословно)

- **Use Case Definition:** Evaluation of the proposed task for relevance and value · Assessment
  of model output for ease of user consumption · **Identification and communication of workflow
  nuances, especially if they may introduce bias** · Identification of risks of off-label use
- **Dataset Curation:** Evaluation of tradeoffs in annotation techniques and label types ·
  Assessment and communication of data quality · Label fidelity · Inter-rater variability ·
  Potential for hidden biases
- **Model Evaluation:** Performance metrics · Communication of user experience and potential
  improvements · **Identification of different types of failure modes (e.g., uncorrelated
  errors, mimics, etc.) and their implications** · Bias / fairness evaluation · Alpha-testing
  of early clinical implementations

### Полная программа роли «Developer» (дословно)

- **Problem Identification:** Knowledge of the clinical imaging workflow (from ordering of
  imaging to impact of interpretation on treatment) · Identification of clinical pain points ·
  Clinical IT infrastructure, environment, and imaging volume · Potential integration methods in
  existing workflows and their tradeoffs (**Introduction of novel workflows** ·
  **Augmentation of existing workflows** · **Replacement of existing workflows**)
- **Understanding the Data:** Medical imaging formats and transfer protocols (e.g., DICOM, HL7,
  FHIR) · Physical interpretation of pixel/voxel intensities in different modalities and/or
  series · Significance of pixel/voxel size, anisotropy, acquisition parameters, and other
  imaging properties · Privacy and data safety requirements (e.g., HIPAA, GDPR, etc.)
- **Model Evaluation / Utility Analysis:** **Asymmetric costs of different error types** ·
  Clinical evaluation of ROI · Relevance of interpretability / explainability
- **Algorithm Deployment:** Nascent deployment standards · Hardware availability on-premise and
  in the cloud · Methods of logging and monitoring · Security requirements
- **AI Regulation:** Requirements of the relevant regulatory bodies (FDA, CE, etc.) ·
  Differences between the various classes of risk / device classes · Limitations of regulatory
  approval/clearance

### Замер по рубрике «ж» — и что именно отсутствует

Я прогнал по полному тексту (6196 слов) поиск по словам. Числа точные:

| Искомое | Вхождений | Где |
|---|---|---|
| `automation bias` | **2** | пункт программы «Risks of automation bias and methods of mitigation» (роль User) + абзац введения про «distinctly non-human failure modes» |
| `Asymmetric` | **1** | «Asymmetric costs of different error types» (роль Developer) |
| `workflow modification` | 1 | «Risks of workflow modification» (роль User) |
| `trust` | 2 | **только в списке литературы** (Kitamura & Marques, «Trustworthiness of AI Models in Radiology…», JACR 2021) |
| `deskill` / `de-skill` | **0** | — |
| `skill` (в любой форме, включая «skill decay», «atrophy») | **0** | — |
| `complacen` (утрата бдительности) | **0** | — |
| `over-reliance` / `overreliance` / `under-reliance` | **0** | — |
| `anchor` (якорение) | **0** | — |
| `workload` (нагрузка) | **0** | — |
| `human factors` | **0** | — |
| `vigilan` (бдительность) | **0** | — |
| `burnout` | **0** | — |

**Вывод по этому документу — он для нас самый полезный и самый показательный одновременно.**
Четыре профессиональных общества в 2025 году согласовали программу обучения радиологов работе
с ИИ, и в ней:
- **есть** «искажение решения под подсказкой» — названо, с требованием знать способы
  противодействия;
- **есть** «несимметричная цена разных типов ошибок» — ровно та рубрика, которую мы ищем
  («цена обеих ошибок в одних единицах»), но она отнесена к **разработчику**, а не к врачу,
  который этой моделью пользуется;
- **есть** «риски изменения порядка работы» и три режима встраивания (новый порядок /
  усиление существующего / замена существующего) — то есть переезд нагрузки назван
  **структурно**, но ни разу не количественно (`workload` — ноль вхождений);
- **нет ни единого упоминания квалификации** — ни «deskilling», ни «skill», ни «atrophy»,
  ни «complacency». Слово «навык» в программе обучения навыкам не встречается ни разу.

Отдельно: в списке литературы есть Guo, Zhou, Xu, Huang, Yu, Lu, «Deep Learning for Chest
X-Ray Diagnosis: Competition between Radiologists with or without Artificial Intelligence
Assistance», Journal of Imaging Informatics in Medicine 37(3): 922–934 (2024) — сравнение
радиологов с подсказкой и без. Это единственная в документе работа с замером пары
«человек + модель».

---

## 8a. Сверка центрального измеренного случая курсов MIT с первоисточником

Работа Tschandl et al. — **единственный измеренный случай пары «человек + модель», который
читают во всех итерациях MIT с 2022 по 2025**. Поэтому её вывод стоит привести дословно,
а не по слайду.

**Прочитано:** реферат через Europe PMC `[ПРОЧИТАНО]` 2026-10-14
(PMID 32572267, DOI 10.1038/s41591-020-0942-0; сама статья на nature.com закрыта — WebFetch
отдал переадресацию на вход, поэтому брался реферат из Europe PMC).

Дословно из реферата:

> «We find that **good quality AI-based support of clinical decision-making improves diagnostic
> accuracy over that of either AI or physicians alone**, and that **the least experienced
> clinicians gain the most** from AI-based support. We further find that AI-based multiclass
> probabilities outperformed content-based image retrieval (CBIR) representations of AI in the
> mobile technology environment… In addition to demonstrating the potential benefits associated
> with good quality AI in the hands of non-expert clinicians, **we find that faulty AI can
> mislead the entire spectrum of clinicians, including experts**.»

**Что из этого следует для нашей Лекции 7 — и это ключевая развилка.**

Главный вывод работы — **пара лучше каждой стороны по отдельности**. То есть измеренный
случай, который преподаётся в лучшем из найденных курсов, подтверждает дополнительность,
а не её провал. Провал в этой работе один и он другого рода: **плохая модель сбивает всех,
включая экспертов.**

Значит, случай «пара человек + модель хуже каждой стороны при исправной модели»
в учебную программу MIT **не входит** — ни как кейс, ни как возможность. Курс учит, что
подсказка либо помогает (исправная модель), либо вредит (неисправная модель). Третий исход —
исправная модель, грамотный врач, и всё равно пара хуже — в программе отсутствует.
Это и есть наш содержательный зазор, а не просто недостающая лекция.

## 8b. Две работы из обязательного чтения MIT 2025, которые нам прямо пригодятся

Это уже не про устройство курсов, а про материал, который курсы **дают читать**. Выписываю,
потому что обе — измеренные внедрения с числами, а обе стоят **не** в лекции про человека
и модель.

### TREWS — измеренное внедрение системы раннего предупреждения о сепсисе

Обязательное чтение к занятию 4 (стратификация риска по структурированным данным).
Henry et al., «Factors driving provider adoption of the TREWS machine learning-based early
warning system and its effects on sepsis treatment timing», **Nature Medicine, 2022**,
DOI 10.1038/s41591-022-01895-z. `[РЕФЕРАТ ПРОЧИТАН]` через Europe PMC, 2026-10-14.

Числа из реферата, дословно по смыслу:
- **5 больниц, 2 года**, 9805 ретроспективно выявленных случаев сепсиса;
- чувствительность **82%** (столько случаев система нашла);
- **89% всех срабатываний были рассмотрены** врачом или фельдшером расширенной практики;
- **38% рассмотренных срабатываний врач подтвердил**;
- у пациентов, чьё срабатывание врач подтвердил **в течение 3 часов**, время до первого
  назначения антибиотика сократилось на **1,85 часа** (95% ДИ 1,66–2,00) против тех, чьё
  срабатывание отклонили, подтвердили позже 3 часов или не тронули вовсе;
- врачи приёмного отделения и те, **кто уже имел дело со срабатываниями раньше**, чаще
  взаимодействовали с подсказкой и чаще её подтверждали.

Вывод авторов, дословно: «**Beyond efforts to improve the performance of early warning
systems, efforts to improve adoption are essential to their clinical impact** and should focus
on understanding providers' knowledge of, experience with and attitudes toward such systems.»

**Почему это для нас важно.** Вот измеренная цена поведения человека: 89% рассмотрено, 38%
подтверждено — то есть **почти две трети рассмотренных срабатываний врач отклонил**, и именно
подтверждение (а не само срабатывание) даёт 1,85 часа выигрыша. Это ровно то, чего нет
в лекции про взаимодействие: там разбирают форму подсказки, а здесь измерена доля, в которой
подсказку вообще принимают. При этом работа стоит в лекции про методы стратификации риска.

### Рандомизированное испытание на переезд нагрузки при отборе в испытание

Необязательное чтение к занятию 7 (LLM: извлечение и сжатие информации).
Unlu, Varugheese, Shin, … Blood, «Manual vs AI-Assisted Prescreening for Trial Eligibility
Using Large Language Models — A Randomized Clinical Trial», **JAMA 2025;333(12):1084–1087**,
DOI 10.1001/jama.2024.28047, PMID 39960745, PMCID PMC11833652.
`[БИБЛИОГРАФИЯ И АННОТАЦИЯ ДЛЯ ПАЦИЕНТОВ ПРОЧИТАНЫ]` через PubMed efetch, 2026-10-14.

Аннотация для неспециалистов, дословно: «This randomized clinical trial compares the
**efficiency** of prescreening patients with heart failure using an artificial intelligence
(AI) large language model for inclusion in a clinical trial vs manual prescreening.»

**Оговорка о достоверности:** полные числа испытания я НЕ извлёк. Europe PMC отдал ошибку 500
на полный текст, а `pmc.ncbi.nlm.nih.gov` отвечает заглушкой проверки браузера
(«Checking your browser before accessing pmc.ncbi.nlm.nih.gov») на автоматический запрос.
Работа открытая (PMCID есть) — числа достаются вручную, это стоит дочитать отдельно, если
кейс пойдёт в деку. Группа авторов — Mass General Brigham / Brigham and Women's / Harvard
Medical School, то есть не лабораторная симуляция, а испытание в работающей клинике.

---

## 9. MIT HST.953 / 6.8850 «Clinical Data Learning, Visualization, and Deployments», Fall 2024

**Главная причина включить этот курс в разведку:** это **парный к MLHC курс для медиков**, и он
читается той же школой. Сравнение двух курсов одного сообщества даёт самый сильный вывод всего
файла (см. §13).

**Прочитано** (`[ПРОЧИТАНО]`, 2026-10-14):
- https://ocw.mit.edu/courses/hst-953-clinical-data-learning-visualization-and-deployments-fall-2024/
- `.../pages/syllabus/` · `.../pages/calendar/` · `.../pages/readings/` ·
  `.../pages/instructor-insights/` · `.../pages/selected-lecture-slides/`
- каталог MIT: http://student.mit.edu/catalog/mHSTb.html
- список курсов HST: https://hst.mit.edu/academic-programs/courses

**Номер:** HST.953 = **6.8850[J]** (старые номера 6.S897/6.S982 отменены). 3-0-9.
**Читают:** L. Celi, M. Ghassemi, J. Maley, E. Gottlieb.
**Требование:** `(6.7900 and 6.7930) or permission of instructor` — то есть **MLHC числится
предварительным курсом для HST.953**.

**Состав слушателей — это важно.** Из «Instructor Insights», дословно: 93 студента;
«Two-thirds to three-quarters of the enrolled students were HST students from Harvard Medical
School or were studying at Harvard's T.H. Chan School of Public Health; the remainder were MIT
graduate students». То есть **две трети — три четверти аудитории это медики и специалисты
по общественному здоровью**, остальные — инженеры MIT. Зеркальное отражение MLHC.

Из силлабуса, дословно: «HST.953 is not intended to teach graduate machine learning or
visualization skills to students, and we expect that students will have some working knowledge
of both». Обязательно: подготовка по работе с людьми как субъектами исследования + доступ
к MIMIC-III и eICU-CRD.

### Полный перечень занятий (дословно; курс публикует докладчиков, а не названия — оставлено как есть)

**Раздел «Dataset Creation»**
- Неделя 1 — Marzyeh Ghassemi, «Ethical Machine Learning in Health» / Course Staff, «Course
  Overview» / Catherine Bielick, «The Problems in Healthcare»
- Неделя 2 — Mohammad Mamdani on Challenges of Implementation / Adam Rodman on Project
  Implementation / Jack Gallifant on Ethical Considerations in Data Collection and Use
- Неделя 3 — Lecture by Adam Rodman and Jack Gallifant *(опубликованная дека этой недели
  называется «LLMs in Healthcare»)*

**Раздел «Machine Learning/Visualization»**
- Неделя 4 — Adam Rodman, «Representation Learning in ML and Health» / Takashi and Rodrigo
  on TRIPOD-AI exercise
- Неделя 5 — Adam Rodman on Model Evaluation: Health System / Tom Pollard on Data Sharing
- Неделя 6 — Matthew McDermott on Model Evaluation: Machine Learning Perspective / Leo Anthony
  Celi on HASTE Policy Camp

**Раздел «Implementation»**
- Неделя 7 — Jim Smit on Causal Machine Learning / Shalmali Joshi on Causal Machine Learning
- Неделя 8 — Leo Celi / Liam McCoy / Midpoint presentation
- Неделя 9 — Amol Verma and Gabe Brat / Team work on projects
- Неделя 10 — Heather Mattie / Ned McCague *(дека недели 10 называется «Data Infrastructure»)*
- Неделя 11 — Charlotta Lindvall / Thomas Souneck
- Неделя 12 — Leo Anthony Celi on Haste Policy Camp (дважды)
- Неделя 13 — Project work week
- Неделя 14 — Final presentations

**Лекция про взаимодействие человека и модели: НЕТ.** Ни одного занятия и ни одного
докладчика по искажению решения, якорению, падению квалификации или переезду нагрузки.

### Обязательное чтение (есть, недели 1–12) и его проверка по нашим рубрикам

Полный список прочитан. Результат по шести искомым темам:
**automation bias — нет. Падение квалификации / skill decay — нет. Измеренная работа пары
человек+модель — нет. Чрезмерное доверие врача к выводу модели — нет. Усталость от
оповещений — нет. Переезд нагрузки как названная тема — нет.**

Три ближайших позиции:
- неделя 9 — **Atul Gawande, «Why Doctors Hate Their Computers»** (The New Yorker, 05.11.2018).
  Единственный текст курса про нагрузку на врача — и он публицистический, как и Gawande
  в курсе MLHC 2019;
- неделя 6 — «**Clinician-in-the-Loop Decision Making: Reinforcement Learning with Near-Optimal
  Set-Valued Policies**» — несмотря на название, это методическая работа про множественные
  стратегии в обучении с подкреплением, а не исследование человеческого фактора;
- неделя 8 — «**The Clinician and Dataset Shift in Artificial Intelligence**».

Прочие недели (дословно): нед. 1 — «A Review of Challenges and Opportunities in Machine
Learning for Health», «Ethical Machine Learning in Healthcare», «Do No Harm: A Roadmap for
Responsible Machine Learning for Health Care»; нед. 2 — «MIMIC-III, a Freely Accessible
Critical Care Database», «Reproducibility in Machine Learning for Health Research: Still
a Ways to Go»; нед. 3 — «Recurrent Neural Networks for Multivariate Time Series with Missing
Values», «Making the Most of Text Semantics to Improve Biomedical Vision–Language Processing»,
«Multimodal Fusion with Deep Neural Networks for Leveraging CT Imaging and Electronic Health
Record»; нед. 4 — «Data-Driven Healthcare: Challenges and Opportunities for Interactive
Visualization», «CarePre: An Intelligent Clinical Decision Assistance System», «PhenoLines»,
«An Algorithmic Approach to Reducing Unexplained Pain Disparities in Underserved Populations»;
нед. 5 — «Generating High-Fidelity Synthetic Patient Data…», «Synthetic Data–Anonymisation
Groundhog Day»; нед. 7 — «Interpretable Operations Research for High-Stakes Decisions…»,
«Evaluation of Machine Learning Solutions in Medicine», «**Problems in the Deployment of
Machine-Learned Models in Health Care**», «Implementing Machine Learning in Medicine»;
нед. 10 — «What Artificial Intelligence Means for Health Care», «Revolutionizing Healthcare…»,
«AI Is Already Reshaping Care. Here's What It Means for Doctors»; нед. 12 — «Explainable
Artificial Intelligence in Breast Cancer Detection…», «The Ethical Issues of the Application
of Artificial Intelligence in Healthcare», «Artificial Intelligence in Health Care: A Report
From the National Academy of Medicine».

### Находка внутри деки недели 3 — измеренный переезд нагрузки, поданный как «смешанные результаты»

**Прочитано:** `[PDF ПРОЧИТАН, 33 слайда]`
https://ocw.mit.edu/courses/hst-953-clinical-data-learning-visualization-and-deployments-fall-2024/mithst_953_f24__lec03_slides_rodman.pdf

Дека называется «LLMs in Healthcare». В ней — ровно те числа, которые нам нужны, дословно:
- слайд 19: «Writing notes is the second most time-consuming medical task · Pajama time is
  rampant – full time clinical physicians spend an average of **2.8 hours per unscheduled
  day**… Earliest LLM intervention is "ambient listening"… **However, early data suggests that
  they do not save much time largely due to hallucinations**»;
- слайд 22: «Physicians spend **~1 hour a day** responding to portal messages pre-pandemic,
  with increase of **> 60%**… **Technology has been widely implemented across the US, but early
  data does not show considerable time savings and may even take more time.**»;
- слайд 23, «Patient Communication – Mixed Results»: «Randomized QI study of **122 physicians**
  with AI drafted replies. **Read time was 21.8% higher in LLM group, reply time unchanged,
  and length 17.9% higher.**» Источники: Tai-Seale et al., JAMA Netw Open 2024;7(4):e246565;
  Chen, Guevara, … Bitterman, Lancet Digit Health 2024.

**И вот главное про эту деку.** Сплошной поиск по всем 33 слайдам по словам
`automation bias | deskill | skill decay | over-reliance | anchor | alert fatigue | arbitrat |
workload | human-AI | cognitive | trust` дал **ноль совпадений**. То есть измеренный рост
времени на чтение на 21,8% в деке **есть**, а понятия, под которое его можно подвести, — нет.
Материал подан как «смешанные результаты внедрения», а не как закон поведения пары.
**Это и есть то, что мы в Лекции 7 должны сделать иначе:** не добавить числа (они уже у всех),
а дать им имя и единицу измерения.

### Курс закрывается

Из «Instructor Insights», прямая речь Leo Celi: «**Sadly, the 2024 instance of HST.953 is
likely the last time we will offer the course, as it has been supplanted by a new IMES course
on AI in healthcare.**» Там же: «HST.953 was offered most fall semesters from 2016 through
2024». Подтверждение: в списке курсов HST значится «[HST.953 Collaborative Data Science in
Medicine - not offered Fall 2026]».

Вероятные преемники (из каталога MIT) — **HST.016/HST.017 «Artificial Intelligence in Health
Care I»** (лето 2026, C. M. Stultz) и **HST.018/HST.019 «Artificial Intelligence in Health
Care II»** (IAP/зима 2027, добавляется M. Ghassemi). Из описания HST.016, дословно: «Specific
topics include: deep learning for clinical risk stratification, explaining complex machine
learning models, bias and fairness in clinical machine learning, large language models, and
Generative Pretrained Transformers (GPT models). **No background in AI or machine learning is
required.**» Перечня занятий по неделям для них **не опубликовано**.
**Оговорка:** что именно эти курсы и есть названный Celi «new IMES course» — это вывод
по совпадению, ни один источник их так не называет. Помечено как предположение, не как факт.

Отдельно: **HST.956 (MLHC) тоже не читается весной 2026** — «[HST.956J Machine Learning for
Healthcare - not offered spring 2026]» (https://hst.mit.edu/academic-programs/courses).

### Более ранние версии HST.953

**Fall 2018, «Collaborative Data Science in Medicine»** — `[PDF ПРОЧИТАН, 6 страниц]`:
https://edge.edx.org/asset-v1:MITx+HST.953+2T2018+type@asset+block@HST953_2018_Syllabus___Schedule.pdf
Требования, дословно: «There are no prerequisites for this course other than permission from
a director… However, for **other students, R competency is mandatory**. Students with
biomedical backgrounds are encouraged to attend.» Учебник — «Secondary Analysis of Health
Records», бесплатно у Springer.
Полный план (дословно, `TL` — обычная лекция, `WS` — практикум, `GL` — приглашённая лекция):
нед. 1 Course Introduction (John Halamka) / Overview of MIMIC, eICU (TL, Alistair Johnson) /
Project Pitches (GL); нед. 2 MIMIC III / eICU-CRD Approval + Google Cloud Platform Setup (WS) /
Survey of Tools (WS) / Data Visualization (WS); нед. 3 Reproducibility (WS) / Vital Signs and
Labs (WS) / Exploratory Data Analysis (WS); нед. 4 Formulate a Research Question (TL) /
Clinical Outcomes and Mechanical Ventilation (WS) / Project Mentoring; нед. 5 Pre-processing
(Missing data/Noise) (TL) / Input and Output (WS) / Natural Language Processing (WS);
нед. 6 Google Brain (GL, Jack Po) / Regression (WS) / Project Mentoring; нед. 7 Image
Recognition (GL, Satra Ghosh) / Prediction (WS) / Project Mentoring; нед. 8 Reinforcement
Learning in Healthcare (GL, Finale Doshi-Velez) / Validation and Sensitivity Analysis (WS) /
Project Mentoring; нед. 9 Biased Estimates from Regression (GL) / Causal Inference / Project
Mentoring; нед. 10 Inverse Probability Weighting and Structural Marginal Models (GL) /
Structural Nested Mean Models (GL, Judith Lok) / Potential Causal Framework (GL);
нед. 11 Instrumental Variables (GL, Miguel Hernan, дважды) / Project Mentoring;
нед. 12 Final Project Presentations.
Обязательного списка литературы, кроме учебника, нет. Рубрики «ж» нет; курс 2018 года —
это чистая клиническая эпидемиология плюс причинный вывод.

**Fall 2020, «Collaborative Data Science for Healthcare»** — только указатель на MOOC
(https://ocw.mit.edu/courses/hst-953-collaborative-data-science-for-healthcare-fall-2020,
все `/pages/...` отдают 404). Описание на
https://openlearninglibrary.mit.edu/courses/course-v1:MITx+HST.953x+3T2020/about даёт разбивку
только по трём разделам, дословно: «**Section 1** provides a general perspective about digital
health data… **Section 2** focuses on the Medical Information Mart for Intensive Care (MIMIC)
database… **The last section** is a collection of the workshops around the applications of data
science in healthcare.» **Перечня занятий нет.**

**Оговорка о проверке отсутствия:** версий HST.953 за Fall 2016 и Spring 2019 на OCW
**не существует** — оба предполагаемых адреса отдают 404. На OCW есть только Fall 2020
и Fall 2024.

---

## 10. MIT Critical Data: учебной программы дататонов в открытом виде НЕТ

Это отрицательный результат, но проверенный тремя независимыми путями, а не одним поиском.

- https://criticaldata.mit.edu/activities/courses/ — **404**. Сайт пересобран на Next.js,
  содержимое отрисовывается в браузере; разделы `/research`, `/events`, `/highlights`,
  `/community` открываются, перечней курсов в них нет.
- **Wayback этот адрес никогда не архивировал** («The Wayback Machine has not archived
  that URL»).
- Историческое содержимое найдено в репозитории проекта:
  https://api.github.com/repos/MIT-LCP/critical-data/contents/content/blog — там лежат
  `datathon-2017.md`, `datathon-fall-2014.md`, `datathon-spring-2014.md`, `hst-953-2017.md`,
  `hst-953-2018.md`, `hst-953-2019.md`. Прочитаны `[ПРОЧИТАНО]`:
  - `datathon-2017.md` — это **объявление о мероприятии на выходные, а не программа**:
    «This weekend long (September 25-27) event brings together clinicians, data scientists and
    innovators in healthcare to address current problems in intensive care… The event will
    strengthen cross-disciplinary collaboration around secondary analysis of electronic health
    record data». Перечня занятий нет;
  - `hst-953-2017.md` — есть предыстория, требования и состав преподавателей, но прямо сказано:
    «Syllabus, schedule, and more information will be coming soon». Перечня нет;
  - `hst-953-2019.md` — описание, предыстория, требования, фотогалерея преподавателей.
    Перечня нет.

**Вывод:** у дататонов MIT Critical Data опубликованной программы занятий не существует.

Заодно: **HST.936 «Global Health Informatics to Improve Quality of Care»** (другой курс Celi) —
перечня занятий тоже нет: https://ocw.mit.edu/courses/hst-936x-global-health-informatics-to-improve-quality-of-care-spring-2020/
открывается, но это указатель на MOOC (страницы силлабуса/календаря — 404);
`https://sana.mit.edu/hst936` не отвечает (HTTP 000).

### Учебник курса: «Secondary Analysis of Electronic Health Records» — полное содержание

MIT Critical Data, Springer Cham, 2016, открытый доступ, XXI+427 с., **30 глав**.
`[ПРОЧИТАНО, оба листа содержания]` https://link.springer.com/book/10.1007/978-3-319-43742-2

*Часть «Setting the Stage»:* 1 Objectives of the Secondary Analysis of Electronic Health Record
Data · 2 Review of Clinical Databases · 3 Challenges and Opportunities in Secondary Analyses of
Electronic Health Record Data · 4 Pulling It All Together: Envisioning a Data-Driven, Ideal Care
System · 5 The Story of MIMIC · 6 Integrating Non-clinical Data with EHRs · 7 Using EHR to
Conduct Outcome and Health Services Research · 8 Residual Confounding Lurking in Big Data:
A Source of Error.
*Часть «A Cookbook»:* 9 Formulating the Research Question · 10 Defining the Patient Cohort ·
11 Data Preparation · 12 Data Pre-processing · 13 Missing Data · 14 Noise Versus Outliers ·
15 Exploratory Data Analysis · 16 Data Analysis · 17 Sensitivity Analysis and Model Validation.
*Часть «Case Studies Using MIMIC»:* 18 Trend Analysis: Evolution of Tidal Volume Over Time… ·
19 Instrumental Variable Analysis of Electronic Health Records · 20 Mortality Prediction in the
ICU Based on MIMIC-II (SICULA) · 21 Mortality Prediction in the ICU · 22 Data Fusion Techniques
for Early Warning of Clinical Deterioration · 23 Comparative Effectiveness: Propensity Score
Analysis · 24 Markov Models and Cost Effectiveness Analysis · 25 Blood Pressure and the Risk of
Acute Kidney Injury in the ICU: Case-Control Versus Case-Crossover Designs · 26 Waveform
Analysis to Estimate Respiratory Rate · **27 Signal Processing: False Alarm Reduction**
(Qiao Li, Gari D. Clifford) · 28 Improving Patient Cohort Identification Using Natural Language
Processing · 29 Hyperparameter Selection · 30 Erratum.

**Единственная глава из тридцати, хоть как-то близкая к усталости от оповещений, — 27-я**,
и это инженерное подавление ложных тревог в реанимации, а не разбор того, что ложные тревоги
делают с человеком. Про искажение решения, падение квалификации, измеренную работу пары
и нагрузку надзора в книге нет ничего.

---

## 11. Гарвард (HMS / DBMI): программа «ИИ в медицине» и её курсы

**Сразу две поправки к исходному заданию, обе проверены:**
- **BMI 701 — НЕ курс по ИИ.** Это «Foundations of Biomedical Data»
  (https://dbmi.hms.harvard.edu/education/courses/bmi-701, 4 кредита, осень, PJ Van Camp).
- **Курсы «AI in Medicine I / II» — это BMIF 202 и BMIF 203**, а не BMI 701/702.
  BMIF 203 читается совместно с BMI 702.
- `zitniklab.hms.harvard.edu/AIM/`, `/AIM1/`, `/BMI701/` — все **404**. Живые адреса:
  `/BMI702/` и `/AIM2/`.

### 11a. Обязательные курсы программы AIM (PhD track)

Живая страница https://bmiphd.hms.harvard.edu/aim-track/curriculum отдаёт **403 Access Denied**
(и curl, и curl с браузерным UA, и WebFetch — закрыта Akamai). Прочитан **снимок Wayback**
`[ПРОЧИТАНО]`:
http://web.archive.org/web/20251106202130/https://bmiphd.hms.harvard.edu/aim-track/curriculum

Обязательные курсы, дословно:
> - AI in Medicine I (BMIF 202)
> - AI in Medicine II (BMIF 203)
> - AIM Clinical Experience I (BMIF 301)
> - AIM Clinical Experience II (BMIF 302)
> - Foundation of Clinical Data and its Applications (BMIF 204)
> - Responsible Conduct of Science (MedSci 300QC)

Там же: «The cornerstone of the required curriculum is the flagship AI in Medicine I & II
sequence, taught by leading AI researchers at DBMI, including Isaac "Zak" Kohane, Chirag Patel,
Arjun Manrai, and Marinka Zitnik… students will select 3 elective courses».

### 11b. BMIF 202 «Artificial Intelligence in Medicine I» — перечня занятий НЕТ

`[ПРОЧИТАНО]` https://dbmi.hms.harvard.edu/education/courses/bmif-202
4 кредита, осень. Преподаватели: Arjun (Raj) Manrai, Chirag Patel, Isaac Kohane.
Осень 2026: среды 14:00–17:00, 2 сентября — 2 декабря 2026.

Описание, дословно: «AI in Medicine I is a graduate-level seminar course at Harvard Medical
School… This **discussion-oriented course promotes active engagement through student-led
presentations of seminal papers spanning multiple decades**, from early efforts to apply
decision analysis and rule-based systems to the powerful deep learning and generative AI models
being deployed in medicine today. Students will engage with faculty at HMS and the HMS-affiliated
hospitals, **editors at leading general medical and medical AI journals**, and clinicians driving
change at the point of care… Enrollment is limited.»

**Ни перечня занятий, ни списка литературы не опубликовано.** Поскольку состав работ выбирают
сами студенты и он меняется, сказать, попадают ли туда работы про искажение решения,
**нельзя** — это **пустая клетка, а не отрицательный результат.**

### 11c. BMI 702 «Biomedical Artificial Intelligence», Spring 2024 (Zitnik) — полный план

`[ПРОЧИТАНО: головная страница, силлабус и все 14 страниц занятий]`
https://zitniklab.hms.harvard.edu/BMI702/ · `/BMI702/syllabus/` ·
`/BMI702/lectures/week01/` … `/lectures/module6/week14/`

Заголовок, дословно: «**BMI 702 | Biomedical Artificial Intelligence — Harvard - Foundations
of Biomedical Informatics II, Spring 2024**». Преподаватель Marinka Zitnik.
Оценка: 3×20% задачи, 14% быстрые проверки, 26% опросы перед занятием.
**Кому:** из каталога DBMI (https://dbmi.hms.harvard.edu/education/courses/bmi-702) —
«Prerequisites: BMI 701 and BMI 714. BMI 702 is only open to students in the MMSc in Biomedical
Informatics program», то есть **магистранты HMS по биомедицинской информатике, смешанная
клинико-вычислительная аудитория**, не аспиранты-информатики.
*(Та же страница каталога сейчас показывает уже Spring 2027, преподаватель **Pranav Rajpurkar**,
название изменено на «Foundations of AI in Medicine» — курс поменял руководителя и имя.)*

Полный перечень (дословно; в скобках — тематическая строка с головной страницы):
1. **Week 1 - What Makes Biomedical Problems Unique** (Course overview and introduction to
   biomedical AI)
2. **Week 2 - Clinical AI Part I** (Machine learning using electronic health records, subtype
   discovery, disease diagnosis and prognosis prediction)
3. **Week 3 - Clinical AI Part II** (Machine learning on clinico-genetic datasets, diagnostic
   odyssey and therapy selection)
4. **Week 4 - Trustworthy & Efficient AI Part I** (Interpretability and explainability)
5. **Week 5 - Trustworthy & Efficient AI Part II** (Fairness, bias, distribution shifts,
   and robustness)
6. **Week 6 - Biomedical Graph Learning Part I**
7. **Week 7 - Biomedical Graph Learning Part II**
8. **Week 8 - Medical Language Modeling Part I** (Large language models — приглашённая лекция
   Dr. Jonathan Richard Schwarz)
9. **Week 9 - Medical Language Modeling Part II** (NLP across clinical domains and tasks)
10. **Week 10 - Biomedical Imaging Part I** (Vision and vision-language pre-training, multimodal
    LLMs)
11. **Week 11 - Biomedical Imaging Part II** (Multimodal learning, computational pathology)
12. **Week 12 - Ethical & Legal Considerations for Biomedical AI** (приглашённая лекция
    Dr. Sara Gerke)
13. **Week 13 - Generative AI Part I** (AI-guided drug design, small-molecule generation)
14. **Week 14 - Generative AI Part II** (chemical and genetic perturbations, drug repurposing)

**Лекция про взаимодействие человека и модели: НЕТ.**

**Чтение:** есть, обязательное + дополнительное на каждую неделю; прочитаны все 14 страниц.
По нашим рубрикам: **automation bias — нет; падение квалификации — нет; усталость
от оповещений — нет; измеренная работа пары — нет; переезд нагрузки — нет.**
Единственное близкое — **дополнительное** чтение недели 4: «**AI Can Outperform Doctors.
So Why Don't Patients Trust It?**» — и это про доверие **пациентов**, а не про чрезмерное
доверие врача.
Ближе всего к теме ответственности — неделя 12: обязательно «Potential liability for
physicians using artificial intelligence»; дополнительно «**Beware Explanations From AI in
Health Care**», «**When Does Physician Use of AI Increase Liability?**», «Informed Consent and
Medical Artificial Intelligence: What to Tell the Patient?», «Artificial Intelligence and
Liability in Medicine: Balancing Safety and Innovation». Это юридическая и этическая рамка,
не человеческий фактор.
Неделя 5 целиком про смещение в данных: «Dissecting racial bias in an algorithm used to manage
the health of populations»; «Machine Bias» (ProPublica, 23.05.2016); «Bias In Medicine: Last
Week Tonight with John Oliver»; «Fitbits and other wearables may not accurately track heart
rates in people of color» (Stat News); «We should treat algorithms like prescription drugs»
(Quartz).

### 11d. AIM 2 = BMIF 203 / BMI 702, **Spring 2026** — действующая версия

`[ПРОЧИТАНО: головная страница, силлабус и все 13 страниц занятий]`
https://zitniklab.hms.harvard.edu/AIM2/ · `/AIM2/syllabus/` · `/AIM2/lectures/week01/` …
`week13/` *(адреса вида `/lectures/L1/` — 404, настоящие пути `weekNN`)*

Заголовок, дословно: «**Artificial Intelligence in Medicine II — Harvard - BMIF 203 and
BMI 702, Spring 2026**». Преподаватель Marinka Zitnik; Grey Kuling — Curriculum Fellow.
Оценка: заявка проекта 13%, фиксации в GitHub 10%, промежуточная 15%, итоговая 50%, недельные
проверки чтения 12%.
**Кому:** «BMIF 203 is a course requirement for students in the AIM PhD track. There are
limited spots for other students and cross-registration.»

**Три заявления силлабуса, которые прямо касаются нашего вопроса** (дословно):
> «A core part of the course is evaluation, including how to benchmark models and **develop
> human-AI evaluation loops**.»
> «**Understand how AI systems interact with medical and research workflows, and what makes them
> usable, safe, and reliable in practice.**»
> «What makes a model usable for clinicians or researchers? How should we evaluate performance
> beyond a single metric? **What does it take to deploy an AI system without adding burden or
> introducing new safety risks?**»

Полный перечень (дословно):
1. **Week 1 - NLP I** (Course overview, Introduction to NLP, Clinical NLP, Medical terminology
   challenges, Concept extraction from EHRs, Clinical trial matching)
2. **Week 2 - NLP II** (Embeddings, Transformers and BERT, Clinical BERT, Encoder-only and
   decoder-only architectures, Medical question-answering, **Human-AI evaluation loops**) —
   приглашённый Grey Kuling Ph.D.
3. **Week 3 - Generative AI** (Natural language generation, RAG, Chain-of-thought prompting,
   Introduction to diffusion generative models)
4. **Week 4 - AI Agents** (Conversational agents, Multi-agent systems, Tool use, RLHF,
   Introduction to training reasoning models with human feedback and soft verifiers)
5. **Week 5 - Medical Imaging I** — приглашённый Grey Kuling Ph.D.
6. **Week 6 - Medical Imaging II** (Vision foundation models, Development and validation of
   medical imaging interpretation models, Model robustness and performance across diverse
   populations) — приглашённый Grey Kuling Ph.D.
7. **Week 7 - Trustworthy AI** (Explainability and interpretability in medical AI, Feature
   importance and Shapley values, Bias and fairness in biomedical AI, Introduction to
   mechanistic interpretability)
8. **Week 8 - Graph AI I**
9. **Week 9 - Graph AI II** (Knowledge graph learning, Graph transformers, Relational
   foundation models)
10. **Week 10 - Molecular AI**
11. **Week 11 - Multimodal AI**
12. **Week 12 - Ethical & Legal Considerations for Medical AI** (Regulation of AI algorithms and
    devices in healthcare, FDA oversight and liability concerns, Prospective clinical trials for
    AI systems and AI-augmented devices) — приглашённая Sara Gerke
13. **Week 13 - Longitudinal AI** (Disease risk prediction using generative transformers, Time
    series in healthcare, Longitudinal modeling of personal health datasets, Digital biomarkers
    and disease progression tracking, Health sensors)

**Лекция про взаимодействие человека и модели: НЕТ.** Словосочетание «Human-AI evaluation
loops» встречается **только как один пункт в тематической строке недели 2** — внутри занятия
про NLP и медицинские вопросы-ответы. Это не лекция, и в списке чтения недели 2 («BERT:
Pre-training of deep bidirectional transformers…», «Toward expert-level medical question
answering with large language models») работ про человеческий фактор нет.

**Чтение по нашим рубрикам:** automation bias, падение квалификации, усталость от оповещений,
измеренная работа пары, переезд нагрузки — **всё отсутствует.**
Ближайшее, и это **самое сильное попадание во всём гарвардском своде**: неделя 7,
**обязательно** — «**The false hope of current approaches to explainable artificial
intelligence in health care**» (довод Ghassemi / Oakden-Rayner / Beam о том, что объяснения,
предъявляемые врачу, порождают необоснованную уверенность). Далее: нед. 7 дополнительно —
«AI Can Outperform Doctors. So Why Don't Patients Trust It?»; нед. 6 дополнительно —
«Medical artificial intelligence and human values»; нед. 4 дополнительно — «Towards
conversational diagnostic AI»; нед. 9 обязательно — «Medical large language models are
vulnerable to data-poisoning attacks»; нед. 12 — тот же юридический набор, что в BMI 702.

### 11e. Остальные обязательные курсы программы AIM

- **BMIF 204 «Foundations of Clinical Data and its Applications»**
  (`[ПРОЧИТАНО]` https://dbmi.hms.harvard.edu/education/courses/bmif-204), осень,
  Sebastian Schneeweiss. Перечень тем, дословно: «data sources (EHRs, claims, ICU records),
  interoperability standards (HL7/FHIR), and data engineering… disease and treatment-outcome
  prediction, causal inference and target-trial emulation, and real-world evidence generation.
  The course addresses high-dimensional data, time-related biases, temporal drift, and
  regulatory/ethical issues such as privacy, fairness, and historical bias.» Разбивки
  по неделям нет. По нашим рубрикам — ничего.
- **BMIF 301/302 «AIM Clinical Experience I/II»** — страницы существуют, но это клиническая
  практика, а не лекционные курсы; **не открывались** (помечаю честно).

---

# Часть II. Европа и Азия

**Отдельное наблюдение, которое само по себе находка.** Пересечение «свежий + открытый +
с перечнем занятий» встречается редко, и зависимость обратная: **чем свежее набор, тем меньше
вуз публикует.** Страница ETH за весну 2026 обрывается на 7-й неделе из четырнадцати
(и в майском снимке Wayback, снятом в конце семестра, те же 7 строк — значит остальное не
выложили никогда). Записи NUS за 2025/26 вообще без расписания. А два полных недельных плана,
какие удалось достать, — это 2022 и 2024 годы. Для нашей Лекции 7 это значит: ссылаться
на «а вот в таком-то вузе сейчас читают вот такую лекцию» надо осторожно, с годом версии.

## 12. ETH Zürich — 261-5120-00L «Machine Learning for Health Care», весна 2026

**Прочитано** (`[ПРОЧИТАНО]`, 2026-10-14):
- каталог: https://www.vvz.ethz.ch/Vorlesungsverzeichnis/lerneinheit.view?lerneinheitId=199318&semkez=2026S&ansicht=ALLE&lang=en
- сайт курса: https://bmi.inf.ethz.ch/teaching/261-5120-00l-machine-learning-for-health-care-spring-2026
- снимок Wayback (май 2026): https://web.archive.org/web/20260519072712/https://bmi.inf.ethz.ch/teaching/261-5120-00l-machine-learning-for-health-care-spring-2026
- версия 2021 года: https://bmi.inf.ethz.ch/teaching/261-5120-00l-machine-learning-for-health-care-spring-2021
- проверено: страницы `spring-2025`, `spring-2024`, `spring-2023` **не существуют** (404)

**Код/год:** 261-5120-00L, весенний семестр 2026 (2025/26). **5 ECTS**, 2V+2A.
Читают: V. Boeva, G. Rätsch, I. Cannistraci. Набор «150 at the most».
**Кому:** **только инженеры и специалисты по данным, медиков нет.** Курс засчитывается
в магистратурах Biomedical Engineering, Computational Biology & Bioinformatics, Cyber Security,
Data Science, EE&IT, Computer Science (в т.ч. минор по машинному обучению), CSE (бакалавриат
и магистратура), Statistics, а также в CAS CS и DAS Data Science.
**Требования, дословно:** «Data Structures & Algorithms, Introduction to Machine Learning,
Statistics/Probability, Programming in Python, Unix Command Line.»
**Оценка:** 70% письменный экзамен 180 минут (на своём устройстве, SEB, одна сторона А4
конспекта) + 30% обязательная проектная работа (два проекта и доклад по статье, ~30 часов).

### Опубликованный план (дословно) — и он обрывается

`[L]` лекция, `[GL]` приглашённая, `[T]` семинар, `[P]` доклады по статьям.

| Даты | Часть 1 (пн) | Часть 2 (вт) |
|---|---|---|
| 16.02.26, 17.02.26 | [L] Introduction / Motivation | [T] Course Organisation |
| 23.02.26, 24.02.26 | [L] Time-Series | – |
| 02.03.26, 03.03.26 | [L] Imaging | [T] Project 1 Introduction |
| 09.03.26, 10.03.26 | [L] Representation Learning | [P] Paper Seminar |
| 16.03.26, 17.03.26 | [L] Natural Language Processing | [P] Paper Seminar |
| 23.03.26, 14.03.26 | [L] Interpretability | [P] Paper Seminar |
| 30.03.26, 03.04.26 | [GL] Interpretability (Pietro Barbiero) | [P] Paper Seminar |

*(«14.03.26» в шестой строке — опечатка **в источнике**, оставлена как есть.)*

Тематические разделы из каталога (дословно): 1) Structured time series 2) Medical notes
3) Medical images 4) Genomics data 5) Explainable/Interpretable ML 6) Representation Learning.

**Полный план той же дисциплины за весну 2021** (единственный полный, что ETH выложил), дословно:
«-- No Lecture -- · Introduction · Medical Imaging Analysis · Supervised methods for Genetics
and Transcriptomics · Unsupervised methods for Genetics and Transcriptomics · **Ethics** ·
-- Easter Break -- · -- No Lecture -- · Survival Analysis · Natural Language Processing ·
Representation Learning · Time-Series and Sequence Analysis · Interpretability · **Privacy** ·
Exam/Polls/Feedbacks/etc»

**Обязательное чтение: не публикуется.** В каталоге сказано «Only public learning materials
are listed», на странице курса — «Lecture content is available from inside ETH network».
Доклады по статьям есть, список статей закрыт. **Значит вопрос про automation bias для ETH
не отвечен отрицательно, он просто неотвечаем** — помечаю честно, это пустая клетка.

**Рубрика «ж»: НЕТ.** Ближайшее — два занятия «Interpretability» (одно приглашённое), то есть
прозрачность модели, а не поведение врача. В версии 2021 были отдельные лекции «Ethics»
и «Privacy»; в опубликованной части плана 2026 года **нет ни той, ни другой**.

## 13. Technion — 336546 «Machine Learning in Healthcare» (биомедицинская инженерия)

**Самый подробный перечень занятий из всех найденных** — с подпунктами внутри каждой лекции.

**Прочитано:**
- силлабус PDF: https://bme.technion.ac.il/wp-content/uploads/2022/11/MLH-syllabus-2022.pdf
  `[PDF ПРОЧИТАН, 6 страниц]` — WebFetch не смог расшифровать, PDF скачан и распакован локально;
- сайт курса: https://aim-lab.github.io/mlcourse.html `[ПРОЧИТАНО]`;
- каталог: https://students.technion.ac.il/local/technionsearch/course/336546/202601?lang=en
  `[ПРОЧИТАНО]`.

**Оговорка о свежести, важная:** силлабус датирован **06.10.2022**, а каталог в разделе
«Semestrial Information» показывает только **зима 2023/24, зима 2022/23, зима 2021/22**.
Запросы каталога за 202601, 202502 и 202402 отдают те же три семестра. То есть по открытому
каталогу **это не набор 2024/25 и не 2025/26**. Сайт курса без даты.

**Устройство:** 3 кредита, 13 недель, 2 часа лекции + 2 часа семинара в неделю.
Читает **Joachim A. Behar**. Приглашённые: **Anne Weill** (Technion-BME) и **Danny Eytan,
MD-PhD (больница Рамбам)**. Набор 32 человека. Язык английский.
Оценка, дословно: «Four assignments: 35%-25%-15%-25%»; посещаемость ≥70% обязательна
и на лекциях, и на семинарах.
**Требования:** 44131 Signals and Systems **и** 104034 Introduction to Probability H **и**
(234112 Programming C **или** 234128 Introduction to Computing With Python) — то есть
биомедицинская инженерия, **не медики**.

### Полный перечень (дословно, с подпунктами)

**Часть I: ML Basis**
- **Н1 — L01-Introduction to machine learning in healthcare:** Course objectives and settings ·
  Introduction to ML in healthcare · Supervised, unsupervised and reinforcement learning ·
  ML for diagnosis, prognosis and treatment · Medical data, sources, challenges and regulations ·
  Polynomial curve fitting · Cost function · Under and overfitting · Notations
- **Н2 — L02-Data exploration and preprocessing** (Exploratory data analysis · Data
  visualization · Abnormality detection and handling · Features scaling); **L03-Linear models
  for regression** (Intuition · Calculus proof · Probabilistic proof · Sequential learning ·
  Cost function)
- **Н3 — L04-Linear models for classification** (Classification versus regression ·
  LR hypothesis representation · Cross entropy · Gradient descent · Multiclass classification:
  one against all, multinomial); **L05-Odds and odds ratio** (Odds ratio · Confounding)
- **Н4 — L06-Regularization** (Overfitting · Cost function · Regularized linear regression ·
  Regularized logistic regression · Ridge, Lasso regression · Geometrical interpretation);
  **L07-Practical consideration on training a model** (Evaluating a model: train, validation
  and test sets · Model selection, learning curves and error analysis · Bias-variance tradeoff ·
  Cross validation approaches · Stratification · Information leakage · Generalization performance)
- **Н5 — L08-Performance statistics** (Performance statistics · Receiver operative curve ·
  Multiclass classification · Training the final ML model); **«Guest speaker Rambam -
  Application of ML in clinical practice»**

**Часть II: Popular classifiers**
- **Н6 — L09-Introduction to nonlinear models** (Linear but with nonlinear features · Change of
  basis); **L10-Support vector machines** (Maximum margin classifiers · Dual representation ·
  Kernel trick · Grid search and random search)
- **Н7 — L11-Feature selection** (Relevance and redundancy · Filters, wrappers and embedded ·
  LASSO, mRMR)
- **Н8 — L12-Unsupervised learning with k-means and Gaussian mixture models** (K-nearest
  neighbor · Probabilistic data analysis: GMM)
- **Н9 — L13-Principal component analysis** (Blind source separation · PCA · Change of basis ·
  Mathematical proof · PCA in machine learning); **L14-Independant component analysis** *[sic]*
  (ICA · Statistical independence versus correlation · Whitening · Beyond ICA: t-SNE)

**Часть III: Neural networks and introduction to deep learning**
- **Н10 — #C21 ANN I: introduction; #C22 ANN II: training a NN**
- **Н11 — #GL01 Performance computing - High Performance Computing (AW)**
- **Н12 — #C23 ANN III: hyperparameters tuning; #C24 Deep Learning CNN**
- **Н13 — #C25 Deep Learning CNN - CNN architectures; #C26 Examples of medical ML @Technion -
  Presentation of ongoing research in the lab.**

Сайт курса добавляет обозначения `L15/L16/L17-Neural Networks I/II/III` и
`L18-Introduction to convolutional neural networks`, плюс 12 практикумов по коду (`C00`–`C11`)
и теоретические семинары `T01`.

**Обязательное чтение: не публикуется** — ни в PDF, ни на сайте. В цели курса входит
«**Ground truth in medical data science**».
**Рубрика «ж»: НЕТ.** Ближайшее — приглашённое занятие недели 5 от врача из Рамбама
«Application of ML in clinical practice».

## 14. Technion — 97248 «Machine Learning For Healthcare» (Uri Shalit) — лучшая формулировка цели

**Прочитано:** https://students.technion.ac.il/local/technionsearch/course/97248/202601?lang=en
`[ПРОЧИТАНО]`

**Оговорка о свежести:** последний указанный семестр — **весна 2023/24** (также весна 2022/23
и 2021/22). **Язык преподавания — иврит.** 3 кредита (2 лекции + 1 лаборатория + 1 проект).
Ответственный — **Uri Shalit**, со-преподаватель — **Danny Eytan** (врач-реаниматолог).
Запись вручную по одобрению преподавателя: письмо + выписка + résumé.
**Требования:** 46202 Data Analysis **или** 46203 Planning and Reinforcement Learning **или**
97209 Machine Learning 2.

**Перечня занятий нет.** Описание, дословно (сохранён странный регистр каталога):
«Machine Learning Has Great Potential For Improving Healthcare. We Will Read and Critically
Discuss Recent Papers Covering How Ml Is Used For Guiding Diagnosis, Personalizing Treatments,
Analyzing Medical Images and Medical Text, Reducing Healthcare Costs, Reducing Unfair Bias, and
For a Better Understanding of Human Physiology.» Список статей закрыт.

**Но цели обучения — самое близкое к нашей теме из всего, что найдено в Европе и Азии.
Дословно, полностью:**

> «At The End of The Course The Student Will Know#
> 1. to Give Three Examples of Diagnostic Tasks in Which Machine Learning Tools Showed an
>    Advantage Over Physicians
> 2. Explain How Machine Learning Tools Can Help Personalize Treatment, And What Are The Special
>    Difficulties in This Task As Opposed To Diagnostic Tasks
> 3. **Explain For Which Medical Tasks The Current Tools of Deep Learning Are Appropriate, and
>    For Which Tasks They Are Not**
> 4. Implement a Machine Learning Model On Medical Data, and **Explain To A Medical Practitioner
>    The Advantages and Disadvantages of The Model Versus a Human Physician**, further, The
>    Student Will Explain **The Situations in Which They Recommend Using The Model, and The
>    Situations in Which It Is Best to Avoid Using It**
> 5. Raise a Number of Ethical Issues Arising From The Use of Machine Learning Tools in The
>    Healthcare Domain»

Третья и четвёртая цели — это прямо «когда не надо», причём четвёртая ставит модель **против**
врача. Это сильнейшая цитата для лекции о суждении и границах, и она из курса, который
со-преподаёт работающий реаниматолог. **Но это всё-таки не наша рубрика:** здесь «когда
рекомендовать модель», а не «что происходит с врачом, который ею пользуется».

## 15. TU München — IN2403 «Artificial Intelligence in Medicine»

**Прочитано:** https://campus.tum.de/tumonline/WBMODHB.wbShowMHBReadOnly?pKnotenNr=2930921
`[ПРОЧИТАНО]`
*(Страница занятия `wbLv.wbShowLVDetail?pStpSpNr=950596772` — приложение на JS, curl отдаёт
только заглушку. `https://kiinformatik.mri.tum.de/.../teaching` — 404. `https://aim-lab.io/` —
отрисовка на JS, читаемого перечня нет.)*

**Код/год:** IN2403, 5 ECTS, магистратура, английский, зимний/летний семестр. Версия описания
**21W, действует с 2021W** — и **до сих пор привязана к действующим учебным планам**, включая
SPO 20261 (магистратура по биоинформатике), 20231 (информатика, математика, Games Engineering),
2025W. Владелец модуля — **проф. Daniel Rückert**. 150 часов всего / 60 аудиторных / 90
самостоятельных.
*Оговорка: TUM публикует один недатированный перечень содержания на версию модуля, а не
понедельный план — то есть он действующий, но не привязан именно к 2025/26.*
**Кому:** магистранты-информатики. **Требования, дословно:** «Introduction to Deep Learning
(IN2346)», «Computer Aided Medical Procedures I (IN2021)».
**Оценка:** письменный экзамен 90 минут, без материалов.

### Полный перечень содержания («Inhalt»), дословно, по порядку

- Introduction: Clinical motivation, clinical data, clinical workflows
- ML for medical imaging
- Data curation for medical applications
- Domain shift in medical applications: Adversarial learning and Transfer learning
- Self-supervised learning and unsupervised learning
- Learning from sparse and noisy data
- ML for unstructured and multi-modal clinical data
- NLP for clinical data
- Bayesian approaches to deep learning and uncertainty
- Interpretability and explainability
- Federated learning, privacy-preserving ML and ethics
- ML for time-to-event modeling, survival models
- ML for differential diagnosis and stratification
- Clinical applications in pathology/radiology/omics

**Способ преподавания, дословно:** «Guest lectures will be held by experts from local hospitals
and med-tech companies to ensure that the covered topics are relevant for clinical practice.»
В цели обучения входит «analyse and evaluate **social and ethical implications**».

### Обязательное чтение — есть, названное. Дословно, полностью

*Рекомендованное:*
1. I. Goodfellow, Y. Bengio and A. Courville. *Deep Learning*. MIT Press, 2016.
2. E. J. Topol. «High-performance medicine: the convergence of human and artificial
   intelligence.» *Nat Med* 25, 44–56, 2019.
3. A. Esteva, K. Chou, S. Yeung, et al. «Deep learning-enabled medical computer vision.»
   *npj Digit. Med.* 4, 5, 2021.
4. B. Norgeot, G. Quer, B.K. Beaulieu-Jones et al. «Minimum information about clinical
   artificial intelligence modeling: the **MI-CLAIM checklist**.» *Nat Med* 26, 1320–1324 (2020).
5. V. Sounderajah, H. Ashrafian, R. Aggarwal et al. «Developing specific reporting guidelines
   for diagnostic accuracy studies assessing AI interventions: The **STARD-AI** Steering Group.»
   *Nat Med* 26, 807–808 (2020).

*Дополнительное:*
6. E. Topol. *Deep Medicine – How Artificial Intelligence Can Make Healthcare Human Again*. 2019.

**Проверка по нашим рубрикам.** Позиции 2 и 6 — единственные, касающиеся отношений человека
и модели, и **обе заявлены положительно уже в названии**: «**сближение** человеческого
и искусственного интеллекта», «снова сделать здравоохранение **человечным**». Позиции 4 и 5 —
требования к отчётности. **Про искажение решения, падение квалификации, измеренную работу пары,
чрезмерное доверие, усталость от оповещений и нагрузку надзора — ничего.**
**Рубрика «ж»: НЕТ.** Ближайшее: «Interpretability and explainability»; «Federated learning,
privacy-preserving ML and ethics».

## 16. Imperial College London — 70014 «Machine Learning for Imaging»

**Прочитано:** https://www.imperial.ac.uk/computing/current-students/courses/70014/
`[ПРОЧИТАНО через WebFetch]` *(curl закрыт CloudFront, 403)*; плюс
https://wp.doc.ic.ac.uk/bglocker/teaching/ `[ПРОЧИТАНО]` — подтверждает, что курс читается
сейчас и что он **заменил** закрытый курс «Medical Image Computing».

**Оговорка:** **учебный год на прочитанной странице не указан.** Ведут **Ben Glocker
и Daniel Rueckert** (тот же Rueckert владеет модулем TUM IN2403).
**Требования, дословно:** «Computer Vision, Introduction to Machine Learning, and Deep
Learning» — только информатика.
**Оценка:** «one assessed mini-project (coursework)» 20% + «a final written exam» 80%.

**Полный перечень тем (дословно, 7 пунктов):**
- Introduction to machine learning for imaging
- Image segmentation
- Image registration
- Self-supervised representation learning
- Inverse problems (super-resolution, image reconstruction)
- Trustworthy machine learning in imaging (privacy, explainability)
- Causality in imaging

Цель обучения, которую стоит привести: студент должен уметь «analyse critically the
**limitations** of machine learning techniques in the domain of image computing».

**Обязательное чтение: проверить нельзя** — страница ссылается на список в системе Leganto,
названия не раскрыты. **Рубрика «ж»: НЕТ.** Ближайшее — «Trustworthy machine learning
in imaging (privacy, explainability)».

## 17. Karolinska Institutet — 2QA338 «Applied Artificial Intelligence (AI) in Healthcare»

**Единственный найденный курс с по-настоящему смешанной аудиторией медиков и инженеров.**

**Прочитано:** https://education.ki.se/course-and-programme-syllabi/course-syllabus-2QA338
`[ПРОЧИТАНО]`
*(Адрес `education.ki.se/course-syllabus/2QA338` из выдачи поиска переадресует на общий
указатель; канонический путь — выше. `.../course_syllabus/2QA338-syllabus.pdf`
и `utbildning.ki.se/kursplan/2QA338` — 404.)*

**Код:** 2QA338, **15 кредитов**, кафедра клинических наук, вмешательств и технологий
(CLINTEC). Второй цикл. Зачёт/незачёт. Дата решения 23.12.2021; «**Course syllabus valid from:
Autumn semester 2022**» — числится действующим. Язык английский.
**Кому — дословно:** «A Bachelor's degree or a professional degree equivalent to a Swedish
Bachelor's degree of at least 180 credits **in health care, medicine or engineering sciences**.»

**Обоснование курса, дословно — оно само по себе по нашей теме:** «The potential use of AI
technologies in healthcare needs healthcare professionals with knowledge of AI to enable
**interactive and explanatory AI** and ensure the quality of AI-based systems to **increase
patient safety**. Knowledge of AI is also important for people involved in **decision-making,
procurement and implementation** of AI-based systems.»

**Цели обучения, дословно:** Describe different AI methods and their strengths and limitations ·
Compare and select relevant AI methods for the development of AI applications in healthcare ·
Reason about legal conditions and ethical challenges in AI · Reflect on obstacles and driving
factors for how AI-based solutions can be applied in healthcare.

### Полный перечень модулей и содержания (дословно)

**Introduction to AI, 4.5 кредита** — Overview of techniques and applications · Traditional
machine learning methods · Artificial neural networks · Supervised, semi-, and non-supervised
learning · Pattern recognition · Interactive process mining · Tools and real-world examples

**AI in health care, 4.5 кредита** — **Medical image analysis without AI** · AI for medical
image analysis and imaging · AI for data analytics and data mining · Future applications
and techniques

**From AI solutions to success stories, 3.0 кредита** — Innovation and entrepreneurship for AI
in health care · Ethical and data protection issues in AI-based solutions · Regulatory
framework · **Design and deployment of AI solutions in health care: stakeholder's views**

**Group project work, 3.0 кредита** — Student activity using tools to implement AI for healthcare

**Способы преподавания, дословно:** «online lectures, seminars, interactive sessions live and
online, **study visits** and individual project work.»

**Обязательное чтение: не публикуется** — в силлабусе нет раздела литературы.
**Рубрика «ж»: НЕТ.**

**Но здесь есть приём, который стоит у них забрать.** Модуль «AI in health care» открывается
пунктом «**Medical image analysis without AI**» — то есть **разбор работы без ИИ ставится
первым, до разбора той же работы с ИИ**. Это ровно то сопоставление «без ИИ / с ИИ», которого
требуют наши собственные правила (§ «Форма подачи слайда»), найденное в живом курсе
медицинского университета со смешанной аудиторией. Второй близкий пункт — «Design and
deployment of AI solutions in health care: stakeholder's views».

**Другие курсы KI, найденные по названию в указателе силлабусов** (названия проверены,
содержание **не читалось**):
- **2LA212 «Artificial Intelligence in Medicine (AIM): implementation»**, 7,5 кредита, кафедра
  женского и детского здоровья, решение **программного совета врачебной программы**
  (Programnämnden för läkarprogrammet), **дата решения 17.02.2026, действует с осеннего
  семестра 2026** — самый свежий и самый обещающий по названию. **Но его английская страница
  публикует только «Essential data»: разделов Outcomes, Content, Teaching methods, Examination
  и Literature там нет вообще** (проверено по каждому заголовку — все отсутствуют). Шведский
  путь `utbildning.ki.se/kurs-och-programplaner/kursplan-2LA212` отдаёт 404. Итог: не публикуется.
- 4FF023 Artificial Intelligence for Clinical and Biomedical Applications
- 1QA142 Artificial Intelligence in Mental Healthcare
- 2XX338 Applied Artificial Intelligence (AI) in Healthcare (дублирующий код того же курса)

## 18. NUS — 2025/26, только описания, но одна фраза важна

**Прочитано** (`[ПРОЧИТАНО, полный JSON]`): https://api.nusmods.com/v2/2025-2026/moduleList.json
и `https://api.nusmods.com/v2/2025-2026/modules/{MDG5256,MDG5248,PHM5005,BN5212}.json`

**Это самые свежие записи во всей разведке (учебный год 2025-2026), но NUSMods публикует
описания, а не перечни занятий.** Списков литературы тоже нет.

**MDG5256 «Machine Learning in Medicine»** — 2 MC, деканат медицинского факультета
Yong Loo Lin, семестр 1. **В описании взаимодействие врача и модели названо целью курса,
дословно:** «A solid grasp of these foundational principles and skills will enhance the
**safety and efficiency of clinician-AI interactions** and contribute to improved healthcare
quality.» Форма: «a combination of machine learning article discussions, led by lecturers who
are domain experts, and paper presentation led by students.»
**Это единственный из восемнадцати разобранных курсов, который ставит взаимодействие человека
и модели в заявленную цель — и он не публикует перечня занятий, по которому можно было бы
проверить, есть ли за этой целью хоть одно занятие.**

Прочие: **MDG5248 «Ethics of Health Data and Artificial Intelligence»** — 4 MC, семестр 2,
«Privacy, consent, public interest, bias, transparency, governance, and public engagement»;
**PHM5005 «AI and Machine Learning for Precision Medicine»** — 4 MC, биохимия, семестр 1;
**BN5212 «Advanced Machine Learning for Biomedical Engineering and Sciences»** — 4 MC,
биомедицинская инженерия, семестр 1.
Прочие названия из списка модулей 2025-2026 (**только названия**): BL5633 Applications of AI
in Biotech and Biomed · BMI5101 Advanced Biomedical Informatics · BN5211 Medical Robotic
Intelligence · GMS5174 / GMS5674 Health Informatics & Digital Transformation · GMS5204 Data
Science + Healthcare · HI5101 Health Informatics and Data Visualisation · HI5102 How
Informatics can enable «Value Based Healthcare» · IE5205 Healthcare System and Analytics ·
SPH5104 Analytics for Better Health · SPH5414 Informatics for Health · TBA4250 Healthcare
Analytics.

## 19. University of Toronto — LMP1210 «Basic Principles of Machine Learning in Biomedical Research»

Включён потому, что это **полный недельный план курса для медиков** — редкое сочетание.

**Прочитано:** https://sanatonek.github.io/lmp1210/ `[ПРОЧИТАНО]`
*(Также отвечают, но целиком не читались:
https://lmp.utoronto.ca/lmp1210h-basic-principles-machine-learning-biomedical-research,
https://lmp.utoronto.ca/csc2541-topics-machine-learning-machine-learning-healthcare.)*

**Год:** зима 2024 (2023/24). Версии 2025 года не найдено (`lmp1210_2025` — 404).
Читают Rahul G. Krishnan и Sana Tonekaboni.
**Кому — дословно:** «This course is intended for graduate students in **Health Sciences**
to learn the basic principles of machine learning in biomedical research and to build and
strengthen their computational skills of medical research.» И далее: «The students will learn
the current practices and applications of ML in medicine, and **understand what ML can and
cannot do for medicine**.»
**Требований нет**; на второй неделе сдаётся «Math Diagnostics».

### Полный перечень (дословно, 12 занятий)

| № | Дата | Тема |
|---|---|---|
| 1 | Jan 11 | Intro to ML in medicine, nearest neighbor classifier |
| 2 | Jan 18 | Tree-based classifier; Python tutorial for introduction to Python |
| 3 | Jan 25 | Linear methods for regression and classification; Python tutorial for evaluation methods |
| 4 | Feb 01 | Neural networks |
| 5 | Feb 08 | Ensemble models; Python tutorial for supervised learning practice |
| 6 | Feb 15 | Unsupervised learning for clustering: K-means, Gaussian mixture models |
| — | Feb 22 | Reading Week |
| 7 | Feb 29 | Unsupervised learning for clustering; Python tutorial for unsupervised learning practice |
| 8 | Mar 07 | Office hours for the final project |
| 9 | Mar 14 | Guest Lecturer: Dr. Robert Grant Machine Learning in Oncology |
| 10 | Mar 21 | Advanced deep learning methods for medical image analysis |
| 11 | Mar 28 | Term project presentation |
| 12 | Apr 04 | Term project presentation |

**Обязательного чтения нет, и это сказано прямо, дословно:** «Suggested readings included help
you understand the course material. **They are not required**, i.e. you are only responsible
for the material covered in lecture.» Названные источники — все методические: Bishop «Pattern
Recognition and Machine Learning»; Goodfellow/Bengio/Courville «Deep Learning»; MacKay
«Information Theory, Inference, and Learning Algorithms»; конспекты Roger Grosse (Linear
Regression, Linear Classifiers, Multilayer Perceptrons, Backpropagation, Mixture Models);
конспекты David Liu по CSC110/111; PyTorch «Training a Classifier»; руководство Jaan Altosaar
по VAE; «Introduction to VAEs (Kingma and Welling)».

**Рубрика «ж»: НЕТ** — ни в перечне, ни в литературе.

**Но в этом курсе есть почти-попадание, которое просто обязано попасть в нашу деку.**
У курса длинная оговорка про порождающие модели, и она по сути есть довод о чрезмерном
доверии — только обращённый **к студентам, а не к медицине**. Дословно:

> «**Overreliance on generative AI may give you a false sense of how much you've actually
> learned**, which will lead to poor performance on the midterm test and final exam, in later
> courses, or in future work or studies after graduation.»

Курс про машинное обучение в медицине предупреждает о падении собственной квалификации
от чрезмерного доверия к модели — **в разделе про академическую честность, про самого себя,
а не про медицину, которой он учит.** Лучшей иллюстрации к нашему зазору не придумать.

## 20. UCL — закрыт, сообщаю честно

**UCL был одной из двух приоритетных целей, и прочитать его не удалось.** Все пути закрыты
Cloudflare:
- `https://www.ucl.ac.uk/module-catalogue/modules/artificial-intelligence-for-biomedicine-and-healthcare-COMP0172`
  — curl: «Enable JavaScript and cookies to continue»; WebFetch: **403**;
- `.../artificial-intelligence-in-healthcare-CHME0016` — то же; **в Wayback CDX снимков
  этого модуля нет вообще**;
- `https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/artificial-intelligence-enabled-healthcare-msc`
  — curl возвращает пусто;
- `https://www.ucl.ac.uk/intelligent-imaging-healthcare/programme/modules` — 403.
Повтор с полным браузерным User-Agent и Accept-Language — по-прежнему закрыто.

**Один модуль UCL прочитать всё же удалось — через Wayback** `[ПРОЧИТАНО]`:
https://web.archive.org/web/20260902031424/https://www.ucl.ac.uk/module-catalogue/modules/advanced-machine-learning-for-healthcare-CHME0035
(снимок 02.09.2026)

**CHME0035 «Advanced Machine Learning for Healthcare»**, 15 кредитов, факультет наук
о здоровье населения, **Институт информатики здравоохранения**.
Ограничения, дословно: «This an optional module for students on the **MSc Health Data Science**
and **MRes in Artificial Intelligence in Enabled Healthcare**. You must have completed the
Artificial Intelligence in Healthcare **CHME0016** module or equivalent prior to taking this
module.»
Цели обучения (дословно, 8): Be familiar with widely-used ML algorithms · Create structured code
for practical implementation and reproducible research · Know the general approaches to optimize
the models · Understand how to build advanced ML models to solve supervised and unsupervised
learning problem in clinical environments · Understand how does reinforcement learning work,
and how to implement it in practice · The foundation of NLP and large language model (LLM),
and their application in healthcare area · Understand the mathematics necessary for constructing
ML solutions · Work with a range of dataset, e.g. labelled data, clinical data, time series
data, and medical images · Be able to design and implement various ML algorithms in a range
of real-world applications.
Названная литература (всего две позиции): «Deep Learning» (Goodfellow, Bengio, Courville);
«Deep Learning with Python» (François Chollet). **Работ по человеческому фактору нет.**

**Структурная находка про UCL:** **каталог модулей UCL перечней занятий не публикует вообще** —
шаблон страницы это описание + цели обучения + ограничения + короткий список литературы.
То есть даже будь он открыт, понедельного плана он бы не дал; самая мелкая гранулярность
у UCL — **перечень модулей**.

**Перечень модулей UCL — ТОЛЬКО СНИППЕТ из выдачи поиска, ни одна страница не открывалась,
доверять нельзя:**
- *MRes AI Enabled Healthcare*: обязательные CHME0032 Healthcare Artificial Intelligence
  Journal Club, CHME0033 Dissertation in AI Enabled Healthcare; по выбору CHME0012 Principles
  of Health Data Science, CHME0013 Data Methods for Health Research, CHME0015 Advanced Methods
  in Data Science and Statistics, CHME0016 Artificial Intelligence in Healthcare, CHME0031
  Programming with Python for Health Research, CHME0034 Applied Computational Genomics,
  CHME0035 Advanced Machine Learning for Healthcare, CHME0039 Artificial Intelligence
  in Healthcare Group Project;
- *MSc AI for Biomedicine and Healthcare*: обязательные COMP0172, COMP0186 Foundations of AI,
  COMP0187 Probabilistic Modelling, COMP0188 Deep Representations and Learning, COMP0286
  Project; по выбору COMP0082 Bioinformatics, COMP0087 Statistical NLP, COMP0089 Reinforcement
  Learning, COMP0118 Computational Modelling for Biomedical Imaging, COMP0189 Applied AI,
  COMP0195 Accountable, Transparent, and Responsible AI, COMP0261, COMP0264 Generative AI.

**Оксфорд не разбирался вовсе** — помечаю как пробел разведки, а не как отсутствие.

## 21. University of Arizona — «Artificial Intelligence, AI literacy and Medicine» (для студентов-медиков)

Включён потому, что это **курс для старшекурсников-медиков**, то есть ровно та аудитория,
которой рубрика «ж» нужнее всех.

**Прочитано:** `[PDF ПРОЧИТАН, 5 страниц]`
https://astec.arizona.edu/sites/default/files/2024-03/Syllabus-%20Artificial%20Intelligence,%20AI%20Literacy,%20and%20Medicine.docx.pdf
*(WebFetch расшифровать PDF не смог, скачан и разобран локально PyMuPDF.)*
Выложен в марте 2024. «Course Number TBD» — номер на момент публикации не присвоен.

**Руководитель:** Allan J. Hamilton, MD, FACS — Regents' Professor of Surgery, исполнительный
директор Arizona Simulation Technology & Education Center (ASTEC), руководитель отделения ИИ.
**Кому, дословно:** «This semester long course offers **senior medical students** an in-depth
exploration of artificial intelligence (AI) in healthcare… help to be able to apply AI tools and
methodologies into their own future medical practices **beginning with the first day of
internship**.» Набор: максимум 20 человек. Зачёт/незачёт, непрофильный факультатив.
**Учебник:** Peter Lee, Carey Goldberg, Isaac Kohane, «The AI Revolution in Medicine: GPT-4
and Beyond» (Pearson, 2023) — **тот же учебник, что рекомендован дополнительно в MIT MLHC 2025**.
Плюс статьи через Perusall.

### Полный перечень (дословно, по неделям и дням)

**Week 1: Introduction to AI and its Foundational Principles**
- Day 1-3: Basics of Artificial Intelligence, Machine Learning, Deep Learning.
- Day 4-5: Introduction to programming languages and platforms relevant to AI (e.g., Python,
  TensorFlow).

**Week 2: Applications of AI in Clinical Medicine**
- Day 6-8: AI in diagnostics (Radiology, Pathology), AI-driven decision support systems.
- Day 9-10: AI in treatment planning, predictive modeling, patient monitoring.

**Week 3: Challenges, Ethics, and Implementation of AI**
- Day 11-12: Integration challenges of AI in healthcare, AI in Electronic Health Records (EHRs).
- Day 13-14: Ethical considerations, data privacy, biases in AI, and patient autonomy.

**Week 4: Future Prospects, Student Projects, and Conclusion**
- Day 15-17: Exploration of cutting-edge AI applications, including AR/VR in medicine, genomics,
  and AI's role in global health.
- Day 18-19: Group project work, where students identify a medical challenge and propose
  an AI-driven solution.
- Day 20: Project presentations, course reflection, and discussion on career opportunities
  in medical AI.

Домашние задания (дословно): нед. 1 «Exploratory tasks related to AI concepts and basic
programming»; нед. 2 «**Engage with AI-driven diagnostic tools, evaluate AI predictions with
real clinical scenarios**»; нед. 3 «Ethical case studies, data breach scenarios, and bias
identification in AI models».

### Замер по рубрике «ж»

Сплошной поиск по всем 5 страницам:

| Искомое | Вхождений |
|---|---|
| `automation bias` | **0** |
| `deskill` | **0** |
| `over-reliance` / `reliance` | **0** |
| `human-AI` | **0** |
| `human factor` | **0** |
| `workload` | **0** |
| `anchor` | **0** |
| `alert fatigue` | **0** |
| `workflow` | **0** |
| `complacen` | **0** |
| `trust` | 2 — и оба в целях курса, в значении «модели можно доверять для работы с пациентом» («can be trusted for patient care») |
| `skill` | 1 — и это «Demonstrate the necessary **skills** to effectively collaborate with… data scientists», то есть про навык сотрудничества, не про его утрату |

**Рубрика «ж»: НЕТ.** Курс, который прямо обещает подготовить студента-медика к применению ИИ
**с первого дня интернатуры**, не содержит ни одного занятия и ни одного слова о том, как
подсказка модели меняет его решение и его квалификацию. Домашнее задание недели 2 требует
«оценить предсказания ИИ на настоящих клинических сценариях» — то есть студента ставят ровно
в ту ситуацию, про искажения которой ему не рассказали.

---

# Часть III. Массовые и профессиональные программы (Stanford Coursera, Johns Hopkins, Michigan, DeepLearning.AI)

**Почему они здесь.** Это курсы, через которые тему проходит на порядок больше людей, чем через
MIT: у одной стэнфордской специализации 97 392 записавшихся. Если искать, где рубрика «ж»
должна была бы появиться раньше всего — то здесь, потому что аудитория не инженерная.

**Техническая оговорка:** страницы Coursera отдают перечни модулей прямо в HTML, поэтому
`curl` + снятие тегов даёт **полный текст, а не сниппет** — всё ниже прочитано целиком.
А вот `ep.jhu.edu`, `publichealth.jhu.edu`, `malonecenter.jhu.edu`, `bme.jhu.edu`,
`online.stanford.edu`, `engineering.jhu.edu` отдают **403 (Cloudflare)** и curl, и WebFetch —
они брались через Wayback, это помечено по каждому пункту. **Архив Интернета посреди работы
ушёл в недоступность** («Internet Archive services are temporarily offline»), из-за чего два
пункта остались непроверенными до конца — они помечены как пробел, а не как отсутствие.

## 22. Stanford «AI in Healthcare» — специализация Coursera (Nigam Shah и др.)

**Прочитано** (`[ПРОЧИТАНО целиком]`, 2026-10-14):
https://www.coursera.org/specializations/ai-healthcare и страницы всех пяти курсов:
`/learn/intro-to-healthcare`, `/learn/introduction-clinical-data`,
`/learn/fundamental-machine-learning-healthcare`,
`/learn/evaluations-ai-applications-healthcare`, `/learn/ai-in-healthcare-capstone`.
Плюс https://web.archive.org/web/20251002120517/https://online.stanford.edu/programs/artificial-intelligence-healthcare
*(напрямую stanford.edu отдаёт 202 и пустое тело — защита от роботов).*

**Версия:** дословно из раздела вопросов: `Original Release Date: 08/10/2023` /
`Expiration Date: 08/09/2029` для курсов 1–4; итоговый проект — `11/16/2023`.
Коды Stanford: SOM-XCHE0008–0012. Организуют School of Medicine и Stanford Center for Health
Education; аккредитовано для непрерывного медицинского образования (ACCME/ACPE/ANCC).
**97 392 записавшихся** на момент чтения.
**Кому, дословно:** «Beginner level — No prior experience required»; «This specialization is
designed for **both healthcare providers and computer science professionals**, offering
insights to facilitate collaboration between the disciplines.»
**Преподаватели по курсам:** К1 Nigam Shah, Mildred Cho, Laurence Baker. К2 Nigam Shah,
Steven Bagley, David Magnus. К3 Matthew Lungren, Serena Yeung. К4 Tina Hernandez-Boussard,
Mildred Cho. К5 Matthew Lungren, Nigam Shah и ещё трое.

### Курс 1 — «Introduction to Healthcare» (7 модулей, 12 ч)

- **M1 «Overview of Health Care Systems and Key Challenges They Face»** (12 видео):
  Introduction · A Simple Interaction Between Providers and Patients · The Problem of Risk ·
  Solving the Problem of Risk: Risk Pooling · Insurance and Intermediaries for Risk Pooling ·
  Beyond Patients, Providers, and Intermediaries · Overview of the Types and Roles of
  Intermediaries · Overview of the Types and Roles of Providers · Providers and Levels of Care ·
  The Challenge of Rising Health Care Costs · The Challenges of Quality and Access ·
  **Lessons for AI and Data**
- **M2 «Physicians, Physician Practices, and Physician Payment»** (12 видео):
  Characteristics of Physician Practices · Physicians, Intermediaries, and Networks · Fee for
  Service Payment · Procedure Codes and Diagnosis Codes · The Medicare Fee Schedule ·
  Capitation Payment Systems: Overview and Structure · Capitation Payment Systems: Scope of
  Capitation · Episode-Based Payment Systems and Salary Systems · Risk Shifting in Physician
  Payment · **Incentives Created by Physician Payments** · Lessons for AI and Data · Wrap Up
- **M3 «Hospitals, Other Provider Organizations, and Related Payment Systems»** (13 видео):
  Basic Operations and Characteristics of Hospitals · How Hospitals Relate to Physicians and
  Intermediaries · Hospital Payment Methods: Charge Masters/FFS and Per Diem · …: DRGs ·
  …: Global Budgets · Hospital Payment Topics · Risk and Incentives in Hospital Payment ·
  Independent Facilities – Structure and Payment · Health Care Systems and Larger Provider
  Organizations · Pay for Performance · EMRs, EHRs, and PHRs · Providers, Provider Incentives,
  Data, and Tools · Wrap Up
- **M4 «Intermediaries, Health Insurance Plans, and Health Care Financing»** (15 видео):
  Intermediaries and their Goals · … and the Broad Challenges Facing Health Care Systems ·
  Networks and Selective Contracting · Provider Payment Methods and Levels · Patient Cost
  Sharing · Utilization Review, Gatekeepes, and Other Methods of Directly Influencing Care
  *[sic, опечатка в источнике]* · Coverage Decisions · Combinations and Tradeoffs · Three
  Stereotypical Plan Designs: «Traditional», HMO, and PPO · Some More Recent Trends in Plan
  Design · Public and Private Plans · The U.S. Medicare Program · The U.S. Medicaid Program ·
  Intermediaries: Lessons for Innovators · Wrap Up
- **M5 «Health Care Products and Prescription Drugs, and Quality Measurement and
  Improvement»** (13 видео): Health care products, approvals, and prescription drugs ·
  Prescription Drug Approval Processes · Patents, Branded Drugs, and Generic Drugs · Patients,
  Insurance, Formularies, and Prescription Drugs · Intermediaries, Pharmacy Benefit Managers,
  Drug Prices, and Rebates · Products and Prescription Drugs Wrap Up · Quality of Care Overview
  and Key Organizing Concepts · Overview, and Structural Quality Measures · Process Quality
  Measures · Outcome Quality Measures and Satisfaction Measures · Overview of Some Approaches
  to Improving Quality · Innovation and Data in Quality Improvement · Wrap Up
- **M6 «Ethics»** (4 видео): Overview of AI applications in delivery of health care services
  and ethical issues · Ethical frameworks for health care and for AI · AI and incentives in
  health care delivery and payment structures · More examples of AI and incentives…
- **M7 «Course Wrap Up»**

### Курс 2 — «Introduction to Clinical Data» (8 модулей, 12 ч)

- **M1 «Asking and answering questions via clinical data mining»** (12 видео): Welcome ·
  Introduction to the data mining workflow · Real Life Example · Example: Finding similar
  patients · Example: Estimating risk · Putting patient data on timeline · Revisit the data
  mining workflow steps · Types of research questions · Research questions suited for clinical
  data · **Example: making decision to treat** · Properties that make answering a research
  question useful · Wrap Up
- **M2 «Data available from Healthcare systems»** (16 видео): Review of the healthcare system ·
  Review of key entities and the data they collect · **Actors with different interests** ·
  Common data types in Healthcare · Strengths and weaknesses of observational data ·
  **Bias and error from the healthcare system perspective** · Bias and error of exposures and
  outcomes · How a patient's exposure might be misclassified · How a patient's outcome could be
  misclassified · Electronic medical record data · Claims data · Pharmacy · Surveillance
  datasets and Registries · Population health data sets · A framework to assess if a data
  source is useful · Wrap Up
- **M3 «Representing time, and timing of events, for clinical data mining»** (12 видео):
  Introduction · Time, timelines, timescales and representations of time · Timescale: Choosing
  the relevant units of time · What affects the timescale · Representation of time · Time series
  and non-time series data · Order of events · Implicit representations of time · Different ways
  to put data in bins · Timing of exposures and outcomes · **Clinical processes are
  non-stationary** · Wrap Up
- **M4 «Creating analysis ready datasets from patient timelines»** (18 видео): Turning clinical
  data into something you can analyze · Defining the unit of analysis · Using features and the
  presence of features · How to create features from structured sources · Standardizing
  features · Dealing with too many features · The origins of missing values · Dealing with
  missing values · Summary recommendations for missing values · Constructing new features ·
  Examples of engineered features · When to consider engineered features · Main points about
  creating analysis ready datasets · Structured knowledge graphs · So what exactly is in
  a knowledge graph · What are important knowledge graphs · How to choose which knowledge graph
  to use · Wrap Up
- **M5 «Handling unstructured healthcare data: text, images, signals»** (19 видео):
  Introduction to unstructured data · What is clinical text · The value of clinical text ·
  What makes clinical text difficult to handle · Privacy and de-identification · A primer on
  Natural Language Processing · Practical approach to processing clinical text · Summary –
  Clinical text · Overview and goals of medical imaging · Why are images important? · What are
  images? · A typical image management process · Summary – Images · Overview of biomedical
  signals · Why are signals important? · What are signals? · What are the major issues with
  using signals? · Summary – Signals · Wrap Up
- **M6 «Putting the pieces together: Electronic phenotyping»** (11 видео): Introduction to
  electronic phenotyping · Challenges in electronic phenotyping · Specifying an electronic
  phenotype · Two approaches to phenotyping · Rule-based electronic phenotyping · Examples of
  rule based electronic phenotype definitions · Constructing a rule based phenotype definition ·
  Probabilistic phenotyping · Approaches for creating a probabilistic phenotype definition ·
  Software for probabilistic phenotype definitions · Wrap Up
- **M7 «Ethics»** (7 видео): Introduction to Research Ethics and AI · The Belmont Report:
  A Framework for Research Ethics · Ethical Issues in Data sources for AI · Secondary Uses of
  Data · Return of Results · AI and The Learning Health System · Ethics Summary
- **M8 «Course Conclusion»**

### Курс 3 — «Fundamentals of Machine Learning for Healthcare» (8 модулей, 14 ч)

- **M1 «Why machine learning in healthcare?»** (7 видео): Why machine learning in healthcare? ·
  History of AI in Medicine · Course Overview · Why Healthcare Needs Machine Learning ·
  Machine Learning Magic · Machine Learning, Biostatistics, Programming ·
  **«Can Machine Learning Solve Everything?»**
- **M2 «Concepts and Principles… part 1»** (8 видео): Machine Learning Terms, Definitions, and
  Jargon Part 1 / Part 2 · How Machines Learn Part 1 / Part 2 · Supervised Machine Learning
  Approaches: Regression and the «No Free Lunch» Theorem · Other Traditional Supervised Machine
  Learning Approaches · Support Vector Machine (SVM) · Unsupervised Machine Learning
- **M3 «Concepts and Principles… part 2»** (10 видео): Introduction to Deep Learning and Neural
  Networks · Deep Learning and Neural Networks · Cross Entropy Loss · Gradient Descent ·
  Representing Unstructured Image and Text Data · Convolutional Neural Networks · Natural
  Language Processing and Recurrent Neural Networks · The Transformer Architecture for
  Sequences · Commonly Used and Advanced Neural Network Architectures · Advanced Computer
  Vision Tasks and Wrap-Up
- **M4 «Evaluation and Metrics for machine learning in healthcare»** (5 видео): Introduction to
  Model Performance Evaluation · Overfitting and Underfitting · Strategies to Address
  Overfitting, Underfitting and Introduction to Regularization · Statistical Approaches to Model
  Evaluation · Receiver Operator and Precision Recall Curves as Evaluation Metrics
- **M5 «Strategies and Challenges in Machine Learning in Healthcare»** (9 видео): Introduction
  to Common Clinical Machine Learning Challenges · **Utility of Causative Model Predictions** ·
  **Context in Clinical Machine Learning** · Intrinsic Interpretability · Medical Data
  Challenges in Machine Learning Part 1 / Part 2 · How Much Data Do We Need? ·
  **Retrospective Data in Medicine and «Shelf Life» for Data** · Medical Data: Quality vs Quantity
- **M6 «Best practices, teams, and launching your machine learning journey»** (6 видео) —
  **это и есть единственный модуль по человеческому фактору во всей специализации:**
  Clinical Utility and Output Action Pairing · Taking Action – Utilizing the OAP Framework ·
  Building Multidiciplinary Teams for Clinical Machine Learning *[sic]* · Governance, Ethics,
  and Best Practices · **«On Being Human in the Era of Clinical Machine Learning»** (8 мин) ·
  **«Death by GPS and Other Lessons of Automation Bias»** (5 мин).
  Материалы для чтения: Study Guide Module 6 · Citations and Additional Readings ·
  Video Image Credit · **Recommended Reading for Ethics** (15 мин)
- **M7 «Foundation models (Optional Content)»** (8 видео, 97 мин): Introduction to Foundation
  Models · Adapting to Technology · General AI and Emergent Behavior · How Foundation Models
  Work · Healthcare Use Cases for Text Data · Healthcare Use Cases for Non-textual Unstructured
  Data · **Challenges and Pitfalls** · Conclusion
- **M8 «Course Conclusion»**

### Курс 4 — «Evaluations of AI Applications in Healthcare» (8 модулей, 11 ч)

- **M1 «AI in Healthcare»** (10 видео): Learning Objectives · Common Definitions · Overview ·
  Why AI is needed in Healthcare · Examples of AI in Healthcare · Growth of AI in Healthcare ·
  Questions Answered by AI · AI Output · **«Think beyond area under the curve»** · Recap
- **M2 «Evaluations of AI in Healthcare»** (15 видео): Learning Objectives · Recap: Framework ·
  Stakeholders · **Clinical Utility** · **Outcome: Action Pairing, An Overview** ·
  **Lead Time** · Type of Action · OAP Examples · **Number Needed to Treat** ·
  **Net Benefits** · **Decision Curves** · Feasibility overview · **Implementation Costs** ·
  **Clinical Evaluation and Uptake** · Summary
- **M3 «AI Deployment»** (19 видео): Learning Objectives · The Problem · Practical Questions
  Prior to Deployment · Deployment Pathway · Design and Development · Stakeholder Involvement ·
  Data Type and Sources · Settings · In Silico Evaluation · **«Net Utility & Work Capacity»** ·
  Statistical Validity · **«Care Integration, Silent Mode»** · Clinical Integration,
  Considerations · Technical Integration · Deployment Modalities · Continuous Monitoring and
  Maintenance · Challenges of Deployment · **Sepsis Example** · Summary
- **M4 «Downstream Evaluations of AI in Healthcare: Bias and Fairness»** (18 видео): Learning
  Objectives · Real World Examples of AI Bias · Introduction – Types of Bias · Historical Bias ·
  Representation Bias · Measurement Bias · Aggregation Bias · Evaluation Bias ·
  **Deployment Bias** · What is algorithmic Fairness · Anti-classification · Parity
  Classification · Calibration · Applying Fairness Measures · Lack of Transparency ·
  Minimal Reporting Standards · Opportunities and Challenges · Summary
- **M5 «The Regulatory Environment for AI in Healthcare»** (18 видео): Learning Objectives ·
  The Problem · International Definitions Used for Regulatory Purposes · Definition Statement &
  Risk Framework · Valid Clinical Association · Analytical Evaluation · Clinical Evaluation ·
  General Control · de novo Notifications · Software Modification · TPLC ·
  **Locked vs Adapted AI solutions** · Examples · Non-Regulated Products · EU Regulations ·
  Chinese Guidelines · OMB Guidelines · Summary
- **M6 «Best Ethical Practices for AI in Health Care»** — только тексты (3): Problem
  Formulation · Identifying Conflicts of Interest · Mitigating Conflicts of Interest
- **M7 «AI and Medicine (Optional Content)»** (9 видео): Introduction: Navigating the
  Intersections of AI and Medicine · Life Cycle of AI · A Deep Dive into Historical and Societal
  Dimensions · Race-Based Medicine and Race-Aware Approach · Bias Mitigation Strategies ·
  Exploring Potentials and Ethical Quandaries · Dismantling Race-Based Medicine · Deploying AI
  into Healthcare Settings · Conclusion
- **M8 «Course Wrap Up»**

### Курс 5 — «AI in Healthcare Capstone» (5 модулей, 11 ч)
M1 «Getting Started, Phase 1: Data Collection» · M2 «Phase 2: Model Training Part 1» ·
M3 «Phase 3: Model Training Part 2» · M4 «Phase 4: Model Evaluation» · M5 «Phase 5: Model
Deployment and Regulation, Wrap Up». Каждый модуль — текст + 2 оцениваемых проекта
+ 2 взаимных проверки.

### Чтение и приговор по рубрике «ж»

**Обязательное чтение есть, но названия закрыты.** В каждом модуле курсов 2–4 есть материал,
названный буквально «**Citations and Additional Readings**»; в курсе 3 модуль 6 добавляет
«**Recommended Reading for Ethics**». Содержимое доступно только записавшимся — **ни одного
названия статьи достать не удалось, и выдумывать я их не буду. Это пустая клетка, не догадка.**

**Отдельного модуля по взаимодействию человека и модели НЕТ.** Вся тема во всей
пятикурсовой специализации — это **четыре позиции**:
- «**Death by GPS and Other Lessons of Automation Bias**» (5 минут, курс 3 модуль 6) —
  **единственный материал про искажение решения под подсказкой во всей программе.** Сплошной
  поиск по страницам всех пяти курсов по шаблону
  `automation bias|deskill|skill decay|over-reliance|alert fatigue|human-AI team|anchoring|
  complacency|vigilance` даёт **ровно одно совпадение — это оно**;
- «On Being Human in the Era of Clinical Machine Learning» (8 минут);
- «Net Utility & Work Capacity» и «Care Integration, Silent Mode» (по 2 минуты, курс 4
  модуль 3) — угол нагрузки и надзора.

**Падение квалификации, якорение на подсказке и усталость от оповещений не встречаются
ни в одном названии.**

**Обратите внимание на название единственного материала про automation bias:** он назван
по бытовому отказу автомобильного навигатора («Death by GPS»), а не по клиническому случаю.
Пятиминутное видео с бытовой метафорой — это весь объём, который ведущая медицинская школа
США отводит на искажение врачебного решения под подсказкой в курсе на 97 тысяч человек.

**Соседняя, не-Coursera программа Стэнфорда:** «Applications of Machine Learning in Medicine
Program» (`[ПРОЧИТАНО через Wayback]`
https://web.archive.org/web/20250627172435/https://online.stanford.edu/programs/applications-machine-learning-medicine-program),
ведёт Nigam Shah. Всего два курса, разбивки по модулям нет:
**«Data Foundations for Machine Learning in Medicine»** (XMLPH110, 10 ч) и
**«Model Development, Deployment, and Ethical Considerations»** (XMLPH210, 10 ч).

## 23. Johns Hopkins

### 23a. Школа общественного здоровья Bloomberg — официальный каталог 2026-27

**Прочитано:** https://e-catalogue.jhu.edu/public-health/ `[ПРОЧИТАНО целиком, 7786 строк
после снятия тегов]`. Заголовок дословно: «Bloomberg School of Public Health | 2026-27 Edition».
*(`publichealth.jhu.edu/courses` — 403 и для curl, и для WebFetch; его копия в Wayback
`web/20260908070328` открывается, но сам указатель отрисовывается на JS и строк курсов
не отдаёт. `course.jhsph.edu` отвечает, но закрыт входом.)*

**Курса под названием «Artificial Intelligence in Public Health» в школе НЕТ** — поиск точной
строки по полному тексту каталога даёт ноль. **Это проверенное отрицание, а не пустая выдача
поиска.** Полный набор курсов с ИИ в названии, дословно из каталога:

| Номер | Точное название | Кредиты |
|---|---|---|
| PH.140.618 | AI Programming in Python for Public Health. | 2 |
| PH.140.629 | AI for Public Health in Python. | 4 |
| PH.140.644 | Statistical Machine Learning: Methods, Theory, and Applications. | 4 |
| PH.140.650 | AI Methods for Geospatial Data. | 3 |
| PH.140.690 | Artificial Intelligence for Improved Patient Outcomes. | 1 |
| PH.140.697 | AI Tools for Data Science and Statistics. | 1 |
| PH.340.611 | Using Generative Artificial Intelligence (AI) to Improve Public Health. | 1 |
| PH.340.621 | Using Generative Artificial Intelligence (AI) to Improve Public Health. | 1 |
| PH.340.631 | Practical Skills in Using Generative Artificial Intelligence (GenAI) in Public Health. | 2 |
| PH.550.610 | Using Generative Artificial Intelligence (AI) to Improve Public Health. | 1 |
| PH.550.616 | Critical Thinking About Artificial Intelligence (AI) and Public Health. | 2 |
| PH.220.612 | IH Professional Seminar Series: AI in Global Health. | 1 |
| PH.221.684 | Transforming Health Systems Research through Artificial Intelligence. | 3 |
| PH.221.696 | Introducing AI in Clinical Settings. | 2 |
| PH.224.600 | Applied Artificial Intelligence for the Social, Behavioral and Mental Health Sciences. | 3 |

Курсов серии 280.xxx по ИИ не существует. Описание PH.220.612 в каталоге явно устаревшее
и шаблонное (рассказывает про résumé, сопроводительные письма и LinkedIn, а не про ИИ) —
привожу как есть.

**Школа публикует только описания курсов, без разбивки по модулям или неделям** — это свойство
каталога, подтверждено по всем 15 строкам. Три самых близких описания, дословно:

- **PH.140.690 «Artificial Intelligence for Improved Patient Outcomes» (1 кр.):** «Equips
  students with the essential skills to build and evaluate AI and predictive modeling tools in
  medicine… **Addresses the limits of AI's potential to benefit patients** and presents
  actionable insights to overcome these challenges.»
- **PH.221.696 «Introducing AI in Clinical Settings» (2 кр.):** «Introduces health professionals
  to the fundamentals of artificial intelligence (AI) in clinical settings… **Emphasizes change
  management, risk mitigation, and ethical considerations such as medical liability and job
  displacement.** Develops a solution to an AI-related challenge at their workplace…»
- **PH.550.616 «Critical Thinking About Artificial Intelligence (AI) and Public Health»
  (2 кр.):** «Provides an interactive forum for discussion about key emerging topics in AI and
  public health. Strengthens critical thinking skills with a focus on AI and health. Supplements
  AI skills-based courses by encouraging students to think more deeply about key topics.» —
  **перечня тем не опубликовано**, открытого силлабуса найти не удалось.

**Искажение решения, падение квалификации, усталость от оповещений, измеренная работа пары:
НОЛЬ вхождений во всём каталоге 2026-27.** Сплошной поиск по шаблону
`automation bias|deskilling|skill decay|over-reliance|alert fatigue|human-AI|human-in-the-loop|
anchoring|cognitive bias` по всем 7786 строкам даёт **одно** совпадение, и оно **не в курсе
по ИИ**: это курс по поведенческой экономике здоровья, где перечислены «framing and anchoring,
mental accounting… heuristics and biases». Самое близкое из курсов по ИИ — формулировка
«**job displacement**» у PH.221.696.

### 23b. JHU на Coursera — «Introduction to Using Generative AI in Public Health»

**Прочитано целиком:** https://www.coursera.org/learn/generative-ai-to-improve-public-health
Ведёт **Brian Klaas**. 3 модуля, 2535 записавшихся. Это сетевая версия PH.340.611 / 550.610.

- **M1 «The How and What? of Generative AI»** (11 видео, 155 мин): ChatGPT · Claude ·
  Microsoft Copilot & Comparison · General AI · Generative AI · Current Approaches, Current
  Problems · Prompt Engineering · **Truth** · **Bias** · **Sociocultural Harms** ·
  **Confabulations**
- **M2 «Applying Generative AI to Public Health Research and Practice»** (7 видео, 144 мин):
  Education/Learning · Brainstorming · Data Analysis · How Faculty Are Using Generative
  Artificial Intelligence in Their Work · The Future of Generative Artificial Intelligence for
  Use in Public Health Research · Case Studies of Generative AI in Public Health Research:
  Digital Global Health and Bioethics · Getting Involved in Public Health Research With
  Generative AI. **Названная литература:** «AI Assisted Causal Effect Estimation» ·
  «Simulations for Social Science Experiments» · «Generating Novel Research Ideas» ·
  «Activity: Teach Yourself Using AI»
- **M3 «The Future of Generative AI: Ethical and Big Picture Considerations»** (1 видео,
  37 мин): Areas of Future Concern. **Названная литература: «AI and Trust».**

Модуля по взаимодействию человека и модели нет. По искажению решения, падению квалификации,
чрезмерному доверию и усталости от оповещений — ноль. Единственная позиция из семейства
«доверие» — текст «**AI and Trust**» (название открыто, содержание закрыто).

Отдельно проверено: партнёрская страница https://www.coursera.org/partners/jhu **не содержит**
никакой специализации JHU «AI in Healthcare» — ссылка «AI in Healthcare Specialization»
в её подвале это общесайтовая реклама **стэнфордской** специализации.

### 23c. JHU Engineering for Professionals (инженерная школа Whiting)

**Курса под названием «Artificial Intelligence in Medicine» в EP не существует**, и ничто
в серии 585.xxx по биомедицинской инженерии ему не соответствует. Проверено по полному
официальному перечню
https://e-catalogue.jhu.edu/engineering/engineering-professionals/applied-biomedical-engineering/
`[ПРОЧИТАНО целиком, перечислены все 60+ строк EN.585.xxx]`. Единственный курс по ИИ в 585.xxx:

**EN.585.649 «Artificial Intelligence and Machine Learning for Global Health» (3 кр.)** —
дословно: «…foundational course in AI for Global Health… does not require prior background in
machine learning or global public health. It takes a unique approach by teaching foundational
machine learning topics using case studies and real-life data from global health innovation
projects across Africa, South Asia, and Latin America. Students will learn machine learning
topics alongside **weekly case studies involving datasets from projects on Malaria, Maternal
Health, Neonatal Health, Primary Health Care, Cancer, and more.**… **Prerequisites: Programming
knowledge in a high-level language such as Python.**»
Также в серии: EN.585.719 Sparse Representations in Computer Vision and Machine Learning ·
EN.585.771 Biomedical Data Science · EN.585.783 Introduction to Brain-Computer Interfaces.

**Настоящий курс EP про ИИ в здравоохранении лежит в программе по ИИ, а не в биомедицине:**

**EN.705.617 «Artificial Intelligence in Healthcare» (3 кр.)** —
https://e-catalogue.jhu.edu/engineering/engineering-professionals/artificial-intelligence/
`[ПРОЧИТАНО]` + https://web.archive.org/web/20251015083601/https://ep.jhu.edu/courses/705617-artificial-intelligence-in-healthcare/
`[ПРОЧИТАНО через Wayback; напрямую ep.jhu.edu — 403]`.
Следующий набор — **весна 2026**; сетевой асинхронный; 5455 долларов;
**ведут Ian McCulloh и Daniel Byrne**. Описание дословно: «…Structured around real-world
healthcare workflows, students will explore how artificial intelligence can be integrated to
enhance clinical decision-making, improve operational efficiency, and support patient outcomes…
from predictive modeling and clinical decision support to **robotic process automation** and the
responsible use of large language models… They then build and evaluate AI models that augment
clinical reasoning, such as risk scoring and diagnostic support. The course also explores the
application of generative AI to medical documentation and patient communication and culminates
in the implementation of robotic and process automation tools to **streamline healthcare
workflows**…» **Понедельного плана не опубликовано** — ссылка «Syllabus» закрыта входом.

Близкие курсы той же программы (описания прочитаны по тому же адресу каталога):
- **EN.705.614 «AI and Human Relationships»** — дословно: «…examines how artificial
  intelligence is reshaping human relationships in areas that have traditionally relied on human
  presence—such as companionship, teaching, therapy, management, and collaboration. Students
  will explore **when AI enhances human connection and when it substitutes for or undermines
  it**… AI in workplace relationships, including **algorithmic management, performance
  monitoring**, and HR systems…»
- **EN.705.612 «Values and Ethics in Artificial Intelligence»** (включает «**technological
  unemployment**») · **EN.705.613 «Responsible AI»** · **EN.705.640 «Cognitive and Behavioral
  Foundations for Artificial Intelligence»** · **EN.705.714 «Artificial Intelligence in
  Biology – Cancer Detection & Drug Development»** · **EN.705.716 «AI Systems for Life Sciences»**
- **EN.520.659 «Machine Learning for Medical Applications»** в EP существует (подтверждено
  через Wayback CDX и снимок 23.01.2025, где видно только «Course Number 520.659»). Описание
  **достать не удалось** — тело снимка обрезано, а Архив Интернета ушёл в недоступность прежде
  чем удалось взять другой срез. **Открытый пробел, помечаю честно.**

### 23d. JHU Malone Center — «Data Science for AI in Healthcare»

**Прочитано через Wayback** `[ПРОЧИТАНО]`:
https://web.archive.org/web/20250426051818/https://malonecenter.jhu.edu/ai-course/
*(живой сайт — 403 и для curl, и для WebFetch).*
**Кому, дословно:** «designed for **clinicians and engineers** who would like to learn more
about machine learning and artificial intelligence and their applications in health care.»
Требований нет. Финансирование — грант DELTA ректората JHU. Ведут Swaroop Vedula,
Mathias Uberath, Anand Malpani, Brian Caffo, Greg Hager.
**Оговорка:** на этом снимке статус набора — «will be live this fall», то есть версия
**до запуска**.

**Полный силлабус, дословно:**
- Module 1: Terminologies
- Module 2: Fundamentals of Data Science
- Module 3: Anatomy of Research Studies
- Module 4: Case Study
- **Module 5: When Machines Don't Work**
- Module 6: Interpretable AI in Healthcare
- Module 7: Society & AI in Healthcare

Разбивки по занятиям нет. Названная литература на странице одна: «Reznick, et. al. Task Force
Report on Artificial Intelligence and Emerging Digital Technologies. Royal College of Physicians
and Surgeons of Canada» — цитируется в обоснование того, что ИИ стал «new fundamental
competency for healthcare providers».
**Модуль 5 — про режимы отказа модели, а не про человеческий фактор**; слов про искажение
решения и падение квалификации на странице нет.

### 23e. JHU ExecEd — «AI for Improved Patient Outcomes» (однодневный)

**Прочитано через Wayback** `[ПРОЧИТАНО]`:
https://web.archive.org/web/20251214201006/https://engineering.jhu.edu/ExecEd/course/ai-for-improved-patient-outcomes/
*(живая страница — 403).* Даты: 14.01.2026 и 17.04.2026, 1365 долларов, 6,25 часа
AMA PRA Cat-1. Ведёт **Daniel Byrne** (бывший руководитель исследований ИИ в Вандербильте).
**Кому, дословно:** «Physician-scientists eager to build and test AI tools · Biomedical
informatics professionals · Biostatisticians interested in AI · Nursing leaders and
researchers · Chief Medical Informatics Officers · Healthcare executives and administrators
evaluating AI vendors · Entrepreneurs in the AI healthcare space.»
**Перечня занятий нет**, только цели. Но формулировки целей прямо по нашей теме, дословно:
«improving outcomes, **reducing clinician workload**»; «addressing common challenges such as
**regression to the mean, label leakage, and misinterpreted accuracy metrics**»; «identify
clinically valuable AI applications aimed at enhancing patient safety and **reducing clinician
burnout**»; «**cut through marketing hype**».

### 23f. ★ JHU + Great Learning — «AI and Agentic AI in Healthcare»: единственная программа с модулем про переезд нагрузки

**Прочитано целиком:** https://online.lifelonglearning.jhu.edu/jhu-ai-in-healthcare-certificate-program
**Версия:** действующий набор, «Application closes on 15th Oct 2026»; отзывы слушателей
датированы сентябрём 2026. 10 недель сетевого обучения, 6 CEU, **без требований
к программированию**. Ведут **Ian McCulloh** (директор исполнительного и профессионального
образования по ИИ в JHU) и **Daniel Byrne** — те же двое, что читают EN.705.617.

**Заявленные результаты программы включают, дословно:**
> «**Analyze human baselines, prospect theory, status quo bias, and risk-based approaches in
> clinical workflows**»
> «**Lead through the shift from manual task execution to human-in-the-loop and human-on-the-loop
> agent supervision**»

**Полная программа, дословно:**
- **PRE-WORK — HISTORY OF AI IN HEALTHCARE**
- **MODULE 1: FOUNDATIONS OF AI FOR HEALTHCARE**
  - WEEK 1: AI IN HEALTHCARE: FOUNDATIONS AND FRAMEWORKS
  - WEEK 2: UNDERSTANDING THE BUILDING BLOCKS OF AI IN HEALTHCARE
- **MODULE 2: AI FOR INTELLIGENT DECISION SUPPORT** — описание модуля дословно: «…Participants
  will **analyze the human baseline concept in AI, risk-based approaches, and psychological
  factors such as prospect theory and status quo bias**. The module also covers AI's role in
  **managing information overload**… and the challenges associated with **AI biases and human
  oversight**.»
  - **WEEK 3: AI FOR CLINICAL DECISION SUPPORT** — «…explore the concept of the **human
    baseline** in AI, comparing it to risk-based approaches while considering **manual processes
    and the effects of prospect theory and status quo bias**…»
  - **WEEK 4: LARGE LANGUAGE MODELS AND THE SHIFT TO AGENTIC AI** — «…how LLMs and Agents
    automate administrative tasks, facilitate patient interactions, and **reduce clinician
    burnout**, while also evaluating **LLM limitations such as reliability gaps, training-data
    bias, and the need for human oversight**… A case study on the move from ambient scribes to
    agentic documentation workflows…»
  - **WEEK 5: AUTOMATION, ROBOTICS, AND AGENTIC AI IN HEALTHCARE** — «…Using a structured
    evidence rubric, participants evaluate agentic deployments against accuracy thresholds,
    **select appropriate oversight tiers, and work through the human-in-the-loop and
    human-on-the-loop spectrum, along with common failure modes**, and regulatory fit…»
- **MODULE 3: AI FOR POPULATION HEALTH AND DISEASE MANAGEMENT**
  - WEEK 6: AI FOR IMPROVED HEALTH OUTCOMES · WEEK 7: LEARNING BREAK ·
    WEEK 8: DESIGNING PREVENTIVE HEALTHCARE STRATEGIES
- **MODULE 4: AI BUSINESS STRATEGY FOR HEALTHCARE**
  - **WEEK 9: HEALTH DATA, ETHICS, AND AGENTIC AI GOVERNANCE** — «…**accountability in
    multi-agent workflows**… the **audit trails** these systems require…»
  - **WEEK 10: CHANGE MANAGEMENT AND THE SHIFT TO AGENT SUPERVISION** — «…The week also covers
    the **workforce shift from task execution to agent supervision, including trust-building in
    human-agent teams, override protocols, and monitoring the performance of deployed agents**.
    A case study on this transition guides participants in developing a practical care team
    transition plan.»
- **MASTERCLASS 1: AI PROJECT MANAGEMENT AND DESIGN** · **MASTERCLASS 2: FUTURE TRENDS IN AI
  AND HEALTHCARE** · **MASTERCLASS 3: AI-POWERED PRE-VISIT CLINICAL RISK ASSESSMENT USING n8n**

**Названные разборы случаев, дословно:** «AI-Assisted COVID-19 Detection Using Chest X-Rays»
(DeepCOVID-XR | COVID-Net | Qure.ai; Grad-CAM) · «From Ambient Scribes to Agentic Documentation
Workflows» · «Evaluating an Agentic Prior Authorization Tool» · «Governing Multi-Agent AI Across
Healthcare Systems» · **«From Task Execution to Agent Supervision»** — «Explore how care teams
shift from executing tasks to supervising agents, covering **trust-building in human-agent
teams, override protocols, and performance monitoring of deployed agents**.»

**Приговор по нашему вопросу.** Это **единственная программа всей разведки, у которой есть
модуль, названный про переезд нагрузки на надзор** — «WEEK 10: CHANGE MANAGEMENT AND THE SHIFT
TO AGENT SUPERVISION». Но подана она как **управление изменениями и надзор за агентами, а не
как искажение решения или падение квалификации**: буквальных слов «automation bias»,
«deskilling», «skill decay» и «alert fatigue» на странице **нет вообще** (проверено поиском;
при этом 11 вхождений «oversight», по 2 на «human-in-the-loop» и «human-on-the-loop», 1 на
«clinician burnout»). Психология решения присутствует, но заведена через **теорию перспектив
и склонность к сохранению текущего положения**, а не через якорение на подсказке модели.
**Обязательного списка литературы не опубликовано.**

### 23g. Что достать не удалось (по JHU)

- **Силлабусы Malone Center помимо §23d:** `malonecenter.jhu.edu` живым отдаёт 403; страница
  `/ai-course/` — единственная найденная с силлабусом. Для адреса
  `ep.jhu.edu/courses/585631-artificial-intelligence-in-medicine/` в Wayback снимков нет
  (`archived_snapshots: {}`) — что согласуется с тем, что такого курса в каталоге нет.
- **`bme.jhu.edu/.../ai-in-medicine-for-medical-trainees/`** (направление магистратуры
  «AI in Medicine» в биомедицинской инженерии JHU): живым 403, в Wayback никогда
  не архивировалось (`archived_snapshots: {}`). О существовании известно **ТОЛЬКО ИЗ СНИППЕТА**
  выдачи (название «AI in Medicine - Johns Hopkins Biomedical Engineering»). Перечень курсов
  не получен.

## 24. University of Michigan — «Data Augmented Technology Assisted Medical Decision Making» (DATA-MD)

Это **самый близкий к курсу о суждении** из всех найденных курсов для врачей, и потому самый
показательный.

**Прочитано целиком:**
https://www.coursera.org/learn/data-augmented-technology-assisted-medical-decision-making
Ведёт **Cornelius James**. 4 модуля, 18 заданий, начальный уровень.
**Версия, дословно:** «This activity is released for CME credit on **07/30/2024** and expires
06/31/2027» *[sic]*; 3,5 часа AMA PRA Cat-1.
**Кому, дословно:** «created with the needs of **medical students, residents, fellows,
practicing physicians, advanced practice providers, and registered nurses** in mind. Others,
like educators, computer programmers, and data scientists, may also find value.»
Рамка курса, дословно: «The **National Academy of Medicine (NAM)** recommends ensuring that
clinicians can effectively use technology – including AI – to improve the diagnostic process.»
Выступающие: **Maggie Makar, Benjamin Li, Nicholson Price, Karandeep Singh**.

- **M1 «Introduction to Artificial Intelligence and Machine Learning»** (17 видео, 71 мин):
  Welcome to the Course · Welcome to Module 1 · Meet A.I.L.A. · What Is Big Data? · Locating the
  Data and Datasets · AI/ML in Health Care · Meet Professor Maggie Makar · What is ML? ·
  Methodologies · Supervised Learning · Unsupervised Learning · Reinforcement Learning ·
  Deep Learning · How Models Are Developed: Part 1 / Part 2 / Part 3 ·
  **Challenges With Model Development**. Тексты: Course Syllabus · Pre-Course Survey · Meet Your
  Instructor · CME Information · **Bibliography** · Module 1 Lecture Notes
- **M2 «Foundational Biostatistics and Epidemiology in AI/ML for Health Care Professionals»**
  (15 видео, 57 мин): Welcome to Module 2 · Evidence-Based Medicine (EBM) · **Overlap of EBM,
  AI, and ML** · **The Diagnostic Process** · Clinical Questions · Correlation vs. Causation ·
  Hypothesis Testing · Confidence Intervals · Frequency Measures · Probability and Bayesian
  Statistical Analysis · Bayes Theorem · Likelihood Ratios · How Do We Evaluate Predictive
  Models? · Introduction to ROC Curves · **Calibration**.
  **Вопрос к обсуждению, дословно: «What are some concerns that you have about using machine
  learning in clinical practice?»**
- **M3 «Using AI/ML to Augment Diagnostic Decisions»** (14 видео, 81 мин): Welcome to Module 3 ·
  Clinical Case: Part 1 · The Diagnostic Process · **Critical Appraisal** · Validity of the
  Results (Part 1 / Part 1 Continued / Part 2 / Part 2 Continued) · What Are the Results? ·
  Clinical Case: Part 2 · **Do Results Apply?** (×3) · **Monitoring Performance**.
  **Названная обязательная литература, дословно: «Core Reading: Assessment of Accuracy of an
  Artificial Intelligence Algorithm to Detect Melanoma in Images of Skin Lesions»** +
  Bibliography + Module 3 Lecture Notes. Задания: Module 3 Graded Assignment ·
  **Diabetic Retinopathy Case**
- **M4 «Ethical and Legal Use of AI/ML in the Diagnostic Process»** (15 видео, 75 мин):
  Welcome to Week 4 · Medical Ethics · Data Availability · Data Collection and Curation ·
  Meet Professor Nicholson Price · Patient Privacy and Data · Data Ownership · Goals of
  Governance Key Stakeholders · Sources and Dimensions of Algorithmic Bias ·
  **Bias and Performance Over Time** · **«Clinician Response to Bias»** (2 мин) · Transparency ·
  **«Who Is Liable When Something Goes Wrong?»** (8 мин) · **«Trust»** (3 мин) ·
  Takeaways For Providers.
  **Вопрос к обсуждению, дословно: «What factors will influence your trust in AI-based
  technologies designed for use in health care?»**

**Приговор.** DATA-MD — курс для врачей, построенный вокруг **диагностического процесса**
и **критической оценки** (M3 это по сути разбор «применимы ли результаты к моему пациенту»).
И при этом **отдельного модуля по взаимодействию человека и модели в нём нет.** Вся тема —
четыре коротких позиции: «Clinician Response to Bias» (2 мин), «Trust» (3 мин), «Who Is Liable
When Something Goes Wrong?» (8 мин), «Monitoring Performance» (6 мин) — плюс два вопроса
к обсуждению про доверие и опасения.
Сплошной поиск по странице по шаблону `automation bias|deskilling|skill decay|over-reliance|
alert fatigue|human-AI team|anchoring|complacency` — **ноль совпадений.**
Обязательное чтение есть, и **одно название открыто** (работа про точность алгоритма
распознавания меланомы); содержимое помодульных «Bibliography» закрыто — **пустая клетка,
не догадка.**

Проверено и отсеяно: «AI for Energy and Biomedical Applications» (UMich,
https://www.coursera.org/learn/ai-for-energy-biomedical-applications, `[ПРОЧИТАНО]`) — три
модуля, из них по медицине только «AI in Medical Imaging, Genomics, and Drug Discovery»;
по человеческому фактору ничего. Партнёрская страница https://www.coursera.org/partners/umich
**не содержит** специализации «AI in Healthcare»; курсы «AI for Healthcare» (ведёт «AI CERTs
Team») и «AI Technologies in Healthcare» — **не мичиганские**, проверено открытием страниц.

## 25. DeepLearning.AI «AI for Medicine» (Pranav Rajpurkar и др.)

**Прочитано целиком:** https://www.coursera.org/specializations/ai-for-medicine и страницы
`/learn/ai-for-medical-diagnosis`, `/learn/ai-for-medical-prognosis`,
`/learn/ai-for-medical-treatment`.

**Версия:** дата выпуска на страницах **не указана** (нет медицинской аккредитации — нет
и отметки о сроке). 58 678 записавшихся на специализацию, 96 212 на первый курс.
**Преподаватели (из JSON страницы): Eddy Shyu, Pranav Rajpurkar, Amirhossein Kiani,
Bora Uyumazturk**; Andrew Ng появляется в видео.
**Кому и требования, дословно:** «Intermediate level»; «No prior medical expertise is
required!»; «a working knowledge of **deep neural networks, particularly convolutional
networks, and proficiency in Python programming at an intermediate level** will be essential.»

### Курс 1 — «AI for Medical Diagnosis» (3 раздела)
**W1 «Disease Detection with Computer Vision»** (20 видео): Welcome to the Specialization with
Andrew and Pranav · Demo · Recommended Pre-requisites · Medical Image Diagnosis · Eye Disease
and Cancer Diagnosis · Building and Training a Model for Medical Diagnosis · Training,
Prediction, and Loss · Image Classification and Class Imbalance · Binary Cross Entropy Loss
Function · Impact of Class Imbalance on Loss Calculation · Resampling to Achieve Balanced
Classes · Multi-Task · Multi-task Loss, Dataset size, and CNN Architectures · Working with
a Small Training Set · Generating More Samples · Model Testing · Splitting Data by Patient ·
Sampling · **Ground Truth and Consensus Voting** · Additional Medical Testing.
**W2 «Evaluating Models»** (10 видео): Sensitivity, Specificity and Evaluation Metrics ·
Accuracy in Terms of Conditional Probability · Sensitivity, Specificity and Prevalence ·
PPV, NPV · Confusion Matrix · ROC Curve and Threshold · Varying the Threshold · Sampling from
the Total Population · Confidence Intervals · 95% Confidence Interval.
**W3 «Image Segmentation on MRI Images»** (10 видео): Medical Image Segmentation · MRI Data and
Image Registration · Segmentation · 2D U-Net and 3D U-Net · Data Augmentation for Segmentation ·
Loss Function for Image Segmentation · **Different Populations and Diagnostic Technology** ·
**External Validation** · **Measuring Patient Outcomes** · Congratulations!

### Курс 2 — «AI for Medical Prognosis» (4 раздела)
**W1 «Linear Prognostic Models»** (11 видео): Course 2 Intro · Prerequisites and Learning
Outcomes · Medical Prognosis · Examples of Prognostic Tasks · Atrial Fibrillation · Liver
Disease Mortality · Risk of Heart Disease · Risk Score Computation · Evaluating Prognostic
Models · Concordant Pairs, Risk Ties, Permissible Pairs · C-Index.
**W2 «Prognosis with Tree-based Models»** (15 видео): Decision Trees for Prognosis · Decision
Trees · Dividing the Input Space · Building a Decision Tree · How to Fix Overfitting · Survival
Data · Different Distributions · Missing Data Example · Missing Completely at Random · Missing
at Random · Missing Not at Random · Imputation · Mean Imputation · Regression Imputation ·
Calculate Imputed Values.
**W3 «Survival Models and Time»** (16 видео): Survival Models · Survival Function · Valid
Survival Functions · Collecting Time Data · When a Stroke is Not Observed · Heart Attack Data ·
Right Censoring · Estimating the Survival Function · Died Immediately, or Never Die · Somewhere
in-between · Using Censored Data · Chain Rule of Conditional Probability · Deriving Survival ·
Calculating Probabilities from the Data · Comparing Estimates · Kaplan Meier Estimate.
**W4 «Build a Risk Model Using Linear and Tree-based Models»** (24 видео): Hazard Functions ·
Hazard · Survival to Hazard · Cumulative Hazard · Individualized Predictions · Relative Risk ·
Ranking Patients by Risk · Individual vs Baseline Hazard · Smoker vs Non-smoker · Effect of Age
on Hazard · Risk Factor Increase Per Unit Increase in a Variable · Risk Factor Increase or
Decrease · Intro to Survival Trees · Survival Tree · Nelson Aalen Estimator · Comparing Risks
of Patients · Mortality Score · Evaluation of Survival Model · Permissible and Non-Permissible
Pairs · Possible Permissible Pairs · Example of Harrell's C-Index · Example of Concordant
Pairs · Week 4 Summary · Congratulations!

### Курс 3 — «AI for Medical Treatment» (3 раздела)
**W1 «Treatment Effect Estimation»** (12 видео): Intro to Course 3 · About Course 3 ·
**Absolute Risk Reduction** · Randomized Control Trials · Causal Inference · Average Treatment
Effect · Conditional Average Treatment Effect · T-Learner · S-Learner · Evaluate Individualized
Treatment Effect · C-for-benefit · C-for-benefit Calculation.
**W2 «Medical Question Answering»** (10 видео): Medical Question Answering · Handling Words
with Multiple Meanings · Define the Answer in a Text · Automatic Label Extraction for Medical
Imaging · Synonyms for Labels · Is-a Relationships for Labels · Presence or Absence of
a Disease · Evaluating Label Extraction · Precision, Recall and F1 Score · Evaluating on
Multiple Disease Categories.
**W3 «ML Interpretation»** (9 видео): Drop Column Method · Permutation Method · Individual
Feature Importance · Shapley Values · Combining Importances · Shapley Values for all Patients ·
Interpreting CNN Models · Localization Maps · Heat Maps.

**Приговор.** **Ни модуля, ни занятия, ни практикума, ни текста по взаимодействию человека
и модели во всей специализации нет.** Сплошной поиск по страницам всех четырёх курсов
по шаблону `automation bias|deskill|skill decay|over-reliance|alert fatigue|human-AI team|
human-in-the-loop|anchoring|oversight|workload|complacency` — **ноль совпадений.**
Это чисто инженерная программа «как построить». Ближайшее к нашей теме у неё — не поведенческое,
а гносеологическое: «Ground Truth and Consensus Voting», «External Validation», «Measuring
Patient Outcomes» и весь раздел W3 про интерпретируемость. В каждом курсе есть текст,
названный буквально «**Citations**», содержание закрыто — **пустая клетка, не догадка.**

### Сводка по части III

| Программа | Есть ли модуль, посвящённый рубрике «ж»? | Что есть вместо |
|---|---|---|
| Stanford AI in Healthcare (Coursera, 2023) | **Нет** | 2 занятия в К3-М6: «Death by GPS and Other Lessons of Automation Bias» (5 мин), «On Being Human in the Era of Clinical Machine Learning» (8 мин); + «Net Utility & Work Capacity» и «Care Integration, Silent Mode» в К4-М3 |
| Каталог JHU BSPH (2026-27) | **Нет** | Ничего. Ноль вхождений по всему каталогу; ближайшее слово — «job displacement» (PH.221.696) |
| JHU Coursera (GenAI в общественном здоровье) | **Нет** | Один текст — «AI and Trust» |
| JHU Malone «Data Science for AI in Healthcare» | **Нет** | Модуль 5 «When Machines Don't Work» — режимы отказа, не человеческий фактор |
| **JHU + Great Learning «AI and Agentic AI in Healthcare»** | **ДА — единственная в разведке** | «WEEK 10: CHANGE MANAGEMENT AND THE SHIFT TO AGENT SUPERVISION» + нед. 3 (теория перспектив, склонность к сохранению текущего, «human baseline») + нед. 5 (уровни надзора) + разбор «From Task Execution to Agent Supervision» |
| JHU EP EN.705.617 AI in Healthcare | Неизвестно (силлабус закрыт) | В описании про это молчок; у соседнего EN.705.614 «AI and Human Relationships» есть «когда ИИ подменяет и подрывает» и «алгоритмическое управление» |
| Michigan DATA-MD (2024) | **Нет** | «Clinician Response to Bias» (2 мин), «Trust» (3 мин), «Who Is Liable When Something Goes Wrong?» (8 мин), «Monitoring Performance» (6 мин), 2 вопроса к обсуждению |
| DeepLearning.AI AI for Medicine | **Нет** | Ничего |

**Два вывода, которые стоит унести в лекцию.**
**(а) Искажение решения под подсказкой встречается ровно один раз на ~130 опубликованных
модулей этой части разведки** — одним пятиминутным видео Стэнфорда, названным по отказу
бытового навигатора. То есть образцовые учебные программы по клиническому ИИ подробно учат
оценивать модель и почти не учат поведению врача.
**(б) Единственная программа, построившая на этом модуль, переформулировала тему как «надзор
за агентами» и «управление изменениями»** (JHU/Great Learning, неделя 10) — это угол нагрузки
надзора, а не угол падения квалификации.
**Падение квалификации, усталость от оповещений и якорение на подсказке — отсутствуют
по названию во всех перечисленных программах.**
Все списки литературы, которые закрыли бы вопрос окончательно (стэнфордские «Citations and
Additional Readings» ×14 и «Recommended Reading for Ethics»; мичиганские «Bibliography» ×4;
«Citations» ×3 у DeepLearning.AI), закрыты записью на курс; во всей этой части разведки
**открыты всего два названия** — мичиганская работа про точность распознавания меланомы
и «AI and Trust» у JHU.

---

# Часть IV. Российские программы

**Общий итог вперёд:** найдено **6 программ и курсов с дословно опубликованной структурой**.
**Ни в одной нет темы про искажение решения под подсказкой, якорение, падение квалификации
или переезд нагрузки на арбитраж.** Ближайшее — одна шестичасовая тема «Этические аспекты
и роль человека» у Сеченова, про содержание которой публично ничего не известно, и обязательный
общеуниверситетский модуль «Культура ИИ» у ИТМО (не медицинский).

## 26. ⭐ Сеченовский университет — ДПО «Специалист по искусственному интеллекту и анализу данных в медицине»

Лучшая российская находка: полный учебный план с часами по каждой теме.

**Прочитано** (`[ПРОЧИТАНО]`, 2026-10-14):
- страница Цифровой кафедры: https://www.sechenov.ru/univers/structure/institute/institut-biodizayna-i-modelirovaniya-slozhnykh-sistem/tsentr-tsifrovoy-meditsiny/tsifrovaya-kafedra-/
- **учебный план PDF** (`[PDF ПРОЧИТАН, текстовый слой]`):
  https://www.sechenov.ru/upload/iblock/978/9ydi6p29mbcldvcexc5y6z6ndun2toq8/Uchebnyy-plan-Spetsialist-po-II_na-sayt.pdf

**Подразделение:** Институт цифрового биодизайна и искусственного интеллекта в медицине,
Центр цифровой медицины и ИИ в медицине. Проект «Цифровые кафедры» (приказ Минобрнауки № 169
от 25.02.2025 — **план актуален на 2025/2026**). Профессиональная переподготовка, **256 часов**.
**Кому:** студенты бакалавриата, магистратуры и специалитета вуза, то есть преимущественно
**медики, получающие дополнительное ИТ-образование**. Требований к подготовке на странице нет.

### Полный учебный план (дословно, с часами)

**Модуль 1. Основы искусственного интеллекта — 16 ч**
1. Тема 1. Введение в искусственный интеллект и его роль в медицине — 2 ч
2. Тема 2. Обзор технологий искусственного интеллекта — 2 ч
3. Тема 3. Медицинские данные и работа с ними — 3 ч
4. Тема 4. Обучение моделей и извлечение знаний из медицинских данных — 3 ч
5. Тема 5. Применение ИИ в медицине: от диагностики до администрирования — 2 ч
6. Тема 6. ИИ в отраслях медицины: практические примеры — 2 ч
7. Промежуточное тестирование по теме — 2 ч

**Модуль 2. Управление информационными проектами и ресурсами — 32 ч**
1. Тема 1. Введение в управление проектами — 6 ч
2. Тема 2. Инициация и планирование проекта — 6 ч
3. Тема 3. Методы и подходы управления проектами — 6 ч
4. Тема 4. Экономика проекта — 6 ч
5. Тема 5. Управление рисками и качеством проекта — 6 ч
6. Промежуточное тестирование по теме — 2 ч

**Модуль 3. Аналитика данных — 38 ч**
1. Тема 1. Введение в медицинскую аналитику и инструменты для работы с данными — 10 ч
2. Тема 2. Анализ и визуализация медицинских данных — 10 ч
3. Тема 3. Разведочный анализ данных (EDA) в медицине — 8 ч
4. Тема 4. Статистический анализ — 8 ч
5. Промежуточное тестирование по теме — 2 ч

**Модуль 4. Машинное обучение — 40 ч**
1. Тема 1. Основы машинного обучения — 6 ч
2. Тема 2. Обучение с учителем — 6 ч
3. Тема 3. Обучение без учителя — 6 ч
4. Тема 4. Валидация данных и оценка моделей — 6 ч
5. Тема 5. Оптимизация гиперпараметров модели — 6 ч
6. Тема 6. Машинное обучение без программирования — 6 ч
7. Промежуточное тестирование по теме — 4 ч

**Модуль 5. Глубокое обучение и нейронные сети — 40 ч**
1. Тема 1. Введение в нейронные сети — 6 ч
2. Тема 2. Языковые модели и обработка медицинских текстов — 6 ч
3. Тема 3. Компьютерное зрение в медицине — 6 ч
4. Тема 4. Безкодовые инструменты для ИИ в медицине — 6 ч
5. Тема 5. Как обучают модели и оценивают их работу — 6 ч
6. **Тема 6. Этические аспекты и роль человека — 6 ч**
7. Промежуточное тестирование по теме — 4 ч

Практическая работа — 22 ч · Самостоятельная работа — 46 ч · Итоговая аттестация — 22 ч ·
**Итого 256 ч**

**Рубрика «ж»:** единственная близкая позиция — **«Тема 6. Этические аспекты и роль человека»,
6 часов из 256, то есть 2,3% программы**. Что именно внутри — **не раскрыто**: рабочая
программа дисциплины не опубликована, в учебном плане только название и часы.
**Назвать это темой про искажение решения под подсказкой я не могу** — формулировка говорит
про «роль человека» в общем виде, и это надо держать как пустую клетку, а не как попадание.
**Литература:** в опубликованном плане её нет вообще — ни основной, ни дополнительной.

Соседние программы той же Цифровой кафедры (планы лежат рядом, не разбирались): «Специалист
по телемедицинским технологиям и дистанционному мониторингу состояния здоровья», «Разработчик
решений виртуальной и дополненной реальности в медицине».

**Технические оговорки, пригодятся при перепроверке:** `sechenov.ru` блокирует обычный curl
(«Доступ к сайту sechenov.ru запрещён»), проходит с браузерным `User-Agent`.
**`digitalmed.sechenov.ru` не существует — NXDOMAIN.** Страница
`/univers/structure/institute/institut-tsifrovoy-meditsiny/` отдаёт 404: института
с таким названием нет, он называется «Институт цифрового биодизайна и искусственного
интеллекта в медицине».

## 27. Сеченовский университет — магистратура 09.04.02 «Информационные системы и технологии в медицине»

**Прочитано:**
- учебный план (скан PDF, прочитан постранично как изображение):
  https://www.sechenov.ru/upload/iblock/667/297tlwddhm22i3k2db4eqlnc2houio5x/InSiT_o_2_2020_UP-2959.pdf
- ОПОП (текстовый PDF, через Wayback, `[ПРОЧИТАНО целиком]`):
  https://web.archive.org/web/20241212201230/https://www.sechenov.ru/sveden/education/programs/000000002959%2009.04.02.pdf
- реестр: https://www.sechenov.ru/sveden/education/eduaccred/

**Версия плана: год набора 2020/2021**, период освоения 01.09.2020 — 31.08.2022, утверждён
Учёным советом 20.01.2021, протокол № 1. Очная, 2 года, 120 з.е.
**Кому:** ФГОС ВО 09.04.02 плюс профстандарт «06.016 Руководитель проектов в области
информационных технологий» — то есть **технари, выпускники ИТ-бакалавриата**. Медицинская
подготовка не требуется и не упоминается.

**Блок 1, обязательная часть (45 з.е.), дословно и по порядку:**
1. О.1 Автоматизированное построение расчетных сеток в биомедицинских приложениях — 3 з.е.
2. О.2 Теория оптимизации — 6
3. О.3 Арифметико-логические основы и схемотехника ЭВМ — 6
4. О.4 Суперкомпьютеры — 3
5. О.5 Искусственный интеллект — 6
6. О.6 Архитектура микропроцессорных систем и средств — 6
7. О.7 Конструкторское проектирование и технология производства БИС и СБИС — 6
8. О.8 Стандартизация программных средств и информационных технологий — 3
9. О.9 Управление программными проектами — 6

**Часть, формируемая участниками (9 з.е.):** 10. УОО.1 Иностранный язык для научного
общения — 3 · 11. УОО.2 Защита информации — 6
**Элективные (6 з.е.):** 12. Телемедицина / Наукометрия — 3 · 13. Защита прав интеллектуальной
собственности / Вычислительные системы, сети и телекоммуникации — 3
**Блок 2. Практика (48 з.е.):** Технологическая практика (учебная) — 3 · Научно-исследовательская
работа — 42 · Технологическая практика — 3
**Блок 3. ГИА (12 з.е.):** Выполнение и защита выпускной квалификационной работы — 12
**ФТД. Факультативы:** Нейронные сети — 3

**Рубрика «ж»: НЕТ ни одной темы.** Литература в учебном плане не публикуется (она в РПД;
для этой программы выложена лишь одна РПД).

### Проверяемая находка: у действующей версии этой программы план не открывается

В том же реестре есть **более новая направленность — «09.04.02 Информационные системы
и технологии, Интеллектуальные информационные технологии в медицине»**. Её ссылки
на «Учебный план», «Описание образовательной программы» и все РПД ведут на пути вида
`/_files_aup/aup/UP/81c42738-afdf-11f0-b04d-0050568800ad`. **Проверено 6 таких ссылок —
все отдают HTTP 404.** Старые ссылки того же реестра (`/upload/iblock/...`) работают.
То есть структура актуальной программы «Интеллектуальные информационные технологии
в медицине» **фактически не опубликована**: ссылки на неё в разделе «Сведения
об образовательной организации» битые.

### Магистратура 2025 с Депздравом Москвы — только пресс-релиз

Программа «Информационные системы и технологии» с 01.09.2025, занятия в Центре цифровой
медицины, практика в учреждениях ДЗМ. **Перечень дисциплин есть только в пресс-релизе,
не в учебном плане**, и он неполный — «среди ключевых дисциплин», дословно:

> федеральные информационные подсистемы здравоохранения, защита информации в медицинских
> информационных системах, управление изменениями при внедрении цифровых технологий
> в здравоохранении, цифровые сервисы здравоохранения, технологии разработки и сопровождения
> программного обеспечения, матричные методы для сжатия и анализа данных, программная инженерия

Источник (`[ПРОЧИТАНО]`): https://www.cnews.ru/news/line/2025-05-20_sechenovskij_universitet
**Кому:** «выпускники бакалавриата и специалитета ИТ-направлений… а также специалисты
с медобразованием» — **смешанно**.

## 28. ⭐ НИУ ВШЭ — «Большие данные и машинное обучение в медицине» (Medical Informatics)

**Прочитано:** https://www.hse.ru/edu/courses/836732681 `[ПРОЧИТАНО целиком]`

Курс по выбору магистерской программы **«Науки о данных (Data Science)»**, 01.04.02 Прикладная
математика и информатика, факультет компьютерных наук, Департамент анализа данных
и искусственного интеллекта. **2-й курс, 1–2 модуль. Язык английский. 6 кредитов,
50 контактных часов.** Преподаватель — **Пьяных Олег Станиславович** (Harvard Medical School /
Massachusetts General Hospital). Версия силлабуса — **2023/2024**.
**Кому:** технари, магистранты прикладной математики и анализа данных.

### Содержание курса (дословно, по порядку)

1. Introduction: What is MI, and what it is not
2. Standards: Overview and HL7
3. Standards: DICOM
4. Making sense of standards
5. Computed tomography; Image enhancement
6. **Computer-Aided Diagnostics (CAD)**
7. Networking and teleradiology
8. Security
9. Scheduling and queuing
10. Simulation/Modeling in Medicine
11. Clinical software development; Medical startups
12. Medical startups
13. Unusual applications

**Оценивание, дословно:** `0.8 * Class homework/projects, assigned after each lecture
+ 0.2 * Exam`

**Литература — дословно, вся, какая есть:**
- Recommended Core Bibliography: Pianykh, O. S. *Digital imaging and communications in medicine
  (DICOM): a practical introduction and survival guide.* Springer Science & Business Media,
  2009. 417 pp.
- Recommended Additional Bibliography: Pianykh O. S. *Digital Image Quality in Medicine.*
  Springer International Publishing, 2014. 140 pp.

То есть вся литература курса — **две книги одного автора (он же преподаватель), обе про DICOM
и качество изображений**. Работ про искажение решения, падение квалификации или совместную
работу человека и модели нет.
**Рубрика «ж»: НЕТ.** Тема 6 «Computer-Aided Diagnostics (CAD)» — про сами системы
автоматизированной диагностики, а не про поведение врача рядом с ними.

**Оговорка:** полная версия силлабуса с почасовым тематическим планом лежит за кнопкой
«Full Syllabus» на https://dp.hse.ru/#/summary?implementationId=8207844434 — **доступ закрыт
капчей** (API `/api/i/summary/` переадресует на `/captcha`), прочитать не удалось.

## 29. ⭐ НИУ ВШЭ — «Информационно-аналитические технологии в здравоохранении»

Единственный найденный российский курс **для управленцев и медиков**, где опубликован полный
тематический план.

**Прочитано:** https://www.hse.ru/ma/health/courses/918957435.html `[ПРОЧИТАНО целиком]`
Хлебные крошки страницы: магистерская программа «Управление и экономика здравоохранения» →
Учебные курсы → «**Информационно-аналитические технологии в здравоохранении 2024 и 2025
учебного года**». Факультет социальных наук. Курс по выбору, русский.
Автор — **Алмазов Андрей Александрович**.
**Кому:** магистранты управления и экономики здравоохранения — **управленцы и медики**,
не технари.

### Содержание дисциплины (дословно, по порядку)

1. Тема 1. Общие принципы формирования и развития информационно-коммуникационных систем
   в социальной сфере и здравоохранении России и зарубежных стран: сравнительный анализ.
2. Тема 2. Единая государственная информационная система в сфере здравоохранения.
3. Тема 3. Личный кабинет пациента/здоровья, электронные копии медицинской документации,
   цифровой след и цифровые данные индивидуума.
4. Тема 4. Дистанционная медицина (телемедицина).
5. Тема 5. Цифровая зрелость медицинской организации, методика оценки. **Информационная
   квалификация и навыки персонала.**
6. Тема 6. Информационные системы и планирование, проектное управление.
7. Тема 7. Управленческий учет в медицинской организации, расчет реальной себестоимости
   медицинских услуг, первичный учет, управление маршрутизацией пациента и ресурсами,
   управление отношениями с пациентами, поддержка комплексных программ ведения пациента.
8. Тема 8. Присутствие в интернете и социальных сетях (сайты, программы продвижения,
   информационные каналы и мессенджеры), «интернет знаний» как следующий этап развития общей
   информационно-коммуникационной среды.
9. Тема 9. Правовое регулирование отношений в сфере информационных технологий и вопросы
   информационной безопасности.
10. Тема 10. Информационные аналитические технологии в вопросе управления и сохранения
    статуса здоровья индивидуума.
11. Тема 11. Проблематика использования информационно аналитических технологий в социальном
    и коммерческом страховании. Цифровые двойники в здравоохранении.
12. **Тема 12. Экспертные системы и системы поддержки принятия врачебных решений.**
13. Тема 13. Биоинформатика. Введение в тему.
14. Тема 14. Онтологии и семантика в здравоохранении. AI vs Онтологии. Управление знаниями.
15. Тема 15. Презентация и обсуждение индивидуальных и групповых проектов.

Из аннотации: магистрант должен знать «основные принципы использования и **границы
применимости** современных ИТ-технологий в медицине и здравоохранении» и «принципы создания
и применения систем поддержки принятия врачебных решений».
**Оценивание, дословно:** `0.2 * Итоговый экзамен + 0.2 * Эссе на заданную тему
+ 0.4 * Тематический доклад (мини-группа 3-5 чел) + 0.1 * Активность на занятиях`

**Рубрика «ж»:** ближайшее — **«Тема 12. Экспертные системы и системы поддержки принятия
врачебных решений»**, но она про сами системы, не про поведение врача. Тема 5 содержит оборот
«Информационная квалификация и навыки персонала» — это про **ИТ-грамотность сотрудников,
а не про падение клинической квалификации**, путать нельзя. **Темы про искажение решения
под подсказкой, якорение или арбитраж нет.**

### Отдельная находка: поле «обязательная литература» заполнено мусором

В блоке «Рекомендуемая основная литература» на этой странице опубликовано, дословно (первые
позиции):

> `!Bien dicho!, Pinilla, R., 2005` · `!Continuemos! : intermediate Spanish, Jarvis, A. C.,
> 2003` · `!Hola, amigos!, Jarvis, A. C., 2004` · `!Yo soy el Che! : el hombre visto desde
> adentro, Ortega, L., 2009` · `"A nation of a hundred million idiots"? : a social history
> of Japanese television, 1953-1973, Chun, J. M., 2009` …

и далее, уже по делу: «Экономика и управление в здравоохранении: учебник и практикум для
вузов», Решетников А. В., 2017 · «Проектное управление в сфере информационных технологий»,
Грекул В. И., 2015 · «Проектирование информационных систем», Коваленко В. В., 2012.
В дополнительной: «Блеск и нищета информационных технологий: почему ИТ не являются
конкурентным преимуществом», Карр Н. Дж., 2005 · «Biomedical computing: digitizing life
in the United States», November J., 2012.

Строка проверена в исходном HTML — это **именно опубликованный текст страницы**, а не ошибка
разбора. Похоже на автоматическую подстановку из библиотечного каталога по алфавиту.
**Формально обязательная литература есть; содержательно значительная её часть к дисциплине
отношения не имеет.** Для нашей лекции это хороший материал сам по себе: поле «обязательная
литература» заполнено и не значит ничего.

## 30. НИУ ВШЭ — магистратура «Анализ данных в биологии и медицине» (ФКН)

**Прочитано:** https://www.hse.ru/ma/adbm/courses `[ПРОЧИТАНО целиком]` — заголовок страницы
«**Учебные курсы 2026/2027 учебного года**»; плюс https://www.hse.ru/ma/adbm/

Академический руководитель Попцова М. С., научный руководитель Гельфанд М. С.
25 бюджетных и 10 платных мест, русский и частично английский.
**Кому — дословно:** «Магистратура предназначена для бакалавров в области прикладной
математики и/или анализа данных и специалистов, работающих в области наук о жизни…».
Два входа: прикладная математика и анализ данных (ВШЭ, МГУ, МФТИ и др.) **либо** биологи
и медики. Вступительное испытание — конкурс портфолио с собеседованием. **Смешанно.**

**Полный перечень курсов 2026/2027 (дословно, в порядке страницы):**
1. Алгоритмы в биоинформатике — обязательный, русский
2. Анализ данных секвенирования 1 — по выбору, русский
3. Sequencing Data Analysis 2 — обязательный, английский
4. Биоинформатические методы в исследованиях происхождения — по выбору, русский
5. Введение в молекулярную биологию — по выбору, русский
6. Генетические технологии в персонализированной медицине — по выбору, русский
7. Глубинное обучение — обязательный, русский
8. Machine Learning in Bioinformatics — обязательный, английский
9. Методы моделирования пространственной структуры протеинов — обязательный, русский
10. Молекулярное моделирование — по выбору, русский
11. Основы программирования в R и Python — обязательный, русский
12. Практическая биоинформатика — обязательный, русский
13. Прикладная статистика — обязательный, русский
14. Семинар наставника «Анализ данных в биологии и медицине» — обязательный, русский (две записи)
15. Современные методы в молекулярной биологии — по выбору, русский
16. Сравнительная геномика — по выбору, русский
17. Фармацевтическая информатика — по выбору, русский

**Рубрика «ж»: НЕТ ни одной темы.** Программа чисто биоинформатическая — клинического
применения и живого врача в ней нет вовсе.

## 31. НИУ ВШЭ — магистратура «Управление и экономика здравоохранения» (ФСН)

**Прочитано:** https://www.hse.ru/ma/health/courses `[ПРОЧИТАНО целиком]` —
«**Учебные курсы 2026/2027 учебного года**»

**Полный перечень (дословно):**
1. Бизнес планирование деятельности медицинской организации — по выбору
2. **Информационно-аналитические технологии в здравоохранении** — по выбору *(разобран в §29)*
3. Медицинское страхование и страхование здоровья — по выбору
4. Научно-исследовательский семинар — обязательный (две записи)
5. Организация и экономика здравоохранения — обязательный
6. Организация и экономика здравоохранения - 2 — по выбору
7. Правовое обеспечение государственного и частного здравоохранения — обязательный
8. Семинар наставника — обязательный (две записи)
9. Теория и механизмы государственного управления — обязательный
10. Управление и экономика социальной сферы — обязательный
11. Управление качеством в здравоохранении — по выбору
12. Управление лекарственным обеспечением — по выбору
13. Управление медицинскими и страховыми организациями — обязательный
14. Управление человеческими ресурсами в здравоохранении — по выбору
15. Ценностно-ориентированное здравоохранение и внедрение инновационных технологий — по выбору
16. Экономика общественного сектора — обязательный

**Всё содержание по ИИ сосредоточено в одной дисциплине по выбору** (№ 2). Рубрики «ж» нет.

## 32. ИТМО — магистратура «Биоинформатика и системная биология»

**Прочитано:**
- https://abit.itmo.ru/program/master/bioinformatics `[ПРОЧИТАНО, данные из встроенного
  `__NEXT_DATA__`]`
- **учебный план 2026** (`[PDF ПРОЧИТАН целиком, текстовый]`):
  https://abitlk.itmo.ru/file_storage/academic_plan/2026/academic_plan_10332_01.04.02.pdf

⚠️ **Оговорка:** по ссылке, которую даёт сама страница (`https://abit.itmo.ru/file_storage/...`),
файл отдаёт **404**; тот же путь на хосте `abitlk.itmo.ru` работает. То есть кнопка «Скачать
учебный план» на сайте абитуриента битая.

**Версия: год набора 2026.** 01.04.02, 120 з.е., английский, Институт прикладных компьютерных
наук. **Кому:** и биологи/медики, и ИТ/математики — первый семестр разводит их по разным
дисциплинам (у биологов математика и программирование, у ИТ-шников биология и статистика).

**Блок 1. Модули — 60 з.е. / 2160 ч (дословно):**
*Профессиональные дисциплины (24 з.е.):* Introduction to Bioinformatics / Введение
в биоинформатику (3, сем. 1) · Scientific Python / Программирование на языке Python для
научных задач (3, сем. 2) · Bioinformatics algorithms / Алгоритмы в биоинформатике (3,
сем. 2) · Transcriptomics / Транскриптомика (3, сем. 2) · Systems Biology / Системная биология
(6, сем. 2) · Medical Genetics / Медицинская генетика (6, сем. 2)
*Профессиональные по выбору (9 з.е.), три пары:* Discrete Mathematics / Дискретная математика
**или** Algorithms and Data Structures · Molecular biology / Молекулярная биология **или**
Programming in Python · Statistics / Статистика **или** Advanced Statistics — все по 3 з.е., сем. 1
*Профильные по выбору (12 з.е., все сем. 3, по 3 з.е.):* Microbial Omics / Омиксные технологии
микроорганизмов · Structural bioinformatics / Структурная биоинформатика ·
Advanced Machine Learning / Машинное обучение (углубленный курс) · Optimization and Sampling ·
Population genetics and genomics · Natural language processing / Обработка естественного языка
*Универсальная (надпрофессиональная) подготовка — 15 з.е.:* **Applied Artificial Intelligence →
AI Culture / Культура ИИ (3 з.е., сем. 1)** · Иностранный язык (6) · Мировоззренческий модуль
(3): Introduction to Conceptual Thinking / Основы концептуального мышления;
**Critical Thinking Skills (Advanced) / Навыки критического мышления (продвинутый уровень)** ·
Предпринимательская культура → MVP to Market · микромодули Soft Skills (Доказательный подход
к управлению карьерой · Публичные выступления · Управление стрессом · Эмпатичная коммуникация ·
**Art & math of decision making / Инструменты принятия решений** · Медиация · Планирование
карьерной траектории) и большие курсы (Emotional Intelligence и др.)

**Блок 2. Практика — 54 з.е.:** Research Work 9+9+9+15 (сем. 1–4) · Research Seminar 3+3 ·
Pre-graduation Internship 6
**Блок 3. ГИА — 6 з.е.** · **Блок 4. Факультативы:** Introduction to Linux ·
Higher Mathematics · **«Как учиться в партнерстве с ИИ» (3 з.е.)** · «Когнитивные ошибки
в понимании людей» · «Введение в киберпсихологию» и ещё около пятидесяти общеуниверситетских

**Рубрика «ж»:** медицинской — **НЕТ**. Есть два неотраслевых попадания: обязательный модуль
**«AI Culture / Культура ИИ»** и факультатив **«Как учиться в партнерстве с ИИ»**. Содержание
ни того, ни другого в учебном плане не раскрыто (только название и часы), рабочие программы
ИТМО публично не отдаёт. **Литература:** в учебном плане ИТМО литературы нет вообще — только
дисциплины, зачётные единицы и часы.

**Отдельной программы «ИИ в медицине» или «Цифровое здравоохранение» у ИТМО найти
не удалось.** Проверено: `abit.itmo.ru/program/master/digital_health` — 404; поиск
по магистратурам; перечень программ в JSON страницы. Единственное медицинское попадание среди
названий — та самая «Биоинформатика и системная биология». **Оговорка: страница перечня
магистратур отрисовывается на клиенте, полный список через её JSON вытащить не удалось —
поэтому это «не нашли», а не «доказано отсутствие».**

## 33. Что по России проверить не удалось и почему

- **openedu.ru («Открытое образование») — платформа лежала.** `https://openedu.ru/course/`
  и `https://openedu.ru/api/v1/courses/` отдают **HTTP 502** с текстом на самой странице:
  «Платформа "Открытое образование" временно недоступна из-за масштабной аварии у облачного
  провайдера». Проверено дважды с интервалом, оба раза 502.
  Обход через Wayback: Архив Интернета по ходу работы уходил в 429, затем в полную
  недоступность, потом частично вернулся. Через CDX API удалось получить около 6000 архивных
  адресов курсов openedu и разложить по организациям: **hse (2039), mephi (1799),
  ITMOUniversity (1099), mipt (501), misis (301), eltech (94), bmstu (70), miit (8), kpfu (5),
  mednet (2), msu (1), spbstu (1)**. Медицинских вузов на платформе в этой выборке нет;
  единственный медицинский адрес — `openedu.ru/course/mednet/ozno/` (снимки 2022 года,
  «Организация здравоохранения и общественное здоровье», не про ИИ). Курса по ИИ в медицине
  с разбивкой по неделям найти не удалось — но, **пока платформа лежит, это «не проверено»,
  а не «не существует».**
- **Полные силлабусы ВШЭ (dp.hse.ru)** — закрыты капчей.
- **Сколтех, МФТИ (Физтех-школа биологической и медицинской физики), РНИМУ им. Пирогова,
  Университет Иннополис, Яндекс Практикум** — **не смотрели**, бюджет ушёл на глубину
  по шести программам выше. Помечаю как пробел разведки.

## Сводка по России

| Программа | Версия | Кому | Тема про человека и модель | Литература про искажение решения / падение квалификации |
|---|---|---|---|---|
| Сеченов, ДПО «Специалист по ИИ в медицине», 256 ч | 2025/26 | медики + ИТ-доп. | «Этические аспекты и роль человека», **6 ч из 256**, содержание не раскрыто | литературы в плане нет вовсе |
| Сеченов, магистратура 09.04.02 | набор 2020 | технари | **нет** | не публикуется |
| Сеченов, «Интеллектуальные информационные технологии в медицине» | действующая | — | **план не опубликован** (6 ссылок → 404) | — |
| ВШЭ, «Большие данные и МО в медицине» | 2023/24 | технари | **нет** | нет (две книги по DICOM одного автора) |
| ВШЭ, «Информационно-аналитические технологии в здравоохранении» | 2024 и 2025 | управленцы, медики | **нет** (есть «Экспертные системы и СППВР» — про системы) | список частью мусорный, нужного нет |
| ВШЭ, «Анализ данных в биологии и медицине» | 2026/27 | смешанно | **нет** | — |
| ВШЭ, «Управление и экономика здравоохранения» | 2026/27 | управленцы | **нет** | — |
| ИТМО, «Биоинформатика и системная биология» | набор 2026 | смешанно | медицинской **нет**; есть общий «Культура ИИ» и факультатив «Как учиться в партнерстве с ИИ» | литературы в плане нет |

---

# Часть V. Выводы

Ниже — сведение по **26 прочитанным программам** (MIT ×5 итераций + HST.953 ×3 + Stanford ×2 +
Harvard ×4 + профессиональный силлабус радиологов + ETH ×2 + Technion ×2 + TUM + Imperial +
Karolinska + NUS + Toronto + UCL + Arizona + Stanford Coursera + JHU ×6 + Michigan +
DeepLearning.AI + Сеченов ×2 + ВШЭ ×4 + ИТМО).

## 34. Что системно ЕСТЬ во всех этих курсах

**1. Методы машинного обучения — половина курса и больше, везде.** Это не уклон отдельных
курсов, а устройство жанра. MIT 2019: 13 лекций из 25. Стэнфорд: 9 из 14. Technion: 26 занятий
подряд от полиномиальной подгонки до свёрточных сетей. Инвариант: **курс «ИИ в медицине» —
это курс машинного обучения, в котором медицина поставляет данные.**

**2. Неизменная тройка «данные → модель → оценка метрик».** Разведочный анализ,
предобработка, пропуски, шум, разметка, обучение, переобучение, подбор гиперпараметров,
ROC-кривая, калибровка. Воспроизводится дословно от MIT до Сеченова независимо от аудитории.

**3. Четыре «человеческие» рубрики, и они везде одни и те же четыре.** Это важнее всего:
каждый курс отводит человеку место — и всегда одно из этих четырёх:
- **интерпретируемость и объяснимость** (MIT, Stanford, Harvard, ETH ×2, TUM, Imperial,
  DeepLearning.AI, Malone) — свойство **модели**;
- **справедливость и смещение в данных** (MIT, Stanford, Harvard, Stanford Coursera целым
  модулем из 18 видео) — свойство **данных**;
- **этика, приватность, согласие** (почти все) — свойство **процедуры**;
- **регуляторика и ответственность** (MIT, Harvard, Stanford Coursera, Arizona, KI, TUM) —
  свойство **организации**.

**Ни одна из четырёх не является свойством человека, принимающего решение.**

**4. Сдвиг распределения и устаревание модели — зрелая, хорошо поставленная тема.** «Dataset
and temporal shift: detection and mitigation» (MIT), «Domain shift in medical applications»
(TUM), «Bias and Performance Over Time» (Michigan), «Retrospective Data in Medicine and
"Shelf Life" for Data» (Stanford Coursera). Курсы хорошо понимают, что модель портится
со временем.

**5. Приглашённый врач — обязательный элемент, и почти всегда один и тот же жанр.** Technion
(Danny Eytan, Рамбам), TUM («experts from local hospitals and med-tech companies»),
Stanford (Gabriel Brat, Jonathan Chen), MIT (Leo Celi, Andy Beck, Connie Lehman), Toronto
(Robert Grant). Жанр — «как это выглядит в клинике», рассказ о применении. **Не** замер того,
что подсказка делает с решением рассказчика.

**6. Разбор отказов модели есть почти везде — и это отказы модели, а не пары.** «When Machines
Don't Work» (JHU Malone), «Cautionary Tales» (MIT 2025), «Challenges and Pitfalls» (Stanford
Coursera), «Unpredictable, nonhuman failure modes» (силлабус радиологов), «Problems in the
Deployment of Machine-Learned Models in Health Care» (HST.953). Курсы честны про то, что
модель ломается.

**7. Требования к отчётности — быстро растущая тема.** TRIPOD-AI и PROBAST-AI (MIT 2022),
MI-CLAIM и STARD-AI (TUM, HST.953), CHAI Applied Model Card (MIT 2025), Model Cards и Data
Cards (лекция MIT про человека и ИИ), «Minimal Reporting Standards» (Stanford Coursera).

**8. Проектная работа с настоящими данными — почти везде.** MIMIC-III, eICU-CRD, CheXpert,
UK Biobank. Итоговый проект и защита есть у MIT, HST.953, Stanford, ETH, Technion, Toronto,
ИТМО, Сеченова.

## 35. Чего в них системно НЕТ

Это главный результат разведки. Четыре отсутствия, и все четыре — ровно то, на чём стоит
наша Лекция 7.

### 35.1. Измеренного случая, где пара «человек + модель» хуже каждой стороны по отдельности

**Нет ни в одном из 26 курсов.** Это не пробел в чтении: я проверил **единственный измеренный
случай пары, который вообще преподаётся** (Tschandl et al., читается в MIT с 2022 по 2025) —
и его собственный вывод **противоположный**: «good quality AI-based support of clinical
decision-making **improves diagnostic accuracy over that of either AI or physicians alone**».

Курсы предъявляют студенту **двоичную картину**: подсказка либо помогает (исправная модель),
либо вредит (неисправная модель — «faulty AI can mislead the entire spectrum of clinicians,
including experts»). **Третьего исхода — исправная модель, грамотный врач, и пара всё равно
хуже — в учебной картине мира нет.**

Ближайшее, что встречается, и оба раза это не то:
- слайд 17 деки MIT: внутри области передачи решения модель делает 3 ошибки, человек — 5
  (то есть передавать человеку хуже, чем не передавать) — но это про **неправильно
  спроектированный порог**, а не про пару как таковую;
- слайд 29 деки MIT: новички страдают от плохой модели сильнее всех — опять **плохая модель**.

### 35.2. Измеренного падения квалификации

**Нет нигде. И это не «мало» — это ноль по слову.** Сплошные поиски, которые я прогнал лично:

| Где искал | Объём | `deskill` / `skill decay` / `atrophy` |
|---|---|---|
| Список литературы MIT 6.S897 2019 | 1728 слов, ~60 работ | **0** (а `skill` в любой форме — тоже 0) |
| Силлабус радиологов AAPM/ACR/RSNA/SIIM 2025 | 6196 слов | **0** (`skill` в любой форме — 0) |
| Дека лекции Стэнфорда по этике (№ 13) | 57 слайдов | **0** |
| Дека лекции MIT про человека и ИИ (№ 18) | 51 слайд | **0** |
| Дека HST.953 «LLMs in Healthcare» | 33 слайда | **0** |
| Силлабус Arizona для студентов-медиков | 5 страниц | **0** (единственный `skill` — «навыки сотрудничества») |
| Каталог JHU BSPH 2026-27 | 7786 строк | **0** |
| Все 5 курсов специализации Стэнфорда на Coursera | ~130 модулей | **0** |
| Вся специализация DeepLearning.AI (4 курса) | — | **0** |
| 6 российских программ | — | **0** |

**Падение квалификации — не недоразобранная тема. Её в учебных программах не существует
как понятия.** Опыт врача входит в программы ровно один раз — на слайде 29 деки MIT, и там
он **постоянная величина**, модификатор сиюминутной выгоды от подсказки, а не величина,
которая со временем меняется под действием самой подсказки.

### 35.3. Измеренного переезда нагрузки на арбитраж

**Назван структурно в трёх местах, посчитан — ни в одном.**

Что есть:
- **единственный модуль с этим в названии** на всю разведку: JHU + Great Learning,
  «WEEK 10: CHANGE MANAGEMENT AND THE SHIFT TO AGENT SUPERVISION» — и это **управление
  изменениями**, а не замер;
- силлабус радиологов: «Risks of workflow modification» и три режима встраивания
  (новый порядок / усиление / замена) — структурно названо, **`workload` = 0 вхождений**;
- Stanford Coursera: «Net Utility & Work Capacity» и «Care Integration, Silent Mode» —
  по 2 минуты каждое;
- передача решения (learning to defer) у MIT — **математика** выбора, кому отдать случай,
  а не замер того, сколько нагрузки куда переехало.

**А числа при этом в курсах уже лежат — просто без имени и без единицы.** Три замера,
которые я нашёл внутри курсов:
1. **дека HST.953, слайд 23:** рандомизированное исследование, **122 врача**, черновики ответов
   от модели — **время чтения выросло на 21,8%**, время ответа не изменилось, длина выросла
   на 17,9% (Tai-Seale et al., JAMA Netw Open 2024). И там же: «ambient scribes… **do not save
   much time largely due to hallucinations**»; «**may even take more time**»;
2. **дека MIT, слайды 14–15:** модель отказалась читать **20% снимков**, и эти пациенты
   **поехали к офтальмологу** вместо ожидания на месте (Beede et al., CHI 2020);
3. **дека MIT, слайд 28:** одна из двух форм подсказки дала **0% прироста точности
   и +10 секунд** на случай.

Каждое из трёх — переезд нагрузки в чистом виде. **Ни одно не названо переездом нагрузки.**
В деке HST.953 это подано заголовком «Patient Communication – **Mixed Results**», и сплошной
поиск по той деке по словам `workload | arbitrat | human-AI | automation bias` даёт ноль.
**Наша работа в Лекции 7 — не найти числа (они уже опубликованы и даже преподаются),
а дать им имя и единицу.**

### 35.4. Цены обеих ошибок в одних единицах

**Названо один раз на 26 курсов, и адресовано не тому человеку.**

Единственное попадание: силлабус радиологов 2025, роль **Developer**, раздел «Model Evaluation /
Utility Analysis» → «**Asymmetric costs of different error types**». То есть несимметричная
цена ошибок — обязанность **разработчика**, а не врача, который этой моделью пользуется.
В программе роли **User** этого пункта нет.

Везде остальное ложные тревоги и пропуски живут **в разных шкалах и не сводятся**:
чувствительность и специфичность, ROC-кривая, PPV и NPV, FNR −23% против FPR +2%
(дека MIT, диабетическая ретинопатия). Ближайшее к сведению в одну шкалу — Stanford Coursera
курс 4: «Number Needed to Treat», «Net Benefits», «Decision Curves», «Implementation Costs».
Это правильное направление, и оно единственное.

### 35.5. Ещё три отсутствия, которые стоит держать в голове

- **Якорение на подсказке не названо нигде** как искажение решения. Вместо него работают два
  других языка: «мысленная модель» и пара «over-reliance / under-reliance» (дека MIT), либо
  «теория перспектив и склонность к сохранению текущего положения» (JHU/Great Learning).
  Механизм описан, но как **ошибка проектирования интерфейса** или как **общая психология
  решений**, не как якорение на конкретной подсказке.
- **Усталость от оповещений (alert fatigue) — ноль по названию во всех 26 курсах.**
  Единственный близкий артефакт во всём своде — глава 27 учебника MIT Critical Data
  «Signal Processing: False Alarm Reduction», и это **инженерное подавление ложных тревог
  в реанимации**, а не разбор того, что они делают с человеком.
- **Самое дешёвое наблюдение и самое говорящее:** в списке литературы курса-эталона MIT 2019
  слово `clinician` встречается **дважды, и оба раза это название модели** («The Artificial
  Intelligence Clinician»). А в деке стэнфордской лекции по этике на 57 слайдов слово
  `clinician` встречается **ноль раз**.

## 36. Четыре наблюдения про устройство, которые сильнее любого отдельного пробела

**1. Тема есть у инженеров и отсутствует у медиков — ровно наоборот нужному.**
Два курса одной школы, читаются одним сообществом:
- **MLHC / HST.956** — аудитория EECS MIT, зачитывается как квалификационный курс по ИИ
  для информатиков. **Лекция про человека и модель есть, стоит с 2021 года
  и не пропадала ни в одной итерации.**
- **HST.953** — 93 слушателя, из них **две трети — три четверти медики** из Гарвардской
  медицинской школы и школы общественного здоровья. Есть целый раздел «Implementation»,
  пять работ про внедрение. **Лекции про человека и модель нет. Ни одной работы по нашим
  рубрикам в списке литературы нет.**

При этом MLHC числится **предварительным курсом** для HST.953. То есть формально медик, дойдя
до HST.953, лекцию уже прослушал. Фактически требование записано как
`(6.7900 and 6.7930) or permission of instructor` — а медики из Гарварда проходят
по «permission of instructor».
Тот же разрыв у Гарварда: AIM 2 (весна 2026) **заявляет целью** «Understand how AI systems
interact with medical and research workflows» и «What does it take to deploy an AI system
**without adding burden** or introducing new safety risks?» — и не имеет ни лекции,
ни обязательной работы об этом; «Human-AI evaluation loops» существует как **один пункт
в тематической строке занятия про обработку языка**.
И у Arizona: курс обещает подготовить студента-медика к работе с ИИ **с первого дня
интернатуры**, домашнее задание недели 2 требует «оценить предсказания ИИ на настоящих
клинических сценариях» — и ни одного слова про то, как подсказка сдвигает его решение.

**2. У темы нет обязательного чтения — даже там, где есть лекция.** Хронология лекции MIT:
2022 — чтения нет вовсе; 2023 — чтения нет; 2024 — Tschandl задан по-настоящему;
2025 — **Tschandl закомментирован в разметке и не задаётся**. За четыре итерации обязательное
чтение было **один раз**. У лекции про справедливость обязательное чтение было все четыре года.
В стэнфордской специализации на 97 тысяч человек вся тема — **одно пятиминутное видео**,
названное по отказу автомобильного навигатора («Death by GPS»), а не по клиническому случаю.

**3. Чем свежее программа, тем меньше публикуется — проверять это придётся вручную.**
ETH за весну 2026 выложил 7 недель из четырнадцати (и в майском снимке, снятом в конце
семестра, те же 7 строк). NUS за 2025/26 — описания без расписания. Каталог модулей UCL
перечней занятий **не публикует вообще, по устройству шаблона**. Самый свежий курс KI
(2LA212, решение 17.02.2026) публикует только «Essential data» — без содержания, целей,
литературы и формы контроля. А два полных недельных плана, какие удалось достать, —
2022 и 2024 годов. **Отсюда практическое следствие: любое утверждение «сейчас в вузе X читают
Y» надо подписывать годом версии силлабуса, иначе оно недоказуемо.**

**4. Поле «обязательная литература» может быть заполнено и ничего не значить.** Самый
наглядный случай — страница дисциплины ВШЭ «Информационно-аналитические технологии
в здравоохранении», где в «Рекомендуемой основной литературе» опубликованы, дословно,
`!Bien dicho!`, `!Hola, amigos!`, `!Yo soy el Che!` и социальная история японского
телевидения. Проверено в исходном HTML — это текст страницы, а не ошибка разбора. А у курсов
Coursera наоборот: обязательное чтение есть у всех, но называется «Citations and Additional
Readings» и закрыто записью на курс — во всей части III **открыто всего два названия работ**
из примерно двадцати таких полей.

## 37. Что из этой разведки можно прямо забрать в Лекцию 7

**Приёмы, найденные в живых курсах:**
1. **Karolinska:** модуль «AI in health care» открывается пунктом «**Medical image analysis
   without AI**» — работа без ИИ ставится первым, до той же работы с ИИ. Это наше правило
   «сопоставление без ИИ / с ИИ читается с одного взгляда», найденное в живом курсе
   медицинского университета.
2. **Technion 97248, цель 4:** «**Explain To A Medical Practitioner The Advantages and
   Disadvantages of The Model Versus a Human Physician… The Situations in Which They Recommend
   Using The Model, and The Situations in Which It Is Best to Avoid Using It**» — лучшая
   найденная формулировка цели «когда не надо», из курса, который со-преподаёт работающий
   реаниматолог.
3. **Cai et al. (CSCW 2019), из деки MIT:** патологи просили «**Report AI performance
   on sub-categories of known human pitfalls**» — «у неё хорошая точность, кроме
   периневральной инвазии; увидишь периневральную инвазию — не ведись». Это готовая форма
   подачи: точность модели **на тех случаях, где ошибается человек**.
4. **Mozannar et al. (NeurIPS 2024), оттуда же:** правила на естественном языке — «Rely on the
   AI for patients under the age of 40», «Ignore on the AI whenever x-ray shows a pigtail
   catheters», «Rely on AI whenever AI score is above 95%».

**Три цитаты, которые работают со сцены:**
- **Toronto LMP1210**, оговорка про порождающие модели: «**Overreliance on generative AI may
  give you a false sense of how much you've actually learned**». Курс про ИИ в медицине
  предупреждает о падении квалификации от чрезмерного доверия — **в разделе про академическую
  честность, про себя самого, а не про медицину, которой учит.**
- **NUS MDG5256:** цель курса — «enhance the **safety and efficiency of clinician-AI
  interactions**». Единственный курс из 26, поставивший взаимодействие человека и модели
  в заявленную цель — и не опубликовавший перечня занятий, по которому можно проверить, есть
  ли за целью хоть одно занятие.
- **Beede et al. (CHI 2020), слова медсестры из деки MIT:** «**Some images are blurry, and
  I can still read it, but the system can't.**»

**Числа, готовые к плашкам «было → стало»:**
- **122 врача**, черновики ответов пациентам: время чтения **+21,8%**, время ответа
  без изменений, длина **+17,9%** (Tai-Seale, JAMA Netw Open 2024 — преподаётся в HST.953);
- **155 оценивающих**, рак кожи: многоклассовые вероятности **+13,3% точности, −1 с**;
  похожие изображения **~0% точности, +10 с** (Tschandl, Nature Medicine 2020);
- **TREWS, 5 больниц, 2 года, 9805 случаев:** **89%** срабатываний рассмотрено, **38%**
  подтверждено, подтверждённые в 3 часа дали **−1,85 часа** до первого антибиотика
  (Henry, Nature Medicine 2022 — обязательное чтение MIT 2025);
- **диабетическая ретинопатия, Таиланд:** FNR **−23%**, FPR **+2%**; **20% снимков** модель
  не прочла; эти пациенты **поехали** к офтальмологу (Ruamviboonsuk 2019 + Beede 2020);
- **GPT-4 и чтение записей пациентом, n=200:** на **20%** точнее — «**However, GPT-4
  definitions and answers often contained serious errors!**» (Mannhardt 2024);
- **черновики ответов пациентам:** врачи использовали **20%** черновиков
  (Garcia, JAMA Netw Open 2024).

**Одно предложение, которое стоит произнести со сцены.**
Двадцать шесть прочитанных программ лучших университетов мира. Лекция про то, как подсказка
модели меняет решение врача, есть **в одной** — и та читается информатикам, а не медикам.
Падение квалификации не упоминается **ни в одной** — ноль вхождений слова на всех списках
литературы, каталогах и деках, какие удалось вскрыть. А числа, измеряющие переезд нагрузки,
**уже лежат внутри этих курсов** — под заголовком «смешанные результаты».

