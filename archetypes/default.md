---
title: "{{ replaceRE "[[:^alpha:]]" " " .Name | humanize }}"
date: {{ .Date }}
slug: "{{ replaceRE "[[:^alpha:]]" "-" .Name | replaceRE "-{2,}" "-" | replaceRE "^-" "" | lower }}"
draft: false
tags: [""]
---

