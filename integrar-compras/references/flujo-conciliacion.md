# Cómo se integra una compra de SUNAT en Finangher (web)

Recorrido verificado el 2026-11-17 navegando la página Conciliación (los
arreglos publicados el 2026-11-18 ya están incorporados), en
computadora, con la sesión del dueño iniciada. Los textos entre «comillas» son
los que se leen en pantalla; si uno no aparece, leer la pantalla antes de seguir.

## Antes de empezar

- El negocio debe tener conectada su cuenta de SUNAT (Configuración →
  Facturación electrónica). Sin eso, Conciliación no trae nada.
- Si la cuenta tiene varios negocios, comprobar cuál está activo en la insignia
  de arriba a la derecha; se cambia en «Ver todos mis espacios».

## 1. Traer lo que SUNAT informa

1. Menú lateral → **Conciliación**. Abre en la pestaña «Mes», en el mes actual.
2. La tarjeta del mes tiene el botón **Consultar a SUNAT**. Si una consulta
   falla, muestra el motivo junto al botón.
3. Al responder, la tarjeta dice «SUNAT consultado el <fecha>» y debajo aparece
   «Lo que SUNAT ya conoce de tu negocio» → «Compras · a tus proveedores», con
   una fila por proveedor: «N comprobantes · M por registrar».
4. Cada mes se consulta por separado, con la flecha «Mes anterior» o el
   selector «Elegir mes».
5. Las facturas con fecha de meses pasados aparecen aparte: «SUNAT te propone N
   compras de meses anteriores», con «Revisar».

Un mes puede tardar: «SUNAT está preparando tus comprobantes…». La página se
vuelve a leer sola; no insistir seguido. El mes que se mira queda en la
dirección de la página y sobrevive a una recarga. «Consultar» en la vista Año
consulta de verdad y consume lo mismo que la consulta mensual.

## 2. Abrir una compra

1. Tocar la fila del **proveedor**. Abre su ficha con el historial.
2. Tocar la factura «Por registrar». Abre «Factura <número> · Pendiente de
   registrar».
   Abrir una factura tarda 10 a 15 segundos («Generando representación
   gráfica…»); esperar.
3. **Registrar compra**. No se adjunta ningún archivo: Finangher trae la factura
   de SUNAT y abre la hoja «Comprar» ya llena con cada línea, el total y el
   proveedor.

## 3. Asociar cada ítem

Cada línea trae el botón **Asociar**. Mientras falte alguna, la hoja dice «Falta
asociar N producto(s) antes de registrar» y el botón de registrar está apagado.

1. **Asociar** abre «Asociar producto»: arriba la línea de la factura, un
   buscador, el botón «Nuevo» y el catálogo, con el «Más parecido» primero.
2. **Si el producto ya existe**: elegirlo. La línea queda asociada.
3. **Si tiene variantes**: elegir la presentación que corresponde a la unidad de
   la factura. La pantalla confirma con «Entrarán N kilogramos a tu stock (10 ×
   Saco x 40 kilogramo)»; comparar ese número con la factura.
4. **Si no existe**: «Nuevo» (abre con el nombre de la factura; cambiarlo por el
   nombre que usa el negocio) → «Producto» o «Servicio» → «Continuar».

Cuenta de pasos: cada línea son dos o tres acciones (buscar, elegir, variante).
Una factura de 11 líneas ronda los 25 pasos.

Después de asociar, **leer cómo quedó la línea**: cantidad, unidad y precio por
unidad.

## 4. Pago y registro

- **La hoja abre con una cuenta ya marcada** (por ejemplo Yape) y «Registrar»
  se activa al asociar la última línea. Cambiar el pago al que dijo el dueño
  antes de pulsar nada.
- **Al elegir la forma de pago, la lista de ítems se pliega.** Queda solo una
  fila («2 items · S/ …») o desaparece de la vista. No se perdió nada: tocar esa
  fila la vuelve a desplegar. Desplegarla y revisar las líneas otra vez antes
  de registrar.
- El comprobante queda en «Ninguno», con la nota «Esta compra ya tiene la
  factura de tu proveedor». **No tocar «Liquidación de compra».**
- Forma de pago:
  - **Al contado** → elegir la cuenta (Efectivo, Yape, Plin…) → «Registrar S/ …».
  - **A crédito** → avisa «La deuda quedará en S/ …» → «A crédito S/ …».
  - **Dividir monto** → una fila por medio de pago; el resto puede quedar como
    saldo pendiente.
- Al registrar aparece «¡Compra Exitosa!».

## 5. Comprobar

| Qué | Dónde |
|---|---|
| Quedó registrada | Conciliación: la factura pasa a «Registrada» y baja el contador del proveedor |
| Inventario | Mi catálogo: el disponible del producto subió en la cantidad comprada |
| Pago al contado | Inicio: el saldo de la cuenta bajó por el total |
| Deuda | Contactos: el proveedor muestra «Le debes S/ …» |
| Comprobante | En la compra: la factura con «Descargar» (PDF) y el XML |
| Producto nuevo | Mi catálogo → «Lo que compro» |

La compra queda con la fecha de la factura, no con la de hoy.

## Lo que la pantalla ya resuelve sola

- Proveedor, ítems, cantidades y total vienen de la factura.
- **Recuerda las asociaciones.** Cuando el mismo proveedor vuelve a facturar el
  mismo ítem, el producto que se eligió la vez anterior aparece primero como
  «Más parecido», aunque su nombre no se parezca. No lo asocia sola: hay que
  elegirlo.
- El nombre del catálogo no cambia: el producto conserva el nombre del negocio
  y la compra conserva el texto del proveedor.

## Trampas conocidas

- **«Más parecido» no es «correcto».** La primera vez es solo parecido de
  nombre, y puede proponer algo que no tiene nada que ver.
- **Unidades que no coinciden.** Si la factura dice «1 unidad» y el producto del
  catálogo se mide en «kilogramo» y no tiene variantes, la línea pasa a «1
  kilogramo» sin avisar. Comparar la unidad de la factura con la de la línea
  asociada; si difieren, preguntar al dueño antes de registrar.
- **Caja sin fondos.** Se puede pagar al contado desde una cuenta que no tiene
  ese dinero y queda en negativo, sin aviso. El saldo no se ve desde la hoja
  «Comprar»: mirarlo en Inicio antes de abrir la compra.
- **Líneas con precio cero.** Son entregas gratuitas del proveedor. Cada línea
  de la factura lleva su motivo (bonificación por la compra, publicidad,
  muestra…): leerlo en la factura abierta, no preguntárselo al dueño. Se asocian
  como cualquier otra línea: la cantidad entra al inventario y no suma al total
  a pagar. En Observaciones se ponen con su motivo («4 productos de
  bonificación, sin costo»). Preguntar solo si la factura no muestra el motivo.
- **Notas de crédito y anuladas.** Una nota de crédito aparece como compra «por
  registrar» con monto negativo, y la factura que anula sigue visible en la
  ficha del proveedor como anulada. Ninguna de las dos se registra como compra.
- **La forma de pago no se toma de la factura.** Aunque diga «Contado», la hoja
  deja elegir cualquiera.
- **La memoria no asocia sola.** Aunque el mismo proveedor repita el ítem, hay
  que volver a elegir el producto en cada factura.
- **Tras registrar, el primer clic puede perderse** y cerrar la ficha del
  proveedor que quedó detrás. Mirar la pantalla antes de volver a pulsar.
- **«No es del negocio».** Las compras por registrar de meses anteriores ofrecen
  esa opción. No usarla sin que el dueño lo diga: descarta la compra.
- **Factura sin detalle.** Dice «Productos por completar · SUNAT no entregó el
  detalle de esta factura» y ofrece «Subir XML» y «Registrar compra». Pedir el
  XML al dueño y subirlo. Si solo hay PDF, leer de ahí los ítems y cargarlos a
  mano con «Registrar compra», comprobando que la suma dé el total de SUNAT. No
  registrar a ciegas.
- **«Necesita tu decisión».** El mes puede traer «Compras por revisar» y
  «Compras sin comprobante». Informarlo; no resolverlo sin el dueño.
- **Compras que no son mercadería** (comisiones bancarias, servicios): se
  integran igual, asociadas a un servicio; no mueven inventario.

## Cuando el proveedor también usa Finangher

Si el proveedor emite su factura desde Finangher, la compra **aparece sola** en
el negocio que compra, sin pasar por Conciliación. Antes de integrar una factura
de SUNAT, buscarla en Inicio → «Operaciones recientes» y en la ficha del
proveedor (Contactos): si ya está, no registrarla otra vez.

- Llega con el producto ya asociado. Si el negocio no lo tenía, se crea solo en
  Mi catálogo → «Lo que compro», y el inventario sube.
- **No mueve dinero sola.** Dice «Pagado», pero la cuenta queda en «Seleccionar
  cuenta»; el saldo baja recién cuando se elige. Preguntar al dueño de qué
  cuenta salió.
- Una entrega gratuita (bonificación, donación) llega como «Entrega gratuita ·
  S/ 0.00»: sube el inventario y no pide cuenta.
- No aparece en la página Operaciones ni en Conciliación del mes.

## Si una línea quedó en el producto equivocado

La compra con factura no se edita («Editar» y «Eliminar» están apagados; el
motivo apunta a Inicio → Operaciones recientes) y la
línea no se puede apuntar a otro producto. Por eso la asociación se revisa
**antes** de registrar. Si igual quedó mal, **el inventario sí se corrige**:
en Mi catálogo, cada producto tiene movimientos de stock de tipo ajuste (compra
no registrada antes, error de conteo, pérdida…). Se resta del producto
equivocado y se suma al correcto, con el visto bueno del dueño. El comprobante
no cambia.

## No probado todavía

Facturas de más de 11 líneas, compra por saco con venta por kilo, subir el
XML o cargar a mano desde el PDF una factura que llegó sin detalle, notas de crédito de un proveedor, vincular una compra que ya se había registrado a mano, una factura
que mezcla líneas pagadas y gratuitas, y el recorrido en celular. En estos
casos, detenerse y confirmar con el dueño.
