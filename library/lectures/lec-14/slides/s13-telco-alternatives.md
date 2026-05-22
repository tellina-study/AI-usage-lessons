---
id: s13
type: assertion_visual
duration_min: 1
assertion: "Альтернативы AI в телекоме: 3GPP SON, инженерия трафика по Erlang, ПИД/MPC, федеративное обучение."
learning_goal: "Alternative tools для телеком"
failure_bucket: strict_in
media_tier: "Custom python-pptx schema"
---

# Альтернативы AI в телекоме — проверенные классические инструменты

## Visible content

4 карточки в сетке 2×2:
• 3GPP SON — Self-Organizing Networks: Self-configure/Self-optimize/Self-heal — rule-based, сертифицированный. «Когда AI "улучшает" SON — спросите, что именно. SON и так работает.»
• Erlang traffic engineering — 1909 → 2026: Erlang B/C формулы для расчёта нагрузки + Markov chains. «Лучше любой ML для прогноза blocking probability.»
• ПИД / MPC — Control theory: стабильность доказана 60 лет в URLLC, power amplifiers, antenna tuning. «Layer-Adaptive PID + ML гибрид — выбор там, где ML только подсказывает, а PID управляет.»
• Federated Learning + DP — Privacy-preserving: обучение без обмена сырыми данными (Differential Privacy). «Compliance-friendly (GDPR). Не быстро, но проходит аудит.»

## Speaker notes

Альтернативы AI в телекоме — четыре класса проверенных инструментов, которые работают и сейчас, и часто лучше AI.

Первое — 3GPP SON, Self-Organizing Networks. Это standardized набор функций: самоконфигурация при подключении новой соты, самооптимизация параметров на основе measurement reports, самовосстановление при отказе. Rule-based, сертифицированный, развёрнут глобально. Когда вендор приходит и говорит «наш AI улучшит SON» — первый вопрос: что именно улучшит? SON и так работает.

Второе — Erlang traffic engineering. Это математическая теория от 1909 года, когда датский инженер Эрланг работал в копенгагенской телефонной компании. Erlang B и Erlang C формулы рассчитывают вероятность блокировки звонка при заданной нагрузке. Markov chains для моделирования сетевых очередей. Эта математика — лучшая для прогноза blocking probability на дюрабельных таймскейлах. Никакая ML здесь не нужна и не лучше.

Третье — ПИД-регуляторы и model predictive control. Это control theory, шестьдесят лет в проде. В URLLC, в power amplifiers, в антенной настройке. Стабильность доказана через Lyapunov-функции — это математика, не статистика. Если хочется ML — лучший паттерн Layer-Adaptive PID плюс ML гибрид: ML смотрит на телеметрию и подсказывает gains для PID-регулятора, но управление остаётся за PID.

Четвёртое — federated learning плюс differential privacy. Это не альтернатива AI в строгом смысле, скорее compliance-friendly архитектура. Обучение происходит на distributed устройствах без отправки сырых данных в облако. GDPR-friendly. Медленнее централизованного обучения, но проходит аудит.

Общий принцип: 80% защиты за 20% стоимости — это про правильный выбор классических инструментов там, где AI не даёт преимущества.
