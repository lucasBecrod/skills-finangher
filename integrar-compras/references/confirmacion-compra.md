# El mensaje de confirmación de una compra

Mismo criterio que el de ventas: un molde fijo, pocos bloques, siempre en el
mismo orden. Se envía como mensaje normal de la conversación. Los datos se
copian de la pantalla con la compra ya armada.

## Molde de una compra

```
**COMPRA** de <tu negocio> a <proveedor> · <FACTURA> <serie-número> · <fecha>

| En la factura | Cant. | En tu catálogo | Importe |
|:---|---:|:---|---:|
| <descripción del proveedor> | <cant.> | <tu producto> | <importe> |
| <descripción del proveedor> | <cant.> | ＋ <producto nuevo> | <importe> |
| **Total** | | | **S/ <total>** |

**Pago:** <Yape, al contado | a crédito | S/ <x> ahora por <cuenta>, saldo S/ <y>>
**Inventario:** <sube en N productos | no cambia (servicio)>

⚠️ **Observaciones**
- <una línea por cada cosa que el dueño debe mirar>
(omitir el bloque si no hay ninguna)

¿Registro? Responde **sí** o dime el cambio.
```

## Reglas de cada bloque

**Primera línea.** Qué es, de qué negocio, a quién y con qué factura.

**Tabla.** Dos nombres por fila: cómo lo llamó el proveedor y cómo se llama en
el catálogo del negocio. Es el corazón del mensaje: ahí el dueño ve si el
emparejamiento es correcto. Un producto que se va a crear lleva «＋» delante.
Hasta 20 filas, todas; con más, las que tienen «＋», las que van en
Observaciones y las 5 de mayor importe, y una fila «… y N ítems más ya
asociados».

**Pago.** El que dijo el dueño para esta compra.

**Inventario.** Qué va a cambiar al registrar. Si la compra es solo de
servicios, se dice que no cambia.

**⚠️ Observaciones.** Solo cuando hay algo:

- Un ítem que el proveedor llama distinto y se asoció por indicación del dueño.
- Un producto que se va a crear, y si es producto o servicio.
- La factura dice una forma de pago y el dueño indicó otra.
- Una unidad de medida rara en la factura («kilogramo» para algo que no se pesa).
- Una compra de un mes anterior.

**Cierre.** Siempre la misma frase.

## Molde de un lote

Para varias compras del mismo proveedor que se resuelven igual:

```
**<N> COMPRAS** de <tu negocio> a <proveedor> · <mes o rango>

| Factura | Fecha | Ítems | Total |
|:---|:---|---:|---:|
| <serie-número> | <fecha> | <n> | <total> |
| **Total** | | | **S/ <total>** |

**Pago:** <igual para todas>
**Inventario:** <resumen de lo que sube>

¿Registro las <N>? Responde **sí**, dime cuáles no, o dime el cambio.
```

## Después de la respuesta

- **Sí** → registrar, una por una, comprobando cada una.
- **Un cambio** → hacerlo, verificar y reenviar el molde completo.
- **No**, otra cosa o silencio → no registrar.
