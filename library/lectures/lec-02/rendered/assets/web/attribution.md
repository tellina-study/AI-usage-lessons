# Атрибуция веб-изображений — Лекция 2 v3.2 (issue #183, round 4)

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
