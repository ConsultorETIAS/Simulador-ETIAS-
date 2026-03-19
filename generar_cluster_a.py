import os

OUTPUT_DIR = "."
os.makedirs(OUTPUT_DIR, exist_ok=True)

SIMULADOR_URL = "https://consultoretias.github.io/Simulador-ETIAS-/"

PAGINAS = [
    {
        "slug": "etias-rechazo-solicitud",
        "titulo": "ETIAS: ¿Qué pasa si me rechazan? Guía completa 2026",
        "h1": "¿Qué pasa si me rechazan el ETIAS?",
        "descripcion": "Guía completa sobre el rechazo de ETIAS: causas, derechos, plazos de apelación y soluciones para viajeros latinoamericanos en 2026.",
        "intro": "Recibir un rechazo de ETIAS puede ser angustiante, pero <strong>no significa el fin de tu viaje a Europa</strong>. Existen causas específicas, plazos claros y un proceso de apelación formal que puedes seguir.",
        "faq_extra": [
            ("¿Cuánto tiempo tengo para apelar un rechazo?", "Tienes derecho a apelar dentro de los plazos establecidos por el país Schengen de destino principal, generalmente entre 7 y 30 días hábiles tras la notificación."),
            ("¿Un rechazo ETIAS aparece en mi historial?", "Sí. Los rechazos quedan registrados en el sistema ETIAS y pueden ser consultados en futuras solicitudes. Por eso es importante aportar documentación sólida desde el inicio."),
        ]
    },
    {
        "slug": "etias-con-antecedentes-penales",
        "titulo": "ETIAS con antecedentes penales: ¿Puedo viajar a Europa?",
        "h1": "ETIAS con Antecedentes Penales: Lo que Necesitas Saber",
        "descripcion": "¿Tienes antecedentes penales y quieres solicitar ETIAS? Guía completa sobre cómo afectan al proceso y qué puedes hacer.",
        "intro": "Tener antecedentes penales <strong>no es automáticamente una causa de rechazo</strong> de ETIAS. El sistema evalúa la naturaleza del delito, su gravedad y si representa un riesgo actual para el espacio Schengen.",
        "faq_extra": [
            ("¿Qué tipo de antecedentes pueden causar rechazo?", "Delitos graves como narcotráfico, terrorismo o crímenes violentos tienen mayor probabilidad de rechazo. Infracciones menores o condenas ya cumplidas pueden no afectar la solicitud."),
            ("¿Debo declarar mis antecedentes en ETIAS?", "Sí. ETIAS pregunta explícitamente sobre condenas penales. Omitirlas puede resultar en rechazo definitivo o prohibición de entrada. La honestidad protege tu caso."),
            ("¿Conviene contratar un consultor para este caso?", "Sí. Un consultor especializado puede evaluar tu situación específica antes de enviar la solicitud, maximizando las posibilidades de aprobación."),
        ]
    },
    {
        "slug": "etias-visa-negada-previa",
        "titulo": "ETIAS si antes me negaron una visa europea",
        "h1": "ETIAS con Visa Europea Negada Anteriormente",
        "descripcion": "¿Te negaron una visa Schengen antes? Descubre cómo afecta a tu solicitud ETIAS y qué documentación preparar.",
        "intro": "Una visa europea negada en el pasado <strong>no cierra automáticamente la puerta a ETIAS</strong>, pero sí es un factor que el sistema analiza. La clave está en demostrar que las circunstancias han cambiado.",
        "faq_extra": [
            ("¿ETIAS puede ver que me negaron una visa antes?", "Sí. ETIAS consulta bases de datos europeas que incluyen historial de visas. Una negativa previa será visible y deberás estar preparado para justificarla."),
            ("¿Cuánto tiempo debe pasar desde una visa negada?", "No hay un plazo mínimo establecido. Lo determinante es si las causas del rechazo anterior ya fueron resueltas."),
        ]
    },
    {
        "slug": "etias-rechazo-apelar",
        "titulo": "Cómo apelar un rechazo de ETIAS paso a paso",
        "h1": "Cómo Apelar un Rechazo de ETIAS: Guía Paso a Paso",
        "descripcion": "Proceso completo para apelar un rechazo de ETIAS. Documentos necesarios, plazos y estrategia para aumentar probabilidades de éxito.",
        "intro": "Si tu ETIAS fue rechazado, tienes <strong>derecho legal a apelar</strong> ante las autoridades del país Schengen de destino principal. El proceso es formal pero accesible si sigues los pasos correctos.",
        "faq_extra": [
            ("¿Ante quién se apela el rechazo de ETIAS?", "La apelación se presenta ante las autoridades migratorias del país Schengen que identificaste como destino principal en tu solicitud."),
            ("¿Puedo solicitar ETIAS de nuevo mientras apelo?", "No se recomienda enviar una nueva solicitud mientras la apelación está activa. Espera la resolución o consulta con un especialista."),
            ("¿Necesito abogado para apelar?", "No es obligatorio, pero un asesor migratorio especializado en Schengen puede aumentar significativamente las probabilidades de éxito."),
        ]
    },
    {
        "slug": "etias-tiempo-revision-extended",
        "titulo": "ETIAS en revisión extendida: cuánto tarda y qué hacer",
        "h1": "ETIAS en Revisión Extendida: Tiempos y Acciones",
        "descripcion": "¿Tu ETIAS lleva más de 96 horas en revisión? Guía sobre qué significa, cuánto puede tardar y qué hacer mientras esperas.",
        "intro": "Cuando ETIAS entra en <strong>revisión extendida</strong> supera el plazo estándar de minutos y puede tardar hasta 30 días. Esto no significa rechazo: es un proceso de verificación adicional completamente normal.",
        "faq_extra": [
            ("¿Cuánto puede durar la revisión extendida?", "El plazo máximo legal es de 30 días naturales. Si supera ese tiempo sin respuesta, tienes derecho a solicitar información al punto de contacto ETIAS."),
            ("¿Puedo comprar boletos de avión mientras espero?", "No se recomienda hasta tener la aprobación. Si ya compraste boletos y ETIAS tarda, contacta a la aerolínea sobre políticas de cambio."),
            ("¿Por qué ETIAS entra en revisión extendida?", "Puede deberse a verificación de antecedentes, inconsistencias menores en datos, o simplemente volumen elevado de solicitudes."),
        ]
    },
    {
        "slug": "etias-cancelado-que-hacer",
        "titulo": "Me cancelaron el ETIAS: causas y soluciones",
        "h1": "ETIAS Cancelado: Qué Hacer si te Revocan la Autorización",
        "descripcion": "¿Te cancelaron el ETIAS aprobado? Conoce las causas de revocación y los pasos para recuperar tu autorización de viaje.",
        "intro": "Un ETIAS aprobado puede ser <strong>revocado o cancelado</strong> si surgen nuevas circunstancias después de la aprobación. Conocer las causas te ayuda a actuar rápido y proteger tu viaje.",
        "faq_extra": [
            ("¿Por qué cancelan un ETIAS ya aprobado?", "Las causas incluyen: nueva información en bases de datos policiales, inconsistencias detectadas posteriormente, o cambios en tu situación migratoria."),
            ("¿Puedo volver a solicitar ETIAS si me lo cancelaron?", "Sí, pero debes resolver primero la causa de la cancelación. Solicitar sin atender el problema subyacente resultará en nuevo rechazo."),
        ]
    },
    {
        "slug": "etias-dudas-declaracion",
        "titulo": "Qué declarar en ETIAS sin cometer errores",
        "h1": "Cómo Rellenar la Declaración ETIAS sin Errores",
        "descripcion": "Guía detallada sobre qué declarar en cada campo del formulario ETIAS para evitar errores que causen retrasos o rechazo.",
        "intro": "El formulario ETIAS requiere <strong>precisión y honestidad</strong>. Un error tipográfico o una omisión pueden derivar en revisión extendida o rechazo. Esta guía te explica campo por campo qué declarar.",
        "faq_extra": [
            ("¿Qué pasa si cometo un error en el formulario?", "Si ya enviaste la solicitud con un error, deberás cancelarla y enviar una nueva. Los errores no se pueden editar una vez enviada."),
            ("¿Debo declarar visitas a países conflictivos?", "Sí. ETIAS pregunta sobre viajes a ciertos países en los últimos 10 años. Omitirlos es causa directa de rechazo por declaración falsa."),
            ("¿Qué domicilio declaro si viajo por varios países?", "Declara el domicilio del primer país Schengen que visitarás o donde pasarás más tiempo."),
        ]
    },
    {
        "slug": "etias-enfermedad-cronica",
        "titulo": "ETIAS con enfermedad crónica o discapacidad",
        "h1": "ETIAS con Enfermedad Crónica o Discapacidad: Guía Completa",
        "descripcion": "¿Tienes una enfermedad crónica o discapacidad y quieres solicitar ETIAS? Todo lo que necesitas saber sobre el proceso.",
        "intro": "Las enfermedades crónicas y discapacidades <strong>no son causa de rechazo automático</strong> de ETIAS. El sistema europeo evalúa riesgos de seguridad, no condiciones médicas.",
        "faq_extra": [
            ("¿ETIAS pregunta sobre enfermedades?", "El formulario puede preguntar sobre ciertas enfermedades infecciosas con riesgo de salud pública. Las enfermedades crónicas no infecciosas generalmente no afectan la solicitud."),
            ("¿Necesito seguro médico especial para ETIAS?", "ETIAS no exige seguro médico, pero para viajeros con condiciones crónicas se recomienda ampliamente contratar cobertura internacional específica."),
        ]
    },
    {
        "slug": "etias-doble-nacionalidad",
        "titulo": "ETIAS con doble nacionalidad latinoamericana",
        "h1": "ETIAS con Doble Nacionalidad: Qué Pasaporte Usar",
        "descripcion": "¿Tienes doble nacionalidad y quieres solicitar ETIAS? Guía sobre qué pasaporte presentar y cómo evitar confusiones legales.",
        "intro": "Si tienes doble nacionalidad, la regla es clara: <strong>solicita ETIAS con el pasaporte que usarás para entrar a Europa</strong>. Si uno de tus pasaportes es de un país de la UE, no necesitas ETIAS.",
        "faq_extra": [
            ("Tengo pasaporte mexicano e italiano, ¿necesito ETIAS?", "No. Si entras a Europa con tu pasaporte italiano eres ciudadano UE y no necesitas ETIAS. Solo necesitas ETIAS si entras con el pasaporte mexicano."),
            ("¿Puedo tener dos ETIAS con diferentes pasaportes?", "Técnicamente sí, pero cada ETIAS está vinculado a un pasaporte específico. Solo usa el ETIAS del pasaporte con el que viajas."),
            ("¿Debo declarar mi segunda nacionalidad en ETIAS?", "Sí. El formulario pregunta sobre otras nacionalidades. Omitirlo puede considerarse declaración falsa."),
        ]
    },
    {
        "slug": "etias-pasaporte-danado",
        "titulo": "ETIAS con pasaporte próximo a vencer o dañado",
        "h1": "ETIAS con Pasaporte por Vencer o en Mal Estado",
        "descripcion": "¿Tu pasaporte está dañado o vence pronto? Descubre si puedes solicitar ETIAS y qué requisitos de vigencia exige Europa.",
        "intro": "Europa exige que tu pasaporte tenga <strong>al menos 3 meses de vigencia adicional</strong> más allá de tu fecha de salida. Un pasaporte dañado o ilegible puede causar problemas en frontera incluso con ETIAS aprobado.",
        "faq_extra": [
            ("¿Puedo solicitar ETIAS si mi pasaporte vence en 6 meses?", "Depende de tu fecha de viaje. Si el pasaporte vence más de 3 meses después de tu regreso, es válido. Si no, renueva el pasaporte primero."),
            ("¿Qué pasa si renuevo el pasaporte después de obtener ETIAS?", "Tu ETIAS queda invalidado. Deberás solicitar uno nuevo vinculado al nuevo número de pasaporte."),
            ("¿Un pasaporte con páginas llenas es problema?", "No para ETIAS, pero en frontera europea pueden negarte entrada si no tienen espacio para sellar. Renueva si quedan menos de 2 páginas libres."),
        ]
    },
    {
        "slug": "etias-menor-edad-solo",
        "titulo": "ETIAS para menores viajando sin padres",
        "h1": "ETIAS para Menores que Viajan Solos o sin Ambos Padres",
        "descripcion": "Guía completa para padres: cómo gestionar ETIAS de menores que viajan solos, con un solo padre o con terceros a Europa.",
        "intro": "Un menor necesita ETIAS propio para viajar a Europa, pero cuando viaja <strong>sin ambos padres o tutores</strong> también se requieren documentos adicionales de autorización que van más allá del ETIAS.",
        "faq_extra": [
            ("¿Qué documentos adicionales necesita un menor que viaja solo?", "Carta notariada de autorización de ambos padres o tutores legales, copia de documentos de identidad de los padres y contacto de emergencia en destino."),
            ("¿Los menores pagan ETIAS?", "No. Los menores de 18 años están exentos del pago de €7, aunque deben obtener la autorización ETIAS igualmente."),
            ("¿Quién solicita el ETIAS de un menor?", "El padre, madre o tutor legal debe completar la solicitud en nombre del menor."),
        ]
    },
    {
        "slug": "etias-adulto-mayor",
        "titulo": "ETIAS para adultos mayores: guía paso a paso",
        "h1": "ETIAS para Adultos Mayores: Guía Simplificada",
        "descripcion": "Guía clara y sencilla sobre ETIAS para viajeros mayores de 60 años. Exenciones de pago, proceso simplificado y recomendaciones.",
        "intro": "Los viajeros mayores de 70 años están <strong>exentos del pago de €7</strong> de ETIAS. El proceso es idéntico al de cualquier otro viajero pero esta guía lo explica de forma simplificada.",
        "faq_extra": [
            ("¿Los mayores de 70 años también necesitan ETIAS?", "Sí, la autorización es obligatoria para todos independientemente de la edad, aunque los mayores de 70 años no pagan los €7."),
            ("¿Puede un familiar solicitar ETIAS en nombre de un adulto mayor?", "Sí. Cualquier persona puede completar el formulario en nombre de otro, siempre que los datos sean del titular del pasaporte."),
            ("¿Hay asistencia especial en aeropuerto para adultos mayores con ETIAS?", "ETIAS no otorga asistencia especial, pero puedes solicitarla directamente a la aerolínea al comprar tu boleto."),
        ]
    },
    {
        "slug": "etias-error-formulario",
        "titulo": "Cometí un error en mi solicitud ETIAS: qué hacer",
        "h1": "Error en el Formulario ETIAS: Cómo Corregirlo",
        "descripcion": "¿Cometiste un error en tu solicitud ETIAS? Guía de acción inmediata según el tipo de error y el estado de tu solicitud.",
        "intro": "Los errores en ETIAS <strong>no se pueden editar una vez enviada la solicitud</strong>. Sin embargo, dependiendo del tipo de error y del estado actual, hay acciones que puedes tomar para resolverlo.",
        "faq_extra": [
            ("¿Qué hago si me equivoqué en el número de pasaporte?", "Debes cancelar la solicitud actual y enviar una nueva con los datos correctos. No intentes viajar con una solicitud con datos erróneos."),
            ("¿Un error tipográfico en el nombre causa rechazo?", "Puede causar problemas en frontera aunque el ETIAS sea aprobado. El nombre debe coincidir exactamente con el pasaporte."),
            ("¿Puedo cancelar mi solicitud ETIAS?", "Sí, puedes cancelar una solicitud pendiente antes de que sea procesada. Una vez aprobada, no se puede modificar."),
        ]
    },
    {
        "slug": "etias-nombre-diferente-boleto",
        "titulo": "ETIAS y nombre distinto en el boleto de avión",
        "h1": "ETIAS: Qué Pasa si el Nombre no Coincide con el Boleto",
        "descripcion": "¿Hay diferencias entre el nombre en tu ETIAS y tu boleto de avión? Guía para resolver inconsistencias antes de viajar.",
        "intro": "La inconsistencia entre el nombre en el ETIAS y el boleto de avión <strong>puede impedirte abordar el vuelo</strong>, aunque ambos sean válidos por separado. Este problema tiene solución si actúas a tiempo.",
        "faq_extra": [
            ("¿Qué hago si mi boleto tiene un nombre abreviado?", "Contacta a la aerolínea para corregir el nombre en el boleto. Es más fácil que re-solicitar el ETIAS."),
            ("¿Los apellidos compuestos causan problemas en ETIAS?", "Sí, frecuentemente. Asegúrate de que el nombre en ETIAS coincida exactamente con cómo aparece en tu pasaporte, incluyendo todos los apellidos."),
            ("¿Las aerolíneas verifican que el nombre coincida con ETIAS?", "Sí. Las aerolíneas verifican la validez del ETIAS al momento del check-in y pueden negarte el embarque si hay inconsistencias."),
        ]
    },
    {
        "slug": "etias-historial-viajes",
        "titulo": "¿Afecta mi historial de viajes la aprobación ETIAS?",
        "h1": "Historial de Viajes y su Impacto en la Aprobación ETIAS",
        "descripcion": "Descubre cómo tu historial de viajes previos — a Europa y a otros destinos — puede influir en la aprobación o rechazo de tu ETIAS.",
        "intro": "Tu historial de viajes es uno de los factores que el sistema ETIAS analiza automáticamente. <strong>Un buen historial de viajes puede favorecer tu aprobación</strong>, mientras que ciertos viajes pueden generar revisión adicional.",
        "faq_extra": [
            ("¿Viajes a qué países pueden complicar mi ETIAS?", "Viajes recientes a países en conflicto activo o con tensiones con la UE pueden generar revisión extendida. ETIAS pregunta explícitamente sobre esto."),
            ("¿Tener muchos viajes a Europa ayuda?", "Sí. Un historial de entradas y salidas regulares sin incidentes es una señal positiva de comportamiento migratorio responsable."),
            ("¿Puedo declarar solo los viajes que recuerdo?", "Debes declarar todos los viajes relevantes que ETIAS solicite. Omitir viajes intencionalmente puede considerarse fraude."),
        ]
    },
    {
        "slug": "etias-trabajo-irregular-europa",
        "titulo": "ETIAS si trabajé sin papeles en Europa antes",
        "h1": "ETIAS si Trabajaste Irregularmente en Europa: Qué Esperar",
        "descripcion": "¿Trabajaste sin documentos en Europa y ahora quieres solicitar ETIAS? Guía honesta sobre riesgos, opciones y cómo proteger tu caso.",
        "intro": "Haber trabajado irregularmente en Europa es uno de los antecedentes que puede <strong>generar revisión extendida o rechazo en ETIAS</strong>. Sin embargo, cada caso es diferente y el tiempo transcurrido importa.",
        "faq_extra": [
            ("¿Cómo sabe ETIAS que trabajé sin papeles antes?", "ETIAS cruza datos con el Sistema de Información Schengen (SIS) y otras bases de datos europeas. Si fuiste detectado, deportado o sancionado, estará registrado."),
            ("¿Cuántos años deben pasar para que no afecte?", "Depende de si hubo deportación, multa u orden de expulsión. Sin registro formal, el impacto es menor. Con registro, consulta con un especialista."),
            ("¿Debo declararlo en el formulario ETIAS?", "Si ETIAS pregunta sobre estancias irregulares previas, debes responder con honestidad. Una declaración falsa es peor que el antecedente en sí."),
        ]
    },
    {
        "slug": "etias-solicitud-ultima-hora",
        "titulo": "ETIAS de última hora: ¿se puede aprobar en 24 horas?",
        "h1": "ETIAS de Última Hora: Tiempos Reales y Qué Hacer",
        "descripcion": "¿Necesitas ETIAS urgente para viajar en menos de 48 horas? Guía sobre tiempos reales de aprobación y opciones si el tiempo es crítico.",
        "intro": "La mayoría de las solicitudes ETIAS se aprueban en <strong>minutos</strong>, lo que técnicamente permite solicitarlo incluso horas antes del vuelo. Sin embargo, esto implica un riesgo importante si tu caso requiere revisión manual.",
        "faq_extra": [
            ("¿Cuál es el tiempo mínimo recomendado para solicitar ETIAS?", "Se recomienda solicitarlo con al menos 72 horas de anticipación. Para perfiles sin ningún antecedente, 24 horas suelen ser suficientes."),
            ("¿Hay forma de acelerar el proceso ETIAS?", "No existe proceso exprés oficial. Sin embargo, asegurarte de que todos los datos sean correctos y no tener antecedentes reduce el riesgo de revisión extendida."),
            ("¿Qué pasa si viajo sin ETIAS aprobado?", "La aerolínea no te permitirá abordar. El ETIAS debe estar aprobado antes del check-in, no solo solicitado."),
        ]
    },
    {
        "slug": "etias-rechazo-sin-motivo",
        "titulo": "ETIAS rechazado sin explicación: pasos a seguir",
        "h1": "ETIAS Rechazado sin Explicación: Qué Hacer",
        "descripcion": "¿Rechazaron tu ETIAS sin darte una razón clara? Guía sobre tus derechos, cómo obtener información y los pasos para resolver el rechazo.",
        "intro": "ETIAS puede rechazar solicitudes indicando solo la categoría general del rechazo, <strong>sin detallar la causa específica</strong> por razones de seguridad. Esto es legal pero no significa que no tengas opciones.",
        "faq_extra": [
            ("¿Tengo derecho a saber por qué rechazaron mi ETIAS?", "Tienes derecho a conocer la categoría del rechazo (seguridad, migración, salud pública) pero no necesariamente la causa específica si involucra seguridad nacional."),
            ("¿Puedo solicitar mis datos del sistema ETIAS?", "Sí. Puedes ejercer tu derecho de acceso a datos ante la autoridad supervisora del país Schengen de destino bajo el RGPD europeo."),
            ("¿Un consultor puede descubrir el motivo real?", "Un asesor migratorio especializado puede hacer consultas formales y revisar tu historial en bases de datos europeas para identificar la causa probable."),
        ]
    },
]


def generar_html(p):
    faqs_base = [
        ("¿ETIAS es una visa?", "No. ETIAS es una <strong>autorización de viaje electrónica</strong>, no una visa. Es un requisito adicional para países latinoamericanos con exención de visa Schengen, obligatorio desde Q4 2026."),
        ("¿Cuánto cuesta ETIAS?", "El costo oficial es <strong>€7 euros</strong>. Menores de 18 y mayores de 70 años están exentos del pago."),
        ("¿Cuánto tarda la aprobación normal?", "La mayoría se aprueban en <strong>minutos</strong>. En casos de revisión manual puede tardar hasta 96 horas o excepcionalmente hasta 30 días."),
        ("¿Dónde solicito ETIAS?", "Exclusivamente en el portal oficial de la Unión Europea. No hay oficinas físicas en Latinoamérica."),
    ]
    faqs_all = faqs_base + p.get("faq_extra", [])
    faqs_html = "\n".join(
        f'    <div class="faq-item"><h3>{q}</h3><p>{a}</p></div>'
        for q, a in faqs_all
    )
    pasos = [
        ("1", "Verifica tu situación", "Usa nuestro simulador gratuito para identificar si tu perfil tiene algún factor de riesgo antes de solicitar."),
        ("2", "Prepara documentación", "Reúne pasaporte vigente, correo electrónico y tarjeta de pago internacional."),
        ("3", "Completa el formulario", "Responde con precisión y honestidad cada campo del formulario oficial ETIAS."),
        ("4", "Guarda la confirmación", "Una vez aprobado, guarda tu autorización en el celular o imprímela."),
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
.badge{{display:inline-block;background:#e94560;color:white;padding:.25rem .75rem;border-radius:20px;font-size:.85rem;margin-top:.5rem}}
.container{{max-width:800px;margin:0 auto;padding:2rem 1rem}}
.alert{{background:#fff3cd;border-left:4px solid #ffc107;padding:1rem 1.25rem;border-radius:4px;margin-bottom:2rem}}
.alert-danger{{background:#fde8e8;border-left:4px solid #e94560;padding:1rem 1.25rem;border-radius:4px;margin-bottom:2rem}}
h2{{font-size:1.4rem;color:#1a1a2e;margin:2rem 0 1rem;border-bottom:2px solid #e94560;padding-bottom:.4rem}}
.step{{display:flex;gap:1rem;margin-bottom:1.5rem;align-items:flex-start}}
.step-number{{background:#e94560;color:white;width:2rem;height:2rem;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:bold;flex-shrink:0}}
.cta-box{{background:#1a1a2e;color:white;padding:2rem;border-radius:8px;text-align:center;margin:2rem 0}}
.cta-box p{{margin-bottom:1rem;opacity:.9}}
.cta-btn{{display:inline-block;background:#e94560;color:white;padding:.9rem 2rem;border-radius:6px;text-decoration:none;font-weight:bold;font-size:1.05rem}}
.consulta-box{{background:#fff8e1;border:2px solid #ffc107;padding:1.5rem;border-radius:8px;text-align:center;margin:2rem 0}}
.consulta-box p{{margin-bottom:1rem;color:#1a1a2e}}
.faq-item{{background:white;border-radius:6px;padding:1.25rem;margin-bottom:1rem;box-shadow:0 1px 3px rgba(0,0,0,.07)}}
.faq-item h3{{font-size:1rem;color:#1a1a2e;margin-bottom:.5rem}}
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
<nav class="breadcrumb"><a href="{SIMULADOR_URL}">Inicio</a> › <a href="etias-rechazo-solicitud.html">Rechazo ETIAS</a> › {p['h1']}</nav>
<div class="alert-danger"><strong>⚠️ Caso especial:</strong> Esta página aborda situaciones que pueden complicar tu solicitud ETIAS. Te recomendamos usar el simulador antes de solicitar.</div>
<p style="margin-bottom:1.5rem">{p['intro']}</p>

<div class="consulta-box">
  <p><strong>¿Tu caso tiene factores de riesgo?</strong> Simula tu solicitud gratis y recibe orientación personalizada antes de enviarla.</p>
  <a class="cta-btn" href="{SIMULADOR_URL}">🛂 Simular mi caso ETIAS</a>
</div>

<h2>Pasos Recomendados</h2>
{pasos_html}

<h2>Preguntas Frecuentes</h2>
{faqs_html}

<div class="cta-box">
  <p>¿Tienes dudas sobre tu caso específico? Usa el simulador gratuito para evaluar tu perfil ETIAS.</p>
  <a class="cta-btn" href="{SIMULADOR_URL}">🚀 Simular ETIAS Ahora — Es Gratis</a>
</div>
</div>
<footer>ETIAS Consultant Simulator | No afiliado a la Unión Europea | Información con fines educativos | <a href="{SIMULADOR_URL}" style="color:#e94560">Volver al Simulador</a></footer>
</body>
</html>"""


for p in PAGINAS:
    path = os.path.join(OUTPUT_DIR, f"{p['slug']}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(generar_html(p))
    print(f"OK {path}")

print(f"\nListo: {len(PAGINAS)} páginas Cluster A generadas")
