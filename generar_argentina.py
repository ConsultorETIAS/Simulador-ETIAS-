import os

OUTPUT_DIR = "."
os.makedirs(OUTPUT_DIR, exist_ok=True)

SIMULADOR_URL = "https://consultoretias.github.io/Simulador-ETIAS-/"

PAIS = "Argentina"
EQUIVALENCIA = "aprox. $7.000 ARS"

PAGINAS = [
    {"slug":"etias-argentina","titulo":"ETIAS Argentina 2026 | Autorización de Viaje a Europa para Argentinos","h1":"ETIAS Argentina 2026","descripcion":"Todo lo que necesitas saber sobre ETIAS si tienes pasaporte argentino. Requisitos, costos y simulador gratuito.","intro":"El <strong>Sistema Europeo de Información y Autorización de Viaje (ETIAS)</strong> será obligatorio para ciudadanos argentinos que viajen a Europa a partir de <strong>Q4 2026</strong>.","faq_extra":[]},
    {"slug":"etias-argentina-requisitos","titulo":"Requisitos ETIAS para Argentinos 2026 | Lista Completa","h1":"Requisitos ETIAS para Ciudadanos Argentinos","descripcion":"Lista completa de requisitos para solicitar ETIAS con pasaporte de Argentina en 2026.","intro":"Antes de solicitar ETIAS, asegúrate de cumplir con todos los requisitos establecidos por la Unión Europea para ciudadanos de Argentina.","faq_extra":[("¿Mi pasaporte argentino debe tener vigencia mínima?","Sí, tu pasaporte debe tener al menos 3 meses de vigencia más allá de la fecha de salida de Europa."),("¿Necesito seguro de viaje para ETIAS?","ETIAS no exige seguro de viaje, aunque se recomienda contratarlo para cubrir emergencias médicas en el exterior.")]},
    {"slug":"etias-argentina-costo","titulo":"¿Cuánto Cuesta ETIAS para Argentinos? Precio 2026","h1":"Costo de ETIAS para Pasaporte Argentino","descripcion":"Precio oficial de ETIAS para ciudadanos de Argentina: €7 euros. Equivalencia en pesos y métodos de pago aceptados.","intro":"El costo oficial de ETIAS es <strong>€7 euros</strong> (aprox. $7.000 ARS). Se paga con tarjeta de débito o crédito internacional.","faq_extra":[("¿Puedo pagar ETIAS con tarjeta argentina?","Sí, se aceptan tarjetas Visa y Mastercard emitidas en Argentina. Verifica que tu banco permita transacciones internacionales en euros."),("¿Menores de 18 años pagan ETIAS?","No. Los menores de 18 años están exentos del pago de €7, aunque igualmente deben obtener la autorización ETIAS.")]},
    {"slug":"etias-argentina-como-solicitar","titulo":"Cómo Solicitar ETIAS desde Argentina 2026 | Guía Paso a Paso","h1":"Cómo Solicitar ETIAS si Eres Argentino","descripcion":"Guía paso a paso para solicitar ETIAS con pasaporte de Argentina. Proceso online, documentos necesarios y tiempos de respuesta.","intro":"Solicitar ETIAS desde Argentina es un proceso completamente online que toma menos de 20 minutos. Aquí te explicamos cada paso.","faq_extra":[("¿Puedo solicitar ETIAS desde el celular?","Sí, la solicitud ETIAS puede completarse desde cualquier dispositivo con conexión a internet, incluidos smartphones.")]},
    {"slug":"etias-argentina-tiempo-respuesta","titulo":"¿Cuánto Tarda ETIAS para Argentinos? Tiempo de Respuesta 2026","h1":"Tiempo de Respuesta ETIAS para Ciudadanos de Argentina","descripcion":"ETIAS responde en minutos para la mayoría de los argentinos. Conoce los tiempos exactos y qué hacer si hay demoras.","intro":"La mayoría de las solicitudes ETIAS de ciudadanos argentinos se aprueban en <strong>minutos</strong>. En casos que requieren revisión manual, el plazo puede extenderse hasta 96 horas.","faq_extra":[("¿Qué hago si ETIAS tarda más de 96 horas?","Puedes contactar a las autoridades ETIAS o a la embajada del país europeo que visitarás. Se recomienda no comprar vuelos hasta tener la aprobación.")]},
    {"slug":"etias-argentina-vigencia","titulo":"¿Cuánto Dura ETIAS para Argentinos? Vigencia y Renovación 2026","h1":"Vigencia de ETIAS para Pasaporte Argentino","descripcion":"ETIAS para argentinos tiene vigencia de 3 años o hasta que venza el pasaporte. Todo sobre renovación y múltiples entradas.","intro":"Tu ETIAS tendrá validez de <strong>3 años</strong> o hasta la fecha de vencimiento de tu pasaporte argentino, lo que ocurra primero. Permite múltiples entradas al espacio Schengen.","faq_extra":[("¿Puedo entrar a Europa varias veces con el mismo ETIAS?","Sí. ETIAS permite múltiples entradas al espacio Schengen durante su vigencia, respetando el límite de 90 días cada 180 días."),("¿Qué pasa si renuevo mi pasaporte argentino?","Si obtienes un pasaporte nuevo, deberás solicitar un ETIAS nuevo ya que está vinculado al número de pasaporte.")]},
    {"slug":"etias-argentina-paises-cubiertos","titulo":"¿A Qué Países de Europa Puedo Entrar con ETIAS? Guía Argentina","h1":"Países Cubiertos por ETIAS para Argentinos","descripcion":"Lista completa de los 30 países del espacio Schengen a los que puedes entrar con ETIAS teniendo pasaporte argentino.","intro":"Con tu ETIAS puedes entrar a los <strong>30 países del espacio Schengen</strong> sin visa adicional.","faq_extra":[("¿ETIAS sirve para Reino Unido?","No. El Reino Unido no forma parte del espacio Schengen y tiene su propio sistema ETA. Necesitarás ETA UK por separado."),("¿Puedo ir a España con ETIAS?","Sí. España es parte del espacio Schengen y está cubierta por ETIAS.")]},
    {"slug":"etias-argentina-vs-visa","titulo":"ETIAS vs Visa Schengen para Argentinos: ¿Cuál Necesito?","h1":"ETIAS vs Visa Schengen: Guía para Ciudadanos Argentinos","descripcion":"¿Necesitas visa o ETIAS para ir a Europa con pasaporte argentino? Comparativa clara para 2026.","intro":"Argentina tiene acuerdo de exención de visa con el espacio Schengen. A partir de Q4 2026, los argentinos necesitarán ETIAS en lugar de visa.","faq_extra":[("¿ETIAS reemplaza la visa Schengen?","No exactamente. Los argentinos nunca necesitaron visa para turismo en Europa. ETIAS es un nuevo requisito adicional para países con exención de visa."),("¿Qué es más fácil, visa o ETIAS?","ETIAS es significativamente más simple: online, €7 y aprobación en minutos. Las visas requieren cita, entrevista y documentación extensa.")]},
    {"slug":"etias-argentina-rechazo","titulo":"¿Me Pueden Rechazar ETIAS si Soy Argentino? Causas y Soluciones","h1":"Causas de Rechazo de ETIAS para Pasaporte Argentino","descripcion":"Conoce las causas de rechazo de ETIAS para ciudadanos de Argentina y qué hacer si tu solicitud es denegada.","intro":"Aunque la mayoría de los argentinos obtienen ETIAS sin problemas, existen causas que pueden derivar en rechazo.","faq_extra":[("¿Puedo apelar un rechazo de ETIAS?","Sí. Si tu ETIAS es rechazado, tienes derecho a apelar ante las autoridades del país Schengen de destino principal."),("¿Un arresto previo en Argentina afecta mi ETIAS?","Depende de la naturaleza del delito y si fue reportado internacionalmente. Consulta con un especialista si tienes antecedentes.")]},
    {"slug":"etias-argentina-turismo","titulo":"ETIAS para Turismo en Europa con Pasaporte Argentino 2026","h1":"ETIAS para Turistas Argentinos en Europa","descripcion":"¿Planeas viajar a Europa como turista con pasaporte argentino? Todo sobre ETIAS para turismo en 2026.","intro":"Si eres argentino y planeas visitar Europa como turista después de Q4 2026, necesitarás ETIAS. El proceso es simple y completamente online.","faq_extra":[("¿Cuántos días puedo estar en Europa como turista con ETIAS?","Con ETIAS puedes permanecer hasta 90 días dentro de un período de 180 días en el espacio Schengen.")]},
    {"slug":"etias-argentina-negocios","titulo":"ETIAS para Viajes de Negocios desde Argentina a Europa 2026","h1":"ETIAS para Viajeros de Negocios Argentinos","descripcion":"¿Viajas a Europa por negocios con pasaporte argentino? ETIAS cubre visitas de negocios de corta duración.","intro":"Los viajes de negocios de corta duración (hasta 90 días) a Europa con pasaporte argentino están cubiertos por ETIAS.","faq_extra":[("¿Puedo firmar contratos o asistir a reuniones con ETIAS?","Sí. ETIAS cubre reuniones, conferencias, negociaciones y ferias comerciales, siempre que no impliquen empleo remunerado local."),("¿Necesito carta de invitación para ETIAS de negocios?","No es obligatorio, pero tener una carta de tu contraparte europea puede facilitar el proceso en caso de revisión manual.")]},
    {"slug":"etias-argentina-estudios","titulo":"ETIAS para Estudiantes Argentinos en Europa 2026","h1":"ETIAS para Estudiantes con Pasaporte Argentino","descripcion":"¿Eres estudiante argentino y planeas ir a Europa? Conoce si ETIAS cubre cursos cortos y programas de intercambio.","intro":"ETIAS cubre estancias de <strong>hasta 90 días</strong>, lo que lo hace válido para cursos cortos, conferencias académicas o visitas de exploración universitaria.","faq_extra":[("¿ETIAS sirve para un semestre de intercambio?","No. Un semestre supera el límite de 90 días de ETIAS. Para estudios largos necesitarás visa de estudiante del país correspondiente."),("¿Puedo ir a una entrevista de admisión universitaria con ETIAS?","Sí. Las entrevistas, visitas a campus y cursos intensivos cortos están cubiertos por ETIAS.")]},
    {"slug":"etias-argentina-menores","titulo":"ETIAS para Menores Argentinos: Guía para Familias 2026","h1":"ETIAS para Menores de Edad con Pasaporte Argentino","descripcion":"¿Viajas a Europa con tus hijos argentinos? Guía completa sobre ETIAS para menores de edad en 2026.","intro":"Los menores de edad con pasaporte argentino también necesitan ETIAS para viajar a Europa, pero están exentos del pago de €7.","faq_extra":[("¿Un menor puede viajar a Europa solo con ETIAS?","ETIAS es solo la autorización de viaje. Los menores que viajan sin ambos padres también necesitan carta de autorización de los tutores legales."),("¿El ETIAS de mi hijo está vinculado al mío?","No. Cada viajero, incluidos los menores, debe tener su propio ETIAS vinculado a su propio pasaporte.")]},
    {"slug":"etias-argentina-adultos-mayores","titulo":"ETIAS para Adultos Mayores Argentinos: Todo lo que Necesitas Saber","h1":"ETIAS para Adultos Mayores con Pasaporte Argentino","descripcion":"Guía simplificada de ETIAS para argentinos mayores de 70 años. Exenciones, proceso y recomendaciones.","intro":"Los adultos mayores de 70 años con pasaporte argentino están <strong>exentos del pago</strong> de €7, aunque igualmente deben obtener la autorización ETIAS.","faq_extra":[("¿Los mayores de 70 años tienen algún beneficio adicional?","Además de la exención de pago, el proceso es idéntico al de cualquier otro viajero.")]},
    {"slug":"etias-argentina-buenos-aires","titulo":"ETIAS desde Buenos Aires 2026 | Guía para Viajeros Porteños","h1":"ETIAS para Viajeros de Buenos Aires hacia Europa","descripcion":"Guía ETIAS específica para residentes de Buenos Aires. Aeropuertos, vuelos a Europa y proceso de autorización.","intro":"Buenos Aires es el principal hub de conexión entre Argentina y Europa. Si viajas desde Ezeiza (EZE), necesitarás ETIAS a partir de Q4 2026.","faq_extra":[("¿Desde qué aeropuertos de Buenos Aires salen vuelos directos a Europa?","El Aeropuerto Internacional Ezeiza (EZE) opera vuelos directos a Madrid, Roma, París, Frankfurt y Londres.")]},
    {"slug":"etias-argentina-cordoba","titulo":"ETIAS desde Córdoba Argentina 2026 | Guía para Viajeros","h1":"ETIAS para Viajeros de Córdoba hacia Europa","descripcion":"Todo sobre ETIAS para residentes de Córdoba, Argentina que planean viajar a Europa en 2026.","intro":"Desde Córdoba los viajeros suelen conectar por Buenos Aires (EZE) para volar a Europa. A partir de Q4 2026 todos necesitarán ETIAS antes de embarcar.","faq_extra":[("¿Puedo solicitar ETIAS desde Córdoba?","Sí. ETIAS es un trámite 100% online, puedes solicitarlo desde cualquier ciudad de Argentina.")]},
    {"slug":"etias-argentina-italia","titulo":"ETIAS para Argentinos que Viajan a Italia 2026","h1":"ETIAS Argentina → Italia: Guía Completa","descripcion":"¿Quieres visitar Roma, Milán o Venecia con pasaporte argentino? Todo sobre ETIAS para la ruta Argentina–Italia.","intro":"Italia es uno de los destinos más visitados por los argentinos, con una de las comunidades de descendientes italianos más grandes del mundo. A partir de Q4 2026 se requiere ETIAS.","faq_extra":[("¿Los argentinos con ciudadanía italiana doble necesitan ETIAS?","No. Si tienes pasaporte italiano eres ciudadano de la UE y no necesitas ETIAS. Solo aplica para quienes viajan exclusivamente con pasaporte argentino.")]},
    {"slug":"etias-argentina-espana","titulo":"ETIAS para Argentinos que Viajan a España 2026","h1":"ETIAS Argentina → España: Todo lo que Necesitas Saber","descripcion":"¿Planeas ir a España con pasaporte argentino? Guía completa sobre ETIAS para la ruta Argentina–España en 2026.","intro":"España es el destino europeo más visitado por los argentinos por los lazos culturales e históricos. Con ETIAS, viajar a Madrid o Barcelona solo requiere una autorización previa online.","faq_extra":[("¿Puedo entrar a España directamente desde Argentina con ETIAS?","Sí. Hay vuelos directos desde Buenos Aires a Madrid, y ETIAS es válido para entrada directa.")]},
    {"slug":"etias-argentina-preguntas-frecuentes","titulo":"Preguntas Frecuentes ETIAS para Argentinos 2026 | FAQ Completo","h1":"FAQ: Todo sobre ETIAS para Ciudadanos de Argentina","descripcion":"Respuestas a las preguntas más frecuentes sobre ETIAS para viajeros con pasaporte argentino.","intro":"Recopilamos las preguntas más frecuentes de viajeros argentinos sobre ETIAS. Si tienes dudas, aquí encontrarás respuestas claras y actualizadas.","faq_extra":[("¿ETIAS es lo mismo que el ESTA de USA?","Son conceptos similares: ambos son autorizaciones de viaje electrónicas para países con exención de visa. ETIAS es el sistema europeo equivalente al ESTA americano."),("¿Puedo solicitar ETIAS si tengo doble ciudadanía?","Debes solicitarlo con el pasaporte que usarás para entrar a Europa. Si tienes pasaporte de país UE, no necesitas ETIAS."),("¿ETIAS debe solicitarse con anticipación?","Se recomienda solicitarlo al menos 72 horas antes del viaje, aunque muchas solicitudes se aprueban en minutos."),("¿Existe agencia oficial ETIAS en Argentina?","No. ETIAS es un trámite 100% online ante la Unión Europea. No hay oficinas físicas en Argentina.")]},
]

def generar_html(p):
    faqs_base = [
        ("¿ETIAS es una visa?","No. ETIAS es una <strong>autorización de viaje electrónica</strong>, no una visa. Los ciudadanos argentinos ya están exentos de visa Schengen; ETIAS es un requisito adicional desde Q4 2026."),
        ("¿Cuánto cuesta ETIAS para argentinos?","El costo oficial es <strong>€7 euros</strong> (aprox. $7.000 ARS). Menores de 18 y mayores de 70 años están exentos del pago."),
        ("¿Cuánto tiempo tarda la aprobación?","La mayoría se aprueban en <strong>minutos</strong>. En casos de revisión manual puede tardar hasta 96 horas."),
        ("¿Con qué pasaporte debo solicitar ETIAS?","Debes solicitarlo con el pasaporte argentino que usarás para viajar a Europa. Cada pasaporte requiere su propio ETIAS."),
    ]
    faqs_all = faqs_base + p.get("faq_extra",[])
    faqs_html = "\n".join(f'    <div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q,a in faqs_all)
    pasos = [
        ("1","Completa el formulario online","Ingresa datos personales, número de pasaporte y detalles del viaje en el portal oficial ETIAS."),
        ("2","Paga €7 con tarjeta","Se acepta tarjeta de débito o crédito internacional. Aprox. $7.000 ARS."),
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
<nav class="breadcrumb"><a href="{SIMULADOR_URL}">Inicio</a> › <a href="etias-argentina.html">ETIAS Argentina</a> › {p['h1']}</nav>
<div class="alert"><strong>⚠️ Importante:</strong> ETIAS será obligatorio para ciudadanos de Argentina a partir de <strong>Q4 2026</strong>.</div>
<p>{p['intro']}</p>
<h2>Requisitos para Ciudadanos de Argentina</h2>
<ul class="req-list">
<li>Pasaporte argentino válido (más de 3 meses de vigencia)</li>
<li>Correo electrónico activo</li>
<li>Tarjeta de débito/crédito internacional para el pago de €7</li>
<li>Acceso a internet (solicitud 100% online)</li>
<li>Máximo 90 días de estancia por cada 180 días</li>
</ul>
<h2>Proceso de Solicitud ETIAS</h2>
{pasos_html}
<div class="cta-box"><p>¿Quieres saber si cumples los requisitos para obtener ETIAS con tu pasaporte argentino?</p><a class="cta-btn" href="{SIMULADOR_URL}">🛂 Probar Simulador ETIAS Gratis</a></div>
<h2>Países del Espacio Schengen Cubiertos por ETIAS</h2>
<div class="countries">{paises_html}</div>
<h2>Preguntas Frecuentes sobre ETIAS para Argentinos</h2>
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
