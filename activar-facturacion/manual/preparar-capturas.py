"""Recorta, tapa datos personales y marca cada captura del manual.

Coordenadas en píxeles del archivo original (captura a escala 2x).
mask = rectángulos que se tapan; mark = recuadros rojos sobre lo que se toca;
label = (x, y, texto) junto a una marca.
"""
import os

from PIL import Image, ImageDraw, ImageFilter, ImageFont

# Carpeta con las capturas originales (sin tapar), fuera del repo.
BASE = os.environ.get("CAPTURAS_ORIGINALES", "capturas-originales")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "capturas")
ROJO = (227, 38, 47)
GRIS = (90, 90, 96)
FUENTE = ImageFont.truetype(os.environ.get("FUENTE", "/System/Library/Fonts/Helvetica.ttc"), 34)

# Nombre del usuario y de la empresa en la cabecera de «Asignación de opciones».
CAB_OPCIONES = (930, 343, 1555, 385)

PASOS = {
    # --- SUNAT ---
    "s01-ingreso": dict(src="sol/03-sol-ingreso.png"),
    "s02-menu-secundarios": dict(
        src="sol/06-sol-admin-secundarios.png", mask=[(366, 660, 1194, 890), (1466, 660, 1932, 890), (366, 1098, 1208, 1246)],
        mark=[(20, 452, 188, 498)]),
    "s03-crear-secundario": dict(
        src="sol/07-sol-crear-secundario-vacio.png", mark=[(415, 578, 832, 712), (26, 786, 142, 820)],
        label=[(850, 600, "Usuario: FINANGHE · Clave: la escribes tú")]),
    "s04-programas-see": dict(
        src="sol/11-sol-see-servicio-envio.png", mask=[CAB_OPCIONES],
        mark=[(425, 878, 952, 1022), (1042, 586, 1932, 736)]),
    "s05-programas-factura": dict(
        src="sol/17-sol-fe-4-tercerizacion-pse.png", mask=[CAB_OPCIONES],
        mark=[(425, 688, 900, 1022), (1042, 586, 1932, 660), (238, 1222, 352, 1262)]),
    "s06-buscar-api": dict(
        src="sol/21-sol-buscar-api.png", mark=[(628, 266, 1912, 370), (1500, 698, 1875, 780)]),
    "s07-registrar-api": dict(
        src="sol/22-sol-api-registre-aplicacion.png", mask=[(720, 572, 2000, 632, (233, 236, 239)), (720, 744, 2000, 804, (233, 236, 239))],
        mark=[(708, 560, 2012, 644), (708, 732, 2012, 816), (708, 1044, 990, 1114)],
        label=[(1300, 520, "Finangher"), (1300, 692, "https://finangher.com")]),
    "s08-buscar-certificado": dict(
        src="sol/23-sol-buscar-certificado.png", mark=[(628, 266, 1912, 370), (776, 848, 1120, 928)]),
    "s09-solicitar-cdt": dict(
        src="sol/25-sol-cdt-acepto.png", mask=[(1392, 799, 1926, 863), (1392, 897, 1926, 961), (1392, 995, 1926, 1059), (1392, 1093, 1926, 1157)],
        mark=[(786, 1436, 1272, 1482)]),
    "s10-alta-servicio": dict(
        src="sol/28-sol-altas-bajas-pse-tabla.png", mark=[(622, 984, 824, 1036)]),
    "s11-alta-servicio-ruc": dict(
        src="sol/30-sol-alta-servicio-ruc-intai.png", crop=(900, 640, 1820, 1060),
        mark=[(1068, 794, 1312, 842), (1256, 886, 1430, 932), (1530, 948, 1648, 996)],
        label=[(1360, 748, "20602186793 y «..»")]),
    # --- Finangher (versión clara) ---
    # Configuración › Facturación al inicio de cada paso, marcando solo su fila.
    "f01a-config-usuario-sol": dict(
        src="fin/f01-configuracion.png", mask=[(988, 290, 2000, 368), (30, 1550, 380, 1605)],
        mark=[(896, 722, 2178, 822)]),
    "f01b-config-api": dict(
        src="fin/f01-configuracion.png", mask=[(988, 290, 2000, 368), (30, 1550, 380, 1605)],
        mark=[(896, 822, 2178, 926)]),
    "f01c-config-firma": dict(
        src="fin/f01-configuracion.png", mask=[(988, 290, 2000, 368), (30, 1550, 380, 1605)],
        mark=[(896, 926, 2178, 1026)]),
    "f01d-config-sin-sunat": dict(
        src="fin/f01-configuracion.png", mask=[(988, 290, 2000, 368), (30, 1550, 380, 1605)],
        mark=[(896, 1098, 2178, 1396), (896, 1466, 2178, 1674)]),
    "f02-regimen": dict(src="fin/f02-regimen.png"),
    "f09-configuracion-logo": dict(
        src="fin/f09-configuracion-logo.png",
        mask=[(1072, 486, 1338, 534), (30, 1550, 380, 1605)],
        mark=[(924, 410, 1050, 536), (1068, 548, 2156, 676)],
        label=[(540, 440, "Tu logo"), (1500, 690, "Tu dirección fiscal")]),
    "f10-afectacion-igv": dict(
        src="fin/f10-afectacion-igv.png", mark=[(1710, 326, 2516, 1590)]),
    "f11-comprobantes": dict(
        src="fin/f11-comprobantes.png", mark=[(1710, 246, 2516, 666)]),
    "f03-usuario-sol": dict(
        src="fin/f03-usuario-sol.png",
        mark=[(1710, 284, 2516, 404), (1710, 468, 2516, 588)]),
    "f04-credenciales-api": dict(
        src="fin/f04-credenciales-api.png",
        mark=[(1710, 300, 2516, 420), (1710, 468, 2516, 588)],
        label=[(1960, 262, "= ID de SUNAT"), (1980, 430, "= CLAVE de SUNAT")]),
    "f05-subir-certificado": dict(
        src="fin/f05-subir-certificado.png",
        mark=[(1798, 320, 2490, 438), (1798, 560, 2490, 678), (1798, 704, 2490, 824)]),
    "f06-no-tengo-certificado": dict(
        src="fin/f06-no-tengo-certificado.png",
        mark=[(1798, 540, 2490, 670), (1798, 948, 2490, 1066)]),
    "f07-codigo-para-facturar": dict(
        src="fin/f07-codigo-para-facturar.png",
        mark=[(1790, 448, 2490, 566)]),
    "f08-listo-para-emitir": dict(
        src="fin/f08-listo-para-emitir.png", mask=[(988, 290, 2000, 368), (30, 1550, 380, 1605)],
        mark=[(896, 924, 2178, 1026)]),
}


def preparar(nombre, src, crop=None, mask=(), mark=(), label=()):
    im = Image.open(os.path.join(BASE, src)).convert("RGB")
    # Las capturas claras de Finangher quedaron a 1x: se suben a 2x para usar
    # las mismas coordenadas que el resto.
    if im.width < 1500:
        im = im.resize((im.width * 2, im.height * 2), Image.LANCZOS)
    # Datos personales: difuminado (se nota que hay un dato, no se lee). Con
    # color explícito, se rellena (campos con valores viejos que confunden).
    for r in mask:
        caja = tuple(r[:4])
        if len(r) > 4:
            ImageDraw.Draw(im).rectangle(caja, fill=r[4])
        else:
            zona = im.crop(caja)
            chica = zona.resize((max(1, zona.width // 14), max(1, zona.height // 14)))
            zona = chica.resize(zona.size).filter(ImageFilter.GaussianBlur(10))
            im.paste(zona, caja[:2])
    d = ImageDraw.Draw(im)
    for r in mark:
        d.rounded_rectangle(r, radius=14, outline=ROJO, width=7)
    for x, y, t in label:
        w = d.textlength(t, font=FUENTE)
        d.rounded_rectangle((x - 10, y - 6, x + w + 10, y + 40), radius=8, fill=ROJO)
        d.text((x, y), t, fill="white", font=FUENTE)
    if crop:
        im = im.crop(crop)
    im.save(os.path.join(OUT, nombre + ".png"), optimize=True)


os.makedirs(OUT, exist_ok=True)
for nombre, cfg in PASOS.items():
    preparar(nombre, **cfg)
    print("ok", nombre)
