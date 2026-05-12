# s05b — Iteration log (sub-issue #54 spike)

Лимит: 5–7 итераций. Цель — оценить, можно ли без template'а сделать слайд `assertion_visual` пригодным для широкой публики.

Слайд 4:3 (10×7.5"). Layout: `Blank` (index 6).

Финальный результат: `s05b-final.pptx` (= `s05b-iter-6.pptx`), `s05b-final.png`.
**Принят к использованию: да** — после 6 итераций результат пригоден для публичной лекции.

---

## Iteration 1 — Baseline (Blank layout, 3 текстовых блока)

**What I did:**
- `create_presentation(id="s05b-spike")` → 4:3, 11 layouts, default 9144000×6858000 EMU.
- `add_slide(layout_index=6)` (Blank).
- `manage_text(operation="add")` ×3:
  - assertion: top=0.4, left=0.5, w=9, h=1, fs=24, bold, center, dark navy [20,30,60]
  - central question: top=2.5, h=2.5, fs=44, bold, center, vmid, red [200,30,30]
  - stakes: top=5.8, h=1.3, fs=14, gray [80,80,80]
- `save_presentation` → `s05b-iter-1.pptx`
- `libreoffice --headless --convert-to pdf` + `pdftoppm -r 150 -png` → `s05b-iter-1-1.png`
- `Read` PNG → vision describe.

**What I saw on PNG:**
- Иерархия читается: маленький тёмный заголовок сверху, огромный красный вопрос по центру, мелкий серый стейкс снизу.
- Assertion помещается в 2 строки.
- Центральный вопрос — 3 строки, читается, но визуально wall-of-text.
- Стейкс на самом дне, выглядит оторванно (как footer).
- Чистый белый фон, никаких визуальных акцентов.
- Ничего не отрезано, переполнения нет.

**Problems found:**
- P1: Stakes-блок «висит» внизу, выглядит как footer, а не как контекст вопроса.
- P1: Центральный вопрос — 3 строки, было бы сильнее в 2.
- P1: Нет визуальной связи между assertion ↔ central question.
- P2: Скучный белый фон.
- P2: «5–10%» в стейксе — главная цифра-якорь, не выделена.

**Decision for next iter:**
- Уменьшить шрифт центрального вопроса до 40 → попасть в 2 строки.
- Передвинуть стейкс выше (top=5.2) и добавить горизонтальную линию-разделитель над ним.
- Bold «10%» в стейксе через text_runs.
- Добавить тонкую цветную линию-акцент под assertion.

---

## Iteration 2 — `format_runs` ловушка

**What I did:**
- Новый presentation `s05b-iter-2`, тот же layout 6.
- assertion (без изменений).
- `add_shape(rectangle)` 3" × 0.05" в y=1.65 — красная линия-акцент под заголовком.
- central question fs=40, w=9.4 — для 2 строк.
- `add_shape(rectangle)` 7" × 0.02" в y=5.3 — серый разделитель над стейксом.
- Plain `manage_text(operation="add")` placeholder для stakes (shape_index=4).
- `manage_text(operation="format_runs", shape_index=4, text_runs=[...])` — 7 inline runs с разными bold/colors для выделения «80%», «90%», «5–10%».

**What I saw on PNG:**
- Assertion — норм.
- Красная линия — норм, добавляет ритм.
- Центральный вопрос — норм, 2 строки.
- Серый разделитель — норм.
- **Stakes сломан полностью:** каждый run на отдельной строке, выравнивание сбилось на left, 8 строк вместо 2, низ обрезан.

**Problems found:**
- **P0 — bug в `format_runs`:** в `tools/content_tools.py:456-459` каждый run после первого попадает в новый paragraph (`text_frame.add_paragraph()`), а не в текущий. Inline-форматирование разных run-ов в одном параграфе невозможно через эту операцию. Подтверждено чтением исходника MCP-сервера.
- P0: Alignment сбилось на left (format_runs не сохраняет alignment текстового бокса).
- P1: Stakes overflow за пределы слайда.

**Decision for next iter:**
- Отказаться от `format_runs` для inline-эмфазиса. Выделение цифр перенести в backlog (для #56 — либо форкнуть MCP, либо использовать несколько текстовых боксов рядом).
- Stakes как plain text с явным `\n` между предложениями.

---

## Iteration 3 — Чистый baseline без format_runs

**What I did:**
- Новый presentation `s05b-iter-3`.
- assertion (как раньше).
- Красная линия-акцент 3" в y=1.65.
- Центральный вопрос: top=2.4, h=2.4, fs=40, bold, center, vmid, red.
- Серый разделитель 7" в y=5.5.
- Stakes: один `manage_text add` с явным `\n`, fs=14, center, gray.

**What I saw on PNG:**
- Иерархия отличная.
- Центральный вопрос — 2 строки, доминирует.
- Stakes — 4 строки (каждое предложение wraps), читается, помещается.
- Красный акцент + серый разделитель — добавляют ритм, разводят зоны.
- Слайд цельный, без переполнений.

**Problems found:**
- P1: Большая пустая зона между центральным вопросом (~y=4.5) и серым разделителем (y=5.5) — слайд выглядит немного «sparse».
- P2: «Gartner 2025).» в первой строке стейкса перенос неудобный («2025)» отдельно).
- P2: Центральный вопрос недостаточно visually dominant — он плавает в воздухе, без визуального контейнера.

**Decision for next iter:**
- Добавить cream callout box (subtle background) за центральным вопросом + красный левый «accent bar» (3-4mm), чтобы дать вопросу визуальный вес.

---

## Iteration 4 — Cream callout + красный accent bar

**What I did:**
- Новый presentation `s05b-iter-4`.
- assertion + красная линия (как iter-3).
- `add_shape(rectangle)` cream [252,245,240], 8.6" × 2.5" в (0.7, 2.5) — callout box.
- `add_shape(rectangle)` red [200,30,30], 0.12" × 2.5" в (0.7, 2.5) — левый accent bar.
- Центральный вопрос: left=1, top=2.6, w=8.2, h=2.3, fs=40 — внутри callout с padding.
- Stakes (как iter-3, без серого разделителя — callout сам разводит зоны).

**What I saw on PNG:**
- Callout преобразил слайд: центральный вопрос теперь имеет визуальный вес.
- **Регрессия:** центральный вопрос снова на 3 строки (callout уже 8.6" vs 9.4" в iter-3, ширина текста 8.2" — wraps к «Как инженеру ИУ6 / попасть в оставшиеся / 10%?»).
- Stakes — 3 строки, читается, OK.
- Drop shadow callout'а от libreoffice — ненужный, но не критично.

**Problems found:**
- P1: Регрессия 2→3 строки в центральном вопросе.
- P2: Callout box чуть уже комфортного.

**Decision for next iter:**
- Расширить callout до 9.4" (вернуть ширину iter-3) и текст центрального вопроса до w=9.
- Уменьшить fs центрального вопроса с 40 до 38 как страховку от 3-line wrap.

---

## Iteration 5 — Расширенный callout, fs 38, 2 строки

**What I did:**
- Новый presentation `s05b-iter-5`.
- assertion + красная линия (как раньше).
- callout 9.4" × 2.5" в (0.3, 2.4); accent bar 0.12" × 2.5" в (0.3, 2.4).
- Центральный вопрос: left=0.6, top=2.5, w=9, h=2.3, fs=38, vmid, center, red.
- Stakes: top=5.6, w=9, fs=14, center.

**What I saw on PNG:**
- Центральный вопрос на 2 строки. Доминирует.
- Callout пропорциональный, accent bar — узнаваемый паттерн «pull quote».
- Stakes — 3 строки, читается, естественно располагается под callout.
- **Микро-issue:** текст вопроса визуально сидит в верхней половине callout, есть пустое пространство снизу. Vertical_alignment=middle не сработал в полной мере (видимо python-pptx auto_fit конфликтует).

**Problems found:**
- P1: Текст в callout не идеально центрирован вертикально — пустота снизу ~30%.
- P0: Ничего критичного.

**Decision for next iter:**
- Уменьшить высоту callout с 2.5 до 2.0 и поднять его на y=2.7 — текст займёт callout плотнее.
- Передвинуть стейкс на y=5.4 (соответствует новому положению callout).

---

## Iteration 6 — Финальная подгонка пропорций

**What I did:**
- Новый presentation `s05b-iter-6`.
- assertion + красная линия (как раньше).
- callout 9.4" × **2.0"** в (0.3, **2.7**); accent bar тех же размеров.
- Центральный вопрос: left=0.6, top=2.75, w=9, h=1.9, fs=38, vmid, center, red.
- Stakes: top=**5.4**, w=9, fs=14.

**What I saw on PNG:**
- Центральный вопрос на 2 строки, заполняет callout плотнее (нижний margin визуально ушёл).
- assertion + accent line + callout + stakes — 4 чёткие визуальные зоны с воздухом между ними.
- Слайд цельный, проф. вид, никаких overflow/cut-off.
- Stakes хорошо разводится с callout (зазор ~0.7", естественный).
- Иерархия 100% читается с 5 метров.

**Problems found:**
- P2: Callout drop shadow от libreoffice (артефакт рендера, в реальном PPT в PowerPoint его не будет — стандартный python-pptx auto-shadow).
- P2 (косметика): «Gartner 2025).» в первой строке стейкса перенос — minor; принимаем.

**Decision:** **Accept.** Сохраняю как `s05b-final.pptx` / `s05b-final.png`.

---

## Сводка итераций

| # | Что добавили | Результат | Ключевая проблема |
|---|--------------|-----------|-------------------|
| 1 | Baseline 3 текстовых бокса | Удивительно неплох | Sparse, без визуальных акцентов |
| 2 | format_runs для bold чисел | **Регрессия** | format_runs ломает inline-runs (bug) |
| 3 | Откатились на plain text + 2 разделителя | Чисто, но sparse | Большая пустота в середине |
| 4 | Cream callout + accent bar | Большой шаг вперёд | Регрессия 2→3 строки |
| 5 | Расширенный callout, fs 38 | Почти готово | Vmid не сработал плотно |
| 6 | Уменьшили высоту callout до 2.0 | **Принято** | — |

Итого: 6 итераций, лимит 5-7 — в рамках.
