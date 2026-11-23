# Los mensajes de Claude en el chat del equipo

Siempre el mismo molde para cada momento, con los mismos bloques en el mismo
orden: el equipo aprende dónde mirar. Se envían como **mensaje normal de
texto**, sin botones ni formularios, y se responden escribiendo o dictando
«sí», «no» o el cambio.

Los datos se copian de la pantalla de Finangher con el documento ya armado,
no del mensaje del equipo.

**Antes de emitir no se envía ningún PDF ni nada con aspecto de hoja.** El
borrador es este texto. El PDF va después, cuando el documento ya existe.

Los moldes de comprobante son los de
[`registrar-venta`](../../registrar-venta/references/confirmacion.md), con lo
propio del pedido (anticipo descontado, saldo, envío). Sus reglas de bloque
valen aquí. El molde del anticipo (al vender) está en
[`registrar-venta`](../../registrar-venta/references/proforma-anticipo-envio.md#molde-de-anticipo).

## Guía

```
**GUÍA DE REMISIÓN** de <negocio> · motivo Venta · pedido <código>

**Para:** <cliente> · <RUC|DNI> <número>
**Sale de:** <dirección de partida, distrito>
**Llega a:** <agencia> <oficina de destino>
**Lleva:** <agencia> (transporte público)
**Carga:** <n> bultos · <peso> kg · <n> productos
**Fecha de salida:** <hoy, dd/mm/aaaa>

¿Emito la guía? Responde **sí** o dime el cambio.
```

Después de emitir: «Guía <serie-número> emitida. Aquí el PDF. El rótulo
<impreso | va en el PDF para imprimir>.»

## Envío guardado

```
Guardado en el pedido <código>:
**Orden:** <número de orden> · **Clave:** <clave>
Revisa que coincidan con el ticket.

Reviso el envío el <día> a las <hora> y te aviso, <nombre de quien vende>.
```

## Llegó

```
@<quien vende> el pedido <código> de <cliente> ya está en <agencia> <oficina
de destino> desde el <fecha>.
Saldo por cobrar: S/ <saldo>.
```

Si sigue en camino al tercer día:
«@<quien vende> el pedido <código> sigue <estado> desde el <fecha>. Dejo de
revisarlo; avísame si quieres que vuelva a mirar.»

## Comprobante final

```
**FACTURA** de <negocio> para <razón social> · RUC <número>

| Producto | Cant. | Precio | Importe |
|:---|---:|---:|---:|
| <producto> | <cant.> | <precio> | <importe> |
| **Impuestos** (IGV 18 %) | | | <igv> |
| **Total del pedido** | | | <total> |
| **Anticipo** (<serie-número>) | | | −<anticipo> |
| **A pagar** | | | **S/ <saldo>** |

**Pago:** S/ <saldo> por <medio>
**Entrega:** te pregunto al emitir

¿Emito? Responde **sí** o dime el cambio.
```

Después de emitir: «Factura <serie-número> emitida, descuenta el anticipo
<serie-número>. Pedido <código> cobrado. Aquí el PDF. Recuerda pasarle al
cliente la orden y la clave de retiro.»

## Estado

Una línea, en el orden del pedido:

```
Pedido <código> de <cliente>: <Por empacar | Por despachar | En agencia desde <fecha> | Entregado> · cobro <pendiente S/ x | parcial, saldo S/ x | completo> · <comprobantes emitidos>.
```
