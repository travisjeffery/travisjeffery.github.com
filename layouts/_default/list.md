{{ partial "markdown-frontmatter.md" . }}
# {{ .Title }}
{{ range .Pages.ByDate.Reverse }}
{{- $md := .OutputFormats.Get "markdown" -}}
{{- if .Params.externalURL }}
- [{{ .Title }}]({{ .Params.externalURL }}){{ if not .Date.IsZero }} ({{ .Date.Format "2006-01-02" }}){{ end }}{{ with $md }} — [Markdown]({{ .Permalink }}){{ end }}
{{- else if $md }}
- [{{ .Title }}]({{ $md.Permalink }}){{ if not .Date.IsZero }} ({{ .Date.Format "2006-01-02" }}){{ end }}
{{- else }}
- [{{ .Title }}]({{ .Permalink }}){{ if not .Date.IsZero }} ({{ .Date.Format "2006-01-02" }}){{ end }}
{{- end }}
{{- end }}
