# Pasos en SUNAT (los hace el dueño)

Todo esto ocurre en **SUNAT Operaciones en Línea (SOL)**, con el RUC y la
Clave SOL **principal** del dueño:
`https://e-menu.sunat.gob.pe/cl-ti-itmenu/MenuInternet.htm`

Claude dicta un paso por mensaje y pregunta qué ve. Los nombres de menú de SOL
cambian con el tiempo: si no aparece una opción, pedir una captura y buscarla
por su nombre en el buscador del menú antes de rendirse.

---

## A. Usuario SOL secundario

**Qué es, para explicárselo al dueño:** es un acceso restringido que el dueño le
da a Finangher. SUNAT tiene miles de funciones; este usuario solo puede entrar a
las que el dueño marca con check (las de comprobantes electrónicos), y nada
más: no ve ni toca declaraciones, pagos, deudas ni el resto de su SUNAT. La
Clave SOL principal sigue siendo solo del dueño, y él puede suspender o
eliminar este usuario cuando quiera desde la misma pantalla.

Lo usa **el sistema**, nunca una persona: Finangher lo necesita para emitir con
certificado propio y para traer las compras de SUNAT.

**Una sola clave para todo.** Antes de empezar, el dueño elige **una clave**
que usará para el usuario secundario y, más adelante, para el certificado
digital. Así no se confunde de clave. Regla para que sirva en los dos:
**10 a 12 caracteres, solo letras y números (sin @, puntos ni símbolos), con al
menos una mayúscula, una minúscula y un número.** SOL acepta de 8 a 12
caracteres (lo dice al pie del formulario); el certificado exige que sea
alfanumérica y algunos certificados comprados piden al menos 10. La escribe y
la anota el dueño; Claude no la ve ni la dicta.

1. En SOL, menú **Bienvenido ▾ › Administración de usuarios secundarios ›
   Crear Usuario**. La pantalla lista los secundarios que ya existen.
   - **Si ya hay uno llamado `FINANGHE` activo**, es el de Finangher: no crear
     otro. Ir al paso 3 con ese usuario.
   - **Si `FINANGHE` aparece como «Eliminado»**, SUNAT no deja volver a usar
     ese nombre. Crear otro que el dueño reconozca como del sistema (por
     ejemplo `FACTURAS`).
2. Llenar el registro: tipo y número de documento de la persona (con DNI,
   SUNAT completa nombres y apellidos), usuario **`FINANGHE`** (sin la R final:
   así el dueño sabrá en el futuro que ese usuario es del sistema de
   Finangher) y la clave, dos veces. El correo se deja vacío: es opcional y no
   se le pide al dueño. Pulsar **Siguiente**.
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
   pago**. Ahí hay dos ramas, y en **cada hoja de las dos** se marcan **todas
   sus casillas, sin dejar ninguna**:

   - **SEE - Del Contribuyente y Envío de Documentos** (3 hojas): Servicio de
     Envío de Documentos Electrónicos · Certificado Digital · Consultar Envíos
     de CPE.
   - **Factura Electrónica** (7 hojas): Certificado Digital · Correo
     Electrónico · Consultar Factura, Boletas y Notas · Comunicación de
     Tercerización con PSE · Comprobante de Retención Electrónico ·
     Comprobante de Percepción Electrónico · Guía de Remisión.

   Hacer clic en cada hoja del árbol de la izquierda; sus casillas aparecen a
   la derecha y la casilla de arriba («Opción») las marca todas. Pasar a la
   siguiente hoja (SOL conserva lo marcado). Al final, **Siguiente** guarda.
   «Resumen de opciones asignadas» muestra lo vigente. Nada de Aduaneros ni
   Bienes Fiscalizados.

**Fin del tramo 1:** llevar ya el usuario `FINANGHE` y su clave a Finangher
(Usuario SOL secundario) y confirmar «Guardado» antes de seguir.

## A2. Credenciales API SUNAT

Sirven para que Finangher consulte SIRE (compras y ventas) y emita guías. Se
crean con la Clave SOL principal.

1. En el buscador del menú escribir **API** y elegir **Gestión Credenciales de
   API SUNAT**. Se abre «API SUNAT · REGISTRE SU APLICACIÓN».
   - **Si el formulario ya muestra una aplicación con ID y CLAVE**, no crear
     otra: se usa esa misma. Pulsar el **lápiz** (editar), **Seleccionar
     Todos** los programas y actualizar, sin cambiar nombre ni URL. Luego
     llevar ese mismo ID y CLAVE a Finangher y saltar al fin del tramo 2.
2. **Nombre de su aplicación:** `Finangher`. **URL de su aplicación:**
   `https://finangher.com`.
3. **Seleccionar Todos** los programas de la lista.
4. Más abajo, en la misma pantalla: tipo de aplicación **Desktop**, no Web.
5. **Guardar**. SUNAT muestra el **ID** y la **CLAVE**. El dueño los copia
   directamente a Finangher; no se dictan ni se pegan en el chat.

**Fin del tramo 2:** pegar en Finangher (Credenciales API SUNAT) y confirmar
«Guardadas» antes de seguir. Los nombres cambian entre una pantalla y otra:

| SUNAT | Finangher |
|---|---|
| ID | ID (en versiones anteriores, «Client ID») |
| CLAVE | Clave (en versiones anteriores, «Client secret») |

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
3. Al generarlo, SOL pide una contraseña para el archivo. El dueño escribe **la
   misma clave que eligió para el usuario secundario** (por eso se pidió solo
   letras y números). La necesitará en Finangher.
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
