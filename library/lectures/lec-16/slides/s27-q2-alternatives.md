---
id: s27
type: alternatives_list
duration_min: 2
assertion: "Альтернатива Q2: hand-held OGI (FLIR GFx320, Opgal EyeCGas) + portable Picarro / LI-COR. Когда AI не нужен — OGMP Level 5 (прямое измерение) + custody transfer metering."
learning_goal: "LO3 alternative Q2 + 2 criteria"
failure_bucket: strict_in
chapter_ref:
  parts: [chapter-part3.md]
  sections: ["§3.7 OGI + Picarro alternative"]
visual:
  type: image
  description: "Teledyne FLIR GFx320 product photo + Picarro G2210-i portable analyzer photo"
  source_url: "https://www.flir.com/products/gfx320/"
  acquisition_tier: 1
visible_numbers: ["EU LDAR 4×/год", "$5-15M/год LDAR на cluster", "20-40% LDAR cost reduction с AI hybrid"]
russification_check: "FLIR, GFx320, Opgal, EyeCGas, Rebellion Photonics, Honeywell, Picarro, G2210-i, LI-COR, LI-7810, EPA Method 21, EU LDAR — brand list; «cavity ring-down spectroscopy» → «спектроскопия с резонатором» inline."
speaker_notes_target_words: 220
---

# Альтернатива Q2: hand-held OGI + Picarro/LI-COR. AI не для compliance Level 5.

## Visible content

Заголовок: «Альтернатива Q2: ground OGI + portable analyzers» (28pt deep ocean).
Sub: «Hybrid Bridger Photonics + ground OGI = working model. AI снижает LDAR cost на 20-40% для well-equipped operator.» (16pt italic)

**Слева — Ocean rounded box «Hand-held OGI cameras»:**

- **Teledyne FLIR GFx320** — industry standard. IR-фильтр + цифровая запись для аудита. EPA Method 21, EU LDAR.
- **Opgal EyeCGas** — конкурент; добавляет **QOGI** (quantitative OGI) capability.
- **Rebellion Photonics (Honeywell)** — fixed hyperspectral 24/7.

**Справа — Ocean rounded box «Portable laser analyzers»:**

- **Picarro G2210-i / G2401** — спектроскопия с резонатором; **лабораторная точность 0,5 ppb** на месте измерения.
- **LI-COR LI-7810** — конкурент Picarro.
- Используется как **ground truth для калибровки** OGI + aerial measurements.

**Bottom bar (gold tint) — Когда AI не нужен в Q2:**

1. **OGMP 2.0 Level 5 verification** — прямое измерение всех источников. ML estimate не приемлем.
2. **Custody transfer metering** — regulator требует mass flow meter класса 0,2% точности.

**Структурный взгляд LDAR:** $5-15M/год на cluster для крупного European operator. **AI hybrid снижает на 20-40%** через aerial campaigns 2×/год + targeted ground OGI на flagged sites.

## Speaker notes

Это критический раздел в Q2. Альтернатива AI MRV — это ground-based прямое измерение campaigns.

ручные OGI-камеры. Teledyne FLIR GFx320 — ключевой отрасль standard. Видит углеводородные газы как «облако» через IR-фильтр; цифровая запись для аудита. Используется EPA Method 21, EU LDAR (выявление и устранение утечек) programmes. Opgal EyeCGas — конкурент FLIR; добавляет quantitative OGI кап.ability — не только видит утечку, но и приближённо измеряет её расход. Rebellion Photonics, теперь Honeywell — fixed hyperspectral imaging system, постоянный мониторинг.

переносной laser analyzers. Picarro G2210-i — спектроскопия затухания в полости, спектроскопия с резонатором; измеряет концентрации метана с лабораторной точностью на месте измерения. Часто используется как эталон для калибровки OGI и aerial measurements. LI-COR LI-7810 — конкурент Picarro.

Когда AI не нужен в Q2 — два критерия. Первый — OGMP 2.0 Level 5 верификация. Level 5 требует прямого измерения всех источников эмиссии на operational asset. ML estimate не приемлем как primary methodology. Поэтому Level 5 operators обязаны иметь Picarro или LI-COR плюс OGI campaigns; AI здесь — дополнение для prioritization, не замена.

Второй критерий — custody transfer metering. Регуляторно требуется mass flow meter класса точности ноль и две десятых процента.

Структурный взгляд на LDAR (выявление и устранение утечек) programmes. EU LDAR (выявление и устранение утечек) требует операторов проводить survey четыре раза в год плюс ремонт утечек в течение пяти-пятнадцати рабочих дней. Расходы для крупного European operator — порядка пяти-пятнадцати миллионов долларов в год на один production cluster. AI MRV может снизить эти расходы на двадцать-сорок процентов через aerial campaigns раз в два месяца плюс targeted ground OGI на flagged sites. Это substantial value, который не эффектен в маркетинговой картине, но practical для соответствие budgets.
