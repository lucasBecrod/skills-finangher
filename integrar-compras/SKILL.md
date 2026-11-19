---
name: integrar-compras
description: >
  Integrar en Finangher las compras que SUNAT ya informó de tu negocio: trae cada
  factura, asocia cada ítem a un producto tuyo y registra la compra con su pago.
  Usar cuando pidan "registra esta compra", "registra mis compras", "integra las facturas de compra",
  "pon al día mis compras de SUNAT", "qué compras tengo sin registrar", "sube
  esta factura de mi proveedor". No toma fotos ni lee papeles: usa la factura
  electrónica que el proveedor emitió con el RUC del negocio. No emite
  comprobantes ni corrige una compra ya registrada.
---

# /integrar-compras — Tus compras de SUNAT, dentro de tu negocio

Nacido de dos experimentos de noviembre de 2026: un agente integró compras
reales navegando la página Conciliación, primero en un negocio de servicios y
después en una tienda con mercadería, variantes y facturas de más de diez
líneas. Una compra de una línea toma menos de un minuto; una de 11 líneas, unos
25 pasos.

## Para qué tamaño de trabajo sirve

**Las compras de hoy o de la semana, no el año atrasado de una sola vez.** Cada
línea pide buscar, elegir producto y, si tiene, elegir variante. El ritmo que
funciona es integrar lo que llegó en el día: una factura de 40 líneas es un
trabajo razonable; un mes entero se parte por día o por proveedor, con un cierre
después de cada tanda. Si el dueño pide «todo el mes», proponer ese orden antes
de empezar.

## Principio rector

**La factura ya está en SUNAT. No se vuelve a escribir: se trae y se acomoda.**
Cuando un proveedor factura con el RUC del negocio, la compra queda en SUNAT
completa, ítem por ítem. El trabajo no es copiarla; es decidir qué significa en
este negocio: a qué producto corresponde cada ítem y cómo se pagó.

**Registrar una compra mueve el negocio.** Sube el inventario, baja la caja o
crea una deuda con el proveedor. Por eso se arma, se muestra y se espera el «sí».

## Capas de conocimiento

| Capa | Qué contiene | De dónde sale |
|---|---|---|
| **Sistema** | Cómo funciona Conciliación: pantallas, pasos, trampas | [references/flujo-conciliacion.md](references/flujo-conciliacion.md) |
| **SUNAT y contexto peruano** | Solo llega lo facturado con el RUC del negocio; una boleta simple o un ticket no aparecen; una compra reciente puede tardar en llegar | La trae la skill |
| **Negocio** | Catálogo, cuentas de pago, proveedores | **Se lee de Finangher** |
| **Operación** | Qué compras integrar, cómo se pagó cada una, a qué producto corresponde cada ítem | **Lo dice el dueño**; el sistema propone, no decide |

## Paso 0 · Ver qué hay

Abrir Conciliación y consultar a SUNAT los meses pendientes
([flujo](references/flujo-conciliacion.md)). Responderle al dueño con el
panorama antes de tocar nada:

> SUNAT informa **9 compras** sin registrar: 2 de <proveedor A> (S/ 39.80) y 7
> de <proveedor B> (S/ 229.28), de octubre y meses anteriores. ¿Las integro
> todas, o empiezo por algún proveedor?

Con más de unas diez compras, proponer por dónde empezar (lo más reciente, o el
proveedor con más mercadería) en vez de ofrecer hacerlas todas seguidas.

Si no hay ninguna, decirlo y recordar las dos razones posibles: no hay compras
facturadas con el RUC en ese período, o son recientes y aún no llegan.

## Paso 1 · Lo que hay que saber de cada compra

La factura trae proveedor, ítems, cantidades y total. Faltan cuatro datos que el
sistema no puede saber:

| # | Dato | Opciones | Cómo se resuelve |
|---|---|---|---|
| 1 | **Cómo se pagó** | Al contado y con qué cuenta (caja, Yape, Plin, banco) · a crédito · una parte ahora | **Preguntar siempre.** La factura puede decir «Contado» y haberse pagado de otra forma; decir lo que dice la factura y pedir confirmación |
| 2 | **A qué producto corresponde cada ítem** | Uno que ya existe en el catálogo · uno nuevo | Finangher propone el «más parecido». Si el nombre coincide sin duda, usarlo. Si el proveedor lo llama distinto, o hay varios candidatos, **preguntar** |
| 3 | **Qué variante** | La presentación del producto que se compró (tamaño, peso, sabor) | Si el producto tiene variantes, la factura suele decir cuál. Si no lo dice con claridad, **preguntar** |
| 4 | **Si es nuevo: producto o servicio** | Producto (lleva inventario) · servicio | Preguntar si no es evidente por la descripción |

Agrupar las preguntas: una sola vez por proveedor para el pago («¿las 7 del
banco se pagaron por débito de tu cuenta?») y una sola vez por ítem repetido.
No preguntar lo que la factura ya dice.

Reglas que no dependen del negocio:

- **El comprobante manda.** Proveedor, ítems, cantidades y total son los de la
  factura. No se editan ni se borran para «hacer que cuadre»; si algo no
  corresponde a la realidad, detenerse y decirlo.
- **Nunca asociar por parecido cuando hay duda.** Un ítem mal asociado sube el
  inventario del producto equivocado.
- **Saco o kilo: manda la unidad de la factura.** Si la cantidad viene en
  sacos (5 sacos), se elige la presentación «Saco x 40 kg» con esa cantidad. Si
  viene en kilos (200 kg), son kilos, aunque el producto se venda por saco. Solo
  se pregunta cuando el número sería absurdo en esa unidad. Al elegir la
  variante la pantalla dice «Entrarán N kilogramos a tu stock»: ese número debe
  coincidir con lo que dice la factura.
- **El pago viene marcado y no es una respuesta.** La hoja abre con una cuenta
  ya elegida (por ejemplo Yape) y el botón «Registrar» se activa apenas todas
  las líneas quedan asociadas. Un clic registraría con esa cuenta. No pulsarlo
  hasta tener el pago dicho por el dueño.
- **Una compra que ya se registró a mano no se duplica:** se vincula con su
  factura.

## Paso 2 · Armar la compra, sin registrar

Seguir [references/flujo-conciliacion.md](references/flujo-conciliacion.md)
hasta dejar la compra lista: ítems asociados y pago elegido. **No pulsar
«Registrar».** El dueño ya debe tener su sesión iniciada; este skill no pide ni
escribe contraseñas ni claves de SUNAT.

## Paso 3 · Verificar y pedir el «sí»

Comprobar en pantalla, contra la factura y lo que dijo el dueño:

1. Proveedor y número de la factura.
2. Cada ítem asociado al producto correcto, sin ninguno «por asociar».
3. Cantidades y total iguales a los de la factura.
4. Forma de pago y cuenta.

Si algo no coincide, no registrar. Cuando coincide, enviar la confirmación con
el molde de [references/confirmacion-compra.md](references/confirmacion-compra.md)
y esperar la respuesta. Se envía como mensaje normal; el dueño contesta «sí»,
«no» o el cambio con sus palabras.

Cuando son muchas compras del mismo proveedor y el mismo tipo, se puede
confirmar por lote: una tabla con todas, sus totales y lo que cambia en el
inventario. La primera de cada proveedor se confirma sola.

## Paso 4 · Registrar y comprobar

Con el «sí»: pulsar «Registrar» **una sola vez** y comprobar el efecto antes de
pasar a la siguiente:

- Conciliación ya la muestra como registrada.
- El inventario del producto subió en la cantidad comprada.
- Al contado: bajó el saldo de la cuenta. A crédito: aparece la deuda con el
  proveedor.

Responder con lo que quedó: «Registrada la F001-123 de <proveedor>: +12 unidades
de <producto>, S/ 240.00 pagados por Yape».

## Al terminar

Un cierre corto: cuántas compras se integraron, cuántas quedaron y por qué, qué
productos nuevos se crearon y cuánto subió el inventario. Y lo que quedó para
el dueño: ítems que no se pudieron asociar, compras que no eran de mercadería.

## Cuando algo sale mal

| Situación | Qué hacer |
|---|---|
| SUNAT no responde o rechaza la conexión | Detenerse y decirlo. No reintentar en bucle |
| El negocio no tiene conectada su cuenta de SUNAT | Decir qué falta y que se configura en Finangher, en Facturación electrónica. Ofrecer ayuda: es una puesta en marcha que se hace una vez |
| SUNAT lista la factura pero no trae sus líneas («Productos por completar») | Pedirle al dueño el archivo de la factura. **De preferencia el XML** (el proveedor lo envía junto con el PDF): se sube con «Subir XML» y la compra queda con todas sus líneas y su comprobante verificado. **Si solo tiene el PDF, también sirve:** se leen los ítems del PDF y se cargan a mano en «Registrar compra»; el total debe coincidir con el que informa SUNAT. No inventar el detalle ni registrar solo el total sin que el dueño lo decida |
| Aparece una nota de crédito «por registrar», con monto negativo | No es una compra nueva: descuenta o anula una factura. Decírselo al dueño con el número de ambas y no registrarla sin su indicación |
| El mes muestra «Necesita tu decisión» (compras por revisar, compras sin comprobante) | Incluirlo en el panorama del Paso 0 y preguntarle al dueño; no resolverlo por cuenta propia |
| Un ítem no corresponde a nada del catálogo | Preguntar si se crea como nuevo; no asociarlo a algo parecido |
| La pantalla no confirma el registro | No volver a pulsar «Registrar». Mirar si la compra ya figura como registrada |
| La compra quedó mal registrada | Decirlo con su número. Corregirla lo decide el dueño |

## Bitácora de tropiezos

Igual que en `registrar-venta`: lo que no salió como dice este skill se anota en
`~/.finangher/bitacora.md`, sin datos de proveedores ni montos, y solo se
comparte con Finangher si el dueño quiere.

## Lo que este skill no hace

- Registrar una compra a partir de una foto o un ticket. Si la compra no tiene
  factura con el RUC del negocio, no está en SUNAT: se registra a mano como una
  compra sin comprobante.
- Conectar el negocio con SUNAT ni pedir sus claves.
- Declarar impuestos ni decidir temas tributarios.
- Modificar o eliminar una compra ya registrada.
