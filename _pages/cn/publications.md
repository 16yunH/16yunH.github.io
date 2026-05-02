---
layout: archive
title: "发表论文"
permalink: /cn/publications/
author_profile: true
lang: zh
---

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single-cv.html %}
{% endfor %}
