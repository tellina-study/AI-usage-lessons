# Knowledge Base Index

> Last compiled: 2026-04-07 (topic→lecture mapping actualized vs RPD canon 2026-05-16) | Sources: 47 indexed (16 exports + 10 research + 6 course research + 15 papers) | Ontology: 293 triples

## Course Structure

- 17-lecture RPD canon: [`library/project/course-plan.md`](../library/project/course-plan.md)
- [Lectures](lectures/) -- produced: lec-01, lec-02, lec-03, lec-07; remaining (lec-04, 05, 06, 08-17) planned
- [Documents](documents/) -- 16 Google Drive exports cataloged
- [Papers](papers/) -- 15 academic PDFs downloaded (Lecture 1)

## Topics

### AI Fundamentals (45+ sources)
Classification taxonomies, history, definitions, benchmarks, human vs AI capabilities.
Lectures: 1 (primary, produced), 2 (produced); revisited across industry lectures 4-17 via LO1
Primary: [notes/research/lecture-1/classifications.md](../notes/research/lecture-1/classifications.md) (9 taxonomies, 25+ papers)
-> [Topic index](topics/ai-fundamentals/_index.md)

### AI Agents (30+ sources)
Definitions, architectures (ReAct, Toolformer), frameworks (Anthropic, Google, LangChain), autonomy levels.
Lectures: 3 (primary -- "Архитектуры AI-систем: агенты, RAG, API", produced), 1 (brief overview)
Primary: [notes/research/lecture-1/model-chat-agent-app.md](../notes/research/lecture-1/model-chat-agent-app.md)
-> [Topic index](topics/ai-agents/_index.md)

### AI Ethics and Regulation (12+ sources)
Bias, fairness, transparency, regulatory frameworks, responsible AI.
Cross-cutting theme (LO3/LO8), no dedicated lecture -- addressed in industry context (e.g. L5, L7, L15), systematized in L17
-> [Topic index](topics/ai-ethics/_index.md)

### AI in Software Development (15+ sources)
AI-assisted coding, testing, DevOps, CI/CD integration.
Lectures: 4 (primary, planned)
-> [Topic index](topics/ai-in-software/_index.md)

### AI in Finance and Retail (10+ sources)
Banking, insurance, trading, retail analytics.
Lectures: 5 (primary, planned)
-> [Topic index](topics/ai-in-finance/_index.md)

### AI in Medicine (8+ sources)
Diagnostics, drug discovery, clinical decision support.
Lectures: 7 (primary, produced)
-> [Topic index](topics/ai-in-medicine/_index.md)

### AI in Manufacturing and Agriculture (6+ sources)
Production optimization, precision agriculture, supply chain.
Lectures: 11 (primary, planned); related: 10 (agriculture), 12 (automation & digital twins)
-> [Topic index](topics/ai-in-manufacturing/_index.md)

### AI in Government and Education (6+ sources)
Public services, smart cities, regulatory compliance.
⚠ Нет выделенной лекции в актуальном РПД (legacy topic, prior course structure) -- pending owner decision
-> [Topic index](topics/ai-in-government/_index.md)

### AI in Creative Industries (6+ sources)
Media, art, music, content generation.
Lectures: 8 (primary, planned)
-> [Topic index](topics/ai-in-creative/_index.md)

### Prompt Engineering (cross-cutting)
Skill progression across course: Role+Task+Context -> PARTS -> chain-of-thought.
Cross-cutting -- micro-exercises in all 17 lectures, systematized in L17 (no standalone lecture)
-> [Topic index](topics/prompt-engineering/_index.md)

## Learning Outcomes

LO descriptions and lecture mapping per RPD canon ([`course-plan.md`](../library/project/course-plan.md) §Покрытие LO). Assessment (seminar) column ⚠ not re-verified against current RPD seminar plan — pending owner check.

| Code | Description | Lectures (canon) | Assessment ⚠ |
|------|-------------|------------------|--------------|
| LO1 | Классифицировать типы AI-решений и сопоставить их с задачами индустрий | 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16 | Sem 5, 10, 17 |
| LO2 | Оценить применимость AI-решения к конкретной бизнес-задаче | 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16 | Sem 5, 10, 17 |
| LO3 | Проанализировать риски AI-систем: безопасность данных, ограничения, уязвимости | 5, 7, 9, 14, 16 | Sem 5, 10, 17 |
| LO4 | Применить AI-инструменты для решения типовой аналитической задачи | 1, 3, 4, 8, 15 | Sem 1, 17 |
| LO5 | Сформулировать обоснованное заключение о перспективах AI в индустрии | 8, 10, 12, 15 | Sem 10, 17 |
| LO6 | Выявить типичные ошибки и ограничения AI-систем | 1, 2, 5, 7, 15 | Sem 1, 17 |
| LO7 | Обосновать выбор архитектуры AI (чат, агент, RAG, API, модель) | 2, 3, 4, 6, 9, 11, 12, 13, 14, 16 | Sem 17 |
| LO8 | Определить роль человека и AI в совместной работе: human-in-the-loop | 7, 11, 15 | Sem 17 |

## Normative Requirements

| Code | Description | Learning Outcomes |
|------|-------------|-------------------|
| PKS-3 | Classify and identify AI tasks | LO1, LO2, LO4, LO5 |
| PKS-4 | Evaluate ethical and social implications | LO3, LO6, LO7, LO8 |

## Compilation Log

- 2026-04-07: Phase 1 complete — RAG expanded to 47 files, ontology loaded (293 triples)
- 2026-04-07: Phase 2 — ontology populated with 8 lectures, 8 LOs, 2 requirements, 4 seminars; wiki index created
- 2026-04-07: Phase 4 — cross-links resolved (0 [[wiki-links]] remaining), backlinks + related topics added to all 11 pages, link validation passed
- 2026-04-07: #22 — ontology enriched (389 triples, 17 concepts), RAG expanded (61 docs), /query-kb skill created
- 2026-04-07: #23 — final tests: 7 manual tool calls for 3 scenarios (was 53 baseline)
- 2026-04-07: #24 — roast complete, pre-commit hook + post-compile automation added
- 2026-05-16: #97 п.3 — topic→lecture mapping actualized vs RPD canon (17 lectures); produced statuses set for L1/L2/L3/L7; ai-ethics & prompt-engineering reframed as cross-cutting; ai-in-government flagged ⚠ outdated (no dedicated lecture in current RPD, pending owner decision)
