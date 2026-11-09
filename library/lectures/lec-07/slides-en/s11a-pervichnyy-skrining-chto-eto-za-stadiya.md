---
id: s11a
local_id: s1-01a
section: "1. Первичный скрининг и отбор на обследование"
type: norm
title: "Primary screening: what kind of stage is this"
assertion: "Стадия называется первичным скринингом и отбором на обследование; данные о человеке на входе — возраст, пол и интервал, вопрос один — звать ли его смотреть вообще; получают эти данные четырьмя способами, решение стадии определяет, попадёт ли человек в поле зрения, и стоит стадия первой потому, что непозванного не видит ни одна модель, а порог назначен документом раньше любого замера точности"
source: "—"
media: ""
media_needed: ""
media_note: "иллюстрация не поставлена, и место под неё на кадре отсутствует: описание стадии занимает экран целиком. Любой один снимок — письмо, маммограф, кабинет чтения — показал бы один способ получения данных из четырёх и прочитался бы как вся стадия. Настоящий документ программы стоит кадром ниже, на s12, где он и есть предмет"
timing_min: 0.6
in_bucket: false
method_steps: ["заземление", "описание стадии"]
form: []
vizforma: "дорожки"
vfy: false
status: собран
scheme:
  kind: dorozhki
  exit: "Entered screening"
  caption: "Four entry points, none follows from another"
  rows:
    - {label: "", steps: ["Population registry"]}
    - {label: "", steps: ["Complaint"]}
    - {label: "", steps: ["Doctor's referral"]}
    - {label: "", steps: ["Chart review"]}
---

## Visible slide text

- Known about the person: barely anything — age · sex · interval
- One question: whether to call them in to look. What follows is either an examination, or nothing

**Why this stage comes first.** Nobody sees the uninvited; the threshold is set by a document before any accuracy is ever measured.

**Without a model, there are three orders of work:** call in by age · wait for a complaint · sort those who've already come in by severity.

## Speaker notes

Primary screening and selection for examination — that's what the industry calls this stage, and an engineer walking into a medical project will hear exactly these words. What's known about the person going in is scant: age, sex, and the interval since the last examination. The stage asks one question — whether to call this person in to look at all, and "no" is followed by nothing. The stage has to be described before the tool: otherwise it's unclear what the tool is even intervening in.

Screening is examining people who have no complaints, by a group-membership criterion: age, sex, occupation, a prior diagnosis. The benefit of screening rests on one assumption: a finding made earlier than the complaint changes the outcome. If the disease is treated the same way whether found early or late, screening remains pure cost plus the harm of false alarms.

Data about the person at this stage is scant, and that's its main property. Age. Sex. Interval since the last exam. Sometimes a questionnaire or a single complaint the person brought in themselves. None of what's usually called medical data exists yet: no scan, no test, no examination. And the question decided on this data is also just the one: whether to call this person in to look at all.

There are four ways to obtain this data, and they give different things. An invitation by population registry is the case where there's no data on the person yet, and they're called in by a formal criterion: year of birth, sex, interval. A person's own request with a complaint runs the opposite way: they came in because they felt something, and a symptom drives what follows; their probability of having the disease going in is entirely different, and in the next section that probability will determine what any positive result even means. A referral from another doctor brings someone else's hypothesis along with the person. Reviewing documents already on the chart adds no new measurement at all — it extracts from what's already recorded and becomes a source of its own decision.

The decision this stage makes is short: the person either comes into view, or doesn't. What follows the decision is either an examination, or nothing — until the next interval, or until the day the person feels it themselves.

Now about why this stage comes first, because the order here isn't a convenience of exposition. There are three pillars, and each can be checked. First — who was invited: you can only look at someone who came into view, and a person who wasn't invited is seen by no system, however accurate it is. Second — which group the numbers were computed on: the group on which any measurement's properties are computed is assembled by this very stage, and the share of true alerts among all raised depends on how prevalent the disease is in the assembled group. Third — where the threshold for "sick" sits: the point past which the system declares "sick" is set by protocol, priced against the outcome, and that price is set before any accuracy at all — by whoever decided what's worse, missing a finding or calling in someone unnecessarily. All three pillars sit on this stage, and that's why it can't be moved anywhere else.

And the last thing before the breakdowns — how this decision is made with no trained model at all. This work has to be called by name, because the model will be compared against exactly this: a model compared against an empty space always wins, and that win means nothing. There are three orders of work here. First — call everyone in by age and interval: a program runs, the person takes no part in the decision. Second — wait for a complaint: do nothing until the person comes in on their own. Third — sort the flow of people who've already come in by severity: who gets seen today, who in two weeks; the classical tool for this sorting is five severity categories assigned by a nurse under protocol, and each category gets a mandated time to be seen by a doctor. Of these three, the classical regimes of selection, costed in one price, are two — the first two; their figures, base, and caveats stand on a separate slide in this section. The third order is counted differently, in a different unit. Inside screening reading itself stand two more regimes devised before any automation at all: double reading, where two people read the scan without seeing each other's conclusion, and arbitration — a third reader, brought in only on disagreement.

A mistake at this step isn't visible where people usually look for it: it happens before any diagnosis and before any accuracy measurement.

Occupation is a fourth group criterion alongside age, sex, and prior diagnosis: it's used to call people in for occupational exams, and that's the same no-complaints screening. What follows the stage's decision is either an examination, or nothing — until the next interval, or until the day the person feels it themselves. The threshold set by a document is the age at which people get called in, the interval between invitations, and the criterion for recalling someone for further testing.
