# Venta desde una proforma, con anticipo o con envío

Tres variantes de la misma venta. Recorridas en un entorno de prueba de
Finangher en noviembre de 2026 con una factura y un envío por Shalom. Después
de vender, el pedido sigue con [`despachar-pedido`](../../despachar-pedido/).

## Desde una proforma

1. **Operaciones** → abrir la proforma del cliente. Revisar «Válida hasta»
   dentro de la proforma (la lista puede decir «vence Ahora» aunque la fecha
   sea otra). Si venció, decirlo y preguntar si se vende igual.
2. Tocar **«Venta»**: el carrito se arma con los productos y el cliente de la
   proforma. Verificarlo igual con el Paso 3 de la skill.
3. No usar el botón del enlace que ve el cliente («Aceptar y pagar») para
   cobrar: en la prueba mostró el monto sin IGV.

## Con envío

Si el pedido dice adónde va, configurarlo al vender:

1. **«Enviar»** (aparece después de elegir el cliente) → «Destino» (buscar el
   distrito) → **«Configurar envío»**: método (por ejemplo **Shalom**),
   **«Agencia Shalom»** (la oficina de destino), «Quién recibe» (el DNI puede
   completar el nombre; si no lo encuentra, escribirlo) y «Teléfono».
2. **«Guardar envío».** El chip muestra «Shalom (<distrito>) → <nombre>».

Si el pedido no lo dice, no inventarlo: el envío se puede agregar después
desde Operaciones (ver `despachar-pedido`).

## Con anticipo (una parte ahora, el resto después)

El anticipo es un **comprobante real** por la parte que se paga ahora: se
confirma con el «sí» como cualquier comprobante.

1. **Leer el pago** del comprobante que mandaron (captura de Yape, Plin o
   transferencia): monto, fecha y a quién se pagó. Si no se lee, si fue a otra
   cuenta o no coincide con lo que dice el pedido, preguntar. Nunca registrar
   un pago que no se pudo leer.
2. **«Dividir monto»**: el monto del anticipo con su medio.
3. **«Permitir fiado»** para el saldo («S/ x se registrará como deuda»).
4. Activar **«Emitir Factura por anticipo»** («Factura de S/ x ahora»; con
   boleta, lo mismo).
5. Confirmar con el molde de anticipo (abajo). Con el «sí», el botón dice
   **«A crédito S/ <saldo>»**: pulsarlo una vez.
6. **Desde una proforma no aparece «¡Venta Exitosa!»:** Finangher abre directo
   el pedido, con «1 anticipo · falta factura» y el anticipo «Aceptado». En
   una venta normal aparece «¡Venta Exitosa!» con el botón «Operaciones».
7. Enviar el PDF del anticipo **ya emitido**. Antes de emitir, solo el texto
   del molde.

## Molde de anticipo

Mismas reglas que [confirmacion.md](confirmacion.md):

```
**FACTURA de anticipo** de <negocio> para <razón social> · RUC <número>

| Concepto | Cant. | Importe |
|:---|---:|---:|
| Anticipo · pedido de <productos o proforma> | 1 | <base> |
| **Impuestos** (IGV 18 %) | | <igv> |
| **Total** | | **S/ <anticipo>** |

**Pedido:** S/ <total> · saldo S/ <saldo> a crédito
**Pago:** S/ <anticipo> ahora por <medio>
**Opciones:** <envío por <agencia> a <destino> | ninguna>
**Entrega:** te pregunto al emitir

¿Emito? Responde **sí** o dime el cambio.
```

Con boleta: «**BOLETA de anticipo** … para <nombre> · DNI <número>».
