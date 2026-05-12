# Дизайн-плейбук для учебных презентаций (issue #55 redo)

**Назначение.** На основе этого playbook создаётся агент `presentation-designer` и пересобираются 6 пилотных слайдов Лекции 1. Ничего «энциклопедического» — только то, что нужно для практической работы. Все источники проверены HTTP-запросами 2026-05-12.

---

## 1. Inspiration references

Не «гуглить идеи», а смотреть, как делают серьёзные образовательные decks 2024–2026:

- **Stanford CS231n / CS224n** — slide PDFs на курсовом сайте; assertion-headlines, большие схемы, много диаграмм-нотаций. Хорошие примеры серьёзного академического стиля без скуки. (`https://cs231n.stanford.edu/`, `https://web.stanford.edu/class/cs224n/slides/`)
- **MIT OCW 6.034 / 6.S191** — slides MIT Deep Learning. Чёрный фон + цветные диаграммы (контраст ради проектора), большие иконки как метафоры разделов. (`https://ocw.mit.edu/`)
- **fast.ai lectures** — Jeremy Howard. Слайды короткие, плотный визуал (notebook-screenshots, диаграммы), assertion-headlines, минимум текста. (`https://www.fast.ai/`)
- **Strange Loop / GOTO conference talks** — например, доклады Hillel Wayne, Niki Vazou. Большие схемы, типографика как структурный элемент. (`https://www.thestrangeloop.com/sessions.html`, `https://gotopia.tech/`)
- **3Blue1Brown** (видео, не слайды) — манимация, но приёмы переносимы: один концепт = одна композиция, цвет несёт семантику. (`https://www.3blue1brown.com/`)
- **Linear `linear.app/method`** — не образовательный, но эталон серьёзного «product+content» визуала: пастельный тёмный фон, чистая типографика, тонкие иконки. (`https://linear.app/method`)
- **Refactoring UI book** (Adam Wathan, Steve Schoger) — base text для всех решений ниже. (`https://refactoringui.com/`)

Чего избегаем как референс: corporate-PowerPoint-templates с слайдов SlidesGo/Canva; «Apple keynote-style» полноэкранные фото с гигантским текстом (хорошо для product launch, неработоспособно для технической лекции).

---

## 2. Принципы (7, без воды)

1. **Assertion-evidence** (Michael Alley, Penn State). Заголовок слайда — полное предложение-тезис (≤2 строки). Тело слайда — визуальное доказательство тезиса (схема / число / картинка). Bullet-list **запрещены** в этой парадигме. Уже зафиксировано в `tools/presentation-build/README.md` §1.
2. **Multimedia principle (Mayer)**. Учат лучше «слова + картинка» вместе, чем только слова. **Каждый assertion_visual слайд обязан иметь визуал** (icon/illustration/chart/shape diagram). Слайд без визуала = сломанный слайд.
3. **Spatial contiguity**. Текст-подпись держать рядом с визуалом, к которому он относится (≤1 inch на 1920×1080 эквивалент). Не выносить подпись на противоположный край.
4. **Data-ink ratio (Tufte)**. Больше «чернил» на данные, меньше — на декор. Для нашей текущей боли это значит: **никаких декоративных красных полосок-подчёркиваний под каждым заголовком**. Полоса оправдана только если она маркирует семантику (например, разделитель секций).
5. **Визуальная иерархия через размер + контраст, не через цвет**. Главный элемент — самый крупный и/или с самым тёмным фоном. Цвет — для семантики (категории, состояния), а не для «оживления».
6. **Negative space — это контент**. ~30–40% площади слайда должно быть пустым. Если всё занято — глаз не знает, куда смотреть.
7. **Один слайд = одна мысль**. Если на слайде 2 идеи — это 2 слайда. Лучше дека из 30 фокусированных слайдов, чем из 15 «с двумя темами на каждом».

Anti-patterns (то, что мы сейчас делаем):
- ✗ Каждый слайд = большой цветной заголовок + красная декоративная полоса под ним → шум.
- ✗ Числа крупно красным шрифтом без визуального якоря (43%/27%/23%/15% на s04) — это **не** chart, это типографика. Для распределения нужен bar/donut/dot.
- ✗ Empty grey rectangle как «здесь будет картинка» (s01) — лучше явная иконка-плейсхолдер с подписью «live feed», чем серый прямоугольник.

---

## 3. Источники иконок (CDN-friendly, проверено)

Все URL ниже проверены `curl` 2026-05-12. Все библиотеки **MIT** или Apache 2.0 — свободны для использования в учебных материалах **без attribution**.

### Lucide (рекомендуем как primary)

- License: ISC (≈ MIT).
- 1500+ иконок, line-style, 24×24 grid, stroke 2px, `currentColor`.
- URL pattern (jsDelivr, без редиректа):
  ```
  https://cdn.jsdelivr.net/npm/lucide-static@latest/icons/<name>.svg
  ```
  Альтернатива через unpkg (302→200): `https://unpkg.com/lucide-static@latest/icons/<name>.svg`.
- Browse: `https://lucide.dev/icons/`
- Примеры релевантных имён: `camera`, `bot`, `bar-chart-3`, `pie-chart`, `users`, `hand`, `target`, `book-open`, `lightbulb`, `cpu`, `brain`, `eye`, `arrow-right`, `trending-up`.

### Tabler Icons

- License: MIT, 6000+ иконок, line + filled варианты.
- URL pattern:
  ```
  https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/outline/<name>.svg
  https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/filled/<name>.svg
  ```
- Browse: `https://tabler.io/icons`

### Phosphor Icons

- License: MIT, 9000+ иконок, 6 weights (`thin/light/regular/bold/fill/duotone`).
- URL pattern:
  ```
  https://cdn.jsdelivr.net/npm/@phosphor-icons/core@latest/assets/regular/<name>.svg
  https://cdn.jsdelivr.net/npm/@phosphor-icons/core@latest/assets/bold/<name>.svg
  https://cdn.jsdelivr.net/npm/@phosphor-icons/core@latest/assets/duotone/<name>.svg
  ```
- Browse: `https://phosphoricons.com/`

### Heroicons (Tailwind UI команда)

- License: MIT, ~300 иконок, два размера 24/20, два варианта outline/solid.
- URL pattern (raw GitHub, jsDelivr тоже работает):
  ```
  https://raw.githubusercontent.com/tailwindlabs/heroicons/master/optimized/24/outline/<name>.svg
  https://raw.githubusercontent.com/tailwindlabs/heroicons/master/optimized/24/solid/<name>.svg
  https://raw.githubusercontent.com/tailwindlabs/heroicons/master/optimized/20/solid/<name>.svg
  ```
- Browse: `https://heroicons.com/`
- Примечание: `unpkg.com/heroicons@latest/...` редиректит, путь к SVG другой; используй raw.githubusercontent.

### Material Symbols (Google)

- License: Apache 2.0, 3000+ иконок, fill/wght/grade variants.
- URL pattern (gstatic):
  ```
  https://fonts.gstatic.com/s/i/short-term/release/materialsymbolsoutlined/<name>/default/24px.svg
  ```
- Альтернатива (raw GitHub):
  ```
  https://raw.githubusercontent.com/google/material-design-icons/master/symbols/web/<name>/materialsymbolsoutlined/<name>_24px.svg
  ```
- Browse: `https://fonts.google.com/icons`

### LobeHub icons (для AI-логотипов)

- License: MIT — содержит логотипы DeepSeek, ChatGPT, Claude, Gemini, Mistral и десятков других AI-сервисов.
- URL pattern (jsDelivr, проверено):
  ```
  https://cdn.jsdelivr.net/npm/@lobehub/icons-static-svg@latest/icons/<name>.svg
  https://cdn.jsdelivr.net/npm/@lobehub/icons-static-png@latest/dark/<name>.png
  https://cdn.jsdelivr.net/npm/@lobehub/icons-static-png@latest/light/<name>.png
  ```
- Имена: `deepseek`, `openai`, `chatgpt`, `claude`, `gemini`, `mistral`, `qwen`. **Yandex/GigaChat скорее всего отсутствуют** — для них либо взять нейтральный `cpu`/`bot` icon из Lucide, либо вручную скачать с brand-страниц (Яндекс: `yandex.ru/company/general_info/yandex_brandbook/`).

### Правило выбора

В рамках одной презентации — **одна семья иконок** (например, только Lucide или только Phosphor regular). Смешивать стили (line + duotone + filled из разных семейств) — анти-паттерн, расфокусирует.

---

## 4. Источники иллюстраций

### unDraw (рекомендуем как primary)

- License: open-source, **без attribution** для коммерческого и личного использования.
- Цвет настраивается на сайте: один параметр primary color → SVG скачивается перекрашенным.
- Прямого URL-pattern для скачивания **нет** — нужно через сайт. Workaround: один раз скачать набор тематических иллюстраций руками, положить в `library/lectures/lec-NN/assets/illustrations/`. Кэш = local source.
- Browse: `https://undraw.co/illustrations`
- Релевантные ключевые слова для нашего курса: `artificial intelligence`, `data trends`, `online survey`, `programmer`, `analytics`, `idea`, `engineering team`, `presentation`.

### Storyset (Freepik)

- License: Freepik license — free with attribution (для учебных слайдов attribution в speaker notes / footer вполне допустимо).
- Стиль более красочный, есть варианты `flat`, `pana`, `bro`, `cuate`, `rafiki`, `amico`.
- Цвет настраивается на сайте.
- Browse: `https://storyset.com/`

### Lukasz Adam

- License: free (MIT-like), минималистичные иллюстрации.
- Browse: `https://lukaszadam.com/illustrations`

### DrawKit

- License: смесь — есть free-tier (без attribution для проектов), есть premium.
- Browse: `https://drawkit.com/free-illustrations`

### Стратегия использования

Не качать «всё подряд». Подход:
1. На одну лекцию — максимум 1–2 иллюстрации (на cover + на один ключевой слайд).
2. Один стиль во всей лекции (либо unDraw, либо Storyset, не миксовать).
3. Цвет иллюстрации согласован с палитрой деки.
4. Для большинства слайдов нужны **иконки**, а не иллюстрации. Иконки масштабируются и не отвлекают.

---

## 5. PowerPoint MCP image embedding — что реально работает

**Подтверждено чтением исходника `office-powerpoint-mcp-server==2.0.7` (`tools/content_tools.py:511-624`):**

### `manage_image` accepts:

| `source_type` | `image_source` | Поддержка |
|---|---|---|
| `"file"` (default) | абсолютный путь к локальному файлу | ✅ работает |
| `"base64"` | base64-кодированные байты (записываются как `.png`) | ✅ работает (only `.png` content) |
| URL | — | ❌ **НЕ поддерживается** |

### Поддерживаемые форматы (через python-pptx + PIL внутри):

- ✅ PNG — основной формат, рекомендуется.
- ✅ JPEG — ок для фото.
- ✅ GIF, BMP, TIFF — поддерживаются PIL, но не используем.
- ✅ EMF — vector, поддерживается python-pptx нативно (но конвертация SVG→EMF на Linux неудобна).
- ❌ **SVG — НЕ поддерживается** ни python-pptx, ни PIL. Issue в upstream открыт уже годы (`scanny/python-pptx#394`, `#652`).

### Workflow для иконок (SVG → PNG → embed):

Поскольку все источники в §3 отдают SVG, нужен промежуточный шаг конвертации. На WSL Ubuntu 24.04 в нашем env:

- `librsvg2-2` стоит, но **CLI `rsvg-convert` отсутствует** (это пакет `librsvg2-bin`). Нужно `sudo apt install -y librsvg2-bin`.
- Python `cairosvg` и `Pillow` **не установлены**. Ставить: `pip install --user --break-system-packages cairosvg Pillow`.
- Node 22 доступен — можно поставить `npm i -g @resvg/resvg-js-cli` как альтернатива.

**Рекомендуемый recipe (выбрать один и зафиксировать):**

```bash
# Вариант A — librsvg CLI (быстро, нативно)
sudo apt install -y librsvg2-bin
rsvg-convert -w 256 -h 256 in.svg -o out.png

# Вариант B — Python cairosvg (without sudo)
pip install --user --break-system-packages cairosvg
python3 -c "import cairosvg; cairosvg.svg2png(url='in.svg', write_to='out.png', output_width=256)"
```

Цвет SVG-иконки задаётся атрибутом `stroke` или `fill` в SVG. Lucide использует `currentColor` — нужно sed-заменой подставить нужный HEX перед конвертацией:

```bash
sed -e 's/currentColor/#0F172A/g' lucide-camera.svg > /tmp/coloured.svg
rsvg-convert -w 256 -h 256 /tmp/coloured.svg -o camera-navy.png
```

### Layout кэша иконок

```
library/lectures/lec-NN/assets/icons/
  src/                 ← original SVG (commit-friendly)
    camera.svg
    bar-chart-3.svg
    ...
  rendered/            ← PNG для embed (.gitignore — re-rendered on demand)
    camera-navy-256.png
    bar-chart-3-blue-256.png
```

### `apply_picture_effects` и enhance

`apply_picture_effects(slide_index, shape_index, effects)` принимает словарь эффектов. `manage_image(operation="enhance", ...)` отдельная — берёт PIL-параметры (brightness, contrast, saturation, sharpness, blur, filter). Эти tools полезны если у нас есть фотография, которую надо desaturate/blur (например, фон-photo). Для иконок и иллюстраций они не нужны — управляйте цветом на этапе SVG.

### Известные limitations (см. `notes/mcp-limitations.md`)

- Нет `update_shape_position` / `delete_shape` → если иконка уехала не туда, пересобирай слайд с нуля.
- Нет `list_shapes` → держи mental-model порядка добавления, иначе `shape_index` для `apply_picture_effects` поплывёт.

---

## 6. drawio MCP — что реально умеет

3 tools: `open_drawio_xml`, `open_drawio_csv`, `open_drawio_mermaid`.

**Что они делают:** генерируют draw.io диаграмму **в формате URL для онлайн-редактора** (`https://embed.diagrams.net/?...` с inline-данными в query string). Они **открывают редактор**, не возвращают файл. Для встраивания в PPTX это **бесполезно напрямую** — PNG/SVG они не отдают.

**Подтверждено** beta-описанием инструмента в схеме: «Opens the draw.io editor with a diagram from XML content. Use this to view, edit, or create diagrams in draw.io format». Цель — interactive viewing, не render-pipeline.

### Альтернативы для diagrams:

1. **Schema-as-shape primitives (рекомендуем для нашего пайплайна).** Согласно `tools/presentation-build/README.md` §1.5 — «Diagrams as shapes». Используем `add_shape` + `add_connector` PowerPoint MCP. Преимущество: native PPTX shapes, можно править post-hoc. Минус: ручной layout. Хорошо для 3–7-узловых схем.

2. **Mermaid CLI → SVG → PNG → embed.** Если нужна реальная диаграмма (flowchart, sequence) — Mermaid CLI:
   ```bash
   npm i -g @mermaid-js/mermaid-cli
   mmdc -i diagram.mmd -o diagram.png -w 1600 -H 900 -t neutral -b transparent
   ```
   `-t neutral` или `-t default` — приличные стандартные темы. Кастомная тема через `-t base -c config.json` (color override).

3. **draw.io desktop CLI (если установлен) → PNG.** Не в нашем env по умолчанию. Если понадобится — `apt install drawio` либо AppImage.

**Решение:** для пилота #55 — только schema-as-shapes. Mermaid CLI добавим в #56 или #57 при первой реальной потребности в неструктурируемой shape-диаграмме (sequence, ER).

---

## 7. Per-slide design recipes для s01–s05b

Контент фиксирован (см. `library/lectures/lec-01/slides/sNN-*.md`). Это **только визуальный рецепт**.

### s01 — live_demo (camera ice-breaker)

**Текущая боль:** пустой grey rectangle 4:3 без подписи в центре + 2 строки текста.

**Рецепт:**
- Заголовок-assertion (тот же): «Narrow AI работает на ноутбуке без облака — рабочая инженерная лошадка». Шрифт 36pt, navy, выравнивание left, ~40% ширины слайда сверху.
- В центре — **большая иконка камеры с диагональной стрелкой к иконке `bot` или `cpu`**, а не пустой rectangle:
  - Lucide `camera` (1) → arrow → Lucide `cpu` (2) → arrow → text-block с фразой «N people detected · ~30 fps» в monospace-шрифте.
  - Цвет иконок: navy (#0F172A) на cream-фоне; стрелки — accent blue (#2563EB).
  - Размер иконок: 96–128px после rendering.
- Под визуалом — caption «Live camera feed на проекторе» курсивом, 14pt, slate-500 (#64748B). Это явный плейсхолдер вместо текущего серого квадрата.
- Низ слайда — мелким шрифтом source-line: «YOLOv8 (Ultralytics, 2023) · ~30 fps real-time на CPU · без интернета».

**Что embed:**
- `lucide camera.svg` → recolor → PNG 128×128.
- `lucide cpu.svg` или `lucide bot.svg` → PNG 128×128.
- 2 connector-стрелки `add_connector(connector_type="straight", ..., color=[37, 99, 235])`.

### s02 — cover

**Текущая боль:** просто текст + декоративная красная полоса.

**Рецепт (Hybrid: Cover + Hero-illustration):**
- Top-left — корпоративная мета мелким шрифтом «МГТУ им. Н.Э. Баумана · ИУ6 · [дата]», 14pt slate-500.
- Заголовок: «Лекция 1. Введение — AI вокруг нас», 44pt, navy.
- **Главный элемент — центральный вопрос «Как инженеру ИУ6 попасть в оставшиеся 10%?»** — крупно (60pt), wraps в 2 строки, выровнен по центру, без декоративной красной плашки. Контраст обеспечивается размером, не цветом.
- Над/слева от вопроса — небольшая декоративная иллюстрация unDraw `artificial-intelligence` или Storyset `ai-tech` в фирменном blue, ~30% ширины, opacity 0.85. Не доминирует, акцент на тексте.
- Низ — LO/время/преподаватель, 14pt slate-500.
- Background — мягкий вертикальный градиент cream→white или solid white.

**Что embed:**
- 1 PNG-иллюстрация unDraw (predownloaded в `assets/illustrations/`).

### s03 — poll questions

**Текущая боль:** «1» и «2» крупным красным шрифтом + текст вопросов. Нет визуального ритма.

**Рецепт:**
- Заголовок-assertion: «Сначала — ваша оценка, потом — данные». Уменьшить размер до 32pt — это не главный слайд.
- Два больших card-блока бок-о-бок (rounded-rectangle через `add_shape("ROUNDED_RECTANGLE", ...)`, fill #F8FAFC, line #CBD5E1, 0.5pt):
  - **Card 1.** Лево-верх: иконка `lucide hand` (или `users`) 48px navy. Справа от иконки: «Какой % россиян использовали AI в 2025?» 24pt navy. Под вопросом — 4 chips-варианта `<20% / 20-40% / 40-60% / >60%` (`add_shape("ROUNDED_RECTANGLE", small)`, fill light-blue #DBEAFE, text 14pt navy).
  - **Card 2.** Аналогично с иконкой `lucide message-square` или `terminal`. Вопрос: «Кто использовал AI сегодня? Для чего?». Chips: `код / текст / перевод / другое`.
- Низ слайда — self-study note курсивом 12pt slate-500.

**Что embed:**
- 2 lucide-иконки PNG.
- 8 rounded-rectangle shapes (2 cards + 6 chips).

### s04 — poll reveal data

**Текущая боль:** все цифры — крупный красный текст. Нет chart, нет визуального якоря «51%», нет сравнения долей рынка.

**Рецепт (data block):**
- Заголовок-assertion: «Разница между вашей оценкой и реальностью — карта ваших слепых зон про AI». 28pt navy.
- Слайд делится на 2 секции горизонтально (top 60%, bottom 35%, gap 5%).
- **Top секция — «51%» через donut chart:**
  - `add_chart(chart_type="DOUGHNUT", ...)` с данными `[51, 49]`, цвет accent blue (#2563EB) для 51% и slate-200 для 49%.
  - Слева от donut — крупный текст «**51%** россиян использовали AI в 2025», 32pt navy.
  - Под текстом — caption «ВЦИОМ 2025 · генеративные модели для текста / кода / перевода» 12pt slate-500.
- **Bottom секция — bar chart долей рынка LLM:**
  - `add_chart(chart_type="BAR_CLUSTERED", categories=["DeepSeek","ChatGPT","YandexGPT","GigaChat"], series_values=[[43,27,23,15]], color_scheme="colorful")`. Горизонтальный bar — лучше читается для долей рынка.
  - Опционально: рядом с категориями — мини-логотипы из LobeHub (DeepSeek/ChatGPT доступны; YandexGPT/GigaChat — нейтральная иконка `lucide cpu`).
  - Caption «Сумма >100% — респонденты могли указать несколько вариантов · Bloomberg 2025» 12pt slate-500.
- **Внизу инсайт-плашка** удалить — она дублирует заголовок. Заголовок и так инсайт.

**Что embed:**
- 1 donut chart (`add_chart`).
- 1 horizontal bar chart (`add_chart` с `chart_type="BAR_CLUSTERED"`).
- 2–4 PNG-логотипа AI-сервисов (предзагруженные).

### s05a — instructor card

**Текущая боль:** просто 3 placeholder с цифрами 1/2/3 крупно. Нет «лица».

**Рецепт:**
- Заголовок-assertion: «Кто я и почему мне это важно». 32pt navy, выравнивание left.
- Слайд делится на 2 колонки: левая 35% — placeholder photo, правая 65% — 3 пункта.
- **Левая колонка:**
  - Rounded rectangle (`ROUNDED_RECTANGLE`, fill slate-100, line slate-300) ~3.5"×4.5" → внутри `lucide user` иконка 192px slate-400 + label «фото преподавателя» 12pt italic slate-500. Это явный placeholder, который потом заменится реальной фотографией.
- **Правая колонка — 3 пункта:**
  - Каждый пункт — иконка слева (32px, navy) + текст справа (24pt navy). Иконки разные:
    - Пункт 1 (опыт с AI): `lucide briefcase` или `lucide cpu`.
    - Пункт 2 (почему важен): `lucide target` или `lucide compass`.
    - Пункт 3 (на выбор): `lucide heart` или `lucide users`.
  - Между пунктами — gap ~0.4", без разделителей.
- Низ — пометка `draft-pending-content` курсивом 11pt slate-500.

**Что embed:**
- 1 placeholder rectangle + 1 user-icon PNG.
- 3 lucide-иконки PNG.

### s05b — course frame + central question

**Текущая боль:** заголовок + декоративная полоса + большой красный central-question + 4 строки stakes мелким текстом. Нет инфографики 90% / 10%.

**Рецепт (assertion_visual с инфографикой):**
- Заголовок-assertion: «Главный вопрос курса — не "можно ли AI?", а "НУЖНО ли и ГДЕ?"». 30pt navy.
- **Центральный визуал — funnel-инфографика 90% / 10% слева, центральный вопрос справа:**
  - Левая половина (40% ширины): простая funnel-схема через shapes.
    - Большой trapezoid сверху (fill slate-200): «100 AI-пилотов в РФ».
    - Узкий rectangle снизу (fill accent blue #2563EB): «10 в проде».
    - Между ними — стрелка вниз с подписью «−90% откатываются» 14pt slate-600.
    - Альтернатива: big-number block — «90%» (huge slate-400) over «10%» (huge accent blue) с разницей в размере.
  - Правая половина (55%): central-question «Как инженеру ИУ6 попасть в оставшиеся 10%?» 36pt navy, выровнен left, занимает 3 строки.
- Под визуалом, мелким шрифтом 12pt slate-500: «Gartner 2025 · АНО ЦЭ 2025 · AI-компонента = модель / LLM-API / классификатор».

**Что embed:**
- Funnel: 2 trapezoid/rectangle shapes + 1 connector + текстовый блок.
- Опционально: 1 lucide иконка `funnel` или `filter` маленькая в качестве маркера секции.

---

## 8. Recommended palette

### Главная палитра — «Bauman Modern» (используем по умолчанию)

Опирается на синий как фирменный цвет МГТУ Баумана (подтверждено в гайдлайнах их дочерних структур: «синий — основной цвет Университета, связан с инновациями и технологиями»). Tailwind-style 9-shades scale, AA-accessible.

| Role | HEX | Tailwind alias | Где |
|---|---|---|---|
| Primary text / heading | `#0F172A` | slate-900 | Заголовки, body text |
| Secondary text | `#475569` | slate-600 | Captions, labels |
| Muted text / placeholder | `#94A3B8` | slate-400 | Footer-meta, draft-tags |
| Background | `#FFFFFF` | white | Default slide bg |
| Soft surface (cards) | `#F8FAFC` | slate-50 | Card-fills, dividers |
| Border / hairline | `#CBD5E1` | slate-300 | Card outlines |
| Accent primary | `#2563EB` | blue-600 | CTA, key data, иконки |
| Accent dark | `#1D4ED8` | blue-700 | Hover-equivalent, emphasis |
| Accent light bg | `#DBEAFE` | blue-100 | Chip backgrounds, highlights |
| Success (для charts) | `#059669` | emerald-600 | Positive data |
| Warning (для charts) | `#D97706` | amber-600 | Attention data |
| Danger / pitfall | `#DC2626` | red-600 | Только для true-negative («90% провалов») |

**Rationale:** убираем cream + navy + дешёвый красный → переходим на чистый white + slate + blue-600. Slate (вместо чёрного для текста) — мягче на проекторе, не «давит». Accent blue 600 близок к Tailwind / Linear / Stripe — современный и серьёзный, при этом коррелирует с Bauman blue. Красный остаётся в палитре, но **только для семантики «провал/проблема»**, не для декора.

### Запасная палитра — «IBM Carbon Inspired» (если основная надоест или нужен dark-mode)

Опирается на IBM Carbon — корпоративный, очень читаемый, AA-AAA accessible.

| Role | HEX | Carbon alias |
|---|---|---|
| Primary text | `#161616` | gray-100 |
| Secondary text | `#525252` | gray-70 |
| Background | `#FFFFFF` | white |
| Surface | `#F4F4F4` | gray-10 |
| Border | `#E0E0E0` | gray-20 |
| Accent | `#0F62FE` | blue-60 (IBM signature) |
| Accent dark | `#0043CE` | blue-70 |
| Accent light bg | `#EDF5FF` | blue-10 |

Использовать одну палитру на всю лекцию — не миксовать в одной деке.

### Для charts (`add_chart` color_scheme)

Built-in `color_scheme` PowerPoint MCP принимает: `"colorful"`, `"monochromatic"`, `"office"`. Из них приличный — `"colorful"` (но проверить визуально). Если не подходит — задать цвета руками через post-edit shape-fill (но для chart shapes это limited).

---

## 9. Recommended fonts

**В PPTX-доставке шрифт должен быть либо системным, либо embedded в файл.** PowerPoint поддерживает font embedding (Save → Tools → Save Options), но через python-pptx это нетривиально. Для безопасности — выбираем **шрифты, которые либо системные на Windows/macOS, либо доступны через Google Fonts (студент откроет файл в browser-PowerPoint и шрифт подгрузится).**

### Рекомендуемая иерархия

| Tier | Шрифт | Используется для | Backup |
|---|---|---|---|
| Heading | **Inter** | Заголовки, big numbers | Calibri, Arial |
| Body | **Inter** (тот же — упрощает) | Основной текст | Calibri, Arial |
| Mono | **JetBrains Mono** или **IBM Plex Mono** | Code snippets, demo output (s01) | Consolas, Courier New |

**Альтернативы (если Inter не нравится):**
- **IBM Plex Sans** — тот же fit, чуть более «инженерный», kazak-Cyrillic поддержка отличная.
- **Manrope** — современный, geometric, хорошо читается.
- **Roboto** — безопасный default, но «слишком GoogleProduct».

**Правило размеров (в pt, для 16:9 1920×1080):**
- Heading (assertion): 28–36pt
- Sub-heading: 20–24pt
- Body: 16–18pt
- Caption / source: 11–13pt
- Big number (hero): 60–96pt

### Cyrillic + Latin

Inter, IBM Plex Sans, Manrope — все имеют полный Cyrillic glyph set. **Не использовать Roboto Slab или fancy display fonts** — у них Cyrillic неполный.

### Установка / verify

```bash
# Inter via Google Fonts (для проверки в браузере)
curl -o /dev/null "https://fonts.googleapis.com/css2?family=Inter"

# Скачать .ttf для embedding в Linux WSL (опционально)
fc-list | grep -i inter   # check if installed
sudo apt install -y fonts-inter  # Ubuntu 24.04
```

В `manage_fonts` PowerPoint MCP использовать:
```python
manage_fonts(operation="set_font", slide_index=N, shape_index=M, font_name="Inter", ...)
```

---

## 10. Quick action checklist для presentation-designer агента

Этот checklist агент идёт сверху вниз для каждого слайда:

### Pre-flight (один раз на начало работы)

- [ ] Проверить и при необходимости установить: `librsvg2-bin` (`sudo apt install -y librsvg2-bin`), либо `pip install --user --break-system-packages cairosvg Pillow`.
- [ ] Установить (если нет) шрифт Inter: `sudo apt install -y fonts-inter`.
- [ ] Создать `library/lectures/lec-01/assets/icons/{src,rendered}/`.
- [ ] Создать `library/lectures/lec-01/assets/illustrations/`.
- [ ] Скачать 1–2 unDraw illustrations (для s02 cover) с правильным цветом #2563EB и положить в `assets/illustrations/`.

### На каждый слайд

- [ ] Прочитать `slides/sNN-*.md` — это **content source-of-truth**, не менять.
- [ ] Прочитать рецепт §7 для этого слайда.
- [ ] Определить какие иконки нужны (по списку §3) → скачать SVG → recolor (sed currentColor → HEX из палитры) → конвертировать SVG→PNG (rsvg-convert) → положить в `assets/icons/rendered/`.
- [ ] Построить слайд: `add_shape` для блоков, `manage_image` для иконок и иллюстраций (`source_type="file"`, абсолютный путь), `add_chart` для charts (s04), `add_connector` для стрелок.
- [ ] Использовать палитру §8 (Bauman Modern) — все цвета только из неё.
- [ ] Использовать шрифт Inter везде; Mono только для code (s01).
- [ ] Применить assertion-evidence: заголовок = тезис; визуал доминирует.
- [ ] Snapshot → render PNG (existing pipeline через libreoffice + pdftoppm).
- [ ] Visually inspect через Read tool. Чек: визуал занимает ≥40% площади? есть негативное пространство? цвет несёт семантику, а не декорирует?
- [ ] Если provided — итерация.

### Post-build

- [ ] Обновить `iteration-log.md` для каждого слайда.
- [ ] Обновить `notes/mcp-limitations.md` если нашлись новые ограничения (особенно вокруг `add_chart`, иконки-recolor).
- [ ] Проверить, что `assets/icons/src/*.svg` закоммичены, `assets/icons/rendered/*.png` — в `.gitignore` (re-rendered on demand).

### Гейт перед мерджем

- [ ] Все 6 слайдов имеют ≥1 визуальный элемент (иконка / иллюстрация / chart / схема), не считая заголовок.
- [ ] Ни на одном слайде нет «empty grey rectangle» как плейсхолдера.
- [ ] Цветовая палитра консистентна (только из §8).
- [ ] Шрифт консистентен (Inter + опц. Mono).
- [ ] Snapshots обновлены, диффабельны на PR.

---

## Sources

- [How to Create an Assertion-Evidence Presentation (Penn State, Alley)](https://cpb-us-e1.wpmucdn.com/sites.psu.edu/dist/7/13153/files/2008/10/Assertion-Evidence-Slides-Instruction_Set.pdf)
- [Assertion-Evidence Approach](https://www.assertion-evidence.com/)
- [Mayer's 12 Principles of Multimedia Learning](https://www.digitallearninginstitute.com/blog/mayers-principles-multimedia-learning)
- [Tufte's Principles of Data-Ink (EDAV class)](https://jtr13.github.io/cc19/tuftes-principles-of-data-ink.html)
- [Refactoring UI — Building Your Color Palette (preview)](https://refactoringui.com/previews/building-your-color-palette)
- [IBM Carbon Design System — Color guidelines](https://carbondesignsystem.com/elements/color/usage/)
- [Lucide Icons (lucide.dev)](https://lucide.dev/)
- [Tabler Icons (GitHub)](https://github.com/tabler/tabler-icons)
- [Heroicons (Tailwind labs, GitHub)](https://github.com/tailwindlabs/heroicons)
- [Phosphor Icons CDN (jsDelivr)](https://www.jsdelivr.com/package/npm/@phosphor-icons/core)
- [Material Symbols Guide (Google Fonts)](https://developers.google.com/fonts/docs/material_symbols)
- [unDraw — Open-source illustrations](https://undraw.co/)
- [Storyset FAQ (license)](https://storyset.com/faqs)
- [LobeHub icons (DeepSeek and other AI logos)](https://lobehub.com/icons/deepseek)
- [python-pptx SVG support issue #394](https://github.com/scanny/python-pptx/issues/394)
- [Linear brand guidelines](https://linear.app/brand)
- [Stripe accessible color systems](https://stripe.com/blog/accessible-color-systems)
- [Bauman MSTU (Wikipedia)](https://en.wikipedia.org/wiki/Bauman_Moscow_State_Technical_University)
- [Inженириум МГТУ им. Баумана brand guide (synий = primary)](https://inginirium.ru/brand/)
- [draw.io export documentation](https://www.drawio.com/doc/faq/export-diagram)
- [draw.io MCP server (jgraph)](https://github.com/jgraph/drawio-mcp)
- [Mermaid CLI](https://github.com/mermaid-js/mermaid-cli)
- [office-powerpoint-mcp-server (PyPI)](https://pypi.org/project/office-powerpoint-mcp-server/)
