# reader-simulator (rendered, 2 weeks later) — критика slides v2

**Дата:** 2026-05-20
**Verdict:** **APPROVE-WITH-POLISH** (1 P0 + 5 P1 + 2 P2)
**Self-containedness:** 27/34 = **79.4%** (под 85% production threshold)

---

## TL;DR

Через 2 недели у меня в голове прочно держится keystone OODA (s05 + s33 двойной reinforcement), L1-L5 ladder, HITL/HOOL/HOTL триада, 7-criteria matrix, и три canonical failures: Lavender (10%×37000=3700), MCAS (346 deaths, 4 урока), Maven 3-era shift. Слабее держатся: ALIS (название — да, причины provala — fuzzy), Vincennes (помню UI под stress, но связь с LLM не очевидна без notes), и весь **s18 vendor landscape — структурный blocker** (5 вендоров + 6 acronyms densely packed).

---

## P0 (BLOCKING — structural)

### P0-1 — s18 (Decide vendor landscape, PNG s-15) NOT self-contained

**Issue:** 5 vendors × 6 acronyms × 5 financial figures densely packed на одном слайде. Через 2 нед без живой лекции я не восстановлю vendor map.

- Acronyms без inline def: IL6, FedRAMP, JWICS, SIPR, SC2S, IDIQ
- Russian C2 «Svod / Glaz / Groza» — что это?
- $1.3 млрд, €12 млрд, IL6 — числа без visual hierarchy

**Fix options:**
- A) SPLIT на 2 slides: «US vendors (Palantir + Scale + Anthropic-AWS)» и «European + Russian C2»
- B) Keep one slide, но добавить vendor logos + inline acronym tooltips + visual hierarchy для финансовых figures

---

## P1 (significant — должны fix)

### P1-1 — 8 acronyms без inline definition в visible body

| Acronym | Slide | Expansion needed inline |
|---|---|---|
| CCA | s20 (Anduril Fury) | Collaborative Combat Aircraft |
| MCAS | s23 | Maneuvering Characteristics Augmentation System |
| IFF | s23 Patriot callback | Identification Friend or Foe |
| ROE | s21, s25 | Rules of Engagement |
| BVR | s21 X-62A | Beyond Visual Range |
| ALIS | s11 | Autonomic Logistics Information System |
| FedRAMP HIGH | s18 | Federal Risk and Authorization Management Program |
| FMEA / FTA | s23 | Failure Mode and Effects Analysis / Fault Tree Analysis |

### P1-2 — Russian codenames без context
- Krasukha-4 / Borisoglebsk-2 (s14) — inline «российские наземные РЭБ-системы»
- Geran-2 / Shahed-136 (s22) — inline «российская модификация Shahed-136 loitering munition»

### P1-3 — s11 ALIS failure 3 conditions visible
3 нарушенных условия (быстрый feedback / ground truth / FP-cost < FN-cost) — currently только в speaker notes. Сделать visible на slide.

### P1-4 — Vincennes-LLM мост (s17) visible
Currently только в notes. Сделать visible одной фразой: «LLM confident BS = Aegis 1988 pattern».

### P1-5 — Photo identification clarity
- s11: который plane Airbus / который F-35
- s17: caption «Iran Air A300, 290 KIA»

---

## P2 (polish)

### P2-1 — Vendor logos на s18
Logo-based identification вместо text-only улучшит recognition.

### P2-2 — Section 4 entry frame
«Граница и регулирование» — entering без явного «теперь мы поднимаемся над OODA». Visible frame одной строкой.

---

## Concept retention through 2 weeks

| Concept | Retention | Notes |
|---|---|---|
| OODA / Sense→Decide→Act | ✅ Strong | s05 + s33 двойной reinforcement |
| L1-L5 ladder | ✅ Strong | Table + ms-to-intervention — самодостаточная |
| HITL/HOOL/HOTL | ✅ Strong | 3 human-position panels + L1-L5 mapping |
| 7 criteria | ✅ Strong | Working tool |
| «Accuracy не та метрика» | ✅ Strong | 10%×37000=3700 explosive |
| Cost-asymmetry $300 vs $3M | ✅ Strong | Gold callout |
| Maven 3-era | ✅ Strong | Pivot markers |
| ms-to-intervention numbers | ⚠️ Medium | Concept ясен, конкретные числа fuzzy |
| Decide vendor landscape | ❌ Weak | s18 структурно слабый |

---

## Failure-block retention

| Failure | Retention | Урок explicit visibly? |
|---|---|---|
| Lavender | ✅ Strong | ✅ 3 урока explicit |
| MCAS | ✅ Strong | ✅ 4 урока explicit |
| Vincennes 1988 | ⚠️ Medium | ⚠️ LLM-мост только в notes |
| Lancet rollback | ⚠️ Medium | ⚠️ «Demo ≠ продакшен» — есть |
| F-35 ALIS | ❌ Weak | ❌ 3 нарушенных условия только в notes |
| Patriot 2003 | ✅ Strong | ✅ Automation bias visible |
| GPS spoofing | ✅ Strong | ✅ 32× метрика |
| Adversarial SAR | ⚠️ Medium | ⚠️ mechanism fuzzy |

---

## Strict-in AI-Failure доля (independent check)

Через 2 нед я уверенно помню Lavender, MCAS, Patriot, ALIS-как-failure, Maven shift, UN GGE/ICRC + 7-criteria + «когда не AI» = ~12-15 slides из 34 (~40-44%). **Выше 30% threshold с большим запасом. PASS.**

---

## Schemas retention (13/14 self-sufficient через 2 weeks)

s05 OODA chain, s07 sensor types, s09 constellation, s11 RU sense, s12 cost-asymmetry, s17 4-source pipeline, s21 Lavender funnel, **s32 L1-L5 ladder (excellent)**, s33 UN GGE chronology, s35 Maven timeline, **s36 HITL/HOOL/HOTL triad (excellent)**, s39 7-criteria matrix, s42 closing — все self-sufficient. Только s18 vendor landscape — fail.

---

## Glossary effectiveness

**6 main s04:** SAR, ATR, ISR, EW, LAWS, OODA — все хорошо. ✅

**Promised by glossary footer:**
- HITL/HOOL/HOTL — ✅ defined visibly на s-28
- MCAS — ❌ acronym not raspshifrovan visibly на s-23
- CCA — ❌ not defined visibly на s-20
- IFF — ❌ not defined visibly на s-23

---

## Final assessment

Concept каркас лекции (OODA, L1-L5, HITL/HOOL/HOTL, 7 criteria) — excellent для 2-weeks-later self-study, retains прочно. Failure-блоки Lavender + MCAS — best-in-deck по explicit lesson formulation. **Главный 2-weeks-later blocker — s18 vendor landscape + acronym density** на 6-8 slides. Через 2 нед без живой лекции я уверенно восстанавливаю keystone framework и canonical failures, но детальную vendor map — нет.

**Verdict:** APPROVE-WITH-POLISH (1 P0 structural — s18 redesign + 5 P1 inline acronym glossing).
