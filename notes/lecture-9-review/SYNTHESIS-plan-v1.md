# SYNTHESIS — Phase 1 plan critique (plan-v1.md)

**Дата:** 2026-05-20
**Target:** `notes/lecture-9-review/plan-v1.md`
**Critics:** methodology-critic + reader-simulator (text-only)
**Aggregated verdict:** **REVISE → v2** (reader-text flagged 2 P0 — нельзя двигаться в Phase 2 без fix)

---

## Verdict-таблица

| Critic | Verdict | P0 | P1 | P2 |
|---|---|---|---|---|
| methodology-critic | APPROVE-WITH-POLISH | 0 | 3 | 6 |
| reader-text | APPROVE-WITH-POLISH (но 2 P0!) | 2 | 3 | 3 |

**Convergent verdict:** **REVISE** (reader P0 — must-fix перед Phase 2 chapter).

**Counter-check (CLAUDE.md ENFORCED):** 2 P0 + 4 P1 в v1 → REVISE, не APPROVE-WITH-POLISH. Этот SYNTHESIS используем как fix-list для plan-v2.

---

## P0 (BLOCKING для Phase 2)

### P0-1 — Glossary gap (оба критика independently)
**Issue:** ~10 acronyms (SAR, ATR, ISR, EW, LAWS, OODA, HITL, BPSA, HALE, Bayesian NN) использованы в плане без явного определения. Студент ИУ6 блокирован первые 5-10 мин Р1.

**Fix в v2:**
- Добавить в Раздел 0 после keystone slide отдельный **«Glossary» mini-slide** с 6-8 ключевыми acronyms (SAR, ATR, ISR, EW, LAWS, OODA). Остальные (HITL, HOOL, HOTL, AMRAAM, V-BAT, CCA) — расшифровывать inline при первом упоминании.
- Mandate-line в Phase 2 brief: «book-editor расшифровывает каждый acronym при первом упоминании в chapter».

### P0-2 — Р2 Decide vendor-overload (reader-text)
**Issue:** 13 vendor/program names за 14 мин (Palantir MSS, Scale Donovan, Defense Llama, Thunderforge, Helsing Altra, Centaur, Anthropic-Palantir-AWS, NASA FDL FOXES, DAGGER++, Svod, Glaz, Groza, ZOV Maps). Студент выпадет к Р3.

**Fix в v2:**
- Резать до **5-6 named working cases** в Р2:
  - Palantir MSS (US flagship)
  - Scale Donovan / Defense Llama (foundation models for defense)
  - Helsing Altra (EU)
  - Anthropic-Palantir-AWS partnership (recent 2024-2025 narrative)
  - Russian C2 (Svod **OR** Glaz-Groza — выбрать один с caveat, не оба)
- Остальные (Centaur, FDL FOXES, DAGGER++, Thunderforge) — упомянуть строкой в "honorable mentions" boxed-list, не разворачивать.

---

## P1 (significant, fix перед Phase 2)

### P1-1 — LO1 mixes Bloom levels (methodology)
**Issue:** LO1 объединяет Remember (recall AI methods) + Apply (apply to case selection) — два уровня Bloom.

**Fix в v2:**
- Разбить на **LO1a (Remember):** «Distinguish ключевые AI-методы в aerospace/defense (CV/ML/DL/RL/foundation models) и их применимость».
- **LO1b (Apply):** «Применить критерии «когда AI / когда не AI» к конкретному use-case (заданный case study)».

### P1-2 — Р4 pacing нереалистичен (methodology)
**Issue:** 7 sub-sections × 2 мин = unrealistic для LAWS, UN GGE, ICRC, SKR, Maven, L1-L5 ladder, HITL.

**Fix в v2:**
- Объединить 4.3 ICRC + 4.4 Stop Killer Robots → один sub-section «International civil society stance» (3-4 мин).
- Дать **4.1 L1-L5 ladder** = 4 мин (центральный visual + operational definitions per level).
- Дать **4.6 HITL/HOOL/HOTL** = 3 мин (центральная mental model + visual).
- Остальные (UN GGE, Maven, Anthropic-Palantir + OpenAI ban shift, Russia votes) — по 2 мин.
- Total: 4+3+4*2 = 15 мин ✓

### P1-3 — L1-L5 ladder требует operational definitions (reader)
**Issue:** В Р4.1 — «MSS=L1, Saker Scout=L2» magic assignment без criteria.

**Fix в v2:**
- Добавить в plan-v2 §«L1-L5 ladder definitions»:
  - L1 = AI **выдаёт** information, human decides (Palantir MSS analyst).
  - L2 = AI **рекомендует** action, human authorises (Saker Scout target lock).
  - L3 = AI **executes** action в pre-authorised envelope, human supervises (Anduril Fury wingman).
  - L4 = AI **engages** target по pre-set rules, human может intervene (Patriot auto mode).
  - L5 = AI **executes lethal action** без human (LAWS — currently debated, not deployed).

### P1-4 — HITL visual, не bullet (reader)
**Issue:** Human-In-The-Loop (HITL) / Human-On-The-Loop (HOOL) / Human-Out-of-The-Loop (HOTL) — центральная mental model LAWS-блока. В плане упомянута строкой.

**Fix в v2:**
- В plan-v2 §«Р4.6 Human-in-the-loop» — explicit instruction для Phase 5 designer: визуализация trio HITL/HOOL/HOTL с конкретными примерами per уровень.

---

## P2 (polish, можно фиксить в Phase 2 brief, не блокирует)

### P2-1 — LO2 Lancet backup (methodology)
Lancet ATR rollback — backup case если IDF Lavender уйдёт в day-of dispute. Зафиксировать в plan-v2.

### P2-2 — Hook B недооценён (methodology)
Hook B (F-35 ALIS failure-first) лучше align с курсовой миссией «учить говорить нет неподходящему ИИ» чем Hook A (BEFORE/AFTER satellite). Reader-text **подтвердил** Hook A — оба правы pedagogically. Решение orchestrator + user в plan-v2: оставить **Hook A** (нейтральный, visual evergreen, ставит вопрос), Hook B = **backup**.

### P2-3 — 7 критериев в 4 мин (methodology)
Р5.1 — 7 критериев «когда не AI» за 4 мин = по 35 сек на критерий. Распределить **2-3 критерия по разделам** (Р1: «когда не AI для sense», Р2: «когда не AI для decide», Р3: «когда не AI для act»), а в Р5.1 — **consolidate matrix** 7 criteria в 1 slide + 2 мин explanation.

### P2-4 — Russian context 22-25% > 15-20% target (methodology + reader)
Reader **подтвердил**: 22-25% комфортно, без агитации. Methodology **рекомендует принять**: cost-of-removal = потеря Bauman-relevance. **Решение:** принять 22-25%, зафиксировать в plan-v2 и не резать в Phase 2.

### P2-5 — DoD Directive 3000.09 (methodology)
Открытый вопрос: отдельный слайд в Р4 или строка в Normative References? **Decision plan-v2:** строка в Normative References + краткое упоминание в Р4.2 (UN GGE context).

### P2-6 — Anthropic+OpenAI ban перенести Р2→Р4 §4.5 (methodology)
Plan-v1 упоминает Anthropic-Palantir-AWS partnership в Р2 (Decide). Methodology рекомендует перенести в Р4.5 «Recent shift in big-tech defense posture» (2024-2025 narrative bound к Maven walkout).

### P2-7 — Russian-context civilian dual-use balance (reader)
В Р3 (Act) — все Russian кейсы defense (Geran-2, Lancet). Reader просит **один civilian case**: Cognitive Pilot (КАМАЗ autonomous trucking) или VisionLabs (civil CV).

**Fix:** добавить в Р3 одну строку про Cognitive Pilot как civilian counterpoint Russian dual-use.

### P2-8 — OODA-sourcing (reader)
Boyd 1976 USAF — historic context добавляет доверие к оси. В plan-v2 §«Keystone axis» — одна строка про авторство.

### P2-9 — Sber GigaChat на ISS (reader)
Усилить caveat или удалить совсем. **Decision plan-v2:** удалить (single-source, не верифицировано независимо, не критичен для narrative).

---

## Что НЕ менять (convergent consensus)

- ✓ Keystone axis **OODA** (Sense → Decide → Act) с инъекциями dual-use bridge (Р0) + L1-L5 ladder (Р4)
- ✓ 6 разделов структура (0/1/2/3/4/5)
- ✓ Hook **A** (BEFORE/AFTER satellite) как primary, Hook B как backup
- ✓ Strict-in 39-56% (counter-check PASS — обширный запас)
- ✓ Russian context 22-25% (reader confirmed комфортно)
- ✓ Р4 целиком strict-in (LAWS / UN GGE / ICRC / Maven / HITL / Russia votes)
- ✓ Closing callback в Р5.4
- ✓ Tools-per-taxonomy L4+ ENFORCED — PASS
- ✓ Aerostate исключён (research recommendation honored)
- ✓ Sber GigaChat ISS — **теперь удалить** (P2-9)

---

## Phase 2 readiness gate

Условие старта chapter draft (Phase 2):
1. ✓ plan-v2 содержит все 2 P0 fixes (glossary, Р2 vendor-cut).
2. ✓ plan-v2 содержит все 4 P1 fixes (LO1 split, Р4 pacing, L1-L5 definitions, HITL visual mandate).
3. ✓ plan-v2 P2 fixes — большинство применены (полировка), допустим перенос 1-2 в book-editor brief.
4. ✓ book-editor получает Phase 2 brief со **всеми решёнными вопросами**.

После plan-v2 — quick orchestrator re-read (verify P0/P1 closed) → Phase 2 chapter draft.

---

## Next action

Спавн book-editor для **plan revision v1 → v2** с explicit fix-list выше.
