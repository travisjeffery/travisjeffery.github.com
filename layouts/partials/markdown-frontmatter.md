{{- $title := .Title -}}
{{- if .IsHome -}}
  {{- $title = .Site.Title -}}
{{- end -}}
{{- $date := .Date -}}
{{- if $date.IsZero -}}
  {{- $candidate := (where .Pages "Section" "posts").ByDate.Reverse -}}
  {{- if eq (len $candidate) 0 -}}
    {{- $candidate = .Pages.ByDate.Reverse -}}
  {{- end -}}
  {{- if eq (len $candidate) 0 -}}
    {{- $candidate = (where .Site.RegularPages "Section" "posts").ByDate.Reverse -}}
  {{- end -}}
  {{- with index $candidate 0 -}}
    {{- $date = .Date -}}
  {{- end -}}
{{- end -}}
{{- $canonicalURL := .Permalink -}}
{{- with .OutputFormats.Get "html" -}}
  {{- $canonicalURL = .Permalink -}}
{{- end -}}
{{- $tags := slice -}}
{{- range .Params.tags -}}
  {{- $t := strings.TrimSpace (printf "%v" .) -}}
  {{- if $t -}}
    {{- $tags = $tags | append $t -}}
  {{- end -}}
{{- end -}}
---
title: {{ $title | jsonify }}
{{- if not $date.IsZero }}
date: {{ $date.Format "2006-01-02" }}
{{- end }}
url: {{ $canonicalURL | jsonify }}
{{- if .IsHome }}
description: {{ .Site.Params.description | jsonify }}
{{- end }}
{{- with .Params.externalURL }}
external_url: {{ . | jsonify }}
{{- end }}
{{- if $tags }}
tags: [{{ range $i, $t := $tags }}{{ if $i }}, {{ end }}{{ $t | jsonify }}{{ end }}]
{{- end }}
agent:
  instructions: "Use this search API to find relevant content across this site with keywords or natural-language queries, instead of crawling individual pages. Results are returned in Markdown."
  endpoint: "https://travisjeffery.com/.well-known/search?q={query}"
  method: "GET"
  documentation: "https://developers.cloudflare.com/ai-search/how-to/search-for-agents/"
---
