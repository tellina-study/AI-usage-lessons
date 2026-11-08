---
id: s31
type: assertion_visual
duration_min: 2.4
assertion: "The decision rule is five questions; the full taxonomic matrix of six classes is assembled from all the parts; this spectrum is current engineering practice."
learning_goal: "The decision rule (a 5-point checklist) + the FULL taxonomic matrix (the crystallization of s06) + context on current practice"
learning_outcomes: [LO1, LO2, LO7]
chapter_ref: "§6.2 — The decision rule and the full taxonomic matrix"
references: []
visual:
  pattern: schema_matrix
  primary: "A 5-point checklist on the left in an Ocean rounded box; on the right, a compact full matrix of 6 classes (Nature · What it guarantees · Maturity · Who is responsible)"
  illustration:
    type: schematic
    sources:
      - "Self-generated split layout (checklist + table) via PowerPoint shapes + add_table (Ocean palette)"
      - "Lucide icons https://lucide.dev — `list-checks` (checklist), `table` (matrix), 32px inline, recolored to Primary mid `#065A82`"
    caption: "The decision rule + the full taxonomic matrix (crystallization)"
interaction: none
---

# The decision rule and the full taxonomic matrix

## Assertion

The decision rule is five questions; the full taxonomic matrix of six classes is assembled from all the parts; this spectrum is current engineering practice.

## Visual

On the left, in an Ocean rounded box — a mental checklist of 5 points (icon `list-checks`): "1. Name the kind of AI, place it on the axis. 2. Deterministic or probabilistic? 3. What is being optimized, and who set the constraints? Is the statement complete? 4. Is there an exact/normative tool? 5. Who is responsible?" On the right — a compact full matrix of 6 classes (icon `table`, single-line cells, ≥14pt, fill ≥75%): rows = Topology optimization / Evolutionary-GA / Surrogate-PINN / Computer vision / LLM assistant / Generative AI for geometry; columns = Nature · What it guarantees · Maturity 2026 · Who is responsible. This is the matrix promised back in s06 and deliberately withheld until now. At the bottom, a narrow context strip (12pt): "Specialized departments and supercomputing centers at technical universities work across this whole spectrum — from certified solvers to accumulated archives of computations." A gold accent (`#F0AB00`) on the "Who is responsible" column (everywhere — the engineer).

## Speaker notes

Let's assemble the decision rule. Before trusting a tool with a design decision, you must, in sequence: name the kind of AI and place it on the axis "deterministic — probabilistic"; determine whether this is deterministic optimization solving a given equation, or a probabilistic model guessing from examples; ask what is being optimized and who set the constraints — is the statement complete, is a load case or a technological constraint or a normative inspection missed; check whether there is an exact or normative tool — if the problem is a certification one, or a certified solver exists, probabilistic AI is superfluous or dangerous; and finally, remember that the signature and responsibility are not delegated to a model.

Now, with every class examined and every cell filled with meaning, let's present the full taxonomic matrix — the one promised at the start of the lecture and deliberately withheld. Topology optimization — deterministic, guarantees the optimum of a given function under given constraints, mature, the engineer is responsible for the statement and the check. Evolutionary algorithms — stochastic optimization, mature in a niche. Surrogates and PINNs — probabilistic approximation, accurate only in the training domain, the final step on a solver. Computer vision — probabilistic classification, a first filter for defects. LLM assistant — probabilistic and generative, guarantees linguistic form, not facts. Generative AI for geometry — probabilistic and generative, guarantees nothing about physics, a concept and an early beta. In every row, the "who is responsible" column reads: the engineer.

This matrix is not for memorizing — it's for applying: it operationalizes all three anchor questions across the six classes at once. Specialized departments and supercomputing centers at technical universities work across this whole spectrum — from certified solvers to accumulated archives of computations; what has been described here is not theory from the future, but current engineering practice.
