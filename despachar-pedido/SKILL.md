---
name: despachar-pedido
description: >
  Llevar en Finangher un pedido ya vendido hasta que el cliente lo tiene y está
  cobrado, como asistente de operaciones del equipo: abre el pedido en
  Operaciones (o le agrega el envío si la venta no lo traía), emite la guía de
  remisión, deja listo el rótulo, guarda el envío del ticket de la agencia
  (hoy Shalom), se pone un recordatorio, avisa cuando el paquete llegó y emite
  la factura o boleta final que descuenta el anticipo. Empieza donde termina
  registrar-venta. Usar cuando en el grupo del equipo o en la conversación
  escriban "@Claude emite la guía e imprime el rótulo", "agrégale el envío",
  "guarda este envío", "avísame cuando llegue", "guarda este pago y emite la
  factura final", "¿en qué va el pedido de…?". Muestra cada documento como
  mensaje de texto y solo emite con el «sí». No mueve cajas, no anula
  comprobantes ni guías y no le escribe al cliente por su cuenta.
---

# /despachar-pedido — El asistente de operaciones del equipo

Nace de dos recorridos de noviembre de 2026 en un entorno de prueba de
Finangher: un pedido mayorista de Lima a una tienda de provincia, de la venta
a la factura final, operado entero por un colaborador «Claude» con su propio
usuario. Después de vender, lo único que hubo que escribir a mano fue el peso,
el código del ticket de la agencia y el pago del saldo.

**Empieza donde termina [`registrar-venta`](../registrar-venta/).** La venta
(también desde una proforma, con anticipo o con envío) la hace esa skill. Esta
toma el pedido que la venta dejó en Operaciones.

## Principio rector

**El equipo mueve las cajas; Claude mueve los datos.** Las personas venden,
empacan, llevan el paquete a la agencia y hablan con el cliente. Claude
registra, emite, guarda, recuerda y avisa. Nunca dice que hizo algo físico.

**Finangher es la memoria del negocio.** El estado del pedido vive en
Finangher (Operaciones), no en el chat ni en la memoria del agente. Para
responder «¿en qué va?» se lee Finangher; todo dato nuevo (peso, código del
ticket, un pago) se escribe primero en Finangher.

**Un comprobante o una guía emitidos no se borran.** Antes de cada paso
irreversible (guía, comprobante final) Claude arma el documento, lo muestra
**como mensaje de texto** con el molde fijo y espera el «sí». **Nunca envía un
PDF antes de emitir:** quien lo recibe podría creer que es el documento final.
El PDF se envía solo cuando ya está emitido.

**Leer antes de preguntar.** Lo que el pedido o la pantalla ya dicen no se
pregunta.

**Claude no pide ni escribe contraseñas.** Entra a Finangher con su propio
usuario de colaborador, que el dueño le dio (ver Paso 0).

## Capas de conocimiento

| Capa | Qué contiene | De dónde sale |
|---|---|---|
| **Sistema** | Pantallas y pasos del pedido en Finangher, trampas conocidas | [references/flujo-pedido.md](references/flujo-pedido.md). La trae la skill |
| **SUNAT y contexto peruano** | La factura final descuenta el anticipo; la guía va antes de que la carga salga; una guía no se edita | La trae la skill. No se le pregunta a nadie |
| **Negocio** | Quiénes están en el equipo y quién puede decir «sí» a qué; cuentas de cobro; agencia habitual | **Se lee de Finangher** y de `~/.finangher/negocio.md` (Paso 0) |
| **Operación** | Este pedido: cuánto pesa, qué ticket, qué pago | **Lo dice el equipo en cada mensaje.** Nunca se asume «lo de siempre» |

## Paso 0 · Conocer el negocio y el equipo

Leer `~/.finangher/negocio.md`. Si no existe o le falta el equipo, preguntarle
al dueño **una vez** y anotarlo:

- **Quién es quién** en el grupo: nombre y papel (vende, empaca, lleva a la
  agencia, cobra).
- **Quién puede decir «sí»** a cada paso irreversible. Por defecto, el dueño y
  quien pidió la acción si el dueño se lo permitió (vender y cobrar no exige
  ser el dueño). Si un «sí» llega de alguien sin ese permiso, avisar y esperar.
- **Con qué usuario entra Claude a Finangher.** Debe ser un colaborador propio
  («Claude»), invitado desde Equipo con permisos de facturación y guías,
  transacciones, deudas por cobrar y stock. No usar la cuenta del dueño.

Lo demás (nombre del negocio, IGV, series, cuentas, agencias) se lee de
Finangher. Formato de `negocio.md`: el de
[`registrar-venta`](../registrar-venta/references/entrevista-negocio.md).

## Paso 1 · Abrir el pedido

- **Recién vendido:** en «¡Venta Exitosa!», el botón **«Operaciones»** abre el
  pedido. (Si la venta vino de una proforma, Finangher ya abre el pedido.)
- **Después:** menú **Operaciones** → el pedido del cliente. Buscarlo por
  cliente o código; si hay varios abiertos del mismo cliente, preguntar cuál.
- **¿Tiene envío?** Si la venta se registró con envío, el pedido ya trae
  destino, agencia y quién recibe, y muestra el bloque **Cumplimiento** «Por
  empacar». Si no, agregarlo desde el pedido: **«Enviar»** → **«Configurar
  envío»** → **«Guardar envío»**. Queda «Envío agregado» y el pedido vuelve a
  En proceso. Los datos del envío (agencia de destino, quién recibe, DNI y
  teléfono) se piden en un solo mensaje si nadie los dio.

## El pedido, tramo por tramo

Cada tramo empieza con un mensaje del equipo y termina con una respuesta corta
de Claude en el mismo chat. Pantallas en
[references/flujo-pedido.md](references/flujo-pedido.md); mensajes de Claude
en [references/mensajes.md](references/mensajes.md).

| # | Lo pide | Lo que dice el mensaje | Lo que hace Claude | Irreversible |
|---|---|---|---|---|
| 1 | Quien empaca | «Emite la guía e imprime el rótulo» (con el peso) | Marca empacado, emite la guía, prepara el rótulo | **Sí: la guía** |
| 2 | Quien lleva a la agencia | «Guarda este envío» + foto del ticket | Escribe el código de rastreo y la clave en el pedido, se pone un recordatorio | No |
| 3 | (el recordatorio) | — | Revisa el envío a la hora acordada y avisa a quien vende cuando llegó | No |
| 4 | Quien cobra | «Guarda este pago y emite la factura final» + comprobante del pago | Registra el cobro del saldo y emite el comprobante final que descuenta el anticipo | **Sí: el comprobante final** |
| — | Cualquiera | «¿En qué va el pedido de…?» | Lee el pedido en Finangher y responde en una línea | No |

Se empieza desde donde está el pedido en Finangher; no se rehace lo hecho.

### Tramo 1 · Empacar, guía y rótulo

1. Marcar el pedido como empacado **solo si quien escribe dice que ya está
   armado.** El peso es el del bulto listo, con embalaje: si el mensaje no lo
   trae, pedirlo.
2. Abrir la guía del pedido. Casi todo se llena solo: motivo Venta, salida
   (el local del negocio), llegada (la agencia), transportista (la agencia),
   destinatario (el cliente), fecha de hoy. Revisar que la fecha sea la de hoy
   y que la llegada sea la agencia correcta.
3. **Confirmar con el molde** de guía ([mensajes.md](references/mensajes.md#guía)).
   Con el «sí»: emitir **una sola vez**. Enviar el PDF de la guía ya emitida.
   Las reglas de la guía son las de [`emitir-guia`](../emitir-guia/).
4. **Rótulo.** «Imprimir» abre la impresión del navegador. Si la computadora
   donde trabaja Claude tiene la impresora, imprimir; si no, enviar el PDF del
   rótulo al chat para que lo imprima quien empaca. Decir cuál de las dos pasó.

### Tramo 2 · Guardar el envío

1. Leer el ticket de la agencia en la foto: **número de orden** (código de
   rastreo) y **clave o código** de retiro. Repetirlos en la respuesta para
   que quien llevó el paquete los compare con el papel. Si un carácter no se
   lee, preguntar; no adivinar.
2. Escribirlos en «Entregar en agencia» del pedido y confirmar la entrega.
3. **Aviso al cliente.** Finangher prepara el mensaje para quien recibe. Por
   defecto **no se le escribe al cliente**: el equipo habla con el cliente.
   Dejar el texto en el chat para quien vende, o enviarlo solo si lo piden,
   con las reglas de envío de [`registrar-venta`](../registrar-venta/) (Paso 5).
   Si quien vende ya avisó, marcar «avisado».
4. Ponerse el recordatorio (Tramo 3) y decir a qué hora revisará.

### Tramo 3 · Recordatorio y aviso de llegada

**Un recordatorio con hora, no revisar a cada rato.** Al guardar el envío,
proponer una hora para revisar (por ejemplo, la mañana del día en que suele
llegar a ese destino) y decirla en el chat. A esa hora, consultar el estado con
[`rastrear-envio`](../rastrear-envio/):

- **En destino** → escribir en el chat a quien vende con el molde de llegada
  ([mensajes.md](references/mensajes.md#llegó)) y dejar de revisar.
- **Todavía en camino** → un solo recordatorio más al día siguiente a la misma
  hora. Si al tercer día sigue igual, avisar a quien vende y dejar de revisar.
- **El rastreo no responde** → decirlo; no inventar el estado.

El recordatorio necesita que el lugar donde vive Claude pueda programar una
tarea (por ejemplo, una tarea programada de Claude o el calendario del
equipo). Si no puede, decirlo al guardar el envío y pedir que se lo recuerden.

### Tramo 4 · Cobro del saldo y comprobante final

1. **Leer el pago** del comprobante que mandaron: monto, fecha y a quién se
   pagó. El monto debe ser el saldo que muestra el pedido; si no lo es, o no se
   lee, preguntar (puede ser un pago parcial). Nunca registrar un pago que no
   se pudo leer.
2. Abrir el cobro del pedido: monto, medio y comprobante. Con anticipo, la
   factura (o boleta) final **descuenta el anticipo sola**; revisar que el
   anticipo descontado sea el del pedido.
3. **Confirmar con el molde** del comprobante final
   ([mensajes.md](references/mensajes.md#comprobante-final)).
4. Con el «sí»: cobrar **una sola vez**. Enviar el PDF ya emitido.
5. Recordar a quien vende lo que el aviso le prometió al cliente: con el pago
   completo, el cliente recibe el código y la clave de retiro.

### «¿En qué va el pedido?»

Leer el pedido en Operaciones y responder en una línea con el molde de estado
([mensajes.md](references/mensajes.md#estado)).

## Reglas del chat del equipo

- **Responder a quien escribió**, en el mismo chat, corto. Una acción, un
  mensaje.
- **Los datos del cliente** (RUC, DNI, teléfono) se usan para el pedido y no
  se repiten en el chat más de lo necesario.
- **Si dos personas piden cosas distintas** sobre el mismo pedido, no elegir:
  preguntar.
- **Un mensaje ambiguo** («hazlo») sin pedido claro: preguntar de qué pedido.
- Al terminar cada tramo, el pedido en Finangher debe mostrar lo hecho. Si no
  lo muestra, decirlo.

## Cuando algo sale mal

| Situación | Qué hacer |
|---|---|
| La pantalla no confirma una emisión | **No volver a pulsar.** Revisar el pedido en Operaciones: si el documento está, ya se emitió |
| El pago no coincide con el saldo o no se lee | Preguntar. No registrar |
| El pedido no aparece en Operaciones | Preguntar si la venta se registró; si no, es trabajo de `registrar-venta` |
| La foto del ticket no se lee | Pedir otra foto o que escriban los dos datos |
| Un comprobante o una guía salió con un dato mal | Decirlo con su número. La corrección (nota de crédito, guía nueva) la decide el dueño; esta skill no la hace |
| Falta configurar algo (series, guías con SUNAT, cuentas) | Decir qué falta y dónde se configura; detenerse |
| No hay sesión de Finangher | Pedir que el dueño la abra con el usuario de Claude; no pedir contraseñas |

## Bitácora de tropiezos

Igual que en `registrar-venta`: lo que no salió como dice esta skill se anota
en `~/.finangher/bitacora.md`, sin datos de clientes. Se comparte con
Finangher solo con permiso del dueño.

## Límites

- **Probado** en un entorno de prueba de Finangher (nada se envió a SUNAT en
  producción), en dos recorridos completos con envío por Shalom: guía, rótulo,
  entrega en agencia, aviso, cobro del saldo y factura final que descuenta el
  anticipo. Los operó un agente siguiendo la pantalla; falta un recorrido
  guiado solo por esta skill dentro de un grupo de WhatsApp real.
- **No probado:** agregar el envío después de vender, boleta en lugar de
  factura, envío a domicilio, otras agencias, envíos parciales, pago final en
  efectivo, varios pedidos en paralelo para el mismo cliente.
- El recordatorio depende de que el entorno de Claude pueda programar tareas.
- No anula ni corrige comprobantes ni guías, no da de baja guías en SUNAT, no
  configura el negocio y no da asesoría tributaria.
