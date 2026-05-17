# Consistency Checker Report — Лекция 4 — 2026-05-17 (re-QA delta v1.2-tools, Решение #102)

**Scope:** targeted 3-artifact alignment после tool-добавления (Решение #102).
chapter **v1.2** ↔ deck **v3.3** ↔ speech **v1.2**. Issue #99, pre-GATE-C.
**Mode:** delta (tool-content alignment + book-first + frozen-integrity + terminology + orphan), не full re-QA.

## VERDICT: APPROVE-CLEAN

3-artifact tool-alignment: **YES**. book-first: **YES**. RISK-1 / RISK-2: подтверждены **не-блокеры**.
Frozen-слайды: **неприкосновенны**. mode≠brand-anchor drift: **нет** (допустимый pedagogical-anchor).
Terminology: **0 forbidden**, канон выдержан. «мейнтейнер»: **owner-note** (flag-only, вне scope critic).

## Severity counts
- P0 (factual contradiction / book-first violation / frozen-slide touched): **0**
- P1 (significant 3-artifact tool drift): **0**
- P2 (minor): **0**
- Owner-notes (вне scope critic, REPORT-only): **1** («мейнтейнер»)

---

## 1. 3-artifact tool-set alignment matrix

Источник истины: chapter v1.2 `[for-slide-sNN]`. Deck v3.3 tool-strip рендерится через
`build_lec04.py::tools_strip()` (helper, [v3.3, Решение #102]) — НЕ через deck.yaml/slides/*.md
(deck.yaml/slides/glossary `git status` = 0 modified; tool-контент в build-слое + rendered .pptx).

| Уровень | chapter v1.2 | deck v3.3 (tools_strip chips) | speech v1.2 | Aligned? |
|---|---|---|---|---|
| **A** §1.2 `[s06]` | Copilot ghost-text · Cursor Tab · JetBrains full-line/AI Assistant | `Copilot ghost-text` · `Cursor Tab` · `JetBrains AI` | «Copilot ghost-text, Cursor Tab, ассистент JetBrains» | ✓ |
| **B** §1.3 `[s07]` | ChatGPT/Claude/Gemini (чат-LLM) · Copilot Chat · Cursor Cmd-K | `ChatGPT-чат` · `Copilot Chat` · `Cursor Cmd-K` | «ChatGPT, Claude, Gemini … Copilot Chat, Cursor Cmd-K» | ✓ |
| **C** §2.2 `[s12]` | Claude Code · Cursor Composer/Agent · **Codex (CLI/Cloud)** | `Claude Code` · `Cursor Composer` · `Codex CLI` | «Claude Code, Cursor Composer, Codex CLI» | ✓ |
| **D** §3.2 `[s15]` | Copilot coding agent (GA) · Devin 2.0 · Jules · **Codex Cloud** | `Copilot agent` · `Devin 2.0` · `Jules` · `Codex Cloud` | «Copilot coding agent, Devin 2.0, Jules, Codex Cloud» | ✓ |

### Vendor/mode-naming consistency — verified, no drift

- **Codex C-vs-D разделение НЕ drift, а намеренный mode-split (book-first).** chapter §2.2 явно
  пишет «**Codex** в режиме **CLI / Cloud**» (уровень C, CLI-агент на well-scoped задачах);
  chapter §3.2 — «**OpenAI Codex Cloud**» (уровень D, async overnight-PR). Deck зеркалит:
  s12 chip `Codex CLI`, s15 chip `Codex Cloud`. Speech: s12 «Codex CLI», s15 «Codex Cloud».
  Это **режим≠бренд в действии** (один продукт на двух уровнях по режиму) — каноничный
  пример несущего правила лекции, не рассинхрон. Все 3 артефакта консистентны.
- **«Copilot coding agent» → chip «Copilot agent»** (s15): сокращение зафиксировано в
  iteration-log v3.3 («режим тот же, короче для chip-fit»); chapter §3.2 и speech s15 несут
  полную форму «Copilot coding agent». Это chip-renderer constraint, не семантический drift —
  режим (issue→PR оркестратор) идентичен во всех 3. ✓
- **adoption-направление словами** — идентичная семантика во всех 3:
  - A: «самый зрелый и широкий по охвату; лидер по охвату Copilot-класс, рост лидера встал»
    (chapter §1.2 ↔ deck strip ↔ speech s06) ✓
  - B: «чат-LLM — самый массовый способ применять AI к коду» (chapter §1.3 ↔ deck ↔ speech s07) ✓
  - C: «самый быстрорастущий уровень; паттерн "связка инструментов"» (chapter §2.2 ↔ deck ↔ speech s12) ✓
  - D: «самый молодой сегмент; мульти-агент = emerging, не мейнстрим» (chapter §3.2 ↔ deck ↔ speech s15) ✓
- **anti-hype/границы-оговорки** (AI-Failure-усиление, не реклама) — derive из chapter v1.2, идентичны:
  - A «"#1" = охват, не динамика; стагнация ≠ умер; режим ставит, не логотип» ✓
  - B «чат-LLM строго B, петля copy-paste; без обвязки "агентно" = маркетинг» ✓
  - C «SWE-bench как доказательство автономии дыряв; высокая цифра ≠ мерджить без senior; режим≠бренд» ✓
  - D «Devin "fully-autonomous" = overclaim; Copilot agent в проде = 5 отказов + kill switch → гейты обязательны» ✓

**Вывод §1:** тул-наборы / вендоры / режимы / adoption-направление / оговорки **идентичны** во всех
3 артефактах. 0 случаев «Codex CLI в одном vs Codex Cloud в другом без причины» — C/D split
обоснован book-first и есть в chapter явно. **3-artifact tool-alignment = YES, 0 drift.**

---

## 2. mode≠brand anchor — допустимый pedagogical-anchor, НЕ chapter↔speech drift

| Артефакт | mode≠brand размещение |
|---|---|
| chapter v1.2 | §0.4, маркер `[for-slide-s04]` — полный абзац-правило (Copilot=A+B+C+D, Cursor=A+B+C, Claude Code=C+D; границы B↔C «итерирует+тесты сам?», C↔D «источник задачи + PR-выход?») |
| speech v1.2 | устно на **s03**-фрагменте (keystone): «уровень — это режим, а не бренд. Copilot — A,B,C,D; Cursor — A,B,C; Claude Code — C и до D. "У нас стоит Copilot" не сообщает уровень риска» |
| deck v3.3 | **НЕ выносит** mode≠brand на видимый s03/s04. Подтверждено: build_s03/build_s04 — 0 токенов «режим/бренд/Copilot=A/маппить»; slides/s03·s04.md — 0 совпадений; build_s03/s04 НЕ изменены в v3.3-диффе. |

**Оценка drift:** допустимый pedagogical-anchor, **НЕ drift**. Обоснование:
- Семантика идентична chapter §0.4 (тот же набор Copilot/Cursor/Claude Code mode-mappings,
  то же ядро «логотип не сообщает уровень»). speech ничего не добавляет вне §0.4.
- Сдвиг s04→s03 в speech — **pedagogically корректен**: правило вводится сразу за keystone-картой
  A→D (s03), где студент впервые видит уровни — это естественная точка «как читать карту».
  chapter маркирует `[for-slide-s04]`, но речь — устная развёртка, не построчное зачитывание
  маркеров; раннее введение правила усиливает keystone, не противоречит ему.
- **Book-first НЕ нарушен:** speech говорит ровно то, что в chapter §0.4 (источник истины),
  просто на один слайд-фрагмент раньше. Контента вне chapter speech не вносит.
- **deck-консистентность:** owner-решение «keystone s03 НЕ трогаем» (Решение #102) соблюдено —
  deck не выносит mode≠brand на видимый s03/s04. 3 артефакта согласованы: chapter — текст-правило,
  speech — устный anchor на s03, deck — keystone-чистота (5-сек читаемость защищена).

**mode≠brand-anchor drift: НЕТ.**

---

## 3. Book-first compliance — YES

- **deck/speech 0 утверждений вне chapter v1.2.** Все тул-факты (названия, режимы,
  adoption-направления, anti-hype-оговорки) прямо derive из chapter v1.2 §1.2/§1.3/§2.2/§3.2
  + `notes/research/lecture-4/tools-landscape.md` «2026-05-17 update» (источник chapter-фактов).
  Cross-read deck `tools_strip()` invocations ↔ chapter — 0 новых утверждений.
- **`git diff` chapter:** только chapter.md/part2/part3 модифицированы (M, uncommitted).
  Changelog chapter v1.2 явно: «Финализированный контент v1.1 НЕ менялся: числа, кейсы,
  citations, нарратив/структура, `[for-slide-sNN]` s01–s32 сохранены. Только ДОБАВлены
  тул-секции + mode≠brand». Это **additive book-editor upstream-шаг**, не designer/speech-writer.
- Каскад порядок (Решение #102): chapter v1.1→v1.2 → deck derive → speech v1.1→v1.2 derive —
  соблюдён. deck.yaml chapter_ref s06/s07/s12/s15 уже = §1.2/§1.3/§2.2/§3.1,§3.2 (book-first
  satisfied без правки yaml).

**Book-first: YES, 0 нарушений.**

---

## 4. Designer RISK-1 (chapter «не UNMODIFIED») — подтверждён НЕ-блокер

- `git status`: chapter.md / chapter-part2.md / chapter-part3.md = **M (modified, uncommitted)**.
- Chapter changelog **v1.2 (2026-05-17) — Решение #102** присутствует, описывает ровно
  additive tool-секции + mode≠brand-правило; «финализированный v1.1 НЕ менялся».
- Это **незакоммиченный v1.2 book-editor upstream-шаг каскада** (book-first: chapter правится
  ПЕРВОЙ, deck/speech derive). designer/speech-writer chapter НЕ трогали (RISK-1 designer-репорт
  корректен: «chapter*.md UNMODIFIED» в iteration-log относился к designer-touch, а chapter
  модифицирован book-editor'ом выше по каскаду).
- Ожидаемо в book-first каскаде: оркестратор коммитит всё вместе после re-QA delta + GATE C.
- **Вердикт: НЕ блокер.** Ожидаемое состояние pre-commit book-first каскада.

---

## 5. Designer RISK-2 ([VFY] не в speaker-notes) — подтверждён НЕ-блокер

- Точные волатильные числа (Copilot adoption/awareness, ChatGPT-доля, Claude Code 6×/CSAT,
  SWE-bench Verified ~88,7%/Pro ~64,3%, Copilot agent 17M PR/5 outages) живут в:
  **chapter v1.2 `[for-slide-sNN]` + research** (`tools-landscape.md` «2026-05-17 update»)
  с `[VFY-day-of]`-разметкой; **speech preflight `[VFY-day-of]`** (строки 25–30) — day-of re-verify.
- **Видимый слой** (deck tool-strip + устный s06/s07/s12/s15) несёт **только направление словами**
  (паттерн s12/s27): «самый зрелый/широкий», «самый массовый», «самый быстрорастущий»,
  «самый молодой/emerging» — без точных волатильных долей. Подтверждено: 0 волатильных %/долей
  в tool-strip-тексте (только «2026»-title, «№1»-качеств., «Devin 2.0»-версия, «5 отказов»-
  event-stable anti-hype-якорь — owner-approved/non-volatile).
- Frozen speaker-notes (s06 ~281w / s12 ~262w) **НЕ раздуты**: +параграф с числами пробил бы
  300w-ceiling ENFORCED speaker-notes-contract + нарушил бы «существующий контент СОХРАНИТЬ»
  (notes = finalized v1.1). Числа намеренно НЕ в notes — они в chapter (book-first source).
- Консистентно с Решение #100 (видимый слой = направление, не точные доли) + Решение #9
  (volatile → `[VFY-day-of]`, не на видимом слое). **Вердикт: НЕ блокер.**

---

## 6. Frozen-слайды + keystone s03 + s04 — неприкосновенны (verified)

- **deck.yaml / deck-part2.yaml / slides/*.md / glossary.yaml**: `git status` = **0 modified**.
- **build_lec04.py diff (HEAD):** изменены ТОЛЬКО — `tools_strip()` helper (+) и builder-функции
  `build_s06` / `build_s07` / `build_s12` / `build_s15` + loader-spacing. **build_s03 / build_s04
  / все прочие 29 builders — 0 правок в диффе** (grep `def build_s03|build_s04` в диффе = 0).
- **Keystone s03 + s04 байт-семантически нетронуты:** 0 mode≠brand-токенов в build_s03/s04
  (owner-constraint «keystone не трогаем» соблюдён).
- **Валидатор не сломан:** `build_lec04.py` enforce `ids == expected` (s01–s32 base + suffix
  s04a/s24a/s28a), `base_in_order == base` (s01–s32 нумерация неизменна),
  `totals.slides == 35`, `len(builders) == 35`. Нумерация неизменна.
- **chapter `[for-slide-sNN]` s01–s32**: changelog v1.2 явно «маркеры s01–s32 сохранены»;
  v1.2 — только additive tool-секции под существующими `[for-slide-s04/s06/s07/s12/s15]`.
- 35 LOCKED, suffix-ID конвенция (s04a/s24a/s28a) цела.

**Frozen + keystone + s04 неприкосновенны: подтверждено. Изменены только s06/s07/s12/s15
(+ build helper/loader/log/yaml-не-трогался). 0 frozen-слайдов тронуто.**

---

## 7. Terminology / glossary — консистентно, 0 forbidden

- **0 forbidden-англицизмов** (grep `пайплайн|фоллбэк|эдж-кейс|инсайт|автокомплит` по
  chapter×3 + speech + slides/*.md + build_lec04.py с фильтром правильных форм) = **0 hits**.
- Канон-термины выдержаны 3 артефакта: «автодополнение» (НЕ автокомплит) ✓;
  «кодинг-агент» ✓; «оркестратор» ✓; «"почти правильный" код» ✓; mode/режим vs бренд —
  каноничный mode≠brand ✓; «SWE-bench (Verified/Pro)» ✓; «slopsquatting» ✓; «supply-chain» ✓.
- Новые тул-термины (Copilot ghost-text / Cursor Tab / JetBrains AI / ChatGPT-чат /
  Copilot Chat / Cursor Cmd-K / Claude Code / Cursor Composer / Codex CLI / Codex Cloud /
  Copilot coding agent / Devin 2.0 / Jules) — единообразны chapter↔deck↔speech (см. §1 matrix);
  не в glossary (post-lock additions Решение #102) — но 1-формны во всех артефактах, 0 drift.

### Owner-note (REPORT-only, rename = USER scope, вне scope critic)

- **«мейнтейнер»** — pre-existing v1.1 контент (chapter §0.1 METR-контекст, §4.5 curl-кейс,
  chapter-part2 ×неск., chapter-part3 сводная таблица). НЕ в `glossary.yaml`
  `forbidden_anglicisms` (там только пайплайн/фоллбэк/эдж-кейс/инсайт). Это кириллизованный
  `maintainer`. **Flag-only owner-note:** не введён v1.2, не tool-related, rename требует
  USER-approval (Glossary LOCK: critic MAY flag, MAY NOT rename/propose-canonical-change).
  Не блокер re-QA delta; отмечаю для владельца на будущее (вне scope текущего tool-touch).

---

## 8. Orphan / drift / структурная целостность — 0 issues

- **Speech ↔ deck slide-coverage:** speech fragment headers `## [sNN ]` = **35**;
  extracted slide-IDs = ровно `s01–s32 + s04a + s24a + s28a` = **35** = deck.yaml validator
  expected. **0 orphan references** (нет ссылки на удалённый/несуществующий слайд).
- **Chapter orphan refs:** grep `см. слайд|see slide|→ sNN` в chapter×3 = **0 hits**.
- **5 точек возврата ЦВ целы:** возврат 1 (s08, brief) → 2 (s13) → 3 (s17) → 4 (s21 частично/
  полный s24) → 5 (s26), консолидация s24 — все present в speech + slides, последовательность
  не нарушена.
- **6 дивайдеров целы:** «Раздел первый…шестой из шести» = s04a/s10/s14/s18/s24a/s28a в speech
  (bridge-фразы present); Раздел 0 = открытие без дивайдера (по плану §2.2).
- **v1.1 known divergences без регрессии:**
  - **#1 (curl→s22 slopsquatting):** speech §«Открытые расхождения» документирует — deck
    отдаёт s22 под slopsquatting, curl (#5 §4.5) живёт в chapter как deep-narrative + устный
    якорь s25/s32 + Q&A. speech-writer следовал deck-порядку (book/deck-first + No-Extra-Content).
    Не регрессия — pre-existing v1.1, корректно re-reported, strict-in ≥35% держится без полного
    curl-нарратива (~46% минут). Не tool-related; вне scope tool-delta; **не блокер.**
  - **#2 (s05 двойная роль):** s05 несёт «цена ошибки растёт с автономией» (Решение #100) +
    рамка «4 вопроса» (chapter §1.1 + §0.4). По смыслу согласуется с chapter, drift нет.
    Pre-existing, корректно re-reported. Не tool-related; **не блокер.**

---

## Топ-фиксов (per artifact)

- **Chapter:** 0 фиксов. v1.2 additive каскад корректен; коммит вместе с deck/speech после GATE C.
- **Slides/deck:** 0 фиксов. tools_strip-реализация в build-слое book-first-консистентна; frozen цел.
- **Speech:** 0 фиксов. Тул-развёртка + mode≠brand-anchor s03 derive из chapter v1.2, 0 drift.

## Open items (REPORT-only, НЕ блокеры, требуют owner/orchestrator-решения)

1. **«мейнтейнер»** — owner-note для будущего glossary-решения (rename = USER scope; не tool-related).
2. **RISK-2 [VFY] не в speaker-notes** — подтверждённый намеренный design (Решение #100/#9);
   если владелец хочет числа в notes — потребует speaker-notes-contract waiver (300w-ceiling).
   Critic-рекомендация: текущее состояние консистентно, waiver НЕ требуется для tool-delta.
3. **v1.1 divergences #1/#2** — pre-existing, корректно re-reported speech-writer'ом, без
   регрессии; вне scope tool-delta. Решение по #1 (полный curl-нарратив устно?) — owner-вопрос
   при необходимости, не блокер GATE C по tool-content.

---

**Финальный verdict: APPROVE-CLEAN.** 3-artifact tool-alignment YES (0 drift, C/D Codex-split
обоснован book-first). Book-first YES. RISK-1/RISK-2 — подтверждённые не-блокеры. Frozen +
keystone s03 + s04 неприкосновенны (только s06/s07/s12/s15 builders + tools_strip helper).
mode≠brand — допустимый pedagogical-anchor, НЕ drift. Terminology 0 forbidden. «мейнтейнер» —
owner-note. **0 P0 / 0 P1 / 0 P2.** Готово к GATE C по критерию cross-artifact consistency.
