# Lecture 4 — Прогрессия автономности, конфигурации, методологии, docs-as-code

**Date:** 2026-05-16 · **Researcher:** fact-checker research subagent · **Issue:** #99

---

## 1. Лестница автономности (4 уровня) — связь с «лестницей сложности» Л3

| Ур. | Уровень | Что делает AI | Кто решает | Эффективность 2026 | Где растёт риск / где человек обязателен | Источник |
|---|---|---|---|---|---|---|
| **A** | **Автодополнение** (Copilot tab-completion, Copilot-класс) | Дописывает строку/блок по контексту | Человек принимает каждое предложение | Зрелый. Лаб. RCT: **+55%** скорости на изолированной задаче (CI [21%,89%], p=.0017); поле MS/Accenture **+7.5…21.8% PR/нед** | Риск низкий; человек = постоянный фильтр. Риск: автопринятие без чтения → клоны/уязвимости | GitHub Research, arXiv:2302.06590 (2023-02); MIT GenAI pub |
| **B** | **Мелкие задачи через чат/inline** (объясни, напиши функцию, фикс) | Генерит фрагмент/функцию/фикс в диалоге | Человек ставит задачу + ревьюит результат | «70%/80%-проблема»: быстро до ~70–80%, последние 20–30% трудны | Риск: «почти правильно» (66% фрустрация SO 2025), скрытые баги; человек = review + последняя миля | addyo.substack.com «70%»(2024-12)/«80%»(2025); survey.stackoverflow.co/2025 |
| **C** | **Кодинг-агент, крупные задачи** (Claude Code/Codex-класс: многофайловые правки, прогон тестов) | Планирует, правит много файлов, гоняет тесты, итерирует | Человек ставит задачу, ревьюит PR, мержит | SWE-bench Verified ~85–88.7% (контаминирован); **SWE-bench Pro ~64.3%** (приватные кодбазы) | Риск резко ↑ на незнакомых/приватных кодбазах; человек = review/merge gate, тест-оракул | swebench.com; Scale SWE-Bench Pro; marc0.dev (май 2026) **[VERIFY ON DAY OF LECTURE]** |
| **D** | **Оркестратор + трекер** (issue→PR автономно, multi-agent) | Берёт issue из трекера, делает PR, иногда несколько агентов | Человек — стратегия, approval, merge, prod-гейт | НЕ доказано как ускорение: METR early-2025 **−19%** (медленнее); late-2025 сигнал «unreliable» (selection bias) | Максимальный риск: автономный деструктив (Replit/Kiro/PocketOS); человек ОБЯЗАН на approval/prod/деструктив | metr.org 2025-07-10 / 2026-02-24; arXiv:2507.09089 |

**Связь с Л3:** уровни A→D = подъём по «лестнице сложности» Л3 (от инструмента-помощника к автономному агенту). Принцип Л3 «когда не ИИ» применяется буквально: чем выше уровень автономии, тем строже критерий «здесь нужен человек / non-AI control» (гейты, бэкапы, least-privilege).

**Где человек обязателен (сводно):** (1) выбор «что строить» — essential complexity (Brooks); (2) approval перед prod/деструктивными операциями; (3) merge-решение и accountability; (4) security/threat review; (5) последние 20–30% (edge-cases, интеграция); (6) обучение junior без делегирования генерации.

---

## 2. Конфигурации: solo+AI vs team+AI

### Solo-разработчик + AI как «команда»
**Плюсы:** стоимость AI-стека ~$300–500/мес vs human-эквивалент $80–120k/мес; нет coordination overhead; AI закрывает 80–85% execution (vendor-оценка) — research/synthesis/repetitive на скейле; 36.3% новых венчуров 2026 — solo-founded (растёт); кейсы: Pieter Levels ($3M+ ARR, 0 сотрудников), Ben Broca/Polsia ($1M+ ARR, 1100 клиентов solo).
**Риски:** solo = **«exhausted bottleneck»** — каждое решение/edge-case/24-7 через одного человека; AI не валидирует рынок, цену, кого из клиентов «уволить»; нет второго ревьюера → single point of failure на качестве/безопасности (см. Replit-класс инцидентов — часто именно solo/vibe-контекст).
**Когда:** ранняя стадия, MVP, прототип, well-scoped исполнение; НЕ для high-stakes prod без внешнего ревью.

### Команда людей + AI (обращается к ИИ)
**Плюсы:** сохраняется peer-review, ownership, distributed accountability; AI амплифицирует сильную команду (DORA: «strong teams use AI to become even better»).
**Риски:** SDD/spec-методология **«ломается при переходе от одного к команде»** без shared visibility (что кто планировал, какие constraints/assumptions); AI амплифицирует и слабую команду — «only highlights and intensifies existing problems» (DORA 2025); рост throughput при падении stability требует строгих gates.
**Когда:** prod-системы, регулируемые/критичные домены, долгоживущий код, требуется аудит/ответственность.

**Вывод для лекции:** конфигурация — это trade-off «скорость/стоимость (solo+AI)» против «надёжность/ответственность/масштаб (team+AI)». Human judgment, стратегия, customer-relationship, distribution — невосполнимое конкурентное ядро в обоих.
Источники: blog.mean.ceo (2026); taskade.com one-person-companies (2026); loadsys.com spec-driven-for-teams (2026); DORA 2025.
**Confidence:** $-цифры и 80–85% — vendor/blog (MEDIUM, помечать как оценки); вывод о trade-off (HIGH, согласуется с DORA).

---

## 3. Методологии разработки × ИИ — как каждая реализуется

| Методология | Реализация с ИИ | Что меняется в DoD/CI/quality-gates | Подтверждённость |
|---|---|---|---|
| **TDD** | Тест пишется первым = точная исполняемая спецификация для LLM; малые проверяемые цели вместо «bloated implementation»; self-correction в цикле | DoD: тесты до кода; CI: mutation-score gate (не только line/branch coverage); GraphRAG+TDD −72/−81% failures | HIGH (DORA 2025 «amplifier»; arXiv:2603.17973) |
| **Spec-Driven Dev** | requirements.md/design.md/tasks.md (Kiro), constitution AGENTS.md; агент имплементит против контракта, не freeform-промпта | Spec-review gate; spec = контракт границ (НЕ замена кода как истины); 3–10× first-pass (vendor) | MEDIUM (мейнстрим инструментов; эффект — vendor) |
| **Peer code review** | AI-review как первый проход (Greptile 82%/CodeRabbit 44% catch), человек — второй; AI генерит код «с unknown flaws» → review нужнее | Обязательный human-review остаётся; AI-review не заменяет, дополняет; учитывать FP-noise | HIGH (greptile.com 2025-07; SO 2025) |
| **Pair / ensemble** | AI частично играет «навигатора»; парность опциональнее, точечнее, tool-assisted | Пара — для high-context/critical, не рутины | MEDIUM (medium @pravir.raghu 2025) |
| **Trunk-based + CI/CD** | Частые мелкие коммиты + AI; высокий throughput требует автоматических gates | Gates: mutation, security-scan AI-кода, flaky/детерминизм-gate, approval перед prod | HIGH (DORA 2025 stability↓) |
| **Agile/Scrum, управление командой** | Церемонии сохраняются; planning учитывает «70%-проблему» (оценка ≠ ощущение, см. METR perception-gap) | Estimation на данных, не на «AI ускорит»; ownership/accountability явно за людьми | HIGH (DORA 2025; METR) |
| **Waterfall-остатки** | Spec-up-front частично резонирует с SDD, но essential-complexity всё равно итеративна (Brooks) | — | MEDIUM |

**Какие методологии лучше «ложатся» на ИИ (явный ответ):** **TDD — №1** (тест = спецификация, быстрый детерминированный feedback-loop — именно то, что нужно агенту: DORA 2025 + arXiv:2603.17973). Близко — **spec-driven development** (контракт вместо freeform-промпта, мейнстрим инструментов 2025-26, но эффект-числа vendor). **Trunk-based + строгие CI quality-gates** — необходимое дополнение (компенсирует падение stability). Хуже всего ложится «freeform vibe coding без тестов/спеки/гейтов» — именно отсюда большинство failure-кейсов.

---

## 4. Параллели и различия: AI-разработка vs человеческая

| Аспект | Человек | AI | Вывод |
|---|---|---|---|
| Скорость | Стабильно-предсказуемо | +55% (изолир. задача) … −19% (эксперт, легаси) | Контекстно-зависимо, не универсально |
| Ошибки | Усталость, опечатки, забывчивость | Уверенные галлюцинации, «почти правильно», CWE-паттерны | AI-ошибки опаснее (ложная уверенность) |
| Доверие | Калибруется опытом | Падает с опытом наблюдателя (SO: trust 70→60) | Зрелость = осторожность |
| Ревью | Peer-review норма | Нужен ЧЕЛОВЕЧЕСКИЙ ревью AI-кода | Review не отмирает — усиливается |
| Ответственность | Несёт инженер/команда | Не несёт (агент «лжёт», 95/100 self-rating) | Accountability не делегируется |
| Обучение junior | Через практику/менторство | Делегирование → −17% навык (Anthropic) | Нужен learning-mode, ручная практика |
| Управление | Brooks: команды/дизайн/коммуникация | Амплифицирует, не отменяет: консеквенции **ускоряются** | Методики уточняются, не исчезают |

**Brooks / Mythical Man-Month — актуальность (явно подтверждено):** AI бьёт **accidental** complexity (boilerplate, рутинный debug, доки), НЕ **essential** («The hardest single part of building a software system is deciding precisely what to build»). AI убирает «трение» ручного кода, которое было естественным тормозом плохого дизайна → плохие практики коллапсируют быстрее/масштабнее. Brooks's Law под агентами обсуждается (blog.forret.com «Mythical Agent-Month», 2025-10). DORA-консенсус: «AI doesn't fix a team; it amplifies what's already there». Источники: en.wikipedia.org/Mythical_Man-Month; newsletter.pragmaticengineer.com «Revisiting No Silver Bullets»; blog.forret.com (2025-10). **Confidence: HIGH** (концептуально устойчиво, yearly+).

---

## 5. Documentation-as-code — уровень подтверждённости

**Вердикт: ЧАСТИЧНО подтверждается (MEDIUM).**
- **Подтверждено (HIGH для факта стандарта):** AGENTS.md формализован авг 2025 (OpenAI/Google/Cursor/Factory/Sourcegraph), 20k→40k+ репо к концу 2025, native в Copilot/Codex/Cursor/Jules/Gemini/Factory/Amp/Windsurf/Zed/RooCode. CLAUDE.md/constitution как «project constitution». Машиночитаемый контекст автоматически инжектится агенту. SKILL.md, AAIF-консорциум (дек 2025). Источник: infoq.com 2025-08; agents.md; arXiv:2510.21413.
- **Слабо подтверждено / vendor-overclaim:** «спека = единственный source of truth» — SDD-практики сами говорят **«code remains the source of truth»**; 3–10× first-pass — early-adopter/vendor reports, не независимое исследование.

**Формулировка для лекции:** docs-as-code усиливается **как машиночитаемый контекст для агентов** (де-факто стандарт с авг 2025) — подтверждается; тезис «документация замещает код как истину» — пока vendor-claim, честно помечать «слабо подтверждено».
