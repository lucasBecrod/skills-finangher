# El mensaje de confirmación

Siempre el mismo molde, con los mismos bloques en el mismo orden. El dueño
aprende dónde mirar y nota de inmediato lo que falta o sobra. Pocas palabras:
quien lo lea por primera vez debe entender qué va a pasar y poder decir sí, no
o qué cambiar. No agregar saludos, explicaciones ni bloques nuevos.

Se envía como **mensaje normal de la conversación**, y el dueño responde
escribiendo o dictando. No usar botones, menús de opciones ni formularios para
pedir el sí: el dueño tiene que poder contestar «sí», «no» o un cambio con sus
palabras.

Los datos se copian de la pantalla de Finangher con el carrito ya armado, no
del pedido.

## Molde

```
**<BOLETA | FACTURA | VENTA SIN COMPROBANTE>** de <negocio que emite> para <nombre o razón social> · <DNI|RUC> <número>

| Producto | Cant. | Precio | Importe |
|:---|---:|---:|---:|
| <nombre exacto del catálogo, con variante> | <cant.> | <precio> | <importe> |
| **Impuestos** (<exonerado | IGV 18 % | gratuita | exportación>) | | | <impuestos> |
| **Total** | | | **S/ <total>** |

Precios de catálogo, salvo ✎.

**Pago:** <Yape, al contado | a crédito, vence <fecha> | S/ <x> ahora por <medio>, saldo S/ <y>>
**Opciones:** <ninguna | las que se aparten de lo normal>
**Entrega:** <WhatsApp <número> | te pregunto al emitir>

⚠️ **Observaciones**
- <una línea por cada cosa que el dueño debe mirar antes de decir sí>
(omitir el bloque entero si no hay ninguna)

¿Emito? Responde **sí** o dime el cambio.
```

Sin cliente, la primera línea termina en: `para clientes varios (sin documento)`.

## Reglas de cada bloque

**Primera línea.** Qué comprobante, **de qué negocio** y para quién, juntos: es
lo que no se puede deshacer. El negocio que emite va siempre, aunque el dueño
tenga uno solo: es su oportunidad de notar que la sesión está en otra empresa. El nombre va tal como lo muestra Finangher; si el dueño lo dio por
nombre, aquí ve a quién se encontró.

**Tabla.**

- Productos alineados a la izquierda, números a la derecha, en el orden del
  carrito. Los montos van sin «S/»; solo lo lleva el Total.
- **Impuestos y Total son las dos últimas filas de la misma tabla**, con su
  etiqueta en la columna de productos. Así quedan alineados con los importes y
  no se pierden debajo.
- La fila de Impuestos dice el tratamiento entre paréntesis. Es la línea que
  protege del error de IGV.
- **Precios.** El origen se dice una vez, debajo de la tabla. Solo se marca con
  ✎ el precio que **no** es el del catálogo (lo pidió el dueño o se editó). Si
  ninguno lleva ✎, la línea dice solo «Precios de catálogo.»
- **Hasta 20 ítems:** todos.
- **Más de 20:** solo las filas que el dueño necesita mirar: las marcadas con
  ✎, las que tienen una variante elegida por el skill y las 5 de mayor importe.
  Luego una fila «… y <N> ítems más a precio de catálogo» con su suma, y las
  filas de Impuestos y Total. Debajo: «<N> ítems, <U> unidades en total. Dime
  "lista completa" si quieres verla». Si la pide, enviarla en tablas de 50.
- Una venta larga que viene de una lista del dueño se verifica además por
  **cuadre**: número de ítems, suma de unidades y total deben coincidir con su
  lista. Si no cuadra, va en Observaciones y no se vende.

**Pago.** Una de las tres formas del molde, empezando por el medio. Siempre es
el que dijo el dueño para esta venta; nunca uno asumido.

**Opciones.** Todo lo que se aparta de una venta normal de hoy, en soles, sin
envío. Siempre aparece; si no hay nada, dice «ninguna». Orden fijo:

1. Operación: gratuita · exportación
2. Moneda distinta de soles
3. Fecha distinta de hoy
4. Envío o cita
5. Otros datos que Finangher muestre en el comprobante

**Entrega.** Siempre aparece. Si el dueño ya dio el WhatsApp del cliente, va el
número completo para que lo revise; si no, «te pregunto al emitir». Confirmar la
venta con un número en este bloque autoriza también el envío a ese número.

**⚠️ Observaciones.** Aquí va lo que el dueño debe mirar antes de decir sí. El
triángulo solo aparece cuando hay algo: si la venta es exactamente lo que
pidió, el bloque no existe y el mensaje se ve limpio. Una línea por cosa, sin
adornos:

- Un dato que el dueño no dijo y el skill puso: «Cantidad 1: dijiste "un
  lector"».
- Un precio distinto al del catálogo: «Lector a 65.00; en catálogo está a
  69.00».
- Un contacto elegido entre varios, o un nombre que no era el esperado.
- Un recorrido que el skill no tiene probado.

No usar ⚠️ en ningún otro lugar del mensaje, ni otros emojis.

**Cierre.** Siempre la misma frase.

## Ejemplo con observaciones

```
**BOLETA** de BODEGA EL SOL E.I.R.L. para MARÍA QUISPE HUAMÁN · DNI 40000001

| Producto | Cant. | Precio | Importe |
|:---|---:|---:|---:|
| Lector de DNIe IntelliReader Compatible | 2 | 65.00 ✎ | 130.00 |
| Plan MYPE | 1 | 16.00 | 16.00 |
| **Impuestos** (exonerado) | | | 0.00 |
| **Total** | | | **S/ 146.00** |

Precios de catálogo, salvo ✎.

**Pago:** Yape, al contado
**Opciones:** ninguna
**Entrega:** te pregunto al emitir

⚠️ **Observaciones**
- Lector a 65.00; en catálogo está a 69.00.

¿Emito? Responde **sí** o dime el cambio.
```

## Ejemplo limpio

```
**FACTURA** de BODEGA EL SOL E.I.R.L. para COMERCIAL ANDINA S.A.C. · RUC 20000000001

| Producto | Cant. | Precio | Importe |
|:---|---:|---:|---:|
| Lector de DNIe IntelliReader Compatible | 1 | 69.00 | 69.00 |
| **Impuestos** (exonerado) | | | 0.00 |
| **Total** | | | **S/ 69.00** |

Precios de catálogo.

**Pago:** Yape, al contado
**Opciones:** ninguna
**Entrega:** WhatsApp 900 000 001

¿Emito? Responde **sí** o dime el cambio.
```

## Después de la respuesta

- **Sí** → vender.
- **Un cambio** → hacerlo en el carrito, verificar de nuevo y reenviar el molde
  completo, no solo la línea cambiada.
- **No**, otra cosa o silencio → no vender.
