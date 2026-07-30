---
title: "Kategorilista"
draft: false
---

<html>
<head>
<title>Kategorier</title>
</head>
<body>
<h1>Alla kategorier</h1>
<ul>
{{ range $name, $taxonomy := .Site.Taxonomies.kategorier }}
  <li>{{ $name }} ({{ len $taxonomy }})</li>
{{ else }}
  <li>Inga kategorier registrerade</li>
{{ end }}
</ul>
</body>
</html>
