---
id: s02
type: cover
section: "Section 0. Opening"
duration_min: 0.5
assertion: "Lecture 3. AI system architectures: agents, RAG, API"
learning_goal: "Cover + roadmap of 5 sections; gold marker «Section 0»"
learning_outcomes: [LO7, LO4]
chapter_ref: "§Introduction [for-slide-s02]"
visual_brief: "Clean hero cover (roadmap moved to a separate lecture-map s02a, #212): a large outline «03» (200pt, Primary mid contour) on the left. Right — the tag «LECTURE 3», title 36pt bold deep, below it a subtitle (the lecture's central question), at the bottom a small meta-line (course/audience) WITHOUT timing in minutes. NO roadmap bar (moved to s02a). NO Ocean rounded box callout (the motif belongs to content)."
interaction: none
---

# Visible content

## Title bar
(none — cover composition)

## Body
[Left — a large outline «03» (200pt, Primary mid `#065A82` contour, no fill)]

[Tag above the title — 14pt bold teal `#028090`]
LECTURE 3

[Title — 36pt bold deep `#21295C`]
**AI system architectures: agents, RAG, API**

[Subtitle — 18pt light `#1C7293`]
*Which architecture to choose for a task — and when the right answer is "not AI"*

[Meta-line at the bottom — 14pt italic slate, NO timing]
*3rd year IU6 · Module 1, overview lecture*

## Speaker notes

Today's topic is AI system architectures: agents, RAG, API. This is the last overview lecture of the course's introductory module. Lecture 1 explained what an AI model is and how a prompt is structured; Lecture 2 explained why a prompt works from the inside: tokenization, embeddings, attention, sampling. This lecture answers the next engineering question in order: how do you assemble a working system out of a model — and how do you choose which system to assemble.

There is one keystone idea running through the whole lecture, and it is worth keeping in mind all the way to the end: the choice of architecture is an engineering decision for a specific task, not a matter of following fashion. Often the right answer is the simplest architecture possible. And sometimes the right answer is to not use AI at all. We will keep returning to this idea in every section: first we will look at what a single model call can do and where its limits are, then climb the ladder of complexity — RAG, fine-tuning, agents — and at each rung ask the same question: is this complexity even needed here, and what do we pay for it.
