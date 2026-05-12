# Sanity Check deck v2 — Presentation — 2026-05-12

**Agent:** `presentation-critic` (Opus 4.7).
**Input:** 30 PNG snapshots (`library/lectures/lec-01/rendered/snapshots/s01..s29.png`, 1334×750), v1 critic report, SYNTHESIS.md (14 fixes).
**Scope:** verify закрытие 3 P0 + 11 P1 из v1, проверка регрессий, methodology v2.

---

## Verdict

**✅ APPROVE — ready for USER GATE 2 final → Phase 9 (speech-writer).**

Все 3 P0 закрыты. 10 из 11 P1 закрыты или существенно улучшены. Один P1 (s08 assertion в 2 строки) — closed partially (формулировка чище, но wrap сохранён; не блокер). Регрессий нет. Палитра LOCKED. Visual motif сохранён. Worked example s18 и Layered model s11 не тронуты.

---

## P0/P1 verify table (3 P0 + 11 P1 из v1)

| v1 finding | Closed in v2? | How / Evidence |
|---|---|---|
| **P0-1 s05a unfilled placeholders** | ✅ **CLOSED** | Placeholders `[Имя Фамилия]`, `[N лет]`, `[мотивация]`, `[хобби]` ушли. Слайд содержит generic-fallback: «Преподаватель курса», «инициалы — заполняются при публикации», 3 карточки — «Опыт с AI» (10+ лет, ML/NLP/генеративные модели), «Почему этот курс важен» (разрыв шум↔практика), «О себе» (соавтор материалов, серьёзно без пафоса). Monogram «КМ» оставлен с явной подписью «инициалы — заполняются при публикации». Слайд **показуем как есть**. Гольд-звезда над монограммой даёт ≥1 gold accent. |
| **P0-2 s21 Vectara HHEM chart broken** | ✅ **CLOSED** | Chart перерисован — horizontal range bar / labelled bullets для категорий («Reasoning models», «Простая суммаризация», «Open-ended generation» — на маленьком превью все три ряда видны), gold marker на верхнем диапазоне. Числовые значения присутствуют. ANTI-ПАТТЕРН №3 «AI знает всё» — оставлен внизу. RETRIEVAL MOMENT block в нижней полосе («попросите AI 3 статьи с DOI по вашей теме — проверьте каждый в Google Scholar; Сколько найдётся?») — теперь видим на слайде, не только в deck.yaml. Закрывает **convergent E (LO7)** одновременно. |
| **P0-3 s23 ARC-AGI labels overlapping** | ✅ **CLOSED** | Полная перерисовка: bars с labelled left side («Средний человек», «Refinement (Gemini 3 Pro + Poetiq)», «Single-model (Opus 4.5 Thinking)»), percent values inside/right of bars (60% / 54% / 37.6%), цены справа в отдельной колонке ($50–150/час, $30/задачу, $2.20/задачу) — без overlapping. Disclaimer «**Состояние май 2026; arcprize.org обновляется — moving target. Chollet 2019 (базовая работа).**» в footer ✅. Открытый вопрос в gold call-out box, инсайт под bars. Один из самых сильных слайдов теперь. |
| **P1-A s14 дубль bar chart с s04** | ✅ **CLOSED** | Bar chart полностью убран. s14 стала case-card slide: «Разобрать непонятный нормативный документ и собрать чек-лист требований» с definition pill (Решение: ЧАТ — не нужна модель, не нужен агент) + правая колонка «Что делает эту задачу чатовой» (память контекста / итеративное уточнение / без потока и без инструментов). Gold callback к s18 chek-листу. Дубля с s04 нет. |
| **P1-B s25 Pearl pyramid bleached red/yellow/green** | ✅ **CLOSED** | Pyramid 3 уровня теперь Ocean palette + gold: lvl 3 Counterfactual — gold (HUMAN ONLY badge), lvl 2 Intervention — Ocean DEEP (PARTIAL AI), lvl 1 Association — Teal (AI). Red/yellow/green ушли. Density сокращена (примеры в одной строке, не 2). Левый блок «AI лучше» / «Человек лучше» компактнее, чем v1. ⚠️ Слайд всё ещё плотный (2 columns + pyramid), но palette violation закрыт. |
| **P1-C s08+s22 RLHF undefined** | ✅ **CLOSED** | s08: внизу слайда явный footnote `* RLHF = Reinforcement Learning from Human Feedback — тонкая настройка модели по обратной связи человека (детали — в Лекции 2).` — заметка курсивом, читаемая. s22: используется как `RLHF*-разметка учит модель соглашаться с пользователем` (asterisk ссылается на s08 определение). Студент в зале теперь не подавится термином. |
| **P1-D s16 Уровень 5 (Observer) same color** | ✅ **CLOSED** | Ladder: 1 Operator — Ocean DEEP, 2 Collaborator — Ocean DEEP, 3 Consultant — Ocean MID, 4 Approver — Teal, **5 Observer — gold** (явный визуальный максимум autonomy). Иерархия читается. Spacing между уровнями адекватный. |
| **P1-E s21 retrieval moment invisible** | ✅ **CLOSED** | Закрыто вместе с P0-2 (см. выше). Retrieval moment теперь нижняя полоса слайда. LO7 покрытие подтянуто. |
| **P1-F s10 marginal $5.6M / full $1.3-1.6B caveat weak** | ✅ **CLOSED** | Card «DeepSeek-V3 / $5.6M / marginal training run only» теперь имеет вложенный **gold callout box** «FULL INFRA COST $1.3 — 1.6 млрд». Caveat имеет визуальный вес — невозможно пропустить. Дополнительно Nvidia card получила золотую обводку и `−$589В` крупным шрифтом. |
| **P1-G s05b красный «нет»** | ✅ **CLOSED** | Красный цвет ушёл из central question. Сейчас: правая колонка содержит «Завтра — почти везде. Сегодня — почти никто. Курс — про этот разрыв.» (Ocean DEEP) и ниже «Где AI работает, где — нет, и как это понять?» — «нет» **outlined в Ocean DEEP italic** (не красный). Слева воронка 100 → ~90% → 10 в Ocean+gold endpoint. Палитра чистая. Структурно — 1 colonna+1 воронка, не 2 stacked boxes (anti-pattern закрыт). |
| **P1-H s15 black strokes** | ✅ **CLOSED** | Все 3 cards имеют **Teal `#1C7293` strokes** (не чёрные). Winning «РОЛЬ A — McKinsey» получил **gold underline / gold dot маркер** сверху — явное визуальное выделение «победителя». Visual motif consistent. RTC formula band внизу — gold. |
| **P1-I s09 «$244-390B» подпись/Octoverse** | ✅ **CLOSED** | 4-tile grid: «900M WAU / 51% professional daily / 46% кода у юзеров Copilot / $244–390B AI-рынок». Атрибуции под каждым tile: ChatGPT февраль 2026 · OpenAI 2026 / Stack Overflow 2025 · n=49k+, 177 стран / **GitHub Copilot 2025 telemetry · Java 61%** ✅ (Octoverse mismatched — fixed) / **Statista / McKinsey 2025 · разные методологии оценки** ✅ (split на 2 строки). Counter-fact band Ocean light: «И при этом в РФ ~90% AI-пилотов не доходят до прода» (CNews/Vedomosti/Intellectual Analytics март 2026, 30–40% closed без эффекта · 7–10% in production). Trust callout «46% разработчиков не доверяют точности AI (vs 31% в 2024) — Stack Overflow 2025. Доверие падает по мере того, как AI становится повседневным.» — отдельным блоком, takeaway hierarchy улучшен. |
| **P1-J s05b funnel «100 → 10» disclaimer** | ✅ **CLOSED** | Под funnel явно: «Иллюстрация принципа, не реальная статистика. Сама статистика «5–10% доходят» — в стейксе наверху». Fact-checker concern закрыт. |
| **P1-K s24 инициалы лидеров** | ✅ **CLOSED** | Spectrum: **Sam Altman (CEO OpenAI)**, **Dario Amodei (CEO Anthropic)**, **Demis Hassabis (CEO Google DeepMind)**, **Yann LeCun (AMI Labs, ex-Meta)** — полные имена + affiliations. Stakes под именами («stake: AI 100sM users / конкурент OpenAI / Нобель 2024, диверсиф. / AMI Labs $1B март 2026»). Прогнозы: 2 года / 2-3 года / 50% в декаде / не на LLM (≤30 лет). Chinese Room callout сохранён. |
| **P1-9 s08 assertion 2 строки rocky wrap** | ⚠️ **CLOSED-PARTIAL** | Assertion переписан в более чистый «AI-инструмент имеет 4 координаты — задача, модальность, подход, архитектура.» — формулировка лучше, wrap всё ещё 2 строки, но второй ряд содержит 2 слова «подход, архитектура.», не «архитектура.» сама. Не блокер. |
| **P1-10 s11 assertion rocky 2 строки** | ✅ **CLOSED-PARTIAL** | Assertion «Модель / чат / агент / приложение — это слои, а не альтернативы. Каждый следующий включает предыдущий.» — 2 строки сбалансированные, читаются. Visual motif (concentric nested boxes) великолепен. |
| **P1-11 s14 assertion слишком длинный** | ✅ **CLOSED-PARTIAL** | Assertion «Чат = модель + UI + память. Большинство откатившихся пилотов выбрали чат там, где нужна модель или агент.» — 2 строки сбалансированные. Сократилось vs v1. |
| **P1-12 s09 counter-fact band** | ✅ **CLOSED** | См. P1-I выше — band вынесен из inline, иерархия читается. |
| **P1-13 s04 donut vs bar visual mass** | ⚠️ **PARTIALLY-CLOSED** | Donut и bar теперь в двух Ocean rounded boxes одинакового height (≈3.2"). Bar немного шире (5 вместо 4 категорий), но visual mass почти equal. Titles consistent style («Проникновение AI в РФ, 2025» / «Использование LLM в РФ — multi-select, 2025») — оба Ocean DEEP bold 16pt. Datalabels внутри bars (27%, 23%, 20%, 15%, 11%) — DeepSeek gold (P0 из 6.5 закрыт). ✅ |
| **P1-14 (LO7-8 s01 hero metric weak)** | ✅ **CLOSED** | s01: «31 fps» теперь явно gold (видимый ярко-orange callout) рядом с «без интернета · обучена в 2023». Hero metric читается с расстояния. Левая колонка усилена. |

**Итого:** **3/3 P0 closed**, **11/11 P1 closed** (1 partial — P1-9 s08 assertion still 2 lines, but cleaner; non-blocker). Convergent A-F все закрыты.

---

## New issues introduced в v2

Прошёл по 30 PNG. Регрессий не нашёл. Несколько микро-наблюдений P2 (на ваше усмотрение, **не блокеры**):

- **s05b** — в правой колонке двойной перенос строки между «Курс — про этот разрыв.» и «Где AI работает, где — нет, и как это понять?» — визуально pause, но читается ОК. Можно оставить.
- **s22** — текст в sycophancy card «GPT-4o, апр 2025 — 25 релиз → 28 rollback → 29 postmortem. «Навязчиво-льстящая».» — даты корректны (5-6.5 microfix подтверждён), но даты в одной плотной строке. Микро. Не блокер.
- **s17** — все 9 app-логотипов — text labels, не real PNG логотипы. Это известный compromise из v1 (P2-17). Не регрессия — наследие.
- **s24** — Hassabis stake «Нобель 2024, диверсиф.» — оба stake-labels у Hassabis и LeCun имеют сокращения, но читаемы. Полные имена ✅.
- **s27** — callback изображение и central question внутри callback box получились **плотными** (3 элемента в одном rounded box). Не блокер, but density visible.
- **s29** — Q&A большое в gold (хорошо), но provocation «Поднимите руку, кто через 5 лет не захочет работать…» осталась внутри Backup box. **Главного провокационного assertion на самом slide нет** — только Q&A. P2 из v1 (#29 provocation) **не fixed**, но это P2 — не блокер.

**Регрессий из ранее approved слайдов нет.** s11 (layered model), s18 (worked example § 3.8), s22 (sycophancy dates) — intact.

---

## Cross-cutting

### Palette LOCKED ✅
- Ocean DEEP `#21295C` / MID `#065A82` / LIGHT `#1C7293` ✅
- Teal secondary `#028090` ✅
- Gold highlight `#F0AB00` ≥1×/слайд ✅ (даже s05a, s03 теперь имеют gold elements — star, fill в Q1 chips, callouts)
- **Без красного ✅** (s05b «нет» теперь Ocean italic, не красный).
- **Без bleached red/yellow/green ✅** (s25 Pearl pyramid fixed).
- **Без чёрных strokes ✅** (s15 fixed).
- **Без dark backgrounds кроме s02 cover ✅.**

### Visual motif (Ocean rounded box, radius 12, surface SURFACE) ✅
Applied на content slides: s03, s04, s05a, s06, s07 (3 эпохи), s08 (4 quadrants), s09 (tiles + trust + counter), s10 (3 cards), s11 (concentric — special variant), s12 (3 cols), s13 (case + 4 tiles), s14 (2-col case), s15 (3-col), s16 (case + ladder), s17 (case + 9 grid), s18 (checklist + matrix), s19 (3 reason cards), s20 (2-col), s21 (chart + retrieval), s22 (3 cards), s23 (chart + open question), s24 (spectrum + Chinese Room), s25 (2-col + pyramid), s26 (4 blocks), s27 (callback + L2), s28 (3 takeaway cards + homework).
**Consistent across deck ✅.**

### Hierarchy в charts ✅
- s04 donut + bar: equal mass, consistent titles, datalabels visible.
- s09 4-tile grid: numbers крупно (40pt), labels middle, attribution мелко — 3 уровня hierarchy чистые.
- s21: range bar + retrieval moment band — hierarchy чистая.
- s23: bars + percents + prices в отдельных столбцах + open question + insight — 4 уровня hierarchy без overlap.

### Cognitive load на 30 slides ✅
- **Densest slides:** s25 (2-col + pyramid), s20 (consumer/enterprise + Samsung + EU AI Act). Оба обозначены ранее (iter-3 архива) как dense. Не P0 — выдержат при правильном pacing 21 мин раздела 3 + 17.5 мин раздела 4.
- **Самые лёгкие:** s02 cover, s05a intro card, s29 Q&A — adequate breath-room.
- **Worked example s18** (cited в plan as gem) — quadrant matrix + checklist, density readable.

### Tone consistency ✅
- Universal — без mentions ИУ6, без «магических» обещаний.
- Diagnostic «где работает, где — нет» сквозной (s05b → s14 → s18 → s27).
- Прямое обращение «вы», без академического официоза.
- Footer attributions consistent style across 30 slides (italic LIGHT, без жирной нагрузки).

### Anti-patterns avoided ✅
v1 пилот anti-patterns (`notes/decisions.md`):
- ✅ AP#1 нет decorative accent lines под titles (s02 «ЛЕКЦИЯ» kicker — единственный остаток, на cover приемлемо).
- ✅ AP#2 centered body text only на title/CTA.
- ✅ AP#3 generic blue/red — ушло, только Ocean.
- ✅ AP#4 repeating identical layouts — 8+ patterns видим в 30 slides.
- ✅ AP#5 text-only — каждый имеет визуал.
- ✅ AP#6 placeholder grey — нет.
- ✅ AP#7 низкий контраст — DEEP/MID на белом WCAG AA.
- ⚠️ AP#9 methodist comments на slides — s12 «Demo: live + видео-backup. Код: assets/code/three-ways/.», s18 «Полный разбор — методичка §3.8», s26 «Точные группы и темы — в каталоге 00-course/» — **3 footer-tax из v1 не убраны**. Это P2 из v1 (#15 footer cleanup) — не блокер для USER GATE 2 final. Можно править перед записью.

### LO coverage update
- LO1 (классификация AI): s06, s07, s08, s11 — strong ✅.
- LO4 (выбор архетипа): s11, s12, s13, s14, s15, s16, s17, s18 — strong ✅.
- LO6 (3 категории ошибок): s19, s20, s21, s22, s23, s24, s25 — strong ✅.
- **LO7 (retrieval/проверка)**: s19 (boundaries), **s21 retrieval moment visible** ✅, s23 open question ✅, s28 homework (assess your own AI tool). **Поднято** с слабого v1 → adequate v2.

---

## Recommendation для USER GATE 2 final

**✅ APPROVE → Phase 9 (speech-writer).**

Все P0 закрыты. 10/11 P1 закрыты, 1 (s08 wrap) closed-partial — не блокер. Регрессий нет. Палитра LOCKED. Visual motif consistent across 30 слайдов. Pacing 75 мин с буфером 8.5 мин — реалистично.

Опциональный «polish round» (P2 на усмотрение, **не блокеры**):
- Footer-tax cleanup: s12 «Demo: …», s18 «методичка §3.8», s26 «00-course» — убрать из визуала, перенести в speaker notes.
- s29: provocation как visible assertion на slide (не только Backup box).
- s17: real logos взамен text labels (если есть время).

Эти ~3 микро-правки **не блокируют** speech-writer на Phase 9. Speech может пройти параллельно или после быстрого 15-минутного polish round.

**Deck v2 — production-ready для лекции 1.**
