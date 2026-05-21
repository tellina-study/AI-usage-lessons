# Content — Лекция 10 production retrospective

**Дата:** 2026-05-21. **Issue:** #126 closed. **PR:** #136 merged.

## Артефакты произведены

### 3 финальных артефакта Лекции 10

| Артефакт | Версия | Объём | Path |
|---|---|---|---|
| `chapter.md` + `chapter-part2.md` + `chapter-part3.md` | v3.3 finalized | **~32 434 слов** / 3 файла / 536/366/480 строк | `library/lectures/lec-10/` |
| `rendered/lec-10.pptx` + 43 PNG snapshots + assets | v2 finalized | 5.17M PPTX, 43 слайда | `library/lectures/lec-10/rendered/` |
| `speech.md` | v2 finalized | ~5,940 narrative spoken / 879 строк / 7,765 raw | `library/lectures/lec-10/speech.md` |

### Промежуточные артефакты

- **Plan:** `notes/lecture-10-review/plan-v1.md` → `plan-v2.md` (APPROVE-CLEAN)
- **Research:** `notes/research/lecture-10/` × 4 файла (5618 + 6621 + 6319 + 3790 = 22,348 слов фактуры) + `00-summary.md`
- **Critic reports:** `notes/lecture-10-review/critique-of-*` × 13 файлов (plan-v1 methodology + reader; plan-v2 methodology narrow; chapter-v1 methodology + fact-checker + reader-text; chapter-v3 methodology + fact-checker narrow; slides-v1 presentation + student-sim + reader-rendered + consistency + fact-checker; speech-v1 methodology + fact-checker + consistency)
- **iteration-log.md** — Phase 6 + Phase 8 + Phase 11 render logs

### Manifest update

`catalog/manifests/lectures.yaml` lec-10: `status: planned` → `produced`, `repo_dir: null` → `lec-10`, `learning_outcomes: [LO1, LO2, LO5]` → `[LO1a, LO1b, LO2, LO5]` (Bloom-split применён в plan-v2), `issue: 126` link, `repo_title_note` с 3-artifact summary + 2 NEW ENFORCED rules.

## Quality assessment

### Strengths (3 пика методической честности)

1. **Keystone-axis «Лестница AI-проникновения L1→L5»** + closed-loop vs open-environment injection — reader-simulator (через 2 нед) verified sticky: «через 2 недели восстанавливается по памяти». Чёткая mnemonic + 5 уровней с growing controllability/ROI/predictability + сжимающейся биологической непредсказуемостью. **Это сильнее OODA-keystone Лекция 9** для отраслевой лекции (там был conceptual axis, здесь — taxonomic ladder с success+failure на каждом уровне).

2. **Cognitive Pilot vs ИТЭЛМА как «архитектурный выбор внутри AI domain»** (AP2a vs AP2b split):
   - **AP2a:** CV не выдерживает open-environment → используй другой класс AI (sensor-fusion на multi-GNSS)
   - **AP2b:** AI как класс не применим (термодинамика VF) → используй mechanical / direct measurement
   - **Это strongest pedagogical insight лекции:** студенты привыкли видеть «AI vs не-AI» dichotomy; явный split на «architecture choice within AI domain» vs «genuine не-AI» — concept-cracker после L7 (closed-loop medicine) + L9 (OODA dual-use).

3. **Plenty Compton hook + closing callback arc:**
   - **§ 0 Hook:** Plenty Compton split-frame ribbon-cutting May 2023 / закрытие Dec 2024 + «$940M потерь, valuation $1.9B → <$15M, 19 месяцев»
   - **§ 6 Closing payback:** «Plenty не закрылась из-за плохого AI. Plenty закрылась из-за термодинамики LED ≈100× sunlight»
   - **Hook → keystone → 5 анти-AI критериев → close** — narrative arc complete; reader-sim verified sticky через 2 нед.

### Cargill CMAX worked example (operational LO2 артефакт)

- $8M hedge × 45bp manual baseline → 8bp CMAX = 37bp diff × $8M = $29 600 ≈ $32k per trade
- На тысячи сделок annual — миллионы $ economy
- **«Когда не агент»** критерий явный: (a) сезонная feedback L1; (b) непрерывный risk-cascade end-to-end без статистики; (c) accountability dilution
- **Студент после лекции имеет formula + worked example + альтернатива** — это уровень LO2 (critical vendor-claim assessment) operational

### Pre-purchase verification checklist § 6.1a (operational LO5)

- 5 блоков × 2 пункта + scoring rubric (8-10 green = buy / 5-7 conditional / ≤4 reject)
- Applied к конкретным case studies в chapter (Monarch MK-V red flags / See & Spray high score / ChatGPT-as-advisor reject)
- **Студент может применить чек-лист к любому AgTech-вендор claim** — это LO5 (≥5 критериев «когда не AI») + LO2 (critical assessment) merged operational

### Failure-bucket strict-in distribution

| Артефакт | Strict-in % | Distributed по разделам? |
|---|---|---|
| chapter v3.3 | ~39% holistic | ✓ Part 1 33-35% / Part 2 47% Раздел 2 / 40% Раздел 3 / 36% Раздел 4 / Part 3 86% Раздел 5 + 33% Раздел 6 |
| slides v2 | ~44% (19/43 slides) | ✓ Р1 50% / Р2 53% / Р3 30% / Р4 40% / Р4-bis 100% by-design / Р5 33% |
| speech v2 | ~42% (independent count) | ✓ 17-75% per section; 11 failure blocks F1-F11 distributed |

**Все 3 артефакта PASS ENFORCED ≥30% holistic distributed.** Mission «учить когда применять AI, а когда нет» — соблюдено operationally.

## Что нужно follow-up

### Documented limitations (honest disclosure в финальном GATE C)

1. **s37 closing hero = FarmWise Titan stand-in для Carbon Robotics LaserWeeder G2** — Wikimedia gap + Tier 1 og:image failed for Carbon Robotics. Caption «представительное фото · полевые роботы L1-L2» honest disclaimer. **→ Possible future fix:** explicitly contact Carbon Robotics для high-res press image; archive locally.

2. **s09 foundation models density** — упрощена до ≤3 key claims, но не split на 2 slides (defensible per brief). Reader-simulator flag P0; presentation-critic flag P1. **→ если student-feedback после реальной лекции укажет density burnout, split в lec-10 v2.5.**

3. **Tier 1 og:image fetched 0/6** для vendor pages (TechCrunch / Deere / BASF / Carbon Robotics / Merck / Monarch — все JS-rendered/paywalled). Всё через Tier 2 Wikimedia. **→ improvements.md P3:** investigate playwright/chromium для JS-render og:image extraction.

4. **Лекция 11 production** уже завершена параллельно (#127 / PR #129) с тем же ≥30k правилом — конфликт в `tools/lecture-production/README.md` ловко resolved при PR #136 merge. **Pattern verified:** multi-lecture parallel production через worktree-isolation работает.

### Cross-references к другим лекциям

- L7 (медицина closed-loop) — explicit cross-link в chapter §7.2 + s04 glossary + speech §0
- L9 (OODA / satellite analytics) — cross-link в chapter §1 (foundation models satellite overlap)
- L11 (cyber-physical manufacturing) — foreshadow в s37 closing bridge + chapter §6.4
- L2 (foundation models / edge ML) + L3 (RAG / agentic) — prereq cross-refs

## Что НЕ войдёт (scope cuts explicitly documented в plan-v2)

- Deep RL theory для autonomous tractors (L2/L3 prereq)
- Foundation model architecture details (Лекция 3 покрытие)
- AlphaFold + CRISPR-GPT (биотех — отдельная лекция)
- LAWS-adjacent применения дронов (Лекция 9 покрытие)
- Полная теория carbon credits markets (1 блок Verra phantom + Indigo clarifier достаточно)
- MES / ZIIoT / Жировой комбинат Русагро (слишком отраслево-узко)
- Гидропоника / аквапоника specific agronomy

## RAG index update

**НЕ обновлён в этой сессии.** lec-10 не ingested в local RAG. **→ improvements.md P2:** ingest lec-10 chapter в `mcp-local-rag` для future cross-lecture queries.

## Summary

3 артефакта finalized + manifest produced + 2 NEW ENFORCED rules в инфраструктуре. Mission «учить когда применять AI, а когда нет» соблюдена через 39/44/42% holistic strict-in distribution. Strongest pedagogical insights — keystone лестница + AP2a/AP2b split + Plenty Compton arc + Cargill CMAX worked example + § 6.1a pre-purchase checklist.

Documented limitations honest (s37 proxy hero, s09 density partial fix, Tier 1 og:image gap). Cross-lecture references consistent. Manifest + ontology link через issue #126 + PR #136.
