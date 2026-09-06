---
id: s07
type: case_study
section: "Section 1. Time-series forecasting"
duration_min: 2.5
assertion: "X5: accuracy >70%, +5 billion ₽, −2% write-offs; Magnit builds its own F&R after the departure of SAP/Blue Yonder — forecasting is dictated by the task, neither adopted an LLM"
learning_goal: "Real Russian example + import substitution of forecasting systems as an engineering task"
chapter_ref: "§1.3"
visual_brief: "2 panels: X5 (3 stat cards, gold on +5 billion) + Magnit (import substitution). Conclusion card. Footer — attribution caveat."
interaction: none
verify_day_of: true
---

# Visible content

## Title bar
Forecasting is dictated by the task: neither X5 nor Magnit adopted an LLM.

## Body
[Ocean rounded box — 2 panels]

**X5 Group** *(Pyaterochka, Perekrestok)*
- demand-forecast accuracy **> 70%**
- **+5 billion ₽** in additional revenue from ML tools
- write-offs of expired goods **−2%**
*(per company data / industry reviews, 2023)*

**Magnit** *(a large Russian grocery-retail chain)* — import substitution of forecasting systems
- before 2022: foreign vendors of the SAP / Blue Yonder class
- after their departure: an in-house forecasting + auto-ordering system (F&R), a pilot at a distribution center
*(per company statement, 2024–2025)*

[Conclusion card]
Forecast accuracy converts directly into money: fewer write-offs, fewer lost sales.

[Gold callout, bottom]
Neither X5 nor Magnit solves this task with a language model — they build specialized forecasting systems, because **the type of AI is dictated by the task**.

[Footer]
*Per company data and industry reviews (X5/TAdviser 2023; shoppers.media/TAdviser 2024–2025); the numbers are presented as claimed by the companies.*

## Speaker notes

Let's move to a real example from Russia. X5 Group, the Pyaterochka and Perekrestok chains, has been developing its own demand-forecasting algorithms since 2019. Per company data and industry reviews, forecast accuracy exceeds seventy percent; by the end of 2023, ML tools had brought in about five billion rubles in additional revenue and reduced write-offs of expired goods by about two percent. What this means for the engineer in essence: the forecast is not an end in itself, it is wired to the decision about ordering and shelf replenishment; forecast accuracy converts directly into money — fewer write-offs, fewer lost sales.

The second example is especially instructive in the Russian context. Before 2022, Magnit used forecasting-and-logistics systems from foreign vendors of the SAP and Blue Yonder class. After their departure from the Russian market, since the autumn of 2024 the company has been developing its own demand-forecasting and auto-ordering system: the pilot started at a distribution center, and per the company's statement it planned to migrate thousands of product items to the new system. The pedagogical conclusion: the departure of foreign vendors made import substitution of forecasting systems not a theoretical but a direct engineering task for the Russian industry — this is the context in which you will work.

And note the main point: neither X5 nor Magnit solves this task with a language model. They build specialized forecasting systems, because the type of AI is dictated by the structure of the task, not by which tool is currently on everyone's lips. This is the thesis of the lecture, confirmed at the scale of the country's largest retail chains.
