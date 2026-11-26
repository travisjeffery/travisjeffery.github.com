{{ partial "markdown-frontmatter.md" . }}
# {{ .Site.Title }}

{{ .Site.Params.description }}

I'm an infrastructure engineer and the author of [Distributed Services with Go](https://pragprog.com/titles/tjgo/distributed-services-with-go/), which teaches distributed systems by building a persistent event-stream service from scratch to production.

- GitHub: [https://github.com/travisjeffery](https://github.com/travisjeffery)
- Twitter: [https://twitter.com/travisjeffery](https://twitter.com/travisjeffery)
- Email: [tj@travisjeffery.com](mailto:tj@travisjeffery.com)
- LLMs Index: [{{ "llms.txt" | absURL }}]({{ "llms.txt" | absURL }})

## Posts
{{ range (where .Site.RegularPages "Section" "posts").ByDate.Reverse }}
{{- $md := .OutputFormats.Get "markdown" -}}
{{- if .Params.externalURL }}
- [{{ .Title }}]({{ .Params.externalURL }}) ({{ .Date.Format "2006-01-02" }}){{ with $md }} — [Markdown]({{ .Permalink }}){{ end }}
{{- else if $md }}
- [{{ .Title }}]({{ $md.Permalink }}) ({{ .Date.Format "2006-01-02" }})
{{- else }}
- [{{ .Title }}]({{ .Permalink }}) ({{ .Date.Format "2006-01-02" }})
{{- end }}
{{- end }}
