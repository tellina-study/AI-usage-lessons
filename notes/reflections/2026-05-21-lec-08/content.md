# Лекция 8 — рефлексия по content

**Дата:** 2026-05-21
**Лекция:** 8 «AI в креативных индустриях и медиа»

## Keystone axis: «Что AI добавил → что изменил → что сломал»

**Решение.** Owner choice на USER GATE 0 — выбрал «сначала новое, потом проблемы», а не категорию «инструмент vs авторство» или «удешевление vs обесценивание».

**Validation в production.** Axis работала хорошо:
- Раздел 1 (12') — concrete new capabilities (Sora 2, Genie 3, ElevenLabs voice cloning)
- Раздел 2 (10.5') — pipeline + cost-collapse + displacement
- Раздел 3 (24') — failure budget (12 cases) — главный failure-носитель
- Раздел 4 (8') — критерии «AI не нужен»
- Раздел 5 (4') — actionable checklist

**Что работало.** Three-time framing создаёт natural story arc: enthusiasm (new things possible) → reality (economy shifts) → consequences (legal/brand failures). Студент уходит с complete mental model.

**Что не работало.** Mismatch axis (3 времени) vs taxonomy (4 области) — orthogonal taxonomies. Plan v1 не делал связь явной; methodology-critic flag-нул как P1.3. Fix: явный mini-параграф «эти 4 области = sub-classifier внутри каждого времени; cross-product 3×4 = 12 cells».

## Failure/judgment ≥30% strict-in (ENFORCED L4-L17)

**Достигнуто.** Chapter 36.6%, deck 41%, speech 50% — все 3 артефакта > 30% threshold. Distribution holistic, не сконцентрировано в одном артефакте.

**Что особенно сильно сработало:**
- **12 case-слайдов в §3** (s20-s31) с explicit «Урок для инженера» в Ocean rounded box gold-highlighted. Format consistent, делает критическое мышление scaffold-ed.
- **Kelly McKernan plaintiff portrait** (s23) — actual artist, не abstract case. Photo of real person elevates case from «legal abstraction» to «human story».
- **Drew Ortiz fake profile screenshot** (s29) — actual CNN reporting visual, students могут recognize SI fake author scandal как concrete reality.
- **Arup CFO 5-step attack diagram** (s26) — concrete attack chain (Email → Video invite → Call with deepfakes → 15 transactions → $25.6M gone).
- **Korea schoolgirl crisis с PBS protest photo** (s27, sensitive — no deepfake visuals) — class-harm impact tangible.

**Lesson:** **real images** для failure cases dramatically стronger чем mock cards. «Kelly McKernan portrait» делает case immediately human; «Andersen v Stability AI» как text — abstract.

## «Урок для инженера» как teaching device

**Что работало.** 15 explicit «Урок для инженера» blocks (chapter + slides §3) — concentrated phrase, actionable. Examples:
- s21 NYT: «Если модель может процитировать твой обучающий корпус дословно — это НЕ "добросовестное использование", это доказательство нарушения. Проверка сходства результата обязательна.»
- s26 Arup: «Видеозвонок ≠ подтверждение личности в 2024+. Финансовые транзакции требуют проверки через независимый канал.»
- s27 Korea: «Доступная capability + слабый enforcement = массовый class harm. Для consumer-facing AI tools обязателен safety layer (NSFW detection + age verification + reporting pipeline) ДО launch.»

**Insight.** «Урок» это не «summary» — это **applicable принцип** для инженера, оценивающего AI-инструмент в его собственном проекте. Это переводит case из «новости индустрии» в «mental model для решений».

**Pattern для воспроизведения:** каждый failure case в любой лекции должен заканчиваться 1-2-sentence «Урок» которая applicable для engineer mind, не abstract.

## Russian context (s10a)

**Decision.** Owner выбрал на USER GATE 0 «мини-блок в Разделе 1». Research dossier (mini, 818 слов) добавил Kandinsky 6.0 / Шедеврум / SymFormer / законопроект Минцифры 18.03.2026.

**Что работало.** s10a показывает «local convenience vs frontier» урок — RU-tools полезны для RU-промптов / без VPN / рубли, но НЕ frontier-quality (нет direct Sora 2 Pro competitor). Это HONEST framing, не пропаганда и не критика.

**Side note.** Если бы Russian context занимал отдельный раздел (5-7 слайдов вместо 1), pacing бы overrun, и focus terralised бы с global landscape. Owner judgment был верный — 1-slide мини-блок enough.

## 2026 freshness и `[VFY-day-of]` discipline

**13 volatile facts** помечены `[VFY-day-of]` в research dossier + chapter. Stable facts (исторические инциденты, даты подачи исков) — без пометки.

**Что работало.** Volatile-fact tagging позволяет lecturer review перед лекцией (1 day before) только short list, не полную главу.

**Что НЕ работало.** Designer оставил `[VFY-day-of для версий и цен в frontmatter]` теги в visible body слайдов 8, 15, 35 — leak. Это другой класс ошибки: marker предназначен для frontmatter / speaker notes, не visible. **Lesson saved earlier в Лекция 4 reflection; этот reflection re-confirm.**

## 12-case structure в Разделе 3

**Plan v2 design choice (owner-approved at GATE 0):** 12 case-слайдов «1 case = 1 slide» для navigability, vs 6-7 consolidated «1 slide = 2 cases» для density. Owner chose 12 detailed.

**Validation.** Каждый case unique enough, чтобы deserve dedicated slide. Critics в Phase 7.5 flag-нули «5 consecutive identical layouts s21-s25» — это была implementation issue (designer used same layout 5×), не plan issue. Fix: layout diversification (Bloomberg Law card / Verdict badge / Trial chip / Settlement matrix / Fair-use 4-factor) per s21-s25 — все теперь visually distinct.

**Insight.** Variety of emphasis (not just variety of content) prevents fatigue. 12 cases с same layout = boring marathon; 12 cases с different visual emphasis = engaging variety.

## Speaker notes 150-300 words pattern

**27/39 в range** (covers + dividers + Q&A short by design). Notes derived from chapter content, readable as student-facing material 2 weeks post-lecture.

**Что работало.** Speaker notes structure: assertion + evidence + implication, no «слева donut, справа bar» layout descriptions. Lecture content reusable как self-study reference.

**Lesson.** Notes — это второй учебный artefact, не lecturer prompts. Treat them as readable student text, not as «what to say». В производстве этот стандарт сохраняется хорошо.

## Cross-references к другим лекциям

**Soft cross-refs:**
- Lec-1 framing «где AI работает / где не» — Лекция 8 углубляет до 4 конкретных критериев
- Lec-3 архитектуры — Sora 2 / Veo 3.1 как API endpoints (устный bridge)
- Lec-5 financial-failure parallel — Сбер AI scoring как legal-risk frame
- **Lec-7 4-actor responsibility framework** — Лекция 8 имеет analog (artist/likeness owner ScarJo / training-data source Andersen / victim Arup / IP holder Sony) — параллель тонкая, не делает explicit new framework
- **Lec-9 bridge** — kinetic-stakes escalation (brand-trust failure → human-life failure), s39 hero image = X-62 VISTA F-16 DARPA ACE

**Что работало.** Soft cross-refs help students see course narrative arc, без force-fitting nicht-existent frameworks.

## Что не использовал из research dossier

Research dossier (4406 + 818 слов) включал больше material чем поместилось в лекции:
- Mid-tier image generators (Imagen 4 detail, Flux Pro pricing breakdown) — упомянуто briefly
- Suno SJ hearing dates evolution — упомянуто briefly
- Adobe Firefly Foundry детали — отложено как Лекция 3 cross-ref
- Lionsgate × Runway training data agreement details — упомянуто briefly

**Insight.** Research dossier > chapter > slides > speech по объёму. Каждый downstream artifact filters. Это правильный funnel — наличие лишнего material даёт outline flexibility, не overload.

## Что добавил бы если бы делал заново

1. **Hero на s01 + s39 С САМОГО НАЧАЛА** — не ждать owner intervention. Memory rule [[hero-images-required]] теперь это enforces.
2. **6-tier image acquisition в Phase 5 первого design pass** — не как «fix after mocks». Memory rule [[no-mock-fallbacks]] enforces.
3. **Russification в Phase 1 plan** — explicit Russification mandate в каждый producer agent prompt с самого начала. Memory rule [[russification]] enforces.
4. **Layout diversification план в Phase 1** — для 12-case sections, explicit emphasis-variety plan (big number / verdict badge / timeline / matrix / 4-factor breakdown).

Эти 4 improvements делают будущие лекции (Лекция 10+) faster производство и меньше owner-interventions.
