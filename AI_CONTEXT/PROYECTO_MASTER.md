# ETIAS CONSULTANT SIMULATOR - PROYECTO MASTER

**Propietario:** Daniel
**Objetivo:** Dominar mercado ETIAS México antes de Q4 2026
**URL:** https://consultoretias.github.io/Simulador-ETIAS-/
**Última actualización:** 2026-03-14

---

## ESTADO ACTUAL (14 Mar 2026)

### ✅ COMPLETADO HOY

| Tarea | Archivo/URL | Estado |
|-------|-------------|--------|
| Verificación Google Search Console | googleb3774603a75b32a8.html | ✅ Activo |
| Sitemap.xml enviado | 2 URLs indexadas | ✅ Completado |
| Robots.txt configurado | Permitir todo | ✅ Activo |
| Landing page SEO | /etias-mexico.html | ✅ Online |
| Sincronización Git | main branch | ✅ Up to date |

### 📊 MÉTRICAS ACTUALES
- **Usuarios reales:** 0
- **Tráfico:** 0
- **Indexación Google:** En proceso (24-48h)
- **Costo mensual:** $0
- **Commits totales:** 5

---

## PRÓXIMA SESIÓN AGENDADA

**📅 Martes 16 Marzo 2026 - 14:00 (1h 30min)**

**Objetivo:** Implementar envío automático de PDF por email

**Tareas:**
- Configurar EmailJS (200 emails/mes gratis)
- Modificar index.html con función enviarPDFporEmail()
- Testing con usuario de prueba
- Deploy vía Termux

**Recordatorios:** 13:00 (1h antes) + 13:45 (15 min antes)

---

## PRIORIDADES

### 🔥 URGENTE (Esta semana)
1. [ ] Envío automático PDF (Mar 16 - agendado)
2. [ ] Verificar indexación Google (48-72h post-sitemap)
3. [ ] Testear sistema memoria con otros LLMs

### 📋 IMPORTANTE (Próximas 2 semanas)
4. [ ] Crear requisitos-etias.html
5. [ ] Crear cuando-entra-vigor-etias.html
6. [ ] Formulario waitlist integrado

---

## REGLAS DEL PROYECTO

### ✅ SÍ HACER
- Documentar cambios en AI_CONTEXT/
- Usar Termux para deployment
- Actualizar ESTADO_ACTUAL.md después de cada sesión
- Usar PROMPTS.md con cualquier LLM

### ❌ NO HACER
- NO modificar index.html sin backup
- SÍ monetizar desde julio 2026 (ver DECISIONES.md 2026-07-01)
- NO agregar features sin validación
- NO sobre-optimizar código funcionando

---

**Commits totales:** 5  
**Última sincronización:** 2026-03-14  
**Próxima sesión:** Martes 16 Mar, 14:00

---

## CAMINO E: Modelos de integración con agencias europeas y agregadores de vuelos

**Objetivo**: reemplazar dependencia de SEO orgánico por distribución vía
plataformas que ya concentran al viajero.

**Modelos técnicos disponibles ($0-bajo costo de entrada)**:

1. **NDC / GDS APIs (Amadeus, Sabre, Travelport)**
   Self-service, sin ventas ni contrato. Permite ofrecer validación ETIAS
   como servicio adicional dentro de flujos de reserva ya existentes.

2. **Agregadores de vuelos con API de afiliado**
   - Kiwi.com Tequila API — motor de búsqueda de vuelos con API pública gratuita
   - Travelpayouts — red de afiliados travel, comisión por venta, sin costo fijo
   - Duffel — API moderna de reservas, self-service, pensada para startups

3. **Modelo "capa de compliance" (parasitario, alineado a tu tesis)**
   No compites por vuelos ni hoteles — te posicionas como capa de
   validación de documentos de viaje (ETIAS) que cualquier agregador
   puede insertar antes del checkout, vía webhook o iframe embebido.

4. **White-label / reventa a agencias pequeñas**
   Mismo Kit de Agencia, pero distribuido directamente a agencias
   receptivas europeas que ya atienden turistas LATAM, en vez de
   esperar que te encuentren por Google.

**Siguiente paso concreto**: elegir UNO de los 4 modelos para prototipar
antes de dispersar esfuerzo en los 4 — mismo error de fragmentación ya
documentado dos veces en este archivo.

