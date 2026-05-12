# v2 — Sweep синтез всех 4 рецензентов

**Issue:** #55 v2 review.
**Дата:** 2026-05-12.
**Источник:** 4 параллельных QA-агента (`presentation-critic` + `student-simulator` + `reader-simulator` mode=rendered + designer self-review через general-purpose).

---

## Конвергентные находки (≥2 агента согласны)

### 1. s01 — слайд **паразитирует на live demo**
- **critic (P0):** «противоречит intent'у `live_demo` — схема вместо минимума».
- **student:** «слайд пустой паразит при работающем демо», «три квадрата как методичка для первокурсника».
- **designer:** «process flow — это диаграмма ABOUT live demo, не сам demo».
- **reader-rendered:** «без записи демо бесполезен через 2 недели».

→ Схему **убираем**. Заменяем на **mock-screenshot** с bbox + «N=3 человека в кадре» (preview-артефакт). Для self-study — это «вместо записи».

### 2. s02 ↔ s05b — **дубль central question**
- **critic (P0):** «дублируют центральный вопрос → убивает reveal».
- **designer:** «функционально сломан как единственный dark среди light».
- **student:** «3 минуты сидел и гадал «10% от чего»».
- **reader-rendered:** «при произвольном порядке листания — могу не понять».

→ **Развести:** на s02 убрать центральный вопрос (или сделать тизером без раскрытия). Раскрытие — на s05b. Cover переделать в **light** (или сделать coherent dark-tail на s05b также).

### 3. s04 — **факт-ошибка в названии chart'а** + axis label
- **user:** «странное название».
- **critic (P0):** «"Доли LLM-рынка" = ложь о метрике; multi-select = use, не market share».
- **designer:** «дублирует assertion-headline; рынок не имеет долей; нет axis label».

→ Переименовать на **«Использование LLM в РФ, 2025»**. Axis label «% пользователей AI». Сноска «multi-select» крупнее. Не «доли рынка».

### 4. s05a placeholder = **доверие к преподу проседает**
- **student:** «самый болезненный момент — нельзя показывать студентам черновик».
- **reader-rendered:** «через 2 недели бесполезен».
- **designer:** «photo placeholder = недоделанность, monogram-tile вместо».

→ Заменить «фото преподавателя» placeholder на **monogram-tile** (круг с инициалами или нейтральная иконка) ИЛИ временно скрыть слайд из self-study варианта.

### 5. s03 — **слишком формально, как Google Form**
- **user:** «херь какая-то».
- **student:** «слайд для 7 класса средней школы».
- **designer:** «метафора Google Form вместо classroom poll, иконки 32px мелкие, нет emotional CTA».
- **critic:** «Q2 — два вопроса в одном с misleading chips (одинаково оформлены при разной семантике)».

→ Иконки **96px** (большие), gold-CTA «**УГАДАЙ**» сверху как тизер, **Q2 разделить** (или поправить chips: семантически отделить Q2.1 «использовал ли» от Q2.2 «для чего»).

### 6. Монохромность — частично, но **под-использован gold**
- **user:** «очень монохромно».
- **student:** «синий везде, единственный акцент за 6 слайдов — жёлтое 10%».
- **designer:** «корень не в кол-ве цветов, а в одинаковой intensity 3 синих + редкость gold (16% deck)».
- **critic:** «не нужно добавлять цвета — нужно использовать имеющиеся 2 уровня синего как иерархию».

→ **Сохранить Ocean.** Добавить **Teal `#028090`** для secondary contrast (charts, secondary icons). **Расширить gold** до one highlight per slide минимум — использовать как эмоциональный «вот это важно» якорь, не реликвию.

---

## Уникальные находки (одного агента, но важные)

### От student
- DeepSeek 43% удивил — **хочет деталей** (что это за зверь?). На s04 не объяснено.
- «Не закрыл ноутбук — уже плюс для первой пары» — общее ощущение между «нормально» и «зашло».
- Топ-вопросы после: почему DeepSeek? почему 90% умирают? «использовали AI» = что значит?

### От reader-rendered
- **Сломанные ссылки** на s14/18/27 в speaker notes (в пилоте этих слайдов нет).
- Speaker notes **смешивают две аудитории** — методист и студент. Нужна явная секция «**For self-study:**».
- DeepSeek/YandexGPT/GigaChat не объяснены.
- s05b «**выводящая фраза**» «Завтра — почти везде. Сегодня — почти никто...» спрятана в notes — **должна быть на слайде**.

### От critic
- s05b — **competing focal points** (funnel vs central question). Funnel мелкий, текст справа крупный.
- Typography hierarchy **плавает**: s01=28pt, s04=24pt — нужна унификация.

### От designer
- **Visual motif отсутствует** (Anthropic skill: «one distinctive repeated element across all slides»).
- → Ввести «**Ocean rounded box**» как sweep элемент (radius=12, surface=`#F4F7FA`, stroke=`#1C7293`).
- **Footer-tax**: 5 типов мелкого курсива (источник, self-study, caveat, draft-tag, definition) визуально однообразны, семантически разные. Стандартизовать.
- **Photo s05a** — даже когда заполнено будет, реальное фото препода + реальный live screenshot YOLOv8 решат больше чем все digital improvements.

---

## Топ-10 правок для v3 (приоритизировано)

| # | Слайд | Правка | Severity |
|---|---|---|---|
| 1 | s04 | Переименовать chart на **«Использование LLM в РФ, 2025»**, axis label «% пользователей», multi-select крупнее | **P0 factual** |
| 2 | s02+s05b | Развести central question — на s02 убрать или тизером без расшифровки, на s05b раскрыть | **P0 narrative** |
| 3 | s01 | Убрать process-flow схему. Заменить на mock-screenshot YOLOv8 с bbox + N=3 | **P0 intent** |
| 4 | s05a | Monogram-tile вместо «фото преподавателя» placeholder | P1 |
| 5 | s03 | Иконки 96px, gold-CTA «УГАДАЙ», Q2 разделить или semantically distinct chips | P1 |
| 6 | s05b | Funnel 45-50% ширины + main takeaway «Завтра — почти везде. Сегодня — почти никто» крупно | P1 |
| 7 | palette | Добавить **Teal `#028090`** для secondary accents (charts, иконки), расширить gold до 1×/слайд min | P1 |
| 8 | motif | Ввести «**Ocean rounded box**» как sweep элемент во всех слайдах | P1 |
| 9 | typography | Унифицировать hierarchy: assertion 28pt, sub 20pt, body 16pt, caption 12pt | P2 |
| 10 | speaker notes | Стандартизовать: секция «**For self-study:**» в каждом note-блоке, отделена от методиста | P2 |

### Bonus (не P0/P1, но дёшево)
- В **s04** speaker notes — 1 абзац контекста про DeepSeek/YandexGPT/GigaChat для self-study.
- В **s02+s05b** speaker notes — пометить ссылки на s14/18/27 как «в полной версии лекции».
- Footer-tax: один общий стиль, 2 строки максимум на слайд.

---

## Что сходится и что расходится между agents

**Сходится:**
- Все 4 нашли что-то в s01/s02/s03/s04/s05a/s05b (никто не выпал из-под огня).
- 3 из 4 сказали про s01 «избыточная схема» / «противоречит demo» / «бесполезен без записи».
- 3 из 4 сказали про s05a «placeholder = недоделанность».
- 3 из 4 сказали про монохромность («да но...»).

**Расходится:**
- **Cover (s02) light vs dark**: designer советует переключить на light; critic не считает dark проблемой; student просто говорит «непонятно про 10%». → Решает пользователь.
- **Coral как secondary**: designer советует добавить Coral; critic — нет, использовать имеющиеся синие. → Я склоняюсь к **Teal**, не Coral (МГТУ + AI tone).
- **Visual motif Ocean rounded box**: только designer назвал явно — это его профессиональная оптика, имеет смысл взять.

---

## Файлы

- `library/lectures/lec-01/qa-reports/2026-05-12-v2/presentation-critic.md`
- `library/lectures/lec-01/qa-reports/2026-05-12-v2/student-simulator.md`
- `library/lectures/lec-01/qa-reports/2026-05-12-v2/reader-rendered.md`
- `library/lectures/lec-01/qa-reports/2026-05-12-v2/designer-self-review.md`
- `library/lectures/lec-01/qa-reports/2026-05-12-v2/SYNTHESIS.md` ← этот файл
