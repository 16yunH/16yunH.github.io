---
layout: archive
title: "简历"
permalink: /cn/cv/
author_profile: true
lang: zh
---

{% include base_path %}

<div style="display: flex; gap: 20px; margin-bottom: 20px;">
  <a href="{{ base_path }}/files/CV_zh.pdf" class="btn btn--primary" style="text-decoration: none;">下载中文简历</a>
  <a href="{{ base_path }}/files/CV_en.pdf" class="btn btn--primary" style="text-decoration: none;">下载英文简历</a>
</div>

教育经历
======
* **计算机科学技术 本科**，复旦大学，中国上海，2023.09 - 2027.07（预计）
* **计算机科学 交换生**，德克萨斯大学奥斯汀分校，美国奥斯汀，2025.08 - 2025.12

专业技能
======
* **机器学习**: 完成李宏毅 ML2022 全部课程与实验
* **深度学习**: 熟悉 CNN, RNN, LSTM, GAN, Diffusion Model, 熟练掌握 PyTorch
* **数据结构**: 修读复旦大学《数据结构（荣誉）》课程（孙未未教授），具备扎实的数据结构与算法设计能力
* **编程语言**: C, C++, Python, Java, LaTeX
* **自动驾驶**: 规划 (Planning)、预测 (Prediction)、决策 (Decision Making)
* **计算机视觉**: 熟悉多视图几何、三维重建 (SfM/Stereo) 及相机标定；掌握目标检测、图像分割与光流估计技术
* **语言能力**: 中文（母语）、英语（流利）

科研经历
======
* **大模型推理反思与自查机制研究**
  * *研究助理 (导师: 黄萱菁)*，中国上海，2024.09 - 2025.06
  * 基于 Llama3.1 探索类似 o1 的自查纠错机制
  * 设计基于树搜索与逆向推理的数据合成策略
  * 构建 Self-Critic 训练管线，在 GSM8K 测试集上验证了复杂逻辑推理能力的显著提升

* **部分可观测环境下的自动驾驶风险地图学习**
  * *核心研究员 (导师: 丁文超)*，中国上海，2024.10 - 2025.05
  * 研究成果已整理并投稿至 IEEE Robotics and Automation Letters (RAL)
  * 利用时空建模构建动态风险场，解决部分可观测下的安全预测问题
  * 提出结合扩散模型的场景生成算法解决数据稀缺问题
  * 设计轻量级网络实现实时高精度预测

项目经历
======
* **LCDP-Sim: 基于语言条件的扩散策略机械臂控制系统**
  * *独立开发者*，2025.12 - 至今
  * 开发端到端 VLA 系统，利用 Diffusion Policy 将视觉与语言指令映射为高精度机械臂动作
  * 集成 CLIP 语义理解与 U-Net 动作生成，实现 Action Chunking (16步预测) 消除累积误差
  * 在 ManiSkill2 仿真环境中构建从数据采集、分布式训练到模型评估的完整闭环管线

* **MapNavigation**
  * *独立开发者*，2024.12 - 至今
  * 结合 OpenStreetMap 数据与高德地图 API 的导航系统
  * 实现了混合选点（手动点击或位置搜索）、详细路线信息显示和多种道路类型支持

* **NeuralStyle: 模块化神经风格迁移工具箱**
  * *独立开发者*，2025.06 - 至今
  * 基于 PyTorch 实现高度解耦的风格迁移库，支持多风格批处理与自动化生成工作流
  * 构建了基于 Web 的交互界面，允许用户在浏览器端上传图片并实时生成风格化结果

获奖情况
======
**国际级**
* **2024**: Finalist, Water, sanitation, and hygiene for the prevention and care of neglected tropical diseases

**国家级/省级**
* **2025.05**: 第五届美团商业分析精英大赛 优秀作品奖
* **2024.12**: 全国大学生数学建模竞赛 (CUMCM) 三等奖
* **2023**: Finalist, Full-stack AI development engineer skills training by NVIDIA

发表论文
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
