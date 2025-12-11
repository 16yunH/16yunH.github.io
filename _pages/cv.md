---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<div style="display: flex; gap: 20px; margin-bottom: 20px;">
  <a href="{{ base_path }}/files/CV_en.pdf" class="btn btn--primary" style="text-decoration: none;">Download English CV</a>
  <a href="{{ base_path }}/files/CV_zh.pdf" class="btn btn--primary" style="text-decoration: none;">Download Chinese CV</a>
</div>

Education
======
* **B.S. Candidate in Computer Science**, Fudan University, Shanghai, China, Sep. 2023 - Jul. 2027 (Expected)
* **Exchange Student in Computer Science**, University of Texas at Austin, Austin, Texas, Aug. 2025 - Dec. 2025

Research Experience
======
* **Sep. 2024 - Jun. 2025: Research Assistant**
  * Fudan University Natural Language Processing Group
  * Project: Research on ChatGPT-o1 model reproduction and reflection ability improvement
  * Supervisor: Professor Xuanjing Huang
  * Duties: Constructing, evaluating, and optimizing reflection datasets; synthesizing and training self-critic data based on Llama3.1-8b-instruct; generating diverse reflection process data using tree search reasoning and reverse reasoning strategies

* **Oct. 2024 - May 2025: Research Focus**
  * MagicLab, Fudan University  
  * Project: Learning Risk Map for Autonomous Driving in Partially Observable Environments
  * Supervisor: Wenchao Ding
  * Duties: Engineering risk field representations using spatiotemporal modeling; developing traffic scene generation with diffusion models; designing lightweight neural networks for risk prediction
  * Status: Research submitted to IEEE Robotics and Automation Letters (RAL)

Skills
======
* **Machine Learning**
  * Completed all lectures and labs of ML2022 by Hung-yi Lee
  * Proficient in various ML algorithms and techniques

* **Deep Learning**  
  * CNN, RNN, LSTM, Transformer, GAN, Diffusion Models
  * Strong command of PyTorch framework

* **Programming Languages**
  * C, C++, Python, Java, LaTeX
  
* **Specialized Areas**
  * AI-Driven Autonomous Driving: planning, prediction, and decision making
  * Computer Vision: Multi-view Geometry, 3D Reconstruction (SfM/Stereo), Camera Calibration, Object Detection & Segmentation, Optical Flow
  * Data Structures & Algorithms: Completed Data Structure (Honor) course by Weiwei Sun

* **Languages**
  * Chinese (Native), English (Fluent)

Projects
======
* **LCDP-Sim: Language-Conditioned Diffusion Policy** (Dec. 2025 - Present)
  * Independent Developer, Austin, Texas
  * Developed an end-to-end Vision-Language-Action (VLA) system utilizing Diffusion Policy
  * Integrated CLIP text encoder and U-Net-based DDPM/DDIM architecture for high-fidelity action generation
  * Implemented Action Chunking (16-step prediction) to mitigate error accumulation
  * Built complete pipeline for data collection, distributed training, and closed-loop evaluation in ManiSkill2

* **MapNavigation** (Dec. 2024 - Present)
  * Independent Developer
  * Long-term maintained project combining OpenStreetMap data with Gaode Maps API
  * Features: hybrid point selection, detailed route information, support for different road types
  * Repository: [https://github.com/16yunH/MapNavigation](https://github.com/16yunH/MapNavigation)

* **NeuralStyle** (Jun. 2025 - Present)  
  * Independent Developer
  * Modular neural style transfer toolkit with batch processing capabilities
  * Interactive web interface and configurable pipeline for experimentation
  * Repository: [https://github.com/16yunH/NeuralStyle](https://github.com/16yunH/NeuralStyle)

Extracurricular Activities
======
* **Core Member**, China Undergraduate Mathematical Contest in Modeling (CUMCM), Sep. 2024
* **Core Member**, Fudan University's team of aid education in Yudu, Jiangxi, Jan. 2024 - Feb. 2024
* **Member**, Fudan Piano Association, Oct. 2023 - Present
* **Keyboard Player**, Fudan Musicians Alliance, Sep. 2024 - Present

Honors & Awards
======
* **2024**: Finalist, Water, sanitation, and hygiene for the prevention and care of neglected tropical diseases (Geneva, Switzerland)
* **2025.05**: Excellent Work Award, The 5th Meituan Business Analytics Elite Competition  
* **2024.12**: 3rd Prize, China Undergraduate Mathematical Contest in Modeling (CUMCM)
* **2023**: Finalist, Full-stack AI development engineer skills training by NVIDIA

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
