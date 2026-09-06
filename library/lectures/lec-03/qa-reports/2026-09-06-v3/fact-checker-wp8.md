VERDICT: APPROVE-WITH-POLISH

# Fact-Checker Report — Лекция 3 v4.0, WP8 classic-base-first (issue #185) — 2026-09-06

Scope: только НОВЫЙ classic-base-first контент (§N.0 подразделы + блоки «что оставить из классики»).
Проверены: chapter.md §1.0, §2.0 + §1.7/§2.4 classic-remainder блоки; chapter-part2.md §3.0 + §3.5 remainder; chapter-part3.md §4.0; chapter-part5.md §5.0 + References §5.0. Остальная глава — вне scope (проверена ранее).

## Severity counts
- P0 (false fact / broken citation / misattribution): **0**
- P1 (missing source / suspicious number / distorted definition): **0**
- P2 (cite format / minor / body-vs-reference gap): **3**

Live-verified через WebSearch: **9 named-фактов** (BM25/Okapi, Rule of Least Power, YAGNI, Design by Contract, OODA, Ousterhout publisher, knowledge distillation, catastrophic forgetting, RRF).

---

## VERIFIED classic named-facts (все атрибуции корректны)

### §1.0 (chapter.md) — формальная спецификация / императив vs декларатив
- ✓ **Design by Contract → Bertrand Meyer / Eiffel.** Verified live: DbC введён Meyer в 1986 как центральная фича языка Eiffel (пред-/постусловия, инварианты). Атрибуция в §1.0 («контрактное программирование в стиле Design by Contract», Eiffel-контекст) корректна.
- ✓ **Z-нотация, TLA+** как машинно-проверяемые формальные спецификации — корректно (Z — formal specification language; TLA+ — Lamport). Не атрибутированы поимённо в §1.0, но названы верно как классы формальной спецификации; ошибки нет.
- ✓ **Императивный vs декларативный, SQL/Prolog как декларатив.** Корректно: SQL описывает искомый результат (планировщик решает «как»); Prolog — декларативный логический язык. Характеристика точная.
- ✓ **OpenAPI / Protobuf как контракты интерфейса** — корректно (схемы API / сериализации как формальный контракт вход/выход).

### §2.0 (chapter.md) — классический информационный поиск
- ✓ **Инвертированный индекс** как фундамент полнотекстового поиска (Lucene, Elasticsearch, PostgreSQL FTS) — корректно, устоявшийся факт.
- ✓ **TF-IDF** («частота термина, взвешенная обратной частотой в коллекции») — определение точное. IDF-компонента восходит к Karen Spärck Jones (1972, «A statistical interpretation of term specificity»); в §2.0 не приписана ложному автору — атрибуции нет, ошибки нет.
- ✓ **BM25 / семейство Okapi.** Verified live: BM25 = ранжирующая функция вероятностного семейства, разработана Stephen Robertson и Karen Spärck Jones (Okapi IR system, City University London, 1980-90-е). §2.0 называет «Best Matching 25, ранжирующая функция семейства Okapi» — корректно. Определение (насыщение по частоте + нормировка на длину документа) точное.
- ✓ **Булев поиск** (AND/NOT/OR как логическое выражение) — корректно.
- ✓ **RRF (Reciprocal Rank Fusion)** в §2.4 remainder-блоке. Verified live: RRF = Cormack, Clarke, Büttcher, SIGIR 2009. §2.4 описывает функционально (слияние BM25 + dense), без ложной атрибуции. Ошибки нет.
- ✓ **Anthropic Contextual Retrieval: top-20 промахи 5,7% → 1,9%** — числа согласованы с ранее проверенной частью главы (§2.1); в scope WP8 повторно не переверифицировались (не новый факт).

### §3.0 (chapter-part2.md) — классическое ML
- ✓ **Transfer learning / предобучение → дообучение** — корректная классическая двухфазная схема (CV/NLP до LLM). Определение точное.
- ✓ **Train/validation/test split** + правило «не тестировать на обучающих данных» — корректно, каноническое определение.
- ✓ **Градиентный спуск / эпоха** — корректно (полный проход по обучающей выборке = эпоха; шаг в сторону уменьшения ошибки).
- ✓ **Catastrophic forgetting как классический феномен.** Verified live: описан McCloskey & Cohen (1989) как «catastrophic interference» на sequential-обучении. §3.0/§3.2 трактуют его как классическое явление, обостряемое дообучением — корректно.
- ✓ **Knowledge distillation → Hinton, Vinyals, Dean, arXiv:1503.02531, 2015.** Verified live: atrib + arXiv ID + год корректны (paper March 2015; presented NIPS 2014 DL Workshop). §3.0 верно разделяет distillation и fine-tuning как разные техники.

### §4.0 (chapter-part3.md) — автоматизация и оркестрация
- ✓ **Конечный автомат (state machine)** — корректное определение (состояния + правила переходов, конструктивная невозможность неразрешённых переходов).
- ✓ **BPMN** («Business Process Model and Notation») — расшифровка и роль (граф. нотация процесса, исполняемая движком) корректны.
- ✓ **DAG-оркестраторы / Airflow** — «directed acyclic graph задач с явными зависимостями» — корректно.
- ✓ **RPA** («Robotic Process Automation») — расшифровка и определение (автоматизация рутины поверх интерфейсов по жёсткому сценарию) корректны.
- ✓ **Теория управления / контур обратной связи (feedback loop)** — корректная атрибуция plan→act→check к классической control theory / АСУ / робототехнике.
- ✓ **OODA-петля → John Boyd.** Verified live: Observe–Orient–Decide–Act, разработана полковником ВВС США John Boyd (нач. 1970-х, из анализа воздушного боя). §4.0 называет «военно-инженерный аналог», атрибуция Boyd — корректна.

### §5.0 (chapter-part5.md) — классический выбор технологии + References
- ✓ **KISS** («keep it simple») — корректно.
- ✓ **YAGNI → Extreme Programming.** Verified live: принцип XP, приписывается Ron Jeffries (XP co-founder). §5.0 body атрибутирует «XP»; Reference §5.0 цитирует Fowler, *Yagni* (2015, martinfowler.com/bliki/Yagni.html) как источник-объяснение — корректно (Fowler — общепризнанный популяризатор, не заявлен автором принципа). Ошибки нет.
- ✓ **Rule of Least Power → Berners-Lee, Mendelsohn, W3C TAG, 2006.** Verified live: W3C TAG Finding, авторы Tim Berners-Lee и Noah Mendelsohn, опубл. 23 Feb 2006 (одобрено TAG 14 Feb 2006), URL w3.org/2001/tag/doc/leastPower.html — совпадает с Reference §5.0. Атрибуция и дата корректны.
- ✓ **Ousterhout, *A Philosophy of Software Design*, 2018, Yaknyam Press.** Verified live: НЕ галлюцинация — Yaknyam Press реальный (self-publishing imprint Ousterhout, Palo Alto), год 2018 корректен. Reference §5.0 корректен.
- ✓ **IEEE 29148:2018** (Systems and software engineering — Requirements engineering) — корректный стандарт requirements engineering; Reference §5.0 указывает верный номер и год.
- ✓ **Build-vs-buy / требования-инжиниринг** — корректные классические понятия, определения точные.

---

## DISPUTED / FALSE facts
Нет.

## NEEDS-CITATION (статистика без источника)
Нет новых статистических claim'ов в classic-base-first контенте, требующих источника. Числовые claim'ы в §N.0-соседних абзацах (NoLiMa, 70/30, LoRA 98.4%, prompt-caching %) — это ранее проверенный не-WP8 контент с уже проставленными `[VFY-day-of]` / cadence-метками; вне scope данного прохода.

## UNVERIFIABLE
Нет. Все 9 ключевых named-фактов подтверждены live через WebSearch.

---

## P2 issues (polish, не блокирующие)

**P2-1 — §5.0 body: Rule of Least Power атрибутирован только Berners-Lee.**
Quote (§5.0): «Принцип наименьшей мощности (rule of least power) — из инженерных заметок W3C (Tim Berners-Lee)».
Issue: co-author **Noah Mendelsohn** опущен в теле, хотя Reference §5.0 указывает обоих корректно. Не ошибка (Berners-Lee — ведущий автор), но для строгости стоит «(Tim Berners-Lee, Noah Mendelsohn, W3C TAG)».
Severity: P2.

**P2-2 — §3.0/§3.5: catastrophic forgetting вводится без исторической атрибуции.**
Термин используется как классический феномен (корректно по сути), но без указания первоисточника (McCloskey & Cohen, 1989). Для «классической базы с нуля» опциональная сноска на 1989 усилила бы точность. Не ошибка — определение верное.
Severity: P2 (optional enrichment).

**P2-3 — §1.0: Z-нотация / TLA+ названы без годов/авторов.**
Перечислены верно как классы формальной спецификации, но без атрибуции (Z — Abrial et al.; TLA+ — Lamport). Для named-инструментов классики короткая атрибуция была бы консистентна с уровнем детализации §5.0. Не ошибка.
Severity: P2 (optional).

---

## Топ-3 правки до публикации
1. **P2-1** — добавить Mendelsohn в тело §5.0 к Rule of Least Power (1 слово; выравнивает body с Reference). Рекомендуется.
2. **P2-2** — опциональная сноска McCloskey & Cohen (1989) при первом вводе catastrophic forgetting. Опционально.
3. **P2-3** — опциональная краткая атрибуция Z/TLA+/Lamport в §1.0. Опционально.

## Итог
Classic-base-first контент (WP8) фактически чист: 0 P0, 0 P1. Все 9 классических named-атрибуций (Meyer/Eiffel, Robertson/Spärck Jones, Boyd, Berners-Lee/Mendelsohn, Jeffries/XP, Hinton/Vinyals/Dean, McCloskey/Cohen, Cormack et al., Ousterhout/Yaknyam) подтверждены live и корректны. Определения классических понятий (инвертированный индекс, TF-IDF, BM25, булев поиск, конечный автомат, BPMN, DAG, RPA, transfer learning, train/test split, градиентный спуск, KISS/YAGNI/least-power, requirements engineering) — точные, без искажений. Три P2 — косметические (полнота атрибуции в теле vs reference), не блокируют публикацию.

**VERDICT: APPROVE-WITH-POLISH** (0 P0, 0 P1, 3 P2).
