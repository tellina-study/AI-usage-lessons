---
lecture: 2
title: "Lecture 2. How Modern Large Models Work— Lecturer's Speech"
length_words: ~4720
duration_min: 75
status: reviewed
version: v1.2
derives_from: [chapter.md v1.2, deck.yaml v1.8 (35 slides), plan-v2-final.md v2.1]
slides_covered: [s01, s02, s02a, s03, s04, s04a, s04b, s05, s06, s07, s08, s08a, s09, s09a, s10, s12, s13, s13a, s14, s15, s16, s17, s17a, s18, s19, s20, s21, s22, s22a, s23, s24, s25, s26, s28, s29]
---

# Lecturer's Speech · Lecture 2 v1.2

**Duration:** 75 minutes.
**Version:** v1.2— issue #156 sync with deck v1.8 polish pass (see Changelog below).

## Changelog v1.1 → v1.2 (issue #156)

- **s01 rewritten entirely**— the old hook about tokenization (`tokenization is fascinating`, EN/RU/code example) replaced with a new hook about the selectivity of human attention ("what are you NOT paying attention to right now?"), synced with the final `slides/s01-live-tokenizer-demo.md`. Section heading updated.
- **s27 (homework) removed**— the slide was pulled from the deck (homework is now delivered only via the seminar, per the Lecture 1 pattern). The bridge phrase at the end of s26 was rewritten without a reference to s27; s25 "first of three frames" → "first of two" (after removing s27, 2 cross-cutting frames remain, not 3); s26 "second frame" → "second, final frame". The pre-flight checklist item about the s27 homework was updated (reference to the seminar instead of the slide).
- **Russification cleanup** (s13a, s14, s15, s16, s23)— pinpoint leftovers of the English `attention`/`attention map` in the lecturer's spoken text were replaced with "внимание" / "карта внимания", in sync with the Russification pass over the deck (build_lec02.py). The Vaswani 2017 paper title was left as a quote of the original with the Russian translation alongside. s24— "attention" → "внимание" in the text of the first "why".
- **s07**— a short spoken addition (2 sentences) about arithmetic was added: GPT-4 at 59%/4%/~0% accuracy on 3/4/5-digit multiplication without tools (arXiv 2410.19730), in sync with the new fact-checked call-out on the slide.
- **s24**— the section heading was kept meaning-based ("The three 'whys' closed"), not renamed to match the slide's exact title bar ("Answers to the questions from the start of the lecture")— the section did not contain a "payoff" or §-references, so no substantive changes were needed beyond the attention fix.
- **Frontmatter**— `slides_covered` (36→35, s27 removed), `derives_from` deck.yaml v1.7→v1.8, `length_words` recomputed, `duration_min` breakdown updated.

## Changelog v1.0 → v1.1

P1 (6 closed):
- **P1-A**— s17 "30%" → "50%" (sync with Liu et al. authoritative + slide).
- **P1-B**— s06 "GPT-3.5— about a hundred thousand tokens" removed (was not on the slide).
- **P1-D**— bridge phrases added to s04a / s13 / s22a divider fragments.
- **P1-E**— "мы с вами" / "давайте" redistributed: 1 → s21 (autoregressive), 1 → s25 (when not an LLM), 1 → s28 (bridge to Lecture 3); 1 removed from s04b for balance.
- **P1-F**— 8th pre-flight item added: "Verify vocab-size GPT-4o ~200k / Llama 3 ~128k, quarterly cadence".
- **M-P2-1**— `pipeline` × 3 in stage cues → `конвейер`.

P2 (3 closed best-effort):
- **M-P2-3**— s17 trimmed by ~14 words (228 → 214) for slack from 94 WPM.
- **M-P2-4**— "in-context steering" mention added in s15 (17/17 glossary canonical).
- **M-P2-2**— `феатуры` → `признаки`, `Real-time` → `Реальное время` in s25.

---

## Pre-flight checklist (day before the lecture)

- [ ] Open `tiktokenizer.vercel.app` in a browser— verify that the site works and that the `o200k_base` tokenizer is available. This is the backup live tool for s05 / s07, in case someone in the audience asks "and how would this get split up".
- [ ] **Pre-test strawberry**: the day before the lecture, ask ChatGPT, Claude, and GigaChat the question "how many letters `r` are in the word `strawberry`". Note which answers come back and which of the models invoke an external tool. On s07 this is needed as a background fact, not as a central demo moment.
- [ ] Open `huggingface.co/playground` and make sure the model `Meta-Llama-3-8B-Instruct` is available and the temperature slider works. This is needed as a backup live tool for the demonstration on s19 (the effect of temperature)— the hands-on work with this tool itself is now an assignment for seminar 2, not a separate lecture slide. If HF Playground is down— switch to the backup: the `together.ai` playground or local Ollama with Llama 3 (it's on the laptop).
- [ ] Check three numbers for s16: GPT-3.5— 4 thousand tokens (a historical fact, does not change), Claude 3.5— 200 thousand (mid-2024), Claude 4.7 / the current flagship— on the order of a million. If a new model with a different window came out over the past week— update the spoken number.
- [ ] Prepare a live comparison for s19: the ChatGPT API or the OpenAI playground, the same query "Today I ate..." at `T=0` and `T=1.5`, three runs at each temperature. Screenshots— in `assets/s19-temperature-demo/` as a backup in case the internet goes down.
- [ ] Check the router and the projector 15 minutes before the start. HDMI, resolution, so the slides are readable from the back row.
- [ ] A timing checklist on paper: 6 sections × the sum across slides = 75 minutes. A clock in front of you.
- [ ] Verify the vocab-size numbers for s05/s06: GPT-4o ~200k tokens (`o200k_base` in `tiktoken`), Llama 3 ~128k (`tokenizer.json` in the HF repo `meta-llama/Meta-Llama-3-8B`). Cadence— quarterly: check that new model versions have not shifted the order of magnitude.

---

## [s01]— What you are NOT paying attention to right now

"Hello. Let's start not with AI, but with you.

While you're reading this sentence— what are you NOT paying attention to right now?

Your brain is continuously solving, right now, a small but important task: what to keep in focus, and what to leave in the background. Somewhere on the periphery— a notification on your phone that you noticed at the edge of consciousness and set aside. An unfinished thought about your evening plans— "did I buy the tickets?". The feeling of the chair you're sitting on— uncomfortable, but you forgot about it until I said so. All of this was competing for one and the same limited resource— your attention. And you weren't aware of this choice in the moment, but it was happening constantly, all this time.

On the slide— exactly this: a character being pulled in three directions at once— a notification, a stray thought, an unfinished task. This isn't about distractedness as a flaw. This is the normal, working architecture of attention in a human. We physically cannot process everything at once with equal fullness, so the brain constantly sets priorities: what goes into focus, what into the background.

Your brain chooses every second what matters and what is background.

So here's the thing. Today's lecture is about what happens inside an AI model between your request and its response. And one of the four internal stages we'll go through is called, literally, the same thing as what you just felt— the attention mechanism. When the model processes your text, it too decides which parts of the input to "look at" more closely, and which to leave in the background.

An important caveat right away, which we'll come back to closer to the middle of the lecture, in the section on the attention mechanism: the similarity here is in the name and in the general idea of "choosing a priority", not in the mechanics. Inside the model this isn't a psychological process but a concrete computable operation— a matrix of weights that can be computed and looked at. We'll compute it and look at it when we get to the heart of the matter.

But before we get there, you and I need to walk the whole path of a request through the model in order: tokenization, embeddings, attention, sampling. Each stage has its own concrete engineering consequence for how you work with AI in practice. That's where we'll begin."

---

## [s02]— Cover

"Lecture two. How modern large models work.

The second of seventeen. If in the first one we looked at AI from the outside— where it works, where it doesn't— then today we look inside."

---

## [s02a]— Lecture map

"Six sections in 75 minutes. Right now— the introduction. Next: tokenization, embeddings, attention, sampling, the finale. I'll be coming back to this map at every section."

---

## [s03]— Deepening the "model" layer from Lecture 1

"A brief recap. In the first lecture we established: AI systems are built in layers— the model at the bottom, above it the chat, above the chat the agent, on top the application. And the base layer— the model— we described as stateless inference: data in, a prediction out, no memory between calls.

This description is enough to talk about where the model is used within a large system. But not enough to talk about what happens inside it. In the first lecture, you and I left the internals of the model a black box— today we carefully open it.

Today we're deepening exactly this bottom layer. Four stages of inference, each with a practical consequence."

---

## [s04]— The main question of the lecture

"The main question is on the slide. What inside an LLM changes how we use it?

The answer won't be formulas. The answer will be four mechanisms and three practical promises that I make right now.

First: by the end of the lecture, you and I will understand why a prompt with a role works better than an empty one. Second: why AI is bad at counting letters. Third: why the same request gives different answers. These three "whys" were left open by Lecture 1. Today we'll close all three."

---

## [s04a]— Section 1: Tokenization

"After a short acquaintance with the course's promises— we move to the first layer of LLM mechanics. The first section of six. Tokenization— how the model sees your text. Six slides, eleven and a half minutes."

---

## [s04b]— Data flow in an LLM

"Before we dive into the details— the overall flow. Top to bottom, left to right. Text turns into tokens. Tokens— into vectors. The vectors go into the LLM, which is in the center, in gold. Out of the LLM come vectors. Those turn back into tokens. Tokens— into the text of the response.

Today we go through all of these stages one by one. Under the pipeline— four sub-cards: Section 1— tokenization, Section 2— vectors, Section 3— what the LLM does with the vectors inside, Section 4— the reverse conversion into tokens via sampling."

---

## [s05]— A token is an id from the model's vocabulary

"What a token is formally. A token is an identifier, an integer, from the model's vocabulary. This vocabulary is fixed at training time and does not change at the moment of use. The vocabulary size of modern models is on the order of hundreds of thousands of entries. For GPT-4o— about two hundred thousand; for Llama 3— about one hundred twenty-eight thousand.

Three markup examples. The word `cat`— one token. The word `tokenization`— two: `[token]` and `[ization]`. The word `клубника` (strawberry)— three tokens: `[к]`, `[луб]`, `[ника]`. The "rarer" a word is in the model's training corpus, the finer it gets split.

A simple rule of thumb that engineers use: on average one token is four characters in English or two characters in Russian.

A small exercise for intuition. How will the word `сильнее` (stronger) get split— into one token, two, or three? Think for a second. Hint: for Russian even a short word usually yields two or three tokens. The exact answer— on `tiktokenizer.vercel.app`, you can check it right in the browser."

---

## [s06]— BPE— a compromise

"The algorithm by which the vocabularies of most modern models are built is called BPE— Byte-Pair Encoding. It's a compromise between two extremes.

You could take individual characters as the vocabulary— then any text is representable, but the sequences come out very long. You could take whole words— then the sequences are short, but any typo or neologism becomes `<unknown>`. BPE sits in the middle: the vocabulary is subsequences of varying length that the algorithm found as the most frequent in the training corpus.

On the left— a training corpus of four words: `low`, `lower`, `newest`, `widest`. On the right— what BPE will learn: `low`, `er`, `new`, `est`, `wid`. Frequent roots and frequent suffixes— separately.

The main engineering detail that often gets missed: the BPE vocabulary is built once, before the model is trained. At the moment the model runs, tokenization is a lookup of ready-made rules, not a computation in real time. So when we say "the model's tokens", we always mean its fixed vocabulary. And two different models from the same producer can have different vocabularies— this is tied to the training corpus, not a common standard."

---

## [s07]— Why AI is bad at counting letters

"Now— the classic example you've surely seen. To the question "how many letters `r` are in the word `strawberry`" many models answer "two". The correct answer is three. Why does this happen?

The word `strawberry` for the model is three tokens: `[st]`, `[raw]`, `[berry]`. Three numeric units arrive at the model's input. Not ten letters `s, t, r, a, w, b, e, r, r, y`, but three ids. And inside each token there is no explicit list for the model saying "here's an `r` at positions three and eight". Inside there's statistical information about the contexts in which the token `[raw]` occurs. Not letter-by-letter.

This phenomenon we call letter-blindness. It's not a bug and not poor training. It's a structural consequence of how tokenization is built.

Three practical consequences. First— counting characters is fundamentally unreliable. Second— minor typos can lead to a split into completely different tokens, and the model suddenly answers differently. Third— case and spaces: `cat`, ` cat` with a space, `Cat`, and `CAT`— these are different tokens with different vectors.

The engineering conclusion. If your task requires an exact character-level operation— counting letters, searching for a substring, checking a regex— don't do it with a pure LLM. Use an external tool: a Python sandbox, a regular expression, specialized code.

A small practical caveat: modern top models often answer this question correctly— but not because a single forward pass through a neural network can count letters. They internally invoke Python or generate a step-by-step count. A single pass through the network, on its own, does not count letters.

And the same nature hits not only letters but arithmetic too: digits also get split by the tokenizer unpredictably, the place value does not coincide with the token boundary. Hence a measurable degradation— GPT-4 without external tools gives about 59% accuracy on three-digit multiplication, 4% on four-digit, and almost zero on five-digit."

---

## [s08]— The same text: more expensive in Russian

"A direct consequence of the fact that BPE was trained on a corpus with a large English skew— the cost of tokenization differs across languages.

English— about 0.25 tokens per character. A hundred characters— twenty-five tokens. Russian— about 0.5: those same hundred characters turn into fifty tokens. Chinese— about 0.8. Python code— about 0.4.

The engineering consequence. The same request by meaning, in Russian, costs roughly twice as much as in English. The specific gap depends on the text and the tokenizer— the range is from one and a half to two and a half times. If you and I have a batch task over thousands of documents and the subject area allows working in English, it makes sense to translate the inputs and outputs. This is a significant line item in the budget.

The second consequence— the context window is also spent unevenly. A document of eighty thousand characters in English will fit into twenty thousand tokens. The same document in Russian— into forty thousand. We'll come back to the window in the third section."

---

## [s08a]— Section 2: Embeddings

"The second section of six. Embeddings— a space of meanings. This is the second stage of the pipeline: after the text is cut into tokens, each token is turned into a vector. What this means and why— the next five slides."

---

## [s09]— What an embedding is

"When you and I said "a token is an id from the vocabulary", an open part remained. How does the model work with this id? Directly with the number— it doesn't: there's no meaningful arithmetic between tokens. The model needs to represent the meaning of each token in a form suitable for a neural network.

That way— an embedding, that is, a vector representation. Each token in the vocabulary is assigned a vector of fixed length— a list of floating-point numbers. For the token `[кот]` (cat) this might look like `[0.21, -0.45, 0.88,..., 0.13]`— several hundred or several thousand numbers.

The vector isn't assigned by hand. It's learned during the model's training— together with all the other weights of the neural network. When training ends, the "token → vector" table is fixed. At inference the model does a lookup: it got a token id, grabbed the vector, passed it into the next layer.

Concrete dimensions. OpenAI's specialized models for output embeddings: `text-embedding-3-small`— 1536 dimensions, `text-embedding-3-large`— 3072. The dimensions of the internal embedding tables of flagship models like GPT-4 are not officially published— the order of magnitude is estimated at several thousand dimensions. You and I don't actually need the exact number; what matters is the order of magnitude."

---

## [s09a]— The embedding space

"The main property of embeddings is stated in one phrase: tokens close in meaning lie near each other in the space of vectors.

On the slide— a simplified two-dimensional projection. In reality there are thousands of dimensions, but for intuition we compress them into a plane. Three clusters: animals— cat, dog, tiger— gathered in one corner. Transport— car, auto, motorcycle— in another. Programming languages— Python and JavaScript— in a third.

And nobody labeled "cat and dog are one category". This property arose on its own from the fact that in the training corpus both words often appeared in similar contexts. Closeness in the embedding space is a statistical reflection of how words are used. Not a semantic reference written by a human.

Three facts on the right side. Dimensionality— thousands of dimensions. Training— the coordinates are learned automatically. The projection into 2D— this is PCA or t-SNE, needed only for your and my intuition."

---

## [s10]— Semantic similarity on sentences

"Embeddings work not only for individual words but— and this is the main thing in 2026 practice— for whole sentences. Let's take five short phrases and measure how close they are to each other.

Five sentences. The first— "How to set up SSL". The second— "Installing an HTTPS certificate". The third— "Deploying a React component". The fourth— "Building a React application". The fifth— "A borscht recipe".

The scale we see is called cosine similarity. It's a measure of the angle between two vectors; values from minus one to one. Closer to one— the vectors are co-directed, meaning the sentences are close in meaning.

Here's what comes out with a modern embedding model. The first and the second— synonyms in the web-security domain— about 0.85. The third and the fourth— both about working with React— about 0.78. Borscht against any technical one— a range from 0.05 to 0.15. Low, but not zero.

The main takeaway. A modern embedding captures meaning, not an exact string match. `SSL` and `HTTPS`— different strings, but they're close in the embedding space because in the training corpus they appeared in the same contexts. The same for React, for synonyms in technical language, for pairs across different languages.

The concrete numbers on the slide are illustrative. The exact values depend on the chosen model. You can reproduce this with the open-source `sentence-transformers/all-MiniLM-L6-v2` or via OpenAI `text-embedding-3-small`. The main thing is the order of magnitude: synonyms 0.7–0.9, incompatible domains— around zero.

This same mechanism underlies semantic search and RAG— we'll talk about RAG in the next lecture."

---

## [s12]— Embeddings— the foundation of LLM understanding

"Let's gather what we've arrived at in this section. Embeddings are the foundation of how an LLM "understands" your and my language. The model works not with strings but with vectors. And all the semantics— at the level of the geometry of these vectors.

The full cycle: words— tokens— vectors— the LLM in the center, in gold— vectors— tokens— words. In both directions. First the input, then the reverse conversion into the output. Embeddings— the bridge between text and the neural network.

Three practical observations. First— paraphrasings: the model calmly understands "how to set up SSL" and "installing an HTTPS certificate" as close tasks. Second— synonyms: "doctor" and "therapist"— close points. Third— cross-linguality: `клубника` (strawberry) and `strawberry` also turn out to be near each other, because in multilingual corpora these words occur in the same contexts.

Semantic closeness at the sentence level is the basis of LLM understanding. This is what distinguishes modern AI from full-text search."

---

## [s13]— Section 3: The attention mechanism

"We've established embeddings— now the question: how does the model decide which vectors to look at right now. The third section of six. The densest— eighteen minutes, six slides. The attention mechanism— the central operation of the transformer."

---

## [s13a]— Attention is a matrix

"Before we take apart what attention does by meaning— how it's built technically. And here it's important to establish: attention is a matrix operation, not a linear one.

On the slide— a simplified seven-by-seven attention matrix for the sentence "The cat ate the mouse because it was hungry". Each row and each column is a token. The color of a cell encodes the weight: dark— a high weight, light— a low one. The cell "it → mouse" is highlighted in gold— it currently has the highest weight.

The key thing here— each token looks at all the others simultaneously. Not sequentially, the way you and I would read. Simultaneously. This is the very idea from the famous Vaswani 2017 paper— «внимание— это всё, что вам нужно» (in the original "attention is all you need").

Three facts. First— the matrix has dimension N by N, where N is the number of tokens in the context. Hence the quadratic cost: double the context— the cost quadruples. Second— the matrix is recomputed at every generation step. Third— attention heads in a modern model number not one but dozens or hundreds in parallel, each with its own matrix."

---

## [s14]— Attention— a distribution of weights

"Now by meaning. What attention produces at its output. A convenient metaphor— a flashlight in a dark room.

Imagine you and I are standing in a room with a large number of objects. These are all the tokens of the context. We need to answer a specific question— predict the next token. We can't brightly light up everything at once. We aim the flashlight at the objects that are relevant to the question right now. At the center of the beam— bright. At the periphery— dim.

This is attention. A distribution of light across the scene. And this distribution changes depending on what we're asking right now.

Formally: for each token, attention returns a distribution of weights over all the other tokens of the context. The sum of the weights always equals one. One large weight— "I lean heavily on this token". A small one— "this one is almost unimportant right now". We won't introduce any formulas— for the user's understanding it's enough to establish three facts.

First— as input, attention gets all the tokens of the context. Not one and not a part. All of them. If the context is 10 tokens— it looks at 10. If 100 thousand— at 100 thousand.

Second— at the output, for each token there is a distribution, the sum is one. This is simply "how we divide attention among the tokens at this moment".

Third— this distribution is recomputed anew at every generation step. Taking into account that the previous token has already been chosen and added to the context.

In a real model, attention heads number not one but dozens in parallel, and there are dozens of layers. But for your and my level of understanding, one phrase is enough: attention produces a distribution of weights over the tokens of the context."

---

## [s15]— A working example and the role effect

"The main example of the lecture. Let's take a concrete sentence: "The cat ate the mouse because it was hungry".

When the model reaches the token "it", it needs to determine what this token refers to. To the mouse or to the cat. At the level of attention this is visible. Over the token "it" a distribution of weights appears. The largest weight— on the token "mouse"; that's how the sentence is understood. A medium weight— on "was". A thin one— on "hungry". On the slide this is three arrows of different thickness.

An important caveat. The picture with three arrows is a strong simplification. A real attention map contains hundreds of connections at once, and in each of the dozens of layers the picture is its own. We aggregate hundreds of values into one thick arrow for intuition.

And even more important— the model doesn't do grammatical parsing. It statistically looks at the tokens for which the statistics say "these are usually connected to 'it' in similar contexts". Correlation, not parsing.

A small exercise. Think for 30 seconds: where does the model look in the sentence "The program crashed because it forgot to handle null"?

On most modern models the maximum is on the token "program". This agrees both with grammar and with the statistics of technical texts. On some individual models a redistribution is possible— this is normal variability.

Now the main practical consequence. The first of the three "whys" from Lecture 1. Why a prompt with a role works better than an empty one.

Let's compare two prompts for the same task. Without a role: "Explain asynchronicity". With a role: "You are a Python expert. Explain asynchronicity to a junior".

At the level of attention, the second gives a qualitatively different picture. When the model reaches the moment of generating the first token of the response, its attention is distributed over the whole preceding context. In the first case the context is short— almost only the word "asynchronicity". The model leans on the most general statistics. It produces a generalized answer.

In the second case the context has the tokens `Python`, `expert`, `junior`. And they get a substantial weight in the distribution of attention. The next generated token is chosen from a distribution shifted by these tokens. The answer will turn out to be more concrete— about Python, not in general. With simpler explanations— because the audience is a junior. And in a more expert register.

A working explanation. Role tokens get an elevated weight in attention when generating the first tokens of the response. The role in the prompt is not a request "trust me". It's an explicit input signal directly affecting the distribution of attention. In engineering language this is called in-context steering— controlling the model's behavior through the context itself, without retraining the weights. This is the first of the three "whys", and we've just explained it through the mechanism."

---

## [s16]— The context window

"Since attention works on all the tokens of the context, a natural limitation appears: the context window. This is the maximum that the model can process in a single request.

Over three years the window grew by orders of magnitude. Three key points. GPT-3.5 at the moment ChatGPT was released in 2022— about 4 thousand tokens. Claude 3.5 in mid-2024— 200 thousand. The current flagships— Claude 4.7, the current GPT— on the order of a million.

One million is, very roughly, fifteen hundred to two thousand pages of English text. It seems that "the model sees everything" and the problem has disappeared. This impression is deceptive for two reasons.

First— the cost grows quadratically. The base version of the attention mechanism requires each of the N tokens to look at every other one. That's N-squared operations. Double the length of the context— the cost quadruples. A million tokens of input— sixteen times more expensive than a hundred thousand. In the API price this is directly visible.

The second reason— the model doesn't use all positions in the window equally well. We move to this on the next slide."

---

## [s17]— Lost in the middle

"In 2023 a group from Stanford and Berkeley published a paper with the provocative name "Lost in the Middle".

The experiment is simple. Into a large context a single significant fact is inserted— at the beginning, in the middle, or at the end. Then the model is asked for that fact and the accuracy of the answer is measured. On the graph you and I see the characteristic U-shaped curve.

Accuracy around 70–80% when the fact is at the beginning. It drops to 50% in the middle. It rises again to 70–80% at the end.

The nature of the effect is tied to how models learn to work with long context. In typical documents important statements are located either at the beginning or at the end. The statistics of the position of important tokens have a U-shape, and the model absorbs it. An important token in the middle it weighs less, out of habit.

The engineering conclusion. If you and I have a long prompt with instructions and data— place the most important thing at the beginning or at the end. Not in the middle. The most common mistake— a long preamble of rules with a critical constraint sunk in the middle of it. This instruction the model will systematically ignore.

The solution is simple. Critical instructions— at the very beginning, in the system prompt. Or repeat them explicitly at the end, right before the task."

---

## [s17a]— Section 4: Sampling

"The fourth section of six. Sampling— from a distribution to a token. This is the last stage of inference. After all the attention layers have done their work, we get a probability distribution. What to do with it next— the next six slides."

---

## [s18]— The probability distribution

"At the input of sampling— what the previous three stages produced. The model went through tokenization, embeddings, all the attention layers. At its output— a probability distribution over all the tokens of the vocabulary.

That is, for each of the one hundred or two hundred thousand tokens of the vocabulary the model said: "the probability that the next one is exactly this one equals such-and-such a value". The sum of all probabilities is one.

A concrete example. The user wrote "Today I ate..." and awaits the continuation. On the bar chart— the distribution of the next token. An apple— 0.32. Pizza— 0.19. A salad— 0.14. A bun— 0.11. A cucumber— 0.08. The remaining two hundred thousand tokens of the vocabulary— each less than five hundredths.

Two things are visible. The distribution is not uniform. The model has statistical preferences based on the training corpus. But also not point-like— there are several plausible candidates, and among them the probabilities differ noticeably.

Next— sampling. This is the rule by which the model selects one token from the distribution. The one that will go into the response. And it's exactly the sampling rule that determines how "creative" or "deterministic" the answer will be.

On the slide the apple is highlighted in gold— let's say the model chose exactly it. This will be the first token of the response. Next— the next step of the distribution, now with the apple in the context."

---

## [s19]— Temperature

"The main sampling parameter is temperature. A single API parameter. It controls how "sharp" the choice will be.

Three copies of the distribution from the previous slide. On the left— `T=0`. In the center— `T=0.7`. On the right— `T=2`. Look at the difference.

`T=0`. All the probabilities are compressed onto the apple. Argmax— take the one whose probability is maximal. The model will almost always choose exactly the apple. The answer is predictable and almost deterministic. Repeat the request ten times— you'll get the same thing.

`T=0.7`, the standard mode. The model samples proportionally to the probabilities. An apple in 32% of cases. Pizza in 19. A salad in 14. Natural variability— each run may return a different answer, but all the answers are in the zone of the plausible.

`T=2`. The distribution smooths out. The difference between probable and rare tokens decreases. The model starts choosing unexpected options. In extreme cases the answers come out almost chaotic.

Besides temperature there are two alternative knobs. Top-p, or nucleus sampling: it cuts off the "tail" of rare tokens, keeping the minimal subset with a total probability ≥ p. Top-k: it keeps exactly the k most probable ones. In practice, for most tasks temperature is enough. Top-p and top-k— the second layer of control.

This is the third of the three "whys" from Lecture 1. Why the same request gives different answers. Because at `T > 0` sampling is a stochastic process. From one and the same distribution each run may choose a different token. This isn't a bug— it's an engineering decision that gives models a natural variability."

---

## [s20]— 4 API knobs per scenario

"Let's gather the four main parameters by which an engineer controls the LLM's work through the API.

Temperature, top_p, max_tokens, the system prompt. Four scenarios— four rows of the table.

Classification. `T=0`, a small max_tokens— fifty to two hundred, a minimal system prompt with the output schema in JSON. Any stochasticity is harmful: if on one document one run gives "complaint" and another "question"— reproducibility is broken.

Code generation. `T=0.2-0.3`, slightly nonzero, top_p— 0.9, a large max_tokens, a thousand and more. The system prompt— the role `senior Python developer` and the context of the repository. A clean zero gives repetitive "textbook" code; 0.2— variability only among nearly equally good solutions.

Chat explanation. The standard. `T=0.7`, top_p— 0.9, max_tokens five hundred to a thousand, a system prompt that describes the audience.

Creative writing. `T=0.9-1.2`— stochasticity here is a desired property. Top_p— 0.95, max_tokens— two thousand and more. A prompt about style.

This table isn't a prescription but a reference point. In real work you and I calibrate for our own task. The main thing is to understand the frame: four knobs, and they're pulled in a coordinated way."

---

## [s21]— The autoregressive loop

"Let's look at how all four stages of inference fold into a single loop.

Lecture 1 described the model as a stateless function: input— data, output— a prediction, no state between calls. But in a chat with an LLM you and I observe a long answer— a phrase, a paragraph, a page. Where does a long answer come from, out of stateless calls?

The answer— autoregressive generation. From `autoregressive`— literally "self-regressing". The model leans on its own previous outputs. A cyclic process.

Step 1. The current context: the system prompt plus the dialogue history plus the new request plus everything the model has already generated for this response.

Step 2. Forward pass— a full pass of the context through the four stages we went through. This is the step we studied in the first three sections— on the slide it's highlighted in gold.

Step 3. The probability distribution of the next token.

Step 4. Sampling— we choose one token.

Step 5. The chosen token is appended to the response. And back to step 1.

The loop repeats until a special "end of response" token is generated or until the counter runs into max_tokens.

Each individual step is stateless. The model remembers nothing between steps. All the "memory" is carried by the context itself, which is fed in full each time. The illusion of memory is created not by the model but by the orchestrator, which assembles and feeds the context."

---

## [s22]— Local vs cloud

"One short moment. The loop described is one and the same in the cloud and locally.

On the left— Local. Ollama, llama.cpp. Models of 1–13 billion parameters: Qwen 2.5, Llama 3.1 8B. Privacy, no pay-per-token, slower.

On the right— Cloud. OpenAI, Anthropic, Yandex, GigaChat. Hundreds of billions of parameters. Higher quality, a larger window, a latency of 200–500 ms. Pay-per-token.

Architecturally, inference is identical. What differs is the size and the environment. Deeper— was in Lecture 1."

---

## [s22a]— Section 5: Finale

"You and I have gone through the four stages of inference— now we connect them into one pipeline and close the three "whys" from Lecture 1. The fifth, final section. The finale. We close the three "whys", the two cross-cutting frames, the seminar assignment, the bridge to Lecture 3. Nine minutes."

---

## [s23]— The inference pipeline

"Let's fold it all into one diagram. The LLM inference pipeline— four stages.

Tokenization— the text is cut into tokens from a fixed vocabulary built by BPE.

Embedding— each token is assigned a learned vector; geometric closeness is semantic closeness.

Attention— dozens of layers build distributions of weights over the tokens of the context.

Sampling— from the distribution, by the rule set by temperature, one token is chosen.

This was that "black box" that we opened. Next— the consequences."

---

## [s24]— The three "whys" closed

"A return to the three promises I gave at the start. They're also the three "whys" that you and I are closing today.

First. Why a prompt with a role is better than an empty one. The answer: role tokens get a high weight in attention when generating the first tokens of the response. The distribution shifts toward the role. Slide s15.

Second. Why AI is bad at counting letters. The answer: the model sees tokens, not letters. `Strawberry` for it is three tokens, not ten characters. This is a structural consequence of BPE tokenization. It isn't fixed by fine-tuning or by a larger model on pure inference. Slides s05 and s07.

Third. Why the same request gives different answers. The answer: at a temperature above zero, sampling is stochastic. Each run may choose differently. Slides s18 and s19.

Three "whys" closed through the mechanism, not through intuition. This is the main learning goal of today's lecture."

---

## [s25]— When not an LLM

"The first of the two cross-cutting frames of the finale. When an LLM is not the right tool. You and I now know how to justify this through the mechanics.

A simple decision tree. Three "not an LLM" branches.

The first. The task is classification into a small fixed set of categories. Five to twenty classes, thousands of labeled examples. Most likely, classical ML: logistic regression, XGBoost, a small BERT with fine-tuning. An LLM here will be more expensive and less accurate.

The second. Interpretability or adjustability is needed. Finance, medicine, the legal sphere. Classical methods with a transparent structure— features, a decision tree, rules. An LLM— a black box in the sense of explaining an individual prediction.

The third. A critical response time under 100 milliseconds. Real time, anti-fraud, edge devices. A specialized small model, not an LLM with a latency of 200–500 ms.

In all other cases— an LLM is applicable, and often optimal. Knowing the mechanics of the internals is needed, among other things, to carefully understand where it isn't needed."

---

## [s26]— Attention ≠ causality

"The second, final frame of the finale. A return to Pearl's three levels of causality from Lecture 1.

The human. "X happened because Y"— a model of causality. Correlation, intervention, the counterfactual "what would have been". Relies on domain knowledge.

AI. "X follows Y in the data"— statistical correlation. Attention looks at tokens, it doesn't build a causal graph. Pearl's level 1— strongly. Level 2— partially. Level 3— no.

This isn't a temporary shortcoming. It's a limitation of the paradigm. Counterfactual questions— the zone of human judgment."

---

## [s28]— Bridge to Lecture 3

"What's in Lecture 3. The topic— "Agents, RAG, API: how AI goes beyond the chat".

In the pipeline that you and I assembled today, there's a hard limitation: the model sees only the context, it can't go outside. Lecture 3 will show how this is circumvented through four classes of tools.

RAG. Semantic search over your database plus an LLM. The same pipeline with an enriched context. The embeddings we went through are the foundation.

Tools and function calling. The model generates a structured call in JSON. An external system executes it, returns the result. The canonical way to work around letter-blindness.

MCP. An open standard for connecting tools, Anthropic, November 2024.

Agent loop. The cycle act— observe— reflect. At each step the model decides, sees the result, corrects the plan.

Everything is built on top of single-shot inference."

---

## [s29]— Q&A

"Thank you for your attention. Open Q&A.

If there aren't questions right away— a few directions people usually ask about.

First— deeper on the trade-off in choosing a temperature for a specific production task. Second— about model sizes, local vs cloud, what to choose for our scenario. Third— about the tokenization of Russian, Chinese, and how the Russian models— YandexGPT, GigaChat— cope better or worse. Fourth— about long context: is a million tokens already "seeing everything" or not yet.

Any question on today's material, or looking ahead— go ahead."

---

## Buffer reserve

- 5 minutes of Q&A at the end (s29).
- 4 minutes for transitions and pace adjustment (distributed among the sections)— increased from 2 to 4 after the removal of s27 (issue #156): the freed-up ~2 minutes, instead of being redistributed across the remaining sections, went here as general slack rather than being dissolved unnoticed into the text.
- If the active speech is going faster than planned— add retrieval moments on s07 ("try it yourself on tiktokenizer"), s15 (the second example with grammatical ambiguity), s19 (a live comparison of T=0 vs T=1.5).
- If it's going slower— shorten s12 (entirely a reformulation, can be done in a minute), s22 (one screen, can be 30 seconds), s26 (a callback to Lecture 1, can be compressed).

**End of speech. Lecture 2— 75 minutes.**
