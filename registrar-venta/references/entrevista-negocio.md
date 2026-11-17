# Conocer el negocio

Se hace una sola vez y solo cubre la capa del **negocio**: lo que no cambia de
una venta a otra. Qué se vende, a quién, con qué comprobante y cómo paga son
datos de cada operación y **no van aquí**.

**Primero leer, después preguntar.** El dueño ya configuró su negocio en
Finangher; hacerle repetir lo que el sistema muestra es hacerle perder tiempo,
y además el sistema es el que está al día.

## Lo que se lee de Finangher

| Dato | Dónde se lee |
|---|---|
| Nombre de la tienda, tal como lo escribe el dueño | Encabezado del punto de venta |
| Enlace de la tienda | La dirección del navegador: `finangher.com/marketplace/<enlace>` |
| Medios y cuentas de cobro | Los botones de pago del punto de venta. **No se guardan en la ficha**: se leen en cada venta, porque pueden cambiar |
| WhatsApp del negocio | El número de contacto de la tienda en Finangher. Si no está, preguntarlo una vez y pedir al dueño que lo guarde en Finangher |
| Razón social, RUC y representante legal | Los datos del negocio en Finangher y el encabezado del comprobante. Sirven para reconocer de quién es una sesión o un perfil |
| Si emite comprobantes | Que el punto de venta ofrezca «Boleta» y «Factura» |
| Tratamiento de IGV | La línea «Impuestos» de la primera venta armada, antes de vender |

## Lo único que se pregunta

1. **Si no hay una pestaña de Finangher abierta:** «¿Cuál es tu tienda en
   Finangher?».
2. **Confirmar el IGV que mostró el sistema**, la primera vez, dentro de la
   confirmación de esa venta: «Finangher calcula tus ventas como exoneradas
   (impuestos S/ 0.00). ¿Es correcto para tu negocio?». Si dice que depende del
   producto o del cliente, anotar su regla con sus palabras.

Nada más. Si en una venta aparece algo del negocio que no se puede leer, se
pregunta en ese momento y se anota.

## Formato de la ficha

```markdown
# Ficha del negocio — <nombre tal como lo escribe el dueño>
Actualizada: <fecha>

- Tienda: <nombre>
- Enlace: finangher.com/marketplace/<enlace>
- IGV: con IGV | exonerado | mixto → <regla en palabras del dueño>
  (confirmado por el dueño el <fecha>)

## Lo que el dueño fue aclarando sobre su negocio
- <fecha> · <caso> → <decisión>
```

La ficha guarda poco a propósito. No guarda comprobante ni pago «habitual»,
medios de cobro, claves, certificados ni números de cuenta.
