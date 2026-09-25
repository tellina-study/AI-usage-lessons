---
lecture: 5
title: "Глава 5 — Источники и дальнейшее чтение"
status: draft
version: v1
cross_ref: "Часть 1 — chapter.md (§0, Раздел 1). Часть 2 — chapter-part2.md (Раздел 2, 3). Часть 3 — chapter-part3.md (Раздел 4, 5). Часть 4 — chapter-part4.md (Раздел 6). Часть 5 — chapter-part5.md (Раздел 7, Заключение, Q&A backup, Глоссарий)."
---

# Глава 5 — Источники и дальнейшее чтение

> **Что это за файл.** Это справочный аппарат главы — полный список источников и рекомендаций для дальнейшего чтения, вынесенный из Части 5 (`chapter-part5.md`) в отдельный файл (issue #212, структурная правка). Глава физически остаётся пятичастной (`chapter.md` + `chapter-part2.md` … `chapter-part5.md`); этот файл — приложение к ней, не «Часть 6», и не входит в измеряемое тело главы (библиография по определению не может быть контентом про провалы/ограничения/альтернативы — правило курса уже исключает источники из подсчёта объёма главы, см. `CLAUDE.md` § «Chapter Depth Baseline»). Глоссарий остался в `chapter-part5.md` — определения читает студент, это не аппарат.

## Источники

Все источники сверены с research-досье (`notes/research/lecture-5-pdlc/`), дата обращения — 2026-09-06, если не указано иное. Источники 1–40 — из первоначального драфта главы (Части 1–4); источники 41–58 добавлены при доведении главы до паритета с Лекцией 4 (issue #212, Deep-dive box'ы и Раздел 7) и сверены отдельно, дата обращения — 2026-09-25, если не указано иное. Источники 59–61 добавлены отдельной правкой (issue #212, структурная правка) для провала #3 IBM Watson Health (§1.9, Часть 1), у которого не было собственной записи в списке несмотря на подробный разбор в теле главы; сверены поиском 2026-09-25.

**Классика (петля, discovery, design, эксперимент, SRE)**
1. Blank, S. *The Four Steps to the Epiphany* (2003); Lean LaunchPad, Stanford/Berkeley (2011). Customer Development, «no facts inside your building».
2. Fitzpatrick, R. *The Mom Test* (2013). 3 правила интервью.
3. Torres, T. *Continuous Discovery Habits* (2021); producttalk.org — opportunity-solution tree, two-step synthesis, AI «raises the floor».
4. UK Design Council. *The Double Diamond* (2003–2005). Brown, T. «Design Thinking», HBR (2008).
5. Nielsen, J. 10 usability heuristics (1994, ред. 2020); «you are not the user»; 5 users ≈85% / 1 user ≈31% problems.
6. Ries, E. *The Lean Startup* (2011). MVP/BML.
7. Cooper, R. *Winning at New Products* (термин Stage-Gate в печати 1988).
8. Kohavi, R., Tang, D., Xu, Y. *Trustworthy Online Controlled Experiments*, CUP (2020); Kohavi & Thomke, «The Surprising Power of Online Experiments», HBR (сент.–окт. 2017) — Bing ≈$100M / +12%.
9. Spool, J. «The Back Story for the $300 Million Button», UIE (17 окт. 2011) — usability-редизайн, НЕ RCT (для контраста с Bing).
10. Fabijan, A. и др. «Diagnosing Sample Ratio Mismatch», KDD 2019 (Microsoft) — SRM, «fever is a symptom».
11. McClure, D. «Startup Metrics for Pirates» (2007) — AARRR. Rodden, K. и др. HEART, Google Research (2010). Ellis, S. — North Star Metric.
12. Google SRE. *Site Reliability Engineering* (2016) + SRE Workbook — SLI/SLO/error budget, «changes ~70% of outages».

**AI-эра (инструменты, evals, LLMOps, governance)**
13. Anthropic. *2026 Agentic Coding Trends Report* (янв. 2026) — сжатие стадий разработки, agent teams `[SECONDARY, триангулировано]`. Cherny, B. (инженер Anthropic), публичное заявление, 9 марта 2026 — код на инженера «+200% в этом году» (оригинал: up 200% this year; заявление не уточняет точное окно сравнения, поэтому не пересказывается как строгий двенадцатимесячный year-over-year период). Anthropic, анонс инструмента «Code Review» (~10 марта 2026; независимо подтверждено InfoQ, 17 апр. 2026) — содержательные комментарии человеческого ревью: 16%→54% после внедрения.
14. Bain & Company. *The Rise of the AI Development Life Cycle* (2026) — continuous flow, bottleneck displacement, «human review at critical junctures».
15. Reganti, A. & Badam, K. «Why your AI product needs a different development lifecycle», Lenny's Newsletter (19 авг. 2025) — CC/CD, agency-ladder, «not ready to give it high agency».
16. Weil, K. Lenny's Podcast (10 апр. 2025) — «writing evals is going to become a core skill». Husain, H. hamel.dev — 3-level eval framework.
17. Anthropic. «Demystifying evals for AI agents» (9 янв. 2026) — pass@k vs pass^k, grader types, 8-step roadmap.
18. Zheng, L., Chiang и др. «Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena», NeurIPS 2023 (arXiv:2306.05685) — ~85%/~81% agreement.
19. DeepMind Safety. «Specification gaming: the flip side of AI ingenuity» (21 апр. 2020) — CoastRunners. Anthropic. «Sycophancy to Subterfuge» (arXiv:2406.10162, 14 июня 2024).
20. Perplexity Deep Research; Dovetail; v0 by Vercel; Figma Make; Google Stitch; bolt.new; Cursor; NVIDIA NeMo Guardrails; Guardrails AI; LangSmith/Langfuse/Arize Phoenix/Helicone — инструменты 2025–2026 `[VFY-day-of: версии]`.
21. NN/g. *State of UX 2026* (Moran, Budiu, Gibbons) — AI slop, technology-led design.
22. «Generated Inaccessible: Measuring WCAG Violations in AI UI Design Tools», ACM Web4All 2026 — 21 880 оценок, 29,0% соответствие `[FACT-CHECK]`.
23. Gartner. *Market Guide for Guardian Agents* (25 фев. 2026) — определение, adoption 70%/23%. Sber GigaCowork (CIPR-2026) `[VFY-day-of]`.
24. Deloitte. *2026 Global Technology Leadership Study — «From Operators to Orchestrators»* — 75% / 42% / 81%.
25. Sber. «AI-Disrupt PDLC» v1.0 (ЦИПР, 19 мая 2026) / v2.0 (~июль 2026) — intent/implementation loop, maturity 0–5, IDP-экономика, удалённые v1-цифры `[VFY-day-of]`.

**Провалы (13 кейсов)**
26. NN/g (Rosala & Moran). «Synthetic Users» (обновл. 21 июня 2024) — 3/7 vs 7/7, drone «game-changer».
27. Fortune (7 окт. 2025). Deloitte Australia A$440k / фабрикованные цитаты. Damien Charlotin, AI Hallucination Cases Database.
28. Washington Post (24 окт. 2024) + CBS News (янв. 2026). Character.AI / Sewell Setzer III.
29. EEOC (9 авг. 2023). iTutorGroup $365 000.
30. Forbes / AndroidPolice (май 2024). Google AI Overviews — eat rocks / glue on pizza.
31. CNBC (17 июня 2024). McDonald's × IBM drive-thru — ~100 из ~13 786 (≈0,7%).
32. WSJ «Facebook Files» (2021) / House E&C Committee record; Techdirt (28 окт. 2021, поправка «все реакции ×5»); CNN/The Hill.
33. Med-PaLM 2 (arXiv:2305.09617; Nature Medicine 2024) — 86,5% MedQA. *Mata v. Avianca* (S.D.N.Y., 22 июня 2023, санкция $5000) = ChatGPT. Magesh и др., Stanford RegLab (arXiv:2405.20362) — Lexis+ 17% / Westlaw 33% / GPT-4 88%.
34. GeekWire (нояб. 2021) + SEC 10-K FY2021. Zillow Offers — $304–408M, ~2000 (25%), ~$80k/дом.
35. CanLII / ABA (14 фев. 2024). *Moffatt v. Air Canada*, 2024 BCCRT 149 — $812,02.
36. Bloomberg (8 мая 2025) + Fortune (10 окт. 2025). Klarna — 700 FTE → разворот политики, 853 FTE. The Markup (29 марта 2024). NYC MyCity — 10/10. VentureBeat / AI Incident DB #622. Chevrolet «$1 Tahoe».
37. MIT NANDA (июль 2025) — «95%» / воронка 60→20→5 / COI `[FACT-CHECK]`. Fortune (18 авг. 2025). 80,000 Hours podcast. NewMR.
38. RAND. «The Root Causes of Failure for AI Projects» (RRA2680-1) — «80%» как хеджированная ссылка, «80,3%» = фабрикация точности (урок, НЕ цифра).
39. Gartner (7 апр. 2026, 782 I&O-лидеров; июнь 2025, 3400+); martech.org. S&P Global (окт. 2025) — 17%→42%. BCG AI Radar 2025, «From Potential to Profit: Closing the AI Impact Gap» (янв. 2025, опрос 1803 C-level руководителей, 19 стран, 12 отраслей) — 75%/25%/60% без финансового KPI; не путать с сентябрьским отчётом BCG «The Widening AI Value Gap: Build for the Future 2025» (n=1250) — другие заголовочные цифры (5%/35%/60%), см. врезку в §7.2 (Часть 5).
40. Business Standard / Retail Dive (3 апр. 2024). Amazon Just Walk Out — 700/1000 (цель 50/1000), 27 из 44 магазинов.

**Дополнительные источники (Deep-dive box'ы §1/§4/§5/§6 и синтез §0/§7, issue #212)**
41. Bainbridge, L. «Ironies of Automation», *Automatica*, 19(6), 775–779 (1983) — асимметрия автоматизации: мониторинг требует более высокой, не более низкой квалификации. (§0.5, Часть 1)
42. Argyris, C. & Schön, D. *Organizational Learning: A Theory of Action Perspective* (1978) — одиночная/двойная петля обучения. (§0.4, Часть 1)
43. Nielsen Norman Group. Rosala, K. «AI-Moderated Interviews: If, When, and How to Use Them» (30 янв. 2026), nngroup.com/articles/ai-interviewers — 3/10 «естественно», 5/10 «комфортно»; ограничение «не гонится за неожиданной находкой». (Deep-dive box, Раздел 1, Часть 1)
44. Sharma, M. и др. «Towards Understanding Sycophancy in Language Models», arXiv:2310.13548, ICLR 2024 — метрика feedback positivity (сдвиг позитивности ответа относительно нейтрального базового ответа), по пяти моделям (Claude 1.3, Claude 2, GPT-3.5, GPT-4, LLaMA 2): ≈72–91% при явном согласии пользователя, ≈7–28% при явном несогласии (Figure 1). (Deep-dive box, Раздел 1, Часть 1)
45. Christensen, C. *Competing Against Luck* (2016) — Jobs-to-be-Done, пример молочного коктейля McDonald's. (§1.2, Часть 1)
46. Ulwick, A. Outcome-Driven Innovation (ODI, с 1999) — метод JTBD switch-интервью. (§1.2, Часть 1)
47. Cagan, M. *Inspired* (2008, 2-е изд. 2017); «Product Risk Taxonomy», SVPG (10 июля 2023) — четыре риска (Value/Usability/Feasibility/Viability). Cagan, M. & Nika, M. «AI Product Management», SVPG (16 апр. 2024). (§1.2, Часть 1)
48. Huryn, P. Синтез пятого («этического») риска поверх четырёх рисков Кагана (2026) `[VFY-day-of]`. (§1.6, Часть 1)
49. Schneier, B. «Agentic AI's OODA Loop Problem», schneier.com (окт. 2025) — Observe/Orient из недоверенных входов, скорость как уязвимость. (§0.5, Часть 1)
50. Cronbach, L.J. & Meehl, P.E. «Construct Validity in Psychological Tests», *Psychological Bulletin* (1955). (Deep-dive box, §4.6, Часть 3)
51. Brunswik, E. (1940–1950-е); формулировка закреплена Орном, М. — ecological validity. (Deep-dive box, §4.6, Часть 3)
52. Alaa, A., Hartvigsen, T., Raji, D. и др. «Medical Large Language Model Benchmarks Should Prioritize Construct Validity», arXiv:2503.10694 (2025). (Deep-dive box, §4.6, Часть 3)
53. Atil, B., Baldwin, D. и др. «Non-Determinism of "Deterministic" LLM Settings», Eval4NLP 2025, arXiv:2408.04667 — до 15 п.п. разброса между прогонами, до 70 п.п. между лучшим и худшим. (§5.2 и Deep-dive box §5.2, Часть 3)
54. Braintrust (2026) — кейс Notion: рост throughput исправлений с 3 до 30 в день после systematic offline+online eval `[VFY-day-of]`. (§4.3, Часть 3)
55. McKinsey & Company / QuantumBlack. «Unlocking the value of AI in software development» (нояб. 2025) — редизайн операционной модели, «технически правдоподобный, но организационно неверный» вывод без контекстного слоя. (§6.2, Часть 4)
56. Forrester. «Agentic Software Development Takes The Lead» (2026) — 30–40% на кодировании / <10% team-wide без end-to-end адаптации; «скорость усиливает сбои». (§3.4, Часть 2; §6.2, Часть 4)
57. Gartner. «AI in the Software Development Life Cycle» / 2026 Hype Cycle for Agentic AI — 5-стадийная кривая внедрения агентов (2025–2029), agentwashing `[VFY-day-of]`. (§6.2, Часть 4)
58. Jevons, W.S. *The Coal Question* (1865) — парадокс роста потребления при росте эффективности использования ресурса. (Deep-dive box, Раздел 6, Часть 4)

**IBM Watson Health — §1.9 (Часть 1), добавлено структурной правкой issue #212**
59. Ross, C. & Swetlitz, I. «IBM's Watson recommended 'unsafe and incorrect' cancer treatments», STAT (25 июля 2018), statnews.com/2018/07/25/ibm-watson-recommended-unsafe-incorrect-treatments — расследование по утечке внутренних презентационных слайдов IBM Watson Health (2017); Случай A, Watson for Oncology, Memorial Sloan Kettering.
60. The University of Texas System. *Special Review of Procurement Procedures Related to the M. D. Anderson Cancer Center Oncology Expert Advisor Project* (ноябрь 2016), utsystem.edu — институциональный аудит закупочных процедур, легший в основу разбора Случая B (Oncology Expert Advisor, MD Anderson): нарушения конкурсных процедур, продление контракта без пересмотра, дефицит донорского финансирования.
61. Strickland, E. «IBM Watson, Heal Thyself: How IBM Overpromised and Underdelivered on AI Health Care», *IEEE Spectrum*, vol. 56, no. 4, pp. 24–31 (апр. 2019), spectrum.ieee.org/how-ibm-watson-overpromised-and-underdelivered-on-ai-health-care — обзорный материал, явно различающий Watson for Oncology (MSK) и Oncology Expert Advisor (MD Anderson) как два разных, независимых проекта IBM Watson Health.

---

## Дальнейшее чтение

- **Steve Blank, Bob Dorf. *The Startup Owner's Manual*** — операционное развёртывание Customer Development.
- **Teresa Torres. *Continuous Discovery Habits*** — метод непрерывного дискавери и opportunity-solution tree.
- **Ron Kohavi, Diane Tang, Ya Xu. *Trustworthy Online Controlled Experiments*** — исчерпывающий референс по продуктовым экспериментам (OEC, SRM, ловушки).
- **Google. *Site Reliability Engineering* + *The SRE Workbook*** (бесплатно на sre.google) — SLI/SLO/error budget с нуля.
- **Anthropic Engineering. «Demystifying evals for AI agents»** (9 янв. 2026) — практический eval-роадмап, pass@k/pass^k.
- **Reganti & Badam. «Why your AI product needs a different development lifecycle»** (Lenny's Newsletter) — CC/CD и agency-ladder.
- **NN/g. State of UX 2026 + «Synthetic Users» + «AI-Moderated Interviews»** — дизайн и дискавери в AI-эру, границы синтетических пользователей и AI-интервьюеров.
- **DeepMind. «Specification gaming»** + **Anthropic. «Sycophancy to Subterfuge»** — закон Гудхарта в ML, от игрушечных RL-примеров до frontier-моделей.
- **Marty Cagan. *Inspired*** — классическая продуктовая таксономия рисков (Value/Usability/Feasibility/Viability), основа для §1.2 и пятого риска Huryn.
- **Eliza Strickland. «IBM Watson, Heal Thyself»**, IEEE Spectrum — лучший обзорный разбор двух разных провалов IBM Watson Health в онкологии для тех, кто хочет полную хронологию за пределами §1.9.
- Для критического чтения статистики провалов: **NewMR «Myth #2»** и **80,000 Hours podcast** про MIT NANDA — как проверять знаменатель и конфликт интересов.
