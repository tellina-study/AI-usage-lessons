---
id: s06
type: assertion_visual
duration_min: 2.5
assertion: "AI в медицине — 4 разные индустрии, не один tools-set. Modality × Scope = design-driven taxonomy."
learning_goal: "4 типа AI-применений как mental model"
learning_outcomes: [LO1]
frame_mapping: ["Другой AI"]
chapter_ref: "§1.1 — Четыре типа AI-применений"
references: []
visual:
  pattern: matrix
  primary: "2×2 matrix с осями Modality (image/signal ↔ text/molecule) × Scope (single patient ↔ population/pharma); 4 ячейки с примерами + 4 иконки Lucide по углам"
  illustration:
    type: schematic
    sources:
      - "Self-generated 2×2 matrix через PowerPoint shapes (Ocean palette)"
      - "Lucide icons https://lucide.dev — `scan` (диагностика), `heart-pulse` (population imaging), `pill` (personalized), `flask-conical` (drug discovery), recolored к Primary mid `#065A82`"
      - "LobeHub icons CDN — small logos mosmed.ai, DeepMind, Insilico Medicine для примеров в ячейках"
    caption: "4 типа AI-применений (modality × scope); иконки Lucide"
interaction: none
---

# AI в медицине — 4 разные индустрии, не один tools-set

## Assertion

AI в медицине — 4 разные индустрии, не один tools-set. Modality × Scope = design-driven taxonomy.

## Visual

Большая 2×2 matrix занимает центр слайда. Ось X (горизонтальная): scope — слева «single patient», справа «population / pharma». Ось Y (вертикальная): modality — сверху «image / signal», снизу «text / molecule». В четырёх ячейках: верхняя-левая — «AI-диагностика» (CT/MRI/X-ray, дермато-скан), пример mosmed.ai, IDx-DR; иконка `scan`. Верхняя-правая — «Population imaging analytics», иконка `heart-pulse`. Нижняя-левая — «Personalized medicine» (genomic AI, clinical decision support), иконка `pill`. Нижняя-правая — «Drug discovery + эпидемиология» (AlphaFold, Insilico, Generate Biomedicines), иконка `flask-conical`. Внизу caption: «Фокус лекции: верх-лево (s9–13) + низ-право (s15–17)».

## Speaker notes

AI в медицине — это не одна индустрия и не один стек технологий. Удобно рассмотреть четыре типа применений на двух осях. Первая ось — modality, или модальность данных: изображение и сигнал против текста и молекулы. Image- и signal-задачи — рентген, КТ, МРТ, ЭКГ, дерматологический скан — обрабатываются компьютерным зрением: CNN, Vision Transformer, специализированные foundation-модели вроде MedCLIP и BiomedCLIP. Text- и molecule-задачи — клинические записи, генерация молекул, прогнозирование структуры белка — обрабатываются другими архитектурами: трансформерами для текста, генеративной химией типа Insilico Chemistry42, AlphaProteo для молекул, AlphaFold для структур белков.

Вторая ось — scope: один пациент против популяции или фармы. Single-patient задачи — это диагноз или назначение конкретному человеку. Population-задачи — это анализ когорт и индустриальные процессы: программы скрининга, drug discovery, эпидемиологический мониторинг.

Пересечение двух осей даёт четыре ячейки. AI-диагностика — самая массовая (76 процентов FDA-списка) — это mosmed.ai, IDx-DR, Aidoc, Care Mentor AI. Population imaging analytics — мониторинг скрининговых программ. Персонализированная медицина — genomic AI и clinical decision support. Drug discovery — AlphaFold, Insilico, Generate Biomedicines. Эта классификация — не визуальный декор: modality определяет ML-stack, а scope определяет regulatory pathway (single patient = medical device по логике FDA SaMD; population analytics — другой регуляторный путь). Сегодня мы углубляемся в левую колонку (диагностика) и нижнюю-правую (drug discovery).
