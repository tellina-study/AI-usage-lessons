---
title: "Design/Prototyping section — classical base + AI 2025-26 opportunities, best practices, limits, named tools"
lecture: lec-05
purpose: "Source for rebuilt DESIGN/PROTOTYPING section: teach classical design fundamentals FIRST (strong engineers, not design-trained), then AI opportunities + limits + best practices + named tools. Complements (does not duplicate) 40-classics-pdlc.md (frameworks/PDLC backbone) and 50-failures-and-limits.md (cross-phase failure catalog, incl. Character.AI #4 and iTutorGroup #3 already covered there)."
access_date: 2026-09-06
audience: "advanced 3rd-year IT students, all vibe-code, none design-trained — teach the vocabulary and judgment a strong engineer lacks"
status: research-complete
---

# Design/Prototyping — classical base, then AI opportunities, limits, and named tools

This section is the missing prerequisite layer under the row-3 entry in `40-classics-pdlc.md` (Design Thinking + Double Diamond, already covered there at the framework/critique level for the PDLC spine). Here the goal is narrower and more basic: give an engineer who has never taken a design course the vocabulary and mental models a designer already has, **before** showing what AI changes. Do not re-teach the Natasha Jen/Nussbaum insider critique of Design Thinking — that's already the payload in `40-classics-pdlc.md` row 3; here it is referenced, not repeated.

---

## 1. Classical design base — what an engineer must know from scratch

### 1.1 Design Thinking (Empathize → Define → Ideate → Prototype → Test)

Five-stage human-centered methodology, canonically taught by Stanford d.school and popularized by IDEO/David Kelley and Tim Brown (HBR 2008 "Design Thinking"):

1. **Empathize** — observe and engage users in their real environment to understand needs, not assumptions; the stage unique to design thinking vs. generic problem-solving.
2. **Define** — synthesize empathy findings into a clear, actionable problem statement (a "point of view"), converting research into a framed question.
3. **Ideate** — generate a high volume of candidate solutions via brainstorming, deliberately deferring judgment (quantity before quality).
4. **Prototype** — build the cheapest possible tangible representation of a subset of ideas, to think with hands and make ideas testable.
5. **Test** — put prototypes in front of real users, gather reaction, and cycle back to any earlier stage — the process is iterative and non-linear, not a strict waterfall of five boxes.

The stages are non-linear in practice: teams jump back from Test to Define constantly. This iterative property is the one design-thinking idea worth insisting on for engineers, who tend to read "5 stages" as a linear checklist. **(For the insider critique — Natasha Jen "Design Thinking is Bullshit," Bruce Nussbaum "a failed experiment" — see `40-classics-pdlc.md` row 3; not repeated here.)**

### 1.2 Double Diamond (Discover → Define → Develop → Deliver)

UK Design Council framework (2003–05), a visual model of two diverge/converge cycles:

- **Diamond 1 — the right problem:** *Discover* (diverge: broad research, explore the problem space) → *Define* (converge: synthesize into a specific brief).
- **Diamond 2 — the right solution:** *Develop* (diverge: generate/prototype many solution directions) → *Deliver* (converge: test, refine, and ship one).

Mapping to Design Thinking for teaching: Discover ≈ Empathize, Define ≈ Define, Develop ≈ Ideate+Prototype, Deliver ≈ Test. The teachable point for engineers: **two separate diverge/converge cycles**, not one — most engineers instinctively converge on a solution before the problem itself has been validated (they skip diamond 1 and jump straight into diamond 2). This exact failure mode — skipping problem-validation and converging early on a solution — is the load-bearing engineering anti-pattern to call out.

### 1.3 Prototyping / wireframing / fidelity spectrum

- **Wireframe** — low-fidelity, grayscale skeleton showing layout/structure/information hierarchy, no visual styling or real content; fast and cheap, meant to be thrown away.
- **Mockup** — mid-to-high fidelity static visual design (color, typography, real-ish content) but not interactive.
- **Prototype** — a simulated interactive experience (clickable Figma prototype, or now an AI-generated working front end) used to test flows and interactions before writing production code.
- **Fidelity spectrum:** low-fi (paper sketches, boxes-and-arrows) → mid-fi (wireframes) → high-fi (pixel-accurate, interactive). Rule of thumb: use the *lowest* fidelity that still answers the current question — high-fidelity too early anchors reviewers on visual polish instead of the underlying flow/logic (a bias worth flagging explicitly, since AI tools now make high-fidelity the *cheap default*, inverting this rule of thumb — see §2).

### 1.4 Nielsen's 10 usability heuristics (1994, refined 2020)

Jakob Nielsen's heuristics are rules of thumb for **expert review** (heuristic evaluation) — not a substitute for testing with real users, but a fast, cheap way to catch problems before spending money on a study. The ten (canonical list):

1. Visibility of system status
2. Match between system and the real world (plain user language, not developer jargon)
3. User control and freedom (undo/redo, a clear "emergency exit")
4. Consistency and standards
5. Error prevention
6. Recognition rather than recall
7. Flexibility and efficiency of use
8. Aesthetic and minimalist design
9. Help users recognize, diagnose, and recover from errors
10. Help and documentation

Teachable framing for engineers: these map almost 1:1 onto things engineers already do for good API design (clear error messages, idempotent undo, consistent naming) — so the heuristics are a transfer of an already-familiar discipline (defensive programming / good error handling) onto UI decisions, not an alien new skillset.

### 1.5 Design systems

A **design system** is the living, governed set of principles + design tokens + coded components + patterns + documentation that keeps a product visually and behaviorally consistent at scale. Distinguish clearly from a **component library** (a set of reusable coded/Figma building blocks — the artifact) — the design system is the larger governance layer that a component library sits inside (single source of truth aligning design/dev/product). The teachable point that becomes load-bearing for AI in §2: **a design system is a guardrail** — a way of constraining generative freedom to what's already validated, tested, and on-brand, so it is the natural harness for AI-generated UI.

### 1.6 Interaction design / UX vs. UI

- **UI (User Interface)** — the surface: visual design, layout, typography, color, iconography, individual screens.
- **UX (User Experience)** — the whole: how it feels to use the product across the full journey — flows, information architecture, friction, emotional response, whether it actually solves the user's problem. UI is a subset/output of UX; a beautiful UI on top of a broken flow is still bad UX.
- **Interaction design** is the layer between the two: how the user's actions and the system's responses are choreographed (what happens on click/hover/scroll/error) — one of the reasons "generate a nice-looking screen" (what most AI tools do well) is not the same job as "design the interaction" (what still needs a human decision).

### 1.7 The value of usability testing

- Nielsen's own hard-earned lesson, repeated as a mantra in the field: **"you are not the user"** — anyone close to a build project is, by definition, atypical, and will systematically mis-predict what confuses a real user.
- Testing with a single user reveals **~31%** of the usability problems that exist in an interface on average — meaning tiny, cheap tests already surface a third of the problems; Nielsen's classic guidance (5 users finds ~85% of problems in a *qualitative* study) is why usability testing does not need to be expensive or large-N to pay off — it needs to happen at all, iteratively, early.
- ROI framing: usability investment in something like a corporate intranet can pay back **10x or more** at scale — the standard argument against "we don't have budget to test."
- This is the essential counter-balance for §3: no matter how fast AI makes prototype generation, this step — putting the artifact in front of a real human and watching them struggle — has no AI substitute, because the thing being measured is a human's actual confusion, not a model's guess at what would confuse them.

---

## 2. AI in design 2025-26 — opportunities, best practices, named tools

### 2.1 Named tools and what each is actually good for (as of Sept 2026)

| Tool | What it does | Status/notes (2025-26) |
|---|---|---|
| **v0 by Vercel** (v0.dev) | Text-to-React-UI: generates production-ready React/Next.js components (Tailwind + shadcn/ui) from a prompt; deploys instantly to Vercel for sharing/testing | Started 2023 as a text-to-component experiment; Feb 2026 update added Git integration, VS Code-style editor, DB connectivity, agentic workflows — matured from "prototyping toy" into a production platform. Still relies on external tools for backend/auth/DB logic. |
| **Figma Make** (+ Figma "First Draft") | Generates full screens/prototypes from a text prompt *inside* Figma, pulling in the team's own design-system components (buttons, cards, layouts already in use) rather than generic ones | 2025-26: 72% of designers report using generative AI in their workflow; 91% say it improves output *quality*, not just speed. Deep integration with an org's own design system is the differentiator vs. generic generators. |
| **Google Stitch** (formerly **Galileo AI**) | Text/sketch-to-hi-fi UI mockup generator (mobile + web), editable output | Galileo AI acqui-hired by Google (May 2025), relaunched as Stitch (Gemini-powered); late-2025 updates improved layout refinement and responsiveness. |
| **Uizard** | Turns screenshots/sketches into wireframes; cheaper/lighter tier than Stitch/Figma Make | Free tier: 2 projects/3 generations per month; paid from ~$12/mo for 500 generations. |
| **bolt.new** | Prompt-to-full-stack-app in-browser, zero local setup — greenfield JS apps, not just UI | Launched Oct 2024, reached $20M+ ARR in ~2 months; canonical "vibe coding" tool (term popularized by Andrej Karpathy, early 2025). 2026 workflow pattern: prototype in Bolt → clone locally → refine/scale in Cursor. |
| **Cursor** | AI-native code editor; for design purposes used to refine/scale what a generator (v0/Bolt) produced into production-grade code | Targets professional engineers for long-term maintainability, not initial rapid prototyping. |
| **Midjourney / DALL·E** | Concept art, mood boards, hero imagery, visual-direction exploration — not UI generation | Best practice: use for early divergent visual-direction exploration (mood, tone, style references), not for pixel-accurate interface work. |
| **AI copy/microcopy tools** (Jasper, ChatGPT/Claude, Notion AI, Figma text plugins, Grammarly Business) | Draft button labels, error messages, empty-states, onboarding copy; brainstorm/stress-test message alternatives; keep voice consistent via style-guide features | Genuinely strong at *volume of alternatives* for A/B-style copy testing; weak at knowing the *right* tone for a specific brand without a style guide feeding it. |
| **AI alt-text/accessibility tools** (AutoAlt.ai, AltText.ai, Alt Magic) | Auto-generate image alt text at scale | Caveat: overlay-based accessibility tools (accessiBe, UserWay) inject alt text into the DOM only, not the HTML source — invisible to search engines and some assistive tech pipelines; EU accessibility law (June 28, 2025) makes this a compliance-relevant gap, not just an SEO nuance. |

### 2.2 Concrete workflow example (2025-26 state of practice)

A realistic team workflow, synthesizing the above: (1) PM/designer describes the screen or flow in a prompt to **Figma Make** or **v0**, constrained to the team's existing design-system components; (2) the generator produces 2-4 divergent directions in minutes, something that used to take a day of wireframing; (3) a human designer **converges** — picks the direction, discards the rest, and hand-edits details the model got wrong (spacing, hierarchy, edge cases); (4) the chosen direction goes through a real **usability test** (§1.7) with actual users, not an AI-simulated persona; (5) engineers pull the validated design into **Cursor**/production code, where a human still owns state management, error handling, and interaction logic AI tends to gloss over.

### 2.3 Best practice: "AI for divergence, human for convergence"

This is the single cleanest framing for the whole AI-in-design section, and it is stated directly in current practitioner literature: co-creative AI tools are best used to maximize the **volume and diversity** of early-stage exploration (associative thinking, metaphors, cross-domain analogies, many stylistic variations) — precisely the Ideate/Develop diverge step in §1.1–1.2. **Convergence — defining which problem is worth solving, and refining one direction until it actually fits the context, constraints, and real users it serves — is explicitly identified as the human strength that "no prompt can replace."** Teams that deliberately alternate divergence and convergence, rather than letting the AI's first plausible output become the anchor, get faster and more comfortable at both over time. A design-system (§1.5) is the natural guardrail that keeps AI-driven divergence from drifting off-brand or off-pattern — generation stays inside validated components while still producing many options.

### 2.4 What's genuinely good here

- **Speed of first draft:** what took a day of wireframing now takes minutes — the biggest, least controversial win, freely admitted even by critics of "AI slop" (below).
- **Design-system-aware generation** (Figma Make): because it pulls the team's *own* components rather than generic ones, output requires materially less rework than naive text-to-UI.
- **Democratization of a "decent-looking" first pass:** non-designers (PMs, engineers) can now produce something presentable to kick off a conversation, instead of a rough box-and-arrow sketch — useful specifically for the "strong engineer, not design-trained" persona this lecture targets.
- **Copy/microcopy volume:** genuinely strong for generating many candidate microcopy variants fast, if a style guide/voice is fed in as a constraint.

---

## 3. AI limits in design — and what to keep from the classics

### 3.1 "AI slop" and homogenization — the clearest 2025-26 critique

Nielsen Norman Group's own **State of UX 2026** report (Kate Moran, VP Research & Content, with Raluca Budiu and Sarah Gibbons) makes the homogenization argument explicit: *"UI is still important, but it'll gradually become less of a differentiator"* — because as AI design tools improve, **"anyone will be able to make a decent-looking UI (at least from a distance)."** Moran separately diagnoses the underlying organizational failure mode: *"In the design space, there's a lot of pressure to show the shareholders, 'Look, we put AI in our product'"* — what she calls **technology-led design**: starting from the tool and searching backward for a problem it could solve, the inverse of Design Thinking's Empathize-first sequence in §1.1. NN/g's own forward-looking framing for 2026: *"Lazy AI features and AI slop are now ubiquitous, and the shine is fading fast. When everything gets an AI sparkle, it becomes noise, not novelty."*

The mechanism behind homogenization: generators are trained on the same large corpora of existing UI patterns, so many independent teams prompting for "a modern dashboard" converge on visually similar output — the opposite of differentiation, and a direct inversion of §1.1's Ideate principle (diverge before converge) if teams stop at the first AI draft.

### 3.2 Accessibility gaps — now with a hard number

A 2025-26 academic study (*"Generated Inaccessible: Measuring WCAG Violations in AI UI Design Tools,"* ACM Web4All 2026 conference proceedings) ran **21,880 accessibility assessments** across five WCAG success criteria on interfaces produced by AI UI-generation tools and found only **29.0% overall compliance**. The worst-performing, most basic criteria were exactly the ones a classic design-system checklist would catch trivially: **color contrast (26.8% compliant)** and **use of color (19.2% compliant)**. A related finding worth stressing for the "platform vs. prompt" point: **platform design mattered more to accessibility outcomes than user prompts did** — i.e., asking the AI to "make it accessible" in the prompt did not reliably fix it; the underlying generator's defaults did. This directly rebuts the naive "just prompt it correctly" defense of AI-generated design.

### 3.3 Hallucinated UX patterns

Nielsen Norman Group's own explainer on AI hallucinations for designers frames LLMs as **"fill-in-the-blank machines"** that produce statistically plausible but factually/functionally wrong output with unwarranted confidence — the design-specific version of the same failure mode already catalogued for research/legal citations in `50-failures-and-limits.md` case #2 (MAHA/Deloitte/court-citation hallucinations). In design specifically this manifests as: an AI-recommended "best practice" UI pattern that looks authoritative but doesn't correspond to any real, validated pattern, or contradicts the product's own established interaction conventions. Compounding risk flagged in current practitioner writing: **using AI-generated personas instead of real usability testing creates a closed "hallucination loop" — the AI designs for an AI's guess at a user, and no real human ever checks it.** This is precisely the failure §1.7's usability-testing argument exists to prevent, and it is the single strongest reason real testing cannot be skipped just because prototyping got cheap.

### 3.4 Loss of craft/taste and the convergence gap

The "AI for divergence" best practice in §2.3 has a mirror-image failure: teams that skip the human-convergence step and ship the AI's first plausible draft lose the refinement/taste layer entirely — what NN/g frames as **"reviewing hallucinated UX patterns is more mentally exhausting than designing from scratch,"** because a human still has to catch every subtle wrongness in something that *looks* finished, which is cognitively harder than building from an acknowledged blank slate. The classic value of Nielsen's heuristics (§1.4) as a *fast expert-review* layer becomes more, not less, relevant here — it's the cheapest available check against exactly this failure mode, faster than a full usability study when a first-pass AI draft needs a sanity check before it reaches real users.

### 3.5 Safety-by-design must stay explicit (cross-reference, not duplicated)

`50-failures-and-limits.md` case #4 (Character.AI, engagement-optimized companion design with safety features retrofitted only after a documented suicide) and case #3 (iTutorGroup, hard-coded age-discrimination in a hiring-screen design decision) are both **design-phase** failures already fully written up there — use them as the on-point design failures for this lecture rather than duplicating new cases; §4 below adds framing, not new incidents.

### 3.6 What to keep from the classics — synthesis

| AI limit | Classic countermeasure that still works | Why AI can't substitute for it |
|---|---|---|
| AI slop / homogenization | Design Thinking's Empathize-first sequence + real divergent Ideate (many *genuinely* different directions, not variations on one AI draft) | Homogenization is a training-data artifact; only grounding in a *specific* team's real users produces genuine differentiation |
| Accessibility gaps (29% WCAG compliance) | Nielsen's heuristics as fast expert-review gate + a design system with accessibility baked into components/tokens | Platform defaults, not prompts, drive the failure — a governance layer (design system) that enforces contrast/labeling regardless of prompt is the only reliable fix |
| Hallucinated UX "best practices" | Real usability testing (§1.7) — the ~31%-of-problems-per-single-test rule | Testing measures actual human confusion; an LLM has no access to that signal, only to statistical plausibility |
| Loss of craft / taste, cognitively-exhausting review | Design critique culture + the double-diamond convergence step done by a human | Taste is a judgment call about *this* product's specific users and brand — not a pattern-matchable property across training data |
| Safety-by-design omitted | Explicit safety/harm review as a *named phase gate* before ship (not a retrofit) | See Character.AI / iTutorGroup in `50-failures-and-limits.md` — no AI tool currently treats "who could be harmed by this flow" as a first-class design question by default |

---

## 4. On-point design-phase failures

Both canonical design-phase failures for this lecture are **already fully written up** in `50-failures-and-limits.md` — do not duplicate, cross-reference:

1. **Character.AI / Sewell Setzer III suicide** (`50-failures-and-limits.md` case #4) — engagement-maximizing companion-app design shipped without safety-by-design (no self-harm detection/escalation, no age verification at launch); guardrails (2-hour daily limit for minors, ban on open-ended chat for under-18s, selfie age-verification) added only **after** wrongful-death litigation, not at MVP. **Lesson:** for products designed around emotional attachment of vulnerable users, safety guardrails must be part of the MVP design brief, not a post-tragedy patch. **Criterion:** engagement-optimized design targeting minors' emotional attachment without a built-in crisis-detection-and-human-escalation path is a structural design flaw, not a polish item.

2. **iTutorGroup hiring-bot age discrimination** (`50-failures-and-limits.md` case #3) — resume-screening system hard-coded to auto-reject women 55+ and men 60+; EEOC's first-ever AI-discrimination settlement, Aug 2023, $365,000. **Lesson:** design decisions that touch legally protected categories (age, sex, race) must have anti-discrimination law reviewed as part of the design brief from day one, not discovered via a candidate's lucky resubmission with a younger birthdate.

For lecture use: these two together give the section its ≥30% strict-in failure content without needing new cases — one is a consumer-facing UX/safety-by-design failure, the other is a decision-logic/algorithmic-discrimination failure, covering both halves of "design failures" cleanly.

---

## 5. What the lecture is likely MISSING about the design phase in the AI era

These are genuine emerging topics in 2025-26 UX practice that a classical-design-base + AI-tools framing (§1–§3) does not naturally surface, and that current sources flag as the *next* frontier of design skill specifically because AI products break the deterministic-system assumption every classic tool above was built for:

1. **Designing for non-deterministic/probabilistic output.** Traditional UX and every heuristic in §1.4 assumes a deterministic system: same input → same output, so "consistency" (heuristic #4) is achievable by definition. LLM-based products break this — **the same input can produce different outputs on different runs** — and current practitioner writing (Thoughtworks, UX Tigers) explicitly frames this as requiring new patterns: **graceful failure** (making uncertainty/error/escalation recoverable by design, not an afterthought), **co-creation** (treating AI output as a draft the user edits, never a final verdict), and **responsible autonomy** (scoping how much the AI is allowed to do unsupervised, based on the stakes and reversibility of the action). This is a genuinely new design skill with no classical-era analogue — worth a dedicated slide, not a footnote.

2. **Trust/transparency UX — communicating uncertainty and confidence honestly.** NN/g's designer-facing recommendation (§3.3) is concrete and lecture-ready: use first-person contextual uncertainty language ("I'm not completely sure, but...") rather than generic legal disclaimers (which become invisible clutter), show confidence indicators (High/Medium/Low), and provide source attribution links so users can verify. This is a direct, teachable design pattern the lecture can name explicitly — currently the deck likely treats "AI limitations" as a caveat rather than a first-class UX design problem with known emerging patterns.

3. **Human-in-the-loop UX patterns as an explicit design category.** 2025 practitioner consensus treats "confirmation checkpoints" (explicit user review/approval before an AI action with real cost takes effect — financial, system-state, access-control changes) and auditability (logging why a human overrode or accepted an AI suggestion) as a named, reusable pattern family — not a one-off safety bolt-on. This connects directly to the Character.AI failure in §4: a confirmation-checkpoint/escalation-to-human pattern, designed in from the start, is exactly what was missing.

4. **"AI disclosure" as a UX obligation, not just a legal footnote.** Being transparent about *where* AI is used in a product (the lecture could cite GitLab Duo's approach of labeling AI-touched surfaces explicitly) is emerging as a distinct design requirement, separate from confidence-indicator UX (#2 above) — telling the user "this response was AI-generated" is a different design decision from telling them "the AI is 70% confident in this response."

5. **Error states designed specifically for AI failure modes.** Classical error-state design (heuristic #9, §1.4) assumes the system knows it failed (a 404, a validation error). AI failure is different and harder: the system often doesn't know it's wrong (a hallucination is delivered with full confidence) — so "error state" design for AI has to be about *inviting user skepticism proactively* (§3.3's confidence indicators) rather than reactively catching a detected failure. This reframes heuristic #9 rather than replacing it, which is a clean way to teach it as an extension of the classic, not a wholly new topic.

**Recommendation for the lecture plan:** items 1 and 3 are the highest-value additions — they are the most concrete, most teachable in slide form, and most directly extend (rather than contradict) the classical heuristics already being taught in §1.4, which keeps the "classics first, then AI adds/stresses them" narrative structure intact.

---

## Sources

All accessed **2026-09-06**.

**Classical design base**
- [LogRocket — What is the Double Diamond design process?](https://blog.logrocket.com/ux-design/double-diamond-design-process/) — 4-phase structure, diverge/converge cycles.
- [UXPIN — Double Diamond Design Process Explained (2026)](https://www.uxpin.com/studio/blog/double-diamond-design-process/) — phase-by-phase detail, 2026-updated.
- [IxDF — What is Design Thinking? (updated 2026)](https://ixdf.org/literature/topics/design-thinking) — 5-stage canonical structure.
- Stanford d.school Design Thinking Bootleg (referenced via `40-classics-pdlc.md`, not re-fetched — see that file's Sources for direct link).
- [UXtweak — How to Conduct Heuristic Evaluation w/ Nielsen's 10 Usability Heuristics](https://blog.uxtweak.com/usability-heuristics/) — full 10-heuristic list with examples.
- [UX Tigers (Jakob Nielsen) — How I Developed the 10 Usability Heuristics](https://www.uxtigers.com/post/usability-heuristics-history) — origin 1994, 2020 refinement, "fundamental principles haven't changed."
- [Ramotion — Design System vs Component Library](https://www.ramotion.com/blog/design-system-vs-component-library/) — governance vs. building-blocks distinction.
- [UXPA International — The ROI of Usability](https://uxpa.org/the-roi-of-usability/) — 10x ROI framing.
- [Medium/Hippo Digital — "You are not the user"](https://medium.com/hippo-digital/you-are-not-the-user-but-what-about-when-you-are-35abe4006b8) — Nielsen mantra, atypicality of insiders.
- NN/g — 5-users-finds-most-problems / single-user ~31%-of-problems finding (well-established NN/g result, cross-referenced via UXPA ROI page above; canonical NN/g article: "Why You Only Need to Test with 5 Users").

**AI opportunities, tools, best practices**
- [TemperStack — How to prototype with v0 AI assistant on Vercel (April 2026)](https://www.temperstack.com/learn/vercel/prototype-with-v0/) — v0 feature set, Feb 2026 update (Git integration, VS Code-style editor, DB connectivity).
- [Marc Andrews — V0 By Vercel Review 2026](https://marcandrews.com/v0-by-vercel-review-2026-ai-powered-react-ui-generator/) — React/Tailwind/shadcn stack, limitations (backend/auth/DB still external).
- [Figma — 11 of the Best AI Design Tools for 2026](https://www.figma.com/resource-library/ai-design-tools/); [Figma — AI in Design: Transforming the Way We Create](https://www.figma.com/resource-library/ai-in-design/) — 72% designer AI adoption, 91% quality-improvement figure, Figma Make design-system integration.
- [CODERCOPS — Figma AI in 2026: First Draft, AI Grid, and What Changed for Design Handoff](https://www.codercops.com/blog/figma-ai-design-tools-2026) — First Draft workflow (prompt → draft → human fine-tune).
- [Banani — Galileo AI for UI Design (now Google Stitch): 2026 Updated Review](https://www.banani.co/blog/galileo-ai-features-and-alternatives) — May 2025 Google acqui-hire, Stitch relaunch, late-2025 updates.
- [Nextool.ai — Galileo AI vs Uizard (2026)](https://nextool.ai/compare/galileo-ai-vs-uizard-ai/) — Uizard pricing/tier detail.
- [BuildBetter — 8 Best Bolt.new Alternatives in 2026](https://blog.buildbetter.ai/best-bolt-alternatives-in-2026/) — Bolt.new Oct 2024 launch, $20M+ ARR in ~2 months.
- [Department of Product — How to use Cursor for non-engineering](https://departmentofproduct.substack.com/p/how-to-use-cursor-for-non-engineering) — vibe-coding term origin (Karpathy, early 2025), Bolt→Cursor workflow pattern.
- [arXiv 2512.18388 — Exploration vs. Fixation: Scaffolding Divergent and Convergent Thinking for Human-AI Co-Creation](https://arxiv.org/html/2512.18388v1) — "AI for divergence, human for convergence" mechanism, big-picture-overview anti-fixation feature.
- [Medium/Sandra Murillo Paz — The Converger Mindset](https://medium.com/@sandra_76930/the-converger-mindset-31e4fe4d0b31) — convergence as human strength, "no prompt can replace" framing.
- [4951 Studios — AI for UX Writing: Microcopy, Error Messages, and Voice Consistency (Nov 2025)](https://www.4951studios.com/blog/2025/11/ai-for-ux-writing-microcopy-error-messages-and-voice-consistency/) — named copy-tool list (Jasper, ChatGPT/Claude, Notion AI, Grammarly Business).
- [AutoAlt.ai — Best Alt Text Software 2026: 9 Tools Compared](https://www.autoalt.ai/blog/best-alt-text-software/) — overlay-tool DOM-vs-HTML-source caveat; EU accessibility law June 28, 2025.

**AI limits, homogenization, accessibility gaps, hallucinated patterns**
- [NN/g — State of UX 2026: Design Deeper to Differentiate](https://www.nngroup.com/articles/state-of-ux-2026/) — Kate Moran/Raluca Budiu/Sarah Gibbons; "UI... gradually become less of a differentiator," "technology-led design," 2026 AI-slop-backlash framing.
- [Yahoo News — 2025 was the year AI slop went mainstream](https://uk.news.yahoo.com/2025-ai-slop-went-mainstream-070206147.html) — Kate Moran shareholder-pressure quote, "technology-led design" direct quote.
- [ACM Digital Library — Generated Inaccessible: Measuring WCAG Violations in AI UI Design Tools (Web4All 2026 proceedings)](https://dl.acm.org/doi/10.1145/3800424.3800430) — 21,880 assessments, 29.0% overall compliance, color contrast 26.8%/use-of-color 19.2% worst criteria, platform-vs-prompt finding. *(Fetch blocked by paywall/403; findings corroborated via search-result abstract excerpt.)*
- [NN/g — AI Hallucinations: What Designers Need to Know](https://www.nngroup.com/articles/ai-hallucinations/) — "fill-in-the-blank machines," Google AI Overview rocks-eating example, designer recommendations (contextual uncertainty language, confidence indicators, source attribution, avoid generic disclaimers).
- Practitioner sources on "hallucination loop" (AI personas replacing real usability testing) and "reviewing hallucinated patterns is more exhausting than designing from scratch" — surfaced via aggregated 2025-26 UX-trend search; treat as practitioner-consensus framing rather than single-attributable-source quote, cross-check before using verbatim in slides.

**Non-deterministic UX / trust / human-in-the-loop (the "missing" section)**
- [Thoughtworks — Product design in the age of AI: Designing non-deterministic systems](https://www.thoughtworks.com/insights/blog/experience-design/Product-design-in-the-age-of-AI-Designing-non-deterministic-systems) — deterministic-assumption breakdown, same-input-different-output framing.
- [UX Tigers (Jakob Nielsen) — Embrace AI's Uncertainty in UX](https://www.uxtigers.com/post/ai-uncertainty-ux) — graceful failure / co-creation / responsible-autonomy pattern triad.
- [UX Collective/Taras Bakusevych — 39 principles for designing human-AI interaction](https://uxdesign.cc/39-principles-for-designing-human-ai-interaction-87be5fabdbbe) — broader principle catalogue, background for pattern selection.
- [aufaitux — Human-in-the-Loop UX: Designing AI People Can Trust](https://www.aufaitux.com/blog/human-in-the-loop-ux/) — confirmation-checkpoint pattern, cost/reversibility-based escalation.
- [Ideafloats — Human-in-the-Loop AI in 2025: Proven Design Patterns](https://blog.ideafloats.com/human-in-the-loop-ai-in-2025/) — auditability/logging-of-overrides pattern.
- [UX Collective/Allie Paschal — AI transparency in UX: Designing clear AI interactions](https://uxdesign.cc/ai-transparency-in-ux-designing-clear-ai-interactions-ba9b6ba4761b) — GitLab Duo AI-surface-labeling example, opt-out-of-personalization guidance.
