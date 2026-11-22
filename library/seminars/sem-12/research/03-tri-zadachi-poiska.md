# Исследование: три задачи поиска по картинкам (Кейс 3, Семинар 12)

Дата чтения всех источников — 2026-11-21. Каждый источник прочитан прямым `curl` (при PDF —
извлечение текста через `pymupdf`), не через пересказ поисковика, кроме случаев, явно
помеченных как «вторичный источник, не проверен прямым чтением».

---

## 1. Чем в практике решают каждую из трёх задач и почему их путают

Зал видит одну задачу — «поиск по картинке». В инженерной практике это три разных системы с
разной математикой внутри, и путаница в основном идёт от того, что все три отдают пользователю
одинаковый UI: рамку с картинкой и список результатов.

### 1.1. «Найди ровно эту же картинку» — точный повтор / пересжатие / пересъёмка

Решается **хэш-функцией изображения** (perceptual hash / robust hash) — детерминированной функцией без модели. Входная
картинка сводится к короткой битовой строке; совпадение проверяется расстоянием Хэмминга между
строками, без обращения к весам нейросети и без сетевого вызова.

Эталонный промышленный пример — **PhotoDNA** (Microsoft, в партнёрстве с Dartmouth College,
2009). Официальное описание с сайта `microsoft.com/en-us/photodna` (прочитано напрямую,
`curl -sL`, 2026-11-21):

> «PhotoDNA creates a unique digital signature (known as a "hash") of an image which is then
> compared against signatures (hashes) of other photos to find copies of the same image. When
> matched with a database containing hashes of previously identified illegal images, PhotoDNA is
> an incredible tool to help detect, disrupt and report the distribution of child exploitation
> material. PhotoDNA is not facial recognition software and cannot be used to identify a person
> or object in an image.»
> — [microsoft.com/en-us/photodna](https://www.microsoft.com/en-us/photodna), прочитано 2026-11-21

Технология донирована **NCMEC** (National Center for Missing & Exploited Children) и доступна
бесплатно технологическим компаниям и правоохранительным органам; официальная страница
подтверждает, что PhotoDNA «used by organizations around the world and has assisted in the
detection, disruption, and reporting of millions of child exploitation images». Конкретный список
крупных пользователей и численная оценка ложноположительных срабатываний — в независимом
PDF-кейсе ITU/ICMEC (прочитан напрямую, `curl`, 1 страница):

> «PhotoDNA enables the U.S. National Center for Missing & Exploited Children (NCMEC) and leading
> technology companies such as Facebook, Twitter, and Google, to match images through the use of
> a mathematical signature with a likelihood of false positive of 1 in 10 billion.»
> — [itu.int/.../ICMEC_PhotoDNA.PDF](https://www.itu.int/en/cop/case-studies/Documents/ICMEC_PhotoDNA.PDF), прочитан 2026-11-21

Второй, уже открытый эталон того же семейства — **PDQ** (Meta/Facebook, открыт в 2019). Прямое
чтение официального README в репозитории (`curl` на `raw.githubusercontent.com`, 2026-11-21):

> «PDQ stands for: **P**: A perceptual hasher… **D**: It is a spectral hashing algorithm, namely,
> it uses a Discrete Cosine Transform (DCT); **Q**: One of its outputs is a quality metric…
> Apocryphally, it is also short for "Pretty Darn Quick", as it was designed to be efficient to
> run at scale.»
> — [github.com/facebook/ThreatExchange, pdq/README.md](https://github.com/facebook/ThreatExchange/blob/main/pdq/README.md), прочитан 2026-11-21

Там же, в том же README, честно задокументировано ограничение хэша на поворот (разбирается
подробно в разделе 2).

### 1.2. «Найди похожую по смыслу» — семантическое сходство

Решается **мультимодальным эмбеддингом**: нейросеть переводит изображение в вектор
фиксированной размерности так, что смыслово близкие изображения оказываются рядом в векторном
пространстве; поиск — это приближённый поиск ближайших соседей (ANN) по этому векторному
пространству, в отличие от сравнения битовых строк хэша.

Pinterest описывает это прямо в своей инженерной публикации KDD'20 (прочитана напрямую,
`curl` на `arxiv.org/pdf/1908.01707`, PDF, извлечение через pymupdf):

> «Over 250M users come to Pinterest monthly to discover ideas… from our content corpus of
> billions of Pins… we've built a variety of visual search products… including Flashlight
> (2016), Lens (2017)…»
> — Zhai et al., *Learning a Unified Embedding for Visual Search at Pinterest*, KDD 2019,
> [arxiv.org/pdf/1908.01707](https://arxiv.org/pdf/1908.01707), прочитан 2026-11-21

Google формулирует задачу так же явно в собственном исследовательском блоге (прочитан напрямую,
`curl`, 2026-11-21):

> «We ask participants to build a single universal image embedding model capable of representing
> objects from multiple domains at the instance level. We believe that this is the key for
> real-world visual search applications…»
> — [blog.research.google, Introducing the Google Universal Image Embedding Challenge](https://blog.research.google/2022/08/introducing-google-universal-image.html), 2022, прочитан 2026-11-21

Amazon собрал тот же паттерн в официальной эталонной архитектуре **AWS Guidance for Visual
Search** (страница прочитана напрямую, `curl`, 2026-11-21): модель **Amazon Titan Multimodal
Embedding G1** на Bedrock превращает изображение (и, опционально, его описание) в вектор, вектор
кладётся в индекс k-NN (OpenSearch/DocumentDB/Aurora), поиск — k-NN запрос к этому индексу. В том
же документе AWS явно комбинирует метод 2 с методом 1: шаг 7 эталонной архитектуры генерирует
подпись изображения моделью Claude 3.5 Sonnet и добавляет её текст в запрос эмбеддинга «for
better search results» — то есть в современной продакшен-практике подпись словами и эмбеддинг усиливают друг друга внутри одного пайплайна.

### 1.3. «Найди ту, где есть вот это» — поиск по признаку/детали внутри картинки

Это третья, отдельная задача: внутри картинки есть конкретный объект/деталь, и вопрос именно
о нём, а не о сходстве всей картинки целиком. Решается **детекцией объектов + эмбеддингом на
уровне найденного региона**, а не эмбеддингом всей картинки.

Pinterest описывает ровно эту систему в продакшен-отчёте KDD'20 «Shop The Look» (PDF прочитан
напрямую, `curl` + pymupdf):

> «Shop The Look is an online shopping discovery service at Pinterest, leveraging visual search
> to enable users to find and buy products within an image… Detected objects in a scene are
> displayed as dots… Tapping on a dot expands it into a bounding box…»
> — Shiau et al., *Shop The Look: Building a Large Scale Visual Shopping System at Pinterest*,
> KDD 2020, [arxiv.org/pdf/2006.10866](https://arxiv.org/pdf/2006.10866), прочитан 2026-11-21

Числа оттуда же (деплой в продакшен, не лабораторный прототип): «cumulative relative gains of
over 160% in end-to-end human relevance judgements and over 80% in engagement» после перехода от
поиска по целой картинке к поиску по обнаруженным внутри неё объектам.

Krawetz (раздел 2) в своём первоисточнике 2011 года уже называет этот же паттерн применительно к
хэшам: «if you have a face detection algorithm, then you can compute hashes for each face» —
то есть идея «сначала выдели деталь, потом сравнивай» не специфична для эмбеддингов, она
встречается и в хэш-подходе, просто хуже там работает на произвольных объектах (хэш не умеет
«понимать», что является объектом, его нужно сначала вырезать внешним детектором).

### Почему зал путает три задачи

Все три выдают одинаковый интерфейс («загрузи картинку → получи список похожих»), но решают
разные вопросы: хэш отвечает «это тот же файл после технических искажений?», эмбеддинг — «это
тот же смысл?», детектор+эмбеддинг региона — «есть ли внутри этот конкретный объект?». Подмена
одной задачи другой — системная инженерная ошибка: PhotoDNA прямо в официальном описании
оговаривает, что не умеет отвечать на вопрос 1.3 («is not facial recognition software and cannot
be used to identify a person or object in an image»), а большинство продакшен-систем (AWS
Guidance, Pinterest) в 2026 году уже смешивают методы 1.1–1.3 внутри одного пайплайна, что и
создаёт у пользователя иллюзию единой задачи.

---

## 2. Устройство перцептивного хэша по первоисточнику

Прочитаны оба кандидата напрямую.

- **Neal Krawetz, «Looks Like It», The Hacker Factor Blog, 26 мая 2011.** Прочитан напрямую
  (`curl` с браузерным User-Agent на `hackerfactor.com`, зеркало без HTTPS — прямой HTTPS-адрес
  вернул 403; зеркало отдало 200, текст статьи и комментарии извлечены полностью). URL:
  [hackerfactor.com/blog/?/archives/432-Looks-Like-It.html](http://www.hackerfactor.com/blog/?/archives/432-Looks-Like-It.html),
  прочитан 2026-11-21.
- **Christoph Zauner, «Implementation and Benchmarking of Perceptual Image Hash Functions»**,
  диссертация (Diplomarbeit), Fachhochschule Oberösterreich, Hagenberg, июль 2010, 90+ страниц.
  Прочитана напрямую (`curl` на `phash.org/docs/pubs/thesis_zauner.pdf`, текст извлечён через
  `pymupdf`, 30 216 слов). URL: [phash.org/docs/pubs/thesis_zauner.pdf](https://www.phash.org/docs/pubs/thesis_zauner.pdf),
  прочитан 2026-11-21.

### 2.1. Устройство (дословно по Krawetz, с формализацией по Zauner)

Самый простой вариант — **Average Hash (aHash)**, по Krawetz:

> «Reduce size. … shrink it to 8x8 so that there are 64 total pixels… Reduce color. The tiny 8x8
> picture is converted to a grayscale… Average the colors. Compute the mean value of the 64
> colors. Compute the bits. … Each bit is simply set based on whether the color value is above or
> below the mean. Construct the hash. Set the 64 bits into a 64-bit integer.»

Более устойчивый вариант — **pHash** (DCT-based hash), по Krawetz:

> «Reduce size. … 32x32 is a good size… Compute the DCT. … While JPEG uses an 8x8 DCT, this
> algorithm uses a 32x32 DCT. Reduce the DCT. … just keep the top-left 8x8. Those represent the
> lowest frequencies in the picture. Compute the average value. … Further reduce the DCT. … Set
> the 64 hash bits to 0 or 1 depending on whether each of the 64 DCT values is above or below the
> average value… Construct the hash.»

Сравнение хэшей — расстояние Хэмминга (число позиций бит, в которых два хэша различаются), тоже
по Krawetz: «construct the hash from each image and count the number of bit positions that are
different… A distance of zero indicates that it is likely a very similar picture… a distance of
10 or more? That's probably a very different picture.»

Zauner формализует тот же DCT-шаг строго математически (Определение 3.1–3.2, тип-II DCT):

> «Let x[m], m = 0, …, N − 1, denote an N-point real signal sequence. Then … X[n] =
> √(2/N) · Σ x[m]·cos[(2m+1)·nπ/2N], (n = 0, …, N − 1).» и далее: «Low-frequency DCT coefficients
> of an image are mostly stable under image manipulations… This property is also utilized by the
> JPEG image compression standard… The result is an 8x8 transform coefficient array in which the
> elements close to the top-left (index position (0, 0)) represent low-frequency components and
> are therefore deemed to be perceptually most significant.»

### 2.2. Почему поворот ломает хэш, а пересжатие — нет (инженерное объяснение + измерение)

**Инженерная причина.** Хэш — это не описание «смысла» изображения, а фиксированный набор битов,
привязанный к конкретным осям и позициям: позиция каждого пиксельного блока в усреднённой
решётке (aHash) или позиция конкретного коэффициента в матрице DCT (pHash) жёстко завязана на
то, где на изображении «верх», «низ», «лево», «право». Пересжатие JPEG меняет **высокочастотные**
детали — ровно то, что average/DCT-хэш сознательно отбрасывает на шаге «Reduce the DCT» (см.
Zauner выше: «low-frequency DCT coefficients… mostly stable under image manipulations»).
Поворот, напротив, меняет **все** пространственные координаты сразу — верх становится боком,
горизонтальные линии становятся диагональными, — то есть меняет именно ту низкочастотную
структуру, на которой построен весь хэш. Поэтому у хэша нет «запаса прочности» против поворота:
это не два разных по силе искажения одного типа, а искажение, которое задевает ось хэша
напрямую, против искажения, которое её не задевает вовсе.

**Измерение по первоисточнику (Zauner, глава 6, «Benchmark Results», разделы 6.3.3 и 6.3.4).**
Таблицы приведены как в первоисточнике, среднее расстояние (mean distance, 0 = идентичны,
0.5 = случайное совпадение):

| Искажение | DCT-хэш | Marr-Hildreth | Radial variance | Block mean |
|---|---|---|---|---|
| JPEG, quality=80 (табл. 6.8) | **0.001** | 0.045 | 0.000 | 0.001 |
| Поворот на 5° (табл. 6.9) | **0.335** | 0.486 | 0.358 | 0.220 |

Вывод в тексте диссертации: «Using this kind of image operation [rotation by 5°] none of the
tested image hash functions is robust… Even when rotating by only 1°, the average distance score
is approximately 0.30» (про Marr-Hildreth). Для JPEG — обратный вывод: «The radial variance based
image hash function is almost not influenced at all by the quality parameter. Even when using a
quality parameter of 0 the average distance score of this hash function is negligible.»

**Независимое подтверждение от продакшен-системы.** README алгоритма **PDQ** (Meta,
`pdq/README.md`, прочитан напрямую) честно документирует тот же дефект уже на действующей в
продакшене системе 2019–2026 годов, даже после специальной «дигедральной» хитрости (вычислить
хэш для всех 8 поворотов/отражений сразу):

> «PDQ does not guarantee exact rotational invariance. Small variations can occur in the hash
> values for each rotation due to how PDQ processes the image's grid alignment in its DCT
> (Discrete Cosine Transform) phase… two rotated versions of an image can have a slightly
> different set of eight dihedral hashes.»

То есть ограничение «поворот ломает DCT-хэш» — не артефакт одной старой академической
реализации 2010 года, оно подтверждено независимо production-кодом Meta пятнадцатью годами
позже, с той же технической причиной (сетка DCT жёстко привязана к осям изображения).

---

## 3. Где в индустрии дедуплицируют хэшем, а где — эмбеддингом

### 3.1. Хэш

- **PhotoDNA** (Microsoft/NCMEC) — см. раздел 1.1. Используется Facebook, Twitter (на момент
  публикации источника), Google и «leading technology companies» по всему миру; заявленная
  вероятность ложного срабатывания — 1 на 10 миллиардов (источник ITU/ICMEC, раздел 1.1).
- **PDQ** (Meta, открыт в 2019) — тот же класс задачи (поиск известных вредоносных изображений
  на масштабе), но открытый код вместо закрытого протокола. README прямо называет происхождение
  из индустриальной задачи «T&S» (Trust & Safety): «This is a collection of reference
  implementation for the PDQ image hashing algorithm… designed to be efficient to run at scale.»
  Throughput совпадения хэшей через связку с индексом FAISS прямо указан авторами: «The faiss
  matching implementation has been proven up to 4000 images/sec.»

### 3.2. Эмбеддинг

- **Pinterest Visual Search** (Flashlight 2016, Lens 2017, Shop The Look 2020) — KDD-публикации
  компании, прочитаны напрямую (раздел 1.2–1.3). Масштаб из первого источника: «250M users…
  billions of Pins».
- **Google Lens / Google Images «search by image»** — Google Research формулирует задачу через
  единую эмбеддинг-модель в блоге Universal Image Embedding Challenge (раздел 1.2, прочитан
  напрямую). Патентная заявка US11782998B2 «Embedding Based Retrieval for Image Search»
  (обнаружена через поиск, не прочитана первоисточником полностью — см. раздел 6) описывает
  архитектуру с отдельными эмбеддинг-сетями для изображения и текста.
- **Amazon визуальный поиск** — официальная эталонная архитектура AWS Guidance for Visual Search
  (раздел 1.2, прочитана напрямую): Amazon Titan Multimodal Embedding G1 на Bedrock + k-NN индекс
  в OpenSearch/DocumentDB/Aurora. Отдельно у Amazon есть исследовательская публикация про
  мультимодальную (текст+картинка) версию той же системы — найдена через поиск
  (`arxiv.org/html/2412.13364v1`, «Bringing Multimodality to Amazon Visual Search System»), но
  не вычитана первоисточником построчно внутри этой сессии — помечается как не до конца
  верифицированная.

---

## 4. Цена и задержка каждого метода

Здесь честно разделяются числа, подтверждённые первоисточником, и числа, взятые из агрегаторов
(отмечены явно как не первичные — по канону курса §8.7 цифра без первоисточника хуже честного
пробела).

**Хэш — вычисление и сравнение.**
- Исследовательская (неоптимизированная) реализация Zauner, 2010, один поток, CPU Intel Core 2
  Duo T9300 2.50GHz (железо указано в самой диссертации, табл. 6.1): DCT-хэш — **9.7 сек/картинку**
  на хэширование, Block-mean-value-хэш — **0.6 сек/картинку**. Это числа конкретной академической
  реализации 15-летней давности на слабом железе, не ориентир для продакшена — приводятся как честная точка отсчёта из конкретного эксперимента, без претензии на
  «типичную скорость хэширования» в современных системах.
  — Zauner, табл. 6.3, прочитано напрямую.
- Production-измерение у Meta касается поиска совпадения по уже вычисленным хэшам в индексе: «The faiss
  matching implementation has been proven up to 4000 images/sec» — доли миллисекунды на
  сравнение одного хэша при поиске по индексу. — PDQ README, прочитано напрямую, раздел 3.1.
  Порядок величины для самого вычисления бит хэша (без сети, без обращения к GPU) в современных
  SIMD-реализациях — **микросекунды–единицы миллисекунд на изображение**; точного числа у
  первоисточника (README PDQ) для этого конкретного шага нет, это честный порядок величины, не
  измеренное число.

**Эмбеддинг через модель.**
- Задержка вызова эмбеддинг-модели по сети — порядок величины **десятки–сотни миллисекунд за
  вызов**, цена — доли цента за вызов на уровне токенов. Это оценка **вторичных источников**
  (агрегаторы ценообразования API, не официальная документация провайдера) — конкретные цифры
  (например, «100–300 мс», «$0.02 за 1М токенов») **не проверены прямым чтением первоисточника**
  в рамках этой сессии и приводятся только как порядок величины, не как точный факт.
- Локальный инференс CLIP-подобной модели на GPU, по той же непервичной категории источников —
  порядок величины **единицы миллисекунд на изображение при батчинге**; тоже не проверено
  первоисточником.
- Pinterest прямо называет инженерную причину, почему этот порядок величины имеет значение на
  масштабе: эмбеддинги приходится **бинаризовать** (сжимать до битовой формы) именно из-за
  затрат на хранение и задержку: «we need efficient representations to (1) decrease cold storage
  costs… (2) reduce bandwidth… (3) improve the latency of real-time scoring». — Zhai et al.,
  прочитано напрямую, раздел 1.2.

**Векторный индекс (ANN) на масштабе миллионов/миллиардов.**
- Прямое чтение wiki репозитория **FAISS** (Meta, `facebookresearch/faiss`, страница
  «Indexing 1G vectors», прочитана напрямую через `raw.githubusercontent.com`, 2026-11-21):
  при индексации ~1 млрд векторов и параметрах `nprobe=128, quantizer_efSearch=32` — recall@1 =
  0.6786, **время поиска 0.05387 мс на запрос**; при `nprobe=64` — recall@1 = 0.6421, время
  0.03028 мс на запрос. Это измеренные числа конкретного железа (GPU-ускоренный индекс,
  батч-запросы), не универсальная константа — ANN торгует точностью (recall ~0.64–0.68, то есть
  система пропускает 30%+ истинных совпадений в топ-1) за эту скорость, это и есть
  приблизительность approximate nearest neighbor. — [github.com/facebookresearch/faiss/wiki/Indexing-1G-vectors](https://github.com/facebookresearch/faiss/wiki/Indexing-1G-vectors),
  прочитано 2026-11-21.

**Сводный порядок величины (честно, с указанием, что проверено первоисточником, а что нет):**

| Метод | Шаг | Порядок величины | Проверено первоисточником? |
|---|---|---|---|
| Хэш | сравнение по индексу (production, PDQ+FAISS) | до 4000 изображений/сек | да (README PDQ) |
| Хэш | вычисление бит (академическая реализация 2010) | 0.6–9.7 сек/изображение на слабом CPU одним потоком | да (Zauner, табл. 6.3) — НЕ показатель современного продакшена |
| Эмбеддинг | вызов модели по сети | десятки–сотни мс | нет, оценка агрегаторов |
| ANN-индекс | поиск по 1 млрд векторов (GPU) | ~0.03–0.05 мс/запрос при recall ~0.64–0.68 | да (FAISS wiki) |

---

## 5. Документированный случай с ценой для человека

**Решение оркестратора (2026-11-21, коммит `4e6e7f45`):** первоначально найденный здесь случай
Google Photos/«Марк» (ложное срабатывание классификатора признака, пожизненная блокировка
аккаунта) **передан Кейсу 1** — тот кейс уже стоит на материале Google (отключённая группа
ярлыков в Google Photos), и два кейса одного занятия на имени одной компании читались бы как
повтор, а не как два независимых свидетельства. Случай описан и процитирован полностью в
`research/01-*.md` (зона Кейса 1), здесь не повторяется.

### Основной случай Кейса 3: Apple NeuralHash (2021) — коллизии хэша найдены до запуска,
### функция отложена — провал устройства, а не реализации

Это документированный провал именно **механизма** перцептивного хэша — ровно устройства,
разобранного в разделе 2 этого файла, сломанного на его собственной логике: две разные картинки
были сведены к одному хэшу не из-за ошибки кода, а потому что короткая битовая подпись
математически обязана иметь коллизии (у 64–96-битного хэша пространство выходов сильно меньше
пространства входных изображений). Цена — именная и датированная: выпуск функции сличения
отложен, затем отменён, до того как она успела обработать хотя бы одну настоящую фотографию
пользователя — то есть цена наступила РАНЬШЕ потенциального вреда конкретному человеку, что и
отличает этот случай от кейсов, где цена приходит после ошибки на живых данных.

Технический первоисточник — рецензируемая публикация MIT (workshop ICML 2022), прочитана
напрямую (`curl` на `arxiv.org/pdf/2207.14258`, PDF, извлечение через pymupdf):

> «In 2021, Apple unveiled NEURALHASH, an algorithm aimed at detecting Child Sexual Abuse
> Material (CSAM) in images that are uploaded to iCloud… We make the surprising discovery that
> NEURALHASH is approximately linear, which inspires the development of novel black-box attacks
> that can (i) evade detection of "illegal" images, (ii) generate near-collisions, and
> (iii) leak information about hashed images, all without access to model parameters.»
> — Bhatia & Meng, *Exploiting and Defending Against the Approximate Linearity of Apple's
> NeuralHash*, ICML 2022 ML4Cyber Workshop, [arxiv.org/pdf/2207.14258](https://arxiv.org/pdf/2207.14258),
> прочитано 2026-11-21.

Хронология цены во времени, подтверждённая прямым чтением новостной статьи с датой публикации
(не пересказом):

> «In a statement on Friday morning, Apple told TechCrunch: … we have decided to take additional
> time over the coming months to collect input and make improvements before releasing these
> critically important child safety features… Within a few weeks of announcing the technology,
> researchers said they were able to create "hash collisions" using NeuralHash, effectively
> tricking the system into thinking two entirely different images were the same.»
> — TechCrunch, *Apple delays plans to roll out CSAM detection in iOS 15 after privacy backlash*,
> опубликовано 2021-09-03, [techcrunch.com/2021/09/03/apple-csam-detection-delayed/](https://techcrunch.com/2021/09/03/apple-csam-detection-delayed/),
> прочитано напрямую 2026-11-21.

Функция была окончательно отменена в декабре 2022 года (по данным вторичных источников,
собранных поисковиком; дата отмены не вычитана первоисточником напрямую в рамках этой сессии —
честно помечается как не до конца верифицированная).

**Почему этого случая достаточно для раздела 2.** Бриф разрешает закрыть пункт случаем, цена
которого названа и подтверждена первоисточником — здесь это так: исследователи нашли коллизии
NeuralHash в течение нескольких недель после анонса (TechCrunch, дата публикации 2021-09-03),
Apple публично отложила запуск в том же заявлении. Второй найденный случай с ценой для
конкретного человека (Google Photos/«Марк», NYT 2022) ушёл в материал Кейса 1 по решению
оркестратора — выдумывать третий, отдельный от уже найденных, не требуется (канон §4.3:
выдуманный пример хуже честного использования уже подтверждённого).

---

## 6. Чего найти не удалось

- **Точная задержка вызова облачной эмбеддинг-модели (OpenAI/аналоги) и её официальная
  документация с цифрой SLA.** Найдены только вторичные агрегаторы цен и задержек
  (`deploybase.ai`, `theneuralbase.com`), не первоисточник (официальная документация провайдера
  не публикует фиксированную цифру задержки как контракт). Раздел 4 явно помечает эти числа как
  непроверенные первоисточником — порядок величины, не факт.
- **Архитектурные детали патента Google «Embedding Based Retrieval for Image Search»
  (US11782998B2).** Патентный документ найден через поиск (USPTO image-ppubs PDF), но не прочитан
  построчно первоисточником в рамках этой сессии — использован только пересказ поисковика; это
  честно отражено в разделе 3.2.
- **Дата официальной отмены Apple CSAM/NeuralHash (декабрь 2022).** Встречается в нескольких
  вторичных источниках поисковика (не проверено прямым `curl` на официальное заявление Apple
  о полной отмене программы в рамках этой сессии) — приводится в разделе 5 с явной пометкой
  «не до конца верифицировано».
- **PhotoDNA Fact Sheet (архивный .doc от Microsoft, декабрь 2009).** Файл скачан напрямую
  (`curl`, HTTP 200, корректный .doc формат подтверждён `file`), но текстовое содержимое не
  извлеклось доступными в системе инструментами (`strings` вернул только таблицу стилей Word, не
  основной текст; `antiword`/`catdoc`/`libreoffice` не установлены в системе). Данные из этого
  документа **не использованы** — вместо него в разделе 1.1 и 3.1 использована актуальная страница
  `microsoft.com/en-us/photodna` и отдельный PDF-кейс ITU/ICMEC, оба прочитаны напрямую и
  содержательно перекрывают фактшит.
- **Документированный денежный кейс «маркетплейс склеил два разных товара по картинке и это
  стоило продавцу денег».** Целенаправленный поиск такого случая с указанием конкретной суммы и
  источника в рамках этой сессии не проводился — честно оставляется как неисследованное
  направление, а не заменяется выдумкой: бриф разрешает закрыть раздел 5 случаем NeuralHash,
  найденным и подтверждённым первоисточником.
- **Текст статьи The New York Times напрямую (первоисточник случая Google Photos/«Марк», ушёл в
  материал Кейса 1).** Прямой `curl` (с браузерным User-Agent, не через WebFetch) на
  `nytimes.com` вернул HTTP 403 — платный доступ. Это не было принято на веру по одному
  отрицательному ответу: проверены дополнительно AP (403), Gizmodo (403) и, наконец, зеркало
  Information Age / ACS (200, полный текст с прямыми цитатами из оригинала NYT) — использовано
  оно, с явным указанием, что это пересказ с цитатами,
  а не сам текст NYT.
