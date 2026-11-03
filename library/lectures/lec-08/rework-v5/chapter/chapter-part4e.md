# Часть 4e. Глоссарий и сводная библиография

Начало части 4 — [`chapter-part4.md`](chapter-part4.md),
[`chapter-part4b.md`](chapter-part4b.md), [`chapter-part4c.md`](chapter-part4c.md),
[`chapter-part4d.md`](chapter-part4d.md).

## Оглавление (Часть 4e)

- [Глоссарий](#глоссарий)
- [Сводная библиография](#сводная-библиография)

---

# Глоссарий

Термины даны в том виде, в каком они используются в главе: русское слово основное, английское в
скобках при первом появлении. Раздел главы, где термин вводится, указан в конце статьи.

**Расшумление** (denoising) — пошаговое удаление шума из зашумлённого состояния. Порождающий
процесс медиа-модели: начинается со случайного шума и за S шагов приходит к изображению, звуку
или видео. Каждый шаг выполняется одной и той же обученной сетью, которой сообщают текущее
состояние и номер шага. Раздел 1.

**Прямой процесс** (forward process) — портящее преобразование, пошагово подмешивающее к
исходным данным гауссов шум по заданному расписанию. Обучения не требует: задан формулой.
Нужен затем, чтобы получить обучающие пары «зашумлённое состояние → что в нём лишнее».
Раздел 1.

**Латентное пространство** (latent space) — сжатое представление данных, в котором работает
модель. Изображение 1024×1024 превращается в решётку латентных патчей, в сумме около 4096
единиц; расшумление идёт по ним, а не по пикселям. Экономит вычисления на два порядка.
Раздел 1.

**Автокодировщик** (autoencoder, VAE) — пара сетей: кодировщик сжимает изображение в латентное
представление, декодировщик восстанавливает из него картинку. В медиа-модели играет роль
токенизатора. Переход с четырёх каналов латента на шестнадцать вернул мелкий высокочастотный
рисунок и вместе с ним читаемый текст внутри кадра. Раздел 1.

**Стартовый шум, зерно** (seed) — число, задающее начальное случайное состояние генерации. При
детерминированном сэмплере, тех же весах и тех же параметрах одно и то же зерно даёт один и тот
же результат локально. Смена версии библиотеки, типа точности или видеокарты результат меняет.
Раздел 1, критерий отказа 4 в § 6.3.

**Обусловливание** (conditioning) — подача модели дополнительного условия, которое влияет на
результат: текстового промпта, карты глубины, позы, референсного изображения. Подсказывает
**форму**; истину подложить этим способом невозможно. Раздел 1, § 6.3.

**Перекрёстное внимание** (cross-attention) — механизм, которым текстовое условие попадает
внутрь расшумления: запросы берутся из латентного состояния, ключи и значения — из эмбеддингов
промпта. Промпт при этом остаётся **постоянным** условием на всех шагах; истории, как в диалоге
языковой модели, здесь нет. Раздел 1.

**CFG, направляющая без классификатора** (classifier-free guidance) — приём усиления
соответствия промпту: модель прогоняется дважды, с условием и без него, и предсказания
экстраполируются с коэффициентом. Температурой не является — меняет само предсказание и
удваивает стоимость шага. Раздел 1, вопрос 2 самопроверки.

**Негативный промпт** (negative prompt) — текст, подставляемый вместо пустого условия во втором
проходе CFG; экстраполяция уводит результат от описанного в нём. Гарантией не является: это
смещение, а не запрет. Раздел 1.

**Спрямлённый поток** (rectified flow) — постановка задачи, в которой путь от шума к данным
делается максимально прямым, а сеть учится предсказывать скорость движения по нему. Позволяет
резко сократить число шагов без потери качества; лежит в основе моделей линий SD3 и FLUX.
Раздел 1.

**DiT, диффузионный трансформер** (diffusion transformer) — архитектура, заменившая U-Net:
латентные патчи обрабатываются обычными блоками внимания, как токены в языковой модели. Даёт
предсказуемый рост качества при росте вычислений. Вариант MMDiT ведёт два потока — текстовый и
изобразительный — с общим вниманием. Раздел 1.

**Сэмплер** (sampler, solver) — правило, по которому выполняется очередной обратный шаг: сколько
вычесть из предсказанного, сколько шума добавить обратно. Бывает детерминированным и
стохастическим; от его выбора зависят и скорость, и воспроизводимость. Раздел 1.

**Дистилляция** (distillation) — обучение быстрой модели повторять результат медленной. В
расшумлении сводит число шагов с тысячи до четырёх и менее, что и сделало генерацию дешёвой.
Разновидность с состязательной потерей добавляет к дистилляционной цели дискриминатор, убирающий
замыленность. Раздел 1.

**LoRA** (low-rank adaptation) — низкоранговые матрицы-адаптеры, добавляемые в выбранные слои
при замороженной базовой модели; обучаются десятки и сотни мегабайт вместо гигабайт. Тот же
приём, что курс ввёл для языковых моделей. Раздел 1.

**ControlNet** — обучаемая копия кодирующей половины модели, принимающая структурное условие
(края, карта глубины, поза) и вливающая его в замороженный оригинал через нулевые свёртки.
Работает на инференсе, веса базы не меняет. Раздел 1.

**IP-Adapter** — «промпт картинкой»: референсное изображение кодируется и подаётся отдельным
перекрёстным вниманием, параллельно текстовому. Около 22 млн параметров; закрывает значительную
часть задач, для которых иначе дообучали бы модель. Раздел 1.

**Аудиокодек, нейронный** (neural audio codec) — сеть, сжимающая звук в дискретные токены и
восстанавливающая его обратно. Его **частота кадров** (сколько наборов токенов на секунду звука)
определяет максимальную длину того, что модель способна выдать за раз. Раздел 2.

**Остаточное векторное квантование** (residual vector quantization, RVQ) — способ дискретизации
звука несколькими кодовыми книгами подряд: первая даёт грубое приближение, каждая следующая
кодирует остаток от предыдущих. Даёт несколько параллельных потоков токенов на каждый кадр
звука — задача, которой у текста нет. Раздел 2.

**Разделение источников** (source separation) — машинное выделение отдельных партий (голоса,
ударных, фортепиано) из готовой смеси. Задача, обратная синтезу: ничего нового не порождается.
Инструмент «Now and Then»; образец критерия отказа 3. Раздел 2, § 6.3.

**Пространственно-временное внимание** (spatiotemporal attention) — внимание, считающееся сразу
по всем патчам пространства и времени видеоклипа. Даёт согласованность между кадрами и платит
за неё квадратичным ростом стоимости при удлинении клипа или увеличении стороны кадра. Раздел 3.

**Причинный (каузальный) трёхмерный автокодировщик** (causal 3D VAE) — автокодировщик,
сжимающий видео одновременно по пространству и по времени, причём причинно: каждый кадр
кодируется только по себе и по предшествующим, а первый — отдельно, только пространственно. Это
позволяет одной модели работать и с изображением, и с видео; коэффициент сжатия здесь — самый
сильный рычаг стоимости. Раздел 3.

**Гауссово спрыскивание** (3D Gaussian splatting) — представление трёхмерной сцены набором
полупрозрачных гауссовых «клякс», растеризуемых напрямую видеокартой. Против NeRF: обучение 48
часов → 41 минута, показ 0,06 → 134 кадра в секунду при почти равном качестве (PSNR 27,69 →
27,21), и размер 8,6 → 734 МБ. Разменяли память на скорость. Раздел 4.

**NeRF** (neural radiance field, нейронное поле яркости) — представление сцены одной небольшой
сетью, которая по точке и направлению взгляда выдаёт цвет и плотность. Даёт трёхтысячекратное
сжатие сцены ценой очень медленного показа. Предшественник гауссова спрыскивания. Раздел 4.

**Ретопология** (retopology) — перестройка сетки модели в аккуратную, преимущественно
четырёхугольную, пригодную для анимации. Сгенерированная геометрия приходит плотной и
неструктурированной (её извлекают алгоритмами изоповерхности), поэтому стадия остаётся ручной.
Раздел 4.

**Развёртка** (UV unwrapping) — разметка соответствия между поверхностью трёхмерной модели и
плоской текстурой. На плотной несвязной сетке производственного качества не получается; стадия
остаётся. Раздел 4.

**Риггинг** (rigging) — построение скелета и управляющих элементов, которыми модель приводится
в движение. Требует понимания, как объект деформируется при анимации; в извлечённой
изоповерхности такой информации нет. Раздел 4.

**Дискриминативная задача** (discriminative task) — задача различения, в которой по входу
предсказывается метка либо оценка, а не новое содержимое. Распознавание сгенерированного,
классификация, поиск по изображению. Те же блоки внимания, обратное направление. Раздел 5.

**ViT, визуальный трансформер** (vision transformer) — трансформер, применённый к изображению,
нарезанному на патчи. Основа современных распознавателей; в связке с текстовым кодировщиком даёт
совместное пространство изображений и подписей. Раздел 5.

**AUC, площадь под кривой** (area under the ROC curve) — мера качества ранжирования
распознавателя по всем возможным порогам сразу. Может оставаться высокой тогда, когда точность
при рабочем пороге упала до случайной: 94,9 при 51,9 % верных решений. Спрашивать следует
точность при рабочем пороге. Раздел 5, вопрос 7 самопроверки.

**C2PA, Content Credentials** — открытый стандарт подписи происхождения **снаружи** содержимого:
криптографически заверенные метаданные о том, чем и как файл сделан и что с ним делали.
Криптография работает; уязвимо звено доверия к тому, кто подписывает. Раздел 5.

**SynthID** — семейство водяных знаков **внутри** содержимого: незаметное изменение самих данных
(пикселей, звука, распределения токенов текста), переживающее обычные преобразования. Вместе с
C2PA образует две половины одной задачи: подпись снаружи и знак внутри. На моделях с открытыми
весами отсутствует. Раздел 5.

**Провенанс, происхождение** (provenance) — прослеживаемая история того, откуда взялся результат.
У ответа языковой модели с RAG есть ссылка на документ; у сгенерированного кадра её нет и быть
не может, потому что вклад каждого обучающего примера размазан по миллиардам весов. Отсюда и
нужда в подписи снаружи. Разделы 5 и 6.

---

# Сводная библиография

Источники сгруппированы по разделам главы. Все адреса проверялись при сборке материала
27 октября 2026 года.

## Общее: масштаб, траектория, рынок

- Everypixel Journal, замер числа сгенерированных изображений, 15 августа 2023 (не обновлялся) —
  https://www.marketingprofs.com/charts/2023/49890/surge-of-ai-generated-images-online
- Goldman Sachs Research. The Potentially Large Effects of Artificial Intelligence on Economic
  Growth. 26 марта 2023 —
  https://www.gspublishing.com/content/research/en/reports/2023/03/27/d64e052b-0f6e-45d7-967b-d7be35fabd16.pdf
- Research and Markets, Generative AI in Media Market Report —
  https://www.researchandmarkets.com/reports/5980596/generative-ai-in-media-market-report
- The Business Research Company, Generative AI in Media and Entertainment Global Market Report —
  https://www.thebusinessresearchcompany.com/report/generative-ai-in-media-and-entertainment-global-market-report

## Раздел 6: производственные случаи и адреса платежа

- Caixin Global. Cover Story: How AI Took Over China's Micro-Drama Industry in 90 Days.
  1 июня 2026 —
  https://www.caixinglobal.com/2026-06-01/cover-story-how-ai-took-over-chinas-micro-drama-industry-in-90-days-102449814.html
- TechNode, о китайских микродрамах, 3 сентября 2026 —
  https://technode.com/2026/09/03/from-wild-growth-to-tech-driven-growth-in-chinas-ai-short-drama-industry/
- fxguide, разбор «Air Head» (отношение 300:1) —
  https://www.fxguide.com/fxfeatured/actually-using-sora/
- PR Newswire, Toys "R" Us Studios и Native Foreign, июнь 2024 —
  https://www.prnewswire.com/news-releases/toysrus-studios-and-native-foreign-use-openais-sora-to-narrate-the-origin-story-of-beloved-toyrus-brand-302180332.html
- Блог Kwork. Рынок фриланса 2025: итоги года —
  https://blog.kwork.ru/rynok-frilansa/rynok-frilansa-2025-itogi-goda-ot-kwork
- Sostav. Кейс «Яндекс Практикума»: как сократить бюджет на съёмку в 10 раз. 16 апреля 2026 —
  https://www.sostav.ru/publication/kejs-yandeks-praktikuma-kak-sokratit-byudzhet-na-semku-reklamnogo-rolika-v-10-raz-s-pomoshchyu-nejrosetej-83189.html

## Раздел 6: четыре рынка

- TechCrunch, Deezer о доле сгенерированной музыки в загрузках, 20 апреля 2026 —
  https://techcrunch.com/2026/04/20/deezer-says-44-of-songs-uploaded-to-its-platform-daily-are-ai-generated/
- Deezer Newsroom, превышение 50 % суточной загрузки, июль 2026 —
  https://newsroom-deezer.com/2026/07/ai-music-exceeds-50-percent-daily-uploads-deezer/
- Cinevva, исследование раскрытий на Steam, 20 июля 2026 —
  https://app.cinevva.com/news/2026-07-20-steam-ai-disclosure-study
- Totally Human, независимый счёт по 53 597 релизам —
  https://www.totallyhuman.io/blog/the-surprising-new-number-of-genai-games-on-steam
- Audio Publishers Association, Research FAQ (итоги 2025) — https://www.audiopub.org/research-faq
- Хабр, независимый замер доли машинной музыки на Яндекс Музыке —
  https://habr.com/ru/articles/1036166/
- Euronews, Breaking Rust и его знаменатель, 14 ноября 2025 —
  https://www.euronews.com/2025/11/14/breaking-rust-ai-artist-tops-us-chart-for-first-time-as-study-reveals-alarming-recognition

## Раздел 6: опыты и измерения производительности

- Dell'Acqua F. et al. Navigating the Jagged Technological Frontier. SSRN 4573321, 18 сентября
  2023 — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321
- Noy S., Zhang W. Experimental Evidence on the Productivity Effects of Generative Artificial
  Intelligence. MIT, рабочая версия 2 марта 2023 —
  https://economics.mit.edu/sites/default/files/inline-files/Noy_Zhang_1.pdf · журнальная
  версия: *Science* 381(6654):187–192, 14 июля 2023, doi:10.1126/science.adh2586
- METR. Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity.
  10 июля 2025 — https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ ·
  полный текст: arXiv:2507.09089 — https://arxiv.org/abs/2507.09089
- Peng S. et al. The Impact of AI on Developer Productivity: Evidence from GitHub Copilot.
  arXiv:2302.06590, 13 февраля 2023 — https://arxiv.org/abs/2302.06590
- Brynjolfsson E., Li D., Raymond L. Generative AI at Work. arXiv:2304.11771, 23 апреля 2023;
  *QJE* 2025 — https://arxiv.org/abs/2304.11771
- Rajpal S. From Producing to Validating: How AI Is Deskilling Freelancers. arXiv:2608.26089,
  26 августа 2026 — https://arxiv.org/abs/2608.26089
- Ju H., Aral S. Collaborating with AI Agents: Field Experiments on Teamwork, Productivity, and
  Performance. arXiv:2503.18238, 23 марта 2025 (MIT IDE) — https://arxiv.org/abs/2503.18238

## Раздел 6: устройство моделей и границы метода

- Carlini N. et al. Extracting Training Data from Diffusion Models. arXiv:2301.13188, 2023 —
  https://arxiv.org/abs/2301.13188
- Jayasumana S. et al. Rethinking FID: Towards a Better Evaluation Metric for Image Generation.
  CVPR 2024 —
  https://openaccess.thecvf.com/content/CVPR2024/papers/Jayasumana_Rethinking_FID_Towards_a_Better_Evaluation_Metric_for_Image_Generation_CVPR_2024_paper.pdf
- Hessel J. et al. CLIPScore: A Reference-free Evaluation Metric for Image Captioning.
  arXiv:2104.08718, 2021 — https://arxiv.org/abs/2104.08718
- Huang K. et al. T2I-CompBench. arXiv:2307.06350, 2023 — https://arxiv.org/abs/2307.06350
- Zhang L., Rao A., Agrawala M. Adding Conditional Control to Text-to-Image Diffusion Models
  (ControlNet). arXiv:2302.05543, 2023 — https://arxiv.org/abs/2302.05543
- Ye H. et al. IP-Adapter. arXiv:2308.06721, 2023 — https://arxiv.org/abs/2308.06721
- Mildenhall B. et al. NeRF. arXiv:2003.08934, 2020 — https://arxiv.org/abs/2003.08934

## Раздел 6: куда идёт индустрия

- Wikipedia, Sora (text-to-video model), раздел о прекращении —
  https://en.wikipedia.org/wiki/Sora_(text-to-video_model)
- Reuters, о прекращении Sora, 24 марта 2026 —
  https://www.reuters.com/technology/openai-set-discontinue-sora-video-platform-app-wsj-reports-2026-03-24/
- TechCrunch. Why OpenAI really shut down Sora. 29 марта 2026 —
  https://techcrunch.com/2026/03/29/why-openai-really-shut-down-sora/
- Hollywood Reporter, Тайлер Перри о приостановке стройки на $800 млн —
  https://www.hollywoodreporter.com/business/business-news/tyler-perry-ai-alarm-1235833276/
- Scrollflow. AI Video Generation After Sora: The Real October 2026 Map —
  https://www.getscrollflow.com/blog/ai-video-generation-after-sora
- Suno, примечания к выпускам (v6 от 9 сентября 2026) — https://suno.com/release-notes
- Wikipedia, Genie (world model) — https://en.wikipedia.org/wiki/Genie_(world_model)
- R&D World, о Genie 3 —
  https://www.rdworldonline.com/googles-genie-3-breaks-through-the-real-time-barrier-for-ai-world-models/

## § 8.1–8.3: рынок труда

- Challenger, Gray & Christmas. Challenger Report, September 2026 (PDF) —
  https://www.challengergray.com/wp-content/uploads/2026/10/Challenger-Report-September-2026.pdf
- Brynjolfsson E., Chandar B., Chen R. Canaries in the Coal Mine? Stanford Digital Economy Lab,
  август 2026 (PDF) — https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf
- Bureau of Labor Statistics, Occupational Outlook Handbook: Graphic Designers —
  https://www.bls.gov/ooh/arts-and-design/graphic-designers.htm · Interpreters and Translators —
  https://www.bls.gov/ooh/media-and-communication/interpreters-and-translators.htm · Announcers
  and DJs — https://www.bls.gov/ooh/media-and-communication/announcers.htm
- Indeed Hiring Lab. AI Exposure Isn't Squeezing Advertised Pay in the US — It's Boosting It.
  17 сентября 2026 —
  https://hiringlab.indeed.com/2026/09/17/ai-exposure-isnt-squeezing-advertised-pay-in-the-us-its-boosting-it/
- Indeed Hiring Lab. How Employers Are Talking About AI in Job Postings. 28 октября 2025 —
  https://hiringlab.indeed.com/2025/10/28/how-employers-are-talking-about-ai-in-job-postings/
- Zhu Y., Tyson G., Hui X. The Invisible Hand: Generative AI Adoption on an Online Freelancing
  Market. arXiv:2512.02509, 2 декабря 2025 — https://arxiv.org/abs/2512.02509
- Demirci O., Hannane J., Zhu X. Who Is AI Replacing? *Management Science*, 2025 —
  https://pubsonline.informs.org/doi/10.1287/mnsc.2024.05420
- Hui X., Reshef O., Zhou L. The Short-Term Effects of Generative AI on Employment. CESifo WP
  10601, 2023 — https://ideas.repec.org/p/ces/ceswps/_10601.html
- CVL Economics. Future Unscripted, январь 2024 (полный текст, Архив Интернета) —
  https://archive.org/details/future-unscripted-the-impact-of-generative-artificial-intelligence-on-entertainment-industry-jobs
- World Economic Forum. Future of Jobs Report 2025 (PDF) —
  https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf
- ILO Working Paper 140. Generative AI and Jobs: A Refined Global Index of Occupational Exposure.
  20 мая 2025 —
  https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure
- Wang Z., Baxi A., Bakhshi H., Siepel J. Demand for Creativity and AI Skills in the
  Post-ChatGPT Labour Market: Evidence from UK Job Vacancies. Creative Industries Policy and
  Evidence Centre, 2026 —
  https://pec.ac.uk/discussion_paper_/demand-creativity-ai-skills-post-chatgpt/ · журнальная
  версия: *Regional Studies*, doi:10.1080/00343404.2026.2688960
- AI-Generated “Workslop” Is Destroying Productivity. *Harvard Business Review*, 22 сентября
  2025 (опрос 1 150 работников, Stanford Social Media Lab совместно с BetterUp Labs) —
  https://hbr.org/2025/09/ai-generated-workslop-is-destroying-productivity
- CNews, hh.ru о премии за ИИ-навыки, 21 августа 2026 —
  https://www.cnews.ru/news/line/2026-08-21_kak_zarabotat_na_nejrosetyah
- Sostav, HINT по данным hh.ru о рекламных профессиях, 23 октября 2026 —
  https://www.sostav.ru/publication/reklamnye-professii-teryayut-poiskovuyu-populyarnost-87987.html
- Sostav, Okkam Creative об агентствах и доверии аудитории, 12 февраля 2026 —
  https://www.sostav.ru/publication/100-reklamnykh-agentstv-ispolzuyut-nejroseti-no-ne-vse-potrebiteli-gotovy-eto-prinyat-81674.html
- NAVA, методика опроса 2026 — https://navavoices.org/vo-survey-2026/
- Voice Crafters, State of Voice Acting 2026 — https://www.voicecrafters.com/state-of-voice-acting/

## § 8.4: право

- SCOTUSblog, Thaler v. Perlmutter, дело 25-449 —
  https://www.scotusblog.com/cases/thaler-v-perlmutter/
- U.S. Copyright Office, Copyright and Artificial Intelligence, Part 2: Copyrightability (PDF) —
  https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf
- U.S. Copyright Office, Part 3: Generative AI Training (предварительная версия, PDF) —
  https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-3-Generative-AI-Training-Report-Pre-Publication-Version.pdf
- Authors Guild, об окончательном одобрении мирового соглашения с Anthropic —
  https://authorsguild.org/news/court-grants-final-approval-anthropic-copyright-settlement/
- ChatGPT Is Eating the World, разбор решения Kadrey v. Meta, 25 июня 2025 —
  https://chatgptiseatingtheworld.com/2025/06/25/meta-prevails-on-fair-use-in-ai-training-in-kadrey-v-meta-but-judge-chhabria-cautions-a-better-record-of-dilution-or-market-harm-could-prevail-in-other-cases/
- AI Lawsuit Tracker, Andersen v. Stability AI —
  https://ailawsuittracker.com/cases/andersen-v-stability-ai-ltd-3-23-cv-00201/
- CMS, Getty Images v Stability AI: разрешение на апелляцию —
  https://cms.law/en/gbr/legal-updates/getty-images-v-stability-ai-permission-to-appeal-sought-by-getty-images-at-consequentials-hearing
- Taylor Wessing, Next steps for Getty v Stability, январь 2026 —
  https://www.taylorwessing.com/en/insights-and-events/insights/2026/01/next-steps-for-getty-v-stability-why-has-permission-to-appeal-been-granted
- Cooley, о вступлении в силу обязанностей прозрачности AI Act, 3 августа 2026 —
  https://www.cooley.com/news/insight/2026/2026-08-03-eu-ai-act-transparency-obligations-take-effect-2-august-2026
- Европейская комиссия, руководство по обязанностям прозрачности —
  https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations
- Официальное опубликование Федерального закона № 243-ФЗ от 26 июля 2026 —
  http://publication.pravo.gov.ru/document/0001202607260003
- Российская газета, полный текст Федерального закона № 243-ФЗ, 31 июля 2026 —
  https://rg.ru/documents/2026/07/31/fz243-dok.html
- Право.ру, АСГМ защитил дипфейк (дело № А40-200471/2023) — https://pravo.ru/news/250272/
- Хабр, разбор отказа по сгенерированным изображениям —
  https://habr.com/ru/articles/1067546/
- Интерфакс, о позиции Правительства по проекту статьи 152.3 ГК —
  https://www.interfax.ru/russia/1003742
- Holland & Knight, о Tennessee ELVIS Act —
  https://www.hklaw.com/en/insights/publications/2024/04/first-of-its-kind-ai-law-addresses-deep-fakes-and-voice-clones
- Billboard, что означают лицензионные сделки Suno и Udio —
  https://www.billboard.com/pro/what-suno-udio-licensing-deals-mean-future-ai-music/
- Publisher AI Deals and Payments Tracker — https://keywordseverywhere.com/news/publisher-ai-deals/
- Getty Images, карточка модели генеративного сервиса —
  https://developer.gettyimages.com/ai-generation/model-card/
- Microsoft On the Issues, Copilot Copyright Commitment —
  https://blogs.microsoft.com/on-the-issues/2023/09/07/copilot-copyright-commitment-ai-legal-concerns/
- Российская газета, исследование Ipsos об отношении к маркировке, 20 октября 2026 —
  https://rg.ru/2026/10/20/issledovanie-sravnilo-effektivnost-reklamnyh-rolikov-sozdannyh-ii-i-chelovekom.html

## Справочный аппарат главы

- Реестр разборов Лекции 8 (якорь всех чисел главы): `rework-v5/REESTR-RAZBOROV.md` и части 2–3.
- Общий бриф авторов главы: `rework-v5/chapter/BRIEF-OBSHCHIY.md`.
- План лекции: `rework-v5/PLAN-01-os-vopros-keystone.md`,
  `rework-v5/PLAN-02-hrebet-i-raskladka.md`, `rework-v5/PLAN-03-chto-perenositsya-i-poryadok.md`.
