---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

You can also download my [CV in PDF format]({{ base_path }}/files/CV_en.pdf).

Education
======
* **B.S. Candidate in Computer Science**, Fudan University, Shanghai, China, Sep. 2023 - Present
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
  * Data Structures & Algorithms: Completed Data Structure (Honor) course by Weiwei Sun

* **Languages**
  * Chinese (Native), English (Fluent)

Projects
======
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
* **2024**: Finalist, Water, sanitation, and hygiene for the prevention and care of neglected tropical diseases (International)
* **2025**: Excellent Work Award, The 5th Meituan Business Analytics Elite Competition  
* **2024**: 3rd Prize, China Undergraduate Mathematical Contest in Modeling
* **2023**: Finalist, Full-stack AI development engineer skills training by NVIDIA

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
