# Дневник студента ИУ6 — Лекция 15 «AI в научных исследованиях» — 2026-05-27 (v1 slides review)

Я — третьекурсник ИУ6 МГТУ. ML базово прошёл, AlphaFold в новостях видел, NotebookLM пробовал. CASP, IDP, DFT, MD, BO+GP, ECMWF, AIRI, Boltz-1, Aurora, GraphCast, Coscientist vs Co-Scientist, ICMJE — впервые слышу. Сижу на лекции, вижу 39 PNG и слышу речь лектора (speaker notes).

---

## Verdict (4-level)

**APPROVE-WITH-POLISH.** Лекция концептуально сильная, keystone (s03 «лестница 6 ступеней») работает как диагностический инструмент, walked examples (s07/s25/s28/s34) очень хорошие. Но есть 4-5 слайдов, где PNG **физически не читается** в зале (s13/s14/s18/s24/s34 — текст слишком мелкий) и 1-2 designer-extras утечки (s28 «Стоимость: 5 мин» как timing markers; s29 overflow «CELLLS»). Не REJECT — основа крепкая, payoff arc есть.

---

## Engagement Table (sample 10 random slides)

| Slide | Что | Реакция студента |
|---|---|---|
| s01 | Hook AlphaFold + Galactica | **Engaged** — резкий контраст, обе истории конкретные, понятно зачем здесь |
| s03 | Keystone лестница 6 ступеней | **Engaged** — диагностический tool, цвет ступени 3 (золото) сразу скажет «прорыв», 6 (красная) — «запрещён» |
| s04 | Глоссарий 15 терминов | **Phone time** — wall of text, 15 строк, я не успеваю прочесть и слушать |
| s07 | WE-1 grant idea tree | **Engaged** — 6 шагов, могу follow и применить к своей курсовой |
| s10 | Sakana cherry-pick | **Engaged** — большая золотая «1%» цифра, urgent message |
| s14 | AlphaFold DB 200M vs 200K | **Phone time** — PNG визуально mini-сlide, всё сжато, цифры мелкие |
| s17 | Палгрейв 35 из 36 | **Engaged** — emotional impact, donut + «1 из 36» — это запомнится |
| s19 | AlphaProof IMO | **Engaged** — clean chart, P1-P6 цветной столбчатый, понятно что решено/не решено |
| s27 | NotebookLM 17M / Elicit 138M | **Neutral** — три равных карточки, всё одинаково, я не понимаю что главное |
| s33 | 4 категории «AI не нужен» | **Engaged** — диагностика, картинка quadrant + примеры — могу применить |
| s39 | Closing AlphaFold DB | **Neutral** — слишком много миниатюр одной темы, не one-hero как обещали |

---

## 5 Mental Hooks I'd Retain через 2 weeks

1. **«AlphaFold взял Нобель — Galactica прожила 3 дня. Различать — задача инженера.»** (s01) — золотой hook, два события одной эпохи.
2. **«6 ступеней лестницы научного цикла; на 3-й (Experiment) — прорыв, на 6-й (Review) — AI запрещён.»** (s03 keystone) — диагностический tool на любую задачу.
3. **«Sakana: 100 черновиков → 3 на ICLR → 1 принят = 1% истинная автономия.»** (s08/s10) — конкретные числа, легко пересказать.
4. **«Палгрейв-Шуп проверил 36 проб A-Lab — 35 содержали ошибки. AI предсказывает структуру, но не открытие.»** (s17) — самая шоковая часть лекции, эмоциональный fix.
5. **«Frontiers / PROTEMNS / ZXPENS / 3 дня до retraction.»** (s29) — visceral, помню термины и временные рамки.

---

## Top 5 Confusions / Terminology Gaps

1. **s04 glossary — 15 терминов сразу.** «Закрытый/открытый мир» определён в одну строку — этого мало, чтобы понять. RAG, IDP, CASP, DFT/MD, BO/GP, ECMWF, ICMJE — впервые слышу всё, и через 30 секунд показ переключился на s05. **Решение:** glossary как backup, а не как ступенька; ввести термины inline когда встречаются.

2. **s11 «BO+GP байесовская» — что это вообще?** Я знаю «оптимизация», слово «байесовский» помню из ТВиМС. Слайд показывает кривую сходимости — это понятно (BO быстрее). Но что внутри — для меня черный ящик, и в речи лектора тоже не разворачивается. **Я унесу:** «BO+GP — это 40 лет статистики, обгоняет Sakana». Но **не унесу:** «когда BO+GP лучше RL или CNN».

3. **s09 Coscientist vs Co-Scientist.** Главное — «не путать», но я бы и так не путал, я о них только что услышал. **Полезнее было бы:** один из них в речи и забыть второй, или мнемоника «CMU 2023 = эксперимент, DeepMind 2026 = гипотеза».

4. **s18 Aurora vs ECMWF.** PNG настолько мелкий, что я не могу прочесть «AIFS» и «IFS». Услышал «5000× быстрее эталона» — впечатляет, но что такое эталон не понял. ECMWF — впервые слышу.

5. **s31 ICMJE / Springer / Elsevier / Frontiers / Nature.** Я знаю Springer и Nature как brand. ICMJE — впервые. Таблица 5×4 — что-то от чего-то зависит, но **«мне зачем»** не сформулировано до s31 — раздел 4 про этику, но как студент я не подаю в Nature на 3-м курсе.

---

## Cognitive Load Hotspots

| Slide | Проблема | Severity |
|---|---|---|
| **s04** | Глоссарий 15 терминов × 3 колонки = wall of text, я не успеваю прочесть | P1 — phone time гарантирован |
| **s13** | PNG визуально очень мелкий — фото лиц + ribbon + timeline + 3 строки сразу | P1 — physically unreadable в зале |
| **s14** | «AlphaFold-2 vs AlphaFold-3» — flowchart мелкими буквами + 4 даты + ribbons | P1 — physically unreadable |
| **s18** | Aurora vs ECMWF — глобус + chart + caption всё в 720p сжато | P1 — physically unreadable |
| **s22** | Allen MICrONS — 1 мм³ + 84k нейронов + 500M синапсов + 4 км аксонов, и фото мозга | P1 — слишком плотно, цифры теряются |
| **s23** | LIGO conformal — теоретический термин «conformal prediction» без объяснения | P2 — поверхностно понимаю |
| **s24** | AlphaFold IDP — IDP неизвестный термин, pLDDT неизвестен | P1 — два неизвестных термина |
| **s34** | WE-3 catalyst — PNG почти неразличим, текст микроскопический | P1 — physically unreadable |
| **s37** | RU context — 3 центра × (название + 2024-2025 публикации + GigaChat 2 + регуляторная рамка + разрывы) | P2 — много, но интересно |

**Топ-3 «text-only wall»:** s04 (глоссарий), s31 (ICMJE 5×4 таблица), s37 (RU context).

**Топ-3 «pretty but empty» нет** — здесь скорее обратная проблема: красивые шаблоны (s33 quadrant, s07 6-step tree) работают, но плотные PNG (s13/s14/s18) сэйвят дизайн ценой читаемости.

---

## Mock-Fallback Detection (student POV)

- **s01 hero:** PNG показывает «AlphaFold Nobel» + цитату MIT Tech Review о Galactica. Левая часть — фото с цветной композицией (выглядит как стилизованная карточка, не настоящее Nobel-фото). Правая — текст-цитата в красной рамке. **Подозрение:** левая часть — stylized card mimicking screenshot, не реальная Nobel ceremony photo. Я бы хотел увидеть **узнаваемое лицо Hassabis / Jumper / Baker** или **реальный AlphaFold ribbon**. Сейчас левая часть выглядит как «архитектурное здание + текст» — это не Nobel ceremony.

- **s39 closing:** на PNG множество мелких миниатюр (AlphaFold ribbons + chart + flowchart). Это **не hero** — это **collage из миниатюр**. Меморий рулу «hero ≥40% площади» не выполнен. Я бы хотел один **большой** AlphaFold ribbon (типа PDB 7Z6T full-screen), а не 6 миниатюр.

- **s14 AlphaFold DB screenshot:** «AlphaFold 2 vs AlphaFold 3» — выглядит как stylized timeline card, не реальный screenshot AlphaFold DB сайта.

- **s27 NotebookLM/Elicit:** три равные карточки без реальных скриншотов интерфейсов NotebookLM/Elicit/Consensus. Студент, который пользуется NotebookLM, заметит, что это **не интерфейс**. Я бы хотел увидеть реальный NotebookLM screen.

---

## P1-DELETE Recommendations

### DELETE (recommend)
- **None polnostyu DELETE** — лекция плотная и каждый слайд несёт что-то.

### MERGE / CONSOLIDATE
- **s09 (Coscientist vs Co-Scientist)** → MERGE в s07/s08 как одна строка. «Не путать» — это too granular для 1-го показа лекции; в курсе они два раза не понадобятся.
- **s23 (LIGO ML)** → MERGE в s22 (Allen MICrONS) как «третий пример Analyse-фазы». LIGO для студента 3-го курса — астрофизика, далеко; merge сократит §3 и даст больше места §5 (самой важной).
- **s27 (NotebookLM/Elicit/Consensus)** → можно сократить до 1 карточки + сказать «есть ещё две похожие» в речи. Студент 3-го курса знает NotebookLM, две другие — лишний шум.
- **s37 (RU context)** → разделить или вынести в backup. Это **не часть keystone-лестницы**, это политико-институциональный довесок. Для лекции про когда AI работает и когда нет — это не payoff.

### REDESIGN (не DELETE, но переделать)
- **s04 glossary 15 терминов** → REDESIGN: вместо wall of text — **mini-card на 4-6 ключевых терминов** (RAG, фундаментальная модель, открытый/закрытый мир, HITL). Остальное в backup.
- **s13/s14 AlphaFold timeline/DB** → REDESIGN с **меньше элементов на слайде**. Сейчас PNG настолько плотный, что я как студент в зале вижу «много букв, переключусь на телефон».
- **s18 Aurora/ECMWF** → REDESIGN: один большой chart + название модели + название эталона, и НЕ пихать globe + multi-panel.
- **s22 Allen MICrONS** → REDESIGN: один большой connectome rendering + 3 цифры (84k neurons, 500M synapses, 4km axons), без фото здания.
- **s24 AlphaFold IDP** → REDESIGN: ввести IDP отдельной строкой (или в s04 glossary вынести), а не запихнуть в s24 inline.
- **s34 WE-3 catalyst** → REDESIGN. **Сейчас этот PNG физически нечитабелен.** Это разобранный пример — он должен быть **четко виден**. Структура 6 шагов как s07 — была бы понятна.
- **s39 closing** → REDESIGN до **одного hero** (real AlphaFold ribbon, ≥40% площади) + 1-2 строки текста. Сейчас это collage.

### DESIGNER-EXTRA LEAK FLAGS
- **s28 («Стоимость: 5 мин / 15 мин / 5 мин / 20 мин»)** — это **timing markers в visible body**. Хотя контекстуально это «cost of verification» (часть лесов AI-policy), визуально читается как «сколько времени тратит каждый шаг» = timing. **CLAUDE.md правило «No Timing in Slides»** активируется. Заменить на «низкая стоимость / средняя / высокая» (text label) или просто убрать time labels — speaker notes уже несут информацию.
- **s29 footer «CELLLS»** — текст ««CELLLS»» **обрезается рамкой**, наполовину выходит ниже. Это visual bug — нужно либо уместить, либо удалить третье слово.
- **s06/s12/s20/s26/s32 — section dividers с tags WE-1, Sakana cherry-pick, Coscientist vs Co-Scientist** — это `→ sNN` map-tags не в visible body, но **выглядят как «навигационная подсказка»**. Студенту они ничего не дают (имена слайдов которые впереди — мне как студенту не помогают), а лектору — это «scaffold». **CLAUDE.md правило «No Extra Content»**: «вы здесь» / «→ sNN» — designer-extra. **Не критично**, но если убрать — слайды чище.
- **s32 footer «Самая важная часть лекции — про осознанный отказ от AI»** — это **методический комментарий в visible body** («самая важная часть»). По правилу «No Methodology in Slides» — это designer-extra. Заменить на смысл раздела одной строкой («Когда AI не нужен — критерии и зрелые альтернативы»).
- **s07 footer «Возвращаемся к рамке в §5 и применяем в разобранном примере WE-3 (катализатор).»** — это **forward-reference («§5», «WE-3»)** в visible body. Студенту в 7-й минуте лекции это «вы здесь» подсказка из scaffold. Замени на «Эту рамку применим в финальном WE-3 примере» (без § номера и без кода WE-3 видного).

---

## Cross-Lecture Continuity Assessment

- **s03 footer «Отличие от лекций 13 и 14: научный цикл итеративный, не последовательный.»** — natural callback, мне как студенту полезно (я Лекцию 13 «лестница среды» помню). **Useful.**
- **s35 «Зрелые методы 30-70 лет: не запасные — основные» footer (BO+GP 1989, DFT 1965, ANOVA 1925, Simplex 1947)** — natural, embedded in content. **Useful.**
- **s39 footer «Лекция 16 — медтех: частично закрытый (геофизика) + частично открытый (резервуар)»** — bridge to L16. **Reasonable** для tease, но на closing slide это «слишком много forward-info». Я бы предпочёл один сильный takeaway («Биология лучше известна — финал ещё далеко») + ровный bridge «продолжим в Лекции 16».

No condescending callbacks замечено. Cross-lecture continuity **в норме**.

---

## Overall Narrative Arc — Payoff Structure

**Да, payoff structure есть и работает:**

1. **Hook (s01):** AlphaFold vs Galactica — две стороны медали. Sets central tension.
2. **Keystone (s03):** 6 ступеней лестницы → diagnostic tool. **Returns в §5.**
3. **Central question (s05):** «где прорыв, где фабрика статей, как решать» + 5-step framework anticipated.
4. **§1 Hypothesis+Design (s06-s11):** AI продаётся за автономию (Sakana 1%), но даёт **узкую помощь** (Coscientist 2023 + BO+GP). Урок: расширение, не автономия.
5. **§2 Experiment (s12-s19):** AlphaFold + GNoME + AlphaProof — **самые сильные успехи**. Нобель уровень. Но трещины (Палгрейв 35/36).
6. **§3 Analyse (s20-s25):** **самые надёжные применения** AI. CNN экзопланеты, MICrONS, LIGO, AlphaFold IDP problem. + WE-TESS framework.
7. **§4 Write+Review (s26-s31):** **самый острый раздел этики.** NotebookLM работает, но Frontiers / NeurIPS показывают каскадное загрязнение литературы. ICMJE policies.
8. **§5 Когда AI не нужен (s32-s39):** **payoff — диагностический вопросник + 5 зрелых альтернатив + WE-3 application + vendor framework.**

**Главный приём «5-шаговая рамка собирается к концу»** работает: s05 anonsiruet, s07 применяет, s25 применяет, s28 применяет, s34 завершает применение. **Это сильный pedagogical arc.**

**Слабости arc:**
- §3 (s21-s25) — самый «спокойный» раздел, после §2-trauma (Палгрейв) и до §4-trauma (Frontiers). Здесь energy ~75-65% (45-я минута лекции), и **плотные PNG s22/s23/s24** = phone time risk.
- §4 ICMJE table (s31) — институциональная **в момент, когда я уже устал**. Это «правила игры» для аспиранта, не для меня 3-курсника. Energy ~60%.
- s37 RU context — позиция в самом конце (66-я мин?), когда energy ~50%. Институциональная информация в момент low energy = phone time.

---

## Summary

- **Top-3 моменты, где зацепило:** s01 (Galactica 3 days), s10/s17 (Sakana 1% + Палгрейв 35/36), s28/s29 (WE-2 bibliography + Frontiers PROTEMNS).
- **Top-3 моменты, где отвлёкся:** s04 (glossary wall), s13/s14 (mini-fonts на PNG), s18-s24 кластер (плотные слайды §3 + новые термины).
- **Top-5 вопросов после лекции:**
  1. Где грань между «AI как расширение» и «autonomous fraud»? — кажется, это вопрос о цене проверки.
  2. Что такое closed-world / open-world педагогически точно? — определение мелькает, но я бы хотел один минут разбор.
  3. ICMJE — это нормативно для меня как студента 3 курса? Когда я столкнусь?
  4. Sakana v2 — это рабочий инструмент или ещё прототип? Могу ли я попробовать сейчас?
  5. RU context (AIRI, Sber AI, Yandex Research) — где у нас доступ к их LLM как студентов?

- **Общее ощущение:** **«зашло».** Лекция держит структуру keystone → walked examples → diagnostic. Главные тезисы (1% автономии, 35/36 ошибок, PROTEMNS/ZXPENS, 5 зрелых альтернатив 30-70 лет) — четкие mental hooks. Хочу видеть переработку 5-6 «mini-PNG» слайдов (s13/s14/s18/s22/s24/s34) и cleanup designer-extras на s28/s32/s37.
