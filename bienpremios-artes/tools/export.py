"""Exporta los renders a 2x a PNG de 1080 px con los nombres de entrega.

Uso: python3 tools/export.py <carpeta_render> <carpeta_destino>
  BP2026_Promo_FOMO-03_Especialistas.png -> Artes Nominaciones BP 2026 etapa nominados FOMO-03.png
  BP2026_Promo_V1_Especialistas.png      -> V1 Especialistas.png
"""
import glob, os, re, sys
from PIL import Image

src, dst = sys.argv[1], sys.argv[2]
os.makedirs(dst, exist_ok=True)
for f in sorted(glob.glob(os.path.join(src, '*.png'))):
    b = os.path.basename(f)
    m = re.search(r'(FOMO-\d\d)', b)
    if m:
        nombre = f'Artes Nominaciones BP 2026 etapa nominados {m.group(1)}.png'
    else:
        nombre = 'V1 Especialistas.png' if 'V1_Esp' in b else 'V1 Marcas.png'
    im = Image.open(f).convert('RGB')
    im.resize((1080, im.height * 1080 // im.width), Image.LANCZOS).save(os.path.join(dst, nombre), optimize=True)
    print(nombre)
