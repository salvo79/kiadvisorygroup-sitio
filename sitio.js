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

    // Formulario «Cuéntenos su desafío»: lo envía contacto.php a contact@kiadvisorygroup.com; si el servidor no
    // responde, abre el correo del visitante con la solicitud ya escrita
    var form = document.getElementById('formulario-contacto');
    if (form) {
        form.addEventListener('submit', function (ev) {
            ev.preventDefault();
            var d = new FormData(form);
            var en = document.documentElement.lang === 'en';
            d.append('idioma', en ? 'en' : 'es');
            var aviso = document.getElementById('mensaje-enviado');
            var boton = form.querySelector('button[type="submit"]');
            var mostrar = function (texto, ok) {
                aviso.textContent = texto;
                aviso.style.color = ok ? 'var(--cian-osc)' : '#b91c1c';
                aviso.hidden = false;
            };
            var porCorreo = function () {
                var e = en ? ['Name', 'Company', 'Job title', 'Email', 'Phone', 'Area of interest', 'Industry', 'Timeframe', 'Initial consultation'] : ['Nombre', 'Empresa', 'Cargo', 'Correo', 'Teléfono', 'Área de interés', 'Industria', 'Horizonte', 'Consulta inicial'];
                var lineas = [e[0] + ': ' + d.get('nombre'), e[1] + ': ' + (d.get('empresa') || '—'), e[2] + ': ' + (d.get('cargo') || '—'), e[3] + ': ' + d.get('email'), e[4] + ': ' + (d.get('telefono') || '—'), e[5] + ': ' + d.get('area'), e[6] + ': ' + (d.get('industria') || '—'), e[7] + ': ' + (d.get('horizonte') || '—'), '', d.get('desafio')];
                window.location.href = 'mailto:contact@kiadvisorygroup.com?subject=' + encodeURIComponent(e[8] + ' · ' + (d.get('empresa') || d.get('nombre'))) + '&body=' + encodeURIComponent(lineas.join('\n'));
                mostrar(en ? 'Your email app opened with the request ready to send. If it didn’t open, write to us at contact@kiadvisorygroup.com.' : 'Se abrió su correo con la solicitud lista para enviar. Si no se abrió, escríbanos a contact@kiadvisorygroup.com.', true);
            };
            boton.disabled = true;
            mostrar(en ? 'Sending…' : 'Enviando…', true);
            fetch('/contacto.php', { method: 'POST', body: d, headers: { Accept: 'application/json' } })
                .then(function (r) {
                    return r.json().then(function (j) {
                        return { r: r, j: j };
                    });
                })
                .then(function (x) {
                    mostrar(x.j.mensaje, x.j.ok);
                    if (x.j.ok) form.reset();
                })
                .catch(porCorreo) // sin PHP o sin red: por el correo del visitante
                .finally(function () {
                    boton.disabled = false;
                });
        });
    }
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
