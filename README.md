# Skills de Finangher

Skills de código abierto para que tu agente (Claude) haga tareas del día a día
de un negocio peruano. Las publica [Finangher](https://finangher.com) y son
gratis: úsalas, cópialas y mejóralas.

| Skill | Qué hace |
|---|---|
| [`rastrear-envio`](rastrear-envio/) | Le das a Claude el número de orden y el código de tu ticket de Shalom y te responde en qué estado está el envío. |
| [`registrar-venta`](registrar-venta/) | Le pides a Claude una boleta o factura y la arma en tu Finangher, te muestra el resumen, la emite con tu «sí» y le envía el PDF a tu cliente. |

## rastrear-envio

Claude consulta la página pública de rastreo de Shalom
(`shalom.com.pe/rastrea`) con los dos datos impresos en el ticket y te
responde el estado: En origen, En tránsito, En destino o Entregado, con sus
fechas.

- **No pide contraseña** ni inicia sesión en Shalom Pro.
- **Solo consulta.** No crea guías ni modifica nada.
- La consulta tarda unos segundos y no abre ninguna ventana.

### Qué necesitas

- [Claude Code](https://claude.com/claude-code), en la aplicación de escritorio o en la terminal.
- [Node.js](https://nodejs.org) 18 o más reciente.
- El ticket del envío: **número de orden** y **código** de 4 caracteres.

### Instalar

La forma fácil: abre Claude Code y pídeselo.

> Instala la skill rastrear-envio de https://github.com/lucasBecrod/skills-finangher

A mano:

```bash
git clone https://github.com/lucasBecrod/skills-finangher.git
mkdir -p ~/.claude/skills
cp -r skills-finangher/rastrear-envio ~/.claude/skills/
cd ~/.claude/skills/rastrear-envio
npm install playwright
npx playwright install chromium
```

Abre una conversación nueva en Claude Code para que cargue la skill.

### Usar

Escríbele a Claude como le escribirías a una persona:

> ¿Dónde está mi pedido de Shalom? Orden 100000000, código AB12

También puedes correr el guion directamente:

```bash
node ~/.claude/skills/rastrear-envio/scripts/rastrear-shalom.js 100000000 AB12
```

### Límites que debes conocer

- Probado en una computadora personal (Mac). No está probado en servidores en la nube.
- Consulta un pedido a la vez, cuando alguien pregunta. No está hecho para revisar cientos de pedidos seguidos.
- Si Shalom cambia su página, la skill avisa que no pudo consultar; no inventa un estado.
- La página de Shalom muestra el nombre y el DNI de quien recogió. La skill no los repite salvo que se lo pidas.
- El número de orden y el código permiten ver el estado de ese envío: no los publiques.

Este proyecto no es de Shalom ni está afiliado a Shalom. Usa su página pública
de rastreo igual que lo haría una persona.

## registrar-venta

Le pides a Claude una boleta o una factura como se lo pedirías a una persona, y
Claude la arma en tu Finangher. Antes de emitir te muestra un resumen fijo y
espera tu «sí».

- **Revisa que el pedido esté completo.** Si falta el producto, el cliente, el
  comprobante o la forma de pago, te lo pregunta en un solo mensaje.
- **No decide tus impuestos.** Usa lo que tu negocio ya tiene configurado en
  Finangher y verifica la línea de impuestos antes de vender.
- **Solo emite con tu confirmación**, y pulsa «Vender» una sola vez.
- **No pide ni escribe contraseñas.** Tú inicias sesión; Claude opera tu sesión.
- Al terminar te ofrece enviarle el PDF a tu cliente por WhatsApp.
- No emite notas de crédito ni anula comprobantes.

### Qué necesitas

- Una cuenta en [Finangher](https://finangher.com) con tu negocio configurado:
  productos en el catálogo y, si vas a emitir comprobantes, la facturación
  electrónica activada.
- Un Claude que pueda operar tu navegador con tu sesión iniciada (por ejemplo,
  Claude con su extensión para Chrome, o Claude Code con una herramienta de
  navegador).

### Instalar

Abre Claude Code y pídeselo:

> Instala la skill registrar-venta de https://github.com/lucasBecrod/skills-finangher

A mano:

```bash
git clone https://github.com/lucasBecrod/skills-finangher.git
mkdir -p ~/.claude/skills
cp -r skills-finangher/registrar-venta ~/.claude/skills/
```

No tiene dependencias que instalar: son instrucciones para Claude.

### Usar

> Emite una boleta de 2 polos talla M al DNI 40000001, pagó por Yape

La primera vez Claude lee de Finangher cómo está configurado tu negocio y te
pide confirmar una sola cosa: si tus ventas llevan IGV o están exoneradas.

### Límites que debes conocer

- Probada en computadora, en `finangher.com`, emitiendo boletas al contado. Lo
  que todavía no está probado (crédito, adelantos, operaciones gratuitas o de
  exportación, moneda distinta de soles) está listado en la propia skill, y en
  esos casos Claude siempre te pide confirmación.
- La instalación desde cero en otra computadora no está probada.
- Un comprobante emitido no se borra: se corrige con otro comprobante. Por eso
  la skill pregunta antes de emitir.
- Si Finangher cambia una pantalla, Claude lee lo que ve y se detiene ante la
  duda; no adivina.

## Licencia

[MIT](LICENSE). Hecho por Finangher.
