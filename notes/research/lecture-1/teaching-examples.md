# Как ведущие курсы открывают Lecture 1: анализ и рекомендации

**Дата:** 2026-03-31
**Цель:** Извлечь конкретные приемы из Lecture 1 лучших курсов для проектирования нашей вводной лекции.

---

## 1. Как каждый курс открывается (Lecture 1)

### 1.1 Stanford CS221: Introduction (bottom-up, задачно-ориентированный)

**Что покрывает Lecture 1:**
- Определение AI через набор реальных задач: web search, speech recognition, face recognition, machine translation, autonomous driving, automatic scheduling
- Постановка вопроса: "Что объединяет эти задачи?" -- формализация через модели, состояния, действия
- Введение понятий: reflex-based models vs state-based models vs variable-based models vs logic-based models
- Обзор курса как "карты" -- какие инструменты для каких задач
- Первое домашнее задание (Foundations) выдается сразу

**Педагогический прием:** "Вот реальные задачи, давайте найдем общие принципы" -- индуктивный подход от примеров к абстракциям.

**Источник:** [Stanford CS221](https://stanford-cs221.github.io/spring2024/), [Lecture 1 slides (PDF)](https://web.stanford.edu/class/archive/cs/cs221/cs221.1186/lectures/overview.pdf)

### 1.2 MIT 6.S191: Intro to Deep Learning (foundations-first, энергичный)

**Что покрывает Lecture 1 (69 минут):**
- Мотивация: почему deep learning сейчас -- данные, вычисления, алгоритмы
- Перцептрон как базовый строительный блок
- Полносвязные сети (fully connected networks)
- Функции активации, loss functions
- Алгоритм обратного распространения ошибки (backpropagation)
- Стохастический градиентный спуск (SGD)

**Lab 1 (сразу после):** практическая работа в TensorFlow -- вычисления, определение моделей, автоматическое дифференцирование.

**Педагогический прием:** быстрый темп, энергичная подача, весь фундамент нейросетей за 1 лекцию. "Bootcamp mindset" -- интенсивное погружение. Все видео и слайды бесплатно на YouTube.

**Источник:** [MIT 6.S191](https://introtodeeplearning.com/), [YouTube плейлист](https://www.youtube.com/playlist?list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI)

### 1.3 Harvard CS50 AI: Week 0 -- Search (алгоритмический фундамент)

**Что покрывает Week 0:**
- DFS, BFS -- базовые алгоритмы поиска
- Greedy Best-First Search, A* -- эвристический поиск
- Adversarial Search: Minimax, Alpha-beta pruning

**Почему начинают с Search (педагогическое обоснование):**
1. "You can't run before you walk" -- поиск это фундамент, на котором строятся все остальные темы
2. Search интуитивно понятен: навигатор ищет маршрут, игра выбирает следующий ход
3. Search не требует математической подготовки (в отличие от ML)
4. Задачи Week 0 -- Degrees (6 степеней разделения) и Tic-Tac-Toe -- мотивирующие и наглядные
5. Логическая цепочка курса: Search -> Knowledge -> Uncertainty -> Optimization -> Learning -> Neural Networks -> Language -- каждая тема опирается на предыдущую

**Педагогический прием:** начать с того, что студенты могут понять и запрограммировать за первую неделю, создавая ощущение успеха. Два проекта сразу.

**Источник:** [CS50 AI Week 0](https://cs50.harvard.edu/ai/weeks/0/), [Lecture Notes](https://cs50.harvard.edu/ai/notes/0/)

### 1.4 fast.ai: Lesson 1 -- "Getting Started" (top-down, результат-first)

**Что покрывает Lesson 1:**
- End-to-end пример: обучение модели классификации изображений за 5 минут
- Проект "Is it a bird?" -- создание модели, которая отличает птиц от не-птиц
- Введение в Jupyter Notebook и библиотеку fastai
- Создание моделей на собственных данных
- Концептуальное объяснение transfer learning

**Почему top-down работает:**
- Студент видит результат в первые 5 минут -- модель, которая в 2015 была cutting-edge research
- Мотивация через немедленный успех: "Я уже могу это делать"
- Теория вводится позже, когда студент уже имеет интуицию о том, что происходит
- К уроку 2 студент деплоит модель на Hugging Face Space через Gradio
- Контраст с университетским подходом: "Не нужно 3 семестра математики, чтобы начать"

**Педагогический прием:** "Whole game" -- показать весь процесс целиком, потом разбирать по частям. Как учат играть в футбол: сначала играют, потом разбирают технику.

**Источник:** [fast.ai Lesson 1](https://course.fast.ai/Lessons/lesson1.html), [Forum](https://forums.fast.ai/t/lesson-1-official-topic/95287)

### 1.5 Andrew Ng -- AI for Everyone: Week 1 (нетехнический, аналогии)

**Что покрывает Week 1 "Что такое AI?" (~1 ч 49 мин):**
- Определение Machine Learning и связь с AI/Deep Learning
- Large Language Models -- объяснение для начинающих
- Данные: сбор, типы (структурированные vs неструктурированные)
- Терминология: deep learning, machine learning, data science, AI -- как связаны
- Нейронные сети -- интуитивное объяснение с диаграммами (без формул)
- Что делает компанию "AI-компанией"
- Возможности и ограничения AI (распознавание авто -- да, интерпретация жестов -- нет)
- "1-секундное правило": если человек может решить задачу за 1 секунду, AI вероятно тоже может

**Педагогический прием:** объяснение AI через бизнес-аналогии, полное отсутствие кода, фокус на "что AI может и не может". Множество конкретных примеров из реального бизнеса.

**Источник:** [Coursera: AI for Everyone](https://www.coursera.org/learn/ai-for-everyone)

### 1.6 Google MLCC: первый модуль (модульный, визуальный)

**Что покрывает первый модуль (Linear Regression):**
- Линейные модели как отправная точка
- Loss functions -- как измерить ошибку
- Gradient descent -- как модель учится
- Hyperparameter tuning -- как настраивать модель

**Особенности формата:**
- Модульная структура -- можно начать с любого модуля (но рекомендуется по порядку)
- 130+ интерактивных упражнений
- Badge of completion за каждый модуль
- Обновлен в 2024: добавлены модули по LLM и AutoML

**Педагогический прием:** самодостаточные модули с немедленной обратной связью. Визуализации вместо формул. Геймификация через бейджи.

**Источник:** [Google MLCC](https://developers.google.com/machine-learning/crash-course)

### 1.7 Microsoft AI for Beginners: Lesson 1 (исторический, контекстный)

**Что покрывает Lesson 1 "Introduction and History of AI":**
- История AI: от Тьюринга до ChatGPT через символический AI, экспертные системы, AI Winter
- Weak AI vs Strong AI (AGI) -- различие и текущий статус
- Примеры weak AI: Siri, Alexa, рекомендательные системы, чат-боты
- Strong AI как теоретическая концепция
- Подходы к AI: symbolic (top-down) vs neural (bottom-up) vs emergent/evolutionary

**Педагогический прием:** исторический нарратив как рамка для понимания. "Откуда мы пришли и куда идем." Бесплатный GitHub-репозиторий, формат Learn + Build.

**Источник:** [GitHub: AI-For-Beginners Lesson 1](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/1-Intro/README.md)

---

## 2. Педагогические подходы к Lecture 1

### 2.1 Top-down vs Bottom-up

| Подход | Курс | Суть | Плюсы | Минусы |
|--------|------|------|-------|--------|
| **Top-down** | fast.ai, MIT 6.S191 | Сначала результат, потом теория | Мотивирует, быстрый успех | Студент может не понимать, что делает |
| **Bottom-up** | CS221, CS188, ETH | Сначала фундамент, потом применения | Глубокое понимание | Мотивация падает к 3-й лекции по теории |
| **Middle-out** | CS50 AI | Начать с интуитивно понятного (Search), наращивать сложность | Баланс теории и практики | Может казаться "слишком простым" для подготовленных |
| **Нетехнический** | Ng AI for Everyone | Аналогии, бизнес-кейсы, ноль кода | Доступен всем | Не подходит для технической аудитории |

### 2.2 Demo-first vs Theory-first

| Подход | Кто использует | Что делают |
|--------|---------------|------------|
| **Demo-first** | fast.ai (модель за 5 мин), MIT 6.S191 (lab сразу) | Показать работающую систему, потом объяснить |
| **Theory-first** | Stanford CS221, ETH Zurich | Определения, формализация, потом примеры |
| **Example-first** | Ng (кейсы из бизнеса), CS230 (case studies) | Реальные примеры, потом обобщение |
| **History-first** | Microsoft AI for Beginners | Хронология AI, потом текущее состояние |

### 2.3 History-based vs Task-based

- **History-based** (Microsoft, Columbia edX): рассказ от Тьюринга до GPT. Хорошо для контекста, но может быть скучным если затянуть.
- **Task-based** (CS221, CS50 AI): "Вот задача, вот как AI ее решает". Более engaging, но требует хорошего подбора задач.
- **Гибрид** (Ng AI for Everyone): краткая история (5 мин) + переход к задачам. Оптимально для нашего формата.

### 2.4 Интерактивные элементы в L1

| Элемент | Курс | Описание |
|---------|------|----------|
| Live demo | fast.ai | Обучение модели в реальном времени |
| Lab сразу | MIT 6.S191 | TensorFlow notebook после лекции |
| Два проекта | CS50 AI | Degrees + Tic-Tac-Toe на первой неделе |
| Квиз | Ng, Google MLCC | Концептуальные вопросы после каждого блока |
| Think-pair-share | AI Pedagogy Project (Harvard) | Сравнение своего ответа с ответом AI |
| Emoji Scavenger Hunt | Google AI Experiments | Браузерная игра с ML -- камера + нейросеть |
| Quick Draw | Google | Рисуешь -- нейросеть угадывает |

---

## 3. Видео, материалы и ресурсы для L1

### 3.1 Рекомендуемые видео (YouTube)

| Видео | Длительность | Для чего |
|-------|-------------|----------|
| [MIT 6.S191 Lecture 1 (2025)](https://www.youtube.com/playlist?list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI) | ~69 мин | Полная лекция: от перцептрона до backprop |
| [3Blue1Brown: Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) | 4 видео, ~1 ч | Визуальное объяснение нейросетей -- лучшие анимации |
| [Andrej Karpathy: Intro to LLMs](https://www.youtube.com/watch?v=zjkBMFhNj_g) | ~60 мин | "Busy person's intro to LLMs" -- отличный обзор |
| [Andrej Karpathy: Deep Dive into LLMs](https://www.youtube.com/watch?v=7xTGNNLPyMI) | ~3.5 ч | Глубокий разбор ChatGPT (февраль 2025) |
| [CS50 AI Lecture 0: Search](https://www.youtube.com/watch?v=WbzNRTTrX0g) | ~2 ч | Полная лекция по алгоритмам поиска |
| [Two Minute Papers](https://www.youtube.com/@TwoMinutePapers) | 2-5 мин | Короткие обзоры последних достижений AI |
| [fast.ai Lesson 1](https://www.youtube.com/watch?v=8SF_h3xF3cE) | ~90 мин | Top-down подход: модель за 5 минут |

### 3.2 Демо для показа на лекции

| Демо | URL | Что демонстрирует |
|------|-----|-------------------|
| Quick, Draw! | https://quickdraw.withgoogle.com/ | Нейросеть угадывает рисунки -- весело, наглядно |
| Teachable Machine | https://teachablemachine.withgoogle.com/ | Обучение модели прямо в браузере без кода |
| Emoji Scavenger Hunt | https://emojiscavengerhunt.withgoogle.com/ | ML через камеру телефона |
| DALL-E / Midjourney | Любой генератор изображений | Генеративный AI в действии |
| ChatGPT / Claude | chat.openai.com / claude.ai | Live-демонстрация LLM |
| AI Experiments | https://experiments.withgoogle.com/collection/ai | Коллекция интерактивных AI-демо от Google |
| Hugging Face Spaces | https://huggingface.co/spaces | Готовые ML-демо от сообщества |

### 3.3 Рекомендуемые чтения для L1

| Материал | Тип | Для кого |
|----------|-----|----------|
| fast.ai Chapter 1 (Jupyter notebook) | Практическое руководство | Технические студенты |
| "AI for Everyone" Week 1 (Coursera, audit free) | Видеолекции | Все студенты |
| Microsoft AI-For-Beginners Lesson 1 (GitHub) | Текст + код | Самостоятельное изучение |
| "Attention Is All You Need" (2017) | Научная статья | Продвинутые студенты (optional) |
| Wait But Why: "The AI Revolution" | Блог-пост | Общее понимание контекста AI |

---

## 4. Что работает для вовлечения студентов в L1

### 4.1 Работающие приемы

1. **Немедленный результат.** fast.ai показывает обученную модель за 5 минут. MIT 6.S191 дает lab сразу после лекции. CS50 AI выдает 2 проекта на первой неделе. Студент должен уйти с L1 с ощущением "я уже что-то могу".

2. **Live-демо с участием аудитории.** Quick Draw, Teachable Machine, ChatGPT -- когда студенты сами взаимодействуют с AI на лекции, engagement вырастает в разы. Harvard AI Pedagogy Project рекомендует think-pair-share с AI как участником.

3. **"WOW-момент".** Показать что-то неожиданное: DALL-E генерирует картинку по запросу студентов, ChatGPT решает задачу из их домена, демонстрация deepfake или голосового клонирования. Цель -- вызвать эмоциональную реакцию.

4. **Честный разговор об ограничениях.** Ng: "1-секундное правило" для оценки что AI может. Показать провалы AI (hallucinations, bias, adversarial examples). Студенты уважают честность больше, чем хайп.

5. **Связь с их жизнью.** Рекомендательные системы (YouTube, Spotify), поисковые движки, автозамена на телефоне -- AI уже в их жизни. Начать с "вы уже используете AI каждый день".

6. **Icebreaker: "Человек или AI?"** Дать студентам тексты/изображения и попросить угадать -- сгенерировано AI или создано человеком. Анонимный чат (2 минуты) -- угадай, это человек или бот.

### 4.2 Распространенные ошибки (что НЕ делать)

| Ошибка | Почему плохо | Что делать вместо |
|--------|-------------|-------------------|
| Начать с истории AI от Тьюринга (20+ мин) | Скучно, студенты засыпают | Краткая историю (3-5 мин) или вообще пропустить |
| Начать с математики (градиентный спуск, матрицы) | Пугает нетехническую аудиторию, скучно для технической | Начать с демо, математику -- позже |
| Перегрузить терминологией | AI, ML, DL, NLP, CV, RL, LLM, AGI -- каша | Вводить термины по одному, по мере необходимости |
| Обещать слишком много ("AI заменит все") | Хайп разочаровывает, теряется доверие | Честно: вот что AI может, вот что не может |
| Показать только успехи AI | Однобокая картина | Показать и провалы: hallucinations, bias, adversarial attacks |
| Не дать ничего попробовать руками | Пассивное слушание = низкий engagement | Хотя бы одно интерактивное демо |
| Предположить уровень аудитории | Одни скучают, другие не понимают | Начать с опроса: "Кто уже пользовался ChatGPT? Кто писал код с AI?" |

### 4.3 Исследовательские находки (педагогика)

Исследование педагогических подходов к преподаванию AI (ScienceDirect, 2024, Бангладеш, 18 студентов бакалавриата) выявило 5 ключевых факторов эффективности:
1. **Значимость обратной связи** -- немедленная, конкретная
2. **Комбинация теории и практики** -- нельзя только одно
3. **Самостоятельный темп обучения** -- модульность, возможность повторить
4. **Связь с реальными задачами** -- не абстрактные примеры
5. **Интеграция с будущей карьерой** -- зачем это студенту

AI Pedagogy Project (Harvard, 2023+) рекомендует:
- Hands-on experimentation с AI инструментами
- Обсуждение возможностей И ограничений
- Критическое мышление, а не слепое принятие
- Think-pair-share с AI как "третьим участником"

**Источники:**
- [An exploration of pedagogical approaches in teaching AI courses (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S2590291124002729)
- [AI Pedagogy Project (Harvard)](https://aipedagogy.org/)

---

## 5. Что наш курс должен позаимствовать для Lecture 1

### 5.1 Конкретные идеи для нашей Lecture 1

**Структура (рекомендуемая, ~90 мин):**

| Блок | Время | Содержание | Источник идеи |
|------|-------|-----------|---------------|
| 1. Hook | 5-7 мин | Live-демо: ChatGPT/Claude решает задачу из домена студентов. "WOW-момент". | fast.ai (немедленный результат) |
| 2. Опрос аудитории | 3-5 мин | "Кто использовал AI? Для чего? Что получилось / не получилось?" | Harvard AI Pedagogy (shared goals) |
| 3. AI в вашей жизни | 10 мин | Рекомендации YouTube, поиск Google, автозамена, фильтр спама -- вы уже используете AI. Навигатор = алгоритм поиска. | CS50 AI (интуитивная связь) |
| 4. Что такое AI? | 15 мин | Определение через задачи (не через формулы). Weak vs Strong AI. ML vs DL vs GenAI -- как связаны. Краткая история (3-5 мин, не больше). | Ng (аналогии), Microsoft (история), CS221 (задачи) |
| 5. Что AI может и не может | 10 мин | Успехи + провалы. Hallucinations, bias, adversarial examples. "1-секундное правило" Ng. | Ng (ограничения), Harvard (критическое мышление) |
| 6. Интерактив | 10-15 мин | Teachable Machine: обучить модель прямо на лекции (камера, 3 класса). Или Quick Draw. Или "Человек или AI?" | Google AI Experiments, Wharton (Teachable Machine) |
| 7. Обзор курса | 10 мин | Карта курса: что будем изучать, зачем, какие проекты. Сквозной проект. | CS221 (карта), CMU 17-445 (milestones) |
| 8. Первое задание | 5 мин | Выдать "нулевое задание" -- попробовать 3 AI-инструмента и написать рефлексию (что удивило, что не получилось). | ETH (нулевой проект), GenAI for Everyone (промптинг) |

### 5.2 Что НЕ делать (на основе анализа)

1. **НЕ начинать с 20-минутной истории AI.** Даже Microsoft, у которых Lesson 1 = история, признают, что это работает только как фон. Краткая история (3-5 мин) достаточно.

2. **НЕ начинать с математики.** Ни один успешный вводный курс не начинает с формул на первой лекции. Даже MIT 6.S191 дает математику *внутри* контекста нейросетей, а не отдельно.

3. **НЕ перегружать терминологией.** Ng вводит термины постепенно, по одному, с примерами. Не давать AI/ML/DL/NLP/CV/RL/LLM/AGI/GenAI за одну лекцию.

4. **НЕ только теория, НЕ только демо.** Исследование из Бангладеша подтверждает: нужна комбинация. fast.ai только демо на L1 -- работает, но студенты теряются без контекста. CS221 только теория -- мотивация падает.

5. **НЕ обещать революцию.** Честность Ng ("вот что AI может, а вот что нет") работает лучше хайпа. Показать и провалы AI.

6. **НЕ предполагать уровень аудитории.** Начать с опроса. Смешанная аудитория -- норма (два потока МФТИ DLS: base/advanced).

### 5.3 Ключевые принципы для нашей L1

| Принцип | Обоснование | Источник |
|---------|-------------|----------|
| Результат за первые 5-10 минут | Мотивация через немедленный успех | fast.ai, MIT 6.S191 |
| Интерактивный элемент обязателен | Пассивное слушание = низкий engagement | Harvard AI Pedagogy, Google demos |
| Честность: что AI может и не может | Доверие аудитории | Ng, Stanford Teaching Guide |
| Связь с жизнью студентов | Релевантность = мотивация | CS50 AI, Ng |
| Задание на первой лекции | "Якорь" для самостоятельной работы | CS50 AI (2 проекта), ETH (нулевой проект) |
| Карта курса в конце | Студент понимает, куда идем | CS221, CMU 17-445 |

---

## Источники

### Курсы и университеты
- [Stanford CS221](https://stanford-cs221.github.io/spring2024/)
- [Stanford CS221 Lecture 1 PDF](https://web.stanford.edu/class/archive/cs/cs221/cs221.1186/lectures/overview.pdf)
- [MIT 6.S191](https://introtodeeplearning.com/)
- [Harvard CS50 AI](https://cs50.harvard.edu/ai/)
- [fast.ai Lesson 1](https://course.fast.ai/Lessons/lesson1.html)
- [Andrew Ng: AI for Everyone (Coursera)](https://www.coursera.org/learn/ai-for-everyone)
- [Andrew Ng: Generative AI for Everyone (Coursera)](https://www.coursera.org/learn/generative-ai-for-everyone)
- [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course)
- [Microsoft AI for Beginners (GitHub)](https://github.com/microsoft/AI-For-Beginners)

### Педагогические ресурсы
- [AI Pedagogy Project (Harvard)](https://aipedagogy.org/)
- [Stanford AI Teaching Guide](https://teachingcommons.stanford.edu/teaching-guides/artificial-intelligence-teaching-guide)
- [Pedagogical approaches to teaching AI (ScienceDirect, 2024)](https://www.sciencedirect.com/science/article/pii/S2590291124002729)
- [UC Berkeley ML course redesign (CDSS)](https://cdss.berkeley.edu/news/uc-berkeleys-introductory-machine-learning-course-gets-optimized-ai-age)
- [AAC&U Institute on AI, Pedagogy, and the Curriculum](https://www.aacu.org/event/2025-26-institute-ai-pedagogy-curriculum)

### Демо и инструменты
- [Quick, Draw! (Google)](https://quickdraw.withgoogle.com/)
- [Teachable Machine (Google)](https://teachablemachine.withgoogle.com/)
- [Google AI Experiments](https://experiments.withgoogle.com/collection/ai)
- [Hugging Face Spaces](https://huggingface.co/spaces)

### Видео
- [3Blue1Brown: Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
- [Andrej Karpathy: Intro to LLMs](https://www.youtube.com/watch?v=zjkBMFhNj_g)
- [Two Minute Papers (YouTube)](https://www.youtube.com/@TwoMinutePapers)
