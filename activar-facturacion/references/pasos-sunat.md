# Pasos en SUNAT (los hace el dueño)

Todo esto ocurre en **SUNAT Operaciones en Línea (SOL)**, con el RUC y la
Clave SOL **principal** del dueño:
`https://e-menu.sunat.gob.pe/cl-ti-itmenu/MenuInternet.htm`

Claude dicta un paso por mensaje y pregunta qué ve. Los nombres de menú de SOL
cambian con el tiempo: si no aparece una opción, pedir una captura y buscarla
por su nombre en el buscador del menú antes de rendirse.

---

## A. Usuario SOL secundario

Es una credencial que el dueño crea para que **el sistema** (no una persona)
trabaje con SUNAT sin conocer la clave principal. Finangher la usa para emitir
con certificado propio y para traer las compras de SUNAT.

1. En SOL, menú **Bienvenido ▾ › Administración de usuarios secundarios ›
   Crear usuario**.
2. El dueño elige el nombre de usuario (por ejemplo `FACTURAS`) y
   una clave. **Los anota él**, en un lugar seguro; no se dictan a Claude.
3. **Modificar Programas** del usuario y marcar, en *Comprobantes de pago*:

   | Rama | Opción |
   |---|---|
   | SEE - Del Contribuyente y Envío de Documentos › Servicio de Envío de Documentos Electrónicos | Servicio de Envío de Documentos Electrónicos por Servicio Web |
   | SEE - Del Contribuyente › Certificado Digital | Registro y Mantenimiento de Correo y Certificados Digitales |
   | SEE - Del Contribuyente › Consultar Envíos de CPE | Todas las consultas de envío y «Consultar Disponibilidad del Servidor» |
   | Factura Electrónica › Certificado Digital | Registro y Mantenimiento de Correo y Certificados Digitales |
   | Factura Electrónica › Correo Electrónico | Actualizar Correo Electrónico |
   | Factura Electrónica › Consultar Factura, Boletas y Notas | Consultar Factura, Boletas y Notas |
   | Factura Electrónica › Comunicación de Tercerización con PSE | Altas/Bajas de PSE |
   | Comprobante de Retención / de Percepción / Guía de Remisión | Sus consultas |

   Hacer clic en cada hoja del árbol de la izquierda, marcar sus opciones a la
   derecha y pasar a la siguiente (SOL conserva lo marcado). Al final,
   **Siguiente** guarda. «Resumen de opciones asignadas» muestra lo vigente.
   Nada de Aduaneros ni Bienes Fiscalizados.

## B. Certificado gratuito de SUNAT (CDT)

1. En SOL, buscar **Certificado Digital Tributario** (en *Comprobantes de pago
   › SEE - Del Contribuyente*) y solicitarlo.
2. SOL dice si el RUC puede obtenerlo. Si no, **copiar el motivo tal cual** y
   volver a [elegir-camino.md](elegir-camino.md).
3. Al generarlo, SOL pide una contraseña para el archivo. El dueño la escribe y
   la guarda; la necesitará en Finangher.
4. Descargar el archivo (`.pfx` o `.p12`) a la computadora donde se abrirá
   Finangher.
5. Seguir con **D** para confirmar que quedó como emisor del SEE - Del
   Contribuyente.

## C. Certificado comprado a una entidad acreditada

La entidad acreditada (por ejemplo Girasol) entrega
el certificado en un archivo `.pfx`/`.p12` con su contraseña y, aparte, la
parte pública `.cer`. La descarga suele ser **de una sola vez**: bajar el
certificado y la contraseña en ese momento.

1. En SOL: **Comprobantes de pago › SEE - Del Contribuyente › Certificado
   Digital › Registro y Mantenimiento de Correo y Certificados Digitales**.
2. Registrar el correo y **subir el archivo `.cer`** (la parte pública; el
   `.pfx` con la clave privada nunca se sube a SUNAT, va a Finangher).
3. Seguir con **D**.

## D. Casilla «SEE - Del Contribuyente» (camino certificado)

En la misma pantalla de *Registro y Mantenimiento de Correo y Certificados
Digitales*, marcar **«Deseo emitir a través del SEE - Del Contribuyente»** y
guardar.

**La calidad de emisor rige desde el día calendario siguiente.** Si se marca
hoy, la primera boleta se emite mañana. Decírselo al dueño antes de terminar,
para que no se sorprenda.

### Si la primera boleta vuelve con 0111

`0111 — No tiene el perfil para enviar comprobantes electrónicos` en la
**primera** boleta casi siempre es esta casilla: no se marcó, o se marcó hoy.

1. Preguntar si la marcó y cuándo.
2. Si no la marcó, marcarla.
3. **No eliminar la venta.** El número no llegó a SUNAT; se reintenta al día
   siguiente y sale con el mismo número.

## E. Autorizar al PSE (camino PSE)

1. En SOL: **Comprobantes de pago › Factura Electrónica › Comunicación de
   Tercerización con PSE › Altas/Bajas de PSE**.
2. **Alta Servicio.** Escribir el RUC del PSE que muestra Finangher
   (`20602186793`, INTAI S.A.C.) y la **fecha de inicio**. SOL solo acepta una
   fecha posterior a hoy: poner la más próxima que permita.
3. Guardar y pedirle al dueño una captura de la constancia, para él.
4. Volver a Finangher y pulsar **«Ya lo habilité en SUNAT»**.

El PSE puede firmar desde la fecha de inicio. Si la primera venta es antes,
esperar a esa fecha.
