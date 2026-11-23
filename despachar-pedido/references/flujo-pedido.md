# El pedido en Finangher, pantalla por pantalla

Recorrido en un entorno de prueba de Finangher en noviembre de 2026, con un
colaborador «Claude» y envío por Shalom a una oficina de destino. Empieza
cuando la venta ya está registrada. Los nombres
entre comillas son los que muestra la pantalla; si una pantalla dice otra
cosa, detenerse, describir lo que se ve y anotarlo en la bitácora.

## Abrir el pedido

La venta la registra [`registrar-venta`](../../registrar-venta/) (también
desde proforma, con anticipo o con envío:
[proforma-anticipo-envio.md](../../registrar-venta/references/proforma-anticipo-envio.md)).

1. **Recién vendido:** «¡Venta Exitosa!» → botón **«Operaciones»**. Desde una
   proforma no aparece esa ventana: Finangher abre directo el pedido.
2. **Después:** menú **Operaciones** → el pedido. El pedido muestra
   Cumplimiento, Cobro («Parcial» con el saldo, si hubo anticipo) y
   Comprobante («1 anticipo · falta factura», si hubo anticipo).
3. **Sin envío:** el pedido figura «Entregado / Entregado a <cliente>» (venta
   de mostrador). En Cumplimiento, **«Alistar pedido»** abre dos opciones:
   «Recoger aquí» y **«Enviar a otro lugar»**. Elegir esta → «Destino» (buscar
   el distrito) → **«Configurar envío»**: método (por ejemplo **Shalom**),
   **«Agencia Shalom»** (la oficina de destino), «Quién recibe» (el DNI puede
   completar el nombre; si no lo encuentra, escribirlo) y «Teléfono» →
   **«Guardar envío»**. Aparece «Pedido en alistamiento» y el pedido pasa a
   «Por empacar». El menú «Acciones» del pedido solo trae «Editar venta» y
   «Eliminar»: el envío no se agrega desde ahí.

## Cumplimiento: empacar, guía, rótulo, agencia, aviso

Todo está en el pedido (Operaciones → el pedido), bloque **Cumplimiento**:

1. «Por empacar» → **«Marcar como empacado»**.
2. **«Guía pendiente»** → **«Revisar datos»** → «Datos del traslado», casi
   completo. Falta **«Peso del envío en kilogramos»**; el botón final no se
   activa sin él. Revisar la fecha de salida: la hoja puede mostrarla en
   formato mes/día (`11/22/2026`).
3. **«Emitir guía»** (en un entorno de prueba dice «Generar guía en PDF»). La
   tarjeta «Guía de remisión» queda con «Imprimir» y descargar. En la pantalla
   del pedido el número puede verse cortado («T00…»): leerlo del PDF.
4. **«Rótulo del paquete»:** «Imprimir», «Compartir rótulo PDF», «Descargar
   rótulo PDF» o «Continuar sin rótulo». Solo «Imprimir» (queda «Rótulo
   preparado») o «Continuar sin rótulo» hacen avanzar el pedido; descargar o
   compartir el PDF no.
5. **«Entregar en agencia»:** «CÓDIGO DE RASTREO» y «CONTRASEÑA DE RETIRO
   (OPCIONAL)», del ticket de la agencia. **«Confirmar entrega en agencia».**
   Si no cambia nada, recargar la página, reabrir el pedido y confirmar una
   vez.
6. **«Avisar al destinatario»:** mensaje de WhatsApp listo («Ya enviamos tu
   pedido #<código> por Shalom… Apenas completes el pago te envío el código de
   seguimiento y la clave de retiro…») o **«Marcar como avisado»**.

## Cobro del saldo y comprobante final

1. En el pedido, **«Registrar cobro»** → «Cobrar a <cliente>» con el saldo.
   La hoja no muestra los productos ni el IGV, y la cuenta de cobro aparece
   enmascarada («Yape ****XXXX»).
2. Medio de pago y comprobante. Con anticipo, la pantalla indica que la
   factura descuenta el anticipo. **«Cobrar S/ <saldo>»**, una vez.
3. El pedido queda con Cobro «Cobrado» y Comprobante con el anticipo y la
   factura final. El número final puede verse cortado: leerlo del PDF.

## Trampas vistas

| Trampa | Qué hacer |
|---|---|
| Números de guía y factura cortados en el pedido | Leerlos del PDF o del bloque del comprobante |
| El colaborador ve ventas antiguas del negocio en Operaciones | Abrir el pedido por cliente y código; no tomar otro |
| En el buscador de productos o clientes un clic no pasa | Esperar a que la lista termine de cargar y volver a tocar el resultado; si sigue igual, anotarlo |
| La factura dice «Forma de pago: Contado» aunque haya saldo a crédito | Anotarlo en la bitácora; no corregirlo a mano |
| La factura final escribe en letras («SON: …») el total del pedido, no el importe a pagar | Anotarlo en la bitácora; el importe a pagar correcto está en la línea «Importe a pagar» |
| «Confirmar entrega en agencia» no responde después de agregar el envío en la misma pantalla | Recargar, reabrir el pedido y confirmar una vez |
| En la lista, el pedido en agencia dice «En tránsito»; dentro, «Enviado» con «Entregado en agencia» | Es el mismo estado: el paquete está en la agencia |
