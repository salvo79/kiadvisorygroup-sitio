#!/usr/bin/env python3
"""Deja el sitio listo para agentes de IA (idempotente; correr después de bocetos.py y cada vez que cambie el contenido).

- <link rel="canonical"> en cada página pública (las de redirección ya lo tienen)
- JSON-LD: Organization + WebSite en todas, WebPage / ContactPage / CollectionPage según la página,
  SoftwareApplication (Infinity Workflow) con la oferta del CRM Base y BreadcrumbList
- sitemap.xml con alternas es/en, robots.txt con Content-Signal y Sitemap, llms.txt
- Versión Markdown (.md) de cada página pública, que .htaccess sirve con «Accept: text/markdown»

Uso: python3 _herramientas/agentes.py
"""
import html
import json
import re
import subprocess
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BASE = 'https://kiadvisorygroup.com/'
ORG_ID = BASE + '#organizacion'
SITIO_ID = BASE + '#sitio'
CORREO = 'contact@kiadvisorygroup.com'
# Perfiles externos de la empresa (LinkedIn, directorios…): agregarlos aquí para el «sameAs» del JSON-LD
PERFILES = []
REDIRECCIONES = {'industrias.html', 'metodologia.html', 'servicios.html', 'socios.html'}


def paginas():
    for p in sorted(RAIZ.rglob('*.html')):
        rel = p.relative_to(RAIZ).as_posix()
        if rel.startswith(('_herramientas/', '.github/')) or rel in REDIRECCIONES:
            continue
        yield p, rel


def idioma(rel):
    return 'en' if rel.startswith('en/') else 'es'


def alterna(rel):
    return rel[3:] if rel.startswith('en/') else 'en/' + rel


def fecha(rel):
    try:
        f = subprocess.run(['git', 'log', '-1', '--format=%cs', '--', rel], cwd=RAIZ, capture_output=True, text=True).stdout.strip()
        return f or date.today().isoformat()
    except Exception:
        return date.today().isoformat()


def meta(s, nombre):
    m = re.search(rf'<meta name="{nombre}" content="([^"]*)"', s)
    return html.unescape(m.group(1)) if m else ''


def titulo(s):
    m = re.search(r'<title>(.*?)</title>', s, re.S)
    return html.unescape(m.group(1).strip()) if m else ''


# ───────────── JSON-LD ─────────────
def organizacion(lang):
    es = lang == 'es'
    nodo = {
        '@type': 'Organization',
        '@id': ORG_ID,
        'name': 'KI Advisory & Strategy Group',
        'alternateName': ['KI-Advisory & Strategy Group', 'KI Advisory'],
        'url': BASE,
        'logo': BASE + 'img/favicon.svg',
        'slogan': 'Intelligence that transforms',
        'description': 'Consultoría de planeación estratégica, programación operativa, implementación y evaluación, con modelos matemáticos y la plataforma Infinity Workflow.' if es else 'Consulting in strategic planning, operational scheduling, implementation, and evaluation, with mathematical models and the Infinity Workflow platform.',
        'email': CORREO,
        'contactPoint': [{'@type': 'ContactPoint', 'contactType': 'sales', 'email': CORREO, 'availableLanguage': ['es', 'en'], 'areaServed': ['MX', 'ES', 'Latin America'], 'url': BASE + ('contacto.html' if es else 'en/contacto.html')}],
        'address': {'@type': 'PostalAddress', 'addressLocality': 'Ciudad de México', 'addressCountry': 'MX'},
        'areaServed': ['México', 'España', 'Latinoamérica'],
        'knowsAbout': ['Planeación estratégica', 'Programación lineal', 'Investigación de operaciones', 'S&OP', 'Fuerza de ventas', 'CRM', 'Analítica de datos', 'Inteligencia artificial'] if es else ['Strategic planning', 'Linear programming', 'Operations research', 'S&OP', 'Sales force', 'CRM', 'Data analytics', 'Artificial intelligence'],
        'owns': {'@id': BASE + 'infinity-workflow.html#producto'},
    }
    if PERFILES:
        nodo['sameAs'] = PERFILES
    return nodo


def sitio_web(lang):
    return {'@type': 'WebSite', '@id': SITIO_ID, 'url': BASE, 'name': 'KI Advisory & Strategy Group', 'inLanguage': ['es', 'en'], 'publisher': {'@id': ORG_ID}}


def producto(lang):
    es = lang == 'es'
    img = BASE + f'img/app/{lang}/'
    return {
        '@type': 'SoftwareApplication',
        '@id': BASE + 'infinity-workflow.html#producto',
        'name': 'Infinity Workflow',
        'applicationCategory': 'BusinessApplication',
        'applicationSubCategory': 'CRM, Sales planning, Optimization',
        'operatingSystem': 'Web (Windows, macOS, iOS, iPadOS, Android)',
        'description': ('Plataforma modular en la nube: planeación con optimización (LP), programación comercial, CRM para equipos en campo, operación diaria, evaluación contra el plan, analítica de datos y un agente de IA.' if es
                        else 'Modular cloud platform: optimization-based planning (LP), sales scheduling, CRM for field teams, daily operations, plan-versus-actual evaluation, data analytics, and an AI agent.'),
        'url': BASE + ('infinity-workflow.html' if es else 'en/infinity-workflow.html'),
        'creator': {'@id': ORG_ID},
        'publisher': {'@id': ORG_ID},
        'inLanguage': ['es', 'en'],
        'featureList': (['Optimización del plan de ventas, compras e inventario', 'Comparador de escenarios, sensibilidad y backcasting', 'Programación comercial por vendedor', 'CRM: cartera, rutas con check-in, pedidos y cobranza', 'Agente de IA y ampliación de cartera (nivel Pro)', 'Evaluación del plan contra lo real', 'Analítica de datos (módulo adicional)', 'Integraciones: Teams, Slack, WhatsApp Business, Outlook, API para CRM/ERP']
                        if es else ['Sales, purchasing, and inventory plan optimization', 'Scenario comparator, sensitivity, and backcasting', 'Sales scheduling by salesperson', 'CRM: portfolio, routes with check-in, orders, and collections', 'AI agent and portfolio expansion (Pro tier)', 'Plan-versus-actual evaluation', 'Data analytics (add-on module)', 'Integrations: Teams, Slack, WhatsApp Business, Outlook, API for CRM/ERP']),
        'screenshot': [img + f for f in ('lp-resultados.jpg', 'lp-comparador.jpg', 'seguimiento-mapa.jpg', 'evaluacion.jpg', 'pro-asistente.jpg')],
        'offers': [{'@type': 'Offer', 'name': 'Prueba del CRM Base' if es else 'Base CRM trial', 'price': '0', 'priceCurrency': 'MXN', 'description': 'Prueba sin costo con alta asistida y usuarios limitados; no incluye inteligencia artificial (nivel Pro)' if es else 'No-cost trial with assisted setup and limited users; does not include artificial intelligence (Pro tier)', 'seller': {'@id': ORG_ID}}],
    }


def grafo(rel, s):
    lang = idioma(rel)
    url = BASE + rel
    nombre = titulo(s)
    tipo = 'ContactPage' if rel.endswith('contacto.html') else 'CollectionPage' if rel.endswith('perspectivas/index.html') else 'WebPage'
    pagina = {'@type': tipo, '@id': url + '#pagina', 'url': url, 'name': nombre, 'description': meta(s, 'description'), 'inLanguage': lang, 'isPartOf': {'@id': SITIO_ID}, 'about': {'@id': ORG_ID}, 'publisher': {'@id': ORG_ID}, 'dateModified': fecha(rel)}
    nodos = [organizacion(lang), sitio_web(lang), pagina]
    if rel.endswith('infinity-workflow.html'):
        nodos.append(producto(lang))
        pagina['mainEntity'] = {'@id': BASE + 'infinity-workflow.html#producto'}
    # Migas
    inicio = BASE + ('en/index.html' if lang == 'en' else 'index.html')
    migas = [('Inicio' if lang == 'es' else 'Home', inicio)]
    if '/perspectivas/' in '/' + rel and not rel.endswith('perspectivas/index.html'):
        migas.append(('Perspectivas' if lang == 'es' else 'Insights', BASE + ('en/' if lang == 'en' else '') + 'perspectivas/index.html'))
    if not rel.endswith(('/index.html',)) and rel != 'index.html':
        migas.append((nombre.split(' · ')[0], url))
    elif rel.endswith('perspectivas/index.html'):
        migas.append(('Perspectivas' if lang == 'es' else 'Insights', url))
    if len(migas) > 1:
        nodos.append({'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': u} for i, (n, u) in enumerate(migas)]})
    return {'@context': 'https://schema.org', '@graph': nodos}


def cabecera(rel, s):
    url = BASE + rel
    s = re.sub(r'\s*<link rel="canonical" href="[^"]*" />', '', s)
    s = re.sub(r'\s*<script type="application/ld\+json" id="datos-estructurados">.*?</script>', '', s, flags=re.S)
    s = re.sub(r'\s*<link rel="alternate" type="text/markdown"[^>]*>', '', s)
    md = re.sub(r'\.html$', '.md', url)
    ld = json.dumps(grafo(rel, s), ensure_ascii=False, indent=1).replace('</', '<\\/')
    extra = (f'\n    <link rel="canonical" href="{url}" />'
             f'\n    <link rel="alternate" type="text/markdown" href="{md}" title="Markdown" />'
             f'\n    <script type="application/ld+json" id="datos-estructurados">\n{ld}\n    </script>\n')
    return s.replace('</head>', extra + '</head>', 1)


# ───────────── Markdown ─────────────
class AMarkdown(HTMLParser):
    BLOQUES = {'p', 'div', 'section', 'li', 'h1', 'h2', 'h3', 'h4', 'summary', 'figcaption', 'tr', 'blockquote', 'ul', 'ol', 'details', 'figure'}
    OMITIR = {'script', 'style', 'svg', 'noscript', 'header', 'footer', 'nav', 'button', 'select', 'textarea', 'form'}

    def __init__(self, base):
        super().__init__(convert_charrefs=True)
        self.base, self.out, self.omitir, self.enlace, self.dentro_main = base, [], 0, [], 0

    VACIAS = {'img', 'br', 'hr', 'input', 'meta', 'link', 'source', 'wbr', 'col', 'area', 'base', 'track', 'embed', 'param'}

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'main':
            self.dentro_main += 1
        # Dentro de un elemento omitido se lleva la profundidad de todas sus etiquetas (no solo las de OMITIR)
        if self.omitir:
            if tag not in self.VACIAS:
                self.omitir += 1
            return
        if tag in self.OMITIR or 'trampa' in (a.get('class') or '') or a.get('aria-hidden') == 'true':
            if tag not in self.VACIAS:
                self.omitir = 1
            return
        if tag in self.BLOQUES:
            self.out.append('\n\n')
        if tag in ('h1', 'h2', 'h3', 'h4'):
            self.out.append('#' * int(tag[1]) + ' ')
        elif tag == 'li':
            self.out.append('- ')
        elif tag in ('b', 'strong'):
            self.out.append('**')
        elif tag == 'em':
            self.out.append('*')
        elif tag == 'br':
            self.out.append('  \n')
        elif tag == 'a' and a.get('href') and not a['href'].startswith(('#', 'javascript')):
            self.enlace.append(a['href'])
            self.out.append('[')
        elif tag == 'a':
            self.enlace.append(None)
        elif tag == 'img' and a.get('alt'):
            self.out.append(f"![{a['alt']}]({self.abs(a.get('src', ''))})")

    def handle_endtag(self, tag):
        if tag == 'main':
            self.dentro_main -= 1
        if self.omitir:
            if tag not in self.VACIAS:
                self.omitir -= 1
            return
        if tag in ('b', 'strong'):
            self.out.append('**')
        elif tag == 'em':
            self.out.append('*')
        elif tag == 'a' and self.enlace:
            h = self.enlace.pop()
            if h:
                self.out.append(f'](' + self.abs(h) + ')')

    def handle_data(self, d):
        if not self.omitir:
            self.out.append(re.sub(r'\s+', ' ', d))

    def abs(self, h):
        if h.startswith(('http', 'mailto:', 'tel:')):
            return h
        from urllib.parse import urljoin
        return urljoin(self.base, h)

    def texto(self):
        t = ''.join(self.out)
        t = re.sub(r'[ \t]+\n', '\n', t)
        t = re.sub(r'\n[ \t]+', '\n', t)
        t = re.sub(r'\*\*\s*\*\*', '', t)
        t = re.sub(r'\n{3,}', '\n\n', t)
        return t.strip() + '\n'


def markdown(rel, s):
    m = re.search(r'<main\b.*?</main>', s, re.S)
    cuerpo = m.group(0) if m else s
    p = AMarkdown(BASE + rel)
    p.feed(cuerpo)
    lang = idioma(rel)
    pie = ('\n---\n\n' + ('Fuente' if lang == 'es' else 'Source') + f': {BASE + rel} · KI Advisory & Strategy Group · {CORREO}\n')
    return f"# {titulo(s)}\n\n> {meta(s, 'description')}\n\n" + p.texto() + pie


# ───────────── Archivos del sitio ─────────────
def sitemap(lista):
    filas = []
    for rel in lista:
        alt = alterna(rel)
        xs = []
        if alt in lista:
            es, en = (rel, alt) if idioma(rel) == 'es' else (alt, rel)
            xs = [f'    <xhtml:link rel="alternate" hreflang="es" href="{BASE + es}" />', f'    <xhtml:link rel="alternate" hreflang="en" href="{BASE + en}" />', f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE + en}" />']
        prioridad = '1.0' if rel in ('index.html', 'en/index.html') else '0.9' if 'infinity-workflow' in rel else '0.8' if 'contacto' in rel else '0.6'
        filas.append('  <url>\n' + f'    <loc>{BASE + rel}</loc>\n    <lastmod>{fecha(rel)}</lastmod>\n    <priority>{prioridad}</priority>\n' + '\n'.join(xs) + ('\n' if xs else '') + '  </url>')
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + '\n'.join(filas) + '\n</urlset>\n'


ROBOTS = f"""# kiadvisorygroup.com · política para rastreadores y agentes
# Content-Signal (https://contentsignals.org): search = aparecer en buscadores; ai-input = usarse como fuente en
# respuestas de IA con referencia; ai-train = entrenar modelos de IA.
User-agent: *
Content-Signal: search=yes, ai-input=yes, ai-train=no
Allow: /
Disallow: /contacto.php
Disallow: /_herramientas/

Sitemap: {BASE}sitemap.xml
"""


def llms(datos):
    def grupo(r):
        return ('en' if r.startswith('en/') else 'es') + ('-p' if 'perspectivas/' in r else '')

    def lista(clave):
        return '\n'.join(f'- [{t.split(" · KI")[0]}]({BASE + r[:-5]}.md)' + (f': {d}' if d else '') for r, t, d in datos if grupo(r) == clave)
    return f"""# KI Advisory & Strategy Group

> Consultora de planeación estratégica, programación operativa, implementación y evaluación (Ciudad de México · España · Latinoamérica). Desarrolla Infinity Workflow, una plataforma modular en la nube: optimización del plan de ventas (LP), programación comercial, CRM para equipos en campo con agente de IA, evaluación contra el plan y analítica de datos. Strategy and operations consulting firm; creator of the Infinity Workflow platform. Contact: {CORREO}

Cada página tiene su versión Markdown (enlazada abajo) y en HTML (misma ruta con .html). El sitio está en español e inglés.

## Español

{lista('es')}

## Perspectivas (diagramas de Infinity Workflow)

{lista('es-p')}

## English

{lista('en')}

## Insights (Infinity Workflow diagrams)

{lista('en-p')}

## Contacto / Contact

- Correo / Email: {CORREO}
- Formulario / Form: {BASE}contacto.html · {BASE}en/contacto.html
"""


def main():
    lista, datos = [], []
    for p, rel in paginas():
        s = p.read_text(encoding='utf8')
        s = cabecera(rel, s)
        p.write_text(s, encoding='utf8')
        p.with_suffix('.md').write_text(markdown(rel, s), encoding='utf8')
        lista.append(rel)
        datos.append((rel, titulo(s), meta(s, 'description')))
    (RAIZ / 'sitemap.xml').write_text(sitemap(lista), encoding='utf8')
    (RAIZ / 'robots.txt').write_text(ROBOTS, encoding='utf8')
    (RAIZ / 'llms.txt').write_text(llms(datos), encoding='utf8')
    print(f'✔ {len(lista)} páginas: canonical, JSON-LD y Markdown · sitemap.xml · robots.txt · llms.txt')


if __name__ == '__main__':
    main()
