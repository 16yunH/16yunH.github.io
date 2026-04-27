---
layout: archive
title: "发表论文"
description: "洪运的发表论文 - 自动驾驶风险地图、IEEE RA-L"
permalink: /cn/publications/
author_profile: true
lang: zh
---

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single-cv.html %}
{% endfor %}
