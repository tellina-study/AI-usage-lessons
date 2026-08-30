---
id: s31
type: failure_case
duration_min: 2
assertion: "CCS 190× scale-up gap к 2050 — engineering reality vs policy targets. AI plume migration на 100 лет hallucinate легко. Gartner 2027: 40% agentic AI проектов будут отменены."
learning_goal: "Failure 1 Q4 + LLM hallucination long horizon"
failure_bucket: strict_in
chapter_ref:
  parts: [chapter-part3.md]
  sections: ["§4.4 Провал 1: CCS scale-up gap + LLM hallucination"]
visual:
  type: chart
  description: "Bar chart 190× gap: current 40 Mt → IEA target 7.6 Gt vertical; либо timeline plume migration 100 лет с uncertainty band"
  acquisition_tier: self_render
visible_numbers: ["190× scale-up gap CCS", "40% agentic AI отменены к 2027 (Gartner)", "$1B+ Sleipner Norway 1996 - oldest CCS"]
russification_check: "CCS, Sleipner, Eclipse, INTERSECT, Gartner, OpenAI, Anthropic, GPT-4, Claude — brand list; «галлюцинация LLM», «out-of-distribution», «physics-informed neural network (PINN)», «обратная атмосферная задача» — RU."
speaker_notes_target_words: 230
---

# 190× CCS scale-up gap + AI hallucinate на 100-летнем горизонте

## Visible content

Заголовок: «CCS 190× scale-up gap — engineering reality vs policy» (28pt deep ocean).
Sub: «AI helps per-unit cost. AI не масштабирует индустрию. AI на 100-летнем horizon — hallucinate easy.» (16pt italic)

**Слева — Ocean rounded box «Что AI обещает vs не доставляет»:**

- **Обещает:** improved monitoring 10-15%; capture cost reduction 10-20%; faster site selection.
- **Доставляет:** да, в pilots — реальные цифры.
- **Не доставляет:** **scale** (gold accent).
- 40 Mt/год → 7,6 Gt/год: даже 100% improvement per-unit cost оставляет 95× за пределами.

**Справа — Ocean rounded box «Long-horizon hallucination»:**

- CCS injection хранит CO₂ на **сотни-тысячи лет**.
- Mandatory: monitoring + verification на десятилетия.
- Critical: где CO₂ через 50, 100, 500 лет?
- Sleipner Норвегия 1996+ → **30 лет данных, остальное — extrapolation**.
- LLM-based agents: «уверенный ответ на out-of-distribution» — структурный риск.
- **Gartner 2027: 40% агентных AI-проектов будут отменены** (cost overruns + poor risk controls).

**Bottom bar (gold tint) — 3 mitigation:**

«(1) **Hybrid AI + physics** (PINN, ROM) — research-grade в 2026. (2) **Human-in-the-loop mandatory** для long-horizon. (3) **Multi-method triangulation** — никогда одна ML-модель.»

## Speaker notes

Это центральный провал Q4. Разрыв масштабирования CCS в 190 раз — инженерная реальность против политических целей. Это структурный разрыв, не «AI плохо работает».

Что AI обещает: улучшение точности мониторинга десять-пятнадцать процентов. снижение стоимости улавливания десять-двадцать процентов. быстрее выбор площадки. Что доставляет — да, эти цифры в пилотах реальные. Что не доставляет — масштаб. AI не масштабирует индустрию с сорока млн т в год к семи и шести десятым млрд т в год; даже со ста процентами улучшение удельной стоимости эта цель остаётся в девяносто пять икс за пределами достижения.

Долгосрочная галлюцинация AI для миграция шлейфа на сто лет. закачка CCS хранит CO₂ под землёй на сотни и тысячи лет. Обязательно регуляторное требование — мониторинг плюс верификация на десятилетия. Главный вопрос: где будет облако CO₂ через пятьдесят, сто, пятьсот лет?

Классический физически обоснованный modelling — Eclipse плюс геомеханика — имеет большие интервалы неопределённости на сто-летнем горизонте. Геомеханика на длинных временных шкалах слабо валидирована.

AI-прогноз миграции облака CO₂ — наложение на классическую физику. Может ускорить предварительный сценарный отбор. Но на вне распределения обучения сценариях — например, землетрясение разрушает кап.rock в год сорок седьмой — галлюцинирует.

Прогноз Gartner на 2027 год — сорок процентов агентских AI-проектов будут отменены из-за превышения бюджетов и слабого контроля рисков. Для нефтегаза — это прямое предупреждение.

Mitigation — три направления. Первое — гибридный AI + физика через PINN (нейросеть с встроенной физикой) или ML с физическими ограничениями — встраивает физические законы сохранения в функция потерь. снижает галлюцинации, но дороже вычисления. К 2026 году — исследовательский уровень. Второе — человек в контуре обязательно для длинный горизонт прогнозы. Senior инженер по разработке плюс геомеханика expert делает финальный суждение. Третье — триангуляция несколькими методами. Никогда не полагаться на одну ML-модель; всегда verify через independent физический симулятор плюс аналоговый бассейн плюс данные мониторинга на нескольких временных шагах.
