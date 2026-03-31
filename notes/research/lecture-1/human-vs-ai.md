# Research: Human vs AI — Lecture 1

Status: draft
Date: 2026-03-31

---

## 1. Narrow AI (ANI) vs AGI vs ASI

### 1.1 Definitions and Taxonomy

The three-level taxonomy of artificial intelligence:

- **ANI (Artificial Narrow Intelligence):** AI optimized for a single task or narrow domain (e.g., chess, image classification, language translation). All current deployed AI systems are ANI.
- **AGI (Artificial General Intelligence):** Hypothetical AI with human-level cognitive abilities across virtually all domains. Can transfer knowledge, reason abstractly, learn new tasks without retraining.
- **ASI (Artificial Superintelligence):** Hypothetical AI that vastly surpasses human intelligence in every domain — science, creativity, social reasoning, and beyond.

**Key source:** Bostrom, Nick. *Superintelligence: Paths, Dangers, Strategies.* Oxford University Press, 2014. Bostrom defines superintelligence as "any intellect that greatly exceeds the cognitive performance of humans in virtually all domains of interest." He outlines two classes of control mechanisms: capability control (limiting the superintelligence's abilities) and motivation selection (aligning its goals with humanity's interests).

- [Superintelligence — Wikipedia](https://en.wikipedia.org/wiki/Superintelligence)
- [Superintelligence, Ten Years On — Quillette (2024)](https://quillette.com/2024/07/02/superintelligence-10-years-on-nick-bostrom-ai-safety-agi/)
- [Taking superintelligence seriously — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0016328715000932)
- Bostrom, N. "Future Progress in Artificial Intelligence: A Survey of Expert Opinion." [PDF](https://nickbostrom.com/papers/survey.pdf)
- Alfonseca, M. et al. "Superintelligence Cannot be Contained: Lessons from Computability Theory." *JAIR*, 2021. [PDF](https://jair.org/index.php/jair/article/download/12202/26642/25638)

### 1.2 Searle's Chinese Room Argument (Strong vs Weak AI)

**Key source:** Searle, John. "Minds, Brains, and Programs." *Behavioral and Brain Sciences*, 3(3), 1980, pp. 417-424.

Core argument: A person in a room following symbol-manipulation rules for Chinese characters can produce perfectly sensible Chinese responses without understanding a single word. Therefore, a computer executing a program cannot have genuine understanding or consciousness, regardless of how intelligent its behavior appears.

**Searle's distinction:**
- **Strong AI:** "The appropriately programmed computer really is a mind" — computers can literally understand and have cognitive states.
- **Weak AI:** Computers simulate thought; their apparent understanding is not genuine understanding.

The paper became the most influential target article in *Behavioral and Brain Sciences* history, generating decades of commentaries.

- [Chinese Room Argument — Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/chinese-room/)
- [Chinese Room Argument — Internet Encyclopedia of Philosophy](https://iep.utm.edu/chinese-room-argument/)
- [Original paper — University of Colorado](https://rintintin.colorado.edu/~vancecd/phil201/Searle.pdf)
- [Chinese Room — Britannica](https://www.britannica.com/topic/Chinese-room-argument)

### 1.3 Current AGI Debate (2024-2026): Key Positions

**Sam Altman (OpenAI):** In January 2026, declared "we are now confident we know how to build AGI." Has stated we are "beginning to slip past human-level AGI toward superintelligence." Timeline: approximately 5 years from 2023-24 remarks.

**Dario Amodei (Anthropic):** At Davos 2026: "I'm more confident than I've ever been that we're close to powerful capabilities... in the next 2-3 years." Predicted AI would replace all software developer work within a year and reach "Nobel-level" scientific research in multiple fields within two years.

**Demis Hassabis (Google DeepMind):** Said current AI systems are "nowhere near" human-level AGI. Estimated 50% chance AGI might be achieved within the decade, but not through models built exactly like today's. Identified key gaps: few-shot learning, continuous learning, better long-term memory, improved reasoning and planning. "Maybe we need one or two more breakthroughs before we'll get to AGI."

**Yann LeCun (Meta):** The strongest skeptic. "We're never going to get to human-level intelligence by training LLMs or by training on text only. We need the real world." Calls AGI "a marketing term" and "complete BS" as a concept. Advocates retiring the term, using "Powerful AI" or "human-level AI" instead. Within hours of LeCun's public statements, Hassabis responded on X: "Yann is just plain incorrect here."

**Key disagreement:** Whether current LLM-based approaches can scale to AGI (Altman, Amodei say yes with iteration; LeCun says fundamentally no; Hassabis says breakthroughs needed).

- [AI luminaries at Davos clash — Fortune (Jan 2026)](https://fortune.com/2026/01/23/deepmind-demis-hassabis-anthropic-dario-amodei-yann-lecun-ai-davos/)
- [AI's Biggest Minds Public Fight — Medium/Predict (Dec 2025)](https://medium.com/predict/ais-biggest-minds-just-had-a-public-fight-over-whether-general-intelligence-even-exists-and-872c317f63a9)
- [Progress Towards AGI and ASI: 2024-Present — CloudWalk](https://www.cloudwalk.io/ai/progress-towards-agi-and-asi-2024-present)
- [Will we have AGI by 2030? — 80,000 Hours](https://80000hours.org/ai/guide/when-will-agi-arrive/)

---

## 2. What AI Does Better Than Humans

### 2.1 Pattern Recognition at Scale

AI systems can process and identify patterns in datasets far beyond human capability. In medical imaging, AI performs ultra-rapid analysis of large datasets, with performance reaching or exceeding specialist-level accuracy in specific diagnostic tasks.

However, a 2024 study showed humans still excel at recognizing objects in unusual poses — state-of-the-art deep networks and large vision-language models are "systematically brittle" on unusual poses.

- [Toward human-level concept learning: Pattern benchmarking — ScienceDirect (2023)](https://www.sciencedirect.com/science/article/pii/S2666389923001435)
- [Comparison: humans and AI recognizing objects in unusual poses — arXiv (2024)](https://arxiv.org/html/2402.03973v2)
- [Computers Now Recognize Patterns Better Than Humans — Scientific American](https://www.scientificamerican.com/article/computers-now-recognize-patterns-better-than-humans-can/)

### 2.2 Specific Benchmarks: AI Surpassing Human Performance

| Domain | System | Year | Result |
|--------|--------|------|--------|
| **Chess** | IBM Deep Blue | 1997 | Beat world champion Garry Kasparov 3.5-2.5 in a 6-game match. First defeat of a reigning world chess champion by a computer under tournament conditions. |
| **Chess** | DeepMind AlphaZero | 2017 | Thoroughly beat Stockfish-8 (world's top chess engine) after just 4 hours of self-play training. |
| **Go** | DeepMind AlphaGo | 2016 | Beat Lee Sedol (one of world's top Go players) 4-1 in Seoul. Go has ~10^170 possible board positions vs chess's ~10^47. |
| **Image recognition** | Microsoft ResNet | 2015 | 3.57% error rate on ImageNet, surpassing estimated human error rate of 5.1%. He et al., "Deep Residual Learning for Image Recognition." |
| **Protein folding** | DeepMind AlphaFold2 | 2020 | Predicted >90% of protein structures with experimental accuracy at CASP14, crushing all previous benchmarks. |
| **Protein folding** | AlphaFold3 | 2024 | 50% more accurate than best traditional physics-based methods on PoseBusters benchmark. First AI to surpass physics-based tools for biomolecular structure prediction. Won 2024 Nobel Prize in Chemistry. |

- [Deep Blue — IBM History](https://www.ibm.com/history/deep-blue)
- [AlphaGo vs Lee Sedol — Wikipedia](https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol)
- [Time for AI to cross human performance in ImageNet — AI Impacts](https://aiimpacts.org/time-for-ai-to-cross-the-human-performance-range-in-imagenet-image-classification/)
- He et al. "Deep Residual Learning for Image Recognition." [arXiv (2015)](https://arxiv.org/pdf/1512.03385)
- [Machine learning cracked protein-folding, won 2024 Nobel Prize — The Conversation](https://theconversation.com/machine-learning-cracked-the-protein-folding-problem-and-won-the-2024-nobel-prize-in-chemistry-240937)
- [AlphaFold3 — Google Blog](https://blog.google/innovation-and-ai/products/google-deepmind-isomorphic-alphafold-3-ai-model/)

### 2.3 Speed, Throughput, and Consistency

AI advantages:
- **Speed:** Can process millions of data points per second where humans process a handful.
- **Consistency:** Does not fatigue, does not have emotional variation, maintains identical performance at hour 1 and hour 10,000.
- **Volume:** Can analyze entire genomic datasets, financial markets, or satellite imagery archives in time frames impossible for humans.
- **Scalability:** Performance can be improved by adding compute; human expertise does not scale this way.

### 2.4 Specific Numbers

- AlphaFold2 predicted structures of ~200 million proteins (virtually all known proteins) — a task that would have taken experimental biologists centuries.
- GPT-4 class models process ~100,000 tokens per minute; a fast human reader processes ~250 words/minute.
- Deep Blue evaluated 200 million chess positions per second.

---

## 3. What Humans Do Better Than AI

### 3.1 Causal Reasoning

**Key source:** Pearl, Judea & Mackenzie, Dana. *The Book of Why: The New Science of Cause and Effect.* Basic Books, 2018.

Pearl argues AI has been "handicapped by an incomplete understanding of what intelligence really is." His prescription: teach machines to understand the question "why."

**Pearl's Ladder of Causation (three levels):**
1. **Association** (seeing/observing): "What if I see X?" — Current ML operates here.
2. **Intervention** (doing): "What if I do X?" — Requires causal models.
3. **Counterfactual** (imagining): "What if I had done X instead?" — The highest level, requires genuine causal understanding.

Pearl notes that GPT/ChatGPT handles causal problems "in a very sloppy way." Example: asked what would happen if a rifleman refrained from shooting in a firing squad scenario, the system responds "It's illegal to shoot in California." This illustrates how current AI conflates correlation with causation.

- [Judea Pearl on LLMs and Causal Reasoning — causalens](https://causalai.causalens.com/resources/blog/judea-pearl-on-the-future-of-ai-llms-and-need-for-causal-reasoning/)
- [To Build Truly Intelligent Machines, Teach Them Cause and Effect — Quanta Magazine (2018)](https://www.quantamagazine.org/to-build-truly-intelligent-machines-teach-them-cause-and-effect-20180515/)
- [Why AI needs to understand consequences — Nature (2023)](https://www.nature.com/articles/d41586-023-00577-1)

### 3.2 Common Sense Reasoning

**Key source:** Levesque, Hector; Davis, Ernest; Morgenstern, Leora. "The Winograd Schema Challenge." *AAAI*, 2012. [PDF](https://cdn.aaai.org/ocs/4492/4492-21843-1-PB.pdf)

The Winograd Schema Challenge tests pronoun disambiguation requiring common-sense knowledge about the physical and social world. Example: "The trophy doesn't fit in the suitcase because it is too [big/small]." — switching one word reverses the correct answer.

**Key finding (2023):** LLMs have defeated the Winograd Schema Challenge but the original authors concede this does not demonstrate common sense — "full-blooded thinking is still far off." Any purely linguistic test is unlikely to tell us much about genuine common sense or intelligence.

**Additional source:** Marcus, Gary & Davis, Ernest. *Rebooting AI: Building Artificial Intelligence We Can Trust.* Pantheon, 2019. Argues current deep learning approaches lack genuine understanding and common sense.

- [Winograd Schema Challenge Results — IEEE Spectrum](https://spectrum.ieee.org/winograd-schema-challenge-results-ai-common-sense-still-a-problem-for-now)
- [The Defeat of the Winograd Schema Challenge — arXiv (2022)](https://arxiv.org/pdf/2201.02387)
- [Language, common sense, and the Winograd Schema Challenge — ScienceDirect (2023)](https://www.sciencedirect.com/science/article/abs/pii/S0004370223001777)
- [Winograd Schema Challenge — NYU (Davis)](https://cs.nyu.edu/~davise/papers/WinogradSchemas/WS.html)

### 3.3 Transfer Learning Across Domains

Humans learn a concept in one domain and effortlessly apply it to another. A child who learns "balance" on a bicycle transfers that concept to surfing, walking on ice, or carrying a tray. AI systems require massive retraining for each new domain or task.

There remains "a large gap between AI pattern recognition and human-level concept learning, as humans can learn amazingly well even under uncertainty from just a few examples and are capable of generalizing these concepts to solve new conceptual problems."

### 3.4 Creativity

Research findings are mixed:
- AI can improve creative performance and facilitate integration of distant concepts.
- However, people ascribe lower creativity to AI-produced work when they know the source.
- Human creativity involves intentionality, lived experience, emotional resonance, and cultural context that AI lacks.
- AI creativity is fundamentally pattern recombination from training data; human creativity can produce genuinely novel concepts from first principles.

- [Humans vs AI: preference for human-created artwork — PMC (2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10319694/)
- [Humans as Creativity Gatekeepers — Journal of Business and Psychology (2023)](https://link.springer.com/article/10.1007/s10869-023-09910-x)

### 3.5 Ethical Judgment and Empathy

A surprising finding: AI responses were rated as more compassionate than human expert crisis responders in controlled studies. However, this reflects linguistic pattern matching, not genuine empathy.

For ethical judgment: "AI produces outputs but does not interpret meaning... the real learning occurs when students weigh ethical, cultural, and contextual factors — judgments that no algorithm can provide." Overreliance on AI reduces independent critical analysis.

- [AI perceived as more compassionate than human experts — Nature Communications Psychology (2024)](https://www.nature.com/articles/s44271-024-00182-6)
- [Empathy: AI vs Human — JMIR Mental Health (2024)](https://mental.jmir.org/2024/1/e62679)

### 3.6 Understanding "Why" Not Just "What"

Humans naturally build causal models of the world. AI systems (especially LLMs) excel at identifying statistical patterns ("what tends to co-occur") but struggle with genuine explanatory reasoning ("why does X cause Y"). This maps directly to Pearl's Ladder of Causation — current AI primarily operates at Level 1 (association), while humans routinely operate at Levels 2 and 3.

---

## 4. AI in the Physical World — Challenges

### 4.1 Moravec's Paradox

**Key source:** Moravec, Hans. *Mind Children.* Harvard University Press, 1988.

"It is comparatively easy to make computers exhibit adult level performance on intelligence tests or playing checkers, and difficult or impossible to give them the skills of a one-year-old when it comes to perception and mobility."

**Evolutionary explanation:** Sensorimotor skills required millions of years of evolution to develop, while abstract reasoning is evolutionarily recent. The "deliberate process we call reasoning is the thinnest veneer of human thought, effective only because it is supported by this much older and much more powerful sensorimotor knowledge."

- [Moravec's Paradox — Wikipedia](https://en.wikipedia.org/wiki/Moravec's_paradox)
- [Moravec's Paradox and its Implications — Epoch AI](https://epoch.ai/gradient-updates/moravec-s-paradox)

### 4.2 Robotics: Current State

**Boston Dynamics:** Atlas (latest-generation humanoid) navigates industrial sites, identifies and lifts objects with near-human precision. Still limited to structured environments.

**Figure AI:** Figure 02 humanoid robot can fold clothes, clean tables, pack shopping bags. Tested in BMW factories for parts assembly. Powered by OpenAI large models.

2024 was called "the year of talking AI"; 2025 is called "the year of walking AI."

- [Rise of AI in Robotics: 2025 Breakthroughs in Physical AI — Forward Future](https://www.forwardfuture.ai/p/the-rise-of-embodied-ai)
- [Comprehensive Survey on Embodied Intelligence — SciOpen (2024)](https://www.sciopen.com/article/10.26599/AIR.2024.9150042)

### 4.3 Autonomous Driving

**SAE Levels (Society of Automotive Engineers):**
- Level 0: No automation
- Level 1: Driver assistance (adaptive cruise control)
- Level 2: Partial automation (lane keeping + adaptive cruise)
- Level 3: Conditional automation (car drives itself in specific conditions, human must be ready)
- Level 4: High automation (car drives itself in defined areas, no human needed)
- Level 5: Full automation (any conditions, anywhere)

**Current state (2025):**
- Level 2 dominates the market.
- Waymo operates robotaxi services (Level 4) in limited US cities since 2024.
- No system has achieved Level 5.
- Operating costs: $4.5-5.5/km for autonomous taxis vs $0.6/km for personal cars. McKinsey estimates cost parity (<$1.2/km) not until 2035.
- Safety incidents increasing as more autonomous vehicles deploy.
- China and Germany lead regulatory frameworks; US and South Korea in deployment.

- [State of Autonomous Driving in 2025 — AUTOCRYPT](https://autocrypt.io/state-of-autonomous-driving-2025/)
- [SAE Levels of Driving Automation Refined — SAE](https://www.sae.org/blog/sae-j3016-update)

### 4.4 Why Physical AI Is Harder

**The sim-to-real gap:** Models trained in simulation fail when transferred to real environments. Simulations cannot capture the full complexity, variability, and unpredictability of real-world physics.

**Key differences from digital AI:** "Unlike digital AI, which operates primarily in symbolic, linguistic, or pixel domains, Physical AI grounds cognition within the constraints of physics, embodiment, and thermodynamics."

**Core challenges (from 2024-2025 surveys):**
1. Hardware limitations
2. Model generalization across physical environments
3. Physical world understanding (noise, friction, deformation)
4. Multimodal integration (vision + touch + proprioception)
5. Safety constraints (cannot "undo" physical actions)
6. Semi-duplex problem: most embodied AI processes instructions fully before acting, struggling with dynamic environments

**Solutions being explored:** Domain randomization, digital twins, real-to-sim-to-real pipelines, foundation models for robotics.

- [Physical AI: Bridging the Sim-to-Real Divide — Springer (2025)](https://link.springer.com/article/10.1007/s44379-025-00050-y)
- [Digital Twins to Embodied AI: Review — OAE Publish (2025)](https://www.oaepublish.com/articles/ir.2025.11)
- [Embodied AI Survey — arXiv (2025)](https://arxiv.org/pdf/2505.14235)
- [Embodied AI Paper List — GitHub (SYSU)](https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List)

---

## 5. The Generalization Argument

### 5.1 Chollet's ARC-AGI Benchmark

**Key source:** Chollet, Francois. "On the Measure of Intelligence." arXiv, 2019.

Chollet defined intelligence as **skill-acquisition efficiency on unknown tasks** — how quickly can you learn new skills? He created the Abstraction and Reasoning Corpus (ARC) to measure this, focusing on tasks that "humans solve effortlessly yet AI finds challenging."

**ARC tests fundamental gaps in AI:**
- Ability to generalize from limited examples
- Synthesis of symbolic rules
- Flexible application of known concepts in novel contexts

**2024 results:** OpenAI featured ARC-AGI-1 as a leading benchmark for their o3-preview model. ARC-AGI-2 introduced adversarial task construction and contamination resistance to measure generalization under abstraction pressure.

- [ARC Prize — What is ARC-AGI?](https://arcprize.org/arc-agi)
- [ARC Prize 2024: Technical Report — arXiv](https://arxiv.org/pdf/2412.04604)
- [ARC Prize 2025 Results and Analysis](https://arcprize.org/blog/arc-prize-2025-results-analysis)
- [Comprehensive Behavioral Dataset for ARC — Nature Scientific Data (2025)](https://www.nature.com/articles/s41597-025-05687-1)

### 5.2 AI Generalization vs Human Reasoning

**AI excels at:**
- Interpolation within training distribution
- Pattern matching across massive datasets
- Statistical generalization (finding regularities in data)
- Scaling: more data and compute improve performance predictably

**Humans excel at:**
- Extrapolation beyond training distribution
- Reasoning from first principles
- One-shot and zero-shot learning in novel domains
- Building causal models from minimal observations
- Compositional reasoning (combining known concepts in novel ways)

The gap: "There is still a large gap between AI pattern recognition and human-level concept learning." Humans learn under uncertainty from just a few examples and generalize to novel problems. AI systems require orders of magnitude more data for comparable tasks and remain brittle outside their training distribution.

---

## Summary Table: Human vs AI Strengths

| Capability | AI Advantage | Human Advantage |
|------------|-------------|-----------------|
| Pattern recognition at scale | Large datasets, speed | Novel/unusual patterns, few-shot |
| Consistency | No fatigue, no emotion | Adaptive judgment |
| Data processing volume | Millions of records/sec | Contextual interpretation |
| Causal reasoning | Statistical correlation | Genuine "why" understanding |
| Common sense | Language patterns | Physical/social world knowledge |
| Creativity | Recombination at scale | Genuine novelty, intentionality |
| Physical interaction | Structured environments | Any environment, adaptive |
| Ethical judgment | Consistent rules application | Context, empathy, values |
| Generalization | Within training distribution | Across domains, first principles |
| Speed | Orders of magnitude faster | Efficient with minimal data |

---

## Key References (Consolidated)

### Books
1. Bostrom, Nick. *Superintelligence: Paths, Dangers, Strategies.* Oxford University Press, 2014.
2. Pearl, Judea & Mackenzie, Dana. *The Book of Why: The New Science of Cause and Effect.* Basic Books, 2018.
3. Marcus, Gary & Davis, Ernest. *Rebooting AI: Building Artificial Intelligence We Can Trust.* Pantheon, 2019.
4. Moravec, Hans. *Mind Children.* Harvard University Press, 1988.

### Seminal Papers
5. Searle, John. "Minds, Brains, and Programs." *Behavioral and Brain Sciences*, 3(3), 1980.
6. Chollet, Francois. "On the Measure of Intelligence." arXiv:1911.01547, 2019.
7. He, Kaiming et al. "Deep Residual Learning for Image Recognition." arXiv:1512.03385, 2015.
8. Levesque, H.; Davis, E.; Morgenstern, L. "The Winograd Schema Challenge." *AAAI*, 2012.
9. Silver, D. et al. "Mastering the Game of Go with Deep Neural Networks and Tree Search." *Nature*, 529, 2016.
10. Jumper, J. et al. "Highly accurate protein structure prediction with AlphaFold." *Nature*, 596, 2021.

### Recent Surveys and Papers (2024-2025)
11. ARC Prize 2024 Technical Report. arXiv:2412.04604.
12. "A Review of Embodied AI and the Road Ahead." arXiv:2505.14235, 2025.
13. "Physical AI: Bridging the Sim-to-Real Divide." Springer, 2025.
14. "Comprehensive Survey on Embodied Intelligence." SciOpen, 2024.
15. "Third-party evaluators perceive AI as more compassionate." *Nature Communications Psychology*, 2024.
