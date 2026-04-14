---
permalink: /
title: "Yun Hong"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% assign home = site.data.homepage %}

{{ home.intro.en }}

## Education

{% for edu in home.education %}
### {{ edu.institution_en }} | {{ edu.location_en }}
**{{ edu.degree_en }}**  
*{{ edu.period_en }}*
{% for highlight in edu.highlights %}
- {{ highlight.en }}
{% endfor %}

{% endfor %}

## Research Experience

{% for exp in home.research %}
### {{ exp.title_en }}
**{{ exp.role_en }}** | {{ exp.location_en }}  
*{{ exp.period_en }}*
{% for bullet in exp.bullets %}
- {{ bullet.en }}
{% endfor %}

{% endfor %}

## Internship Experience

{% for intern in home.internships %}
### {{ intern.company_en }}
**{{ intern.role_en }}** | {{ intern.location_en }}  
*{{ intern.period_en }}*
{% for bullet in intern.bullets %}
- {{ bullet.en }}
{% endfor %}

{% endfor %}

## Project Experience

{% for project in home.projects %}
### [{{ project.name_en }}]({{ project.link }})
**{{ project.role_en }}** | {{ project.location_en }}  
*{{ project.period_en }}*
{% for bullet in project.bullets %}
- {{ bullet.en }}
{% endfor %}

{% endfor %}

## Skills

{% for skill in home.skills %}
{% if skill.en contains ':' %}
{% assign skill_parts = skill.en | split: ':' %}
- **{{ skill_parts[0] }}:**{{ skill.en | remove_first: skill_parts[0] | remove_first: ':' }}
{% else %}
- {{ skill.en }}
{% endif %}
{% endfor %}

## Honors and Awards

### International
{% for award in home.honors.international %}
- **{{ award.year }}**: {{ award.item_en }}
{% endfor %}

### Domestic
{% for award in home.honors.domestic %}
- **{{ award.year }}**: {{ award.item_en }}
{% endfor %}
