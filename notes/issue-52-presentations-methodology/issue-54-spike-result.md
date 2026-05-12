# Sub-issue #54 — Результат спайка (s05b)

**EPIC:** #52
**Issue:** #54
**Branch:** issue-54-pilot-spike-s05
**Дата:** 2026-05-12

---

## TL;DR

- **Итераций:** 6 из 7 разрешённых.
- **Финальный результат:** годен для публичной лекции.
- **Рекомендация по template-подходу для #55:** **(a) Без community-template** — нативного python-pptx + Blank layout + примитивов (rectangle + textbox) хватает для `assertion_visual`. Перейти на template имеет смысл только если в #55 окажется, что 2-3 других слайд-типа требуют сложной типографики/брендинга.

---

## 1. Pipeline валидирован живьём

Полный цикл отработал без затыков:

```
PowerPoint MCP (create_presentation, add_slide, manage_text, add_shape)
  → save_presentation → .pptx
  → libreoffice --headless --convert-to pdf  (LibreOffice 24.2.7.2)
  → pdftoppm -r 150 -png  (poppler 24.02.0)
  → Read tool на PNG  (Claude vision читает картинку)
  → анализ → MCP правка → re-render
```

Все 6 итераций прошли по этому циклу без ошибок инфраструктуры. Render одной итерации (PPTX→PDF→PNG): ~2 секунды.

---

## 2. Финальный визуальный результат

Файлы:
- Source: `/home/levko/AI-usage-lessons/library/lectures/lec-01/slides/s05b-course-frame.md`
- Deck spec: `/home/levko/AI-usage-lessons/library/lectures/lec-01/deck.yaml`
- Финальный PPTX: `/home/levko/AI-usage-lessons/library/lectures/lec-01/rendered/spike/s05b-final.pptx`
- Финальный PNG: `/home/levko/AI-usage-lessons/library/lectures/lec-01/rendered/spike/s05b-final.png`
- Лог итераций: `/home/levko/AI-usage-lessons/library/lectures/lec-01/rendered/spike/iteration-log.md`

Слайд содержит 4 визуальные зоны:
1. **Сверху** — assertion полным предложением (24pt bold, dark navy, центр).
2. **Узкая красная линия** — визуальный разделитель.
3. **Cream callout box (252,245,240) + красный accent bar слева** — внутри центральный вопрос «Как инженеру ИУ6 попасть в оставшиеся 10%?» (38pt bold red, 2 строки).
4. **Снизу** — stakes-параграф со статистикой Gartner + АНО ЦЭ (14pt gray, 3 строки).

Иерархия читается с расстояния, переполнений нет, ничего не отрезано. Стилистика подходит для публичной лекции в МГТУ Баумана.

---

## 3. Рекомендация: template-подход для пилота #55

### Вывод: **community-template НЕ нужен на старте #55**

Аргументы:
- Шесть итераций без template'а дали публикабельный результат. Дополнительный визуальный «вес» добавили простые примитивы (callout box + accent bar).
- Community-templates (SlidesCarnival, Slidesmania) обычно идут с готовыми мастер-слайдами и кастомными layout'ами. Преимущество — экономия на дизайне; цена — потеря контроля над позиционированием. В нашем visual-loop control имеет приоритет.
- `apply_professional_design` MCP-tool (color schemes, темы) **не пробовался в этом спайке**, чтобы не смешивать переменные. Можно протестировать в #55 как промежуточный шаг между «голый python-pptx» и «полноценный template».

### Что попробовать в #55, если slide-types окажутся сложнее

Порядок предпочтения:
1. **Сначала** — `apply_professional_design(operation="apply_theme", color_scheme="modern_blue"|...)`: добавляет тему без потери контроля.
2. **Потом** — кастомный locked-template: 3-4 master-слайда (cover, assertion_visual, two_column, full_image), руками собранный в PowerPoint и подключённый через `create_presentation_from_template`. Это путь #56.
3. **В крайнем случае** — community SlidesCarnival/Slidesmania: только если нужен «брендовый» вид и контроль над типографикой не критичен.

---

## 4. Limitations PowerPoint MCP, обнаруженные на спайке

| # | Limitation | Серьёзность | Workaround на спайке | Рекомендация для #55+ |
|---|-----------|-------------|----------------------|----------------------|
| 1 | **Нет `list_shapes` / `get_shape_properties`** | Высокая | Держал mental-model порядка add_text/add_shape, отслеживал shape_index по порядку добавления | Форкнуть GongRzhe MCP, добавить 2 простых wrapper-tool над `slide.shapes` (return name, type, left, top, width, height, текст если есть) |
| 2 | **`format_runs` ломает inline-runs** (`tools/content_tools.py:456-459`): каждый run после первого попадает в новый paragraph через `text_frame.add_paragraph()` вместо `paragraph.add_run()`. Также теряется alignment. | Высокая для типографики | Отказался от inline-эмфазиса цифр, использую uniform color | Зафиксить в форке: добавить ключ `inline: true` в run, либо новую операцию `format_inline_runs` |
| 3 | **Нет API для перемещения/изменения существующего shape** (`update_shape_position`, `resize_shape`, `delete_shape` отсутствуют) | Средняя | Каждая итерация = новая presentation с нуля. Дёшево для одного слайда, дорого для деки | Не блокер для #55 (deca в 6 слайдов перерендеривается за <30 сек), но для деки в 29 слайдов уже узкое место. Форкнуть и добавить shape-mutation tools. |
| 4 | **`vertical_alignment="middle"` не до конца работает** в комбинации с `auto_fit`: текст оседает в верхней части бокса, оставляя пустоту снизу | Низкая | Явно подгоняю height бокса под визуальную высоту текста (ит. 5→6) | Достаточно. В #55 закладывать height ≈ 1.0 × визуальной высоты. |
| 5 | **LibreOffice добавляет drop-shadow к rectangle-shape по умолчанию** при PDF-конверсии — ненужный артефакт | Низкая | Принимаю — в реальном PowerPoint клиента тени могут быть/не быть в зависимости от темы | Можно явно `shadow=False` через python-pptx — но MCP-tool это не выставляет. Не блокер. |
| 6 | **Нет атомарной операции «текст + box-фон»** — для callout приходится складывать 2 shape (rect под текст + textbox сверху) с ручным позиционированием | Низкая | Это нормальный python-pptx паттерн, работает | OK, в #56 добавить SKILL-helper `add_callout_block(text, bg, accent_color, ...)` поверх MCP. |

### Что нужно добавить в форк (приоритет для #55-#56)

**P1 (высокий — мешает реальной работе):**
- `list_shapes(slide_index)` → list of {shape_index, type, name, left, top, width, height, text?}
- `format_inline_runs` (новая операция) или фикс `format_runs` (сохранять paragraph)

**P2 (средний — нужно для масштабирования):**
- `update_shape_position(shape_index, left?, top?, width?, height?)`
- `delete_shape(shape_index)`

**P3 (косметика):**
- `add_callout_block` — composite tool

---

## 5. Готовность к sub-issue #55

- Pipeline работает живьём, цикл 5-7 итераций реалистичен (6 на простом слайде).
- Source-of-truth `slides/sNN.md` + `deck.yaml` подтверждены — переносятся в pilot.
- Slide-type `assertion_visual` имеет рабочий рецепт: 4 зоны (assertion / accent line / callout box+accent bar+question / stakes).
- Limitations задокументированы; форк MCP можно отложить до момента, когда конкретная limitation реально блокирует слайд.
- 3 QA-агента (`presentation-critic`, `student-simulator`, `reader-simulator`) можно безопасно запускать на готовом deck в #55.
