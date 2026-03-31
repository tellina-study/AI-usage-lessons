# Lecture 1: History and Scientific Definitions of AI

Research for applied AI course at MGTU Baumana. Compiled 2026-03-31.

---

## Part 1: Scientific Definitions of AI

### 1.1 Alan Turing (1950)

**Source:** Turing, A.M. (1950). "Computing Machinery and Intelligence." *Mind*, 59(236), 433-460.

Turing did not define "artificial intelligence" directly. Instead, he opened his paper with:

> "I propose to consider the question, 'Can machines think?'"

He immediately noted that defining "think" and "machine" in the usual way would be dangerous, as it would reduce the question to a Gallup poll. Instead, he proposed the **Imitation Game** (now known as the **Turing Test**): an interrogator communicates via text with a human and a machine, and must determine which is which. If the machine can fool the interrogator consistently, it demonstrates intelligent behavior.

Turing's approach was **pragmatic, not definitional** -- he replaced the philosophical question "Can machines think?" with the operational question "Can machines do what we (as thinking entities) can do?"

**Key quote from the paper:**

> "Are there imaginable digital computers which would do well in the imitation game?"

**Citation:** [Original paper (PDF), University of Maryland Baltimore County](https://courses.cs.umbc.edu/471/papers/turing.pdf); [Oxford Academic (Mind journal)](https://academic.oup.com/mind/article-abstract/LIX/236/433/986238)

---

### 1.2 John McCarthy et al. (1955 proposal, 1956 conference)

**Source:** McCarthy, J., Minsky, M.L., Rochester, N., Shannon, C.E. (1955). "A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence." August 31, 1955.

The Dartmouth proposal is credited with **coining the term "artificial intelligence."** The key passage:

> "The study is to proceed on the basis of the conjecture that every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it."

McCarthy later refined his personal definition:

> "Artificial intelligence is the science and engineering of making intelligent machines."

The proposal was authored by four people: **John McCarthy** (Dartmouth), **Marvin Minsky** (Harvard), **Nathaniel Rochester** (IBM), and **Claude Shannon** (Bell Labs). The conference took place in the summer of 1956 at Dartmouth College, Hanover, New Hampshire.

**Citation:** [Original proposal (PDF), Stanford](http://jmc.stanford.edu/articles/dartmouth/dartmouth.pdf); [Stanford formal archives](https://www-formal.stanford.edu/jmc/history/dartmouth/dartmouth.html); [AI Magazine reprint](https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/1904)

---

### 1.3 Russell & Norvig -- Four Approaches (1995, 4th ed. 2020)

**Source:** Russell, S.J., Norvig, P. *Artificial Intelligence: A Modern Approach.* Pearson. (1st ed. 1995, 4th ed. 2020).

Russell and Norvig organize definitions of AI into a 2x2 matrix crossing two dimensions:
- **Thinking vs. Acting**
- **Humanly vs. Rationally**

| | Humanly | Rationally |
|---|---------|-----------|
| **Thinking** | Cognitive modeling -- replicating human thought processes in machines | Laws of thought -- using formal logic to derive correct conclusions |
| **Acting** | Turing Test -- behaving indistinguishably from a human | Rational agent -- acting to achieve the best expected outcome given beliefs and goals |

**Detailed breakdown:**

1. **Thinking humanly (cognitive science approach):** Build programs that think the way humans think. Requires a correct theory of human cognition. Example: cognitive architectures like ACT-R, SOAR.

2. **Thinking rationally (logicist approach):** Encode "laws of thought" as formal logic. The machine reasons correctly from premises to conclusions. Limitation: not all intelligence is logical; computational intractability of pure logic.

3. **Acting humanly (Turing Test approach):** A machine passes if a human interrogator cannot distinguish it from a human in conversation. Requires: natural language processing, knowledge representation, automated reasoning, machine learning, and (for a "total" Turing Test) computer vision and robotics.

4. **Acting rationally (rational agent approach):** An agent that acts to achieve the best expected outcome. Russell & Norvig favor this approach as the most general. It subsumes the others and handles cases where there is no provably correct action, requiring the agent to act under uncertainty.

**Citation:** [Berkeley chapter 1 excerpt (PDF)](https://people.eecs.berkeley.edu/~russell/aima1e/chapter01.pdf); [OpenLearn / Open University](https://www.open.edu/openlearn/mod/oucontent/view.php?id=116249&section=2.4)

---

### 1.4 ISO/IEC 22989:2022 -- International Standard

**Source:** ISO/IEC 22989:2022. *Information technology -- Artificial intelligence -- Artificial intelligence concepts and terminology.* ISO, 2022.

Two key definitions from sections 3.1.3 and 3.1.4:

**Artificial intelligence (AI)** [as a discipline]:
> "Research and development of mechanisms and applications of AI systems."

**Artificial intelligence system (AI system):**
> "Engineered system that generates outputs such as content, forecasts, recommendations or decisions for a given set of human-defined objectives."

This is the first internationally standardized definition. It is deliberately broad and technology-neutral, covering ML, rule-based, statistical, and hybrid systems. An amendment (DAmd 1) is being developed to add terminology for generative AI.

**Citation:** [ISO standard page](https://www.iso.org/standard/74296.html); [ISO Online Browsing Platform](https://www.iso.org/obp/ui/#iso:std:iso-iec:22989:ed-1:v1:en); [ANSI Blog overview](https://blog.ansi.org/ansi/incits-iso-iec-22989-2022-2023-ai-terminology/)

---

### 1.5 Kaplan & Haenlein (2019)

**Source:** Kaplan, A., Haenlein, M. (2019). "Siri, Siri, in my hand: Who's the fairest in the land? On the interpretations, illustrations, and implications of artificial intelligence." *Business Horizons*, 62(1), 15-25.

> "A system's ability to correctly interpret external data, to learn from such data, and to use those learnings to achieve specific goals and tasks through flexible adaptation."

This definition emphasizes three components: (1) interpretation of data, (2) learning, and (3) flexible goal-directed adaptation. It is widely cited in business and management research.

**Citation:** [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0007681318301393); [ResearchGate](https://www.researchgate.net/publication/328761767)

---

### 1.6 Summary Table of Definitions

| Author/Source | Year | Definition / Core Idea |
|---|---|---|
| Turing | 1950 | "Can machines think?" -- replaced by the Imitation Game (behavioral test) |
| McCarthy et al. | 1955 | "Every aspect of intelligence can be so precisely described that a machine can simulate it" |
| McCarthy | ~1960s | "The science and engineering of making intelligent machines" |
| Russell & Norvig | 1995/2020 | Four quadrants: thinking/acting x humanly/rationally; favor "rational agent" |
| Kaplan & Haenlein | 2019 | "A system's ability to interpret data, learn from it, and achieve goals through flexible adaptation" |
| ISO/IEC 22989 | 2022 | "Engineered system that generates outputs... for human-defined objectives" |

---

## Part 2: History Timeline

### 1950 -- The Turing Test

Alan Turing publishes "Computing Machinery and Intelligence" in *Mind* journal. Proposes the Imitation Game as a practical test for machine intelligence. This paper is foundational: it frames the entire field before the field even has a name.

### 1956 -- Dartmouth Conference (Birth of AI)

The Dartmouth Summer Research Project on Artificial Intelligence, organized by McCarthy, Minsky, Rochester, and Shannon. Six-week workshop at Dartmouth College. The term "artificial intelligence" is coined. Attendees include future founders of major AI labs. This is considered the **official birth of AI as a field.**

### 1966 -- ELIZA

Joseph Weizenbaum at MIT creates ELIZA (described in January 1966 in *Communications of the ACM*). ELIZA uses pattern matching and substitution to simulate conversation. The most famous script, DOCTOR, simulates a Rogerian psychotherapist.

**Why it matters:** ELIZA demonstrated the "ELIZA effect" -- people attributed understanding and empathy to a simple pattern-matching program. Weizenbaum's own secretary reportedly asked him to leave the room so she could talk privately with ELIZA. This raised fundamental questions about human-computer interaction that remain relevant to LLM-era chatbots.

Named after Eliza Doolittle from Shaw's *Pygmalion*.

### 1974-1980 -- First AI Winter

**What happened:** Funding collapsed, labs closed, researchers left the field.

**Why:**
1. **Overpromising:** Early AI researchers predicted human-level AI within a decade (Minsky, 1967: "Within a generation... the problem of creating 'artificial intelligence' will substantially be solved"). Reality fell far short.
2. **The Lighthill Report (1973):** Sir James Lighthill's report to the British Science Research Council devastated UK AI funding. He identified "combinatorial explosion" as a fundamental barrier and criticized AI for failing to deliver on promises. UK government essentially eliminated AI research funding.
3. **DARPA funding cuts (1974):** DARPA had been AI's largest funder. When projects failed to deliver practical military applications, funding was cut. The Mansfield Amendment further restricted military funding to research with direct military relevance.
4. **Technical limitations:** Insufficient computational power, no effective learning algorithms, inability to handle real-world complexity.

### 1980s -- Expert Systems Boom

Expert systems (rule-based AI) became commercially successful. Companies invested heavily in systems like XCON (DEC), MYCIN (medical diagnosis), and Dendral (chemical analysis). The Japanese Fifth Generation Computer project (1982) triggered a global AI arms race. Lisp machines became a profitable hardware niche. AI industry revenue reached billions of dollars by mid-1980s.

### 1987-1993 -- Second AI Winter

**What happened:** The expert systems market collapsed. Specialized AI hardware companies (Symbolics, Lisp Machines Inc.) went bankrupt. Government funding was slashed again.

**Why:**
1. **Hardware economics:** General-purpose workstations from Apple, Sun, and IBM became more powerful and cheaper than specialized Lisp machines. Symbolics went bankrupt by 1991.
2. **Expert system limitations:** The "qualification problem" -- these systems worked in narrow domains but made catastrophic errors on anything unusual. They could not learn or adapt.
3. **Maintenance costs:** Knowledge bases required constant updating by expensive knowledge engineers. Total cost of ownership exceeded value.
4. **Government retreat:** DARPA leadership under Jack Schwarz (1987) dismissed expert systems as "clever programming" and cut AI funding "deeply and brutally." The Japanese Fifth Generation project failed to meet its goals.
5. **Hype cycle collapse:** Companies that had over-invested based on inflated expectations pulled back.

### 1997 -- Deep Blue vs. Kasparov

IBM's Deep Blue defeated world chess champion Garry Kasparov in a six-game match in New York City (May 11, 1997). Score: 3.5-2.5. Deep Blue evaluated 200 million chess positions per second. This was the **first defeat of a reigning world chess champion by a computer** under tournament conditions.

Significance: Demonstrated that specialized AI could surpass human performance in a well-defined domain. But Deep Blue was brute-force search, not "intelligence" in a general sense -- it could not play checkers, let alone hold a conversation.

### 2011 -- IBM Watson on Jeopardy!

IBM's Watson DeepQA system defeated Jeopardy! champions Ken Jennings (74-game winner) and Brad Rutter ($3.25M all-time earner) in February 2011. Watson won $77,147 vs. Jennings' $24,000 and Rutter's $21,600.

Significance: Watson demonstrated natural language understanding -- parsing puns, wordplay, and complex questions. It represented a shift from brute-force computation (Deep Blue) to language processing. However, Watson's subsequent commercial applications largely failed to deliver on promises.

### 2012 -- AlexNet / ImageNet Breakthrough

Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton at the University of Toronto submitted AlexNet to the ImageNet Large Scale Visual Recognition Challenge (September 30, 2012). AlexNet reduced the top-5 error rate from 26.2% to 15.3%, beating the nearest competitor by 9.8 percentage points.

**Why this was the turning point for deep learning:**
- Trained on two NVIDIA GTX 580 GPUs (in Krizhevsky's bedroom)
- Proved that deep convolutional neural networks, trained on GPUs, dramatically outperform hand-engineered features
- Yann LeCun called it "an unequivocal turning point in the history of computer vision"
- Cited over 172,000 times (Google Scholar)
- Launched the modern deep learning era: within a decade, neural networks would synthesize voices, beat Go champions, model language, and generate artwork

### 2014 -- Generative Adversarial Networks (GANs)

Ian Goodfellow et al. publish "Generative Adversarial Nets" (June 2014, NeurIPS). Introduced a framework where two neural networks (generator and discriminator) compete in a minimax game. The generator learns to produce realistic data; the discriminator learns to distinguish real from generated.

Significance: GANs opened the door to **generative AI** -- machines that create new content (images, audio, video) rather than just classifying existing data. This was a conceptual leap: from AI as analysis to AI as creation.

### 2016 -- AlphaGo vs. Lee Sedol

Google DeepMind's AlphaGo defeated Lee Sedol, one of the world's top Go players, 4-1 in Seoul (March 9-15, 2016). Go was considered the "grand challenge" of game AI because its search space (~10^170 positions) makes brute-force approaches impossible.

**Why it mattered more than Deep Blue:**
- AlphaGo used deep neural networks + Monte Carlo tree search, not brute force
- It *learned* from human games and self-play, rather than being hand-programmed
- Many experts had predicted AI would not beat top Go players for another decade
- The Korea Baduk Association awarded AlphaGo an honorary 9 dan rank

### 2017 -- "Attention Is All You Need" (Transformer Architecture)

Vaswani, A. et al. (2017). "Attention Is All You Need." Published June 12, 2017. Eight authors at Google.

Introduced the **Transformer** architecture, based entirely on self-attention mechanisms, eliminating recurrence and convolutions. Key innovations: multi-head attention, positional encoding, parallelizable training.

**Impact:** Over 173,000 citations (among the top 10 most-cited papers of the 21st century). The Transformer became the foundation for virtually all modern language models: BERT, GPT, T5, PaLM, Claude, Gemini. This paper is arguably the single most consequential technical contribution to the current AI era.

**Citation:** [arXiv:1706.03762](https://arxiv.org/abs/1706.03762)

### 2020 -- GPT-3

OpenAI released GPT-3, a language model with **175 billion parameters** (100x GPT-2's 1.5B). Trained on 570 GB of text. Demonstrated few-shot learning: GPT-3 could perform tasks it was never explicitly trained for, given just a few examples in the prompt.

Key result: In news article generation tests, humans could only distinguish real from generated articles 52% of the time (essentially a coin flip).

GPT-3 was not publicly available as a chatbot but was accessible via API, primarily used by developers and researchers. It showed that scale alone could produce emergent capabilities.

### 2022 -- ChatGPT Launch (The Pivot Moment)

**November 30, 2022:** OpenAI released ChatGPT (based on GPT-3.5) as a free public chatbot.

**Speed of adoption:** 1 million users in 5 days. By 2025: 700 million weekly users, 18 billion messages per week (~10% of global adult population). No technology in history has been adopted this fast.

**Why this was the pivot moment:** See Part 3 below.

### 2023 -- GPT-4, Claude, Multimodal Era

- **March 2023:** OpenAI releases GPT-4, a multimodal model (text + images)
- **March 2023:** Anthropic launches Claude
- **December 2023:** Google launches Gemini (natively multimodal: text, images, audio, video)
- The "AI race" intensifies: Meta (LLaMA open-source), Mistral (European), and others enter the field
- RLHF (Reinforcement Learning from Human Feedback) and Constitutional AI become standard alignment techniques

### 2024 -- AlphaFold Nobel Prize, AI Agents

- **October 2024:** Demis Hassabis and John Jumper (Google DeepMind) win the **Nobel Prize in Chemistry** for AlphaFold2, which predicted the 3D structure of virtually all 200 million known proteins. Shared with David Baker for computational protein design. First Nobel Prize awarded for AI-driven scientific discovery.
- **September 2024:** OpenAI releases o1 (reasoning model) -- "thinking before answering" becomes a new paradigm
- **AI agents** emerge as a major paradigm: systems that combine LLMs with tools, data, and autonomous decision-making to complete multi-step tasks

### 2025 -- Current State

- **Reasoning models:** o3, o4-mini (OpenAI), Claude reasoning capabilities (Anthropic), Gemini reasoning (Google). Reasoning becomes a standard capability: the model "thinks step by step" before answering.
- **Flagship convergence:** GPT-5 family, Claude Opus 4/4.5, Gemini 3.0 -- reasoning, tool use, and conversation quality merge into single models
- **AI agents go mainstream:** Claude Code (autonomous development), OpenAI Operator (web tasks), Gemini Deep Research (multi-source synthesis). Gartner projects 40% of enterprise apps will embed AI agents by mid-2026.
- **Anthropic's MCP (Model Context Protocol):** Emerges as a standard for connecting LLMs to tools and data
- **Cost efficiency:** Reasoning capabilities that cost $60/M tokens in 2024 cost under $1/M tokens by late 2025
- **Industry shift:** "Doing more with less" -- smaller, purpose-built models for specific tasks instead of ever-larger general models

---

## Part 3: The Pivot Moment -- How LLMs Changed the Meaning of "AI"

### Before ChatGPT (pre-November 2022)

For most people and many professionals, "AI" meant:
- **Narrow ML systems:** recommendation engines, spam filters, image classifiers, voice assistants
- **Expert tools:** systems for specialists (data scientists, engineers)
- **Something distant:** either a sci-fi concept or an invisible backend optimization
- **Academic pursuit:** a research field with periodic hype cycles and winters

The public understanding was shaped by Hollywood (Terminator, Her, Ex Machina) more than by actual technology. Most people had never directly interacted with an AI system in a way that felt like "intelligence."

### The Shift

ChatGPT was not a new technology -- Transformers (2017), GPT-3 (2020), and InstructGPT (2022) already existed. The revolution was **packaging**: placing a powerful LLM behind a simple chat interface, free, accessible to anyone with a browser. As noted by researchers, "the true catalyst for the boom was not the invention of a new technology, but the packaging of that existing, powerful technology into a product that anyone could use."

### After ChatGPT (post-November 2022)

"AI" now means, for most people:
- **Conversational agents:** systems you talk to, that understand and generate natural language
- **Generative tools:** systems that create text, images, code, music, video
- **Accessible technology:** available to anyone, not just specialists
- **Daily utility:** writing assistant, code helper, research partner, tutor

The term "Generative AI" became a household phrase. "Gen AI" and "GAI" entered common vocabulary. The public perception of AI became **LLM-centric**: AI = models that generate text, images, and video.

### Academic Perspective on the Paradigm Shift

Vasant Dhar (Communications of the ACM, 2024) identifies four paradigm shifts in AI:
1. **Symbolic AI / Expert Systems** (1960s-1980s): human knowledge encoded as rules
2. **Statistical ML** (1990s-2000s): learning patterns from data using probability and statistics
3. **Deep Learning** (2012-2020): neural networks learning features directly from raw data (vision, speech, text)
4. **Foundation Models / Generative AI** (2020-present): pre-trained on massive corpora, general-purpose, configurable to many tasks via prompting

The shift from paradigm 3 to paradigm 4 is qualitatively different from previous shifts. Earlier AI systems were **narrow** -- trained for one task, deployed for one task. Foundation models are **general** -- trained broadly, adapted to thousands of tasks via natural language instructions. This makes AI feel like "intelligence" to non-specialists for the first time.

**Key scholarly sources:**
- Dhar, V. (2024). "The Paradigm Shifts in Artificial Intelligence." *Communications of the ACM*. [ACM Digital Library](https://dl.acm.org/doi/10.1145/3664804); [arXiv preprint](https://arxiv.org/pdf/2308.02558)
- Chakravarthy, S. "When Did LLMs Define AI?" -- traces how public perception shifted from "AI = narrow ML" to "AI = LLMs." [Medium](https://medium.com/@sriya.chakravarthy1999/when-did-llms-define-ai-e765e9716754)
- Tansley, T. et al. (2024). "Artificial intelligence: reflecting on the past and looking towards the next paradigm shift." *Journal of Experimental & Theoretical Artificial Intelligence*. [Taylor & Francis](https://www.tandfonline.com/doi/full/10.1080/0952813X.2024.2323042)

### Implications for the Course

This shift matters for an applied AI course because:
1. Students come in with an LLM-centric understanding of AI. The course must broaden this to include the full spectrum (optimization, search, planning, probabilistic reasoning, computer vision, robotics).
2. The history of AI winters shows that hype-reality gaps have consequences. Students should understand the current boom in historical context.
3. The definition question is not academic -- it affects regulation (EU AI Act), standards (ISO/IEC 22989), liability, and professional practice.

---

## Sources

### Primary Sources
- [Turing, A.M. (1950). Computing Machinery and Intelligence. Mind, 59(236)](https://academic.oup.com/mind/article-abstract/LIX/236/433/986238)
- [Turing paper full text (PDF)](https://courses.cs.umbc.edu/471/papers/turing.pdf)
- [McCarthy et al. (1955). Dartmouth Proposal (PDF)](http://jmc.stanford.edu/articles/dartmouth/dartmouth.pdf)
- [Dartmouth Proposal (Stanford HTML)](https://www-formal.stanford.edu/jmc/history/dartmouth/dartmouth.html)
- [Vaswani et al. (2017). Attention Is All You Need. arXiv:1706.03762](https://arxiv.org/abs/1706.03762)
- [Goodfellow et al. (2014). Generative Adversarial Nets. NeurIPS](https://arxiv.org/abs/1406.2661)
- [ISO/IEC 22989:2022](https://www.iso.org/standard/74296.html)

### Secondary Sources
- [Dartmouth AI history (Dartmouth College)](https://home.dartmouth.edu/about/artificial-intelligence-ai-coined-dartmouth)
- [AlexNet and ImageNet: The Birth of Deep Learning (Pinecone)](https://www.pinecone.io/learn/series/image-search/imagenet/)
- [How AlexNet Transformed AI (IEEE Spectrum)](https://spectrum.ieee.org/alexnet-source-code)
- [Deep Blue (IBM History)](https://www.ibm.com/history/deep-blue)
- [Watson Jeopardy (IBM History)](https://www.ibm.com/history/watson-jeopardy)
- [AlphaGo vs Lee Sedol (Wikipedia)](https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol)
- [AlphaFold Nobel Prize (NobelPrize.org)](https://www.nobelprize.org/prizes/chemistry/2024/press-release/)
- [ELIZA (Wikipedia)](https://en.wikipedia.org/wiki/ELIZA)
- [AI Winter (Wikipedia)](https://en.wikipedia.org/wiki/AI_winter)
- [AI Winter history (DataCamp)](https://www.datacamp.com/blog/ai-winter)
- [ChatGPT release (History.com)](https://www.history.com/this-day-in-history/november-30/chatgpt-released-openai)
- [Kaplan & Haenlein (2019). Siri, Siri (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S0007681318301393)
- [Dhar, V. (2024). Paradigm Shifts in AI (ACM)](https://cacm.acm.org/research/the-paradigm-shifts-in-artificial-intelligence/)
- [Russell & Norvig Chapter 1 (Berkeley PDF)](https://people.eecs.berkeley.edu/~russell/aima1e/chapter01.pdf)
- [2025: The Year in LLMs (Simon Willison)](https://simonwillison.net/2025/Dec/31/the-year-in-llms/)
- [The First AI Winter (Holloway)](https://www.holloway.com/g/making-things-think/sections/the-first-ai-winter-19741980)
- [The Second AI Winter (Holloway)](https://www.holloway.com/g/making-things-think/sections/the-second-ai-winter-19871993)
