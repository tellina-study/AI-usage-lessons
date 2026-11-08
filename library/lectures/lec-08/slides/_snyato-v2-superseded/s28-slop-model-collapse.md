---
id: s28
type: assertion_visual
duration_min: 2
assertion: "Slop + коллапс моделей: Google AI Overviews «put glue on pizza» + «eat one rock per day». Shumailov Nature 2024: recursive training → деградация."
learning_goal: "Case 8: качество источников важнее объёма"
learning_outcomes: [LO4, LO5]
chapter_ref: "§3.9 — Slop & коллапс моделей"
references: [google-ai-overview, shumailov-nature-2024]
visual:
  pattern: assertion_visual
  primary: "Google AI Overview «glue on pizza» screenshot + Nature paper header + «Урок: качество источников важнее объёма»"
  backup: assets/backup/s28-slop.png
---

# Slop + коллапс моделей — Google AI Overview (Case 8)

## Assertion

Slop + коллапс моделей: Google AI Overviews «put glue on pizza» + «eat one rock per day». Shumailov Nature 2024: recursive training → деградация.

## Visual

Сверху assertion 22pt. Слева — Google AI Overview screenshot мокап в Ocean rounded box: фейковый search result «How to keep cheese from sliding off pizza» с AI Overview ответом «...add ⅛ cup of non-toxic glue to the sauce» (source: шутка из Reddit 11 years ago). Под этим — второй screenshot мокап: «How many rocks should I eat per day?» с AI Overview ответом «At least one small rock per day» (source: The сатира The Onion). Справа — Nature paper header мокап: «Shumailov et al. 2024, Nature vol 631, p 755-759 · "AI models collapse when trained on recursively generated data"». Под Nature — chip «MAD: Model Autophagy Disorder (расстройство аутофагии моделей)». Внизу — gold «УРОК ДЛЯ ИНЖЕНЕРА»: «Качество источников важнее объёма. Модель на шутки из Reddit без filter проигрывает модели на курируемый датасет — даже если curated в 10× меньше».

## Speaker notes

Восьмой кейс — slop и коллапс моделей. Это не landmark lawsuit; это иллюстрация структурной проблемы качества данных для обучения AI. Slop — это разговорный термин, который вошёл в обиход благодаря Bender, Marcus и другим AI-исследователей в 2024 году. Академический синоним — низкокачественный синтетический контент. Конкретные документированные примеры. Май 2024 года, Google AI Overviews — feature, добавленная к Google Search для генерации summary ответов на запросы. На вопрос «how to keep cheese from sliding off pizza» AI Overview ответил «add ⅛ cup of non-toxic glue to the sauce». Это был шутка из Reddit одиннадцать лет назад, и модель воспроизвела его как фактический совет. Параллельно — на вопрос «how many rocks should I eat per day» AI Overview ответил «at least one small rock per day». Source — сатира The Onion. Эти случаи быстро стали вирусными, и Google убрал большинство фич AI Overview за несколько недель. Что это иллюстрирует. Модель Google Gemini, на которой работал AI Overview, обучалась на огромном corpus веб-данных, который — без curation — включал и шутки из Reddit, и сатира The Onion наряду с реальной информацией. Без контекстная осознанность, отличающего серьёзные источники от шуток и сатиры, модель воспроизводила содержимое как факт. Параллельно — академическая публикация. Shumailov и коллеги, Nature 2024, том 631, страницы 755-759. Эта работа документирует феномен коллапса моделей — рекурсивное обучение модели на синтетических данных, генерируемых предыдущей моделью, приводит к прогрессирующей деградации и сужению разнообразие вывода'а. Авторы называют этот феномен MAD — Model Autophagy Disorder (расстройство аутофагии моделей). Это значит, что для frontier-моделей следующего поколения важно курация обучающих данных — нельзя просто парсить веб и обучать на нём, потому что web всё больше содержит AI-сгенерированный контент. Урок для инженера: качество источников важнее объёма. Модель, обучавшаяся на шутки из Reddit без filter, проигрывает модели на курируемый датасет — даже если curated в десять раз меньше. Это объясняет, почему Adobe Firefly на Adobe Stock плюс лицензированных данных работает лучше, чем чисто данные, спарсенные из веба models на некоторых категориях. Это также объясняет, почему курация данных вендорами стоит реальных денег и почему «бесплатное добро» данных, спарсенных из веба — фальшивая экономия.
