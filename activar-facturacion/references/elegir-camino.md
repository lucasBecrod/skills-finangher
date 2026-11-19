# Elegir el camino de la firma

SUNAT pide una **firma digital** en cada boleta y factura. Hay dos maneras de
tenerla en Finangher. El resto de la configuración es igual en las dos.

| | Certificado propio | PSE |
|---|---|---|
| Quién firma | El negocio, con su certificado | Un Proveedor de Servicios Electrónicos autorizado por SUNAT, en nombre del negocio |
| Qué necesita el dueño | Un certificado `.pfx`/`.p12` y su contraseña, registrado en SUNAT | Autorizar al PSE en SOL y un código para facturar que entrega Finangher |
| Costo del certificado | Gratis si SUNAT le da el CDT; si no, se compra a una entidad acreditada | No necesita certificado |
| Vence | El certificado vence (normalmente en 1 a 3 años) y hay que renovarlo | No vence mientras la autorización siga activa |
| Cambiar después | Se puede pasar al PSE desde la misma pantalla | «Volver a mi certificado» desde la misma pantalla |

Cambiar de camino **no cambia la serie ni reinicia el número** de los
comprobantes.

## Datos del PSE que usa Finangher

Finangher no firma ni es un PSE: usa uno. El que se autoriza en SOL es:

- **RUC:** 20602186793
- **Razón social:** INTAI S.A.C. (Facturita)

Finangher muestra estos mismos datos en «Firma de tus comprobantes › No tengo
certificado», con un botón para copiar el RUC. Si la pantalla muestra otro RUC,
**manda la pantalla**: usar ese y anotar la diferencia en la bitácora.

## Árbol de decisión

1. **¿SUNAT muestra el RUC como no activo o no habido?** → No se puede activar
   todavía. Regularizar en SUNAT.
2. **¿Es PRICO, agente de retención o de percepción?** → SUNAT lo obliga a
   emitir por OSE. Estos caminos no sirven; escribir a Finangher.
3. **¿Ya tiene a mano un archivo `.pfx`/`.p12` vigente con su contraseña?** →
   Se sube ese. Casi nunca pasa: no asumirlo ni preguntarlo como primera opción.
4. **¿Ya pidió el certificado gratuito dos veces?** → SUNAT no da un tercero:
   *PSE* o certificado comprado.
5. **Todos los demás (también Nuevo RUS)** → **ir a pedir el certificado
   gratuito de SUNAT (CDT)**. Es el camino por defecto: se obtiene en la misma
   sesión y no depende de Finangher. SUNAT lo da a quien cumple sus requisitos
   (los vigentes están en `https://cpe.sunat.gob.pe/certificado-digital`); para
   saber si el negocio califica, no se adivina: se pide y SOL responde. Si SOL
   no lo da, anotar el motivo que muestra y pasar al *PSE* (o a un certificado
   comprado si el dueño prefiere).

Por qué este orden: si se pregunta «¿tienes certificado?», todos dicen «no» y
terminan en el PSE, esperando a que Finangher registre su RUC y les entregue el
código. Con el CDT el dueño termina solo y en el momento.

## Cómo proponerlo

Una propuesta, con su razón, y la alternativa en una línea:

> Te recomiendo pedir el certificado gratuito de SUNAT: tu régimen MYPE suele
> tenerlo y se obtiene en el momento. Si SUNAT no te lo da, usamos el PSE y no
> necesitas certificado. ¿Vamos?
