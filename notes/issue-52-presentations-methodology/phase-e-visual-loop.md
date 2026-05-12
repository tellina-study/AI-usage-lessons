# Phase E — Визуальный итеративный цикл (упущенный компонент)

**Issue:** #52
**Дата:** 2026-05-12
**Контекст:** ответ пользователя на раунд 2 — «в генерации ты можешь и должен участвовать так, как это делал бы реальный человек: либо полностью создавать слайды через mcp/skills/api, либо править и улучшать то, что сделано инструментально; потом смотреть ВИЗУАЛЬНО что получилось и при необходимости улучшать».

Это **отсутствовавший first-class компонент** в моём proposal'е. У меня был только «render → отчёт». Должно быть «render → визуальный осмотр → правка → re-render → визуальный осмотр → ...».

---

## 1. Что значит «визуальный цикл» в нашем контексте

Claude **мультимодален** — может прочитать PNG/JPG как изображение и описать/раскритиковать то, что видит. Это позволяет агенту работать как дизайнер:

```
[ render initial slide ]
        │
        ▼
[ snapshot slide → PNG ]
        │
        ▼
[ Claude vision: смотрю → описываю → критикую ]
        │
        ├── визуально OK → done
        │
        └── визуально не OK → точечная правка
                │
                ▼
        [ re-render → snapshot → look ]
                │
                ▼
            ... loop ...
```

Это не «отдельный QA-агент» — это **встроенный в сборку deck'а механизм**. Агент-сборщик (`deck-editor` или его наследник) **обязан** после каждого слайда (или пакета) посмотреть результат и либо принять, либо подправить.

---

## 2. Два режима участия агента (как описал пользователь)

### Режим A — полная сборка через MCP/API
Агент создаёт каждый слайд с нуля программными вызовами. Никакого инструментального baseline'а. Полный контроль за каждой формой/текстом/картинкой. Применимо когда:
- Нужен полный контроль (для slide-types типа `assertion_visual` с конкретным позиционированием).
- Инструмент-генератор по итогу не даёт нужный результат.
- Конкретный слайд не вписывается в шаблон.

### Режим B — инструментальный baseline + агент-правки сверху
Инструмент (Marp/Slidev/Pandoc) генерирует «черновой» слайд из markdown. Дальше агент смотрит визуально и:
- если ОК — оставляет.
- если есть мелкие проблемы — правит markdown/CSS/директивы.
- если структурные проблемы — переключается в режим A для этого слайда.

Это «как реальный человек» — пишет в markdown, рендерит, открывает PowerPoint, двигает что-то на 10 пикселей вправо, меняет шрифт.

---

## 3. Что меняется в требованиях к инструменту

Добавляется **новое измерение оценки:**

- **Granular positional control** — может ли агент после первого рендера попросить «сдвинь shape X вправо на 50, увеличь шрифт title до 48pt»? Без полной перерисовки.
- **Snapshot rendering** — есть ли быстрый способ получить PNG слайда после правок?
- **Round-trip** — можно ли применять правки несколько раз без накопления артефактов?

### Сводная по кандидатам с учётом визуального цикла

| Tool | Initial render | Snapshot → PNG | Granular fine-tune | Цикл «как человек» |
|---|---|---|---|---|
| **Google Slides** (workspace-mcp) | `batch_update_presentation` | **`get_page_thumbnail`** (нативный MCP) | `batch_update_presentation` с `updateShapeProperties`, `updateTextStyle`, `updatePageElementTransform` | ✅ всё в одном MCP |
| **Marp** (markdown) | `marp file.md -o file.pptx` | `marp file.md --images png` | edit markdown / CSS class — re-render | ⚠️ непрямой (через source) |
| **Slidev** | `slidev export --format pptx` | `slidev export --format png` | edit markdown / Vue layout — re-render | ⚠️ непрямой |
| **PptxGenJS** (TS code) | `node build.ts` | libreoffice headless → png | edit TS code, re-run | ⚠️ через код |
| **Marp + python-pptx** (hybrid) | Marp PPTX baseline | libreoffice → png | python-pptx правит готовый PPTX напрямую | ✅ есть escape hatch |

**Что меняется:** Google Slides **возвращается в кандидаты**, потому что:
- `get_page_thumbnail` — нативный MCP-инструмент, агент сразу видит результат.
- `batch_update_presentation` — агент может править positional/style без перерисовки.
- Никаких внешних зависимостей (libreoffice, npm, python-pptx, playwright).

Но при этом проблема пользовательского опыта v0 («ужасная и уродливая») сохраняется: причина не только в отсутствии визуального цикла, но и в:
- Использовании предопределённых layouts (`TITLE_AND_BODY`).
- Отсутствии библиотеки slide-types.
- Отсутствии типографики/цветовой схемы.

С **визуальным циклом** + **BLANK layout + custom shapes** + **single accent color + system font** + slide-types — Google Slides может выдать результат заметно лучше v0.

---

## 4. Новая рекомендация по инструменту (после учёта визуального цикла)

Я **меняю свою предыдущую рекомендацию** (Marp → ?). Теперь вижу **3 жизнеспособных варианта**, и стоит сделать **сравнительный спайк** перед выбором.

### Вариант 1: **Google Slides + визуальный цикл** (workspace-mcp full path)
- **Source:** `library/lectures/lec-NN/deck.yaml` + `slides/*.md` (репо).
- **Build:** subagent через `batch_update_presentation`, BLANK layouts + кастомные shapes.
- **Visual loop:** `get_page_thumbnail` → Claude vision → правки через `batch_update_presentation`.
- **Drive:** native, файл уже в Drive после рендера.
- **Comments:** native Google Slides comments.
- **Reproducibility:** `last-render.json` с полным транскриптом операций.

**Плюсы:** ноль новых зависимостей; всё в одном MCP; нативные комменты для D1; thumbnails сразу.
**Минусы:** «Google Slides look» (но смягчается с визуальным циклом + дисциплиной layout'ов); D0 пользователь сказал «выкидываем» — но это было ДО учёта визуального цикла.

### Вариант 2: **Marp + python-pptx + libreoffice** (markdown-source-of-truth)
- **Source:** `library/lectures/lec-NN/deck.yaml` + `slides/*.md` с Marp directives.
- **Build:** `marp` cli → PPTX baseline.
- **Visual loop:** `libreoffice --headless --convert-to png` → Claude vision → если правка нужна: edit markdown/CSS (быстрая) или python-pptx fix (точечная).
- **Drive:** загрузка PPTX через `mcp__workspace-mcp__create_drive_file`.
- **Comments:** Drive импортирует PPTX в Google Slides view; внешний рецензент комментирует там, мы пуллим через `list_presentation_comments`.
- **Reproducibility:** markdown commit + (если был python-pptx fix) скрипт правки в `slides/sNN.fix.py`.

**Плюсы:** markdown-first, индустриально-стандартный PPTX, есть escape hatch для тонких правок, multi-format (HTML/PDF тоже).
**Минусы:** 3 инструмента (marp, python-pptx, libreoffice) — больше setup; reproducibility сложнее (где жить fixes); python-pptx меняет PPTX, после чего повторный `marp` сотрёт правки → нужна дисциплина «либо markdown, либо .fix.py».

### Вариант 3: **PptxGenJS programmatic + libreoffice**
- **Source:** TS-код в `tools/presentation-build/src/lectures/lec-NN.ts`.
- **Build:** `node build.ts` → PPTX.
- **Visual loop:** libreoffice → png → Claude vision → edit TS → re-run.
- **Drive:** upload PPTX.

**Плюсы:** полный контроль, всё в одном языке.
**Минусы:** **не markdown-source** (репо-first философия частично страдает — слайды это код, не текст). Для соло-мейнтейнера сравнительно тяжело.

---

## 5. Спайк нового формата (рекомендую заменить spike v1)

**Старый спайк (Phase E v1):** Marp vs Slidev на s05.
**Новый спайк (с учётом визуального цикла):** **3 параллельных мини-спайка на одном слайде s05**.

| Спайк | Инструмент | Время | Что измеряем |
|---|---|---|---|
| A | Google Slides + визуальный цикл | ~30 мин | сколько итераций, насколько хорошо выглядит, удобен ли цикл |
| B | Marp + python-pptx fix + libreoffice | ~45 мин | сколько шагов до acceptable, удобен ли hybrid setup |
| C | PptxGenJS | пропускаем (явно тяжело) | — |

После спайка А и B — выбираем по **визуальному результату** и **сложности setup'а**. Не по идеологии.

Спайк делает subagent с инструкцией **«работай как дизайнер: рендер → посмотри → улучшай»**. Я (orchestrator) смотрю результаты, представляю пользователю.

---

## 6. Что меняется в агентах (presentation-critic)

`presentation-critic` теперь **обязательно работает с PNG-снимками** (не только с yaml/md).

```yaml
agent: presentation-critic
inputs:
  - deck.yaml
  - slides/*.md
  - rendered/slide-png/sNN.png   # ОБЯЗАТЕЛЬНО
methodology:
  - look at PNG first
  - then cross-check with assertion in deck.yaml
  - flag visual issues: overflow, hierarchy, contrast, decorative imagery
  - flag pedagogical issues: assertion mismatch, content density
output: per-slide findings (P0/P1/P2)
```

`student-simulator` и `reader-simulator` — **уже видят только PNG** (по нашему дизайну в Phase D), так что для них ничего не меняется.

**Дополнительно** — **вшитый «inline-критик» в build-process** (не отдельный агент):
- После каждого пакета слайдов сборщик сам делает thumbnail и проверяет: переполнение? отрезанный текст? картинка не вписалась?
- Это «sanity check» уровня (не методический), но он экономит итерации с критиком.

---

## 7. Reproducibility при визуальном цикле

**Проблема:** если агент вручную сдвинул что-то на «10px вправо», как воспроизвести?

**Решение через `last-render.json`:**
```json
{
  "presentation_id": "...",
  "deck_yaml_hash": "sha256:...",
  "render_log": [
    {"step": 1, "kind": "create_slide", "type": "assertion_visual", "slide_id": "..."},
    {"step": 2, "kind": "insert_text", "shape": "title", "value": "..."},
    {"step": 3, "kind": "visual_fix", "slide_id": "...", "operation": "move_shape", "params": {...}, "reason": "title overflowed image"}
  ]
}
```

Re-render = replay render_log из чистого состояния. Идемпотентно. Все «человеческие» правки агента залогированы и воспроизводимы.

→ Для пилота: сохраняем `render_log`, не делаем replay. После пилота — добавляем replay-режим.

---

## 8. Запросы на обновление в proposal'е (Phase C delta)

1. **Visual loop — first-class шаг build-process'а**, не QA-after-thought.
2. **Tool choice пересматриваем** — Google Slides возвращается в кандидаты; добавляем спайк A vs B.
3. **`presentation-critic` смотрит PNG** обязательно.
4. **`render_log`** в `last-render.json` для воспроизводимости человеческих правок.
5. **Inline-sanity-check** в сборке (не отдельный агент): переполнение, отрезанный текст.

---

## 9. Что нужно от пользователя (раунд 3)

1. **Согласен на сравнительный спайк A (Google Slides) vs B (Marp+python-pptx)?** Я бы делал параллельно: 2 subagent'а, каждый рендерит s05 и итерирует визуально 3-5 раз, на каждой итерации саммари «что изменил». В конце — оба варианта PNG + лог итераций для твоего выбора.
2. **«Как человек» включает редкие правки в Drive напрямую от внешнего рецензента?** Если да — это аргумент в пользу варианта 1 (Google Slides) или варианта 2 с PPTX (open в Drive как Slides). Вариант 3 (TS code) вообще исключает прямую правку.
3. **Reproducibility до уровня «replay log» — критична для пилота или достаточно «коммит markdown'а + ручной список правок»?** Я бы для пилота просто логировал, без replay.
4. **Где живёт `render_log`** — в `library/lectures/lec-01/rendered/last-render.json` (рядом с PPTX/snapshots) — OK?

После твоих ответов — финальный апдейт proposal'а и старт F.0 (спайк).
