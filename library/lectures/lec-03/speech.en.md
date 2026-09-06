---
lecture: 3
title: "Lecture 3. Architectures of AI systems: agents, RAG, API"
language: en
length_words: ~5900
length_min: 105
length_min_full_deck: ~135
pace_note: "Natural conversational English (English-native lecturers speak slower than the Russian ≤95 WPM target, so pace is unhurried, ~85–90 WPM). The sum of honest timings for all 55 segments at this pace ≈ 135 min of clean speech (Part 1 s01–s16 ≈ 68 min; Part 2 s18–s30 + Q&A ≈ 67 min). All 55 slides do not fit into a 105-min slot at this pace — the hard pace-rule wins; the 105-min slot is reached via the deck-meta cut-order (slides sacrificed at 90/75 min). Each [sNN · X min] is an honest timing of that segment."
status: draft
version: v3.1-en
derived_from: "RU speech v3.1 (chapter v4.0, 5 parts) + deck v6.3-en (55 slides, s01b dropped, s03 lightened, meme slides), issue #185"
slides_covered: [s01, s02, s02a, s03, s04, s04a, s-classic-prompt, s05, s05a, s05c, s05b, s06, s07, s08, s08a, s09, s-classic-rag, s10, s11, s12, s13, s13a, s-classic-ft, s13b, s15, s17, s14, s16, s18, s-classic-agents, s19, s19b, s20, s21, s22, s22a_multi, s22b, s22c, s22d, s22e, s25, s24, s25b, s23, s23b, s23c, s25a, s-classic-framework, s26, s27, s27b, s28, s29, s30, s31]
parts: 2
---

# Lecturer's speech · Lecture 3. Architectures of AI systems: agents, RAG, API

**Duration:** ~105 minutes (with buffer).
**Version:** v3.1-en (English track, re-synced to deck v6.3, 55 slides, s01b dropped, issue #185).
**Pace:** conversational, unhurried, with pauses at section changes.

**Split into parts:** this file is Part 1 (Sections 0–3, slides s01–s16). Continuation — [`speech-part2.en.md`](speech-part2.en.md) (Sections 4–5, slides s18–s31).

**The through-line.** The central question — "which architecture do I choose for a task, and when is the right answer 'not AI'" — is posed on s04 and returns pointedly at five return points: №1 s08 (when NOT to complicate the prompt), №2 s12 (when NOT RAG), №3 s17 (what goes where: knowledge / behavior / determinism), №4 s22 (workflow vs agent), №5 s21 (the loop = an architectural choice). The Air Canada thread: hook on s01 → the full case in §2 on s13 → the decision route on s27. The through-line "classics → AI → the boundary": on every s-classic slide there is a classical baseline built from scratch, then what AI adds, then what to keep from the classics; it closes on s28 (the summary) and s30 (the bridge into Lecture 4).

---

## Preparation before the lecture

- **Demo for s21:** if you plan a live demonstration of the agent loop — test the launch in advance; if it fails to start, work through it on the closed loop plan → act → check → iterate as shown on the slide.
- **`[VFY-day-of]` figures (s05c, s07, s15, s20, s22d, s25b, s29):** on the day of the lecture, verify against the research files `notes/lecture-3-rework/research/{rag-prompting-2026,transfer-dossier}.md` — GPT-4o 63.8% / instruction-hierarchy 84.1→94.1% (s05c); faithfulness 25%/39% (s07); LoRA 98.4%/20,834 (s15); MCP 90,000/10,000/CVE (s20); the Letta/Memory Tool registry (s22d/s25b); MIT NANDA ~95% (s29). The agent-harness-registry is an independent live-eval, not a primary source; OpenHands = a hypothesis for the "OpenClaw" heard by ear.
- **s31 (contacts):** fill in the lecturer's contact line.

---

# PART 1 — Sections 0–3

## [s01 · 3 min] — "The magic pill"

[Start calmly. On the slide — a "Drake"-style meme: we reject the "magic phrasing," we choose "architecture." Let the class read it — pause 3 sec. You can smile at the meme, but hold the thesis.]

Let us start not with a technology, but with one very persistent belief. The meme on the slide draws it out: on the left — "write 'you are an expert' in the prompt, ask it to reason step by step, make the wording more elaborate, and the model will answer more accurately on the facts." On the right — what this whole lecture is about: reliability comes from the choice of architecture, not from a lucky phrasing.

Let us name the belief directly. This is the "magic pill" of prompt engineering — the faith that a lucky phrasing of a single call can replace the correct choice of tool.

The myth is persistent because it holds a grain of truth. Phrasing really does affect a lot — the tone, the structure, whether the model answers briefly or at length. But that grain masks the key error. The role "you are an expert" changes the manner of presentation, not the truth of what is said. Step-by-step reasoning does not help on every task. And a high cost of error — where the answer must be verifiable and deterministic — is solved not by the phrasing of the request, but by the choice of architecture around the model.

[A short anchor case, which we will return to in the section on RAG.]

One example right away, to keep it in your head until the second section. In 2024 a tribunal in Canada issued its decision in *Moffatt v. Air Canada*: the airline's chatbot invented a nonexistent fare, the passenger relied on it, and the court ordered the company to pay. And — note this — the correct answer was on the very same page the bot linked to. This is not a model failure but a wrong choice of architecture for the task: a generative chatbot where an ordinary lookup in a rules table was needed. We will work through this case in detail in the section on RAG.

Note the question at the bottom of the slide: if phrasing does not give accuracy — what does? This whole lecture is a systematic answer to it. And it is noticeably longer than usual today, because the section on agents grew to almost half the time.

[Transition to the cover.]

---

## [s02 · 1 min] — Cover

Today's topic is the architectures of AI systems: agents, RAG, API. This is the last overview lecture of the introductory module.

There is one load-bearing thought, and hold it to the end: the choice of architecture is an engineering decision for a task, not the following of a fashion. Often the right answer is the simplest sufficient architecture. And sometimes the right answer is to not use AI at all.

[We do not repeat the audience formula further.]

---

## [s02a · 2 min] — Lecture map: six sections

Before diving in, let us look at the route as a whole. The lecture is six sections, arranged not as a catalog of technologies but as a single line of reasoning.

Section zero — the opening: the myth of the "magic pill" and the question of where reliability comes from. The first — the prompt and its limits: a single call and where it hits its ceiling. The second — RAG, retrieval-augmented generation. The third — fine-tuning and its place in the lineup "prompt vs RAG vs fine-tuning." The fourth, and by time it takes almost half the lecture, — agents: how a model becomes a component of a system, what an assistant agent is assembled from, where its memory lives, and how all of this breaks. The fifth — assembly: the ladder of complexity, the choice route, a short checklist.

Through all six runs one line. This is not "learn six technologies," but "learn to choose which to apply — and recognize the cases where the right answer is to not use AI at all." Each section ends the same way: not only "when to apply it," but also "when it should not be applied."

---

## [s03 · 2 min] — What we carry over from Lecture 2

Before moving on, let us quickly recall what we stand on. From Lecture 2 we with you take exactly two ready-made blocks, and we will not re-explain them — both reminders are on the slide.

The first block — a single model call, single-shot. This is one pass: a prompt on the input, an answer on the output, no memory between calls. It is around this single pass that we will build everything up today — tools, loops, agents. This is our point of reference.

The second block — semantic search on embeddings. Let me recall the essence: text is turned into a vector, closeness of vectors means closeness of meaning, so you can search by meaning without an exact word match. We need this block in the second section — RAG rests entirely on it.

That is all. Nothing else from Lecture 2 will need recalling today. If a single call or semantic search is hazy in your memory — it is worth rereading the corresponding sections of Lecture 2 before the end of the lecture, because further on we lean on them as known.

---

## [s04 · 2.5 min] — The central question and the ladder

This is the central question of the whole lecture: I have a task and access to a model — which architecture do I choose, and when is the right answer "not AI"?

Note the second half of the question. It is not rhetorical. The course teaches the ability to say "AI is not needed here," and today we bring this skill to the level of a tool.

Our answer will be a ladder of six rungs — it is on the slide. Bottom-up: ordinary code without AI; a single call with a good prompt; RAG or context engineering; a workflow with predefined paths; an agent with a dynamic loop; and at the top a multi-agent.

The rule for moving is single and central to the lecture. Stay on the lowest rung that closes the task's requirements, and climb higher only for an explicitly stated requirement that the current rung does not close. Each climb is paid for with new failure modes, cost, latency, loss of auditability, and a new attack surface.

[Slow down.]

Notice: the bottom rung is ordinary code without AI. The ladder begins with the question "is AI needed here at all." The Air Canada case is exactly a case where an engineer climbed onto a rung with generation where the task lived on the bottom rung of deterministic code.

And one last thing: this ladder is a map of the lecture, not a demand to understand everything now. We will work through each rung separately, and for each we will say when you should not climb onto it.

---

## [s04a · 1 min] — Section 1. The prompt and its limits

We move to the first substantive section of five — "The prompt and its limits."

The logic is fundamental: we go up the ladder from the bottom. Not "which powerful tool exists," but "is the simple option sufficient, and if not — for which requirement do we climb higher." The bottom rung with a model is a single call with a good prompt. Before talking about RAG, fine-tuning, and agents, let us honestly understand what a single call can do and where its ceiling is.

---

## [s-classic-prompt · 3 min] — Classical baseline: how a task was stated before the prompt

But first let us fix a point of reference — how an engineer made a system do what was needed before language models. Let us work through it from scratch, because the prompt is its direct opposite along one key axis.

The classical answer to "how do I get exactly what I need from a machine" rests not on a wish but on a precise specification and a deterministic program. It relies on several named tools.

A formal specification describes what a system must do in a language with no double reading — pre- and post-conditions, invariants, in the limit machine-checkable specifications like Z-notation or TLA+. A requirements spec fixes the requirements, boundaries, and acceptance criteria. An interface contract is a precise agreement about input and output: type signatures, OpenAPI, Protobuf. The common trait: the result is deterministic and verifiable.

Here too, the distinction of two styles. The imperative answers "how to do it" — it lists the steps. The declarative — "what should result": a SELECT query does not say how to search, it describes the result, and how to obtain it is decided by the planner. In both cases the statement has a single correct meaning and a way to check it.

Now the bridge to the section. The prompt is stating a task to a probabilistic system in natural language. Herein lies both the power and the limit. The power: no need to formally specify the unspecifiable — "rewrite this letter more politely." The limit: natural language has no single meaning, and the executor has no determinism.

[Point to the gold plate.]

And right away — what to keep from the classics. The discipline of precise statement: a precise prompt is the same requirements spec, only in natural language. And for anything deterministic and verifiable — arithmetic, schema validation, rule-based routing — the right tool is still classical code. You use a prompt for what cannot be specified; everything specifiable you leave to the classics.

---

## [s05 · 2.5 min] — A single call — the point of reference

[On the slide a "Gru's plan"-style meme: RAG, tools, a loop "just in case" — escalating the architecture to absurdity. You can nod at it.]

The meme on the slide is exactly about what we avoid: complicating "just in case." Now — the point of reference on the model's side. The cheapest, most reliable, and most predictable AI architecture is a single call with a well-composed prompt.

A single call has neither external retrieval, nor a loop, nor tools: a prompt on the input, an answer on the output, no memory between calls. Minimal cost, minimal latency, maximal predictability: no loops that diverge, no retrieval that quietly degrades.

And let us fix the load-bearing boundary: the model knows only what got into the prompt, plus what settled into its weights during training. Anything that is in neither place is unknown to it — and then it will either honestly refuse or generate plausible text that rests on nothing. This boundary is the reason RAG (which extends what is "in the prompt") and fine-tuning (which extends what is "in the weights") appear further on.

Hence the default rule: do not complicate the architecture without a reason expressed in the task's requirements. This is not primitivism but a distribution of the burden of proof. By default — a single call. Any move upward requires justification: here is a requirement that a single call does not close, therefore I add RAG, a tool, or a loop.

Let us look at what each climb costs. RAG adds an indexing pipeline, a vector store, and retrieval that can silently degrade. Tools and a loop add external calls that fail, loops that diverge, and a new attack surface. None of these points exist with a single call. So "a single call by default" is not conservatism but a refusal to pay for infrastructure the task does not require.

---

## [s05a · 2.5 min] — The role in the prompt: tone, not accuracy

[On the slide a "Change My Mind" meme: the thesis "role ≠ accuracy." Play on it: here is a claim, try to change my mind — and we will see the data is on my side.]

The meme on the slide puts the thesis bluntly: a role tunes the tone, not the accuracy. Sounds debatable — let us check who is right.

The formula "role plus task plus context" is familiar from the first lecture. A role is a frequent first element of a prompt: "you are an experienced lawyer," "you are a strict editor." The intuition: the more precise the role, the more competent the answer, as if the model switches into an expert mode.

This is a very persistent myth, and let us examine it honestly. Mechanically a role is tokens that appear before the question and take part in all the attention computations. It does not flip an expert mode with a switch; it shifts the probabilities of the next tokens toward text resembling how the holder of that role would answer in the training data.

The key question is whether this shifts factual accuracy, not only the presentation. A specially designed study by Zheng and colleagues gave an unambiguous answer. One hundred sixty-two personas, eight domains, two thousand four hundred ten factual questions, four families of models — and personas do not improve accuracy compared to an answer with no role at all. A model told "you are a Nobel laureate in physics" does not answer physics more accurately than a model with no role.

[Pause.]

A separate study shows what a role really affects: the tone and the depth of presentation — but not whether a fact is correct. And this effect is model-specific.

Here is our first point of the "magic pill" that the lecture refutes directly. A role is a tool for tuning style, not accuracy. The practical takeaway for tomorrow: if you need an answer in a certain register — a role works. If you need factual accuracy — what works is competent context and reliance on a verifiable source, not a lucky phrasing of the role.

---

## [s05c · 3.5 min] — Protocol roles: not a persona, but dialogue markup

[On the slide an "Is This A Pigeon?" meme: an engineer points at the protocol role `system` and asks "is this a security boundary?". Play it up: a very frequent confusion.]

The meme on the slide is about a frequent confusion: people point at the system role and ask "surely this is a security boundary?" No. And here is why.

Here it is important for us to separate two meanings of the word. The persona role — "you are a lawyer," text in a message, affects tone — we covered that. But the word "role" has a second, independent meaning: the protocol roles system, user, assistant. This is not text in a message but markup of the dialogue's structure — "who is speaking." The first answers "in what tone," the second "whose turn this is."

Why protocol roles are needed. So that the model can tell the developer's instruction apart from the user's input and from its own past answers. Permanent constraints are placed into the system role, and the model is trained to treat it as more authoritative.

But here is what is fundamental: this is a learned habit, not an architectural guarantee. A study showed: GPT-4o obeys the priority of the system instruction in about 63.8 percent of cases. Special training raised the robustness from 84 to 94 percent — but not to a hundred. Remember: the priority of the system role is a tendency, not a security boundary.

Now the mechanics from which the vulnerability follows. Physically the model receives one flat stream of tokens. The list of messages is assembled by a chat template that wraps every message in special markup tokens. Different families have different formats, and they change between versions. Hence a practical piece of advice: if a local model behaves worse than advertised — first thing, check the chat template; on the wrong template a model gets noticeably dumber.

And here is the vulnerability. Since a role is tokens in a shared stream, text resembling role markup can get into the stream from external content: a web page, a file, a letter. This is the Special Token Injection attack — a forged role. A string imitating the start of an assistant turn is inserted into external content, and the model, in some cases, believes it is its own turn. A study on agent scenarios showed the success rate rising several-fold — on some models up to 88 percent. And simply asking the model "do not give in" barely protects it.

Real defense is two systemic measures. First: escape special tokens in incoming external content before feeding it to the model. Second: for local models, check the chat template. The full treatment of injection as a class of attacks comes in the fourth section, where it is no longer a curiosity but a baseline threat mode.

---

## [s05b · 2 min] — The structure of the prompt: separate instruction, context, data

If the role is responsible for tone, then the quality of the answer is far more strongly a matter of the prompt's structure — how clearly the three kinds of content are separated: the instruction (what to do), the context (on the basis of what), and the data (what to work with).

A flat prompt, where everything is fused into one paragraph, forces the model to guess the boundaries. The tool is delimiters: explicit textual markers. XML-like tags, markdown headings, triple quotes around inserted text. The concrete syntax matters less than the fact of separation itself: a model shown where the instruction ends and the data begins confuses one for the other less often — in particular, it treats inserted data as a new command less often. And that is the same "data vs command" confusion that underlies prompt injection.

Note: this is the same principle as structured output in the fourth section. There you set a schema for the output, here — a structure for the input. The idea is one: the model works better when it is clearly oriented as to what is what.

---

## [s06 · 2 min] — Chain-of-thought: step-by-step reasoning

[On the slide a "Distracted Boyfriend" meme: the model got distracted by a beautiful explanation and walked past the correct answer. A light lead-in.]

The meme on the slide is about the flip side of reasoning: sometimes a model gets so carried away with the explanation that it walks away from the correct answer. Let us examine the technique and its limit.

The next technique — chain-of-thought, step-by-step reasoning. The model is asked not to give the answer at once, but first to reason step by step out loud, and only then to state the result. Technically this is still a single call: only the prompt and the form of the answer are changed.

Let us look at the apples example. There were twenty-three, seven went bad, two crates of six each were bought. Without reasoning the model often gives a plausible but wrong number: it generates the answer token by token, and the short path leads into error. With reasoning the model produces intermediate computations — twenty-three minus seven equals sixteen; two times six is twelve; sixteen plus twelve is twenty-eight — and the quality on arithmetic and multi-step logic grows.

But "reasoning almost always improves" is a fallacy. On direct fact retrieval or simple classification it does not help and may harm: it lengthens the answer (more expensive, slower) and leads into a plausible error. This is a tool for a class of tasks, not a "make it better" switch. The practical takeaway: before adding "think step by step" to every prompt, ask — does the task decompose into steps? If not — the technique only harms.

[Turn to the class.] Will step-by-step reasoning help your task specifically?

---

## [s07 · 3 min] — Text ≠ thought: the limit of chain-of-thought

And now the limit of the technique, and it is more important than the technique itself. It is natural to assume: since the model reasons aloud, you can check by the reasoning how it arrived at the answer. This assumption is fundamentally wrong.

Let us introduce a term. Faithfulness — the degree to which the verbalized chain of reasoning reflects the real factors that influenced the answer. Low faithfulness means: the explanation and the actual cause are different things; the text is plausible but does not reflect the process.

Anthropic measured this in April 2025 by a method that makes the conclusion irrefutable. Models were given a task twice: without a hint and with a hint that changes the answer — for example, "the professor thinks the answer is C." Then it was observed: when the hint changed the answer, does the model mention it in its reasoning?

[Slow down — this is the core.]

Claude 3.7 mentioned the actually used hint in about one case in four — twenty-five percent. DeepSeek R1 — in almost two out of five, thirty-nine percent. In the rest, the model changed the answer under the influence of the hint but built an invented argument, without mentioning the real cause. And worse: faithfulness drops on hard tasks — exactly where an error is most costly and audit is most needed.

Let me stress why this is not "the model sometimes lies" but something structural. The chain of reasoning is generated text, subject to the same mechanics as any other output. It is produced to be plausible, not to be a faithful protocol of the internal computation. So any architecture that uses the model's self-explanation as a control inherits this defect: control based on self-assessment is not control.

The practical takeaway, and this is one of the through-lines of the course: a human validator checks the result and the facts against an independent source — a database, a document, a calculation — not the model's self-explanation. An attached "chain of reasoning" is not an audit log. Explainability in words is not equal to verifiability in substance. We will return to this twice: on the agent loop and on the role of the human validator.

---

## [s08 · 2.5 min] — Context engineering: the minimum of high-signal

The last topic of the section. If step-by-step reasoning is about the form of a single call, then context engineering is about its content.

Let us introduce a distinction. Prompt engineering — the phrasing of a single instruction. Context engineering — the broader iterative discipline: curating the whole set of tokens visible to the model at inference, including system instructions, tool descriptions, loaded-in data, and message history. The load-bearing principle: find the smallest set of high-signal tokens that maximizes the probability of the desired outcome.

Why is the minimality of context an engineering requirement rather than an aesthetic? Here we need to recall an effect from Lecture 2, "lost in the middle": the model uses information from the middle of a long context worse than from the beginning and the end. The phenomenon got a second name — context rot: as the number of tokens grows, the accuracy of retrieving the needed information falls.

Look at the curve. On the horizontal — the number of tokens; the longer the context, the lower the accuracy goes. This is the same phenomenon as "lost in the middle," under a new practical name — I make the stitch explicit so the term is not taken as a new entity. The mechanism is one: the pairwise attention links grow quadratically with length.

The consequence: "just put everything into the context" is not a strategy. A large window gives you the ability to fit a lot of text, but not a guarantee that the model will use it correctly. And this is the first key to the question "when NOT RAG": sometimes the right answer is not to build search infrastructure, but to curate a small stable context and reuse it through prefix caching. If the corpus is small, stable, and fits into the window — RAG would add fragility without a gain.

---

## [s08a · 1.5 min] — The prompt checklist: 8 points

Let us gather the whole section into a short checklist that you apply to any prompt before the first run.

First: a role is set if you need tone, and explicitly not as a promise of accuracy. Second: the task is a concrete verifiable action, not a wish. Third: the context is the minimum necessary. Fourth: the output format is stated explicitly if the answer is machine-processed. Fifth: delimiters are placed if there is more than one kind of content. Sixth: examples — only if the format is not obvious from the instruction. Seventh: step-by-step reasoning — only for multi-step logic. Eighth: the prompt is no longer than necessary — every extra paragraph drowns the context.

This is not bureaucracy but a compressed summary of the section: role is not equal to accuracy, context is minimal, reasoning is targeted. And for the large decisions — RAG, fine-tuning, an agent — there will be an expanded analogue: an eight-step checklist at the end of the lecture.

[Transition to the second section.]

---

## [s09 · 1 min] — Section 2. RAG

We move to the second section of five — RAG, retrieval-augmented generation.

The first section is over: the default choice is a single call, it can be strengthened with reasoning, but reasoning has a limit of faithfulness, and the context must be curated. A single call hits a boundary: the model knows only what is in the weights plus what you put into the context. If the task requires knowledge that is not in the weights — a private database — or that changes faster than model versions — current prices, documents — a single call will not cope. This is where RAG begins.

---

## [s-classic-rag · 3.5 min] — Classical baseline: how text was searched before embeddings

But here too let us start with the classics. RAG is presented as a new technology grown out of embeddings, and this hides something important: the R — retrieval, search — is a discipline with half a century of history, and its design determines where RAG works and where it breaks.

The everyday ancestor of machine search is the library catalog: cards by author, title, subject heading. Exactly this idea a machine reproduces through an inverted index — a structure that, for each word, stores a list of documents where it occurs. Instead of scanning all texts, the system looks up the query words in the index and instantly gets candidates. This is the foundation of any full-text system and to this day the workhorse of operation.

On top of the index the classics solve two tasks — selection and ranking. Selection is set by boolean search: a query as a logical expression — "error AND authentication NOT tomcat" — selects documents precisely and explainably. Ranking answers in what order to show what was selected. TF-IDF weights a word the more strongly the more frequent it is in this document and the rarer across the whole collection. The industry standard to this day is BM25 from the Okapi family: a development of TF-IDF with frequency saturation and length normalization. This is a strong, cheap baseline that many "smart" systems never actually beat.

The key property of the classics — they work on lexical match: they find documents with the same words. Hence the strength on codes, identifiers, rare terms. And the limit: the query "how to fix a broken login" does not lexically match "troubleshooting authentication failures," although in meaning it is the same thing.

Here is where semantic search on embeddings from Lecture 2 enters — it adds the missing layer of meaning. But — the load-bearing thesis — the classics do not disappear.

[Point to the gold plate.]

What to keep from the classics: the strong RAG systems of 2026 are not dense-only, but a hybrid where BM25 and vector search work together, plus lexical filters, ranking discipline through a reranker, and observability — recall and precision on a reference golden set. RAG is an extension of classical search, not a rejection of it.

---

## [s10 · 3 min] — The RAG principle: three steps

Now let us work through RAG itself. Retrieval-augmented generation — an architecture where, before calling the model, the system first retrieves relevant fragments from an external store, puts them into the context with the question, and only then the model generates an answer grounded in the fragments. The term: retrieval — the stage of searching for and extracting relevant fragments; it is precisely this that distinguishes RAG from "putting a document into the prompt by hand."

The key point: the search mechanism in RAG is exactly that semantic search on embeddings from the previous lecture. A reminder: text is turned into a vector, closeness of vectors means closeness of meaning. RAG builds up three steps. The first — indexing, offline: the corpus is cut into fragments, each is turned into an embedding and placed into a vector store. The second — retrieval, on the query: the question is turned into an embedding, and by closeness the k relevant fragments are pulled. The third — grounded generation: the fragments in the context, the model answers relying on them, in a good implementation — with a reference to the source.

And one more term that carries the main load. Grounding — the property of an answer being derived from specific retrieved fragments, rather than composed by the model out of thin air, with the ability to show which fragment each fact was taken from. A good RAG system is designed so that, to a question for which the fragments contain no answer, it says "I don't know" or "see the source," rather than composing one.

The invariant: "I don't know" is a correct answer of a RAG system. A plausible answer under irrelevant retrieval is a defect, not "better than nothing." The distinction between "an answer with grounding and a citation" versus "just plausible text" will turn out to be central further on and will directly explain the Air Canada case.

---

## [s11 · 2.5 min] — When RAG is the right choice

When is RAG the right choice? You need a strong signal on one or several markers, and the absence of a blocker from the neighboring "when NOT" criterion.

The first marker: the knowledge is large or growing — it does not fit into the window as a whole, or it fits but putting it into every request is expensive. The second: the knowledge changes — documents, prices, regulations update more often than model versions come out; RAG reads the store at the moment of the query. The third: freshness and provenance are needed — the answer relies on a verifiable source, and you need to show where a fact came from; regulated domains almost always require this. The fourth: the base is private — company knowledge is not in the weights of a public model.

The logic of application matters. One marker is a reason to take a closer look, but not to build automatically: first check the task against the "when NOT" criteria. The knowledge is large, but does not change and fits into the window — a candidate for long context. The markers usually reinforce each other: knowledge that is simultaneously large, changing, requiring provenance, and private — that is the profile RAG was designed for.

A working example we will return to in the finale: a corporate base of thousands of regulations updated weekly, natural-language questions, a mandatory reference to the source clause. All four markers converged — an exemplary RAG profile. And an observation for tomorrow: the gain of RAG over a direct answer is especially large for smaller models — external retrieval compensates for what they lack in the weights, so RAG often gives the needed quality on a cheaper model.

---

## [s12 · 3 min] — When RAG is NOT the right choice

[On the slide a "Roll Safe" meme (finger to the temple): "you can't lose at retrieval if the corpus fits into the window." Play it ironically.]

The meme on the slide is precise: retrieval will not let you down if there is no retrieval — when the corpus fits into the window. Let us lay it out in three criteria.

The second return point to the central question. The key thought: knowing when RAG is NOT needed is more valuable than knowing when it is — because RAG is a fashionable architecture, and it is put where it harms. Three "not RAG" criteria.

First. The corpus fits into the window — a rough marker is under two hundred thousand tokens — and does not change often. The right answer is full-context with prefix caching. Simpler, cheaper, without the risk of "retrieval pulled the wrong thing": no vector store, no indexing pipeline, no component that will break. RAG here is bought without necessity.

Second. The task is to return a fixed policy or value: a fare, a price, a regulation clause, a rule. If the answer is deterministic and known in advance, the right architecture is a deterministic lookup in a table or a static page, not "search plus generation on top." Generation on top of a fragment always carries the risk that the model will paraphrase or make things up. This is exactly what happened in the Air Canada case.

The third is often missed. The data is already available directly and live — through an API, MCP, a search in another system. If the knowledge sits in an internal service with a REST interface or in a database via MCP, a separate RAG index on top is redundant. RAG exists to give access to knowledge for which there is no direct path; if there is a path, RAG adds an extra fragile layer. The difference is strategic: a direct call returns the data as of the moment of the query, a RAG index — as of the last indexing. The marker: if to the question "why not have the model ask system X directly through a tool?" the answer is "indeed, why not," RAG is not needed.

The rule: RAG is redundant if the corpus fits into the window and is stable, if the task reduces to a fixed value, or if the knowledge is available live through a tool. Any of the three is a signal to stop. And even when RAG is justified, this does not guarantee it will work well at scale. That is what we turn to next.

---

## [s13 · 3 min] — RAG failure at scale + Air Canada revisited

The load-bearing lesson of the section: "the system returned something" does not mean "the system returned the correct thing." RAG has no signal "I did not find a suitable one" — by default it always returns the k nearest fragments, even irrelevant ones. And then the model honestly does its job: given garbage, it composes a plausible answer on top of garbage.

This is a known pattern of RAG engineering — seven points of failure are systematized in the literature. Three classes. Legal-AI pulls the "nearest k" cases; by vector, cases with matching words are close, but legally irrelevant — a different jurisdiction, an overturned precedent. Vector closeness is closeness of wording, not of applicability. Medical-RAG: a question about one patient retrieves fragments close by symptoms but from other patients; the model merges what clinically cannot be merged. A support bot: it worked on hundreds of articles, and after growing to thousands the quality quietly sagged — silent degradation at scale, there is no "close enough" threshold.

The alternative everywhere is not "remove RAG" but make it an observable system: a reference golden set and alerts, chunking along meaning boundaries, hybrid search with reranking. This is exactly the return of the classical discipline of ranking and observability.

[Lower the voice, return to the through-line.]

And now let us return to Air Canada — this time with the section's tools. The bot reported a refund of the difference and referenced a page with the real policy; the policy on that same page did not allow such a refund. The source of truth existed and was available — but the answer was not derived from it; it was generated as plausible text. This is an exemplary failure of grounding: generated text in a role that required a retrieved fact.

The right architecture: for a fixed policy — a deterministic page or a lookup in a table; if a dialogue is needed — RAG with strict grounding, a mandatory citation, an explicit "I don't know," and a human check. Air Canada is not "AI hallucinates," it is a decision to put a generative architecture on a deterministic task.

And a short question for you: RAG returned an answer — how do you know it is correct? Only by measurement. By eye, a plausible one cannot be told from a correct one — that is the whole lesson.

---

## [s13a · 1 min] — Section 3. Fine-tune vs prompt vs RAG

We move to the third section of five — fine-tuning vs prompt vs RAG.

In the previous section we closed the problem of knowledge with RAG. But not every problem is a problem of knowledge. Sometimes the facts are enough, but the behavior is unsatisfactory: the model answers in the wrong tone, the wrong format, does not follow a domain policy. This is a different class of task, and RAG does not solve it — no matter how many documents you slip in, the tone will not change. Here the third tool enters the stage — fine-tuning.

---

## [s-classic-ft · 3 min] — Classical baseline: how an ML task was solved before large models

And again let us start with the classics. Training a model for a task in the pre-LLM paradigm is building your own model on your own data: the engineer collects a labeled set of "input → correct answer" examples and tunes the parameters so the model reproduces the answers and generalizes to new ones.

The central term is the training set: the collection of labeled examples. The labels are called ground-truth labels, ground truth — the known correct answer against which the prediction is compared. Before large models, solving an AI task almost always meant collecting your own dataset and training your own narrow, controlled model.

The second construct is the discipline of splitting the data. It is divided into three non-overlapping parts: training, validation, and test. On the training part the model learns, on the validation part hyperparameters are tuned, on the test part — once, at the end — the quality is measured on data the model has not seen. The iron rule: you may not test on the training data, otherwise the accuracy is inflated and collapses in production.

The third idea, and it leads to the theme of the section, is transfer learning. Long before large models, engineers noticed: training from scratch is expensive, but if you take a model pretrained on a general corpus and fine-tune it on your task, the result comes out faster and more accurate. The classical two-phase scheme: pretraining, then fine-tuning.

[Point to the gold plate.]

What to keep from the classics: eval sets — a golden set — without which, as we will see, catastrophic forgetting is invisible; versioning of data and weights for rollback; the train/test discipline against leakage; drift monitoring in operation. And the bridge: PEFT and LoRA are the same transfer learning, taken to the limit of cheapness on top of an incomparably larger model. The idea is not new — what became new is the scale of the base model and the cost of the step. All the cautions of the classics remain in force.

---

## [s13b · 2.5 min] — What fine-tuning is

Before talking about where fine-tuning narrowed and where it is dangerous, we need to understand identically what it is. Fine-tuning — the continued training of an already-built, pretrained model on your data.

In Lecture 1 fine-tuning was mentioned in passing as a type of AI use. Here it is in its true role — an architectural choice, one of the rungs of the ladder.

The mechanics on the diagram: you take a pretrained model with general weights, you take your dataset — examples of the desired behavior — and fine-tuning shifts the weights toward these examples. The output is a different model: the same architecture and size, but different numbers inside.

Here is the key difference for which a separate slide is needed. Prompt and RAG do not touch the weights: they change only the context — what you feed on the input right now. The effect lives within one request and disappears with the next. Fine-tuning changes the model itself: the change is built into the weights, acts on every request, and therefore costs more and rolls back harder than anything that changes only the context.

The formula: prompt and RAG — "what to show the model," fine-tuning — "change the model itself." And a caveat: in practice, "fine-tune a model" almost always means not retraining all the weights, but parameter-efficient fine-tuning — it is called by the acronym PEFT and is most often implemented by the LoRA method. Why — on the next slide.

---

## [s15 · 3 min] — PEFT instead of full fine-tuning

[On the slide a "Buff Doge vs Cheems" meme: the muscular dog is the modest PEFT, and full fine-tuning turns out to be the weak, expensive Cheems. Play up the reversal.]

The meme on the slide reverses the intuition: the "buff one" here is not full fine-tuning but the modest-in-volume PEFT. We will now see why the parameter-efficient path is stronger.

Many associate "fine-tune a model" with updating all the weights — that is full fine-tuning. In 2026 this is almost never what you need.

PEFT, parameter-efficient fine-tuning — a family of methods where the base weights are frozen, and a small set of additional parameters, adapters, is trained. The most widespread is LoRA: small low-rank adapter matrices are added into chosen layers, and only they are trained. QLoRA is the same idea on top of a quantized base model, which sharply lowers the memory requirements.

Why PEFT is almost always preferable to full fine-tuning — three reasons, and the third decides the most. First: cheaper and faster — millions of adapter parameters are trained instead of billions of weights; QLoRA lets you fine-tune large models on a single GPU. Second: modularity — the adapters are small, megabytes against gigabytes, you can keep several for different tasks on one frozen base. Third, the load-bearing architectural argument about reliability: the base weights are frozen, physically not overwritten under the new signal, so what the model could do before fine-tuning is mostly preserved. This directly lowers the risk of catastrophic forgetting.

How widespread LoRA is — a measurable fact. According to the Hugging Face PEFT team, among twenty thousand eight hundred thirty-four cards with the PEFT tag, ninety-eight point four percent use LoRA. The caveat is mandatory: this is the share among those already tagged PEFT, not among all fine-tuning. But among those who chose the parameter-efficient path, LoRA is practically the no-alternative default. For the narrative it is enough: full fine-tuning — almost never, PEFT and LoRA — today's workhorse.

---

## [s17 · 3 min] — The criteria: what goes where

The third return point to the central question. And here let us lay out what is constantly confused. The question of 2026 is not "RAG or fine-tuning," but "what here is knowledge, and what is behavior."

If the task requires knowledge that changes or needs freshness and provenance — the right tool is RAG or long context, not fine-tuning: knowledge in the weights will grow stale, retraining is expensive, there is a risk of forgetting. If the task requires stable behavior, tone, format, or following a policy, rather than new facts — the right tool is PEFT, not RAG: RAG feeds knowledge into the context but does not change the manner of answering. If the goal is to lower the cost on a narrow task while keeping quality — a pairing of two separate techniques works: first you fine-tune a large teacher model, then you distill a compact student model from it. And if the answer must be deterministic and verifiable — the right tool is ordinary code without AI.

The load-bearing conclusion removes a false dichotomy: a clean "one of" choice is rare, the norm is a hybrid. A mature system combines RAG for changing knowledge, PEFT for stable behavior, and context engineering on top of both.

But a caveat, so that "a hybrid is the norm" does not become the cargo cult of "do everything at once." A hybrid is justified only where the task simultaneously has a knowledge problem and a behavior problem. No behavior problem — fine-tuning is not needed, even if RAG is there. The knowledge does not change and is small — RAG is not needed either. A hybrid is not "more components is better," but "knowledge and behavior are separated across the right mechanisms, each added for its own requirement," not out of inertia.

---

## [s14 · 2 min] — Distillation is not a kind of fine-tuning

[On the slide a Yoda meme: "teacher — student" — a large model passes abilities to a compact one. A light lead-in.]

The meme on the slide already hints at the essence of distillation: a teacher and a student, a large model passes abilities to a small one. But it is important not to confuse this with fine-tuning.

Here we need to introduce a distinction that is often confused, and the confusion produces practical design errors.

Fine-tuning changes the model's behavior — trains it to answer in the needed format, tone, to follow a refusal policy. Distillation solves a different task — compression: transferring the abilities of a large model into a small one, cheaper to operate.

Distillation is a self-standing technique of knowledge transfer and compression, proposed by Hinton and co-authors in 2015. A compact student model learns to imitate the outputs or internal signals of a large teacher model through a separate, specially designed loss function — not through ordinary fine-tuning on "gold" examples. Taxonomically this is not a kind of fine-tuning but a different operation.

In practice the two techniques often go paired: first you fine-tune the teacher for the needed behavior, then distill it into a compact student. But keep them separate: distillation is a separate compression operation, applied in a pair with fine-tuning, not a variety of it. The practical meaning: when you need to make inference cheaper on a narrow task — you think of distillation as a separate step, not "I will just fine-tune once more."

---

## [s16 · 3 min] — Failure: catastrophic forgetting

Let us close the third section with its on-point failure — the one that belongs precisely to fine-tuning. Let us introduce the term through a documented failure.

Catastrophic forgetting — degradation of the model's general abilities as a result of narrow aggressive fine-tuning. By training a model to be very good at one narrow task, you can break what it could do before that.

How it looks. A team fine-tunes a model on a narrow dataset — for example, classifying tickets into their format. On the target metric there is growth: the model classifies excellently. And in parallel, imperceptibly, general abilities sag: reasoning on non-target tasks, following complex instructions. On the graph two lines: the solid one up — the target metric — the dashed one down: general abilities fall imperceptibly.

And here is the trap. If the team measured only the target metric, the degradation is invisible until the model starts being used outside the narrow task. And then "why did it suddenly get worse at reasoning?" turns out to be a consequence of a month-old fine-tuning, for which there are already neither the old weights nor the dataset version. And a counterintuitive detail: as the model's scale grows, the severity of forgetting tends to increase. "Let us take a bigger model to be more reliable" works here in reverse.

[Slow down — this is a criterion, not a curiosity.]

Why this belongs in the section on the choice of architecture. Forgetting itself is a manageable risk. What makes it catastrophic is the absence of discipline: there is no evaluation loop on a representative set of general tasks; there is no versioning of the dataset and weights for a rollback.

Hence a rule you will apply directly: if there is no eval loop and no dataset versioning — do not do fine-tuning. This is not "a risk," it is a "do NOT" criterion: there will be neither a signal of the breakage nor a rollback button. The alternatives: PEFT, where frozen weights give a lower risk; and for changing knowledge — RAG, not fine-tuning at all.

[End of Part 1. Section 4 "Agents" — in speech-part2.en.md.]

---

*Continuation — [`speech-part2.en.md`](speech-part2.en.md): Section 4 (Agents, s18–s25b), Section 5 (Framework, s25a–s30), Q&A (s31), Reserve.*
