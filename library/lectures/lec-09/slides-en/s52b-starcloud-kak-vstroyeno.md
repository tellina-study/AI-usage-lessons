---
id: s52b
local_id: s4-03-3
section: "4. Space for AI"
type: schema_pipeline
title: "How a request's path through Starcloud is built"
assertion: "The only difference from a ground-based data center is the satellite link in and out; the inference itself inside the chip is identical to Earth's"
source: "—"
media: ""
media_needed: "Phase 10 (issue #317): a pipeline diagram of the request's path — assembled from the chapter text (chapter-part3.md, §4.3, the 'Position in the data flow' item), not from slide s52 (that breakdown isn't there)."
scheme:
  caption: "The request's path up and the answer's path down — the computation inside the chip doesn't differ from Earth's"
  arrows: true
  rows:
    - {label: "Path up", steps: ["User's\nrequest", "Ground\nstation", "Satellite\nlink", {text: "H100 onboard:\nGemma inference", ai: true}]}
    - {label: "Path down", steps: ["Computation\nresult", "Same\nsatellite link", "Ground\nstation", "Answer to\nthe user"]}
in_bucket: false
status: draft
---

## Visible slide text

**What's new is only at the input and output.** The satellite link up and down — that's the entire difference from an ordinary ground-based data center.

**Inside the chip — nothing new.** Inference on the Gemma model aboard the H100 runs exactly as it would on Earth: the difference is in the location and the power source, not in the computation.

## Speaker notes

The adjacent Starcloud breakdowns have already named the fact and its cost: the first data-center-class GPU in space, the first AI model answer from such a chip in orbit. This diagram lays out the path of a single request step by step — from the user to the answer and back — to show exactly where something genuinely new appears in this chain, and where everything is built exactly the way it is on Earth.

The path up: the user's request is carried by a ground station over a satellite link to the satellite, where the H100 processor is physically installed. It's on this very spacecraft that inference on the open Gemma model runs — the same computing operation any ground-based data center performs, just physically moved out to orbit.

The path down: the computation result is sent back over the same satellite link, through the same ground station, and reaches the user as an ordinary answer. The only difference between this chain and an equivalent request at a ground-based data center is the presence of a satellite link at the input and output; the computing process itself, inside the chip, is identical to Earth's.

An honest gap, also named in the adjacent breakdowns: the sources confirm the fact that requests to Gemma are being served, but they don't publish latency or bandwidth statistics for this link compared to a ground-based equivalent — without those numbers, there's no way to judge when orbital compute becomes not just working, but competitive on response speed, rather than only on access to solar power.
