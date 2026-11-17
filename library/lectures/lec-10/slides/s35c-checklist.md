---
id: s35c
type: schema_checklist
duration_min: 1.3
assertion: "10 вопросов в 5 блоках (Классификация / Промышленное состояние / Ответственность / Lock-in / Подключение). 8-10 green = buy / pilot; 5-7 = conditional; ≤4 = reject. Минимальный аудит-чек, ответ не словами вендора, а внешними источниками."
learning_goal: "LO2 операционно — application артефакт для due diligence"
learning_outcomes: [LO2]
chapter_ref: "§6.1a Часть 3 — Pre-purchase verification checklist"
references: []
visual:
  pattern: schema_checklist_5blocks
  primary: "Vertical schema 5 blocks × 2 пункта + scoring rubric (8-10 / 5-7 / ≤4)"
---

# Чек-лист проверки перед покупкой ИИ-решения

## Assertion

10 вопросов в 5 блоках (Классификация / Промышленное состояние / Ответственность / Lock-in / Подключение). 8-10 green = buy / pilot; 5-7 = conditional; ≤4 = reject. Минимальный аудит-чек, ответ не словами вендора, а внешними источниками.

## Visual

Под assertion 28pt bold — vertical schema из 5 blocks, каждый блок в Ocean rounded box с icon Lucide 32px Primary mid + 2 nested пункта.

**Блок 1 — Классификация решения** (icon `list-checks`):
1. **Ступень лестницы (L1-L5)** — однозначный ответ от вендора?
2. **Режим работы AI** — rule-based / ML / CV / sensor-fusion / RAG-grounded / agentic? **Бренд ≠ режим**

**Блок 2 — Промышленное состояние** (icon `factory`):
3. **Число production-внедрений** — не «sold», не «pilot», не «partner announcement»; verifiable через customer references
4. **Точность на краевых случаях** — bench-test от **независимой** экстеншн-службы; documented failure modes

**Блок 3 — Ответственность и регуляторика** (icon `gavel`):
5. **Условия ответственности в EULA** — если «autonomous», кто отвечает за collision/damage? Маркетинг ≠ контракт
6. **Регуляторный статус** — EU AI Act high-risk; FCC compliance; локальные сертификации; запросить compliance documentation

**Блок 4 — Lock-in и exit-route** (icon `unlock`):
7. **Exit-route данных** — доступ к истории обработок, спутниковым снимкам, метрикам стада при разрыве?
8. **Multi-vendor совместимость** — эксклюзив или работает в смешанном парке?

**Блок 5 — Подключение и resilience** (icon `wifi-off`):
9. **Минимальная связь** — всегда cloud / периодическая / offline? Какая часть функций при отказе канала?
10. **Mechanical fallback** — деградация в «обычный трактор / доильный аппарат» при отключении AI?

Справа от schema (или внизу) — **scoring rubric** в Teal-tint box:

- **8-10 green** ✓ → buy / pilot ready
- **5-7 green** ◐ → conditional pilot (1-2 объекта + критерии выхода)
- **≤4 green** ✗ → reject or escalate to expert audit

Bottom callout 14pt italic в gold-tint box: «**Каждый пункт проверяется НЕ словами вендора**, а **внешними источниками**: independent reports, public registers, customer references, regulatory filings. Это конкретный практический инструмент критической оценки вендорского claim — навык, которым инженер защищает компанию от vendor maskirovka».

Footer 12pt italic: «Источник: Chapter v3.1 §6.1a Часть 3».

## Speaker notes

Прежде чем свести пять критериев — чеклист предварительной верификации для AgTech-решения: десять вопросов в пяти блоках по два пункта, ответ не словами вендора, а внешними источниками.

Блок первый — классификация решения. Первый вопрос: на какой ступени лестницы (L1-L5) решение? Если вендор не может однозначно ответить — продукт смешивает уровни; «универсальная платформа для всего цикла АПК» почти всегда означает, что L1-функции не отработаны. Второй вопрос: какой режим работы ИИ — rule-based, классический ML, CV, sensor-fusion, RAG-grounded LLM, агентный? Бренд не равен режиму, и ответ подсказывает, на каком классе провалов решение уязвимо.

Блок второй — промышленное состояние. Третий вопрос: сколько production-внедрений — не «sold», не «pilot», не «partner announcement» — и сколько из них верифицировано независимо через customer references? Четвёртый: какова точность на краевых случаях конкретной среды развёртывания — тип почвы, климат, порода скота? Запросить bench-test от независимой сельскохозяйственной экстеншн-службы, не от вендора, и список задокументированных failure modes.

Блок третий — ответственность и регуляторика. Пятый вопрос: если продукт продаётся как «autonomous», кто отвечает за collision или damage? Ответ «фермер» — vendor maskirovka: маркетинг говорит «autonomous», контракт — «вы отвечаете». Шестой: регуляторный статус в юрисдикции — EU AI Act high-risk, FCC compliance, локальные сертификации; отказ предоставить compliance documentation — red flag.

Блок четвёртый — lock-in и exit-route. Седьмой вопрос: какая exit-route при разрыве — кто получит доступ к истории обработок, снимкам, метрикам стада, и что сказано об этом в контракте? Восьмой: решение требует эксклюзивной привязки или работает в смешанном парке?

Блок пятый — подключение и resilience. Девятый вопрос: связь всегда cloud, периодическая или offline, и какая доля функций доступна при отказе канала? Десятый: что происходит при отключении AI-функции — политика, истечение подписки, решение вендора — и возможна ли деградация в «обычный трактор» без потери базовых функций?

Восемь-десять green — buy / pilot ready; пять-семь — conditional pilot на одном-двух объектах с критериями выхода; четыре и меньше — reject или escalate to expert audit. Каждый из десяти пунктов проверяется не словами вендора, а внешними источниками — independent reports, public registers, customer references, regulatory filings: это инструмент, которым инженер защищает компанию от vendor maskirovka.

## Источники

- Chapter v3.1 §6.1a Часть 3.
