---
title: "Kategorier - test"
draft: false
---

## Lista på inlägg i 'kategorier'

{{ range (where .Site.RegularPages "Params.kategorier" "intersect" (slice "testkateg")) }}
- [{{ .Title }}]({{ .RelPermalink }})
{{ else }}
Inga inlägg hittades för taxonomin.
{{ end }}
