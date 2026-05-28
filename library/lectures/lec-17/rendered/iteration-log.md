# Лекция 17 — visual render iteration log (Phase 6)

Issue #145 · capstone · 40 slides · 16:9 (13.333×7.5") · Ocean palette v3.

Pipeline (reproducible):
```
python3 render_scatter.py     # 7 signature scatter PNGs → assets/charts/
python3 build_lec17.py        # lec-17.pptx (notes = file refs)
python3 inject_notes.py       # FULL speaker notes from slides/*.md (## speaker_notes)
libreoffice --headless --convert-to pdf lec-17.pptx
pdftoppm -r 110 -png lec-17.pdf snapshots/sNN
```

Render approach: python-pptx primitives (per MCP limitations #54-3/#71-1 — full
rebuild each iteration, no in-place mutate). Signature scatter via literal SVG +
rsvg-convert (MCP limitation #69-svg-fallback — exact palette + reproducible;
matplotlib not installed). Font: Arial → Liberation Sans (Cyrillic-capable fallback;
Inter/JetBrains not installed).

---

## Master scatter coordinate system (shared asset — 7 slides)

`scatter_coords.py` = ONE source of truth for all scatter slides. Same plane,
progressive layer reveal. Rendered by `render_scatter.py` into `assets/charts/`.

- **Convention:** x = Применимость ИИ (0 non-AI → 1 full AI); y = Автономия (0 L0 → 1 L5).
- **Module colors:** M1 (L1-L8) `#065A82` / M2 (L9-L12) `#028090` / M3 (L13-L17) `#F0AB00`.
- **Bimodal:** L10 agro (See & Spray ↑ / Monarch ↓), L13 logistics (склад ↑ / робот-такси / чёрный лебедь ≈L0), L15 (AlphaFold ↑ / Galactica ↓).
- **Point kinds:** ok = filled, fail = hollow ring + dot, near0 = dashed ring.

Consistency verified: s01 / s22 / s23 / s24 / s38 all use identical coords from the
same module (only layers/zones/highlights/labels differ). s03 + s28 = same axes/
quadrants без точек/с warning-зоной. **No coordinate drift between slides.**

| slide | scatter PNG | what shown |
|---|---|---|
| s01 hero | s01-hero-scatter.png | 18 pts, gradient bg, no labels, title overlay (clean) |
| s03 keystone | s03-keystone-quadrants.png | empty axes + 4 labeled quadrants, LR gold warning |
| s22 batch1 | s22-batch1.png | 4 starter pts (L4/L5/L7/L9) |
| s23 batch2 | s23-batch2.png | 8 pts, L10 bimodal gold-ringed |
| s24 batch3 | s24-batch3-full.png | ~18 pts, L13 trio gold-ringed |
| s25/s26/s27 clusters | s24-batch3-full.png (reuse) | full map + zone-label text + members |
| s28 empty quad | s28-empty-quadrants.png | LR warning zone gold-dashed + shift arrow |
| s38 poster | s38-master-poster.png | A1 1600×1000, 4 colored zones + all labels |

---

## Hero acquisition (§5.7 6-tier)

### s01 hero — clean 2D scatter (orchestrator C4: single iconic, not composite)
Generated scatter (render_scatter.py), gradient Ocean bg, module-colored points,
title overlay «Шестнадцать отраслей — шестнадцать точек одной карты». ≥40% area.
Foreshadows keystone. NOT a stylized card — real rendered data-viz.

### s40 closing hero — REAL image (6-tier acquisition)
- **Tier 1 (og:image):** не пробовался (Tier 2 succeeded first).
- **Tier 2 (Wikimedia Commons):** SUCCESS. Query «Control room operator» →
  `File:Telescope operator at work in VLT control room (img-4458).jpg` (ESO, **CC BY 4.0**).
  Real photo of an engineer/operator looking intently at dashboards in a control room —
  authentic fit for «инженер за данными / перед картой».
  - URL: `https://upload.wikimedia.org/.../1280px-Telescope_operator_at_work_in_VLT_control_room_%28img-4458%29.jpg`
  - Stored: `assets/screenshots/s40-engineer-map.png` + `.url`
  - Embedded full-width hero band (≥40% area) via crop-fill (no distortion), gold overlay
    «Знать ИИ — значит знать его границы» + 3 positioning cards. Attribution visible:
    «ESO · CC BY 4.0 · оператор в зале управления VLT».
- Tiers 3-6 not needed (Tier 2 delivered). **NO mock fallback used.**

---

## Per-slide iterations (≥3 each, summary)

Visual loop: GENERATE → CONVERT (libreoffice+pdftoppm) → INSPECT (Claude vision) →
FIX → re-render. All slides ≥3 effective passes (full-deck rebuilds + targeted fixes).

### Deck-wide iterations
- **iter 1:** full 40-slide build, first render. Inspected cover/map/keystone/criteria/
  ladder/scatter/cheatsheets/Q&A/closing.
- **iter 2 (fixes found):**
  - scatter module colors rendered dark → SVG fill missing `#` prefix → FIXED (now M1 blue / M2 teal / M3 gold distinct).
  - scatter label overlap with gold rings (склад Symbotic) → increased label offset for ringed points.
  - s24 annotation column: 5th card (L16) overflowed footer → adaptive spacing FIXED (5 cards fit).
  - s16 L1 flow: Project Maven (5th example) hidden behind criteria box → restructured to single row of 5 + full-width criteria box.
  - s40 closing: silhouette-shape mock → replaced with REAL ESO control-room photo (Tier 2).
- **iter 3 (Russification + polish):**
  - deep latin scan → russified «production»→«пром. эксплуатация», «AI fit»→«применимость ИИ», «vs»→«против», «bimodal»→«двойственная», «deep learning»→«глубокое обучение», «inference»→«вывод (inference)», «autonomy»→«автономия», «pipeline»→«конвейер», «closed-loop»→«закрытая петля», «open-environment»→«открытая среда», «foundation models»→«фундаментальные модели», «malware»→«вредонос», «high-performers»→«лидеры», «customer service»→«поддержка клиентов», «L9 aero»→«L9 авиа», «L12 manuf»→«L12 произв.», «recap»→«опора».
  - removed «Strict-in ядро лекции» from s30 footer (internal methodology term, not student-facing).
  - s35 attribution clipping (right-aligned overflow) → moved to left footer.
- **iter 4 (final verify):** all snapshots re-inspected @ 110dpi + key slides @ 130dpi;
  notes word counts verified (38/40 in 150-320; 2 dividers intentionally shorter).

### Schema readability checklist (per schema slide)
- **s03 quadrant:** axis labels INSIDE + direction arrows; LR warning gold; PASS.
- **s14 layered ladder:** bottom-aligned ascending stair (NOT centered); L5 grey/top; component captions per step; ≤6 levels; PASS.
- **s15 matrix:** fill rate ~92% (one «—» где нет соответствия); single-line headers; icons-by-column not used (3-scale columns instead, labeled); PASS.
- **s22/s23/s24/s28 quadrant scatter:** points contained; module legend present; failure markers distinct; axis labeled; PASS.
- **s37 cheatsheet matrix (12×4):** all 12 rows filled; gold row 12; readable @ 110dpi; PASS.

### 5-second test (sample)
- s01: «карта 16 отраслей = одна плоскость» → PASS (matches assertion).
- s09: «CrowdStrike radius на порядки больше всех» → PASS (gold row jumps out).
- s24: «логистика = 3 точки одной отрасли» → PASS (L13 trio gold-ringed).
- s33: «3 мега-паттерна провалов» → PASS (3 equal cards + procedure).
- s40: «инженер за данными — знать границы» → PASS (real photo + gold phrase).

---

## Verification results

- **Slides:** 40/40 built. PPTX 810 KB, PDF 1.79 MB.
- **Media coverage:** 34/40 slides with real visual (charts/scatter/tables/card-grids/
  hero photo) = 85%. Text-light: only s04/s39 (by design — re-ask + Q&A) and the 5
  section dividers (decorative number) + which still carry roadmap-bar/gold-tag visuals.
- **Speaker notes:** 40/40 injected (## speaker_notes lowercase), 134-238 words,
  connected student text. No layout descriptions / no «Лектору».
- **Scaffold/timing/methodology scan (visible + notes):** 0 lecture-timing on dividers/
  cover/Q&A; 0 methodology comments; 0 LO codes / §refs in visible.
  - NOTE: «strict-in» appears 1× in s29 speaker_notes (source slides/s29-*.md authored
    in Phase 5). Source-content issue (not a render artifact) — flagged for Phase 7 QA
    (I do not edit source markdown). «18 месяцев»/«20 минут» in s12 visible = vendor ROI
    claim + diagnostic-procedure duration (content, not lecture pacing) — kept.
- **Deep latin scan (visible PPTX):** non-allowlisted unique = 2 («See»+«Spray» = the
  See & Spray brand, keep-listed). All other Latin = brand/case names + glossed acronyms
  + course-canonical level names (advisory/supervised/conditional/high/full).
- **Baseline coverage:** measurable claims carry inline denominators — CrowdStrike
  «8,5 млн устройств / $5+ млрд (Parametrix Fortune 500)»; See & Spray «5 млн из ≈900 млн
  акров США = 0,55% / ≈1→0,5 фунт/акр»; Zillow «$304 млн / ≈2 000 из ~8 000»; Monarch
  «38% ≈53 из ~140»; Plenty «$940 млн+ с 2014 → Chapter 11»; Copilot «20+ млн из ≈28 млн»;
  MIT 95% vs McKinsey 5,5% explicitly «РАЗНЫЕ измерения».

---

## Phase 8b — P0 quadrant geometry CANON + 7 P1 (2026-05-28)

Source of truth: corrected chapter v3 (§0.3 + §3.5-§3.7 + §5). 2D plane:
X = применимость ИИ [left=low, right=high]; Y = автономия [bottom=L0, top=L5].

### P0 — quadrant geometry was SWAPPED, now CANON
Prior render had WARNING in lower-right + CAPPED in upper-left (inverted). Fixed to:
- **upper-right** = closed-loop success (green) — software/fraud/warehouse/AlphaFold
- **upper-left** = WARNING low-fit×high-autonomy (gold dashed) — Monarch/robotaxi/Galactica/Cruise/CrowdStrike/F-35 ALIS
- **lower-right** = CAPPED high-fit×low-autonomy regulatory, FILLED (blue) — медицина Aidoc/аэро/cyber Sense
- **lower-left** = classical/non-AI (grey) — OR/MPC/EOQ/чёрный лебедь

Changes:
- `scatter_coords.py`: QUADRANTS dict UL↔LR labels swapped; failure points re-plotted
  to upper-left (L10_monarch 0.27/0.74, L13_taxi 0.34/0.70, L15_galac 0.30/0.66);
  L13_swan tightened to lower-left (0.20/0.10); L7_med/L14_cyber stay lower-right (capped).
  M1 module color 065A82→21295C (navy) for distinguishability.
- `render_scatter.py`: tint zones re-mapped (UL=gold warning, LR=blue capped);
  quadrant-label gold key LR→UL; `highlight_lr`→`highlight_ul` for s28; added
  `highlight_ur`/`highlight_lr` per-cluster variants; shift arrows relocated to UL;
  legend M1 navy. New PNGs: s25-cluster-ur / s26-cluster-ul / s27-cluster-lr.
- `cheatsheets/render_master_poster.py`: ZONE_LABELS UL↔LR swapped; tints re-mapped;
  warning dashed border UL; legend navy + boxed in lower-left.
- build_lec17.py text: s03 callout / s22 assertion+L7+footer / s23 Monarch / s24
  robotaxi / s25/s26/s27 zone labels / s28 title+body — all corner refs → CANON.
- Source markdown speaker_notes + visible (s03/s22/s23/s24/s26/s27/s28/s38) — all
  «нижний правый=warning» / «верхний левый=capped» refs flipped to CANON.

Visual verify (PNG inspect): s03 / s28 / s38 / s24 / cheat-sheet#4 PDF — WARNING gold
in upper-left (Monarch/robotaxi/Galactica), CAPPED blue lower-right (медицина/аэро/cyber),
points match zone semantics, no closed-loop point inside warning highlight.

### 7 P1 fixes
1. **M1/M2/M3 colors distinguishable** — M1 navy #21295C / M2 teal #028090 / M3 gold
   #F0AB00. Legend updated on all scatter slides + poster.
2. **s25/s26/s27 per-cluster highlight** — dedicated PNGs with corner-specific zone tint
   + stroke (s25 UR teal / s26 UL gold / s27 LR blue) replacing flat master reuse.
3. **s29 strict-in leak** — stripped from slides/s29 speaker_notes + media section;
   re-injected. PPTX scan: «strict-in» = 0.
4. **s34 empty placeholders** — A4/A4/A4/A1 boxes → real mini-renders of 4 cheat-sheets
   (downscaled snapshots c1-c4 @ 520px) + A4/A1 format chip. PPTX 3.2MB→1.56MB.
5. **s01 roadmap competes with hero** — roadmap_bar removed from s01; hero scatter clean.
6. **s14 gold badge overflow** — «частый в проде» chip width 1.5 + reserved text gutter
   on gold row so desc «кто решает» no longer truncated.
7. **s10/s16 advisory latin** — glossed «advisory (советующий)» at first visible use on
   s10 headline + s16 headline (consistent с s14 «Advisory (советует)»).

### Verification
- Slides: 40/40 built. PPTX 1.56 MB, PDF 2.11 MB. Notes 40/40 injected.
- Scaffold/timing/methodology scan (visible+notes): strict-in / методическ / Лектору /
  metadata-leak / LO / §refs = 0. («20 минут» = procedure duration; «Преподаватель» =
  exam-scenario actor — both content, kept.)
- Deep latin scan: 251 unique = brand/case names + acronyms (ODD/ALIS/EPANET/RAG/OODA/
  SBOM/MITRE/FDA) + canonical level names (advisory/supervised/conditional/high/full) +
  mode names — all keep-list; P1 #7 added RU gloss to advisory.
- Master scatter coords IDENTICAL between deck s38 and cheat-sheet #4 (shared
  scatter_coords.py). Cheat-sheet PDFs rebuilt: c4 + cheatsheets-all reflect CANON.
- Snapshots: 40/40 re-generated @ 96dpi.
- DISMISSED student-simulator «14 broken layout» — bbox confirmed full-frame content.

---

## Phase 8c-2 (FINAL render — 40→37 restructure) — issue #145

**REBUILD under new 37-slide deck.yaml v2.** Old build_lec17.py hardcoded
s01..s40 in OLD order; fully rewritten under new sequence:
s01 title cover / s02 keystone / s03 Р1-divider / s04-s09 Р1 / s10 Р2-divider /
s11-s17 Р2 / s18 Р3-divider / s19 lecture-map-16 / s20-s26 Р3 / s27 Р4-divider /
s28-s31 Р4 / s32 cheatsheets-overview / s33-s36 cheatsheet-previews / s37 QA.

### Scatter (render_scatter.py + scatter_coords.py)
- Chart names remapped to v2 positions: s02-keystone / s20-batch1 / s21-batch2 /
  s22-batch3-full / s23-cluster-ur / s24-cluster-ul / s25-cluster-lr /
  s26-empty-quadrants / s36-master-poster.
- **L-codes stripped from point labels** (was "L4 разработка ПО" → "разработка ПО").
- **Legend industry-named** (was "Модуль 1 (L1-L8)" → "Модуль 1 — основы +
  ранние отрасли"), white backdrop for readability.
- Geometry verified: WARNING upper-left (gold dashed), CAPPED lower-right (blue),
  closed-loop upper-right (teal), classical lower-left (grey). Logistics trio +
  bimodal agro/science failures in UL.

### 13 case images embedded (real, with RU attribution labels)
see-and-spray→s05 · crowdstrike→s06 · ups-orion→s08 · aidoc→s13 · waymo→s14 ·
symbotic→s15 · klarna→s16 · alphafold→s23 · monarch→s24 · epic-sepsis→s25 ·
uber-tempe→s28 · arup-deepfake→s29 · getty-stability→s30. Each ≥25% slide area,
attribution caption (source + license from MANIFEST) in corner. s16 reworked to
2×3 card grid + klarna photo column; s28/s29/s30 reworked to 2×2 grid + photo column.

### Hero slides
- s01: CLEAN title (title dominant left, hero scatter ~40% right, capstone chip,
  gold-hook in motif box). Owner "потерял титульный" → now explicitly a title.
- s37: SIMPLE QA farewell ("Знать ИИ — значит знать его границы" + "Вопросы?" +
  "До новых встреч" + 3 anchors). NO photo-hero, NO career cards, subtle Ocean bg.

### Layout overflow fix (owner #6 — main complaint)
Visual-loop ≥3 iter on flagged slides. Fixes found + applied:
- failure-grid card 4 (s28): alt text wrapped 2 lines, overflowed strip →
  shortened to "человек-на-петле с алертом." + taller multiline strip.
- photo attributions overflowed 1-line bar → img_attribution() now 2-line (0.34"),
  attributions shortened (case-detail front-loaded).
- All blocks manual-sized (autofit off). Verified per-slide: text within shapes,
  no clipping. Checked at 150 DPI: s01/s02/s05/s06/s07/s08/s09/s11/s12/s13/s14/
  s15/s16/s17/s19/s20/s23/s24/s25/s26/s28/s29/s30/s31/s32/s33/s34/s35/s36/s37.

### ENFORCED checks (final)
- self-grep timing/methodology/scaffold/refs (visible + notes): 0 hits.
- L6-L17 lecture codes: 0 (autonomy L0-L5 verified as mode names, kept).
- "GOLD:" designer-token leak in s28/s29/s30 footers → russified ("Главное" /
  "Самая яркая цифра" / "Главная статистика курса").
- deep_latin_scan: unique−whitelist = ∅ for narrative (only brand names +
  established acronyms + L0-L5 autonomy mode names advisory/supervised/
  conditional/high/full/domain remain).
- inject_notes: 37/37 injected, no empty, no unexpected-short (SHORT_OK={3,10,18,27,37}).
- snapshots regenerated s01-s37; old s38-s40 deleted.

### Chapter inline markers renumber (P1, done)
47 [for-slide-sNN] markers remapped from OLD 40-slide → NEW 37-slide positions
across chapter.md + part2/3/3b/4. No s38-40 left. s28-30 (12-failures) have no
inline anchors (prose-described in §4.1-4.12 — matches original). chapter_ref
§X.Y intact.

---

## Phase 11b — cross-artifact slide polish (Phase 10 findings)

Re-render after 3 cross-artifact fixes (consistency + reader-speech reports
2026-05-28-speech-v1). Pipeline re-run: render_scatter → build_lec17 →
inject_notes → pdf → 37 sNN snapshots.

### Fix 1 — D3 Monarch stale quadrant label (consistency P1, closest-to-P0)
After v3 geometry fix, Monarch canon coords = (0.27, 0.74) = upper-left WARNING
(low fit + high autonomy), plotted as "fail" hollow marker in gold warning zone.
But s21 caption + builder still said "нижний правый" / "↓" (STALE).
- s21 md `## visible` line 36: "Monarch ↓ нижний правый" → "Monarch ↖ верхний
  левый, зона предупреждения, провал".
- build_lec17.py s21 caption: "Monarch ↓ с пометкой провала" → "Monarch ↖
  верх-лево (зона предупреждения), провал".
- s21 md `## media` design-note + deck.yaml s21 media_kind synced.
- VERIFIED on s21.png: chart marker (upper-left, gold ring) + right caption now
  MATCH. Cross-checked s24.png open-env cluster (also upper-left) — consistent.

### Fix 2 — s02 keystone slang "капнута" (reader cross-artifact)
s02 LR quadrant label "AI работает, автономия капнута" (slang) → "AI работает,
автономия ограничена (регулятором)" — matches speech "прикручена/ограничена
регулятором".
- scatter_coords.py QUADRANTS["LR"] label edited (only s02 uses
  show_quadrant_labels=True → only s02 chart affected).
- s02 md `## visible` line 39 synced.
- VERIFIED on s02.png. NOTE: "капнут" survives on s20/s25/s36 as the deck's
  established cluster terminology — OUT of Fix 2 scope (s02 keystone only).
  Flagged for pre-GATE.

### Fix 3 — s31/s37 Latin (HITL / STOP) for RU audience (reader cross-artifact)
- s31 assertion "плохой HITL" → "плохой человек в петле" (matches s31 cards which
  already said "Человек в петле спроектирован плохо"). md + builder + deck.yaml.
- s37 recap "✗ → STOP" → "✗ → СТОП". md + builder.
- Extended (brief authorized: "Russify STOP where visible call-to-action"):
  s04 callout "✗ → STOP" → "✗ → СТОП"; s33 title + footer STOP → СТОП + footer
  HITL → "человека в петле" (prose footer). md + builder + deck.yaml synced.
- VERIFIED: latin STOP = 0 in visible; СТОП present s04/s33×2/s37; HITL = 0 in
  s31/s37. Remaining HITL (4×) only on cheatsheets s33-cell/s34-footer/s35×2 —
  compact glossed reference acronyms (cheatsheet allowlist + chapter gloss
  "человек в петле", parallel to HOOL/ODD). Flagged for pre-GATE.

### Self-grep results (orchestrator-independent)
- Scaffold/L-codes/§/→sNN/methodology in visible: 1 hit = s09 "семь критериев за
  20 минут" — CONTENT claim (exercise speed, like "за 18 месяцев"), NOT a slide
  timing-marker; pre-existing, out of modify-list. Flagged.
- Scaffold/timing/methodology in speaker_notes: 0.
- Latin STOP in visible: 0. HITL in visible: 4 (cheatsheets, glossed).
- deep_latin_scan visible: 167 unique / 381 occ — all brands (Waymo/AlphaFold/
  Watson/Symbotic/Getty/Arup/Tesla/IBM/MIT/EPANET/Zillow/Klarna/Cruise/etc) +
  acronyms (ODD/HOOL/SAE/MPC/RCT/BSOD) + autonomy-ladder L1-L5 names
  (advisory/Supervised/Conditional/High/Full) + CC BY-SA attribution. No new
  narrative latin introduced; net latin REDUCED by fixes.

### Artifacts
- lec-17.pptx 6.3M / 37 slides / 37 notes injected (0 warnings).
- lec-17.pdf 3.3M.
- 37 sNN.png snapshots @ 110dpi re-generated.
- Geometry canon (scatter_coords §26-30) intact: WARNING=upper-left,
  CAPPED=lower-right FILLED.
