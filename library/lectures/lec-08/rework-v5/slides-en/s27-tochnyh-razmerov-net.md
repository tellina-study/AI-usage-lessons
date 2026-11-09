---
id: s27
section: "1. Still Image"
title: "There Are No Exact Dimensions: a Generator Doesn't Replace CAD. And \"RAG for Pictures\" Is a Category Error"
type: comparison
assertion: "An image of a part where \"it looks like an M12 thread\" doesn't contain an M12 thread — it contains raster points that are statistically similar to photographs of threads. For diffusion there's nowhere to feed in a source of truth; for token-based autoregression there is a context, but the conclusion is the same: no token gets checked against a fact on the output"
source: "OpenAI, Addendum to GPT-4o System Card, 25.03.2025 · Gemini 2.5 Flash Image, 2025"
chapter_ref: "chapter-part1c.md — the architecture of conditioning and the consequence of the architecture the technical block took apart; chapter-part1d.md §1.15 — RAG for pictures; the link to the bionic partition case"
columns:
  title: "What you can't do — and where a generator is still useful"
  left:
    head: "What you can't do"
    items:
      - "Measure it — there's no scale in the image"
      - "Verify it — looks like it passed a calculation, and it didn't"
      - "Manufacture or maintain it: there's no geometry, no build tree"
  right:
    head: "Where a generator is useful"
    items:
      - "Look search — storyboarding, shape variants"
      - "Visualizing what's already calculated — rendering, lighting"
      - "The boundary: when a picture becomes a data source"
blocks:
  - {label: "The formulation worth carrying away", value: "a generator answers \"what does it look like.\" CAD answers \"what is it\"", note: "substituting the first for the second is a forgery, not a saving"}
  - {label: "The same check — for a text task", value: "feeding a source into context works for a language model and for not one single image-generation architecture", note: "for denoising there's no context at all; for autoregression there is context, but no token gets checked against a fact", key: true}
media: ""
timing_min: 2.0
in_bucket: true
status: собран
---

## Visible slide text

**"It looks like an M12 thread" on a picture is not an M12 thread: it's raster points that resemble a photo of a thread.**

**The technique "a source in context, a citation on the output" doesn't work for pictures — the reasons differ by architecture.**

## Speaker notes

This section's limitation is formulated for an engineering audience so that it can be checked
before a project launches, not after. A generator produces a picture of an object. There's no
model of the object inside the picture: no units of measurement, no tolerances, no materials, no
kinematics, no constraints as checkable conditions, no build tree. An image of a part where it
looks like there's an M12 thread doesn't contain an M12 thread — it contains raster points
statistically similar to photographs of threads: you can cut a thread from the first, and you
can't from the second, because there's nothing to cut.

From this come four practical prohibitions, each checkable in a second. You can't measure it:
there's nothing to take a dimension off the generation with, there's no scale in the image — even
a ruler drawn in the frame will come out statistically plausible, with markings in arbitrary
places. You can't verify it — and here's the dangerous part: a generated construction never went
through a strength calculation or an assembly check, and it looks exactly as if it had. The error
has no outward sign that a quick glance or a sign-off would catch; an inconvenient limitation
forces you to do extra work, a dangerous one lets you skip needed work and not notice it. You
can't manufacture it: there's no geometry on the output a machine tool would accept. You can't
maintain it: there's no build tree, which means "change the diameter and recalculate" is
impossible — any change requires a new generation, and a new generation gives you a different
part, not a modified version of the same one.

An honest second half is mandatory, or the slide turns into a prohibition instead of a
criterion. At the look-search stage, a generator works exactly as advertised, and by the same
economics. In visualizing something already calculated, the geometry came from the calculation,
and the model does exactly what it should — handle the appearance. In presentation materials,
the same. The boundary runs exactly where a picture stops being an illustration and starts being
a data source for the next step of production. The formulation worth carrying away: a generator
answers the question "what does it look like," CAD answers the question "what is it"; swapping
the second for the first is a forgery, not a saving. The link to the bionic partition case is
direct: there, the win was attributed to the model after the fact; here, people try to put the
model where a solver is needed, ahead of time — both are errors of the same class, and both are
caught by one question: what's the criterion in this task, and can it be checked by computation.

The same class of limitation is visible from the other side too, and an engineer coming from
work with language models arrives at it as one of the first questions: we have a technique that
fixes confident lying — put the source in context and demand a citation; where's the equivalent
technique for pictures? There isn't one, and the reason is architectural, not a product gap.
Step by step: in a language model, the source lands in the context — a sequence of tokens the
model reads before answering, and attention can reference it. In diffusion and flow there's no
context in this sense at all: the description is a constant condition, unchanged across all
fifty steps, and it goes in as a set of vectors that bias attention; there's nowhere to put a
document, the only input besides the starting noise is the conditioning channels, and they carry
geometry and style, not statements. For autoregression over image tokens (since 2025), there is
literally a context, and it grows by the same mechanism as a language model's, and you can put a
reference image or text into it — but that doesn't fix the task: not one image token, whether
discrete or continuous, gets verified against an external fact on the output, for any 2026
architecture.

What conditioning actually does: a depth map says "this object is closer," a pose says "the arm
is raised," a face reference says "like this." Not one channel is able to carry a statement of
the form "this engine model has six mounting bolts" — none of them have a form for a statement,
or a mechanism for verifying it's met. Conditioning suggests a shape, not a truth. And there's no
citation mechanism: document retrieval works paired with demanding a citation, while for a
generated frame provenance physically doesn't exist — every training example's contribution is
smeared across billions of weights; the vendor isn't hiding it, it doesn't exist.

Three practical consequences. First: a legal check of the output from inside the model is
impossible — whether it resembles someone else's protected work is decided only by comparing from
the outside, by reverse image search. Second: you can't "delete one fact" from the model — the
same limitation that applies to a language model's weights, hence the entire industry of
output-side filters instead of internal edits. Third: this is also where provenance signatures
and built-in watermarks come from — an engineering admission that the task isn't solved inside
the model, not a convenient extra feature.

The contrast with a language model is sharp: there, schema grammar masks invalid tokens at
decoding time, and an invalid format physically can't be generated. Here there's no equivalent,
and there won't be one as long as the output is continuous: there's nothing to mask, nothing to
forbid, you can't strike a continuous quantity out of a vocabulary that doesn't exist. The
engineering conclusion that ties both of the slide's limitations together: meeting a technical
specification in a generative media pipeline is guaranteed by a loop around the model — an
output-side check, a detector, a human validator, regeneration on failure. This is the same
"human validator" construction the course has already made a mandatory element of an agentic
system, and here it stops being a recommendation: it's the only way to meet the specification. A
project where the loop isn't engineered has no mechanism for meeting the client's requirements,
no matter how much time was spent tuning the prompt.
