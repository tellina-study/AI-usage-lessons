# Presentation Critic — slides v3.2 SANITY CHECK — 2026-05-13

**Scope:** Phase 12.6 sanity check after designer applied 19 user-driven fixes (slides v3.1 → v3.2). Quick visual + closure review, not full rerun.
**Inputs reviewed:** iteration-log-v32.md, deck.yaml v3.2 (33 slides), 12 representative iter14 PNG snapshots, 8 sample slide markdowns (s09, s11, s12, s16, s17, s18, s19, s19a, s21), chapter §5.2.

## Verdict

**APPROVE-WITH-MINOR.**

All 19 user fixes are applied as specified. Visual quality on the rebuilt/redesigned slides is solid: layouts read cleanly, the new dialog-cycle (s16) and bottom-aligned layers (s11) work, the s12 matrix is now genuinely useful (26+ filled cells with concrete products), s19 split into s19+s19a is coherent, s21 quadrant axes work as scale markers. Palette LOCKED, motif retained, gold ≥1 per content slide, 0 footer-tax confirmed. Two P2 cosmetic issues; zero P0/P1 regressions detected.

## Closure check — 19 user fixes

| # | Fix | Status | Evidence |
|---|---|---|---|
| 1 | GLOBAL strip «Лектору» | ✅ | grep on `slides/*.md` returns 0 occurrences across all 32 source files |
| 2 | s02a no «Что мы пройдём за 75 мин» subtitle | ✅ | iter14-03 shows clean «Карта лекции — 5 разделов» title only; current section in gold |
| 3 | s04 bar chart 8 LLM rows matching s03 | ✅ | iter14-05 shows ChatGPT 27 / YandexGPT 23 / DeepSeek 20 (gold) / GigaChat 15 / Шедеврум 11 / Claude нет данных РФ / Gemini нет данных РФ / Ничем (см. donut) — все 8 опций видимы |
| 4 | s04 donut centred «51%» + circular | ✅ (P2) | iter14-05 — donut круглый, «51%» 56pt по центру, подпись «раз в неделю и чаще». Minor: bottom of «51%» glyphs слегка касается ring — читается, но не идеально центрировано вертикально |
| 5 | s04 takeaway band removed | ✅ | iter14-05 — нижняя полоса «Сравнивайте методологии…» отсутствует, footnote в одну строку |
| 6 | s05b funnel 10% single-line | ✅ | iter14-07 — funnel 100% / -90% / 10% (gold) — все три блока одна строка; 10% gold endpoint крупно и читаемо |
| 7 | s07 9 events + Vaswani deep-dive, no AI Effect | ✅ | iter14-09 — 3 группы × 3 события, single-line labels через em-dash, gold 2017 oval доминирует, Vaswani callout с 8 авторами + 160K цитирований внизу. AI Effect callout остался только на s06 (iter14-08) — не дублируется |
| 8 | s09 OpenClaw + Kimi K2.5 NEW; убраны Llama-3 + MCP | ✅ | iter14-11 — 4 эпизода: Mistral 7B / DeepSeek R1 (gold) / OpenClaw / Kimi K2.5. Все 4 single-line subtitles читаемы. Llama-3 и MCP отсутствуют |
| 9 | s11 layers bottom-aligned + teal-tinted captions | ✅ | iter14-13 — 4 концентрических Ocean rounded boxes с общим нижним краем; названия слоёв на teal-tinted полосах сверху каждого слоя; gold callout «Выбор слоя — инженерное решение» внизу слева |
| 10 | s12 icons + 26+ filled cells | ✅ | iter14-14 — 6 Lucide иконок над колонками, 26 заполнено из 30 (только text/прогноз и звук-видео/планир пустые с em-dash); YOLO в gold, BERT/spaCy/BM25/CLIP/GPT-4o/DALL-E/Whisper/Prophet/ARIMA/ReAct/Devin/OpenClaw — конкретные продукты вместо абстрактных типов |
| 11 | s15 pipeline RIGHT_ARROW shapes | ✅ | iter14-16 — 5 блоков (Сырой вход / Препроцессинг / Модель / Постпроцессинг / Выход), gold-стрелки между ними чёткие, отсутствуют артефакты от старого rect+rotated_triangle |
| 12 | s16 dialog cycle redesign | ✅ | iter14-17 — USER слева в двух кругах (отправитель сверху + получатель снизу), Сообщение → LLM → Ответ → USER, Системный промпт сверху с gold-стрелкой вниз, ⋮ continuation indicator под Ответом, 2 gold callouts справа. Layout читается за 2-3 секунды |
| 13 | s17 production disclaimer card | ✅ | iter14-18 — слева кейс корп.чата с примером диалога, справа gold-tinted Ocean rounded box «Чистые чаты почти не используются в production. Почти везде расширены до агентов — для долгосрочной памяти и RAG». Bar chart полностью заменён |
| 14 | s18 USER added with bidirectional arrows | ✅ | iter14-19 — USER (LIGHT синий круг) слева, две стрелки → / ← к LLM/Chat блоку, Оркестратор сверху в gold, Память + Инструменты внизу. Layout сбалансирован |
| 15 | s19 split → s19 + s19a | ✅ | iter14-20 = s19 (200 PDF, 7 нумерованных шагов с teal-tinted tool boxes справа, gold orchestrator loop, gold takeaway внизу). iter14-21 = s19a NEW (5 уровней Operator→Observer слева с gold уровнем 5; справа 4 рамки in/on/out/Override с gold out-of-the-loop; gold takeaway внизу). Два слайда согласованы по structure |
| 16 | s21 Q1 vertical-LEFT + Q2 horizontal-BOTTOM, no takeaway | ✅ | iter14-23 — ВОПРОС 1 «Нужно ли взаимодействие?» с маркерами ДА (gold-tinted) / НЕТ (white) в narrow left column на vertical axis; ВОПРОС 2 «Нужна ли работа с инструментами?» с маркерами НЕТ / ДА (gold) под колонками квадранта. Маркеры читаются как scale markers, не как декорация. Bottom takeaway отсутствует |
| 17 | s28 homework simplified | ✅ | iter14-30 — gold callout «Принесите свой AI-инструмент → пропустите через 2-вопросный квадрант → одностраничный разбор». «Защитите перед группой» отсутствует. Subline «Любой формат (текст / схема / таблица). Тема семинара — Какой тип AI выбрать» |
| 18 | s29 + chapter §5.2 module reshuffle | ✅ | iter14-31 — М1: 1 Введение / 2 БМ / 3 Агенты / 4 ПО / 5 Финансы / 7 Медицина (no 6, no 8). М2: 6 Инж.проект / 9 Авиакосмос / 10 Сельское / 11 Производство / 12 Цифр.двойники. М3: 8 Креативные / 13 Логистика / 14 Телеком / 15 Наука / 16 Нефтегаз / 17 Синтез. Chapter §5.2 confirmed sync via grep |
| 19 | s30 no YOLO callback, full-width 4-concept grid | ✅ | iter14-32 — Токены / Эмбеддинги / Внимание / Температура в 2×2 grid с иконками; bottom takeaway «Эти 4 концепта объясняют поведение всех современных LLM — от ChatGPT до DeepSeek». YOLO frame отсутствует |

**19/19 fixes applied as specified.**

## P0 issues (блокеры)

None.

## P1 issues (важные)

None. Все redesigned slides читаются за положенное время и не имеют overflow / overlap / illegibility артефактов.

## P2 issues (косметика)

### P2-1 — s04 donut «51%» vertical centring slightly off
**Slide:** s04 (iter14-05).
**Issue:** Цифра «51%» 56pt по центру donut'а — нижний edge глифов («5») слегка касается донат-ring'а внизу. Подпись «раз в неделю и чаще» 11pt italic тоже почти прижата к ring'у.
**Recommendation:** Если donut PNG будет regenerated в дальнейшем — поднять центр текста на ~3-4% высоты donut, чтобы цифра + subtitle были визуально центрированы как блок, а не текст-anchor по средней линии. Не блокер для презентации.
**Visual evidence:** в iter14-05 — глифы «51%» в нижней половине внутреннего отверстия donut'а.

### P2-2 — s09 эпизоды с 2-line subtitles читаются неравномерно
**Slide:** s09 (iter14-11).
**Issue:** Mistral 7B имеет 2 строки subtitle («Apache 2.0» / «обходит Llama-2 13B»), у DeepSeek R1 — 2 строки («$589B» / «Nvidia drop за день») с gold-выделением второй строки, у OpenClaw — 2 строки («100K★ stars» / «за квартал»), у Kimi K2.5 — 2 строки («open multimodal» / «swarm mode»). Все читаемы, но иерархия (что tagline, что метрика) непоследовательна между карточками: у DeepSeek gold подсвечивает обе строки — у OpenClaw / Kimi нет gold внутри карточки.
**Recommendation:** Для consistency — выделить gold ОДНУ метрику в каждой карточке (например: «100K★» в gold у OpenClaw, «swarm mode» в gold у Kimi K2.5). Тогда eye наводится на ключевую цифру каждого эпизода. Не блокер.
**Visual evidence:** iter14-11.

## Visual policies — сохранены ✅

- **Palette LOCKED Ocean+Teal+Gold.** На всех проверенных snapshots: deep navy `#21295C` (titles, нижний слой), teal `#028090` (secondary cards), Ocean blue `#065A82` / `#1C7293` (motif strokes), Gold `#F0AB00` (1-2 акцента/слайд). Никаких новых hue не появилось.
- **0 footer-tax.** Проверил 12 snapshots — нет «Demo:», «Код:», «методичка §X», «Backup:», «Refs:». Только семантический content + reference внутри карточек где это часть данных (например, «ВЦИОМ окт 2025, n=1600, multi-select» в s04 — это data attribution, не footer-tax).
- **Visual motif Ocean rounded box** — на каждом content слайде есть один или несколько Ocean rounded boxes (radius 12, surface `#F4F7FA`, stroke `#1C7293`). Confirmed on s05b, s09, s11, s12, s16, s17, s18, s19, s19a, s21, s23, s28.
- **Gold ≥1×/слайд.** Confirmed на каждом из проверенных content slides — где-то gold accent, где-то gold callout, где-то gold endpoint funnel'а / 2017 oval / takeaway band.
- **0 неестественных англицизмов на visible content.** Терминология: где есть английский — это либо product name (ChatGPT, GPT-4o, Claude, DeepSeek), либо устоявшийся термин с русским переводом рядом («attention» рядом с «Внимание», «vector DB» рядом с «эмбеддинги»). На s09 «open multimodal» / «swarm mode» / «$589B Nvidia drop» — всё это технические термины, естественные для контекста. Не нашёл проблемных конструкций.

## Strong points retained / improved

1. **s11 nested layers** — теперь действительно работает как mental model. Bottom-aligned дает ощущение «слой стоит на земле»; teal-tinted полосы с компонентами читаются как metadata о каждом слое; левая колонка с «Каждый следующий слой включает предыдущий» + gold callout внизу даёт двойную подачу assertion'а (визуальную + вербальную).
2. **s12 matrix** — был большой риск в v3.1, что заполненная матрица станет нечитаемой стеной. С Lucide иконками над колонками + цветовым кодированием (MID/LIGHT/TEAL/GOLD по типу задачи) + 26+ ячеек — теперь это самый информативный слайд лекции, и при этом scannable.
3. **s16 dialog cycle** — переход от 6 vertical step boxes к компактной diagram с 2 USER кругами + Сообщение/Ответ + LLM + Системный промпт сверху с gold-стрелкой — намного интуитивнее. Цикличность подчёркнута continuation indicator «⋮ следующая итерация».
4. **s19 + s19a split** — действительно даёт каждому концепту своё пространство. s19 показывает «как агент работает» через worked example с tool-аннотациями, s19a даёт «уровни автономии» как design vocabulary. Pacing 1.5+1.5 vs прежние 2.5 — оправданное разделение, +0.5 минут к разделу 3.
5. **s21 quadrant axes** — Q1/Q2 как scale markers (а не как заголовки) — это корректный assertion-evidence pattern. Студент видит «ВОПРОС 1: Нужно ли взаимодействие?» рядом с осью, и ДА/НЕТ маркеры на этой оси показывают, как читать квадрант. Снятие takeaway band внизу освободило место для маркеров без overflow.
6. **s17 production disclaimer** — концептуально важный fix. Bar chart с распределением LLM РФ дублировал s04; production disclaimer уникально вводит понятие «чистый чат vs чат-расширенный-до-агента» и подготавливает s18.

## Cross-deck consistency

- **Speaker notes formatting** — все 32 файла теперь имеют только «## Speaker notes» секцию (150-300 слов) без «## Лектору» блока. Это означает: студент, читающий PPTX через 2 недели, видит цельный нарратив без режиссёрских пометок. Лекторские cues переехали в speech.md (отдельный артефакт). Архитектурно правильно.
- **Section dividers** (s02a / s10 / s22 / s27) — все используют единый template из Fix-17: 6 cards 0..5 horizontal, current section card в gold. Разница только: s02a в overview-state (без выделения current — все равноправные), остальные в zoom-in state (current gold-filled). Confirmed visually.
- **Chapter §5.2 ↔ s29** — оба обновлены до М1 (1-5, 7) / М2 (6, 9-12) / М3 (8, 13-17). Confirmed via grep.
- **Pacing arithmetic** — active 62.5 min + buffer 12.5 min = 75 min total. Раздел 3 теперь 23.0 min (после +0.5 от s19 split). Числа в deck.yaml `pacing:` consistent с описанием в iteration-log-v32.md.

## Recommendation

**APPROVE для перехода к Phase 13 (speech.md update).**

Два P2 issues — cosmetic, не блокируют использование deck'а. Если будет ещё одна build-iteration — можно прихватить P2-1 (donut centring) и P2-2 (s09 gold consistency); если нет — slides v3.2 ready as-is.

Главное достижение revision'а: 19 разнородных fixes применены без введения новых регрессий, и большинство из них — особенно s11/s12/s16/s19+s19a/s21 — улучшают пед.value слайдов, а не просто косметику. Designer'у можно засчитать качественную работу.

**Next step как рекомендовано в iteration-log-v32.md:** speech-writer Opus обновляет speech.md под изменения (особенно s09 episodes, s07 Vaswani, s17 production disclaimer, s19+s19a split, s28 homework, s29 reshuffle, s16 dialog cycle).
