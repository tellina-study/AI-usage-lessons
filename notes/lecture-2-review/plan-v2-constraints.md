# Plan v2 constraints (user-locked, 2026-05-13)

User приняла 4 ключевых scope decisions через AskUserQuestion 2026-05-13. Эти ответы — **hard constraints** для всех downstream работ (plan v2, chapter, slides, speech).

---

## 1. Scope: Узкий LLM internals + cross-cutting frames

**Stem:** 4 концепта Lec-1 §5.3 promise — токены / эмбеддинги / attention / температура. Это backbone лекции.

**Cross-cutting frames (короткие, по 1-2 слайдам каждый, как callbacks к Lec-1, не повторение):**

| Аспект | Размер | Связь с Lec-1 | Где в Лекции 2 |
|---|---|---|---|
| ML vs LLM decision tree | 1-2 слайда | Расширяет §1.4 (задача × модальность) | В начале или в финале — «когда LLM, когда классика» |
| Local vs cloud trade-off | 1 слайд | §4.2 (локальные vs облачные) | Внутри секции «Сэмплинг / inference» — практический контекст |
| Human vs AI | 1 слайд | §4.8 (Pearl 3 уровня) | В заключении — «attention ≠ понимание» (объясняет почему «понимает паттерны, не смысл») |

**Запрещено:**
- Повторять ML/DL/CV/audio классификацию (Lec-1 §1.4 уже сделала). Можно один маленький recap-callback (s03) с подсветкой «модель» layer.
- Заново разбирать локальные модели (Lec-1 §4.2). Только в контексте «сэмплинг работает одинаково локально и в облаке, но размер модели → влияет на качество».
- Заново разбирать Pearl causality. Только короткое замечание «attention статистически смотрит, не понимает причинности — см. Lec-1 §4.8 для глубже».

**Ожидаемый размер:** 28-30 слайдов / 75 мин (Lec-1 = 29, plan v1 = 31 — overload risk).

---

## 2. Название

**Canonical:** «Как работают современные большие модели»

Источник: Lec-1 chapter.md changelog v2→v3 §21 — user явно переименовала из «Архитектура AI: от ML до трансформеров» в student-friendly «Как работают современные большие модели».

**Запрещено:**
- Использовать «Архитектура AI: от ML до трансформеров» в любом из артефактов (chapter title, slide titles, speech intro, references).
- Использовать английский «How LLMs work» (русский canonical).

---

## 3. Learning Outcomes: LO1 + LO4 + LO6 + LO7

User выбрал full mix (включая LO4). Каждый LO needs explicit slide coverage + chapter section.

- **LO1.** Сможет описать четырёхэтапный конвейер inference LLM (токенизация → эмбеддинг → attention → сэмплинг) и назвать назначение каждого этапа в одном предложении.
- **LO4.** Сможет подобрать параметры запроса (`temperature`, `top_p`, `max_tokens`, `system prompt`) под конкретный сценарий: детерминированная классификация, creative writing, точное извлечение факта.
- **LO6.** Сможет назвать минимум три ограничения LLM-инференса, которые идут от архитектуры (миопия токенизации, конечное контекстное окно, стохастичность сэмплинга), и привести инженерный кейс, где каждое опасно.
- **LO7.** Сможет обосновать **три «почему»**, связав каждое с внутренним механизмом:
  - почему промпт с ролью работает лучше пустого (→ attention распределяется на role-токены),
  - почему AI плохо считает буквы (→ tokenizer объединяет несколько букв в один токен; модель не видит букв),
  - почему один и тот же запрос даёт разные ответы (→ сэмплинг из распределения при T > 0).

---

## 4. Git / infrastructure

- **Issue:** #74 «Лекция 2: Как работают современные большие модели — full production»
- **Branch:** `issue-74-lec-02-llm-internals` (от main)
- **Artifacts path:** `library/lectures/lec-02/`
- **Plan v1 path:** `notes/lecture-2-review/plan-v1.md` (renamed from `plan-v1-discarded-llm-internals.md`)
- **Plan v2 final path:** `notes/lecture-2-review/final/plan-v2-final.md` (TBD)
- **Phase 1 critique reports:** `notes/lecture-2-review/2026-05-13-phase1-plan-critique/`

---

## 5. Pipeline & quality gates

См. `tools/lecture-production/README.md`. 11 фаз + 3 USER GATEs + 3 pre-USER-GATE walkthroughs.

**Применяем все правила из `notes/reflections/2026-05-13-lec-01-v3-rebuild/REFLECTION-CONSOLIDATED.md`:**
- 4-level verdict scale во всех critics
- No Extra Content Rule для producers
- Schema Readability Checklist для visual-loop slides
- Pre-USER-GATE walkthrough перед каждым GATE
- WPM ≤95 hard rule в speech
- Cascade-of-changes tracking при revisions
- Glossary lock после chapter approval

---

## 6. Open questions to resolve in Phase 1 (delegated to critics + plan v2 synthesis)

Plan v1 §15 имел 10 open questions. Эти — для разрешения в plan v2 (с justification):

1. Hook s01: tokenizer demo vs CV callback к Lec-1 — **lean to tokenizer demo** (новый, прямой); critic input нужен.
2. s11 Word2Vec классика vs современные embeddings examples — **lean to mix: Word2Vec для intuition (1 slide) + современные sentence embeddings для практики**.
3. s14 multimodal — sustain 2 мин — **lean to 1 мин mention** (cross-cutting сокращение).
4. s17 vs s18 (attention worked example vs role-effect) — **lean to merge в s17 + role-effect = 2-я часть**.
5. s21 long-context fails — **lean to keep, но 2 мин max**.
6. s24 top-p/k — **lean to merge с s23 (T + 1 строка top-p)**.
7. Tone: explanatory или wow — **lean to explanatory-engineering (объяснительно-инженерный)**, чтобы не противоречить Lec-1 «диагностический».
8. Slide count: 31 → **target 28-30** (см. §1 этого документа).
9. Pre-class reading — **out of scope**.
10. ML vs LLM decision tree placement — **lean to s30 (после deep-dive, перед мостом к Lec-3), как «когда что использовать»**.

Critics в Phase 1 проверят эти leans и могут переобосновать.

---

## 7. Non-negotiables (NEVER drift from these)

- Промис §5.3 Lec-1 — 3 «почему» (роль / буквы / T) — должны быть payoff'ены в финальном разделе.
- Терминология из plan v1 §10 (glossary lock) — основа для glossary.yaml.
- Forbidden additions из plan v1 §11 — base list для No Extra Content Rule.
- Tone — explanatory-engineering, без «магия LLM».

---

**Конец constraints. Used as canonical brief для Phase 1 critics + plan v2 synthesis.**
