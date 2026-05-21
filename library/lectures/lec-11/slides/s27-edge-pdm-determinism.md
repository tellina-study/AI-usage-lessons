---
id: s27
type: assertion_visual
duration_min: 2.5
assertion: "POSCO: 180 edge nodes. PLC-цикл = 1–10 мс детерминирован. LLM = 100–500 мс. Latency = determinism, не только speed."
learning_goal: "Edge AI + детерминизм edge-вывода (cornerstone fundamental)"
learning_outcomes: [LO1a, LO7]
chapter_ref: "§3.3 edge AI + детерминизм"
failure_bucket: strict_in
references: [posco-edge-180-nodes-2024, holcim-100-plants-c3ai]
visual:
  pattern: latency_comparison
  primary: "Bar chart: PLC 1–10 мс vs LLM 100–500 мс; POSCO + Holcim фото"
---

# Edge AI + детерминизм edge-вывода

## POSCO (Корея, 2024)

**180 edge inference nodes** — failure detection independent of corporate network.

**+5% efficiency, –10% energy, +3% yield** в hot-rolled steel.

Edge = inference происходит на устройстве рядом с PLC, не отсылается в облако.

## Holcim (Глобально, 2024–2026)

100 заводов C3 AI: kiln optimization + PdM.

Cement kiln — это процессный объект; AI оптимизирует расход топлива + предсказывает отказ valve, sensor.

CEMEX + Optimitive: 10% energy savings, ROI 18 мес, –2–5% CO2 per tonne clinker.

## Детерминизм edge-вывода (cornerstone)

**PLC-цикл = 1–10 мс детерминированный budget.**

**LLM = 100–500 мс недетерминированный.**

Edge AI на ML-копроцессоре рядом с PLC может работать в budget 10–50 мс — но это **специальный edge ML stack** (TensorRT, ONNX Runtime, lightweight модели), не general-purpose LLM.

## Формула (read-out-loud)

**«Latency = determinism, не только speed.»**

Edge не равен cloud не только по location, а по latency-determinism. Гарантированный budget — это другая физика.

## F-35 ALIS callback (lec-09)

Помните ALIS из лекции 9 — $44 000 / лётный час, заменён ODIN. Defense PdM учит тому же, что промышленный.

## Speaker notes

Edge AI — это та граница, где AI приходит close к PLC, но всё ещё не становится контроллером.

POSCO в Корее в 2024 году развернул 180 edge inference nodes на металлургическом производстве. Это nodes — отдельные вычислительные устройства, размещённые на объектах рядом с PLC. На каждом из них работает inference, не обучение. Модель проверена и зафиксирована заранее, на edge она просто делает вывод на текущих данных. Преимущество — failure detection происходит независимо от corporate network. Если интернет упал — edge продолжает работать. Если облако перегружено — local inference моментален.

Результаты POSCO: 5 процентов прирост efficiency, 10 процентов снижение потребления энергии, 3 процента прирост yield на hot-rolled steel. Это значимые цифры на масштабе крупного металлургического производства — десятки миллионов долларов в год.

Holcim, мировой производитель цемента, развернул AI на 100 заводах с C3 AI в 2024-2026. Cement kiln — это процессный объект, где идут высокотемпературные реакции с горючим топливом. AI оптимизирует расход топлива и предсказывает отказ valve, sensor, нагревателей. CEMEX совместно с Optimitive — другой кейс — даёт 10 процентов экономию энергии, ROI 18 месяцев, и снижение CO2 на 2-5 процентов на тонну clinker. Это уже не маркетинговая цифра, это публично заявленный production-результат на масштабе сотен заводов.

И теперь про cornerstone, который я хочу, чтобы вы запомнили формулой. Детерминизм edge-вывода. Latency = determinism, не только speed.

PLC-цикл — 1-10 миллисекунд, детерминированный budget. Это значит, что команда должна выполниться за гарантированный отрезок времени. Это требование самого процесса — если клапан не закроется в течение 5 миллисекунд, реактор пошёл в нештатную ситуацию.

LLM — 100-500 миллисекунд, недетерминированный. Это не «обычно быстро», это «иногда долго, и мы не знаем когда». Foundation model может ответить за 50 мс, а может за 800 — зависит от очереди в облаке, длины контекста, нагрузки на GPU.

Эти два budget различаются в 50-100 раз. Это не временное препятствие.

Что работает на границе — edge ML на копроцессоре рядом с PLC. Не LLM, а специализированная маленькая модель: TensorFlow Lite на embedded board, ONNX Runtime, TensorRT — это специальный edge ML stack с детерминированным inference в budget 10-50 миллисекунд. Эта модель проверяет, например, «значение датчика в норме» — да или нет, за 20 миллисекунд гарантированно. Никаких foundation models, никакого общения с облаком.

Latency не равно determinism. Облачная модель может быть быстрой, но не детерминированной. Edge ML — медленнее на больших задачах, но детерминирован. Для control loop важен детерминизм, не средняя скорость.

И callback к лекции 9: помните F-35 ALIS, $44 тысячи за лётный час, систему заменили на ODIN. Defense PdM учит ровно тому же, что промышленный PdM. Та же физика: AI как augment для оператора (или для механика на земле) работает, AI как autonomous controller на flying systems — не работает. Эти уроки переходят между отраслями.
