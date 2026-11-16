# Skills de Finangher

Skills de código abierto para que tu agente (Claude) haga tareas del día a día
de un negocio peruano. Las publica [Finangher](https://finangher.com) y son
gratis: úsalas, cópialas y mejóralas.

| Skill | Qué hace |
|---|---|
| [`rastrear-envio`](rastrear-envio/) | Le das a Claude el número de orden y el código de tu ticket de Shalom y te responde en qué estado está el envío. |

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

## Licencia

[MIT](LICENSE). Hecho por Finangher.
