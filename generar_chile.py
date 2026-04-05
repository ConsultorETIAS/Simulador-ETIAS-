import os
OUTPUT_DIR = "."
os.makedirs(OUTPUT_DIR, exist_ok=True)
SIMULADOR_URL = "https://consultoretias.github.io/Simulador-ETIAS-/"
EQUIVALENCIA = "aprox. $7.200 CLP"
DATO_UNICO = "Chile fue el primer país sudamericano en obtener exención de visa Schengen en 2004. ETIAS será obligatorio desde Q4 2026."
PAGINAS = [
{"slug":"etias-chile-requisitos","titulo":"Requisitos ETIAS para Chilenos 2026","h1":"Requisitos ETIAS para Chilenos","descripcion":"Lista completa de requisitos ETIAS para pasaporte chileno en 2026.","intro":"Antes de solicitar ETIAS, verifica los requisitos de la UE para ciudadanos de Chile."},
{"slug":"etias-chile-costo","titulo":"Cuánto Cuesta ETIAS para Chilenos 2026","h1":"Costo ETIAS para Chilenos","descripcion":f"ETIAS cuesta €7 euros ({EQUIVALENCIA}) para ciudadanos chilenos.","intro":f"El costo oficial de ETIAS es €7 euros ({EQUIVALENCIA}). Se paga con tarjeta internacional."},
{"slug":"etias-chile-como-solicitar","titulo":"Cómo Solicitar ETIAS desde Chile 2026","h1":"Cómo Solicitar ETIAS si Eres Chileno","descripcion":"Guía paso a paso para solicitar ETIAS con pasaporte chileno.","intro":"Solicitar ETIAS desde Chile es un proceso online de menos de 20 minutos."},
{"slug":"etias-chile-vigencia","titulo":"Vigencia ETIAS para Chilenos 2026","h1":"Vigencia de ETIAS para Pasaporte Chileno","descripcion":"ETIAS para chilenos dura 3 años o hasta que venza el pasaporte.","intro":"Tu ETIAS tendrá validez de 3 años o hasta el vencimiento de tu pasaporte chileno."},
{"slug":"etias-chile-santiago","titulo":"ETIAS desde Santiago de Chile 2026","h1":"ETIAS para Viajeros de Santiago","descripcion":"Guía ETIAS para residentes de Santiago. Vuelos a Europa y proceso de autorización.","intro":"Desde el Aeropuerto Arturo Merino Benítez (SCL) hay vuelos directos a Madrid y Frankfurt. Desde Q4 2026 todos necesitarán ETIAS."},
{"slug":"etias-chile-espana","titulo":"ETIAS Chile a España 2026","h1":"ETIAS para Chilenos que Viajan a España","descripcion":"España es el destino europeo más visitado por chilenos. Guía ETIAS 2026.","intro":"Viajar a Madrid o Barcelona con pasaporte chileno requerirá ETIAS desde Q4 2026."},
{"slug":"etias-chile-turismo","titulo":"ETIAS Turismo Chile Europa 2026","h1":"ETIAS para Turistas Chilenos en Europa","descripcion":"Todo sobre ETIAS para turistas chilenos en Europa 2026.","intro":"Si planeas visitar Europa como turista después de Q4 2026, necesitarás ETIAS."},
{"slug":"etias-chile-negocios","titulo":"ETIAS Negocios Chile Europa 2026","h1":"ETIAS para Viajeros de Negocios Chilenos","descripcion":"ETIAS cubre viajes de negocios de corta duración desde Chile a Europa.","intro":"Los viajes de negocios hasta 90 días a Europa con pasaporte chileno están cubiertos por ETIAS."},
{"slug":"etias-chile-menores","titulo":"ETIAS Menores Chilenos 2026","h1":"ETIAS para Menores con Pasaporte Chileno","descripcion":"Guía ETIAS para familias chilenas que viajan a Europa con menores de edad.","intro":"Los menores con pasaporte chileno necesitan ETIAS pero están exentos del pago de €7."},
{"slug":"etias-chile-adultos-mayores","titulo":"ETIAS Adultos Mayores Chilenos 2026","h1":"ETIAS para Adultos Mayores Chilenos","descripcion":"Mayores de 70 años con pasaporte chileno están exentos del pago de ETIAS.","intro":"Los mayores de 70 años con pasaporte chileno están exentos del pago de €7, pero deben obtener ETIAS."},
{"slug":"etias-chile-rechazo","titulo":"Rechazo ETIAS Chilenos 2026","h1":"Causas de Rechazo ETIAS para Chilenos","descripcion":"Conoce las causas de rechazo de ETIAS para ciudadanos de Chile.","intro":"Aunque la mayoría de chilenos obtienen ETIAS sin problemas, existen causas de rechazo."},
{"slug":"etias-chile-vs-visa","titulo":"ETIAS vs Visa Schengen para Chilenos","h1":"ETIAS vs Visa Schengen Chile","descripcion":"¿Necesitas visa o ETIAS para ir a Europa con pasaporte chileno?","intro":"Chile tiene exención de visa Schengen desde 2004. Desde Q4 2026 necesitarás ETIAS."},
{"slug":"etias-chile-preguntas-frecuentes","titulo":"FAQ ETIAS Chile 2026","h1":"Preguntas Frecuentes ETIAS Chile","descripcion":"Respuestas a las preguntas más frecuentes sobre ETIAS para chilenos.","intro":"Las preguntas más frecuentes de viajeros chilenos sobre ETIAS respondidas."},
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
<nav class="breadcrumb"><a href="index.html">Inicio</a> › <a href="etias-chile.html">ETIAS Chile</a> › {p['h1']}</nav>
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
<li><a href="etias-chile.html" style="color:#e94560">ETIAS Chile — Guía completa</a></li>
<li><a href="etias-chile-requisitos.html" style="color:#e94560">Requisitos ETIAS Chile</a></li>
<li><a href="etias-chile-costo.html" style="color:#e94560">Costo ETIAS Chile</a></li>
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
print(f"\n✅ {len(PAGINAS)} páginas Chile generadas.")
