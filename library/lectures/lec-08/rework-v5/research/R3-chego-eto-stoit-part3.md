---
block: R3 — «Чего это стоит», часть 3
tema: Право и авторство в креативных индустриях — статус на 27 октября 2026
jurisdikcii: США · Великобритания (здесь) | ЕС · Россия · голос и внешность (в part3b)
data_sbora: 2026-10-27
parts: 2
prodolzhenie: R3-chego-eto-stoit-part3b.md
---

# Право и авторство: статус на 27 октября 2026. Часть 1 — США и Великобритания

**Продолжение:** [`R3-chego-eto-stoit-part3b.md`](R3-chego-eto-stoit-part3b.md) — лицензирование как
рабочий ответ · ЕС · Россия · голос и внешность · сводка «что решено / что нет».

## Как читать статусы (курс бьёт за смешение)

Пять разных вещей, которые в прессе называются одним словом «суд решил»:

| Статус | Что это значит на самом деле | Можно ли ссылаться как на правило |
|---|---|---|
| **Иск подан** | Одна сторона изложила свою версию. Суд не сказал ничего | Нет |
| **Motion to dismiss отклонена** | Суд сказал: «если факты истца верны, иск имеет право жить». Про факты не сказано ничего | Нет |
| **Решение по существу (SJ / вердикт)** | Суд разобрал факты и применил право | Да, в пределах своего округа |
| **Мировое без признания вины** | Деньги заплачены, правило не создано. Прецедента нет | Нет |
| **Решение обжаловано** | Нижестоящее решение стоит, но может быть отменено | С оговоркой |

**Главная сводка на 27.10.2026:** ни одной окончательной апелляционной инстанции по fair use для
обучения генеративных моделей в США **не существует**. Всё, что есть, — решения районных судов
(district courts), которые между собой расходятся, и одно английское решение первой инстанции,
обжалованное. Любая фраза «суд признал, что обучение законно» на октябрь 2026 — неточность.

---

## 1. США: авторство сгенерированного

### 1.1 Thaler v. Perlmutter — вопрос закрыт на уровне, выше которого идти некуда

| | |
|---|---|
| **Суд** | D.C. Circuit → Верховный суд США, № 25-449 |
| **Подано** | Заявка на регистрацию 2018; иск 2022; апелляция 2024 |
| **Решение по существу** | D.C. Circuit, **18 марта 2025** — автором по Copyright Act может быть только человек |
| **Что было дальше** | Продление срока на cert получено (июль 2025) → **cert petition подан 9 октября 2025** → brief in opposition правительства **23 января 2026** → ответ заявителя **9 февраля 2026** → распределено на конференцию **11 февраля 2026** |
| **Статус на 2026-10-27** | **Certiorari ОТКАЗАН 2 марта 2026.** Верховный суд дело слушать отказался |
| **Что решено** | Требование человеческого авторства устояло окончательно. Машина автором быть не может |
| **Что НЕ решено** | Сколько именно человеческого вклада достаточно. Талер сам признал, что работа «lacks traditional human authorship» — он спорил о крайнем случае, не о границе |

Источники: [SCOTUSblog, дело 25-449](https://www.scotusblog.com/cases/thaler-v-perlmutter/) ·
[Finnegan, «Supreme Court Declines to Hear Thaler v. Perlmutter»](https://www.finnegan.com/en/insights/ip-updates/supreme-court-declines-to-hear-thaler-v-perlmutter-leaving-human-authorship-requirement-intact.html) ·
[Holland & Knight, «The Final Word?», март 2026](https://www.hklaw.com/en/insights/publications/2026/03/the-final-word-supreme-court-refuses-to-hear-case-on-ai-authorship) ·
[Baker Donelson](https://www.bakerdonelson.com/supreme-court-denies-certiorari-in-thaler-v-perlmutter-ai-cannot-be-an-author-under-the-copyright-act)

**Для лекции.** Отказ в certiorari — это не «Верховный суд согласился». Это «Верховный суд не стал
брать дело». Правило D.C. Circuit действует, но формально обязательно только в своём округе.

### 1.2 Copyright Office, Part 2 «Copyrightability» — где именно проходит граница

**Статус документа: финальный, опубликован 29 января 2025.** Не pre-publication.

Что в нём сказано по существу (это и есть практическая граница):

- Четыре вида человеческого вклада рассматриваются отдельно: (1) ИИ как инструмент обработки
  собственной работы, (2) **ввод промптов**, (3) «expressive inputs» — подача собственного
  охраняемого материала внутрь, (4) модификация и компоновка сгенерированного.
- **Промпты сами по себе авторства не дают**, сколько бы их ни было. Формулировка Бюро:
  *«prompts may reflect a user's mental conception or idea, but they do not control the way that
  idea is expressed»*. Аналогия Бюро — заказчик, описавший художнику, что он хочет: заказчик не
  соавтор. Довод «я трудился» (sweat of the brow) отклонён прямо.
- Охраняется только то человеческое, что **различимо в итоговом результате**. Дело Sahni
  (декабрь 2023): человек наложил фильтр «под Ван Гога» на собственную фотографию — Review Board
  отказал, потому что исходный человеческий снимок в итоге неотделим.

Источники: [copyright.gov/ai](https://www.copyright.gov/ai/) ·
[текст отчёта Part 2 (PDF)](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf) ·
[разбор Skadden](https://www.skadden.com/insights/publications/2025/02/copyright-office-publishes-report)

**Сколько регистраций с раскрытым ИИ-вкладом выдано.** К апрелю 2026 — **более 6 000**; по
показаниям Регистратора подкомитету Сената по интеллектуальной собственности **на 12 мая 2026 —
более 7 000** заявок, где ИИ-материал задекларирован и исключён (disclaimed) по правилам
регистрации. То есть механизм работает: регистрируют не «картинку из нейросети», а человеческий
слой поверх неё, с явным вычетом машинного.
Источник: [Ludwig IP Law, «Copyright Office Touts Registration of 6,000 Human+AI Works»](https://ludwigiplaw.com/copyright-office-touts-registration-of-6000-humanai-works-what-it-means-for-ip-owners/)

### 1.3 Два конкретных дела о регистрации

**Kristina Kashtanova, «Zarya of the Dawn»** (февраль 2023). Бюро оставило регистрацию в силе
**только на текст и компоновку**; изображения, сделанные Midjourney, из охраны исключены. Это
первый практический пример «вычета машинного слоя». Новых событий по этому делу в 2026 году
при поиске не обнаружено — `[VFY]`.

**Jason Allen, «Théâtre D'opéra Spatial»**:

| | |
|---|---|
| **Отказ Бюро** | Review Board, **5 сентября 2023** — человеческий вклад de minimis, машинного материала «more than a minimal amount» |
| **Иск** | District of Colorado, № 1:24-cv-2665, подан **26 сентября 2024** против Copyright Office и Ш. Перлмуттер |
| **Довод истца** | 624 итерации промпта — это «more than the bare minimal mental effort» |
| **Ход дела** | MSJ истца **25 августа 2025** → ответ и встречная MSJ Бюро **16 января 2026** |
| **Статус на 2026-10-27** | **Решения нет ни по одной из двух MSJ** |
| **Что НЕ решено** | Главный практический вопрос курса: считается ли итеративное промптирование творческим вкладом |

Источники: [Artnews](https://www.artnews.com/art-news/news/ai-generated-artwork-colorado-state-fair-copyright-decision-reversal-appeal-1234719694/) ·
[DDG, разбор дела](https://www.ddg.fr/actualite/aritificial-intelligence-ai-and-protection-of-creations-the-return-match-of-the-jason-allen-case) ·
[Romano Law](https://www.romanolaw.com/ai-assisted-art-faces-another-copyright-test-what-the-jason-allen-case-could-mean-for-creators/)

### 1.4 Part 3 «Generative AI Training» — документ, который так и не стал окончательным

| | |
|---|---|
| **Опубликован** | **9 мая 2025**, в формате **pre-publication version** |
| **Статус на 2026-10-27** | **По-прежнему pre-publication. Финальная версия не вышла.** Бюро пишет: «A final version of Part 3 will be published in the future», существенных изменений в анализе и выводах не ожидается |
| **Что в нём** | Обучение может быть fair use, но не автоматически: чем ближе выход модели к рыночной нише исходных работ и чем «пиратнее» источник данных, тем слабее защита. Введено понятие рыночного вреда через **замещение и разводнение рынка** (market dilution) |
| **Чем он НЕ является** | Не законом и не решением суда. Copyright Office ведёт регистрацию; fair use решают суды |

Источники: [copyright.gov/ai](https://www.copyright.gov/ai/) ·
[pre-publication PDF](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-3-Generative-AI-Training-Report-Pre-Publication-Version.pdf) ·
[Baker McKenzie](https://connectontech.bakermckenzie.com/third-copyright-report-on-ai-explores-generative-ai-training/) ·
[Mishcon de Reya](https://www.mishcon.com/news/us-copyright-office-report-part-3-generative-ai-training)

### 1.5 Что случилось с автором отчёта: Perlmutter v. Blanche

На следующий день после публикации Part 3 Регистратор авторских прав Шира Перлмуттер была
уволена. Дальнейшая хронология — отдельный сюжет о том, что происходит с регулятором, когда он
пишет неудобный отчёт.

| | |
|---|---|
| **Суд** | D.D.C., № 1:25-cv-01659 → D.C. Circuit |
| **Подано** | май 2025 |
| **Судебный запрет** | D.C. Circuit **10 сентября 2025** — injunction, сохраняющий Перлмуттер в должности; ходатайство о пересмотре отклонено **1 октября 2025** |
| **Верховный суд** | **30 июня 2026** — экстренное заявление администрации (shadow docket) **отклонено**, injunction остался в силе |
| **Лето 2026** | Доп. меморандум ответчика **31 июля 2026** (ссылка на Trump v. Slaughter); ответ Перлмуттер **14 августа 2026** |
| **Статус на 2026-10-27** | **Дело приостановлено (stay)** судьёй Келли в сентябре 2026 в ожидании судьбы билля H.R. 6028 (он сделал бы Регистратора должностью, назначаемой президентом с согласия Сената). Параллельно идёт график брифинга по апелляции, завершающийся **30 октября 2026** |
| **Что решено** | Ничего по существу. Перлмуттер пока в должности |

Источники: [IPWatchdog, 22 сентября 2026](https://ipwatchdog.com/2026/09/22/d-c-judge-pauses-perlmutter-suit-as-copyright-office-bill-awaits-senate-action/) ·
[Munger Tolles & Olson](https://www.mto.com/achievement/supreme-court-leaves-in-place-injunction-preserving-register-of-copyrights-shira-perlmutters-position/) ·
[Democracy Forward](https://democracyforward.org/news/press-releases/u-s-supreme-court-declines-trump-vance-administrations-shadow-docket-request-leaving-protections-for-copyright-office-leadership-in-place/) ·
[Clearinghouse, карточка дела](https://clearinghouse.net/case/46635/)

---

## 2. США: дела об обучении моделей

### 2.1 Сводная таблица — где что стоит на 27 октября 2026

| Дело | Суд, судья | Подано | Статус на 27.10.2026 | Решено по существу? |
|---|---|---|---|---|
| **Bartz v. Anthropic** | N.D. Cal. (Alsup → Martínez-Olguín) | авг. 2024 | **Закрыто.** Мировое $1,5 млрд, **окончательно одобрено 20 июля 2026** | Частично: есть решение 23–24.06.2025 + мировое |
| **Concord Music v. Anthropic** | N.D. Cal., Eumi K. Lee | 18.10.2023 (+2-е дело 28.01.2026) | Встречные MSJ, **слушание 21 октября 2026 — решения нет** | Нет |
| **Kadrey v. Meta** | N.D. Cal., Chhabria | 2023 | SJ в пользу Meta по обучению (25.06.2025); **08.07.2026 отказано в промежуточной апелляции**; иск о раздаче торрентов жив | Частично, в первой инстанции |
| **Andersen v. Stability AI** | N.D. Cal., Orrick | 13.01.2023 | Discovery. Слушание SJ + class cert **назначено на 17.02.2027** (перенесено с 04.11.2026), может сдвинуться ещё | Нет |
| **Disney/Universal + Warner Bros. v. Midjourney** | C.D. Cal., консолидировано | 11.06.2025 / сент. 2025 | Discovery. Крайний срок подачи всех ходатайств **23 ноября 2026** | Нет |
| **NYT v. OpenAI/Microsoft** | S.D.N.Y., Stein | 27.12.2023 | Встречные MSJ; возражения **23.10.2026**, реплики **20.11.2026**; слушание не назначено | Нет |
| **UMG v. Suno** | D. Mass. | 24.06.2024 | Warner урегулировала (нояб. 2025); UMG и Sony продолжают | Нет |
| **Reservoir Media v. Suno** | N.D. Cal., 3:26-cv-12305 | **21.10.2026** | Иск подан шесть дней назад | Нет |
| **UMG v. Udio** | S.D.N.Y. | 24.06.2024 | **Урегулировано 29.10.2025** + совместная платформа | Нет (мировое) |

**Вывод, который выдерживает проверку:** ни одно из этих дел не дало окончательного
апелляционного правила. Самое крупное денежное событие — мировое, то есть покупка выхода, а не
решение вопроса.

### 2.2 Bartz v. Anthropic — $1,5 млрд, и за что именно

**Решение судьи Alsup, 23–24 июня 2025.** Разделил два действия, и это ключ ко всему:

- **Обучение на законно купленных книгах — fair use.** Формулировка: *«spectacularly
  transformative»*. Покупка бумажных книг, их расшивка и сканирование — тоже fair use (смена
  формата для собственного использования).
- **Хранение библиотеки из ~7 млн пиратских книг** из LibGen и PiLiMi — **не fair use**, даже
  если часть из них потом в обучении не использовалась. Пиратское происхождение само по себе
  создаёт ответственность.

**Мировое соглашение.** Объявлено в сентябре 2025: **$1,5 млрд плюс проценты**, примерно на
**500 000 произведений**, то есть **≈ $3 000 за произведение** — вот база, без которой число
$1,5 млрд ничего не значит.

**Окончательное одобрение — 20 июля 2026.** Детали, которые стоит назвать:

| Параметр | Значение | База |
|---|---|---|
| Сумма | $1,5 млрд + проценты | Крупнейшее взыскание по авторскому праву в истории США |
| Произведений — оценка при объявлении | ~500 000 | $1,5 млрд ÷ 500 000 ≈ $3 000 |
| Произведений — окончательный Works List | **482 460** | $1,5 млрд ÷ 482 460 ≈ **$3 100**; заявлено по 92,77 % списка |
| Валовое распределение на признанное произведение | **≈ $3 100** | **ДО вычета** гонораров и администрирования (openclassactions: «estimated gross allocation»). После вычета — меньше $3 000. Прежняя формулировка «после вычета расходов и гонораров» была арифметически невозможна: вычет не увеличивает |
| Гонорары адвокатов | **≈ $101,56 млн** | **6,8 %** от фонда — ниже обычных 25–33 % по class actions |
| Выплаты представителям класса | $15 000 каждому (3 чел.) | суд **срезал** запрошенные $50 000 |
| Возражения | **53 поданы, все отклонены** | |
| Первые выплаты | ожидаются **к 15 ноября 2026** | |

Источники: [Authors Guild, «Court Grants Final Approval»](https://authorsguild.org/news/court-grants-final-approval-anthropic-copyright-settlement/) ·
[JURIST, июль 2026](https://www.jurist.org/news/2026/07/judge-approves-record-1-5-billion-settlement-involving-anthropic/) ·
[AAP](https://publishers.org/news/aap-welcomes-courts-final-settlement-approval-in-bartz-v-anthropic/) ·
[Pearl Cohen](https://www.pearlcohen.com/federal-court-approves-1-5-billion-anthropic-copyright-settlement-largest-in-history/) ·
[Writer Beware, 23.07.2026](https://writerbeware.blog/2026/07/23/anthropic-settlement-update-final-settlement-approved/)

**Чего это мировое НЕ решило.** Оно не создало правила. Anthropic заплатила за **способ
получения** данных, а не за **обучение на них** — по обучению Alsup высказался в её пользу.
Любая ссылка на «$1,5 млрд за обучение ИИ» — ошибка: это $1,5 млрд за хранение пиратской
библиотеки.

### 2.3 Concord Music v. Anthropic — другое дело, которое постоянно путают с Bartz

Это **не** Bartz. Другие истцы (музыкальные издатели), другой предмет (**тексты песен**, не книги),
другой судья (**Eumi K. Lee**), и оно **не урегулировано**.

| Этап | Дата | Что произошло |
|---|---|---|
| Первый иск | **18 октября 2023** | Издатели: Concord, Universal Music Publishing, ABKCO |
| Guardrails agreement | **январь 2025** | Частичное соглашение: Anthropic обязалась держать фильтры, не выдающие тексты песен дословно. Это **соглашение о технических ограничениях, а не мировое** — спор о самом обучении остался |
| Второй, отдельный иск | **28 января 2026** | Требования **свыше $3 млрд** |
| Встречные MSJ | подано 2026 | Обе стороны просят решить дело без суда присяжных |
| **Слушание** | **21 октября 2026** | Полный день аргументов по fair use, фокус — рыночный вред |
| **Статус на 27.10.2026** | | **Судья Ли решения не вынесла. Мирового нет.** Оба дела живы |

Источники: [Music Business Worldwide](https://www.musicbusinessworldwide.com/music-publishers-file-amended-lyrics-lawsuit-against-anthropic-just-as-ai-firms-separate-1-5b-piracy-settlement-with-authors-wins-court-approval/) ·
[Loeb & Loeb, карточка дела](https://www.loeb.com/en/insights/publications/2025/04/concord-music-group-inc-v-anthropic-pbc) ·
[BakerHostetler](https://www.bakerlaw.com/concord-music-group-inc-v-anthropic-pbc/) ·
[разбор слушания 21.10.2026](https://www.aimusicpreneur.com/ai-music-news/concord-anthropic-fair-use-summary-judgment-hearing-october-2026/)

### 2.4 Kadrey v. Meta — противоположная логика в том же здании суда

Судья **Chhabria**, та же Northern District of California, что и Alsup, **25 июня 2025** — тоже
выиграла компания, но по другой причине и с прямо противоположным объяснением.

- Chhabria дал SJ в пользу Meta **не потому, что обучение заведомо законно**, а потому, что
  истцы **не собрали доказательств рыночного вреда**.
- Он прямо назвал **market dilution** — затопление рынка машинными заменителями — потенциально
  решающим фактором и сказал, что при лучшем доказательственном материале четвёртый фактор
  fair use мог бы уйти присяжным или решить дело в пользу истцов.
- **8 июля 2026** Chhabria **отказался сертифицировать** своё решение для промежуточной апелляции
  в Девятый округ: вопросы fair use должны дойти туда целиком, после окончательного решения.
- **Иск о раздаче книг через торренты (distribution) остаётся нерешённым.**

Источники: [ChatGPT Is Eating the World, 25.06.2025](https://chatgptiseatingtheworld.com/2025/06/25/meta-prevails-on-fair-use-in-ai-training-in-kadrey-v-meta-but-judge-chhabria-cautions-a-better-record-of-dilution-or-market-harm-could-prevail-in-other-cases/) ·
[то же, о ходатайстве об апелляции, 09.06.2026](https://chatgptiseatingtheworld.com/2026/06/09/kadrey-asks-judge-chhabria-to-certify-for-interlocutory-appeal-to-9th-circuit-the-judges-2025-summary-judgment-re-metas-downloading-from-shadow-libraries-for-the-purpose-of-ai-training/) ·
[McKool Smith, сводка 18.06.2026](https://www.mckoolsmith.com/newsroom-ailitigation-62) ·
[FisherBroyles, разбор решения](https://fisherbroyles.com/news/client-alert-summary-and-strategic-analysis-of-judge-chhabrias-fair-use-ruling-in-kadrey-v-meta/)

**Пара Alsup / Chhabria — лучший материал лекции.** Два судьи одного округа, с разницей в два дня,
вынесли решения в пользу ИИ-компаний по взаимоисключающим основаниям. Alsup: обучение
трансформативно по сути. Chhabria: обучение прошло, потому что истцы не доказали вред, и в
следующий раз может не пройти. Для инженера это означает: «суд разрешил обучение» — ложная
новость обоих решений.

### 2.5 Andersen v. Stability AI — дело художников, пятый год без решения

| Этап | Дата | Что произошло |
|---|---|---|
| Подан | **13 января 2023** | N.D. Cal. 3:23-cv-00201, судья Orrick |
| 1-я MTD | **30 октября 2023** | Иск «defective in numerous respects», большинство требований отклонено с правом исправить; выжило прямое нарушение против Stability |
| 2-я MTD | **12 августа 2024** (ECF 223) | **Выжили: прямое нарушение, induced infringement, Lanham Act.** Отклонены с прекращением — требования по DMCA § 1202 («double scienter»). Orrick на стадии pleading **принял** теорию, что произведения «may be contained in Stable Diffusion as algorithmic or mathematical representations» |
| SAC / TAC | 31.10.2024 / **27.02.2026** | Третья изменённая жалоба; ответы ответчиков 13.03.2026 |
| Discovery | **10.02.2026**, **19.05.2026** | Магистрат Cisneros: вопросы о «фирменном стиле» истцов отложены до SJ; Midjourney обязана ответить на доп. вопросы |
| Сдвиг графика | **конец сентября 2026** | Orrick продлил график **примерно на 3 месяца** |
| **Статус на 27.10.2026** | | **Класс не сертифицирован. Fair use не решался. Суда не было.** Слушание SJ + class cert назначено на **17 февраля 2027** (перенесено с 04.11.2026 по просьбе истцов) и может сдвинуться снова |

Источник: [AI Lawsuit Tracker, карточка дела, сверена с реестром 12.10.2026](https://ailawsuittracker.com/cases/andersen-v-stability-ai-ltd-3-23-cv-00201/)

**Осторожно с датами.** В сети широко гуляет «первый в США суд присяжных по обучению на
изображениях начинается 8 сентября 2026». Это **устаревшая** дата из раннего графика; по
состоянию на октябрь 2026 суда не было, ближайшее слушание — февраль 2027. Любой источник,
утверждающий, что суд состоялся, — не проверен.

### 2.6 Disney / Universal / Warner Bros. v. Midjourney

| | |
|---|---|
| **Суд** | C.D. Cal., Disney Enterprises Inc. v. Midjourney Inc., 2:25-cv-05275 |
| **Подано** | Disney + Universal — **11 июня 2025**; Warner Bros. Discovery — **сентябрь 2025** |
| **Консолидация** | Дела Disney и Warner объединены **для всех целей, включая суд**; ведущее — Disney |
| **Сроки** | Экспертный discovery закрыт **21 сентября 2026**; последний день подачи всех ходатайств — **23 ноября 2026** |
| **Статус на 27.10.2026** | **Discovery. Решения по существу нет. Fair use не рассматривался** |
| **Позиция Midjourney** | Отрицает ответственность, заявляет fair use; добивается раскрытия того, как **сами студии** используют ИИ |
| **Фон** | Октябрь 2026 — отраслевой отчёт называет Midjourney моделью, хуже всех соблюдающей голливудские права |

Источники: [CourtListener, реестр дела](https://www.courtlistener.com/docket/70513159/disney-enterprises-inc-v-midjourney-inc/) ·
[Variety, о discovery, 2026](https://variety.com/2026/film/news/midjourney-studios-ai-copyright-discovery-1236800902/) ·
[Deadline, октябрь 2026](https://deadline.com/2026/10/midjourney-worst-offender-flouting-hollywood-copyright-1237154802/)

### 2.7 NYT v. OpenAI / Microsoft — дельта к тому, что уже в главе

| Этап | Дата | Что произошло |
|---|---|---|
| Встречные MSJ | **сентябрь 2026** | И истцы, и OpenAI с Microsoft просят судью Stein решить fair use без суда присяжных |
| Возражения | **23 октября 2026** | Издания оспаривают логику ходатайств OpenAI и Microsoft |
| Реплики | **20 ноября 2026** | срок ещё не наступил |
| Исключение экспертов | подано | OpenAI и Microsoft просят исключить часть экспертных показаний истцов и назначить устные прения |
| **Статус на 27.10.2026** | | **Решения нет. Дата слушания не назначена** |

Источники: [MLex](https://www.mlex.com/mlex/intellectual-property/articles/2541728) ·
[AI Lawsuit Tracker](https://ailawsuittracker.com/cases/new-york-times-v-openai/) ·
[текст ходатайства о SJ (PDF)](https://bcheights.com/wp-content/uploads/2026/10/NYTimes-AI-OpenAI-Summary-Judgment.pdf)

### 2.8 Музыка: свежая дельта — иск Reservoir, поданный шесть дней назад

| | |
|---|---|
| **Дело** | Reservoir Media v. Suno, N.D. Cal., **3:26-cv-12305** |
| **Подано** | **21 октября 2026** |
| **Требования** | **$157,5 млн** законной компенсации по основному требованию: **$150 000 × 1 050 композиций** (умышленное нарушение). Плюс по DMCA — $2,625 млн и $26,25 млн |
| **Опора истца** | Собственный ответ Suno в деле UMG: обучающие данные включают *«essentially all music files of reasonable quality that are accessible on the open Internet»* |
| **Статус** | **Иск подан. Ничего не решено** |

Источники: [PPC Land, разбор жалобы](https://ppc.land/reservoir-sues-suno-for-157-5m-over-1-050-songs-in-ai-training-data) ·
[Music Business Worldwide](https://www.musicbusinessworldwide.com/reservoir-sues-suno-for-infringment-over-1050-songs-including-tracks-by-joni-mitchell-johnny-cash-madonna-and-more/) ·
[Musically, 23.10.2026](https://musically.com/2026/10/23/reservoir-hits-suno-and-anthropic-with-copyright-infringement-lawsuits/)

*Перепроверено оркестратором 2026-10-27. Два уточнения к записи выше.* **(1)** Иск **парный**:
в тот же день Reservoir подала и на **Anthropic** — за **853 текста песен**, отдельным делом;
на кадре их нельзя сливать в один. **(2)** Издания расходятся в сумме требования: $157,5 млн
(PPC Land, по расчёту $150 000 × 1 050) против «более $186 млн» у других — разница в том, какие
из трёх требований (основное + два DMCA) включены в счёт. **Подавать как «иск на сумму порядка
$160–190 млн по трём основаниям»**, а не одной точной цифрой; и это по-прежнему **требование
истца**, а не присуждённое.

**Важная деталь для курса.** Suno выпустила V6 на лицензированных данных **9 сентября 2026** — и
через шесть недель получила новый иск на $157,5 млн за **прошлые** модели. Лицензия на будущее
не закрывает прошлое. Это и есть цена «сначала обучим, потом договоримся».

---

## 3. Великобритания: Getty Images v Stability AI

| | |
|---|---|
| **Суд** | High Court of Justice (England & Wales), судья Joanna Smith |
| **Подано** | январь 2023 |
| **Ход процесса** | В ходе слушаний (июнь 2025) Getty **сама отказалась** от основных требований по обучению и по выходам модели — не хватило доказательств, что обучение происходило в юрисдикции Великобритании |
| **Решение** | **4 ноября 2025**. Веса модели — математические параметры, **не «infringing copy»** по CDPA: вторичное нарушение не доказано. Узкая победа Getty **по товарному знаку** — артефакты водяных знаков Getty в сгенерированных изображениях |
| **Разрешение на апелляцию** | **получено в январе 2026** на consequentials hearing: вопрос признан «novel and important», у довода Getty есть «real prospect of success» |
| **Слушание апелляции** | Ожидается в конце 2026; в одном источнике названа дата **1 октября 2026** — **`[VFY]`, независимо не подтверждена** |
| **Статус на 27.10.2026** | **Решения Court of Appeal нет** (проверено по состоянию на 20 октября 2026) |
| **Что решено** | В первой инстанции: веса ≠ копия произведения по английскому праву |
| **Что НЕ решено** | Законно ли само обучение; что будет, если обучение доказуемо шло в Великобритании; устоит ли вывод о весах в апелляции |

Источники: [Taylor Wessing, «Next steps for Getty v Stability», январь 2026](https://www.taylorwessing.com/en/insights-and-events/insights/2026/01/next-steps-for-getty-v-stability-why-has-permission-to-appeal-been-granted) ·
[CMS, о consequentials hearing](https://cms.law/en/gbr/legal-updates/getty-images-v-stability-ai-permission-to-appeal-sought-by-getty-images-at-consequentials-hearing) ·
[JIPLP, академическая критика решения](https://academic.oup.com/jiplp/article/21/8/538/8721803) ·
[AI Vortex, карточка дела](https://www.aivortex.io/legal/ai-case-law/getty-v-stability-ai-uk/)

**Почему это важно отдельно от США.** В Великобритании нет fair use — есть узкие fair dealing
исключения, в которые обучение коммерческой модели не укладывается. Getty проиграла **не потому,
что обучение признали законным**, а потому, что не смогла доказать, где оно происходило, и
потому, что «копия» по английскому закону требует воспроизведения, а веса таковым не признали.
Два разных способа проиграть один и тот же спор в двух юрисдикциях.

---

**Продолжение — [`R3-chego-eto-stoit-part3b.md`](R3-chego-eto-stoit-part3b.md):**
§4 лицензирование как рабочий ответ · §5 Европейский союз · §6 Россия · §7 голос и внешность ·
§8 сводка «что окончательно решено, а что нет».
