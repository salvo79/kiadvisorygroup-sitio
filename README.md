# kiadvisorygroup.com

Sitio de KI Advisory & Strategy Group: HTML estático (sin compilación), listo para servirse desde `public_html` en Hostinger.

**Publicación**: cada push a `main` lo sube solo a Hostinger con `.github/workflows/publicar.yml` (FTP cifrado, solo lo que cambió, nunca borra en el servidor; excluye `.git`, `.github`, `_herramientas` y este README). Necesita los secretos `FTP_SERVIDOR`, `FTP_USUARIO` y `FTP_CLAVE` (y opcionales `FTP_DIRECTORIO`, por omisión `public_html/`, y `FTP_PROTOCOLO`, por omisión `ftps`). También se lanza a mano en Actions › Publicar en Hostinger › Run workflow.

- `index.html`: portada, servicios, enfoque, Infinity Workflow, industrias y metodología
- `infinity-workflow.html`, `contacto.html`
- `socios.html`: sección inactiva, redirige a la portada (el contenido está en el historial de git)
- `servicios.html`, `metodologia.html`, `industrias.html`: redirigen a su sección nueva (enlaces del sitio anterior)
- `en/`: versión en inglés de `index.html`, `infinity-workflow.html` y `contacto.html` (comparten `estilos.css`, `sitio.js` e `img/`); el selector ES | EN del menú lleva a la página equivalente y cada página declara su alterna con `hreflang`
- `estilos.css`, `sitio.js`, `img/`

El formulario «Cuéntenos su desafío» se envía con `contacto.php` por SMTP autenticado de Hostinger (smtp.hostinger.com:465) con las credenciales de `config-correo.php`, un archivo que vive en el servidor **fuera** de `public_html` y no está en GitHub (`<?php return ['usuario' => 'contact@kiadvisorygroup.com', 'clave' => '…'];`); sin ese archivo usa `mail()` de PHP, a contact@kiadvisorygroup.com, con el correo del visitante como «Responder a». Requiere que exista el buzón contact@kiadvisorygroup.com. Los botones «Agendar consulta» abren una ventana con el mismo envío; el sitio no usa enlaces mailto (nada se manda desde el correo del visitante).

## Perspectivas (bocetos de Infinity Workflow)

`perspectivas/` y `en/perspectivas/` se generan con `python3 _herramientas/bocetos.py` a partir de los bocetos de la aplicación
(`WorkflowHD/FE/public/manuales`, y su traducción en `en/`). Cada boceto queda encerrado en `.boceto-sitio`, con la paleta,
las tipografías, la cabecera y el pie del sitio. Al cambiar un boceto en la aplicación, se vuelve a correr el script.

## Idioma

Inglés por omisión. El script de `<head>` de cada página manda a la versión en español si el navegador del visitante
está en español; si el visitante usa el selector ES | EN (que lleva `?idioma=es|en`), el script de `<head>` guarda su elección y esta manda sobre lo automático.
`estilos.css` y `sitio.js` se cargan con `?v=` (versión): al cambiarlos, sube el número en las páginas para que los navegadores no usen una copia vieja.
`x-default` de `hreflang` apunta a la versión en inglés.

## Capturas de Infinity Workflow

`img/app/es/` y `img/app/en/` tienen las capturas reales de la aplicación (JPEG de 1800 px, modo claro, nombres de
personas y clientes sustituidos por ficticios) que usa la sección «La plataforma en acción» de `infinity-workflow.html`
y `en/infinity-workflow.html`: resultados y hallazgos del modelo LP, comparador de escenarios, programa de ventas,
seguimiento de vendedores (mapa y avance), evaluación del plan y análisis multivariable (módulo adicional de analítica).
La sección «CRM» usa además clientes, crm-pedido, pro-asistente y crm-prospectos (escritorio) y m-clientes, m-pedido, m-asistente y m-cobranza (formato de teléfono 393 × 852, en marcos de iPhone y Android hechos con CSS). Para cambiarlas basta con reemplazar el archivo con el mismo nombre en ambos idiomas.
