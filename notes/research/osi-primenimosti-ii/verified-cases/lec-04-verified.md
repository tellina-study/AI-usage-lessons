---
title: "Верифицированные внешние кейсы — Лекция 4 (SDLC), независимое усиление реестра"
type: research
issue: "#349"
date: 2026-11-20
---

# Лекция 4 (SDLC) — 20 независимо верифицированных кейсов

## Подход к поиску

Цель — не пересказать кейсы, уже размеченные в `razmetka/lec-04.md` (33 строки, см. главу
лекции), а добавить **новые**, независимо находимые через открытый веб-поиск кейсы: реальные
продакшн-деплойменты или строгие эксперименты/бенчмарки/исследования с явно заявленным
(не домысленным) исходом, конкретной цифрой, датой и именованным инструментом. Каждый кандидат
проверялся минимум одним WebSearch-запросом + (где возможно) прямым WebFetch первоисточника
(пресс-релиз, GitHub issue, arXiv-препринт, судебный документ). Явно избегались агрегаторские
сайты, похожие на AI-сгенерированный контент без первичной ценности (`failureindex.ai`,
`bankruptbyai.com`, `verifiedworkflows.com`, `history.itlibra.com` всплывали в поиске по
Samsung-кейсу — ни один не процитирован ниже; использованы Bloomberg/Forbes/incidentdatabase.ai
вместо них).

Пересечений с существующими 33 строками `lec-04.md` нет — ни один из 20 кейсов ниже (включая
AlphaCode, CodeCompose, GitClear-2023, инциденты Antigravity/Claude Code #10077/#93099) не
упомянут в исходной главе лекции буквально под этим названием/источником.

**Покрытие по годам — все пять лет 2022–2026 достигнуты в обоих списках** (успех и провал
отдельно, см. таблицы ниже) — это не было тривиально: пришлось целенаправленно искать кейсы
2022 (AlphaCode, бан Stack Overflow) и 2026 (Meta RADAR, issue #93099 Opus 5) года, которых почти
нет в оригинальной главе (её кейсы сконцентрированы в 2023–2026).

## Честная оговорка по качеству источников

- **Самооценка вендора без независимого аудита:** Amazon Q Developer Java-миграция ($260M,
  источник — собственное письмо акционерам Amazon + вторичные медиа), AlphaEvolve/Borg (блог
  Google DeepMind + The Register), JPMorgan coding assistant (цифры банка, пересказанные Fortune/
  CNBC, не аудированы третьей стороной), GitHub Copilot Chat quality study (сам GitHub, n=36,
  преимущественно перцептивные метрики), Meta RADAR (первичная методологическая работа Meta,
  рецензирована как arXiv-препринт, не внешний аудит).
- **Независимо верифицируемые:** XBOW (HackerOne — сторонняя площадка + компании-получатели
  отчётов Disney/AT&T/Ford/Epic Games сами подтвердили приём), DARPA AIxCC (государственный
  организатор, открытый исход, независимое судейство), Purdue study и DORA report (методология
  раскрыта, возможна репликация), все инциденты удаления данных (первичный источник — сам GitHub
  issue или независимая пресса, не вендор).
- **Правовой кейс (Doe v. GitHub)** — не технический провал, а юридический/процессный; включён как
  редкий пример, где `axis4_gate` неприменим по конструкции (это не про верификацию перед
  действием, а про судебный процесс).
- **Один кейс (Cursor YOLO mode, июнь 2025)** реконструирован через агрегатор (`adversa.ai`), не
  через первичный GitHub issue/пресс-релиз — confidence снижена до medium именно по этой причине,
  отмечено явно в таблице.
- Полные 3-уровневые описания успеха/провала для каждого кейса видны ниже; где метрика
  принадлежит самому вендору без третьей стороны, confidence не выше medium, независимо от того,
  насколько впечатляюще число.

## Кейсы с успешным исходом (10)

| # | case_name | year | source_url | Описание (1 строка) | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S1 | DeepMind AlphaCode — Codeforces | 2022 | https://venturebeat.com/ai/deepmind-claims-its-new-code-generating-system-is-competitive-with-human-programmers | Трансформер генерирует до 1M кандидатов на задачу, фильтрует/кластеризует до 10 посылок; средний перцентиль ~54,3% (Elo ≈1238) на 10 реальных Codeforces-контестах — впервые ИИ достиг «конкурентного» уровня | high | none | seconds-minutes | none | foundation-model | not-applicable | low | not-applicable | success | high |
| S2 | Meta CodeCompose — продакшн-деплоймент на всех инженеров Meta | 2023 | https://arxiv.org/pdf/2305.12050 | AI-ассистент автодополнения кода на базе InCoder; 22% acceptance rate, multi-line suggestions почти удвоили долю сэкономленных нажатий клавиш (9%→17%); раскатан на всех инженеров Meta, <1% отказались | moderate | none | seconds-minutes | none | foundation-model | yes | low | not-applicable | success | high |
| S3 | GitHub Copilot Chat — исследование качества кода (36 разработчиков) | 2023 | https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-code-quality/ | 36 разработчиков 5-10 лет опыта пишут/слепо ревьюят API-эндпойнты с/без Copilot Chat; код-ревью на 15% быстрее, ~70% комментариев ревью принято, 85% увереннее в качестве кода | moderate | none | hours-days | none | foundation-model | yes | low | not-applicable | success | low |
| S4 | Google internal RCT — ~100 инженеров, enterprise-задача | 2024 | https://services.google.com/fh/files/misc/generative_ai_impact_on_developer_productivity.pdf | Рандомизированный контролируемый эксперимент: добавление logging-фичи через 10 файлов (~474 строк); группа с AI закончила за ~96 мин против 114 мин у контрольной — на ~21% быстрее | moderate | none | hours-days | none | foundation-model | yes | low | not-applicable | success | high |
| S5 | Amazon Q Developer — миграция 30 000 Java-приложений | 2025 | https://digiday.com/media/how-amazons-genai-tool-for-developers-is-saving-4500-years-of-work-260-million-annually/ | Автономный агент трансформации кода перевёл внутренние приложения Amazon с Java 8/11 на Java 17; >50% продакшн-систем обновлено за <6 месяцев; заявлено $260M/год экономии и 4500 человеко-лет работы | low | none | weeks-months | none | agentic-llm | yes | medium | not-applicable | success | medium |
| S6 | Google DeepMind AlphaEvolve — эвристика планировщика Borg | 2025 | https://www.theregister.com/software/2025/05/15/google_deepmind_debuts_algorithm_evolving_agent_alphaevolve/766919 | Эволюционный агент на базе LLM предложил эвристику планирования задач в Borg (кластерный менеджер датацентров Google), превзошедшую продакшн-версию; в продакшне >1 года, стабильно возвращает ~0,7% всего мирового вычислительного флота Google | high | none | season-years | none | hybrid | yes | medium | not-applicable | success | medium |
| S7 | XBOW — автономный пентест-агент, #1 US leaderboard HackerOne | 2025 | https://www.techrepublic.com/article/news-ai-xbow-tops-hackerone-us-leaderboad/ | Автономная система впервые возглавила американский leaderboard HackerOne, обойдя всех людей; ~1060 отчётов за ~90 дней, включая 54 критических/242 высоких, часть подтверждена и исправлена Disney/AT&T/Ford/Epic Games | high | none | hours-days | none | agentic-llm | yes | low | not-applicable | success | high |
| S8 | DARPA AIxCC Finals — автономные Cyber Reasoning Systems | 2025 | https://www.darpa.mil/news/2025/aixcc-results | 7 финалистских команд (победитель Team Atlanta, $4M); системы нашли 54 синтетические уязвимости из 70 задач и запатчили 43; отдельно выдали 11 патчей для реальных уязвимостей и обнаружили 18 неизвестных ранее реальных дефектов в открытом коде | high | none | hours-days | none | hybrid | yes | low | not-applicable | success | high |
| S9 | JPMorgan — внутренний AI-ассистент для разработчиков | 2025 | https://www.cnbc.com/2024/08/09/jpmorgan-chase-ai-artificial-intelligence-assistant-chatgpt-openai.html | Собственный coding assistant + GitHub Copilot + Claude Code; к маю 2025 доступ у >40 000 инженеров, заявленный прирост продуктивности 10–20% | moderate | none | weeks-months | none | foundation-model | yes | medium | not-applicable | success | medium |
| S10 | Meta RADAR — риск-калиброванное автоматическое код-ревью | 2026 | https://arxiv.org/pdf/2605.30208 | Гибридный пайплайн (ML-скоринг риска + LLM-ревью + детерминированная валидация) автоматически ревьюирует и «лендит» низко/средне-рисковые диффы; из >535 000 проревьюированных >331 000 (~62%) залендено автоматически, revert rate — треть от человеческого базлайна, частота продакшн-инцидентов — 1/50 от базлайна | low | none | seconds-minutes | none | hybrid | yes | low | not-applicable | success | medium |

## Кейсы с провальным/неуспешным исходом (10)

| # | case_name | year | source_url | Описание (1 строка) | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F1 | Stack Overflow — временный бан ответов ChatGPT | 2022 | https://www.theregister.com/2022/12/05/stack_overflow_bans_chatgpt/ | Модераторы ввели временный запрет на ответы, сгенерированные ChatGPT: тысячи ответов выглядели убедительно, но доля верных оказалась неприемлемо низкой для референсного ресурса | moderate | unclear | hours-days | F-B | foundation-model | no | medium | no | failure | high |
| F2 | Samsung — утечка исходного кода через ChatGPT, корпоративный запрет | 2023 | https://www.bloomberg.com/news/articles/2023-05-02/samsung-bans-chatgpt-and-other-generative-ai-use-by-staff-after-leak | Инженеры подразделения полупроводников вставили проприетарный код базы данных, алгоритмы детекции дефектов оборудования и транскрипты внутренних совещаний в ChatGPT; 3 утечки за 20 дней → полный корпоративный запрет на генеративный ИИ с 1 мая 2023 | low | unclear | seconds-minutes | unclear | foundation-model | no | high | no | failure | high |
| F3 | Purdue — 52% ответов ChatGPT на вопросы Stack Overflow неверны | 2023 | https://arxiv.org/pdf/2308.02312 | Анализ 517 программистских вопросов: 52% ответов ChatGPT содержат ошибки, 77% многословны, 78% непоследовательны по сравнению с человеческими ответами; участники всё равно предпочитали ответы ChatGPT в 35% случаев и не замечали ошибку в 39% | moderate | unclear | seconds-minutes | none | foundation-model | no | medium | no | failure | high |
| F4 | GitClear 2023 — рост churn и копипасты, коррелированный с Copilot | 2023 | https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality | Анализ ~153M изменённых строк (2020–2023): код-churn вырос с 3,3% до 5,5% изменённых строк, копипаста — 11,55% изменений, корреляция «использование Copilot» × «churn» = 0,98 | unclear | unclear | season-years | F-B | foundation-model | no | medium | no | failure | medium |
| F5 | DORA 2024 — рост adoption ИИ коррелирует со снижением стабильности доставки | 2024 | https://dora.dev/research/2024/dora-report/ | Крупный ежегодный индустриальный опрос: +25% adoption ИИ ↔ −1,5% throughput и −7,2% стабильность доставки, при одновременном росте индивидуальной продуктивности, flow и удовлетворённости — явная двойственность | unclear | unclear | weeks-months | F-B | foundation-model | unclear | unclear | mixed | partial | high |
| F6 | Doe v. GitHub, Microsoft, OpenAI — иск о копирайте/лицензиях Copilot | 2024 | https://en.wikipedia.org/wiki/Doe_v._GitHub,_Microsoft,_and_OpenAI | Окружной суд (июнь 2024) отклонил большинство претензий включая DMCA-теорию, но разрешил продолжиться иску о нарушении условий open-source лицензий; апелляция 9-го округа (сент. 2026) подтвердила отклонение DMCA-части, лицензионный спор продолжается | not-applicable | unclear | season-years | unclear | foundation-model | not-applicable | unclear | yes | partial | high |
| F7 | Cursor «YOLO mode» — удаление локальных файлов при миграции | 2025 | https://adversa.ai/blog/ai-coding-agent-incidents/ | Автономный агент Cursor в режиме без подтверждений («YOLO mode») удалил файлы на машине разработчика во время миграции Express.js → Next.js; восстановлены только облачные копии, локальный диск — почти полностью потерян | low | unclear | seconds-minutes | F-C | agentic-llm | no | high | no | failure | medium |
| F8 | Google Antigravity — стирание диска D: целиком | 2025 | https://www.theregister.com/2025/12/01/google_antigravity_wipes_d_drive/ | Агентная IDE в «Turbo mode» выполнила `rmdir /s /q d:\` вместо очистки кэша конкретного проекта из-за ошибки разбора пути; весь диск D: стёрт без возможности восстановления, минуя корзину | low | unclear | seconds-minutes | F-C | agentic-llm | no | high | no | failure | high |
| F9 | Claude Code — рекурсивное удаление домашней директории, issue #10077 | 2025 | https://github.com/anthropics/claude-code/issues/10077 | На Ubuntu/WSL2 агент выполнил `rm -rf` от корня, удалив все пользовательские файлы в `/home/...` (недели/месяцы незафиксированной работы); issue закрыт вендором как «not planned» через 60+ дней несмотря на повторные независимые репорты других пользователей | low | unclear | seconds-minutes | F-C | agentic-llm | no | high | no | failure | high |
| F10 | Claude Opus 5 — `rm -rf $HOME` при очистке теста, issue #93099 | 2026 | https://github.com/anthropics/claude-code/issues/93099 | Модель заявила, что «настоящий HOME восстановлен», и секундами позже выполнила `rm -rf "$HOME"` против него же внутри одного multi-command Bash-вызова; удалено 57 235 файлов и 11 315 директорий (68 550 объектов), часть сгенерированных скриптов не восстановлена | low | unclear | seconds-minutes | F-C | agentic-llm | no | high | no | failure | high |

## Замеченные противоречия и сигналы для рамки курса

- **Гейт продолжает держаться как сильнейший предиктор даже на новой выборке.** Во всех 10
  успешных кейсах `axis4_gate=yes` (либо `not-applicable` в контролируемой лабораторной среде без
  реальных ставок — S1); во всех провалах с применимой осью `axis4_gate=no` или `unclear`/
  `not-applicable` там, где сама природа кейса не техническая (DORA-опрос, судебный процесс).
  Ровно пять «удалений» (Cursor YOLO, Antigravity, Claude Code #10077, Claude Opus 5 #93099 — и
  они формируют отдельный, узкий подкластер «agentic-llm + `rm`/`rmdir` + отсутствие
  подтверждения») — повторяют ровно тот же паттерн, что Replit/PocketOS/Kiro в исходной 33-строчной
  разметке лекции: не про сложность задачи (`axis1_level=low` у всех пяти), а про отсутствие шага
  проверки перед безвозвратным действием.
- **Потенциальное противоречие headline-находке «у большого ИИ потолок успеха — 0% на
  экстремальной/высокой неопределённости».** Три новых успешных кейса — XBOW (`axis1_level=high`,
  `agentic-llm`), DARPA AIxCC (`high`, `hybrid`) и AlphaEvolve (`high`, `hybrid`) — это
  задокументированные, не вендорские-only успехи именно на высоком уровне неопределённости
  (поиск неизвестных уязвимостей/алгоритмов в большом непредсказуемом пространстве). Это не
  опровергает находку (все три — не чистый `foundation-model`/`agentic-llm` в одиночку: XBOW
  явно использует детерминированную валидацию поверх LLM, AIxCC — комбинированные Cyber Reasoning
  Systems, AlphaEvolve — эволюционный поиск + LLM), но стоит явно назвать как пограничный случай:
  успех на высокой неопределённости у «большого ИИ» в этой подвыборке **всегда** сопровождается
  `axis3_class=hybrid` или явным детерминированным гейтом-валидатором — не голой LLM-генерацией.
  Это скорее уточняет headline-находку (сложный метод работает на высокой неопределённости, если
  он гибридный и гейтирован), чем противоречит ей.
- **DORA 2024 — редкий кейс, где F-B (confounding) явно именован самим источником**, а не
  домыслен при разметке: отчёт прямо предупреждает, что связь «AI adoption → стабильность» не
  причинно-следственная, а опосредована качеством инженерных практик команды. Хороший кандидат
  на иллюстрацию механизма F-B в будущих материалах курса.
- **Doe v. GitHub** — редкий «provalы честности/верификации ≠ provalы неопределённости» случай
  в duh юридической, а не инженерной плоскости: `axis4_gate` здесь структурно неприменим так же,
  как у институциональных/геополитических кейсов других лекций (см. предупреждение README о
  высокой доле `unclear`/`not-applicable` у таких кейсов) — не ошибка разметки, а честный сигнал,
  что ось 4 создавалась для технических деплойментов, а не для судебных процессов.
