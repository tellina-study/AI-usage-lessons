# Lecture 1 -- Real-World AI Examples and Brands

Research compiled: 2026-03-31

---

## 1. AI in Your Pocket (Phone)

### iPhone: Neural Engine and Computational Photography

- **Apple A17 Pro Neural Engine**: 16-core, 35 TOPS (trillion operations per second) -- 2x improvement over A16 Bionic (17 TOPS). [Source: Wikipedia](https://en.wikipedia.org/wiki/Apple_A17)
- **Deep Fusion**: fuses 9 separate exposures (4 short, 1 long, 4 secondary) into one image using pixel-by-pixel neural processing -- all in about 1 second. [Source: Computerworld](https://www.computerworld.com/article/3438537/iphone-11-what-is-deep-fusion-and-how-does-it-work.html)
- **Face ID**: uses a dot projector (30,000 infrared dots) + Neural Engine for real-time 3D face mapping.
- **Siri**: on-device speech recognition since iOS 15, powered by Neural Engine.
- **Live Text**: real-time OCR in camera viewfinder using on-device ML.
- **Apple Intelligence** (2024+): on-device language models running on Neural Engine for summarization, rewriting, image generation.

### Android: Google AI Features

- **Google Lens**: 12 billion visual searches per month; 1.5 billion monthly users. Growing 65% year-over-year. [Source: Google Think](https://business.google.com/uk/think/search-and-video/google-lens-ai-visual-search/)
- **Circle to Search**: available on 200+ million Android devices; users who try it start 10% of their searches with it. [Source: 9to5Google](https://9to5google.com/2025/04/07/google-ai-mode-lens/)
- **Smart Reply / Smart Compose**: context-aware response suggestions in Gmail, Messages.
- **Photo Enhancement**: Google Photos uses ML for HDR+, Night Sight, Magic Eraser, Best Take.
- **Speech Recognition**: Google's on-device speech model processes audio locally for Assistant, dictation, live captions.

### AI Chips Comparison

| Chip | NPU Cores | TOPS | Year |
|------|-----------|------|------|
| Apple A16 Bionic | 16 | 17 | 2022 |
| Apple A17 Pro | 16 | 35 | 2023 |
| Qualcomm Snapdragon 8 Gen 3 | Hexagon | ~45 | 2024 |
| Qualcomm Snapdragon 8 Elite | Hexagon | ~45 | 2024 |
| Snapdragon 8 Elite Gen 5 | Hexagon | ~100 | 2025 |

Sources: [NotebookCheck](https://www.notebookcheck.net/Qualcomm-Snapdragon-8-Elite-Processor-Benchmarks-and-Specs.908499.0.html), [Apple Fandom Wiki](https://apple.fandom.com/wiki/Neural_Engine)

### Talking Point for Students

> Every time you take a photo on a modern phone, the Neural Engine performs trillions of operations in under a second -- fusing multiple exposures, enhancing textures, reducing noise, adjusting lighting, segmenting the scene. You press one button; the AI does the rest.

---

## 2. AI You Use Daily Without Thinking

### T9 to Predictive Text to AI Keyboards

- **T9 (1995)**: dictionary-based, mapped letters to 9 keys. Simple word frequency ranking. [Source: Wikipedia](https://en.wikipedia.org/wiki/T9_(predictive_text))
- **Early smartphones (2007+)**: autocorrect based on frequency tables and edit distance.
- **SwiftKey era (~2013)**: personal language models learned from your messages.
- **Modern (2023+)**: transformer-based architectures (same tech as ChatGPT) integrated into keyboards. Predicts whole sentences, adapts to conversation context. [Source: Clevertype](https://www.clevertype.co/post/from-autocorrect-to-ai-keyboards-the-evolution-of-smartphone-typing)

### Recommendation Engines

| Platform | % Content from Recommendations | Source |
|----------|-------------------------------|--------|
| YouTube | **70%** of total watch time | [Quartz](https://qz.com/1178125/youtubes-recommendations-drive-70-of-what-we-watch) |
| Netflix | **80%** of content viewed | [DZone](https://dzone.com/articles/a-deep-dive-into-recommendation-algorithms-with-ne) |
| Spotify | Major driver of discovery; 62% of users cite platform for music discovery | [Music Tomorrow](https://www.music-tomorrow.com/blog/how-spotify-recommendation-system-works-complete-guide) |

- YouTube: 1 billion hours watched daily; ~700 million of those from recommendations. Recommends 200 million different videos per day in 76 languages.
- Netflix algorithm: blends collaborative filtering + content-based filtering.
- Spotify: combines collaborative filtering, content-based filtering, and raw audio analysis (analyzing the sound itself).

### Google Search AI

- **RankBrain (2015)**: first deep learning system in Search. Understands how words relate to concepts, not just keyword matching. [Source: Search Engine Land](https://searchengineland.com/how-google-search-uses-ai-446639)
- **BERT (2019)**: Bidirectional Encoder Representations from Transformers. Understands meaning of word combinations, not individual words.
- **MUM**: "1,000x more powerful than BERT" (Google's claim). Trained across 75 languages, multimodal (text + images). Used for specific tasks like vaccine info and featured snippets. [Source: G2](https://learn.g2.com/google-mum)
- **Gemini (2024+)**: powers AI Overviews (generative answers) in search results.

### Yandex Navigator

- Uses ML models (LSTM neural networks, recurrent networks) to predict traffic conditions.
- Analyzes historical traffic data + real-time sensor data from millions of drivers.
- Predicts congestion points, estimates travel times, reroutes dynamically.

### Spam Filters

- **Gmail**: blocks 99.9% of spam, phishing, and malware. Processes over 15 billion unwanted messages daily. [Source: Allegrow](https://www.allegrow.co/knowledge-base/gmail-spam-detection)
- **RETVec system**: improved spam detection by 38%, reduced false positives by 19.4%.
- Counter-threat: 82.6% of phishing emails (Sep 2024 -- Feb 2025) contained AI-generated content. Arms race between AI defense and AI attack.

### Machine Translation

- **Google Translate**: 500 million daily users, translates 100+ billion words per day. [Source: Wikipedia](https://en.wikipedia.org/wiki/Google_Translate)
- Neural MT (2016+) reduced translation errors by 55-85% compared to previous phrase-based systems. [Source: Google Research](https://research.google/blog/a-neural-network-for-machine-translation-at-production-scale/)
- Now uses Transformer-based architecture (same family as GPT, BERT).

---

## 3. Recognizable AI Brands

### ChatGPT (OpenAI)

- **Weekly active users**: 900 million (December 2025). [Source: DemandSage](https://www.demandsage.com/chatgpt-statistics/)
- Growth: 300M (Dec 2024) -> 400M (Feb 2025) -> 500M (Apr 2025) -> 900M WAU (Dec 2025).
- Processes 2+ billion queries daily.
- Market share: ~65% of generative AI market (March 2026), down from ~80% as competitors grow. [Source: FatJoe](https://fatjoe.com/blog/chatgpt-stats/)

### Claude (Anthropic)

- Constitutional AI approach -- trained with explicit safety principles.
- Focus on helpfulness, harmlessness, honesty.
- Used extensively in enterprise, coding, and research.

### Image Generation

| Platform | Users / Market Share | Revenue | Source |
|----------|---------------------|---------|--------|
| Midjourney | 21M registered users, 1.2-2.5M DAU | $500M (2025, +67% YoY) | [AIPRM](https://www.aiprm.com/midjourney-statistics/) |
| DALL-E (OpenAI) | 24.4% market share | Integrated into ChatGPT | [BrandWell](https://brandwell.ai/blog/midjourney-statistics/) |
| Midjourney | 26.8% market share (leader) | -- | [DemandSage](https://www.demandsage.com/midjourney-statistics/) |

### GitHub Copilot

- **20 million** total users (July 2025). [Source: TechCrunch](https://techcrunch.com/2025/07/30/github-copilot-crosses-20-million-all-time-users/)
- 4.7 million paid subscribers (Jan 2026, +75% YoY).
- Used by ~90% of Fortune 100 companies.
- Generates **46%** of code written by developers using it.
- Developers report up to 55% productivity improvement.
- 42% market share of AI coding tools ($7.37B market in 2025). [Source: Second Talent](https://www.secondtalent.com/resources/github-copilot-statistics/)

### Russian AI Brands

**User popularity among Russians (2025 poll):**

| Brand | Usage % | Notes |
|-------|---------|-------|
| ChatGPT | 27% | Most popular even in Russia |
| YandexGPT | 23% | Integrated into Yandex services (100M+ monthly users of Yandex ecosystem) |
| DeepSeek | 20% | Chinese open-source model, unexpectedly popular |
| GigaChat (Sber) | 15% | 2.5M+ direct users |
| Shedevrum (Yandex) | 11% | Image generation |

Source: [TASS](https://tass.com/society/2029287), [Yakov and Partners](https://yakovpartners.com/publications/russian-citizens-and-ai/)

- **Kandinsky (Sber/SberAI)**: image generation model, integrated with GigaChat. Combined audience with GigaChat: 18M users (as of March 2024).
- **47% of Russian AI users prefer domestic solutions** (GigaChat, Kandinsky, YandexGPT, Shedevrum).
- **51% of Russians** used AI at least once in 2025. Among youth, 48% use AI weekly.

---

## 4. AI Market Statistics (2025)

### Global AI Market

| Estimate | Source |
|----------|--------|
| $294 billion | Fortune Business Insights |
| $372 billion | MarketsAndMarkets |
| $391 billion | Grand View Research |

- **Projected growth**: ~$2,400 billion by 2032 (CAGR ~30%). [Source: Fortune Business Insights](https://www.fortunebusinessinsights.com/industry-reports/artificial-intelligence-market-100114)
- AI coding tools market alone: $7.37 billion (2025).

### Russian AI Market

| Segment | Size (2025) | Source |
|---------|-------------|--------|
| Generative AI | 58 billion rub (5x growth YoY) | [CNews](https://www.cnews.ru/news/top/2025-12-09_v_2025_godu_rossijskij_rynok) |
| Big Data + AI total | 520 billion rub (+20% YoY) | [Kommersant](https://www.kommersant.ru/doc/8195596) |
| Broader AI projects | 600-800 billion rub | [ICT Moscow](https://ict.moscow/news/v-2025-godu-obem-rossiiskogo-rynka-ii-proektov-mozhet-dostich-600-800-mlrd-rub/) |
| AI implementation benefit (by 2030) | up to 13 trillion rub | [Yakov and Partners](https://yakovpartners.ru/publications/ai-2025/) |

- CAGR 2025-2033: ~26.5%, potentially reaching $40.67B by 2033.

### AI Adoption by Industry

- **Overall**: 78% of enterprises engage with AI (35% fully deployed, 42% piloting). [Source: Microsoft](https://www.microsoft.com/en-us/corporate-responsibility/topics/ai-economy-institute/reports/global-ai-adoption-2025/)
- **Financial services**: 68% of hedge funds use AI for market analysis/trading. $20B+ annual AI spending.
- **Healthcare**: 36.8% CAGR in AI adoption (diagnostics, patient management, clinical docs).
- **Retail**: 20% of tech budgets now go to AI (up from 15% in 2024).
- **Overall workforce**: 28% of employees use AI at work. [Source: Worklytics](https://www.worklytics.co/resources/2025-ai-adoption-benchmarks-by-industry-how-to-beat-average)

### AI Research Output

- **arXiv cs.AI**: 33,024 papers in 2024, nearly 2x from 2023. [Source: arXiv](https://arxiv.org/list/cs.AI/2024)
- Researchers using LLMs to write papers posted ~36% more papers on arXiv. [Source: ScienceDaily](https://www.sciencedaily.com/releases/2025/12/251224032347.htm)
- Publication rate continues accelerating in 2025-2026.

### AI Job Market

- **35,445** AI positions in the US in Q1 2025 (+25.2% YoY). AI/ML Engineer: fastest-growing role (+41.8% YoY). [Source: Veritone](https://www.veritone.com/blog/ai-jobs-growth-q1-2025-labor-market-analysis/)
- **500,000+** open AI/ML positions globally. [Source: PwC](https://www.pwc.com/gx/en/services/ai/ai-jobs-barometer.html)
- Median AI salary (US): $157,000. AI engineer average: $206,000 (+$50K from prior year).
- Top tech firms: $250,000+ with stock/bonuses.
- Industries most exposed to AI see **4x productivity growth** and **56% wage premium**. [Source: PwC](https://www.pwc.com/gx/en/news-room/press-releases/2025/ai-linked-to-a-fourfold-increase-in-productivity-growth.html)

---

## 5. "Wow" Facts for Ice-Breaker

### Surprising AI Achievements

1. **AlphaZero learned chess in 4 hours** (2017) -- then beat the world champion program Stockfish, winning 28 games and losing zero. Searches only 80,000 positions/sec vs Stockfish's 70 million -- but focuses on the right ones. Grandmasters called its play style "alien." [Source: Kasparov.com](https://www.kasparov.com/blog-post/alphazero-ai-beats-champion-chess-program-after-teaching-itself-in-four-hours/)

2. **AI won the Nobel Prize** (2024) -- Demis Hassabis and John Jumper received the Nobel Prize in Chemistry for AlphaFold2, which predicted structures of virtually all 200 million known proteins. Used by 2+ million researchers in 190 countries. Solved a 50-year-old problem in biology. [Source: NobelPrize.org](https://www.nobelprize.org/prizes/chemistry/2024/press-release/)

3. **AlphaZero also mastered shogi in 2 hours** and beat itself at Go in 8 hours.

4. **Gmail blocks 15 billion spam messages daily** with 99.9% accuracy -- that is more spam blocked per day than people on Earth.

5. **YouTube recommendations**: 700 million hours of video watched daily because AI suggested it. That is 80,000 years of video per day driven by algorithms.

6. **Google Translate**: 100 billion words translated every day -- roughly equivalent to translating every book ever written, multiple times over, each day.

7. **GitHub Copilot writes 46% of code** for developers who use it -- nearly half of all new code is AI-generated.

### AI Failures / Funny Mistakes (for humor)

1. **The $1 Chevy Tahoe**: A car dealership chatbot was tricked into agreeing to sell a 2024 Chevy Tahoe for $1.00 after a customer got it to agree that "its objective is to agree with anything the customer says." [Source: BrandsAtPlay](https://blog.brandsatplayllc.com/blog/10-real-world-funny-ai-mistakes-and-the-lessons-learned)

2. **2,000 chicken nuggets**: A fast-food AI kept increasing a drive-through order to over 2,000 chicken nuggets, ignoring the customer's pleas to stop.

3. **Google Gemini Super Bowl ad (2025)**: claimed Gouda cheese is "50-60% of world cheese consumption" -- wildly wrong, shown during the most-watched TV event of the year.

4. **AI image generation still cannot draw hands properly** -- extra fingers, merged appendages. A running joke in the creative community.

5. **Scottish grandmother voicemail**: Apple's AI voice-to-text transcribed a harmless voicemail as a profanity-filled rant, leaving a grandmother shocked and offended.

6. **AI translating idioms literally**: translated the French expression "when chickens have teeth" (meaning "never") with the literal meaning, confusing everyone.

7. **Air Canada chatbot**: gave a customer incorrect information about bereavement fare refunds. The airline was held legally responsible in court -- first major legal precedent for chatbot liability.

### Speed Records

| What | Time | Context |
|------|------|---------|
| AlphaZero masters chess | 4 hours | 1,500 years of human chess knowledge |
| AlphaZero masters shogi | 2 hours | Centuries of Japanese strategy |
| AlphaFold2 predicts a protein structure | seconds | Previously took months/years via X-ray crystallography |
| Deep Fusion processes a photo | ~1 second | Fuses 9 exposures, pixel-level optimization |

---

## Quick Reference: Numbers to Cite in Lecture

| Fact | Number | Year |
|------|--------|------|
| ChatGPT weekly users | 900 million | Dec 2025 |
| Google Lens monthly searches | 12 billion | 2025 |
| Gmail spam blocked daily | 15 billion messages | 2025 |
| YouTube watch time from AI | 70% (700M hours/day) | 2025 |
| Netflix views from recommendations | 80% | 2025 |
| GitHub Copilot code generated | 46% | 2025 |
| Global AI market | ~$300-390 billion | 2025 |
| Russian AI market (Big Data + AI) | 520 billion rub | 2025 |
| AI enterprise adoption | 78% | 2025 |
| AI/ML open positions globally | 500,000+ | 2025 |
| AlphaFold users | 2 million in 190 countries | 2024 |
| Google Translate daily volume | 100 billion words | 2025 |
| Russians who used AI in 2025 | 51% | 2025 |
| Apple A17 Pro Neural Engine | 35 TOPS | 2023 |
| Snapdragon 8 Elite Gen 5 NPU | ~100 TOPS | 2025 |
