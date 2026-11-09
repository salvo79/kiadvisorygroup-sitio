// KI Advisory · comportamiento del sitio: menú en el celular, aparición al desplazarse y formulario de contacto
(function () {
    var boton = document.querySelector('.boton-menu');
    var menu = document.querySelector('.menu');
    if (boton && menu) {
        boton.addEventListener('click', function () {
            var abierto = menu.classList.toggle('abierto');
            boton.setAttribute('aria-expanded', abierto ? 'true' : 'false');
        });
        menu.querySelectorAll('a').forEach(function (a) {
            a.addEventListener('click', function () {
                menu.classList.remove('abierto');
            });
        });
    }

    // Aparición suave de las secciones (sin JavaScript se ven igual)
    var elementos = document.querySelectorAll('.aparece');
    if ('IntersectionObserver' in window) {
        var obs = new IntersectionObserver(
            function (entradas) {
                entradas.forEach(function (e) {
                    if (e.isIntersecting) {
                        e.target.classList.add('visible');
                        obs.unobserve(e.target);
                    }
                });
            },
            { threshold: 0.12 }
        );
        elementos.forEach(function (el) {
            obs.observe(el);
        });
    } else
        elementos.forEach(function (el) {
            el.classList.add('visible');
        });

    document.querySelectorAll('.anio').forEach(function (el) {
        el.textContent = new Date().getFullYear();
    });

    // Solicitudes de consulta: se envían desde el sitio con contacto.php a contact@kiadvisorygroup.com (nunca desde el
    // correo del visitante). Lo usan el formulario de la página de contacto y la ventana «Agendar consulta».
    var en = document.documentElement.lang === 'en';
    function enviarSolicitud(form) {
        form.addEventListener('submit', function (ev) {
            ev.preventDefault();
            var d = new FormData(form);
            d.append('idioma', en ? 'en' : 'es');
            var aviso = form.querySelector('.aviso-envio');
            var boton = form.querySelector('button[type="submit"]');
            var mostrar = function (texto, ok) {
                aviso.textContent = texto;
                aviso.style.color = ok ? 'var(--cian-osc)' : '#b91c1c';
                aviso.hidden = false;
            };
            boton.disabled = true;
            mostrar(en ? 'Sending…' : 'Enviando…', true);
            fetch('/contacto.php', { method: 'POST', body: d, headers: { Accept: 'application/json' } })
                .then(function (r) {
                    return r.json();
                })
                .then(function (j) {
                    mostrar(j.mensaje, j.ok);
                    if (j.ok) form.reset();
                })
                .catch(function () {
                    mostrar(en ? 'We could not send your request right now. Please try again in a few minutes.' : 'No pudimos enviar su solicitud en este momento. Intente de nuevo en unos minutos.', false);
                })
                .finally(function () {
                    boton.disabled = false;
                });
        });
    }
    var pagina = document.getElementById('formulario-contacto');
    if (pagina) enviarSolicitud(pagina);

    // Ventana «Agendar consulta»: los botones y enlaces a la página de contacto la abren aquí mismo
    var T = en
        ? { titulo: 'Book an initial consultation', lead: 'Free and with no commitment. A partner will reply within one business day.', nombre: 'Name *', empresa: 'Company', email: 'Email *', tel: 'Phone', area: 'Area of interest *', elija: 'Select an option', areas: ['Strategic planning', 'Operational scheduling', 'Operations implementation', 'Evaluation and follow-up', 'Infinity Workflow', 'Other'], desafio: 'Tell us about your challenge *', enviar: 'Send request', cerrar: 'Close' }
        : { titulo: 'Agendar consulta inicial', lead: 'Sin costo y sin compromiso. Un socio le responde en menos de 24 horas hábiles.', nombre: 'Nombre *', empresa: 'Empresa', email: 'Correo *', tel: 'Teléfono', area: 'Área de interés *', elija: 'Elija una opción', areas: ['Planeación estratégica', 'Programación operativa', 'Implementación de operaciones', 'Evaluación y seguimiento', 'Infinity Workflow', 'Otro'], desafio: 'Cuéntenos su desafío *', enviar: 'Enviar solicitud', cerrar: 'Cerrar' };
    var ventana = null;
    function abrirVentana(interes) {
        if (!ventana) {
            ventana = document.createElement('dialog');
            ventana.className = 'ventana-consulta';
            ventana.setAttribute('aria-labelledby', 'titulo-consulta');
            ventana.innerHTML =
                '<button type="button" class="cerrar-ventana" aria-label="' + T.cerrar + '">×</button>' +
                '<div class="antetitulo">KI Advisory &amp; Strategy</div><h2 id="titulo-consulta">' + T.titulo + '</h2><p class="lead-ventana">' + T.lead + '</p>' +
                '<form class="formulario"><label>' + T.nombre + '<input name="nombre" required autocomplete="name" /></label><label>' + T.empresa + '<input name="empresa" autocomplete="organization" /></label>' +
                '<label>' + T.email + '<input name="email" type="email" required autocomplete="email" /></label><label>' + T.tel + '<input name="telefono" type="tel" autocomplete="tel" /></label>' +
                '<label class="ancho">' + T.area + '<select name="area" required><option value="">' + T.elija + '</option>' + T.areas.map(function (a) { return '<option>' + a + '</option>'; }).join('') + '</select></label>' +
                '<label class="trampa" aria-hidden="true">Web<input name="sitio_web" tabindex="-1" autocomplete="off" /></label>' +
                '<label class="ancho">' + T.desafio + '<textarea name="desafio" rows="4" required></textarea></label>' +
                '<div class="ancho"><button class="boton boton-oscuro" type="submit"><span class="con-flecha">' + T.enviar + '</span></button></div>' +
                '<p class="ancho aviso-envio" hidden role="status" aria-live="polite" style="font-weight: 600"></p></form>';
            document.body.appendChild(ventana);
            ventana.querySelector('.cerrar-ventana').addEventListener('click', function () { ventana.close(); });
            ventana.addEventListener('click', function (e) { if (e.target === ventana) ventana.close(); }); // clic fuera
            enviarSolicitud(ventana.querySelector('form'));
        }
        ventana.querySelector('.aviso-envio').hidden = true;
        if (interes) ventana.querySelector('select[name="area"]').value = interes;
        ventana.showModal();
        ventana.querySelector('input[name="nombre"]').focus();
    }
    document.addEventListener('click', function (e) {
        var a = e.target.closest && e.target.closest('a[href*="contacto.html"]');
        if (!a || a.classList.contains('idioma') || a.hash || e.metaKey || e.ctrlKey || e.shiftKey) return;
        var url = new URL(a.href, location.href);
        if (!/\/contacto\.html$/.test(url.pathname) || (document.getElementById('formulario-contacto') && url.pathname === location.pathname)) return;
        if (typeof HTMLDialogElement !== 'function') return; // navegador muy antiguo: va a la página de contacto
        e.preventDefault();
        abrirVentana(url.searchParams.get('interes'));
    });
})();

// Contacto: «Solicitar una demostración» llega con ?interes=… y preselecciona el área
(function () {
    var area = document.querySelector('#formulario-contacto select[name="area"]');
    var interes = new URLSearchParams(location.search).get('interes');
    if (area && interes) area.value = interes;
})();

// Selector ES | EN: la elección del visitante manda sobre el idioma de su navegador (ver el script de <head>)
document.querySelectorAll('a.idioma').forEach(function (a) {
    a.addEventListener('click', function () {
        try {
            localStorage.setItem('ki_idioma', a.getAttribute('hreflang'));
        } catch (e) {}
    });
});

// WebMCP: herramientas para agentes de IA que corren en el navegador (navigator.modelContext). Solo lectura, salvo
// «preparar consulta», que llena el formulario de contacto para que la persona lo revise y lo envíe.
(function () {
    var mc = navigator.modelContext;
    if (!mc || typeof mc.registerTool !== 'function') return;
    var en = document.documentElement.lang === 'en';
    var raiz = location.origin + (en ? '/en/' : '/');
    var PAGINAS = { empresa: 'index.md', 'infinity-workflow': 'infinity-workflow.md', contacto: 'contacto.md', perspectivas: 'perspectivas/index.md' };
    var texto = function (t) { return { content: [{ type: 'text', text: t }] }; };
    try {
        mc.registerTool({
            name: 'ki_informacion',
            description: en
                ? 'Returns, as Markdown, information from KI Advisory & Strategy Group: the firm and its services, the Infinity Workflow platform (modules, CRM Base and Pro, integrations), insights, or contact details.'
                : 'Devuelve en Markdown información de KI Advisory & Strategy Group: la empresa y sus servicios, la plataforma Infinity Workflow (módulos, CRM Base y Pro, integraciones), perspectivas o datos de contacto.',
            inputSchema: { type: 'object', properties: { tema: { type: 'string', enum: Object.keys(PAGINAS), description: en ? 'Topic to read' : 'Tema a consultar' } }, required: ['tema'] },
            annotations: { readOnlyHint: true },
            execute: function (args) {
                var url = raiz + (PAGINAS[args && args.tema] || PAGINAS.empresa);
                return fetch(url, { headers: { Accept: 'text/markdown' } }).then(function (r) { return r.text(); }).then(function (t) { return texto(t + '\n\n' + url); });
            }
        });
        mc.registerTool({
            name: 'ki_preparar_consulta',
            description: en
                ? 'Opens the KI contact form pre-filled (name, email, company, area of interest, challenge) so the person can review and send it. It does not send anything by itself.'
                : 'Abre el formulario de contacto de KI ya llenado (nombre, correo, empresa, área de interés, desafío) para que la persona lo revise y lo envíe. No envía nada por sí sola.',
            inputSchema: { type: 'object', properties: { nombre: { type: 'string' }, email: { type: 'string', format: 'email' }, empresa: { type: 'string' }, area: { type: 'string' }, desafio: { type: 'string' } } },
            execute: function (args) {
                args = args || {};
                var form = document.getElementById('formulario-contacto');
                if (!form) {
                    location.href = raiz + 'contacto.html' + (args.area ? '?interes=' + encodeURIComponent(args.area) : '');
                    return texto(en ? 'Opening the contact page; call the tool again there to pre-fill the form.' : 'Abriendo la página de contacto; vuelve a llamar la herramienta ahí para llenar el formulario.');
                }
                ['nombre', 'email', 'empresa', 'area', 'desafio'].forEach(function (k) { if (args[k] && form.elements[k]) form.elements[k].value = args[k]; });
                form.scrollIntoView({ behavior: 'smooth' });
                return texto(en ? 'The form is filled in. Ask the person to review it and press Send.' : 'El formulario está llenado. Pide a la persona que lo revise y pulse Enviar.');
            }
        });
    } catch (e) {}
})();
