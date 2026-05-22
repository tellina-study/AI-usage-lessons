---
critique_of: library/lectures/lec-12/speech.md (v1)
critic: methodology-critic
verdict: APPROVE-WITH-POLISH
created: 2026-05-22
issue: 133
worktree: /tmp/lec-12-wt
branch: issue-133-lec-12
artifact_length: 6126 words (5083 narrative body)
duration_target: 75 min (~73 active + 2 buffer)
---

# Methodology Critic Report — speech.md v1 — 2026-05-22

## Summary

Лекция 12 speech v1 = solid conversational rendition оси A0→A3 + twin-as-bridge, technically aligned со chapter v3 + slides v3, plan v2 carry-forward executed faithfully. Failure-share strict-in **40.9% words / 42.3% minutes** (target 44%, hard floor 30%) — meets ENFORCED mandate. Locked numbers PASS (sample 10/10). Anonymization PASS (0 named institutions). Inclusive markers «мы с вами» = 11 (target ≥10). Lec-N pattern (cross-refs to lec-11 §3.2 angle, lec-07 FDA prerequisite, lec-13 canonical bridge phrasing) — все present.

**Главные методические сильные стороны:**
- Keystone-axis (s04) предъявлен в §0, до первого погружения; ISA-95 disambiguation embedded.
- Worked example фарма+FDA (s29) — concrete instantiation lec-07 принципа с цифрами (0.5% vs 0.1% precision gap), не абстрактный disclaimer.
- Failure-bucket holistic distribution (§1 4 мин + §2 4 мин + §3 4 мин + §4 4 мин + §4.5 1 мин + §5 15 мин + §6 1 мин = 33 мин из 75 = 44% по plan), не сконцентрирован в §5 = выполняет «holistic» требование (CLAUDE.md AI-Failure rule).
- Architectural angle на Yokogawa FKDPP (twin-as-sandbox, §4.2) — lec-12 differentiator vs lec-11 §3.2 algorithmic angle — выполнено как обещано в plan v2.
- Tone respectful, без familiar CTA, без «магической пилюли»; «трезвая нота» / «трезвая статистика» applied 2× в §6 и §5.

**Методические слабости (3 P1 + 5 P2, 0 P0):**
- s39 структурно over-budget по WPM (250 wpm если interpret marker literally — но это suspect структурная аномалия markup, не intent; см. P1 #1).
- Counterfactual baselines у PdM ROI 10:1 + 25-40% cost reduction не указаны явно — нарушение ENFORCED Baseline / Counterfactual Mandate.
- "Vision 99% точность" presented без сравнения с legacy machine vision baseline (~50% FP), хотя plan v2 §2 это специально включал.

Counter-check: 3 P1 issues + 5 P2 → APPROVE-WITH-POLISH (если бы 5+ P1 — REVISE). Speech show-able с rev pass для baseline additions + s39 marker re-split.

---

## P0 issues (методически непригоден)

**Нет P0.** Speech не требует REVISE.

---

## P1 issues (заметно вредит обучению)

### P1-1. s39 marker / WPM structural mismatch — 250 wpm если читать literal

**Severity:** P1
**Location:** speech.md L516-540
**Issue:** Маркер `[s39 · 2 мин]` обещает 2 минуты для слайда. Реально под этим маркером — 500 слов narrative (5 takeaways recap + bridge + Lec-13 рассуждение + spaceibo). При 75 wpm = 6.7 мин; при 95 wpm hard cap = 5.3 мин. Literal interpretation = 250 wpm, **2.6× over hard cap**.
**Evidence:** L516 marker → L540 «Готов к вопросам» содержит весь §8 closing + bridge + Q&A handover; tracked as «2 мин» в speech frontmatter `pacing_target: ≤95 wpm hard cap на каждом fragment`.
**Recommendation:** Split s39 marker в **two slide-aligned fragments**, например:
- `[s39 · 1 мин] Закрытие — 5 takeaways` (L520-528)
- `[s39 · 3 мин] Мост к Лекции 13 + Q&A handover` (L530-540)

OR обновить frontmatter `duration_min` на s39 в slides/s39-closing-hero.md с 2→4 мин и speech marker accordingly. Plan v2 §8 budget = 2 мин total — likely budget mismatch у plan v2 (closing раздел действительно занимает ~3-4 мин если lectured at normal pace).

**Why это P1, не P2:** DoD enforcement требует WPM ≤95 для **каждого** fragment (не average, не «8 of 10»). Один fragment с 250 wpm = DoD fail. Без полного re-split это пройдёт как «average 71.6 wpm» self-report и проскочит в GATE C — но при чтении лектор либо устроит спешку (impacts retention), либо overrun на 2-4 мин (impacts schedule).

### P1-2. Missing counterfactual: PdM ROI 10:1 / 25-40% cost reduction (L164)

**Severity:** P1
**Location:** speech.md L164 §2 / s13
**Issue:** «Средний ROI — десять к одному за два года. Снижение затрат на обслуживание — 25–40 процентов». Не указано **относительно какой базовой линии**. ROI 10:1 vs reactive maintenance (run-to-failure)? vs preventive (calendar-based)? vs run-time hours-based? Эти базовые линии дают радикально разные ROI absolute values. Аналогично «25-40% cost reduction» — vs annual maintenance budget какого типа.
**Evidence:** L164. Chapter §2 PdM section (`chapter.md`) тоже не указывает baseline явно; plan v2 §2 Evidence: «Deloitte 2026 года. Средний ROI 10:1 за 2 года» — same gap.
**Recommendation:** Add inline baseline phrasing, e.g. «Средний ROI — десять к одному за два года **относительно plan-based / календарного обслуживания** (где замена идёт по календарю независимо от состояния)». Это convert «магическая пилюля»-tone в инженерный compare.

**Why P1:** ENFORCED Baseline / Counterfactual Mandate (CLAUDE.md): «каждое **измеримое количественное утверждение** ОБЯЗАНО иметь **базу** или **counterfactual**». «10:1 ROI» без denominator/baseline = P1 «missing denominator» по mandate. Это структурный gap, не polish.

### P1-3. Missing counterfactual: Vision 99% accuracy vs legacy baseline (L146)

**Severity:** P1
**Location:** speech.md L146 §2 / s12
**Issue:** «Показатели 2026 года — точность 99 процентов и выше, ложные срабатывания от 0,1 до 2 процентов» — без сравнения с **legacy machine vision baseline**. Plan v2 §2 Evidence explicitly: «Legacy machine vision FP ~50%». Speech это потерял.
**Evidence:** L146. Plan v2 §2 line: «Vision QC: точность 99%+ при FP 0,1–2% (Indus Vision / Jidoka 2026). **Legacy machine vision FP ~50%**.» Speech не использует «legacy 50%» counterfactual.
**Recommendation:** Add 1 line после L146: «Это качественный скачок относительно legacy machine vision 2015–2020 годов, где типичная частота ложных срабатываний была около 50 процентов; современная AI-vision снижает её в 25-100 раз».
**Why P1:** Counter-example студент должен иметь, чтобы оценить **engineering significance** 99%-числа. Без baseline — это hype-стат, не инженерная характеристика.

---

## P2 issues (мелочи)

### P2-1. «World Economic Forum» / «MIT Sloan» — Russification leak

**Location:** L466 «World Economic Forum и McKinsey»; L404 «MIT Sloan 2025».
**Issue:** Per [[russification]] rule — для RU-audience canonical RU rendering: «Всемирный экономический форум» / «Школа управления Слоуна MIT». «McKinsey» / «MIT» — accepted as brand names per allowlist.
**Recommendation:** L466 → «программа Всемирного экономического форума и McKinsey»; L404 → leave «MIT Sloan» (часть бренда школы) but consider «исследование Школы управления Слоуна (MIT Sloan 2025)».
**Severity:** P2 — это narrative anglicism, но не блокирует понимание.

### P2-2. «ladder logic» (L216) — anglicism в narrative

**Location:** L216 «Напиши ladder logic для S7-1500».
**Issue:** «ladder logic» — это англоязычный технический термин; в RU-литературе используется «релейная логика» / «ладдер-диаграммы». В контексте quote из ChatGPT prompt это OK (студент пишет ChatGPT на смешанном языке), но в speaker speech (как пример) лучше Russify.
**Recommendation:** «Напиши **релейную логику** для S7-1500» OR keep but add inline gloss: «`ladder logic` (релейную логику)».
**Severity:** P2.

### P2-3. «Cloud 2008-2012, mobile 2010-2014, AI 2015-2020» (L406) — anglicism в era-names

**Location:** L406.
**Issue:** «Cloud» / «mobile» — нерусифицированные tech-era имена; canonical RU: «волна облачных сервисов 2008–2012, мобильная волна 2010–2014, AI 2015–2020».
**Recommendation:** «Волна **облачных сервисов** 2008–2012, **мобильная волна** 2010–2014, AI 2015–2020».
**Severity:** P2.

### P2-4. КАМАЗ / Норникель effect numbers без baseline (L488, L492)

**Location:** L488 «снижение простоев на 10–30 процентов, сокращение срока ввода новой модели на 15–25 процентов» (КАМАЗ); L492 «улучшение извлечения металла на 0,5–1,5 процентных пункта» (Норникель).
**Issue:** «−10-30%» относительно какой базовой линии? Pre-twin? Pre-AI? Аналогично 0.5-1.5 п.п. — относительно какого baseline извлечения (исходный showroom 60%? 80%? — без denominator студент не оценит engineering значимость).
**Recommendation:** L488 → «…на 10-30 процентов **относительно до-twin baseline** (по данным РБК Тренды)». L492 → «…на 0,5-1,5 процентных пункта **от исходного 80-85% извлечения металла** (типичный показатель флотации до AI; точные значения — в открытых отчётах Норникель)».
**Severity:** P2 — это российский раздел, факты validated, но missing-denominator pattern.

### P2-5. Pre-flight checklist item #2 — «Designer указал "7+ единиц"» внутренняя ссылка

**Location:** L551 «Designer указал "7+ единиц"; если опубликовано обновление к 2026-05-22, заменить».
**Issue:** «Designer указал» — это internal-process language (artifact-author reference, не student/lecturer language). В pre-flight (который лектор читает) лучше нейтрально: «На s25/s39 указано "7+ единиц". Если...».
**Recommendation:** L551 → «На s25 и s39 указано "семь и более единиц". Если опубликовано обновление к дате лекции, заменить».
**Severity:** P2.

---

## Cross-cutting issues

### LO coverage gaps
- LO2 (критическая оценка): покрыт §1 (75% fail), §2 (FP cascade), §5 (Gartner). PASS.
- LO5 (архитектура): покрыт §0 keystone, §4 twin-sandbox, §6 7-layer. PASS.
- LO7 (применимость / границы): покрыт всё §5, §3 PLC, §4 RL not for safety-critical. PASS.
- LO8 (отказать AI): покрыт §5 (5 questions vendor + 10 criteria). PASS.

### Cognitive load
- 5 новых концептов на ~10 мин блок: A0 + Kritzinger + 4 layers + рынок + Southeast Asian Port (§1) — границей. Acceptable.
- §5 «10 critеriев» подача компактная: «пройдёмся по самым важным», не пытается прочитать все 10. PASS.
- §6 OPC UA + MQTT + TSN + Lighthouse + 7 слоёв в 6 минут — densely packed. Borderline acceptable; lecturer должен temp slow down (наблюдено в WPM = 67 wpm для §6, который ниже avg — пауза-friendly).

### Sequence breaks
- §4 «35 дней» FKDPP claim repeated 4× (L266, L268, L274 implicit) — acceptable repetition для emphasis. PASS.
- §0 → §1 transition «Прежде чем подниматься по шкале, разберёмся с мостом» (plan v2) NOT в speech — speech использует «Раздел один из восьми. Что такое цифровой двойник в 2026 году». Менее conversational но acceptable.

### Tone drifts
- 0 hits «магическая пилюля» / «революция» / «AI спасёт».
- «Это пропасть между обещанием и доставкой» (L104) — engineering tone, не sensational. PASS.
- 1 «зафиксируем» (плановый conversational hook L102), 1 «давайте посчитаем вместе» (L152), 2 «обратите внимание» — appropriate pacing markers.

### Bridge / cross-references
- lec-11 cross-ref ×4 (L48, L60 ISA-95, L262 FKDPP, L424 vendor questions). Acceptable.
- lec-07 cross-ref ×1 (L384 FDA принцип). Acceptable for §5 worked example.
- lec-13 bridge canonical phrasing: «AI в логистике, цепях поставок и транспорте» MATCHES `notes/lectures/project_lec13_production.md` + plan v2. PASS.

---

## Self-checks (independent verification)

- [x] **WPM independently recalc:** max 91 wpm (s25), avg 71.6 wpm, sections >95 wpm = 0 of 39 (excluding s39 anomaly), sections >90 wpm = 2 (s25, s14 75.5; s22 75.5; s35 76.0 ниже 90 actually). **Excluding s39: max = 91 wpm (s25), all ≤95 wpm.** Если literal s39 250 wpm = DoD fail (см. P1-1). С re-split — PASS.
- [x] **Failure-share strict-in:** 40.9% words (2079/5083) / 42.3% minutes (30 из 71) — exceeds 30% floor, just below plan v2 target 44%. **Holistic distribution PASS** (failure-blocks present in §1, §2, §3, §4, §4.5, §5, §6 — not concentrated в §5 only).
- [x] **Deep latin-token scan:** 525 narrative-body Latin tokens, 51 unique outside brand+acronym allowlist. Most are compound modifiers («AI-инференс», «CAD-чертёж», «ROC-кривая», «RL-агент») — legitimate technical compounds. Real narrative anglicism leaks = **3** (ladder logic L216, Cloud/mobile L406, World Economic Forum L466) — all P2.
- [x] **Numbers sample 10:** 36.19/180.28 PASS, 17.15B PASS, 35 дней Yokogawa PASS, M65535 PASS, 57× cement PASS, 220+ Lighthouse PASS, 16% EBIT PASS, ROI 10:1 PASS (но baseline gap — P1-2), 99% vision PASS (но counterfactual gap — P1-3), 12M Southeast Asian Port PASS. **10/10 match chapter v3 + slides v3.**
- [x] **Anonymization:** 0 named institutions (МГТУ/Бауман/ИУ-N/Кафедра/ВКА/МАИ/СПбГУ/bauman/vka). PASS.
- [x] **Pre-flight actionable:** 9 items, все с specific URLs OR file paths OR concrete actions. PASS. Минор: item #2 wording — P2-5.
- [x] **Lec-13 canonical bridge:** «AI в логистике, цепях поставок и транспорте» L534 + L568 — EXACT match. PASS.
- [x] **s17 PLC fix:** L226 «скомпилируется в TIA Portal без видимых ошибок» + L230 «Контроллер уходит в режим STOP» — MATCHES brief intent. PASS.
- [x] **s20 Yokogawa attribution:** No mention «премия премьер-министра 2023», uses «значимой экономии энергии» — MATCHES brief. PASS.
- [x] **Hannover Messe s01 foreshadow:** L40 «снимок с Hannover Messe этого года». PASS.
- [x] **Keystone in §0:** s04 L54-62 introduces A0→A3 with examples + ISA-95 disambiguation **before** §1. PASS.
- [x] **Inclusive markers «мы с вами»:** 11 hits — ≥10 target. PASS.

---

## Топ-3 правок (приоритизировано)

### 1. (P1-1) Re-split s39 marker into 2-3 fragments OR update duration to 4 мин

**Action:** Either split L516-540 into `[s39a · 1 мин] 5 takeaways` + `[s39b · 3 мин] Лекция 13 bridge`, OR update plan v2 §8 budget 2→4 мин + speech marker s39 → «4 мин». Без этого DoD WPM hard cap fails.

### 2. (P1-2 + P1-3) Add baseline / counterfactual phrases для PdM ROI 10:1 и Vision 99% accuracy

**Action:**
- L164 → «…ROI — десять к одному за два года **относительно plan-based / календарного обслуживания**».
- After L146 → новый sentence: «Это качественный скачок относительно legacy machine vision 2015–2020 годов с типичной FP ~50%; современная AI-vision снижает её в 25-100 раз».

Без этого ENFORCED Baseline Mandate fails как P1 «missing denominator».

### 3. (P2-2 / P2-3 / P2-1) Russification 3 leak points

**Action:**
- L216 «ladder logic» → «релейную логику».
- L406 «Cloud / mobile» → «облачные сервисы / мобильная волна».
- L466 «World Economic Forum» → «Всемирного экономического форума».

---

## Verdict

**APPROVE-WITH-POLISH.**

Speech v1 — methodically solid, conversational tone выдержан, plan v2 carry-forward выполнен, failure-share 30% floor exceeded holistically, locked numbers match across 3 артефакта, keystone-axis present в §0 до первого погружения, lec-N pattern cross-refs accurate.

3 P1 + 5 P2 issues — show-able с known caveats; не требует REJECT/REVISE. Counter-check: ≤4 P1 → APPROVE-WITH-POLISH (если бы P1 ≥5 — change to REVISE). 3 < 5 = APPROVE-WITH-POLISH valid.

Recommend single-pass speech-writer revision на топ-3 правок (≤30 минут work). Затем GATE C ready.
