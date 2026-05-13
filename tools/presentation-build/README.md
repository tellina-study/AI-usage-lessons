# Presentation Build Pipeline

Source-of-truth: this file. Любой агент, работающий со слайдами курса, читает этот файл **первым**.

---

## 1. Архитектурные принципы

1. **Repo-first.** Source — `library/lectures/lec-NN/deck.yaml` + `slides/*.md`. Готовый PPTX лежит рядом в `rendered/`. Google Drive — только публикация и сбор обратной связи (отложено в pilot).
2. **Visual-loop сборка.** Агент работает как живой дизайнер: render → snapshot PNG → читает визуально через Claude vision → правит через MCP → re-snapshot. Лимит: 5-7 итераций на слайд.
3. **Slide-types library.** Каждый слайд — один из определённых типов (см. §4). Title+body как универсальный шаблон **запрещён**.
4. **Assertion-evidence.** Заголовок слайда = тезис (полное предложение), не «тема». Визуал = доказательство тезиса.
5. **Diagrams as shapes.** Схемы строятся примитивами PowerPoint MCP (`add_shape` + `add_connector`), а не как embedded картинки. Embed только когда нет другого пути.

---

## 2. Стек инструментов

| Слой | Инструмент | Назначение |
|---|---|---|
| Source format | `library/lectures/lec-NN/deck.yaml` + `slides/*.md` | структурированный source |
| Render engine | **`powerpoint` MCP** (`office-powerpoint-mcp-server==2.0.7`, GongRzhe) | сборка PPTX из примитивов |
| Snapshot | LibreOffice headless + `pdf2image` | PPTX → PDF → PNG для visual loop |
| Vision | Claude Sonnet/Opus встроенно | агент читает PNG визуально |
| Diagrams (alt) | `drawio` MCP | для сложных схем, когда shape primitives не хватает |

### Установка

```bash
# 1. PowerPoint MCP — через uvx, уже зарегистрирован в .mcp.json
#    (pip install не нужен, uvx запускает в изолированном venv)
uvx --from office-powerpoint-mcp-server==2.0.7 ppt_mcp_server --help

# 2. LibreOffice headless для snapshot — нужен sudo, ставится один раз
sudo apt install -y libreoffice-impress libreoffice-core poppler-utils

# 3. (опционально) pdf2image / Pillow для конвертации PDF → PNG
pip install --user --break-system-packages pdf2image Pillow
```

После установки — verify:
```bash
claude mcp list                                              # powerpoint должен отвечать
libreoffice --headless --convert-to pdf /tmp/test.pptx       # smoke test conversion
```

---

## 3. PowerPoint MCP — критичные tools (37 всего)

Полный список — `tools/list` через MCP. Здесь — только то, что регулярно используется в pipeline.

| Категория | Tools |
|---|---|
| Создание | `create_presentation`, `create_presentation_from_template`, `open_presentation`, `save_presentation` |
| Слайды | `add_slide`, `apply_slide_template`, `manage_slide_masters`, `manage_slide_transitions`, `populate_placeholder` |
| Текст | `manage_text`, `add_bullet_points`, `optimize_slide_text`, `manage_fonts` |
| Шейпы (примитивы) | `add_shape`, `add_connector` |
| Изображения | `manage_image`, `apply_picture_effects`, `manage_hyperlinks` |
| Таблицы и графики | `add_table`, `format_table_cell`, `add_chart`, `update_chart_data` |
| Inspection | `get_presentation_info`, `get_slide_info`, `extract_slide_text`, `extract_presentation_text`, `list_presentations` |
| Шаблоны | `list_slide_templates`, `apply_professional_design`, `auto_generate_presentation`, `get_template_info` |

**Известные limitations PowerPoint MCP** (нет `list_shapes`, баг `format_runs`, нет `update_shape_position`/`delete_shape` и др.) — централизованно зафиксированы в **`notes/mcp-limitations.md`** с конкретными workaround'ами. Перед глубокой работой с MCP — обязательно прочитай этот файл (правило `CLAUDE.md` § «MCP Limitations Catalog»). Новые находки добавлять туда же, не сюда.

---

## 4. Slide-types library (финальная после пилота #55, 8 типов)

Каждый тип = layout + правила контента + чек-лист QA. Слайд **должен** иметь явный `type` в frontmatter и `deck.yaml`.

| Type | Когда | Layout-pattern | Использовался в пилоте |
|---|---|---|---|
| `cover` | Титул лекции (всегда первый, единственный) | Tinted bg + 64pt title + декоративный lecture-number (200pt+ outline) + hero motif + короткий navigation subtitle. **БЕЗ** Ocean rounded box callout (motif для content). | s02 |
| `assertion_visual` | Содержательный слайд (основной тип, ~70% контента) | Assertion-headline (полное предложение) сверху + большой визуал в центре (icon-схема / chart / иллюстрация). Body left-aligned. | s05a, s05b |
| `live_demo` | Внешнее живое демо/код | Минимум на слайде: hook-assertion + mock-screenshot или preview. Главный визуал вне слайда (на проекторе). | s01 |
| `poll_reveal` step 1 | Опрос (часть 1 reveal-пары) | 2 rounded-card блока с 96px иконками (Lucide) + chip-pills для вариантов. Семантически отделить single/multi-select. | s03 |
| `poll_reveal` step 2 (`data_chart`) | Раскрытие данных опроса | 1-2 chart'а (donut + bar) в Ocean rounded box motif. Лидер выделен gold. Methodology caveat 13pt italic. | s04 |
| `process` | Последовательность шагов (3-5) | Numbered horizontal flow через shape-блоки + connectors. (В пилоте не использовался — добавится в следующих лекциях.) | — |
| `comparison` | Сравнение 2 вариантов | Две равные колонки, одинаковая структура. (Не использовался.) | — |
| `summary` | 3 главных вывода (последний слайд раздела или лекции) | 3 крупные тезис-карточки. (Не использовался.) | — |

**Расширения** по реальной нужде: `quadrant` (2×2), `section_divider` (разделитель крупно), `case_study`, `exercise`, `reflection_question`. Не добавляем upfront — только когда понадобятся.

### Schema subtypes (расширение `assertion_visual`, добавлено после Лекции 1 v3 production)

Семь подтипов schema-слайдов с явными правилами читаемости. Любой schema slide **должен** проходить **Schema Readability Checklist** (§5.5) перед accept. Cross-ref: `presentation-designer.md` за per-type building patterns.

| Subtype | Когда | Pattern (пример из Лекции 1) | Critical readability rules |
|---|---|---|---|
| `schema_matrix` | 2D категоризация N×M (например, 4 типа × 4 атрибута) | s12 «4 типа AI-инструментов × характеристики» | **Fill rate ≥75%** (skeleton с пустыми ячейками = недопустимо). Иконки **per column** (визуальная якорь категории). Max 2 строки в ячейке. Font ≥12pt body, ≥14pt header. |
| `schema_quadrant` | 2×2 семантическое позиционирование (impact/effort, scope/autonomy, etc.) | s13 «scope of task × autonomy» / s21 «cost × value» | **Axis labels INSIDE** quadrant как scale markers (не снаружи рамки). Direction-of-scale явно: arrow + low/high пометки на концах оси. Точки/markers центрированы в своём подквадранте, не overflow. Font axis ≥14pt, sub-labels ≥11pt. |
| `schema_layered` | Стек уровней / архитектурные слои (HW → OS → Framework → App) | s11 «4 уровня абстракции AI» | **Bottom-aligned** (общая нижняя граница, не центрирование). Component caption per layer (не пустой box). Max 4 уровня. Каждый layer обозначен и его роль явна (label + 1 фраза описания). |
| `schema_cycle` | Циклический процесс / повторяющийся flow (chat loop, RAG cycle) | s16 «цикл диалога с моделью» | **Explicit start** (entry point с label «начало» / иконка USER / pulse marker) **+ continue** (loop arrow явный, не подразумеваемый). Max 6 элементов (более — split на этапы). Direction (CW / CCW) обозначен arrow heads. |
| `schema_pipeline` | Линейная последовательность шагов с трансформацией данных | s15 «pipeline RAG / agent» | **RIGHT_ARROW MSO_SHAPE** для стрелок (не filled_rect+rotated_triangle гибрид — выглядит сломанно). Owner annotations (кто делает шаг: USER / MODEL / TOOL) если многосубъектный. Unified language sub-labels (RU only — не mix RU/EN). |
| `schema_timeline` | Временная шкала событий | s07 «история AI 1956-2026» | **Em-dash** между датой и событием (не двоеточие, не break-line — даёт single-line layout). Pivot year (ключевая дата трансформации) ≥2× размер обычной даты. Max 3 события на горизонтальную полосу. Year labels не пересекают band borders. |
| `schema_architecture` | Системная диаграмма с актёрами и связями | s18 «архитектура AI-агента» | **USER actor explicit** (человек явно нарисован, не подразумевается). **Bidirectional arrows** где полу-петли реальны (не one-way когда логически two-way). Connectors labeled (что течёт по стрелке). |

Каждый subtype mandates **Schema Readability Checklist pass** (§5.5) перед accept. Designer не может объявить slide done, не пройдя checklist.

### Правила для `assertion_visual` (главный тип)
- **Заголовок слайда = assertion** — полное предложение-тезис, например «Главный вопрос курса — не "можно ли AI?", а "НУЖНО ли и ГДЕ?"». Не «Введение». Не «Цели лекции».
- **Визуал в центре** = доказательство тезиса (схема / число / изображение / icon-композиция). Не декоративная картинка.
- **Не больше 4 буллетов**, если без визуала — заменить на текстовый блок крупным шрифтом.
- **Speaker notes** — что говорит преподаватель (1-3 абзаца).
- **Visual motif Ocean rounded box** — обязательно обрамляет главный контент-блок.

### Правила для `cover`
- **Визуально distinct** от content slides (subtle background tint `#F4F7FA`, крупная типография 60-72pt, decorative lecture number, hero motif).
- **Subtitle/hook** — короткая навигационная фраза (1 строка). НЕ обещание («за 75 мин разберёмся»), НЕ дублирование central question из content.
- **БЕЗ** Ocean rounded box motif (motif принадлежит content слайдам).
- **БЕЗ** методических footers (LO codes, продолжительность — для методиста, не для аудитории).

---

## 5. Visual-loop workflow

**Принцип Anthropic** (буквально работает): «**Assume there are problems. Your job is to find them. A first render without issues indicates insufficient scrutiny. Perform at least one fix-and-verify cycle before declaring success.**»

**Минимум 3 итерации на слайд. Обычно 3-7.** Если на 3-й итерации «всё ок» — недостаточно критики, найди что улучшить.

```
1. PLAN — choose slide type + visual concept (icon? chart? diagram? illustration?)
2. PREP visuals — download icons (curl), recolor (sed/ImageMagick), generate charts (QuickChart), build diagrams (mermaid CLI or shape composition)
   Все assets в library/lectures/lec-NN/rendered/assets/{icons,charts,diagrams,illustrations}/
3. GENERATE — build slide via PowerPoint MCP (BLANK layout + shapes + manage_text + manage_image)
4. CONVERT:
     cd library/lectures/lec-NN/rendered
     libreoffice --headless --convert-to pdf lec-NN-pilot.pptx
     pdftoppm -r 150 -png lec-NN-pilot.pdf snapshots/iter
5. INSPECT — Read PNG через Claude vision. Active checking:
   - контраст текст/фон (WCAG AA min 4.5:1)
   - иерархия (главное больше, второстепенное мелче)
   - spacing/baseline (нет дыр и слипания)
   - image proportions (не сплющен)
   - цвета только из палитры
   - НЕТ accent line под title, НЕТ красного, НЕТ дублирования
   - визуал работает на assertion
   - text wraps аккуратные (не «перево / д»)
6. FIX через MCP — учти limitation [#54-3] (нет update_shape_position → full rebuild presentation на каждой итерации)
7. RE-SNAPSHOT + RE-INSPECT
8. Repeat 5-8. **Min 3 iter** на слайд.
9. LOG в rendered/iteration-log.md (per-slide section: что делал, что увидел, что менял)
```

### Pre-flight checklist (Anthropic principle перед invoking pipeline)

- [ ] Read this README (§1-§5 как минимум).
- [ ] Read `notes/mcp-limitations.md` — известные грабли PowerPoint MCP.
- [ ] Read `notes/decisions.md` (последний раздел) — anti-patterns каталог.
- [ ] Verify tools: `mmdc --version`, `convert --version`, `rsvg-convert --version`, `libreoffice --headless --version`, `pdftoppm -v`.
- [ ] Verify PowerPoint MCP: `mcp__powerpoint__get_server_info` отвечает.

### Post-render QA loop (после стабильной версии)

3 QA-агента запускаются **параллельно**:
- `presentation-critic` — методист + визуальный (yaml + md + PNG).
- `student-simulator` — студент в зале (только PNG + видимые speaker notes).
- `reader-simulator` — 2 режима: `text-only` (md ДО рендера), `rendered` (PNG+notes через 2 недели).

Orchestrator сводит отчёты в `qa-reports/{date}/SYNTHESIS.md`, решает 3-5 главных правок, делает fix-итерацию, ре-рендер.

---

## 5.5 Schema Readability Acceptance Gate (ENFORCED)

Любой schema slide (matrix / quadrant / layered / cycle / pipeline / timeline / architecture) **обязан** пройти 5-этапный gate перед designer-self-approve. Без gate-pass — slide не считается готовым к QA-агентам.

### Шаги (mandatory, в порядке)

1. **Schema Readability Checklist pass** — designer проходит per-subtype checklist (§4 правила выше). Cross-ref `presentation-designer.md` за полный per-type form.
2. **5-Second Test pass** — designer мысленно показывает PNG студенту: «За 5 секунд ты понял главную мысль schema?». Если не уверен — fail.
3. **Projector Readability (50% zoom) pass** — открыть PNG, уменьшить mental zoom до 50% (имитация задних рядов аудитории). Axis labels, owner annotations, sub-labels всё ещё читаемы (≥14pt при оригинальном render для axis, ≥11pt для sub).
4. **Cross-Slide Redundancy check pass** — designer грепает по предыдущим slides: эта схема не дублирует визуал/данные другого слайда (например, bar chart на s04 + s17 — не делать).
5. **Iconography Discipline pass** — иконки одного семейства (Lucide / Heroicons / Phosphor — не mix), recolor в Ocean palette, размер consistent внутри слайда (±10%).

### Логирование

Каждый gate-step **логируется** в `rendered/iteration-log.md` per slide:

```
## sNN [iter K] — schema_quadrant
- Iter changes: axis labels moved INSIDE quadrant; gold marker on Q4
- Inspected PNG: snapshots/iter5/sNN.png
- Schema Readability Checklist: PASS (axis inside, font 14pt, markers contained)
- 5-Second Test: PASS («understood: high-impact + low-effort = quick wins»)
- Projector 50%: PASS
- Cross-slide redundancy: PASS (no dup with s04/s17)
- Iconography: PASS (Lucide, Ocean recolor)
- Verdict: ACCEPT for QA agents
```

Если хоть один step fail — designer продолжает visual loop (§5), не передаёт на QA.

---

## 5.6 Visual Loop iteration cap (ENFORCED)

| Cap | Значение | Действие |
|---|---|---|
| **Min** | 3 итерации на слайд (existing Anthropic principle) | Без 3-iter — slide не может быть declared done. |
| **Max** | **7 итераций на слайд (NEW)** | Hard cap. На 7-й итерации если schema всё ещё не проходит §5.5 gate → **escalate**. |

### Escalation (на iter 7 без pass)

Designer **обязан** остановиться и emit escalation report:

```
## ESCALATION — sNN, iter 7
- Subtype: schema_cycle
- Что пробовали: 6 vertical steps → linear flow → 2 USER icons → ...
- Что не сходится: «cycle direction» не считывается студентом за 5 сек
- Гипотеза: schema concept may need redesign — возможно cycle не подходит, нужен dialogue-form
- Recommend: orchestrator + book-editor пересмотреть assertion слайда
```

Escalation = **stop** для designer, **trigger** для orchestrator: пересмотреть концепт слайда (assertion / type / source-of-truth chapter §) **до** продолжения visual loop. Не перерасходовать iteration capacity на неправильный концепт.

### Per-iteration log контракт

Каждая итерация логируется в `rendered/iteration-log.md`:

```
## sNN [iter K]
- Inspected: snapshots/iter{K-1}/sNN.png — что увидел (1-3 фразы)
- Changed: что поменял (per element: shape coords / text / color / icon)
- Re-snapshot: snapshots/iter{K}/sNN.png
- Schema Readability Checklist: PASS / FAIL (что fail)
- 5-Second Test: PASS / FAIL
- Verdict: continue / accept / escalate
```

Без per-iter лога — итерация не считается проведённой.

---

## 6. `deck.yaml` schema (минимальная, расширяется по необходимости)

```yaml
deck:
  lecture_number: 1
  title: "Введение — AI вокруг нас"
  audience: "бакалавры ИУ6 МГТУ Баумана"
  duration_min: 75
  central_question: "Как инженеру ИУ6 попасть в оставшиеся 10% AI-пилотов?"
  learning_outcomes: [LO1, LO4, LO6, LO7]
  language: ru

slides:
  - id: s01
    file: slides/s01-ice-breaker-cv.md
    type: live_demo
    duration_min: 3
    assertion: "Narrow AI работает на ноутбуке без облака — рабочая инженерная лошадка"
    learning_goal: "Эмоциональный hook + снять страх 'AI = магия'"
    visual:
      pattern: external_demo
      backup: assets/code/ice-breaker-cv/backup/screenshot.png
    interaction: live_demo
    references: [yolov8-ultralytics-2023]
```

Поля минимально нужные: `id`, `file`, `type`, `assertion`, `learning_goal`. Остальные — по необходимости.

---

## 7. Папочная раскладка одной лекции

```
library/lectures/lec-01/
  deck.yaml              ← структура deck'а
  slides/
    s01-*.md             ← один слайд = один файл (diff-friendly), markdown с frontmatter
    s02-*.md
    ...
  assets/
    images/, diagrams/, code/
  rendered/
    lec-01.pptx          ← последний рендер
    snapshots/
      s01.png, s02.png, ...
    iteration-log.md     ← лог визуальных циклов (для каждого слайда)
  qa-reports/
    YYYY-MM-DD/
      reader-text-only.md
      presentation-critic.md
      student-simulator.md
      reader-rendered.md
      summary.md
```

---

## 8. Связанные агенты (`.claude/agents/`)

| Агент | Перспектива | Видит |
|---|---|---|
| `presentation-designer` | Визуальный дизайнер deck'а — строит слайды, итерирует visual loop | yaml + md + PNG + tools (PowerPoint MCP, mmdc, QuickChart, ImageMagick) |
| `presentation-critic` | Методист + визуальный ревью | yaml + md + PNG |
| `student-simulator` | Студент в зале (PNG + видимые speaker notes) | только PNG + видимые speaker notes |
| `reader-simulator` | Студент через 2 недели; **2 режима**: `text-only` и `rendered` | text-only: только md; rendered: PNG + notes |

Каждый агент в своём `.md`-файле начинается с **REQUIRED READING:** этого README.

`deck-editor` агент v1 (Google Slides обёртка) **удалён** в #56 — orchestration теперь через `/build-deck` skill + presentation-designer + 3 QA.

---

## 9. Anti-patterns — НЕ делаем

Полный каталог поддерживается в `notes/decisions.md` § «2026-05-12 — Presentation pipeline». **Перед сборкой обязательно прочитай.** Здесь — top-22 (10 base + 12 schema/visual из Лекции 1 v3 production).

### Base (1-10)

1. ❌ **Accent lines под titles** (Anthropic AI-tell).
2. ❌ **Title+Body универсально** — каждый слайд имеет конкретный тип.
3. ❌ **Generic blue/red palettes** — только Ocean + Teal + Gold.
4. ❌ **Text-only слайды без визуала** — каждый слайд имеет ≥1 визуал.
5. ❌ **Centered body text** — body left-aligned, title центрировать ситуативно.
6. ❌ **Repeating identical layouts** — каждый distinct.
7. ❌ **Familiar CTA tone** («УГАДАЙ», «ты») — уважительная «вы».
8. ❌ **Magic-pill framing** — exploratory navigation tone.
9. ❌ **Methodist comments на слайдах** — в speaker notes.
10. ❌ **Native add_chart PowerPoint MCP** — Office 2010 вид → QuickChart → PNG.

### Schema / visual (11-22, добавлено после Лекции 1 v3)

11. ❌ **Cycle without explicit start** — `schema_cycle` без entry point (label «начало», USER icon, pulse marker). Студент не знает, откуда читать. Fix: add explicit start + continue arrow.
12. ❌ **Matrix <75% fill (skeleton accepted)** — `schema_matrix` с пустыми ячейками = недопустимо. Skeleton-формат («заполню на лекции») — anti-pattern. Fix: либо заполнить ≥75%, либо разбить matrix на 2 узких schema.
13. ❌ **Axis labels outside quadrant** — `schema_quadrant` с подписями осей снаружи рамки. Студент не считывает direction-of-scale. Fix: labels INSIDE как scale markers + arrow.
14. ❌ **Layers centred without bottom-anchor** — `schema_layered` с центрированием boxes. Стек не «стоит» визуально. Fix: bottom-aligned (общая нижняя граница).
15. ❌ **Architecture без USER actor** — `schema_architecture` без явного человека. Студент не понимает, кто инициирует/получает. Fix: explicit USER icon + bidirectional arrows где реально two-way.
16. ❌ **Cross-slide chart duplication** — bar chart на s04 и s17 с похожими данными. Cross-slide redundancy. Fix: keep один, на втором — table или callout.
17. ❌ **Mixed RU/EN sub-labels in schema** — pipeline owners «USER / МОДЕЛЬ / TOOL». Inconsistent. Fix: unified language (RU only).
18. ❌ **2-line wraps в event labels** — timeline с переносом «1956 — Дартмут / ская конференция». Ломает single-line layout. Fix: em-dash + abbreviate event если длинно.
19. ❌ **Designer-added content без brief** — subtitle, навигационные маркеры «Вы здесь», тайминг в видимой области, секция «Лектору» в notes — добавлены designer'ом по своей инициативе. Anti-pattern: «do nothing not in task brief». Fix: report opportunity to orchestrator, не add.
20. ❌ **Equal-height boxes для unequal content** — 4 layer boxes одинаковой высоты при разной длине описаний → text overflow или большие пустые поля. Fix: scale heights к контенту, либо abbreviate.
21. ❌ **Inconsistent gold-emphasis across same-tier cards** — на s09 один из 4 равнозначных breakthrough'ов выделен gold без причины. Confusing. Fix: gold = либо «лидер» (data-driven), либо «callback» (один концепт-якорь), либо ничего на equal cards.
22. ❌ **Projector-distance illegibility** — axis font <14pt, sub-labels <11pt при render для 16:9 deck. На задних рядах нечитаемо. Fix: enforce min font sizes per role (axis 14pt, sub 11pt, body 12pt, header 14pt).

---

## 10. Roadmap инструмента (sub-issues EPIC #52)

- **#53** — setup PowerPoint MCP + 3 QA agents + структура. ✅ merged.
- **#54** — 1-слайдный спайк s05b. ✅ merged.
- **#55** — 6-слайдный пилот Лекции 1 (5 итераций v1→v3.6). ✅ merged.
- **#56 (этот этап)** — стабилизация: README final, SKILL rewrite, decisions.md catalog, CLAUDE.md final.
- **#57** — factory: остальные s06-s29 Лекции 1, затем Л2-Л17.

---

## 11. Открытые вопросы

- **list_shapes / get_shape_properties** — отсутствуют в GongRzhe MCP. Форкнуть при реальной потребности (вероятно в #57 при сложных deck'ах).
- **Reference template PPTX** — не понадобился в пилоте (голый python-pptx + примитивы + recolored icons дали хороший результат). Можно добавить при росте сложности.
- **Drive upload + feedback pull** — отложено до момента, когда понадобится внешний рецензент.
- **FLUX через Replicate API** — для AI-сгенерированных hero illustrations. Опционально, $0.003/image. Подключаем когда понадобится.

---

## 12. References

- **Design playbook:** `notes/issue-52-presentations-methodology/design-research.md`
- **Tool catalog:** `notes/issue-52-presentations-methodology/design-superpowers.md`
- **Anti-patterns + iteration journey:** `notes/decisions.md` § «2026-05-12 — Presentation pipeline»
- **MCP limitations:** `notes/mcp-limitations.md`
- **Anthropic pptx skill** (knowledge source, не используется как skill): `github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md`
