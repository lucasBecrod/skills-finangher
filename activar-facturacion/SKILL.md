---
name: activar-facturacion
description: >
  Guiar al dueño de un negocio peruano para activar la facturación electrónica
  en Finangher hasta emitir su primera boleta aceptada por SUNAT. Usar cuando
  pidan "activa mi facturación", "quiero emitir boletas en Finangher",
  "configura mi certificado", "no tengo certificado digital", "cómo conecto
  Finangher con SUNAT". Elige con el dueño el camino (certificado propio, el
  gratuito de SUNAT o uno comprado, o un PSE), lo acompaña en SUNAT paso a paso
  y deja Finangher listo para emitir. No pide ni escribe la Clave SOL principal.
---

# /activar-facturacion — De cero a la primera boleta aceptada

**El trabajo termina cuando SUNAT acepta la primera boleta del negocio.** Un
certificado subido, una pantalla en verde o un «ya lo habilité» son pasos; el
resultado es la primera boleta aceptada, con su número.

## Principio rector

**Leer antes de preguntar.** Finangher ya sabe el RUC, la razón social, el
domicilio fiscal, si el RUC está activo y habido, y qué falta para emitir
(Configuración › Facturación lo dice fila por fila). Al dueño solo se le
pregunta lo que el sistema no puede saber: su régimen tributario, si tiene un
certificado y si ya hizo un paso en SUNAT.

**En SUNAT trabaja el dueño con sus manos.** Todo lo que pasa dentro de SUNAT
Operaciones en Línea (SOL) lo hace el dueño con su Clave SOL principal: crear el
usuario secundario, obtener o registrar el certificado, autorizar al PSE. Claude
le dicta el paso siguiente, uno a la vez, y le pide que diga qué ve. Claude
**no pide, no lee en voz alta y no escribe** la Clave SOL principal, la clave
del usuario secundario ni la contraseña del certificado: el dueño las escribe
directamente en SUNAT o en Finangher.

## Capas de conocimiento

| Capa | Qué contiene | De dónde sale |
|---|---|---|
| **Sistema** | Las pantallas de Finangher y su orden | [references/pasos-finangher.md](references/pasos-finangher.md) |
| **SUNAT** | Qué pide SUNAT para emitir y dónde se hace en SOL | [references/pasos-sunat.md](references/pasos-sunat.md). No se le pregunta al dueño |
| **Negocio** | RUC, razón social, domicilio, régimen, cómo firma | Se lee de Finangher. El régimen se pregunta una vez y se guarda **en Finangher** |
| **Operación** | La primera venta real | La dice el dueño; se emite con la skill `registrar-venta` |

## Paso 0 · Ver dónde está el negocio

Con la sesión del dueño iniciada en Finangher, abrir **Configuración ›
Facturación** (`/configuracion/facturacion`) del negocio que va a emitir y leer
cada fila: Régimen tributario, Usuario SOL secundario, Firma de tus
comprobantes, Tipo de afectación del IGV, Comprobantes electrónicos. Cada fila
dice «Falta», «Guardado», «Con tu certificado», «Con el PSE», etc.

Contarle al dueño, en un mensaje corto, lo que ya está y lo que falta. Si todo
está listo («Listo para emitir»), saltar al Paso 5.

Si el dueño tiene varios negocios en Finangher, confirmar desde cuál va a
emitir antes de tocar nada.

## Paso 1 · Lo que se pregunta (una sola vez, en un solo mensaje)

1. **¿Cómo declaras tus impuestos?** Nuevo RUS (pagas S/ 20 o S/ 50 al mes)
   o Régimen Especial, MYPE o General. Si no sabe, que lo pregunte a su
   contador; no adivinarlo.
2. **¿Tienes un certificado digital** (un archivo `.pfx` o `.p12` con su
   contraseña)?
3. **¿Ya creaste un usuario SOL secundario** para tu sistema de facturación?

Con esas respuestas se elige el camino en
[references/elegir-camino.md](references/elegir-camino.md). Proponer **uno** y
decir por qué, en una línea. El dueño decide.

| Situación | Camino que se propone |
|---|---|
| Nuevo RUS | **PSE** (Finangher no puede saber si SUNAT le da el certificado gratuito; el PSE no lo necesita) |
| Régimen Especial, MYPE o General, sin certificado | **Certificado gratuito de SUNAT (CDT)**. Si SUNAT no se lo da, **PSE** |
| Ya tiene certificado vigente | **Su certificado** |
| Es PRICO, agente de retención o de percepción | Ninguno de estos caminos sirve: SUNAT lo obliga a emitir por OSE. Derivar a Finangher por WhatsApp |

## Paso 2 · Lo que el dueño hace en SUNAT

Seguir [references/pasos-sunat.md](references/pasos-sunat.md) según el camino.
Un paso por mensaje. Después de cada uno, preguntar qué ve en pantalla. Si SOL
muestra algo distinto a lo descrito, no improvisar: pedir una captura, leerla y
anotar la diferencia en la bitácora.

- **Certificado (gratuito o comprado):** usuario SOL secundario → obtener o
  registrar el certificado → marcar «Deseo emitir a través del SEE - Del
  Contribuyente».
- **PSE:** autorizar al PSE en SOL (Altas/Bajas de PSE) con la fecha de inicio
  que SOL permita. El usuario SOL secundario es opcional en este camino, pero
  se recomienda crearlo igual: Finangher lo usa para traer las compras de
  SUNAT.

## Paso 3 · Lo que se configura en Finangher

Seguir [references/pasos-finangher.md](references/pasos-finangher.md). Claude
puede abrir cada fila y dejar el formulario listo; **los campos de clave los
escribe el dueño**. Orden:

1. Régimen tributario.
2. Usuario SOL secundario (si aplica).
3. Firma de tus comprobantes: subir certificado, **o** autorizar al PSE y
   pegar el código para facturar.
4. Tipo de afectación del IGV (si el régimen lo pide).
5. Comprobantes electrónicos: revisar las series que propone Finangher.

## Paso 4 · Comprobar que dice «Listo para emitir»

Volver a leer Configuración › Facturación. La firma debe decir «Con tu
certificado» o «Con el PSE» y la configuración, «Listo para emitir
comprobantes». La etiqueta debe decir **Emisión real**: «Entorno de pruebas»
significa que no es la cuenta de producción.

Si falta algo, Finangher dice qué (por ejemplo «Falta tu dirección fiscal» o
«Aún no puedes emitir»). Resolver eso y volver a mirar. No pasar al Paso 5
hasta que diga «Listo para emitir».

## Paso 5 · La primera boleta

La primera boleta **es real**: queda en SUNAT y no se borra. Por eso se emite
con una venta real del negocio, no con una de prueba. Preguntar:

> Ya está listo. ¿Cuál es tu próxima venta? La emitimos juntos y así comprobamos
> que todo funciona.

Emitirla con la skill `registrar-venta` (con su resumen y su «sí»). Si no está
instalada, armar la venta en el punto de venta de Finangher, mostrar el resumen
y pulsar «Vender» solo con el «sí» del dueño.

Esperar la respuesta de SUNAT y leer el estado del comprobante en Operaciones:

| Estado | Qué significa | Qué hacer |
|---|---|---|
| Aceptado | Terminado | Decir serie y número. Ofrecer enviarlo al cliente |
| Esperando respuesta de SUNAT | SUNAT no respondió todavía | Esperar; Finangher reintenta solo. No volver a vender |
| Rechazado con **0111** («No tiene el perfil») en la primera boleta | Falta la casilla «SEE - Del Contribuyente», o se marcó hoy y rige desde mañana | Ver [references/pasos-sunat.md](references/pasos-sunat.md) § 0111. No eliminar la venta: se reintenta al día siguiente con el mismo número |
| «El Emisor no se encuentra registrado» (camino PSE) | Finangher todavía no registró el RUC en el PSE | Escribir a Finangher por WhatsApp con el RUC |
| Otro rechazo | Algo de la configuración o del comprobante | Copiar el código y el mensaje tal cual; no reintentar a ciegas. Anotar en la bitácora |

**Cerrar con el resultado:** «Tu primera boleta, B002-1, fue aceptada por
SUNAT. Desde ahora cada venta con boleta o factura se emite sola al vender.»

## Cuando algo sale mal

| Situación | Qué hacer |
|---|---|
| El dueño quiere dictar su Clave SOL o la contraseña del certificado | Agradecer y pedirle que la escriba él en el campo. Nunca repetirla en el chat |
| SOL dice que el RUC no puede obtener el certificado gratuito | Anotar el motivo que muestra SOL y pasar al camino PSE, o a un certificado comprado si el dueño prefiere |
| SUNAT muestra el RUC como no activo o no habido | No se puede activar. El dueño lo regulariza en SUNAT primero |
| Finangher pide «Código para facturar» y el dueño no lo tiene | Lo da Finangher: «¿No tienes el código? Pídelo por WhatsApp» en esa misma pantalla |
| La pantalla no coincide con esta skill | Detenerse, leer lo que hay, preguntar. Anotar en la bitácora |

## Bitácora de tropiezos

Igual que en `registrar-venta`: lo que no salió como dice la skill se anota en
`~/.finangher/bitacora.md`, sin claves, RUC de terceros ni datos de clientes.
Con permiso del dueño se comparte con Finangher.

## Lo que esta skill no hace

- Comprar el certificado por el dueño ni pagar trámites.
- Entrar a SOL con el usuario secundario: esa credencial es del sistema, nunca
  de una persona.
- Decidir el régimen tributario ni la afectación del IGV: los dice el dueño o
  su contador.
- Emitir por OSE (PRICO, agentes de retención o percepción).
- Cargar el catálogo de productos (ver la skill `cargar-catalogo` cuando esté
  publicada).

## Para la persona

El manual para el dueño, con los mismos pasos y sin términos técnicos, está en
[manual/](manual/). Claude puede enviárselo antes de empezar para que tenga a
mano lo que va a necesitar.
