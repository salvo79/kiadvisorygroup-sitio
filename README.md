# kiadvisorygroup.com

Sitio de KI Advisory & Strategy Group: HTML estático (sin compilación), listo para servirse desde `public_html` en Hostinger.

- `index.html`: portada, servicios, enfoque, Infinity Workflow, industrias y metodología
- `infinity-workflow.html`, `contacto.html`
- `socios.html`: sección inactiva, redirige a la portada (el contenido está en el historial de git)
- `servicios.html`, `metodologia.html`, `industrias.html`: redirigen a su sección nueva (enlaces del sitio anterior)
- `en/`: versión en inglés de `index.html`, `infinity-workflow.html` y `contacto.html` (comparten `estilos.css`, `sitio.js` e `img/`); el selector ES | EN del menú lleva a la página equivalente y cada página declara su alterna con `hreflang`
- `estilos.css`, `sitio.js`, `img/`

El formulario de contacto abre el correo del visitante dirigido a salvador.delira@kiadvisorygroup.com.
