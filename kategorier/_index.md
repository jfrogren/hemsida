---
title: "Kategorier"
draft: false
---

Antal kategorier: {{ len .Site.Taxonomies.kategorier }}

{{ range $name, $taxonomy := .Site.Taxonomies.kategorier }}
**Kategori:** {{ $name }} innehåller {{ len $taxonomy }} inlägg.
{{ end }}

Om inget syns, betyder det att Hugo inte hittar några kategorier alls.
