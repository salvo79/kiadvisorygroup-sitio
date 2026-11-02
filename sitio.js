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

    // Formulario: sin servidor, abre el correo del visitante con la solicitud ya escrita
    var form = document.getElementById('formulario-contacto');
    if (form) {
        form.addEventListener('submit', function (ev) {
            ev.preventDefault();
            var d = new FormData(form);
            var lineas = ['Nombre: ' + d.get('nombre'), 'Empresa: ' + (d.get('empresa') || '—'), 'Cargo: ' + (d.get('cargo') || '—'), 'Correo: ' + d.get('email'), 'Teléfono: ' + (d.get('telefono') || '—'), 'Área de interés: ' + d.get('area'), 'Industria: ' + (d.get('industria') || '—'), 'Horizonte: ' + (d.get('horizonte') || '—'), '', d.get('desafio')];
            var asunto = 'Consulta inicial · ' + (d.get('empresa') || d.get('nombre'));
            window.location.href = 'mailto:salvador.delira@kiadvisorygroup.com?subject=' + encodeURIComponent(asunto) + '&body=' + encodeURIComponent(lineas.join('\n'));
            var ok = document.getElementById('mensaje-enviado');
            if (ok) ok.hidden = false;
        });
    }
})();

// Contacto: «Solicitar una demostración» llega con ?interes=… y preselecciona el área
(function () {
    var area = document.querySelector('#formulario-contacto select[name="area"]');
    var interes = new URLSearchParams(location.search).get('interes');
    if (area && interes) area.value = interes;
})();
