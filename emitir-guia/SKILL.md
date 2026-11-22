---
name: emitir-guia
description: >
  Emitir en Finangher la guía de remisión remitente de una mercadería que el
  negocio traslada, operando la web con la sesión del dueño. Caso principal:
  el dueño trae mercadería que le compró a un proveedor; Claude junta en una
  sola guía, con motivo Compra, las facturas de ese proveedor que viajan
  juntas. Usar cuando pidan "haz la guía de mis tres facturas", "emite la guía
  de esta compra", "necesito la guía para traer la mercadería", "saca la guía
  de remisión", "emite la guía de esta venta". Propone lo que Finangher ya
  sabe, pregunta en un solo mensaje lo que solo sabe el dueño (de dónde sale
  la mercadería, quién la lleva, cuánto pesa, cuándo sale), muestra un
  resumen fijo y solo emite con el «sí» del dueño. No corrige ni anula guías
  emitidas, no emite guías de transportista y no da asesoría tributaria.
---

# /emitir-guia — Una guía de remisión para la mercadería que trasladas

> **Disponibilidad (noviembre de 2026).** La guía desde la compra («Trasladar
> mercadería» en el detalle de una compra) **llega a finangher.com con la
> próxima actualización**. Mientras tanto, si Claude no ve ese botón en la
> compra, te avisa y se detiene: no inventa pasos. La guía desde un pedido de
> venta con envío ya está en finangher.com y este skill la recorrió en un
> entorno de prueba de Finangher (ver «Desde una venta con envío»).

Este skill nace de un recorrido de noviembre de 2026. Una emprendedora trajo 18
productos de tres facturas del mismo proveedor y tardó 35 minutos en hacer la
guía en SUNAT. En Finangher, la misma guía (tres facturas, 18 bienes, peso,
partida y llegada, transportista) se armó desde la compra: casi todo se llenó
solo, y el dueño solo tuvo que decir lo que nadie más sabe.

## Por qué importa (una línea, sin asesoría)

La mercadería que viaja sin su guía de remisión puede ser intervenida en el
camino, y la factura no reemplaza a la guía. Por eso la guía se hace **antes**
de que la carga salga.

## Principio rector

**Una guía emitida no se edita.** Si sale mal, se emite otra y la anterior se
da de baja en SUNAT. Por eso el skill arma la guía, la muestra y solo emite
con el «sí».

**Leer antes de preguntar.** El proveedor, las facturas, los productos, las
cantidades y el lugar de llegada ya están en Finangher. Al dueño solo se le
pregunta lo que pasa fuera del sistema.

**Claude no pide ni escribe contraseñas.** El dueño inicia sesión en Finangher
y Claude opera ese navegador.

## Capas de conocimiento

| Capa | Qué contiene | De dónde sale |
|---|---|---|
| **Sistema** | Dónde está el botón, qué se llena solo, qué hay que revisar | La trae la skill (abajo) |
| **SUNAT y contexto peruano** | Quién es remitente y destinatario según el motivo; que la guía va antes del traslado; que una guía no se edita | La trae la skill |
| **Negocio** | Nombre, RUC y dirección del negocio (la llegada); compras registradas con sus facturas | **Se lee de Finangher** |
| **Operación** | Qué compras viajan juntas, de dónde sale la carga, quién la lleva, cuánto pesa, cuándo sale | **Lo dice el dueño en cada guía** |

## Paso 0 · ¿Qué guía es?

Decidir el motivo antes de tocar nada:

| Situación | Guía |
|---|---|
| **El dueño trae** mercadería que compró (la recoge o contrata el transporte) | **Remitente con motivo Compra.** El remitente y el destinatario son el mismo negocio; el proveedor sale de las facturas. Es el caso que cubre este skill |
| **El proveedor la despacha** hasta el negocio | La guía la emite el proveedor, no el dueño. Decírselo y no emitir nada |
| **El dueño vende** y despacha a su cliente | Guía de **venta**, desde el pedido (ver «Desde una venta con envío»). No usar la de compra |
| Devolución, traslado entre locales propios, consignación u otro motivo | Fuera de este skill. Decirlo y detenerse |

## Paso 1 · Ubicar las compras

1. Abrir **Movimientos › Compras** y buscar las compras del proveedor. Si el
   dueño dijo «mis tres facturas», confirmar cuáles son por su número y su
   fecha.
2. Las compras deben estar **registradas en Finangher con su factura
   electrónica**. Si alguna todavía no lo está, primero se integra (skill
   [`integrar-compras`](../integrar-compras/)). Sin la compra registrada no
   hay de dónde sacar las líneas.
3. **Un proveedor por guía.** Si las facturas son de proveedores distintos, son
   guías distintas (una por proveedor). Decirlo y hacerlas por separado.

## Paso 2 · Armar la guía, sin emitir

1. Abrir una de las compras y, en su detalle, pulsar **«Trasladar mercadería»**
   (debajo dice «Emite la guía de remisión»).
   - **Si el botón no aparece**, detenerse y decirlo: la función todavía no
     llegó a la cuenta del dueño, o la compra no puede trasladarse. No buscar
     caminos alternativos.
   - Si aparece **«Configurar para emitir»**, al negocio le falta la conexión
     de guías con SUNAT. Decirlo; no se configura dentro de este skill.
2. En la hoja **«Trasladar mercadería»**, pulsar **«Agregar otra compra de este
   proveedor»** y elegir cada factura que viaja en el mismo camión. La lista
   solo ofrece compras de ese mismo proveedor.
3. Revisar que cada compra muestre sus productos con la cantidad comprada.
   Por defecto viaja todo lo que falta enviar. Si el dueño dijo que solo va una
   parte, ajustar esa cantidad (la pantalla avisa si supera lo pendiente).

**Lo que se llena solo:** proveedor y su RUC; las facturas relacionadas; cada
producto con su descripción, su unidad y su cantidad; el destinatario (el
mismo negocio); la llegada (la dirección del negocio); la fecha de salida
(hoy).

**Lo que se propone y hay que confirmar:** el punto de **salida**. Finangher
propone la dirección fiscal del proveedor que figura en su factura, y **muchas
veces la mercadería no sale de ahí**: un proveedor puede facturar desde su
oficina y despachar desde un almacén en otra ciudad. Nunca darla por buena sin preguntar.

## Paso 3 · Preguntar lo que solo sabe el dueño, en un solo mensaje

> Para la guía de las 3 facturas de <proveedor> me falta:
> 1. **¿De dónde sale la mercadería?** La factura dice <distrito del proveedor>;
>    ¿sale de ahí o de otro almacén? (distrito y dirección)
> 2. **¿Quién la lleva?** Una empresa de transporte (su RUC y, si lo tienes,
>    su registro MTC) o tu propio vehículo (placa y conductor).
> 3. **Peso bruto:** todas las líneas están en kilos y suman **9 520 kg**.
>    ¿Pongo eso, o pesa más con el embalaje?
> 4. **¿Sale hoy?** Si no, ¿qué día?

Reglas:

- **Peso:** si todas las líneas están en kilogramos, proponer la suma; el dueño
  decide si agrega el embalaje. Si hay líneas en otras unidades, pedir el peso
  sin proponer.
- **Salida:** al cambiar el distrito, la hoja conserva la calle anterior y se
  cierra. Volver a abrir **«Editar salida»** y escribir la dirección real. No
  dejar un distrito con la calle de otro lugar.
- **Transporte:** en «¿Quién lleva la mercadería?» elegir **«Empresa de
  transporte · con RUC»** y buscarla por su RUC, o **«Lo traslada el negocio»**
  (vehículo propio). Para una empresa, el registro MTC es opcional en la
  pantalla («Añadir registro MTC · opcional»): ponerlo si el dueño lo tiene.

## Paso 4 · Verificar y pedir el «sí»

Comprobar en la hoja, y mandar este resumen fijo como mensaje normal:

> **Guía de remisión · motivo Compra**
> - Proveedor: <razón social> (RUC <…>)
> - Facturas relacionadas: <F001-…>, <F001-…>, <F002-…>
> - Bienes: <18> líneas, todas con su cantidad
> - Peso bruto: <9 520> kg
> - Ruta: <distrito, provincia, región de salida> → <distrito, provincia,
>   región de llegada>
> - Transporte: <empresa y RUC> · o · <placa y conductor>
> - Fecha de salida: <dd/mm/aaaa>
>
> Una guía emitida no se edita. ¿La emito?

Si algo de la hoja no coincide con el resumen, no emitir: corregirlo primero.

## Paso 5 · Emitir y entregar

Con el «sí», pulsar el botón del final **una sola vez**. En finangher.com dice
**«Emitir guía»**; en un ambiente de prueba dice «Generar guía en PDF» y no
envía nada a SUNAT.

- Esperar a que la tarjeta **«Guía de remisión»** aparezca en la compra con su
  número y su estado. Si la pantalla no confirma, **no volver a pulsar**: mirar
  si la guía ya figura en la compra.
- Descargar el PDF con el botón de descarga de la tarjeta y entregárselo al
  dueño.
- Recordar: **el transportista necesita la guía antes de salir**. Si el dueño
  quiere, prepararle el mensaje para enviársela.
- La compra queda marcada con «Esta compra ya está en 1 guía». Si en otra guía
  viaja el resto, la hoja muestra lo que ya se envió.

## Desde una venta con envío (la forma más habitual)

Cuando el negocio vende y despacha por agencia, la guía tiene motivo **Venta**
y se hace **una por pedido**, dentro del pedido. Comprobado en un entorno de
prueba de Finangher (nada se envió a SUNAT) con un envío por Shalom a una
oficina de destino.

**Dónde nace el envío (al vender).** En **«VENDER»**, el botón **«Enviar»**
solo aparece después de elegir el cliente. Abre «Destino» (buscar el distrito)
y luego **«Configurar envío»**: método (por ejemplo **Shalom**), **«Agencia
Shalom»** (la oficina de destino), «Quién recibe» (el DNI completa el nombre) y
«Teléfono». Se guarda con **«Guardar envío»**. Ese envío es lo que después
alimenta la guía: si la agencia o el destino están mal, la guía sale mal.

**Pasos para la guía:**

1. Al registrar la venta aparece **«¡Venta Exitosa!»** con el botón
   **«Operaciones»**, que abre el pedido. También se llega desde la pestaña
   Operaciones.
2. En **Cumplimiento**, el pedido está «Por empacar». **La guía va después de
   empacar**: pulsar **«Marcar como empacado»** solo cuando el dueño confirme
   que el paquete está armado (el peso es el del bulto listo).
3. En **«Guía pendiente»**, pulsar **«Revisar datos»**. Se abre **«Datos del
   traslado»** casi completa:
   - salida: la dirección fiscal del negocio (preguntar si despacha desde otro
     local);
   - llegada: la dirección de la agencia elegida en el envío;
   - «¿Quién lleva la mercadería?»: la empresa del envío (por ejemplo Shalom,
     con su RUC);
   - fecha de salida: hoy;
   - destinatario: el cliente de la venta.
4. **Lo único que falta es el peso** («Peso del envío en kilogramos», con el
   embalaje). Preguntarlo al dueño; el botón final no se activa sin él.
   Opcionales: registro MTC y «Orden de compra (opcional)».
5. Resumen fijo y «sí» (como en el Paso 4, con motivo Venta, el cliente como
   destinatario y la agencia como llegada). Después, **«Emitir guía»** una sola
   vez (en un ambiente de prueba dice «Generar guía en PDF»).
6. Aparece la tarjeta **«Guía de remisión»** con su número, «Imprimir» y
   descargar. Entregar el PDF: la agencia y el transportista lo necesitan antes
   de recibir el bulto.

Otras salidas del mismo paso: **«Cargar»** (si la guía ya se emitió por fuera)
y **«Continuar sin guía»**. Usarlas solo si el dueño lo dice.

**Lo que sigue en el pedido.** Este skill solo lo describe; no lo ejecuta sin
pedido expreso:

- «Rótulo del paquete»: «Imprimir» o «Continuar sin rótulo».
- «Entregar en agencia»: código de rastreo y contraseña de retiro, que da la
  agencia al recibir el bulto.
- «Avisar al destinatario»: mensaje por WhatsApp o «Marcar como avisado».
- **Cobro**: «Registrar cobro» abre «Cobrar a <cliente>». Ahí se elige el
  comprobante de la venta (Ninguno, Boleta o Factura).

El comprobante (o el anticipo) es un documento fiscal aparte: **nunca se emite
sin el «sí» del dueño**, y para emitirlo se usa [`registrar-venta`](../registrar-venta/).

## Cuando algo sale mal

| Situación | Qué hacer |
|---|---|
| No aparece «Trasladar mercadería» | Detenerse y decirlo. No inventar otro camino |
| Aparece «Configurar para emitir» | Falta conectar las guías con SUNAT. Decirlo y detenerse |
| La compra no está registrada en Finangher | Integrarla primero con `integrar-compras` |
| Facturas de proveedores distintos | Una guía por proveedor |
| La pantalla rechaza la guía y pide una unidad de medida | Preguntarle al dueño la unidad de esa línea. No elegirla por parecido |
| No confirma después de pulsar | No volver a pulsar. Revisar si la guía ya figura en la compra |
| La guía salió con un dato mal | No se edita. La tarjeta ofrece «Emitir guía corregida»; después la anterior se da de baja en SUNAT (Finangher no puede hacerlo por el dueño). Lo decide el dueño |

## Límites

- **La guía desde la compra llega a finangher.com con la próxima
  actualización.** Mientras tanto, Claude avisa y no inventa pasos.
- **Probado** en un ambiente de prueba de Finangher (nada se envió a SUNAT):
  una guía con motivo Compra, tres facturas del mismo proveedor, 18 productos
  en kilogramos, transporte público con empresa de transporte. Armarla tomó
  unos 18 toques.
- **Probado** en el mismo entorno de prueba: la guía de una venta con envío
  por agencia (Shalom, recojo en oficina), dentro del pedido en Operaciones.
  Una vez empacado, la guía se generó con un solo dato escrito (el peso).
  No se ejecutaron el anticipo, el cobro, el comprobante final, la entrega en
  agencia ni el aviso al cliente.
- **No probado:** el transporte con vehículo propio
  (placa y conductor); otros motivos (devolución, traslado entre locales,
  consignación); compras sin factura electrónica; envíos parciales en varias
  guías.
- Para una empresa de transporte, la pantalla pide el RUC y el registro MTC
  (opcional), **no la placa ni el conductor**. Si el dueño necesita que la
  guía los lleve, decírselo antes de emitir.
- **La guía no se edita una vez emitida.** Se corrige con otra guía.
- No emite guías de transportista, no da de baja guías en SUNAT y no da
  asesoría tributaria.
