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

## Requisito: una computadora

**Todo este trabajo se hace desde una computadora**, no desde un teléfono: en
el teléfono el certificado digital no se descarga. Si el dueño está en el
celular, pedirle que pase a una computadora antes de empezar. El archivo del
certificado debe quedar en la misma computadora desde la que se abre
Finangher para subirlo.

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
2. **¿Ya pediste antes el certificado gratuito de SUNAT?** (SUNAT lo da solo
   dos veces por RUC.)
3. **¿Ya creaste un usuario SOL secundario** para tu sistema de facturación?

**No preguntar «¿tienes certificado?».** Casi nadie lo tiene a mano y todos
responden «no», lo que los empuja al PSE y a esperar a Finangher. La pregunta
correcta es si SUNAT le da el certificado gratis, y eso se responde **yendo a
pedirlo**: es el camino por defecto y el más rápido, porque no depende de nadie.

Con esas respuestas se elige el camino en
[references/elegir-camino.md](references/elegir-camino.md). Proponer **uno** y
decir por qué, en una línea. El dueño decide.

| Situación | Camino que se propone |
|---|---|
| Cualquier negocio (también Nuevo RUS) que no lo pidió dos veces | **Pedir el certificado gratuito de SUNAT (CDT)** en el tramo 3. Si SOL no lo da, anotar el motivo y pasar al **PSE** |
| Ya lo pidió dos veces, o SOL lo rechazó | **PSE** (o un certificado comprado, si el dueño prefiere) |
| Dice que ya tiene un archivo `.pfx`/`.p12` vigente con su contraseña | **Ese certificado**: se sube y listo |
| Es PRICO, agente de retención o de percepción | Ninguno de estos caminos sirve: SUNAT lo obliga a emitir por OSE. Derivar a Finangher por WhatsApp |

En Finangher, la firma pregunta «Tengo mi certificado digital / No tengo
certificado». Con el CDT recién descargado, el dueño **sí** lo tiene: elegir
«Tengo mi certificado digital». «No tengo certificado» es solo para cuando SUNAT
no se lo dio.

## Pasos 2 y 3 · Uno por uno: lo que sale de SUNAT va de inmediato a Finangher

**Regla de oro: un dato a la vez.** Cada cosa que se obtiene en SUNAT se lleva
a Finangher **antes** de pedir la siguiente. Nunca hacer todo en SUNAT y luego
todo en Finangher: así se confunden las contraseñas (la del usuario
secundario, la clave API y la del certificado) y se pega una en el lugar de
otra.

Antes de los tramos, en Finangher: **Régimen tributario** (no depende de
SUNAT).

| Tramo | En SUNAT ([pasos-sunat.md](references/pasos-sunat.md)) | En seguida, en Finangher ([pasos-finangher.md](references/pasos-finangher.md)) |
|---|---|---|
| **1 · Usuario secundario** | Crear `FINANGHE` y asignar programas (A) | Configuración › Facturación › **Usuario SOL secundario**: usuario y su clave. Debe quedar «Guardado» |
| **2 · Credenciales API** | Credenciales de API SUNAT: obtener ID y clave | **Credenciales API SUNAT**: pegar ID y clave. Debe quedar «Guardadas» |
| **3 · Firma** | Certificado: pedir el CDT (B) o registrar el comprado (C), y la casilla SEE (D). **O** PSE: Altas/Bajas de PSE (E) | **Firma de tus comprobantes**: subir el archivo con su contraseña, **o** «Ya lo habilité en SUNAT» y el código para facturar |

Al cerrar cada tramo, confirmar con el dueño que la fila de Finangher cambió de
«Falta» a su estado antes de volver a SUNAT. Si el dueño ya tenía hecho algún
tramo en SUNAT (por ejemplo, el usuario secundario), llevar ese dato a
Finangher primero y recién seguir.

En SUNAT: un paso por mensaje, preguntando qué ve. Si SOL muestra algo distinto
a lo descrito, no improvisar: pedir una captura, leerla y anotar la diferencia
en la bitácora. En Finangher, Claude puede abrir la fila y dejar el formulario
listo; **los campos de clave los escribe el dueño**.

En el camino PSE el tramo 2 (API) no es necesario para emitir, pero se
recomienda: Finangher lo usa para traer las compras de SUNAT y emitir guías.

Después de los tres tramos, el dueño ya puede cerrar SUNAT. **El paso 4 es
obligatorio** (sobre todo con RUC 20) y se hace solo en Finangher:

1. **Régimen tributario.**
2. **Tipo de afectación del IGV**, si el régimen lo pide.
3. **Comprobantes electrónicos**: revisar las series de boleta y factura.
4. **Logo del negocio** (Configuración, sobre la imagen del negocio, ícono de
   cámara) y **dirección fiscal** en la misma tarjeta. El logo se imprime en
   boletas y facturas: sin logo, el comprobante sale con las dos iniciales del
   nombre. Pedirle al dueño la imagen del logo; si no la tiene en ese momento,
   decírselo y dejarlo anotado como pendiente.
5. Que cada fila de Configuración › Facturación diga «Configurado» o su estado.

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
