# Presentation Critic Report — Lec-17 Slides v1
**Date:** 2026-05-28 | **Verdict:** REJECT

> VERDICT: REJECT
>
> Причина: 1 P0 (keystone-противоречие осей/квадрантов, несущая ось всего capstone)
> + 5 P1. По правилу шкалы любой P0 → REJECT; ≥5 P1 независимо → REVISE.
> P0 здесь не «polish» — он ломает главный артефакт лекции (2D-карту), на котором
> держатся Разделы 0 и 3 (s03, s22-s28, s38).

---

## Summary

- Всего слайдов: 40 (все отрендерены, 110dpi snapshots, просмотрены визуально через vision)
- **P0 issues (блокеры): 1**
- **P1 issues (важные): 5**
- **P2 issues (косметика): 8**

Общая оценка: deck **сильный по контенту и методике** — отличная failure/judgment-насыщенность
(s08-s12, s19, s26, s30-s33, s37 — provals + уроки + альтернативы), книжно-выверенные baseline'ы
(s08/s09/s32 inline denominators), чистые section dividers без timing, дедикейтед Q&A (s39),
**настоящий** hero на s40 (ESO VLT control room, Tier 2 Wikimedia, ≥45% area, attribution
видна). Card-grids (s19/s30/s31/s32/s33) сбалансированы и читаемы. Cheat-sheet previews
(s35/s36/s37) — полные таблицы, читаемы на slide-scale.

**Но** несущая концептуальная ось capstone (2D-карта) имеет внутреннее геометрическое
противоречие в подписях квадрантов, которое тиражируется через весь Раздел 3 и на master
poster s38. Это **структурный** дефект, не косметика. Плюс 5 P1, частично подтверждённых
peer-агентами (student-simulator независимо нашёл s34-placeholder + roadmap-bar на hero).

---

## Compliance checks (pass/fail)

| Check | Status | Заметка |
|---|---|---|
| Schema readability §5.5 (scatter/quadrant) | **PARTIAL FAIL** | оси подписаны, точки contained; НО M1/M2 цвета неразличимы (P1-1) + cluster slides без highlight (P1-2) + keystone quadrant semantics broken (P0) |
| Master scatter coordinate consistency | **PASS (coords)** / **FAIL (semantics)** | координаты точек идентичны s01/s22/s23/s24/s38 (нет drift); прогрессивный reveal 4→8→18 логичен; НО точки не попадают в нарративно назначенные квадранты (P0) |
| Hero s01 (clean iconic scatter, ≥40%, foreshadow) | **PASS с оговоркой** | real rendered scatter, foreshadows keystone, ≥40% area; НО roadmap-bar сверху конкурирует (P1-5) + scatter в rounded box с большими белыми полями (~40%, на грани) |
| Hero s40 (real ESO photo, ≥40%, overlay, attribution) | **PASS** | настоящее фото оператора VLT, ≥45% area, gold overlay «Знать ИИ — значит знать его границы», attribution «ESO · CC BY 4.0» видна. НЕ mock. Образцовый closing hero |
| Card-grids s19/s30/s31/s32 (4 cards, balanced, no overflow) | **PASS** | карточки сбалансированы по высоте, читаемы, gold-highlight семантичен |
| Cheat-sheet previews s35/s36/s37 readable | **PASS** | таблицы 7×4 / 6×5 / 12×3 полностью заполнены и читаемы на slide-scale; QR-placeholder (серый бокс) — допустимо для v1 |
| Cheat-sheet overview s34 thumbnails | **FAIL** | 4 пустых прямоугольника «A4/A4/A4/A1» — выглядит недоделанным (P1-4) |
| Ocean palette + Gold ≥1×/слайд + rounded box motif | **PASS** | палитра выдержана, gold-акцент на каждом слайде, motif последователен |
| Section dividers s06/s13/s21/s29 (смысл + tag, БЕЗ минут) | **PASS** | все 4 чистые, tag-row без timing, roadmap-bar current=gold |
| Lec-N-1 pattern (lecture-map / dividers / Q&A / roadmap только на dividers+cover) | **PASS** | s02 lecture-map присутствует, 4 section dividers + s34 overview-as-intro, s39 dedicated Q&A, roadmap-bar только на cover+dividers (НЕ на content slides) |
| No scaffold/timing/methodology в visible body | **PASS** | 0 timing на dividers/cover/Q&A; 0 LO codes; 0 §refs; 0 «методическ»/«Лектору» в visible |
| No scaffold в speaker_notes | **FAIL** | «strict-in» 1× в s29 speaker_notes (P1-3) — подтверждён известный flag |
| Deep latin scan (visible PPTX) | **PASS с оговоркой** | 160 unique, но ~95% = brand/case names (CrowdStrike, See & Spray, Zillow, Monarch, Galactica, AlphaFold...) + glossed acronyms (ODD/HITL/LLM/RAG/LAWS) + course-canonical level names. Genuine anglicisms — P2 cluster, не P0/P1 |
| Baseline/counterfactual coverage | **PASS** | measurable claims несут denominators (CrowdStrike 8,5 млн; See & Spray 5 млн из ≈900 млн = 0,55%; Zillow ≈2 000 из ~8 000; Monarch ≈53 из ~140; MIT 95% vs McKinsey 5,5% явно «РАЗНЫЕ измерения») |

---

## P0 issues

### P0-1 — Keystone quadrant semantics geometrically broken (s03 → s22-s28 → s38)
**Severity:** P0 (несущая ось capstone; ломает Раздел 0 + весь Раздел 3)
**Slides:** s03 (определение), s22/s23/s24/s25/s26/s27 (нарратив кластеров), **s28** (наиболее остро), s38 (poster)

**Issue (концептуальный, подтверждён чтением source s03 + s28):**
Keystone определяет оси (s03 source):
- X (горизонталь): слева = «детерминированный non-AI» (низкая применимость), справа = «полный AI» (высокая применимость)
- Y (вертикаль): снизу = L0 (низкая автономия), сверху = L5 (высокая автономия)

Но подпись квадранта **противоречит** этой геометрии:
- s03 + s28 называют **«нижний правый»** квадрант = «**низкая применимость × высокая автономия**».
- Геометрически: нижний-правый = высокий-X (**высокая** применимость) × низкий-Y (**низкая** автономия). Это ПРОТИВОПОЛОЖНОСТЬ подписи.
- «Низкая применимость × высокая автономия» геометрически = **верхний-ЛЕВЫЙ** угол. Но верхний-левый отдельно подписан как «AI работает, автономия капнута регулятором».

То есть семантика **верхнего-левого и нижнего-правого квадрантов перепутана местами**. «Зона катастроф» (low fit × high autonomy) должна быть вверху-слева; «капнутая регулятором / advisory» (high fit × low autonomy — самое безопасное сочетание, которое сами speaker_notes s28 называют «приемлемое решение») должна быть внизу-справа.

**Visual evidence:**
- **s28 rendered:** заголовок «Пустой нижне-правый квадрант» + подсвеченный gold-dashed бокс в нижне-правой области, но **в боксе ЛЕЖАТ ~6 точек** (робот-такси, несколько teal/blue, Galactica). Квадрант, объявленный «пустым», фактически непустой. Прямое визуальное противоречие assertion.
- **s38 master poster:** нижне-правая зона залита gold/orange (warning), и это **самая населённая зона** карты (робот-такси, L9 авиа, L14 кибербез, L7 медицина, Galactica, Monarch, L11, L6, L16). Прямо противоречит «нижний правый — пустой и опасный».
- **s22 assertion:** «регулируемая медицина — наверху-слева», но на карте L7 медицина стоит в центре-справа (mid-fit, low-mid autonomy), НЕ вверху-слева. Точка не попадает в нарративно назначенный квадрант.
- **s27 (cluster high-stakes «верхний левый»):** перечисляет медицину/авиакосмос, но на reused scatter эти точки в центре, не вверху-слева.

**Recommendation (для orchestrator + book-editor, НЕ designer самостоятельно):**
Это chapter-level concept fix, не render-fix. Варианты:
1. **Поменять местами семантику** верхнего-левого и нижнего-правого квадрантов в s03 + s28 source (catastrophe-zone → upper-left; regulated/capped → lower-right) и переразместить точки так, чтобы они попадали в свои квадранты. Cascade: s03, s22-s28, s38, и проверить chapter §0.3/§3.7.
2. **ИЛИ** переопределить, что именно warning-зона (если задумана как «high autonomy push без applicability») — и тогда исправить axis-стрелки/подписи так, чтобы геометрия совпала с нарративом.
3. Любой вариант требует, чтобы «empty/dangerous» квадрант был **визуально пуст** на s28 и s38 (сейчас он самый полный).

**Почему P0, а не P1:** это несущий артефакт capstone, предъявленный как keystone (s03) ДО первого погружения, и тиражируемый через 7 слайдов Раздела 3 + master poster. Студент, прослеживающий «низкая применимость + высокая автономия» по подписям осей, укажет на верхний-левый угол — и обнаружит, что слайд подсвечивает нижний-правый. Это разрушает доверие к главному инструменту лекции.

---

## P1 issues

### P1-1 — Module colors M1/M2 перцептивно неразличимы на scatter-слайдах
**Severity:** P1 (schema readability — теряется измерение «модуль курса»)
**Slides:** s01, s22, s23, s24, s38 (везде, где master scatter)
**Issue:** deck.yaml LOCKED цветовое кодирование M1 `#065A82` (Ocean blue) / M2 `#028090` (Teal) / M3 `#F0AB00` (Gold). M3 (gold) различим отлично. Но M1 и M2 на render читаются как **один и тот же тёмный сине-бирюзовый** — на s24/s38 я не могу отличить L8 креатив (M1) от L9/L11/L12 (M2) по цвету. Легенда заявляет 3 цвета, но визуально работают 2 (тёмный + gold).
**Visual evidence:** s24 legend «Модуль 1 / Модуль 2 / Модуль 3» — первые два квадратика почти идентичны; точки на поле неразличимы между M1/M2. iteration-log claims «iter2 fix → M1 blue / M2 teal distinct», но визуально это не достигнуто.
**Recommendation:** увеличить контраст между M1 и M2 — либо сдвинуть M2 к более светлому/зелёному тону, либо различать формой/обводкой (M1 filled circle / M2 filled square), сохранив gold для M3. Проверить на 50% zoom.

### P1-2 — Cluster slides s25/s26/s27 переиспользуют master scatter без per-cluster highlight + caption-vs-position mismatch
**Severity:** P1 (schema readability — known flag #12b подтверждён)
**Slides:** s25 (closed-loop), s26 (open-env), s27 (high-stakes)
**Issue:** все три используют ОДИН и тот же full scatter PNG (s24-batch3-full) с текстовой подписью квадранта внизу («верхний правый квадрант» / «нижний правый — зона предупреждения» / «верхний левый — регуляторно капнуто»). **Нет визуального highlight** обсуждаемого квадранта (нет shaded zone / bounding box на самом поле — в отличие от s28, где зона залита). Глаз не направлен к WHERE кластера. Хуже: подписи называют corner-квадранты, но фактические члены кластера (перечислены в боковой панели) на reused карте лежат в центре/по диагонали, не в названных углах (см. P0-1). Zone-label текста недостаточно.
**Visual evidence:** s27 caption «верхний левый квадрант — регуляторно капнуто» + члены Медицина/Авиакосмос, но на карте эти точки в центре-справа.
**Recommendation:** добавить per-cluster shaded/bounded зону на каждом из s25/s26/s27 (как сделано на s28) — НО только ПОСЛЕ исправления P0-1, иначе highlight обнажит mismatch. Альтернатива: переформулировать caption под «диагональную полосу», если переразмещение точек невозможно.

### P1-3 — «strict-in» leak в s29 speaker_notes
**Severity:** P1 (scaffold leak — internal methodology term)
**Slide:** s29 (section divider 4)
**Issue:** подтверждён known flag (a). Rendered PPTX s29 NOTES содержит «…это самое концентрированное **strict-in** содержание всей лекции». Это внутренний методологический термин (метрика failure-share из CLAUDE.md), не student-facing. Visible body s29 чистый (iter3 убрал из s30 footer, но s29 пропустили). Источник: `slides/s29-*.md` `## media` блок («Strict-in ядро лекции») + `## speaker_notes` (стр. 51).
**Visual evidence:** независимый grep по rendered pptx notes — единственный hit во всём deck.
**Recommendation:** убрать «strict-in» из s29 speaker_notes (заменить на «самое концентрированное содержание про границы применимости») + из `## media` блока source. Это правка source markdown (designer не редактирует source — orchestrator routes to book-editor/source owner).

### P1-4 — s34 cheat-sheet overview: пустые placeholder-thumbnails выглядят недоделанными
**Severity:** P1 (выглядит как недорисованный слайд)
**Slide:** s34
**Issue:** 4 карточки-превью содержат пустые белые прямоугольники с серой надписью «A4 / A4 / A4 / A1» — без мини-контента карточек. Для capstone, где cheat-sheets = главный takeaway, это читается как «слайд не дорисовали». Подтверждено независимо student-simulator (P1-1 в их отчёте: «я подумал — а где сами карточки?»).
**Visual evidence:** s34 — 4 blank rectangles с format-labels внутри.
**Recommendation:** заменить пустые рамки на уменьшенные мини-превью реальных таблиц из s35/s36/s37/s38 (downscaled screenshot-thumb), чтобы overview показывал, ЧТО студент получит.

### P1-5 — Roadmap-bar на s01 (hero cover) конкурирует с hero-визуалом
**Severity:** P1 (Lec-N-1 pattern + hero composition)
**Slide:** s01
**Issue:** сверху s01 прибит полный навигационный бар «1.Критерии / 2.Лестница / 3.Карта 16 / 4.Провалы / 5.Карточки». По правилу курса roadmap-bar допустим на cover — формально не нарушение. Но s01 — это **hero**, и бар съедает верхнюю полосу, отвлекая от вау-карты (scatter foreshadow keystone). Hero должен сначала дать чистую карту. Подтверждено независимо student-simulator (P1-3).
**Visual evidence:** s01 — навбар занимает верхние ~7% над subtitle/title/scatter; scatter при этом в rounded box с большими белыми полями (эффективная площадь карты ~40%, на грани требования).
**Recommendation:** убрать roadmap-bar с s01 (hero) — оставить только на dividers (бар появится на s06). Дополнительно: увеличить scatter внутри rounded box (сократить белые поля), чтобы карта занимала ближе к 50% area и читалась как hero.

---

## P2 issues (косметика)

- **P2-1 — Anglicism cluster в visible body.** Не P0/P1 (большинство — brand/case/acronym), но накопительно для RU-аудитории МГТУ ИУ6: «CAPSTONE» (s01 subtitle → «итоговая»), «маппинг/маппятся» (s13/s15 ×4 → «отображение/соответствие»), «фрод» (s08/s16/s17/s22 → «мошенничество»), «скоринг» (s16 → «оценка»), «чек-лист» (s06/s34 → «контрольный список»), «в проде» (s14 pill → «в эксплуатации»), «бенчмарк» (s30 → «эталонный тест»), «алертом» (s19/s30/s37 → «оповещением»), «датасеты» (s32 → «наборы данных»), «коммита» (s33 → «фиксации»), «тест-сете» (s20), «репозитории» (s34/s35). Рекомендация: пройтись Russification-таблицей; brand/case/acronym оставить.
- **P2-2 — Level-names в английском.** «Advisory / Supervised / Conditional / High / Full» на s14/s15/s16/s17/s36 — course-canonical level names с RU-глоссами в скобках. Конвенция defensible (показывает верность нотации каждой лекции), но для RU capstone можно усилить русскую подачу. Borderline P2.
- **P2-3 — Gold pill «частый в проде» перекрывает текст L1 на s14.** Pill наезжает на описание L1 «Человек решает всегда» — слово «всегда» частично закрыто. Сдвинуть pill вправо/вверх.
- **P2-4 — «non-AI» в axis label.** «детерминированный non-AI» на всех scatter-осях → «детерминированный не-AI» (дефис, как в speaker_notes).
- **P2-5 — s12 «20 минут» / «15-20 минут» в visible.** Это content (длительность диагностической процедуры в assertion), НЕ lecture pacing — допустимо per iteration-log. Но на грани с no-timing rule; если возможно, переформулировать без минут («за один проход» / «быстро»).
- **P2-6 — QR-placeholder серый бокс** на s35/s37 — приемлемо для v1, но пометить как known-gap (заменить реальным QR при финализации PDF).
- **P2-7 — «HOOL» / «HITL»** без inline-расшифровки на s19/s36/s37 (есть на других слайдах) — добавить gloss при первом появлении в Разделе 2.
- **P2-8 — s01 M1/M2 легенда** мелкая в верхнем-левом углу scatter — увеличить если scatter масштабируется (см. P1-5).

---

## Per-slide visual notes (s01-s40 brief)

- **s01** hero scatter — real rendered data-viz, foreshadows keystone; ⚠ roadmap-bar конкурирует (P1-5), M1/M2 неразличимы (P1-1), «CAPSTONE» (P2).
- **s02** lecture-map 4×4 — отлично, модули различимы на card-scale, без roadmap-bar. PASS.
- **s03** keystone quadrant — axis labels inside, 4 quadrant, side-panel «Две оси», gold callout foreshadow s28; ⚠ semantics broken (P0-1).
- **s04** central question — сильный, gold-emphasis, L1→L17 pills, 3 numbered cards, drift glossed. PASS.
- **s05** roadmap 5 tag-cards — без минут, gold на Раздел 4 семантичен. PASS.
- **s06** divider 1 — чистый, tag без минут. PASS.
- **s07** 7-criteria list — иконки Lucide, gold на #4 (cost). Читаем на full-res. PASS.
- **s08** comparison closed/open — two-column, baseline'ы inline (5 млн из ≈900 млн и т.д.). PASS.
- **s09** blast-radius table — CrowdStrike gold row, baseline strong, 5-sec test работает. PASS.
- **s10** Pearl 3-level stack + Apple Card reframed (explainability), gold takeaway. PASS.
- **s11** criterion 7 + Q1/Q3 quadrant tools (classics win, «AI не нужен» gold). PASS.
- **s12** worked example вода — 7-row checklist ✓/⚠/✗, row 4 gold, verdict panel. PASS; ⚠ «20 минут» (P2-5).
- **s13** divider 2 — чистый; ⚠ «маппинг» (P2-1).
- **s14** ladder L0→L5 layered, bottom-aligned, L5 grey; ⚠ gold pill перекрывает L1 текст (P2-3), level-names EN (P2-2).
- **s15** mapping matrix — fill ~92%, Table A + Врезка B, footer callout; ⚠ «маппинг» ×много (P2-1), EN level labels (P2-2).
- **s16** L1 advisory flow + 5 example cards (Project Maven в ряду — iter2 fix OK). PASS.
- **s17** L2/L3 panels + ODD callout. PASS; ⚠ «фрод» (P2).
- **s18** L4 examples + L5 5-blocker list + Tesla NHTSA L2 callout. PASS (сильный limitation-контент).
- **s19** antipatterns card-grid 6 cards, heights consistent. PASS; ⚠ «overreach»/«HOOL»/«алертом» (P2).
- **s20** worked example экзамены — «потолок=L1» gold, Анализ+Вердикт panels. PASS.
- **s21** divider 3 — чистый, tag без минут. PASS.
- **s22** batch1 4 starter pts; ⚠ assertion «медицина наверху-слева» не совпадает с position (P0-1).
- **s23** batch2 8 pts, L10 bimodal gold-ringed (See&Spray/Monarch); ⚠ M1/M2 неразличимы (P1-1). Coords consistent.
- **s24** full map ~18 pts, L13 trio gold-ringed; ⚠ M1/M2 (P1-1). Coords consistent, progressive reveal OK.
- **s25** cluster closed-loop — reused scatter + text caption; ⚠ нет highlight (P1-2).
- **s26** cluster open-env — reused scatter + gold caption + failure list; ⚠ нет highlight + position mismatch (P1-2).
- **s27** cluster high-stakes — reused scatter + caption; ⚠ нет highlight + position mismatch (P1-2, P0-1).
- **s28** empty quadrants — DOES have gold-dashed shaded zone + shift arrow; ⚠ «пустой» квадрант фактически полон точек (P0-1).
- **s29** divider 4 — visible чистый; ⚠ «strict-in» в speaker_notes (P1-3).
- **s30** failures 1-4 card-grid, card 2 gold (p^N math). PASS (footer «strict-in» убран — iter3 confirmed).
- **s31** failures 5-8 card-grid, card 8 gold (deepfake). PASS.
- **s32** failures 9-12 card-grid, footer MIT/McKinsey honesty. PASS.
- **s33** synthesis 3 mega-pattern cards + gold 30-sec procedure. PASS (5-sec test работает).
- **s34** cheat-sheets overview — ⚠ пустые A4/A1 placeholder thumbnails (P1-4).
- **s35** cheatsheet #1 matrix 7×4 — полная, читаема, gold STOP-rule, QR-placeholder. PASS.
- **s36** cheatsheet #2 ladder 6×5 — полная, L1 gold, footer antipatterns. PASS; ⚠ EN level-names (P2-2).
- **s37** cheatsheet #3 failures 12×3 — все 12 строк, row 12 gold, читаема. PASS (главный sheet — delivers).
- **s38** master poster A1 — 4 colored zones, все 16 labeled; ⚠ нижне-правая «warning» зона — самая полная (P0-1), M1/M2 (P1-1).
- **s39** Q&A dedicated — scenario + Краткая опора recap + gold positive recap; без timing. PASS.
- **s40** closing hero — **real ESO VLT photo**, ≥45% area, gold overlay, attribution видна, 3 positioning cards. PASS (образцовый).

---

## Cross-deck issues

1. **Keystone-axis integrity (P0-1)** — единственный блокер; затрагивает 9 слайдов (s03, s22-s28, s38) + chapter §0.3/§3.7. Fix требует book-editor + orchestrator (concept-level), cascade через весь Раздел 3.
2. **Module-color system (P1-1)** — 3-цветное кодирование заявлено в deck.yaml как LOCKED, но визуально работают 2 цвета. Системная правда: либо усилить M1/M2 контраст, либо различать формой.
3. **Cluster-slide highlight pattern (P1-2)** — s25/s26/s27 единственные scatter-слайды без зоны-highlight; несогласованно с s28 (который highlight имеет). Унифицировать ПОСЛЕ P0-1.
4. **Anglicism consistency (P2-1/P2-2)** — для RU capstone накопительно; level-names и «маппинг» — самые частые. Не блокер, но пройтись Russification-таблицей.
5. **Pattern compliance с Lec-15** — PASS по структуре (lecture-map, dividers, dedicated Q&A, roadmap только на dividers+cover). Единственное отклонение — roadmap-bar на hero s01 (P1-5, formally allowed на cover, но мешает hero).

---

## Заметка для orchestrator: расхождение со student-simulator P0

Student-simulator (08:52) заявил **P0 «сломанная вёрстка ≈14 слайдов: контент сжат в левый-верхний угол, низ пустой, шрифт нечитаем»** (s07, s12, s14, s17, s19, s23-s28, s32, s33, s37, s40).

**Это НЕ подтверждается** объективной проверкой:
- Current snapshots (mtime 08:44) **предшествуют** отчёту student-simulator (08:52) — оба смотрели один и тот же render.
- `convert -trim` bounding-box: s07=1368×747, s14=1369×664, s23=1369×748, s28=1369×670, s33=1370×655 из 1467×825 — **контент заполняет почти всю площадь** (поля ~50px), НЕ сжат в угол.
- Мои full-resolution reads (+ crops + 50% projector-zoom s23/s07) показывают контент по всему полю, читаемый.

**Вероятная причина:** артефакт downscaled-отображения PNG в vision-панели (некоторые full-res PNG рендерятся мелко при первом открытии — я сам это наблюдал на s07 до crop). Student-simulator, вероятно, оценил по уменьшенному превью.

**Рекомендация orchestrator:** НЕ принимать student-simulator P0 «broken layout» как структурный без re-verify. Реальные readability-риски тоньше: M1/M2 цвет (P1-1) + мелкие scatter point-labels на 50% zoom (на грани, P2-8) + font на плотных schema. s34-placeholder (P1-4) и roadmap-bar на hero (P1-5) student-simulator нашёл верно — эти подтверждаю.

---

## Recommendations для Phase 8 (приоритет)

1. **[P0-1 BLOCKING]** Orchestrator + book-editor: исправить keystone quadrant semantics (поменять местами upper-left ↔ lower-right семантику ИЛИ переопределить axis-направления), переразместить точки так, чтобы попадали в свои квадранты, убедиться что «empty/dangerous» квадрант визуально пуст на s28/s38. Cascade: s03, s22-s28, s38 + chapter §0.3/§3.7. **Без этого фикса deck не показывать.**
2. **[P1-1]** Усилить M1/M2 цветовой контраст (или различать формой) на всех scatter (s01/s22/s23/s24/s38).
3. **[P1-2]** Добавить per-cluster shaded zone-highlight на s25/s26/s27 (как s28) — после P0-1.
4. **[P1-3]** Убрать «strict-in» из s29 speaker_notes + `## media` source.
5. **[P1-4]** Заменить пустые A4/A1 placeholders на s34 мини-превью реальных таблиц.
6. **[P1-5]** Убрать roadmap-bar с s01 hero + увеличить scatter в hero-боксе.
7. **[P2 batch]** Russification pass (anglicism cluster), gold-pill overlap s14, «non-AI»→«не-AI».

После fix-итерации — re-snapshot + re-run этого критика на изменённых слайдах (особенно P0-1 cascade).
