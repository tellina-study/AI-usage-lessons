---
id: s18
type: assertion_visual
duration_min: 2.5
assertion: "Palantir Maven Smart System — главный американский decision-support флагман. Потолок ~$1,3 миллиарда до 2029 года. Уровень автономии L1 Assistive."
learning_goal: "MSS как пример L1; история Maven 2017-2026"
learning_outcomes: [LO1a, LO1b]
chapter_ref: "§2.2 — Palantir MSS"
references: [defensescoop-2025-mss, govconwire-2024]
visual:
  pattern: assertion_visual
  primary: "Timeline 3 milestones + L1 badge + capability summary"
---

# Palantir Maven Smart System — главный американский флагман Decide

## Assertion

Palantir Maven Smart System — главный американский decision-support флагман. Потолок ~$1,3 миллиарда до 2029 года. Уровень автономии L1 Assistive.

## Visual

Сверху — assertion 28pt bold. Под ней:

**Левая колонка (60%)** — Palantir logo (24px из LobeHub) + horizontal timeline в Ocean rounded box:
- **Май 2024** · $480M IDIQ Army contract (start)
- **Сентябрь 2024** · +$99.8M (расширение все рода войск)
- **Май 2025** · +$795M ceiling increase (gold pivot)
- → **~$1,3 млрд до 2029** (gold callout)

Под timeline — capability bullets:
- Fusion multi-источниковой разведки
- AI-assisted target nomination
- Дашборды для командиров

**Правая колонка (40%)** — info-card «L1 Assistive»:
- Большой бейдж «L1» (gold, 80pt)
- Подпись 16pt: «Assistive»
- 14pt text: «AI выдаёт детекции и сводки. Командир решает.»
- Mini-icon `user-check` 32px

Внизу — small history callout 12pt italic Primary light: «История Maven 2017: Google leak март 2018 → 4000+ подписей → контракт не продлён июнь 2018 → подхвачен Palantir, Anduril, Scale. Разбор — Раздел 4».

Source 12pt italic: «DefenseScoop 2024-2025; GovConWire 2024».

## Speaker notes

Главный американский decision-support флагман — это Palantir Maven Smart System, или MSS. История начинается с Project Maven в 2017 году — программа Министерства обороны США по анализу drone footage с помощью ML. В марте 2018 года через утечку стало известно, что Google помогает в этой программе; к июню 2018 контракт с Google не был продлён под давлением сотрудников. Программа была подхвачена Anduril, Palantir и Scale — этот сюжет подробно разберём в Разделе 4.

MSS — это UI-orchestration layer Palantir над Maven AI. Контракты: первый IDIQ на 480 миллионов в мае 2024 года; дополнение на 99,8 миллиона в сентябре 2024 года на расширение на все рода войск; увеличение потолка на 795 миллионов в мае 2025 года. Суммарный потолок — около 1,3 миллиарда долларов до 2029 года. Эти цифры могут уточняться к моменту лекции и помечены как требующие day-of верификации.

Capability — fusion мульти-источниковой разведки, AI-assisted target nomination, дашборды для командиров. Уровень автономии — L1, Assistive. Это значит: AI выдаёт детекции и сводки, командир решает. Никаких kinetic engagements MSS сам не делает; решение — за человеком. Это и есть главный паттерн «AI-accelerator, не AI-decision-maker», который мы будем видеть как образец на L1-L2.

Что инженеру здесь важно понять: Palantir выиграл этот рынок не только моделями, но инфраструктурным стеком — FedRAMP HIGH, авторизация на нескольких уровнях classified networks (SC2S, SIPR, JWICS). Это огромная инженерная работа, по объёму сравнимая с разработкой собственно AI. Когда вы оцениваете defense-AI вендора, разделяйте две оси: AI capability и authorization stack. Обе важны, но это разные инженерные компетенции.
