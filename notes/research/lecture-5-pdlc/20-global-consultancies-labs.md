# Global Consultancies & AI Labs Reframing the SDLC/PDLC (2025–2026)

Research pass for Lecture 5 (PLDLC). Compiled 2026-09-06. Focus: primary-source framework names, phase models, headline numbers (with attribution), how each source claims the classic linear/Agile model breaks, and — critically — documented failure modes / governance risks / limits.

> **Access note:** the Anthropic PDF (source 1) could not be parsed as text via direct fetch (binary/font-encoded stream); all Anthropic figures below are reconstructed from multiple secondary write-ups that quote the report directly (Tessl, Allstacks, NYU Shanghai RITS, Pathmode, HiveTrail — see Sources). Flagged `[SECONDARY]` where this applies. All other sources were fetched directly from the primary page unless noted `[SEARCH-SYNTH]`.

---

## 1. Anthropic — "2026 Agentic Coding Trends Report" (Jan 22, 2026) `[SECONDARY, multi-source triangulated]`

**Framework / structure:** No single named phase model. The report is organized in **three layers**: *foundation trends*, *capability trends*, *impact trends* — with case studies (Rakuten, CRED, TELUS, Zapier, Legora, Fountain, Augment Code).

**Headline thesis — "collapsing stages":** Every classical SDLC stage compresses in duration, not disappears:
- Requirements/planning: days–weeks → **minutes** (intent expression)
- System design: weeks → **seconds** of agent comprehension
- Implementation: weeks–months → **minutes** of agent-driven execution
- Onboarding to a new codebase: **weeks → hours** (this collapse reportedly began in 2025; 2026 is framed as the year orgs learn to fully exploit it for talent deployment / project resourcing)

The systemic reframing: engineers shift from **writing code** to **orchestrating agent teams** that can run autonomously for hours or days. Organizations move from a single coding agent to **groups of specialized agents working in parallel under an orchestrator**, each with a defined role.

**Numbers (flag volatile `[VFY-day-of]`):**
- Developers report using AI in **~60%** of their work `[VFY-day-of]`
- But developers **fully delegate only 0–20%** of tasks to AI `[VFY-day-of]`
- …while **actively supervising 80–100%** of what they do delegate `[VFY-day-of]`
- Claude Code cited elsewhere at **$2.5B ARR** as of the report window `[VFY-day-of]` — commercial signal, not a methodology metric, but useful as scale context

**How the linear/Agile model breaks:** The report's implicit claim is that stage *boundaries* survive but stage *duration* does not — this creates a **review/visibility bottleneck**: "as agents produce more code, review capacity does not scale at the same rate, creating a widening visibility and quality gap." This is the report's central systemic risk, not a side note.

**Named failure/limit (critical for lecture):**
- **The delegation-supervision gap**: teams delegate narrow tasks but must supervise almost all of them — full autonomy is explicitly *not* what's happening in practice, contradicting the "agents replace developers" narrative.
- **Review capacity does not scale with generation capacity** — this is Anthropic's own documented systemic risk: code volume grows faster than human ability to verify it, which is a direct governance/quality risk, not a promotional claim.
- Context engineering (not raw model capability) is flagged by secondary commentary as "the skill that matters most" — implying that orgs without strong context/knowledge infrastructure will not realize the compression benefits and may instead accumulate unreviewed risk.

---

## 2. Bain & Company — "The Rise of the AI Development Life Cycle" (2026) — fetched directly

**Framework name:** **"AI Development Life Cycle"** (lowercase in Bain's own usage — not a trademarked acronym). No proprietary two-loop diagram was found in the fetched page itself (the "two-loop" language appears in *related* Bain agent-ops content — see caveat below), but the PDLC-specific article does articulate a continuous-flow replacement for the classic phase gate model.

**Continuous flow model — core mechanic:** *"AI shatters these boundaries, and it can define requirements, generate code, test, and iterate all within a more continuous flow."* The **PM↔engineering boundary explicitly breaks**: *"The separation between product and engineering begins to break down. Companies are moving toward an AI development life cycle in which AI is embedded across the entire process and product and engineering operate as a more integrated system."*

**Design principle for agents:** *"Agents perform best when work is structured around them, with fresh context windows at each stage and human review at critical junctures."* This is Bain's version of "rebuild the process around the agent, don't bolt the agent onto the old process" — directly matches the brief's framing.

**"Close the loop" principle:** runtime feedback loops back into planning across teams — described as a discipline, not automatic. `[Caveat]` The more explicit "two nested iteration loops" (per-agent feedback loop + shared context/memory layer, so later agents inherit what earlier agents learned) comes from a **related but distinct Bain piece** ("How to Win with AI" / agent-ops decision series), not verbatim in the PDLC article itself — treat as Bain's broader agentic-ops doctrine rather than a PDLC-specific two-loop diagram. `[VFY-day-of]`

**Numbers:**
- Executives project **5×–10× productivity gains** over several years `[VFY-day-of]`
- **63%** report higher output per engineer
- **53%** report faster release cycles
- 2024 baseline productivity gains: **10–15%**, with leaders reaching **30%**

**Named failure/limit modes (Bain is unusually explicit here — good lecture material):**
1. **Bottleneck displacement** — optimizing one activity (e.g., code generation) just moves the constraint downstream (review, QA, deployment).
2. **Pilot proliferation** — many isolated pilots, little translation into sustained workflow change or measured business impact.
3. **Measurement gaps** — companies cannot prove ROI because they never instrumented the old process, so there's no valid baseline for comparison.
4. **Team resistance** — new workflows fail without deliberate enablement/change management.
5. **Narrow focus on code completion** — misses the larger PDLC value pool (requirements, QA, ops, documentation).
6. Human review is explicitly retained as mandatory "for high-risk changes" — Bain does **not** claim full autonomy is safe or desirable yet.

---

## 3. McKinsey / QuantumBlack — "Unlocking the value of AI in software development" (Nov 2025) `[SEARCH-SYNTH + related McKinsey pieces]`

**Authorship:** Charlotte Relyea, Martin Harrysson, Matt Linderman, with Jose Mario Pena, Nandita Bothra, Natasha Maniar — McKinsey Technology, Media & Telecommunications Practice / QuantumBlack, AI by McKinsey. Published November 2025.

**Three enablers/pillars (as stated by McKinsey, closest verbatim available):** *"Top performers reinforce these shifts with three critical enablers — upskilling, impact measurement, and change management — that ensure adoption translates into sustained performance gains."* Note: this phrasing (**upskilling / impact measurement / change management**) is McKinsey's own three-pillar framing for *sustaining* gains — adjacent McKinsey pieces (Reimagining Tech Infrastructure for Agentic AI; Rewiring Software Delivery for the Agentic Era) supply the more technical trio the brief anticipated:
- **Context-aware ecosystem** — "agent factories need organizational context and memory... top businesses build knowledge graphs that function as an AI memory layer across the SDLC, connecting customer feedback, architecture decisions, design documents, tickets, GitHub activity, incident reports, and compliance rules."
- **Hard validation rules** — "as agent-driven execution scales, validation and control become as critical as the agents themselves... enterprises are converging on autonomous testing frameworks to validate both rules-based and AI-driven logic."
- **New team/operating-model metrics** — role and operating-model overhaul implied by the upskilling/measurement/change-management triad above; McKinsey frames this as a management problem, not a tooling problem.

**Headline thesis:** Value from AI in software development is unlocked only when orgs treat it as an **operating-model redesign** (context infrastructure + validation discipline + people systems), not a point-tool rollout. This closely parallels Bain's "bottleneck displacement" warning from a different angle.

**Named limit/governance risk:** Without organizational context/memory infrastructure, agents produce technically plausible but organizationally wrong output (McKinsey's "agentic AI mesh" pieces stress that agents need **orchestration + governance layers** to "operate safely" at scale — implying that ungoverned multi-agent systems are the default failure mode, not an edge case).

---

## 4. EY — "Rise of AI is reshaping product development" + EY.ai PDLC launch (Mar 18, 2026) — fetched directly + press release

**Framework name:** **EY.ai PDLC** (Product Development Lifecycle), built with **8090's Software Factory** platform. Explicitly positioned as **AI-native**, replacing "outdated, linear software development" with a "dynamic, AI-driven model."

**"Iron triangle" thesis (verbatim):** *"With PDLC, it is now possible to achieve all three legs of the iron triangle, which essentially states that you can choose between performance, cost and quality but only achieve two of the three... obtain a better-quality outcome, a product that delivers higher performance in less time and at a significantly reduced cost."* This is EY's central rhetorical claim: **AI breaks the classic speed/cost/quality trade-off** rather than just shifting it.

**PDLC phase/scope redefinition:** widens from "software code generation" alone to include end-user documentation, training materials, marketing collateral, and infrastructure configuration — i.e., PDLC ⊃ SDLC in EY's model; product delivery, not just code, is the unit of orchestration.

**Numbers:**
- Waterfall project **failure rate 59%** (2013–2020, cited from Standish Group's Chaos Report) — EY's own baseline-for-comparison, useful as an *inherited* legacy stat, not new
- Demo case: enterprise investment-management tool built in **2 days vs. 10+ weeks** traditionally, with **6–7 fewer developers** required `[VFY-day-of — single demo case, not a population statistic]`
- **70% increase** in software development productivity/cost efficiency; delivery sped up **80×**; **95%+ automated test coverage** `[VFY-day-of — EY's own use-case figures, likely a best-case/marketing example]`
- Aside, non-PDLC illustrative stat used in EY's broader AI narrative: an AI algorithm identified breast-cancer risk **4–6 years** before clinical radiologist diagnosis (not a PDLC number — used to illustrate "AI catches things earlier," reused loosely across EY collateral)

**How the linear model breaks:** EY explicitly names "outdated, linear software development" as the target to replace — i.e., its argument is against **Waterfall specifically** (citing the 59% historical failure rate) more than against Agile.

**Named governance/failure risk:**
- **Algorithmic bias and transparency** in AI-driven decisions — named directly as a governance concern
- **"Strong role in human judgment" retained despite automation** — EY does not claim full automation is safe
- **Workforce displacement** requiring reskilling programs — treated as a real organizational risk, not a talking point
- **Ethical oversight mechanisms** flagged as essential
- **Need for internal AI champions** for adoption to survive past pilot stage (echoes Bain's "pilot proliferation" risk from the demand side)
- Human oversight described as **"indispensable"** to prevent "unintended consequences" — EY's own words, notably cautious given this is also a product-launch page.

---

## 5. Gartner — "AI in the Software Development Life Cycle" / 2026 Hype Cycle for Agentic AI `[SEARCH-SYNTH, multiple Gartner-sourced secondary reports]`

**Framework: Five-stage agentic AI adoption curve** (Gartner's clearest phase model of all sources — good lecture anchor):
- **Stage 1 (by end 2025):** almost every enterprise app embeds AI assistants (chat-style)
- **Stage 2 (by 2026):** **40%** of enterprise apps integrate **task-specific agents** (up from <5% in 2025)
- **Stage 3 (by 2027):** ~1/3 of implementations use **collaborative agents** for complex tasks
- **Stage 4 (by 2028):** multi-agent ecosystems dynamically collaborate *across* applications
- **Stage 5 (by 2029):** **≥50%** of knowledge workers create, govern, and deploy agents on demand

**Core distinction Gartner insists on:** **agents vs. assistants** — "agents that act autonomously across the [lifecycle] versus assistants that accelerate a [user]'s keystrokes." This maps directly onto the lecture's "collapsing stages" theme: Gartner's claim is that the SDLC only *actually* changes once you cross from assistant-stage to agent-stage tooling — most orgs are still one stage behind where they think they are.

**"Agentwashing" — Gartner's own named risk:** vendors rebrand existing chatbots/genAI assistants as "agents" without delivering agentic outcomes — a **measurement/definitional governance risk**, i.e., organizations may believe they're further along the adoption curve than they are.

**Numbers (high-value, heavily cited across secondary press — flag `[VFY-day-of]` for reprint accuracy):**
- **40%** of enterprise apps will feature task-specific agents by end of 2026, up from **<5%** in 2025 (Gartner press release, Aug 2025)
- **More than 40%** of agentic AI projects will be **canceled/abandoned by 2027** — cited reasons: rising costs, unclear ROI, poor risk management, hype-driven adoption without clear deployment roadmaps
- 2026 Gartner CIO Survey: only **17%** of organizations have actually deployed AI agents to date; **>60%** expect to within two years — i.e., a large intention–deployment gap
- Adjacent (RAND Corporation, cited in Gartner-linked commentary, not Gartner itself): AI project failure rates **exceed 80%**, with root cause typically **data quality**, not model quality — useful cross-check against Deloitte's data-quality finding (§6)

**Named failure/limit (this is Gartner's strongest material for the "when AI does NOT help" angle):**
- **Agentwashing** as a systemic market-distortion risk
- **Technology/maturity mismatch**: "current models lack the maturity and agency to autonomously achieve complex business goals or follow nuanced instructions over time" — many use cases positioned as agentic **don't actually require agentic implementation** (i.e., over-application of agents where simpler automation would do — directly usable as a "criteria for when AI is NOT needed" teaching point)
- Most deployments remain **narrowly scoped**; fully autonomous agents are explicitly "not ready for the majority of enterprise use cases" per Gartner's own 2026 framing

---

## 6. Deloitte — "2026 Global Technology Leadership Study" ("From Operators to Orchestrators") — fetched directly (press release)

**Framework name:** No SDLC-phase model — this is an **operating-model / leadership-mandate** framework: **"From Operators to Orchestrators."** Relevant to the lecture as the *organizational governance* counterpart to the more technical frameworks above (Bain/EY/Gartner describe the pipeline; Deloitte describes who is accountable for redesigning it and why most orgs can't yet).

**Sample:** **660+ tech leaders**, global survey.

**Headline thesis (verbatim):** *"The era of the operational technologist is over... Today's CIO isn't just leading technology; they are being asked to redesign the very fabric of how the business runs."* — Anjali Shaikh, Managing Director, Deloitte Consulting LLP.

**Numbers:**
- **75%** of tech leaders say their **operating model must fundamentally change** to drive greater AI value (this is the number named explicitly in the brief)
- **81%** are confident they *can* scale AI — creating an internal contradiction Deloitte flags directly: confidence in capability without confidence the *structure* around it is ready
- **42%** report **low or no ROI** on AI investments to date
- **79%** cite "driving business outcomes" as their top priority (shift away from pure operational/technology management)
- **71%** of organizations have **five or more** distinct tech leadership roles — i.e., AI accountability is diffuse, not owned by one function
- **41%** of tech leaders say the business views them as **unable to keep pace with demand**

**How the linear model breaks (organizational lens, not technical):** Deloitte's argument is that the **PDLC/SDLC bottleneck is no longer technical — it's structural**: legacy funding models, governance structures, and talent models were not built for continuous AI-embedded workflows, so even where the technical capability for continuous flow (Bain) or context-aware ecosystems (McKinsey) exists, the **organization's budget/governance cadence still runs on old (often annual/quarterly) cycles**, creating friction between what the tooling can do and what the org can absorb.

**Named barrier/governance risk (this is the "barriers to new PDLC" material the brief asked for):**
- **Poor data quality**, security concerns, talent shortages, legacy systems named as the **primary scaling blockers — not the AI technology itself**
- Funding models and governance structures explicitly said to have **"not kept pace"** with the demands placed on tech leaders
- Structural gap between "bold ambition" and "legacy operating models, talent, and budget" — Deloitte's own framing of the central tension

---

## 7. GitHub / Microsoft — "Test-First AI" methodology `[NOT FOUND as a named public framework]`

Extensive search (direct queries for "Test-First AI," "AI as environment not Copilot," GitHub/Microsoft Build 2026 sessions) did **not surface a publicly published report or blog post under this name** as of 2026-09-06. What surfaced instead, adjacent but distinct:
- Microsoft Build 2026 recap material on first-party model stack and Copilot agent capability expansion (general coverage, not a named methodology)
- OpenHands and similar "autonomous SWE agent in a sandboxed environment" tooling (third-party, not GitHub/Microsoft-authored) — closest existing match to the "AI as environment, not just a chat assistant" framing, but not attributable to GitHub/Microsoft
- No GitHub Blog or Microsoft Source post titled or thematically matching "Test-First AI" was located

**Recommendation for the lecture:** either (a) drop this citation and substitute the **Forrester** finding below (which independently makes a very similar "agents must produce tests, not just code" point with real numbers), or (b) mark explicitly as **`[VFY-day-of — could not verify public source, may require Google Workspace / GitHub direct search or the report may be an internal/keynote reference not yet public]`**. Do not present "Test-First AI" as a confirmed GitHub/Microsoft-branded methodology without further verification — this is a genuine gap, not an oversight in search effort.

---

## Bonus / supplementary source found during search: Forrester — "Agentic Software Development Takes the Lead" (2026)

Not in the original brief but directly relevant and strong on the failure/governance angle requested. Fetched directly.

**Implicit 3-stage evolution model:**
- **2023–2024 ("TuringBots"):** agents focused on coding + unit testing only
- **2025:** expanded to documentation, design, test generation
- **2026:** **cross-stage orchestration** across analysis, planning, design, build, test, delivery

**Headline thesis:** *"GenAI is no longer just helping developers to write code faster; it is reshaping how software is planned, built, tested, and delivered."*

**Numbers:**
- Coding-only improvements: **30–40% gains**
- Team productivity **without end-to-end adoption**: **<10% increase** — i.e., Forrester's own evidence for bottleneck displacement (narrow AI use caps total gains at single digits/low teens even when the automated slice improves 3-4×)

**Named failure/limit (strong, concrete — good for lecture):**
- Agents "**hallucinate, introduce subtle defects, or propagate errors faster than humans**"
- "**Speed amplifies failures**" — autonomous systems disseminate errors at unprecedented velocity (direct rebuttal to naive "faster = better" framing)
- "**Trust becomes the limiting factor**" as autonomy increases — i.e., the ceiling on adoption is organizational trust, not model capability
- AI-generated artifacts require **equal or higher** testing rigor than human-written code, not less

---

## Comparison Table

| Source | Framework name | Key phases / stages | Headline thesis | Notable number | Failure / limit noted |
|---|---|---|---|---|---|
| **Anthropic** (Jan 2026) `[secondary]` | 3 layers: foundation/capability/impact trends | Requirements→design→implementation, each collapsing in duration | Engineers shift from writing code to orchestrating agent teams; stage boundaries persist, durations collapse (weeks→hours/minutes) | Fully delegate only **0–20%** of tasks despite AI touching **~60%** of work `[VFY-day-of]` | Review capacity doesn't scale with generation capacity → widening quality/visibility gap |
| **Bain** (2026) | "AI Development Life Cycle" (continuous flow) | PM+eng merge into one continuous define→build→test→iterate flow, structured around agents with fresh context windows | Rebuild the process around agents; don't bolt agents onto old phase gates | **5–10×** projected productivity; **63%** higher output/engineer; **53%** faster releases | Bottleneck displacement, pilot proliferation, measurement gaps, team resistance, narrow code-only focus |
| **McKinsey/QuantumBlack** (Nov 2025) | 3 enablers (upskilling / impact measurement / change management) + context-aware ecosystem / validation / new metrics | Knowledge-graph memory layer across SDLC; autonomous testing/validation frameworks; operating-model redesign | Value comes from operating-model redesign, not point-tool adoption | (no single flagship % — enabler-based framing) | Ungoverned multi-agent systems are the default failure mode without orchestration/governance layers |
| **EY / 8090** (Mar 2026) | EY.ai PDLC (AI-native, replaces linear Waterfall) | PDLC ⊃ SDLC: code + docs + training + marketing + infra config, unified | AI-native PDLC breaks the iron triangle — speed, cost, AND quality simultaneously | Legacy Waterfall failure rate **59%** (Standish, 2013–20); demo: **2 days vs 10+ weeks** `[VFY-day-of]` | Algorithmic bias/transparency, workforce displacement, need for reskilling, human judgment "indispensable" |
| **Gartner** (2026 Hype Cycle) | 5-stage agentic adoption curve (2025–2029) | Assistants → task agents → collaborative agents → multi-agent ecosystems → workers as agent builders | Real transformation starts only at the agent (not assistant) stage; most orgs overestimate their stage | **40%** of apps w/ task agents by 2026 (from <5%); **>40%** of agentic projects canceled by 2027; only **17%** actually deployed | "Agentwashing," maturity mismatch, many use cases don't need agentic implementation at all |
| **Deloitte** (2026 Global Tech Leadership Study) | "From Operators to Orchestrators" (operating-model mandate, not phase model) | N/A — leadership/governance framework, not pipeline stages | PDLC bottleneck is now structural/organizational, not technical | **75%** say operating model must change; **42%** report low/no AI ROI; **81%** confident vs. 75% needing change (internal contradiction) | Funding/governance structures haven't kept pace; data quality, security, talent, legacy systems are the real blockers |
| **Forrester** (2026, bonus) | Implicit 3-stage: TuringBots → expanded scope → cross-stage orchestration | Analysis→planning→design→build→test→delivery, agent-orchestrated | GenAI reshapes planning/build/test/delivery, not just coding | Coding gains **30–40%**; whole-team gains **<10%** without end-to-end adoption | Hallucination, error propagation at speed, "trust becomes the limiting factor" |
| **GitHub/Microsoft "Test-First AI"** | Not found as named public source | — | — | — | Could not verify; recommend dropping or flagging `[VFY-day-of]` |

---

## Sources

1. Anthropic, *2026 Agentic Coding Trends Report* (Jan 22, 2026). PDF: https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf — **direct fetch failed** (binary/font-encoded PDF, no extractable text via WebFetch). Triangulated via:
   - https://tessl.io/blog/8-trends-shaping-software-engineering-in-2026-according-to-anthropics-agentic-coding-report
   - https://www.allstacks.com/blog/the-orchestration-gap-what-anthropics-report-means-for-engineering-leaders
   - https://rits.shanghai.nyu.edu/ai/anthropics-2026-agentic-coding-trends-report-from-assistants-to-agent-teams/
   - https://pathmode.io/blog/orchestration-era-needs-intent
   - https://hivetrail.com/blog/anthropic-2026-agentic-coding-report/
   - https://www.claudeainews.com/news/anthropic-2026-agentic-coding-report
   - https://agentmarketcap.ai/blog/2026/04/05/anthropic-agentic-coding-trends-report-claude-code-eight-shifts
   - Landing page: https://resources.anthropic.com/2026-agentic-coding-trends-report
   - Access date: 2026-09-06.

2. Bain & Company, *The Rise of the AI Development Life Cycle* (2026). https://www.bain.com/insights/the-rise-of-the-ai-development-life-cycle/ — **fetched directly**, full text retrieved. Access date: 2026-09-06.
   - Related Bain agent-ops doctrine (two-loop / feedback-loop language, cited as adjacent not identical): https://www.bain.com/insights/solutions/turn-artificial-intelligence-into-proprietary-intelligence/decision-6-the-learning-system/

3. McKinsey & Company / QuantumBlack, *Unlocking the value of AI in software development* (Nov 2025). https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/unlocking-the-value-of-ai-in-software-development — direct fetch timed out; content triangulated via search snippets + related McKinsey pieces:
   - https://www.mckinsey.com/capabilities/quantumblack/our-insights/seizing-the-agentic-ai-advantage
   - https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/reimagining-tech-infrastructure-for-and-with-agentic-ai
   - https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/rewiring-software-delivery-for-the-agentic-era
   - https://medium.com/quantumblack/agentic-workflows-for-software-development-dc8e64f4a79d
   - Access date: 2026-09-06. **Recommend re-fetch of the primary McKinsey URL directly (not via search) before final lecture use** — timeout was likely transient.

4. EY, *Rise of AI is reshaping product development* (2026). https://www.ey.com/en_us/insights/ai/rise-of-ai-is-reshaping-product-development — **fetched directly**, full text retrieved. Access date: 2026-09-06.
   - EY.ai PDLC launch press release (Mar 18, 2026): https://www.ey.com/en_us/newsroom/2026/03/ernst-young-llp-and-8090-launch-ey-ai-pdlc
   - Cross-post: https://www.prnewswire.com/news-releases/ernst--young-llp-and-8090-launch-ai-native-eyai-product-development-lifecycle-pdlc-to-help-enterprises-break-free-from-slow-costly-and-failure-prone-software-development-302716620.html
   - Product page: https://www.ey.com/en_us/services/consulting/ai-native-pdlc-reinventing-software-delivery

5. Gartner, *2026 Hype Cycle for Agentic AI* + related SDLC/agent coverage. https://www.gartner.com/en/articles/hype-cycle-for-agentic-ai — accessed via search synthesis (not directly fetched); supporting citations:
   - Gartner press release (Aug 26, 2025), "40% of Enterprise Apps...": https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025
   - "Over 40% of Agentic AI Projects Likely to Be Abandoned by 2027": https://www.cdomagazine.tech/aiml/over-40-of-agentic-ai-projects-likely-to-be-abandoned-by-2027-gartner-forecast ; https://martech.org/gartner-40-of-agentic-ai-projects-will-fail-making-humans-indispensable/ ; https://www.forbes.com/sites/solrashidi/2025/06/28/ai-agents-and-hype-40-of-ai-agent-projects-will-be-canceled-by-2027/
   - CIO survey / 17% deployed stat: aggregated via search (Keyhole Software, Simbian, informedclearly.com coverage)
   - Access date: 2026-09-06. **Recommend direct fetch of gartner.com articles before final use** — Gartner content is often paywalled/gated; only press-release-tier public pages confirmed accessible.

6. Deloitte, *2026 Global Technology Leadership Study — "From Operators to Orchestrators"*. Press release fetched directly: https://www.deloitte.com/us/en/about/press-room/2026-global-technology-leadership-study-release.html — Access date: 2026-09-06.
   - Related: https://www.deloitte.com/us/en/insights/topics/technology-management/rewiring-ai-operating-model.html
   - Study landing page: https://www.deloitte.com/us/en/programs/chief-information-officer/articles/global-technology-leadership-study.html

7. GitHub / Microsoft, "Test-First AI" methodology — **not located** as a named public source despite direct and adjacent searches (Microsoft Build 2026 recap, GitHub topic pages, "AI as environment" framing). See §7 above for detail. Access date: 2026-09-06.

8. **Bonus:** Forrester, *Agentic Software Development Takes The Lead: From Code Assistants To Orchestrated SDLC Agents* (2026). https://www.forrester.com/blogs/agentic-software-development-takes-the-lead-from-code-assistants-to-orchestrated-sdlc-agents/ — **fetched directly**, full text retrieved. Access date: 2026-09-06.

9. Supplementary / cross-check on AI project failure rates: RAND Corporation findings on AI project failure rates (>80%, data quality as root cause), cited via Gartner-adjacent secondary coverage — original RAND report not independently fetched in this pass; flag `[VFY-day-of]` if used as a standalone citation.
