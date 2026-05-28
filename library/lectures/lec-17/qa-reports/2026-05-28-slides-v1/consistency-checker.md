# Consistency Checker Report — Lec-17 Slides v1

**Date:** 2026-05-28 | **Phase:** 7 (slides QA, mode=chapter+slides) | **Verdict:** APPROVE-WITH-POLISH

## Severity counts

- **P0** (factual contradiction / missing coverage): 0
- **P1** (significant drift): 1
- **P2** (minor inconsistency): 4

## Summary

40-слайдовый deck v1 для capstone Лекции 17 показывает **очень высокую** cross-artifact
согласованность с chapter v2 (5-part, 30 191 слов). Все три структурных артефакта курса —
7 критериев, лестница L0→L5, 12 провалов, mapping table §2.7, карта 16 отраслей — перенесены
на слайды без структурных расхождений. **Все 8 исправленных v2-фактов** (Cruise 10.12.2024,
Tesla 2018, Arup CFO-video deepfake, Apple Card explainability-reframe, Plenty $940M raised /
Chapter 11, MIT 95% ≠ McKinsey 5.5% decoupling) корректно унаследованы слайдами — старые
v1-ошибки **не** воспроизведены. Scatter-координаты стабильны через три reveal-батча
(s22→s23→s24). Rendered visible body последовательно использует Russified canonical-термины
(«применимость ИИ», «закрытая петля»).

Единственный **P1** — leak chapter-internal методологического термина `strict-in` в
speaker_notes слайда s29 (student-facing). Остальное — P2 (frontmatter/notes-level
terminology drift, не доходящий до rendered visible body; design-direction `## media`
комментарии со словом `strict-in`, которые надо strip в Phase 8). Это не структурный gap;
deck готов к USER GATE B после lightweight Phase-8 polish.

---

## Chapter ↔ slides alignment

| Раздел / артефакт | Chapter | Slides | Aligned? |
|---|---|---|---|
| Keystone 2D-плоскость (2 оси + 4 квадранта) | §0.3 | s03 | ✓ (rendered: оси + 4 подписанных квадранта, warning zone gold) |
| Главный вопрос re-asked + 3 вопроса | §0.4 | s04, s39 | ✓ |
| 7 критериев AI/non-AI | §1.0-§1.4 | s07-s11 | ✓ (все 7 присутствуют, парами) |
| Worked example #1 (ЖКХ-вода) | §1.5 | s12 | ✓ (verdict L1 advisory + A/B vs EPANET) |
| Лестница автономии L0→L5 (6 ступеней) | §2.1-§2.6 | s14, s16-s18 | ✓ |
| Mapping table (2 таблицы: direct + orthogonal) | §2.7 | s15 | ✓ (rendered: Таблица A + Врезка B ортогональные оси) |
| Антипаттерны per level | §2.8 | s19 | ✓ (6 карточек: L1 Klarna → L5 LAWS + cross-level) |
| Worked example #2 (приём экзаменов) | §2.9 | s20 | ✓ (потолок L1) |
| Карта 16 отраслей (~20 точек) | §3.1-§3.3 | s22-s24 | ✓ (3 reveal-батча; L13 3 точки; L16 anchor) |
| 3 кластера (closed-loop / open-env / high-stakes) | §3.4-§3.6 | s25-s27 | ✓ |
| Пустые квадранты дидактика | §3.7 | s28 | ✓ |
| Топ-12 провалов | §4.1-§4.12 | s30-s32 | ✓ (одинаковый список, факты, источники) |
| Synthesis 3 mega-pattern + 30-сек процедура | §4.13 | s33 | ✓ |
| 4 cheat-sheets | §5.1-§5.4 | s35-s38 | ✓ (decision matrix 7×4 / ladder 6×5 / failures 12×4 / map A1) |
| Карьерная траектория | §5.5 | s39 notes, s40 | ✓ |
| Closing «знать ИИ = знать границы» | §5.7 | s40 | ✓ |

**Результат: 15/15 разделов покрыты, без структурных gaps.** Каждый slide `chapter_ref`
указывает на корректную часть (5-part split slide_map верифицирован: s01-05→chapter.md,
s06-20→part2, s21-28→part3, s29-33→part3b, s34-40→part4).

### Coverage parity checks

- 7 критериев на slides (s07 overview + s08-s11) = 7 критериев chapter §1 ✓
- L0→L5 ladder (s14) = chapter §2.1-§2.6 ✓
- 12 провалов (s30/s31/s32 + s37 cheat-sheet) = chapter §4.1-§4.12 — **идентичный список + факты** ✓
- Mapping table s15 = chapter §2.7 (Таблица A direct ladders L4/L9/L12 + Врезка B orthogonal L13/L14) ✓
- 3 кластера + warning quadrant дидактика = §3.4-§3.7 ✓

---

## Fact-consistency (v2 corrected facts inherited)

Slides проверены на наследование **исправленных v2-фактов** (НЕ старые v1-ошибки):

| Факт | Требуемое v2 значение | Слайды | Статус |
|---|---|---|---|
| Cruise GM closure | 10 декабря 2024 (НЕ 2023) | s08, s19 | ✓ PASS (s08: «GM закрыл подразделение 10 дек. 2024»; s19: dragging «2.10.2023», closure корректно отделён) |
| Cruise dragging incident | 2 октября 2023 | s08, s19 | ✓ PASS (отделён от closure) |
| Tesla tweet | 2018 (НЕ July; chapter точн. 13 апр 2018) | s31, s37 | ✓ PASS («Tesla 2018»; нет ошибочного July) |
| MIT NANDA 95% ≠ McKinsey 5.5% | decoupled, разные измерения | s32, s37, s39 | ✓ PASS (s32 footer: «95% (MIT) и 5,5% (McKinsey) — РАЗНЫЕ измерения, не одно число»; rendered visible) |
| Deepfake | Arup CFO+colleagues **video** (НЕ CEO voice), февр. 2024 | s31, s37 | ✓ PASS (s31 footer: «после видео-конференции с имитацией финансового директора и коллег»; «видео+голос = новый вектор») |
| Apple Card | explainability lesson, DFS 2021 cleared (НЕ «bias proven») | s10, s35 | ✓ PASS (s10 rendered: «Goldman Sachs оправдан... Урок — объяснимость, не предвзятость») |
| Plenty | $940M **raised** (НЕ loss) + Chapter 11 март 2025 | s26 | ✓ PASS («$940 млн+ привлечено с 2014 → обвал стоимости → Chapter 11, март 2025») |
| BCCRT (НЕ «Canadian») | Air Canada tribunal | s31, s37 | ✓ PASS (нет ошибочной атрибуции «Canadian»; tribunal name опущен в компактной карточке — допустимо) |
| Zillow | $304M, ≈2 000 из ~8 000, ноябрь 2021 | s08 | ✓ PASS (baseline denominator inline) |
| Monarch | 38%, ≈53 из ~140 peak, янв. 2025 | s08, s23, s26 | ✓ PASS |
| Epic Sepsis | AUC 0.76 → 0.63, 38k пациентов | s08, s35 | ✓ PASS (gold-highlighted contrast) |
| CrowdStrike | 8.5M устройств, $5+ млрд = insurance estimate (НЕ P&L) | s09, s28 | ✓ PASS (s09: «оценка Parametrix по Fortune 500 — не P&L CrowdStrike») |

**Все 12 sampled measurable claims имеют v2-корректные значения. 0 fact-drift.**

### τ-bench / Sierra (chapter §4.2) — non-issue

Chapter §4.2 атрибутирует Sierra τ-bench (Bret Taylor, июнь 2024) + Salesforce CRMArena
отдельно. Слайд failure-2 (s30) и synthesis (s33) **не называют** ни Sierra, ни Salesforce —
используют обобщённую формулировку «накопление ненадёжности в многошаговом агенте» +
«$4 200-петля (L3) / агентная SE (L4)» + формула p^N. Это **корректное упрощение** для
compact card-grid; поскольку слайд не делает атрибуцию вообще, нет риска воспроизвести старую
v1-ошибку «Salesforce». **Не drift.** (Если хочется — Phase 8 может добавить «Sierra τ-bench»
в speaker_notes s30 для полноты, но не required.)

---

## Scatter coord consistency

Проверены координаты отраслевых точек через все reveal-слайды (s22 batch1 → s23 batch2 →
s24 batch3 full) + кластерные слайды (s25/s26/s27/s28) + cheat-sheet s38.

| Точка | s22 | s23 | s24 | s38 | Consistent? |
|---|---|---|---|---|---|
| L4 SE | верх-право | (carried) верх-право | верх-право | верх-право | ✓ |
| L5 финансы (фрод) | верх-середина | (carried) | (carried) | — | ✓ |
| L7 медицина | верх-лево | (carried) | (carried) | верх-лево | ✓ |
| L9 авиакосмос | верх-середина с потолком | (carried) | (carried) | — | ✓ |
| L10 См&Sp / Monarch (bimodal) | — | См&Sp ↑ / Monarch ↓ | (carried) | bimodal | ✓ |
| L13 склад/робот-такси/чёрн.лебедь (3 точки) | — | — | L4 / L3 / L0 | 3 точки | ✓ |
| L16 (4-quadrant matrix врезка) | — | — | data×process | — | ✓ |

**Координаты стабильны:** 4 точки s22 переотрисованы в тех же позициях на s23 и s24
(verified в rendered snapshots — L4 верх-право, L7 верх-лево сохраняются). Bimodal-отрасли
(L10/L13/L15) consistent multi-point. Quadrant assignments в scatter совпадают с chapter §3
cluster analysis (closed-loop верх-право = §3.4; open-env низ-право = §3.5; high-stakes верх-лево
= §3.6; warning empty низ-право = §3.7). **0 coordinate drift.**

---

## Terminology / Russification drift

Rendered **visible body** последовательно использует Russified canonical-формы:
- «применимость ИИ» (rendered: s03, s22, s23, s24, s27 title, s10 body, s28) — canonical ✓
- «закрытая петля» (rendered: s25 title «Кластер закрытой петли», s08, s33) — canonical ✓
- «человек в петле» доминирует (19×) над «HITL» (11×, в основном в `## media` allowlist) ✓
- «лестница автономии L0→L5» consistent ✓

**Drift, ограниченный frontmatter + speaker_notes (НЕ rendered visible body):**

- **s10 speaker_notes L52:** «применимость **AI** высокая» (смешанная RU/EN форма). Rendered
  visible body на этой же строке (Pearl level-1) корректно использует «применимость **ИИ**
  высокая» — verified в snapshot. Drift только в озвучке. **P2.**
- **s27 / s25 frontmatter `assertion:`** содержат «AI fit» / «closed-loop» — НЕ propagated в
  rendered title (s27 title = «применимость ИИ высокая»; s25 title = «Кластер закрытой петли»).
  `## media` design-direction также содержит «closed-loop». **P2** (frontmatter/design-layer,
  стрип в Phase 8 опционален).

**Anglicism в rendered title (AI / advisory) — НЕ consistency-drift:** s10 title «...AI
остаётся на advisory...», s25 «...применения AI» используют Latin «AI» / «advisory». Это
**consistent с chapter**, который свободно смешивает AI/ИИ + advisory + HITL по всему тексту
(academic chapter). Не cross-artifact drift; передаю как FYI для presentation-critic /
russification-проверки (вне scope consistency-checker).

---

## Baseline consistency

Measurable claims на slides несут **те же baselines/denominators**, что chapter v2:

| Claim | Chapter baseline | Slide | Aligned? |
|---|---|---|---|
| See & Spray −50% гербицидов | ≈1 фунт/акр → ≈0.5; 5M из ~900M US ag = 0.55% | s08, s35 | ✓ (s08: «(с ≈1 фунт/акр до ≈0,5... на 5 млн акров из ≈900 млн = 0,55%)») |
| Copilot 20M users | из ~28M GitHub devs ≈70% | s09 | ✓ («20+ млн... из ≈28 млн зарегистрированных») |
| CrowdStrike $5+ млрд | insurance estimate (Parametrix Fortune 500), не P&L | s09, s28 | ✓ |
| Monarch 38% | ≈53 из ~140 peak Q3 2024 | s08, s23, s26 | ✓ |
| Zillow $304M | ≈2 000 из ~8 000 employees | s08 | ✓ |
| Plenty $940M | raised since 2014 (не loss) | s26 | ✓ |
| Epic Sepsis AUC | 0.76 vendor → 0.63 на 38k пациентов | s08, s35 | ✓ |

**Все sampled measurable claims на slides сохраняют denominators/baselines из chapter.** 0
«missing denominator» drift между артефактами.

---

## P0/P1/P2 issues

### D1 — `strict-in` (chapter-internal методологический термин) leaked в speaker_notes s29
**Severity:** P1
**Where:** s29 speaker_notes L51 — «...это самое концентрированное **strict-in** содержание
всей лекции.»
**Issue:** `strict-in` — internal термин CLAUDE.md / chapter-frontmatter (AI-Failure Content
Rule metric). Он НЕ должен появляться в student-facing speaker_notes (которые студент читает в
self-study). Это методологический мета-комментарий о структуре лекции, а не материал. Подтверждает
flag из task brief (§6 Known flags).
**Recommendation:** Phase 8 — переписать фразу без `strict-in`, например: «...это самое
концентрированное содержание про границы применимости во всей лекции». Фикс в **слайде**
(не chapter — chapter уместно использует strict-in в frontmatter/narrative).

### D2 — `strict-in` в `## media` design-direction (s05, s19) + speaker_notes терминология
**Severity:** P2
**Where:** s05 `## media` L42 («Раздел 4... strict-in ядро»); s19 `## media` L48 («Это strict-in
слайд»); `failure_bucket: strict_in` frontmatter (20 слайдов).
**Issue:** `## media` — design-direction для designer, не rendered к студенту; `failure_bucket`
— frontmatter metadata. Оба НЕ student-facing. Но `strict-in` как метка лучше не оставлять в
.md если deck публикуется как self-study source.
**Recommendation:** Phase 8 — опционально strip `strict-in` упоминания из `## media` блоков
(s05/s19). `failure_bucket: strict_in` frontmatter — оставить (это orchestration metadata, exempt).
Низкий приоритет.

### D3 — «применимость AI» (смешанная форма) в speaker_notes s10
**Severity:** P2
**Where:** s10 speaker_notes L52 — «...Здесь применимость AI высокая...»
**Issue:** Canonical RU = «применимость ИИ». Rendered visible body на этой строке использует
корректную «применимость ИИ» — drift только в озвучке лектора.
**Recommendation:** Phase 8 — заменить «применимость AI» → «применимость ИИ» в s10 notes.

### D4 — «AI fit» / «closed-loop» в frontmatter assertion + design-direction (s25, s27, s38)
**Severity:** P2
**Where:** s27/s10 `assertion:` («AI fit высокий»); s25 `assertion:` + `## media` («closed-loop»);
s38 `## media` («closed-loop структуре»).
**Issue:** Английские термины в frontmatter/design-layer. НЕ propagated в rendered visible body
(s27 rendered title = «применимость ИИ высокая»; s25 rendered title = «Кластер закрытой петли»).
**Recommendation:** Phase 8 — опционально синхронизировать frontmatter assertion с canonical RU
(«применимость ИИ» / «закрытая петля») для чистоты source-of-truth. Не влияет на rendered deck.

### D5 — frontmatter `length_words: 30109` vs actual 30 191
**Severity:** P2 (chapter-internal, not slide-related)
**Where:** chapter.md frontmatter `length_words: 30109`; фактический word count всех 5 частей = 30 191.
**Issue:** Метаданные слегка расходятся с фактом (Δ82 слова, 0.27%). Не влияет на slides.
**Recommendation:** Phase 8 / book-editor — обновить `length_words: ~30 191` (или оставить ~30109
как округление; оба >30k baseline). Информационно.

---

## Coverage gaps

**Нет.** Все LO chapter покрыты слайдами:
- LO1 (главный вопрос) → s04, s39
- LO2 (7 критериев применить) → s07-s12
- LO3 (2D-координата) → s03, s22-s28
- LO4 (8+ провалов + урок + альтернатива) → s30-s33, s37
- LO5 (лестница L0→L5) → s14-s20
- LO6 (4 cheat-sheets) → s34-s38
- LO7 (карьерная позиция) → s40
- LO8 (16 отраслей как карта) → s02, s24, s38, s40

Все slide assertions имеют основу в chapter (через chapter_ref). Все assertion'ы карточек
#1-#4 имеют обоснование в §5.1-§5.4. Speech-артефакт ещё не создан (Phase 9-11) — full
3-artifact consistency check отложен до Phase 10.

---

## Топ-фиксов для Phase 8 (per artifact)

- **Slides (P1, обязательно):** s29 speaker_notes — убрать `strict-in` (D1).
- **Slides (P2, желательно):** s10 notes «применимость AI» → «применимость ИИ» (D3); strip
  `strict-in` из s05/s19 `## media` (D2); синхронизировать s25/s27 frontmatter assertion к
  canonical RU (D4).
- **Chapter (P2, информационно):** `length_words` метаданные → 30 191 (D5).
- **Опционально:** добавить «Sierra τ-bench» в s30 speaker_notes для атрибуционной полноты
  (не required — слайд корректно не атрибутирует вообще).

---

## Verdict rationale

**APPROVE-WITH-POLISH.** 1 P1 + 4 P2 (< порога ≥5 P1 → REVISE). Zero P0, zero structural
coverage gaps, zero fact-drift, zero scatter-coordinate drift, все 8 v2-фактов корректно
унаследованы, rendered visible body Russified consistently. Единственный P1 (s29 strict-in
leak) + P2 polish — lightweight Phase-8 fixes, не требующие re-design или re-render. Deck готов
к USER GATE B после Phase-8 strip-pass.
