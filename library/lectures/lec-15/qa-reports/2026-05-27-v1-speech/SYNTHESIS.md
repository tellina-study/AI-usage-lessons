# Phase 10 Speech v1 Critique Synthesis

**Date:** 2026-05-27.
**Combined Verdict:** **REVISE** (consistency + fact-checker drive; methodology APPROVE-WITH-POLISH).
**Total P0:** 4. **Total P1:** ~13 (deduplicated). **Total P2:** ~16.

---

## Verdicts по критикам

| Critic | Verdict | P0 | P1 | P2 |
|---|---|---|---|---|
| methodology-critic | APPROVE-WITH-POLISH | 0 | 4 | 7 |
| fact-checker | REVISE | 2 | 4 | 3 |
| consistency-checker | REVISE | 2 | 5 | 9 |
| **Combined** | **REVISE** | **4** | **13** | **~16** |

---

## P0 issues — BLOCKING до USER GATE C

### P0-1 (consistency) — Galactica date cascade — chapter+speech+slide.md+deck.yaml stale
- **Current canonical (correct, per MIT TR Nov 18 2022):** Galactica launched **15 ноября 2022**, retracted **17 ноября 2022** (3 days)
- **PPTX rendered:** «15 ноября 2022» ✓ (Phase 8 fixed)
- **STALE WRONG:** chapter v2.3 (§0.2) + speech v1 [s01] + slide.md (s01-hook-alphafold-galactica.md L44) + deck.yaml L49 — все say «17 ноября 2022» как launch date
- **Cascade fix:** chapter (4 files) + speech.md + slides/s01-*.md + deck.yaml

### P0-2 (consistency) — s37 PPTX fabricated RU institutional narrative
- **Rendered PPTX s37 visible body** contains products/orgs NOT in chapter or speech:
  - «AIRI: Сбер + НТИ» (false — AIRI is independent)
  - «Sber AI Lab: GigaChat / GigaTune / GigaChat 3 / ML в финансах и медицине» (NOT in chapter — chapter says climate + energy)
  - «Yandex Research: YandexGPT / Яндекс Переводчик / YandexGPT 5» (NOT in chapter — chapter says YaLM-100B + RuGPT family)
- **s37 slide.md source IS correct** — divergence introduced in build script
- **Re-render required:** regenerate s37 from canonical slide.md

### P0-3 (fact) — MICrONS neuron count 3-way drift
- **Chapter §3.3 (canonical?):** «84 000 нейронов»
- **Speech [s22]:** «сто двадцать тысяч анатомически реконструированных нейронов»
- **Nature April 2025 primary (MICrONS Consortium):** «>200 000 cells / 0.5 billion synapses»
- **Decision needed:** verify Nature primary, sync 3 artifacts
- **Recommendation:** «более 200 000 нейронов» per Nature 640 paper — update chapter + speech + slides

### P0-4 (fact) — Palgrave-Schoop affiliations (inherited chapter error)
- **Chapter + speech:** «команда из Ливерпульского университета»
- **Actual (Chemistry World 2024 + ChemRxiv 10.26434/chemrxiv-2024-5p9j4):** **Palgrave = UCL** (University College London) + **Schoop = Princeton**
- **Fix:** chapter-part2 §2.5 line 147 + speech [s17] + slide.md s17 + chapter-part4 refs

---

## P1 issues — should fix

### Methodology speech P1 (4):
- **P1-M1** Anglicism leaks (5 spots): «Sto» typo L170 (must be «Сто»), «upfront / milestone-платежей / milestone'ов» L214, «Open-weights» L308, «GNoME-inference» L612
- **P1-M2** WE-1 (s07) 151 words vs 200-280 target — expand ~50 words to maintain WE structural consistency
- **P1-M3** s08 missing Sakana arxiv 2504.08066 Yamada citation (cascade from chapter v2.3)
- **P1-M4** «Длительность: 75 минут» line 27 — metadata leak в narrative body, move to frontmatter

### Fact P1 (4):
- **P1-F1** FrontierMath 52.4% freshness alert: Epoch AI May 12 2026 announced AI-assisted review flagged ~1/3 problems с fatal errors. Augment [VFY-day-of] note
- **P1-F2** NotebookLM 17M MAU — quarterly cadence, add to preflight verify list
- **P1-F3** Elicit 138M / 4× — quarterly cadence
- **P1-F4** WE-2 timing «3 часа» speech vs «4 часа» chapter — minor cascade drift

### Consistency P1 (5):
- **P1-C1** MICrONS 3-way drift (cross-link P0-3)
- **P1-C2** s39 hero spec/impl/speech mismatch: speech says «скриншот alphafold.ebi.ac.uk», PPTX shows ribbon composite. Decision: retry screenshot OR honest spec+speech update
- **P1-C3** Speech failure-share — consistency claims marginal ~32%, methodology claims 81%, fact-checker independent ~40%. Conflicting measurement — sample independently
- **P1-C4** Phase 7 carryover: s39 hero, s03 keystone bilingual labels verify
- **P1-C5** Failure-bucket retag deck.yaml: formal 25.6% (10/39) → 38% holistic (count mixed-but-failure-dominant slides s01/s18/s19/s37/s38)

---

## P2 issues — nice to fix

- **P2-M5** BO/GP no inline EN abbreviation gloss s11 (vs IDP gloss on s24 — consistency)
- **P2-M6** YaLM-100B gloss in speech [s37]
- **P2-M7** s39 closing strengthening
- **P2-C cluster** Russification leaks:
  - «cherry-pick» EN-only in slides (chapter uses bilingual)
  - «foundation модели» mixed in s18 PPTX + speech [s37] (chapter «фундаментальные модели»)
  - «академической интегриты» anglicism in s26 PPTX divider
  - «open-source» EN-only in s14/s15
- **P2-F cluster** Minor citation polish

---

## Path to USER GATE C

1. **Phase 11 — single batched revision agent** (~45-60 min estimated):
   - **Chapter mini-fix** (cascade Galactica date 17→15, Palgrave affiliations Ливерпульский→UCL+Princeton, MICrONS canonical decision)
   - **Speech revision v2** (apply all 4 P0 cascade + 13 P1 + selected P2)
   - **Slides re-render s01 + s37** from canonical sources (Galactica date + RU institutional narrative fix)
   - **Sync к main repo** все updates
2. **Phase 11.5 — Pre-USER-GATE C walkthrough** (orchestrator-independent):
   - Cross-artifact consistency grep
   - 3-way cascade integrity spot-check 8-10 anchors
   - Designer-extras / Russification deep scan
   - Cornerstones consistency
   - Pre-flight actionability + 0 orphan refs
3. **USER GATE C** (final approval, 3 artifacts)

**Storage:** `/tmp/lec-15-wt/library/lectures/lec-15/qa-reports/2026-05-27-v1-speech/SYNTHESIS.md`

**Estimated Phase 11:** ~45-60 min (cascade fixes + speech revision + slides re-render 2 slides + sync).
