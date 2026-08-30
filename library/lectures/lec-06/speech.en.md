---
lecture: 6
title: "Lecture 6. AI in Engineering Design and CAD/CAM"
issue: 101
status: finalized
version: v2
length_min: 75
length_words: "~5775 произносимых / ~6300 файл"
slides_covered: [s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24, s25, s26, s27, s28, s29, s30, s31, s32]
derived_from: "chapter.md (status=reviewed, ~12 860 слов) + deck.yaml (32 слайда, finalized) + plan-v2.md"
note: "Conversational. Local-binding РАЗРЕШЁН (речь для зала ИУ6 МГТУ Баумана). Mars Climate Orbiter — сквозной мотив (крючок ~s11, кульминация s23, callback s26 + s32)."
---

# Lecturer's Speech · Lecture 6. AI in Engineering Design and CAD/CAM

**Duration:** 75 minutes. **Version:** v2 (finalized).

Notation used throughout the text: `[pause]` — a short pause of 2–3 sec; `[pause, let it sink in]` — longer; `[question to the room]` — rhetorical or with a show of hands; `[lower your voice]` — a shift to a serious tone; `[point to slide]` — gesture toward the screen; `[if the demo/image doesn't load]` — a fallback for a technical failure.

---

## [s01 · 0.5 min] — Cover

"Good afternoon. Lecture six — 'AI in Engineering Design and CAD/CAM'. Today we have seventy-five minutes on where artificial intelligence in design actually works, where it pretends to, and — most important for an engineer — where it needs to firmly say 'no'."

[Do not read the subtitle off the slide — go straight to the hook.]

[Move to s02.]

---

## [s02 · 4 min] — Hook: the bracket that gets mistaken for the work of a neural network

[Point to slide — photo of the openwork bracket.]

"Look at this part. [pause, let them examine it] A seat-mounting bracket. It was made by General Motors together with Autodesk, shown in '18. Eight separate parts of the old assembly were consolidated into one. That one is about forty percent lighter and about twenty percent stronger than what was there before. The program produced more than a hundred and fifty shape variants; the engineer chose one.

And its shape is this one. Branching, openwork, like a bone or a coral. No draftsman would draw it by hand. Marketing next to a picture like this writes: 'AI designed this part.'

[question to the room] And here's my first question to you. What kind of AI designed this? [pause, let them think] A diffusion model, like Midjourney for images? A large language model? Some generative neural network?

[lower your voice] The correct answer: none of the generative AI. Not a single neural network 'came up with' this shape. [pause]

It was produced by a deterministic numerical optimizer. It solved a problem precisely posed by an engineer: minimize mass subject to a constraint on stresses and under given loads. And the mathematical statement of this problem is not from the ChatGPT era. It goes back to the work of the Australian engineer Anthony Michell. Nineteen hundred and four. A hundred years before diffusion models.

[pause, let it sink in] This is not nitpicking over words. If you think the part was 'thought up by AI,' you lose your grip on two things at once. First: the result is fully determined by physics and by the statement of the problem. Same inputs — same answer. Forget a load case — you get a mathematically flawless but unusable part. Second: responsibility for the statement and for the verification lies with the engineer, not with 'artificial intelligence.' You can't hold AI to account. You will be held to account.

And it is from this divergence — between how a technology is presented and what it is in essence — that we'll be working today. This is, in effect, the engineer's chief practical risk in year twenty-six.

[if the photo doesn't load: describe it in words — 'imagine a light branching structure, like fused bones.']

[Move to s03.]"

---

## [s03 · 2.5 min] — Lecture map: three questions and six parts

"To keep from getting lost in this menagerie, you and I need one working tool. It's simple. It's three questions you ask *yourself* before trusting a tool with a design decision.

Question one: is this deterministic math that, given the same inputs, gives the same answer — or a trained probabilistic model that samples from a distribution? That's one.

Question two: what exactly is being optimized, and who set the constraints — the engineer or the data? That's two.

Question three: who bears the legal and engineering responsibility for the result? That's three.

[point to slide] Remember these three questions. We'll come back to them in every part of the lecture — this is our anchor.

And there are six parts. First, the foundation: what does 'kind of AI' even mean, and a taxonomy of six classes. Then, one by one, the three classes where the cost of error in design is highest: generative design, surrogate models, and generative AI with large language models. Then — where AI isn't needed or isn't applicable in principle, and who is responsible for it all. And at the end we'll assemble everything into a single decision rule on a concrete problem.

An honest caveat right away. We'll learn to name all six classes and place them on the axis. But in depth, with a dissection of the failures, we'll examine three — the ones where an error costs the most. This is not a gap; it's a deliberate focus.

[Move to s04 — the first section.]"

---

## [s04 · 0.3 min] — Divider: Part 1

"Part one of six. Name the kind of AI — the foundation and the taxonomy of six classes."

[Minimal. Move to s05.]

---

## [s05 · 3.5 min] — Foundation: solving an equation vs. guessing from examples

"Before we enumerate the classes, you and I need one distinction. Without it, the whole further conversation about 'where AI fails' would sound like 'well, it sometimes makes mistakes.' And what matters to us is not 'sometimes' but *why* — why the errors of some classes are structurally inevitable and of others are not.

The distinction is this. On one side — deterministic optimization. It *solves an equation* the engineer posed. You formulate an objective function — say, the mass of a part. You set constraints — force equilibrium, a strength condition, a volume constraint. The algorithm numerically searches for the point that satisfies these equations. The physical law is present here *explicitly* — it is written into the equilibrium equations, and they are solved at every iteration. Same input data — same answer. Reproducible. Traceable.

On the other side — a trained generative model. A diffusion model of geometry or a large language model. [lower your voice] Inside it there is no equilibrium equation. None at all. It was trained on a huge corpus of examples — shapes, texts, drawings — and it learned to reproduce the statistics of that corpus. That is, 'what a part usually looks like' or 'how a paragraph of a specification usually sounds.' When such a model 'generates' a part, it produces something *similar to what was in the training data*. Not something that *satisfies the equilibrium equation*.

[pause, let it sink in] I'll put it as the load-bearing thesis of the whole lecture. Deterministic optimization solves a given equation and, given the same inputs, gives the same answer. A trained generative model guesses from learned examples, and there is no physical law inside it — it reproduces what the answer usually looks like, not what satisfies the equation.

And from this comes an immediate, important consequence. An error of a deterministic optimizer — if the statement is correct — is reproducible, it's visible. But an error of a generative model is *not self-diagnosing*. The model does not 'know' that the geometry it produced does not carry the load. Exactly as a language model does not 'know' that the GOST number it named does not exist.

This axis is our working tool for the whole lecture. Whenever you meet any tool 'with AI,' the first thing you do is place it on this axis. Does it solve an equation — or guess from examples?

[Move to s06.]"

---

## [s06 · 3.5 min] — Skeleton of the taxonomy: one axis, six labels

"Now, with this axis in hand, let's lay out six classes on it. Notice: I am *not* giving you the full table with all its attributes right now — who guarantees what, what maturity, who's responsible. It would overload you now: half its cells are terms you don't yet know. We'll assemble this full matrix gradually and present it at the very end — when each cell is filled with meaning.

[point to slide — horizontal axis] There's one axis — deterministic on the left, probabilistic on the right. Six classes along it.

On the left, the most deterministic — optimization ML, also known as topology optimization. A numerical search that moves the density of material at every point of the part and minimizes mass subject to the constraint 'stress no higher than allowable.' Same inputs — same answer. This is what marketing calls 'generative design.'

Next to it — evolutionary, genetic algorithms. A stochastic search by mutation and selection, but according to an objective function *explicitly set* by the engineer. Random — yes, but not a generative model.

Further, surrogate models and PINNs. A neural network that learned the mapping 'geometry and loads — stress fields' on thousands of past computations. It answers instantly, but it guesses rather than solves.

Then computer vision — convolutional networks for defect inspection. A probabilistic image classifier.

Then the LLM assistant — a large language model for text: drafts of memos, explanation of standard clauses, generation of CAD scripts.

And the rightmost, the most probabilistic — generative AI for geometry. Diffusion and transformer models that produce a 3D shape from text or a sketch. A pure generative model. Physical guarantees — zero.

See the structure? Classes one and two — optimization of a given function. Class three — approximation of a solver. Classes four through six — probabilistic models of perception and generation, with no physical law inside at all. And the farther right along the axis — the fewer the built-in guarantees and the higher the cost of error.

[Move to s07.]"

---

## [s07 · 3 min] — Recognition of pair 1: optimization ML + surrogate/PINN

"Let's run quickly through recognition — three columns per class: when it fits, when it's not applicable, what the classical alternative is. Not to memorize — to recognize.

Optimization ML, topology optimization. Fits: reduce mass at a given stiffness, find a non-trivial force scheme, a part for additive manufacturing. Not applicable: when constraints are set incompletely — it will honestly produce an optimum *under the wrong statement*; it doesn't replace the manufacturability check and normative inspection. Classical alternative: parametric optimization with section selection from a standard range plus a code-based calculation. And for a standard structure — just a normative calculation with no optimization at all.

Surrogate models and PINNs. Fits: quickly run many variants within the training domain, preliminary screening. Not applicable: extrapolation beyond the training distribution, problems with field discontinuities, final certification calculations. Classical alternative: a full FEA or CFD solver with a mesh-convergence check.

Notice the format: 'when yes — when no — what to replace it with.' This is not slide decoration. This is precisely the operational form of our main question. You and I will repeat this frame for every class.

[Move to s08.]"

---

## [s08 · 3.2 min] — Recognition of pair 2: generative AI/LLM + CV + GA

"Three more classes in the same frame.

Generative AI and LLM. Fits: early concept sketch, mood board, shape variety for a design review; a draft of technical text subject to mandatory review. Not applicable: any part going into calculation or production without full manual rework; a source of truth on grades, standard numbers, tolerances. Alternative: parametric CAD with explicit constraints plus deterministic topology optimization plus FE validation; the normative base and grade catalog.

Computer vision. Fits: high-volume routine sorting as a first filter, highlighting suspicious zones to an operator. Not applicable: as the sole arbiter of fitness in safety-critical non-destructive testing — models transfer poorly between rigs and materials. Alternative: normative inspection with a qualified NDT technician and a certified POD methodology — probability of detection.

Evolutionary algorithms. Fits: conflicting requirements that don't yield well to gradients. The canonical example — the evolved antenna of NASA's ST5 mission, launched in two thousand six: a genetic algorithm found an 'organic'-looking shape in about three person-months versus five for the classical approach, and it worked as intended. Not applicable: when interpretability and certification explainability are needed — an expert can't 'read' this shape and can't explain it to a regulator. This is a weak point even for the successful ST5.

[point to slide — three questions at the bottom] And here are those very three anchor questions again. Deterministic or probabilistic. What is being optimized and who set the constraints. Who is responsible. Keep them in mind — from here on we apply them for real.

[Move to s09 — the second section.]"

---

## [s09 · 0.3 min] — Divider: Part 2

"Section two of six. Generative design is not generative AI."

[Move to s10.]

---

## [s10 · 2.5 min] — The terminological trap

"Let's return to our bracket from the very beginning and state the debunking thesis at full force.

When Fusion, Creo, or CATIA show a 'Generative Design' window and caption the result with the words 'AI generates the design' — a substitution of concepts is taking place. And this substitution has a concrete engineering cost. Under the hood is topology optimization. A deterministic numerical method. Same inputs — same result. Not a single trained generative model inside. By the way, Autodesk itself draws this distinction on its blog — it states that topology optimization is a method *inside* generative design, not 'generative AI.' [don't quote verbatim — paraphrase.]

[question to the room] Why does this matter practically, not at the level of nitpicking over terms? An engineer who thinks 'AI came up with the part' makes two mistakes at once. First: he underestimates his responsibility for the statement of the problem. If AI came up with it, then AI is the one to answer for it. But in reality every feature of the shape is determined by the given loads and constraints. Set them wrong, and the shape will be mathematically optimal and engineering-wise useless. The second mistake: he overestimates the tool's 'creativity.' The optimizer does not invent the part's function. It only distributes material within a given space under a given function.

The lesson of the section is direct: before trusting — ask 'what kind of AI is this.' And for 'generative design' the honest answer is almost always: deterministic optimization, not a generative model.

[Move to s11.]"

---

## [s11 · 3.8 min] — Classical lineage: from the known to SIMP

"And now — where all this came from. And we'll build not from empty ground, but from what you already know.

Bridge one — from strength of materials. You know the strength condition: the von Mises equivalent stress must not exceed the allowable. And from the same place — the intuition of underloaded material. If in some cross-section of a part the stress is far below the allowable — that material isn't working at full capacity. In principle, it can be removed, and the part will still hold. Push this thought to the limit — and you get the idea of a fully-stressed structure: exactly as much material as needed, nothing excess anywhere. It was *this* idea that Michell formalized in nineteen hundred and four. I'll stress: he gave the intuition and the statement, not a formula. Practice came only with the computing technology of the sixties. AI did not give birth to the idea here — it made an old idea computationally cheap.

Bridge two — from lecture two of this course. Remember gradient descent? A step against the gradient, repeat. The same method of steepest descent was proposed by Cauchy in eighteen forty-seven. And it is precisely this — not a neural network — that moves material densities in topology optimization. The only difference is *what* we move: in a neural network — the weights, here — the material density at every point. The search algorithm is the same, and it is a century and a half older than deep learning.

The method itself, as a numerical one, was born with Bendsøe and Kikuchi in eighty-eight. The industry's workhorse is the SIMP method, Bendsøe, eighty-nine. The idea is simple, and it's the one that refutes the word 'AI.' To each cell of the part we assign a density from zero to one: zero — void, one — material. Stiffness is taken as density to the power *p*, usually cubed. Why a power? Without it, the optimizer would leave 'gray' half-densities — physically meaningless. The power makes intermediate values unfavorable, and the solution is pushed toward black-and-white.

[pause]

[point to slide — lineage timeline] What's inside the loop? At every step the equilibrium equation is *explicitly solved*. The physical law is in the algorithm's math. No trained generative model. The algorithm does not sample from a distribution of designs — it converges to the minimum of a function set by the engineer. When Fusion 'generates' a bracket — under the hood is a descendant of SIMP of the year eighty-nine plus an FE solver in the loop. 'AI generates' here is misleading exactly as much as 'AI solved the quadratic equation' would be.

[pause] And a small hint at the future. Remember the phrase 'the seam between systems': inputs from one place, expectations in another. We'll come back to it in the most dramatic part of the lecture. KKT and Lagrange multipliers — the formal optimality condition — we'll leave to the chapter.

[Move to s12.]"

---

## [s12 · 3 min] — Real industrial cases

"Two cases have become canonical. Let's examine them with the kind of AI specified.

General Motors, that very seat bracket. Eight parts of the assembly consolidated into one. The chosen variant — about forty percent lighter and about twenty percent stronger than the previous one. The program produced more than a hundred and fifty alternatives. Kind of AI: multi-criteria numerical optimization plus cloud enumeration under the goal 'minimum mass subject to stress constraints and a given manufacturing method.' This is *not* a diffusion model. 'A hundred and fifty variants' are a hundred and fifty points that satisfy the optimality condition under different weightings of the goals. Not a hundred and fifty samples from a neural network.

Airbus, the 'bionic partition' for the A320. A cabin partition: mass reduced by about forty-five percent — on the order of thirty-five kilograms versus about sixty-five for the standard one. A lattice 'bone' structure, Scalmalloy material for laser sintering, assembled from many printed sections. Kind of AI again: topology and lattice optimization plus evolutionary enumeration. Not a generative model.

[question to the room] And note the recurring pattern: both parts require 3D printing. This is no accident. This is a constraint we'll return to literally two slides from now — and it will turn out to be more important than it seems.

[Move to s13.]"

---

## [s13 · 2.8 min] — Russia: an honest picture

"What about Russia. The picture is honestly uneven, and honesty here is precisely the value, not an occasion for delight or gloom.

Real achievements. OKB Sukhoi produced a load-bearing bracket using a bionic approach — an aluminum bracket for the Su-57. The digital model was built on a supercomputer. The part is about a quarter lighter than traditional analogues. A prototype door-hinge bracket for the MS-21-300 was also worked on, in titanium versions — laser layer-by-layer powder fusion.

And now the substitution of concepts. In KOMPAS-3D, topology optimization is available via the APM FEM application, a joint product of ASCON and the NTC 'APM.' According to the vendor, it excludes a substantial fraction of the model's volume while preserving strength. [don't state the exact number — vendor claim.] Essential for our lecture: this is a deterministic density-based algorithm of the SIMP family. *Not AI.* The same terminological trap as with Western vendors, just on a domestic tool that you know from your CAD lab classes. And the C3D geometric kernel is, by the way, a strategic asset: essentially two or three geometric kernels are commercially available in the world, and having one's own is a great rarity.

[lower your voice] And where Russia honestly lags. A mature AI-generative engine at the level of Fusion, as of year twenty-six, essentially does not exist. Only topology optimization is confirmed — deterministic. This is an honest gap, and there's no point dressing it up. For an engineer this means: the domestic alternative to Western 'generative design' is classical topology optimization plus manual reconstruction. A normal tool with clear guarantees.

[Move to s14.]"

---

## [s14 · 2.9 min] — The section's failure: garbage-in → optimal garbage

"Now — the fundamental limitation of topology optimization. And it is *not the one* usually expected.

The optimizer honestly solves the posed problem. The word 'posed' is key. If the statement is incomplete — a fatigue load case is forgotten, technological constraints of casting or cutter access aren't set, assembly isn't accounted for — the algorithm will still converge to a mathematically flawless optimum. But *under the wrong statement*. Garbage-in — optimal garbage: garbage at the input gives optimal garbage at the output.

[question to the room] This is familiar to you from strength of materials, right? You missed a design load case — the calculation is arithmetically correct, the structure is dangerous. Here it's the same, but more insidious: a beautiful 'organic' shape looks so convincing that its unfitness isn't visible to the eye. The chief risk of topology optimization is not a 'hallucination' — there is none here, the method is deterministic. The chief risk is *incompletely set constraints*.

[point to slide — pipeline] And a concrete example. Topology optimization readily produces a closed internal cavity with curved ribs that no cutter can reach at any orientation, and that can't be obtained by casting without a non-extractable core. It can be manufactured only additively. Remember I promised to come back to 3D printing? Here it is. Russian engineers note directly in publications: generative geometry is often non-manufacturable by traditional methods, hard to measure and to inspect against ESKD, and requires manual reconstruction. That is, a generative tool is an *input* into the design process, not its *output*.

And this is not a 'childhood illness' about to be cured. There is simply *no* term in the optimization criterion for technological inaccessibility, unless the engineer put it there. Lesson: the right tool for a serial machined part is classical parametrics plus manual topology optimization for manufacturability. The optimizer as an idea generator — yes. As a source of finished production geometry for a series — no.

[Move to s15 — the third section.]"

---

## [s15 · 0.3 min] — Divider: Part 3

"Section three of six. AI speeds up the computation, but does not replace the physics."

[Move to s16.]

---

## [s16 · 3 min] — From the familiar FE analysis to a surrogate

"In the previous part we solved the equilibrium equation inside the optimization loop and didn't specify what equation it was. Let's close the gap — again from the familiar.

You've seen FE analysis at least as a CAD user: break the part into a mesh of finite elements, apply loads and fixtures, get a color picture of the stress field. What the solver does in essence: it takes a load vector, solves a system of linear equations for displacements, and from displacements computes strains and stresses. The matrix of this system is the stiffness matrix; it encodes geometry, material, and fixtures. This is proven, traceable, deterministic math that is more than sixty years old.

[question to the room] And what is a surrogate? It is a neural network that learned the mapping 'geometry and loads — stress field' on thousands of *past* FE computations and now answers almost instantly. The key word is *learned*. The surrogate does not solve the equation. It *guesses its solution from examples*. This is exactly the right side of our axis: it guesses from learned examples.

How does a surrogate differ from the generative model we'll examine in the next part? In that the training examples were physically correct — a certified solver computed them. Therefore, within what the surrogate 'saw,' it is reliable. Beyond that — it is not.

[point to slide — two columns] Under the hood — a system of equilibrium equations; the surrogate doesn't solve it. The full derivation of this system, the weak Galerkin form — I leave to the chapter, read it as lineage. And remember one economic detail: the surrogate is trained *in advance*, offline, on an archive of thousands of expensive computations. For it to be useful — someone must first pay for thousands of runs of the exact solver. This will be useful to us in a minute.

[Move to s17.]"

---

## [s17 · 2.5 min] — State of 2026: reading the numbers critically

"What the market offers by year twenty-six. And we read the numbers critically.

Ansys SimAI, release 2026 R1 — a surrogate based on a reduced-order model, interpolating between previously computed results; the claimed speedup — on the order of tens to hundreds of times on compute-heavy problems. Altair PhysicsAI within HyperWorks 2026 — trained on a historical archive of simulations, with a claimed speedup *up to on the order of a thousand times*. NVIDIA PhysicsNeMo — an open Python framework for physics-AI, from pure PINNs to neural operators.

[lower your voice] A methodological remark, and an important one. Each of these speedups is 'up to N times' on a special case *favorable to the vendor*. Averaged across the fleet of problems, the gain is more modest. And almost always the return-on-investment calculation *excludes* the cost of generating the training archive — those very thousands of expensive runs of the exact solver I just mentioned. Treat numbers of the 'thousand-fold' variety as an upper bound on a narrow class of problems. Not as a typical speedup. This is an engineer's reflex — you see a beautiful number, ask: on what exactly, and what wasn't included.

[Move to s18.]"

---

## [s18 · 3.3 min] — PINN: hype versus reality

"A separate subclass — PINNs, physics-informed neural networks. The idea is beautiful: a penalty for the residual of a differential equation is added to the loss function, so the network 'respects' the physics. Marketing presents this as 'a neural network that knows physics.' The reality, per peer-reviewed surveys of year twenty-five, is markedly more modest.

I'll explain the main limitation through strength of materials — you know this. A stress concentrator. At a hole, a fillet, a groove, the stress field has a sharp local peak. It's precisely there that the part fails; it's for the sake of this peak that the stress concentration factor is computed. So here's the thing: a neural network with smooth activation functions easily learns smooth fields and poorly learns sharp jumps. This property is called spectral bias: the network 'gravitates' toward smoothed solutions.

[lower your voice] The consequence is direct and unpleasant. A PINN trained on a part with a concentrator tends to *smear out* the peak at the hole and produce an *underestimated* stress in the dangerous cross-section. [pause] An underestimated stress at a concentrator is an underestimated risk of fracture. This is the worst possible type of error in a strength calculation. Not 'a bit inaccurate,' but 'dangerous in exactly the wrong direction.'

And more. A PINN does not outperform mature numerical methods on standard forward problems, and is often *slower*. It doesn't generalize beyond the training scenario. On failure it is opaque: you can't attribute the blame — physics, data noise, or network capacity. And on noisy measurements it is dangerous: differentiation amplifies high-frequency noise, and the network begins to fit the noise as physics. Per the surveys, this is a fundamental property of the method, not a flaw of the implementation — you can't 'fix' it with a bigger network.

[point to slide — where PINN is useful] Where PINN is genuinely useful — there is such a niche. Sparse data, *inverse problems* — recovering an unknown parameter from a measured response, complex geometry, data assimilation. A narrow but real area. Beyond it, 'PINN instead of a solver' is false confidence.

[Move to s19.]"

---

## [s19 · 2.6 min] — Why a surrogate at all: the applicability criterion

"[question to the room] A natural question: if a surrogate guesses, and a PINN smears things out — why do we even need a third part? The answer is constructive.

Why a surrogate is useful to you personally. At the *search* stage a designer runs through dozens and hundreds of variants: what if the rib is thicker, what if the boss is moved, what if a different material. Computing each with a full certified FEA is expensive in time. This is where a surrogate is in its place: run five hundred bracket variants in minutes, screen out the obviously weak ones, keep five to ten candidates. But — and this is the criterion — the *final* calculation for each selected candidate is done by a certified deterministic solver. The surrogate speeds up the enumeration at the search stage. It does not produce a certifiable result.

[lower your voice] The central conclusion of the part. A surrogate is valid only within the domain it was trained on. Extrapolation beyond it — a new regime, a new material, geometry out of distribution — gives a *silent error*. The model does not report that it has left the boundary. It simply confidently produces a wrong number. Remember this formulation: the absence of an error report here does *not mean* correctness.

Russia. The CAE package 'Logos' by Rosatom — the flagship of import-independent supercomputer simulation; native neural-network solvers inside the kernel are not confirmed in open sources, surrogates are applied in the ecosystem's wrapper. The CML-Bench platform of the Polytech, led by Borovkov — an example of an accumulated knowledge base, with a claimed more than three hundred and sixty thousand solved problems. This is a Russian illustration of the same pattern: an archive of computations — a surrogate assistant.

[Move to s20 — the fourth section.]"

---

## [s20 · 0.3 min] — Divider: Part 4

"Section four of six. Where a hallucination costs dearly. And remember the foundation: generative AI contains no physical law."

[Move to s21.]

---

## [s21 · 2.8 min] — Landscape 2026: marketing versus maturity

"Let's split the landscape into two layers that differ greatly in maturity.

Layer one, relatively mature — LLM copilots on top of CAD. Autodesk Assistant in Fusion: a text prompt turns into commands — 'split this body,' 'extrude the face by an inch' — it can also generate and execute scripts via the API. Siemens Design Copilot: an assistant on Siemens's knowledge, with a claimed auto-generation of a significant share of the two-dimensional drawing views. Mastercam Copilot — an assistant for machining programming. This is the LLM as an *interface to existing deterministic operations*, under the engineer's control.

Layer two, immature — text-to-CAD and neuro-CAD. Zoo.dev — an open text-to-CAD, text into 3D with export. Autodesk Project Bernini — a research generative 3D model. [point to slide — gold highlight] And here's an essential detail: Autodesk itself marks Bernini as 'strictly experimental, not for public use.' This is an honest maturity signal from the vendor itself — it contrasts with the marketing 'AI designs for the engineer.' Autodesk Neural CAD is announced, but commercial availability is 'upcoming,' with no date. The academic front is active, but these are research works, not production tools.

Conclusion on the landscape: the mature thing is the LLM as an interface to deterministic operations. Generation of *geometry* from text in year twenty-six is a concept and an early beta. This is confirmed even by the vendor's own labeling of Bernini.

[Move to s22.]"

---

## [s22 · 2.7 min] — The pattern: where an LLM is useful

"There is a concrete pattern where an LLM brings real benefit. Let's state it precisely, to separate it from the anti-pattern on the next slide.

An LLM is good at generating a *draft of a text artifact with precise terminology and form*: the structure of an explanatory memo, a template for technical specifications, a reformulation of a requirement, an explanation of how a standard's clause is arranged. Here the model is strong precisely in what it was trained on — linguistic form. A well-crafted prompt describes the required structure and terminology of the document, and the output is a skeleton that saves time on routine.

[lower your voice] But — and this is a boundary built into the pattern. The *factual content* — specific material grades, standard numbers, numerical tolerances, coefficient values — is subject to mandatory verification by the engineer against the normative base. The LLM gives the correct *form* and potentially the wrong *content*. This combination is useful for a draft and dangerous for a final document.

The pattern is formulated thus, write it down: the LLM writes the draft — the engineer verifies the facts against the primary source. Always. Without exception. [pause] And now — what happens when this rule is broken. This is the most important slide of the lecture.

[Move to s23.]"

---

## [s23 · 3.5 min] — The anti-pattern: Mars Climate Orbiter and its brethren

[lower your voice — the climax.]

"The twenty-third of September, nineteen ninety-nine. Contact with the interplanetary station Mars Climate Orbiter was lost during Mars orbit insertion. The total cost of the mission — about three hundred and twenty-seven million dollars. [pause, let it sink in]

[question to the room] Complex physics? An error in the equations of celestial mechanics? [pause] No. The ground software module that computed thruster impulses — contractor Lockheed Martin — produced data in pound-force-seconds. And the trajectory-computation program — JPL — expected newton-seconds. The discrepancy — more than fourfold, four point four five. The conversion was *performed by no one*. JPL assumed the other side had done it.

And here is the finding of the investigation board — and for us today it is central. Responsibility was placed *not* on an error in a formula. But on the *absence of an independent check* that would have caught the mismatch at the interface of the two systems. At the seam. Where each assumed the other would check.

[pause, let it sink in] Let's project this onto year twenty-six. An LLM assistant in the engineering process is *exactly such a seam between systems*. Remember I asked you to remember this phrase back in the part about SIMP? Here it is. It takes quantities from one context, passes them into another, and it *confidently* confuses units: psi and megapascals, millimeters and inches, newton-meters and pound-feet. Accepting a number from AI without an independent dimensional check is a digital Mars Climate Orbiter. Three hundred and twenty-seven million dollars for an unchecked seam.

[point to slide — Gimli and Hyatt in one line] Two brethren of the same failure, briefly. Gimli Glider, '83: a Boeing 767 ran out of all its fuel in flight due to a manual recalculation with the wrong coefficient — they landed with no engines, by gliding, and got away with it. A human *confidently* applied the wrong coefficient — AI does the same just as convincingly. Hyatt Regency, '81: the collapse of two suspended walkways in a hotel, a hundred and fourteen dead. The manufacturer changed the suspension joint to simplify assembly — the load on the connection doubled — the engineer signed off effectively without an independent recalculation. Accepting an AI suggestion to 'let's simplify this joint' without a recalculation is the structural equivalent of that sign-off.

The connecting thread of the three: not one catastrophe came from complex physics. All three — an undetected mismatch or an unchecked change at a seam where each thought the other would check. An AI assistant creates such seams in commercial quantities. The evidence — on the next slide.

[Move to s24.]"

---

## [s24 · 2.7 min] — Benchmarks and the lesson learned

"The historical analogues showed a *pattern*. Benchmarks give *reproducible statistics* — this is an argument of a different type, and you can't lump them into one 'argument.'

ORCA Benchmark, year twenty-five. Five hundred real quantitative problems, the five strongest models of year twenty-six — the flagships of OpenAI, Google, Anthropic, xAI, DeepSeek. Accuracy — roughly in the range of forty-five to sixty-three percent. The best model — on the order of sixty-three. [pause] That is, on engineering calculations the strongest models err on about a third to a half of the problems.

EngiBench: a drop in accuracy of about eight to eleven percent under a simple *rephrasing* of the problem statement. A sign that the model relies on surface pattern-matching rather than robust reasoning. And an aerospace case: a model, asked about the surface treatment of titanium fuselage fasteners, recommended a coating that violates *three* aerospace standards at once. What's valuable is not the model's name but the character of the error: it sounded expert — and violated three independent standards at once.

[point to slide — gold lesson] The lesson learned, three points. First: an LLM is not a source of truth on grades, GOST, tolerances, numbers. 'Confidently wrong' is more dangerous than 'doesn't know,' because it doesn't raise your guard. Second: dimensional and factual control plus independent verification are mandatory at every interface with AI. Third: an AI suggestion that changes the force scheme is formalized as a formal change-request, not accepted as a chat remark. Loud specifically-AI catastrophes in design are still few — the topic is young, the damage comes with a lag. This is not an argument for safety. The engineer's task is to prevent the first loud AI failure, not to dissect it after the fact.

[Move to s25 — the fifth section.]"

---

## [s25 · 0.3 min] — Divider: Part 5

"Section five of six. When to tell AI 'no'."

[Move to s26.]

---

## [s26 · 3.8 min] — Criteria of non-applicability and the right tool

"This is the concentrated core of the whole mission of the course. Earlier we looked at *how* the classes fail. Here — the *criteria* by which you say 'no' in advance, and which tool is more correct.

There is one decisive rule, write it down: the higher the determinism of the problem and the cost of error — the less room in it for probabilistic AI. Let me unfold this into criteria.

A certification calculation. Reproducibility and traceability are needed; LLMs and surrogates give scatter and are not certifiable. The right tool — a certified deterministic solver with a convergence check plus independent verification.

A safety factor. It is set by the code and the responsible engineer, not 'optimized' by a model; AI can 'eat up' the margin under the wrong goal. The right thing — a normative value per the standard plus engineering justification.

Normative inspection — GOST, tolerances, fits. An LLM hallucinates standard numbers and grades. The right thing — the normative base and grade catalog plus a normative inspector, cross-checking against the primary source.

Legal responsibility. AI is not a subject of responsibility; the signature is the engineer's. Further: if there's an exact deterministic solver — an approximation isn't needed. Safety of life — load-bearing structures, aviation, pressure vessels — the cost of error is a life, and a probabilistic model gives no guarantees. Units at the seam between systems — our Mars — machine dimension checking plus a unified system of units. A change to the force scheme — our Hyatt — a formal change-request with an independent recalculation.

[lower your voice] Summary — the operational form of the course's mission. AI in engineering is a tool for *expanding variety and drafting*. Not an *arbiter of truth* and not a *bearer of responsibility*. And note honestly: this is *not a ban* on AI. Topology optimization — deterministic — is nowhere banned in this table. The bans concern the probabilistic classes where a guarantee is needed. This is a designation of place, not an ideology.

[Move to s27.]"

---

## [s27 · 2.5 min] — Russia: normative boundaries

"The Russian context adds concrete boundaries — and they are hard, not a matter of taste.

The ESKD barrier. The Unified System of Design Documentation requires strictly regulated drawings, specifications, tolerances. 'Grown' organic geometry fits poorly onto the two-dimensional drafting paradigm — issuing inspection-compliant documentation for it is non-trivial. This is familiar to you from your ESKD coursework: a beautiful shape that there's no correct way to dimension and tolerance.

Attestation. The computation kernel APM Structure3D holds a Rostekhnadzor certificate — without certified verification a structure is not admitted to supervised production. 'Logos Strength' undergoes industry verification. An AI-generated or surrogate-computed structure without certified verification is formally not admitted — the boundary is legal.

Sanctions-and-licensing risk. The forced blocking of previously working AutoCAD and Fusion for Russian users in twenty-two to twenty-four — a concrete example: a cloud-tethered tool becomes a single point of failure at the state level. The architectural conclusion, and this is risk engineering, not ideology: for critical infrastructure, local deployment plus an open format lowers the risk class. The drivers — Federal Law 187 on the security of critical information infrastructure and the amendments of Federal Law 58.

And the law. Under Russian law a machine is not a subject of copyright; responsibility for the structure is borne by the engineer or the executing organization, not the tool. This removes the illusion of 'AI designed it — AI is to blame.'

[Move to s28.]"

---

## [s28 · 2.9 min] — Human versus AI and the contrast with TRIZ

"Let's close the part with a conceptual boundary that ties the whole spine together.

Who is responsible. The engineer sets the constraints and *is responsible* for the result. The signature of the designer and the analyst under the documentation is legal responsibility for safety. It cannot be delegated to an optimizer or a neural network. This constraint is not technical — it is *deontological*. Responsibility always rests with the human, regardless of the geometry's origin. AI proposes the shape — the human is responsible and verifies.

[point to slide — TRIZ contrast] And a useful historical comparison — one close to you. The Theory of Inventive Problem Solving, TRIZ, Altshuller, work begun in year forty-six. It formalizes *invention* — resolving a technical contradiction, choosing a working principle, the ideal final result. Whereas 'generative design' optimizes the *shape at a fixed function and a fixed space*. These are different levels. Changing the working principle of an assembly, resolving the contradiction 'strong yet light' by changing the scheme — this is the level of TRIZ and engineering creativity. It is inaccessible to a topology optimizer — that one only distributes material within a given volume.

[lower your voice] A historical irony, think about it. Back in year forty-six the Soviet engineering school asserted that creativity is algorithmizable — but it algorithmized precisely *conceptual invention*. Whereas modern 'generative design' algorithmizes a narrower slice than TRIZ promised eighty years ago. The formula that ties up the spine: AI generates — the human is responsible, verifies, and invents the function.

[Move to s29 — the sixth section.]"

---

## [s29 · 0.3 min] — Divider: Part 6

"Section six of six, the last. Synthesis: the decision rule on a concrete problem."

[Move to s30.]

---

## [s30 · 2.4 min] — Worked decision: lighten the bracket

"Let's assemble everything into one fully worked example. This is precisely that measurable form of a justified choice for which the lecture exists.

The problem. Given a load-bearing bracket, we need to reduce its mass. Two production scenarios. Variant 'a': a serial part, milled on a five-axis machine. Variant 'b': a single part, made additively — metal 3D printing. We run *both* branches through our three anchor questions.

Variant 'a', milling. Question one: a strength guarantee for a serial part is needed — the base tool is deterministic. Generative AI of geometry drops out immediately — probabilistic, no guarantees. Question two: we optimize mass subject to a strength constraint, but the critical constraint is milling manufacturability. Pure topology optimization will produce a shape non-manufacturable by a cutter — our garbage-in. A surrogate for certification is not applicable — a silent error. Question three: certified verification and a signature are needed. Conclusion on 'a': classical parametrics plus manual topology optimization for manufacturability, and the final step — a certified FEA.

Variant 'b', additive. The same first question — a deterministic tool. But additive removes the technological constraints on shape — the 'organics' here is manufacturable. The topology-optimization statement works at full force; we add printing features to the constraints. The part is load-bearing — the final step is still on a certified solver; a surrogate is appropriate for enumerating topologies, not for the final step. Conclusion on 'b': deterministic topology optimization — that very 'generative design' — plus the final step on a solver; generative AI of geometry — no.

[point to slide — gold] Notice: the same problem gave *different* justified answers. And they were separated by *one* anchor question — the second, about the completeness of the statement and manufacturability. Not 'by taste' — by walking down the tree with an explicit 'why not the others.'

[Move to s31.]"

---

## [s31 · 2.4 min] — The decision rule and the full taxonomic matrix

"Now — a mental checklist, your decision rule. Five points, before you trust a tool with a design decision.

First: name the kind of AI, place it on the deterministic — probabilistic axis. Second: deterministic or probabilistic — does it solve a given equation or guess from examples. Third: what is being optimized and who set the constraints — is the statement complete, no load case or normative inspection missed. Fourth: is there an exact or normative tool — if the problem is a certification one or there's a certified solver, probabilistic AI is superfluous or dangerous. Fifth: who is responsible — the signature is not delegated to a model.

[point to slide — full matrix] And now, when every cell is filled with meaning — that very full matrix of six classes that I promised at the start and deliberately didn't give right away. Nature, what it guarantees, maturity, who is responsible. Look at the last column — 'who is responsible.' Everywhere one word: the engineer. This is not for memorizing, it's for applying.

[pause] And, so that you understand — this is not theory from the future. This is being done right where you are, here. At the RK9 department, in the Research and Education Center for supercomputer modeling at Bauman, in the advanced engineering school for digital materials science — with this whole spectrum they work right now: from certified solvers to accumulated archives of computations. What was described today is current engineering practice.

[Move to s32.]"

---

## [s32 · 0.9 min] — Q&A

"The main thing that should remain is not a list of technologies but the discipline of the question: name the kind of AI, check the completeness of the statement, ask about the exact normative tool, remember — the signature is not delegated. Remember Mars — three hundred and twenty-seven million for an unchecked seam; don't create such seams with AI silently. The ability to say 'no' with justification is what distinguishes an engineer from a button operator. [point to slide — Q&A] Thank you. Now — your questions."

[Backup questions — ONLY if the room is silent; they are not part of the s32 speaker timing, they go into the reserve:]
— If 'generative design' is math from nineteen hundred and four, why the buzz precisely now?
— PINN is 'physics-informed' after all — why do I say it doesn't know physics?
— Russia lags in AI-generative CAD — is this a death sentence? [hint: a differentiated picture, the C3D kernel, an honest alternative.]

---

## Reserve (buffer ~3–4 min within the 75)

The buffer is distributed within the long fragments (s02 hook, s11 lineage, s23 Mars, s26 criteria) — where the 'let it sink in' pauses give the lecturer flexibility of ±20–30 sec. If the lecture is running faster — go deeper on any of the three Q&A questions above, or work through an additional example for s30 (a cast gearbox housing, serial production — the answer from the self-check of Part 6 of the chapter). If slower — s07/s08 (recognition) and s17 (state of 2026) are compressed to the key lines without losing the thread.

---

## Pre-lecture preparation / Pre-flight

Each point is a concrete action with a checkable result. To be done on the day of the lecture.

**Live-data refresh (3 points from the chapter's `verify_day_of` — MANDATORY):**

1. **ORCA benchmark (for s24).** Open the current ORCA leaderboard / arXiv:2511.02589 and verify the accuracy range "~45–63%, best ~63%". Cadence — weekly; fresh 2026 flagships may shift the upper bound. If it has changed — correct the spoken formulation on s24 ("best ~63%" and "a third to a half of the errors") and note it synchronously in the s24 speaker notes. Source: https://arxiv.org/abs/2511.02589.
2. **Ansys SimAI (for s17).** Check https://www.ansys.com/products/ai/simai — the current release. In the speech and on s17 it says "release 2026 R1". If 2026 R2 has come out — replace the release number in the spoken phrase on s17 and in the s17 speaker notes.
3. **Altair PhysicsAI "up to ~1000×" (for s17).** Sanity-check the vendor's claim "up to on the order of a thousand times" (HyperWorks 2026 / PhysicsAI) against https://www.prnewswire.com/news-releases/altair-hyperworks-2026-delivers-design-and-simulation-at-scale-with-ai-302634806.html — whether it has been revised. If the vendor has changed the wording — update the spoken text on s17 as a range, not an exact number.

**Content and navigation:**

4. Run through the deck `library/lectures/lec-06/rendered/lec-06.pdf` in full (32 slides): make sure the photo of the GM bracket on s02 displays. If it doesn't load — prepare a fallback: the verbal description from the s02 fragment ("a light branching structure, like fused bones").
5. Check that the s23 snapshot (Mars Climate Orbiter — the lead block, Gimli/Hyatt in one line) is readable from the far row: $327M, ×4.45, "seam between systems". This is the climax slide — the text must be visible without strain.
6. Cross-check the spoken numbers against the final deck (drift control, they must match in meaning/range; the slide-visible value may be deliberately softened — e.g. GM strength "+~20%" in the speech/chapter → "noticeably stronger" on slide s02/s12, Phase-7 conservatism — this is the norm, not drift: speech/chapter = source of truth): GM −~40% mass / +~20% strength / 150+ variants; Airbus −~45% (~35 vs ~65 kg); Su-57 ~¼ lighter; Mars $327M / ×4.45 / 1999; ORCA ~45–63%; Michell 1904 / Bendsøe–Kikuchi 1988 / SIMP 1989 / Cauchy 1847 / KKT 1939–1951 / Altshuller 1946. APM FEM "~70% of volume" — do NOT say as an exact number (vendor claim), only "a substantial fraction of the volume, per the vendor's claim".
7. Check the timer markup: the 6 dividers (s04/s09/s15/s20/s25/s29) are spoken in ~15–20 sec each — don't stretch them; the main budget is on s02, s05–s06, s11, s23, s26.
8. The Bauman binding on s31 (the RK9 department, the Research and Education Center for supercomputer modeling, the advanced engineering school "digital materials science") — verify the currency of the unit names on the day of the lecture; if they have been renamed — update the spoken text on s31.

**Orphan-reference control:** the speech covers exactly s01…s32 (32 slides; 6 dividers s04/s09/s15/s20/s25/s29; Q&A s32). There are no references to non-existent slides. On any change to deck.yaml (add/delete/rename of a slide) — regenerate this pre-flight and reconcile slides_covered in the frontmatter.
