import os

OUTPUT_DIR = "."
os.makedirs(OUTPUT_DIR, exist_ok=True)

SIMULADOR_URL = "https://consultoretias.github.io/Simulador-ETIAS-/"

PAIS = "Brasil"
EQUIVALENCIA = "aprox. R$40 BRL"

PAGINAS = [
    {"slug":"etias-brasil","titulo":"ETIAS Brasil 2026 | Autorización de Viaje a Europa para Brasileños","h1":"ETIAS Brasil 2026","descripcion":"Todo lo que necesitas saber sobre ETIAS si tienes pasaporte brasileño. Requisitos, costos y simulador gratuito.","intro":"El <strong>Sistema Europeo de Información y Autorización de Viaje (ETIAS)</strong> será obligatorio para ciudadanos brasileños que viajen a Europa a partir de <strong>Q4 2026</strong>.","faq_extra":[]},
    {"slug":"etias-brasil-requisitos","titulo":"Requisitos ETIAS para Brasileños 2026 | Lista Completa","h1":"Requisitos ETIAS para Ciudadanos Brasileños","descripcion":"Lista completa de requisitos para solicitar ETIAS con pasaporte de Brasil en 2026.","intro":"Antes de solicitar ETIAS, asegúrate de cumplir con todos los requisitos establecidos por la Unión Europea para ciudadanos de Brasil.","faq_extra":[("¿Mi pasaporte brasileño debe tener vigencia mínima?","Sí, tu pasaporte debe tener al menos 3 meses de vigencia más allá de la fecha de salida de Europa."),("¿Necesito seguro de viaje para ETIAS?","ETIAS no exige seguro de viaje, aunque se recomienda contratarlo para cubrir emergencias médicas.")]},
    {"slug":"etias-brasil-costo","titulo":"¿Cuánto Cuesta ETIAS para Brasileños? Precio 2026","h1":"Costo de ETIAS para Pasaporte Brasileño","descripcion":"Precio oficial de ETIAS para ciudadanos de Brasil: €7 euros. Equivalencia en reales y métodos de pago aceptados.","intro":"El costo oficial de ETIAS es <strong>€7 euros</strong> (aprox. R$40 BRL). Se paga con tarjeta de débito o crédito internacional.","faq_extra":[("¿Puedo pagar ETIAS con tarjeta brasileña?","Sí, se aceptan tarjetas Visa y Mastercard emitidas en Brasil. Verifica que tu banco permita transacciones internacionales en euros."),("¿Menores de 18 años pagan ETIAS?","No. Los menores de 18 años están exentos del pago de €7, aunque igualmente deben obtener la autorización ETIAS.")]},
    {"slug":"etias-brasil-como-solicitar","titulo":"Cómo Solicitar ETIAS desde Brasil 2026 | Guía Paso a Paso","h1":"Cómo Solicitar ETIAS si Eres Brasileño","descripcion":"Guía paso a paso para solicitar ETIAS con pasaporte de Brasil. Proceso online, documentos necesarios y tiempos de respuesta.","intro":"Solicitar ETIAS desde Brasil es un proceso completamente online que toma menos de 20 minutos. Aquí te explicamos cada paso.","faq_extra":[("¿Puedo solicitar ETIAS desde la app del celular?","Sí, la solicitud ETIAS puede completarse desde cualquier dispositivo con conexión a internet, incluidos smartphones.")]},
    {"slug":"etias-brasil-tiempo-respuesta","titulo":"¿Cuánto Tarda ETIAS para Brasileños? Tiempo de Respuesta 2026","h1":"Tiempo de Respuesta ETIAS para Ciudadanos de Brasil","descripcion":"ETIAS responde en minutos para la mayoría de los brasileños. Conoce los tiempos exactos y qué hacer si hay demoras.","intro":"La mayoría de las solicitudes ETIAS de ciudadanos brasileños se aprueban en <strong>minutos</strong>. En casos que requieren revisión manual, el plazo puede extenderse hasta 96 horas.","faq_extra":[("¿Qué hago si ETIAS tarda más de 96 horas?","Puedes contactar a las autoridades ETIAS o a la embajada del país europeo que visitarás. Se recomienda no comprar vuelos hasta tener la aprobación.")]},
    {"slug":"etias-brasil-vigencia","titulo":"¿Cuánto Dura ETIAS para Brasileños? Vigencia y Renovación 2026","h1":"Vigencia de ETIAS para Pasaporte Brasileño","descripcion":"ETIAS para brasileños tiene vigencia de 3 años o hasta que venza el pasaporte. Todo sobre renovación y múltiples entradas.","intro":"Tu ETIAS tendrá validez de <strong>3 años</strong> o hasta la fecha de vencimiento de tu pasaporte brasileño, lo que ocurra primero. Permite múltiples entradas al espacio Schengen.","faq_extra":[("¿Puedo entrar a Europa varias veces con el mismo ETIAS?","Sí. ETIAS permite múltiples entradas al espacio Schengen durante su vigencia, respetando el límite de 90 días cada 180 días."),("¿Qué pasa si renuevo mi pasaporte brasileño?","Si obtienes un pasaporte nuevo, deberás solicitar un ETIAS nuevo ya que está vinculado al número de pasaporte.")]},
    {"slug":"etias-brasil-paises-cubiertos","titulo":"¿A Qué Países de Europa Puedo Entrar con ETIAS? Guía Brasil","h1":"Países Cubiertos por ETIAS para Brasileños","descripcion":"Lista completa de los 30 países del espacio Schengen a los que puedes entrar con ETIAS teniendo pasaporte brasileño.","intro":"Con tu ETIAS puedes entrar a los <strong>30 países del espacio Schengen</strong> sin visa adicional.","faq_extra":[("¿ETIAS sirve para Reino Unido?","No. El Reino Unido no forma parte del espacio Schengen y tiene su propio sistema ETA. Necesitarás ETA UK por separado."),("¿Puedo ir a Portugal con ETIAS?","Sí. Portugal es parte del espacio Schengen y está cubierto por ETIAS.")]},
    {"slug":"etias-brasil-vs-visa","titulo":"ETIAS vs Visa Schengen para Brasileños: ¿Cuál Necesito?","h1":"ETIAS vs Visa Schengen: Guía para Ciudadanos Brasileños","descripcion":"¿Necesitas visa o ETIAS para ir a Europa con pasaporte brasileño? Comparativa clara para 2026.","intro":"Brasil tiene acuerdo de exención de visa con el espacio Schengen. A partir de Q4 2026, los brasileños necesitarán ETIAS en lugar de visa.","faq_extra":[("¿ETIAS reemplaza la visa Schengen?","No exactamente. Los brasileños nunca necesitaron visa para turismo en Europa. ETIAS es un nuevo requisito adicional para países con exención de visa."),("¿Qué es más fácil, visa o ETIAS?","ETIAS es significativamente más simple: online, €7 y aprobación en minutos. Las visas requieren cita, entrevista y documentación extensa.")]},
    {"slug":"etias-brasil-rechazo","titulo":"¿Me Pueden Rechazar ETIAS si Soy Brasileño? Causas y Soluciones","h1":"Causas de Rechazo de ETIAS para Pasaporte Brasileño","descripcion":"Conoce las causas de rechazo de ETIAS para ciudadanos de Brasil y qué hacer si tu solicitud es denegada.","intro":"Aunque la mayoría de los brasileños obtienen ETIAS sin problemas, existen causas que pueden derivar en rechazo.","faq_extra":[("¿Puedo apelar un rechazo de ETIAS?","Sí. Si tu ETIAS es rechazado, tienes derecho a apelar ante las autoridades del país Schengen de destino principal."),("¿Un arresto previo en Brasil afecta mi ETIAS?","Depende de la naturaleza del delito y si fue reportado internacionalmente. Consulta con un especialista si tienes antecedentes.")]},
    {"slug":"etias-brasil-turismo","titulo":"ETIAS para Turismo en Europa con Pasaporte Brasileño 2026","h1":"ETIAS para Turistas Brasileños en Europa","descripcion":"¿Planeas viajar a Europa como turista con pasaporte brasileño? Todo sobre ETIAS para turismo en 2026.","intro":"Si eres brasileño y planeas visitar Europa como turista después de Q4 2026, necesitarás ETIAS. El proceso es simple y completamente online.","faq_extra":[("¿Cuántos días puedo estar en Europa como turista con ETIAS?","Con ETIAS puedes permanecer hasta 90 días dentro de un período de 180 días en el espacio Schengen.")]},
    {"slug":"etias-brasil-negocios","titulo":"ETIAS para Viajes de Negocios desde Brasil a Europa 2026","h1":"ETIAS para Viajeros de Negocios Brasileños","descripcion":"¿Viajas a Europa por negocios con pasaporte brasileño? ETIAS cubre visitas de negocios de corta duración.","intro":"Los viajes de negocios de corta duración (hasta 90 días) a Europa con pasaporte brasileño están cubiertos por ETIAS.","faq_extra":[("¿Puedo firmar contratos o asistir a reuniones con ETIAS?","Sí. ETIAS cubre reuniones, conferencias, negociaciones y ferias comerciales, siempre que no impliquen empleo remunerado local."),("¿Necesito carta de invitación para ETIAS de negocios?","No es obligatorio, pero tener una carta de tu contraparte europea puede facilitar el proceso en caso de revisión manual.")]},
    {"slug":"etias-brasil-estudios","titulo":"ETIAS para Estudiantes Brasileños en Europa 2026","h1":"ETIAS para Estudiantes con Pasaporte Brasileño","descripcion":"¿Eres estudiante brasileño y planeas ir a Europa? Conoce si ETIAS cubre cursos cortos y programas de intercambio.","intro":"ETIAS cubre estancias de <strong>hasta 90 días</strong>, lo que lo hace válido para cursos cortos, conferencias académicas o visitas de exploración universitaria.","faq_extra":[("¿ETIAS sirve para un semestre de intercambio?","No. Un semestre (4-6 meses) supera el límite de 90 días de ETIAS. Para estudios largos necesitarás visa de estudiante del país correspondiente."),("¿Puedo ir a una entrevista de admisión universitaria con ETIAS?","Sí. Las entrevistas, visitas a campus y cursos intensivos cortos están cubiertos por ETIAS.")]},
    {"slug":"etias-brasil-menores","titulo":"ETIAS para Menores Brasileños: Guía para Familias 2026","h1":"ETIAS para Menores de Edad con Pasaporte Brasileño","descripcion":"¿Viajas a Europa con tus hijos brasileños? Guía completa sobre ETIAS para menores de edad en 2026.","intro":"Los menores de edad con pasaporte brasileño también necesitan ETIAS para viajar a Europa, pero están exentos del pago de €7.","faq_extra":[("¿Un menor puede viajar a Europa solo con ETIAS?","ETIAS es solo la autorización de viaje. Los menores que viajan sin ambos padres también necesitan carta de autorización de los tutores legales."),("¿El ETIAS de mi hijo está vinculado al mío?","No. Cada viajero, incluidos los menores, debe tener su propio ETIAS vinculado a su propio pasaporte.")]},
    {"slug":"etias-brasil-adultos-mayores","titulo":"ETIAS para Adultos Mayores Brasileños: Todo lo que Necesitas Saber","h1":"ETIAS para Adultos Mayores con Pasaporte Brasileño","descripcion":"Guía simplificada de ETIAS para brasileños mayores de 70 años. Exenciones, proceso y recomendaciones.","intro":"Los adultos mayores de 70 años con pasaporte brasileño están <strong>exentos del pago</strong> de €7, aunque igualmente deben obtener la autorización ETIAS.","faq_extra":[("¿Los mayores de 70 años tienen algún beneficio adicional?","Además de la exención de pago, el proceso es idéntico al de cualquier otro viajero.")]},
    {"slug":"etias-brasil-sao-paulo","titulo":"ETIAS desde São Paulo 2026 | Guía para Viajeros Paulistanos","h1":"ETIAS para Viajeros de São Paulo hacia Europa","descripcion":"Guía ETIAS específica para residentes de São Paulo. Aeropuertos, vuelos a Europa y proceso de autorización.","intro":"São Paulo es el principal hub de conexión entre Brasil y Europa. Si viajas desde Guarulhos (GRU), necesitarás ETIAS a partir de Q4 2026.","faq_extra":[("¿Desde qué aeropuertos de SP salen vuelos directos a Europa?","El Aeropuerto de Guarulhos (GRU) opera vuelos directos a Lisboa, Madrid, Frankfurt, París y Londres.")]},
    {"slug":"etias-brasil-rio","titulo":"ETIAS desde Río de Janeiro 2026 | Guía para Viajeros Cariocas","h1":"ETIAS para Viajeros de Río de Janeiro hacia Europa","descripcion":"Todo sobre ETIAS para residentes de Río de Janeiro que planean viajar a Europa en 2026.","intro":"Desde el Aeropuerto Internacional Galeão (GIG) en Río de Janeiro operan vuelos a varios destinos europeos. A partir de Q4 2026 todos necesitarán ETIAS.","faq_extra":[]},
    {"slug":"etias-brasil-portugal","titulo":"ETIAS Brasil → Portugal 2026 | Guía Especial para Brasileños","h1":"ETIAS para Brasileños que Viajan a Portugal","descripcion":"Guía especial ETIAS para la ruta Brasil–Portugal. El destino europeo más visitado por brasileños también requiere ETIAS desde Q4 2026.","intro":"Portugal es el destino europeo más popular entre los brasileños por los lazos culturales e idiomáticos. A partir de Q4 2026 el ETIAS será obligatorio incluso para entrar a Portugal.","faq_extra":[("¿Portugal tiene algún proceso especial para brasileños?","No. ETIAS es un sistema unificado de la UE. Portugal no tiene proceso diferenciado para brasileños.")]},
    {"slug":"etias-brasil-espana","titulo":"ETIAS para Brasileños que Viajan a España 2026","h1":"ETIAS Brasil → España: Todo lo que Necesitas Saber","descripcion":"¿Planeas ir a España con pasaporte brasileño? Guía completa sobre ETIAS para la ruta Brasil–España en 2026.","intro":"España es uno de los destinos más visitados por turistas brasileños en Europa. Con ETIAS, viajar a Madrid o Barcelona solo requiere una autorización previa online.","faq_extra":[("¿Puedo entrar a España directamente desde Brasil con ETIAS?","Sí. España tiene vuelos directos desde São Paulo y Río de Janeiro, y ETIAS es válido para entrada directa.")]},
    {"slug":"etias-brasil-italia","titulo":"ETIAS para Brasileños que Viajan a Italia 2026","h1":"ETIAS Brasil → Italia: Guía Completa","descripcion":"¿Quieres visitar Roma, Milán o Venecia con pasaporte brasileño? Todo sobre ETIAS para la ruta Brasil–Italia.","intro":"Italia es uno de los destinos soñados para los brasileños, con millones de descendientes de italianos en el país. A partir de Q4 2026 se requiere ETIAS.","faq_extra":[("¿Los brasileños con ciudadanía italiana doble necesitan ETIAS?","No. Si tienes pasaporte italiano eres ciudadano de la UE y no necesitas ETIAS. Solo aplica para quienes viajan con pasaporte brasileño.")]},
    {"slug":"etias-brasil-preguntas-frecuentes","titulo":"Preguntas Frecuentes ETIAS para Brasileños 2026 | FAQ Completo","h1":"FAQ: Todo sobre ETIAS para Ciudadanos de Brasil","descripcion":"Respuestas a las preguntas más frecuentes sobre ETIAS para viajeros con pasaporte brasileño.","intro":"Recopilamos las preguntas más frecuentes de viajeros brasileños sobre ETIAS. Si tienes dudas, aquí encontrarás respuestas claras y actualizadas.","faq_extra":[("¿ETIAS es lo mismo que el ESTA de USA?","Son conceptos similares: ambos son autorizaciones de viaje electrónicas para países con exención de visa. ETIAS es el sistema europeo equivalente al ESTA americano."),("¿Puedo solicitar ETIAS si tengo doble ciudadanía?","Debes solicitarlo con el pasaporte que usarás para entrar a Europa. Si tienes pasaporte de país UE, no necesitas ETIAS."),("¿ETIAS debe solicitarse con anticipación?","Se recomienda solicitarlo al menos 72 horas antes del viaje, aunque muchas solicitudes se aprueban en minutos."),("¿Existe agencia oficial ETIAS en Brasil?","No. ETIAS es un trámite 100% online ante la Unión Europea. No hay oficinas físicas en Brasil.")]},
]

def generar_html(p):
    faqs_base = [
        ("¿ETIAS es una visa?","No. ETIAS es una <strong>autorización de viaje electrónica</strong>, no una visa. Los ciudadanos brasileños ya están exentos de visa Schengen; ETIAS es un requisito adicional desde Q4 2026."),
        ("¿Cuánto cuesta ETIAS para brasileños?","El costo oficial es <strong>€7 euros</strong> (aprox. R$40 BRL). Menores de 18 y mayores de 70 años están exentos del pago."),
        ("¿Cuánto tiempo tarda la aprobación?","La mayoría se aprueban en <strong>minutos</strong>. En casos de revisión manual puede tardar hasta 96 horas."),
        ("¿Con qué pasaporte debo solicitar ETIAS?","Debes solicitarlo con el pasaporte brasileño que usarás para viajar a Europa. Cada pasaporte requiere su propio ETIAS."),
    ]
    faqs_all = faqs_base + p.get("faq_extra",[])
    faqs_html = "\n".join(f'    <div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q,a in faqs_all)
    pasos = [
        ("1","Completa el formulario online","Ingresa datos personales, número de pasaporte y detalles del viaje en el portal oficial ETIAS."),
        ("2","Paga €7 con tarjeta","Se acepta tarjeta de débito o crédito internacional. Aprox. R$40 BRL."),
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
<nav class="breadcrumb"><a href="{SIMULADOR_URL}">Inicio</a> › <a href="etias-brasil.html">ETIAS Brasil</a> › {p['h1']}</nav>
<div class="alert"><strong>⚠️ Importante:</strong> ETIAS será obligatorio para ciudadanos de Brasil a partir de <strong>Q4 2026</strong>.</div>
<p>{p['intro']}</p>
<h2>Requisitos para Ciudadanos de Brasil</h2>
<ul class="req-list">
<li>Pasaporte brasileño válido (más de 3 meses de vigencia)</li>
<li>Correo electrónico activo</li>
<li>Tarjeta de débito/crédito internacional para el pago de €7</li>
<li>Acceso a internet (solicitud 100% online)</li>
<li>Máximo 90 días de estancia por cada 180 días</li>
</ul>
<h2>Proceso de Solicitud ETIAS</h2>
{pasos_html}
<div class="cta-box"><p>¿Quieres saber si cumples los requisitos para obtener ETIAS con tu pasaporte brasileño?</p><a class="cta-btn" href="{SIMULADOR_URL}">🛂 Probar Simulador ETIAS Gratis</a></div>
<h2>Países del Espacio Schengen Cubiertos por ETIAS</h2>
<div class="countries">{paises_html}</div>
<h2>Preguntas Frecuentes sobre ETIAS para Brasileños</h2>
{faqs_html}
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

print(f"\nListo: {len(PAGINAS)} paginas generadas")
