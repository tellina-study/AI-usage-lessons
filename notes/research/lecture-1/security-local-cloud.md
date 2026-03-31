# Research: Local vs Cloud AI Models and Security Considerations

**For:** Lecture 1
**Researched:** 2026-03-31
**Status:** Draft

---

## 1. Cloud AI Services -- What Happens to Your Data

### 1.1 OpenAI (ChatGPT / API)

**Consumer ChatGPT (Free, Plus):** Data is used for training by default. Users can opt out via settings, but the default is opt-in to training. Conversations may be reviewed by human annotators for safety and quality.

**API:** Since March 1, 2023, data sent to the OpenAI API is **not** used to train models unless the organization explicitly opts in. Zero Data Retention (ZDR) agreements are available for enterprise API customers -- OpenAI never retains prompts or responses under ZDR.

**ChatGPT Enterprise / Business:** Data is **not** used for training by default. Stronger privacy protections, SOC 2 compliance, encryption at rest and in transit.

Sources:
- [OpenAI: How your data is used to improve model performance](https://openai.com/policies/how-your-data-is-used-to-improve-model-performance/)
- [Data controls in the OpenAI platform](https://developers.openai.com/api/docs/guides/your-data)
- [OpenAI Help Center: Data usage](https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance)

### 1.2 Anthropic (Claude)

**Consumer (Free, Pro, Max):** As of September 28, 2025, Anthropic asks users whether they wish to share data for training. This is framed as voluntary contribution. If opted in, data retention extends to five years (previously 30 days). Deleted conversations are not used for training.

**Business (Claude for Work, Education, Gov, API via Bedrock/Vertex):** Existing privacy protections remain. Data is **not** used for training.

**Key detail:** Anthropic states collected data will never be sold to third parties and undergoes filtering to reduce sensitive data exposure.

Sources:
- [Anthropic: Updates to Consumer Terms and Privacy Policy](https://www.anthropic.com/news/updates-to-our-consumer-terms)
- [TechCrunch: Anthropic users face a new choice](https://techcrunch.com/2025/08/28/anthropic-users-face-a-new-choice-opt-out-or-share-your-data-for-ai-training/)
- [Anthropic Privacy Center: Data retention](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data)

### 1.3 Google Gemini

**Consumer (Free):** User data can be used for model training unless opted out via Gemini Apps Activity settings. A subset of chats is reviewed by human reviewers. Reviewed chats are retained up to three years (disconnected from user account before review).

**Enterprise (Google Workspace, Cloud):** Prompts, AI outputs, and code are **not** used for training base Gemini models. Content is treated as customer-owned data with strong protections.

Sources:
- [Google: Gemini Apps Privacy Hub](https://support.google.com/gemini/answer/13594961?hl=en)
- [Google Cloud: How Gemini uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance)
- [Gemini Training Data: Consumer vs Enterprise Policies](https://i10x.ai/news/google-gemini-training-data-consumer-vs-enterprise)

### 1.4 Enterprise vs Consumer Tiers -- Summary Table

| Provider | Consumer Default | Consumer Opt-out? | Enterprise Default | API Default |
|----------|-----------------|-------------------|-------------------|-------------|
| OpenAI | Trains on data | Yes | No training | No training |
| Anthropic | Asks permission (Sep 2025+) | Yes | No training | No training |
| Google | Trains on data | Yes | No training | No training |

**Key takeaway for students:** Free tiers of all major providers use your data for training by default or ask for permission. Enterprise and API tiers consistently do not train on your data. The privacy gap between free and paid tiers is significant.

### 1.5 The Samsung Incident (2023)

In March-April 2023, Samsung semiconductor division engineers leaked confidential data through ChatGPT in three separate incidents:

1. An engineer pasted **proprietary source code** from a semiconductor database into ChatGPT to debug it.
2. Another engineer **recorded a company meeting**, transcribed it, and fed the transcription to ChatGPT to generate meeting notes.
3. A third engineer used ChatGPT to **optimize a test sequence** for chip yield/defect identification.

**Consequences:**
- Since ChatGPT (consumer tier) retains data for training, Samsung's trade secrets were effectively handed to OpenAI.
- Samsung banned all external generative AI tools company-wide.
- Introduced an emergency 1024-byte prompt limit as a stopgap.
- Eventually lifted the ban after developing internal AI tools and policies.

**Lesson:** This is the canonical example of what happens when employees use consumer AI tools with proprietary data. It demonstrates why enterprise policies and tiers exist.

Sources:
- [Bloomberg: Samsung Bans ChatGPT After Leak](https://www.bloomberg.com/news/articles/2023-05-02/samsung-bans-chatgpt-and-other-generative-ai-use-by-staff-after-leak)
- [TechRadar: Samsung workers leaked company secrets](https://www.techradar.com/news/samsung-workers-leaked-company-secrets-by-using-chatgpt)
- [Cybernews: Lessons learned from ChatGPT's Samsung leak](https://cybernews.com/security/chatgpt-samsung-leak-explained-lessons/)
- [AI Incident Database: Incident 768](https://incidentdatabase.ai/cite/768/)

---

## 2. Local/On-Premise AI Models

### 2.1 Meta Llama

- **Llama 4** (April 2025): MoE architecture. Scout (109B total, 17B active) with 10M token context window. Maverick (400B total, 17B active).
- **License:** Llama Community License -- free for most uses, restrictions for very large companies (700M+ monthly active users).
- **Local deployment:** Fully supported via Ollama, vLLM, Hugging Face TGI.
- **Strengths:** Large ecosystem, well-documented, strong community, Meta's continued investment.

### 2.2 Mistral

- **Mistral Large 3** (123B parameters, 128k context, 80+ languages) -- now Apache 2.0 licensed.
- **Mistral Small 4** -- also Apache 2.0, optimized for speed and efficiency.
- **European origin:** Headquarters in Paris. Relevant for GDPR-conscious organizations.
- **Strengths:** Strong multilingual performance, permissive licensing, efficient inference.

### 2.3 DeepSeek

- **DeepSeek V3:** 671B MoE (37B active), MIT license, general-purpose.
- **DeepSeek R1:** Same architecture, specialized in chain-of-thought reasoning. 97.3% on MATH-500 (highest open model score).
- **License:** MIT -- fully open.

**Critical security note on DeepSeek's cloud service:**
- DeepSeek stores data on **Chinese servers**, subject to Chinese national security laws.
- Hidden code found transmitting user data to China Mobile's registry (CMPassport.com).
- Weak encryption, potential SQL injection flaws, unencrypted data transmissions identified.
- **Banned** by US Navy, NASA, and multiple government agencies.
- Under GDPR investigation in Italy, Ireland, Belgium, Netherlands, France.
- **Italy blocked the app** pending investigation.

**Key distinction for students:** DeepSeek's **open-weight models** (V3, R1) can be downloaded and run locally with full privacy. The **cloud service** (deepseek.com, mobile app) has serious data security concerns. The model weights themselves are safe; the cloud service is not.

Sources:
- [Hugging Face: 10 Best Open-Source LLMs](https://huggingface.co/blog/daya-shankar/open-source-llms)
- [n8n Blog: Best open-source LLMs 2025](https://blog.n8n.io/open-source-llm/)
- [Red Hat: State of open source AI models 2025](https://developers.redhat.com/articles/2026/01/07/state-open-source-ai-models-2025)
- [NPR: DeepSeek data safety](https://www.npr.org/2025/01/31/nx-s1-5277440/deepseek-data-safety)
- [Krebs on Security: DeepSeek risks](https://krebsonsecurity.com/2025/02/experts-flag-security-privacy-risks-in-deepseek-ai-app/)
- [Euronews: DeepSeek EU data privacy issues](https://www.euronews.com/next/2025/02/06/what-are-the-data-privacy-issues-plaguing-chinese-ai-deepseek-in-the-eu)

### 2.4 Tools for Running Models Locally

**Ollama:**
- CLI-first, developer-oriented.
- API-compatible (OpenAI-compatible endpoint).
- ~20% faster inference than LM Studio in benchmarks.
- Better at handling concurrent requests (request batching).
- Production-ready for self-hosted deployments.

**LM Studio:**
- GUI application, better for exploration and prototyping.
- 1000+ pre-configured models (2025 update).
- MLX engine support on macOS (more memory-efficient).
- Team collaboration features added in 2025.
- Mobile companion for iOS/Android.

**Other tools:** vLLM (high-throughput serving), Hugging Face TGI, llama.cpp (underlying engine for both Ollama and LM Studio).

Sources:
- [Openxcell: LM Studio vs Ollama](https://www.openxcell.com/blog/lm-studio-vs-ollama/)
- [HyScaler: LM Studio vs Ollama 2025](https://hyscaler.com/insights/ollama-vs-lm-studio/)
- [SitePoint: LM Studio vs Ollama Complete Comparison](https://www.sitepoint.com/lm-studio-vs-ollama/)

### 2.5 Performance: Local vs Cloud

| Aspect | Cloud API | Local (Consumer GPU) |
|--------|-----------|---------------------|
| Model quality | Frontier models (GPT-4o, Claude Opus, Gemini Ultra) | Good but behind frontier (7B-70B open models) |
| Latency | Network-dependent, typically 0.5-2s first token | Lower latency for small models, GPU-dependent |
| Throughput | Effectively unlimited (rate limits apply) | Limited by GPU VRAM and compute |
| Privacy | Data leaves your machine | Data stays on your machine |
| Cost model | Per-token (pay as you go) | Upfront hardware + electricity |
| Offline use | No | Yes |
| Max model size | Unlimited (provider handles it) | Limited by VRAM (24GB on RTX 4090) |

---

## 3. The Security Tradeoff

### 3.1 Privacy-Preserving AI Research

**Federated Learning (FL)** has emerged as the primary paradigm for privacy-preserving collaborative AI training. Key developments:

- FL enables multiple clients to train a shared global model **without centralizing data**.
- Active research areas: differential privacy integration, model compression for communication efficiency, defense against adversarial attacks on FL systems.
- Applications: healthcare (cross-hospital model training), finance (fraud detection across institutions), IoT/edge computing.
- **Challenges noted in 2025 research:** high communication costs, statistical heterogeneity (non-IID data), persistent privacy vulnerabilities despite protections.

**Key papers (2024-2025):**
- "Federated Learning: A Survey on Privacy-Preserving Collaborative Intelligence" (arXiv, 2025) -- comprehensive survey of FL architecture and protocols.
- "Exploring Privacy Mechanisms and Metrics in Federated Learning" (Artificial Intelligence Review, 2025) -- reviews centralized and decentralized FL approaches.
- "Deep Federated Learning: A Systematic Review" (Frontiers in Computer Science, 2025) -- systematic review of methods, applications, challenges.

Sources:
- [arXiv: Federated Learning Survey](https://arxiv.org/html/2504.17703v3)
- [Springer: Privacy Mechanisms in FL](https://link.springer.com/article/10.1007/s10462-025-11170-5)
- [Frontiers: Deep Federated Learning Review](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2025.1617597/full)

### 3.2 NIST AI Risk Management Framework

Released January 2023, significantly expanded through 2024-2025 with companion playbooks and profiles.

**Four core functions:** Govern, Map, Measure, Manage -- applied across the full AI lifecycle.

**2025 updates signal a shift** from planning to operationalizing AI risk management:
- Governance now spans full lifecycle: concept, design, data acquisition, model development, testing, deployment, monitoring, retirement.
- Sector regulators (CFPB, FDA, SEC, FTC, EEOC) increasingly reference NIST AI RMF principles.
- Voluntary but becoming de facto standard for demonstrating responsible AI use.

Sources:
- [NIST: AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [IS Partners: NIST AI RMF 2025 Updates](https://www.ispartnersllc.com/blog/nist-ai-rmf-2025-updates-what-you-need-to-know-about-the-latest-framework-changes/)
- [Wiz: NIST AI RMF tl;dr](https://www.wiz.io/academy/ai-security/nist-ai-risk-management-framework)

### 3.3 EU AI Act -- Data Requirements

**Effective timeline:**
- August 2025: General-purpose AI rules take effect. New models must comply immediately.
- August 2027: Deadline for already-deployed models to comply.
- Penalties: up to 15M EUR or 3% of worldwide annual turnover.

**Key data requirements:**
- Providers must publish **detailed summaries of training data** across six categories: publicly accessible datasets, private third-party datasets, crawled/scraped sources, user-sourced data, synthetic datasets, other.
- High-risk AI systems require high-quality training data: relevant, representative, error-free, complete.
- Special categories of personal data may only be processed for bias detection when no alternative exists.

**November 2025: Digital Omnibus** proposed to simplify overlapping EU digital regulation (GDPR, Data Governance Act, AI Act).

Sources:
- [EU AI Act: Article 10 - Data and Data Governance](https://artificialintelligenceact.eu/article/10/)
- [European Parliament: EU AI Act overview](https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence)
- [Ethyca: AI data becomes legal liability](https://www.ethyca.com/news/ai-data-becomes-legal-liability-impact-of-the-eu-ai-act)

---

## 4. What Students Should Know

### 4.1 Data You Should NEVER Send to Consumer Cloud AI

1. **Source code** (proprietary, client, or employer code)
2. **Personal data** (names, emails, phone numbers, SSNs, medical records)
3. **NDA-protected content** (client documents, partnership details)
4. **Authentication credentials** (passwords, API keys, tokens, certificates)
5. **Financial data** (bank details, salary info, internal financial reports)
6. **Legal documents** (contracts under review, attorney-client communications)
7. **Patient/medical data** (HIPAA violations carry severe penalties)
8. **Internal strategic documents** (business plans, unreleased product details)

**Alarming statistic:** Sensitive data makes up **34.8% of employee ChatGPT inputs** in 2025, up from 11% in 2023.

### 4.2 How to Evaluate If Cloud AI Is Appropriate

Decision framework for students:

1. **Data sensitivity check:** Would you post this data publicly? If no, think twice about free-tier AI.
2. **Tier check:** Are you using consumer (free) or enterprise tier? Consumer tiers train on your data.
3. **Regulatory check:** Does the data fall under GDPR, HIPAA, NDA, or other regulations?
4. **Reversibility check:** Once submitted, data cannot be "unsubmitted" -- assume it persists.
5. **Alternative check:** Can you use a local model instead? For code completion, summarization, and drafting, local 7B-13B models are often sufficient.

### 4.3 Corporate AI Policies -- Real Examples

**Common policy elements (from analysis of 18+ corporate AI policies):**
- Prohibited data categories (as listed above)
- Approved AI tools list (enterprise tiers only)
- Human review requirements for AI-generated output
- Disclosure requirements (when AI was used)
- Training and awareness mandates

**Notable corporate responses:**
- **Samsung:** Banned all external AI after the 2023 leak; later developed internal tools.
- **US Government agencies (Navy, NASA):** Banned DeepSeek cloud service.
- **Multiple EU regulators:** Investigating DeepSeek data practices.

**Trend:** 76% of organizations have established governance structures and policies to guide AI use (2025), but 60% still lack ethical AI policies.

Sources:
- [Morgan Lewis: AI Usage Policies Revisited](https://www.morganlewis.com/blogs/sourcingatmorganlewis/2025/12/ai-usage-policies-revisited-structure-trends-and-transparency)
- [Nexos.ai: AI policy for companies](https://nexos.ai/blog/ai-policy-for-companies/)
- [Corporate Compliance Insights: Planning Your AI Policy](https://www.corporatecomplianceinsights.com/planning-your-ai-policy-start-here/)

---

## 5. Statistics and Numbers

### 5.1 AI Adoption and Policies

- **88%** of organizations report regular AI use in at least one business function (2025, up from 78% in 2024). -- [McKinsey: State of AI 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)
- **76%** have established governance structures and policies for AI use.
- **60%** of businesses using AI are **not** developing ethical AI policies.
- **74%** fail to address potential biases in AI systems.
- **34.8%** of employee ChatGPT inputs contain sensitive data (up from 11% in 2023).

### 5.2 AI-Related Data Breaches

- **13%** of organizations reported breaches of AI models or applications; **97%** of those lacked proper AI access controls. -- [IBM: Cost of a Data Breach Report 2025](https://www.ibm.com/reports/data-breach)
- AI-driven attack breaches cost **USD 4.49M** on average.
- Shadow AI breaches averaged **USD 4.63M**.
- **16%** of all breaches in 2025 involved attackers using AI (37% phishing, 35% deepfakes).
- Gartner predicts **40%+ of AI-related data breaches** will arise from cross-border GenAI misuse by 2027. -- [Gartner Press Release](https://www.gartner.com/en/newsroom/press-releases/2025-02-17-gartner-predicts-forty-percent-of-ai-data-breaches-will-arise-from-cross-border-genai-misuse-by-2027)

### 5.3 Cost Comparison: Cloud API vs Local GPU

**Cloud API costs (2025):**
- GPT-4-class performance: ~$0.40/million tokens (down from $20/M in late 2022).
- Budget models: fractions of a cent per million tokens.
- Cloud GPU rental (H100): $1.49-$6.98/hour depending on provider.

**Local hardware costs:**
- RTX 4090 (24GB VRAM): $1,600-$2,000 purchase price.
- RTX 5090 (32GB VRAM): ~$2,000-$2,500.
- Electricity: ~$90-$135/year for 8hr/day usage; ~$500-$750/year for continuous operation.
- Can run 7B-13B models efficiently; 70B models with quantization.

**Breakeven analysis:**
- Below ~50K-100K daily requests: Cloud API is cheaper (avoids idle GPU costs).
- Above 100K daily requests: Self-hosted is cheaper (with 50%+ GPU utilization).
- For moderate usage (1-10M tokens/day): Single RTX 4090 achieves ROI within 6-12 months.
- Quantization reduces operational costs by 60-70%.

Sources:
- [Introl: Inference Unit Economics](https://introl.com/blog/inference-unit-economics-true-cost-per-million-tokens-guide)
- [GMI Cloud: GPU Cloud Cost Comparison 2025](https://www.gmicloud.ai/blog/2025-gpu-cloud-cost-comparison)
- [Introl: Local LLM Hardware Pricing Guide 2025](https://introl.com/blog/local-llm-hardware-pricing-guide-2025)

---

## Key Takeaways for Lecture 1

1. **The free tier trap:** Every major provider trains on your free-tier data by default. Enterprise tiers and APIs do not. Students must understand this distinction.

2. **Local models have closed the gap:** 2025 was the year open-source models reached parity with cloud models in many tasks. Running locally is now practical, not just theoretical.

3. **DeepSeek paradox:** The models (open weights, MIT license) are excellent and safe to run locally. The cloud service has serious data security concerns due to Chinese data laws.

4. **Samsung is the canonical cautionary tale:** Three engineers, one month, three separate leaks of proprietary data. This will happen to students' future employers if policies are not in place.

5. **Regulation is catching up:** NIST AI RMF, EU AI Act, and sector regulators are all creating frameworks. Students entering the workforce will need to understand compliance requirements.

6. **The decision is not binary:** It is not "cloud vs local" but rather "which data, to which tier, for which purpose." A decision framework is more useful than a blanket rule.
