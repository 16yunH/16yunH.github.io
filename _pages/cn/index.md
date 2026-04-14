---
permalink: /cn/
title: "洪运"
author_profile: true
lang: zh
---

{% assign home = site.data.homepage %}

{{ home.intro.zh }}

## 教育经历

{% for edu in home.education %}
### {{ edu.institution_zh }} | {{ edu.location_zh }}
**{{ edu.degree_zh }}**  
*{{ edu.period_zh }}*
{% for highlight in edu.highlights %}
- {{ highlight.zh }}
{% endfor %}

{% endfor %}

## 专业技能

{% for skill in home.skills %}
- {{ skill.zh }}
{% endfor %}

## 科研经历

{% for exp in home.research %}
### {{ exp.title_zh }}
**{{ exp.role_zh }}** | {{ exp.location_zh }}  
*{{ exp.period_zh }}*
{% for bullet in exp.bullets %}
- {{ bullet.zh }}
{% endfor %}

{% endfor %}

## 实习经历

{% for intern in home.internships %}
### {{ intern.company_zh }}
**{{ intern.role_zh }}** | {{ intern.location_zh }}  
*{{ intern.period_zh }}*
{% for bullet in intern.bullets %}
- {{ bullet.zh }}
{% endfor %}

{% endfor %}

## 项目经历

{% for project in home.projects %}
### [{{ project.name_zh }}]({{ project.link }})
**{{ project.role_zh }}** | {{ project.location_zh }}  
*{{ project.period_zh }}*
{% for bullet in project.bullets %}
- {{ bullet.zh }}
{% endfor %}

{% endfor %}

## 荣誉与奖项

### 国际级
{% for award in home.honors.international %}
- **{{ award.year }}**：{{ award.item_zh }}
{% endfor %}

### 国内级
{% for award in home.honors.domestic %}
- **{{ award.year }}**：{{ award.item_zh }}
{% endfor %}
