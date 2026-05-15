# AI-Failure & Judgment Content Audit — Лекция 4 «AI в медицине и фармацевтике»

**VERDICT: APPROVE-CLEAN**

Дата: 2026-05-15 · Аудитор: methodology-critic · Режим: read-only (материалы не правились)
Артефакты: chapter.md (draft v3, 12 679 слов), deck.yaml + slides/*.md (27 содержательных + дивайдеры), speech.md (draft v2, ~6 800 слов)
Правило: `CLAUDE.md` § «AI-Failure & Judgment Content Rule (ENFORCED — фундаментальное)»; процедура — `methodology-critic.md` § Share Check; enforcement — `lecture-production/README.md` §3.6.

---

## 1. Резюме

Все три артефакта **существенно** превышают порог ≥30% bucket-контента, и доля **распределена**, а не сконцентрирована в одном «этическом» кластере. Bucket-контент проходит сквозной нитью через все 5 разделов: PPV-парадокс (§2.2), bias в CV (§2.5), DSP-1181 провал (§3.4), весь раздел 4 (Obermeyer, LLM-анти-паттерны, Change Healthcare, 4-actor framework). Это структурно сильная лекция по критерию суждения. Counter-check (single-artifact concentration / <30%) — **не срабатывает**.

Доли:

| Артефакт | Метрика | Доля bucket | Порог | Статус |
|---|---|---|---|---|
| chapter.md | слова (body, без TOC/LO/глоссария/источников) | **61.8%** (строгий вариант, partial=0: 46.3%) | ≥30% | PASS |
| slides (deck) | минуты (27 content-слайдов, 64 мин) | **52.7%** (slide-count: 46.3%) | ≥30% | PASS |
| speech.md | минуты говорения (mirrors deck) | **~52.7%** | ≥30% | PASS |

Слабейший артефакт по абсолютной доле — **slides/speech (~53%)**, но это всё равно ×1.75 от порога. Разрыв до 30% — **отсутствует** (положительный запас ~23 п.п. в слабейшем артефакте).

---

## 2. Метод измерения

**Bucket** (per rule): (a) документированный провал ИИ + выученный урок; (b) разбор фундаментального ограничения/риска; (c) явный критерий «здесь ИИ не нужен/не применим»; (d) сравнение с более правильным альтернативным инструментом. НЕ засчитаны: общие дисклеймеры, однострочные оговорки без урока/критерия/альтернативы, «магическая пилюля + осторожно».

**Процедура.** Chapter сегментирован по `###`-подсекциям (word count через regex `\S+`). База доли = тело главы (строки 89–567): исключены оглавление, учебные цели, центральный вопрос, введение, глоссарий, источники (служебные блоки, не контент). Каждая подсекция помечена in (1.0) / partial (0.5) / out (0.0). Slides/speech — по минутам из `deck.yaml duration_min` (27 content-слайдов; дивайдеры s05b/s08a/s13a/s19a/s24a, cover s02, Q&A s29, poll-механика s03 исключены из базы).

### 2.1 Chapter — таблица секция → класс → слова

| Секция | Слова | Класс | Обоснование |
|---|---|---|---|
| 0.1 Chester demo | 272 | out | demo «что работает» |
| 0.2 Опрос | 237 | out | калибровка аудитории |
| 0.3 Рамка | 204 | out | дорожная карта |
| 1.1 4 типа | 309 | out | таксономия |
| 1.2 Масштаб FDA/mosmed | 396 | out | scale (есть оговорка про «4 млрд руб» — но это fact-hygiene, не урок ИИ) |
| 1.3 Инструктивный кейс | 305 | **partial** | «качественно другая стоимость ошибки» + критерии (калибровка, audit-trail, fallback) — рамка границ |
| 2.1 Pipeline | 256 | out | техника (closing-оговорка про confidence score → почти partial) |
| 2.2 Sens/spec/prev/PPV | 474 | **in** | фундаментальное ограничение: «94% accuracy → 8% PPV в screening»; явный due-diligence-критерий |
| 2.3 AI vs радиолог | 557 | **partial** | augmentation gap (Goh: AI alone > врач+AI) — урок про workflow-провал; «вопрос поставлен неправильно» |
| 2.4 mosmed.ai | 242 | out | success-story (operational) |
| 2.5 Bias в CV | 366 | **in** | 2 документированных провала (Daneshjou derm, Sjoding pulse-ox) + урок «validation set покрывает deployment population» |
| Self-check 2 | 98 | **in** | PPV-расчёт + 2 механизма bias |
| 3.0 Рамка §3 | 73 | **in** | критерий: peer-reviewed vs self-reported, разный уровень скептицизма |
| 3.1 Pipeline drug | 440 | **partial** | «AI не влияет на attrition»; «AI ускоряет approval — не verified» |
| 3.2 AlphaFold/Proteo | 376 | **partial** | pLDDT-caveat, «independent replication не зафиксирована», «accelerator, не replacement» |
| 3.3 Insilico/RU | 630 | **partial** | verified-vs-claim разделение; «18 мес не verifiable независимо»; честная RU-оговорка |
| 3.4 DSP-1181 | 379 | **in** | документированный провал (discontinued 2022) + урок «design ≠ efficacy»; Recursion/Exscientia merger как сигнал трудной экономики |
| 3.5 Регулирование | 461 | **partial** | high-risk во всех 3 юрисдикциях; PCCP как ответ на ограничение one-and-done |
| Self-check 3 | 85 | **in** | attrition, verifiable claims, PCCP |
| 4.1 Зачем границы | 105 | **in** | постановка: думать о границах на стадии design |
| 4.2 AI-объяснитель границы | 403 | **in** | критерий «AI — объяснитель, не источник истины»; что AI делает плохо (интуиция, цифры без источника) |
| 4.3 Obermeyer 2019 | 435 | **in** | каноничный bias case + урок про proxy + альтернатива (hybrid proxy → bias −84%) |
| 4.4 LLM-анти-паттерны | 597 | **in** | 3 кейса (Tessa, adversarial 83%, self-diagnosis) + уроки + критерий «LLM ≠ medical AI» |
| 4.5 Безопасность данных | 468 | **in** | Change Healthcare breach + урок + критерий «OpenAI API для PHI = noncompliance» |
| 4.6 4-actor framework | 536 | **in** | архитектура ответственности; критерий «final responsibility undivided»; 3 инженерных принципа |
| Self-check 4 | 159 | **in** | 6 вопросов, все на границы/ответственность |
| 5.1 Три вывода | 192 | **partial** | вывод 2 «drug discovery работает частично», вывод 3 «ответственность на враче» |
| 5.2 Что дальше | 126 | out | анонс |
| 5.3 Три наблюдения | 230 | **in** | три принципа ответственного использования = критерии суждения |

**База: 9 528 слов · bucket-взвешенно 5 888 → 61.8%** (строгий, partial→0: 46.3%).

### 2.2 Slides — минуты

База: 64.0 мин (27 content-слайдов). Full-bucket (1.0): **s10** (PPV-парадокс), **s13** (bias CV), **s17b** (DSP-1181 провал), **s19** (AI-объяснитель границы), **s21** (Obermeyer), **s22** (LLM-анти-паттерны), **s23** (Change Healthcare), **s24** (4-actor). Partial (0.5): s08 (стейкс/критерии), s11 (augmentation gap), s15 (attrition), s16 (pLDDT/replication caveat), s17a (verified-vs-claim), s18 (high-risk/PCCP), s20 (постановка границ), s26 (выводы 2+3), s28 (3 принципа в копилку).

**Bucket-взвешенно 33.8 мин из 64 → 52.7%.** Slide-count-метрика: (8 full + 0.5·9 partial)/27 = **46.3%**. Распределение: bucket-слайды есть в каждом из 5 разделов (s10/s13 в Р2, s17b в Р3, s19–s24 в Р4, s26/s28 в Р5).

### 2.3 Speech — минуты говорения

speech.md строго следует deck (slides_covered = тот же список; фрагменты 1:1 со слайдами по таймингу). Bucket-фрагменты: [s10] парадокс PPV (3 мин), [s11] augmentation gap, [s13] bias (2.5), [s15] attrition, [s16] caveat, [s17a/b] verified-vs-claim + провал DSP-1181 (5), [s18] high-risk, [s19] «AI — первое приближение, не источник истины» (3), [s21] Obermeyer (3), [s22] 3 анти-паттерна (4), [s23] breach + «OpenAI API для PHI = noncompliance» (3), [s24] 4-actor (3), [s26/s28] принципы. Уроки сформулированы явно («Инженерный вывод», «медленно, с акцентом»), не однострочными дисклеймерами. **Доля ≈ 52.7% активной речи** (зеркалит deck).

---

## 3. Холистическая оценка

- **≥30% в каждом артефакте:** да — 61.8% / 52.7% / ~52.7%. Минимум (slides ~53%) — почти ×2 порога.
- **Концентрация vs распределение:** распределено. Bucket-нить присутствует в Р1 (1.3 стейкс), Р2 (PPV-парадокс + bias-провалы — 2 из 5 подсекций in), Р3 (DSP-1181 провал + verified-vs-claim рамка — пронизывает весь раздел), Р4 (всё in: 6/6 подсекций), Р5 (3 принципа). Это **не** «вся этика свалена в один раздел» — раздел 4 действительно failure-heavy, но Р2 и Р3 несут самостоятельный judgment-контент (PPV-due-diligence, design≠efficacy).
- **Качество bucket (урок/критерий/альтернатива, не дисклеймер):** высокое. Каждый failure-кейс имеет явный «Engineering lesson». Есть явные критерии-«нет»: «OpenAI/Anthropic API для PHI = noncompliance» (§4.5), «никогда не доверяй одной цифре accuracy» (§2.2), «generative AI ≠ rule-based AI, требует новой валидации» (§4.4). Есть альтернативы: hybrid proxy vs cost-only proxy (§4.3), fine-tuning на DDI vs biased ISIC (§2.5), federated marketplace vs монопольный vendor (§2.4 — partial).
- **Слабейший артефакт:** slides/speech (~53%). Причина — формат: слайды s01/s04/s06/s07/s12 несут «что работает / scale» (out), что нормально для индустриальной лекции. Даже так — запас ~23 п.п.

**Разрыв до 30% holistic: 0 (нет разрыва).** Добавлять контент по этому правилу **не требуется**. Рекомендации ниже — опциональное усиление (chapter ещё draft v3), не gap-closing.

---

## 4. Web-research: верифицированные провалы медицинского ИИ

Проверено через WebSearch 2026-05-15. Цифры/даты сверены, не по памяти.

| # | Кейс | Источник + дата | Проверенная цифра | Урок · куда в Л4 |
|---|---|---|---|---|
| 1 | **IBM Watson for Oncology** — «unsafe and incorrect» рекомендации | STAT News, 25.07.2018 (внутр. документы IBM); MD Anderson свернул контракт ($62M, 2017 Forbes) | Обучен на «синтетических» кейсах 1–2 врачей MSK, не реальных пациентах; пример: химиопрепарат с black-box-warning пациенту с тяжёлым кровотечением. Вреда пациентам не зафиксировано (не применялось на реальных) | Hype vs валидация; обучение на нерепрезентативных данных. → §1.3 или §4.4 как «4-й анти-паттерн / зачем нужна prospective validation» |
| 2 | **Epic Sepsis Model** — внешняя валидация | Wong et al., JAMA Intern Med, 21.06.2021 (Michigan Medicine, 38 455 госпитализаций) | AUC 0.63 (Epic заявлял 0.76–0.83); пропустил **67%** пациентов с сепсисом (1 709 из 2 552); alert на 18% всех госпитализаций (alert fatigue) | Vendor-claimed AUC ≠ external-validated; low base-rate + плохая калибровка. → **сильнейший кандидат на добавление**: §2.2 (PPV/калибровка) или §4.x как US-табличный провал в дополнение к Obermeyer |
| 3 | **COVID ML-модели** — систематический обзор | Roberts et al., Nature Machine Intelligence, 15.03.2021 | 2 212 работ → 62 в обзор; **ни одна не пригодна клинически** из-за methodological flaws / biases (shortcut learning, dataset leakage) | Массовый publish ≠ clinically usable; distribution shift / shortcut. → §2.5 (bias-провалы) или §3-методическая рамка про скептицизм |
| 4 | **Google Health diabetic retinopathy, Таиланд** — field study | Beede et al., CHI 2020, опубл. 27.04.2020 (11 клиник, ноя 2018–авг 2019) | Лаб. accuracy ~90%, но в поле **21%** из 1 838 снимков отклонены как low-quality (освещение); медленный интернет; 2/11 клиник имели затемнённую комнату | Lab ≠ real-world workflow; провал не модели, а деплоймента. → §2.5 или §4.x как «workflow failure», дополняет bias-кейсы |
| 5 | **Дерматология, тон кожи** (уже в Л4 §2.5) | Daneshjou et al., Science Advances 2022; Adamson & Smith 2018 | Sens падает на 20–30% на Fitzpatrick V–VI; ISIC перепредставляет светлую кожу | Уже покрыт. Не дублировать |
| 6 | **Pulse oximeter racial bias** (уже в Л4 §2.5) | Sjoding et al., NEJM 2020; FDA safety comm. 2021 | Систематич. переоценка SpO2 у тёмной кожи; гипоксия пропускается чаще | Уже покрыт. Не дублировать |
| 7 | **FDA recalls AI-устройств** | JMIR Med Inform 2025; PMC12374217 (950 устройств до ноя 2024) | **60 устройств → 182 recall events**; ~43% recalls в первый год после авторизации; «vast majority» recalled-устройств без клинических испытаний; ~5% AI/ML-устройств имеют adverse-event reporting (1 смерть) | 510(k) clearance ≠ prospective testing; post-market surveillance критичен. → §3.5 (регулирование) усиление: «одобрение FDA — не гарантия клинической валидации» |
| 8 | **NEDA Tessa** (уже в Л4 §4.4) | NPR/CBS 2023; AI Incident DB 545 | Cass сменил rule-based→generative, снят за 24ч | Уже покрыт |

**Критерии «здесь ИИ не применять» + альтернатива** (для усиления §2.2/§4):

- **Низкий base-rate без проспективной калибровки** → не доверять model-confidence; альтернатива: валидированные клинические шкалы **qSOFA/SOFA** (низкая dimensionality, traceable) ИЛИ ML только поверх validated-score-входа с external multicenter validation. (Источник по альтернативе: BMC Infect Dis 2023, PMC10977876 — ML поверх SOFA-входа прозрачнее.)
- **Distribution / dataset shift** (Roberts 2021, Google Thailand) → нет деплоймента без field-pilot на целевой популяции; альтернатива: prospective interventional cohort (как Lancet Digit Health 2022 Thailand follow-up), не лабораторный AUC.
- **Нет внешней валидации, есть только vendor-claimed AUC** (Epic Sepsis) → требовать independent external validation перед закупкой; альтернатива: RCT / внешне-валидированная статистика, не self-reported метрика разработчика.

---

## 5. Рекомендации по локациям (опционально, не gap-closing)

Лекция **уже проходит правило с большим запасом**. Ниже — усиления, которые орбита production Л4 (chapter draft v3) **может** учесть для повышения дидактической плотности judgment-блока. Это P2-уровень (улучшение), НЕ P0/P1 (нет структурного дефицита).

1. **§2.2 или новая микро-вставка в §4.4 — Epic Sepsis Model (рек. ~150–200 слов в chapter, +0 слайдов или 1 bullet на s10/s22).** Сильнейший добавочный кейс: показывает «vendor AUC 0.76–0.83 → external 0.63, пропущено 67% сепсиса» — это идеальная иллюстрация уже существующего тезиса §2.2 «не доверяй одной цифре» + критерий «требуй external validation». Дополняет Obermeyer (табличный bias) кейсом табличного **calibration/validation** провала. Источник: Wong et al., JAMA Intern Med 2021.

2. **§3.5 — 1–2 предложения про FDA recalls (рек. ~60–100 слов).** К существующему «1 451 одобрено» добавить контр-факт: «60 из 950 AI-устройств → 182 recall, ~43% в первый год, большинство без клинических испытаний (JMIR Med Inform 2025)». Усиливает критерий «510(k) ≠ prospective validation» и мост к PCCP/post-market surveillance, который уже есть в §3.5/§4.6.

3. **§2.5 — 1 предложение про Google Thailand как «workflow failure» (рек. ~50 слов).** К двум bias-кейсам (Daneshjou, Sjoding) добавить третий тип провала: «лаб ~90% → 21% снимков отклонены в поле из-за освещения (Beede CHI 2020)» — расширяет урок «validation set покрывает deployment population» до «field-pilot обязателен», другой механизм провала (не bias данных, а workflow).

4. **§1.3 — опционально, IBM Watson for Oncology как одно предложение-якорь hype-vs-validation (рек. ~40 слов).** Сейчас §1.3 (partial) обосновывает «зачем медицина инструктивна» через стейкс/регулирование. Watson ($4B, MD Anderson свернул, обучен на синтетике) — каноничный «AI спасёт онкологию → провал» якорь, методически усиливает out→partial→in переход раздела 1.

**Не делать:** дублировать Tessa/Daneshjou/Sjoding (уже в Л4); расширять раздел 4 (он уже 100% bucket — добавление туда усилит концентрацию, чего правило избегает). Все добавления — в Р1–Р3 для ещё лучшего распределения.

---

## 6. Топ-5 приоритетов

| # | Приоритет | Действие | Размер | Severity |
|---|---|---|---|---|
| 1 | Подтвердить APPROVE-CLEAN | Правило выполнено холистически (61.8 / 52.7 / ~52.7%), распределено, качественные уроки/критерии/альтернативы. Gap = 0. | — | — (PASS) |
| 2 | (опц.) Epic Sepsis Model | Микро-вставка в §2.2/§4.4: external AUC 0.63 vs claimed 0.76–0.83, 67% пропущено | ~150–200 слов + 1 bullet | P2 |
| 3 | (опц.) FDA recalls | 1–2 предложения в §3.5: 182 recalls / 950 устройств, 43% в 1-й год | ~60–100 слов | P2 |
| 4 | (опц.) Google Thailand | 1 предложение в §2.5: workflow-failure (21% rejected) как 3-й тип провала | ~50 слов | P2 |
| 5 | (опц.) IBM Watson якорь | 1 предложение в §1.3: hype-vs-validation canonical anchor | ~40 слов | P2 |

**Counter-check (mandatory):** доля <30% или single-artifact concentration? — НЕТ (все ≥52.7%, распределено по 5 разделам, раздел 4 не единственный носитель bucket — §2.2/§2.5/§3.4 несут самостоятельный judgment). Verdict остаётся **APPROVE-CLEAN**. 0 P0, 0 P1, 4 опциональных P2.

---

## Источники (web, верифицировано 2026-05-15)

- IBM Watson for Oncology: [STAT News, 2018-07-25](https://www.statnews.com/2018/07/25/ibm-watson-recommended-unsafe-incorrect-treatments/) · [Henrico Dolfing case study](https://www.henricodolfing.com/2024/12/case-study-ibm-watson-for-oncology-failure.html)
- Epic Sepsis Model: [Wong et al., JAMA Intern Med 2021](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2781307) · [PMC8218233](https://pmc.ncbi.nlm.nih.gov/articles/PMC8218233/)
- COVID ML обзор: [Roberts et al., Nature Machine Intelligence 2021](https://www.nature.com/articles/s42256-021-00307-0)
- Google Thailand DR: [TechCrunch 2020-04-27](https://techcrunch.com/2020/04/27/google-medical-researchers-humbled-when-ai-screening-tool-falls-short-in-real-life-testing/) · [MIT Tech Review](https://www.technologyreview.com/2020/04/27/1000658/google-medical-ai-accurate-lab-real-life-clinic-covid-diabetes-retina-disease/) · [ACM CHI 2020](https://dl.acm.org/doi/fullHtml/10.1145/3313831.3376718)
- FDA recalls AI: [JMIR Med Inform 2025](https://medinform.jmir.org/2025/1/e67552) · [PMC12374217](https://pmc.ncbi.nlm.nih.gov/articles/PMC12374217/)
- Sepsis scores/ML альтернатива: [BMC Infect Dis 2023](https://bmcinfectdis.biomedcentral.com/articles/10.1186/s12879-023-08045-x) · [PMC10977876](https://pmc.ncbi.nlm.nih.gov/articles/PMC10977876/)
