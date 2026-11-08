---
issue: "#304, блок B — продолжение"
дата: "2026-10-29"
см_также: "B-vizual-i-verstka.md (§1–§2: карта области, канон правил)"
---

# Блок B (продолжение). §3–§7

Первая часть — [`B-vizual-i-verstka.md`](B-vizual-i-verstka.md): §1 карта области, §2 канон правил
(70 строк в шести группах A–F).

---

## §3. Расхождения

Места, где практики противоречат друг другу или противоречат текущему решению курса. Каждое —
с обеими сторонами и тем, что из этого решить для нашего случая (не окончательное решение —
материал для следующего шага гайдбука).

### 3.1. Тёмный фон vs светлый фон

- **За тёмный:** в большой затемнённой аудитории (>50 человек — типичный лекционный поток) тёмный
  фон с светлым текстом даёт контраст до 21:1, что покрывает ухудшение условий проекции с запасом
  (mlcpresentations.com; modernpresenter.wordpress.com).
- **За светлый:** светлый фон снижает утомление глаз при включённом или частично включённом свете
  — а курс требует конспектирования на лекции, то есть свет в зале скорее включен частично.
- **Сам Tufte отказывается рекомендовать единое решение** и прямо пишет, что нужно «смотреть на
  реальных условиях» конкретного проектора и зала, а не решать по обсуждению
  (`edwardtufte.com/notebook/recommended-background-for-projected-presentations/`).
- **Для курса:** решение (светлый фон, Ocean палитра на белом/`SURFACE`) принято и не пересматривается
  этим документом — но оно НЕ было проверено замером в реальной аудитории МГТУ с реальным
  проектором, как советует Tufte. Контраст-пороги `deckkit/contrast.py` сами по себе (см. §6.2) тоже
  признают эту границу: «равен WCAG, потому что на проекции не мерено».

### 3.2. Засечки (serif) vs без засечек (sans-serif) на проекторе

- Общепринятая практика презентаций — без засечек на проекторе (меньше артефактов при низком
  разрешении, более ровная толщина штриха на дешёвых проекторах).
- Книжная типографика (Bringhurst) не делает такого разделения впрямую — засечки улучшают
  направляющую строки НА БУМАГЕ при длинном непрерывном чтении.
- **Для курса:** вопрос решён архитектурно (`theme.FONT = "Arial"`, без засечек) и это согласуется
  с практикой презентаций — конфликта с Bringhurst нет, потому что Bringhurst пишет о другом
  носителе (печатная книга, не проекция).

### 3.3. Плотность кадра: питч vs лекция

- Guy Kawasaki «10/20/30»: минимум 30 пт, то есть физически мало знаков на кадре — рассчитано на
  **инвестиционный питч**, 10 слайдов за 20 минут, цель — не читать с экрана вовсе.
- Garner & Alley (Penn State), assertion-evidence: ассерция + визуальное доказательство — это
  РАЗМЕР текста заголовка (сентенция), а не запрет на плотность тела.
- Курсовое снятие ограничения «3–5 строк» (владелец, 2026-10-08) разрешает тяжёлые кадры —
  **для технического разбора**, не для питча. Это не противоречие исследованиям, а выбор другого
  жанра: лекция с разбором кейса — не инвестиционная презентация, и 30-точечное правило Kawasaki
  к ней неприменимо впрямую (см. правило B7 части 1).
- **Расхождение по существу:** оба источника правы для СВОЕГО жанра. Ошибка — прилагать 10/20/30 к
  техническому разбору или плотный технический кадр — к питчу.

### 3.4. Нулевая ось vs нет

- Cairo: нулевая база обязательна для length/height-кодирования, если ноль содержательно значим.
- Контрпример самого Cairo: температура тела 95–105°F — ноль не значим, обрезка не обманывает.
- **Для курса:** все диаграммы `analitika.py` (`stolbtsy`/`gruppy`/`linii`) жёстко ставят
  `beginAtZero: True` без исключений в коде. Это строже Cairo (который допускает исключение), но
  у наших данных (доли, количества людей, деньги) ноль почти всегда значим — исключения пока не
  встречались. Если встретится величина без значимого нуля (например, индекс со средним 100) —
  это узнаваемое расхождение с текущим кодом, которое придётся решать явно, а не молчать.

### 3.5. Легенда vs прямая подпись

- Общее правило data-viz — прямая подпись лучше легенды почти всегда.
- Собственное решение курса (`analitika.gruppy`) оставляет легенду ОБЯЗАТЕЛЬНОЙ там, где серий
  несколько и прямая подпись физически не поместится у конца каждого столбца при горизонтальной
  раскладке. Это не расхождение с источником — источник сам называет это допустимым исключением
  (depictdatastudio.com: «много серий близко по значению» — ровно наш случай группированных
  столбцов по странам/регионам).

### 3.6. WCAG AA как потолок vs как пол

- Решение курса (`contrast.py` докстринг): «порог равен WCAG, не строже, потому что строгий порог
  никто не мерил на настоящей проекции» — то есть WCAG AA используется как ВЕРХНЯЯ допустимая
  граница.
- Практика AV для больших залов (контраст 21:1 между белым и чёрным, п.3.1) предполагает, что
  РЕАЛЬНО нужный контраст на плохой проекции заметно ВЫШЕ, чем web-ориентированный WCAG AA минимум
  4,5:1/3:1 — то есть для зала WCAG AA может оказаться НИЖНЕЙ, а не верхней безопасной границей.
- **Расхождение не решено.** Курсовое решение осознанно консервативно в объявлении («не
  усиливаем порог, пока не измерили»), но контекст применения (проектор, задние ряды, посаженная
  лампа — ровно слова из `contrast.py`) типологически ближе к условиям, где рекомендуют контраст
  выше web-минимума. Замер на настоящем проекторе курса — открытый вопрос, не закрытый этим
  документом.

---

## §4. Что алгоритмизируемо

### 4.1. Hard — скрипт по PPTX/PNG/PDF, порог формулой, инструмент назван

| Метрика | Порог | Инструмент | Статус у нас |
|---|---|---|---|
| Контраст текст/фон пары (WCAG) | 4,5:1 обычный / 3,0:1 крупный (≥18пт либо ≥14пт полужирный) | `python-pptx` + формула относительной яркости WCAG 2.x | **есть** — `deckkit/contrast.py`, доказано selftest'ом (`selftest_contrast.py`) |
| Кегль ниже пола видимого слоя | 12,0 пт по НАСТОЯЩЕМУ кеглю прогона | `python-pptx` runs | **есть** — `deckkit/floor.py` |
| Наложение (overlap) текстовых прогонов | площадь пересечения >2 кв.пт И >12% площади меньшего прогона | `PyMuPDF`/`pymupdf` по собранному PDF | **есть** — `nalozhenie_bbox.py`, доказано `--selftest` |
| Плотность текста кадра | ≤140 слов/кадр, медиана ≤90 слов/раздел (не блокирует) | парсер фронтматтера + тела | **есть** — `deckkit/plotnost.py` |
| Выход текста за поля кадра (ширина/высота рамки) | текст не наезжает сам на себя при рендере | расчёт ширины строки по метрикам шрифта | **есть** — `deckkit/metrics.py` (`[высота]`/`[ширина]`/`[кегль]` — блокирующие) |
| Число знаков в строке (длина строки) | 45–75 печатный / 45–90 экранный (Bringhurst/Butterick) | `pdfmeasure.py` даёт bbox строки — остаётся досчитать символы по кеглю | **частично** — bbox есть, явного счётчика «знаков в строке против диапазона» нет |
| Разъезжание пары столбцов по высоте (число строк) | равное число строк пары на подобранном кегле | `twocol.fit_two`, сторож `[пары]` в `rowblocks.py` | **есть**, доказано на сломанном входе |
| Кегль диаграммы в точках слайда ниже пола | 12,0 пт (умолчание подписей 13,0) | `analitika._pol` | **есть**, отказ без объявленного исключения |
| Числа по-русски (запятая, разряды) на диаграмме | 0 точек вместо запятых в видимом слое | `analitika._perevodchik` | **есть** |
| Научная запись в видимом теле | 0 вхождений `\d+[.,]\d+\s*[·×]\s*10` | grep по собранному видимому слою | **есть как правило (§5.14), не формализовано как отдельный прогон-скрипт** — делается руками |
| Разрешение растрового изображения | ≥150 PPI (минимум), 200–300 PPI комфортно | ширина_px / ширина_на_слайде_in через `python-pptx` (`shape.image.size`, `shape.width`) | **ОТСУТСТВУЕТ** — ни одного прогона, который достаёт DPI встроенной картинки и сверяет с её размером на кадре |
| Соответствие цвета палитре курса (off-palette check) | все заливки/цвета текста ∈ {DEEP, MID, LIGHT, TEAL, SURFACE, WHITE, GOLD, OUTLINE, …} | обход всех run/fill в `python-pptx`, сверка hex с `theme.py` | **ОТСУТСТВУЕТ** — `contrast.py` считает контраст НАЗВАННЫХ цветов, но не проверяет, что цвет вообще из палитры; «левый» hex из ошибки копипаста прошёл бы контраст-проверку, если случайно оказался контрастным |
| Доля пустого пространства кадра | ≥30–40% (hero ≥60%) — порог не из курса, из общей практики | сумма площадей непрозрачных shape/picture bbox / площадь кадра | **ОТСУТСТВУЕТ** |
| Безопасная зона (title/action safe) | текст в 90%×90%, контент в 93–95% | bbox текста против границ 0,05·W/H от края | **ОТСУТСТВУЕТ** как отдельный прогон (у `metrics.check_thin_margin` есть близкий, но не тождественный смысл — остаток поля вокруг тела, не безопасная зона конкретного прогона) |
| Цветовая слепота — симуляция палитры | Okabe-Ito / сравнение под дейтеранопией-протанопией-тританопией | матрица преобразования CVD (стандартные формулы Brettel/Viénot/Machado) на hex-коды палитры | **ОТСУТСТВУЕТ полностью** — ни разу не прогонялось |
| Иконки одного семейства/веса в кадре | единый stroke weight ±10% (уже формулировано в README §5.5 п.5) | сверка SVG `stroke-width` исходных файлов до рендера в PNG | **есть как ручной Schema Readability Checklist (глазами), не как скрипт** |
| Выравнивание блоков по сетке/модулю | left/top координаты кратны модулю сетки ± допуск | `python-pptx` координаты shape | **ОТСУТСТВУЕТ** — у нас геометрия задаётся числами руками в `Geometry` каждой деки, но нет прогона, который проверяет кратность модулю |

### 4.2. Soft — только глазами/суждением

- **Работает ли визуал на assertion** (доказывает ли схема тезис заголовка, а не просто иллюстрирует тему) — требует понимания содержания, не формализуется.
- **Оптическое выравнивание** (п. A6) — зазор между геометрическим и воспринимаемым центром формы.
- **5-Second Test** (README §5.5 п.2) — «понял ли студент главную мысль схемы за 5 секунд» — по определению субъективная проба.
- **Projector Readability при мысленном уменьшении до 50%** (README §5.5 п.3) — имитация задних рядов без реального замера освещённости и расстояния.
- **Правило третей / Z-паттерн «работает»** — выбор композиционного центра, не числовая проверка.
- **Семантика цвета** (несёт ли golden акцент содержательный смысл, или это декор) — требует понимания роли элемента на кадре.
- **Экспозиция примера в названии и первом блоке** (§5.18) — читается ли «что за случай и что в нём делали» за первые два элемента — задача понимания текста, не счёта символов.
- **«Та ли это схема»** (`proverki-i-pravila.md`) — машиной недоступно по построению: файл на месте, геометрия в порядке, а смысл не совпал с содержанием слайда (нужна сверка на настоящей сборке глазами).
- **Качество фото** (настоящий снимок или стилизованная подделка) — по текущему правилу §5.7 проверяется vision-моделью (Claude), не формулой.

### 4.3. Прежде чем добавлять новый hard-check

Общий корень, который `proverki-i-pravila.md` формулирует для процесса в целом, применим и к новым
автоматическим проверкам из §4.1: проверка сдаётся прогоном на заведомо ломаном входе
(`--selftest`), а не доверием к собственной логике. Любая из четырёх «ОТСУТСТВУЕТ» проверок выше,
если будет реализована, обязана доказать на искусственно сломанном файле, что она умеет сказать не
только «ноль».

---

## §5. Границы применимости

Этот раздел — явная привязка канона §2 к конкретному техническому случаю курса, а не абстрактная
типографика.

- **Формат 16:9, холст 13,333″×7,5″ (1920×1080 эквивалент).** Все пороги в пунктах (пт) выше — это
  пункты слайда (1/72 дюйма), не пиксели картинки; расхождение между ними — ровно та ловушка,
  которую `analitika.py` и `scheme.py` явно называют и избегают (правило D14/A9 части 1).
- **PPTX через `python-pptx` + рендер LibreOffice headless.** Это определяет, ЧТО измеримо: XML
  даёт точные bbox, кегль, цвет заливки — но не даёт «что увидит глаз» там, где LibreOffice и
  реальный PowerPoint рендерят по-разному (шрифтовые метрики, антиалиасинг). Мера берётся с
  ВЫВОДА сборки (`.pdf`/`.png`), а не с намерения кода — это принцип, уже сформулированный в
  `proverki-i-pravila.md» («инструмент, через который смотрят, обязан быть тем же, который
  собирает продукт»).
- **`Arial` → рендерится `Liberation Sans`** (метрически совместимый аналог, `notes/mcp-limitations.md`
  #223-10). Правила о кириллических гарнитурах (B14) формально не соблюдены буквально (курс не
  использует PT Sans/Golos/Manrope), но практически совместимы: Liberation Sans имеет полный
  кириллический набор и 4 начертания. Делать замену шрифта этим документом не рекомендуется —
  рекомендуется зафиксировать, что текущее решение СОВМЕСТИМО с каноном по существу (полнота
  начертаний и кириллицы), а не по букве (конкретное имя гарнитуры).
- **Палитра Ocean зафиксирована (LOCKED)**: `#21295C`/`#065A82`/`#1C7293` + `#028090` + золото
  `#F0AB00`. Все цветовые правила §2.C применяются К ЭТОЙ палитре, не предлагают новую. Единственное
  предложенное действие — проверка (CVD-симуляция, OKLCH-монотонность), не замена цветов.
  Исключение — уже найденный и не починенный дефект золота (issue #240, правило C13).
- **Русский текст.** Правила длины строки (B1/B2) взяты из исследований на латинице — кириллица в
  среднем НЕМНОГО шире на знак при том же кегле (не измерено нами отдельно, [не проверено]); порог
  в 66 знаков для русского текста может быть оптимистичным. Это не повод менять порог без замера —
  повод пометить его как перенесённый с допущением.
- **Проекция в вузовской аудитории + публикация PDF + печатные заметки лектора.** Три разных
  носителя с разными требованиями к контрасту и кеглю:
  - проекция — наихудшие условия (задние ряды, свет в зале), отсюда B8/B9/C11;
  - PDF-публикация — читается с экрана до 1 метра, WCAG AA (C1/C2) здесь прямо применим в
    исходном, не ослабленном виде;
  - печатные заметки лектора — отдельный носитель, где кегль печати и кегль видимого слоя кадра
    РАЗНЫЕ по определению (речь, не слайд) — правила §2.B к заметкам не применяются вовсе
    (оговорено в `plotnost.py`: заметки не входят в счёт видимого слоя).
- **Деки собираются двумя независимыми сборщиками** (`build_lec06_p1.py`, `build_lec07.py`) с
  разными числами геометрии (поле 0,55″ у обоих, но верх тела 1,34″ vs 1,46″, подвал 7,00″ vs
  6,94″). Правила сетки (A1, A7) верны ВНУТРИ одной деки; между деками идентичность не гарантирована
  до объединения через `deckkit/geometry.Geometry` (упомянуто в `theme.py` docstring как открытый
  вопрос, не этого документа).

---

## §6. Дельта к текущим правилам курса

### 6.1. Подтверждается внешними источниками

- **Снятие ограничения «3–5 строк видимого текста»** (владелец, 2026-10-08) НЕ противоречит
  исследованиям плотности — Garner & Alley показывают превосходство assertion-evidence над
  bullet-list НЕ по количеству строк, а по структуре (тезис + визуальное доказательство против
  перечня). Miller «7±2» как аргумент ЗА лимит строк — методологически некорректен по признанию
  самого Tufte (§2.F7). Снятие лимита в пользу физического предела (`[высота]`/`[кегль]`) —
  решение, согласованное с источниками, а не отступление от них.
- **WCAG AA как единый порог контраста** (`contrast.py`) — совпадает с признанным индустриальным
  стандартом (W3C SC 1.4.3) буквально по числам (4,5:1/3,0:1, граница крупного текста 18/14пт).
- **Знаменатель как часть подписи столбца, не легенда** (`analitika.py`) — прямо совпадает с
  принципом direct-labeling из практики data-viz (§2.D9/D10) и с Cairo (нельзя показывать долю без
  базы).
- **Нулевая ось по умолчанию у всех диаграмм** (`beginAtZero: True`) — совпадает с Cairo буквально.
- **Столбцы (длина/позиция), не площадь/угол, как основной тип диаграммы курса** — совпадает с
  измеренной иерархией Cleveland & McGill и с отказом от native pie/donut (anti-pattern #10 README).
- **Единое семейство иконок на деку** (design-research.md §3 «правило выбора») — совпадает с
  индустриальной практикой icon design systems (единый stroke weight, §2.E5).

### 6.2. Расширяется / уточняется этим исследованием

- **Контраст WCAG AA как «не строже, потому что не измерено на проекции»** (`contrast.py`
  докстринг) — это ОСОЗНАННО консервативное решение курса, и внешняя практика AV для больших
  затемнённых залов (контраст 21:1 между чёрным/белым, §3.6) ставит под вопрос, достаточен ли
  web-ориентированный порог 4,5:1/3,0:1 для задних рядов освещённой проектором аудитории. Это не
  довод за немедленное ужесточение (курс прав, что не хочет менять порог без замера), а довод за
  то, ЧТО именно измерить следующим шагом: реальный контраст на настоящем проекторе в
  аудиториях МГТУ.
- **Палитра Ocean никогда не проверялась на цветовую слепоту.** Ни design-research.md, ни
  `contrast.py`, ни `theme.py` не содержат ни одного упоминания CVD/дейтеранопии/Okabe-Ito. Учитывая
  статистику (до 8% мужчин с red-green CVD, §2.C4) и состав потока (техническая специальность,
  исторически выше доля мужчин), это реальный, не гипотетический риск, который НИКТО пока не
  замерял. Конкретная проверка: прогнать 4 цвета Ocean (DEEP/MID/LIGHT/TEAL + GOLD) через
  стандартную матрицу симуляции дейтеранопии/протанопии и сравнить попарные контрасты «после» —
  простая разовая проверка, которой в репозитории ещё нет.
- **8H-правило и DSHR 4-6-8** (AV-индустрия, §2.B8/B9) дают формулу «кегль как функция глубины
  аудитории», которой в `floor.py` нет — там жёсткий порог 12 пт, одинаковый для ЛЮБОЙ аудитории.
  Это не ошибка (единый порог проще поддерживать на 17 лекций без знания конкретной аудитории
  каждый раз), но граница применимости правила B8 честно называет: 12 пт — это НЕ расчёт под
  аудиторию МГТУ, это компромиссное число, принятое владельцем решением (`floor.py` докстринг:
  «решение владельца, а не значение по умолчанию»).
- **Разрешение растровых изображений не проверяется формально** (§4.1) — §5.7 требований курса
  («6-уровневая добыча настоящих изображений») отвечает за ПОДЛИННОСТЬ фото, но не за его
  пикселльную достаточность под проекцию. Пример: настоящая, неподделанная фотография в низком
  разрешении пройдёт существующую проверку и всё равно будет пикселизирована на экране.

### 6.3. Случай золота #F0AB00 (issue #240) — разбор

Контраст золота на белом измерен и подтверждён: **1,99:1**, что не проходит ни порог для обычного
текста (4,5:1), ни порог для крупного (3,0:1) — число ниже обоих с большим запасом, то есть
увеличение кегля НЕ спасает (в отличие от многих других случаев, где переход через границу 18пт
даёт послабление порога).

Три инженерных хода, не «убрать золото»:

1. **Опустить цвет текста** — заменить золото на `1C7293` (5,42:1) или `028090` (4,67:1) там, где
   нужен именно текст, а не акцентная заливка. Проходит оба порога. Цена: теряется золото как
   визуальный якорь внимания на этом конкретном элементе.
2. **Перевернуть плашку** — заливка `21295C`, число золотом: контраст 6,85:1, с большим запасом.
   Цена: добавляет иерархию заливкой, которая считывается РАНЬШЕ, чем прочитан текст (это уже
   учтено в докстринге `contrast.py` — выбор между 1 и 2 меняет кадр, не только контраст, и это
   явно отдано владельцу, не сборке).
3. **Третий ход, не описанный в `contrast.py`, но стандартный в литературе: контрастная обводка
   (halo) вокруг знаков** (§2.C17, картографическая и редакторская практика). Контурная линия
   контрастного цвета вокруг золотых букв физически не меняет измеренный WCAG-контраст
   фона/переднего плана (формула WCAG не считает обводку), но МЕНЯЕТ воспринимаемую читаемость —
   это известный ограничитель самого WCAG 2.x (не учитывает обводку, текстуру фона, насыщенность).
   Эта техника НЕ формализуется текущим сканером контраста и не заменяет пп. 1–2 как измеримое
   решение; она дополняет, а не решает P0 по метрике.

Итог: оба уже предложенных курсом хода (1 и 2) — ровно то, что рекомендует внешняя литература по
доступности цвета (поднять яркостный контраст через изменение цвета ЛИБО фона). Новое, что находит
это исследование — явный список альтернатив шире, чем «цвет или заливка», и прямое численное
подтверждение, что 1,99:1 не близко к порогу ни по одному из двух классов текста (не «чуть не
дотягивает», а системно ниже).

### 6.4. Чего не хватает (не покрыто ни текущими правилами, ни этим документом до конца)

- Нет замера настоящей освещённости/контраста в конкретных аудиториях МГТУ (ИУ6) — все пороги
  офисные/web, не измеренные на месте (§3.1, §6.2).
- Нет CVD-проверки палитры Ocean — впервые названа этим документом, не выполнена.
- Нет формального счётчика «знаков в строке» против диапазона Bringhurst/Butterick — только
  инструмент для bbox (`pdfmeasure.py`), без порогового вывода.
- Нет проверки разрешения встроенных изображений.
- Нет проверки «цвет из палитры» (off-palette hex).
- Длина строки для русского текста (66 знаков, Bringhurst) перенесена с латиницы без корректировки
  на среднюю ширину кириллического знака — [не проверено].
- APCA как более точный порог контраста не внедрён (сам стандарт пока draft — решение подождать
  финализации разумно, но стоит зафиксировать как открытый вопрос, а не забытый).

---

## §7. Источники

Все проверены WebSearch/WebFetch 2026-10-29, если не указано иное.

**Сетка и композиция**
- [Grid (graphic design) — Wikipedia](https://en.wikipedia.org/wiki/Grid_(graphic_design))
- [Grid Systems in Graphic Design — Josef Müller-Brockmann (Goodreads)](https://www.goodreads.com/book/show/60664913-grid-systems-in-graphic-design)
- [Baseline — Grid Systems](https://baselinehq.com/4-grid-systems.html)
- [Advanced PowerPoint grids and guides — BrightCarbon](https://www.brightcarbon.com/blog/advanced-powerpoint-grids-guides/)
- [The PPT Grid System — KeyNote Demo](https://keynote.org.cn/blog/grid-system-guide-2025-en/)
- [Embracing the Rule of Thirds in Presentation Design — Ethos3](https://ethos3.com/embracing-the-rule-of-thirds-in-your-presentation-design/)
- [What Is the Rule of Thirds in Presentation Design? — Extended Frames](https://extendedframes.com/what-is-the-rule-of-thirds-in-presentation-design/)
- [Safe area (television) — Wikipedia](https://en.wikipedia.org/wiki/Safe_area_(television))
- [How to Calculate Title-Safe and Action-Safe Margins for Video — DEV Community](https://dev.to/utilitylab/how-to-calculate-title-safe-and-action-safe-margins-for-video-1ifj)
- [How Using White Space Can Make Your Presentation More Effective — SlidesCarnival](https://www.slidescarnival.com/learn/5-tips-for-working-with-white-space-in-your-presentation-slides)
- [Use White Space for Professional Presentation Slides — A1Slides](https://a1slides.com/how-to-use-white-space-professional-slides/)

**Типографика**
- [Line length — Wikipedia](https://en.wikipedia.org/wiki/Line_length)
- [The Elements of Typographic Style — Wikipedia](https://en.wikipedia.org/wiki/The_Elements_of_Typographic_Style)
- [Point size — Practical Typography (Butterick)](https://practicaltypography.com/point-size.html)
- [Summary of key rules — Practical Typography](https://practicaltypography.com/summary-of-key-rules.html)
- [Modular Scale Typography — Craftwork](https://craftwork.design/skills/modular-scale-typography)
- [The 10-20-30 Rule for Presentations — AhaSlides](https://ahaslides.com/blog/10-20-30-rule-presentations/)
- [How big is big enough? The 8H Rule reveals all — Presentation Guild](https://presentationguild.org/how-big-big-enough-the-8h-rule-reveals-all/)
- [DLP: Determining the Minimum Display Size — Texas Instruments](https://www.ti.com/lit/pdf/dlpy006)
- [Golos Text — localfonts.eu](https://localfonts.eu/freefonts/traditional-cyrillic-free-fonts/golos/)
- [PT Fonts — Wikipedia](https://en.wikipedia.org/wiki/PT_Fonts)
- [Manrope Font Free — Font Squirrel](https://www.fontsquirrel.com/fonts/manrope)
- [Facts about figures: numeric styles with OpenType features — rwt.io](https://www.rwt.io/typography-tips/facts-about-figures-numeric-styles-with-opentype-features/)
- [Which fonts to use for your charts and tables — Datawrapper](https://www.datawrapper.de/blog/fonts-for-data-visualization)
- [Leading and Line Spacing Guide — Adobe](https://www.adobe.com/uk/creativecloud/design/discover/leading.html)

**Цвет и доступность**
- [Understanding WCAG SC 1.4.3 — digitala11y](https://www.digitala11y.com/understanding-sc-1-4-3-contrast-minimum/)
- [Success Criterion 1.4.3 — appt.org](https://appt.org/en/guidelines/wcag/success-criterion-1-4-3)
- [What Is the WCAG 4.5:1 Contrast Ratio — testparty.ai](https://testparty.ai/blog/wcag-contrast-ratio-guide-2025)
- [Why APCA as a New Contrast Method? — git.apcacontrast.com](https://git.apcacontrast.com/documentation/WhyAPCA.html)
- [What Is APCA? — ColorContrast](https://www.colorcontrast.org/blog/what-is-apca/)
- [GitHub — xi/apca-introduction](https://github.com/xi/apca-introduction)
- [Deuteranopia — color-blindness.com](https://www.color-blindness.com/deuteranopia-red-green-color-blindness/)
- [Color Blindness Prevalence — news-medical.net](https://www.news-medical.net/health/Color-Blindness-Prevalence.aspx)
- [Okabe-Ito Palette — figcanvas.com](https://figcanvas.com/blog/okabe-ito-palette-hex-rgb-wong-prism)
- [Colorblind-Friendly Palettes for Web Design — AudioEye](https://www.audioeye.com/post/colorblind-friendly-palettes/)
- [Colour Blind Friendly Colours in Design — wearearch.com](https://wearearch.com/blog/color-blind-friendly-colours)
- [OKLCH: Why Your CSS Color System Is Lying to You — DEV Community](https://dev.to/jeremy_longshore/oklch-why-your-css-color-system-is-lying-to-you-4j7a)
- [Perceptual Color Spaces: Lab, LCH, Oklab, OKLCH — ColorFYI](https://colorfyi.com/blog/perceptual-color-spaces/)
- [Recommended Background for Projected Presentations — Edward Tufte](https://www.edwardtufte.com/notebook/recommended-background-for-projected-presentations/)
- [Dark background: use in presentations — Slidor](https://www.slidor.agency/blog/dark-background)
- [Design Presentations That Work in Dark Rooms — SlideBazaar](https://slidebazaar.com/blog/design-presentations-that-for-dark-rooms-with-high-contrast-settings/)
- [The Function of Color in Data Viz — Towards Data Science](https://towardsdatascience.com/the-function-of-color-in-data-viz-a-simple-but-complete-guide-c324ca4c71d0/)
- [Data Viz Color Selection Guide — Atlassian](https://www.atlassian.com/data/charts/how-to-choose-colors-data-visualization)
- [Designing Accessible Text Over Images — Smashing Magazine](https://www.smashingmagazine.com/2023/08/designing-accessible-text-over-images-part1/)

**Графика данных**
- [Chapter 10 Tufte's Principles of Data-Ink — jtr13.github.io](https://jtr13.github.io/cc19/tuftes-principles-of-data-ink.html)
- [Tufte's Design Principles — Georgia Tech CS 7450](https://faculty.cc.gatech.edu/~stasko/7450/16/Notes/tufte.pdf)
- [The Visual Perception of Variation — Stephen Few / Perceptual Edge](https://www.perceptualedge.com/articles/visual_business_intelligence/the_visual_perception_of_variation.pdf)
- [The science behind data visualisation — Creative Bloq](https://www.creativebloq.com/design/science-behind-data-visualisation-8135496)
- [Graphical Perception — Cleveland & McGill 1984 (PKU, PDF)](https://math.pku.edu.cn/teachers/xirb/Courses/biostatistics/Biostatistics2016/GraphicalPerception_Jasa1984.pdf)
- [Cleveland-McGill Hierarchy — textbookofusability.com](https://www.textbookofusability.com/glossary/cleveland-mcgill-hierarchy.html)
- [Axes, scales, and honest baselines — analyticsmadesimple.com](https://analyticsmadesimple.com/analytics/axes-scales-honest-baselines/)
- [Alberto Cairo — charts can lie — Washington Post](https://www.washingtonpost.com/business/2019/10/14/youve-been-reading-charts-wrong-heres-how-pro-does-it/)
- [Donut Chart — Datylon](https://www.datylon.com/resources/chart-library/donut-chart)
- [5 alternatives to pie charts — Tableau](https://www.tableau.com/blog/5-unusual-alternatives-pie-charts)
- [Try to Avoid Color Legends — Data Revelations](https://www.datarevelations.com/avoid-color-legends/)
- [Accessibility Quick Wins: Remove Legends and Directly Label — Depict Data Studio](https://depictdatastudio.com/accessibility-quick-wins-remove-legends-and-directly-label/)
- [Line Chart Best Practices — usefuldatatips.com](https://usefuldatatips.com/tips/visualization/line-chart-best-practices)

**Изображения**
- [Best Resolution For PowerPoint Presentations — PresentationPoint](https://presentationpoint.com/best-powerpoint-screen-resolution/)
- [Best image resolution for PPT — Art of Presentations](https://artofpresentations.com/image-resolution-ultimate-resource/)
- [Creative Commons Attribution — wiki.creativecommons.org](https://wiki.creativecommons.org/wiki/Creative_Commons_Attribution)
- [About CC Licenses — Creative Commons](https://creativecommons.org/share-your-work/cclicenses/)

**Восприятие и вёрстка**
- [10 Gestalt Principles You Should Know — Maze](https://maze.co/blog/gestalt-principles/)
- [7 Gestalt Principles of Design — Netguru](https://www.netguru.com/blog/gestalt-principles-of-design)
- [Visual Hierarchy for Presentations — SlideModel](https://slidemodel.com/visual-hierarchy-for-presentations/)
- [The F-Pattern and Z-Pattern — succodesign](https://succodesign.it/blog/f-pattern-and-z-pattern-how-users-scan-pages)
- [The magical number seven, plus or minus two: Not relevant for design — Edward Tufte](https://www.edwardtufte.com/notebook/the-magical-number-seven-plus-or-minus-two-not-relevant-for-design/)
- [Miller's Law: Why the Magic Number 7 Is a Myth — Yukai Chou](https://yukaichou.com/behavioral-analysis/millers-magical-number-seven-plus-minus-two-working-memory/)
- [How to Create an Assertion-Evidence Presentation — Michael Alley (Penn State, PDF)](https://cpb-us-e1.wpmucdn.com/sites.psu.edu/dist/7/13153/files/2008/10/Assertion-Evidence-Slides-Instruction_Set.pdf)
- [How the Design of Presentation Slides Affects Audience Comprehension — Garner & Alley (PDF)](https://writing.engr.psu.edu/ae_comprehension.pdf)
- [Slide Structure Can Influence the Presenter's Understanding — Garner et al. 2016 (PDF)](http://writing.engr.psu.edu/Garner_et_al_2016.pdf)

**Автоматические проверки**
- [GitHub — jdmiller/pptx-accessibility-scanner](https://github.com/jdmiller/pptx-accessibility-scanner)
- [Make your PowerPoint presentations accessible — Microsoft Support](https://support.microsoft.com/en-us/office/make-your-powerpoint-presentations-accessible-to-people-with-disabilities-6f7772b2-2f33-4bd2-8ca7-dae3b2b3ef25)

**Внутренние источники курса (не внешние, использованы для «[курс]»-строк канона)**
- `tools/presentation-build/deckkit/contrast.py`
- `tools/presentation-build/deckkit/floor.py`
- `tools/presentation-build/deckkit/theme.py`
- `tools/presentation-build/deckkit/plotnost.py`
- `tools/presentation-build/deckkit/scheme.py`
- `tools/presentation-build/deckkit/twocol.py`
- `tools/presentation-build/nalozhenie_bbox.py`
- `tools/presentation-build/analitika.py`
- `tools/presentation-build/trebovaniya-k-soderzhaniyu-forma.md`
- `tools/presentation-build/proverki-i-pravila.md`
- `tools/presentation-build/README.md`
- `notes/issue-52-presentations-methodology/design-research.md`
- `notes/issue-52-presentations-methodology/design-superpowers.md`
- `notes/mcp-limitations.md` (#223-10, шрифт Arial→Liberation Sans)
