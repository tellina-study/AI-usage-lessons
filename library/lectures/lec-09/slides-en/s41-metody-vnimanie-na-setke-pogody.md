---
id: s41
local_id: s3-02a-2
section: "3. Design and new capabilities"
type: schema_layered
title: "How the methods are built: attention on the weather grid"
assertion: "The same attention mechanism as in a language model (Lecture 2) — except here the neighbors are not tokens, but points on the atmosphere's grid"
source: "—"
media: ""
media_needed: "Phase 7 (issue #317): added architecture with a breakdown inside the boxes (`arhitektura:`) — the attention mechanism itself (query/key/value), which was not on the slide at all. The Lecture 2 vs AIFS/AIGEFS comparison stays as plates below."
arhitektura:
  blocks:
    - head: "Query of a point"
      role: "input"
      lines:
        - "'what information do I need from my neighbors'"
        - "computed for every grid point"
    - head: "Keys of the neighbors"
      role: "work"
      lines:
        - "compared against the query — which neighbors are relevant"
        - "neighbor = physical adjacency on the grid, not a position in text"
    - head: "Values of the neighbors"
      role: "output"
      lines:
        - "the physical quantities of neighboring points"
        - "a weighted sum by the match between the query and the keys"
blocks:
  - {label: "Lecture 2: attention over tokens", value: "Q/K/V, neighbor = a position in text", note: "'a flashlight in a dark room' — the beam is pointed at the relevant tokens"}
  - {label: "AIFS/AIGEFS: attention over the atmosphere's grid", value: "Q/K/V, neighbor = physical adjacency of points", note: "a point's query is compared against the keys of physically close points", key: true}
in_bucket: false
status: draft
---

## Visible slide text

**Why the architectures are 16-layer** — not a coincidental number, but a trade-off between how far one point's influence needs to spread in a single pass and how much that costs computationally.

## Speaker notes

Lecture 2 already broke down the attention mechanism in a language model: for every token, three projections are computed — query, key, and value — and the model decides how strongly each token should attend to every other token, weighting the values by the match between the query and the keys. The working metaphor is a flashlight in a dark room: the beam is pointed at the relevant tokens.

This same idea — not similar, but structurally the same — works inside the AIFS and AIGEFS processor. The difference between the two applications is not in the weighting math itself, but in what counts as a "neighbor." For a language model, a neighbor is a position in the sequence of words. For a weather model, a neighbor is the physical adjacency of points on the globe's grid: a grid point computes a query and compares it against the keys of physically close points, not against an arbitrary other point on the planet directly.

Take a grid point over the ocean, near which a low-pressure area is forming. Its query is, roughly speaking, "what information from my neighbors do I need to predict my own pressure six hours from now." The keys of neighboring points are what each one can offer: a point with falling pressure carries a key different from its calm neighbors. The values are the physical quantities of those points themselves, summed with weights according to the degree of match.

This does not mean the influence of distant points is unreachable — the architecture is multi-layered. AIFS is built as a 16-layer transformer with a sliding attention window: at each layer, a point sees only the neighbors within the window, but across several layers the influence spreads further. AIGEFS is a message-passing graph network: at each layer, a node collects messages from directly connected nodes. Message-passing and attention are close relatives in idea, but not literally one mechanism in formula detail: AIFS is literal Q/K/V attention, AIGEFS is a related but formally different aggregation method, tracing back to the GraphCast architecture.
