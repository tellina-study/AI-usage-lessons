# Атрибуция веб-изображений — Лекция 2 v3.3 (issue #183, round 5)

Непубличная презентация (внутренний курс МГТУ). Требование по правам —
только эта таблица с указанием источника; на слайдах подписи-источники
убраны deck-wide (v3.2, owner-мандат) — включая скриншоты и мемы.

Все файлы скачаны через `curl`/WebFetch/WebSearch 2026-09-06.

## v3.2 update (round 4) — owner: «вижу только 1 мем (пират) и 1 хорошую
## иллюстрацию (кости) — замени все остальные и докинь»

Новые файлы (см. таблицу ниже для деталей): `surprised-pikachu-tokenize.jpg`,
`expanding-brain-strawberry.jpg`, `magikarp-clean.png`, `pam-same-picture.jpg`,
`spotlight-clean.jpg`, `gorshochek-1984-crop.jpg`, `pepe-silvia.jpg`.

Заменены/убраны: `strawberry-openai-crop.jpg` (s05a, s08 — заменены),
`solidgoldmagikarp-1.png` (s10 — убран, заменён на Magikarp-артворк),
`word2vec-king-analogy-arrows.png` (s12a — заменён на Pam-мем),
`illustrations/s14-space.png` (s14 — убран совсем, дублировал scatter),
`attention-paper-title.png` (s18a — заменён на spotlight),
`web/gorshochek-ubbelohde-1909.jpg` (s31 — заменён на кадр мультфильма),
`this-is-fine-meme-fb.jpg` (s35a — заменён на Pepe Silvia).

Оставлены без изменений (owner-одобрено v3.1, убрана только видимая
подпись-источник под картинкой — атрибуция теперь только здесь):
`dice-wikimedia.jpg` (s26a), `matryoshka-wikimedia.jpg` (s33a),
`well-yes-actually-no-template.jpg` (s01, s28).

### v3.2-active (текущие файлы, используемые в рендере)

| Локальный файл | Слайд | Описание | URL источника | Дата скачивания | Лицензия / статус |
|---|---|---|---|---|---|
| `well-yes-actually-no-template.jpg` | s01, s28 | Мем-шаблон «Well yes, but actually no» (пират из Aardman/Sony «Pirates! Band of Misfits»), пустой верх для своего текста | https://imgflip.com/memetemplate/171918715/Well-yes-but-actually-no (image src: `https://i.imgflip.com/2uctbv.jpg`) | 2026-09-06 | Imgflip meme template — fair use, образовательный некоммерческий контекст |
| `surprised-pikachu-tokenize.jpg` (из `surprised-pikachu-template.jpg`) | s05a (divider) | Мем-шаблон Surprised Pikachu (аниме-кадр, официальный кадр Pokémon anime) — свой текст поверх шаблона: «модель уверенно отвечает неправильно — она видит куски, не буквы» | https://imgflip.com/memetemplate/159392707/Surprised-Pikachu-High-Quality (image src: `https://i.imgflip.com/2mwc77.jpg`) | 2026-09-06 | Imgflip meme template — fair use, образовательный некоммерческий контекст |
| `expanding-brain-strawberry.jpg` (из `expanding-brain-template.jpg`) | s08 (content) | Мем-шаблон Expanding Brain (4 панели) — свой текст поверх шаблона: гонка патчей GPT-5.2→5.5→5.6→StrawberryBench | https://imgflip.com/memetemplate/153941834/Expanding-brain-4-panels (image src: `https://i.imgflip.com/2jnia2.jpg`) | 2026-09-06 | Imgflip meme template — fair use, образовательный некоммерческий контекст |
| `magikarp-clean.png` (из `magikarp-official.png`) | s10 (content) | Официальный артворк покемона Magikarp (Ken Sugimori, Pokémon Red/Blue) — прямая отсылка к имени glitch-токена «SolidGoldMagikarp» | pngkey.com (зеркало официального артворка Nintendo/Game Freak/Ken Sugimori) | 2026-09-06 | Fan-hosted mirror официального артворка — образовательное некоммерческое использование |
| `pam-same-picture.jpg` (из `pam-same-picture-template.jpg`) | s12a (divider) | Мем-шаблон «They're the same picture» — Pam (Jenna Fischer), сериал «The Office», эпизод «Search Committee» (2011) | https://knowyourmeme.com/memes/theyre-the-same-picture (image: `https://i.kym-cdn.com/entries/icons/mobile/000/027/752/6lwrp2xhplg41.jpg`) | 2026-09-06 | Культовый интернет-мем, образовательное некоммерческое использование |
| `spotlight-clean.jpg` (из `spotlight-template.jpg`) | s18a (divider) | Стоковое фото/иллюстрация театрального прожектора: 3 луча света на подиум в тёмной комнате — буквальная метафора attention («луч высвечивает одно, вокруг темнота») | https://imgflip.com/memetemplate/445572892/Spotlight (image src: `https://i.imgflip.com/7da68s.jpg`) | 2026-09-06 | Imgflip template — fair use, образовательный некоммерческий контекст |
| `gorshochek-1984-crop.jpg` (crop of `gorshochek-yt1-max.jpg`) | s31 (content) | Кадр из мультфильма «Горшочек каши» (Союзмультфильм, 1984, реж. Наталия Голованова) — девочка держит горшочек, момент «горшочек, не вари!» | YouTube-видео мультфильма (thumbnail через `img.youtube.com/vi/o6m9Ae5zTCI/maxresdefault.jpg`) | 2026-09-06 | Советский мультфильм — образовательное использование, культурно-узнаваемая отсылка для русскоязычной аудитории |
| `pepe-silvia.jpg` (из `pepe-silvia-template.jpg`) | s35a (divider) | Мем-шаблон Pepe Silvia / conspiracy board — Charlie Day (Charlie Kelly), сериал «It's Always Sunny in Philadelphia», эпизод «Sweet Dee Has a Heart Attack» (S4E10) | https://imgflip.com/memetemplate/74331809/Pepe-Silvia (image src: `https://i.imgflip.com/1896sh.jpg`) | 2026-09-06 | Культовый интернет-мем, образовательное некоммерческое использование |
| `dice-wikimedia.jpg` | s26a (divider) | Фото пары казино-костей (Caesars Palace, музейный экспонат) — owner-одобрено v3.1, оставлено без изменений в v3.2 (убрана только видимая подпись) | https://commons.wikimedia.org/wiki/File:Wuerfel_72.JPG | 2026-09-06 | Wikimedia Commons, CC-BY-SA (стандартная лицензия загрузки) |
| `matryoshka-wikimedia.jpg` | s33a (divider) | Фото набора русских матрёшек (5 штук, убывающего размера) — owner-одобрено v3.1, оставлено без изменений в v3.2 (убрана только видимая подпись) | https://commons.wikimedia.org/wiki/File:Russian-Matroshka.jpg | 2026-09-06 | Wikimedia Commons, CC-BY-SA 3.0 / GFDL (автор: Fanghong) |

### v3.1-historical (заменены в v3.2, файлы оставлены на диске для traceability, в рендере больше НЕ используются)

| Локальный файл | Слайд (было) | Описание | URL источника | Дата скачивания | Лицензия / статус |
|---|---|---|---|---|---|
| `strawberry-openai-crop.jpg` (crop of `strawberry-openai-forum-1.jpeg`) | s05a (divider) | Реальный скриншот ChatGPT: «There are two 'r' characters in the word 'strawberry'» — виральный баг подсчёта букв | https://community.openai.com/t/incorrect-count-of-r-characters-in-the-word-strawberry/829618 (image: `https://us1.discourse-cdn.com/openai1/original/4X/1/b/7/1b7aeccadf53d14b6b3e85f579c61bd5fd6419ba.jpeg`) | 2026-09-06 | OpenAI Community forum screenshot — образовательное использование |
| `strawberry-openai-forum-1.jpeg` (uncropped) | s08 (content) | То же — полный скриншот переписки с продолжением («Check again please» → «Are you 100% sure?» → «Would you bet a million dollars») | там же | 2026-09-06 | То же |
| `word2vec-king-analogy-arrows.png` | s12a (divider) | «king − man + woman ≈ queen» — word2vec embedding heatmap с явным заголовком-формулой (Jay Alammar, «The Illustrated Word2vec») | https://jalammar.github.io/illustrated-word2vec/ (image: `https://jalammar.github.io/images/word2vec/king-analogy-viz.png`) | 2026-09-06 | Образовательный блог, широко цитируемая иллюстрация — fair use |
| `attention-paper-title.png` | s18a (divider) | Титульная страница статьи «Attention Is All You Need» (Vaswani et al., 2017) — рендер официального PDF с arXiv | https://arxiv.org/pdf/1706.03762 (arXiv:1706.03762v7) | 2026-09-06 | arXiv — открытый доступ; в самой статье указано: «Google hereby grants permission to reproduce the tables and figures in this paper solely for use in journalistic or scholarly works» |
| `this-is-fine-meme-fb.jpg` | s35a (divider) | «This is fine» — культовый кадр из веб-комикса Gunshow #648 (K.C. Green, 2013), пёс за столом в горящей комнате | https://knowyourmeme.com/memes/this-is-fine (image: `https://i.kym-cdn.com/entries/icons/facebook/000/018/012/this_is_fine.jpg`) | 2026-09-06 | Культовый интернет-мем, некоммерческое образовательное использование |
| `solidgoldmagikarp-1.png` | s10 (content) | Реальный скриншот GPT Playground: модель не может повторить glitch-токен «petertodd», отвечает не в тему («unspeakable one») — тот же корпус исследований LessWrong, что открыл SolidGoldMagikarp | https://www.lesswrong.com/posts/8viQEp8KBg2QSW4Yc/solidgoldmagikarp-iii-glitch-token-archaeology (image: `https://res.cloudinary.com/lesswrong-2-0/image/upload/v1676351877/mirroredImages/8viQEp8KBg2QSW4Yc/xgcwkc4ykkoj01bc4v8e.png`) | 2026-09-06 | LessWrong — открытый доступ, образовательное использование |
| `gorshochek-ubbelohde-1909.jpg` | s31 (content) | Иллюстрация Отто Уббелоде (1909) к сказке братьев Гримм «Сладкая каша» / «Горшочек каши» — гора каши поглощает деревню (метафора бесконечного цикла без стоп-условия) | https://en.wikipedia.org/wiki/Sweet_Porridge (image: `https://upload.wikimedia.org/wikipedia/commons/9/96/Otto_Ubbelohde_-_Der_süße_Brei.jpg`) | 2026-09-06 | Общественное достояние (автор умер в 1922, работа 1909 года) |
| `logos/openai.png`, `logos/anthropic.png`, `logos/google.png`, `logos/deepseek.png`, `logos/xai.png`, `logos/qwen.png` | s36 | Логотипы AI-компаний (передний край + открытые веса), рендер SVG из LobeHub icon-set, recolor в Ocean palette `#21295C` | https://cdn.jsdelivr.net/npm/@lobehub/icons-static-svg@latest/icons/{name}.svg | 2026-09-06 | LobeHub icons-static-svg — открытый npm-пакет для брендинга AI-сервисов |

## Попытки, не давшие результата (FAILED)

- **s37 (бенчмарки)** — искал скриншот Chatbot Arena leaderboard для доп. иллюстрации внутри раздела. `lmarena.ai/leaderboard` редиректит на `arena.ai/leaderboard`, WebFetch не вернул полезного скриншота/og:image за разумное число попыток. Решение: НЕ добавлять mock — s37 остаётся с логотипами AI-компаний (переиспользование из s36 набора, не обязательный по брифу пункт) и текстовыми карточками, без доп. картинки. Не P0 — бриф пометил s36/s37 как «на твой выбор, не обязательно».
- **word2vec диаграмма (s12a)** — прежде чем остановиться на `king-analogy-viz.png`, пробовал: (1) Wikimedia Commons поиск «word2vec king queen embedding» — 0 релевантных диаграмм (только PDF-презентации); (2) ResearchGate figure «The classical king-woman-man-queen example» — 403 Forbidden при прямом фетче изображения; (3) esciencecenter.nl blog редирект — картинка на странице оказалась несвязанной иллюстрацией (мультяшные лица), отброшена; (4) Mikolov et al. 2013 (`N13-1090`, «Linguistic Regularities») — скачал и отрендерил PDF постранично, нужного scatter-plot с countries/capitals на первых страницах не нашёл (не тратил больше времени на весь PDF, т.к. iteration budget). Итог (v3.1): `king-analogy-viz.png` (Jay Alammar) — реальная, легко читаемая иллюстрация формулы «king − man + woman ≈ queen». **v3.2: заменена на мем Pam «They're the same picture»** — owner explicit: научная диаграмма не считается «мемом», нужен узнаваемый формат.

## v3.2 (round 4) — попытки и компромиссы

- **s05a (робот/токенизация)** — 3+ попытки найти узнаваемый мем-формат конкретно про «робот дословно/по кускам читает текст»: (1) WebSearch «robot literal reading meme template» → нашёлся только нерелевантный «Robot Chitti reading books» (индийское кино, не мем-формат); (2) WebSearch «instructions unclear meme» → нашёлся установленный формат, но референсный кадр (рука в потолочном вентиляторе) визуально и тематически не подходит к теме токенизации; (3) WebSearch «this is not a pipe/captcha AI robot literal» → Magritte-пародии и captcha-мемы существуют, но не как единый чистый шаблон с пустым полем для текста. Решение: **Surprised Pikachu** (высокое качество, чистый шаблон с пустым верхним полем, семантически подходит — «AI уверенно удивлён, отвечая неправильно») — общепризнанный, узнаваемый формат, применённый по аналогии вместо специфичного-но-ненайденного «robot reading» формата.
- **s10 (glitch-токены)** — Magikarp: пробовал (1) официальный PNG с прозрачным фоном через pngkey — получил JPEG с белым фоном (не строго transparent PNG, но визуально идентично на белом слайде); достаточно для встраивания, доп. попытки поиска чистого alpha-PNG не потребовались (quality приемлема).
- **s33a (матрёшка → chonk chart)** — пробовал WebSearch «chonk chart meme cat scale template» — нашёл описания формата (посты, товары на Etsy/Redbubble), но НЕ нашёл прямую ссылку на чистое изображение шаблона с лицензией, пригодной для скачивания через curl (все результаты — маркетплейсы мерча, не raw image URLs). Решение: оставил матрёшку (owner уже одобрил в v3.1) — убрал только подпись-источник, как и остальные unchanged-слайды.
- **s31 (горшочек)** — 2 YouTube-видео с мультфильмом найдены; thumbnail с video ID `o6m9Ae5zTCI` дал качественный `maxresdefault.jpg` (1280×720) с чётким кадром героини у горшочка; video ID `8KH0RVWNv88` дал только low-res `120×90` (thumbnail не сгенерирован в maxres) — использован первый.

## v3.3 update (round 5, issue #183) — owner-мандат «+8–12 новых образов на
## контентные слайды без образа; иконки в ocean-box не считаются»

Прошёл все 47 слайдов деки, сверил assertion каждого слайда с фактическим
наличием узнаваемого образа (не иконка). Добавлено **4 новых образа** на
слайды, где нашлось честное свободное место без потери читаемости
(s15, s25 — второй образ, s39, s40); остальные кандидаты из брифа (s09, s11,
s21, s22, s27, s30, s32, s37) оказались плотными слайдами без свободной зоны
— пропущены с логированием причины в `iteration-log.md` (не насиловал
плотные схемы ради формального числа).

### v3.3-active (новые файлы, используются в рендере)

| Локальный файл | Слайд | Описание | URL источника | Дата скачивания | Лицензия / статус |
|---|---|---|---|---|---|
| `spiderman-similarity.jpg` (свой текст поверх `spiderman-pointing-template.jpg`) | s15 (content) | Мем-шаблон Spider-Man Pointing at Spider-Man (два человека-паука указывают друг на друга) — метафора «похожи ≠ об одном» для similarity ≠ релевантность | https://imgflip.com/memetemplate/114923726/Spiderman-Pointing-At-Spiderman (image src: `https://i.imgflip.com/1wf7pq.jpg`) | 2026-09-06 | Imgflip meme template — fair use, образовательный некоммерческий контекст |
| `needle-haystack-wikimedia.jpg` (уменьшенная копия `needle-haystack-wikimedia-full.jpg`, оригинал 4951×3451) | s25 (content) | Реальное фото иголки в стоге сена — буквальная метафора-якорь needle-in-a-haystack (поиск дословной вставки) | https://commons.wikimedia.org/wiki/File:Needle_in_haystack4.jpg (full: `https://upload.wikimedia.org/wikipedia/commons/5/5a/Needle_in_haystack4.jpg`) | 2026-09-06 | Wikimedia Commons, CC-BY-SA 4.0 |
| `twobuttons-llm-vs-code-toponly.jpg` (crop верхней панели `twobuttons-llm-vs-code.jpg`, свой текст поверх `twobuttons-template.jpg`) | s39 (content) | Мем-шаблон Two Buttons (потный человек между двумя красными кнопками) — «LLM» / «обычный код», метафора трудного выбора инструмента | https://imgflip.com/memetemplate/119139696/Two-Buttons (image src: `https://i.imgflip.com/1g8my4.jpg`) | 2026-09-06 | Imgflip meme template — fair use, образовательный некоммерческий контекст |
| `xkcd-552-correlation.png` | s40 (content) | xkcd #552 «Correlation» — классический трёхпанельный комикс про corr ≠ causation, прямое попадание в тезис «внимание = корреляция, не причинность» | https://xkcd.com/552/ (image: `https://imgs.xkcd.com/comics/correlation.png`) | 2026-09-06 | xkcd — CC-BY-NC 2.5, образовательное некоммерческое использование |

### v3.3 — попытки, не давшие результата (не встроены в деку)

Скачаны и сгенерированы, но **не встроены** — на целевых слайдах не нашлось
честного свободного места без урезания существующего контента (см. детальный
geometry-анализ в `iteration-log.md` per slide):

- `always-has-been-template.png` (Astronaut Always Has Been, https://imgflip.com/memetemplate/255177692) + производный `always-has-been-ru-cost.jpg` — кандидат для s11 (стоимость русского токена). s11 плотный: chart-box + 2 текстовых блока справа заполняют слайд почти до footer (~0.6" свободного места на всю ширину — недостаточно для читаемого 16:9 мема).
- `gandalf-template.jpg` (You Shall Not Pass, https://imgflip.com/memetemplate/38607795) — кандидат для s30 (structured outputs — маскирование невалидных токенов). Слайд заполнен до ~0.4" от footer, свободного места нет.
- `stonks-template.png` (https://imgflip.com/memetemplate/186821996) — кандидат для s22 (экономика prompt caching). Обе колонки + gold callout заполняют слайд до ~0.35" от footer.
- `drake-template.jpg` (Drake Hotline Bling, image src `https://i.imgflip.com/30b1gx.jpg`) — кандидат для s27 (температура T=0 vs сэмплинг). 3 панели + 2 callout-строки заполняют слайд до ~0.4" от footer.

### v3.3 — s33a chonk chart, попытка #4 (продолжение v3.2 попытки #1)

Три дополнительных попытки в этом раунде (итого 4 с учётом v3.2):
1. WebSearch «chonk chart meme original cat scale image "a heckin chonker" template download» — только описания/историю мема (Know Your Meme, Etsy-мерч), без raw image URL.
2. WebFetch `knowyourmeme.com/memes/chonk-oh-lawd-he-comin` напрямую — единственная найденная «image URL» оказалась placeholder blank GIF (`blank-b3f96f160b75b1b49b426754ba188fe8.gif`), не реальный чарт.
3. WebSearch по прямым CDN-паттернам (`pbs.twimg.com`, `i.imgur.com` + названия категорий чарта) — 0 прямых ссылок на изображение, только вторичные упоминания.
4. Проверил альтернативу — ветеринарная «Body Condition Score» шкала (Wikimedia/vet sources) — это **другой артефакт** (клинический scoring chart 1-9, без юмористических категорий «Fine Boi/Heckin Chonker/Oh Lawd»), не соответствует брифу «chonk chart meme».

Итог: chonk chart остаётся ненайденным за 4 задокументированные попытки.
Матрёшка (`matryoshka-wikimedia.jpg`) остаётся на s33a без изменений — per
brief §9 «если не выйдет — оставь матрёшку без подписи».

## v3.3 round 2 (issue #183 — увеличение round-1 вставок + образы Группы B)

Оркестратор отклонил round 1: (A) 4 вставленных образа — «марки в пустых
контейнерах»; (B) отказ «нет места» опровергнут для s09/s11/s22/s30/s32/s37.
Round 2: образы Группы A увеличены до 2.3–4.5" (подписи перерисованы крупнее
в `gen_memes_v33_r2.py`), образы Группы B вставлены со сжатием наименее
ценных элементов слайдов. Скипы s21/s27 подтверждены оркестратором.

### v3.3-r2-active (новые файлы, используются в рендере)

| Локальный файл | Слайд | Описание | URL источника | Дата скачивания | Лицензия / статус |
|---|---|---|---|---|---|
| `mathlady-template.jpg` → `mathlady-tokens.jpg` (свой текст «[123][456][78]?» поверх) | s09 (content) | Мем Math Lady / Confused Lady (4 панели с формулами) — недоумение от нарезки числа токенизатором | https://knowyourmeme.com/memes/math-lady-confused-lady (image: `https://i.kym-cdn.com/entries/icons/original/000/021/464/14608107_1180665285312703_1558693314_n.jpg`) | 2026-09-06 | KYM CDN — fair use, образовательный некоммерческий контекст |
| `pressx-template.jpg` | s37 (content) | Мем Press X to Doubt (L.A. Noire, детектив Коул Фелпс + промпт «X Doubt») — реакция на витринные лидерборд-результаты | https://imgflip.com/memetemplate/110733816/LA-Noire-Press-X-To-Doubt (image: `https://i.imgflip.com/1txerc.jpg`) | 2026-09-06 | Imgflip template — fair use, образовательный некоммерческий контекст |
| `joker-burning-money-yt.jpg` → `joker-burning-money.jpg` (кроп леттербокса + бейджа «1080p») | s32 (content) | Кадр The Dark Knight (2008): Джокер поджигает гору денег — «невидимые токены жгут бюджет» | https://www.youtube.com/watch?v=gtXbJ_savbo (thumbnail: `https://i.ytimg.com/vi/gtXbJ_savbo/maxresdefault.jpg`) | 2026-09-06 | YouTube thumbnail (tier 4) — fair use, образовательный некоммерческий контекст |
| `xkcd-552-correlation-2x.png` | s40 (content) | xkcd #552 «Correlation» в 2x-разрешении (918×371) — замена 1x-версии под увеличенную вставку 4.5" | https://xkcd.com/552/ (image: `https://imgs.xkcd.com/comics/correlation_2x.png`) | 2026-09-06 | xkcd — CC-BY-NC 2.5, образовательное некоммерческое использование |
| `needle-haystack-crop.jpg` (умеренный кроп `needle-haystack-wikimedia.jpg`) | s25 (content) | Умеренный кроп фото иголки в стоге (930×656 из 1200×836) — иголка занимает ~30% ширины кадра, контекст стога сохранён | см. `needle-haystack-wikimedia.jpg` (Wikimedia Commons) | 2026-09-06 (кроп) | Wikimedia Commons, CC-BY-SA 4.0 |
| `twobuttons-template.jpg` (повторное скачивание — отсутствовал локально) | s39 (via `twobuttons-llm-vs-code-toponly.jpg`) | Шаблон Two Buttons для регенерации этикеток крупнее (52px/38px) | https://imgflip.com/memetemplate/119139696/Two-Buttons (image: `https://i.imgflip.com/1g8my4.jpg`) | 2026-09-06 | Imgflip template — fair use |

### Ранее скачанные (v3.3 round 1), теперь ВСТРОЕНЫ в деку

- `always-has-been-ru-cost.jpg` → **s11** (подписи перерисованы крупнее: 54/48px).
- `gandalf-template.jpg` → **s30** как `gandalf-token.jpg` (добавлена подпись «НЕВАЛИДНЫЙ ТОКЕН НЕ ПРОЙДЁТ», 54px).
- `stonks-template.png` → **s22** (без оверлея, как есть).
- `drake-template.jpg` — остаётся НЕ встроенным (скип s27 подтверждён оркестратором).
- `always-has-been-template.png` — шаблон-источник для `always-has-been-ru-cost.jpg`.

### v3.3 r2 — попытки, не давшие результата

- **Math Lady, попытка 1:** `https://i.imgflip.com/1fyz5c.jpg` (из брифа) — 404/пусто; успех со 2-й попытки через KYM CDN (см. выше).
- **Press X to Doubt, попытка 1:** `https://i.imgflip.com/1ii4oc.jpg` (из брифа) — оказался ДРУГИМ мемом (Trump Bill Signing, 1866×1529); заменён корректным `1txerc.jpg` через imgflip-страницу шаблона.
- **Burning money, попытки 1-3 (не встроены):** Wikimedia Commons поиск «burning money» дал (1) `burning-money-wikimedia.jpg` (May Day 2017 NYC, CC-BY 2.0) — тёмная толпа, деньги не читаются; (2) «Burning fake money.JPG» — женщина у таза, деньги не читаются; (3) «Burning Paper Money.jpg» — пламя в темноте без опознаваемых денег. Решение: tier-4 YouTube thumbnail сцены Джокера (выше) — иконический и однозначно читаемый кадр. Файл `burning-money-wikimedia.jpg` оставлен в assets как артефакт поиска, в деке НЕ используется.
