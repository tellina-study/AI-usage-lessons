---
id: s20
type: assertion_visual
duration_min: 1.5
assertion: "«AI and copyright» is not one question but 4 categories of lawsuits: training-data scraping / output similarity / style imitation / voice/likeness."
learning_goal: "Taxonomy of 4 lawsuit categories"
learning_outcomes: [LO4, LO5]
chapter_ref: "§3.1 — Copyright: taxonomy of 4 categories"
references: []
visual:
  pattern: quadrant
  primary: "2×2 matrix of categories + «Lesson for the engineer» Ocean rounded box"
---

# AI copyright — 4 lawsuit categories

## Assertion

"AI and copyright" is not one question but 4 categories of lawsuits: training-data scraping / output similarity / style imitation / voice/likeness.

## Visual

On top, the assertion 26pt. Center — a 2×2 matrix in the Ocean palette: Category 1 (Training-data scraping — input side, NYT, Andersen): mid blue. Category 2 (Output similarity / memorization, NYT verbatim-citation theory): light teal. Category 3 (Style imitation, Andersen "in the style of"): gold-tint outline. Category 4 (Voice/likeness, ScarJo, SAG-AFTRA Digital Replicas): teal accent. Each cell contains — the category name + theory of harm + 1 example case. To the right of the matrix — a gold Ocean rounded box "Lesson for the engineer": "'AI copyright' is not one question but 4 different risk categories; look at which of the 4 applies to your process."

## Speaker notes

The "AI vs copyright" paradigm is not one legal question but four different categories of lawsuits, with different legal logic, different precedents, different outcomes. An engineer assessing an AI tool for a creative task must understand which of the four categories their process falls into in order to correctly assess the risk profile. Category one — training-data scraping without a license, input side. Lawsuits focus on the AI company having assembled a training corpus, including copyright-protected works, without a license from the rights holders. Theory of harm — the very fact of including a protected work in the training dataset is an infringement. The outcome depends on whether the court recognizes training as "fair use" in the US or its analogs in other jurisdictions. Category two — output similarity or memorization, output side. Lawsuits focus on the AI reproducing copyright-protected material in the output — the model memorizes and regurgitates training content. Theory of harm — not the manner of training but the model's ability to return protected content given the right prompt. Category three — style imitation. Lawsuits about generating "in the style of a specific artist." Style itself is not copyrightable in most jurisdictions, but a class action (a group lawsuit by a group of plaintiffs in the US) by artists can survive an MTD on DMCA and publicity rights. Category four — voice and right of publicity. This is a different class of legal regulation — right of publicity. ScarJo v. OpenAI Sky, SAG-AFTRA Digital Replicas clause. Lesson for the engineer: "AI copyright" is not one question but four different risk categories. Look at which of the four applies to your process. If you are building a product on a foundation model — categories one and two, the risk of NYT- and Getty-type lawsuits. If you are building a creator tool that generates "in the style of X" — category three, the risk of an Andersen class action. If you use the voice or face of specific people — category four, the risk of ScarJo and SAG-AFTRA clauses. This classification is the basis for all the next five cases of the section.
