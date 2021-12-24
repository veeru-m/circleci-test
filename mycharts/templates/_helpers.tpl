{{- define "prom-service-name" -}}
{{- if .Values.app.prometheusRule.name -}}
{{- .Values.app.prometheusRule.name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}

{{- define "prom-service-monitor" -}}
{{- if .Values.app.serviceMonitor.name -}}
{{- .Values.app.serviceMonitor.name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}
