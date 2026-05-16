# Lecture 4 — AI в разработке ПО — Sources

**Date:** 2026-05-16 · **Researcher:** fact-checker research subagent · **Issue:** #99
**Topic:** AI в разработке программного обеспечения (НЕ medicine — стэйл-файлы перемещены в `_stale-medicine-topic/`)
**Lecture-date assumed:** ~2026-05/06 (verify; freshness deltas vs 2026-05-16)

Freshness-флаги: **W**=weekly (VERIFY ON DAY OF LECTURE) · **Q**=quarterly · **M**=monthly · **Y**=yearly+ (стабильно)
Confidence: H=high (primary/peer-reviewed) · M=medium (vendor/press) · L=low (blog/aggregator/anecdote)

| # | URL | Автор/Издание | Дата | Тип | Fresh | Conf | Используется в |
|---|---|---|---|---|---|---|---|
| 1 | https://survey.stackoverflow.co/2025/ai | Stack Overflow | 2025-12 | Survey (primary) | Y | H | trends Q1/Q4; failures #11,#12 — 84% use, trust 70→60, distrust 46>33, «highly trust» 3.1%, «almost right» 66% |
| 2 | https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/ | Stack Overflow press | 2025-12 | Press | Y | H | trust «all-time low» формулировка |
| 3 | https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ | METR | 2025-07-10 | Study (primary) | Y | H | trends Q1(г); failures #10 — −19% slowdown, n=16/246, perception-gap |
| 4 | https://arxiv.org/abs/2507.09089 | METR (Becker et al.) | 2025-07 | arXiv | Y | H | METR primary paper |
| 5 | https://metr.org/blog/2026-02-24-uplift-update/ | METR | 2026-02-24 | Update | Q | H | late-2025 −18%/−4% «unreliable signal», selection bias |
| 6 | https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report | Google Cloud / DORA | 2025-09-23 | Report (primary) | Y | H | trends Q3/Q4; failures #17 — adoption 90%, stability↓, «amplifies» |
| 7 | https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf | DORA 2025 PDF | 2025-09 | Report PDF | Y | H | n~5000, 7 capabilities |
| 8 | https://dora.dev/research/2024/dora-report/ | DORA 2024 | 2024 | Report | Y | H | прошлогодний baseline |
| 9 | https://cloud.google.com/discover/how-test-driven-development-amplifies-ai-success | Google Cloud / DORA | 2025 | Article | Y | H | TDD amplifies AI |
| 10 | https://www.helpnetsecurity.com/2025/04/14/package-hallucination-slopsquatting-malicious-code/ | Help Net Security | 2025-04-14 | News | Y | H | failures #6 — 576k samples, ~20%, 21.7%/5.2% (число сэмплов исправлено 756k→576k v1.1, транспозиция) |
| 11 | https://en.wikipedia.org/wiki/Slopsquatting | Wikipedia | 2025+ | Encyclopaedia | Y | M | термин, Seth Larson PSF апр 2025 |
| 12 | https://nesbitt.io/2025/12/10/slopsquatting-meets-dependency-confusion.html | Andrew Nesbitt | 2025-12-10 | Blog | Q | M | slopsquatting × dependency-confusion |
| 13 | https://arxiv.org/html/2512.08213 | UTSA et al. | 2025-12 | arXiv | Y | H | package hallucination quantized LLMs |
| 14 | https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/ | Fortune | 2025-07-23 | News | Y | H | failures #1 — Replit prod-БД |
| 15 | https://incidentdatabase.ai/cite/1152/ | AI Incident DB | 2025-07 | Incident DB | Y | H | Replit Incident 1152 |
| 16 | https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/ | The Register | 2025-07-21 | News | Y | H | Replit детали |
| 17 | https://www.fastcompany.com/91372483/replit-ceo-what-really-happened-when-ai-agent-wiped-jason-lemkins-database-exclusive | Fast Company | 2025 | News | Y | M | Replit CEO версия |
| 18 | https://www.ruh.ai/blogs/amazon-kiro-ai-outage-ai-governance-failure | ruh.ai | 2026 | Analysis | Q | M | failures #2 — Kiro 13ч outage |
| 19 | https://particula.tech/blog/ai-agent-production-safety-kiro-incident | particula.tech | 2026 | Analysis | Q | M | Kiro safety-lessons |
| 20 | https://medium.com/codetodeploy/when-ai-writes-the-code-a-deep-dive-into-amazons-2026-ai-linked-outages-434ffd85a0d2 | Medium/CodeToDeploy | 2026-03 | Blog | Q | L | Amazon 2026 outages контекст |
| 21 | https://www.euronews.com/next/2026/04/28/an-ai-agent-deleted-a-companys-entire-database-in-9-seconds-then-wrote-an-apology | Euronews | 2026-04-28 | News | Q | M | failures #3 — PocketOS/Cursor 9 сек |
| 22 | https://zenity.io/blog/current-events/ai-agent-database-deletion-pocketos | Zenity | 2026-04 | Analysis | Q | M | PocketOS детали |
| 23 | https://medium.com/@bruvajc/the-biggest-ai-disasters-of-2025-and-why-many-are-likely-to-repeat-in-2026-aa71bb0be4af | Medium/@bruvajc | 2026-02 | Aggregator | Q | L | failures #4 — агрегатор 10+ инцидентов (rm -rf ~/) |
| 24 | https://thenewstack.io/curls-daniel-stenberg-ai-is-ddosing-open-source-and-fixing-its-bugs/ | The New Stack | 2025/26 | News | Y | H | failures #5 — curl AI-slop |
| 25 | https://www.theregister.com/2026/01/21/curl_ends_bug_bounty/ | The Register | 2026-01-21 | News | Y | H | curl закрытие bug-bounty |
| 26 | https://socket.dev/blog/curl-shuts-down-bug-bounty-program-after-flood-of-ai-slop-reports | Socket | 2026-01 | Analysis | Y | H | curl valid-rate <5% |
| 27 | https://www.legitsecurity.com/blog/camoleak-critical-github-copilot-vulnerability-leaks-private-source-code | Legit Security | 2025-10 | Sec research | Y | H | failures #7 — CamoLeak CVE-2025-59145 CVSS 9.6 |
| 28 | https://securityboulevard.com/2025/10/saas-security-alert-camoleak-prompt-injection-in-github-copilot-chat-enables-private-code-secret-exfiltration/ | Security Boulevard | 2025-10 | Sec news | Y | H | CamoLeak механизм |
| 29 | https://thenextweb.com/news/lovable-vibe-coding-security-crisis-exposed | TNW | 2026 | News | Q | M | failures #8 — Lovable CVE-2025-48757, RLS |
| 30 | https://www.theregister.com/2026/02/27/lovable_app_vulnerabilities/ | The Register | 2026-02-27 | News | Q | H | Lovable 18k users / Moltbook |
| 31 | https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-generated-code-vulnerability-surge-2026/ | Cloud Security Alliance | 2026 | Research note | Q | M | AI-CVE surge, 40–62% vuln |
| 32 | https://getautonoma.com/blog/vibe-coding-failures | getautonoma | 2026 | Blog | Q | L | failures #9 — Tea App, агрегатор |
| 33 | https://www.gitclear.com/ai_assistant_code_quality_2025_research | GitClear | 2025-02 | Research | Y | H | failures #13 — 211M LOC, copy-paste 8.3→12.3, refactor 24.1→9.5 |
| 34 | https://gitclear-public.s3.us-west-2.amazonaws.com/GitClear-AI-Copilot-Code-Quality-2025.pdf | GitClear PDF | 2025-02 | Report PDF | Y | H | GitClear primary PDF |
| 35 | https://dl.acm.org/doi/10.1145/3716848 | ACM TOSEM | 2025 | Peer-reviewed | Y | H | failures #14 — Copilot security empirical |
| 36 | https://arxiv.org/abs/2108.09293 | Pearce, Ahmad, Tan, Dolan-Gavitt, Karri (NYU) | 2022 (IEEE S&P) | arXiv | Y | H | NYU «Asleep at the Keyboard?» ~40% vuln 89 scenarios CWE-79/89/798/22 (arXiv ID исправлен 2310.02059→2108.09293 v1.1: 2310.02059 = Fu et al., чужая статья) |
| 37 | https://arxiv.org/abs/2510.26103 | Schreiber & Tippe | 2025-10-30 | arXiv | Y | H | failures #15 — 7703 файла, 12.1% CWE, Python 16-18.5% |
| 38 | https://www.anthropic.com/research/AI-assistance-coding-skills | Anthropic | 2026-02 | Research (primary) | Y | H | failures #16 — n=52 junior, −17% |
| 39 | https://arxiv.org/pdf/2601.20245 | Shen & Tamkin (Anthropic) | 2026-02-03 | arXiv | Y | H | Anthropic «How AI Impacts Skill Formation» primary, n=52 junior −17%, >60%/≥65% split, Trio (название статьи уточнено v1.1) |
| 40 | https://www.infoq.com/news/2026/02/ai-coding-skill-formation/ | InfoQ | 2026-02 | News | Y | H | Anthropic study coverage |
| 41 | https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/ | GitHub | 2022 | Research | Y | H (vendor) | trends Q1(а) — +55% lab RCT |
| 42 | https://arxiv.org/abs/2302.06590 | Peng/GitHub et al. | 2023-02 | arXiv | Y | H | Copilot +55% primary, CI[21,89] |
| 43 | https://mit-genai.pubpub.org/pub/v5iixksv | MIT GenAI | 2024 | Field exp | Y | H | MS/Accenture +7.5–21.8% PR/нед, n=1974 |
| 44 | https://addyo.substack.com/p/the-70-problem-hard-truths-about | Addy Osmani (Google) | 2024-12 | Essay | Y | M | trends Q1(б) — «70%-проблема» |
| 45 | https://addyo.substack.com/p/the-80-problem-in-agentic-coding | Addy Osmani | 2025 | Essay | Y | M | «80%-проблема» обновление |
| 46 | https://zed.dev/blog/ai-70-problem-addy-osmani | Zed Blog | 2025 | Repost | Y | M | 70%-проблема cross-ref |
| 47 | https://www.swebench.com/ | SWE-bench | 2026 | Leaderboard | **W** | H | SWE-bench Verified — VERIFY ON DAY |
| 48 | https://labs.scale.com/leaderboard/swe_bench_pro_public | Scale AI | 2026 | Leaderboard | **W** | H | SWE-bench Pro 64.3% — VERIFY ON DAY |
| 49 | https://www.marc0.dev/en/leaderboard | marc0.dev | 2026-05 | Leaderboard | **W** | M | GPT-5.5 88.7% (2026-04-23) — VERIFY ON DAY |
| 50 | https://blog.jetbrains.com/research/2026/04/which-ai-coding-tools-do-developers-actually-use-at-work/ | JetBrains Research | 2026-04 | Survey (primary) | Q | H | tools-landscape primary, n>10k |
| 51 | https://newsletter.pragmaticengineer.com/p/ai-tooling-2026 | Pragmatic Engineer | 2026 | Newsletter | Q | M | tools cross-check, tool-stacking |
| 52 | https://www.ideaplan.io/blog/ai-coding-assistant-market-share-2026 | ideaplan.io | 2026 | Market | Q | M | market $12.8B, CAGR |
| 53 | https://www.getpanto.ai/blog/cursor-ai-statistics | getpanto.ai | 2026 | Stats | Q | L | Cursor $2B ARR, >1M платящих |
| 54 | https://thenewstack.io/ai-coding-tool-stack/ | The New Stack | 2026 | Analysis | Q | M | tool-stacking Cursor+Claude Code |
| 55 | https://www.greptile.com/benchmarks | Greptile | 2025-07 | Benchmark | M | M (vendor) | code-review: Greptile 82%/CodeRabbit 44%/Graphite 6% |
| 56 | https://www.devtoolsacademy.com/blog/state-of-ai-code-review-tools-2025/ | DevTools Academy | 2025 | Survey | M | L | code-review landscape |
| 57 | https://corgea.com/blog/the-best-ai-powered-sast-in-2025/ | Corgea | 2025 | Vendor analysis | M | L | AI-SAST FPR-разброс |
| 58 | https://xygeni.io/blog/top-sast-tools/ | Xygeni | 2026 | Vendor analysis | M | L | SAST TP/FP сравнение (vendor-bias!) |
| 59 | https://semgrep.dev/products/semgrep-code/ | Semgrep | 2026 | Vendor | M | M | Semgrep Assistant −20% noise |
| 60 | https://docs.github.com/en/code-security/responsible-use/responsible-use-autofix-code-scanning | GitHub Docs | 2025-26 | Docs | M | H | Copilot Autofix responsible-use |
| 61 | https://www.pixee.ai/blog/best-sast-tools-2026 | Pixee | 2026 | Vendor | M | L | Pixee 76% merge-rate |
| 62 | https://dl.acm.org/doi/10.1145/3696630.3728544 | Meta (ACM FSE) | 2025 | Peer-reviewed | Y | H | TestGen-LLM mutation-guided |
| 63 | https://arxiv.org/pdf/2501.12862 | Foster/Meta et al. | 2025-01 | arXiv | Y | H | TestGen-LLM primary, 32% vs 5.3% / 2.4% vs 15% |
| 64 | https://arxiv.org/html/2506.02954v2 | MutGen authors | 2025-06 | arXiv | Y | H | mutation-guided test gen; источник чисел 32% vs 5,3% классов / 2,4% vs 15% мутантов (§4.1 — атрибуция перенесена с #63 на #64 v1.1); coverage слабый индикатор |
| 65 | https://arxiv.org/html/2602.08146 | AdverTest authors | 2026-02 | arXiv | Y | M | AdverTest +8.56%/+63.3% |
| 66 | https://www.diffblue.com/resources/java-unit-test-generator-comparison-diffblue-cover-vs-evosuite-vs-randoop-vs-squaretest/ | Diffblue | 2025-26 | Vendor | M | L | Diffblue bytecode-подход |
| 67 | https://www.microsoft.com/en-us/research/blog/systematic-debugging-for-ai-agents-introducing-the-agentrx-framework/ | Microsoft Research | 2025 | Research | Y | H | AgentRx +23.6% failure-localization |
| 68 | https://galileo.ai/blog/best-ai-agent-debugging-root-cause-analysis-tools | Galileo | 2025 | Vendor analysis | M | L | AI-debug limitations, Gartner >40% canceled 2027 |
| 69 | https://aws.amazon.com/blogs/migration-and-modernization/accelerate-your-mainframe-modernization-journey-using-ai-agents-with-aws-transform/ | AWS | 2025 | Vendor blog | Y | M | AWS Transform GA май 2025, COBOL→Java |
| 70 | https://press.aboutamazon.com/2024/12/new-amazon-q-developer-capabilities-accelerate-large-scale-transformations-of-legacy-workloads | Amazon press | 2024-12 | Press | Y | M | Amazon Q transform превью re:Invent 2024 |
| 71 | https://en.wikipedia.org/wiki/The_Mythical_Man-Month | Wikipedia | — | Encyclopaedia | Y | H | Brooks essential/accidental, No Silver Bullet |
| 72 | https://newsletter.pragmaticengineer.com/p/revisiting-no-silver-bullets-in-the | Pragmatic Engineer | 2025 | Essay | Y | M | No Silver Bullet в эпоху AI |
| 73 | https://blog.forret.com/2025/2025-10-26/mythical-agent-month/ | Peter Forret | 2025-10-26 | Blog | Y | M | Brooks's Law под агентами |
| 74 | https://www.infoq.com/news/2025/08/agents-md/ | InfoQ | 2025-08 | News | M | H | AGENTS.md формализован авг 2025, 20k+ репо |
| 75 | https://agents.md/ | AGENTS.md | 2025-26 | Spec site | M | H | AGENTS.md спецификация |
| 76 | https://arxiv.org/html/2510.21413v1 | Context-eng authors | 2025-10 | arXiv | Y | M | context engineering OSS |
| 77 | https://intuitionlabs.ai/articles/agentic-ai-foundation-open-standards | IntuitionLabs | 2025-26 | Analysis | M | L | AAIF дек 2025 (MCP+Goose+AGENTS.md) |
| 78 | https://blog.mean.ceo/the-solo-founder-ai-agent-stack-that-is-replacing-entire-startup-teams/ | mean.ceo | 2026 | Blog | Q | L | solo+AI стоимость $300-500 vs $80-120k |
| 79 | https://www.taskade.com/blog/one-person-companies | Taskade | 2026 | Blog | Q | L | 36.3% solo-founded 2026, Levels/Broca |
| 80 | https://www.loadsys.com/blog/spec-driven-development-ai-teams/ | Loadsys | 2026 | Blog | Q | L | SDD «ломается» team-переход |
| 81 | https://www.infoworld.com/article/4171332/four-cutting-edge-tools-for-spec-driven-development.html | InfoWorld | 2026 | Analysis | M | M | SDD-инструменты Kiro/SpecKit/Tessl |
| 82 | https://github.com/gotalab/cc-sdd | gotalab (GitHub) | 2026 | Repo/docs | M | M | «code remains source of truth» — docs-as-code оговорка |
| 83 | https://arxiv.org/html/2603.17973v1 | TDAD authors | 2026-03 | arXiv | N | M | НЕ цитируется в v1.1: arXiv:2603.17973 = «TDAD: Test-Driven Agentic Development» (регрессии 6.08→1.82%, ~70%), НЕ «GraphRAG+TDD −72/−81% peer-review» — была misattribution. §5.1 теперь ведёт структурным аргументом (тест=исполн. спека §1.5 + детерм. feedback-loop), источник = DORA «How TDD Amplifies AI Success» (#9) |

**Итого: 83 источника.** HIGH: ~38 · MEDIUM: ~28 · LOW: ~17.
**Weekly (VERIFY ON DAY OF LECTURE):** #47, #48, #49 (все SWE-bench/leaderboard).
**Quarterly (refresh при близкой дате):** #5, #18-23, #29-32, #50-54, #78-80 (market/adoption/recent incidents).
