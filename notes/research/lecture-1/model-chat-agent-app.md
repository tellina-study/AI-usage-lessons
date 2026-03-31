# Model vs Chat vs Agent vs Application: Research Notes

Research compiled 2026-03-31 for Lecture 1.

---

## 1. AI Model (Standalone)

### Definition

A trained neural network that maps input to output through learned parameters. Operates as a pure function: receives data, produces predictions or transformations. No conversational state, no tool access, no planning loop.

### Academic Sources

- **Kreuzberger et al. (2023)** "Machine Learning Operations (MLOps): Overview, Definition, and Architecture" — arXiv:2205.02302. Defines model deployment patterns: batch inference, real-time serving, model-as-a-service. Covers the lifecycle from training to production serving.
- **MLOps deployment patterns** distinguish two approaches: "deploy model" (promote artifact) vs "deploy code" (promote training pipeline). Key serving modes: batch inference (periodic), online/real-time inference (per-request).

### Examples

| Model | Domain | Input → Output |
|-------|--------|----------------|
| YOLOv8/v9 | Computer vision | Image → bounding boxes + labels |
| Whisper (OpenAI) | Speech | Audio → transcript text |
| Stable Diffusion / SDXL | Image generation | Text prompt → image |
| BERT / RoBERTa | NLP | Text → embeddings / classification |
| AlphaFold | Biology | Amino acid sequence → 3D structure |
| Segment Anything (SAM) | Vision | Image + prompt → segmentation mask |

### When to Use

- High throughput, low latency requirements (e.g. video processing at 30+ FPS)
- Specific, well-defined task with stable input/output format
- Full control over infrastructure, versioning, and behavior
- Deterministic or near-deterministic output needed
- Edge/embedded deployment (no cloud dependency)

---

## 2. Chat (Conversational AI / LLM Chat)

### Definition

Natural language interface to a large language model. User sends text, model responds in text. Maintains conversation context within a session. No persistent memory across sessions (unless added by the product). No autonomous tool use — the model generates text, not actions.

### Academic Sources

- **Dam et al. (2024)** "A Complete Survey on LLM-based AI Chatbots" — arXiv:2406.16937. Comprehensive survey covering the evolution from rule-based chatbots to LLM-based systems. Reviews ChatGPT, Gemini, Claude, and domain-specific chatbots across education, healthcare, business.
- **Fui-Hoon Nah et al. (2024)** "A Contemporary Review on Chatbots, AI-Powered Virtual Conversational Agents, ChatGPT: Applications, Open Challenges and Future Research Directions" — ScienceDirect. Domain-based analysis of chatbot applications and performance.
- **Waseem et al. (2025)** "A Survey on Chatbots and Large Language Models: Testing and Evaluation Techniques" — ScienceDirect. Framework for testing and evaluating chatbot and LLM performance.

### Examples

| Product | Provider | Notes |
|---------|----------|-------|
| ChatGPT | OpenAI | GPT-4o/4.5, web + mobile, plugins |
| Claude | Anthropic | Claude 4 Opus/Sonnet, long context |
| Gemini | Google | Multimodal, integrated with Google ecosystem |
| GigaChat | Sberbank | Russian-language, multimodal (text + images via Kandinsky), 2.5M+ users by 2024 |
| YandexGPT | Yandex | Optimized for Russian, integrated with Alice voice assistant |
| Mistral Chat (Le Chat) | Mistral AI | European, open-weight models |
| DeepSeek Chat | DeepSeek | Chinese, strong reasoning capabilities |

### When to Use

- Exploration, brainstorming, creative work
- One-off questions and analysis
- Learning and explanation
- Draft generation (text, code, plans)
- When human judgment guides every step

---

## 3. AI Agent

### Definition

A system that uses an LLM as its reasoning core, augmented with planning, memory, and tool use capabilities. It receives a goal, decomposes it into steps, executes actions via external tools, observes results, and iterates until the goal is achieved or a stop condition is reached.

**Lilian Weng's formulation (2023):** Agent = LLM + Memory + Planning + Tool Use

**Google Agents Whitepaper (2024):** "An agent is an application that attempts to achieve a goal by observing the world and acting upon it using available tools." Three components: the Model (decision maker), Tools (extensions, functions, data stores), and the Orchestration Layer (reasoning via ReAct, CoT, ToT).

### Key Academic Papers

**Foundational:**

- **Yao et al. (2022/2023)** "ReAct: Synergizing Reasoning and Acting in Language Models" — arXiv:2210.03629, ICLR 2023. Core idea: interleave reasoning traces with actions. The agent reasons about what to do, acts, observes, reasons again. Outperformed baselines by 34% on ALFWorld and 10% on WebShop.
- **Schick et al. (2023)** "Toolformer: Language Models Can Teach Themselves to Use Tools" — arXiv:2302.04761, NeurIPS 2023 (Meta AI). LLM self-trains to decide which APIs to call, when, and how to incorporate results. Tools include calculator, search engines, Q&A system, translator, calendar.
- **Weng, Lilian (2023)** "LLM Powered Autonomous Agents" — lilianweng.github.io. Influential blog post defining the agent = LLM + planning + memory + tools framework. Referenced by virtually every subsequent survey.

**Surveys (2024-2025):**

- **Wang et al. (2023, updated 2025)** "A Survey on Large Language Model based Autonomous Agents" — arXiv:2308.11432, Frontiers of Computer Science. Unified framework for LLM agent construction. 4500+ citations.
- **Xinzhel et al. (2025)** "A Review of Prominent Paradigms for LLM-Based Agents" — CoLing 2025. Taxonomy: tool use (incl. RAG), planning, feedback learning.
- **Liu et al. (2025)** "Survey on Evaluation of LLM-based Agents" — arXiv:2503.16416. First comprehensive survey of agent evaluation methodologies.
- **Li et al. (2024)** "A Survey on LLM-based Multi-Agent Systems" — Springer Vicinagearth. Five components: profile, perception, self-action, mutual interaction, evolution.

**Autonomy Levels:**

- **"Levels of Autonomy for AI Agents" Working Paper (2025)** — arXiv:2506.12469. Defines five levels by user role: (1) Operator — user controls, (2) Collaborator — user works jointly, (3) Consultant — user advises, (4) Approver — user reviews/authorizes, (5) Observer — user monitors passively. Proposes AI autonomy certificates for governance.

### Examples

| Agent | Type | Key Feature |
|-------|------|-------------|
| Claude Code | Coding agent | Terminal-native, local environment, interactive |
| Devin (Cognition Labs) | Coding agent | Cloud sandbox, fully autonomous, delegates PRs |
| AutoGPT | General autonomous | Plan → Act → Observe → Update loop, open-source |
| CrewAI | Multi-agent framework | Role-based agents (Manager/Worker/Researcher), hierarchical or distributed |
| LangGraph | Agent orchestration | Graph-based workflow, human-in-the-loop gates |
| OpenAI Assistants API | Platform agent | Tool use, code interpreter, file search |
| Manus | General agent | Autonomous task execution, web browsing |

### When to Use

- Multi-step tasks requiring planning and iteration
- External tools needed (APIs, databases, file systems, browsers)
- Task outcome cannot be achieved in a single LLM call
- Quality improves with self-reflection and correction
- Human oversight desired but not at every token

---

## 4. AI-Powered Application

### Definition

An end-user product that embeds AI as one component among many (UI, data pipeline, business logic, integrations). The user interacts with a purpose-built interface, not directly with the model. The AI is invisible or semi-visible — it powers features, not the entire experience.

### Characteristics

- **Purpose-built UI** — user does not write prompts; interacts via buttons, forms, voice, gestures
- **AI as feature, not product** — the application solves a domain problem; AI is the engine underneath
- **Deterministic UX** — same user action produces consistent, predictable application behavior (even if AI output varies internally)
- **Managed quality** — application adds guardrails, fallbacks, human review, caching around AI outputs

### Examples

| Application | AI Inside | User Sees |
|-------------|-----------|-----------|
| Google Translate | Neural MT models | Text box + translation |
| Grammarly | NLP models + LLM | Red/blue underlines + suggestions |
| Notion AI | GPT-4 / Claude | "Summarize" / "Improve writing" buttons |
| GitHub Copilot | Codex / GPT-4 | Inline code completions |
| Spotify (Discover Weekly) | Collaborative filtering + deep learning | Playlist |
| Yandex Navigator | ML routing models | Map + voice directions |
| Adobe Firefly | Diffusion models | "Generate" button in Photoshop |
| Duolingo (Explain My Answer) | GPT-4 | Explanation card after wrong answer |
| Google Photos | Vision models | Search by content, face grouping |

### When to Use

- End users need a simple, polished interface
- Domain-specific problem with clear UX
- AI quality must be managed (guardrails, fallbacks, human review)
- Business requires SLAs, compliance, audit trails
- Scale requires caching, optimization, cost management

---

## 5. Comparison Framework

### The Autonomy-Control Matrix

| | Low Autonomy | High Autonomy |
|---|---|---|
| **Narrow scope** | **Model** — single task, full control, deterministic | **Agent (task-specific)** — autonomous but domain-bounded |
| **Broad scope** | **Chat** — broad but human-directed every step | **Agent (general)** — broad and self-directed |

**Application** sits orthogonally: it wraps any of the above in a product UX.

### Five Axes of Comparison

| Axis | Model | Chat | Agent | Application |
|------|-------|------|-------|-------------|
| **Level of control** | Full (developer controls everything) | Medium (user steers via prompts) | Low-Medium (user sets goal, agent decides how) | Lowest for user over AI internals; highest UX control |
| **Determinism** | High (same input → same output, mostly) | Low (stochastic, temperature-dependent) | Low (path depends on tool results, environment) | Medium-High (guardrails + caching stabilize output) |
| **Number of steps** | 1 (single inference) | 1 per turn, N turns per session | N steps per task, autonomous iteration | Varies; AI calls are embedded in application flow |
| **Human-in-the-loop** | None at inference time | Every turn | Optional checkpoints (approver/observer model) | Varies by design (from none to approval gates) |
| **Tool access** | None | None (unless tool-use is added) | Core capability | Managed by application logic |

### Anthropic's Agentic Spectrum (Dec 2024)

From "Building Effective Agents" (anthropic.com/research/building-effective-agents):

Distinguishes **workflows** (predefined code paths orchestrating LLMs + tools) from **agents** (LLMs dynamically directing their own processes). Five workflow patterns of increasing complexity:

1. **Prompt Chaining** — sequential LLM calls, each processing previous output
2. **Routing** — classifier sends input down specialized paths
3. **Parallelization** — task split and run concurrently
4. **Orchestrator-Workers** — central LLM decomposes task, delegates to workers, synthesizes
5. **Evaluator-Optimizer** — one LLM generates, another evaluates in a loop

Key principle: "Find the simplest solution possible, and only increase complexity when needed."

### Andrew Ng's Four Agentic Design Patterns (2024)

1. **Reflection** — AI critiques its own output, uses feedback to improve
2. **Tool Use** — API calls and external tool interaction
3. **Planning** — decomposing complex tasks into steps
4. **Multi-Agent Collaboration** — specialized agents working together

Ng notes: Reflection and Tool Use are consistently effective. Planning is powerful but less consistent.

### Google Agents Whitepaper (Nov 2024)

Three-component framework: Model + Tools + Orchestration Layer. Tools are typed as Extensions (API bridges), Functions (client-side logic), and Data Stores (dynamic knowledge). Orchestration uses reasoning techniques (ReAct, CoT, ToT).

### Levels of Autonomy (arXiv:2506.12469, 2025)

Analogous to SAE autonomous driving levels:

| Level | User Role | Description |
|-------|-----------|-------------|
| 1 | Operator | User actively controls the agent |
| 2 | Collaborator | User and agent work jointly |
| 3 | Consultant | User provides guidance, agent leads |
| 4 | Approver | User reviews and authorizes agent decisions |
| 5 | Observer | User monitors passively |

---

## 6. Industry Examples by Type

### Model Deployments

| Company | Model | Use Case |
|---------|-------|----------|
| Tesla | Vision NN (HydraNet) | Autopilot perception |
| Shazam (Apple) | Audio fingerprint NN | Song identification |
| Pinterest | Visual search model | "Shop the Look" |
| Spotify | Audio analysis models | Music classification, recommendations |

### Chat Products

| Company | Product | Notable Feature |
|---------|---------|-----------------|
| OpenAI | ChatGPT | Plugins, GPTs, code interpreter |
| Anthropic | Claude | 200K context, artifacts |
| Google | Gemini | Multimodal, Google integration |
| Sberbank | GigaChat | Russian language, image generation |
| Yandex | YandexGPT/Alice | Russian language, voice assistant |
| Mistral AI | Le Chat | European, open-weight |

### Agent Products

| Company | Product | Notable Feature |
|---------|---------|-----------------|
| Cognition Labs | Devin | Autonomous software engineer, cloud sandbox |
| Anthropic | Claude Code | Terminal agent, local dev environment |
| AutoGPT (open-source) | AutoGPT | Goal-driven autonomous loop |
| CrewAI | CrewAI Framework | Multi-agent role-based orchestration |
| LangChain | LangGraph | Graph-based agent workflows |
| Microsoft | AutoGen | Multi-agent conversation framework |
| Adept AI | ACT-1 | Computer-use agent |

### AI-Powered Applications

| Company | Product | AI Feature |
|---------|---------|------------|
| Google | Google Translate | Neural machine translation |
| Google | Google Photos | Visual search, face recognition |
| Grammarly | Grammarly | Writing correction + generation |
| Notion | Notion AI | Summarize, expand, translate |
| GitHub | Copilot | Code completions + chat |
| Adobe | Firefly / Photoshop AI | Generative fill, expand, remove |
| Duolingo | Max subscription | GPT-4 powered explanations |
| Spotify | DJ feature | Personalized audio commentary |
| Yandex | Yandex Navigator | ML-powered routing |
| Canva | Magic Design | AI layout generation |

---

## 7. Key Sources Index

### Academic Papers

1. Yao et al. (2022) — ReAct — arXiv:2210.03629 — https://arxiv.org/abs/2210.03629
2. Schick et al. (2023) — Toolformer — arXiv:2302.04761 — https://arxiv.org/abs/2302.04761
3. Wang et al. (2023/2025) — LLM Agents Survey — arXiv:2308.11432 — https://arxiv.org/abs/2308.11432
4. Dam et al. (2024) — LLM Chatbots Survey — arXiv:2406.16937 — https://arxiv.org/abs/2406.16937
5. Kreuzberger et al. (2023) — MLOps Survey — arXiv:2205.02302 — https://arxiv.org/abs/2205.02302
6. Liu et al. (2025) — Agent Evaluation Survey — arXiv:2503.16416 — https://arxiv.org/abs/2503.16416
7. Li et al. (2024) — Multi-Agent Survey — Springer — https://link.springer.com/article/10.1007/s44336-024-00009-2
8. Levels of Autonomy (2025) — arXiv:2506.12469 — https://arxiv.org/abs/2506.12469
9. Waseem et al. (2025) — Chatbot Evaluation — ScienceDirect — https://www.sciencedirect.com/science/article/pii/S2949719125000044
10. AI Agents vs Agentic AI Taxonomy (2025) — arXiv:2505.10468 — https://arxiv.org/abs/2505.10468

### Industry Sources

11. Anthropic (Dec 2024) — "Building Effective Agents" — https://www.anthropic.com/research/building-effective-agents
12. Weng, Lilian (Jun 2023) — "LLM Powered Autonomous Agents" — https://lilianweng.github.io/posts/2023-06-23-agent/
13. Andrew Ng (Mar 2024) — Agentic Design Patterns — https://www.deeplearning.ai/courses/agentic-ai/
14. Google (Nov 2024) — Agents Whitepaper — https://ppc.land/content/files/2025/01/Newwhitepaper_Agents2.pdf
15. LangChain (2024) — State of AI Agents Report — https://www.langchain.com/stateofaiagents
