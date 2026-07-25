# Edge Functions — respaldo con control de versiones

Proyecto Supabase: `wcijfoaawfuqnxhqolpz` · Funciones: **113** · Último respaldo: 2026-07-25T17:08:07.819Z

## Qué es esto
Copia versionada del código de todas las Edge Functions. Se actualiza **cada hora** (cron `fn-backup-git`) y solo commitea lo que cambió, así que el historial de git muestra **qué cambió, cuándo y en qué función**.

## Importante
- **Es respaldo, no origen del deploy.** Editar aquí NO despliega nada.
- `manifest.json` guarda el estado de cada función, incluido **verify_jwt**.

## Funciones PÚBLICAS (verify_jwt = false) — 86
Las llaman webhooks externos o el pixel del sitio. **Si alguna amanece con verify_jwt=true, se rompe** (pasó con `bhx`: tumbó el tracking del sitio un día). Al redeployar por API, Supabase la pone en true por defecto — hay que apagarla de nuevo en el panel.

- `admin-accesos`
- `agenda-backfill`
- `api-health`
- `aprecio-guardar`
- `archivo-load`
- `backfill-contacts`
- `bf-expositor`
- `bhx`
- `biencal-admin`
- `biencal-email`
- `build-css`
- `build-legacy`
- `calendly-sync`
- `calendly-webhook`
- `candidato-accion`
- `comisiones`
- `compra-intake`
- `contacts-fresh`
- `cp-load`
- `cultura-guardar`
- `enagic-load`
- `evaluacion-guardar`
- `ga-pages-sync`
- `ga-query`
- `ga-sync`
- `get-csf`
- `gh-commit`
- `gh-deploy`
- `gh-puttree`
- `goto-call`
- `goto-hook`
- `goto-oauth`
- `goto-rec-hook`
- `goto-recording`
- `goto-rectest`
- `gsc-lookup`
- `gsc-pages-sync`
- `gsc-sync`
- `health-alert`
- `historia-backfill`
- `historia-mass`
- `lead-intake`
- `log-acceso`
- `mbti-guardar`
- `meta-adclone`
- `meta-adlinks`
- `meta-audiences`
- `meta-hist`
- `meta-lal-value`
- `meta-names`
- `meta-urltags`
- `ontraport-push`
- `ontraport-tags-dict`
- `ontraport-tracking`
- `op-dedup`
- `op-dedup-merge`
- `op-field-audit`
- `op-fields`
- `op-meta`
- `op-meta-temp`
- `op-prune`
- `op-push-score`
- `op-retag`
- `op-verify`
- `outbox-worker`
- `perfil-guardar`
- `push-conversions`
- `recordatorios`
- `referidos-push`
- `report360`
- `resolve-booking`
- `rh-empleado`
- `rh-import`
- `rh-panel`
- `rrhh-reintegrate`
- `seg-note`
- `ses-webhook`
- `stripe-list`
- `sync-llamar`
- `track`
- `ui-prefs`
- `verifica`
- `wa-assign`
- `whatsapp-fichaje`
- `whatsapp-inbound`
- `yt-sync`

## Restaurar una función
1. Abrir `supabase-functions/functions/<slug>/index.ts` en la versión de git deseada.
2. Copiar el código (sin el encabezado de comentarios).
3. Redeployar en Supabase y **verificar verify_jwt contra manifest.json**.
