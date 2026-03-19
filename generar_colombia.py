import os

OUTPUT_DIR = "."
os.makedirs(OUTPUT_DIR, exist_ok=True)

SIMULADOR_URL = "https://consultoretias.github.io/Simulador-ETIAS-/"

EQUIVALENCIA = "aprox. $31.000 COP"
DATO_UNICO = "Colombia fue incluida en la lista de exención de visa Schengen en 2015, lo que permite a sus ciudadanos viajar a Europa sin visa. ETIAS será el nuevo requisito a partir de Q4 2026."

RELATED_LINKS = """
<div class="related-links">
  <h2>Guías relacionadas</h2>
  <ul>
    <li><a href="etias-colombia.html">ETIAS Colombia — Guía completa</a></li>
    <li><a href="etias-colombia-requisitos.html">Requisitos ETIAS para colombianos</a></li>
    <li><a href="etias-colombia-costo.html">Costo de ETIAS para colombianos</a></li>
    <li><a href="etias-brasil.html">ETIAS Brasil</a></li>
    <li><a href="etias-mexico.html">ETIAS México</a></li>
  </ul>
</div>"""

PAGINAS = [
    {"slug":"etias-colombia","titulo":"ETIAS Colombia 2026 | Autorización de Viaje a Europa para Colombianos","h1":"ETIAS Colombia 2026","descripcion":"Todo lo que necesitas saber sobre ETIAS si tienes pasaporte colombiano. Requisitos, costos y simulador gratuito.","intro":"El <strong>Sistema Europeo de Información y Autorización de Viaje (ETIAS)</strong> será obligatorio para ciudadanos colombianos que viajen a Europa a partir de <strong>Q4 2026</strong>. " + DATO_UNICO,"faq_extra":[]},
    {"slug":"etias-colombia-requisitos","titulo":"Requisitos ETIAS para Colombianos 2026 | Lista Completa","h1":"Requisitos ETIAS para Ciudadanos Colombianos","descripcion":"Lista completa de requisitos para solicitar ETIAS con pasaporte de Colombia en 2026.","intro":"Antes de solicitar ETIAS, asegúrate de cumplir con todos los requisitos establecidos por la Unión Europea para ciudadanos de Colombia.","faq_extra":[("¿Mi pasaporte colombiano debe tener vigencia mínima?","Sí, tu pasaporte debe tener al menos 3 meses de vigencia más allá de la fecha de salida de Europa."),("¿Necesito seguro de viaje para ETIAS?","ETIAS no exige seguro de viaje, aunque se recomienda contratarlo para cubrir emergencias médicas en Europa.")]},
    {"slug":"etias-colombia-costo","titulo":"¿Cuánto Cuesta ETIAS para Colombianos? Precio 2026","h1":"Costo de ETIAS para Pasaporte Colombiano","descripcion":"Precio oficial de ETIAS para ciudadanos de Colombia: €7 euros. Equivalencia en pesos colombianos y métodos de pago aceptados.","intro":f"El costo oficial de ETIAS es <strong>€7 euros</strong> ({EQUIVALENCIA}). Se paga con tarjeta de débito o crédito internacional.","faq_extra":[("¿Puedo pagar ETIAS con tarjeta colombiana?","Sí, se aceptan tarjetas Visa y Mastercard emitidas en Colombia. Verifica que tu banco permita transacciones internacionales en euros."),("¿Menores de 18 años pagan ETIAS?","No. Los menores de 18 años están exentos del pago de €7, aunque igualmente deben obtener la autorización ETIAS.")]},
    {"slug":"etias-colombia-como-solicitar","titulo":"Cómo Solicitar ETIAS desde Colombia 2026 | Guía Paso a Paso","h1":"Cómo Solicitar ETIAS si Eres Colombiano","descripcion":"Guía paso a paso para solicitar ETIAS con pasaporte de Colombia. Proceso online, documentos necesarios y tiempos de respuesta.","intro":"Solicitar ETIAS desde Colombia es un proceso completamente online que toma menos de 20 minutos.","faq_extra":[("¿Puedo solicitar ETIAS desde el celular?","Sí, la solicitud puede completarse desde cualquier dispositivo con conexión a internet, incluidos smartphones.")]},
    {"slug":"etias-colombia-tiempo-respuesta","titulo":"¿Cuánto Tarda ETIAS para Colombianos? Tiempo de Respuesta 2026","h1":"Tiempo de Respuesta ETIAS para Ciudadanos de Colombia","descripcion":"ETIAS responde en minutos para la mayoría de los colombianos. Conoce los tiempos exactos y qué hacer si hay demoras.","intro":"La mayoría de las solicitudes ETIAS de ciudadanos colombianos se aprueban en <strong>minutos</strong>. En casos de revisión manual, el plazo puede extenderse hasta 96 horas.","faq_extra":[("¿Qué hago si ETIAS tarda más de 96 horas?","Puedes contactar a las autoridades ETIAS o a la embajada del país europeo que visitarás. Se recomienda no comprar vuelos hasta tener la aprobación.")]},
    {"slug":"etias-colombia-vigencia","titulo":"¿Cuánto Dura ETIAS para Colombianos? Vigencia y Renovación 2026","h1":"Vigencia de ETIAS para Pasaporte Colombiano","descripcion":"ETIAS para colombianos tiene vigencia de 3 años o hasta que venza el pasaporte. Todo sobre renovación y múltiples entradas.","intro":"Tu ETIAS tendrá validez de <strong>3 años</strong> o hasta la fecha de vencimiento de tu pasaporte colombiano, lo que ocurra primero.","faq_extra":[("¿Puedo entrar a Europa varias veces con el mismo ETIAS?","Sí. ETIAS permite múltiples entradas al espacio Schengen durante su vigencia, respetando el límite de 90 días cada 180 días."),("¿Qué pasa si renuevo mi pasaporte colombiano?","Si obtienes un pasaporte nuevo, deberás solicitar un ETIAS nuevo ya que está vinculado al número de pasaporte.")]},
    {"slug":"etias-colombia-paises-cubiertos","titulo":"¿A Qué Países de Europa Puedo Entrar con ETIAS? Guía Colombia","h1":"Países Cubiertos por ETIAS para Colombianos","descripcion":"Lista completa de los 30 países del espacio Schengen a los que puedes entrar con ETIAS teniendo pasaporte colombiano.","intro":"Con tu ETIAS puedes entrar a los <strong>30 países del espacio Schengen</strong> sin visa adicional.","faq_extra":[("¿ETIAS sirve para Reino Unido?","No. El Reino Unido tiene su propio sistema ETA. Necesitarás ETA UK por separado."),("¿Puedo ir a España con ETIAS?","Sí. España es parte del espacio Schengen y uno de los destinos favoritos de los colombianos en Europa.")]},
    {"slug":"etias-colombia-vs-visa","titulo":"ETIAS vs Visa Schengen para Colombianos: ¿Cuál Necesito?","h1":"ETIAS vs Visa Schengen: Guía para Ciudadanos Colombianos","descripcion":"¿Necesitas visa o ETIAS para ir a Europa con pasaporte colombiano? Comparativa clara para 2026.","intro":"Colombia obtuvo exención de visa Schengen en 2015. Los colombianos no necesitan visa para turismo en Europa. A partir de Q4 2026 necesitarán ETIAS.","faq_extra":[("¿ETIAS reemplaza la visa Schengen?","No exactamente. Los colombianos nunca necesitaron visa para turismo. ETIAS es un nuevo requisito adicional para países con exención de visa."),("¿Qué es más fácil, visa o ETIAS?","ETIAS es significativamente más simple: online, €7 y aprobación en minutos.")]},
    {"slug":"etias-colombia-rechazo","titulo":"¿Me Pueden Rechazar ETIAS si Soy Colombiano? Causas y Soluciones","h1":"Causas de Rechazo de ETIAS para Pasaporte Colombiano","descripcion":"Conoce las causas de rechazo de ETIAS para ciudadanos de Colombia y qué hacer si tu solicitud es denegada.","intro":"Aunque la mayoría de los colombianos obtienen ETIAS sin problemas, existen causas que pueden derivar en rechazo.","faq_extra":[("¿Puedo apelar un rechazo de ETIAS?","Sí. Si tu ETIAS es rechazado, tienes derecho a apelar ante las autoridades del país Schengen de destino principal."),("¿Antecedentes judiciales en Colombia afectan mi ETIAS?","Depende de la naturaleza del delito y si fue reportado internacionalmente. Consulta con un especialista si tienes antecedentes.")]},
    {"slug":"etias-colombia-turismo","titulo":"ETIAS para Turismo en Europa con Pasaporte Colombiano 2026","h1":"ETIAS para Turistas Colombianos en Europa","descripcion":"¿Planeas viajar a Europa como turista con pasaporte colombiano? Todo sobre ETIAS para turismo en 2026.","intro":"Si eres colombiano y planeas visitar Europa como turista después de Q4 2026, necesitarás ETIAS. El proceso es simple y completamente online.","faq_extra":[("¿Cuántos días puedo estar en Europa como turista con ETIAS?","Con ETIAS puedes permanecer hasta 90 días dentro de un período de 180 días en el espacio Schengen.")]},
    {"slug":"etias-colombia-negocios","titulo":"ETIAS para Viajes de Negocios desde Colombia a Europa 2026","h1":"ETIAS para Viajeros de Negocios Colombianos","descripcion":"¿Viajas a Europa por negocios con pasaporte colombiano? ETIAS cubre visitas de negocios de corta duración.","intro":"Los viajes de negocios de corta duración (hasta 90 días) a Europa con pasaporte colombiano están cubiertos por ETIAS.","faq_extra":[("¿Puedo asistir a reuniones o ferias con ETIAS?","Sí. ETIAS cubre reuniones, conferencias y ferias comerciales, siempre que no impliquen empleo remunerado local.")]},
    {"slug":"etias-colombia-estudios","titulo":"ETIAS para Estudiantes Colombianos en Europa 2026","h1":"ETIAS para Estudiantes con Pasaporte Colombiano","descripcion":"¿Eres estudiante colombiano y planeas ir a Europa? Conoce si ETIAS cubre cursos cortos y programas de intercambio.","intro":"ETIAS cubre estancias de <strong>hasta 90 días</strong>, válido para cursos cortos, conferencias académicas o visitas de exploración universitaria.","faq_extra":[("¿ETIAS sirve para un semestre de intercambio?","No. Un semestre supera el límite de 90 días. Para estudios largos necesitarás visa de estudiante del país correspondiente."),("¿Puedo ir a una entrevista de admisión con ETIAS?","Sí. Las entrevistas y visitas a campus están cubiertos por ETIAS.")]},
    {"slug":"etias-colombia-menores","titulo":"ETIAS para Menores Colombianos: Guía para Familias 2026","h1":"ETIAS para Menores de Edad con Pasaporte Colombiano","descripcion":"¿Viajas a Europa con tus hijos colombianos? Guía completa sobre ETIAS para menores de edad en 2026.","intro":"Los menores de edad con pasaporte colombiano también necesitan ETIAS para viajar a Europa, pero están exentos del pago de €7.","faq_extra":[("¿Un menor puede viajar a Europa solo con ETIAS?","ETIAS es solo la autorización de viaje. Los menores que viajan sin ambos padres también necesitan carta de autorización de los tutores legales.")]},
    {"slug":"etias-colombia-adultos-mayores","titulo":"ETIAS para Adultos Mayores Colombianos: Todo lo que Necesitas Saber","h1":"ETIAS para Adultos Mayores con Pasaporte Colombiano","descripcion":"Guía simplificada de ETIAS para colombianos mayores de 70 años. Exenciones, proceso y recomendaciones.","intro":"Los adultos mayores de 70 años con pasaporte colombiano están <strong>exentos del pago</strong> de €7, aunque igualmente deben obtener la autorización ETIAS.","faq_extra":[("¿Los mayores de 70 años tienen proceso diferente?","No. El proceso es idéntico al de cualquier otro viajero, solo están exentos del pago.")]},
    {"slug":"etias-colombia-bogota","titulo":"ETIAS desde Bogotá 2026 | Guía para Viajeros Bogotanos","h1":"ETIAS para Viajeros de Bogotá hacia Europa","descripcion":"Guía ETIAS específica para residentes de Bogotá. Aeropuertos, vuelos a Europa y proceso de autorización.","intro":"Bogotá es el principal hub aéreo de Colombia. Desde el Aeropuerto El Dorado (BOG) operan vuelos directos a Madrid, Lisboa y otras ciudades europeas. A partir de Q4 2026 todos necesitarán ETIAS.","faq_extra":[("¿Desde El Dorado hay vuelos directos a Europa?","Sí. Hay vuelos directos a Madrid (Iberia, Avianca), Lisboa y otras ciudades europeas desde el Aeropuerto El Dorado (BOG).")]},
    {"slug":"etias-colombia-medellin","titulo":"ETIAS desde Medellín 2026 | Guía para Viajeros Paisas","h1":"ETIAS para Viajeros de Medellín hacia Europa","descripcion":"Todo sobre ETIAS para residentes de Medellín que planean viajar a Europa en 2026.","intro":"Desde el Aeropuerto Internacional José María Córdova (MDE) en Medellín operan conexiones a Europa vía hubs principales. A partir de Q4 2026 todos los colombianos necesitarán ETIAS.","faq_extra":[]},
    {"slug":"etias-colombia-espana","titulo":"ETIAS Colombia → España 2026 | Guía Especial","h1":"ETIAS para Colombianos que Viajan a España","descripcion":"España es el destino europeo más visitado por colombianos. Guía completa ETIAS para la ruta Colombia–España 2026.","intro":"España concentra la mayor comunidad colombiana en Europa, con más de 800.000 residentes colombianos. Viajar a Madrid o Barcelona con ETIAS será el nuevo estándar desde Q4 2026.","faq_extra":[("¿Puedo visitar a familiares en España con ETIAS?","Sí. Las visitas familiares de hasta 90 días están cubiertas por ETIAS, sin necesidad de visa adicional."),("¿Necesito demostrar solvencia económica para ETIAS?","ETIAS no exige demostración de fondos en el formulario, a diferencia de la visa Schengen tradicional.")]},
    {"slug":"etias-colombia-francia","titulo":"ETIAS para Colombianos que Viajan a Francia 2026","h1":"ETIAS Colombia → Francia: Guía Completa","descripcion":"¿Quieres visitar París con pasaporte colombiano? Todo sobre ETIAS para la ruta Colombia–Francia en 2026.","intro":"Francia y especialmente París son destinos aspiracionales para muchos colombianos. A partir de Q4 2026, viajar a Francia con pasaporte colombiano requerirá ETIAS.","faq_extra":[("¿ETIAS me permite entrar directamente a Francia desde Colombia?","Sí. Con escala en cualquier aeropuerto europeo o Schengen, tu ETIAS es válido para entrada a Francia.")]},
    {"slug":"etias-colombia-italia","titulo":"ETIAS para Colombianos que Viajan a Italia 2026","h1":"ETIAS Colombia → Italia: Guía Completa","descripcion":"¿Planeas visitar Roma o Milán con pasaporte colombiano? Todo sobre ETIAS para la ruta Colombia–Italia en 2026.","intro":"Italia es uno de los destinos más populares entre los turistas colombianos en Europa. A partir de Q4 2026 se requiere ETIAS para entrar.","faq_extra":[("¿Puedo hacer un tour por varios países europeos con un solo ETIAS?","Sí. Un solo ETIAS es válido para todos los países del espacio Schengen durante su vigencia.")]},
    {"slug":"etias-colombia-preguntas-frecuentes","titulo":"Preguntas Frecuentes ETIAS para Colombianos 2026 | FAQ Completo","h1":"FAQ: Todo sobre ETIAS para Ciudadanos de Colombia","descripcion":"Respuestas a las preguntas más frecuentes sobre ETIAS para viajeros con pasaporte colombiano.","intro":"Recopilamos las preguntas más frecuentes de viajeros colombianos sobre ETIAS.","faq_extra":[("¿ETIAS es lo mismo que el ESTA de USA?","Son conceptos similares: ambos son autorizaciones electrónicas para países con exención de visa. ETIAS es el sistema europeo equivalente al ESTA americano."),("¿Cuándo exactamente entra en vigor ETIAS para colombianos?","La UE ha anunciado Q4 2026 (octubre-diciembre). Se recomienda estar pendiente de la fecha exacta en fuentes oficiales."),("¿Existe agencia oficial ETIAS en Colombia?","No. ETIAS es un trámite 100% online ante la Unión Europea. No hay oficinas físicas en Colombia."),("¿Puedo solicitar ETIAS para varios viajes futuros?","Sí. Un ETIAS aprobado es válido por 3 años y cubre múltiples entradas al espacio Schengen.")]},
]

def generar_html(p):
    faqs_base = [
        ("¿ETIAS es una visa?","No. ETIAS es una <strong>autorización de viaje electrónica</strong>, no una visa. Los ciudadanos colombianos ya están exentos de visa Schengen; ETIAS es un requisito adicional desde Q4 2026."),
        ("¿Cuánto cuesta ETIAS para colombianos?",f"El costo oficial es <strong>€7 euros</strong> ({EQUIVALENCIA}). Menores de 18 y mayores de 70 años están exentos del pago."),
        ("¿Cuánto tiempo tarda la aprobación?","La mayoría se aprueban en <strong>minutos</strong>. En casos de revisión manual puede tardar hasta 96 horas."),
        ("¿Con qué pasaporte debo solicitar ETIAS?","Debes solicitarlo con el pasaporte colombiano que usarás para viajar a Europa. Cada pasaporte requiere su propio ETIAS."),
    ]
    faqs_all = faqs_base + p.get("faq_extra",[])
    faqs_html = "\n".join(f'    <div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q,a in faqs_all)
    pasos = [
        ("1","Completa el formulario online","Ingresa datos personales, número de pasaporte y detalles del viaje en el portal oficial ETIAS."),
        ("2","Paga €7 con tarjeta",f"Se acepta tarjeta de débito o crédito internacional. {EQUIVALENCIA}."),
        ("3","Espera la respuesta","La mayoría de las solicitudes se resuelven en minutos. Máximo 96 horas en revisión manual."),
        ("4","Guarda tu autorización","Recibirás confirmación por email. Guárdala en tu celular o imprime una copia."),
    ]
    pasos_html = "\n".join(f'    <div class="step"><span class="step-number">{n}</span><div><strong>{t}</strong><p>{d}</p></div></div>' for n,t,d in pasos)
    paises = ["Alemania","Austria","Bélgica","Croacia","Chequia","Dinamarca","Eslovaquia","Eslovenia","España","Estonia","Finlandia","Francia","Grecia","Hungría","Islandia","Italia","Letonia","Liechtenstein","Lituania","Luxemburgo","Malta","Noruega","Países Bajos","Polonia","Portugal","Rumania","Suecia","Suiza","Bulgaria","Chipre"]
    paises_html = "".join(f'<span class="country-tag">{c}</span>' for c in paises)
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
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;color:#1a1a2e;background:#f8f9fa;line-height:1.6}}
header{{background:linear-gradient(135deg,#1a1a2e 0%,#16213e 100%);color:white;padding:2rem 1rem;text-align:center}}
header h1{{font-size:2rem;margin-bottom:.5rem}}
.badge{{display:inline-block;background:#e94560;color:white;padding:.25rem .75rem;border-radius:20px;font-size:.85rem;margin-top:.5rem}}
.container{{max-width:800px;margin:0 auto;padding:2rem 1rem}}
.alert{{background:#fff3cd;border-left:4px solid #ffc107;padding:1rem 1.25rem;border-radius:4px;margin-bottom:2rem}}
h2{{font-size:1.4rem;color:#1a1a2e;margin:2rem 0 1rem;border-bottom:2px solid #e94560;padding-bottom:.4rem}}
.req-list{{list-style:none;padding:0}}
.req-list li{{padding:.6rem 0;border-bottom:1px solid #eee;display:flex;align-items:flex-start;gap:.5rem}}
.req-list li::before{{content:"✅";flex-shrink:0}}
.step{{display:flex;gap:1rem;margin-bottom:1.5rem;align-items:flex-start}}
.step-number{{background:#e94560;color:white;width:2rem;height:2rem;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:bold;flex-shrink:0}}
.cta-box{{background:#1a1a2e;color:white;padding:2rem;border-radius:8px;text-align:center;margin:2rem 0}}
.cta-box p{{margin-bottom:1rem;opacity:.9}}
.cta-btn{{display:inline-block;background:#e94560;color:white;padding:.9rem 2rem;border-radius:6px;text-decoration:none;font-weight:bold;font-size:1.05rem}}
.faq-item{{background:white;border-radius:6px;padding:1.25rem;margin-bottom:1rem;box-shadow:0 1px 3px rgba(0,0,0,.07)}}
.faq-item h3{{font-size:1rem;color:#1a1a2e;margin-bottom:.5rem}}
.countries{{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.75rem}}
.country-tag{{background:#e8f4f8;border:1px solid #b8d9e8;border-radius:4px;padding:.2rem .6rem;font-size:.85rem}}
.related-links{{background:#f0f4f8;border-radius:8px;padding:1.25rem;margin:2rem 0}}
.related-links h2{{border:none;margin-top:0;font-size:1.1rem}}
.related-links ul{{list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.75rem}}
.related-links a{{color:#e94560;text-decoration:none;background:white;padding:.3rem .8rem;border-radius:4px;border:1px solid #ddd;font-size:.9rem}}
footer{{text-align:center;padding:2rem 1rem;font-size:.8rem;color:#999;border-top:1px solid #e0e0e0;margin-top:2rem}}
nav.breadcrumb{{font-size:.85rem;color:#888;margin-bottom:1.5rem}}
nav.breadcrumb a{{color:#e94560;text-decoration:none}}
</style>
</head>
<body>
<header>
<h1>{p['h1']}</h1>
<div class="badge">⚠️ Obligatorio desde Q4 2026</div>
<p style="margin-top:.75rem;opacity:.85;font-size:.95rem">Actualizado: marzo 2026</p>
</header>
<div class="container">
<nav class="breadcrumb"><a href="{SIMULADOR_URL}">Inicio</a> › <a href="etias-colombia.html">ETIAS Colombia</a> › {p['h1']}</nav>
<div class="alert"><strong>⚠️ Importante:</strong> ETIAS será obligatorio para ciudadanos de Colombia a partir de <strong>Q4 2026</strong>.</div>
<p>{p['intro']}</p>
<h2>Requisitos para Ciudadanos de Colombia</h2>
<ul class="req-list">
<li>Pasaporte colombiano válido (más de 3 meses de vigencia)</li>
<li>Correo electrónico activo</li>
<li>Tarjeta de débito/crédito internacional para el pago de €7</li>
<li>Acceso a internet (solicitud 100% online)</li>
<li>Máximo 90 días de estancia por cada 180 días</li>
</ul>
<h2>Proceso de Solicitud ETIAS</h2>
{pasos_html}
<div class="cta-box"><p>¿Quieres saber si cumples los requisitos para obtener ETIAS con tu pasaporte colombiano?</p><a class="cta-btn" href="{SIMULADOR_URL}">🛂 Probar Simulador ETIAS Gratis</a></div>
<h2>Países del Espacio Schengen Cubiertos por ETIAS</h2>
<div class="countries">{paises_html}</div>
<h2>Preguntas Frecuentes sobre ETIAS para Colombianos</h2>
{faqs_html}
{RELATED_LINKS}
<div class="cta-box" style="margin-top:2rem"><p>Simula tu solicitud ETIAS ahora y recibe tu declaración en PDF — completamente gratis.</p><a class="cta-btn" href="{SIMULADOR_URL}">🚀 Simular ETIAS Ahora</a></div>
</div>
<footer>ETIAS Consultant Simulator | No afiliado a la Unión Europea | Información con fines educativos | <a href="{SIMULADOR_URL}" style="color:#e94560">Volver al Simulador</a></footer>
</body>
</html>"""

for p in PAGINAS:
    path = os.path.join(OUTPUT_DIR, f"{p['slug']}.html")
    with open(path,"w",encoding="utf-8") as f:
        f.write(generar_html(p))
    print(f"OK {path}")

print(f"\nListo: {len(PAGINAS)} paginas Colombia generadas")
print("\n--- SITEMAP URLS ---")
for p in PAGINAS:
    pri = "0.9" if p['slug'] == "etias-colombia" else ("0.5" if any(x in p['slug'] for x in ["bogota","medellin"]) else "0.7")
    print(f'  <url><loc>https://consultoretias.github.io/Simulador-ETIAS-/{p["slug"]}.html</loc><changefreq>monthly</changefreq><priority>{pri}</priority></url>')
