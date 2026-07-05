# DECISIONES DEL PROYECTO ETIAS

Registro cronológico de decisiones importantes y lecciones aprendidas.

---

## 2026-03-12 (Sesión Claude + Termux)

### ✅ DECISIÓN: Crear sistema de memoria persistente multi-LLM

**Contexto**: 
- >1 año iterando con LLMs free sin conclusión
- Cada chat empezaba desde cero (Claude, ChatGPT, Moonshot, Kimi)
- Pérdida de contexto entre sesiones
- 45 artefactos HTML creados, ninguno lanzado

**Solución implementada**:
- AI_CONTEXT/PROYECTO_MASTER.md = única fuente de verdad
- AI_CONTEXT/PROMPTS.md = prompt maestro para iniciar cualquier LLM
- AI_CONTEXT/ESTADO_ACTUAL.md = tareas concretas del día
- AI_CONTEXT/DECISIONES.md = este archivo
- Git en Termux para deployment

**Resultado esperado**:
- Continuidad entre sesiones
- Cualquier LLM puede continuar exactamente donde quedó el anterior
- Fin de la parálisis por análisis

---

### ✅ DECISIÓN: NO monetizar hasta Q4 2026

**Contexto**:
- ETIAS no es obligatorio hasta octubre 2026
- Intentar cobrar hoy = imposible (producto no existe)
- Simulador funcional pero sin demanda actual

**Estrategia adoptada**:
- Marzo-Septiembre 2026: Construcción de ventanilla (SEO + leads)
- Octubre 2026: Avalancha de demanda → captura mercado

**Implicaciones**:
- Costo mensual debe ser $0 (no hay revenue)
- Enfoque 100% en posicionamiento SEO
- Capturar 1000 emails waitlist para octubre

---

### ✅ DECISIÓN: Priorizar SEO sobre features

**Contexto**:
- 45 artefactos HTML iterados sin distribución
- 0 tráfico orgánico
- Simulador funcional (~1,150 líneas) pero invisible en Google
- Kimi AI confirmó tamaño real del código

**Prioridades definidas**:
1. SEO básico (sitemap, robots.txt, meta tags)
2. Programmatic SEO (1000 páginas automáticas)
3. Captura de leads (formulario waitlist)

**Features descartadas** (hasta octubre 2026):
- ❌ OCR de pasaporte (ya existe en algún artefacto, no es prioridad)
- ❌ Integración Telegram bot compleja
- ❌ Backend/database
- ❌ Panel admin/CRM
- ❌ Optimizaciones UI/UX del simulador

**Razón**: 
Google tarda 3-6 meses en indexar y rankear contenido nuevo.
Si empezamos SEO en marzo, estaremos rankeados #1 en octubre cuando ETIAS lance.

---

### ✅ DECISIÓN: GitHub Pages + Termux como stack definitivo

**Alternativas consideradas**:
- Vercel
- Netlify  
- Hosting pago
- Editar directo en GitHub web

**Decisión final**: GitHub Pages + Git desde Termux

**Razones**:
- Costo: $0 (vs $5-10/mes otros)
- Control total desde Android vía Termux
- Ya tenemos repo: ConsultorETIAS/Simulador-ETIAS-
- Soporta custom domains (cuando compremos etias-mexico.com)
- Unlimited bandwidth
- SSL gratis
- Git-based deployment (profesional, versionado)

---

### ✅ DECISIÓN: NO modificar index.html existente

**Contexto**:
- index.html tiene ~1,150 líneas (confirmado por Kimi AI)
- Funciona correctamente (genera PDFs, 3 idiomas, 6 pasos)
- Vanilla JS sin frameworks
- 1 dependencia: jsPDF 2.5.1

**Decisión**:
- Dejar index.html intacto
- Crear archivos SEO NUEVOS (sitemap, robots, páginas optimizadas)
- Estos archivos NO requieren modificar código existente

**Razón**:
- "Si funciona, no lo toques"
- 1,150 líneas = riesgo de romper algo
- SEO se logra con archivos adicionales, no modificando el simulador
- Separación de concerns: simulador (funcional) vs SEO (marketing)

---

### ❌ LECCIÓN APRENDIDA: No sobre-optimizar sin usuarios

**Error cometido**:
- >1 año construyendo 45 versiones HTML
- Probando solo con LLMs free
- 0 usuarios reales testeando
- Cada LLM sugería "mejoras" diferentes
- Parálisis por análisis

**Consecuencia**:
- Tiempo perdido en "arquitectura perfecta"
- Features que nadie pidió
- Código funcionando pero sin distribución

**Corrección aplicada hoy**:
- Sistema de memoria persistente (PROYECTO_MASTER.md)
- Reglas claras: NO features, SÍ SEO
- Enfoque en lanzamiento imperfecto
- Documentar decisiones para no repetir errores

---

### 📝 DECISIONES PENDIENTES

- [ ] ¿Comprar dominio etias-mexico.com ($12/año) o seguir con GitHub subdomain?
- [ ] ¿Contactar agencias de viaje AHORA o esperar a tener tráfico SEO primero?
- [ ] ¿Implementar pSEO con 100 páginas o ir directo a 1000?
- [ ] ¿Usar Personal Access Token temporal o crear uno sin expiración?

---

## TEMPLATE PARA NUEVAS DECISIONES
✅/❌ DECISIÓN: [Título]
Contexto:
[Por qué surgió esta decisión]
Alternativas consideradas:
Opción A
Opción B
Decisión final: [La que elegimos]
Razones:
Razón 1
Razón 2
Implicaciones:
Consecuencia 1
Consecuencia 2
---

**Actualiza este archivo después de cada decisión importante para no repetir errores.**

---

## 2026-03-12 (22:00) - DEPLOYMENT EXITOSO

### ✅ HITO: Primer deployment completo del sistema

**Logros**:
- 7 archivos nuevos deployados vía Termux + Git
- Sistema de memoria persistente funcionando
- Archivos SEO básicos live en GitHub Pages
- Commit: d27a9c4..3030dd0

**Archivos deployados**:
1. AI_CONTEXT/PROYECTO_MASTER.md
2. AI_CONTEXT/ESTADO_ACTUAL.md
3. AI_CONTEXT/PROMPTS.md
4. AI_CONTEXT/DECISIONES.md
5. sitemap.xml
6. robots.txt
7. etias-mexico.html

**Resultado**:
- ✅ URLs funcionando en GitHub Pages
- ✅ Sistema de contexto listo para usar con otros LLMs
- ✅ SEO básico implementado
- ✅ Base para escalamiento pSEO

**Próximo paso**:
Submit a Google Search Console para iniciar indexación

---
## 2026-03-17 — EmailJS integrado

- Botón enviar reparado y funcional
- EmailJS conectado: service_hxuq7gn / template_r225rld
- Variables template: {{name}}, {{nombre}}, {{email}}, {{nacionalid}}, {{title}}
- Promise.all: Google Forms + EmailJS simultáneo
- Fix caracteres especiales en PDF footer
- Estado: pre-simulador operativo al 100%

## 2026-03-18 — SEO title y meta description

### ✅ DECISIÓN: Actualizar title y meta description con keywords reales

**Cambio realizado:**
- Antes: `<title>ETIAS Agente Autorizado</title>`
- Después: `<title>ETIAS México 2026 — Tramita tu autorización de viaje a Europa</title>`
- Meta description actualizada con keywords: México, Argentina, Brasil, Colombia, Uruguay, €20, Q4 2026

**Razón:**
- Google reescribía el título porque el original era genérico
- Keywords de búsqueda real aumentan CTR orgánico
- Mercado objetivo: viajeros latinoamericanos a Europa

**Commit:** ca3e5bc
# DECISIONES DEL PROYECTO ETIAS
*(Solo se agrega la entrada nueva. Pega esto al final de tu AI_CONTEXT/DECISIONES.md existente)*

---

## 2026-03-25 — Sitemap estable + Chile + Venezuela

### ✅ DECISIÓN: generar_sitemap.py como script maestro permanente

**Problema identificado**:
- sitemap.xml se estaba editando manualmente o parcialmente
- Estructura XML rota: etiquetas mezcladas, URLs sin cerrar
- Google descartaba el sitemap completo en cada rastreo
- Resultado: 0 indexación a pesar de 174 páginas deployadas

**Solución implementada**:
- `generar_sitemap.py` genera sitemap desde archivos .html reales del repo
- Excluye automáticamente googleb3774603a75b32a8.html
- Asigna priority 1.0 a index.html y 0.7 al resto
- Se ejecuta SIEMPRE al final de cada batch

**Regla nueva**:
- Flujo fijo: generar_[país].py → generar_sitemap.py → git push
- NO editar sitemap.xml manualmente jamás

---

### ✅ DECISIÓN: NO tocar sitemap hasta 8 abril 2026

**Contexto**:
- Sitemap enviado a GSC el 25 marzo con 207 URLs limpias
- Google necesita 2-3 semanas de sitemap estable para indexar
- El problema anterior era cambios diarios que impedían indexación

**Implicación**:
- Próximo batch (Perú, Nuevo León, Puebla) se ejecuta DESPUÉS del 8 abril
- Verificación agendada: 8 abril y 15 abril en calendario

---

### ✅ HITO: 207 URLs en producción — 25 marzo 2026

**Países con cobertura profunda**: México, Argentina, Brasil, Colombia, Chile, Venezuela
**Países con solo hub**: Bolivia, Ecuador, Costa Rica, Honduras, Guatemala, El Salvador, Panamá, Paraguay, Cuba, Nicaragua, Rep. Dominicana, Uruguay
**Próximo**: Perú (hub + spokes completos)

## 2026-05-14 — Sitemap y referencias indexadas

### ✅ DECISIÓN: Agregar referencia sitemap en HEAD de todas las páginas

**Problema detectado:**
- 200 páginas en sitemap.xml
- GSC reportaba "No se ha detectado ningún sitemap de referencia"
- Cada página HTML no tenía `<link rel="sitemap">` en el head

**Solución implementada:**
- Sed loop: agregar `<link rel="sitemap">` antes de `</head>` en 199 archivos
- Git push: commit `2f7e8c2`
- Reenviar sitemap a GSC después de propagar (30 min)

**Estado esperado:**
- Indexación de 200+ URLs en 3-7 días
- Checkpoint: 22 mayo 15:00 en GSC

## 2026-06-07 — Sitemap corregido
- Problema: sitemap solo tenía 5 URLs
- Solución: regenerado con Python, 203 URLs
- Submitido a GSC: etias.netlify.app
- Estado: procesando (24-72h)

## 2026-06-07 — Consolidación dominio principal

### ✅ DECISIÓN: Netlify como dominio único
- GitHub Pages deshabilitado (Branch: None)
- robots.txt apunta a etias.netlify.app/sitemap.xml
- Sitemap con 203 URLs submitido a GSC
- Eliminada canibalización SEO entre dos dominios
- Dominio principal: https://etias.netlify.app

## 2026-06-08 — Cloudflare Worker proxy anti API-key-hell

- Worker: https://etias-proxy.dggamino.workers.dev
- GROQ_KEY guardada como secreto Cloudflare (nunca en HTML)
- Modelo: llama-3.1-8b-instant
- chatWithETIAS: reglas locales + fallback Worker para preguntas libres
- Token CF guardado en ~/etias_cf_token.txt (no commitear)
- Para cambiar modelo: editar ~/worker.js y correr ~/crear_worker.py

---

## 2026-06-29 — FIX CRÍTICO: dominio cruzado robots.txt vs sitemap

### ✅ HALLAZGO: causa raíz de meses sin indexación en Google

**Contexto**:
- >3 meses con sitemap.xml "Correcto" en GSC (203 URLs) pero 0 páginas indexadas
- Se sospechaba CSR, contenido fino, o falta de canonical tags

**Diagnóstico real**:
- robots.txt apuntaba a `https://etias.netlify.app/sitemap.xml`
- Ese dominio (`etias.netlify.app`) NO es nuestro — es un proyecto Netlify ajeno con nombre parecido
- El sitemap real siempre vivió en `https://etias-simulador.netlify.app/sitemap.xml`
- Google nunca pudo conectar robots.txt con el sitemap real con suficiente confianza

**Confirmación del hosting real**:
- El proyecto NO usa GitHub Pages (a pesar de lo que dice PROYECTO_MASTER.md original)
- Hosting real: Netlify, site "etias-simulador", deploy automático desde GitHub main
- Dominio canónico: https://etias-simulador.netlify.app/

**Fix aplicado**:
- robots.txt corregido para apuntar a `https://etias-simulador.netlify.app/sitemap.xml`
- Commit: 1b05899
- Confirmado en producción vía curl

**Lección operativa**:
- Otra sesión (LLM distinto o edición directa en GitHub web) ya había corregido esto
  parcialmente (commits ed61447, f7ee921) sin que quedara reflejado en AI_CONTEXT/
- AI_CONTEXT/ debe actualizarse INMEDIATAMENTE después de cada fix, no al final del día,
  para evitar trabajo duplicado entre sesiones

### 📝 PRÓXIMOS PASOS (registrados 29 jun 2026)
- [ ] Solicitar indexación manual en GSC (cuota diaria se resetea c/24h)
- [ ] Revisar "Indexación de páginas" en GSC en 3-7 días
- [ ] Verificar con site:etias-simulador.netlify.app en Google
- [ ] Revisar y depurar tokens de GitHub sin uso (6 activos detectados, varios sin expiración)

---

## 2026-07-01 — CAMBIO DE REGLA: Activación de monetización

### ✅ DECISIÓN: Iniciar cobro del servicio ETIAS Pass desde julio 2026 (deroga espera a Q4 2026)

**Contexto**:
- Estrategia original (12 mar 2026): NO monetizar hasta Q4 2026, apostar todo a pSEO
- 4 meses de pSEO (82 URLs indexadas) sin conversión a usuarios/leads reales
- 0 usuarios reales, 0 ingreso — la espera pasiva no está funcionando

**Decisión final**: Activar monetización del servicio (Declaración de Representación + gestión documental ETIAS) desde julio 2026, usando los leads ya capturados vía EmailJS/Google Forms como primera base a contactar.

**Alcance explícito**:
- SÍ: cobrar honorarios de intermediación desde ahora
- NO incluido aquí: venta/cesión de datos de leads a terceros (decisión distinta, no activada hoy)

**Implicaciones**:
- ETIAS_PASS_copy_corregido.md pasa de copy preparatorio a copy operativo
- Contactar leads existentes ofreciendo el servicio pagado
- Comunicar el honorario claramente antes de cualquier cobro
- Infraestructura sigue en \$0/mes — cambia la política comercial, no el stack

**Reemplaza**: la regla "NO monetizar hasta Q4 2026" en PROYECTO_MASTER.md, PROMPTS.md y ESTADO_ACTUAL.md

---

## 2026-07-05 — LECCIÓN: pSEO modo "specialist" fallido + confirmación monetización Q3

**Resultado del experimento pSEO**:
- 203 páginas generadas (conteo declarado en esta sesión — inconsistente
  con sesiones previas: 82 URLs en marzo, 24 URLs el 29-jun en Netlify)
- Cero indexación, cero leads, cero clics
- Diagnóstico: thin content — páginas generadas por template sin
  diferenciación sustancial de contenido real

**Factor agravante identificado**: cuenta de Search Console con 6+
propiedades activas de proyectos no relacionados (viralprotest.org,
etias-agency-os.netlify.app, hereditaria.netlify.app, etc.) — patrón de
dispersión entre múltiples dominios/proyectos, mismo error estructural
que ya se documentó en 2026-03-12 (45 artefactos HTML sin lanzar).

**DECISIÓN CONFIRMADA: Monetizar en Q3 2026**
- Se abandona la estrategia de esperar indexación orgánica antes de cobrar
- Canal de distribución pasa de SEO orgánico a integración directa con
  agentes/agencias y plataformas existentes (ver Camino E en PROYECTO_MASTER.md)

