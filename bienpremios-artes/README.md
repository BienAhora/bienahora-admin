# Artes BienPremios 2026 — traspaso

Todo lo necesario para seguir haciendo las artes de BienPremios 2026 (décima edición):
las fuentes del diseño, las fotos recortadas, los scripts para sacar los PNG y las
entregas ya aprobadas. Esta carpeta **no se publica** en admin.bienahora.com
(está en `.vercelignore`, porque trae fotos de nominados).

- **Canvas de diseño (Claude Design):** https://claude.ai/artifact/G9ez7ru29zKZmqXdJrBZ8p
  — es la versión viva; `canvas/project/` es la copia de sus fuentes.
- **Artes promocionales originales (Drive):** https://drive.google.com/drive/u/2/folders/1F9Vp95u7lcERG71i0H6Tl66qBcLl9K8p

## Qué hay aquí

| Carpeta | Qué es |
|---|---|
| `canvas/project/` | Fuentes `.dc.html` de cada tablero y `canvas.json` (orden y páginas del canvas). |
| `canvas/up*/` | Archivos que se subieron al canvas (recortes, logos, fotos). `up6/` son las fotos de las promos a lo ancho completo. |
| `render/_blob/` | Los mismos archivos con el id que usa el canvas (`/_blob/<id>`), para renderizar aquí. |
| `recortes/` | Recortes de los nominados de ejemplo, hechos con BiRefNet-portrait (el mejor resultado). |
| `tools/` | Scripts: renderizar, recortar, exportar con los nombres de entrega. |
| `entregas/` | PNG finales de 1080 px: las 13 promos (post 4:5 e historia 9:16) y los 5 ejemplos de F2. |

## Tableros

- **F2 · Portada con eco** (`F2-PortadaEco` historia 9:16, `F2-Post` post 4:5): la dirección
  elegida para los nominados. Una plantilla por etapa: Nominado → Nominado oficial →
  Semifinalista → Finalista → Ganador.
- **Promo-Nominaciones** (post 4:5) y **Promo-Historias** (9:16): las 13 artes para
  promocionar las nominaciones (FOMO-01 a FOMO-11, V1 Especialistas, V1 Marcas).
- Los demás tableros (Ronda 1, F, G, E) son propuestas anteriores, ya descartadas.

## Reglas acordadas (no cambiar sin preguntar)

- Es la **décima edición** (los 10 años se celebraron el año pasado). El nombre es
  **BienPremios 2026**, aunque la gala sea en abril de 2027; las fechas reales de 2027 se quedan.
- Títulos neutros, uno solo para todos: **Nominado, Nominado oficial, Semifinalista,
  Finalista, Ganador** (la app no tiene que adivinar el género).
- Cada arte se siente como un triunfo: nada de "etapa 2 de 5". Que brille la persona;
  minimalista con detalles "wow".
- La **X** de décima edición va junto al logo y como marca de agua. **No** dentro de los
  laureles: el sello lleva el corazón, "2026" y "DÉCIMA EDICIÓN".
- Logo integrado al fondo (nada de placa negra). Nada de aros en órbita. Las sombras metálicas
  ("eco") se notan, pero discretas.
- Promos: sin partículas tipo nieve (con el rojo parecía Navidad). Las fotos van a lo ancho
  completo, sin cortar gente en las orillas; la franja de arriba la llena la misma foto
  desenfocada. Cada foto tiene su propio aclarado (`br`), porque unas venían oscuras y otras no.
- Copy promo. Especialistas: "Nomina a tu Especialista Wellness favorito" · BIENPREMIOS.COM ·
  CIERRAN EL 25 DE OCTUBRE. Marcas: "Postula tu marca wellness de productos o servicios" ·
  BIENPREMIOS.COM/MARCAS · CIERRAN EL 25 DE OCTUBRE · EXPOSITORES BIENFEST: HASTA EL 30 DE
  NOVIEMBRE (según las bases oficiales de bienpremios.com/bases).
- Liga personal de cada nominado: `bienpremios.com/@handle` (su usuario de Instagram); si no
  tiene, su nombre con guiones.

## Cómo sacar los PNG

```bash
cd bienpremios-artes
pip install pillow fonttools brotli            # + rembg[cpu] para recortar
npm i -g playwright                            # el navegador ya viene en las sesiones en la nube
python3 tools/build_page.py canvas/project/Promo-Historias.dc.html render/promoh.html
(cd render && python3 -m http.server 8790 &)
export PW=$(npm root -g)/playwright
node tools/shoot3.js http://localhost:8790/promoh.html salida_h BP2026_Historia_FOMO-01_Especialistas ...
python3 tools/export.py salida_h "entregas/Artes Nominaciones BP 2026 etapa nominados - Historia 9x16"
```

- `build_page.py` convierte un `.dc.html` en una página normal que el navegador arma solo.
- `shoot.js` (F2 historias, 1x), `shoot2.js` (posts 4:5, 2x), `shoot3.js` (historias 9:16 de las
  promos, 2x): toman una foto de cada pieza, en orden, con los nombres que les pases.
- `cut.py <origen> <destino> birefnet-portrait`: recorta el fondo (de uno en uno; en lote se
  queda sin memoria).
- `match.py`: busca en las fotos de bienfest-web la foto original de un arte (para recuperar
  fotos completas).

Si cambias un tablero, súbelo también al canvas para que la versión viva no se quede atrás.

## Pendiente

1. **App para el equipo:** subir varias fotos (o un folder de Drive) con su liga de
   Instagram y que salgan las artes de F2 en lote.
2. **App para cada nominado:** sube su foto y descarga su arte.
   Recomendación: recorte con BiRefNet en Replicate o fal.ai (mejor que Higgsfield para
   recortar); Higgsfield sólo para mejorar la resolución. Falta decidir:
   - dónde vive cada app (este repo / admin.bienahora.com es la opción natural);
   - Replicate o fal.ai;
   - qué dominios abrir en la red de las sesiones.
3. Conseguir los usuarios de Instagram de los nominados de ejemplo.
