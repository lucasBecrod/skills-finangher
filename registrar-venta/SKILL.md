---
name: registrar-venta
description: >
  Registrar una venta en Finangher y emitir su boleta o factura electrónica,
  operando la web con la sesión del dueño. Usar cuando pidan "emite una boleta",
  "factúrale a este RUC", "registra esta venta", "véndele X a Y", "cóbrale por
  Yape y dale su boleta", "pasa esta proforma a venta", "emite el anticipo".
  También vende desde una proforma, con anticipo o con envío por agencia; el
  despacho sigue con despachar-pedido. Revisa que el pedido esté completo, arma la venta,
  muestra un resumen fijo y solo emite con el «sí» del dueño. No emite notas de
  crédito ni anula comprobantes.
---

# /registrar-venta — Vender y emitir el comprobante en Finangher

Nacido de la prueba del 2026-11-16: la misma boleta, operada por Claude, tomó
5 min 30 s y 16 pasos en el portal de SUNAT y salió con el IGV equivocado; en
Finangher tomó alrededor de un minuto y salió bien, porque el negocio ya estaba
configurado.

## Principio rector

**Un comprobante emitido no se borra: se corrige con otro comprobante.** Por
eso este skill revisa el pedido antes de actuar y pide el «sí» antes del último
clic.

**Leer antes de preguntar.** Lo que Finangher ya sabe se lee de Finangher. Al
dueño solo se le pregunta lo que el sistema no puede responder.

## Capas de conocimiento

Cada dato pertenece a una sola capa. La capa decide de dónde sale.

| Capa | Qué contiene | De dónde sale |
|---|---|---|
| **Sistema** | Cómo funciona Finangher: pantallas, pasos, trampas | [references/flujo-vender.md](references/flujo-vender.md). La trae la skill |
| **SUNAT y contexto peruano** | Reglas que valen para cualquier negocio: una persona tiene DNI y puede tener RUC, factura exige RUC, boleta sobre S/ 700 exige documento, un comprobante se corrige con nota de crédito | La trae la skill. No se le pregunta al dueño |
| **Negocio** | Lo que no cambia de una venta a otra: nombre de la tienda, si lleva IGV o está exonerado, cuentas y medios de cobro, series | **Se lee de Finangher**, donde el dueño ya lo configuró y donde puede cambiar. Solo lo que no se pueda leer se pregunta una vez y se anota en `~/.finangher/negocio.md` |
| **Operación** | Lo que cambia en cada venta: qué, a quién, con qué comprobante, cómo paga | **Lo dice el dueño en cada venta.** Nunca se asume ni se guarda como costumbre |

Dos errores a evitar: preguntarle al dueño algo que la pantalla ya muestra, y
dar por sabido un dato de la operación porque «casi siempre es así». El
comprobante y el pago los confirma el dueño con su cliente en cada venta:
fallar ahí obliga a rehacer el comprobante.

## Paso 0 · Conocer el negocio

Leer `~/.finangher/negocio.md`. Si no existe, seguir
[references/entrevista-negocio.md](references/entrevista-negocio.md): es
corta, porque casi todo se lee de Finangher. El nombre del negocio se escribe
siempre como lo escribe el dueño (mayúsculas incluidas): es su identidad.

## Paso 1 · Revisar el pedido

Pasar el pedido por esta lista. Lo que falte se le pide al dueño **en un solo
mensaje**, corto. «Emite una boleta» a secas no alcanza: responder con lo que
falta.

| # | Dato de la operación | Opciones | Si el pedido no lo dice |
|---|---|---|---|
| 0 | **Desde qué negocio se emite** | El negocio activo en la sesión de Finangher | Ver «El negocio que emite», abajo |
| 1 | **Qué se vende, cuánto y a qué precio** | Productos del catálogo, cantidad, y precio: el que diga el dueño o el del catálogo | Producto y cantidad: preguntar; nunca elegir un producto «parecido»; «un lector» es cantidad 1. Precio: si el dueño dijo uno, usar ese; si no, proponer el del catálogo en la confirmación del Paso 3 |
| 2 | **A quién** | RUC · DNI · clientes varios (sin seleccionar cliente; solo boleta hasta S/ 700 o sin comprobante) | Preguntar, ofreciendo «clientes varios» si aplica |
| 3 | **Comprobante** | Ninguno · boleta · factura | **Preguntar siempre.** No hay comprobante «habitual». Si el pedido dice «boleta» o «factura», ya está dicho |
| 4 | **Cómo paga** | Al contado y con qué medio · a crédito · una parte ahora y el resto después (adelanto) | **Preguntar siempre**, ofreciendo los medios que Finangher muestra en el punto de venta. El pago se registra en una cuenta real del negocio: ponerlo en la equivocada desordena sus finanzas |
| 5 | **Operación especial** | Normal · gratuita (regalo, muestra, bonificación) · exportación | Asumir normal. Solo es especial si el pedido lo dice |
| 6 | **Entrega al cliente** | Enviarle el comprobante por WhatsApp · no enviar | No frena la venta: se pregunta al final (Paso 5). Si el pedido ya trae el número, anotarlo |

**El negocio que emite.** Un dueño puede tener varias empresas en Finangher, y
la sesión solo tiene una activa. Antes de armar la venta, leer en Finangher qué
negocio está activo (nombre de la tienda en el punto de venta) y si la cuenta
tiene otros:

- **La cuenta tiene un solo negocio** → se emite desde ese, sin preguntar.
- **Tiene varios y el pedido dice cuál** → comprobar que el activo es ese. Si
  no lo es, avisar y preguntar antes de cambiarlo: cambiar el negocio activo
  afecta lo que el dueño ve en su propia sesión.
- **Tiene varios y el pedido no lo dice** → preguntar: «¿Desde cuál emito:
  <A> o <B>? Ahora está activo <A>».
- **No se puede saber si tiene varios** → decir cuál está activo y pedir que lo
  confirme la primera vez; anotarlo en la ficha.

En todos los casos el negocio que emite aparece en la primera línea de la
confirmación del Paso 3, con su razón social.

**El producto tiene que ser del negocio.** Buscar el producto en el catálogo
del negocio antes de armar la venta:

- **Un solo resultado que coincide con el pedido** → usarlo.
- **Varios parecidos o repetidos** (mismo nombre, o casi, con otro precio) →
  no elegir. Mostrarlos con nombre y precio y preguntar cuál: «Encontré dos:
  "Lector X Compatible" a S/ 69.00 y "Lector X" a S/ 0.00. ¿Cuál vendo?». Un
  producto a S/ 0.00 o repetido suele ser un registro por limpiar: decírselo.
- **No está en el catálogo** → no vender otro ni crearlo por cuenta propia.
  Preguntar: «No encontré "<producto>" en tu catálogo. ¿Quieres que lo
  agregue?». Si dice que sí, pedirle nombre y precio, y confirmarlos antes de
  crearlo.

Aclaraciones de la lista:

- **Cliente dado por nombre** («a Comercial Andina»): buscarlo en la cartera de
  Finangher. Si sale un solo contacto con documento, usarlo y decirlo; si salen
  varios o ninguno, pedir el RUC o DNI.
- **Clientes varios** depende del total (hasta S/ 700), que recién se ve en el
  carrito: ofrecerlo con esa condición.
- **Medios de pago**: los válidos son los que aparecen en el punto de venta de
  Finangher. Para ofrecerlos se puede abrir el punto de venta y leerlos antes
  de preguntar. Si el dueño nombra uno que no aparece, decírselo: hay que
  crearlo en Finangher antes de usarlo.
- **Operación gratuita**: no hay cobro, no preguntar cómo paga.
- **Adelanto**: preguntar cuánto entra ahora, por qué medio, y cómo queda el
  saldo. Si el comprobante va por el total o solo por el adelanto lo decide el
  dueño.

Lo que **no** se le pregunta al dueño en una venta, porque es del negocio y lo
resuelve Finangher: si lleva IGV o va exonerada, la serie, la moneda habitual.

Reglas que no dependen del negocio:

- **Factura exige RUC** del cliente. Sin RUC no hay factura.
- **Boleta por más de S/ 700 exige documento** del cliente.
- Un RUC o DNI se copia dígito por dígito del pedido.

## Paso 2 · Armar la venta en Finangher, sin vender

Seguir [references/flujo-vender.md](references/flujo-vender.md) hasta dejar el
carrito listo: producto, cliente, comprobante y pago. **No pulsar «Vender».**
Armar el carrito no emite nada y se puede deshacer. El dueño ya debe tener su
sesión iniciada en el navegador; este skill **no pide ni escribe contraseñas**.

## Paso 3 · Verificar y pedir el «sí»

Leer la pantalla y comparar con el pedido. Las seis deben coincidir:

1. Producto y cantidad.
2. Total.
3. **Impuestos**: la línea «Impuestos» debe corresponder al tratamiento de IGV
   del negocio (exonerado → S/ 0.00; con IGV → mayor que cero), o al de la
   operación especial si el pedido la pidió.
4. Cliente y su documento.
5. Tipo de comprobante marcado.
6. Forma y medio de pago.

Si una no coincide, **no vender**: corregir o preguntar.

Cuando las seis coinciden, enviarle al dueño la confirmación con el molde fijo
de [references/confirmacion.md](references/confirmacion.md), llenado con lo
que la pantalla muestra de verdad (no con lo que se pensaba poner), y **esperar
su respuesta**. El molde tiene siempre los mismos bloques en el mismo orden:
comprobante y cliente, tabla de ítems con impuestos y total, pago, opciones,
entrega y, solo si hay algo que mirar, ⚠️ Observaciones.

- **«Sí»** → Paso 4.
- **Una corrección** («ponle 65», «es factura») → cambiarlo en el carrito,
  verificar de nuevo y volver a confirmar con el molde completo.
- **«No»** o silencio → no vender. Dejar el carrito como está y avisar.

La confirmación se pide en **todas** las ventas.

## Paso 4 · Vender y entregar

Solo con el «sí» del dueño: pulsar «Vender» **una sola vez**, esperar a que
termine «Registrando venta» y responder con: serie y número del comprobante,
cliente, total e impuestos. Si lo piden, descargar el PDF.

## Paso 5 · Entregar el comprobante al cliente

**Un comprobante que el cliente no recibió es una venta a medio terminar.** Al
informar el resultado del Paso 4, cerrar siempre con la misma pregunta:

> ¿Se la envío al cliente? Pásame su WhatsApp.

Si Finangher ya muestra un celular en el contacto del cliente, ofrecerlo en vez
de pedirlo: «¿Se la envío al cliente al 9XX XXX XXX?».

- **El dueño da el número o dice que sí** → enviar el comprobante (el PDF o el
  enlace «comprobante digital» que trae la boleta) con un mensaje corto a nombre
  del negocio, y confirmar al dueño que se envió y a qué número.
- **El pedido ya traía el número** → no volver a preguntar: aparece en el bloque
  «Entrega» de la confirmación del Paso 3 y se envía apenas se emite.
- **El dueño dice que no, o no responde** → no enviar nada. Dejarle el PDF.

**Finangher es la memoria del negocio.** Todo dato que el dueño entrega (un
celular, un correo, una dirección) se escribe primero en Finangher, para que la
próxima vez el sistema lo proponga y nadie tenga que volver a pedirlo. El agente
no guarda esos datos por su cuenta.

**El cliente espera su PDF, no un enlace.** Lo que se entrega es el archivo PDF
del comprobante, con un mensaje de una línea, como lo enviaría el dueño:

> Hola <nombre>, aquí está tu boleta B001-15 por S/ 69.00. ¡Gracias por tu compra!

Un solo mensaje: el PDF con ese texto como pie. Sin enlaces, sin datos
tributarios y sin publicidad: el PDF ya trae el QR y el enlace al comprobante
digital, desde donde el cliente descarga el XML y el CDR si los necesita. El archivo lleva un nombre
que el cliente entienda: «Boleta B001-15 - <negocio>.pdf».

Orden: primero escribir el celular en el campo de la venta en Finangher y
guardarlo; después enviar. Detalle en
[references/flujo-vender.md](references/flujo-vender.md), «Entregar el
comprobante». Si el agente no puede adjuntar el PDF en WhatsApp, decirlo y
dejarle al dueño el PDF descargado y el chat abierto.

**Desde qué WhatsApp se envía.** En una computadora puede haber varias sesiones
(la aplicación de WhatsApp, WhatsApp Web en el navegador) y no todas son del
negocio. Antes de enviar, mirar de quién es la sesión que se va a usar (nombre
y número del perfil) y compararla con el WhatsApp del negocio:

- **Es el WhatsApp del negocio** → enviar, sin preguntar.
- **Es de otra persona** (el dueño, el representante legal, un colaborador), o
  **no se puede saber de quién es** → preguntar antes de enviar: «Este WhatsApp
  es de <nombre>. ¿Le envío la boleta desde aquí, o desde el del negocio?».
- Que la pestaña diga «WhatsApp Business» no prueba que sea la cuenta del
  negocio.

Al confirmar el envío, decir siempre desde qué perfil salió.

Reglas del envío:

- Solo al número que el dueño dio o aprobó para **esta** venta. Nunca a un
  número de otra venta ni a uno adivinado.
- El número se repite al dueño dígito por dígito antes de enviar si lo dictó o
  lo escribió con espacios o sin código de país.
- **Un solo envío.** Pulsar enviar una vez. Si no se ve confirmación, mirar el
  chat antes de reintentar: un segundo clic manda el mensaje dos veces.
- Antes de enviar, comprobar que el chat abierto es el del número aprobado.

## Venta desde una proforma, con anticipo o con envío

Si el pedido viene de una proforma, paga una parte ahora y el resto después, o
va por agencia, seguir [references/proforma-anticipo-envio.md](references/proforma-anticipo-envio.md).
El anticipo es un comprobante real y se confirma con su propio molde. Después
de vender, el pedido (empacar, guía, rótulo, agencia, cobro del saldo y
comprobante final) sigue con [`despachar-pedido`](../despachar-pedido/).

## Cuando algo sale mal

| Situación | Qué hacer |
|---|---|
| La pantalla no confirma la venta | **No volver a pulsar «Vender».** Revisar «Operaciones»: si la venta está, ya se registró |
| El producto no está en el catálogo | Preguntar si lo agrega. No crearlo sin el «sí» ni usar otro parecido |
| El carrito ya traía productos o cliente | Detenerse y esperar la respuesta del dueño; no vender encima de un carrito ajeno al pedido. Un carrito vacío se usa sin preguntar |
| El comprobante salió mal | Decirlo tal cual, con su número. La corrección (nota de crédito) la decide el dueño |
| No hay sesión iniciada | Pedir al dueño que entre a Finangher; no pedirle la clave |

## Bitácora de tropiezos

Todo lo que no salió como dice este skill se anota en
`~/.finangher/bitacora.md`, sin datos de clientes ni de ventas: una pantalla
distinta, una trampa, un error del sistema, una equivocación propia, una
corrección del dueño. Se lee al empezar cada venta y se escribe al terminar.
Con permiso del dueño, y solo con su permiso, se comparte con Finangher para
que corrijan el sistema. Formato y reglas en
[references/bitacora.md](references/bitacora.md).

## Lo que este skill no hace

- Notas de crédito, anulaciones ni cambios a un comprobante ya emitido.
- Despachar el pedido después de vender: eso es `despachar-pedido`.
- Configurar el negocio en Finangher (certificado, series, régimen, cuentas de
  cobro): eso se hace una vez en «Configuración». Si falta algo para vender,
  decir qué falta y dónde se configura.
- Decidir temas tributarios. Aplica lo que el negocio tiene configurado; ante
  una duda, pregunta.
