# SYNTHESIS — Phase 3 chapter critique (chapter v1)

**Дата:** 2026-05-20
**Target:** `library/lectures/lec-09/chapter.md` (906 строк, ~14 830 слов)
**Critics:** methodology-critic + fact-checker + reader-simulator (text-only)
**Aggregated verdict:** **REVISE** (fact-checker P0 overrides — directional inversion §4.7 структурный gap)

---

## Verdict-таблица

| Critic | Verdict | P0 | P1 | P2 |
|---|---|---|---|---|
| methodology-critic | APPROVE-WITH-POLISH | 0 | 4 | 8 |
| reader-text-only | APPROVE-WITH-POLISH | 0 | 5 | — |
| fact-checker | **REVISE** | **2** | 5 | 3 |

**Aggregate:** **REVISE** (fact-checker P0 escalates выше APPROVE-WITH-POLISH consensus от других двух).

**Counter-check:** 2 P0 + ~12 unique P1 + ~11 P2 → REVISE верный.

---

## P0 — BLOCKING (fact-checker)

### P0-1 — §4.7 directional inversion «Россия одна из трёх стран против UN LAWS»

**Location:** lines 627-628.

**Issue:** Nov 6 2025 First Committee vote (A/C.1/80/L.41): **6 стран против — Беларусь, Бурунди, КНДР, Израиль, Россия, США.** Россия больше не «одна из трёх». США сместились с «за» (2024) на «против» (2025). Нарратив §4.7 «Россия выпадает из мейнстрима» **структурно ломается**.

**Sources:** [UN Press ga12736](https://press.un.org/en/2025/ga12736.doc.htm), [US Geneva Mission 4 Nov 2025](https://geneva.usmission.gov/2025/11/04/80th-session-of-the-united-nations-general-assembly-first-committee-cluster-4-conventional-weapons/).

**Fix (точная замена, lines 627-628):**

> «Россия — одна из стран, голосующих против резолюций UN LAWS. На голосовании ноябрь 2024 года резолюция прошла 161/3/13; против — Беларусь, КНДР, Россия (Stop Killer Robots, 2024). На голосовании ноябрь 2025 года резолюция прошла 164/6/7 (UN official press; 156/5/8 по Stop Killer Robots); против — Беларусь, Бурунди, КНДР, Израиль, Россия, **США** (UN A/80/PV; US Geneva Mission explanation of vote, 2025). Это значимый сдвиг: США в 2024 голосовали «за», в 2025 — «против», объяснив противодействием конкретной формулировке про переговоры о binding instrument, не отказом от обсуждений LAWS. Россия остаётся в позиции против с 2018 года, но «лагерь против» в 2025 — больше 3 стран, и состав политически разнообразен.»

**Дополнительно:** пересмотреть narrative-интонацию §4.7 в целом. Тезис «инженер не остаётся нейтральным» оставить; «Россия выпадает» заменить на «государства разной позиции, но engineering design определяется одинаково независимо от политического голосования».

### P0-2 — §4.2 vote tally 156/5/8 vs 164/6/7 disambiguation

**Location:** line 537.

**Issue:** Конфликт первоисточников. UN official press = 164/6/7 (A/C.1/80/L.41). Stop Killer Robots = 156/5/8. По evidence hierarchy UN press authoritative.

**Fix (line 537):**

> «6 ноября 2025. Первый комитет, третья подряд резолюция: **164/6/7** (UN official press; 156/5/8 по Stop Killer Robots — расхождение связано с разными счётами First Committee и plenary) `[VFY-day-of]`.»

---

## P1 — Significant (12 unique consolidated)

### P1-1 — Tools-per-taxonomy для Decide звена missing 3 элемента (methodology)
**Location:** §2.1-2.3 (lines 295-338).
**Fix:** Добавить в §2.1 после line 302 параграф с consolidated adoption-direction («растёт по числу контрактов»), anti-hype («accuracy ≠ 90% правильных решений»), infrastructure-separated («FedRAMP/IL4-6/SC2S — три уровня secrecy compartmentation отделены от AI capability»).

### P1-2 — 9 acronyms inline-expansion missing (methodology)
| Acronym | Line | Expansion |
|---|---:|---|
| PIJ | 93 | Palestinian Islamic Jihad |
| CCA | 91 | Collaborative Combat Aircraft |
| DoD | 103 | Department of Defense |
| NGA | 186 | National Geospatial-Intelligence Agency |
| NRO | 190 | National Reconnaissance Office |
| GAO | 237 | US Government Accountability Office |
| ROE | 423 | Rules of Engagement |
| IHL | 558 | International Humanitarian Law |
| BVR | 423 | Beyond Visual Range |

### P1-3 — Lattice + Hivemind undefined в Введении/§3.2 (reader)
**Location:** §3.2 (Anduril Fury + Shield AI V-BAT). Reader блокирован.
**Fix:** Inline-расшифровка при первом упоминании: «Lattice (Anduril proprietary OS для autonomous mesh-coordination)» и «Hivemind (Shield AI autonomy stack)».

### P1-4 — UNGA «5 vs 3 страны» internal numerical inconsistency (methodology, разрешает P0-1)
Уже addressed через P0-1 fix. Q&A В1 line 742 также fix: «трёх великих держав — США, Китай, Россия».

### P1-5 — 7 критериев нумерация распределена непоследовательно (methodology)
**Locations:** §1.8 (line 277), §2.7 (line 383), §3.6 (line 487), §4.6 (line 614), §5.1 matrix.
**Fix:** Глобальная нумерация — §1.8 «**Критерий 1/2**», §2.7 «**Критерий 3/4**», §3.6 «**Критерий 5/6**», §4.6 «**Критерий 7 (cross-cutting)**: HOOL→HOTL — treaty-territory».

### P1-6 — §2.2 Scale Donovan vendor density (reader)
**Location:** §2.2 case 2 (Scale Donovan + Defense Llama + Thunderforge + 4 classified levels в одном параграфе).
**Fix:** Mini-table «product / date / client / capability» вместо prose-list. 4 rows.

### P1-7 — §2.3 honorable mentions skipped at read-pace (reader + methodology)
**Location:** lines 324-336.
**Fix:** Сжать каждый bullet до 1 строки (убрать parenthetical-описания). Сейчас 12 строк → 6 строк.

### P1-8 — §4.1↔§4.6 cross-pointer missing (reader)
**Location:** §4.1 L1-L5 table + §4.6 HITL trio — должны читаться вместе для понимания L3↔L4 границы.
**Fix:** В §4.1 после table — explicit pointer: «См. §4.6 для HITL/HOOL/HOTL mapping per уровень». В §4.6 в начале — «продолжение §4.1 L1-L5 ladder». Опционально: добавить колонку «ms-to-intervention» в §4.1 table.

### P1-9 — §1.3 edge-AI on-orbit flat list (reader)
**Location:** §1.3 (4 программы Slingshot/Φ-sat-2/SDA/TerraTech подряд).
**Fix:** Сгруппировать по mission type: «demonstrators (Φ-sat-2)», «production telemetry (Slingshot Agatha)», «SDA tracking (Tranche 3)», «commercial archive (TerraTech)».

### P1-10 — ICRC position paper год off (fact-checker)
**Location:** line 553, 558.
**Fix:** «(ICRC position paper 2021; Vienna Conference statement 2024; updated 2025)». Quote attribution «(ICRC, 2021 — повторено в 2024 Vienna statement)».

### P1-11 — «Daniela Ek» → «Daniel Ek» (fact-checker + methodology P2-4)
**Location:** line 311.
**Fix:** Daniel Ek (мужское имя, Spotify co-founder).

### P1-12 — F-35 cost per flight hour off-by-$2k (fact-checker)
**Location:** line 239.
**Fix:** «около $42 000 (GAO-22-105128, 2022)» либо «$42-44k в разных GAO reports».

### P1-13 — Geran-2 «5 000+/month» overstated (fact-checker)
**Location:** line 427.
**Fix:** «производительность около 2 700-3 000 дронов в месяц с plan-capacity 5 000+ (Ukrainian Defence Intelligence, 2025; ISW, 2025) `[VFY-day-of]`».

---

## P2 — Polish (11 consolidated)

### Methodology P2 (8)
- P2-m1 §4.7 line 631 «не предлагаем встать в политическую позицию» → «не предписываем определённую позицию — это его выбор»
- P2-m2 §5.4 closing — Phase 5 brief mandate для slide bookend (заголовок + 3 строки)
- P2-m3 §2.3 honorable mentions сжать (уже P1-7)
- P2-m4 §5.2 «ИУ-Х» — verify номер кафедры на bauman.ru
- P2-m5 Q&A В4 закрытые программы РФ — добавить 50-80 слов «как искать»
- P2-m6 DO-178C/ARP4754A в §5.2 line 701 — добавить 30 слов про DAL-A scale
- P2-m7 §5.4 closing — 1 строка про dual-use bridge callback (Опция В)
- P2-m8 §4.7 переписать политическую интонацию (уже addressed P0-1)

### Fact-checker P2 (3)
- P2-f1 Line 465 Patriot Tornado date — «22-23 марта 2003» (overnight)
- P2-f2 Line 419 V-BAT India — добавить «$35M initial emergency procurement»
- P2-f3 Line 441 737 MAX 20-month grounding — clarify «US un-grounding; международная до 2022»

---

## Что НЕ менять (convergent consensus)

- ✅ Keystone axis OODA + sourcing (§0.2) — образцовая реализация
- ✅ 6 разделов структура
- ✅ AI-Failure 44.5% strict-in distribution (verified independently methodology)
- ✅ L1-L5 ladder operational definitions (§4.1) — slide-ready
- ✅ HITL/HOOL/HOTL trio (§4.6) — best mental model в курсе
- ✅ Lavender bias treatment симметричный
- ✅ Russian context distributed балансированно
- ✅ 100 sources diversity (peer-reviewed + gov audit + NGO + industry)
- ✅ Q&A backup quality 10 items
- ✅ Cross-lecture handoffs (lec-06, lec-2-3)
- ✅ Anti-pattern grep clean
- ✅ Trust-but-verify tone

---

## Phase 4 readiness gate

После chapter v2 revision:
1. ✅ Обе P0 (UN LAWS facts) closed verifiably
2. ✅ Все 13 P1 fixes applied
3. ✅ P2 fixes большинство applied
4. ✅ Subset-rerun fact-checker по UN LAWS facts (verify P0 closure) — рекомендуется
5. ✅ Strict-in доля не падает ниже 44%
6. ✅ Document size остаётся ~13-15k слов (P1 fixes — добавления, P1-7 = сокращение)

После chapter v2 → Phase 4.5 pre-gate walkthrough → USER GATE A.

---

## Next action

Спавн book-editor для **chapter revision v1 → v2** с explicit fix-list из 2 P0 + 13 P1 + 11 P2.
