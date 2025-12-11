---
title: "LCDP-Sim: Language-Conditioned Diffusion Policy"
excerpt: "An end-to-end Vision-Language-Action (VLA) system utilizing Diffusion Policy to map RGB images and natural language instructions into robotic control signals."
collection: portfolio
---

## LCDP-Sim Project

**Language-Conditioned Diffusion Policy for Robotic Control**

*Independent Developer | Austin, Texas | Dec. 2025 - Present*

**GitHub Repository**: [https://github.com/16yunH](https://github.com/16yunH)

### Overview
Developed an end-to-end Vision-Language-Action (VLA) system utilizing Diffusion Policy to map RGB images and natural language instructions into robotic control signals.

### Key Features
* **Vision-Language-Action (VLA)**: Maps RGB images and natural language instructions directly to robotic control signals.
* **Diffusion Policy**: Utilizes diffusion models for robust policy learning.
* **Action Chunking**: Predicts 16-step trajectories to mitigate error accumulation and enhance motion smoothness in long-horizon tasks.

### Technical Implementation
* **CLIP Text Encoder**: Integrated for semantic understanding of language instructions.
* **U-Net Architecture**: Employed a U-Net-based DDPM/DDIM architecture for high-fidelity action generation.
* **Simulation**: Built a complete pipeline for data collection, distributed training, and closed-loop evaluation in ManiSkill2 simulation.
