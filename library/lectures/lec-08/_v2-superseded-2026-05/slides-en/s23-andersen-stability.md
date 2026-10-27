---
id: s23
type: assertion_visual
duration_min: 2
assertion: "Andersen v. Stability/Midjourney/DeviantArt — an artists' class action. Motion to dismiss denied → discovery; trial Sep 8, 2026. Style imitation."
learning_goal: "Case 3: style-imitation class action"
learning_outcomes: [LO4]
chapter_ref: "§3.4 — Andersen v. Stability"
references: [andersen-docket, judge-orrick-2024]
visual:
  pattern: assertion_visual
  primary: "Court docket screenshot + timeline (Jan 2023 → Aug 2024 motion to dismiss denied → Sep 8 2026 trial) + «Lesson on style imitation»"
  backup: assets/backup/s23-andersen-docket.png
---

# Andersen v. Stability — style-imitation class action (Case 3)

## Assertion

Andersen v. Stability/Midjourney/DeviantArt — an artists' class action. Motion to dismiss denied → discovery; trial Sep 8, 2026. Style imitation.

## Visual

On top, the assertion 24pt. On the left — a court docket screenshot mock-up in an Ocean rounded box (US District Court, Northern District of California). On the right — a vertical timeline: January 2023 (filing — Andersen, McKernan, Ortiz, Andersen + 7 other artists) → August 2024 (motion to dismiss denied by Judge Orrick → discovery) → February 27, 2026 (third amended complaint) → September 8, 2026 (trial). Below the timeline — a chip "Style imitation 'in the style of [artist]' theory." Below — a gold "LESSON FOR THE ENGINEER": "Style imitation 'in the style of [a specific artist]' is not safe just because style is not copyrightable. Class actions pass a motion to dismiss on DMCA + publicity rights."

## Speaker notes

The third copyright case — Andersen plus McKernan plus Ortiz plus seven other artists v. Stability AI, Midjourney, and DeviantArt. This is a class action filed in January 2023 in the US District Court, Northern District of California. The main argument — generative AI tools let users generate images "in the style of [a specific artist]," which the artists consider an infringement of their publicity rights plus copyright plus DMCA. This is a category-three lawsuit under the previous slide's taxonomy — style imitation. Chronology. In August 2024, Judge Orrick denied a Motion to Dismiss for most claims. This means the class action survived the initial procedural challenge and moves into discovery. This is critically important — discovery in a class action in the US for AI companies means documented internal communications, training-data lists, model checkpoints, everything the plaintiffs' lawyers can demand via a subpoena. The third amended complaint was filed on February 27, 2026; the trial is scheduled for September 8, 2026, that is, four months after our lecture. What this case has already changed. Many adjacent AI image companies — for example, Adobe Firefly — position themselves as commercially safe precisely because Adobe trains Firefly on Adobe Stock plus licensed content, not on web-scraped data. This positioning is directly a response to Andersen-class risk. Lesson for the engineer: style imitation "in the style of a specific artist" is not safe just because style is formally not copyrightable. Class actions pass a motion to dismiss on DMCA plus publicity rights. If your product lets users generate "in the style of [a specific living artist]" — you have Andersen-class risk, and it must be accounted for in the product roadmap not as a theoretical scenario but as a realistic outcome. A practical solution — do not allow users to name living artists in prompts; a mask at the input-filtering stage.
