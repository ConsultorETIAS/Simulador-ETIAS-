import os

OUTPUT_DIR = "."
os.makedirs(OUTPUT_DIR, exist_ok=True)

SIMULADOR_URL = "https://consultoretias.github.io/Simulador-ETIAS-/"

PAGINAS = [
    {
        "slug": "etias-medicos-mexicanos",
        "titulo": "ETIAS para médicos latinoamericanos: viajes de congreso y trabajo",
        "h1": "ETIAS para Médicos: Congresos y Viajes Profesionales a Europa",
        "descripcion": "Guía ETIAS para médicos latinoamericanos que viajan a Europa para congresos, formación o colaboraciones clínicas en 2026.",
        "intro": "Los médicos latinoamericanos viajan frecuentemente a Europa para <strong>congresos, residencias de especialización y colaboraciones clínicas</strong>. Con ETIAS, estos viajes de hasta 90 días no requieren visa.",
        "perfil": "Médicos, especialistas, residentes",
        "faq_extra": [
            ("¿ETIAS cubre asistir a un congreso médico en Europa?", "Sí. La asistencia a congresos, simposios y eventos académicos está cubierta por ETIAS para estancias de hasta 90 días."),
            ("¿Puedo hacer rotaciones clínicas en Europa con ETIAS?", "Depende. Rotaciones sin remuneración ni contrato local de corta duración pueden estar cubiertas. Con contrato europeo necesitarás visa de trabajo."),
            ("¿Qué documentos llevar además de ETIAS a un congreso médico?", "Invitación del congreso, credencial médica, seguro de salud internacional y comprobante de hospedaje."),
        ]
    },
    {
        "slug": "etias-enfermeras-europa",
        "titulo": "ETIAS para enfermeras latinoamericanas que viajan a Europa",
        "h1": "ETIAS para Enfermeras: Viajes Profesionales y Formativos a Europa",
        "descripcion": "Todo sobre ETIAS para enfermeras latinoamericanas: congresos de enfermería, intercambios y estancias formativas en Europa 2026.",
        "intro": "Las enfermeras latinoamericanas que viajan a Europa para <strong>formación, congresos o intercambios profesionales</strong> de corta duración necesitarán ETIAS a partir de Q4 2026.",
        "perfil": "Enfermeras, técnicos en enfermería, parteras",
        "faq_extra": [
            ("¿ETIAS permite trabajar como enfermera en Europa?", "No. ETIAS cubre visitas de hasta 90 días sin empleo remunerado. Para trabajar como enfermera en Europa necesitas visa de trabajo y convalidación de título."),
            ("¿Hay demanda de enfermeras latinoamericanas en Europa?", "Sí, varios países europeos tienen déficit de enfermeras. Pero ese proceso requiere visa de trabajo, no ETIAS."),
        ]
    },
    {
        "slug": "etias-ingenieros-negocios",
        "titulo": "ETIAS para ingenieros latinoamericanos en viajes de negocios a Europa",
        "h1": "ETIAS para Ingenieros: Viajes de Negocios y Proyectos en Europa",
        "descripcion": "Guía ETIAS para ingenieros latinoamericanos que viajan a Europa por proyectos, ferias tecnológicas o negociaciones comerciales.",
        "intro": "Los ingenieros latinoamericanos viajan a Europa para <strong>visitar clientes, asistir a ferias tecnológicas y coordinar proyectos</strong>. ETIAS cubre todas estas actividades de negocios de corta duración.",
        "perfil": "Ingenieros civiles, industriales, de software, mecánicos",
        "faq_extra": [
            ("¿Puedo hacer auditorías técnicas en Europa con ETIAS?", "Sí. Las visitas técnicas, auditorías, supervisión de proyectos y reuniones con clientes están cubiertas por ETIAS."),
            ("¿ETIAS cubre asistir a Hannover Messe u otras ferias industriales?", "Sí. Las ferias industriales y tecnológicas europeas son actividades de negocios cubiertas por ETIAS."),
            ("¿Puedo cobrar honorarios por consultoría durante mi estancia con ETIAS?", "No. Recibir pago de una empresa europea requiere visa de trabajo. ETIAS no permite empleo remunerado local."),
        ]
    },
    {
        "slug": "etias-periodistas-prensa",
        "titulo": "ETIAS para periodistas y medios de comunicación latinoamericanos",
        "h1": "ETIAS para Periodistas: Cobertura y Viajes de Prensa a Europa",
        "descripcion": "Guía especial ETIAS para periodistas y comunicadores latinoamericanos que cubren eventos en Europa en 2026.",
        "intro": "Los periodistas latinoamericanos que viajan a Europa para <strong>cobertura de eventos, reportajes o corresponsalías temporales</strong> de hasta 90 días necesitan ETIAS a partir de Q4 2026.",
        "perfil": "Periodistas, fotógrafos de prensa, comunicadores, bloggers",
        "faq_extra": [
            ("¿ETIAS cubre trabajar como corresponsal temporal en Europa?", "Para coberturas puntuales de hasta 90 días, generalmente sí. Para corresponsalías permanentes o contratos con medios europeos, se requiere visa de trabajo."),
            ("¿Necesito acreditación de prensa además de ETIAS?", "ETIAS es el requisito de entrada. Las acreditaciones de prensa las gestiona cada evento o institución de forma independiente."),
            ("¿Los influencers de viajes necesitan ETIAS?", "Sí. Los creadores de contenido que viajan a Europa para crear contenido necesitan ETIAS como cualquier turista."),
        ]
    },
    {
        "slug": "etias-deportistas-competencia",
        "titulo": "ETIAS para deportistas latinoamericanos en competencias europeas",
        "h1": "ETIAS para Deportistas: Competencias y Eventos en Europa",
        "descripcion": "Guía ETIAS para deportistas latinoamericanos que compiten en torneos, ligas o eventos deportivos en Europa 2026.",
        "intro": "Los deportistas latinoamericanos que viajan a Europa para <strong>competir en torneos, ligas amateur o eventos internacionales</strong> de corta duración necesitarán ETIAS.",
        "perfil": "Deportistas amateur y semiprofesionales, entrenadores, árbitros",
        "faq_extra": [
            ("¿Un deportista profesional con contrato europeo necesita ETIAS?", "No. Los deportistas con contrato de trabajo en Europa necesitan visa de trabajo, no ETIAS."),
            ("¿ETIAS cubre a entrenadores que acompañan delegaciones?", "Sí. Los entrenadores, técnicos y cuerpo médico que acompañan equipos en competencias están cubiertos por ETIAS."),
            ("¿Puedo recibir premios en metálico de un torneo con ETIAS?", "Los premios de competencias deportivas generalmente no se consideran empleo remunerado, pero consulta el caso específico con un especialista."),
        ]
    },
    {
        "slug": "etias-artistas-gira",
        "titulo": "ETIAS para artistas y músicos latinoamericanos en gira por Europa",
        "h1": "ETIAS para Artistas y Músicos: Giras y Actuaciones en Europa",
        "descripcion": "Guía ETIAS para artistas, músicos y performers latinoamericanos que realizan giras o presentaciones en Europa en 2026.",
        "intro": "Los artistas y músicos latinoamericanos que realizan <strong>giras, presentaciones o colaboraciones en Europa</strong> deben entender qué cubre ETIAS y cuándo necesitan visa de artista.",
        "perfil": "Músicos, artistas visuales, performers, actores, bailarines",
        "faq_extra": [
            ("¿Puedo cobrar por actuaciones en Europa con ETIAS?", "Actuaciones remuneradas en Europa generalmente requieren visa de artista o permiso de trabajo, no solo ETIAS. Consulta con un especialista según el país."),
            ("¿ETIAS cubre participar en festivales de música como artista?", "Depende de si hay remuneración y del país. Festivales gratuitos o colaboraciones sin contrato pueden estar cubiertos. Con contrato y pago, necesitas visa."),
            ("¿Un DJ puede tocar en Europa con ETIAS?", "Similar al caso anterior: actuaciones ocasionales sin contrato fijo pueden ser posibles, pero actuaciones remuneradas regulares requieren documentación adicional."),
        ]
    },
    {
        "slug": "etias-estudiantes-intercambio",
        "titulo": "ETIAS para estudiantes latinoamericanos en intercambio universitario",
        "h1": "ETIAS para Estudiantes de Intercambio en Europa",
        "descripcion": "Todo sobre ETIAS para estudiantes latinoamericanos en programas de intercambio universitario en Europa 2026.",
        "intro": "Los estudiantes latinoamericanos en <strong>intercambios universitarios</strong> deben entender cuándo ETIAS es suficiente y cuándo necesitan visa de estudiante según la duración del programa.",
        "perfil": "Estudiantes universitarios, posgrado, Erasmus+",
        "faq_extra": [
            ("¿ETIAS es suficiente para un intercambio de un semestre?", "No. Un semestre universitario supera los 90 días que cubre ETIAS. Para semestres completos necesitas visa de estudiante del país correspondiente."),
            ("¿ETIAS cubre una estancia de investigación de 2 meses?", "Sí. Una estancia de investigación o visita académica de hasta 90 días está cubierta por ETIAS."),
            ("¿Los programas Erasmus+ requieren ETIAS?", "Los estudiantes no europeos en Erasmus+ de larga duración necesitan visa de estudiante. Para visitas cortas de exploración, ETIAS es suficiente."),
            ("¿Puedo hacer una visita previa a la universidad con ETIAS?", "Sí. Visitar el campus, asistir a orientaciones o entrevistas de admisión están perfectamente cubiertos por ETIAS."),
        ]
    },
    {
        "slug": "etias-investigadores-academicos",
        "titulo": "ETIAS para investigadores y académicos latinoamericanos",
        "h1": "ETIAS para Investigadores y Académicos en Europa",
        "descripcion": "Guía ETIAS para investigadores, profesores y académicos latinoamericanos que viajan a Europa para conferencias, estancias o colaboraciones.",
        "intro": "Los investigadores y académicos latinoamericanos que viajan a Europa para <strong>conferencias, estancias cortas o colaboraciones de investigación</strong> de hasta 90 días pueden hacerlo con ETIAS.",
        "perfil": "Investigadores UNAM, Tec, CONICET, universidades públicas y privadas",
        "faq_extra": [
            ("¿ETIAS cubre presentar ponencias en congresos académicos?", "Sí. La participación en congresos, simposios y conferencias académicas está cubierta por ETIAS."),
            ("¿Puedo hacer investigación en laboratorios europeos con ETIAS?", "Para estancias cortas de colaboración sin contrato europeo, generalmente sí. Para proyectos con financiamiento europeo y contrato, necesitas visa de investigador."),
            ("¿Hay alguna visa específica para investigadores europeos?", "Sí. La UE tiene visa de investigador (Directiva 2016/801) para estancias largas. Para visitas cortas, ETIAS es suficiente."),
        ]
    },
    {
        "slug": "etias-empresarios-pymes",
        "titulo": "ETIAS para empresarios PyME latinoamericanos: viajes comerciales a Europa",
        "h1": "ETIAS para Empresarios PyME: Viajes Comerciales a Europa",
        "descripcion": "Guía ETIAS para dueños de PyMEs latinoamericanas que viajan a Europa para negocios, ferias comerciales y reuniones con socios.",
        "intro": "Los empresarios PyME latinoamericanos que viajan a Europa para <strong>explorar mercados, asistir a ferias y reunirse con distribuidores</strong> encontrarán en ETIAS el acceso más simple al mercado europeo.",
        "perfil": "Dueños de PyME, directores comerciales, emprendedores",
        "faq_extra": [
            ("¿Puedo firmar contratos comerciales en Europa con ETIAS?", "Sí. Negociar y firmar contratos comerciales son actividades de negocios cubiertas por ETIAS, siempre que no impliquen empleo directo en Europa."),
            ("¿ETIAS cubre asistir a ferias como Fruit Logistica, FITUR o similares?", "Sí. Las ferias comerciales europeas, ya sea como visitante o expositor, están cubiertas por ETIAS."),
            ("¿Puedo abrir una sucursal europea con ETIAS?", "La exploración y gestión inicial sí. Pero para residir y gestionar operaciones de forma continua necesitarás visa de larga duración o residencia empresarial."),
        ]
    },
    {
        "slug": "etias-transportistas-logistica",
        "titulo": "ETIAS para trabajadores de logística y transporte latinoamericanos",
        "h1": "ETIAS para Logística y Transporte: Viajes Profesionales a Europa",
        "descripcion": "Guía ETIAS para profesionales de logística, transporte y nearshoring latinoamericanos que viajan a Europa por negocios.",
        "intro": "El crecimiento del <strong>nearshoring en Latinoamérica</strong> ha aumentado los viajes de profesionales de logística y transporte a Europa para coordinar operaciones. ETIAS facilita estos desplazamientos.",
        "perfil": "Gerentes de logística, coordinadores de supply chain, operadores de transporte",
        "faq_extra": [
            ("¿Un camionero latinoamericano puede transitar Europa con ETIAS?", "ETIAS es para ciudadanos que viajan como turistas o por negocios, no para conductores comerciales en tránsito. Los conductores profesionales tienen regulación específica."),
            ("¿ETIAS cubre visitar almacenes y centros de distribución europeos?", "Sí. Las visitas técnicas a instalaciones logísticas, reuniones de coordinación y auditorías de proveedores están cubiertas."),
        ]
    },
    {
        "slug": "etias-chefs-gastronomia",
        "titulo": "ETIAS para chefs latinoamericanos: concursos y residencias en Europa",
        "h1": "ETIAS para Chefs y Gastronomía: Europa desde Latinoamérica",
        "descripcion": "Guía ETIAS para chefs y profesionales de gastronomía latinoamericanos que viajan a Europa para concursos, formación o colaboraciones culinarias.",
        "intro": "La gastronomía latinoamericana tiene presencia creciente en Europa. Los chefs que viajan para <strong>concursos, stages, masterclasses o colaboraciones pop-up</strong> de corta duración pueden hacerlo con ETIAS.",
        "perfil": "Chefs, cocineros, sommeliers, pasteleros",
        "faq_extra": [
            ("¿Puedo hacer un stage en un restaurante europeo con ETIAS?", "Un stage no remunerado y de corta duración puede estar cubierto por ETIAS. Un stage con contrato o remuneración requiere visa de trabajo."),
            ("¿ETIAS cubre participar en competencias gastronómicas como el Bocuse d'Or?", "Sí. La participación en competencias culinarias internacionales está cubierta por ETIAS."),
            ("¿Puedo dar clases de cocina mexicana en Europa con ETIAS?", "Clases ocasionales y masterclasses sin contrato fijo pueden estar cubiertas. Para actividad docente regular remunerada necesitas visa."),
        ]
    },
    {
        "slug": "etias-arquitectos-disenadores",
        "titulo": "ETIAS para arquitectos y diseñadores latinoamericanos en Europa",
        "h1": "ETIAS para Arquitectos y Diseñadores: Europa como Destino Profesional",
        "descripcion": "Guía ETIAS para arquitectos, diseñadores gráficos e industriales latinoamericanos que viajan a Europa por proyectos y eventos profesionales.",
        "intro": "Los arquitectos y diseñadores latinoamericanos viajan a Europa para <strong>visitar obras de referencia, participar en bienales y reunirse con clientes internacionales</strong>. ETIAS hace esto más accesible.",
        "perfil": "Arquitectos, diseñadores industriales, gráficos, de interiores",
        "faq_extra": [
            ("¿ETIAS cubre asistir a la Bienal de Venecia o Milan Design Week?", "Sí. La asistencia como visitante o participante en eventos de diseño y arquitectura está cubierta por ETIAS."),
            ("¿Puedo supervisar obra en Europa con ETIAS?", "Visitas puntuales de supervisión pueden estar cubiertas. Dirección de obra continua con contrato europeo requiere visa de trabajo."),
            ("¿Puedo cobrar honorarios por diseño realizado remotamente desde Europa?", "Si el trabajo fue generado para un cliente no europeo y el pago viene de fuera de Europa, generalmente no es considerado empleo local. Consulta con un especialista."),
        ]
    },
    {
        "slug": "etias-abogados-notarios",
        "titulo": "ETIAS para abogados latinoamericanos: congresos y arbitrajes en Europa",
        "h1": "ETIAS para Abogados y Notarios: Viajes Profesionales a Europa",
        "descripcion": "Guía ETIAS para abogados y notarios latinoamericanos que viajan a Europa para arbitrajes internacionales, congresos jurídicos y asesoría a clientes.",
        "intro": "Los abogados latinoamericanos con práctica internacional viajan frecuentemente a Europa para <strong>arbitrajes, litigios internacionales, congresos jurídicos y asesoría a clientes</strong>. ETIAS simplifica estos viajes.",
        "perfil": "Abogados corporativos, árbitros internacionales, notarios",
        "faq_extra": [
            ("¿Puedo representar a un cliente en arbitraje europeo con ETIAS?", "Sí. La participación en arbitrajes internacionales como abogado representante está cubierta por ETIAS para estancias de hasta 90 días."),
            ("¿ETIAS cubre asistir a la Corte Internacional de Arbitraje (ICC)?", "Sí. Asistir como parte, árbitro o abogado en procedimientos de la ICC o tribunales similares está cubierto por ETIAS."),
            ("¿Puedo ejercer como abogado en Europa con ETIAS?", "No. El ejercicio profesional continuo del derecho en Europa requiere habilitación local y visa de trabajo o residencia."),
        ]
    },
    {
        "slug": "etias-pilotos-tripulacion",
        "titulo": "ETIAS para pilotos y tripulación aérea latinoamericana",
        "h1": "ETIAS para Pilotos y Tripulación Aérea: Situación Especial",
        "descripcion": "Guía sobre ETIAS para pilotos y tripulación de cabina latinoamericana que operan rutas o hacen escala en Europa.",
        "intro": "La situación de pilotos y tripulación aérea respecto a ETIAS es <strong>técnicamente especial</strong>. La tripulación en servicio activo tiene regulación diferente a los viajeros regulares.",
        "perfil": "Pilotos comerciales, sobrecargos, tripulación de cabina",
        "faq_extra": [
            ("¿Los pilotos en servicio necesitan ETIAS?", "La tripulación en servicio activo generalmente está exenta bajo regulaciones de aviación internacional (OACI/Eurocontrol). Consulta con tu aerolínea."),
            ("¿Qué pasa si un piloto viaja a Europa como pasajero?", "En ese caso viaja como turista o por negocios personales y sí necesita ETIAS como cualquier ciudadano latinoamericano."),
            ("¿Las escalas técnicas en Europa requieren ETIAS?", "Las escalas en zona de tránsito internacional sin pasar por control migratorio generalmente no requieren ETIAS. Si sales del área de tránsito, sí."),
        ]
    },
    {
        "slug": "etias-influencers-creadores",
        "titulo": "ETIAS para influencers y creadores de contenido latinoamericanos en Europa",
        "h1": "ETIAS para Influencers y Creadores de Contenido en Europa",
        "descripcion": "Todo sobre ETIAS para influencers, youtubers, tiktokers y creadores de contenido latinoamericanos que viajan a Europa en 2026.",
        "intro": "Los creadores de contenido latinoamericanos que viajan a Europa para <strong>crear contenido, asistir a eventos de marca y colaborar con otros creadores</strong> necesitan ETIAS a partir de Q4 2026.",
        "perfil": "Influencers, youtubers, tiktokers, podcasters, bloggers de viaje",
        "faq_extra": [
            ("¿Puedo crear contenido patrocinado en Europa con ETIAS?", "Crear contenido para tus propios canales durante el viaje está cubierto. Contratos de trabajo directo con empresas europeas pueden requerir visa."),
            ("¿Las marcas europeas pueden patrocinar mi viaje con ETIAS?", "Recibir productos o viajes patrocinados generalmente no se considera empleo local. El pago directo en efectivo de empresa europea puede ser zona gris. Consulta."),
            ("¿ETIAS cubre asistir a eventos como el VidCon Europe o similares?", "Sí. La asistencia a eventos de creators como visitante, panelista o creador invitado está cubierta por ETIAS."),
        ]
    },
    {
        "slug": "etias-freelancers-nomadas",
        "titulo": "ETIAS para freelancers y nómadas digitales latinoamericanos",
        "h1": "ETIAS para Freelancers y Nómadas Digitales en Europa",
        "descripcion": "Guía completa sobre ETIAS para freelancers y nómadas digitales latinoamericanos que trabajan remotamente desde Europa.",
        "intro": "Los nómadas digitales latinoamericanos que trabajan remotamente para <strong>clientes fuera de Europa</strong> mientras viajan por el continente tienen una situación particular con ETIAS que vale la pena entender bien.",
        "perfil": "Desarrolladores, diseñadores, consultores, copywriters freelance",
        "faq_extra": [
            ("¿Puedo trabajar remotamente desde Europa con ETIAS?", "ETIAS permite estancias de hasta 90 días. Trabajar remotamente para clientes no europeos desde Europa es una zona gris legal que varía por país. Algunos países ya tienen visa de nómada digital."),
            ("¿Qué países europeos tienen visa de nómada digital?", "Portugal, España, Alemania, Grecia, Croacia y otros ya tienen visas específicas para nómadas digitales. Para estancias largas, estas son mejor opción que ETIAS."),
            ("¿ETIAS es suficiente para 3 meses de trabajo remoto en Europa?", "Técnicamente la entrada es legal con ETIAS. Pero el trabajo remoto prolongado puede generar obligaciones fiscales. Para estadías largas, considera la visa de nómada del país de destino."),
            ("¿Puedo hacer 'visa runs' con ETIAS para quedarme más tiempo?", "No se recomienda. Las salidas y entradas frecuentes para resetear los 90 días pueden ser interpretadas como evasión migratoria y resultar en prohibición de entrada."),
        ]
    },
]


def generar_html(p):
    faqs_base = [
        ("¿ETIAS es una visa?", "No. ETIAS es una <strong>autorización de viaje electrónica</strong>, no una visa. Es un requisito adicional para ciudadanos latinoamericanos con exención de visa Schengen, obligatorio desde Q4 2026."),
        ("¿Cuánto cuesta ETIAS?", "El costo oficial es <strong>€7 euros</strong>. Menores de 18 y mayores de 70 años están exentos del pago."),
        ("¿Cuántos días permite ETIAS en Europa?", "Hasta <strong>90 días por cada período de 180 días</strong> en el espacio Schengen. Para estancias más largas o empleo, se requiere visa específica."),
        ("¿ETIAS permite trabajar en Europa?", "No. ETIAS es para turismo, negocios y visitas de corta duración. Para trabajar de forma remunerada para empleadores europeos necesitas visa de trabajo."),
    ]
    faqs_all = faqs_base + p.get("faq_extra", [])
    faqs_html = "\n".join(
        f'    <div class="faq-item"><h3>{q}</h3><p>{a}</p></div>'
        for q, a in faqs_all
    )
    pasos = [
        ("1", "Verifica qué cubre ETIAS para tu perfil", "Usa el simulador para confirmar que tus actividades en Europa están dentro del alcance de ETIAS."),
        ("2", "Prepara documentación profesional", "Invitación del evento, credencial profesional, itinerario detallado y seguro de viaje."),
        ("3", "Solicita ETIAS con anticipación", "Se recomienda al menos 72 horas antes. El proceso es completamente online."),
        ("4", "Guarda tu autorización", "Descarga o imprime tu ETIAS aprobado. Las aerolíneas lo verifican en el check-in."),
    ]
    pasos_html = "\n".join(
        f'    <div class="step"><span class="step-number">{n}</span><div><strong>{t}</strong><p>{d}</p></div></div>'
        for n, t, d in pasos
    )
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
header h1{{font-size:1.9rem;margin-bottom:.5rem}}
.badge{{display:inline-block;background:#0a7c5c;color:white;padding:.25rem .75rem;border-radius:20px;font-size:.85rem;margin-top:.5rem}}
.perfil-badge{{display:inline-block;background:rgba(255,255,255,.15);color:white;padding:.2rem .65rem;border-radius:20px;font-size:.8rem;margin-top:.4rem}}
.container{{max-width:800px;margin:0 auto;padding:2rem 1rem}}
.alert{{background:#e8f5e9;border-left:4px solid #0a7c5c;padding:1rem 1.25rem;border-radius:4px;margin-bottom:2rem}}
h2{{font-size:1.4rem;color:#1a1a2e;margin:2rem 0 1rem;border-bottom:2px solid #0a7c5c;padding-bottom:.4rem}}
.step{{display:flex;gap:1rem;margin-bottom:1.5rem;align-items:flex-start}}
.step-number{{background:#0a7c5c;color:white;width:2rem;height:2rem;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:bold;flex-shrink:0}}
.cta-box{{background:#1a1a2e;color:white;padding:2rem;border-radius:8px;text-align:center;margin:2rem 0}}
.cta-box p{{margin-bottom:1rem;opacity:.9}}
.cta-btn{{display:inline-block;background:#0a7c5c;color:white;padding:.9rem 2rem;border-radius:6px;text-decoration:none;font-weight:bold;font-size:1.05rem}}
.faq-item{{background:white;border-radius:6px;padding:1.25rem;margin-bottom:1rem;box-shadow:0 1px 3px rgba(0,0,0,.07)}}
.faq-item h3{{font-size:1rem;color:#1a1a2e;margin-bottom:.5rem}}
footer{{text-align:center;padding:2rem 1rem;font-size:.8rem;color:#999;border-top:1px solid #e0e0e0;margin-top:2rem}}
nav.breadcrumb{{font-size:.85rem;color:#888;margin-bottom:1.5rem}}
nav.breadcrumb a{{color:#0a7c5c;text-decoration:none}}
</style>
</head>
<body>
<header>
<h1>{p['h1']}</h1>
<div class="badge">✈️ Guía Profesional ETIAS 2026</div>
<div class="perfil-badge">👤 Para: {p['perfil']}</div>
<p style="margin-top:.75rem;opacity:.85;font-size:.95rem">Actualizado: marzo 2026</p>
</header>
<div class="container">
<nav class="breadcrumb"><a href="{SIMULADOR_URL}">Inicio</a> › <a href="etias-ingenieros-negocios.html">ETIAS Profesional</a> › {p['h1']}</nav>
<div class="alert"><strong>✅ Buenas noticias:</strong> La mayoría de actividades profesionales de corta duración están cubiertas por ETIAS. Esta guía te explica exactamente qué aplica a tu perfil.</div>
<p style="margin-bottom:1.5rem">{p['intro']}</p>

<h2>Pasos para Profesionales</h2>
{pasos_html}

<div class="cta-box">
  <p>¿Quieres confirmar que tus actividades en Europa están cubiertas por ETIAS? Usa el simulador gratuito.</p>
  <a class="cta-btn" href="{SIMULADOR_URL}">🛂 Simular mi caso profesional</a>
</div>

<h2>Preguntas Frecuentes para {p['perfil']}</h2>
{faqs_html}

<div class="cta-box" style="margin-top:2rem">
  <p>Simula tu solicitud ETIAS y recibe tu declaración en PDF — completamente gratis.</p>
  <a class="cta-btn" href="{SIMULADOR_URL}">🚀 Simular ETIAS Ahora</a>
</div>
</div>
<footer>ETIAS Consultant Simulator | No afiliado a la Unión Europea | Información con fines educativos | <a href="{SIMULADOR_URL}" style="color:#0a7c5c">Volver al Simulador</a></footer>
</body>
</html>"""


for p in PAGINAS:
    path = os.path.join(OUTPUT_DIR, f"{p['slug']}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(generar_html(p))
    print(f"OK {path}")

print(f"\nListo: {len(PAGINAS)} páginas Cluster B generadas")
