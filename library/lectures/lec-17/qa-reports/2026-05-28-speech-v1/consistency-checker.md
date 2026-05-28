# Consistency Checker Report (Phase 10 triangle) — Лекция 17 (capstone)

**Date:** 2026-05-28 | **Mode:** full (chapter v3 multi-part ↔ slides v2 37sl ↔ speech v1.0) | **Branch:** issue-145-lec-17

## VERDICT: APPROVE-WITH-POLISH

Триангл chapter ↔ slides ↔ speech **в основном консистентен**. Speech-черновик высокого качества: все 37 фрагментов выровнены со слайдами и порядком deck.yaml, все v3-исправленные факты совпадают через 3 артефакта, geometry-канон 4 квадрантов идентичен, baseline-числа совпадают, терминология консистентна, тон чист. Найден **1 кластер geometry-drift** на точечных координатах L13/L10 (robotaxi / black-swan / Monarch), корень которого — **внутренняя противоречивость chapter §3.3 vs §3.2/§3.5**, каскадно проявившаяся по-разному в slide-тексте и speech. Это **2 P1 + 1 P1 cascade**, не P0: канон 4 квадрантов и rendered scatter корректны; расходятся словесные ярлыки точек. Полируется на Phase 11 синхронизацией к rendered scatter (= de-facto canon).

## Severity counts
- **P0 (factual contradiction / missing coverage):** 0
- **P1 (significant drift):** 3
- **P2 (minor inconsistency):** 3

---

## Speech ↔ slides alignment — PASS

- **37/37 фрагментов** speech (`## [sNN ...]`) присутствуют и **в строгом порядке** s01→s37, идентично списку id в `deck.yaml` и `slides_covered` в frontmatter speech. Orphan-ссылок на удалённые слайды нет (s38/s39/s40 — отсутствуют; s39b в chapter §5.5 — это chapter-internal маркер, не slide-ref; deck.yaml не содержит s39b).
- Каждый speech-фрагмент передаёт assertion соответствующего слайда. Проверено выборочно s02 (keystone), s12 (mapping), s22 (logistics trio), s31 (3 mega-pattern), s37 (closing) — speech говорит то, что на слайде.
- Section dividers (s03/s10/s18/s27) в speech — короткие вступления раздела, согласуются с deck.yaml `type: section_divider`.
- **Orphan reference scan:** speech не ссылается ни на один несуществующий слайд. `## chapter_ref` трейлеры слайдов (содержат §X.X / `chapter-part*.md` / в s22 — `L16`) **НЕ инжектятся** в speaker notes — подтверждено `rendered/inject_notes.py` (извлечение notes останавливается на следующем `## `, т.е. `## chapter_ref` отсекается). Эти коды — production-metadata, не leak в visible/notes. **OK.**

## Speech ↔ chapter — PASS

- Speech derived из chapter v3, не противоречит. Hook (s01), keystone (s02), 7 критериев (s04-s09), лестница (s11-s17), карта (s19-s26), 12 провалов (s28-s31), карточки (s32-s36), closing (s37) — все воспроизводят chapter-нарратив в сжатой устной форме.
- **Главный тезис курса идентичен дословно** во всех 3: «**Знать ИИ — значит знать его границы**» (speech L696, chapter-part4 §5.7 L256, slide s37).
- Speech не overclaim: тезис «AI работает в роли советника — зрелая, измеримая, окупающаяся; это не значит, что AI хуже» (speech s25) совпадает с chapter §3.6. Speech явно балансирует (s37 + резерв L730: «навык говорить нет питается из тех же знаний, что и навык говорить да»).
- «8-10 канонических кейсов» список в speech s37 (Zillow, Watson, CrowdStrike, Galactica, Klarna, Plenty, Cruise, Uber) **идентичен** chapter §5.7 (та же восьмёрка).

## Geometry canon через 3 артефакта — PASS (на уровне 4 квадрантов) / FAIL (на уровне точечных координат L13/L10)

**Канон 4 квадрантов — консистентен через chapter §0.3+§3.7, slide s02+s26, speech s02+s26:**
- upper-right = closed-loop success (high fit + high autonomy) ✓
- **upper-left = WARNING** (low fit + high autonomy, пустой/опасный) ✓
- lower-left = classical wins (low fit + low autonomy) ✓
- **lower-right = CAPPED** (high fit + low autonomy, regulatory ceiling, заполнен) ✓

Примеры-якоря квадрантов совпадают: медицина → нижний правый (capped) во всех 3; CrowdStrike/F-35/Cruise → верхний левый (warning) во всех 3; UPS ORION → нижний левый (classical) в chapter+speech. Rendered scatter (`scatter_coords.py`) подтверждает канон численно: медицина (0.70,0.30)=capped, AlphaFold (0.88,0.66)=ok-UR, Galactica (0.30,0.66)=fail-UL.

**FAIL — точечные координаты L13 (логистика) и L10 (Monarch) расходятся между артефактами** (см. D1-D3 ниже). Корень: chapter §3.3 даёт для robotaxi/black-swan координаты, противоречащие §3.2/§3.5 того же chapter; slide-текст и speech разрешили это противоречие в **разные стороны**.

## v3-исправленные факты через 3 артефакта — все PASS

| Факт | Chapter | Slides | Speech | Совпадает? |
|---|---|---|---|---|
| GM Cruise closure **10 дек 2024** (не 2023) | §0.1, §2.4, §4.1 «10 декабря 2024» | s22/s26 + speaker_notes | s14 L312 «в декабре двадцать четвёртого GM закрыл» | ✓ |
| Tesla tweet **13 апр 2018** (не July) | §4.5 «13 апреля 2018» | s29 «Tesla 2018» / s35 «Tesla 2018» | s29 L560 «апрель восемнадцатого» | ✓ |
| **MIT NANDA 95% ≠ McKinsey 5.5%** (разные measurements) | §3.2, §4.12 (таблица 4 источника), Q&A | s30 L44-45 + media-note L54 «РАЗНЫЕ измерения» / s35 | s30 L588 «это разные измерения, не одно число» | ✓ |
| Deepfake → **Arup CFO + colleagues video** $25M фев 2024 | §3.2, §4.8 «Arup … видео-конференция» | s29 L43 «дипфейк … Arup $25 млн в видео-конференции» | s29 L570 «Arup … видеоконференции … мультимодальная атака» | ✓ |
| Apple Card → **explainability, не bias** (DFS 2021 cleared) | §1.3 «Goldman cleared … lesson explainability» | s07 L37 «оправдан в намеренной дискриминации … explainability» | s07 L176 «урок не про предвзятость … про объяснимость» | ✓ |
| τ-bench → **Sierra** (Bret Taylor), CRMArena → Salesforce | §4.2 «Sierra τ-bench … Salesforce CRMArena отдельно» | (chapter-backup; не на слайдах детально) | (не в speech narrative; chapter-only) | ✓ (no conflict) |
| **Plenty $940M+ raised** (не loss) + Chapter 11 март 2025 | §0.1, §3.2, §4.x «$940M+ raised … Chapter 11 март 2025» | s24 L29 «$940 млн+ привлечено … Chapter 11, март 2025» | s24 L478 «привлёкшие больше 940 млн … банкротство в марте 25» | ✓ |
| **BCCRT** (не «Canadian») Air Canada | §4.8 «BCCRT … Moffatt v. Air Canada» | s29/s35 «Air Canada» (трибунал не назван — OK, сжатие) | (Air Canada не в speech s29 narrative — OK, сжатие) | ✓ (no conflict) |
| Yokogawa FKDPP — JSR field test 2022 | §1.2, §1.4, §3.2 «JSR 35-day 2022 … ENEOS 2023» | s14 «Yokogawa FKDPP» | s08 L190 «Yokogawa … в двадцать втором» / s14 L300 | ✓ |
| CrowdStrike $5+ млрд = **insurance estimate, не P&L** | §0.1, §1.2 «Parametrix … не CrowdStrike P&L» | s06 baseline / s26 «радиус 8,5 млн» | s06 L156 «ущерб пострадавшим компаниям — 5+ млрд» | ✓ |

**Все v3-факты консистентны.** Detail-нюансы (BCCRT-имя трибунала, τ-bench/Sierra) живут в chapter как Q&A-backup; slides/speech их корректно сжали без противоречий — это правильное book-first сжатие, не drift.

## Industry-refs (no L-codes) в slides + speech — PASS

- **Speech:** 0 L-кодов-лекций (L1-L16). Все `L0/L1/.../L5` в speech — это **уровни autonomy ladder** (легитимно). Подтверждено grep'ом: каждое вхождение `L[0-9]` — контекст лестницы автономии. Industry refs во всём speech — по индустрии+кейсу («разработка ПО», «логистика», «складская робототехника»), без номеров лекций.
- **Slides (visible + speaker_notes):** 0 L-кодов-лекций. Единственное вхождение `L16` — в `s22-map-batch3.md:81` внутри секции `## chapter_ref` (production-metadata-трейлер, НЕ инжектится в notes, НЕ в visible). Все прочие `L0-L5` — уровни autonomy ladder. **OK.**
- §X.X-коды и `chapter-part*.md`-рефы присутствуют только в `## chapter_ref` трейлерах + frontmatter `chapter_ref:` + `## media` brand-allowlists — все production-metadata, не visible/notes. Подтверждено inject_notes.py contract.

## Baseline mandate — PASS

Измеримые claims несут базу/counterfactual во всех 3, числа совпадают:
- **See & Spray 5M акров / ~900M US ag = 0.55%:** chapter §1.1 «5M из ≈900M = 0.55%» / speech L134 «пять миллионов из девятисот миллионов … полпроцента» / slide s15 «5 млн акров за 3 года». −50% гербицида с базой «≈1 фунт/акр → 0.5 фунта» в chapter+speech. ✓
- **Zillow $304M + ~2000/8000 (25%):** chapter §0.1 / speech L132 «около двух тысяч человек из восьми» / slide s05 «≈2 000 из ~8 000». ✓
- **Monarch 38% ≈53/~140 peak Q3 2024:** chapter §3.2/§4.1 / speech L432 «53 из ста сорока на пике» / slide s05+s24 «≈53 из ~140». ✓
- **Copilot 20M+/~28M GitHub devs + 46% кода:** chapter §1.2 / speech L144 «двадцать с лишним миллионов платных» / slide s06 «20+ млн (из ≈28 млн)». ✓
- **CrowdStrike 8.5M устройств / $5+ млрд:** все 3. ✓
- **Plenty $940M+ raised:** все 3. ✓

## Terminology / Russification — PASS

- Нет glossary.yaml (не сгенерирован после GATE A), но термины канона консистентны **без glossary** через все 3:
  - «применимость ИИ» (не «AI fit» в visible/speech: speech 0× латинское «AI fit», 24× «применимость»; slides 49× «применимость»).
  - «закрытая петля» / «открытая среда» — единообразно (speech 11× закрытая петля).
  - «человек в петле» (speech 8×, полностью по-русски) — slides используют «HITL» как established acronym в cheatsheet-карточках + s31, что приемлемо (компактный формат карточки, термин введён в курсе). Speech narrative — полная русская форма. Без drift по смыслу.
  - «лестница автономии L0→L5», «домен эксплуатации / ODD», «человек на петле / HOOL» — консистентны.
- Аудит-термины («canary/канарейка», «откат/rollback», «базовая линия/baseline») — speech использует русские формы, slides — смешанно с established-латиницей в карточках. Consistency по концепту сохранена.
- **Tone:** 0 вхождений «ИУ6/МГТУ» (универсальная audience выдержана), 0 «магическая пилюля/серебряная пуля/панацея», уважительная «вы»-форма во всём speech. ✓

## 12 провалов — PASS

Список из 12 канонических классов **идентичен** chapter §4.1-§4.12 ↔ slide s35 (cheatsheet, canonical card) ↔ s28-s30 (card-grids) ↔ speech s28-s30. Имена, источники, уроки, альтернативы совпадают:
1 open-world / 2 reliability compounding / 3 demo≠production / 4 HITL boring / 5 excessive automation / 6 Act без канарейки / 7 Galactica-class / 8 voice-video deepfake / 9 verbatim leak / 10 vendor lock-in / 11 slopsquatting / 12 pilot purgatory. Источники-кейсы совпадают (Zillow/Monarch/Cruise; Uber Tempe/F-35; Tesla/Boeing; CrowdStrike/Cloudflare; Getty/NYT; Climate FieldView/ALIS/Watson). 3 mega-pattern (s31) идентичны chapter §4.13 ↔ speech s31. ✓

## 7 критериев + лестница L0→L5 — PASS

- **7 критериев:** определения идентичны chapter §1 ↔ slide s33 (cheatsheet) ↔ s04 ↔ speech s04. Порядок (среда / данные / повторяемость / цена ошибки / эталон / объяснимость / экономика) и verdict-логика «один ✗ → STOP; ≥2 ⚠ → HITL» совпадают. ✓
- **Лестница L0→L5:** определения каждой ступени (L0 без автоматизации / L1 advisory / L2 supervised / L3 conditional ODD / L4 high HOOL / L5 full недостижим) идентичны chapter §2.1-§2.6 ↔ slide s11/s34 ↔ speech s11. Антипаттерны per-level (L1 Klarna / L2 Uber Tempe / L3 Cruise / L4 CrowdStrike / L5 LAWS / cross-level пропуск ступени) совпадают chapter §2.8 ↔ s16/s34 ↔ speech s16. Маппинг локальных шкал (таблица 2.7a прямые + 2.7b ортогональные: логистика=среда, кибербез=функции) идентичен chapter §2.7 ↔ s12 ↔ speech s12. ✓

---

## DISCREPANCIES

### D1 — robotaxi (Cruise/Waymo): квадрант расходится slide ↔ speech (корень — chapter internal)
**Severity:** P1
**Where:** chapter-part3 §3.3 pt2 + §3.2/§3.5 ⟷ slide s22 ⟷ speech s22
**Issue:** Координата городского робот-такси задана по-разному:
- chapter §3.3 точка 2: «**середина-правая**, с пометкой narrow ODD … L3-L4 narrow» (mid-right)
- chapter §3.2 L181 + §3.5 cluster: Cruise robotaxi → «**верхний левый** квадрант … зона предупреждения» (upper-left)
- slide s22 visible L32: «робот-такси (Waymo L3 / Cruise — провал, **верхний левый** — попытка автономии в открытой среде)» + rendered scatter `L13_taxi` (0.34, 0.70) = **upper-left, fail**
- speech s22 L444: «городское робот-такси: **середина справа**, узкий домен, L3 — Waymo получилось, Cruise нет» (mid-right)

То есть **slide + rendered scatter говорят upper-left (warning), а speech говорит mid-right.** Это derive из **внутренне противоречивого chapter** (§3.3 mid-right vs §3.5 upper-left).
**Recommendation:** Канон — rendered scatter `scatter_coords.py` (L13_taxi 0.34,0.70 = upper-left, fail), т.к. Cruise — failure-кейс, а зона провалов = верхний левый. **Fix speech s22** к «верхний левый» (или нюанс: «Waymo — узкий L3 ближе к центру-правому; Cruise попытался расшириться → ушёл в верхний левый, провал»). Дополнительно **поднять issue book-editor'у:** chapter §3.3 pt2 («середина-правая») рассинхронизирован с §3.2/§3.5 — chapter сам имеет drift, его надо привести к канону (§3.3 → upper-left для Cruise-failure, mid-right оставить только для Waymo-success как nuance). Book-first: chapter — source of truth, но здесь chapter сам ошибается внутри себя → требует фикса.

### D2 — black swan (Суэц/COVID): «вне плоскости» (chapter §3.3) vs «нижний левый» (slide+scatter) vs «верхний левый cluster» (chapter §3.5)
**Severity:** P1
**Where:** chapter-part3 §3.3 pt3 + §3.5 ⟷ slide s22 ⟷ rendered scatter ⟷ speech s22
**Issue:**
- chapter §3.3 точка 3: «фактически **вне плоскости** — это L0» + аннотация «out-of-distribution → AI не работает»
- chapter §3.5 cluster open-env: «L13 black swan (Suez, COVID)» включён в состав **верхне-левого** кластера провалов
- slide s22 visible L33: «чёрный лебедь (Суэц, COVID — фактически L0, **нижний левый**)» + rendered scatter `L13_swan` (0.20, 0.10) = **lower-left, near0**
- speech s22 L444: «чёрный лебедь … фактически **L0** — задача для людей» (квадрант не назван)

Три разных позиции для одной точки: «вне плоскости» / «нижний левый» / «в верхне-левом кластере».
**Recommendation:** Канон — rendered scatter (0.20,0.10 = нижний левый, near-origin), что концептуально верно: L0 black-swan = low fit + low autonomy = классика/человек = нижний левый. **Fix:** (1) chapter §3.5 ошибочно включает black-swan в **верхне-левый** open-env cluster — это противоречит rendered scatter; black-swan ≠ «попытка высокой автономии при низкой применимости» (это L0, низкая автономия). Убрать black-swan из §3.5 upper-left состава ИЛИ переформулировать как «L0 near-origin, не warning-zone». (2) chapter §3.3 «вне плоскости» примирить с «нижний левый near-origin». (3) speech s22 — добавить квадрант «нижний левый» для явности (опционально, P2). Поднять issue book-editor для §3.3+§3.5.

### D3 — Monarch: slide-текст «нижний правый» противоречит собственному rendered chart + канону + speech
**Severity:** P1
**Where:** slide s21 visible ⟷ s21 rendered scatter ⟷ chapter §3.2 ⟷ speech s21
**Issue:**
- slide s21 visible L35: «Агросектор … Monarch Tractor (открытое поле) **↓ нижний правый** с пометкой провала»
- но s21 **rendered chart** (`s21-batch2.png`, scatter_coords `L10_monarch` 0.27,0.74) = **верхний левый, fail**
- chapter §3.2 L155: «открытая среда (Monarch) — в **верхнем левом** с пометкой failure» (canon)
- chapter changelog v3 явно: «L10 Monarch нижний правый→**верхний левый** (warning)» (это был P0-fix v3)
- speech s21 L432: «Monarch … падает в **верхний левый**, в зону провала» (canon)

То есть **slide s21 visible-текст — единственный outlier**: говорит «нижний правый», тогда как его собственный rendered chart, chapter (post-v3-fix), и speech все говорят «верхний левый». Нижний правый = CAPPED success quadrant — геометрически **противоположная** зона для failure-кейса. Это **stale label**, не отловленный при v3 P0-fix (chapter поправили, slide-текст s21 — нет).
**Recommendation:** **Fix slide s21 visible L35**: «нижний правый» → «**верхний левый** с пометкой провала» (согласовать с rendered chart + chapter §3.2 + speech). Это чистый slide-fix (chapter и speech уже корректны), book-first не нарушается. P1, но близко к P0 (прямое противоречие текста ярлыку на keystone-оси + противоречие собственному chart слайда).

---

## P2 issues (minor)

- **P2-1 — speech frontmatter word-count mismatch:** `target_words: ~6200` / `wpm_max: 95`, но фактический объём speech = **7471 слов**. При 75 мин и 95 wpm-cap → ~7125 слов max; 7471 слегка превышает. Cross-artifact это не drift (chapter/slides не зависят), но **timing-риск**: при 95 wpm 7471 слов ≈ 78.6 мин > 75 мин target. Рекомендация Phase 11: либо обновить frontmatter `target_words` к фактическому, либо trim ~300-600 слов (резервные блоки s37 + s05/s06 наиболее plотные). Не блокирует.
- **P2-2 — glossary.yaml отсутствует:** после GATE A не сгенерирован `glossary.yaml`. Терминология де-факто консистентна и без него (проверено grep'ом), но для downstream lock рекомендуется создать (canonical: применимость ИИ / закрытая петля / человек в петле / лестница автономии L0→L5 / домен эксплуатации). Это process-gap, не content-drift.
- **P2-3 — black-swan квадрант в speech s22 не назван** (только «L0»), тогда как slide называет «нижний левый». Не противоречие (L0 ⊂ нижний левый), но добавление квадранта в speech улучшило бы verbal↔visual alignment. Опционально.

---

## Coverage parity — PASS

- Все 8 LO покрыты в slides (LO1 s01/s02, LO2 s04-s09+s33, LO3 s11-s17+s20-s26+s36, LO4 s27-s31+s35, LO5 s11-s17+s34, LO6 s32-s36, LO7 s37, LO8 s19+s37) и отражены в speech-фрагментах.
- Все assertion'ы слайдов имеют обоснование в chapter (через `chapter_ref` mapping, проверено — 37/37 ведут на существующие §).
- Speech не упоминает фактов вне chapter (выборочная проверка: все кейсы speech присутствуют в chapter v3).
- Failure-share (strict-in) parity в speech: failure-кейсы плотно представлены (Cruise×10, CrowdStrike×10, Zillow×6, Galactica×6, Klarna×4, Monarch×4, F-35×4, Plenty×2, Watson×2, Epic Sepsis×2, + 12-провалов раздел s28-s31 + 7-критериев раздел = диагностика «когда НЕ применять»). Capstone ~33% strict-in выдержан и в speech-артефакте. ✓

---

## Топ-фиксы для Phase 11 (per artifact)

**Slides (наименьший impact — fix здесь по book-first):**
1. **s21 visible L35** — Monarch «нижний правый» → «верхний левый» (D3, P1, согласовать с собственным rendered chart). **Highest priority — чистый slide-only fix.**

**Speech:**
2. **s22 narrative L444** — robotaxi «середина справа» → согласовать с rendered scatter «верхний левый» для Cruise-failure (D1, P1); опционально добавить квадрант black-swan «нижний левый» (P2-3).
3. Рассмотреть trim ~300-600 слов / обновить frontmatter target_words (P2-1, timing).

**Chapter (требует book-editor — chapter имеет собственный internal drift):**
4. **§3.3 pt2 (robotaxi) + §3.5 cluster** — привести Cruise-robotaxi к канону «верхний левый» (сейчас §3.3 «середина-правая» ↔ §3.5 «верхний левый» внутренне противоречат) (D1).
5. **§3.3 pt3 + §3.5 (black swan)** — примирить «вне плоскости» / «нижний левый near-origin»; убрать/переформулировать включение black-swan в **верхне-левый** open-env cluster §3.5 (концептуально black-swan = L0 нижний левый, не warning upper-left) (D2).
6. Сгенерировать `glossary.yaml` (P2-2, lock terminology для будущих правок).

**De-facto canon reference для всех geometry-фиксов:** `rendered/scatter_coords.py` (Monarch 0.27/0.74=UL, robotaxi 0.34/0.70=UL, black-swan 0.20/0.10=LL) — он рендерится в PNG, физически встроенные в s20-s26, и геометрически корректен. Все словесные ярлыки точек синхронизировать к нему.

---

## Итог

3-artifact triangle **APPROVE-WITH-POLISH**. Нет P0, нет factual contradictions по фактам/числам/тезисам, нет missing coverage, нет orphan-refs, нет L-code leak, нет tone-drift. Единственный класс проблем — **точечная geometry drift L13/L10** (3×P1), корень которой — **внутренняя противоречивость chapter §3.3 vs §3.2/§3.5** (chapter сам не self-consistent на 3 точках), каскадировавшая по-разному в slide-текст vs speech. Канон 4 квадрантов и rendered scatter корректны — фиксы механические (синхронизация ярлыков к rendered scatter + чистка chapter §3.3/§3.5). 3×P1 < 5 → **не REVISE; APPROVE-WITH-POLISH** с обязательной отработкой D1-D3 + book-editor issue на chapter §3.3/§3.5 self-consistency на Phase 11.
