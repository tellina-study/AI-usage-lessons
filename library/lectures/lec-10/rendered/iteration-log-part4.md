# Лекция 10 — iteration log, часть 4 (продолжение `iteration-log.md`)

## Iteration J — s05c «Ретроспектива отрасли по годам» (owner follow-up, 2026-11-15)

**Trigger:** owner смотрел деку после добавления s05a/s05b и спросил: «а почему нет
никакой ретроспективы за последние годы и красивых графиков? нет прорывов в индустрии
как в космосе в десятки раз?» — запросил многолетнюю ретроспективу с настоящими
графиками.

**Честная находка (до рисования):** в chapter.md/chapter-part2.md НЕТ задокументированной
success-side кривой «в десятки раз» уровня космической индустрии. Реальные многолетние
точки: (а) коллапс — venture-инвестиции в ИИ для поля и вертикальных ферм −91% YoY
2024→2025 (AgFunder Year-in-Review 2025, chapter.md:243,442,465); (б) рост ЦЕНЫ
консолидации, не performance — Blue River $305M (2017) → Bear Flag $250M (2021) →
MSD/Antelliq $3,85 млрд (2024), chapter-part2.md:156-157,270; (в) единственный реальный
success-multiplier — LaserWeeder $900/акр → $550 (Braga Fresh, −39%) и → $232 (Triangle
Farms, −74%), ×1,6-3,9, уже на s16a. Решение: построить честную ретроспективу на этих
точках, не изобретать прорыв.

**Графики (matplotlib, не QuickChart — в этой sandbox нет сетевого доступа к
quickchart.io; curl-проверка дала timeout. matplotlib — тот же инструмент, что
`gen_charts.py` в lec-02/03/04/05, Ocean palette + DejaVu Sans Cyrillic-safe):**
новый скрипт `rendered/gen_charts_s05c.py`:
- `c39-vf-investment-collapse.png` — бар, 2 реальные точки (2024=индекс 100,
  2025=индекс 9, −91%), один hue (Primary light → Gold на обвальном столбце), direct
  value labels, без легенды (одна серия).
- `c40-consolidation-deals.png` — бар, 3 реальные точки по годам, **лог-шкала Y**
  (единственная ось — разброс $250M-$3 850M на порядок; лог явно читаемее линейного,
  где 2017/2021 превратились бы в невидимые полоски). Gold на 2024 (MSD/Antelliq).
  Title прямо называет это «цена, не производительность» — чтобы лог-рост сделок не
  прочитался как capability-кривая.

**4 итерации (минимум 3 выполнено с запасом):**
1. Первая сборка — **P0 overlap**: подпись под каждым чартом перекрывала x-tick labels
   графика (`caption_y` считался от `chart_box_h`, а не от фактического низа embedded
   image — несовпадение на ~0.3"). Также **P1 англицизмы**: «vertical farming» в
   подписи, «success-multiplier» в gold-strip.
2. Фикс геометрии (img_bottom считается ДО размещения, caption начинается после него +
   gap) + Russification fix («вертикальных ферм», «кратный выигрыш»).
3. Фикс англицизма внутри самого PNG — ось Y чарта 1 содержала «индекс
   venture-инвестиций» (латиница внутри картинки, не ловится text-grep по pptx).
   Перегенерирован chart → «индекс венчурных инвестиций».
4. **Честность-fix** (самая важная находка этого цикла): формулировка «было $900/акр →
   стало $550/акр (Braga Fresh) и → $232/акр (Triangle Farms)» визуально читалась как
   ПОСЛЕДОВАТЕЛЬНАЯ цепочка одного хозяйства 900→550→232, хотя это ДВА РАЗНЫХ
   хозяйства от одного и того же baseline $900 (см. s16a — Braga Fresh и Triangle
   Farms это параллельные case studies, не этапы одного процесса). Исправлено на «было
   $900/акр → $550/акр (Braga Fresh) · было $900/акр → $232/акр (Triangle Farms)» +
   явная строка «два разных хозяйства от одной и той же исходной цены — не цепочка
   одного хозяйства». Заодно убран анлийский «baseline» → «исходная цена/baseline»
   из видимого текста (был ещё один англицизм).

**Verification:**
- Deep latin scan (`tools/presentation-build/deep_latin_scan.py`) на visible body +
  speaker notes извлечённых python-pptx: 28 unique tokens вне allowlist, ВСЕ — бренды/
  имена собственные (Blue River, Bear Flag, Antelliq, GEA, CattleEye, LaserWeeder,
  Braga Fresh, Triangle Farms, AgFunder, Deere, MSD Animal Health, Allflex, Western
  Growers Case Study, John) + established citation shorthand «press» (используется по
  всей деке — «Deere press», «DeLaval press» и т.д., не новый паттерн). 0 реальных
  англицизмов.
- Timing/methodology/scaffold grep (visible body + speaker notes): 0 hits (только
  frontmatter `learning_outcomes`/`chapter_ref`, exempt).
- Speaker notes word count: 616 слов (в пределах 500-800 для лекции).
- Projector readability (50% zoom): оси и подписи чартов читаемы, direct value labels
  ≥13pt на картинке (при dpi=200 экспорте matplotlib).
- Visual Mass Balance: 2 чарта + нижняя полоса заполняют вертикаль без избыточного
  whitespace (strip_h увеличен с 1.32 до 1.9 после итерации 1, чтобы вместить
  честность-fix без потери читаемости).
- 5-Second Test: заголовок + оба чарта + gold-strip согласованно передают главное
  сообщение — ретроспектива НЕ показывает прорыв в десятки раз; PASS.
- Снимок: `snapshots/FINAL-s05c.png`.

**Files changed (owner follow-up):**
- Новый: `rendered/gen_charts_s05c.py` (генератор 2 chart PNG).
- Новые ассеты: `assets/charts/c39-vf-investment-collapse.png`,
  `assets/charts/c40-consolidation-deals.png`.
- Новый слайд-файл: `slides/s05c-retrospektiva-otrasli.md`.
- `rendered/build_lec10_p1.py` — вставлен блок s05c между s05b и s06 (divider);
  docstring header обновлён (21 слайд в part1, было 20).
- `deck.yaml` — добавлена запись s05c; header-комментарий «Total: 43 slides» дополнен
  историческим trace до факт. 56 слайдов / 89,1 мин.

**Timing impact:** 55 слайдов / 86,9 мин → **56 слайдов / 89,1 мин** (+2,2 мин, ровно
timing_min нового кадра — ни один другой кадр не менялся).

**Issue #340 (owner follow-up, s05c) Status: COMPLETE.**
