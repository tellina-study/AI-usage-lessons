# Лекция 4 — Visual Loop Iteration Log

Deck: 32 слайда (s01–s32 monotonic). Source: deck.yaml + deck-part2.yaml +
slides/*.md. Render-style эталон: lec-03/rendered/build_v3.py. Palette LOCKED
Ocean + Teal + Gold ≥1×/slide. Motif Ocean rounded box. 16:9 13.333×7.5".

Schema-слайды (Schema §5.5 gate): s03 (matrix mapping), s11 (cycle), s12
(matrix), s15 (pipeline), s20 (matrix), s24 (matrix), s25 (matrix — WATCH),
s27 (matrix), s29 (matrix — WATCH). Dividers: s10/s14/s18.

---

## Iter 1 — all 32 slides (build_lec04.py first render, 110dpi)

- (a) what inspected: full deck montage @25% + per-slide s01, s02, s06, s10,
  s11, s25, s29 @110dpi.
- (b) findings:
  - Structure consistent across all 32: Ocean palette, motif boxes, gold
    highlight present, charts embedded, 7-card roadmap on dividers+cover,
    gold-current marker working.
  - **P1 title-overflow (multi-slide):** long assertion titles wrap to
    2 lines and collide with the element below (icon / italic subtitle).
    Confirmed s01 (title 2-line + collides with gauge icon top-right),
    s06 (title 2-line «читает.» collides with italic def at y=0.94).
    Suspected same on s03/s07/s09/s25/s27/s30 (reduced-font long titles).
  - **P2 s25 color semantics:** TDD row (best fit) and vibe-coding row
    (antipattern) both rendered gold → ambiguous (gold should mean one
    semantic). Need differentiation: TDD gold (winner) vs vibe-coding
    teal/distinct (rejected).
  - s02 cover: PASS (matches lec-03 cover canon).
  - s10 divider: PASS (matches lec-03 divider template exactly).
  - s11 cycle: PASS schema §5.5 (4 steps, arrows, failure modes, check
    gold, explicit continue label, frame plate).
  - s29 matrix (WATCH): PASS schema §5.5 (per-col icons, axis-in,
    teal SOLID=hard-gate semantic, ≥75% fill, dominant gold plate 3pt,
    cells ≥12pt, single-line headers).
  - s25 matrix (WATCH): readable, single-line headers, but color
    semantics ambiguous (see P2).
- (c) checklist status: schema slides s11/s29 PASS; s25 PASS-except-color;
  title-overflow blocks final accept on ≥6 slides.
- verdict: continue → iter 2 (fix title-box heights deck-wide + s25 color).

---

## Iter 2 — fix pass (title-overflow + s25 color semantics)

- (a) inspected: s01, s06, s07, s16 (title-overflow @110dpi); s25 (color).
- (b) changed:
  - s01: title 26→24pt, w=12.25→10.85 (clears icon), h=0.96 (2-line);
         gauge icon moved 11.75→12.05, 0.80→0.74.
  - s06: title 23→20pt single-line, y=0.36 h=0.52; subtitle y 0.94→0.96.
  - s07: title 22→20pt, h=0.86→0.90 (clean 2-line); content box
         by 1.46→1.50, bh 2.70→2.66.
  - s16: title 24→22pt, h=0.62→0.56; content ly 1.30→1.34, lh 4.55→4.52.
  - s25: color semantics — TDD `g` stays GOLD solid (winner);
         vibe-coding `x` GOLD→TEAL solid (rejected antipattern, lec-03
         convention gold=strong/teal=weak). c1 text color explicit.
- (c) checklist: s01/s06/s07/s16 title-overflow RESOLVED (verified @110dpi);
      s25 color semantics now unambiguous (gold=best, teal=rejected) BUT
      subtitle text still said «золото = антипаттерн» → P3 carry to iter 3.
- verdict: continue → iter 3 (s25 subtitle text).

## Iter 3 — s25 subtitle + full-deck systematic review

- (a) inspected: all 32 @110dpi montage + per-slide s04, s05, s09, s13,
      s15, s17, s20, s30, s32 deep.
- (b) changed: s25 subtitle «золото SOLID = антипаттерн…» →
      «золото SOLID = лучшая совместимость; бирюза SOLID = антипаттерн,
      отвергается по построению» (matches new color semantics).
- (c) findings: deck visually coherent, matches lec-03 style language.
      Gold ≥1× on all 32 (programmatic audit PASS). Canvas 13.333×7.5 PASS.
      Schema §5.5: s03 matrix PASS · s11 cycle PASS · s12 matrix PASS ·
      s15 pipeline PASS (RIGHT_ARROW, owner-frame, ≤5 stages) · s20 matrix
      PASS · s24 matrix PASS · s25 matrix PASS · s27 matrix PASS · s29
      matrix PASS. Dividers s10/s14/s18 match lec-03 template.
      Iter-3 not clean (per Anthropic principle, found refinement):
      s15 4th gold stage label «approval · merge · прод-гейт» crowded
      (3-line wrap in box).
- verdict: continue → iter 4 (s15 stage label polish).

## Iter 4 — s15 polish + final accept @150dpi

- (a) inspected: s15, s25 @150dpi; full-deck 25% overview (5-sec gate);
      s29/s25 @50% projector test.
- (b) changed: s15 4th stage «approval · merge · прод-гейт» →
      «approval · merge · прод»; stage font 13→12.5pt, arrow gap
      0.55→0.52, box padding tightened (clean 2-line fit).
- (c) FINAL checklist status:
  - **5-Second Test (25% overview):** PASS — all 32 slides, main message
    = assertion match. Watch-items: s25 «TDD №1 / vibe-coding отвергается»
    reads instantly (gold vs teal); s29 «детерминир. → обычный код без AI»
    (dominant gold plate) reads instantly.
  - **Projector 50% (s29 peak-density WATCH):** PASS — axis-in labels,
    per-col icons, teal SOLID hard-gate semantic, cells ≥12pt legible,
    single-line headers, gold plate stroke 3pt dominant.
  - **Projector 50% (s25 WATCH):** PASS — gold/teal SOLID differentiation
    legible, ≥75% fill, single-line headers.
  - **Schema §5.5 ALL schema slides:** PASS (s03/s11/s12/s15/s20/s24/
    s25/s29 + dividers s10/s14/s18).
  - **Gold ≥1×/slide:** PASS (32/32, programmatic audit).
  - **Palette LOCKED:** PASS (only Ocean + Teal + Gold + surface/grey).
  - **Motif Ocean rounded box:** PASS (every content slide).
  - **16:9 13.333×7.5:** PASS.
  - **No forbidden additions:** PASS (no «Лектору»/«Вы здесь»/timing/
    subtitle-init/CVE#/vendor-pricing/code>3lines/color-only-highlight
    on visible layer; roadmap-bar only on dividers+cover per lec-N-1
    pattern; no local binding ИУ6/Бауман).
- iterations per slide: min 3 (most), 4 (s01/s06/s07/s15/s16/s25).
- verdict: **ACCEPT** — all gates PASS, deck ready for QA agents.

### Per-slide iteration count
- 4 iter: s01, s06, s07, s15, s16, s25 (title-overflow / color / pipeline)
- 3 iter: all other 26 slides (rendered + 2 review passes + final accept)
- All slides ≥3 iter (min), max 4 (well under 7 cap). No escalations.

### Schema §5.5 final pass matrix (v1)
| Slide | Subtype | §5.5 | 5-sec | 50% proj |
|---|---|---|---|---|
| s03 | matrix (mapping) | PASS | PASS | PASS |
| s10 | section_divider | PASS | PASS | PASS |
| s11 | cycle | PASS | PASS | PASS |
| s12 | matrix | PASS | PASS | PASS |
| s14 | section_divider | PASS | PASS | PASS |
| s15 | pipeline | PASS | PASS | PASS |
| s18 | section_divider | PASS | PASS | PASS |
| s20 | matrix | PASS | PASS | PASS |
| s24 | matrix | PASS | PASS | PASS |
| **s25** | **matrix (WATCH)** | **PASS** | **PASS** | **PASS** |
| s27 | matrix | PASS | PASS | PASS |
| **s29** | **matrix (WATCH)** | **PASS** | **PASS** | **PASS** |

---

## v1 → v2 fix-iteration (Phase 7 QA: presentation-critic REVISE + 4 critics)

Issue #99. SYNTHESIS fix-list (P0 + 6 P1 + P2) + 3 USER-decisions (s28/s26/s29
reformulate) + deck-wide newcomer-pass. v1 archived в `archive-v1/`.

### Iter 1 — apply all fixes + first render (150dpi)
- (a) inspected: s01,s03,s04,s06,s08,s12,s13,s17,s22,s26,s28,s29 @150dpi.
- (b) changed (БЛОК A): P0 — 0 [VFY] на видимом (5 футеров→человеч. язык;
  verify-флаг только deck.yaml). P1 §/sNN/LO/Раздел leak — s03/s04/s07/s09/
  s11/s15/s17/s20/s23/s24/s25/s30/s32 + s32-md Body «LO4»/«§6.1». P1 charts
  — s06/s08/s12/s13/s17 декор-bar→крупные mega-stat-плашки (s01-стиль; chart
  embed убран, gen_charts.py больше не нужен). s13 GitClear→3 trend-числа
  (8,3↑12,3 / 24,1↓9,5 / 5,5↑7,9; числа НЕ менялись). P1 s16 confused-deputy
  inline-gloss в notes. P1 s19–23 ритм — s22 → single-focus горизонт.
  attack-flow + hero «58%» (ломает 2-кол ритм). P1 s25/s29 убрана
  color-legend subtitle. P2 s01 явная знаковая легенда. БЛОК B — s28/s26/s29
  переформулированы (s26 EN-цитаты→notes; s29 20-ячеек→доминанта-вывод +
  3 оси; s28 why-for-AI/where-weak). БЛОК C — newcomer Russify s20/s25/s27,
  course-scaffold/vendor-бенчмарк→рус.
- (c) found: s13 right — 3 плашки overflow за ocean-box (bottom-text
  накладывается на 3-ю); s01 — value-колонка узкая, «времени» рвётся
  «врем\nени».
- verdict: continue → iter 2 (fix s13 overflow + s01 layout).

### Iter 2 — fix s13 overflow + s01 row layout
- (a) inspected: s01, s13 @150dpi.
- (b) changed: s13 — sh 1.00→0.86, gap 0.06→0.05, bottom-line привязан к
  факт. концу плашек (no overlap). trend_stat helper — число-бокс scale
  by h, 27→25pt. s01 — 3-кол (label/tag/value) → 2-зона (label+italic-tag
  слева, big 30pt число справа, value-box 0.55→2.35 wide).
- (c) verified: s13 — 3 числа чисто, no overlap, gold на «клоны». s01 —
  «Прогноз / ждали ускорение → −24%», знак однозначен, gold на +19%.
- verdict: continue → iter 3 (full-deck systematic review).

### Iter 3 — full-deck systematic review + final accept
- (a) inspected: s07/s11/s23/s24/s25/s27/s32 deep + 25% montage 5-sec sweep
  + s29 50% projector + byte-diff vs v1.
- (b) found (Anthropic principle — iter-3 not clean): none blocking;
  s23 confused-deputy gloss reads, s24 №-column centered clean, s27 jargon
  Russified, s29 dominant conclusion reads @50%. Montage: palette coherent,
  gold ≥1× all 32, s22 rhythm-break visible.
- (c) FINAL gates:
  - 5-Second Test (25% montage): PASS — main message = assertion на всех 32.
    s04 «5 точек возврата» теперь читается смыслом (не §-кодами); s12/s13/
    s17/s06/s08 числа крупные; s29 доминанта-вывод.
  - Projector 50% (s25/s29 WATCH + s12/s13 new mega-stat): PASS.
  - Schema §5.5: s03/s11/s12/s15/s20/s24/s25/s27/s29 + s10/s14/s18 PASS.
  - Palette LOCKED: PASS (Ocean+Teal+Gold only). Gold ≥1×/slide: 32/32.
  - Canvas 13.333×7.5 (16:9): PASS. 32 slides (no add/del): PASS.
  - 0 [VFY]/[VERIFY]/§/(sNN)/LO на видимом слое: PASS (grep-verified).
  - Speaker notes edited (s16/s28/s32): 297/254/278 слов — в [150,300].
  - Side-effects: lec-01/02/03/07 clean, no ~$*.pptx, only lec-04 touched.
- byte-identical vs v1: 6/32 (s02,s05,s10,s14,s18,s31 — не редактировались);
  changed: 26/32 = ровно edited-set (no unintended render-drift).
- iterations: 3 на изменённые (s01/s13 — 3 с доп. fix-pass на iter 2).
  Max 3, well under 7 cap. No escalations.
- verdict: **ACCEPT** — все gates PASS, v2 готов к re-QA.

---

# v3 — Раздел-0 restructure + сквозной tone-pass (Решение #100, #99)

deck v2 показан владельцу — сторителлинг сломан (несущая ось A→D нигде не
показана; Раздел 0 защищает методологию). Перестройка по plan-v2-final §4.
Archive: rendered/archive-v2/. Baseline grep: 5 visible leaks (всё в s03/s04/s05).

## Iter 1 — s03 KEYSTONE (A→D ladder matrix), 130dpi
- (a) inspected: s03-i1 — новый keystone-матрица 4 строки A/B/C/D × 3 кол.
- (b) findings: title (22pt) wraps 2 строки, «разработку сам» наезжает на
  italic-подзаголовок (FATAL для keystone); level-name рядом с бейджем
  переносится по слогам («автодопо лнение», «оркестрат ор»).
- (c) checklist: 5-sec FAIL (title collision), Matrix fill 100% PASS.
  verdict: continue.

## Iter 2 — s03, 140dpi
- (a) inspected: s03-i2.
- (b) changed: title 22→23pt короче, h↑; level-cell badge слева+имя справа.
- findings: title всё ещё 2 строки («разработке» wrap → collision); матрица
  читается, бейджи эскалируют Light→Mid→Deep корректно.
- (c) 5-sec FAIL (title). continue.

## Iter 3 — s03, 140dpi
- (a) inspected: s03-i3.
- (b) changed: title→«…насколько AI ведёт разработку сам» 26pt; matrix вниз.
- findings: «самостоятельности AI» — «AI» переносится на 2-ю строку,
  collision с подзаголовком сохраняется. continue.

## Iter 4 — s03, 150dpi
- (a) inspected: s03-i4.
- (b) changed: title→«…четыре уровня участия AI.» 27pt (≈52 chars).
- findings: title 1 строка, collision устранена. Level-name всё ещё
  wrap по слогам (name-cell ~0.94" — узко). continue.

## Iter 5 — s03, 150dpi
- (a) inspected: s03-i5.
- (b) changed: col_w[0] 1.78→2.12 (name-area ~1.26"), name 11pt 1-строка.
- findings: ВСЕ level-имена на 1 строку (автодополнение/мелкие задачи/
  кодинг-агент/оркестратор); badge+name читаются идеально; 4 строки чисты.
- (c) 5-sec PASS («4 уровня A→D, AI участвует всё больше вниз»). continue
  (критический глаз: gold недостаточно semantic — только в callout).

## Iter 6 — s03, 150dpi + 75dpi projector-sim — ACCEPT
- (a) inspected: s03-i6 (150dpi) + s03-proj (75dpi back-row sim).
- (b) changed: D-бейдж получил gold-кольцо (апекс автономии = несущий
  gold-акцент, semantic «максимум автономии = максимум риска»).
- (c) Schema §5.5 gate: Matrix fill 100% PASS · single-line headers PASS ·
  color coding semantic (badge escalation = ось автономии, gold ring =
  апекс) PASS · font ≥12pt (badge 26 / content 12 / header 13.5) PASS ·
  ≤2 строки/ячейка PASS · RU-unified PASS. 5-Second PASS. Projector
  75dpi PASS (badges A/B/C/D мгновенно сканируются с задних рядов).
  Cross-slide redundancy PASS (уникальный keystone). Iconography PASS
  (типографские бейджи, consistent). **verdict: ACCEPT** (6 iter).

## Iter 1 — s04 (ЦВ + рамка ответа + 5 якорей), 140dpi
- (a) inspected: s04-i1.
- (b) findings: title 2 строки, «делегируется?» наезжает на gold question
  box + target-иконку (тот же title-overflow класс). 5 якорей именами по
  смыслу читаются; 0 «возвращаемся N раз»/§/disclaimer-футера.
- (c) 5-sec FAIL (title collision). continue.

## Iter 2 — s04, 140dpi
- (a) inspected: s04-i2.
- (b) changed: title→«Центральный вопрос лекции.» 27pt w=9.5 (полная
  assertion = visual: сам gold question box); question box y↑.
- findings: title 1 строка, collision устранена; ЦВ доминирует; teal
  рамка ответа + 5 якорей + gold callout чисто. 0 leaks.
- (c) 5-sec PASS. continue (критический глаз: «обязателен» dot+label
  alignment тесноват).

## Iter 3 — s04, 140dpi + 75dpi projector — ACCEPT
- (a) inspected: s04-i3 + s04-proj.
- (b) changed: 5 якорей — верхняя teal-pill «человек обязателен» (общий
  семантический ярлык множества) + имя-по-смыслу ниже.
- (c) 5-Second PASS («ЦВ + ответ = уровень+конфиг+точка + 5 мест где
  человек обязателен»). Projector 75dpi PASS (ЦВ доминирует, pills
  читаются с задних рядов). Palette PASS (gold question box + gold
  callout; teal pills/frame; deep text). 0 §/(sNN)/«возвращаемся
  N раз»/course-scaffold-disclaimer (grep-verified). **ACCEPT** (3 iter).

## Iter 1 — s05 (слот переиспользован: цена ошибки↑автономия), 140dpi
- (a) inspected: s05-i1. Бывш. «единый паттерн» (свёрнут в s03) → новый
  контентный принцип blast-radius вдоль A→D.
- (b) findings: концепт работает (4 растущих плашки bottom-aligned), но
  D-столбец overflow за Ocean-контейнер; плашки — пустые боксы с мелким
  italic «радиус поражения» (слабая эскалация); scope-текст под баром
  тесно под A. 0 §/meta/«проекция Л3».
- (c) 5-sec partial (рост виден, но D ломает рамку). continue.

## Iter 2 — s05, 140dpi
- (a) inspected: s05-i2.
- (b) changed: пустые боксы → сплошные растущие blast-bars (цвет=badge,
  D=gold), scope-текст НА баре; «человек: ctrl» под баром.
- findings: эскалация A(light)→B(mid)→C(deep)→D(gold) читается сильно;
  но D-бар + gold-ring badge всё ещё чуть наезжают на label-ряд /
  верх контейнера.
- (c) 5-sec PASS (рост = message). continue (overflow fix).

## Iter 3 — s05, 150dpi + 75dpi projector
- (a) inspected: s05-i3 + s05-proj.
- (b) changed: heights A0.60/B1.12/C1.74/D2.42, base_y 4.98, box h 4.10
  — все бары внутри контейнера, D top 2.56 clear of label-ряда.
- findings: чисто и мощно; рост = главное сообщение; projector 75dpi
  читается отлично с задних рядов. Критический глаз: D «человек:» текст
  gold-on-white слабее остальных (MID).
- (c) 5-Second PASS, Projector PASS, bottom-aligned PASS. continue
  (контраст D-подписи).

## Iter 4 — s05, 150dpi — ACCEPT
- (a) inspected: s05-i4.
- (b) changed: D «человек:» подпись GOLD→DEEP (gold уже несёт bar+ring+
  callout; текстовый контраст важнее — palette gold ≥1× выполнено
  семантически D-баром/кольцом/callout).
- (c) Schema §5.5 gate: 5-Second PASS («радиус ошибки растёт A→D,
  человек контролирует крупнее/реже» = assertion) · Projector 75dpi PASS
  · color coding semantic (эскалация Light→Mid→Deep→Gold = ось
  автономии/цены) PASS · bottom-aligned PASS (§s11 counter-example
  соблюдён — бары по общей нижней границе, НЕ центрированы) · font
  ≥11pt PASS · 0 §/(sNN)/meta/«проекция Л3» grep-verified PASS ·
  iconography N/A (типографские бейджи) · cross-slide redundancy PASS
  (уникальный blast-radius визуал; матрица s29 — другая композиция).
  **ACCEPT** (4 iter). NOTE: s05 strict-in-eligible (Решение #100) —
  in_bucket-счётчик НЕ менял (designer scope); → methodology-critic
  Phase-7 re-QA.

## Iter 1–3 — s06/s07 light tone-fix (Решение #100), 140dpi+75dpi proj
- (a) inspected: s0607-cur (baseline), s0607-i1, s0607-proj.
- (b) baseline finding: оба несут residual scaffold-панель «Рамка уровня
  A/B: Что делает AI / Кто решает / Где обязателен / Типичный риск» —
  это бывш. s05 «единый паттерн» grid, теперь свёрнут в s03; подаёт
  уровень как слот методологии, не как новое. s07 title 2-строки.
- (c) changed:
  - s06: title→«Уровень A — автодополнение: безопасен только пока
    человек реально читает» (1 строка, спуск на 1-ю ступень);
    подзаголовок «Первая ступень лестницы…»; правая панель
    scaffold-«Рамка уровня A» → концентр. «Где уже стоит — и в чём
    ловушка» (где стоит/человек/ловушка/цена). Числа +56/+7-22/−19
    НЕ тронуты.
  - s07: title→«Уровень B: человек проверяет после, а не во время —
    первое делегирование» (1 строка); A↔B-таблица (различение) НЕ
    тронута; нижняя scaffold-«Рамка уровня B» → «Что эта граница
    меняет на практике» (3 concrete-следствия). Граница = различение,
    не оправдание классификации.
  - companion .md s06/s07 visible-mirror + frontmatter переписаны
    (убраны §1.1/«рамка §1.1» ссылки); speaker notes — связный
    студенческий текст, «применим рамку» → «где стоит/в чём ловушка»
    / «что меняет на практике».
  - deck.yaml s06/s07 assertion/learning_goal/visual обновлены.
- (c) checks: s06/s07 visible-leak grep = NONE (0 §/«Рамка уровня»/
  «не вводим нового»/«проекция»); 5-sec PASS (s06: «уровень A, 3
  эффекта, где стоит/ловушка»; s07: «граница A↔B, что меняется»);
  projector 75dpi PASS (mega-stat плашки s06 читаются с задних рядов —
  стиль РАБОТАЕТ, SYNTHESIS P1). Числа/факты идентичны baseline.
  **ACCEPT** (3 inspection passes).

## Block 2+3 — deck-wide tone-pass + SYNTHESIS-остаток verify (all 32)
- (a) inspected: contact-sheet (32 @25%) + per-slide s01/s08/s12/s13/s16/
  s17/s19/s20/s21/s22/s23/s25/s26/s28/s29 @95dpi + s29/s06 @75dpi proj.
- (b) FINAL grep (authoritative on lec-04.pptx, narrow+broad patterns):
  **0 visible-layer leaks across all 32** — 0 §-кодов / (sNN) / sNN /
  (Раздел N) / LO / [VFY]/[VERIFY]/[FACT-CHECK] / course-scaffold /
  «не вводим нового» / «проекция Л3» / «возвращаемся N раз» / «учебная
  карта» / «Рамка уровня» / «золото SOLID=» color-legend / meta.
- (c) SYNTHESIS P0/P1/P2 остаток — статус (большинство уже применено
  партиал-v2 commit ad61db5; SYNTHESIS «не применено» был устаревшим):
  - P0 [VFY]-strip: 0/32 ✓ (grep). · P1 §/sNN/LO-leak: 0/32 ✓
    (s03/s04/s05/s06 — мной; s07-s32 — партиал-v2).
  - P1 decor-charts s06/s08/s12/s13/s17 → mega-stat: ✓ visually
    (66% / 88,7%↔64,3% / 8,3↑12,3 trend-stats / −24/−20/+19) — стиль
    s01-плашек, РАБОТАЕТ.
  - P1 s16 confused-deputy notes-глосс: ✓ present (297-сл notes,
    «сбитого-с-толку посредника (confused-deputy)»).
  - P1 s19–s23 ритм: ✓ s22 = горизонтальный 4-step pipeline ломает
    монотон (s19 text/stat · s20 2-col · s21 bullets/inventory ·
    **s22 pipeline** · s23 2-canon/rule-grid — 5 разных layout).
  - P1 s25/s29 color-legend + s29 reformulation: ✓ s25 subtitle =
    content (не color-decode); s29 = owner-тезис «простое/повторяемое
    → AI; сложное/нестандартное → руки» доминантной gold-плашкой +
    3 оси крупно ≥14pt, полная 5×4 → глава. Projector 75dpi PASS.
  - P2 s01 sign-legend: ✓ «ждали ускорение −24 / думали ускорил −20 /
    по времени замедление +19» — однозначно.
  - P2 s26 Brooks: ✓ рус. «Брукс 1986», англ.-цитата → notes;
    доминанта «AI — усилитель, не исправитель… практики уточняются».
  - Owner s28 docs-as-code: ✓ оставлен; «для AI важнее, чем для
    человека» + честное «слабо подтверждено» (vendor-claim).
- speaker-notes wordcount edited (s01–s07): 216/206/281/213/235/281/207
  — все ∈ [150,300]. 0 «Лектору»/[пауза]/[слайд] во всех 32.
- side-effect guard: lec-01/02/03/07 reverted clean, 0 ~$*.pptx,
  только lec-04 в git status. 32 слайда (0 add/del). Палитра LOCKED.
- **DECK v3 ACCEPT** — Раздел-0 перестроен (s03 keystone / s04 ЦВ /
  s05 blast-radius / s06-s07 tone), сквозной tone-pass 0 leaks,
  SYNTHESIS P0/P1/P2 закрыты. Готово к re-QA оркестратором.

---

## v3.1 — tone-strip tail + LO7 s29 + counters (re-QA REVISE fix)

Re-QA 5 критиков → REVISE (2 независимо: сквозной tone-strip Решения #100
не доведён до 0 ВНЕ Раздела 0). Раздел 0 (s01–s07) подтверждён 5/5 — НЕ
тронут (кроме 2 фраз s04 + s01 P2 + s06 METR-dup + s03 chapter_ref sync).
Одна консолидированная fix-итерация, visual-loop ≥3 на изменённых.

### Iter 1 — v3.1 changed slides (150dpi snapshots/v31)
- (a) inspected: s01 s03 s04 s06 s08 s11 s13 s15 s17 s19 s21 s23 s29 s30 +
  authoritative grep pptx visible-layer.
- (b) changed:
  - **P1-A (rendered pptx, build_lec04.py):** s04 «сквозная через всю
    лекцию»→«Ответственность не делегируется», «— разберём каждое»
    убрано; s08/s13 footer «N-я точка возврата ЦВ» убрано; s17 footer
    «методологическая ловушка — в главе. Третья точка возврата» →
    content-only caveat; s23 footer «CVE-номер — в главе. Полный
    четвёртый возврат ЦВ» → content-only (CVE→глава per plan §7);
    s30 footer «Это payoff ЦВ» убрано. s29 «в материалах лекции»/«в
    главе» убрано (P1-B rebuild).
  - **P1-A source-hygiene (slide-files Body):** s24 таблица колонка
    «Точка»→«№», убраны (§1.4)/(§2.3)/(§3.4–§3.5)/(§4.4,§4.7) +
    «Это операциональный ответ … центрального вопроса» убрано;
    s12 Body footer [VFY-day-of] → content-only caveat.
  - **P1-B s29:** rebuild — доминанта-плашка + 5 КАНОНИЧЕСКИХ осей
    §6.1 ПО ИМЕНАМ компактной лентой (Незнакомость кода · Обратимость
    операции · Критичность/прод · Аудит/ответственность · Цена ошибки
    = gold-вето), «Повторяемость» убрана из матрицы → нижняя teal
    «не AI вовсе» плашка (её место — pre-фильтр). Полный 5-осевой
    аппарат — в speaker notes s29 (287 слов, в range, связный текст;
    полная сетка 5×4 — chapter §6.1 source of truth).
  - **P2:** s06 убран дубль (METR)/−19% (×2) → «выигрыш исчезает»
    (s06 partial→out, strict-in не затронут); s19 mutation/quality-gate
    defs → 3-словные (полн. → notes); s21 SAST/DAST/SCA/secret +
    CWE-каталог → термин+3-слова (разворот → notes 273 сл);
    s11 серый «режим отказа» italic убран (→ карты крупнее, читаемее);
    s15 серая «Рамка D» 4-Q strip → gold-callout D-итог (4-Q frame
    в notes 209 сл); s01 знаки −24/−20/+19 — zone-чипы
    ОЖИДАЛИ(grey)/ВЫШЛО(gold) + «быстрее»/«ДОЛЬШЕ».
  - **Счётчики:** deck-part2 ai_failure_judgment count 14→15, s05 в
    in_bucket_slides, убран из partial_out, share «15/32≈47%/54.5%
    мин»; deck.yaml s05 in_bucket:true; s03 chapter_ref «§0.2,§0.4»
    в slide-file (=deck.yaml).
- (c) checklist now pass: authoritative grep TOTAL=0 (2 независимых
  метода: python-pptx slide.shapes + raw-XML <a:t>, notesSlides
  excluded; regex self-tested HIT на 14 leak-классах). s24 Body-table
  0 §-кодов (рендер подтверждён). s29 5 осей по имени present, projector
  50% PASS, 5-sec PASS.

### Iter 2 — s01 geometry fix
- (a) inspected: s01 i1 — «+19% ДОЛЬШЕ» wrap-defect (узкий dirn-box).
- (b) changed: s01 row layout — chip 1.16 / label 1.72→2.02 / value
  3.78 w1.40 28pt / dirn 5.28 w1.45; «дольше» single-line.
- (c) pass: s01 i2 — «+19% дольше» single-line, zone-чипы читаемы,
  sign-ambiguity снят за 5 сек. PASS.

### Iter 3 — confirm stable + full grep
- (a) inspected: s01/s11/s24/s29 i2; full-pptx authoritative grep ×2.
- (b) changed: none (stable).
- (c) pass: TOTAL=0 confirmed both methods; s29 Schema §5.5 gate all
  PASS (axis ≥14pt, semantic gold-veto, fill 100%, RU-unified,
  projector 50% PASS, 5-sec PASS, Lucide consistent); notes carry
  23 return-connectives (narrative moved, not lost).
- **DECK v3.1 ACCEPT** — governing REVISE (tone-strip tail) закрыт;
  LO7 s29 5 осей; счётчики синхронны. Готово к re-QA delta.

### s03 callout scaffold-fix (approved PROPOSED #7)

Контекст: independent orchestrator grep по финальному pptx нашёл 1
оставшийся scaffold-register hit на видимом слое s03 (keystone) —
gold-callout «…линза, которой разберём каждый уровень дальше».
Тот же класс, что уже исправленный s04 «разберём каждое».
По Решению #100 (0 course-scaffold/«мы-лекторы»-meta на видимом слое)
устранён и на keystone. ЕДИНСТВЕННАЯ правка — текст этого callout;
композиция/матрица/бейджи/заголовок/подзаголовок НЕ тронуты.

- Правка: build_lec04.py L603-605 + companion s03 md L32 (visible
  mirror) синхронно. deck.yaml callout не содержит (L148 — frontmatter
  learning_goal, не scaffold-фраза, не тронут). Speaker-notes s03 L40
  НЕ тронут (notes исключены по брифу).
- Формулировка: «Чем ниже в таблице — тем больше решений у AI и тем
  меньше у человека. Эти три колонки — линза, как читать каждый
  уровень.» (lecturer-meta «которой разберём … дальше» удалён,
  смысл «3 колонки = аппарат чтения каждого уровня» сохранён).
- Rebuild OK — 32 слайда LOCKED (deck.yaml + deck-part2.yaml).

#### Iter 1 — s03 full-slide (150dpi)
- (a) inspected: callout fit в gold-плашке, overflow, keystone 5-сек,
  целостность матрицы/бейджей/заголовка.
- (b) changed: none (текст уже применён в build).
- (c) pass: текст в плашке, 2-строчный wrap чистый «уровень.» на
  стр.2, нет overflow/clip; матрица A→D + 3 колонки + цвет-эскалация
  бейджей не тронуты; 5-сек keystone = «4 уровня A→D; ниже = больше
  AI; 3 колонки = линза чтения» = assertion. НЕ деградировал.

#### Iter 2 — s03 callout crop
- (a) inspected: zoom-кроп плашки (projector / 50%-row5 readability).
- (b) changed: none.
- (c) pass: bold deep-blue на gold-tint, высокий контраст,
  читаемо на дистанции; bottom-padding в 0.90"-плашке достаточен.

#### Iter 3 — s03 hi-res full-width callout (200dpi)
- (a) inspected: финальный полный callout end-to-end (без crop-window
  artifact); правый край clear от rounded corner.
- (b) changed: none (stable).
- (c) pass: текст полный и в коробке, нет horiz/vert clip, нет bleed
  в матрицу; scaffold-фраза устранена, смысл сохранён.
- Authoritative re-grep финального pptx (видимый слой, 64 notesSlide
  исключены by design): расширенный 14-класс паттерн → **TOTAL=0**.
- side-effect guard: lec-01/02/03/07 восстановлены из origin/main
  (0 изменений), `~$*.pptx` удалены.
- **s03 callout scaffold-fix ACCEPT** — keystone НЕ деградировал.

---

## v3.2 — +3 suffix-ID дивайдера Р1/Р5/Р6 (Решение #101, owner GATE B)

Точечная итерация v3.1 → v3.2: добавлены 3 раздела-дивайдера для симметрии
7-секционного roadmap-бара. 32 существующих слайда заморожены (5/5 критиков
APPROVE) — контент НЕ тронут. Полная схема 6 дивайдеров на 6 контент-разделов:
s04a(Р1) · s10(Р2, есть) · s14(Р3, есть) · s18(Р4, есть) · s24a(Р5) · s28a(Р6).
Реализация — suffix-ID, cascade-safe: chapter [for-slide-sNN] s01–s32
финализирован GATE A, НЕ renumber. Шаблон — единый `build_section_divider`
(тот же, что s10/s14/s18): здесь_idx → roadmap gold-маркер автоматически.

### Iter 1 — s04a / s24a / s28a (110dpi, vs ref s10/s14/s18)
- (a) inspected: 3 новых дивайдера side-by-side против отрендеренных из того
  же deck эталонов s10(p11)/s14(p15)/s18(p19). Сверял: teal eyebrow «РАЗДЕЛ N»,
  gold-rule, гигантская soft-outline цифра справа, deep-blue подзаголовок,
  italic light-blue narrative bridge, 7-карточный roadmap, gold-маркер.
- (b) changed: none на этой итерации (диагностика).
- (c) pass: s24a (2-строчный titв) и s28a (1-строчный) — стилистически
  идентичны эталонам, roadmap gold корректен (Р5 / Р6). s04a — единственное
  отклонение: подзаголовок «Уровни A и B: автодополнение и мелкие задачи»
  переносится в 3 строки (эталоны 1–2 строки), bridge прижат к титулу →
  нарушена spacing-parity. roadmap Р1 корректен.

### Iter 2 — s04a fix (запятая)
- (a) inspected: s04a после замены «и мелкие задачи» → «, мелкие задачи».
- (b) changed: подзаголовок «Уровни A и B:\nавтодополнение, мелкие задачи»
  (build_lec04.py build_s04a + slide md sync).
- (c) pass: всё ещё 3 строки (~28 символов 2-й сегмент > порог ~25, как у
  эталонного s18 «тест, ревью, безопасность»=25 ✓). FAIL — parity не достигнут.

### Iter 3 — s04a fix (tight 2-строчная форма) + 150dpi final
- (a) inspected: s04a после «автодополнение и чат» (паритет длины с эталонным
  s14 «оркестратор и трекер»); затем все 3 новых @150dpi (#69-render-1:
  финальный accept всегда 150dpi) + parity-montage interleave new/ref.
- (b) changed: подзаголовок «Уровни A и B:\nавтодополнение и чат»
  (build_s04a + slide md sync). Канонич. полное имя раздела сохранено в
  deck.yaml `section:` и slide frontmatter (как s10: section=полное,
  subtitle=короткое).
- (c) pass ALL: s04a — чистые 2 строки, gap до bridge = как у эталонов,
  стилистически НЕОТЛИЧИМ. s24a/s28a @150dpi — без overflow/clip/bleed в
  цифру, bridge в своей зоне. Schema-readability (Timeline/Divider — n/a;
  это section_divider шаблон, паритет с принятыми s10/s14/s18 = критерий).
  5-сек тест PASS ×3: main message = «новый раздел + тема + позиция в
  roadmap» = assertion каждого. Projector 50%: titв+roadmap читаемы.
  Roadmap-маркер: s04a→Р1, s24a→Р5, s28a→Р6 (here_idx-arg, автоматический
  механизм как у существующих); s10/s14/s18 эталоны не сломаны (re-render
  из того же deck).

### Итог v3.2
- Iter на дивайдер: s04a=3, s24a=3, s28a=3.
- build_lec04.py: load_deck() expected 32→35 (base s01–s32 + suffix s04a
  после s04 / s24a после s24 / s28a после s28); base-numbering-неизменности
  assert добавлен; builders 32→35; рендер OK «35 slides».
- deck.yaml +s04a (Р1 регион), deck-part2.yaml +s24a/+s28a; totals 32→35;
  ai_failure_judgment count=15 НЕизменно, share 15/35≈43%, s04a/s24a/s28a
  в partial_out.
- chapter*.md UNMODIFIED; 32 slides/*.md контент не тронут.

---

## v3.3 — per-level тулы 2026, Решение #102

**Scope:** in-place добавление компактной врезки «Инструменты 2026» (Ocean
rounded-box, новый helper `tools_strip()`) на 4 per-level слайда. 35 LOCKED,
нумерация неизменна, keystone s03 + s04 + 30 прочих НЕ тронуты. chapter*.md
UNMODIFIED (book-first: контент блоков уже в chapter v1.2 §1.2/§1.3/§2.2/§3.2
[for-slide-sNN]).

**C-level выбор: s12** (не s11). Обоснование: (1) chapter-маркер C-тулов =
`[for-slide-s12]` (book-first якорь); (2) anti-hype-оговорка «SWE-bench как
доказательство автономии дыряв; бренд≠режим» тематически = s12 trust-слайд
(там и живёт SWE-bench Verified↔Pro); (3) s11 — process/cycle-визуал
(plan→act→check→iterate), врезка-блок туда конфликтует с замкнутым циклом,
на s12 (comparison) врезка ложится нативно под gold-критерий.

**tools_strip helper:** Ocean rounded-box, 2-колоночный внутр. layout —
левая = caption «Инструменты 2026» + chips (вендор-режим) + adoption-
НАПРАВЛЕНИЕ словами; правая = teal ⚠-band (anti-hype/границы, критический
тон, НЕ вендор-реклама; teal = «граница/осторожно» semantics как
teal_callout). 0 §/(sNN)/LO/[VFY]/scaffold + 0 волатильных долей/чисел/
«лидер»/benchmark на видимом слое (только направление словами; Решение
#100/#9 freshness). Точные [VFY-day-of]-числа НЕ выносились — см. open-risk
ниже (book-first: они в chapter v1.2 + research, видимый слой их не несёт).

### s06 (Уровень A) — pages 7
- Iter 1: caveat-band схлопнулся (баг helper: cb_h = h−0.92−0.12 ≈ 0.06);
  strip перекрывал footer.
- Iter 2: helper переписан на 2-кол layout; strip всё ещё впритык к gold-
  callout (5.76) и footer (7.04) — текст caveat переполнял band.
- Iter 3: сжата верхняя вёрстка (left-box lh 3.95→3.46, csh 1.04→0.90,
  right-box 2.55→2.34, gold-callout h 1.46→0.96); strip → y=5.02 h=1.42;
  3-row left-col (caption/chips/direction). Inspected p7: чисто.
- Iter 4: helper финализирован (chips own-row, auto-fit font, left_ratio
  param); re-render. PASS — strip между контентом и footer, 0 overlap,
  Ocean motif, существующие плашки +56/+7…22/выигрыш-исчезает не тронуты.
- Schema (n/a — assertion_visual+strip): 5-sec PASS (main message =
  «один инструмент, три эффекта, на легаси выигрыш исчезает» = assertion;
  strip явно вторичен). Projector 50% crop: chips/direction/⚠ читаемы.
- Iter на s06: 4. Verdict: ACCEPT.

### s07 (Уровень B) — page 8
- Iter 1-2: strip overlap с «что меняет»-box (gap 0.04).
- Iter 3: compare-table сжата (hh 0.50→0.46, rh 0.62→0.54), gold-callout
  4.28→3.92 h 0.78→0.74, «что меняет»-box 5.20→4.72 h 1.66→1.28;
  strip y=6.06. Inspected p8: чисто.
- Iter 4: helper-финализация re-render. PASS — 0 overflow, нет footer на
  s07 → strip до 7.40, compare-table контент не урезан (только spacing).
- 5-sec PASS (main = «B: человек проверяет после, не во время» = assertion).
  Projector crop: chips «ChatGPT-чат·Copilot Chat·Cursor Cmd-K» + ⚠ читаемы.
- Iter на s07: 4. Verdict: ACCEPT.

### s12 (Уровень C — выбран) — page 13
- Iter 1-2: strip впритык к footer; mega-числа под угрозой сжатия.
- Iter 3: верх сжат БЕЗ урезания mega-чисел (42pt 88,7/64,3 = 5-сек
  якорь сохранён); plate-h 1.30→1.14, gold-band 0.46→0.42, boxes
  ly 1.80→1.54 lh 3.28→3.14, gold-callout 5.02→4.80 h 0.76→0.74;
  strip y=5.62 h=1.36. Inspected p13: чисто.
- Iter 4: helper-финализация re-render. PASS — keystone trust-message
  (88,7%/−24пп/64,3%) интактен и доминирует; strip вторичен; footer
  слегка укорочен (дубль-define SWE-bench убран, смысл сохранён).
- Schema_matrix readability: fill OK, single-line, цвет-семантика
  (teal ⚠), font ≥12. 5-sec PASS (main = «88 знакомый vs 64 незнакомый,
  разрыв 24пп» = assertion). Projector crop: strip+footer читаемы.
- Iter на s12: 4. Verdict: ACCEPT.

### s15 (Уровень D) — page 16
- Iter 1-2: 4-я chip «Codex Cloud» клиппилась за левую колонку
  (4 тула > 3 у прочих; left_w слишком узок).
- Iter 3: chips → own-row + auto-fit-font + left_ratio=0.58; «Copilot
  coding agent»→«Copilot agent» (короче, режим тот же); амплифайеры
  сжаты 2.10→1.92, pipeline 1.40→1.30, gold-callout 5.28→4.88;
  strip y=5.84 h=1.36. Inspected p16: 4 chip в ряд, 0 clip.
- Iter 4: re-render. PASS — pipeline+амплифайеры+gold-callout+strip
  без overflow; контент усилителей не урезан (только высота).
- Schema_pipeline readability: RIGHT_ARROW сохранены, owner-аннотации
  не тронуты. 5-sec PASS (main = «тот же цикл + 2 усилителя риска» =
  assertion). Projector crop: 4 chip + ⚠ «Devin overclaim / 5 отказов
  + kill-switch» читаемы.
- Iter на s15: 4. Verdict: ACCEPT.

### Итог v3.3
- Iter на слайд: s06=4, s07=4, s12=4, s15=4 (≥3 min соблюдён;
  iter-3 находил проблемы → accept на iter-4).
- build_lec04.py: +helper `tools_strip()`; 4 builder-функции +tools_strip
  вызов + compressed spacing; рендер OK «35 slides», валидатор
  (35 + base-numbering-неизменность) НЕ сломан.
- Видимый слой 4 изменённых: 0 §/(sNN)/LO/[VFY]/scaffold (authoritative
  grep из rendered .pptx); 0 волатильных долей/% в strip-тексте (только
  «2026»-title, «№1»-качеств., «Devin 2.0»-версия, «5 отказов»-event-
  stable anti-hype-якорь — все owner-approved/non-volatile).
- chapter*.md UNMODIFIED; deck.yaml/deck-part2 chapter_ref s06/s07/s12/s15
  уже = §1.2/§1.3/§2.2/§3.1,§3.2 [for-slide-sNN] v1.2 (book-first
  satisfied) → не правились; keystone s03 + s04 + 30 прочих слайдов
  не тронуты; 35 LOCKED, нумерация неизменна.
- OPEN-RISK (REPORT, не self-fix): точные [VFY-day-of]-числа НЕ
  добавлены в speaker notes — конфликт с ENFORCED speaker-notes
  contract (s06 281w / s12 262w → +параграф пробил бы 300w-ceiling) +
  «существующий контент СОХРАНИТЬ» (notes = finalized v1.1). Числа
  живут в chapter v1.2 [for-slide-sNN] + research (book-first source).
  Видимый слой намеренно несёт только направление-словами (Решение
  #100/#9). Нужно owner-решение.

### micro-polish v3.3 (re-QA delta — methodology P2-1/P2-2 + fact-checker P2-1)
Скоуп: ТОЛЬКО 3 правки, остаётся v3.3, без renumber/новых слайдов.
- **#1 s06 chip:** `JetBrains AI` → `JetBrains AI Assistant` (каноничное
  полное имя; methodology P2-2). Только chip-строка L885 в `tools_strip`-
  вызове s06; s07/s12/s15 chips/direction/caveat НЕ тронуты (build word-
  diff подтверждён: изменена ровно одна строка-список chips).
- **#2 deck-part2.yaml:** `ai_failure_judgment.note` +1 предложение про
  тул-врезки s06/s07/s12/s15 (anti-hype/границы; s06/s07/s15 partial-
  upside, s12 reinforce in-bucket; count=15 неизменно). count /
  in_bucket_slides / partial_out / share_by_slides НЕ тронуты.
- **#3 slide-companions sync:** s06/s07/s12/s15 `## Body`-зеркало —
  добавлен блок «Инструменты 2026» (chips + adoption-направление словами
  + ⚠ anti-hype), текст дословно из rendered v3.3 pptx (binding =
  pptx). `## Speaker notes` companion-секции НЕ раздувались (frozen
  300w; Решение #100/RISK-2 — volatile-числа не в notes).
- **Visual-loop s06 chip-fit (2 iter):** iter-1 full-slide @150dpi —
  врезка рендерится чисто, 3 chips single-row, ⚠ band intact; iter-2
  zoom chip-row — «JetBrains AI Assistant» полностью внутри chip, без
  обрезки/wrap (auto-fit scaler `tools_strip` понизил шрифт на 1 шаг,
  абсорбировал +9 символов). PASS.
- Rebuild: `python3 build_lec04.py` → «35 slides», валидатор OK,
  нумерация неизменна; PDF пересобран (libreoffice rc=0).
- Verify: видимый слой s06 — 0 §/(sNN)/LO/[VFY]/Раздел/→sNN; 0
  волатильных тул-долей в врезке (digits в band = только «2026»-title
  + «№1»-quote; +56%/+7…22% — pre-existing v1.1 effect-size вне
  тул-band, GATE-B-approved, не Решение #102). Visible-text diff vs
  archive-v3.2: ровно pptx 7/8/13/16 (= deck s06/s07/s12/s15,
  ожидаемая v3.3-врезка); keystone s03 + s04 + 31 frozen — visible-
  text байт-идентичны v3.2. chapter*.md / speech.md НЕ тронуты
  designer'ом (diff = pre-session v1.2 WIP). Side-effect guard:
  lec-01/02/03/07 restored origin/main, lock-файлы 0, lec-05/06
  untracked-isolated.
- micro-polish: JetBrains AI Assistant + yaml-note + slide-companion sync

## v3.4 — s22a curl-slop #5 + rename (Решение #103, owner GATE C)

Брифом: +1 suffix-ID контент-слайд **s22a** (curl-slop #5, кейс
безопасности) между s22 (slopsquatting) и s23 (CamoLeak/секреты);
cascade-rename «мейнтейнер»→«сопровождающий» в видимом+notes слое deck;
35→**36** слайдов; ai_failure_judgment count 15→**16**. 35 frozen + keystone
s03 НЕ трогать (кроме rename-if-present). chapter*.md / speech.md /
glossary НЕ трогать designer'ом (book-first — chapter v1.3 финал, источник
§4.5).

### Подготовка
- Archive `rendered/lec-04.pptx`+`.pdf` → `rendered/archive-v3.3/` ДО правок.
- v3.3 baseline visible-text → `/tmp/v33_baseline.json` (35 слайдов) для
  byte-identity diff frozen.
- Side-effect guard: `git checkout origin/main -- lec-01/02/03/07` —
  pathspec не в origin/main на этом ref (lec-NN на другой базе),
  модификаций lec-01/02/03/07 в рабочем дереве нет (git diff --stat
  пуст) → guard moot, подтверждён clean. lock-файлы `~$*.pptx` 0.
  lec-05/06 untracked-isolated (не тронуты).

### Задача 2 — cascade-rename «мейнтейнер»→«сопровождающий»
- Греп всего deck-scope (slides/ + deck.yaml + deck-part2.yaml +
  build_lec04.py): ровно 1 вхождение — s01 speaker notes l.44
  («не студенты, а мейнтейнеры зрелых проектов»).
- Замена → «не студенты, а сопровождающие зрелых проектов»
  (именительный мн., граммат. падеж; согласовано с chapter-part2 l.87
  «сопровождающие зрелых репозиториев»).
- Post-rename греп `мейнтейнер|maintainer` в deck-scope: **exit 1
  (0 вхождений) — PASS**. speech.md l.43 «мейнтейнеры» вне deck-scope
  (book-first, speech-writer per Решение #103 порядок; брифом
  speech.md НЕ трогать) — НЕ правлено, REPORT не fix.

### Задача 1 — slide s22a (curl-slop #5)
- `slides/s22a-curl-slop.md`: frontmatter (id s22a, type case_study,
  `chapter_ref: "§4.5 [for-slide-s22a]"`, in_bucket true, references
  curl-slop-2026) + Body-зеркало + speaker notes. Стиль = failure-слайд
  как s21/s22 (кейс → асимметрия → системно → урок + не-AI альтернатива
  + критерий-footer).
- Derive 100% из chapter §4.5 (строки 200–209, маркер
  `[for-slide-s22a]`): 0 утверждений вне §4.5. Несущая ось — асимметрия
  стоимости (фейк ≈ секунды vs опровержение = часы → DDoS на внимание
  сопровождающих → supply-chain), урок (виновата архитектура процесса,
  не «AI»), не-AI альтернатива (приватное раскрытие GitHub Security
  Advisories · убрать junk-стимул · барьер воспроизводимого PoC на
  входе = машинный критерий, аналогия «тест как спецификация»),
  критерий «когда AI здесь опасен».
- Speaker notes: связный студенческий текст, **299 слов** (контракт
  150–300; матчит s22-эталон 299). `[FACT-CHECK: curl valid-rate <5%,
  ×8 объём, дата сворачивания]` ТОЛЬКО в notes. 0 forbidden lecturer-
  cues, 0 forbidden-англицизмов.
- Видимый слой: 0 §/(sNN)/LO/[VFY]/[FACT-CHECK]/scaffold + 0 точных
  волатильных чисел (×8/<5%/15%/576/43%/58%/1 февраля — нет). Только
  направление/асимметрия словами: «объём кратно вырос», «доля валидных
  рухнула», «секунды» vs «часы человека», «× 1000+».

### Cascade-safe build
- `build_lec04.py`: `build_s22a` вставлен после `build_s22`, перед
  `build_s23` в sequence; load_deck validator — expected += s22a после
  s22, totals assert 35→**36**, builders assert 35→**36**. s01–s32 +
  suffix s04a/s24a/s28a неизменны.
- `deck-part2.yaml`: entry s22a между s22/s23; totals.slides 35→**36**;
  slide_times_sum 77.9→80.9 + s22a 3.0 мин Р4b 11→14 (минутная
  пере-балансировка → methodology-critic re-confirm flag, designer не
  решает один); ai_failure_judgment count 15→**16**, s22a в
  in_bucket_slides (len 16), share «16/36 ≈ 44%», note + распределение
  (s21/s22/**s22a**/s23/s24-Р4) + fact_check_items s22a_curl_slop_rates.
- Rebuild: `python3 build_lec04.py` → «deck spec OK — 36 slides»,
  валидатор OK (totals 36, builders 36, base s01–s32 нумерация
  неизменна), «saved … 36 slides». PDF пересобран (libreoffice rc=0).

### Visual-loop s22a (4 итерации — failure-слайд, page 24)
- **iter1** `snapshots/v34/s22a-iter1-24.png`: context-band overflow
  (3-строчный italic в 0.66" → spill на asymmetry box); column body
  top-weighted; «× 1000+» faint. 5-сек: ось читается, но top шумит.
  FIX: context-band текст короче + h 0.66→0.74; asymmetry box y 1.74→
  1.80.
- **iter2** `…iter2`: context дышит (2 строки), ось — доминанта, teal
  band 1 блок чисто. Issues: LEFT/RIGHT body top-weighted (пусто снизу
  ~0.3"); «× 1000+» 11.5pt слабый; редундантен vs «секунды/часы».
  FIX: column body MIDDLE-anchor; «× 1000+» 13pt над стрелкой +
  «разрыв» под стрелкой = gold-ось-триплет; «секунды/часы» 15→16pt.
- **iter3** `…iter3`: column body вертикально центрирован, ось =
  3-частный gold-маркер (× 1000+ → стрелка → разрыв), LEFT/RIGHT
  visual mass сбалансирован (gold-сторона тяжелее = «дорогая/опасная»
  сторона highlighted, матчит assertion). 5-сек: PASS (message =
  assertion). Projector 50% (`/tmp/s22a-proj50.png`): headline-фразы
  читаемы из 5-го ряда — PASS. Critique: gold-callout (урок) = teal-band
  (системно) одинаковый вес — урок должен доминировать как финальный
  takeaway; «разрыв» 11pt LIGHT faint @50%.
- **iter4** `…iter4` (accept): gold lesson-callout 13.5→**14pt** (3
  строки, тяжелее teal-band — корректная финальная иерархия teal→gold);
  «разрыв» 11.5pt italic **GOLD** (завершает gold-ось-триплет, читаем
  @50%). Вертикальный ритм чист, 0 overflow, mass balanced.
  - 5-Second Test: PASS — message read = «фейк ≈ секунды → [× 1000+
    разрыв] → опровергнуть = часы человека; DDoS на внимание; виновата
    архитектура процесса, чинить процесс не «AI»» = assertion. MATCH.
  - Ocean motif: ocean_box на asymmetry-блоке. Palette LOCKED (DEEP/MID/
    LIGHT/TEAL/GOLD, 0 red/cream). Gold ≥1× (ось асимметрии + lesson-
    callout). Failure-стиль = s21/s22 (кейс→асимметрия→системно→урок+
    не-AI альт+критерий-footer). Iconography: triangle-alert-gold
    (Lucide, Ocean recolor) — semantic (предупреждение/риск).
  - Verdict: ACCEPT (4 iter, min-3 satisfied, found+fixed каждый раунд).
