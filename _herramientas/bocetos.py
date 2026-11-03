"""Monta los bocetos de Infinity Workflow (FE/public/manuales de WorkflowHD) como páginas del sitio, en español e inglés.

Cada boceto se encierra en <div class="boceto-sitio">: sus estilos se limitan a ese contenedor (no chocan con los del
sitio), toma la paleta y las tipografías del sitio y va con la cabecera, el pie y el selector de idioma de la web.
Las imágenes de las tarjetas (img/perspectivas/es|en/<boceto>.jpg) son capturas del inicio de cada boceto ya montado.
Uso:  python3 _herramientas/bocetos.py  [carpeta de los bocetos]   (por omisión ~/Desktop/WorkflowHD/FE/public/manuales)
"""
import html
import os
import re
import sys

SITIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGEN = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/Desktop/WorkflowHD/FE/public/manuales')
BASE = 'https://kiadvisorygroup.com/'
ORDEN = ['mapa-de-infinity-workflow', 'como-decide-el-plan-de-ventas', 'pronosticar-u-optimizar', 'quien-vende-que', 'ciclo-del-plan', 'valores-del-modelo']
TEXTOS = {
    'es': {'seccion': 'Perspectivas', 'carpeta': 'perspectivas', 'titulo': 'Perspectivas', 'lead': 'Cómo pensamos la planeación y la operación: bocetos que explican, con un ejemplo concreto, las ideas detrás de nuestro trabajo y de Infinity Workflow.', 'h1': 'Ideas que <em>se pueden operar.</em>', 'leer': 'Leer', 'volver': 'Todas las perspectivas', 'portada': 'Ver todas las perspectivas'},
    'en': {'seccion': 'Insights', 'carpeta': 'perspectivas', 'titulo': 'Insights', 'lead': 'How we think about planning and operations: sketches that explain, with a concrete example, the ideas behind our work and Infinity Workflow.', 'h1': 'Ideas you can <em>put into operation.</em>', 'leer': 'Read', 'volver': 'All insights', 'portada': 'See all insights'},
}

# Paleta y tipografías del sitio sobre las variables de los bocetos (siempre en tema claro, como el sitio)
TEMA = """
.boceto-sitio { --papel: #f5f7fa; --tarjeta: #ffffff; --tinta: #1b2533; --tenue: #5b6675; --linea: #e6eaf0;
    --azul: #0284c7; --azul-suave: #e0f2fe; --marino: #0a1f3c; --sobre-marino: #ffffff;
    --f-display: 'Source Serif 4', Georgia, serif; --f-texto: 'Inter', 'Helvetica Neue', Arial, sans-serif;
    --f-mano: 'Source Serif 4', Georgia, serif; color-scheme: light; background: var(--papel); background-image: none; }
.boceto-sitio h1, .boceto-sitio h2, .boceto-sitio h3 { font-weight: 500; letter-spacing: -0.01em; }
.boceto-sitio .mano { font-style: italic; font-weight: 500; font-size: 1.12rem; }
/* La cabecera de la página ya muestra la marca, el antetítulo y el título */
.boceto-sitio .hoja > .marca, .boceto-sitio .hoja > .cabeza:first-of-type > .eyebrow, .boceto-sitio .hoja > .cabeza:first-of-type > h1 { display: none; }
.volver-perspectivas { display: inline-flex; margin-top: 26px; color: #c5d3e6; text-decoration: none; font-weight: 600; font-size: .9rem; }
.volver-perspectivas:hover { color: #fff; }
"""


def bloques(css):
    """Divide CSS en [(prelude, cuerpo | None)] respetando llaves anidadas."""
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    res, i = [], 0
    while i < len(css):
        j = css.find('{', i)
        k = css.find(';', i)
        if j == -1:
            break
        if k != -1 and k < j and css[i:k].strip().startswith('@'):  # @import, @charset
            res.append((css[i:k].strip(), None))
            i = k + 1
            continue
        nivel, m = 1, j + 1
        while nivel and m < len(css):
            nivel += {'{': 1, '}': -1}.get(css[m], 0)
            m += 1
        res.append((css[i:j].strip(), css[j + 1:m - 1]))
        i = m
    return res


def separar(sel):
    partes, nivel, actual = [], 0, ''
    for c in sel:
        nivel += {'(': 1, ')': -1, '[': 1, ']': -1}.get(c, 0)
        if c == ',' and nivel == 0:
            partes.append(actual)
            actual = ''
        else:
            actual += c
    return partes + [actual]


def prefijar(sel, p='.boceto-sitio'):
    s = sel.strip()
    m = re.match(r'^(:root|html|body)(?![\w-])', s)
    if m:
        return p + s[m.end():]
    return f'{p} {s}'


def limitar(css):
    salida = []
    for pre, cuerpo in bloques(css):
        if cuerpo is None:
            continue
        if pre.startswith('@media'):
            if 'prefers-color-scheme: dark' in pre or 'prefers-color-scheme:dark' in pre:
                continue  # el sitio es solo claro
            salida.append(f'{pre} {{\n{limitar(cuerpo)}\n}}')
        elif pre.startswith('@supports') or pre.startswith('@container'):
            salida.append(f'{pre} {{\n{limitar(cuerpo)}\n}}')
        elif pre.startswith('@'):
            salida.append(f'{pre} {{{cuerpo}}}')  # @keyframes, @font-face: tal cual
        else:
            sels = [s for s in separar(pre) if 'data-theme="dark"' not in s and "data-theme='dark'" not in s]
            if sels:
                salida.append(', '.join(prefijar(s) for s in sels) + ' {' + cuerpo + '}')
    return '\n'.join(salida)


def texto_plano(h):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', h))).strip()


def leer_boceto(ruta):
    s = open(ruta, encoding='utf-8').read()
    titulo = texto_plano(re.search(r'<title>(.*?)</title>', s, re.S).group(1))
    estilos = '\n'.join(c for c in re.findall(r'<style>(.*?)</style>', s, re.S) if '--papel' in c)
    principal = re.search(r'<main class="hoja">.*?</main>', s, re.S).group(0)
    scripts = re.findall(r'<script>(.*?)</script>', s[s.index('</main>'):], re.S)
    cabeza = re.search(r'<section class="cabeza">(.*?)</section>', principal, re.S).group(1)
    antetitulo = texto_plano((re.search(r'class="eyebrow"[^>]*>(.*?)</', cabeza, re.S) or re.search('()', '')).group(1)) or ''
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', cabeza, re.S).group(1).strip()
    tesis = re.search(r'<p class="tesis"[^>]*>(.*?)</p>', cabeza, re.S)
    resumen = texto_plano(tesis.group(1)) if tesis else ''
    # El boceto que lee colores de la raíz los toma ahora de su contenedor
    scripts = [x.replace('getComputedStyle(document.documentElement)', "getComputedStyle(document.querySelector('.boceto-sitio'))") for x in scripts]
    return dict(titulo=titulo, estilos=limitar(estilos), principal=principal, scripts=scripts, antetitulo=antetitulo, h1=h1, resumen=resumen)


def plantilla(idioma):
    """Cabecera y pie del sitio, tomados de la página de contacto del idioma."""
    s = open(os.path.join(SITIO, 'contacto.html' if idioma == 'es' else 'en/contacto.html'), encoding='utf-8').read()
    return s[:s.index('<main>')], s[s.index('</main>') + len('</main>'):]


def reubicar(h):
    """Rutas relativas un nivel más abajo (perspectivas/)."""
    return re.sub(r'(href|src)="(?!https?:|mailto:|#|/|data:)([^"]+)"', r'\1="../\2"', h)


def pagina(idioma, archivo, titulo, descripcion, cuerpo, otra, extra_head=''):
    cab, pie = plantilla(idioma)
    cab, pie = reubicar(cab), reubicar(pie)
    cab = re.sub(r'<title>.*?</title>', f'<title>{html.escape(titulo)} · KI Advisory &amp; Strategy Group</title>', cab)
    cab = re.sub(r'<meta name="description" content="[^"]*" />', f'<meta name="description" content="{html.escape(descripcion)}" />', cab)
    cab = re.sub(r'hreflang="es" href="[^"]*"', f'hreflang="es" href="{BASE}perspectivas/{archivo}"', cab)
    cab = re.sub(r'hreflang="(en|x-default)" href="[^"]*"', lambda m: f'hreflang="{m.group(1)}" href="{BASE}en/perspectivas/{archivo}"', cab)
    cab = re.sub(r'<a class="idioma" href="[^"]*" hreflang="(es|en)"', lambda m: f'<a class="idioma" href="{otra}?idioma={m.group(1)}" hreflang="{m.group(1)}"', cab)
    cab = cab.replace('</head>', extra_head + '</head>')
    t = TEXTOS[idioma]
    cab = cab.replace(f'>{t["seccion"]}</a>', f' class="activo">{t["seccion"]}</a>', 1)
    destino = os.path.join(SITIO, '' if idioma == 'es' else 'en', 'perspectivas', archivo)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    open(destino, 'w', encoding='utf-8').write(cab + '<main>\n' + cuerpo + '\n    </main>\n' + pie)


def generar():
    tarjetas = {'es': [], 'en': []}
    for idioma in ['es', 'en']:
        t = TEXTOS[idioma]
        for slug in ORDEN:
            ruta = os.path.join(ORIGEN, '' if idioma == 'es' else 'en', slug + '.html')
            if not os.path.exists(ruta):
                print('falta', ruta)
                continue
            b = leer_boceto(ruta)
            otra = f'../en/perspectivas/{slug}.html' if idioma == 'es' else f'../../perspectivas/{slug}.html'
            cuerpo = f'''        <section class="cabecera-pagina sobre-oscuro">
            <div class="contenedor">
                <div class="antetitulo">{html.escape(b['antetitulo'] or t['seccion'])}</div>
                <h1>{b['h1']}</h1>
                <a class="volver-perspectivas" href="index.html">← {t['volver']}</a>
            </div>
        </section>
        <div class="boceto-sitio">
{b['principal']}
        </div>
''' + ''.join(f'<script>{x}</script>\n' for x in b['scripts'])
            pagina(idioma, f'{slug}.html', b['titulo'], b['resumen'][:300], cuerpo, otra, f'    <style>\n{b["estilos"]}\n{TEMA}\n    </style>\n')
            tarjetas[idioma].append((slug, b))
        # Índice de perspectivas
        img = '../img' if idioma == 'es' else '../../img'
        cartas = '\n'.join(f'''                    <a class="perspectiva" href="{slug}.html"><img src="{img}/perspectivas/{idioma}/{slug}.jpg" alt="" loading="lazy" /><small>{html.escape(b['antetitulo'])}</small><h3>{html.escape(b['titulo'])}</h3><p>{html.escape(b['resumen'][:220] + ('…' if len(b['resumen']) > 220 else ''))}</p></a>''' for slug, b in tarjetas[idioma])
        cuerpo = f'''        <section class="cabecera-pagina sobre-oscuro">
            <div class="contenedor">
                <div class="antetitulo">{t['seccion']}</div>
                <h1>{t['h1']}</h1>
                <p class="entrada">{t['lead']}</p>
            </div>
        </section>
        <section>
            <div class="contenedor">
                <div class="perspectivas">
{cartas}
                </div>
            </div>
        </section>'''
        otra = '../en/perspectivas/index.html' if idioma == 'es' else '../../perspectivas/index.html'
        pagina(idioma, 'index.html', t['titulo'], t['lead'], cuerpo, otra)
        # Portada: tres perspectivas destacadas antes del llamado final
        portada = os.path.join(SITIO, 'index.html' if idioma == 'es' else 'en/index.html')
        s = open(portada, encoding='utf-8').read()
        s = re.sub(r'\s*<!-- Perspectivas -->.*?<!-- /Perspectivas -->', '', s, flags=re.S)
        img = 'img' if idioma == 'es' else '../img'
        destacadas = '\n'.join(f'''                    <a class="perspectiva" href="perspectivas/{slug}.html"><img src="{img}/perspectivas/{idioma}/{slug}.jpg" alt="" loading="lazy" /><small>{html.escape(b['antetitulo'])}</small><h3>{html.escape(b['titulo'])}</h3><p>{html.escape(b['resumen'][:180] + ('…' if len(b['resumen']) > 180 else ''))}</p></a>''' for slug, b in tarjetas[idioma][:3])
        bloque = f'''
        <!-- Perspectivas -->
        <section id="perspectivas">
            <div class="contenedor">
                <div class="antetitulo">{t['seccion']}</div>
                <h2 class="aparece">{t['h1']}</h2>
                <div class="perspectivas aparece">
{destacadas}
                </div>
                <a class="enlace" href="perspectivas/index.html" style="margin-top: 40px">{t['portada']}</a>
            </div>
        </section>
        <!-- /Perspectivas -->'''
        s = s.replace('\n\n        <!-- Llamado -->', bloque + '\n\n        <!-- Llamado -->', 1)
        open(portada, 'w', encoding='utf-8').write(s)
    print('ok:', {k: len(v) for k, v in tarjetas.items()})


if __name__ == '__main__':
    generar()
