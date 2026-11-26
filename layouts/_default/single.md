{{ partial "markdown-frontmatter.md" . }}
# {{ .Title }}
{{- if .Params.externalURL }}

Originally published at [{{ .Params.externalURL }}]({{ .Params.externalURL }}).
{{- end -}}
{{- $isOrg := false -}}
{{- with .File -}}
  {{- if eq .Ext "org" -}}
    {{- $isOrg = true -}}
  {{- end -}}
{{- end -}}
{{- if $isOrg }}

<!-- HUGO_ORG_HTML_START -->
{{ .Content }}
<!-- HUGO_ORG_HTML_END -->
{{- else -}}
  {{- $raw := strings.Trim .RawContent "\r\n" -}}
  {{- if strings.TrimSpace $raw }}

{{ $raw }}
  {{- end -}}
{{- end }}

