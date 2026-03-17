import os
from datetime import date

BASE_URL = "https://consultoretias.github.io/Simulador-ETIAS-"
TODAY = date.today().strftime("%d %B %Y").replace("March","marzo").replace("January","enero").replace("February","febrero").replace("April","abril").replace("May","mayo").replace("June","junio").replace("July","julio").replace("August","agosto").replace("September","septiembre").replace("October","octubre").replace("November","noviembre").replace("December","diciembre")
TODAY_ISO = date.today().isoformat()
OUTPUT_DIR = os.path.expanduser("~/storage/shared/Simulador-ETIAS-")

PAGES = [
    # 32 estados mexicanos
    ("etias-aguascalientes","ETIAS Aguascalientes 2026","ciudadanos de Aguascalientes","Aguascalientes"),
    ("etias-baja-california","ETIAS Baja California 2026","ciudadanos de Baja California","Baja California"),
    ("etias-baja-california-sur","ETIAS Baja California Sur 2026","ciudadanos de Baja California Sur","Baja California Sur"),
    ("etias-campeche","ETIAS Campeche 2026","ciudadanos de Campeche","Campeche"),
    ("etias-chiapas","ETIAS Chiapas 2026","ciudadanos de Chiapas","Chiapas"),
    ("etias-chihuahua","ETIAS Chihuahua 2026","ciudadanos de Chihuahua","Chihuahua"),
    ("etias-ciudad-de-mexico","ETIAS Ciudad de México 2026","ciudadanos de CDMX","Ciudad de México"),
    ("etias-coahuila","ETIAS Coahuila 2026","ciudadanos de Coahuila","Coahuila"),
    ("etias-colima","ETIAS Colima 2026","ciudadanos de Colima","Colima"),
    ("etias-durango","ETIAS Durango 2026","ciudadanos de Durango","Durango"),
    ("etias-guanajuato","ETIAS Guanajuato 2026","ciudadanos de Guanajuato","Guanajuato"),
    ("etias-guerrero","ETIAS Guerrero 2026","ciudadanos de Guerrero","Guerrero"),
    ("etias-hidalgo","ETIAS Hidalgo 2026","ciudadanos de Hidalgo","Hidalgo"),
    ("etias-jalisco","ETIAS Jalisco 2026","ciudadanos de Jalisco","Jalisco"),
    ("etias-estado-de-mexico","ETIAS Estado de México 2026","ciudadanos del Estado de México","Estado de México"),
    ("etias-michoacan","ETIAS Michoacán 2026","ciudadanos de Michoacán","Michoacán"),
    ("etias-morelos","ETIAS Morelos 2026","ciudadanos de Morelos","Morelos"),
    ("etias-nayarit","ETIAS Nayarit 2026","ciudadanos de Nayarit","Nayarit"),
    ("etias-nuevo-leon","ETIAS Nuevo León 2026","ciudadanos de Nuevo León","Nuevo León"),
    ("etias-oaxaca","ETIAS Oaxaca 2026","ciudadanos de Oaxaca","Oaxaca"),
    ("etias-puebla","ETIAS Puebla 2026","ciudadanos de Puebla","Puebla"),
    ("etias-queretaro","ETIAS Querétaro 2026","ciudadanos de Querétaro","Querétaro"),
    ("etias-quintana-roo","ETIAS Quintana Roo 2026","ciudadanos de Quintana Roo","Quintana Roo"),
    ("etias-san-luis-potosi","ETIAS San Luis Potosí 2026","ciudadanos de San Luis Potosí","San Luis Potosí"),
    ("etias-sinaloa","ETIAS Sinaloa 2026","ciudadanos de Sinaloa","Sinaloa"),
    ("etias-sonora","ETIAS Sonora 2026","ciudadanos de Sonora","Sonora"),
    ("etias-tabasco","ETIAS Tabasco 2026","ciudadanos de Tabasco","Tabasco"),
    ("etias-tamaulipas","ETIAS Tamaulipas 2026","ciudadanos de Tamaulipas","Tamaulipas"),
    ("etias-tlaxcala","ETIAS Tlaxcala 2026","ciudadanos de Tlaxcala","Tlaxcala"),
    ("etias-veracruz","ETIAS Veracruz 2026","ciudadanos de Veracruz","Veracruz"),
    ("etias-yucatan","ETIAS Yucatán 2026","ciudadanos de Yucatán","Yucatán"),
    ("etias-zacatecas","ETIAS Zacatecas 2026","ciudadanos de Zacatecas","Zacatecas"),
    # 15 países LATAM
    ("etias-colombia","ETIAS Colombia 2026","ciudadanos colombianos","Colombia"),
    ("etias-argentina","ETIAS Argentina 2026","ciudadanos argentinos","Argentina"),
    ("etias-chile","ETIAS Chile 2026","ciudadanos chilenos","Chile"),
    ("etias-peru","ETIAS Perú 2026","ciudadanos peruanos","Perú"),
    ("etias-venezuela","ETIAS Venezuela 2026","ciudadanos venezolanos","Venezuela"),
    ("etias-ecuador","ETIAS Ecuador 2026","ciudadanos ecuatorianos","Ecuador"),
    ("etias-bolivia","ETIAS Bolivia 2026","ciudadanos bolivianos","Bolivia"),
    ("etias-paraguay","ETIAS Paraguay 2026","ciudadanos paraguayos","Paraguay"),
    ("etias-uruguay","ETIAS Uruguay 2026","ciudadanos uruguayos","Uruguay"),
    ("etias-panama","ETIAS Panamá 2026","ciudadanos panameños","Panamá"),
    ("etias-costa-rica","ETIAS Costa Rica 2026","ciudadanos costarricenses","Costa Rica"),
    ("etias-guatemala","ETIAS Guatemala 2026","ciudadanos guatemaltecos","Guatemala"),
    ("etias-honduras","ETIAS Honduras 2026","ciudadanos hondureños","Honduras"),
    ("etias-el-salvador","ETIAS El Salvador 2026","ciudadanos salvadoreños","El Salvador"),
    ("etias-republica-dominicana","ETIAS República Dominicana 2026","ciudadanos dominicanos","República Dominicana"),
    # 15 destinos europeos
    ("etias-viajar-espana","ETIAS para viajar a España 2026","viaje a España","España"),
    ("etias-viajar-francia","ETIAS para viajar a Francia 2026","viaje a Francia","Francia"),
    ("etias-viajar-italia","ETIAS para viajar a Italia 2026","viaje a Italia","Italia"),
    ("etias-viajar-alemania","ETIAS para viajar a Alemania 2026","viaje a Alemania","Alemania"),
    ("etias-viajar-portugal","ETIAS para viajar a Portugal 2026","viaje a Portugal","Portugal"),
    ("etias-viajar-holanda","ETIAS para viajar a Holanda 2026","viaje a Holanda","Holanda"),
    ("etias-viajar-grecia","ETIAS para viajar a Grecia 2026","viaje a Grecia","Grecia"),
    ("etias-viajar-suiza","ETIAS para viajar a Suiza 2026","viaje a Suiza","Suiza"),
    ("etias-viajar-austria","ETIAS para viajar a Austria 2026","viaje a Austria","Austria"),
    ("etias-viajar-belgica","ETIAS para viajar a Bélgica 2026","viaje a Bélgica","Bélgica"),
    ("etias-viajar-suecia","ETIAS para viajar a Suecia 2026","viaje a Suecia","Suecia"),
    ("etias-viajar-noruega","ETIAS para viajar a Noruega 2026","viaje a Noruega","Noruega"),
    ("etias-viajar-dinamarca","ETIAS para viajar a Dinamarca 2026","viaje a Dinamarca","Dinamarca"),
    ("etias-viajar-polonia","ETIAS para viajar a Polonia 2026","viaje a Polonia","Polonia"),
    ("etias-viajar-republica-checa","ETIAS para viajar a República Checa 2026","viaje a República Checa","República Checa"),
    # 18 situaciones específicas
    ("etias-menores-de-edad","ETIAS para menores de edad 2026","menores de edad","Menores de Edad"),
    ("etias-adultos-mayores","ETIAS para adultos mayores 2026","adultos mayores","Adultos Mayores"),
    ("etias-doble-nacionalidad","ETIAS con doble nacionalidad 2026","doble nacionalidad","Doble Nacionalidad"),
    ("etias-pasaporte-vencido","ETIAS con pasaporte próximo a vencer","pasaporte por vencer","Pasaporte por Vencer"),
    ("etias-luna-de-miel","ETIAS para luna de miel en Europa","viaje de luna de miel","Luna de Miel"),
    ("etias-viaje-negocios","ETIAS para viaje de negocios a Europa","viajes de negocios","Viajes de Negocios"),
    ("etias-estudiantes","ETIAS para estudiantes mexicanos","estudiantes","Estudiantes"),
    ("etias-primera-vez","ETIAS primera vez viajando a Europa","primer viaje a Europa","Primer Viaje"),
    ("etias-requisitos-2026","Requisitos ETIAS 2026 completos","requisitos completos","Requisitos Completos"),
    ("etias-precio-costo","Costo y precio ETIAS 2026","costo del trámite","Costo ETIAS"),
    ("etias-cuanto-tarda","¿Cuánto tarda ETIAS? Tiempos 2026","tiempos de respuesta","Tiempos de Respuesta"),
    ("etias-rechazado","¿Qué hacer si rechazan tu ETIAS?","solicitud rechazada","ETIAS Rechazado"),
    ("etias-renovar","Cómo renovar ETIAS 2026","renovación","Renovación ETIAS"),
    ("etias-vs-visa","ETIAS vs Visa Schengen: diferencias","diferencia con visa","ETIAS vs Visa"),
    ("etias-schengen","ETIAS y el espacio Schengen explicado","espacio Schengen","Espacio Schengen"),
    ("etias-urgente","ETIAS urgente: solicitud de última hora","solicitud urgente","ETIAS Urgente"),
    ("etias-errores-comunes","Errores comunes al solicitar ETIAS","errores en la solicitud","Errores Comunes"),
    ("etias-checklist","Checklist ETIAS 2026: todo lo que necesitas","checklist completo","Checklist ETIAS"),
]

TEMPLATE = """<!DOCTYPE html>
<html lang="es-MX">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | ETIAS Consultant Simulator</title>
    <meta name="description" content="Guía completa ETIAS 2026 para {desc}. Requisitos, costos, tiempos y simulador gratuito. Obligatorio desde Q4 2026.">
    <meta name="keywords" content="ETIAS {region}, ETIAS 2026, autorización viaje Europa, {desc}">
    <link rel="canonical" href="{base_url}/{slug}.html">
    <meta property="og:title" content="{title} | ETIAS Consultant Simulator">
    <meta property="og:description" content="Guía ETIAS 2026 para {desc}. Simulador gratuito disponible.">
    <meta property="og:url" content="{base_url}/{slug}.html">
    <meta property="og:type" content="article">
    <style>
        *{{margin:0;padding:0;box-sizing:border-box;font-family:system-ui,-apple-system,sans-serif}}
        body{{line-height:1.6;color:#333;max-width:800px;margin:0 auto;padding:20px}}
        h1{{color:#1a472a;font-size:2rem;margin-bottom:1rem}}
        h2{{color:#2563eb;margin-top:2rem;margin-bottom:1rem}}
        .alert{{background:#fef3c7;border-left:4px solid #f59e0b;padding:1rem;margin:1rem 0}}
        .cta{{background:#1a472a;color:#fff;padding:1rem 2rem;text-decoration:none;display:inline-block;margin:1rem 0;border-radius:4px}}
        ul,ol{{margin-left:2rem;margin-bottom:1rem}}
        li{{margin-bottom:0.5rem}}
        .date{{color:#666;font-size:0.9rem}}
        .breadcrumb{{font-size:0.85rem;margin-bottom:1rem;color:#666}}
        .breadcrumb a{{color:#2563eb;text-decoration:none}}
        .faq{{background:#f8fafc;border-radius:8px;padding:1rem;margin:1rem 0}}
        footer{{margin-top:3rem;padding-top:2rem;border-top:1px solid #ddd;font-size:0.85rem;color:#666}}
    </style>
</head>
<body>
    <nav class="breadcrumb">
        <a href="{base_url}/">Inicio</a> › 
        <a href="{base_url}/etias-mexico.html">ETIAS México</a> › 
        {title}
    </nav>

    <h1>{title}</h1>
    <p class="date">Actualizado: {today}</p>

    <div class="alert">
        <strong>⚠️ Importante:</strong> ETIAS será obligatorio para {desc} que viajen a Europa a partir de <strong>Q4 2026</strong>.
    </div>

    <h2>¿Qué es ETIAS y por qué afecta a {region}?</h2>
    <p>El <strong>Sistema Europeo de Información y Autorización de Viaje (ETIAS)</strong> es un permiso electrónico obligatorio para ciudadanos de países exentos de visa — incluyendo México y toda Latinoamérica — que deseen visitar los 30 países del espacio Schengen.</p>
    <p>A partir de Q4 2026, <strong>{desc}</strong> deberán obtener su ETIAS antes de abordar cualquier vuelo a Europa.</p>

    <h2>Requisitos principales</h2>
    <ul>
        <li>✅ Pasaporte válido (mínimo 3 meses de vigencia tras la fecha de salida de Europa)</li>
        <li>✅ Correo electrónico activo</li>
        <li>✅ Tarjeta de débito o crédito para el pago de €7 (~$140 MXN)</li>
        <li>✅ Datos del viaje (fechas aproximadas, país de entrada)</li>
        <li>✅ Sin antecedentes penales en países Schengen</li>
    </ul>

    <h2>Proceso paso a paso</h2>
    <ol>
        <li>Accede al portal oficial ETIAS de la Unión Europea</li>
        <li>Completa el formulario con tus datos personales y de pasaporte</li>
        <li>Responde las preguntas de seguridad y salud</li>
        <li>Paga la tarifa de €7</li>
        <li>Recibe tu autorización (normalmente en minutos, máximo 96 horas)</li>
        <li>Guarda el número de autorización — lo necesitarás al hacer check-in</li>
    </ol>

    <a href="{base_url}/" class="cta">🛂 Probar Simulador ETIAS Gratis</a>

    <h2>Preguntas frecuentes</h2>
    <div class="faq">
        <p><strong>¿Cuánto cuesta ETIAS para {region}?</strong><br>
        €7 euros (aproximadamente $140 MXN). Menores de 18 y mayores de 70 años están exentos del pago.</p>
    </div>
    <div class="faq">
        <p><strong>¿Cuánto tarda en aprobarse?</strong><br>
        La mayoría de solicitudes se aprueban en minutos. En casos que requieren revisión manual, hasta 96 horas. En casos excepcionales, hasta 30 días.</p>
    </div>
    <div class="faq">
        <p><strong>¿Cuánto tiempo es válido el ETIAS?</strong><br>
        3 años o hasta que expire tu pasaporte, lo que ocurra primero. Con un ETIAS puedes hacer múltiples viajes a Europa.</p>
    </div>
    <div class="faq">
        <p><strong>¿ETIAS es una visa?</strong><br>
        No. Es una autorización de viaje electrónica, similar al ESTA de Estados Unidos. No requiere entrevista ni presentarse en consulado.</p>
    </div>

    <h2>Países europeos donde aplica</h2>
    <p>Alemania, Austria, Bélgica, Croacia, Dinamarca, Eslovenia, España, Estonia, Finlandia, Francia, Grecia, Hungría, Islandia, Italia, Letonia, Liechtenstein, Lituania, Luxemburgo, Malta, Noruega, Países Bajos, Polonia, Portugal, República Checa, República Eslovaca, Suecia, Suiza y más.</p>

    <footer>
        <p>ETIAS Consultant Simulator | No afiliado a la Unión Europea | Información con fines educativos</p>
        <p><a href="{base_url}/">Simulador</a> · <a href="{base_url}/etias-mexico.html">ETIAS México</a></p>
    </footer>
</body>
</html>"""

def generate_pages():
    generated = 0
    urls = []
    
    for slug, title, desc, region in PAGES:
        html = TEMPLATE.format(
            slug=slug,
            title=title,
            desc=desc,
            region=region,
            base_url=BASE_URL,
            today=TODAY,
            today_iso=TODAY_ISO,
        )
        filepath = os.path.join(OUTPUT_DIR, f"{slug}.html")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        urls.append(f"{BASE_URL}/{slug}.html")
        generated += 1
    
    print(f"✅ {generated} páginas generadas")
    return urls

def update_sitemap(new_urls):
    existing = [
        ("https://consultoretias.github.io/Simulador-ETIAS-/", "1.0"),
        ("https://consultoretias.github.io/Simulador-ETIAS-/etias-mexico.html", "0.9"),
    ]
    
    entries = ""
    for url, priority in existing:
        entries += f"""  <url>
    <loc>{url}</loc>
    <lastmod>{TODAY_ISO}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>\n"""
    
    for url in new_urls:
        entries += f"""  <url>
    <loc>{url}</loc>
    <lastmod>{TODAY_ISO}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>\n"""
    
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{entries}</urlset>"""
    
    sitemap_path = os.path.join(OUTPUT_DIR, "sitemap.xml")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap)
    
    print(f"✅ sitemap.xml actualizado con {len(new_urls) + 2} URLs")

if __name__ == "__main__":
    print("🚀 Generando páginas programmatic SEO...")
    urls = generate_pages()
    update_sitemap(urls)
    print(f"\n📊 Total URLs en sitemap: {len(urls) + 2}")
    print("✅ Listo para git push")
