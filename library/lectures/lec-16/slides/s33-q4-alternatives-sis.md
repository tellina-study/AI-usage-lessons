---
id: s33
type: alternatives_list
duration_min: 1
assertion: "Альтернатива Q4: classical APC (Honeywell Profit Controller, Emerson DeltaV) + SIS (SIL3/SIL4 по IEC 61511). ML не сертифицируется под SIL3/SIL4. 3oo2 voting + periodic proof tests."
learning_goal: "LO3 alternative Q4 + SIS deterministic"
failure_bucket: strict_in
chapter_ref:
  parts: [chapter-part3.md]
  sections: ["§4.6 Альтернатива: physics simulators + SIS"]
visual:
  type: diagram
  description: "3 уровня альтернатив (physics for CCS, APC for refinery, SIS for safety) + bottom callout «3oo2 voting + proof tests» + Deepwater Horizon as anchor"
  acquisition_tier: self_render
visible_numbers: ["SIL3 = 0,001-0,0001 PFD", "SIL4 = ещё ниже"]
russification_check: "Eclipse, INTERSECT, Honeywell Profit Controller, Emerson DeltaV, AspenTech aspenONE, Visage, Abaqus, Plaxis, CMG GEM — brand list; «приборная система безопасности (SIS)», «безопасность процесса (process safety)», «защита от единичного отказа (3oo2 voting)» — RU."
speaker_notes_target_words: 220
---

# Альтернатива Q4: physics + classical APC + SIS. ML не сертифицируется под SIL3/4.

## Visible content

Заголовок: «Альтернатива Q4: classical engineering + deterministic safety» (28pt deep ocean).
Sub: «3 категории. Для regulatory submissions — physics-traceable mandatory. AI не accept.» (16pt italic)

**3 Ocean rounded cards вертикально:**

**Card 1 — Physics simulators для CCS:**
- Eclipse + INTERSECT с CCS modules — reservoir-scale CO₂ migration.
- OpenFOAM — CFD around injection wells.
- Visage (SLB), Abaqus (Dassault), Plaxis — geomechanics для caprock stress.
- CMG GEM — compositional simulator для CO₂-impurities.

**Card 2 — Classical APC для refinery:**
- Honeywell Profit Controller — modelling APC standard.
- AspenTech aspenONE — APC integrated в process simulation.
- Emerson DeltaV PredictPro — embedded APC в DCS.
- **APC = model-based predictive control, детерминированное и certifiable.**

**Card 3 — SIS (Safety Instrumented Systems):**
- BOP, PRV, ESD logic + Fire & gas detection.
- IEC 61511 / ISA-84 → **SIL3 (0,001-0,0001 PFD) или SIL4** (gold).
- **ML не сертифицируется** — state space слишком большой для analytical PFD proof.
- Альтернатива: physics-based redundancy + 3oo2 voting + periodic proof tests + fail-safe.

**Bottom bar:**

«**3 критерия «AI не нужен» Q4:** (1) Safety-critical SIS; (2) Long-horizon >10-20 лет; (3) Plant-wide multi-physics coupling. **Cross-ref Deepwater Horizon §6.3** — alarm bypass = 11 deaths.»

## Speaker notes

Это критический раздел для LO3 в Q4. Альтернатива AI в long-horizon CCS, refinery, EGS — это classical physics-based engineering плюс deterministic safety systems.

Physics-based simulators для CCS. Eclipse и INTERSECT с CCS modules — reservoir-scale CO₂ migration. OpenFOAM — CFD around injection wells, multi-phase flow. Geomechanics packages — Visage от SLB, Abaqus от Dassault, Plaxis — для stress analysis в caprock. CMG GEM — compositional simulator для CO₂-impurities scenarios. Эти tools используются для regulatory submissions под EU CCS Directive 2009/31/EC. Регулятор требует physics-traceable modeling; AI surrogate не accept.

Classical APC для refinery. Honeywell Profit Controller — modelling APC standard для US refineries. AspenTech aspenONE — APC integrated в process simulation. Emerson DeltaV PredictPro — embedded APC в DCS. APC — это model-based predictive control, детерминированное и certifiable. ML controller для plant-wide refinery operation requires safety case, что ML не приведёт к exceedance процессных пределов. Safety case для ML структурно сложнее, чем для APC.

SIS — Safety Instrumented Systems. Это deterministic safety logic, сертифицированная под IEC 61511 / ISA-84 на уровень SIL3 или SIL4. Применения: blowout preventer, pressure relief valve, emergency shutdown logic, fire and gas detection.

ML не сертифицируется под IEC 61511. Probability of failure on demand для ML не доказывается аналитически так же, как для дискретной логики; в дискретной логике мы перечисляем все возможные states; для ML это невозможно — state space слишком большой. Альтернатива — physics-based redundancy плюс 3oo2 voting — три датчика, действие при согласии двух — плюс периодические proof tests, плюс fail-safe design.

Три критерия «AI не нужен» в Q4. Safety-critical SIS. Long-horizon prediction beyond десяти-двадцати лет. Plant-wide multi-physics coupling.

Deepwater Horizon 2010 — анкор Q4 SIS-альтернатив. Альтернативы AI без strong safety culture = катастрофа. К нему вернёмся в s38.
