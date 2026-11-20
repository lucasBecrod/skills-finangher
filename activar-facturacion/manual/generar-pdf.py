"""Genera manual-activar-facturacion.pdf desde el HTML.

Las capturas se reducen a JPEG RGB (2000 px, calidad 85) en una copia temporal
y Chromium las incrusta tal cual. No recomprimir el PDF con Ghostscript: deja
perfiles ICC vacíos y Vista Previa muestra las imágenes en blanco.

Uso (necesita Pillow y el paquete playwright de Node):
    NODE_PATH=<carpeta con node_modules/playwright> python3 generar-pdf.py
"""
import os
import re
import shutil
import subprocess
import tempfile

from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.join(AQUI, "manual-activar-facturacion.pdf")

IMPRIMIR = """
const { chromium } = require('playwright');
(async () => {
  const [,, src, out] = process.argv;
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + src, { waitUntil: 'networkidle' });
  await p.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
"""


def main():
    tmp = tempfile.mkdtemp(prefix="manual-")
    try:
        os.makedirs(os.path.join(tmp, "capturas"))
        shutil.copytree(os.path.join(AQUI, "assets"), os.path.join(tmp, "assets"))
        for f in sorted(os.listdir(os.path.join(AQUI, "capturas"))):
            if not f.endswith(".png"):
                continue
            im = Image.open(os.path.join(AQUI, "capturas", f)).convert("RGB")
            if im.width > 2000:
                im = im.resize((2000, round(im.height * 2000 / im.width)), Image.LANCZOS)
            im.save(os.path.join(tmp, "capturas", f[:-4] + ".jpg"), "JPEG", quality=85, optimize=True)

        html = open(os.path.join(AQUI, "manual-activar-facturacion.html")).read()
        html = re.sub(r'(capturas/[^"\'`$]*?)\.png', r"\1.jpg", html)
        html = html.replace('.png"', '.jpg"').replace(".png'", ".jpg'")
        pagina = os.path.join(tmp, "manual.html")
        open(pagina, "w").write(html)

        js = os.path.join(tmp, "imprimir.js")
        open(js, "w").write(IMPRIMIR)
        subprocess.run(["node", js, pagina, SALIDA], check=True)
        print("ok", SALIDA, os.path.getsize(SALIDA) // 1024, "KB")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
