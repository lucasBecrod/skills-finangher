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
ROJO_NUMERO = (240, 0, 0)
GRIS = (90, 90, 96)
FUENTE = ImageFont.truetype(os.environ.get("FUENTE", "/System/Library/Fonts/Helvetica.ttc"), 34)

# Nombre del usuario y de la empresa en la cabecera de «Asignación de opciones».
CAB_OPCIONES = (930, 343, 1555, 385)

PASOS = {
    # --- SUNAT ---
    "s01-ingreso": dict(src="sol/03-sol-ingreso.png"),
    # Técnica de la guía de Facturita: números sobre la misma pantalla.
    "s02-menu-secundarios": dict(
        src="sol/06-sol-admin-secundarios.png", mask=[(366, 660, 1194, 890), (1466, 660, 1932, 890), (366, 1098, 1208, 1246)],
        mark=[(1180, 132, 1702, 222, 1, "i"), (20, 452, 188, 498, 2)],
        label=[(460, 156, "Clic aquí › Usuarios secundarios"),
               (300, 456, "Crear Usuario")]),
    # «Bienvenido» ya se marcó en la pantalla anterior: aquí no se repite.
    "s03-crear-secundario": dict(
        src="sol/07-sol-crear-secundario-vacio.png",
        mark=[(416, 382, 832, 460, 1),
              (416, 580, 832, 622, 2), (416, 620, 772, 666, 3), (416, 664, 772, 710, 4),
              (26, 786, 142, 820, 5)],
        label=[(945, 400, "Elige DNI y escribe el DNI de quien configura"),
               (945, 582, "FINANGHE"), (885, 664, "Tu clave, 2 veces: 10 a 12 letras y números")]),
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
        # Desktop/Web y Guardar quedan más abajo en la misma pantalla: se dibujan.
        debajo="api-desktop-guardar",
        mark=[(1922, 376, 2006, 460), (708, 560, 2012, 644, 1), (708, 732, 2012, 816, 2),
              (708, 1044, 990, 1114, 3, "i"), (700, 1610, 1090, 1680, 4, "i"),
              (712, 1704, 962, 1778, 5, "i")],
        label=[(1300, 520, "Finangher"), (1300, 692, "https://finangher.com"),
               (1230, 400, "¿Ya tienes una? Primero el lápiz"),
               (1130, 1626, "Desktop, no Web")]),
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
        src="fin/f10-afectacion-igv.png",
        mark=[(1714, 328, 2512, 474, 1), (1714, 734, 2512, 942, 2)],
        label=[(1150, 380, "Fuera de la Amazonía"), (1260, 816, "En la Amazonía")]),
    "f11-comprobantes": dict(
        src="fin/f11-comprobantes.png", mark=[(1710, 246, 2516, 666)]),
    "f03-usuario-sol": dict(
        src="fin/f03-usuario-sol.png",
        mark=[(1710, 284, 2516, 404), (1710, 468, 2516, 588)]),
    "f04-credenciales-api": dict(
        src="fin/f04-credenciales-api.png",
        # Los nombres nuevos del formulario (rama fix/credenciales-api-id-clave).
        texto=[(1712, 256, 1880, 298, "ID"), (1744, 336, 2060, 388, "El ID que te muestra SUNAT"),
               (1712, 424, 1900, 466, "Clave"), (1744, 504, 2100, 556, "La clave que te muestra SUNAT")],
        mark=[(1710, 300, 2516, 420, 1), (1710, 468, 2516, 588, 2), (1710, 710, 2516, 826, 3)]),
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


FUENTE_UI = ImageFont.truetype(os.environ.get("FUENTE", "/System/Library/Fonts/Helvetica.ttc"), 26)


def dibujar_api_desktop_guardar(im):
    """Agrega debajo de «Registre su aplicación» lo que la captura no alcanzó:
    tipo de aplicación (Desktop / Web) y los botones Guardar y Cancelar."""
    alto_extra = 360
    nueva = Image.new("RGB", (im.width, im.height + alto_extra), "white")
    nueva.paste(im, (0, 0))
    d = ImageDraw.Draw(nueva)
    y0 = im.height
    d.rectangle((670, y0, 2048, y0 + alto_extra - 20), fill="white", outline=(200, 210, 222), width=2)
    d.text((712, y0 + 24), "(más abajo, en la misma pantalla)", fill=(120, 120, 128), font=FUENTE_UI)
    d.text((712, y0 + 76), "Tipo de aplicación:", fill=(30, 30, 30), font=FUENTE)
    for i, (texto, elegido) in enumerate((("Desktop", True), ("Web", False))):
        cx, cy = 744 + i * 220, y0 + 160
        d.ellipse((cx - 16, cy - 16, cx + 16, cy + 16), outline=(90, 90, 96), width=3)
        if elegido:
            d.ellipse((cx - 8, cy - 8, cx + 8, cy + 8), fill=(13, 110, 253))
        d.text((cx + 28, cy - 18), texto, fill=(30, 30, 30), font=FUENTE)
    for i, texto in enumerate(("Guardar", "Cancelar")):
        x = 722 + i * 270
        d.rounded_rectangle((x, y0 + 228, x + 230, y0 + 290), radius=6,
                            fill=(13, 110, 253) if i == 0 else (240, 240, 240),
                            outline=(200, 200, 200))
        w = d.textlength(texto, font=FUENTE)
        d.text((x + (230 - w) / 2, y0 + 240), texto, fill="white" if i == 0 else (30, 30, 30), font=FUENTE)
    return nueva


DEBAJO = {"api-desktop-guardar": dibujar_api_desktop_guardar}


def preparar(nombre, src, crop=None, mask=(), mark=(), label=(), texto=(), debajo=None):
    im = Image.open(os.path.join(BASE, src)).convert("RGB")
    # Las capturas claras de Finangher quedaron a 1x: se suben a 2x para usar
    # las mismas coordenadas que el resto.
    if im.width < 1500:
        im = im.resize((im.width * 2, im.height * 2), Image.LANCZOS)
    if debajo:
        im = DEBAJO[debajo](im)
    # texto = (x0, y0, x1, y1, nuevo): reemplaza un texto de la pantalla por su
    # versión vigente, con el color de fondo y de letra de la propia captura.
    for x0, y0, x1, y1, nuevo in texto:
        fondo = im.getpixel((x1 - 4, y0 + 4))
        tinta = min((im.getpixel((x, (y0 + y1) // 2)) for x in range(x0, x1)), key=sum)
        ImageDraw.Draw(im).rectangle((x0, y0, x1, y1), fill=fondo)
        ImageDraw.Draw(im).text((x0 + 2, y0 + 6), nuevo, fill=tinta, font=FUENTE_UI)
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
    # mark = (x0, y0, x1, y1) o (x0, y0, x1, y1, número): con número se dibuja
    # un círculo rojo numerado a la izquierda del recuadro, como en la guía de Facturita.
    for r in mark:
        d.rounded_rectangle(r[:4], radius=14, outline=ROJO, width=7)
        if len(r) > 4:
            # A la derecha del recuadro, separado, para no tapar nada; a la
            # izquierda solo si no cabe en la imagen.
            rad, sep = 28, 22
            cy = (r[1] + r[3]) // 2
            cx = r[2] + sep + rad
            if cx + rad > im.width or (len(r) > 5 and r[5] == "i"):
                cx = r[0] - sep - rad
            d.ellipse((cx - rad, cy - rad, cx + rad, cy + rad), fill=ROJO_NUMERO,
                      outline="white", width=4)
            n = str(r[4])
            w = d.textlength(n, font=FUENTE)
            d.text((cx - w / 2, cy - 20), n, fill="white", font=FUENTE)
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
