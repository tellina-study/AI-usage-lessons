---
id: s09
type: data_chart
duration_min: 3
assertion: "AI стал инфраструктурой за 3 года: ежедневный инструмент 51% разработчиков, 46% кода у пользователей Copilot."
learning_goal: "Дать масштаб AI в цифрах; зафиксировать парадокс «массовое внедрение + массовый провал»"
learning_outcomes: [LO1]
references: [stack-overflow-2025, openai-2026-wau, github-octoverse-2025, cnews-vedomosti-2026, statista-mckinsey-2025]
visual:
  pattern: stat_grid_callout
  primary: "Сетка из 4 крупных метрик (900M WAU / 51% daily / 46% кода / 90% откатов) с иконками. Источники компактно под каждой."
---

## Visible content

**Заголовок (assertion):**
AI стал инфраструктурой за 3 года: ежедневный инструмент 51% разработчиков, 46% кода у пользователей Copilot.

**Сетка из 4 метрик (крупно):**

**900M** WAU
*ChatGPT, февраль 2026 (OpenAI)*

**51%** professional daily
*Stack Overflow Dev Survey 2025, n=49k+, 177 стран*

**46%** кода у юзеров Copilot
*GitHub Octoverse 2025 · Java — 61%*

**$244–390B** глобальный AI-рынок
*Statista / McKinsey, 2025*

**Контр-факт (gold strip снизу):**
И при этом в РФ **~90% AI-пилотов не доходят до прода** (CNews / Vedomosti / Intellectual Analytics, март 2026).

**Под контр-фактом:** *46% разработчиков не доверяют точности AI (vs 31% в 2024) — Stack Overflow 2025.*

## Speaker notes

К 2026 году AI — инфраструктурный слой. ChatGPT ~900M WAU (weekly active users, не monthly — month активность существенно выше). GitHub Copilot 20M+ пользователей; у тех, кто пользуется, до 46% строк кода написано AI; для Java — 61%.

Stack Overflow Dev Survey 2025 — **самый цитируемый снимок настроений разработчиков**. n=49k+ из 177 стран. 84% используют/планируют, 51% professional daily, 46% не доверяют точности (vs 31% в 2024) — **доверие падает по мере того, как AI становится повседневным**. Это диагностически важно — динамика, к которой вернёмся в §2.1 и §4.3.

Объём рынка $244–390B — разброс отражает методологию: что считать AI-рынком (продажи моделей, инфраструктура, embedded-AI, услуги интеграции).

**Российская картина — двухслойная**. Пользовательский слой высокий (51% по ВЦИОМ, см. s04). Корпоративный слой буксует: ~90% пилотов не доходят до full industrial deployment (CNews / Vedomosti / Intellectual Analytics, март 2026): 30-40% closed без эффекта; 7-10% in production. Это не уникально для России — corporate AI повсеместно сталкивается с разрывом demo↔prod (McKinsey, BCG, Gartner подтверждают). Здесь — место, где работает инженерное мышление.

Источники: Stack Overflow Dev Survey 2025; OpenAI Feb 2026 (WAU); GitHub Octoverse 2025; Statista 2025; McKinsey 2025; CNews/Vedomosti/Intellectual Analytics март 2026.
