---
id: s05a
type: assertion_visual
duration_min: 1
assertion: "Who I am and why this matters to me"
learning_goal: "Short instructor bio card"
learning_outcomes: [LO1]
visual:
  pattern: instructor_bio_card
  primary: "Left vertical strip (SURFACE background, ~28% width) — portrait photo + full name + divider line + 2 contacts (Telegram, Email) with round icon badges. Right part (white background, ~72%) — specialization heading + short description, then 3 cards in 2 tiers: top tier — 2 cards (experience with a gold accent on \"20+\", expertise), bottom tier — 1 wide card with 4 pill badges for companies (generic building icon, no official logos)."
  backup: "n/a"
---

# Who I am and why this matters to me

## Assertion

Who I am and why this matters to me.

## Visual

Full rebuild against the reference `library/seminars/sem-01/slides/s02-instructor-bio.md`
(issue #155 fix #174).

**Left strip** (SURFACE `#F4F7FA` background, ~28% of slide width, full height):
the instructor's portrait photo (`assets/instructor-photo-crop.png`, cropped
to a 3:4 portrait ratio) in a thin LIGHT frame at the top; below — "Levko
Maxim Nikolaevich" large bold DEEP; a thin divider line
(COVER_OUTLINE); 2 contact lines with round icon badges (Lucide
`send` + "Telegram" / "@Maxim_Levko", Lucide `mail` + "Email" /
"Levko.maxim@gmail.com").

**Right part** (white background, ~72% width): specialization heading
"Architect, technical and product lead for the creation and deployment of
information systems" (MID, bold). Below — 3 Ocean rounded box cards in
2 tiers: top tier (2 cards in a row) — card A "briefcase" icon +
"**20+** years of experience in IT" (the number 20+ highlighted in gold) + "10+ completed
projects led"; card B "layers" icon + "Expertise" +
"Systems analysis · Systems design · Data management ·
Business automation · Product management". Bottom tier (1 wide
card) — "Consulting and in-house" + 4 company pill badges (Yandex, MTS,
Magnit, Sibur), each with a generic building icon (not official logos
— trademark/asset-sourcing risk) in a TEAL_TINT fill.

## Speaker notes

To start — a few words about myself. I am an architect and a technical and product lead
in the development and deployment of information systems, with more than twenty years in IT.
Over that time, more than ten completed projects have been delivered under my leadership — from
systems analysis and architecture design to data management, business-process automation, and product launches.

I have worked both as a consultant and as a full-time employee — with Yandex (the leading Russian internet/search-and-services company), MTS (a major Russian telecom operator),
Magnit (a large Russian grocery-retail chain), and Sibur (the largest Russian petrochemicals producer). These are different industries — technology, telecom, retail,
petrochemicals — and in each of them AI was applied in its own way, with varying degrees of success. That is exactly
why I am interested not in a general conversation about "artificial intelligence", but in a
concrete engineering boundary: where AI genuinely saves time and money, and
where it is a pretty demo that falls apart in production.

This course is an attempt to give you the map I myself did not have when I
was just starting to figure out these tools in real projects. We
will work through concrete engineering decisions, not general declarations, and the
boundaries — where AI breaks — will get just as much attention
as the success stories.

If questions come up during the course that don't fit the lecture format — write to me on
Telegram (@Maxim_Levko) or by email (Levko.maxim@gmail.com). The earlier you
ask a question, the more useful the answer will be — don't save them up until the end of the semester.
