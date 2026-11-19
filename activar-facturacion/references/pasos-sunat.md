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
   Crear Usuario**. La pantalla lista los secundarios que ya existen.
   - **Si ya hay uno llamado `FINANGHE` activo**, es el de Finangher: no crear
     otro. Ir al paso 3 con ese usuario.
2. Llenar el registro: tipo y número de documento de la persona (con DNI,
   SUNAT completa nombres y apellidos), usuario **`FINANGHE`** (sin la R final:
   así el dueño sabrá en el futuro que ese usuario es del sistema de
   Finangher) y una clave de 8 a 12 caracteres, dos veces. El correo es
   opcional. **El dueño escribe la clave y la anota él**, en un lugar seguro;
   no se dicta a Claude. Pulsar **Siguiente**.
   - **Alto: un DNI, un solo secundario activo.** Si SUNAT responde «Ya existe
     un usuario (…) con este número de documento. ¿Desea dar
     permanentemente de baja al usuario anterior y crear este nuevo
     usuario?», **no continuar**. Pulsar **Cancelar** y preguntarle al dueño
     qué es ese usuario: si lo usa su contador u otro sistema, darlo de baja
     lo deja sin acceso. Opciones: crear `FINANGHE` con el documento de otra
     persona del negocio, o reutilizar el secundario existente si el dueño
     confirma que ya no lo usa nadie.
3. **Asignar Programas** (o, para un usuario que ya existe, seleccionarlo y
   **Modificar Programas**). En el árbol: **TRIBUTARIOS › Comprobantes de
   pago**, y marcar:

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

Vale alrededor de S/ 300 (3 años): es justo lo que el dueño quiere si no tiene
certificado; de lo contrario tendría que comprar uno. **Antes de enviar,
confirmar que el negocio no tiene ya un certificado vigente**: si lo tiene, no
pedir el CDT sin que el dueño lo decida.

**SUNAT lo da solo dos veces por RUC** (experiencia de Finangher en las
activaciones). Se puede pedir un segundo antes de que venzan los 3 años, pero
después no hay un tercero: desde entonces el negocio tiene que comprar un
certificado o usar un PSE. Por eso:

- Preguntar si ya lo pidió antes. Si ya lo pidió dos veces, no intentarlo: ir
  al camino PSE o a un certificado comprado.
- Enviar la solicitud **una sola vez** y en una computadora, con tiempo para
  terminar RENIEC, la contraseña y la descarga en la misma sesión.
- **La contraseña del certificado no se puede olvidar**: el dueño la anota
  antes de generar. Perder el archivo o la contraseña gasta una de las dos
  oportunidades.

1. En SOL, en el buscador del menú escribir **certificado** y elegir
   **Solicitar Certificado Digital Tributario**. Se abre «Solicitud de
   Certificado Digital Tributario» con RUC, razón social, correo y celular del
   contribuyente. Si un dato está mal, se corrige primero en SUNAT.
   - Marcar **Acepto los términos y condiciones** y pulsar **Enviar
     Solicitud**. Lo pulsa el dueño, con su «sí».
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

Fuente: guía del PSE «Guía para ALTA SUNAT como proveedores de servicios
electrónicos a INTAI SAC» (Facturita, versión 2.0; capturas de 2020–2021, el
menú de SOL puede verse distinto hoy).

1. En sunat.gob.pe: **Operaciones en Línea (SOL) › Mis trámites y consultas ›
   Ingresar**. El dueño escribe RUC, usuario y clave SOL y pulsa **Iniciar
   sesión**.
2. En el menú, pestaña **Empresas**.
3. **Comprobantes de pago › Factura Electrónica › Comunicación de
   Tercerización con PSE › Altas/Bajas de PSE**. Se abre «COMUNICACIÓN
   TERCERIZACIÓN CON PSE», con una tabla (RUC, Razón Social, Inicio
   Autorización, Fin Autorización, Baja).
   - **Si la tabla ya muestra `20602186793` sin fecha de fin**, el alta ya
     existe: no crear otra. Ir al paso 7.
4. Botón **Alta Servicio** (debajo de la tabla). Se abre «Alta de
   autorización de PSE».
5. En **RUC**, el dueño pega `20602186793` (o el que muestre Finangher) y
   pulsa el botón **«…»** al costado. SUNAT completa la razón social: debe
   decir **INTAI SOCIEDAD ANONIMA CERRADA**. Si sale otra o ninguna, el RUC está
   mal escrito: no guardar.
6. En **Inicio Autorización Envío**, elegir la fecha más próxima que SUNAT
   permita (siempre posterior a hoy) y pulsar **Guardar**. La tabla debe
   listar el RUC del PSE, su razón social y esa fecha de inicio. Pedirle al
   dueño una captura de esa tabla, para él.
7. Volver a Finangher y pulsar **«Ya lo habilité en SUNAT»**.

El PSE puede emitir por el negocio **desde la fecha de inicio** que se guardó.
Si la primera venta es antes, esperar a esa fecha y decírselo al dueño antes de
terminar.
