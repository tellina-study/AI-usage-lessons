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

15-пунктный каталог поддерживается в `notes/decisions.md` § «2026-05-12 — Presentation pipeline». **Перед сборкой обязательно прочитай.**

Краткий top-10:

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
