---
id: s15
type: case_study
duration_min: 3
assertion: "The model is a component, not a system. Inference: input → preprocessing → model → postprocessing → output"
learning_goal: "Model = stateless inference; preprocessing/postprocessing — the developer's responsibility"
learning_outcomes: [LO1, LO4]
references: [kreuzberger-2023-mlops, jumper-2021-alphafold]
visual:
  pattern: pipeline_with_examples
  primary: "Eyebrow pill «MODEL» on top; schema: 5 blocks horizontally (Raw input → Preprocessing → Model → Postprocessing → Output) enclosed in a shared frame labeled «This is already an application»; 4 model examples below"
---

# The model is a component, not a system. Inference: input → preprocessing → model → postprocessing → output

## Assertion

The model is a component, not a system. Inference: input → preprocessing → model → postprocessing → output.

## Visual

An eyebrow pill «MODEL» in the top-left corner — a single pattern with s16/s17/s18/s19/s19a, showing which of the 4 ways to build is being analyzed on the slide. On top a horizontal schema in an Ocean rounded box: 5 blocks in sequence — Raw input → Preprocessing → Model → Postprocessing → Output. Gold arrows between the blocks. Under each block a short caption with an example (camera frame, resize+normalize, inference, NMS+softmax, JSON). The whole 5-block pipeline is enclosed in an additional outer frame labeled «This is already an application» — visually showing that the "model" is only one block inside a whole application. Below, four small cards with model examples, the role under each name a single-line caption with no line breaks: YOLOv8 — «detection in images», Whisper — «speech recognition», Stable Diffusion — «image generation», AlphaFold — «protein-structure forecasting».

## Speaker notes

The model, in our terminology, is a trained neural network or another ML algorithm that takes an input of a certain type and returns an output. It has neither state between calls, nor access to external tools, nor a dialogue with the user. From the standpoint of engineering integration it's the simplest component: a call to the model is a function, and it behaves like a function.

A very important detail that's often missed: the model is not a standalone system, but a component. In production there's always a wrapper of preprocessing and postprocessing around the model. Schematically: a raw input — for example, a frame from a camera, text, or audio — passes through preprocessing (resize, normalization, tokenization), then through the model's inference, then through postprocessing (filtering, formatting, packaging the bounding box, softmax), and only then do we get an output for the application.

Preprocessing and postprocessing are the responsibility of the system's developer, not of the model itself. This isn't a caveat — it's critically important for estimating the budget and complexity of an AI project. A YOLO detector by itself takes a nominal fifty lines of code, but a working system with YOLO inside contains hundreds of lines: reading the video stream, resizing frames, normalization, NMS filtering after inference, packaging the result into the format the factory's MES system expects. Estimating the "roll YOLO onto the line" project by the volume of the model's work gives an estimate that's off by tens of times.

Canonical examples of models. YOLO — object detection in images, the same one that was at the start of the lecture. Whisper by OpenAI — speech recognition. Stable Diffusion — image generation from text. BERT — vector representations of text. AlphaFold — prediction of the three-dimensional structure of a protein from its amino-acid sequence; for it Hassabis and Jumper received the 2024 Nobel Prize in Chemistry. Segment Anything by Meta — universal image segmentation.

When the model is the right choice. High load, for example processing a video stream at thirty frames per second — impossible for a chat interface. A single clearly defined task with a stable shape of input and output. A requirement of determinism or predictability. Edge deployment without the internet. Embedding AI as a functional unit inside a larger product.
