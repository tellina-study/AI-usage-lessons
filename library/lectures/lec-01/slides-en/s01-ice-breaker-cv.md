---
id: s01
type: live_demo
duration_min: 3
assertion: "Real-time identification of people — on a laptop, with no internet, since 2023."
learning_goal: "Opening hook: AI as a working local tool"
learning_outcomes: [LO1]
references: [yolov8-ultralytics-2023, mediapipe-google]
visual:
  pattern: external_demo
  primary: "Mock YOLO inference output (2 people in bbox) framed by an Ocean rounded box; assertion on the left"
  backup: assets/code/ice-breaker-cv/backup/screenshot.png
interaction: live_demo
---

# Real-time identification of people — on a laptop, with no internet

## Assertion

Real-time identification of people — on a laptop, with no internet, since 2023.

## Visual

A frame of a YOLO detector at work with two people in bounding boxes, framed by an Ocean rounded box. Assertion on the left, and under it a small definition: "narrow AI — a model that solves one task". Caption under the screenshot: "YOLOv8 on the laptop CPU · ~30 fps · no internet".

## Speaker notes

Right now you are seeing a simple experiment: a laptop with a webcam projects the image of the room onto the screen, and a small program draws a box around every person present in real time and counts the people in the frame. Under the hood is the YOLOv8 model from Ultralytics, published in 2023. It was trained on the standard COCO dataset and recognizes 80 object classes; for us right now only the "person" class matters.

This demonstration has three significant properties that form one of the main claims of the lecture. First, the model runs locally — on the CPU of an ordinary laptop, without a graphics card and without any calls to cloud servers. Second, the speed is about 30 frames per second, which is enough for real time on a video stream. Third, no internet: the camera, the model, and the projector are three components in a single room, and no images are transmitted anywhere.

This is an example of what the literature calls narrow AI — a system trained on one clearly defined task and capable of nothing else. This same model cannot hold a conversation with you, it will not write code, and it will not propose a marketing strategy. But on its single task it works fast and predictably. Today we will see that most systems in engineering practice are like this, and that choosing the type of AI to fit the task is a separate skill, one we will be practicing throughout the course.
