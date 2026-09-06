---
id: s26
type: comparison
section: "Section 5. Recommendations"
duration_min: 3
assertion: "Collaborative — «people similar to you took X» (cold-start, popularity bias); content-based — «similar by features to your favorite» (over-specialization)"
learning_goal: "INTRODUCTION FROM SCRATCH: 2 recsys approaches + analogy user×item / cloud of features; weaknesses by name"
chapter_ref: "§5.1"
visual_brief: "Top — a compact 2-column collaborative vs content-based (weaknesses by name). Bottom — VISUAL band d26b (anchor analogy «three salespeople»: collaborative=behavior pattern / content=catalog / hybrid=both+context). Gold — both weaknesses by name. (The d26 matrix was replaced by d26b: the matrix confused student/reader.)"
interaction: none
verify_day_of: false
---

# Visible content

## Title bar
Two basic recommendation approaches — and each with its weakness by name.

## Body
[Ocean rounded box — 2 columns, parallel structure]

**Collaborative filtering** | **Content-based filtering**
*«people similar to you took X»* | *«this is similar by features to your favorite»*
builds a **user × item** matrix, looks for similar rows | uses **item attributes** (genre, brand, price)
does not know *what* the item is — only who interacted with what | does not look at other users at all
**strength:** catches unexpected connections | **strength:** no cold-start for a new item
**weakness:** **cold-start** (no history — nothing to recommend on) + **popularity bias** (the popular surfaces) | **weakness:** **over-specialization** (locks into the niche «more of the same»)

[Left in the first column — d26 (user×item matrix)]

[Analogy card, bottom]
collaborative — «ask people similar to you what they took»; content-based — «take another item similar by description to your favorite». The first risks drowning you in the popular, the second — locking you into a niche.

[Gold callout]
To remember: **what** these approaches are and **which** weakness by name each has. The mechanism — on a concrete matrix later.

## Speaker notes

The task of this section is personalization: what else to buy or watch, ranking the feed, the search results, the home page. The AI type is recommender systems. You are seeing this concept for the first time, so let us unfold the two basic approaches in plain terms, as the core of the section.

The first approach — collaborative filtering. The idea in one phrase: people similar to you by behavior bought or watched something, so you will probably like it too. The system builds a large table «user by item» — who bought or rated what — and looks for similar rows in it. Important: it does not know what the item is, only who interacted with what. Strength: it catches unexpected, non-obvious connections — drill buyers often take precisely these gloves, and the system sees this even without knowing what a drill is. Weaknesses that must be named right away: cold-start — for a new item or a new user there is no history, nothing to recommend on; and popularity bias — the system tends to recommend what is already popular, because there is the most data on it.

The second approach — content-based filtering. The idea: this item is similar by its features to what you already liked. The system uses item attributes — genre, brand, category, price — and recommends the similar. Strength: no cold-start problem for a new item — as soon as an item has attributes, it can be recommended. Weakness: over-specialization — the system locks the user into a narrow niche of «more of the same», not opening anything beyond already known preferences. An analogy that separates the two approaches: collaborative — ask people similar to you what they took; content-based — take another item similar by description to your favorite. The first risks drowning you in the popular, the second — locking you into a niche. Here it is enough to remember what these approaches are and which weakness by name each has; the mechanism itself we will analyze later on a concrete matrix.
