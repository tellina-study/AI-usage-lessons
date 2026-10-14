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

Счёт — по числу лекций/модулей, отнесённых к рубрике целиком (смешанные не считаются,
доли округлены от общего числа содержательных занятий).

| # | Курс | Год | Кому | Лекций | а | б | в | г | д | е | **ж** | Лекция про «ж»? |
|---|------|-----|------|--------|---|---|---|---|---|---|---|---|
| 1 | MIT 6.S897/HST.956 | Spring 2019 | EECS + HST, магистры/PhD | 25 | 4 | 13 | 3 | 1 | 2 | 0 | **0** | **нет** |
| 2 | MIT 6.871/HST.956 | Spring 2022 | EECS + HST, магистры/PhD | 24 | 3 | 12 | 2 | 1 | 2 | 1 | **1** | «Human-AI interaction» |
| 3 | MIT 6.7930/HST.956 | Spring 2021 | то же | 23 | 3 | 12 | 2 | 1 | 1 | 0 | **1** | «Cooperative Decision Making» (Unit 4 «Human Factors») |
| 4 | MIT 6.7930/HST.956 | Spring 2024 | то же | ~24 | — | — | — | — | — | — | **1** | «Human-AI Collaboration in Clinical ML» |
| 5 | MIT 6.7930/HST.956 | **Spring 2025** | то же | 25 | 4 | 11 | 2 | 1 | 2 | 1 | **1** | «Human-AI collaboration in decision making» |
| 6 | Stanford BIODS 220 / CS 271 / BIOMEDIN 220 | Autumn 2020-21 | смешанно, нужен Python+DL | 14 | 2 | 8 | 1 | 0 | 1 | 0 | **0** | **нет** |
| 7 | Stanford BIODS 220 | Autumn 2022-23 | то же | 14 | 2 | 9 | 1 | 0 | 1 | 0 | **0** | **нет** |

Остальные курсы — ниже, по мере того как их планы удалось прочесть (разделы 8+).

**Главный вывод таблицы, который стоит держать в голове при переделке Лекции 7:**
рубрика «ж» — одна лекция из двадцати пяти в лучшем случае, и только в MIT, и только
с 2021 года. У Стэнфорда её нет вовсе. Рубрика «е» (измеренные клинические исходы, испытания)
почти везде нулевая: курсы учат **строить** модель, а не **читать отчёт о том, что вышло
в клинике**.

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

