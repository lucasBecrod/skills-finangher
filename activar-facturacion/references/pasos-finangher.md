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

Se configura siempre, en cualquier camino, igual que la fila **Credenciales API
SUNAT** (tramo 2): todo se deja hecho en la misma sesión de SUNAT, para que el
dueño no tenga que volver a entrar ni escribir claves otra vez.

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
**una sola**. Claude **pregunta, recomienda y marca solo con el «sí» del
dueño**: es su situación tributaria, no una decisión de Claude. Si el dueño
duda, que lo confirme con su contador antes de vender.

Hacer estas preguntas en orden y quedarse con la primera que aplique:

1. **«¿Tu negocio está en la Amazonía y vendes para consumo allí?»** (se puede
   leer de la dirección fiscal: Loreto, Ucayali, Madre de Dios, San Martín,
   Amazonas y zonas de selva de otros departamentos). Si sí →
   **«IGV Exonerado»** y la casilla **«Régimen Amazonía — Ley 27037»** que
   aparece debajo, que pone en el PDF la leyenda de la Amazonía. La
   exoneración exige requisitos (domicilio y actividad en la zona); si no está
   seguro, contador.
2. **«¿Tu negocio es restaurante, hotel o alojamiento turístico?»** Si sí,
   puede corresponderle **«IGV Tasa Reducida MYPE»**, pero solo si cumple todo
   (Ley 31556 y su reglamento, DS 237-2022-EF):
   - es micro o pequeña empresa, con ventas de hasta 1700 UIT al año;
   - al menos el **70 %** de sus ingresos vienen de esas actividades;
   - no está vinculado económicamente con otras empresas o grupos.

   Si deja de cumplir, pierde la tasa desde el mes subsiguiente. Por eso
   Claude la **recomienda, pero pide que la confirme el contador**; nunca la
   marca por defecto. No decir el porcentaje de memoria: la tasa cambia por
   año (Ley 32219); decir «la tasa reducida que muestra Finangher».
3. **Ninguna de las dos (por ejemplo, un negocio en Lima)** → solo **«IGV
   Impuesto General a las Ventas» (18 %)**.

Inafecto y Exportación no se activan salvo que el dueño o su contador lo
indiquen expresamente.

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
