# methodology-critic — критика chapter v1 (Phase 3)

**Дата:** 2026-05-20
**Target:** `library/lectures/lec-09/chapter.md` (906 строк, ~14 830 слов, v1 draft)
**Critic:** methodology-critic
**Verdict:** **APPROVE-WITH-POLISH**

## TL;DR

Chapter v1 — методически крепкая, структурно завершённая, превосходящая baseline lec-07/08. Все 15 P0/P1/P2 items из SYNTHESIS-plan-v1 закрыты. **Independent strict-in count = 44.5%** (book-editor reported 40.7% — занижен; реальная доля выше), distribution holistic: R1=40% / R2=50% / R3=46% / R4=100% / R5=46%. Keystone-axis ENFORCED PASS. Tools-per-taxonomy L4+ PASS для Sense и Act, **PARTIAL для Decide** (P1-1). Glossary mandate PASS на 6 ключевых acronyms, но **~9 acronyms не определены inline** при первом упоминании (P1-2). Internal numerical inconsistency UNGA votes (P1-3). Criteria numbering inconsistent (P1-4). Q&A backup отличная.

**Counter-check:** 4 P1 < 5 → APPROVE-WITH-POLISH корректно (не REVISE).

## Counter-check (ENFORCED)

| Check | Result |
|---|---|
| AI-Failure ≥30% strict-in | **PASS — 44.5%** (independent count) |
| Distribution holistic | **PASS** — R1=39.9% / R2=49.9% / R3=46.5% / R4=100% / R5=45.5% |
| Keystone-axis | **PASS** — §0.2 keystone before R1, заголовок про OODA, Boyd USAF 1976 sourcing |
| Tools-per-taxonomy L4+ | **PASS Sense + Act / PARTIAL Decide** (см. P1-1) |
| Glossary mandate | **MOSTLY PASS** — §0.3 6 acronyms ✓; **9 inline misses** (P1-2) |
| Q&A backup quality | **PASS** — 10 items, depth 100-200 слов |
| Anti-pattern grep | **PASS — 0 hits** |

### Strict-in distribution (independent count)

| Раздел | Words total | Strict-in words | Share |
|---|---:|---:|---:|
| R1 Sense | 2 253 | 898 | 39.9% |
| R2 Decide | 2 261 | 1 128 | 49.9% |
| R3 Act | 2 148 | 998 | 46.5% |
| R4 Boundary | 2 189 | 2 189 | 100% |
| R5 Synthesis | 1 054 | 480 | 45.5% |
| **Total body** | **12 803** | **5 693** | **44.5%** |

## P0 issues (BLOCKING для Phase 4)

**Нет P0.** Chapter не блокирован.

## P1 issues (significant)

### P1-1 — Tools-per-taxonomy для Decide: missing 3 obligatory элемента
**Location:** §2.1-2.3 (lines 295-338).
**Issue.** Sense (line 208) и Act (line 409) имеют consolidated adoption-direction + anti-hype + infra-separation. **Decide отсутствует.** 5 cases с глубиной есть, но не агрегированы на уровне звена.
**Fix.** В §2.1 после line 302 добавить параграф: «**Adoption направление по Decide.** Растёт по числу контрактов (Palantir MSS $1.3B ceiling, Scale Donovan на 3 классифицированных сетях, Anthropic IL6); **но LLM hype outpaces verifiable ground truth**. **Анти-hype:** «accuracy 90%» ≠ «90% правильных решений» — cost-asymmetry FP↔FN. **Инфраструктура (FedRAMP HIGH, IL4/IL6, SC2S/SIPR/JWICS — три уровня secrecy compartmentation) — отделена от AI capability**: это authorization-стек, а не модель.»

### P1-2 — Inline-расшифровка acronyms нарушена для 9 терминов

| Acronym | First use | Expansion |
|---|---:|---|
| PIJ | line 93 | Palestinian Islamic Jihad |
| CCA | line 91 | Collaborative Combat Aircraft, беспилотный wingman |
| DoD | line 103 | Department of Defense |
| NGA | line 186 | National Geospatial-Intelligence Agency |
| NRO | line 190 | National Reconnaissance Office |
| GAO | line 237 | US Government Accountability Office |
| ROE | line 423 | Rules of Engagement |
| IHL | line 558 | International Humanitarian Law, международное гуманитарное право |
| BVR | line 423 | Beyond Visual Range |

### P1-3 — UNGA votes «5 против» vs «3 страны» numerical inconsistency
**Locations:** lines 93, 537, 627, 742.
- Введение/§4.2: «156 за, **5 против**, 8 воздержавшихся» (2025)
- §4.7: «Россия — одна из **трёх** стран, голосующих систематически против»
- Q&A В1: «**трёх** стран» (другая тройка = US/RU/CN)

**Fix.**
- §4.7 line 627: «**Россия — одна из трёх стран, голосовавших в обоих 2024 и 2025 годах подряд против** (Беларусь, Северная Корея, Россия — стабильное ядро no-vote блока)»
- Q&A В1 line 742: «**трёх великих держав — США, Китай, Россия**»

### P1-4 — 7 критериев нумерация распределена непоследовательно
**Locations:** §1.8 (line 277), §2.7 (line 383), §3.6 (line 487), §4.6 (line 614), §5.1 matrix.
**Fix.**
- §1.8: «**Критерий 1 (распределение)** ... **Критерий 2 (single-sensor)**» + пометка «общая нумерация»
- §2.7: «**Критерий 3** ... **Критерий 4** — для звена Decide»
- §3.6: «**Критерий 5** ... **Критерий 6** — для звена Act»
- §4.6: «**Критерий 7 (cross-cutting)**: граница HOOL → HOTL — treaty-territory»

## P2 issues (polish)

1. §4.7 line 631 «не предлагаем встать в политическую позицию» → переписать «не предписываем определённую политическую позицию — это его выбор»
2. §5.4 closing для slide callback — Phase 5 brief mandate
3. §2.3 honorable mentions сжать до 1-строки bullets
4. **§Helsing line 311 «Daniela Ek» → Daniel Ek (gender)** — verify with fact-checker
5. «Кафедра ИУ-Х» line 678 — verify номер
6. Q&A В4 закрытые программы РФ — add 50-80 слов «как искать»
7. DO-178C/ARP4754A line 701 — add 30 слов про DAL-A scale
8. §5.4 closing — добавить 1 строку про dual-use bridge callback

## SYNTHESIS-plan-v1 closure check
**ALL 15 items PASS.**

## Strengths
1. Keystone-axis ENFORCED — образцовая реализация
2. AI-Failure 44.5% comfortable margin + holistic distribution
3. Tools-per-taxonomy Sense + Act PASS
4. Three-frame engineering analysis (civil cert + defense policy + IHL)
5. L1-L5 ladder operational table — slide-ready
6. HITL/HOOL/HOTL триада с «ms to intervention» takeaway
7. Lavender bias treatment симметричен
8. Russian context симметричен западному
9. 100 sources diversity (peer-reviewed + gov audit + NGO + industry + primary investigation)
10. Cross-lecture handoffs explicit (lec-06 CAD, lec-2-3 foundations)
11. Q&A backup — best в курсе to-date
12. 0 anti-pattern violations
13. No-Extra-Content Rule соблюдён

## Verdict justification
- 0 P0
- 4 P1 (< 5 → APPROVE-WITH-POLISH PASS)
- 8 P2

Phase 4 revision можно запускать после fact-checker return.
