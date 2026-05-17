# Research — Лекция 5: источники с датами (для §Источники плана + fact-checker)

> Дата сбора: 2026-05-17 (WebSearch). Формат: ключ — что подтверждает — дата материала — freshness-класс.
> fact-checker Phase 3 верифицирует; первоисточники (cbr.ru, NYDFS, отчёты компаний) приоритетнее агрегаторов.

## Провалы / judgment (01-failures)

1. **Zillow Offers коллапс** — CBS News «Zillow to lay off 25%…», 2021-11-02; Stanford GSB «Flip Flop: Why Zillow's Algorithmic Home Buying Venture Imploded», 2022; insideAI News «$500mm+ Debacle», 2021-12-13; SSRN 4121706 «Zillow Offers' Volatile Error Rate». Класс: исторический, cite as-is.
2. **Apple Card / Goldman / NYDFS** — NYDFS press release `pr202103231` + report `202103_report_apple_card_investigation`, 2021-03-23 (ИСХОД: нарушения не найдено, но непрозрачность); ABC News (вирусный тред), 2019-11; Banking Dive / TechCrunch, 2021-03. Класс: исторический; **точность формулировки исхода обязательна**.
3. **Knight Capital** — SEC Administrative Proceeding (settlement) 2013; Henrico Dolfing case study; CIO.com «Software Testing Lessons». Дата события: 2012-08-01. Класс: исторический.
4. **Fraud false positives** — J.P. Morgan Payments insights (security/fraud), 2024–2025; stripe.com/radar, 2024–2025; Visa annual report 2024; PayPal annual report 2024. Класс: vendor `[FACT-CHECK]` + `[VFY-day-of]` для долей.
5. **Air Canada / chatbot** — Moffatt v. Air Canada, BC Civil Resolution Tribunal, 2024-02-14 (уже в Л3). BizTech Magazine «LLM Hallucinations… Financial Institutions», 2025-08 (вторичная цифра 41%). Класс: исторический (Air Canada) / `[FACT-CHECK]` (41%).
6. **Klarna AI → откат** — Entrepreneur «Klarna CEO Reverses Course…», 2025; CX Dive, 2025; mlq.ai, 2025; Fast Company «Klarna tried to replace its workforce with AI», 2025. Дата дуги: 2023 (запуск) → середина 2025 (откат). Класс: датированный, формулировки CEO — verify.
7. **Wendy's dynamic pricing backlash** — NPR «No, Wendy's says it isn't planning surge pricing», 2024-02-28; CBS News, 2024-02; Today.com, 2024. Класс: датированный, cite as-is.

## Adoption РФ (02-adoption)

8. **Банк России — ИИ на финрынке** — cbr.ru `Consultation_Paper_20112025.pdf` «Применение ИИ на финансовом рынке: текущий статус», 2025-11; cbr.ru «Применение ИИ на финансовом рынке» (раздел fintech), 2025; «Итоги работы Банка России 2025». **Первоисточник — приоритет**, на Phase 2 извлечь точные формулировки (252 организации, 11/12 СЗКО, ~100% автономии скоринга, >80% дают opt-out). Класс: `[VFY-day-of]` для %.
9. **Сбербанк ИИ** — TAdviser «Искусственный интеллект в Сбербанке» (объявления 2024-03-13: 100% решений ИИ, +350 млрд ₽/2023, до 5000 параметров); Коммерсантъ doc/8294785 (корп. портфель 5 трлн ₽, 2025). Класс: `[FACT-CHECK]`/`[VFY-day-of]`.
10. **Т-Банк / Олег** — tbank.ru/about/news (2020, 2024 ребрендинг); TAdviser «Российский рынок цифровизации банков. Обзор 2025» (>40% обращений чат-бот; 70% банков планируют голос к 2025); Wikipedia «Олег (голосовой помощник)» (контекст, не первоисточник). Класс: `[FACT-CHECK]`, **расхождение с РПД «>90%» → USER GATE 0**.
11. **Рынок ИИ РФ** — РБК Компании «Рынок ИИ в России 2025: $2.1 млрд, +45%/год», 2025. Класс: `[FACT-CHECK]` analyst-estimate.

## Ритейл РФ (02-adoption)

12. **X5 прогноз спроса** — x5.ru/news (automated demand & replenishment planning); TAdviser проект «Перекрёсток — система прогнозирования спроса на основе ML»; logistics.ru «Товарные потери X5». Числа: точность >70%, +5 млрд ₽, −2% списаний (2023). Класс: `[FACT-CHECK]`/`[VFY-day-of]`.
13. **Магнит F&R** — shoppers.media «Магнит начал внедрять свою систему прогнозирования спроса», 2024–2025; TAdviser. Класс: `[FACT-CHECK]` (прогнозный эффект).
14. **Ozon/WB рекомендации, рынок маркетплейсов** — Ведомости пресс-релиз 2025-11-27; SelSup «Рынок маркетплейсов 2025: 8.59 трлн ₽», 2025-12; totalcrm 2025. Класс: `[FACT-CHECK]` aggregator; **НЕ переносить Amazon-цифры на РФ**.

## Мир — recsys / CV (02-adoption, 03-ai-types)

15. **Amazon 35% / Netflix 75%** — широко цитируемые «классические» оценки (McKinsey-эра ~2013 / Netflix tech blog ~2015–2016); агрегатор firney.com, agentiveaiq.com. Класс: `[FACT-CHECK]` — формулировать как «исторически приводимая оценка», НЕ как свежий headline.
16. **Amazon Just Walk Out** — CNBC «Amazon ditches cashierless checkout», 2024-04-03; Axios «Amazon's no-checkout flop shows AI's limits», 2024-04-04; TechCrunch «Amazon closes more cashierless stores», 2024-10-04; (>1000 ревьюеров в Индии — несколько источников апр.2024). Класс: датированный, cite as-is.

## Учебно-методические (тон/глубина — как Л3/Л4)
- Russell & Norvig **AIMA 4th ed** — академический образец.
- Goodfellow, Bengio, Courville **Deep Learning** / Николенко и др. **Глубокое обучение** (Питер, 2019) — для anomaly/CV/forecasting контекста (список литературы курса, course-plan-seminars #4,5).
- Курс-каноны: ФЗ-152 «О персональных данных» (текст закона, consultant/garant) — для блока безопасности.
- Внутрикурсовые: `library/lectures/lec-07/chapter.md §2.2` (sensitivity/specificity — МОСТ, не дубль); `lec-02` (ML-vs-LLM дерево); `lec-03` (Air Canada hook, RAG/fact-checking архитектура).

## Открытые fact-gaps для Phase 2/3 (НЕ выдумывать)
- Точная формулировка «>90% обращений» (РПД) vs verified «>40% Т-Банк» — нужен первоисточник либо переформулировка (USER GATE 0).
- ВТБ/Альфа конкретные % — точечный поиск Phase 2, иначе описательно.
- Доля выручки от рекомендаций Ozon/WB — первоисточником не подтверждено.
- Конкретные РФ-кейсы CV-полок/планограмм с числами — точечный поиск Phase 2.
