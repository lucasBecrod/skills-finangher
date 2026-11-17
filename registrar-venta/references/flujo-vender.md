# Cómo se vende en Finangher (web)

Recorrido verificado el 2026-11-16 en `finangher.com`, en computadora, con la
sesión del dueño ya iniciada. Se opera por los textos visibles de la pantalla;
si un texto no aparece, leer la pantalla antes de seguir, no adivinar.

## Dónde

`https://finangher.com/marketplace/<tienda>?mode=pos` abre el punto de venta
directo; también se llega con el botón **Vender** del menú izquierdo. A la izquierda queda el catálogo con «Buscar producto»; a la derecha,
el carrito con el cobro.

## Pasos

| # | Acción | Qué debe verse después |
|---|---|---|
| 1 | **Vender** | Carrito a la derecha, pestaña «Venta» activa (no «Proforma») |
| 2 | Escribir el producto en **Buscar producto** y pulsar el **+** de su tarjeta | El producto en el carrito con su precio de catálogo |
| 3 | **+ Añadir cliente** → escribir RUC o DNI → elegir el resultado | Nombre y documento del cliente en el carrito |
| 4 | Marcar **Ninguno**, **Boleta** o **Factura** | El círculo del comprobante elegido |
| 5 | **Al contado** o **A crédito**; al contado, elegir el medio (Efectivo, Yape, banco…) | El medio con el monto completo |
| 6 | Verificar (paso 3 del SKILL) y pulsar **Vender S/ …** | «Registrando venta» y luego el comprobante con su serie y número |

El **+** de la tarjeta se llama «Agregar 1» para los lectores de pantalla; en
un producto con variantes dice «Elegir entre N opciones» y hay que elegir la
variante del pedido (si el pedido no la dice, preguntar). El precio del
catálogo es el que muestra la tarjeta, aunque lleve una etiqueta de descuento.

Para cambiar la cantidad, usar el control del ítem en el carrito. Para un precio
acordado distinto, **Editar total acordado** → escribir el total → Enter (solo
si el dueño pidió ese precio).

## El cliente

- En el Perú una misma persona puede tener **DNI y RUC** (el RUC 10 lleva su
  DNI dentro). En la cartera aparecen como dos contactos. Es normal: si el
  pedido dice DNI, se elige el del DNI y **no hace falta avisarlo**. Solo se
  menciona en Observaciones si el pedido no decía con cuál documento.
- El nombre que muestra el carrito es el de la agenda del dueño; el comprobante
  sale con el nombre oficial de RENIEC o SUNAT. Pueden diferir.
- Con el carrito sin cliente, el botón dice **Público general**; con cliente,
  **Quitar cliente** lo retira. Cualquiera de los dos abre la ventana «¿A quién le vendes?» con el campo
  «Buscar contacto». Ahí se escribe el documento.
- **Si salen varios resultados**, elegir el que muestra el mismo tipo y número
  de documento del pedido (un DNI y un RUC de la misma persona son clientes
  distintos para el comprobante). Si ninguno coincide exacto, usar «Buscar DNI
  … en RENIEC» o preguntar.
- Si el pedido trae nombre y Finangher muestra otro, detenerse y preguntar. Si
  el pedido solo trae el número, decir en la respuesta final qué nombre mostró
  Finangher.

- Al escribir un **DNI** o un **RUC** completo, Finangher consulta el nombre o
  la razón social (tarda unos 2 segundos) y lo ofrece para elegir. Vale igual
  para un cliente nuevo que para uno de la cartera.
- Un contacto guardado solo con nombre y celular no desbloquea la boleta con
  documento: el carrito ofrece «DNI o RUC» para completarlo ahí mismo.
- Sin cliente, la venta queda «sin identificar»: sirve para «Ninguno» y para
  boletas de hasta S/ 700.

## El buscador de productos

Busca primero en el catálogo del negocio; si no encuentra, ofrece productos de
otros catálogos y, al final, crear uno con texto libre. **Este skill solo
vende productos del catálogo del negocio**: si el buscador no lo encuentra ahí,
o muestra varios parecidos, aplicar la regla «El producto tiene que ser del
negocio» del SKILL. La pantalla no marca de qué catálogo viene cada resultado;
ante la duda, comprobarlo en **Mi catálogo**. Crear un producto desde aquí (el
botón verde «Agregar») es un recorrido **no probado** por este skill.

## Lo que la pantalla ya resuelve sola

- **Impuestos.** Salen de la configuración del negocio y del producto. No hay
  nada que marcar; solo leer la línea «Impuestos» y compararla con el tratamiento del negocio.
- **Precio.** Viene del catálogo, ya como precio final.
- **Razón social y dirección** del cliente al escribir su RUC.
- **Serie y correlativo** del comprobante.

## Trampas conocidas

- **El carrito recuerda la venta anterior.** Comprobante, «Al contado» y el
  medio de pago pueden venir ya marcados con lo de la última venta. No darlos
  por buenos: marcar de nuevo los de este pedido y verificarlos.
- **Pantalla de la venta anterior.** Si al entrar se ve «¡Venta Exitosa!», es
  la venta pasada: **Nueva** abre un carrito limpio.
- **Productos de nombre casi igual.** Al buscar pueden salir dos (por ejemplo
  uno a S/ 0.00). Si el pedido no permite distinguirlos sin duda, preguntar; si
  se eligió uno, decirlo en Observaciones.
- **En resultados de búsqueda el + se llama «Aumentar cantidad»**, no «Agregar
  1». El botón verde «Agregar» junto al buscador crea un producto nuevo: no
  usarlo.
- **«Enviar» y «Cita» del carrito** son el envío del producto y una reserva, no
  el envío del comprobante.
- **Tras la venta**, junto a «Boleta B00X-N · PDF» están «Descargar», «Enviar el
  archivo del comprobante», «Imprimir» y «Más opciones de compartir». El número
  de la boleta puede tardar unos segundos más que «¡Venta Exitosa!».

- **La línea «Impuestos» aparece recién al marcar Boleta o Factura.** Con
  «Ninguno» el carrito solo muestra los ítems y el total. Leerla y anotarla
  antes de vender: la pantalla de éxito ya no la muestra.
- **El ítem se compacta** al añadir el cliente («Lector S/ 69.00»). La cantidad
  se lee en «N item» y en la insignia de la tarjeta del producto.
- **Dos botones «Agregar 1» por tarjeta** (la tarjeta entera y el + interior):
  cualquiera agrega una unidad; pulsar uno solo.
- **«Al contado» no se anuncia como marcado** para lectores de pantalla:
  confirmarlo en una captura, donde se ve resaltado, y en que el medio de pago
  muestre el monto completo.
- **Pantalla de éxito.** Primero «Registrando venta… Tu venta está guardada»,
  luego «¡Venta Exitosa!» con «Boleta B00X-N · PDF».

- **Carrito que no está limpio.** Lo que manda es el contenido del carrito, no
  el aviso de arriba. Un carrito limpio dice «No hay artículos en la cuenta»,
  no tiene cliente y el botón dice «Vender S/ 0.00»: se usa sin preguntar,
  aunque arriba aparezca «Hay ventas recuperadas listas para corregir en el
  carrito» (ese aviso habla de ventas guardadas aparte). Si el carrito **ya
  trae ítems o cliente**, puede venir con otro precio: detenerse y preguntar al
  dueño antes de usarlo o vaciarlo.
- **Factura bloqueada.** Si «Factura» no se deja marcar, el cliente no tiene
  RUC identificado.
- **La emisión tarda.** Entre «Vender» y el número del comprobante pasan unos
  10 a 30 segundos. Esperar; no pulsar de nuevo.
- **Descarga.** Tras la venta, el botón **Descargar** entrega el PDF.

## Entregar el comprobante

Recorrido verificado el 2026-11-16 desde la pantalla «¡Venta Exitosa!»:

| # | Acción | Qué debe verse después |
|---|---|---|
| 1 | **Más opciones de compartir** | Campo «Número de teléfono» (con +51), «Enviar por correo», «Copiar link», «Vista del cliente» |
| 2 | Escribir el celular y pulsar **Compartir** | El campo pasa a mostrar el número guardado («Editar teléfono +51 …») y aparece **Enviar por WhatsApp** |
| 3 | **Enviar por WhatsApp** | Se abre una pestaña de WhatsApp con el chat de ese número y el mensaje ya escrito |
| 4 | Comprobar el chat y enviar **una vez** | El mensaje en el chat, con la hora |

**Hoy «Enviar por WhatsApp» no adjunta el PDF**: abre el chat con un texto largo
(comprobante validado, documento, impuestos, enlace de descarga y una línea de
publicidad). El cliente espera el archivo, así que en el paso 4 **no se envía
ese texto**: se borra el borrador, se adjunta el PDF descargado con
**Adjuntar → Documento** y se escribe el mensaje de una línea del SKILL como
pie. Se envía una vez.

- Si el contacto ya tenía celular, el paso 2 no hace falta: el número viene
  propuesto.
- La pestaña que abre Finangher (`api.whatsapp.com`) pide elegir entre la
  aplicación y WhatsApp Web. Si WhatsApp Web no tiene la sesión del negocio en
  esa pestaña, usar la pestaña de WhatsApp que el dueño ya tiene abierta.
- Sin WhatsApp a mano: «Copiar link» entrega el mismo enlace del comprobante.

## Comprobar después

**Operaciones** (menú izquierdo) lista la venta con su comprobante. Es la
fuente para saber si una venta se registró cuando la pantalla no lo confirmó.

## No probado todavía

«Enviar por correo», operación gratuita y de exportación (se eligen en las opciones fiscales del
comprobante, la flecha junto a «Factura»; si el pedido pide una y no se
encuentra la opción, detenerse y avisar), venta a crédito, adelanto con «Dividir
monto», moneda distinta de soles, envío y cita desde
este skill, y el recorrido en celular.
