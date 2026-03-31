# AI Classification Taxonomies: Academic Sources for Lecture 1

Research compiled: 2026-03-31

---

## 1. By Task Type

Tasks that AI systems perform, often defined within specific subfields (computer vision, NLP, etc.).

### Core task categories

| Task | Description |
|------|-------------|
| Detection / Recognition | Localizing and identifying objects, entities, patterns in data |
| Segmentation | Partitioning input (image, text, signal) into meaningful regions |
| Generation | Synthesizing new content (text, images, audio, code) |
| Prediction / Forecasting | Estimating future values or states from historical data |
| Classification | Assigning predefined categorical labels to inputs |
| Recommendation | Ranking or filtering items based on user preferences and context |
| Clustering | Grouping unlabeled data points by similarity (unsupervised) |
| Regression | Predicting continuous numerical outputs |

### Academic sources

- **Russell, S. & Norvig, P. (2021).** *Artificial Intelligence: A Modern Approach*, 4th ed. Pearson. -- The standard AI textbook (used at 1500+ universities). Part V covers machine learning task types including classification, regression, clustering. Chapters on NLP, computer vision, and robotics define domain-specific tasks (detection, segmentation, generation).
- **Goodfellow, I., Bengio, Y. & Courville, A. (2016).** *Deep Learning*. MIT Press. -- Chapters 5-6 define supervised learning tasks (classification, regression); Chapter 14 covers generative models; Chapter 20 covers deep generative models. Available: [deeplearningbook.org](https://www.deeplearningbook.org/)
- **LeCun, Y., Bengio, Y. & Hinton, G. (2015).** "Deep Learning." *Nature*, 521, 436-444. DOI: 10.1038/nature14539. -- Landmark review defining how deep learning is applied to recognition, detection, segmentation, and generation tasks across vision, speech, and language.
- **Szelidon, R. (2022).** *Computer Vision: Algorithms and Applications*, 2nd ed. Springer. -- Defines core CV tasks: image classification, object detection, semantic/instance segmentation, image generation, 3D reconstruction.

---

## 2. By Modality

Classification based on the type of input data the AI system processes.

### Core modalities

| Modality | Examples |
|----------|----------|
| Tabular / Numerical | Structured databases, spreadsheets, sensor readings |
| Audio / Speech | Speech recognition, music generation, sound classification |
| Images / Video (Computer Vision) | Object detection, image generation, video understanding |
| Text / Language (NLP) | Translation, summarization, question answering, text generation |
| Multimodal | Systems combining two or more modalities (e.g., text + image) |

### Academic sources

- **Baltrusaitis, T., Ahuja, C. & Morency, L.-P. (2019).** "Multimodal Machine Learning: A Survey and Taxonomy." *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 41(2), 423-443. DOI: 10.1109/TPAMI.2018.2798607. arXiv: 1705.09406. -- Defines five core challenges of multimodal learning: representation, translation, alignment, fusion, co-learning. Establishes taxonomy across modalities (language, visual, acoustic).
- **Bayoudh, K., Knani, R., Hamdaoui, F. & Mtibaa, A. (2022).** "Multimodal Classification: Current Landscape, Taxonomy and Future Directions." *ACM Computing Surveys*, 55(5), 1-41. DOI: 10.1145/3543848. -- Comprehensive taxonomy of multimodal classification approaches across text, image, audio, and tabular data.
- **Xu, P., Zhu, X. & Clifton, D. A. (2023).** "Multimodal Learning with Transformers: A Survey." *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 45(10), 12113-12132. -- Covers how transformer architectures handle different modalities and their combinations.

---

## 3. By Learning Approach

Classification based on the nature of the training signal (supervision).

### Core paradigms

| Paradigm | Training Signal |
|----------|----------------|
| Supervised Learning | Labeled input-output pairs |
| Unsupervised Learning | No labels; discovers structure in data |
| Semi-supervised Learning | Small amount of labeled data + large unlabeled data |
| Self-supervised Learning | Labels derived automatically from the data itself (pretext tasks) |
| Reinforcement Learning | Reward/penalty signal from environment interaction |

### Academic sources

- **Mitchell, T. (1997).** *Machine Learning*. McGraw Hill. -- Foundational textbook. Defines: "A computer program is said to learn from experience E with respect to some task T and some performance measure P, if its performance at task T, as measured by P, improves with experience E." Establishes supervised, unsupervised, and reinforcement learning as the three main paradigms.
- **Bishop, C. M. (2006).** *Pattern Recognition and Machine Learning*. Springer. -- Rigorous Bayesian treatment of supervised (classification, regression) and unsupervised (clustering, dimensionality reduction) learning. Covers generative vs. discriminative approaches within each paradigm.
- **Goodfellow, I., Bengio, Y. & Courville, A. (2016).** *Deep Learning*. MIT Press. -- Part I (Ch. 5) formally defines supervised, unsupervised, semi-supervised, and multi-task learning. Part III covers deep generative models (unsupervised).
- **Sutton, R. S. & Barto, A. G. (2018).** *Reinforcement Learning: An Introduction*, 2nd ed. MIT Press. -- The definitive textbook on RL. Defines RL as learning through interaction with an environment to maximize cumulative reward. Covers tabular methods, function approximation, policy gradient methods. Available: [incompleteideas.net/book/the-book-2nd.html](http://incompleteideas.net/book/the-book-2nd.html)
- **Balestriero, R., Ibrahim, M., ..., LeCun, Y. (2023).** "A Cookbook of Self-Supervised Learning." arXiv: 2304.12210. -- Comprehensive survey of self-supervised learning (SSL). Attributes the term to Yann LeCun, who coined it to distinguish SSL from traditional unsupervised learning. LeCun's "cake analogy" (AAAI 2020): "the bulk of the cake is self-supervised learning, the icing is supervised learning, the cherry is reinforcement learning."

---

## 4. By Capability Level

Classification based on the breadth and depth of intelligence.

### The ANI/AGI/ASI framework

| Level | Description | Status |
|-------|-------------|--------|
| Narrow AI (ANI) | Designed for a specific task; excels within narrow domain | Current reality (all existing AI) |
| General AI (AGI) | Human-level intelligence across all cognitive domains | Hypothetical; active research goal |
| Superintelligence (ASI) | Vastly exceeds human cognitive abilities in all domains | Theoretical/speculative |

### Academic sources

- **Searle, J. (1980).** "Minds, Brains, and Programs." *Behavioral and Brain Sciences*, 3(3), 417-424. -- Introduces the Chinese Room thought experiment. Defines the distinction between **Strong AI** (the computer literally has a mind and understands) and **Weak AI** (the computer is merely a tool for studying the mind). This is the origin of the weak/strong AI dichotomy.
- **Bostrom, N. (2014).** *Superintelligence: Paths, Dangers, Strategies*. Oxford University Press. -- Defines superintelligence as "any intellect that greatly exceeds the cognitive performance of humans in virtually all domains of interest." Analyzes pathways from AGI to ASI, including recursive self-improvement ("intelligence explosion"). Discusses instrumental convergence and existential risk.
- **Goertzel, B. & Pennachin, C. (Eds.) (2007).** *Artificial General Intelligence*. Springer. -- Early academic collection defining AGI as a research program distinct from narrow AI. Proposes criteria for what would constitute general intelligence.
- **Russell, S. & Norvig, P. (2021).** *Artificial Intelligence: A Modern Approach*, 4th ed. -- Chapter 1 discusses the philosophical foundations of AI, including the distinction between systems that think/act humanly vs. rationally, connecting to the weak/strong AI debate.

---

## 5. By Architecture

Classification based on the computational model and structure.

### Major architectural families

| Architecture | Key Characteristics | Era |
|--------------|-------------------|-----|
| Traditional ML | Feature engineering + statistical models (SVM, Random Forest, k-NN) | 1990s-2010s |
| Deep Learning (CNNs, RNNs) | Learned representations via neural networks with many layers | 2012-present |
| Transformers | Self-attention mechanism, parallelizable, foundation for LLMs | 2017-present |
| Diffusion Models | Iterative denoising process for generation | 2020-present |
| RL Architectures | Policy/value networks interacting with environments | 1990s-present |

### Academic sources

- **LeCun, Y., Bengio, Y. & Hinton, G. (2015).** "Deep Learning." *Nature*, 521, 436-444. -- Reviews the evolution from traditional ML to deep learning. Covers CNNs (vision), RNNs/LSTMs (sequences), and backpropagation.
- **Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L. & Polosukhin, I. (2017).** "Attention Is All You Need." *Advances in Neural Information Processing Systems* (NeurIPS), 5998-6008. arXiv: 1706.03762. -- Introduces the Transformer architecture based on self-attention. Over 173,000 citations. Foundation for BERT, GPT, and all modern LLMs.
- **Ho, J., Jain, A. & Abbeel, P. (2020).** "Denoising Diffusion Probabilistic Models." *Advances in Neural Information Processing Systems* (NeurIPS). arXiv: 2006.11239. -- Introduces DDPM, the foundational paper for diffusion-based generative models (Stable Diffusion, DALL-E 2, etc.).
- **Islam, M. R., Matin, A. & Hasan, K. F. (2024).** "A Comprehensive Review of Deep Learning: Architectures, Recent Advances, and Applications." *Information*, 15(12), 755. DOI: 10.3390/info15120755. -- 2024 survey covering the evolution from CNNs and RNNs to transformers, GANs, capsule networks, and graph neural networks.
- **Lin, T., Wang, Y., Liu, X. & Qiu, X. (2022).** "A Survey of Transformers." *AI Open*, 3, 111-132. -- Taxonomy of transformer variants: encoder-only (BERT), decoder-only (GPT), encoder-decoder (T5). Covers architectural modifications for efficiency.
- **Khan, A. et al. (2024).** "A Comprehensive Survey on Applications of Transformers for Deep Learning Tasks." *Expert Systems with Applications*, 241, 122666. -- Surveys transformer applications across NLP, vision, audio, and multimodal domains.

---

## 6. Other Taxonomies

### 6a. Generative vs. Discriminative Models

| Type | Goal | Examples |
|------|------|----------|
| Generative | Models the joint distribution P(X,Y) or P(X); can generate new samples | VAE, GAN, Diffusion, GPT |
| Discriminative | Models the decision boundary P(Y|X) directly | Logistic Regression, SVM, BERT (classification) |

**Academic sources:**

- **Ng, A. Y. & Jordan, M. I. (2001).** "On Discriminative vs. Generative Classifiers: A Comparison of Logistic Regression and Naive Bayes." *Advances in Neural Information Processing Systems* (NeurIPS). -- The foundational theoretical comparison. Shows discriminative models have lower asymptotic error, but generative models converge faster with limited data.
- **Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., Courville, A. & Bengio, Y. (2014).** "Generative Adversarial Nets." *Advances in Neural Information Processing Systems* (NeurIPS), 2672-2680. arXiv: 1406.2661. -- Introduces GANs: a generative model (G) trained adversarially against a discriminative model (D).
- **Du, Y. & Kaelbling, L. P. (2024).** "Towards the Unification of Generative and Discriminative Visual Foundation Models: A Survey." *The Visual Computer*. arXiv: 2312.10163. -- Proposes taxonomy of visual foundation models as generative (GVFMs), discriminative (DVFMs), and multi-modal (MVFMs). Documents the convergence trend.

### 6b. Foundation Models vs. Task-Specific Models

| Type | Description | Examples |
|------|-------------|----------|
| Foundation Model | Pre-trained on broad data at scale; adaptable to many tasks via fine-tuning or prompting | GPT-4, BERT, CLIP, Stable Diffusion |
| Task-Specific Model | Trained from scratch or fine-tuned for one task | Spam classifier, medical image segmenter |

**Academic sources:**

- **Bommasani, R. et al. (2021).** "On the Opportunities and Risks of Foundation Models." Stanford CRFM. arXiv: 2108.07258. -- The paper that coined and defined "foundation model." 100+ authors from Stanford. Argues that scale creates emergent capabilities and that foundation models incentivize homogenization across tasks. Covers language, vision, robotics, healthcare, law.

### 6c. Agentic AI Taxonomy (emerging, 2024-2025)

**Academic source:**

- **Masterman, T. et al. (2024).** "The Landscape of Emerging AI Agent Architectures for Reasoning, Planning, and Tool Use: A Survey." arXiv: 2404.11584. -- Surveys single-agent and multi-agent AI architectures that use planning, reasoning, and tool use. Introduces taxonomy based on degree of agency and coordination.

### 6d. Reactive / Limited Memory / Theory of Mind / Self-Aware

An alternative capability taxonomy sometimes seen in introductory AI courses:

| Type | Description |
|------|-------------|
| Reactive Machines | No memory; responds only to current input (e.g., Deep Blue) |
| Limited Memory | Uses recent past data for decisions (e.g., self-driving cars, current LLMs) |
| Theory of Mind | Understands emotions, beliefs, intentions of others (hypothetical) |
| Self-Aware | Has consciousness and self-awareness (hypothetical) |

**Academic source:**

- **Hintze, A. (2016).** "Understanding the Four Types of Artificial Intelligence." *GovTech / The Conversation*. -- Popularized this four-level taxonomy. While widely cited in educational materials, this is more of a pedagogical framework than a peer-reviewed classification.

---

## Summary: Recommended Primary Sources per Classification

| Classification | Primary Source |
|----------------|---------------|
| By task type | Russell & Norvig (2021); LeCun, Bengio & Hinton (2015) |
| By modality | Baltrusaitis, Ahuja & Morency (2019) |
| By learning approach | Mitchell (1997); Sutton & Barto (2018); Balestriero et al. (2023) |
| By capability level | Searle (1980); Bostrom (2014) |
| By architecture | Vaswani et al. (2017); Ho et al. (2020); LeCun et al. (2015) |
| Generative vs. Discriminative | Ng & Jordan (2001); Goodfellow et al. (2014) |
| Foundation models | Bommasani et al. (2021) |
