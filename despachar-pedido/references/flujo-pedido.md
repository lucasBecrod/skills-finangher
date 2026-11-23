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
3. **Sin envío:** en el pedido, **«Enviar»** → «Destino» (buscar el distrito)
   → **«Configurar envío»**: método (por ejemplo **Shalom**), **«Agencia
   Shalom»** (la oficina de destino), «Quién recibe» (el DNI puede completar el
   nombre; si no lo encuentra, escribirlo) y «Teléfono» → **«Guardar envío»**.
   Aparece «Envío agregado» y el pedido vuelve a En proceso. (Lo mismo se
   puede hacer desde la ventana «¡Venta Exitosa!».) Este camino no se recorrió
   todavía en una prueba: si la pantalla muestra otra cosa, detenerse y
   describirla.

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
4. **«Rótulo del paquete»:** «Imprimir» o «Continuar sin rótulo».
5. **«Entregar en agencia»:** código de rastreo y contraseña de retiro, del
   ticket de la agencia. **«Confirmar entrega en agencia».**
6. **«Avisar al destinatario»:** mensaje de WhatsApp listo («Ya enviamos tu
   pedido #<código> por Shalom… Apenas completes el pago te envío el código de
   seguimiento y la clave de retiro…») o **«Marcar como avisado»**.

## Cobro del saldo y comprobante final

1. En el pedido, **«Registrar cobro»** → «Cobrar a <cliente>» con el saldo.
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
