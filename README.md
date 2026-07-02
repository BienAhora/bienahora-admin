# BienAhora — admin.bienahora.com

Sitio estático para páginas administrativas de BienAhora.

## Páginas

- `/verifyip` — página de gracias tras la verificación de IP del bot BienMaría (RRHH).
  Parámetros: `n` (nombre de pila), `s` (`ok` | `dup` | `err`).
  La edge function `verifica` de Supabase registra la IP y redirige aquí.

## Deploy

Vercel (estático, sin build). Dominio: `admin.bienahora.com` (CNAME → `cname.vercel-dns.com`).
