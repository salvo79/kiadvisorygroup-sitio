# kiadvisorygroup.com

Sitio de KI Advisory & Strategy Group: HTML estático (sin compilación), listo para servirse desde `public_html` en Hostinger.

- `index.html`: portada, servicios, enfoque, Infinity Workflow, industrias y metodología
- `infinity-workflow.html`, `contacto.html`
- `socios.html`: sección inactiva, redirige a la portada (el contenido está en el historial de git)
- `servicios.html`, `metodologia.html`, `industrias.html`: redirigen a su sección nueva (enlaces del sitio anterior)
- `en/`: versión en inglés de `index.html`, `infinity-workflow.html` y `contacto.html` (comparten `estilos.css`, `sitio.js` e `img/`); el selector ES | EN del menú lleva a la página equivalente y cada página declara su alterna con `hreflang`
- `estilos.css`, `sitio.js`, `img/`

El formulario de contacto abre el correo del visitante dirigido a contact@kiadvisorygroup.com.

## Perspectivas (bocetos de Infinity Workflow)

`perspectivas/` y `en/perspectivas/` se generan con `python3 _herramientas/bocetos.py` a partir de los bocetos de la aplicación
(`WorkflowHD/FE/public/manuales`, y su traducción en `en/`). Cada boceto queda encerrado en `.boceto-sitio`, con la paleta,
las tipografías, la cabecera y el pie del sitio. Al cambiar un boceto en la aplicación, se vuelve a correr el script.

## Idioma

Inglés por omisión. El script de `<head>` de cada página manda a la versión en español si el navegador del visitante
está en español; si el visitante usa el selector ES | EN, su elección (guardada en el navegador) manda sobre lo automático.
`x-default` de `hreflang` apunta a la versión en inglés.
