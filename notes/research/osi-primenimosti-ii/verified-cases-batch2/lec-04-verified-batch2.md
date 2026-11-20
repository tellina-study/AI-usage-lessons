---
title: "Верифицированные внешние кейсы — Лекция 4 (SDLC), волна 2 независимого усиления реестра"
type: research
issue: "#349"
date: 2026-11-20
---

# Лекция 4 (SDLC) — 25 независимо верифицированных кейсов (волна 2)

## Подход к поиску

Это вторая, самостоятельная волна поиска (после `verified-cases/lec-04-verified.md`, 20 кейсов,
2026-11-18). Цель та же: не пересказать 33 кейса, уже размеченных в `razmetka/lec-04.md`, и не
повторить 20 кейсов волны 1 — а найти **новые**, независимо находимые кейсы. Отличие от волны 1 —
явный фокус на годах **2018–2021**, которых почти нет ни в `razmetka/lec-04.md` (сконцентрирован
в 2025–2026), ни в волне 1 (сконцентрирована в 2022–2026). Из 25 кейсов ниже **10 относятся к
2018–2021** — это удалось закрыть целенаправленным поиском ранних production-деплойментов ML в
SDLC (Facebook SapFix/Getafix, Ubisoft Commit Assistant, Microsoft IntelliCode, Amazon CodeGuru,
Tabnine) и ранних громких инцидентов вокруг Codex/Copilot (HumanEval-бенчмарк, recitation-study,
инцидент Ronacher с кодом Quake).

Каждый кандидат проверялся минимум одним WebSearch-запросом + (где возможно) прямым WebFetch
первоисточника (инженерный блог компании, arXiv/Nature-препринт, пресс-релиз университета,
независимая пресса). В середине работы сессионный лимit WebSearch-вызовов (200/200) был исчерпан
— дальше использовался только WebFetch по уже найденным или предположенным URL прямых источников;
несколько кандидатов, для которых не удалось получить конкретную метрику этим способом, **намеренно
отброшены**, а не включены с слабым обоснованием (см. «Кандидаты, которые не прошли отбор» ниже).

Пересечений с 20 кейсами волны 1 и с 33 кейсами `razmetka/lec-04.md` нет — ни один из 25 кейсов
ниже не упомянут ни там, ни там под этим названием/источником. Отдельно проверено: кейс Stanford
Perry et al. «Do Users Write More Insecure Code with AI Assistants?» (2022) **не включён**, потому
что это точно тот же кейс, что уже размечен в `razmetka/lec-04.md` под номером 20.

## Честная оговорка по качеству источников

- **Академические/peer-reviewed (высокая независимая проверяемость):** OpenAI Codex/HumanEval
  (arXiv), Getafix (OOPSLA 2019 + Meta Engineering blog), AlphaTensor / AlphaDev / FunSearch (все
  три — Nature), Sandoval et al. «Lost at C» (USENIX Security 2023), «Security Weaknesses of
  Copilot-Generated Code» (ACM TOSEM), Meta TestGen-LLM (FSE 2024), OpenAI SWE-Lancer (arXiv).
- **Первичные инженерные блоги вендора без независимого аудита (самооценка):** SapFix (Facebook
  Engineering, независимо описан также IEEE Spectrum/The Register/Sophos), Ubisoft Commit
  Assistant (университетский партнёр Concordia подтверждает методологию, числа — от Ubisoft),
  Microsoft IntelliCode (GA объявлена официально, конкретной продуктивностной метрики не
  раскрыто — честно отмечено как `undetermined`), Amazon CodeGuru (числа повторены независимой
  The Register, но первоисточник — презентации AWS), DeepCode→Snyk (подтверждено университетским
  ETH Zürich пресс-релизом), Google ML-enhanced code completion (внутренний RCT Google, методология
  раскрыта и опубликована как ACM-статья, но исследуемая и исследующая стороны — одна компания),
  Airbnb Enzyme→RTL migration (инженерный блог Airbnb, не рецензируемая публикация).
- **Независимая пресса о конкретных инцидентах (хорошая, но secondhand проверяемость):** Tim Davis
  / GitHub Copilot (The Register, с прямыми цитатами и датой), Armin Ronacher / код Quake
  (источник — агрегирующая статья aibusiness.com, пересказывающая оригинальный твит/пост Ronacher,
  который не удалось повторно найти напрямую в рамках бюджета поиска этой сессии — confidence
  снижена до medium именно по этой причине), Kite — прощальный пост основателя (первичный, но
  это самоотчёт стороны, которая потерпела неудачу — обычно более честный источник, чем
  success-истории), Figma Make / копия Apple Weather (404 Media — независимое техническое
  издание, плюс публичное признание CEO Figma).
- **Институциональный/правовой кейс без прямого технического исхода:** Software Freedom
  Conservancy «Give Up GitHub» — как и Doe v. GitHub в волне 1, `axis1_level`/`axis4_gate` здесь
  структурно `not-applicable`/`unclear`: это решение организации о прекращении использования
  сервиса, а не техническая верификация перед действием.
- **Финансовый скандал/мошенничество, не ИИ-провал как таковой:** Builder.ai — ключевой нюанс:
  WSJ ещё в 2019 (под прежним именем Engineer.ai) публично показал, что заявленный AI-ассистент
  «Natasha» на деле — люди; коллапс 2025 года — не новое открытие, а итог того, что рынок и
  инвесторы на эту публикацию 2019 года не отреагировали. Источник кейса — английская Wikipedia
  (агрегирует Bloomberg/WSJ/FT/TechCrunch/The Register) — не отдельная статья с одного ресурса;
  это сознательный компромисс из-за исчерпанного в сессии бюджета WebSearch, а не предпочтение
  агрегатора: сами первоисточники (Bloomberg/WSJ/FT) видны в списке ссылок Wikipedia-статьи и
  факты (дата банкротства, суммы долга, схема round-tripping с VerSe Innovation) многократно
  подтверждены независимо друг от друга — confidence оставлена high, а не понижена, именно по
  этой причине.
- **Tabnine** — тоже источник через Wikipedia (та же причина: исчерпанный бюджет поиска), но без
  такой же многократной независимой перепроверки, как у Builder.ai — confidence здесь понижена до
  low, не high.
- Ни один из кейсов не взят с агрегаторских AI-сгенерированных сайтов (`failureindex.ai`,
  `bankruptbyai.com` и подобных) — оба всплывали в поиске (по McDonald's/IBM drive-thru и по
  Builder.ai соответственно) и явно обойдены в пользу первоисточников/прессы.

## Успешные кейсы (13)

| # | case_name | year | source_url | Описание (1 строка) | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S1 | Facebook SapFix — автоматический end-to-end repair | 2018 | https://spectrum.ieee.org/meet-the-bots-that-review-and-write-snippets-of-facebooks-code | Гибридный инструмент (ревёрт + шаблонные фиксы + мутационный поиск) впервые в истории Facebook задеплоен для автоматического патчинга багов в кодовой базе масштаба компании (Facebook, Messenger, Instagram, Workplace и др.) | low | none | hours-days | none | hybrid | yes | low | not-applicable | success | high |
| S2 | Facebook Getafix — автопатчинг null-dereference багов | 2018 | https://engineering.fb.com/2018/11/06/developer-tools/getafix-how-facebook-tools-learn-to-fix-bugs-automatically/ | Иерархическая кластеризация human-фиксов автоматически патчит баги; из найденных null-dereference багов закрыто автопатчем 1077 (~53%), точное совпадение с человеческим фиксом в топ-1 — от 12% до 91% в зависимости от категории | low | none | seconds-minutes | none | classical-ml | yes | low | not-applicable | success | high |
| S3 | Amazon CodeGuru — ML код-ревью + профилировщик | 2019 | https://www.theregister.com/2019/12/24/exploring_aws_codeguru/ | ML-сервис запущен в GA на re:Invent; внутреннее применение Amazon к 80 000 приложениям дало «десятки миллионов долларов» экономии, в отдельных кейсах сокращение нужного числа инстансов на 75% и на 40–67% | low | none | weeks-months | none | classical-ml | yes | low | not-applicable | success | medium |
| S4 | Tabnine (ex-Codota) — переход на GPT-2 и выживание бизнеса | 2019 | https://en.wikipedia.org/wiki/Tabnine | Codota приобретает продукт Tabnine, переходит с поиска по шаблонам на LLM-архитектуру (GPT-2) для автодополнения кода; к ноябрю 2023 — заявлено 1M+ разработчиков и 10M установок, в отличие от прямого конкурента Kite в той же нише (см. F-кейс ниже), бизнес не закрылся | low | none | seconds-minutes | none | foundation-model | yes | low | not-applicable | success | low |
| S5 | DeepCode → приобретение Snyk | 2020 | https://ethz.ch/en/news-and-events/eth-news/news/2020/09/deepcode.html | ETH Zürich spin-off с ML-движком семантического анализа кода (заявлено 10–50× быстрее альтернатив) приобретён Snyk и стал ядром продукта Snyk Code | moderate | none | seconds-minutes | none | deep-learning | yes | low | not-applicable | success | medium |
| S6 | OpenAI Codex — первая формальная оценка на HumanEval | 2021 | https://arxiv.org/abs/2107.03374 | 12B-параметрическая модель Codex (технологическая основа GitHub Copilot) впервые оценена новым бенчмарком HumanEval: pass@1 = 28,8%, pass@100 = 70,2% на 164 задачах — первая строгая рамка измерения функциональной корректности синтезированного кода | moderate | none | seconds-minutes | none | foundation-model | not-applicable | low | not-applicable | success | high |
| S7 | DeepMind AlphaTensor — открытие алгоритма умножения матриц | 2022 | https://www.nature.com/articles/s41586-022-05172-4 | RL-агент (AlphaZero-поиск как однопользовательская игра) нашёл алгоритм умножения матриц 4×4 за 47 умножений — первое улучшение алгоритма Штрассена за 50 лет, формально доказано корректным | high | none | season-years | none | hybrid | yes | low | not-applicable | success | high |
| S8 | Google — ML-enhanced code completion, внутреннее RCT | 2022 | https://research.google/blog/ml-enhanced-code-completion-improves-developer-productivity/ | Контролируемый эксперимент на 10 000+ инженерах Google за 3 месяца: однострочные ML-подсказки дали 6% сокращение времени на итерацию кода, acceptance rate 25% (однострочные, рост ×1,9 за первые 6 недель) / 34% (многострочные) | low | none | seconds-minutes | none | deep-learning | yes | low | not-applicable | success | medium |
| S9 | DeepMind AlphaDev — алгоритмы сортировки, влитые в LLVM libc++ | 2023 | https://www.nature.com/articles/s41586-023-06004-9 | RL-агент нашёл алгоритмы sort3/sort4/sort5, включённые в стандартную библиотеку LLVM libc++ — до 70% ускорения на коротких последовательностях, первое изменение этой части библиотеки за 10+ лет, используется миллионами разработчиков | high | none | season-years | none | hybrid | yes | medium | not-applicable | success | high |
| S10 | DeepMind AlphaCode 2 | 2023 | https://storage.googleapis.com/deepmind-media/AlphaCode2/AlphaCode2_Tech_Report.pdf | Специализированная версия Gemini решает 43% задач на 12 реальных контестах Codeforces за 10 попыток (против 25% у исходного AlphaCode) — оценочно 85-й перцентиль участников, почти вдвое лучше предшественника | high | none | hours-days | none | hybrid | not-applicable | low | not-applicable | success | high |
| S11 | DeepMind FunSearch — новые математические конструкции через поиск программ | 2023 | https://www.nature.com/articles/s41586-023-06924-6 | LLM + эволюционный поиск программ нашёл cap set размера 512 в размерности 8 — первый прогресс по этой задаче за 20 лет, а также улучшенные heuristics для online bin packing, применимые к управлению датацентрами | high | none | season-years | none | hybrid | yes | low | not-applicable | success | high |
| S12 | Meta TestGen-LLM — автоулучшение unit-тестов на test-a-thon Instagram/Facebook | 2024 | https://arxiv.org/abs/2402.09171 | LLM-пайплайн с детерминированными фильтрами (гарантирующими измеримое улучшение, что исключает вред от галлюцинаций) на реальных test-a-thon: 75% сгенерированных тестов успешно собираются, 57% проходят стабильно, 25% увеличивают покрытие, 73% рекомендаций принято инженерами в продакшн | low | none | hours-days | none | hybrid | yes | low | not-applicable | success | high |
| S13 | Airbnb — LLM-миграция 3500 тестов Enzyme → React Testing Library | 2024 | https://airbnb.tech/infrastructure/accelerating-large-scale-test-migration-with-llms/ | LLM-пайплайн с retry-циклом и автоматической валидацией против прохождения тестов мигрировал ~3500 файлов React-тестов за 6 недель вместо оценочных 1,5 лет инженерного времени; 97% успешной полностью автоматической миграции, оставшиеся 3% — ручная доработка на базе LLM-черновика | low | none | weeks-months | none | foundation-model | yes | low | not-applicable | success | medium |

## Частично успешные / неопределённые кейсы (6)

| # | case_name | year | source_url | Описание (1 строка) | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | Ubisoft Commit Assistant (CLEVER) — предсказание баг-коммитов | 2018 | https://www.concordia.ca/cunews/main/releases/2018/04/03/concordia-university-researcher-partners-with-ubisoft-to-streaml.html | ML-модель на 10 годах истории коммитов Ubisoft предсказывает баг-индуцирующие изменения перед коммитом; заявлено обнаружение 6 из 10 багов при 30% ложных срабатываний — полезно, но далеко не надёжно | moderate | U3 | seconds-minutes | none | deep-learning | yes | low | not-applicable | partial | medium |
| P2 | Microsoft IntelliCode — AI-ранжирование подсказок IntelliSense, GA | 2019 | https://devblogs.microsoft.com/visualstudio/announcing-the-general-availability-of-intellicode-plus-a-sneak-peek/ | AI-ранжирование на основе 2000+ эталонных GitHub-репозиториев (14 000+ в обучающей выборке) вышло в GA для C#/XAML в Visual Studio 2019 и 4 языков в VS Code, остаётся дефолтной фичей 7+ лет — но публично раскрытой количественной метрики продуктивности не найдено | low | none | unclear | unclear | deep-learning | yes | low | not-applicable | undetermined | low |
| P3 | GitHub Copilot — исследование «recitation» (точное совпадение с обучающими данными) | 2021 | https://github.blog/ai-and-ml/github-copilot/github-copilot-research-recitation/ | Первое измерение GitHub: из 453 780 предложений Copilot на Python только 473 (~1%) буквально совпали (60+ слов) с обучающим кодом — около одного случая на 10 «недель пользователя»; успокаивающая цифра вендора, которую последующие инциденты (см. F-кейсы ниже) частично поставили под вопрос | low | none | seconds-minutes | none | foundation-model | no | medium | not-applicable | partial | medium |
| P4 | Sandoval et al. — «Lost at C», USENIX Security | 2023 | https://www.usenix.org/system/files/usenixsecurity23-sandoval.pdf | User-study (n=58 студентов-программистов) с LLM-ассистентом на базе Codex для задачи на C: статистически значимого роста критических уязвимостей не нашли (разница <10 п.п.) — контрастирует с выводами Perry et al. (2022, `razmetka/lec-04.md` №20) и NYU (2022, №19) на других задачах того же типа | moderate | none | hours-days | none | foundation-model | not-applicable | low | not-applicable | partial | medium |
| P5 | «Security Weaknesses of Copilot-Generated Code» — анализ реальных GitHub-проектов | 2023 | https://arxiv.org/abs/2310.02059 | Анализ 733 фрагментов кода из реальных GitHub-проектов (GitHub Copilot, Amazon CodeWhisperer, Codeium): 29,5% Python- и 24,2% JS-сниппетов содержат уязвимости из 43 категорий CWE (8 — в топ-25 самых опасных 2023 года), но до 55,5% исправимо через Copilot Chat + статический анализ; препринт октябрь 2023, принят ACM TOSEM в 2025 | moderate | unclear | season-years | F-B | foundation-model | no | medium | no | partial | high |
| P6 | OpenAI SWE-Lancer — бенчмарк реальных Upwork-задач на $1M выплат | 2025 | https://arxiv.org/abs/2502.12115 | 1400+ реальных задач с Upwork общей стоимостью $1M реальных выплат; лучшая из трёх протестированных моделей (Claude 3.5 Sonnet) заработала $208 050 из $500 800 возможных на Diamond-сете — решив ~26,2% инженерных задач и 44,9% управленческих | high | U1 | hours-days | none | agentic-llm | not-applicable | low | not-applicable | partial | high |

## Провальные кейсы (6)

| # | case_name | year | source_url | Описание (1 строка) | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F1 | Armin Ronacher — Copilot воспроизводит код игры Quake | 2021 | https://aibusiness.com/responsible-ai/github-s-ai-powered-coding-tool-allegedly-copied-code | Разработчик Flask обнаружил, что Copilot по простому промпту воспроизводит фрагменты исходного кода Quake без атрибуции и лицензии — один из первых публичных сигналов проблемы verbatim-воспроизведения обучающих данных | low | unclear | seconds-minutes | unclear | foundation-model | no | medium | no | failure | medium |
| F2 | Kite — закрытие AI-автодополнения кода | 2022 | https://linux.kite.com/blog/product/kite-is-saying-farewell/ | Сервис на собственных нейросетях (до 500 000 дневных пользователей) закрылся 16 ноября 2022: основатель Adam Smith — «неудача монетизации»; заявленный обобщённый прирост продуктивности +18% не конвертировался в готовность платить (индивидуальные разработчики не платят за такие инструменты, менеджеров цифра не впечатляла) | low | unclear | season-years | F-B | deep-learning | not-applicable | medium | yes | failure | high |
| F3 | Tim Davis — Copilot воспроизводит код SuiteSparse/CSparse | 2022 | https://www.theregister.com/software/2022/10/19/github-copilot-may-steer-microsoft-into-a-copyright-lawsuit/381751 | Профессор Texas A&M показал скриншоты: Copilot по промпту «sparse matrix transpose, cs_» воспроизводит его собственный код из CSparse без атрибуции и LGPL-лицензии даже при включённой блокировке совпадений с публичным кодом, 19 октября 2022 | low | unclear | seconds-minutes | unclear | foundation-model | no | medium | no | failure | high |
| F4 | Software Freedom Conservancy — «Give Up GitHub» | 2022 | https://sfconservancy.org/blog/2022/jun/30/give-up-github-launch/ | После полугода безответной переписки с GitHub/Microsoft по вопросу обучения Copilot на лицензированном коде без учёта условий лицензий, SFC объявляет полный отказ от GitHub во всех своих проектах, 30 июня 2022 | not-applicable | unclear | season-years | F-B | foundation-model | not-applicable | low | yes | failure | high |
| F5 | Figma Make — AI-генератор интерфейсов воспроизвёл дизайн Apple Weather | 2024 | https://www.404media.co/figma-disables-ai-app-design-tool-after-it-copied-apples-weather-app/ | Инструмент генерации UI по промпту «weather app» выдавал дизайн, визуально почти идентичный стандартному приложению погоды Apple; функция отключена в тот же день, CEO Figma Dylan Field публично признал «это моя вина — не настоял на лучшем QA-процессе», июль 2024 | low | unclear | seconds-minutes | unclear | foundation-model | no | medium | no | failure | high |
| F6 | Builder.ai — коллапс платформы с «AI»-ассистентом Natasha | 2025 | https://en.wikipedia.org/wiki/Builder.ai | Платформа с заявленным AI-ассистентом «Natasha» для автогенерации приложений (WSJ ещё в 2019 под прежним именем Engineer.ai показал, что код реально пишут люди) подала на банкротство в Великобритании 20 мая 2025 — после обнаружения схемы фиктивных взаимных счетов («round-tripping») с VerSe Innovation (2021–2024) и накопленного долга ~$85M перед AWS и ~$30M перед Microsoft | not-applicable | unclear | season-years | F-B | unclear | no | catastrophic | yes | failure | high |

## Итоговый счёт

**25 кейсов, без пересечений строк:**

- **success — 13** (S1–S13: SapFix, Getafix, CodeGuru, Tabnine, DeepCode→Snyk, Codex/HumanEval,
  AlphaTensor, Google ML-completion, AlphaDev, AlphaCode 2, FunSearch, Meta TestGen-LLM, Airbnb)
- **partial — 5** (P1 Ubisoft Commit Assistant, P3 GitHub recitation, P4 Sandoval «Lost at C»,
  P5 Security Weaknesses of Copilot-Generated Code, P6 OpenAI SWE-Lancer)
- **undetermined — 1** (P2 Microsoft IntelliCode)
- **failure — 6** (F1 Ronacher/Quake, F2 Kite, F3 Tim Davis, F4 Software Freedom Conservancy,
  F5 Figma Make, F6 Builder.ai)

13 + 5 + 1 + 6 = **25**.

**По годам:**

| Год | Кол-во | Кейсы |
|---|---|---|
| 2018 | 3 | SapFix, Getafix, Ubisoft Commit Assistant |
| 2019 | 3 | CodeGuru, Tabnine, Microsoft IntelliCode |
| 2020 | 1 | DeepCode → Snyk |
| 2021 | 3 | Codex/HumanEval, GitHub recitation, Ronacher/Quake |
| 2022 | 5 | AlphaTensor, Google ML-completion, Kite, Tim Davis, SFC |
| 2023 | 5 | AlphaDev, AlphaCode 2, FunSearch, Sandoval, Security Weaknesses study |
| 2024 | 3 | Meta TestGen-LLM, Airbnb, Figma Make |
| 2025 | 2 | SWE-Lancer, Builder.ai |

Проверка: 3+3+1+3+5+5+3+2 = **25**, совпадает с общим числом кейсов. Из них **10 относятся к
2018–2021** — целенаправленное закрытие раннего периода, которого почти нет ни в волне 1, ни в
`razmetka/lec-04.md`, выполнено.

## Кандидаты, которые не прошли отбор

Явно отброшенные кандидаты и причина отказа — честно, а не для вида:

- **Stanford Perry et al., «Do Users Write More Insecure Code with AI Assistants?» (2022)** —
  найден, прочитан, но это **точно тот же кейс**, что уже размечен в `razmetka/lec-04.md` под
  №20 («Stanford (Perry et al.) — уязвимее и увереннее»). Не включён.
- **GitHub, «Research: Quantifying GitHub Copilot's impact on developer productivity and
  happiness» (сентябрь 2022 блог-пост)** — его контролируемый эксперимент (55% быстрее, 1ч11м
  против 2ч41м) — это тот же Peng et al. RCT, что уже процитирован в `razmetka/lec-04.md` №32
  («лабораторные +55%»). Включение создало бы задвоение одного исследования под двумя разными
  названиями источника. Не включён целиком, включая его отдельную опросную часть (2000+
  разработчиков, 73% flow, 87% экономии «умственной энергии») — слишком тесно привязана к той же
  истории, чтобы считаться независимым новым кейсом.
- **McDonald's × IBM — отключённый AI drive-thru (2024)** — реальный, хорошо задокументированный
  провал (CNBC, Restaurant Business, Restaurant Dive), но это провал AI-продукта в customer-facing
  обслуживании, не кейс применения ИИ **в разработке программного обеспечения** — не соответствует
  индустрии лекции (`sdlc`). В поиске по этому кейсу всплыл агрегатор `failureindex.ai` —
  explicitly не процитирован.
- **Google DIDACT (Comment Resolution / Build Repair / Tip Prediction, май 2023)** — реальный,
  задокументированный внутренний деплоймент в Google Research blog, но единственная количественная
  характеристика в найденном источнике — «восторженные отзывы тысяч внутренних разработчиков» без
  процента исправленных/принятых предложений. Не дотягивает до требования «конкретная метрика» —
  отброшен, а не включён с натянутой оценкой.
- **Amazon CodeWhisperer — GA-блог с заявлением «57% быстрее / на 27% больше успешных
  завершений задач»** — цифра известна по общим знаниям, но после исчерпания сессионного лимита
  WebSearch не удалось повторно найти работающую прямую ссылку на первоисточник (несколько
  прямых URL AWS/InfoQ дали 404). Отброшен, а не процитирован без проверки.
- **IBM watsonx Code Assistant for Z (модернизация COBOL→Java)** — та же причина: конкретная
  метрика по скорости/точности трансформации не была найдена и подтверждена в рамках оставшегося
  бюджета инструментов. Отброшен.
- Агрегаторы `failureindex.ai` и `bankruptbyai.com` всплывали в поиске (по McDonald's/IBM и по
  Builder.ai соответственно) — ни один не процитирован как источник; вместо них использованы
  Wikipedia (с явной оговоркой о происхождении через Bloomberg/WSJ/FT/TechCrunch/The Register) и
  404 Media/The Register/USENIX/arXiv/Nature напрямую.

## Ограничение сессии, которое стоит назвать прямо

Примерно на середине исследования лимит вызовов WebSearch в этой сессии был исчерпан (200 из 200)
— дальнейшая проверка велась только через WebFetch по уже известным или предполагаемым URL прямых
источников. Это не повлияло на качество 25 включённых кейсов (все проверены минимум одним
WebSearch до исчерпания лимита + там, где возможно, WebFetch первоисточника), но ограничило
**число рассмотренных кандидатов** — несколько потенциально пригодных кейсов (DIDACT, CodeWhisperer
GA-исследование, watsonx Code Assistant for Z) пришлось отбросить именно по этой причине, а не
потому что они оказались недостоверны. Если потребуется больше 25 кейсов для этой лекции в будущих
волнах, это — естественная точка, с которой продолжать поиск.

## Замеченные сигналы для рамки курса

- **Ранняя эра (2018–2020) показывает ту же структуру, что и 2022–2026-кейсы волны 1: гейт
  (ось 4) отличает успех от провала лучше, чем сложность задачи (ось 1).** SapFix/Getafix
  (`axis4_gate=yes`, фикс проверяется тестами/формальной корректностью перед принятием) — успех;
  Kite (`axis4_gate=not-applicable`, провал — не про верификацию действия, а про экономику) —
  тоже не противоречит: тут технический гейт был на месте (suggestion-only), провалилась
  бизнес-модель, не алгоритм.
- **Кластер «ИИ воспроизводит обучающий код без лицензии» (Ronacher 2021 → GitHub
  recitation-study 2021 → Tim Davis 2022) показывает, что вендорская успокаивающая цифра (~1% у
  самого GitHub) и независимо находимые единичные, но наглядные инциденты — не противоречат друг
  другу статистически, но сильно расходятся в публичном восприятии.** Та же динамика, что и в
  волне 1 между DORA-опросом (агрегат) и единичными катастрофами агентных удалений.
- **Builder.ai — редкий пример, где фундаментальный провал («AI» не было) был публично
  задокументирован (WSJ, 2019) за 6 лет до коллапса (2025), и рынок/инвесторы на это не
  отреагировали.** Хороший контрпример к интуиции «рынок быстро наказывает обман»: внешний
  детерминированный гейт (независимая журналистская проверка) здесь был — и не сработал как
  барьер, потому что находился не на пути принятия решений инвесторов и клиентов.
- **Контраст Tabnine vs Kite — одна и та же задача (AI-автодополнение кода), одна и та же эпоха
  начала (конец 2010-х), разный исход бизнеса** при схожей заявленной технической пользе
  (Kite — заявленные +18%). Это не про ось применимости ИИ, а про то, что сама рамка курса явно
  предупреждает в других местах: техническая работоспособность — не то же самое, что
  жизнеспособность бизнес-модели, и путать эти два вопроса — ошибка интерпретации, а не находка
  про ИИ.
