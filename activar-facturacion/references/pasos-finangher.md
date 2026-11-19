# Pasos en Finangher

Ruta: **Configuración › Facturación** (`finangher.com/configuracion/facturacion`),
con el negocio que va a emitir activo en la sesión. Cada fila abre una hoja a la
derecha; al guardar, la fila cambia de «Falta» a su estado.

Claude puede abrir las filas, elegir opciones y dejar listo el formulario. **Los
campos de clave los escribe el dueño**: clave del usuario SOL secundario,
contraseña del certificado y código para facturar.

## Antes de empezar

- **Dirección fiscal.** Si Finangher dice «Falta tu dirección fiscal», se
  completa en Configuración (datos del negocio) antes que todo: va impresa en
  cada comprobante.
- Si la pantalla pregunta «Quiero configurar facturación / No quiero
  facturación», elegir la primera.

## 1. Régimen tributario

Fila **Régimen tributario** › «¿Cómo declaras tus impuestos?»:

- **NRUS · pago S/ 20 o S/ 50 cada mes** — solo emite boletas, sin IGV
  discriminado.
- **Régimen Especial, MYPE o General** — puede emitir boletas y facturas.

Elegir lo que dijo el dueño y guardar. Es una declaración sobre el negocio: no
necesita certificado.

## 2. Usuario SOL secundario

Grupo **Conectar con SUNAT** › fila **Usuario SOL secundario**. Usuario:
`FINANGHE` (el que se creó en SOL, sin la R final). El dueño escribe
el usuario y la clave que creó en SOL (paso A de
[pasos-sunat.md](pasos-sunat.md)). Al guardar, la fila dice «Guardado».

- Camino certificado: **obligatorio**.
- Camino PSE: no lo necesita para emitir, pero se recomienda (compras de SUNAT).

La fila **Credenciales API SUNAT** («Para consultas SIRE y emisión de guías»)
no es necesaria para la primera boleta. Dejarla para después.

## 3. Firma de tus comprobantes

Fila **Firma de tus comprobantes** › «¿Cómo firmarás tus comprobantes?».

### Camino certificado — «Tengo mi certificado digital»

1. Elegir **Tengo mi certificado digital**.
2. Seleccionar el archivo `.pfx`/`.p12`.
3. El dueño escribe la contraseña en el campo «La que creaste al descargarlo».
4. **Guardar certificado.** Debe aparecer «Certificado guardado». Si dice «No
   pudimos guardar el certificado · Revisa el archivo y la clave», casi siempre
   es la contraseña: que la vuelva a escribir con cuidado (mayúsculas incluidas).

La fila pasa a «Con tu certificado».

### Camino PSE — «No tengo certificado»

1. Elegir **No tengo certificado** («Autoriza a un PSE para firmar en tu
   nombre»).
2. La hoja muestra **«Habilita este RUC en tu Clave SOL»** con el RUC y la razón
   social del PSE, **Copiar** y **Abrir Clave SOL**. El dueño hace el paso E de
   [pasos-sunat.md](pasos-sunat.md).
3. Solo si el negocio es PRICO o agente de retención/percepción, marcar la
   casilla correspondiente: el PSE no se activa y hay que emitir por OSE.
4. Pulsar **Ya lo habilité en SUNAT**. Aparece «RUC autorizado.».
   Errores posibles: RUC no activo o no habido, falta la dirección fiscal, el
   RUC necesita un OSE, o «No pudimos verificar tu RUC en SUNAT, intenta en unos
   minutos».
5. La hoja dice **«Falta un paso · Aún no puedes emitir»** y pide el **Código
   para facturar**. Ese código lo entrega Finangher después de registrar el RUC
   en el PSE: usar «¿No tienes el código? Pídelo por WhatsApp», que ya trae el
   RUC en el mensaje.
6. Cuando el dueño lo tenga, **él lo pega** en «Pega el código aquí» y pulsa
   **Guardar código**. Debe decir «Código guardado. Ya puedes emitir.» y
   «Listo para emitir».

La fila pasa a «Con el PSE». La hoja muestra «Tus series: B… y F…».

## 4. Tipo de afectación del IGV

Grupo **Emisión electrónica** › **Tipo de afectación del IGV**. Se activa
**una sola**, según dónde está el negocio:

- **Fuera de la Amazonía → «IGV Impuesto General a las Ventas» (18 %).**
- **En la Amazonía → «IGV Exonerado»** (y la casilla «Régimen Amazonía — Ley
  27037» que aparece debajo).

Preguntar al dueño en qué zona está si no se puede leer de su dirección fiscal.
Las demás (Tasa Reducida MYPE 8 %, Inafecto, Exportación) no se activan salvo
que el dueño o su contador lo indiquen expresamente.

Con Nuevo RUS la fila dice «No aplica (Nuevo RUS)»: no se toca.

## 5. Comprobantes electrónicos

Fila **Comprobantes electrónicos**. Se habilita recién con la firma lista
(antes dice «Requiere firma configurada»). Finangher propone las series (por
ejemplo B002 y F002). Revisarlas con el dueño:

- Si ya emitía con otro sistema y esa serie existe en SUNAT, **no repetirla**:
  usar otra (los números se cruzarían).
- El número empieza en 1 salvo que el dueño diga lo contrario.

El interruptor **Envío de comprobantes a SUNAT** debe quedar activado.

## 6. Precios (opcional, no bloquea)

Grupo **Política de precios**: «Cómo cargas tus precios» (si el precio que
escribe ya trae el impuesto) y «Cómo mostrar tus precios». Vienen bien por
defecto (precio con impuesto incluido). Tocarlos solo si el dueño lo pide.

## Señales de listo

- Firma: «Con tu certificado» o «Con el PSE».
- «Listo para emitir comprobantes».
- Etiqueta **Emisión real** (no «Entorno de pruebas»).
