---
id: s14
type: comparison_case
duration_min: 3
assertion: "HPC-гонка Q3: Eni HPC6 — 606 PFLOPS Top500 #5 за $104M. Aramco METABRAIN — 250B параметров на 90 годах данных, $1,8B realized в 2024 (= 0,41% выручки)."
learning_goal: "HPC landscape Q3 + base value $1.8B / $436B"
chapter_ref:
  parts: [chapter-part2.md]
  sections: ["§2.2 HPC-гонка: Eni HPC6 и Aramco METABRAIN"]
visual:
  type: image
  description: "Side-by-side: Eni HPC6 server rack photo + Aramco METABRAIN abstract (либо Aramco Davos 2024 photo Amin Nasser)"
  source_url: "https://www.eni.com/en-IT/business-activities/global-digital.html"
  acquisition_tier: 3
visible_numbers: ["606 PFLOPS / 14k MI250X / $104M (Eni)", "250B params / 90 лет data / $1,8B 2024 (Aramco)", "0,41% выручки"]
russification_check: "Eni, HPC6, Aramco, METABRAIN, NVIDIA, AMD, MI250X, Grace Hopper, Davos, Amin Nasser, KAUST — brand list; «высокопроизводительные вычисления (HPC)», «большая универсальная модель (foundation model)» inline gloss."
speaker_notes_target_words: 260
---

# HPC-гонка Q3: Eni HPC6 + Aramco METABRAIN — две стратегии

## Visible content

Заголовок: «HPC-гонка Q3: $100-400M на инсталляцию» (28pt deep ocean).
Sub: «Не коммодизируется как облако — стратегический CapEx. Малые операторы вытесняются capital barrier.» (16pt italic)

**Слева — Ocean rounded box «Eni HPC6» (декабрь 2024):**

- **606 PFLOPS** peak performance · 477 PFLOPS sustained.
- **14 000 AMD MI250X** GPU.
- **$104 млн** capex (gold accent).
- **Top500 #5** мирового рейтинга.
- Применение: обработка сейсмики + INTERSECT + CCS modelling.
- Стратегия: cost-effective per-FLOP (AMD vs NVIDIA).

**Справа — Ocean rounded box «Aramco METABRAIN» (поэтапно 2024-2025):**

- **~250 млрд параметров** [VFY-day-of] — volatile (7B март 2024 → 250B → claim 1T 2025).
- Обучение на **7 трлн токенов = 90 лет** operational data Aramco.
- 6 000 сотрудников обучены; 430 use cases.
- **$1,8 млрд realized 2024** (Davos янв 2025, CEO Amin Nasser).

**Bottom bar (gold tint) — Базовая контекстуализация:**

- Aramco выручка 2024 = **$436,6 млрд** → $1,8B / $436,6B = **0,41% выручки**. AI добавляет полпроцента к полностью оптимизированной операции.
- **METABRAIN — внутренний продукт.** Aramco не продаёт наружу = competitive moat, без mismatch incentives.

## Speaker notes

HPC-гонка Q3 — это разные стратегии у каждой крупной компании.

Eni HPC6. В декабре 2024 года итальянская Eni запустила суперкомпьютер HPC6 в дата-центре Ferrera Erbognone. Шестьсот шесть PFLOPS пиковой производительности, четыреста семьдесят семь sustained; четырнадцать тысяч графических ускорителей AMD Instinct MI250X; стоимость инсталляции — около ста четырёх миллионов долларов. На декабрьском листинге Top500 — пятое место из примерно пятисот. HPC6 в девять раз мощнее своего предшественника HPC5. Применения: обработка сейсмики, пластовая симуляция на INTERSECT, моделирование CCS.

Aramco METABRAIN. В 2024 году Saudi Aramco разработала METABRAIN — большую универсальную модель внутреннего использования. Объявленные параметры на 2024 год — примерно двести пятьдесят миллиардов; цифры volatile, требуют проверки. Обучение на семи триллионах токенов, представляющих девяносто лет operational data Aramco. Шесть тысяч сотрудников обучены работать с инструментарием на основе METABRAIN. Четыреста тридцать use cases идентифицированы.

Что Aramco публикует. В Давосе в январе 2025 года CEO Aramco Amin Nasser заявил, что AI-инвестиции принесли один и восемь десятых миллиарда долларов реализованной стоимости в 2024 году. Базовая контекстуализация: Aramco выручка 2024 — четыреста тридцать шесть и шесть десятых миллиарда. Делим — это ноль и сорок одна сотая процента выручки. AI не «спасает» компанию — добавляет полпроцента к полностью оптимизированной операции.

Два урока. Первое — один и восемь десятых миллиарда долларов — self-reported, не аудированное число. Второе — METABRAIN внутренний продукт, не продаётся наружу. Это competitive moat и одновременно структурное отличие от BP + Beyond Limits и IBM + Repsol, которые мы разберём через два слайда.
