# Design superpowers для агента `presentation-designer`

**Назначение.** Дополнение к `design-research.md` (issue #55 redo). Здесь — список **инструментов**, которые дают агенту реальную дизайнерскую силу: генерация чартов, диаграмм, иллюстраций, recolor иконок, brand-консистентность. Все варианты проверены 2026-05-12 (web research). Цены ≤ $5/мес или free.

**Контекст окружения** (проверено локально):
- `node v22.22.1`, `npm 10.9.4` — есть.
- `python3`, `uvx`, `curl` — есть.
- `office-powerpoint-mcp-server` v2.0.7 уже подключён.
- `convert`/`magick` (ImageMagick) — **отсутствует**, нужна установка.
- Snapshot pipeline (`libreoffice` + `pdftoppm`) уже работает.

---

## 1. Anthropic Skills Marketplace — findings

### 1.1. Официальный репозиторий `anthropics/skills`

URL: https://github.com/anthropics/skills (~73k stars, Apache 2.0 + source-available).
Marketplace JSON: https://github.com/anthropics/skills/blob/main/.claude-plugin/marketplace.json

**Три плагина** (= три namespace'а в `/plugin marketplace`):

| Plugin | Skills внутри |
|---|---|
| `document-skills` | `pptx`, `docx`, `xlsx`, `pdf` |
| `example-skills` | `algorithmic-art`, `brand-guidelines`, `canvas-design`, `doc-coauthoring`, `frontend-design`, `internal-comms`, `mcp-builder`, `skill-creator`, `slack-gif-creator`, `theme-factory`, `web-artifacts-builder`, `webapp-testing` |
| `claude-api` | `claude-api` |

**Установка в Claude Code** (одной командой):
```
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

### 1.2. Релевантные для нас skills (анализ SKILL.md)

#### `pptx` (КРИТИЧНО — must install)

- **Что делает:** Полный цикл: создание PPTX с нуля через **PptxGenJS** (Node.js), редактирование через unpack→edit-xml→pack, чтение через `markitdown`, конверсия в JPG через soffice+pdftoppm.
- **Дизайн-составляющая:** включает 9 фирменных палитр (Midnight Executive, Forest & Moss, Coral Energy и т.д.), правила контраста (60/30/10), typography pairing, anti-patterns (запрет дефолтного синего, запрет accent-lines под заголовками — характерный AI-tell, который мы сами делали).
- **Workflow:** Generate → Convert → Inspect → Fix → Re-verify (минимум 1 цикл visual QA до завершения).
- **Зависимости:** `pip install "markitdown[pptx]" Pillow`, `npm install -g pptxgenjs`, `soffice`, `pdftoppm`.
- **Польза для нас:** **PptxGenJS даёт декларативный JS API для слайдов** — это альтернатива нашему `office-powerpoint-mcp-server` для случаев, где MCP слабоват (например, точное позиционирование, нестандартные shape-комбинации, программная генерация N-однотипных слайдов). Не заменяем PowerPoint MCP, а дополняем.

#### `brand-guidelines` (полезно как референс паттерна)

- Применяет фирменный стиль (палитра, типографика) к артефактам. У Anthropic это their own brand: Poppins/Lora, дарк #141413 + оранжевый #d97757.
- **Для нас:** не использовать as-is, но **скопировать структуру** для skill'а `tellian-brand-guidelines` (наша палитра + наши шрифты + правила из `design-research.md`).

#### `theme-factory` (умеренно полезно)

- 10 готовых тем (Ocean Depths, Sunset Boulevard, Midnight Galaxy и т.д.) + умеет генерировать новую тему по описанию.
- Каждая тема: hex-палитра + font pairing + контрастные правила.
- **Для нас:** идея для будущего — позволить агенту переключать тему deck'а одной командой. Не на этой итерации.

#### `canvas-design` (НЕ для лекций)

- Создаёт «museum-quality posters/art»: PDF/PNG, философско-художественный подход, **минимум текста, максимум визуала**.
- **Для образовательных слайдов не подходит** — приоритизирует эстетику над дидактической ясностью. Может пригодиться для cover-слайда курса, не больше.

#### `algorithmic-art` (мимо)

- Генеративное искусство через p5.js. Для абстрактных backgrounds **не годится** — слишком художественно, не контролируемо.

### 1.3. Третьесторонние skills (из `VoltAgent/awesome-agent-skills`)

Активны и совместимы с Claude Code:
- **`openai/slides`** — альтернативная PPTX-обвязка через PptxGenJS + Playwright validation. Дублирует `anthropics/pptx`, выбираем один.
- **`openai/imagegen`** — генерация изображений через OpenAI Image API. **Платно через OpenAI key** (~$0.04/image для DALL-E 3). Дороже FLUX.
- **`fal-ai-community/fal-generate`** — генерация images/videos через fal.ai. Хорошие модели, нужен fal API key.
- **`figma/figma-generate-design`** — отвергнуто (выше).

### 1.4. Что НЕ нашли (честно)

В Anthropic skills **нет** официальных skills для:
- Charts (как отдельный skill — рендерить надо самим).
- Diagrams (mermaid/plantuml — нет skill, только CLI tools).
- Image generation (нет официального skill, только third-party).
- Infographics как самостоятельной категории.

Дизайн делается **внутри `pptx`** на уровне ручного оформления через PptxGenJS — никаких готовых infographic-templates marketplace не предоставляет.

---

## 2. Image generation MCPs — recommendation

### 2.1. Сравнение вариантов

| MCP / API | Модель | Цена/img | Качество | Авторизация | Style consistency |
|---|---|---|---|---|---|
| **Replicate FLUX MCP** (`awkoy/replicate-flux-mcp`, `GongRzhe/Image-Generation-MCP-Server`) | FLUX.1 Schnell | **$0.003** | очень высокое для бесплатной | Replicate API key (free credits + pay-as-you-go) | через LoRA training (24 img) — для пилота избыточно |
| **fal.ai MCP** (`fal-ai-community/fal-generate`) | FLUX, SD, Recraft | $0.003-0.05 | высокое, sub-second | fal API key | LoRA training |
| **OpenAI Images MCP** | DALL-E 3 / gpt-image | $0.04-0.08 | высокое, weaker prompt adherence | OpenAI key | reference-image input |
| **Pollinations API** (no MCP, plain HTTP) | FLUX, GPT Image, Seedream | **free, no key** | среднее (свободный публичный endpoint) | нет | seed-based |
| **ComfyUI MCP** (local) | любая SD/FLUX модель | бесплатно (своё железо) | максимальное | нет | полная — LoRA, ControlNet, IPAdapter |

### 2.2. Рекомендация: `replicate-flux-mcp`

**Почему:**
- **$0.003/image** = 333 изображения за $1, легко вписаться в бюджет ≤$5/мес (~1600 генераций).
- FLUX.1 Schnell по prompt adherence лучше DALL-E 3, sub-second генерация.
- Replicate имеет MCP-сервер — нативная интеграция с Claude Code.
- Replicate выдаёт URL изображения → `curl` → сохраняем в `assets/` → `manage_image` PowerPoint MCP. Цикл уже отработан на иконках.

**Не рекомендуем:** Pollinations (без контроля качества для прода), OpenAI Images (в 13× дороже без явного выигрыша), ComfyUI (требует локальной GPU).

**Style consistency для образовательного deck.** Для одной лекции (6-15 слайдов с illustrations) самый прагматичный путь — **system prompt с зафиксированным стилем**:
```
"flat illustration, single-color line art, navy #1a2845 strokes on white,
minimal style, educational textbook aesthetic, no shadows, no gradients"
```
Без LoRA training. LoRA train рассмотреть, **только если** через 2-3 лекции стиль начнёт расползаться. Тренировка 1 LoRA ≈ $2-4 на fal.ai/Replicate (24 reference images, ~10 мин обучения).

**Установка:**
```bash
# 1. Получить Replicate API key (free credits на старте): https://replicate.com/account/api-tokens
# 2. Положить в .mcp.json (gitignored):
claude mcp add replicate-flux -- npx -y replicate-flux-mcp \
  -e REPLICATE_API_TOKEN=r8_xxx
```

---

## 3. Chart generation — recommendation

### 3.1. Сравнение

| Tool | Setup | Output | Chart types | Donut | Bar | Funnel |
|---|---|---|---|---|---|---|
| **PowerPoint MCP `add_chart`** | уже есть | native PPTX chart | bar, line, pie, doughnut | да | да | **нет** |
| **QuickChart API (no MCP)** | `curl` only | PNG via URL | Chart.js full set | да | да | **через плагин** (chartjs-funnel) |
| **QuickChart MCP** (`@gongrzhe/quickchart-mcp-server`) | `npx -y @gongrzhe/quickchart-mcp-server` | PNG | bar, line, pie, doughnut, radar, polarArea, scatter, bubble, gauge | да | да | да (через Chart.js plugins) |
| **Vega-Lite via `vl-convert`** | `cargo install vl-convert` или `pip install vl-convert-python` | PNG/SVG | вся грамматика Vega-Lite | да | да | **через layered marks** |
| **matplotlib via Python** | `pip install matplotlib` | PNG/SVG | всё | да | да | да |
| **Chart.js via headless browser** | сложно | PNG | всё | да | да | да |

### 3.2. Рекомендация: **QuickChart как primary** + matplotlib fallback

**QuickChart API напрямую через `curl`** — простейший вариант:
- Free tier: **60 charts/min, 1000 charts/month** — нам хватит с запасом для 17 лекций.
- Без signup, без API key, без MCP — просто URL: `https://quickchart.io/chart?c={JSON-config}&w=900&h=600&backgroundColor=white`.
- Все стандартные типы (bar/donut/line/pie/radar/scatter), кастомные цвета через Chart.js options, `devicePixelRatio=2.0` для retina-резкости.

**MCP-обёртка** (`@gongrzhe/quickchart-mcp-server`) — опциональна. Для агента удобнее декларативно описать конфиг, MCP сделает HTTP-запрос. Но `curl` через `Bash` тоже подходит и не добавляет ещё один MCP к стеку.

**Funnel chart (s05b: 90%→10% drop-off):**
QuickChart штатно не имеет funnel — но Chart.js поддерживает плагин `chartjs-funnel`, и QuickChart его подгружает. Альтернатива — сделать **horizontal bar chart с убывающими барами** = визуально читается как воронка и проще конфигурировать.

**Рекомендация по стеку:**
1. **QuickChart API** для bar/donut/pie/line — 90% случаев.
2. **matplotlib** через Python script — для funnel/sankey/нестандартных кастомов (когда визуальный дизайн критичен).
3. **PowerPoint MCP `add_chart`** — НЕ использовать. Native PPTX-чарты выглядят как Office 2010 и плохо стилизуются. Лучше PNG из QuickChart, embed как picture.

**Установка:** для QuickChart API ничего не нужно — `curl` уже есть. Для matplotlib: `pip install matplotlib` (если потребуется).

---

## 4. Diagram generation — recommendation

### 4.1. Сравнение

| Tool | Install | Output | Best for |
|---|---|---|---|
| **mermaid CLI** (`@mermaid-js/mermaid-cli`) | `npm install -g @mermaid-js/mermaid-cli` | SVG/PNG/PDF | flowchart, sequence, class, state, ER, gantt, pie |
| **PlantUML** | `apt install plantuml` или JAR + Java | PNG/SVG | UML (классы, sequence, deployment), архитектура |
| **Graphviz/dot** | `apt install graphviz` | PNG/SVG | графы, дерево зависимостей |
| **drawio-desktop CLI** | docker `rlespinasse/drawio-desktop-headless` | PNG/SVG/PDF | если уже есть `.drawio` файлы |
| **excalidraw CLI** (`excalirender`, `excalidraw-brute-export-cli`) | binary download или npx | PNG/SVG | если нужен «hand-drawn» стиль |

### 4.2. Рекомендация: **mermaid CLI** как primary

**Почему mermaid:**
- Самый простой синтаксис (5 минут на любую диаграмму, агент пишет в текстовом виде).
- Покрывает 90% наших нужд: flowchart (process flow камера→модель→bbox), sequence, state, pie.
- Один npm install, нет JAR/Java/Docker.
- Темы: `mmdc -t neutral -b transparent` даёт чистый чёрно-белый вывод, который мы recolor под палитру через ImageMagick.

**Когда нужен PlantUML:** только для канонических UML-диаграмм классов с inheritance. Для нашего курса AI/data это редко.

**Когда нужен Graphviz:** для очень больших графов зависимостей. Тоже не наш случай.

**drawio CLI** — отвергнуто в `phase-e-tool-research.md` (drawio MCP открывает онлайн). drawio-desktop-headless через Docker — overkill для курса.

**Excalidraw** — интересен «hand-drawn» стилем для cover-слайдов или meta-illustrations, но добавляет третий tool в стек. Отложить.

### 4.3. Mapping слайдов пилота #55 на типы диаграмм

| Слайд | Что нужно | Tool |
|---|---|---|
| s01 (camera→model→bbox) | process flow с тремя нодами | **mermaid** flowchart LR |
| s05b (90%→10% воронка) | funnel | **QuickChart bar** (горизонтальный с убыванием) или **mermaid pie (perspective)** |
| s04 (43/27/23/15%) | distribution | **QuickChart donut** (data-ink-friendly) |

---

## 5. Image manipulation / recolor — recommendation

### 5.1. Задача

Иконки из Lucide/Tabler/Phosphor приходят в `currentColor` (= черные/выбранный SVG fill). Чтобы embed в наш deck в брендовом цвете (например navy `#1a2845`), нужен recolor + растрирование в PNG (PowerPoint MCP лучше работает с PNG, чем с SVG).

### 5.2. Сравнение

| Tool | Install | SVG→PNG | Recolor | Resize | Сложность |
|---|---|---|---|---|---|
| **ImageMagick** (`convert`/`magick`) | `apt install imagemagick` | да (с librsvg) | `-fill <color> -opaque <old>` | `-resize` | низкая |
| **rsvg-convert** | `apt install librsvg2-bin` | да | нет (только конверсия) | `-w` | минимальная |
| **Pillow + lxml (Python)** | `pip install Pillow lxml` | через cairo | да (XML edit) | да | средняя |
| **MCP image manipulation server** | — | — | — | — | **активных не нашёл** |

### 5.3. Рекомендация: **ImageMagick**

```bash
# 1. Скачать SVG из Lucide CDN
curl -o /tmp/camera.svg https://cdn.jsdelivr.net/npm/lucide-static@latest/icons/camera.svg

# 2. Конверт + recolor + resize за один проход
convert -density 300 -background none /tmp/camera.svg \
        -fill "#1a2845" -opaque black \
        -resize 256x256 \
        assets/camera-navy.png
```

Порядок флагов важен (`-fill` ДО `-opaque`). `-density 300` для retina, `-background none` сохраняет прозрачность.

**Альтернатива recolor через XML-substitution** (если ImageMagick `-opaque` не ловит из-за `currentColor`):
```bash
sed 's/currentColor/#1a2845/g; s/stroke="black"/stroke="#1a2845"/g' \
  /tmp/camera.svg | convert -density 300 -background none svg:- \
  -resize 256x256 assets/camera-navy.png
```

**Установка:** `sudo apt install imagemagick librsvg2-bin` (librsvg расширяет SVG-поддержку ImageMagick).

---

## 6. Background generation — optional finds

Не критично для пилота, но если понадобится:

- **CSS-gradient generators** (статика): https://uigradients.com/, https://cssgradient.io/ — браузерно. Можно скопировать gradient → отрендерить SVG/PNG локально.
- **Hero Patterns** (https://heropatterns.com/) — SVG-паттерны, MIT, легко вставить как полупрозрачный фон.
- **Pattern Monster** (https://pattern.monster/) — генератор SVG-паттернов с настройкой цвета.
- **AI-generation backgrounds** через FLUX prompted: «abstract minimal navy gradient, soft organic shapes, 1920×1080, educational subtle background, no text» — единственный case для FLUX в фонах, потому что воспроизводимо через seed.

**Не рекомендуем** для образовательного deck'а: фотографические backgrounds (отвлекают), полноэкранные фотостоки (Apple-стиль не работает для технической лекции — уже зафиксировано в `design-research.md` §1).

---

## 7. Brand consistency / accessibility / visual regression

### 7.1. Brand consistency checker

**Готового CLI tool нет** для PPTX. Свой подход:
1. Хранить brand-палитру в `library/lectures/lec-NN/brand.yaml` (hex-коды, шрифты).
2. **Skill `brand-check`** — после генерации deck'а парсит PPTX (через python-pptx), извлекает все цвета и шрифты, сверяет с `brand.yaml`, репортит отклонения. Это 50 строк Python — встроить в `presentation-critic`.
3. Анализ skill'а Anthropic `brand-guidelines` (раздел 1.2) — взять паттерн «Smart Font Application + Shape Color Cycling» и переписать под наш stack.

### 7.2. Accessibility / contrast checker

- **`KurtWeston/color-contrast-checker`** (Python CLI, GitHub) — WCAG AA/AAA расчёт contrast ratio между двумя hex.
- **Минимально:** чистая Python-функция (10 строк) для расчёта WCAG contrast ratio. Не нужен внешний tool.
- **Что проверять:** каждая пара (текст-цвет, фон-цвет) на каждом слайде должна давать ≥ 4.5:1 для основного текста, ≥ 3:1 для заголовков 24pt+. Встроить в `presentation-critic`.

### 7.3. Visual regression testing для слайдов

- **`odiff`** (https://github.com/dmtrKovalenko/odiff) — SIMD-ускоренный pixel-diff, в 6× быстрее ImageMagick/pixelmatch. Идеален для CI: «слайд изменился — покажи diff». Установка: `npm install -g odiff-bin`.
- **Use case:** при итерациях по дизайну слайдов автоматически снимать snapshot до/после, через odiff видеть pixel-diff. Полезно когда pipeline стабилизируется (Лекция 2+), не для пилота.

---

## 8. FINAL: top 5 superpowers — install RIGHT NOW

Для пересборки 6-слайдного пилота #55. Расположены по приоритету.

### #1. **Anthropic `pptx` skill** (must-have, базовый)

```bash
# В Claude Code:
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
```

Зачем: получаем PptxGenJS (декларативный API) как **дополнение** к PowerPoint MCP, плюс embedded дизайн-философию (палитры, anti-patterns, обязательный visual QA loop). 9 готовых палитр + правила контраста — переиспользовать как референс для своего brand.yaml.

**Зависимости (одной командой):**
```bash
sudo apt install -y libreoffice poppler-utils && \
pip install "markitdown[pptx]" Pillow && \
npm install -g pptxgenjs
```

### #2. **mermaid CLI** (для диаграмм — s01, s05b)

```bash
npm install -g @mermaid-js/mermaid-cli
# Использование:
mmdc -i diagram.mmd -o assets/flow.png -t neutral -b transparent -w 1600
```

Зачем: декларативный текст → PNG за 1 секунду. Для process flow s01 (camera→model→bbox) — 3 строки `flowchart LR`. Для s05b воронки — `pie` или комбинация с QuickChart.

### #3. **ImageMagick** (recolor иконок в брендовую палитру)

```bash
sudo apt install -y imagemagick librsvg2-bin
# Использование:
curl -o /tmp/icon.svg https://cdn.jsdelivr.net/npm/lucide-static@latest/icons/camera.svg
convert -density 300 -background none /tmp/icon.svg \
        -fill "#1a2845" -opaque black -resize 256x256 \
        assets/camera-navy.png
```

Зачем: иконки из Lucide/Tabler приходят чёрные, нужны в нашем navy. Без recolor визуальная консистентность ломается. ImageMagick — стандарт, низкая сложность, работает с SVG через librsvg.

### #4. **QuickChart API через `curl`** (charts на s04)

```bash
# Никакого install — только curl. Пример:
CHART='{"type":"doughnut","data":{"labels":["A","B","C","D"],"datasets":[{"data":[43,27,23,15],"backgroundColor":["#1a2845","#3d6a9c","#7ba2c8","#b8cee0"]}]}}'
curl -G "https://quickchart.io/chart" \
  --data-urlencode "c=$CHART" \
  --data "w=900&h=600&backgroundColor=white&devicePixelRatio=2.0" \
  -o assets/s04-distribution.png
```

Зачем: free, no key, бесконечная гибкость через Chart.js JSON, output — готовый PNG для `manage_image`. На s04 (43/27/23/15%) — **donut**, на любых других распределениях — bar/pie/line. Лимит 1000/месяц перекрывает 17 лекций × 5 чартов.

### #5. **Replicate FLUX MCP** (AI-illustrations для cover'ов и hero-визуалов)

```bash
# 1. Создать аккаунт на Replicate, получить API token.
# 2. Положить токен в .mcp.json (gitignored), добавить server:
claude mcp add replicate-flux -- npx -y replicate-flux-mcp \
  -e REPLICATE_API_TOKEN=r8_xxxxxxxxxxxxx
# 3. Restart Claude Code.
```

Зачем: для cover-слайдов и hero-illustrations нужны качественные изображения, иконки и геометрия не покрывают. FLUX.1 Schnell даёт **$0.003/image** = ~1600 шт за $5/мес. Style consistency через зафиксированный system-prompt («flat illustration, navy line art, educational style, no shadows»).

**Сэкономим:** в первой итерации можно обойтись без #5 (использовать только иконки + диаграммы + чарты), а FLUX подключить, когда станет ясна потребность в ≥3 уникальных illustrations на лекцию.

---

## Дополнительные tools (не в top-5, но держать в виду)

- **`odiff`** для visual regression — после стабилизации pipeline (Л2+).
- **`brand-guidelines` skill** Anthropic — паттерн для своего `tellian-brand-guidelines` skill (Лекция 2+).
- **`theme-factory`** — если решим иметь несколько тем (light/dark) в курсе.
- **`vl-convert`** (Vega-Lite CLI) — если QuickChart упрётся в лимиты или нужна сложная семантика данных.
- **PlantUML** — только если появится тема с UML-классами.

---

## Что НЕ устанавливать (явно отвергнуто)

| Tool | Почему |
|---|---|
| **OpenAI Images MCP** (DALL-E) | $0.04/img — в 13× дороже FLUX без явного выигрыша. |
| **fal.ai MCP** | дублирует Replicate, нет преимущества при наших объёмах. |
| **Pollinations API** | нет SLA, нет контроля качества — публичный free endpoint. |
| **ComfyUI MCP** | требует локальной GPU, overkill. |
| **`canvas-design` skill** | художественный стиль, не дидактический. |
| **`algorithmic-art` skill** | генеративное искусство, не для обучения. |
| **`openai/slides`** | дублирует `anthropics/pptx`. |
| **drawio-desktop CLI (Docker)** | overkill, mermaid покрывает наш scope. |
| **PlantUML** на этой итерации | не нужен для AI/data курса. |
| **Excalidraw CLI** | интересен, но добавляет третий tool в diagram-стек. |
| **Native PowerPoint MCP `add_chart`** | визуально как Office 2010, плохо стилизуется → используем PNG из QuickChart. |

---

## Sanity-чек перед запуском пилота

После установки top-5:
1. `mmdc --version` → должен быть ≥10.x
2. `convert --version` → ImageMagick ≥6.9
3. `npm list -g @mermaid-js/mermaid-cli pptxgenjs` → оба установлены
4. `curl 'https://quickchart.io/chart?c={type:%22pie%22,data:{labels:[%22a%22,%22b%22],datasets:[{data:[1,1]}]}}' -o /tmp/test.png && file /tmp/test.png` → "PNG image data"
5. `claude mcp list` → `replicate-flux` есть, статус OK
6. В Claude Code: `/plugin list` → `document-skills@anthropic-agent-skills` есть

Если все 6 чек-боксов зелёные — агент `presentation-designer` готов работать.
