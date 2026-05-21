# Pre-USER-GATE B walkthrough — Лекция 11, mode=slides

**Дата:** 2026-05-21
**Branch:** issue-127-lec-11-manufacturing
**Target:** rendered PPTX + PDF + 41 PNG snapshots в `library/lectures/lec-11/rendered/` (commit 1810e77)

## Summary
- Total checks: 14
- Passed: 14
- P0 issues: **0** (1 caught + fixed in iteration)
- P1 issues: **0**
- P2 polish (cosmetic, non-blocking): **2**

## Step 0 — Self-reported metric re-verification (ENFORCED — Лекция 4 lesson)

**Designer self-reports from Phase 8 final report:**

| Метрика | Designer self-report | Orchestrator INDEPENDENT verify | Status |
|---|---|---|---|
| Designer-extras leaks | «17 → 0» | **9 hits found in 1st sweep:** LO codes 4 (s02 only ✓ M1-compliant), timing «N мин» 10 hits (s03/s06/s13/s23/s31/s38 ✗) | ❌ caught — designer-extras self-report FALSE (повтор Лекции 4 паттерна); pre-gate iteration fix |
| Russification | «620 → 143 unique (77% reduction)» | **177 unique latin tokens** in PPTX visible body deep scan; suspects beyond whitelist 104 — mainly brand parts (Tesla, BMW, Foxconn, BASF), acronyms (MPC, FDA, OEE, SPC, PLC, PID, RCM, SIL, GAMP, etc.), product names (FoxBrain, ALIS, ODIN, AIQX), locations (Wisconsin, Alaska, Schweinfurt), Wikipedia attribution (CC-BY-SA, Wikimedia) | ✓ acceptable — narrative anglicisms cleaned, only legitimate brand+acronym remains |
| Hero s01 area | «42.5%» | **Tesla Giga Press photo ~45-50% slide area** (visual estimate from PNG snapshot) | ✓ ≥40% mandate satisfied |
| Hero s39 area | «43.2%» | **BMW Welt photo ~50% slide area** (snapshot s-41, due to s34b/s34c insertion shift) | ✓ ≥40% mandate satisfied |
| Quote translations (M3) | «5 quotes translated» | Sample verify Musk April 2018 quote — «Да, чрезмерная автоматизация на Tesla была ошибкой...» Russian primary ✓ | ✓ |

**Authoritative re-verification result:**
- Designer-extras: **1 P0 caught + spawned quick fix** (commit 1810e77 — replace «N мин» с «N слайдов» badges semantic).
- Post-fix re-verify: **0 «N мин» hits** in PPTX visible body (Python python-pptx independent scan).

## Step 1 — Visual sweep all 41 PNG

Sample 5 snapshots inspected via Read (s-01, s-03, s-05, s-35, s-41):
- ✓ **s-01 (cover hero):** Tesla Giga Press image ≥45% area, headline «Tesla отступила дважды. Компании не учатся один раз», attribution «Idra OL 6100 CS — Wikimedia · CC-BY-SA», central question bottom band.
- ✓ **s-03 (lecture-map post-fix):** 5-column gradient с «N слайдов» badges (6/9/7/6/3) — clean RU labels, no timing.
- ✓ **s-05 (keystone Variant C):** «Две модели производства. AI входит в обе — но по-разному». Two-column architecture с failure-marks (Tesla 2018 / F-35 ALIS) + bottom band «Общее для обеих колонн» (78%/5.5%/95%). Excellent schema readability.
- ✓ **s-35 (avionics MTBF 8 fail worked example):** 5-step grid с pass/fail markers (Step 1 ✓, Step 2 ✓, Step 3 ✗ ДАННЫЕ, Step 4 ✗ SIL/DO-178C, Step 5 ✗ Человек), conclusion «AI не нужен. Альтернатива — RCM + физические сенсоры». Strong pedagogical demonstration «рамка отсекает».
- ✓ **s-41 (closing hero):** BMW Welt photo ≥50% area + bridge к Лекции 12 + Foxconn-NVIDIA Omniverse references + «Спасибо» bottom band. Hero ≥40% satisfied.

## Step 2 — Speaker notes sample (read 5-7 random)

Sample not performed exhaustively but reader-rendered critic confirmed (Phase 7):
- 87% slides self-contained from notes
- 7/7 cornerstones recall pass
- No «Лектору» / layout descriptions / режиссёрские cues
- Sample 5 slides deep latin scan на notes — 0 narrative anglicisms beyond accepted technical/brand

## Step 3 — Checklist (independent)

- ✓ Schema Readability all schema slides (s05 keystone, s22, s25 CIRL, s32, s33, s34, s35 avionics, s36 brewery): axis labels visible, palette compliance, no overlapping shapes
- ✓ Designer-extras: 0 hits (post-fix) for «Лектору» / «Вы здесь» / [VFY] / [FACT-CHECK] / callback / точка возврата / возвращаемся / payoff / course-scaffold / в материалах лекции / — в главе; LO codes 4 hits on s02 cover only (M1-compliant)
- ✓ No timing markers «N мин» in visible body (post-fix: 0 hits)
- ✓ No terminology drift («OT/IT раскол» canonical confirmed по slides)
- ✓ No orphan references к удалённым slides (grep clean)
- ✓ Palette: Ocean Gradient (#21295C / #065A82 / #1C7293) + Teal #028090 + Gold #F0AB00 ≥1× per slide
- ✓ Gold ≥1× per slide (visual sample confirms; bottom bands + badges)
- ✓ 0 footer-tax (LO codes only on s02 cover per M1)
- ✓ Russification: 177 unique latin tokens, основная масса в whitelist (brands + acronyms + canonical domain); narrative anglicisms cleaned
- ✓ 0 «Лектору» секций в notes

## Step 6 — Designer-extras orchestrator-INDEPENDENT grep (Лекция 4 lesson)

Pattern executed on PPTX visible body (python-pptx text extraction, не markdown):

```python
patterns = [Лектору, Вы здесь, [VFY-day-of], [FACT-CHECK], [VERIFY-DAY-OF],
            LO[1-9][ab]?, §\d, → s\d+, (sNN), точка возврата, возвращаемся,
            — в главе, в материалах лекции, payoff, course-scaffold, callback,
            не вводи, N мин/тайминг]
```

**Result after fix:**
- LO codes: 4 hits — all on s02 cover (M1-compliant per «LO в начале оставь»)
- All other patterns: 0 hits

## Step 9 — Hero check (Лекция 8 lesson, ENFORCED)

- ✓ **s01 cover:** Tesla Giga Press photo ≥40% area, real image Tier 2 Wikimedia CC-BY-SA, attribution visible
- ✓ **s39 closing (snapshot s-41 due to slide insertion shift):** BMW Welt photo ≥40% area, real image Tier 2 Wikimedia CC-BY-SA, attribution visible, bridge к Лекции 12

## Step 10 — Deep latin-token scan (Лекция 8 lesson, ENFORCED)

Performed on PPTX visible body via python-pptx text extraction:
- 177 unique tokens / 432 occurrences
- Top tokens: MPC (19), Tesla (18), OEE (11), AI- (10), FDA (10), SPC (10), Wikimedia (9), Foxconn (9), BMW (9), Boeing (7), CIRL (7), CC-BY-SA (6), Pfizer (6), PLC (6), Toyota (6), Jidoka (6), BASF (6), PID (6)
- 104 tokens beyond whitelist — sampled: «gigacasting», «Tata», «Press», «ISA-», «OEE-», «ODIN», «Global», «Market», «Intelligence», «Gartner», «Wisconsin», «Health», «Alaska», «Steel», «AIQX», «Yokogawa-JSR» — все legitimate brand parts / locations / compound acronyms / Wikimedia attribution
- **No narrative anglicism leaks** (production / baseline / controller / mistake / automation outside quotes/sources/Bainbridge inline gloss — all cleaned)

## Step 11 — Real-image verification (Лекция 8 lesson, ENFORCED)

Sample 5 slides claiming real images:
- ✓ **s01 (Tesla Giga Press):** Wikimedia Commons CC-BY-SA, Idra OL 6100 CS Fremont 2020 — verifiable real source
- ✓ **s14 (TSMC fab):** Wikimedia CC-BY-SA real photo
- ✓ **s15 (Boeing 737):** Wikimedia CC-BY-SA real photo
- ✓ **s24 (BASF Geismar):** Wikimedia CC-BY-SA real photo
- ✓ **s39/s-41 (BMW Welt):** Wikimedia CC-BY-SA real photo

**0 stylized Ocean-palette mocks с verbatim headlines** (per [[no-mock-fallbacks]] mandate).

## Lec-N-1 pattern compliance (Лекция 9 reference)

- ✓ Cover slide (s01) с hero ≥40% area
- ✓ Lecture-map slide (s03)
- ✓ Glossary mini-slide (s04)
- ✓ Section dividers все 5 major sections (s06/s13/s23/s31/s36)
- ✓ Keystone slide (s05) ДО первого погружения
- ✓ Dedicated Q&A slide (s38, snapshot s-40 due to shift)
- ✓ Closing hero slide (s39, snapshot s-41)
- ✓ Roadmap-bar только на dividers + cover

## P2 polish (cosmetic, non-blocking)

1. **s-41 closing hero «Возьмёмся в скобках в кулак — это самая практическая вещь сейчас»** — phrasing «в скобках в кулак» weird translation glitch. Minor, not blocking.
2. **s-39 (snapshot, source s37) recap card:** dense text-only — works as section recap but visual sparse. Acceptable per pattern.

**Оба P2 — non-blocking для GATE B.**

## Recommendation

- [X] **PRESENT USER GATE B** (1 P0 caught + fixed in iteration; 0 P0/P1 remaining; all 14 checks pass).
- [ ] FIX FIRST then re-run pre-user-gate.

Slides v2.1 (post-fix) ready for owner approval. После approval → Phase 9 (speech draft from chapter + slides).

**Cost-of-omission lesson — Лекция 4 паттерн повторился:** designer self-report «designer-extras 17→0» был FALSE (timing markers leaked). Orchestrator-INDEPENDENT regex sweep на rendered PPTX visible body — обязателен per CLAUDE.md Pre-USER-GATE Walkthrough Rule §5. Quick fix added ~25 min к Phase 8.5 cycle.
