import os
OUTPUT_DIR = "."
os.makedirs(OUTPUT_DIR, exist_ok=True)
SIMULADOR_URL = "https://consultoretias.github.io/Simulador-ETIAS-/"
EQUIVALENCIA = "aprox. $7 USD (pago en divisas requerido)"
DATO_UNICO = "Venezuela tiene exención de visa Schengen desde 2004. Con pasaporte venezolano vigente puedes viajar a Europa sin visa. ETIAS será obligatorio desde Q4 2026."
PAGINAS = [
{"slug":"etias-venezuela-requisitos","titulo":"Requisitos ETIAS para Venezolanos 2026","h1":"Requisitos ETIAS para Venezolanos","descripcion":"Lista completa de requisitos ETIAS para pasaporte venezolano en 2026.","intro":"El requisito más crítico para venezolanos es el pasaporte vigente. Verifica que tenga al menos 3 meses de vigencia después de tu fecha de regreso de Europa."},
{"slug":"etias-venezuela-costo","titulo":"Cuánto Cuesta ETIAS para Venezolanos 2026","h1":"Costo ETIAS para Venezolanos","descripcion":f"ETIAS cuesta €7 euros para ciudadanos venezolanos. {EQUIVALENCIA}.","intro":f"El costo oficial de ETIAS es €7 euros ({EQUIVALENCIA}). Se recomienda pagar con tarjeta internacional en dólares o de un familiar en el exterior."},
{"slug":"etias-venezuela-como-solicitar","titulo":"Cómo Solicitar ETIAS desde Venezuela 2026","h1":"Cómo Solicitar ETIAS si Eres Venezolano","descripcion":"Guía paso a paso para solicitar ETIAS con pasaporte venezolano vigente.","intro":"Solicitar ETIAS con pasaporte venezolano es 100% online. Puedes hacerlo desde Venezuela o desde cualquier país donde te encuentres."},
{"slug":"etias-venezuela-vigencia","titulo":"Vigencia ETIAS para Venezolanos 2026","h1":"Vigencia de ETIAS para Pasaporte Venezolano","descripcion":"ETIAS para venezolanos dura 3 años o hasta que venza el pasaporte.","intro":"Tu ETIAS tendrá validez de 3 años o hasta el vencimiento de tu pasaporte venezolano, lo que ocurra primero. Si renovas pasaporte, necesitas ETIAS nuevo."},
{"slug":"etias-venezuela-espana","titulo":"ETIAS Venezuela a España 2026","h1":"ETIAS para Venezolanos que Viajan a España","descripcion":"España concentra más de 400.000 venezolanos. Guía ETIAS para la ruta Venezuela-España 2026.","intro":"España es el destino europeo más visitado por venezolanos. Desde Q4 2026, viajar a Madrid o Barcelona con pasaporte venezolano requerirá ETIAS."},
{"slug":"etias-venezuela-turismo","titulo":"ETIAS Turismo Venezuela Europa 2026","h1":"ETIAS para Turistas Venezolanos en Europa","descripcion":"Todo sobre ETIAS para turistas venezolanos en Europa 2026.","intro":"Si planeas visitar Europa como turista después de Q4 2026, necesitarás ETIAS. El proceso es online y toma menos de 20 minutos."},
{"slug":"etias-venezuela-negocios","titulo":"ETIAS Negocios Venezuela Europa 2026","h1":"ETIAS para Viajeros de Negocios Venezolanos","descripcion":"ETIAS cubre viajes de negocios hasta 90 días desde Venezuela a Europa.","intro":"Los viajes de negocios de corta duración a Europa con pasaporte venezolano vigente están cubiertos por ETIAS."},
{"slug":"etias-venezuela-menores","titulo":"ETIAS Menores Venezolanos 2026","h1":"ETIAS para Menores con Pasaporte Venezolano","descripcion":"Guía ETIAS para familias venezolanas que viajan a Europa con menores.","intro":"Los menores con pasaporte venezolano necesitan ETIAS pero están exentos del pago de €7. Deben tener pasaporte vigente propio."},
{"slug":"etias-venezuela-adultos-mayores","titulo":"ETIAS Adultos Mayores Venezolanos 2026","h1":"ETIAS para Adultos Mayores Venezolanos","descripcion":"Mayores de 70 años con pasaporte venezolano están exentos del pago de ETIAS.","intro":"Los mayores de 70 años están exentos del pago de €7, pero igualmente deben obtener ETIAS con pasaporte venezolano vigente."},
{"slug":"etias-venezuela-rechazo","titulo":"Rechazo ETIAS Venezolanos 2026","h1":"Causas de Rechazo ETIAS para Venezolanos","descripcion":"Conoce las causas de rechazo de ETIAS para ciudadanos de Venezuela.","intro":"La causa más frecuente de problemas en ETIAS para venezolanos es el pasaporte próximo a vencer. Verifica vigencia antes de solicitar."},
{"slug":"etias-venezuela-vs-visa","titulo":"ETIAS vs Visa Schengen para Venezolanos","h1":"ETIAS vs Visa Schengen Venezuela","descripcion":"¿Necesitas visa o ETIAS para ir a Europa con pasaporte venezolano vigente?","intro":"Venezuela tiene exención de visa Schengen desde 2004. Desde Q4 2026 los venezolanos con pasaporte vigente necesitarán ETIAS, no visa."},
{"slug":"etias-venezuela-preguntas-frecuentes","titulo":"FAQ ETIAS Venezuela 2026","h1":"Preguntas Frecuentes ETIAS Venezuela","descripcion":"Respuestas a las preguntas más frecuentes sobre ETIAS para venezolanos.","intro":"Las dudas más comunes de viajeros venezolanos sobre ETIAS: pasaporte, pago en divisas y proceso desde el exterior."},
]
def generar_html(p):
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{p['titulo']}</title>
<meta name="description" content="{p['descripcion']}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://consultoretias.github.io/Simulador-ETIAS-/{p['slug']}.html">
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,sans-serif;color:#1a1a2e;background:#f8f9fa;line-height:1.6}}
header{{background:linear-gradient(135deg,#1a1a2e,#16213e);color:white;padding:2rem 1rem;text-align:center}}
header h1{{font-size:1.8rem;margin-bottom:.5rem}}
.badge{{display:inline-block;background:#e94560;color:white;padding:.25rem .75rem;border-radius:20px;font-size:.85rem;margin-top:.5rem}}
.container{{max-width:800px;margin:0 auto;padding:2rem 1rem}}
.card{{background:white;border-radius:12px;padding:2rem;margin-bottom:2rem;box-shadow:0 2px 8px rgba(0,0,0,.08)}}
.cta-box{{background:linear-gradient(135deg,#1a1a2e,#16213e);color:white;border-radius:12px;padding:2rem;text-align:center;margin-bottom:2rem}}
.cta-btn{{display:inline-block;background:#e94560;color:white;padding:.875rem 2rem;border-radius:8px;text-decoration:none;font-weight:bold}}
nav.breadcrumb{{background:white;padding:.75rem 1rem;font-size:.875rem;border-bottom:1px solid #eee}}
nav.breadcrumb a{{color:#e94560;text-decoration:none}}
footer{{background:#1a1a2e;color:#aaa;text-align:center;padding:2rem 1rem;font-size:.875rem}}
</style>
</head>
<body>
<nav class="breadcrumb"><a href="index.html">Inicio</a> › <a href="etias-venezuela.html">ETIAS Venezuela</a> › {p['h1']}</nav>
<header><h1>{p['h1']}</h1><span class="badge">Obligatorio desde Q4 2026</span></header>
<div class="container">
<div class="card"><p>{p['intro']}</p><br><p>{DATO_UNICO}</p></div>
<div class="cta-box">
<h2 style="margin-bottom:1rem">¿Eres elegible para ETIAS?</h2>
<p style="margin-bottom:1.5rem;opacity:.9">Verifica tu elegibilidad en 2 minutos — gratis</p>
<a href="{SIMULADOR_URL}" class="cta-btn">Usar Simulador ETIAS →</a>
</div>
<div class="card">
<h2 style="margin-bottom:1rem">Guías relacionadas</h2>
<ul style="list-style:none;display:flex;flex-direction:column;gap:.5rem">
<li><a href="etias-venezuela.html" style="color:#e94560">ETIAS Venezuela — Guía completa</a></li>
<li><a href="etias-venezuela-requisitos.html" style="color:#e94560">Requisitos ETIAS Venezuela</a></li>
<li><a href="etias-venezuela-costo.html" style="color:#e94560">Costo ETIAS Venezuela</a></li>
<li><a href="etias-colombia.html" style="color:#e94560">ETIAS Colombia</a></li>
<li><a href="etias-argentina.html" style="color:#e94560">ETIAS Argentina</a></li>
</ul>
</div>
</div>
<footer>© 2026 Consultor ETIAS · <a href="index.html" style="color:#e94560">Simulador ETIAS</a></footer>
</body>
</html>"""
for p in PAGINAS:
    fname = os.path.join(OUTPUT_DIR, f"{p['slug']}.html")
    with open(fname, "w", encoding="utf-8") as f:
        f.write(generar_html(p))
    print(f"✅ {fname}")
print(f"\n✅ {len(PAGINAS)} páginas Venezuela generadas.")
