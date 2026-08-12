# Лекция 3 — Visual-loop iteration log (часть 2)

Продолжение `iteration-log.md` (часть 1 достигла лимита 600 строк).

---

## v4.2 — точечный полировочный патч (issue #157 review, post-QA)

**Контекст:** дека уже прошла полный QA-цикл (presentation-critic +
student-simulator + reader-simulator + consistency-checker), все 4 отчёта —
APPROVE-WITH-POLISH / чисто, 0 P0. Ниже — единый проход по 8 точечным
находкам (не 5 отдельных visual-loop проходов на слайд — это разумные
точечные фиксы, не редизайн).

**Rendering environment note:** в этой сессии LibreOffice/`soffice`
недоступен в sandbox (не установлен, нет root/sudo для установки) → PNG
snapshot regen через `libreoffice --headless --convert-to pdf` +
`pdftoppm` физически невозможен. Верификация сделана через:
1. `python3 build_v3.py` — полная пересборка pptx (успех, 40/40 слайдов,
   без исключений).
2. Программная geometry-проверка через python-pptx: bounding-box каждого
   шейпа на каждом из 40 слайдов — 0 шейпов за границами canvas
   (13.333×7.5"), ручная сверка координат на предмет overlap для всех
   4 изменённых слайдов (s11/s12/s19/s25b) — coordinates пересчитаны
   вручную, 0 коллизий найдено (см. детали по каждому слайду ниже).
3. Deep latin-token scan (`tools/presentation-build/deep_latin_scan.py`)
   на extracted PPTX visible text — 334 occurrences / 176 unique
   (было 338/176 в v4.1) — профиль не изменился, новых англицизмов нет.
4. Scaffold/timing/methodology grep sweep на visible layer — 0 hits
   (включая проверку, что `[требует подтверждения]` действительно исчез
   с видимого слоя).

Визуальный PNG-инспекшн (обязательный шаг §5 pipeline) **не выполнен** в
этой сессии из-за окружения — это ограничение отмечено явно, не скрыто.
Рекомендация: при следующей сессии с доступным LibreOffice — прогнать
полный snapshot regen + визуальную проверку s11/s12/s19/s25b (минимум)
как inspection follow-up, до финального USER GATE sign-off.

### Применённые фиксы

**1. s19 (`build_s19`, build_v3.py) — P1 presentation-critic.**
Trust-warning блок (MCP-доверие, teal box справа): 3 буллета → 2. Оставлены
самые нагруженные по смыслу: (а) код в окружении / доступ к данным —
корневая причина риска, (б) описание попадает в контекст — носитель prompt
injection — конкретный вектор атаки. Убран третий («ещё одна граница
доверия и retention-политика») — он дублируется на s25 (ZDR-блок), поэтому
без потери контента. Bullet spacing увеличен 0.44"→0.52" на освободившееся
место. Хронология брендов (Anthropic 11/2024 / OpenAI 03/2025 / Google
04/2025): font дат 10pt italic → 11.5pt bold italic (тот же размер, что имя
бренда) для проекторной читаемости на заднем ряду.

**2. s19 footer — P2 student-simulator.**
«Числа экономии prompt caching и масштаб экосистемы MCP — в главе;
перепроверить ко дню лекции.» → «Актуальные цифры экономии и масштаб
экосистемы MCP — в главе методички.» Убран императив «перепроверить» (читался
как незакрытый TODO лектора) — теперь звучит как обычная справочная сноска
для читателя.

**3. s11/s12 (`build_s11`/`build_s12`) — P1 presentation-critic.**
Оба слайда использовали идентичный skeleton «N карточек + итоговая
плашка» подряд → визуально сливались. Content/текст не тронут. Визуальная
дифференциация s12 (не s11, чтобы не трогать уже устоявшийся s11):
- Базовая палитра карточек: `LIGHT`/`SURFACE` (primary blue, как у s11) →
  `TEAL_TINT`/`TEAL` (teal accent) — регистр «исключающие критерии /
  осторожность» вместо s11's «primary blue = признаки за RAG».
- Добавлен нумерованный gold/teal badge-кружок в левом верхнем углу каждой
  карточки (паттерн из s22b slot-badge) — силуэт, которого нет у карточек
  s11 (там карточки без номеров).
- Убран текстовый префикс «1./2./3.» из заголовка карточки (дублировался
  бы с новым badge) — сам номер теперь несёт badge, не текст.
- Card 3 (критерий «данные доступны live через API/MCP») остался
  gold-выделенным (как в v4.1) — это не тронуто, сохраняет «сильнейший
  критерий» семантику.
Geometry пересчитана и проверена: badge `x+0.20..0.52`, icon
`x+cw-0.76..cw-0.24`, title text box `x+0.66` шириной `cw-1.55=2.45"` —
между badge и icon, 0 overlap. Макс. 2 строки заголовка при 15pt bold в
2.45" (проверено оценкой char-width), помещается в 0.78"-box.

**4. s25b (`build_s25b`) — P1/P2 student-simulator + reader-simulator.**
OpenHands card note: `[требует подтверждения] вероятный кандидат на
«OpenClaw» из issue #157 — рабочая гипотеза по совпадению профиля, не
установленный факт` (134 симв, читался как незакрытый TODO/draft-синтаксис)
→ `рабочая гипотеза по совпадению профиля — вероятный кандидат на
«OpenClaw», не подтверждённый факт` (97 симв, органичная проза-hedge, тот
же italic 9.5pt что и раньше). Короче на 37 симв → без риска overflow в
существующем `nb_h=1.30` note-боксе (проверено).

**5. Определение agent-harness-registry — P1 reader-simulator.**
Термин используется как источник авторитетности данных на s22b/s22c/s22d/
s25b, нигде не объяснён. Добавлена inline-define строка в speaker notes
s22b (первое использование термина в разделе): «agent-harness-registry —
это независимый публичный реестр, который тестирует экипировку агентов
(память, skills, subagents, MCP) через live-eval бенчмарки на реальных
задачах, а не через вендорские самоотчёты о возможностях.» Не дублируется
на s22c/s22d/s25b — там термин уже используется коротко, читатель отсылается
к первому определению по порядку чтения. Notes word count после правки: 248
слов (в допустимом диапазоне 150-300).

**6. s22d (Tier легенда) — P1 reader-simulator.**
Speaker notes s22d дополнены: «На слайде системы помечены буквой Tier — это
рейтинговая категория реестра от A (лучшие результаты) до D (худшие) по
сумме бенчмарков live-eval; чем ближе к A, тем стабильнее система
показывала себя на полном наборе тестов.» Вставлено перед первым упоминанием
«Letta, Tier D» в тексте notes. Notes word count: 298 слов (на границе
допустимого диапазона 150-300, но в пределах).

**7. s25 (ZDR gloss) — P2 reader-simulator.**
Speaker notes s25 дополнены inline-define при первом развёрнутом упоминании
ZDR: «ZDR, Zero Data Retention, — это политика вендора не сохранять
содержимое запросов после обработки». Вставлено перед существующим
предложением про судебный приказ NYT v. OpenAI. Notes word count: 290 слов
(в допустимом диапазоне).

**8. Frontmatter-фиксы (housekeeping, не влияют на рендер).**
- `slides/s21-agent-loop.md`: `callback s07` → `callback s06` (2 места:
  `learning_goal` frontmatter + inline visible-body caption). Проверено:
  s07 не существует как файл/слайд; контент про faithfulness/human-validator
  живёт на s06 («chain-of-thought… человек проверяет результат, а не
  самообъяснение») — callback теперь указывает на реальный слайд.
- `slides/s29-human-validator-nanda.md`: `callback s07` → `callback s06`
  (2 места: `learning_goal` + `visual_brief` frontmatter). Тот же callback
  target fix.
- `slides/s30-bridge-homework-qa.md`: `(s28)` → `(s27)` (visible body,
  «Mini-apply задача B»). Проверено: «Разминка (задача B)» контент
  фактически построен в `build_s27` (grep по build_v3.py), не s28 — s28
  вообще не существует в деке. s30's md-файл — единственное место, где
  фигурировал `(s28)`; в build_v3.py эта ссылка не хардкожена, так что
  правка изолирована к markdown.
- `slides/s16-catastrophic-forgetting.md`: `chapter_ref: "§3.3` →
  `chapter_ref: "§3.4` (frontmatter). Проверено по chapter-part2.md TOC:
  «3.4. Провал: catastrophic forgetting» — точное совпадение с содержанием
  s16 («Провал: catastrophic forgetting»); §3.3 — это «Когда fine-tuning
  оправдан», другой раздел. Старая ссылка была стале.
Ни один из этих 4 паттернов (`callback s07`, `(s28)`, `§3.3` для s16) не
встречается в `build_v3.py` — все 4 фикса изолированы к markdown-источникам,
без изменения рендера.

### Пересборка + верификация

```
python3 build_v3.py
# → saved lec-03.pptx — 40 slides (успех, без исключений)
```

Post-build checks (все — программные, см. rendering environment note выше):
- python-pptx geometry sweep: 0 shapes out-of-bounds (40/40 слайдов).
- Manual coordinate re-derivation для s11/s12/s19/s25b: 0 overlaps.
- Deep latin scan: 334/176 (было 338/176) — не регрессировал.
- Scaffold/timing/methodology/bracket-leak grep: 0 hits на visible layer.

### Files touched

`rendered/build_v3.py` (4 функции: `build_s12`, `build_s19`, `build_s25b` —
+ docstring комментарий в `build_s11` region не менялся, только `build_s12`),
`rendered/lec-03.pptx` (rebuilt), `slides/s19-api-layer.md` (не трогался —
footer/bullets только в build-скрипте, markdown source этого слайда носит
характер spec, не 1:1 rendered text), `slides/s22b-agent-equipment.md`,
`slides/s22d-memory-failure.md`, `slides/s25-tool-attacks.md` (speaker notes
дополнены), `slides/s21-agent-loop.md`, `slides/s29-human-validator-nanda.md`,
`slides/s30-bridge-homework-qa.md`, `slides/s16-catastrophic-forgetting.md`
(frontmatter housekeeping).

**Не тронуто:** `rendered/lec-03.pdf` и `rendered/snapshots/*.png` — не
regenerated в этой сессии (LibreOffice недоступен, см. environment note).
Требуется regen перед финальным USER GATE, если snapshots используются
как evidence.

VERDICT v4.2: 8/8 запрошенных фиксов применены точечно, pptx пересобран
успешно, geometry programmatically verified 0 overlaps/out-of-bounds,
anglicism profile не регрессировал. **Открытый пункт:** визуальный
PNG-инспекшн (Anthropic vision-loop principle) не выполнен из-за
недоступности LibreOffice в этой sandbox-сессии — рекомендуется как
follow-up перед финальным sign-off. Не закоммичено (по инструкции).
