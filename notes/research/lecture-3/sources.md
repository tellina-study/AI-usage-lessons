# Lecture 3 — Sources — AI-System Architectures (agents, RAG, API)

**Date compiled:** 2026-05-16
**Researcher:** fact-checker subagent (deep-research pass, issue #87)
**Purpose:** грунт для plan-v1 + chapter (Лекция 3 — Архитектуры AI-систем: когда применять и когда НЕ применять)
**Audience:** студенты-инженеры 3 курса (универсальная аудитория)
**Today:** 2026-05-16

> Freshness flags: `STABLE` (conceptual, yearly+), `QUARTERLY` (market/adoption), `MONTHLY` (tool/product features), `VERIFY-ON-DAY` (younger than ~1 month OR weekly-cadence metric used as a hard number).

---

## A. Primary vendor / canonical engineering sources (HIGH confidence)

| # | URL | Author/Publisher | Date | Type | Freshness |
|---|-----|------------------|------|------|-----------|
| A1 | https://www.anthropic.com/research/building-effective-agents | Anthropic (Engineering) | 2024-12-19 | Vendor engineering guide | STABLE |
| A2 | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | Anthropic (Engineering) | 2025-09-29 | Vendor engineering guide (released w/ Sonnet 4.5) | STABLE |
| A3 | https://www.anthropic.com/engineering/multi-agent-research-system | Anthropic (Engineering) | 2025-06-13 | Vendor engineering postmortem | STABLE |
| A4 | https://cognition.ai/blog/dont-build-multi-agents | Walden Yan, Cognition AI | 2025-06-12 | Vendor opinion (counterpoint to A3) | STABLE |
| A5 | https://www.anthropic.com/research/reasoning-models-dont-say-think | Anthropic (Alignment Science) | 2025-04 | Research summary | STABLE |
| A6 | https://assets.anthropic.com/m/71876fabef0f0ed4/original/reasoning_models_paper.pdf | Chen, Benton et al., Anthropic | 2025-04 | Research paper (PDF) | STABLE |
| A7 | https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention | Anthropic | 2026 (live doc) | Vendor policy doc | QUARTERLY |
| A8 | https://openai.com/index/response-to-nyt-data-demands/ | OpenAI | 2025-06 | Vendor statement | STABLE (historical) |
| A9 | https://openai.com/index/fighting-nyt-user-privacy-invasion/ | OpenAI | 2025 | Vendor statement | STABLE (historical) |
| A10 | https://developers.openai.com/api/docs/guides/your-data | OpenAI | 2026 (live doc) | Vendor policy doc | QUARTERLY |
| A11 | https://cookbook.openai.com/examples/fine_tuning_direct_preference_optimization_guide | OpenAI Cookbook | 2025 | Vendor guide (SFT/DPO/RFT) | STABLE |
| A12 | https://platform.openai.com/docs/guides/reinforcement-fine-tuning | OpenAI | 2025-26 (live doc) | Vendor guide | STABLE |
| A13 | https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation | Anthropic | 2025-26 | Vendor / governance announcement | QUARTERLY |
| A14 | https://www.microsoft.com/en-us/research/blog/graphrag-new-tool-for-complex-data-discovery-now-on-github/ | Microsoft Research | 2024-07 | Vendor research blog | STABLE |

## B. Academic / arXiv (HIGH confidence)

| # | URL | Author/Publisher | Date | Type | Freshness |
|---|-----|------------------|------|------|-----------|
| B1 | https://arxiv.org/abs/2210.03629 | Yao et al. (ReAct) | 2022-10 (ICLR 2023) | Peer-reviewed paper | STABLE |
| B2 | https://arxiv.org/abs/2404.16130 | Edge et al., Microsoft (GraphRAG) | 2024-04 | arXiv paper | STABLE |
| B3 | https://arxiv.org/abs/2308.08747 | Luo et al. (catastrophic forgetting in LLM continual FT) | 2023-08 | arXiv paper | STABLE |
| B4 | https://arxiv.org/html/2601.18699v1 | (Mechanistic analysis of catastrophic forgetting) | 2026-01 | arXiv preprint | VERIFY-ON-DAY (recent, preprint) |
| B5 | https://arxiv.org/html/2503.00353v1 | U-NIAH (unified RAG + LLM long-context eval) | 2025-03 | arXiv / ACM TOIS | STABLE |
| B6 | https://research.trychroma.com/context-rot | Chroma Research | 2025 | Industry research report | STABLE |
| B7 | https://arxiv.org/abs/2603.22489 | (MCP threat modeling, tool poisoning) | 2026 | arXiv preprint | VERIFY-ON-DAY (recent preprint, future-dated id) |
| B8 | https://arxiv.org/html/2601.06007v2 | (Prompt caching for long-horizon agentic tasks) | 2026-01 | arXiv preprint | VERIFY-ON-DAY (recent preprint) |

## C. Failure cases / incidents / legal (HIGH–MEDIUM confidence)

| # | URL | Author/Publisher | Date | Type | Freshness |
|---|-----|------------------|------|------|-----------|
| C1 | https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot | McCarthy Tétrault (law firm) | 2024-02 | Legal analysis (Moffatt v. Air Canada) | STABLE |
| C2 | https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/ | American Bar Association | 2024-02 | Legal analysis | STABLE |
| C3 | https://news.bloomberglaw.com/ip-law/openai-must-turn-over-20-million-chatgpt-logs-judge-affirms | Bloomberg Law | 2025-11 | News (NYT v. OpenAI, 20M logs) | STABLE (historical) |
| C4 | https://natlawreview.com/article/openai-loses-privacy-gambit-20-million-chatgpt-logs-likely-headed-copyright | National Law Review | 2025-11 | Legal analysis | STABLE (historical) |
| C5 | https://medium.com/@sattyamjain96/the-agent-that-burned-4-200-in-63-hours-a-production-ai-postmortem-d38fd9586a85 | Sattyam Jain | 2026-04-14 | Engineering postmortem | VERIFY-ON-DAY (recent, single-author blog — MEDIUM confidence) |
| C6 | https://authzed.com/blog/timeline-mcp-breaches | AuthZed | 2026 (running timeline) | Security timeline (aggregator) | QUARTERLY |
| C7 | https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/ | Simon Willison | 2025-04-09 | Expert analysis | STABLE |
| C8 | https://www.docker.com/blog/mcp-horror-stories-github-prompt-injection/ | Docker | 2025 | Vendor security writeup (GitHub MCP) | STABLE |
| C9 | https://unit42.paloaltonetworks.com/model-context-protocol-attack-vectors/ | Palo Alto Unit 42 | 2025 | Security research | STABLE |
| C10 | https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/ | Fortune (citing MIT NANDA) | 2025-08-18 | News on MIT report | STABLE |
| C11 | https://cursor.com/blog/june-2025-pricing | Cursor (Anysphere) | 2025-07-04 | Vendor apology / pricing | STABLE (historical) |
| C12 | https://www.fintechweekly.com/magazine/articles/cursor-pricing-change-user-backlash-refund | FinTech Weekly | 2025-07 | News (Cursor backlash) | STABLE |
| C13 | https://www.cio.com/article/190888/5-famous-analytics-and-ai-disasters.html | CIO | 2024-25 | News roundup (DPD, Chevrolet, NYC MyCity, Zillow, iTutor) | STABLE |
| C14 | https://www.theverge.com/2024/3/29/24117417/nyc-google-microsoft-chatbot-myCity-incorrect-information | The Verge / AP coverage (see also CIO C13) | 2024-03 | News (NYC MyCity) | STABLE |

## D. Analysis / industry secondary (MEDIUM confidence — corroborate before quoting numbers)

| # | URL | Author/Publisher | Date | Type | Freshness |
|---|-----|------------------|------|------|-----------|
| D1 | https://towardsdatascience.com/agentic-rag-failure-modes-retrieval-thrash-tool-storms-and-context-bloat-and-how-to-spot-them-early/ | Towards Data Science | 2026 | Analysis (agentic-RAG failure modes) | QUARTERLY |
| D2 | https://www.kore.ai/blog/seven-rag-engineering-failure-points | Kore.ai (cites Barnett et al. arXiv:2401.05856) | 2024-25 | Analysis (7 RAG failure points) | STABLE |
| D3 | https://www.mindstudio.ai/blog/reliability-compounding-problem-ai-agent-stacks | MindStudio | 2025-26 | Analysis (reliability compounding) | STABLE |
| D4 | https://www.oreilly.com/radar/the-hidden-cost-of-agentic-failure/ | O'Reilly Radar | 2025-26 | Analysis (cost of agentic failure) | QUARTERLY |
| D5 | https://en.wikipedia.org/wiki/Model_Context_Protocol | Wikipedia | 2026 (live) | Encyclopedia (timeline/adoption) | QUARTERLY |
| D6 | https://www.pento.ai/blog/a-year-of-mcp-2025-review | Pento | 2025-12 | Analysis (MCP year-1 review) | QUARTERLY |
| D7 | https://introl.com/blog/prompt-caching-infrastructure-llm-cost-latency-reduction-guide-2025 | Introl | 2025 | Technical guide (prompt caching) | QUARTERLY |
| D8 | https://bigdataboutique.com/blog/fine-tuning-llms-when-rag-isnt-enough | BigData Boutique | 2026 | Analysis (FT vs RAG 2026) | QUARTERLY |
| D9 | https://www.redhat.com/en/topics/ai/rag-vs-fine-tuning | Red Hat | 2025-26 | Vendor-neutral explainer | STABLE |
| D10 | https://www.ibm.com/think/topics/rag-vs-fine-tuning | IBM | 2025-26 | Vendor-neutral explainer | STABLE |
| D11 | https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/graphrag-costs-explained-what-you-need-to-know/4207978 | Microsoft (Azure AI Foundry blog) | 2025 | Vendor cost analysis (GraphRAG) | QUARTERLY |
| D12 | https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models/ | Google Research | 2022-23 | Vendor research blog (ReAct) | STABLE |

---

## Confidence summary

- **HIGH:** A1–A14, B1–B3, B5–B6, C1–C4, C6–C9, C11–C13 (vendor/canonical, peer-reviewed, legal-of-record, security-of-record).
- **MEDIUM:** B4, B7, B8 (recent preprints), C5 (single-author postmortem — illustrative, anonymized), C10 (report methodology = interviews+survey, treat 95% as headline not precise), D-series (corroborate any hard number before putting on a slide).
- **VERIFY-ON-DAY items:** B4, B7, B8 (recent preprints), C5 (Apr 2026), C6 (running timeline — re-pull for newest incidents), plus any MCP download/registry count and market-share figure.

## Numbers that need re-verification on day of lecture

1. MCP monthly downloads (~97M Mar 2026) and registry server count (~9,400 Apr 2026) — adoption metric, **QUARTERLY/VERIFY-ON-DAY**, grows fast (D5/D6).
2. Latest MCP CVEs / breach timeline (C6) — running list, re-pull for newest.
3. Anthropic API retention = 7 days default; ZDR/flagged-content = up to 2 years; batch 29 days; code-exec containers 30 days (A7) — **QUARTERLY**, policy doc, re-fetch.
4. OpenAI API default retention 30 days; ZDR by approval (A10) — **QUARTERLY**, re-fetch; NYT-litigation preservation status (C3/C4) evolving.
5. Any "95% of GenAI pilots fail" framing — cite as MIT NANDA *State of AI in Business 2025*, report methodology, not a precise universal law (C10).
6. Prompt-caching discount/latency figures (up to 90% cost / 85% latency Anthropic; ~50% OpenAI auto) — vendor-published, **QUARTERLY** (A7/D7).
