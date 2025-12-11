---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
lang: en
---

{% include base_path %}

You can also download my [CV in PDF format](http://16yunH.github.io/files/YunHong_CV.pdf).

Education
======
* **B.S. Candidate in Computer Science**, Fudan University, Shanghai, China, Sep. 2023 - Present
* **Exchange Student in Computer Science**, University of Texas at Austin, Austin, Texas, Aug. 2025 - Dec. 2025

Skills
======
* **Machine Learning**: Finished all the lectures and labs of ML2022 by Hung-yi Lee
* **Deep Learning**: Including CNN, RNN, LSTM, GAN, Diffusion Model, and have a good command of PyTorch
* **Data Structure**: Finished Data Structure (Honor) by Weiwei Sun, Fudan University and have a good command of data structure & algorithm
* **Programming**: C, C++, Python, Java, LaTeX
* **AI-Drive**: Autonomous Driving: planning, prediction and decision making
* **Computer Vision**: Multi-view Geometry, 3D Reconstruction (SfM/Stereo), Camera Calibration, Object Detection & Segmentation, Optical Flow
* **Languages**: Chinese, English

Research Experience
======
* **Research on ChatGPT-o1 model reproduction and reflection ability improvement**
  * *Research Assistant*, Shanghai, China, Sep. 2024 - Jun. 2025
  * Under the guidance of Professor Xuanjing Huang from Fudan University Natural Language Processing Group.
  * By constructing, evaluating, and optimizing reflection datasets, we study how to introduce self-inspection and correction mechanisms into model reasoning to improve the performance of models in complex tasks.
  * Responsible for the synthesis and training of self-critic data. Based on Llama3.1-8b-instruct, generate "reflection" answers from wrong to right, and use different strategies to generate diverse data of the reflection process, such as constructing complex reflection paths based on tree search reasoning, and verifying premises from conclusions through reverse reasoning. Use gsm8k test set to evaluate the performance of different methods.

* **Learning RiskMap for Autonomous Driving in Partially Observable Environments**
  * *Status: Preprint; Focused on gaining research experience and training*, Shanghai, China, Oct. 2024 - May. 2025
  * Engineered risk field representations using advanced spatiotemporal modeling techniques.
  * Developed and implemented realistic traffic scene generation leveraging diffusion models combined with gradient optimization.
  * Designed and actualized a lightweight neural network for efficient risk prediction.

Project Experience
======
* **LCDP-Sim: Language-Conditioned Diffusion Policy**
  * *Independent Developer*, Austin, Texas, Dec. 2025 - Present
  * Developed an end-to-end Vision-Language-Action (VLA) system utilizing Diffusion Policy to map RGB images and natural language instructions into robotic control signals.
  * Integrated CLIP text encoder for semantic understanding and employed a U-Net-based DDPM/DDIM architecture for high-fidelity action generation.
  * Implemented Action Chunking (predicting 16-step trajectories) to mitigate error accumulation and enhance motion smoothness in long-horizon tasks.
  * Built a complete pipeline for data collection, distributed training, and closed-loop evaluation in ManiSkill2 simulation.

* **Map Navigation**
  * *Independent Developer*, Shanghai, China, Dec. 5, 2024 - Present
  * This project combines OpenStreetMap data with Gaode Maps API to provide accurate routing and location search capabilities.
  * Implemented various extended features including hybrid point selection (manual map clicks or location search), detailed route information display and support for different road types (motorway, trunk, etc.) with speed limit considerations.

* **NeuralStyle: A Modular Neural Style Transfer Project**
  * *Independent Developer*, Shanghai, China, Jun. 2025 - Present
  * Developed a neural style transfer toolkit in Python with clear modular separation for maintainability and extensibility.
  * Implemented batch processing enabling automated multi-image / multi-style workflows.
  * Designed a configurable pipeline centralizing hyperparameters (e.g., image size, optimization steps, style/content weighting) to streamline experimentation.
  * Built an interactive web interface allowing users to upload content and style images and generate stylized outputs directly in the browser.
  * Provided runnable entry points and a reproducible dependency specification.

Honors & Awards
======
**International**
* **2024**: Finalist, Water, sanitation, and hygiene for the prevention and care of neglected tropical diseases

**Domestic**
* **2024**: 3rd Prize, China Undergraduate Mathematical Contest in Modeling, 2024
* **2023**: Finalist, Full-stack AI development engineer skills training by NVIDIA

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
