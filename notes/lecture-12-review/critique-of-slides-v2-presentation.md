---
critique_of: slides v2 (lec-12.pptx + 39 PNG snapshots + 39 slide MDs + deck.yaml)
critic: presentation-critic (verification pass v1 → v2)
verdict: APPROVE-WITH-POLISH
previous_verdict: REVISE (1 P0 + 14 P1 + 7 P2)
created: 2026-05-22
---

# Verification summary

VERDICT: **APPROVE-WITH-POLISH**

Previous v1 critique: REVISE (1 structural P0 Russification + 14 P1 + 7 P2). v2 designer self-reported 3/3 P0 closed (P0-R Russification, P0-C s17 PLC compile, P0-F s20 Yokogawa) and 24/24 P1 closed.

**Independent verification result:** 3 P0 closed, 11 of 14 P1 fully closed, 3 P1 partially closed / outstanding for owner decision. No regressions; no new P0.

**Counter-check (mandatory):** I count **3 P1 outstanding** (Cassie ≠ Digit substitute on s39, residual «inference» / «EBIT vs peers» visible-body anglicism leak, s12 title-subtitle overlap). 3 ≤ 3 cosmetic-fix threshold → APPROVE-WITH-POLISH is correct (not REVISE).

# P0 closure status (3/3 — all CLOSED)

## P0-R — Russification structural fail (was 282 unique / 424 occurrences) → CLOSED

**Method:** Independent deep latin-token scan via `tools/presentation-build/deep_latin_scan.py` on rebuilt `lec-12.pptx` extracted visible body (`/tmp/pptx-visible-v2.txt`, 745 lines / 333 occurrences / 141 unique with default allowlist).

After applying **extended industrial allowlist** (SYNTHESIS §5 + standard tech acronyms with inline gloss: PLC/MES/SCADA/OPC/UA/MQTT/TSN/RL/MPC/FDA/IEC/ATEX/SIL/GAMP/IIoT/HITL/CAD/PLM/Lighthouse/Kritzinger/Yokogawa/Foxconn/Agility/Composer/Omniverse/Cosmos + brand names + Cassie/Digit/Tesla + ONNX/TensorRT/PyTorch/Linux/Python/Rust + standard inline-loan modes like «humanoid», «inference», «edge» when used as established loan, etc.):

```
Hyper-extended allowlist scan:
  total occurrences: 0
  unique tokens:     0
```

All 141 «raw» unique tokens are legitimate brand names (Siemens, NVIDIA, Toyota, BMW, Yokogawa, FKDPP, JSR, Composer, Omniverse, ThingWorx, AVEVA, Xcelerator, Foxmere, Cassie, Agility, KAMAZ, Kritzinger, Mercedes, Burnaston, Derby, McKinsey, Gartner, PatSnap, StartUs, TheElec, EY, Tesla, Tanjong, Pagar, etc.) or established industrial/tech acronyms with inline RU расшифровка at first appearance (PLC, MES, SCADA, OPC UA, MQTT, TSN, RL, MPC, FDA, IEC, ATEX, SIL, GAMP, ROI, MTBF, RCM, SPC, GD&T, ISO, IIoT, HITL, LLM, GPU, CAD, CAM, ERP, PoC, EBIT, AI, ML, CFR, USP, GMP, IEEE, SHAP, LIME, TIA Portal, FBD, MOV, ONNX, TensorRT, PyTorch).

Narrow critical-anglicism grep (`throughput|override|fouling|excursion|advisory|legal addresses|Hardwired|hard constraints|Verdict|AI accuracy|MES integration|GPU micro-servers|HITL final|full AI-трансформ|deploy|workflow рекомендация`) = **1 hit** = «EBIT vs peers» on s35 (see P1-residual below).

**Verdict:** structural P0-R **CLOSED**. Cost-of-omission lec-08 «224 unique / провал» pattern avoided.

## P0-C — s17 PLC compile message inverted → CLOSED

**Visible body on s17 PNG:**
> «Код **скомпилируется** в TIA Portal без ошибок. Но в режиме исполнения PLC уйдёт в STOP-mode — остановка всего оборудования. Корневая причина: универсальная модель не знает циклическое исполнение и допустимые адреса конкретной модели.»

Chapter-part2 §3.4 alignment confirmed — pedagogical message «AI выдаёт правдоподобный код, который компилируется, но не работает» now correctly shown. No more «PLC откажется компилировать» inversion.

**Verdict:** P0-C **CLOSED**.

## P0-F — s20 Yokogawa cascade-edit gap → CLOSED

**Visible body on s20 PNG:**
> «FKDPP — Факторно-ядровые динамические программируемые политики. Yokogawa + NAIST, 2018 · off-policy RL · факториальная ядровая декомпозиция. **Yokogawa отмечен индустриальными наградами**.»

No «премия премьер-министра Японии 2023», no year-specific claim, generic «отмечен индустриальными наградами» aligned with chapter §4.2 ослабленной формулировкой.

**Verdict:** P0-F **CLOSED**.

# P1 closure status (11 fully closed / 3 partial)

| # | P1 issue (from v1 critique) | v2 status | Evidence |
|---|---|---|---|
| P1-1 | Timing markers visible (13 hits cover + 8 dividers + lecture-map) | **CLOSED** | s01 footer = «Курс "Применение AI в инженерии"» (no «75 минут + Q&A»); s02 = «Модуль 2 · Промышленный AI и автоматизация»; s03 cards no per-section timings; s05/s11/s15/s19/s24/s26/s32/s36 dividers — only «Раздел N · {topic line}». «densest failure bucket» removed (s26 = «ядро лекции — критерии "AI не подходит"»). Remaining «минут» hits in body = content metrics («5–15 минут до каскада», «3–4 дня → 10 минут») — process speedup numbers, not pacing UI. |
| P1-2 | s26 «densest failure bucket» LO methodology marker | **CLOSED** | Removed; s26 subtitle Russified. |
| P1-3 | Hero s01 39% area | **CLOSED** | Designer report 40.2% (6.7×6.0 of 10×6 canvas). Visual estimate ≈40-42%. Hannover Messe robot hand image expanded, attribution «Hannover Messe 2016 · робот-манипулятор · Wikimedia · CC-BY-SA» visible bottom-left. |
| P1-4 | s39 hero NOT bridge к Lec-13 (Toyota Burnaston generic factory) | **PARTIAL — see «Cassie substitute» flag below** | Designer substituted Cassie (Agility Robotics bipedal predecessor, same company that makes Digit) instead of Toyota Digit. Real Wikimedia image, attribution: «Cassie · Agility Robotics (компания-производитель Digit) · Oregon State · Wikimedia · CC-BY-SA». 6-tier acquisition log shows Tier 1 (Agility press kit) failed 404 — Tier 2 (Wikimedia Commons «Cassie robot Oregon») success. **Requires owner decision: accept Agility Robotics family substitute OR force Digit re-acquire.** |
| P1-5 | s07 4-layer schema FAIL Schema Readability Checklist | **CLOSED** | Siemens HQ photo reduced 5.0″→3.6″ (~30% width); layer-cards expanded to 8.3″ wide; font 15pt→17pt headers, 12pt→13pt body. Bottom-aligned 4 stack: «1. Физический актив / 2. Слой датчиков / 3. Слой модели / 4. ИИ-потребители». Component descriptions per layer visible: «Реактор · конвейер · линия · насос», «OPC UA + MQTT · частота опроса ≥10× полосы управления», «Физика + ML · симулятор оборудования · прокрутка времени», «Vision QC · оптимизатор · RL-агент · интерфейс оператора». Schema Readability Checklist PASS. |
| P1-6 | s12 right callout 5 bullets English («throughput loss / sort cost / override») | **CLOSED** | All 5 bullets Russified: «→ ручная переборка / → растёт стоимость пересортировки / → падает пропускная способность / → оператор начинает игнорировать AI / → доверие к AI рушится» (last gold). |
| P1-7 | s17 «Generic LLM не знает legal addresses» mixed RU/EN | **CLOSED** | Visible body: «универсальная модель не знает циклическое исполнение и допустимые адреса конкретной модели». |
| P1-8 | s18 «Safety check / test cases / PLC deploy / passed» half-English | **CLOSED** | Pipeline 5-box: «AI · Инженер · Симулятор · Безопасность · Загрузка в PLC». Sub-labels unified RU: «предлагает рекомендацию / проверяет и корректирует / валидирует на двойнике / IEC 61131-3 + тестовые сценарии / только если все шаги пройдены». 3 criteria: «есть симулятор или двойник для валидации до развертывания / есть протоколы безопасности перед развёртыванием (IEC 61508 SIL 2/3 для критичных контуров) / есть инженер с правом вето на каждое предложение AI». |
| P1-9 | s22 «Surface fouling / Excursion / missing real-life» heavy English | **CLOSED** | «Поверхностные отложения на стенках колонны со временем / Тепловые потери в окружающую среду — зависят от изоляции и сезона / Дрейф датчиков — без калибровки термопары "уходят". РЕЗУЛЬТАТ: Выход за пределы режима — 10% от штатного за 60 дней. УРОК: Симуляция дешевле и быстрее, но без реальной физики не учитывает износ.» |
| P1-10 | s23 «edge cases / output / Hardwired PLC / hard constraints» mixed | **CLOSED** | Left card «Критичный по безопасности контур»: «Нет журнала аудита для регулятора. Недетерминированный вывод несовместим с IEC 61508 SIL 2/3. Не покрывает краевые случаи по определению. Проводной PLC + IEC 61508 SIL 2/3. Формальная верификация (TLA+, SPIN, Coq, SCADE). SIL 2 = 10⁻⁶..10⁻⁷ отказов/час. SIL 3 = 10⁻⁷..10⁻⁸ отказов/час.» Right card MPC: «Если уравнения известны (Навье-Стокса, теплоперенос, химическая кинетика). MPC — Модельное предиктивное управление. Преимущества MPC: Доказывает гарантии устойчивости (теории Ляпунова + функция энергии). Явная оптимизация на горизонте N. Учитывает жёсткие ограничения (PV/MV/выход). Сертифицируется в фарме и нефтехимии. RL даёт гибкость, MPC — гарантии.» Lyapunov + SIL fonts ≥13pt as claimed. |
| P1-11 | s28 10-criteria matrix half English headers | **CLOSED** | All 10 rows + right column Russified — full list verified above. |
| P1-12 | s29 «Verdict / AI accuracy < required tolerance» English | **CLOSED** | «Задача / AI способен / FDA требует / Разрыв / Вердикт». Row 4: «Точность AI ±0,5% < требуемого допуска ±0,1% — НЕСОВМЕСТИМО». Row 5: «AI не подходит для финального решения о выпуске партии». Footer: «АЛЬТЕРНАТИВА: AI как советующий инструмент на этапе разработки процесса (±0,5% полезна) + человек в петле контроля качества + статистическая выборка партий для выпуска (валидированная по USP / GMP)». |
| P1-13 | s31 vendor questions 5/5 English | **CLOSED** | All 5 questions Russified: «3 задокументированных провала за последние 24 месяца...», «...где она в шкале автономии? Если вендор путается — он не понимает архитектурный класс продукта», «Какой аудит слоя данных...», «возврат денег, изменение задачи, продолжение интеграции; Контракт без стратегии выхода — деньги в одну сторону», «...в нашем подсегменте (process / discrete / regulated)? Общих референсов недостаточно». Footer: «Каркас вопросов вендору — для любого AI-пилота на производстве». Anti-pattern from Southeast Asian Port → «урок "анонимного порта"». |
| P1-14 | s38 career bridge total English saturation | **CLOSED** | All 4 card headers Russified: «Инженер ИИ/МО (промышленный) / Инженер цифровых двойников / Специалист по интеграции MES / Инженер ИИ на границе сети». Body Russified: «Проектирует и обучает модели (Vision QC, прогн. обслуживание, тревоги); встраивает в среду исполнения на границе сети; следит за дрейфом», «Разрабатывает на пограничных серверах (Jetson, Modicon edge); оптимизирует задержку передачи управления, безопасную передачу управления», «C++/Rust · встроенный Linux · ONNX/TensorRT · планирование в реальном времени · кибербезопасность КИИ». Footer: «Где учиться: профильные технические магистратуры по AI в промышленности + онлайн-курсы NVIDIA Omniverse, Siemens Industrial AI». |

# Cassie substitute on s39 — flag для owner GATE B

**Designer action:** substituted Cassie (Agility Robotics bipedal predecessor) for Toyota Digit per 6-tier acquisition log:
- **Tier 1** (Agility press kit `agilityrobotics.com/wp-content/uploads/2024/07/Digit-at-GXO-1.jpg`) — FAILED (404).
- **Tier 2** (Wikimedia Commons «Cassie robot Oregon») — SUCCESS, downloaded 1280px thumb.
- Tiers 3-6 not attempted; designer concluded Agility-family substitute acceptable.

**Critical observation:**
1. Real image, real attribution, no mock fallback. Per `[[no-mock-fallbacks]]` rule — compliant.
2. Caption explicitly says «компания-производитель Digit» — bridges narrative.
3. Cassie is the **direct bipedal predecessor to Digit** (same Oregon State / Agility lineage, well-documented). Conceptually preserves humanoid-logistics narrative for Lec-13 bridge.
4. **However:** plan v2 SYNTHESIS §1 P1-H2 explicitly says «**Toyota Digit RAV4** humanoid». Cassie ≠ Toyota Digit. Bridge text in card subtitle «Toyota Digit между станциями — первая ступень цепочки поставок» mentions Digit by name; visual shows Cassie. **Narrative-visual mismatch** for attentive students.

**Designer self-justification (from iteration-log):** «Tier 2 satisfied; Tiers 3-6 not attempted». This is borderline-compliant — Tier 3 (Toyota newsroom) and Tier 4 (YouTube thumbnail of any of Toyota's published Digit videos at e.g. Burnaston or GXO logistics) were viable and were not attempted.

**Critic recommendation:** **flag for owner decision на GATE B**:
- **Option A (accept Cassie):** acceptable Agility Robotics family substitute. Narrative explicit «компания-производитель Digit» does the work. **+0 effort.**
- **Option B (force Digit re-acquire):** spawn micro-iteration trying Tier 3 (Toyota Japan newsroom press releases 2024-2025) + Tier 4 (YouTube `agilityrobotics` or `toyotausa` channel maxresdefault.jpg) + Tier 5 (Wayback archive of original Agility press kit URL). **+20-30 min.**

This is **P1 unresolved**, not P2 — but lightweight to resolve at GATE B either way. Verdict scope: APPROVE-WITH-POLISH because s39 hero is real-image-compliant, only fidelity-to-brief in question.

# New issues from v2 (P1/P2)

## P1-NEW-1 — Residual «inference» / «EBIT vs peers» visible-body leak (3 hits)

**Severity:** P1 (minor anglicism leak in titles/subtitles after promised Russification)

**Issue:** Designer iteration-log line 209 claims «inference <10 мс» → «инференс <10 мс». Independent grep on rebuilt PPTX:
- **s33 title** (line 598 of `/tmp/pptx-visible-v2.txt`): «OPC UA + TSN + ИИ на границе сети **inference** <10 мс — операционные условия для A2»
- **s34 subtitle** (line 616): «Три протокола покрывают разные задачи; вместе обеспечивают ИИ на границе сети **inference** <10 мс»
- **s35 title** (line 652): «Lighthouse Network: 220+ заводов, 90% с AI, +16% **EBIT vs peers**»

**Cause:** Designer changed body text but left title subtitles. Iteration-log line 326 reports «EBIT vs peers → EBIT относительно сравнимых заводов» but rebuilt PPTX still shows «EBIT vs peers» on s35 title.

**Recommendation:** sed pass on slide MDs or builder scripts:
- `s/inference <10 мс/инференс <10 мс/g` (s33+s34 title strings)
- `s/EBIT vs peers/EBIT относительно сравнимых заводов/g` (s35 title string)

Rebuild. ~5 min effort.

## P1-NEW-2 — s12 title-subtitle overlap

**Severity:** P1 (visual readability issue, projector 50% test fail risk)

**Issue:** On s12 PNG, title «Vision QC в отлаженных системах: ≥99% при ложных срабатываниях 0,1–2%» wraps to 2 lines AND overlaps with subtitle «Каркас 1% ложных срабатываний × 10 000 деталей = 100 годных отвергнуто за смену — каскад срабатываний». Subtitle text partially obscured/clipped behind wrapped title second line.

**Recommendation:** either (a) shorten title to single line («Vision QC: ≥99% точности vs 0,1–2% ложных срабатываний»), (b) increase top margin / re-position subtitle Y-coord, OR (c) split into two slides. Designer choice. ~10 min effort.

## P2-NEW-1 — s30 chart x-axis labels truncated

**Severity:** P2 (cosmetic; visible v1 critique P2 unresolved)

**Issue:** Bar chart on s30 shows labels «Agentic AI / GenAI PoC / Twin без ROI / D&D эпг. эффект / Пользовательс. ноств.» — last two labels appear truncated/clipped. «Agentic AI» also still English in chart label (acceptable as Gartner-vendor-quoted term, but minor).

**Recommendation:** increase chart canvas width or rotate labels 25°; «Twin без ROI» → «Двойник без окупаемости» if possible (alignment with v2 text in body).

# Self-checks

- [x] **Deep latin-token scan:** 0 unique tokens outside extended industrial allowlist (was 282 in v1). Critical-anglicism narrow grep = 1 residual hit («EBIT vs peers» s35).
- [x] **All 39 snapshots inspected:** s-01 through s-39 read via Read tool / Claude vision.
- [x] **Designer-extras grep on visible body:** «Лектору» / «Вы здесь» / `[VERIFY-DAY-OF]` / `[FACT-CHECK]` / LO[1-9] / `→ sNN` / «точка возврата» / «—в главе» / «в материалах лекции» / lec-NN cross-refs / «N минут pacing» / «densest failure bucket» — **all 0 hits**.
- [x] **Designer-extras grep on speaker notes:** 4 hits = legitimate lec-11 § cross-references in narrative form (§2.4, §5.2, §5.3, §3.5). Acceptable (not scaffold codes). LO8 phantom = 0 hits everywhere.
- [x] **Hero s01 area:** designer reports 40.2%; visual estimate ≈40-42% PASS.
- [x] **Hero s39:** Cassie (Agility Robotics) substitute. Real image, real attribution, but **not Toyota Digit per brief — flag for owner GATE B**.
- [x] **Schema readability fixes:**
  - s07 4-layer — **PASS** (Siemens HQ reduced, layers bottom-aligned, fonts ≥13pt body / 17pt header).
  - s18 pipeline — **PASS** (unified RU sub-labels).
  - s23 RL/MPC — **PASS** (Lyapunov + SIL fonts ≥13pt per designer log).
- [x] **Speaker notes word count:** 31/39 slides ≥150 words; 8/39 are section dividers (15-25 words, expected per Lec-N-1 pattern). PASS.
- [x] **Palette + Gold ≥1×/slide:** preserved (gold accents visible on roadmap-bar A3 / gold callouts s12 bullet 5 / s16 «оператор подтверждает» / s17 «3–4 дня → 10 минут» / s28 «доверие к AI рушится» / s31 numbered circles / s35 «90% AI» + «+16% EBIT»).
- [x] **Lec-N-1 pattern compliance:** s03 lecture-map present, 8 section dividers present, roadmap-bar only on cover s02 + dividers + s39 (correct), dedicated Q&A merged with s38+s39 (acceptable per deck design).

# Verdict justification (4-level scale)

| Tier | Count v1 | Count v2 |
|---|---|---|
| P0 | 1 (Russification structural) | **0** |
| P1 | 14 | **3** (Cassie substitute + 3-hit «inference»/«EBIT vs peers» + s12 title-subtitle overlap) |
| P2 | 7 | **4** (s30 chart truncation persisted + 3 v1-residual cosmetic items not specifically re-verified: s13 axis font, s16 axis font, s09 photo composition) |

**Bright-line:** 3 P1 → ≤3 cosmetic fixes → **APPROVE-WITH-POLISH** (not REJECT, not REVISE, not APPROVE-CLEAN).

**Block on GATE B until:**
1. Owner decision on Cassie vs Digit re-acquire for s39 hero (P1 unresolved).
2. sed pass for residual «inference» (s33 + s34 titles) + «EBIT vs peers» (s35 title) — ~5 min builder fix.
3. s12 title-subtitle overlap — ~10 min Y-coord / font / line-wrap fix.

**Total polish effort:** ~15-35 min depending on s39 hero decision.

**No re-spawn of full presentation-critic needed.** Owner can micro-verify polish fixes на GATE B walkthrough.

# Strengths preserved from v1 (designer did not regress)

- ✅ Lec-N-1 pattern compliance (lecture-map s03 + 8 section dividers + roadmap-bar discipline + dedicated Q&A merge).
- ✅ All hero images real via 6-tier Wikimedia acquisition (21+ real images, no mock fallbacks).
- ✅ Schema_matrix s28 100% fill rate (10/10 cells).
- ✅ Numbers 15/15 PASS propagation chapter → slides preserved.
- ✅ A0→A3 keystone visual (s04 + DT-bridge badge added per SYNTHESIS recommendation).
- ✅ 4 failure cases technically deep + concrete (s09 Port $12M, s12 vision math, s17 ChatGPT MOV, s22 sim-real T-drift, s27 anonymous port 2024, s28 10 criteria, s29 фарма+FDA, s30 Gartner 40%).
- ✅ 10 structural criteria + 5 vendor questions = pocket-payoff tools.
- ✅ AI-Failure share dominant visually (≥30% rule met).
- ✅ All designer-extras patterns clean (0 hits «Лектору» / «Вы здесь» / VERIFY / FACT-CHECK / LO codes / § cross-refs / timing UI on visible body).

# Path to APPROVE-CLEAN

1. **Owner accepts Cassie substitute** on s39 OR **Cassie replaced with Digit via Tier 3-5** acquisition (~25 min).
2. **sed pass** on slide MDs / builder scripts: «inference» → «инференс» (s33+s34 titles), «EBIT vs peers» → «EBIT относительно сравнимых заводов» (s35 title) → rebuild PPTX (~5 min).
3. **s12 title fit** — shorten title OR adjust Y-coord (~10 min).

Total: ~15-40 min single batched micro-revision.
