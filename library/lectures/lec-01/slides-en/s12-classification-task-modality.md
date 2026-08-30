---
id: s12
type: assertion_visual
duration_min: 1.5
assertion: "Classifying AI systems — two axes: task type × modality"
learning_goal: "Give a working language for analyzing types of builds"
learning_outcomes: [LO1]
references: [russell-norvig-2021, goodfellow-2016-dl]
visual:
  pattern: 2d_classifier_matrix_filled
  primary: "Filled 2D matrix 5×4 (issue #155: the «Planning» column and «Code» row removed) with examples in all cells; Lucide icons on each column (tag/scan/search/sparkles/trending-up), larger and clearer row/column headers; the Forecasting×Text cell now contains «GPT-4o, Claude» (text generation = next-token prediction, same semantics as the «Generation» column); all cells — a single neutral color by task type (YOLO no longer highlighted gold — an ordinary cell, axis readability matters more than the callback effect)"
---

# Classifying AI systems: two axes — task type × modality

## Assertion

Classifying AI systems — two axes: task type × modality.

## Visual

A two-dimensional 5×4 matrix in an Ocean rounded box (issue #155: the «Planning» column and «Code» row removed), filled with concrete examples in all cells. Column headers (task type) — large, single-line, each with a Lucide icon on top: classification (tag), recognition (scan-line), retrieval (search), generation (sparkles), forecasting (trending-up). Row headers (modality) — also larger and clearer: text / image / audio-video / structured data. In each cell — concrete products: BERT, ResNet, PANNs, XGBoost, spaCy NER, YOLO, Whisper, OCR, BM25, CLIP, Shazam, vector DB, GPT-4o/Claude, DALL-E, ElevenLabs, Codex, Prophet, ARIMA. The Forecasting×Text cell is filled with «GPT-4o, Claude» (teal, as in the «Generation» column) — emphasizing that text generation by modern LLMs is based on next-token prediction. Color coding by column (task type): MID for classification/retrieval, LIGHT for recognition/forecasting, TEAL for generation — uniform, with no separate gold highlight of the YOLO cell.

## Speaker notes

To talk about specific AI tools in a common language, we need a simple classification. In this course we use two axes: task type and modality. These two axes are enough to place any AI tool we'll work with in later lectures. A deeper technical classification — by training approach and neural-network architecture — is not the main goal of this lecture for our course; we return to those topics in more depth in Lecture 2.

The "task type" axis — what the system produces as output. Classification — assign a label from a finite set: spam or not spam, defect or not defect. Recognition — detect and identify something in the input: faces, speech, characters. Retrieval — find and rank relevant items: over a corporate knowledge base, by a photo. Generation — create new content: text, image, audio, code. Forecasting — predict a number or a sequence: demand, equipment failure, a stock price.

The "modality" axis — what type of data the system works with. Text. Image — photos, X-ray scans, frames from a conveyor camera. Audio — speech, music, industrial noise. Video — a sequence of images, often plus audio. Structured data — tables, time series, graphs, databases. In the "Retrieval × Structured data" cell we have vector DB — a database for retrieval by semantic similarity, which we'll cover in more detail in the slide on the agent. Multimodal combinations — text plus image, text plus audio plus video.

Let's take three examples to lock this in. Google Translate — task generation, modality text. AlphaFold — task forecasting, modality structured data. YOLO, which you saw at the start of the lecture — task recognition, modality image.

This simple table prevents lumping together systems that are different in nature under the common marketing label "AI". When we go on to analyze types of builds later in the section, we'll ask: which task and which modality.
