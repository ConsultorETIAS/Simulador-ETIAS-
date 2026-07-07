# ETIAS CONSULTANT SIMULATOR - PROYECTO MASTER

**Propietario:** Daniel Gómez Gamiño
**Objetivo:** Dominar mercado ETIAS México antes de Q4 2026
**URL REAL:** https://etias-simulador.netlify.app/
**Repo:** github.com/ConsultorETIAS/Simulador-ETIAS- (rama main → deploy automático en Netlify)
**Última actualización:** 2026-07-06

---

## ⚠️ CORRECCIÓN CRÍTICA (2026-07-06)

Todo el AI_CONTEXT/ hasta hoy decía que el hosting era GitHub Pages
(consultoretias.github.io/Simulador-ETIAS-/). ESA URL DA 404, NO EXISTE.
El proyecto se migró a Netlify (Production deploy, rama main) en algún
momento y la documentación nunca se actualizó. Corregido hoy tras
auditoría con Claude tras diagnóstico en Google Search Console.

---

## ESTADO ACTUAL (6 Jul 2026)

### Hosting y deploy
- Hosting real: Netlify, Production deploy, rama `main`, estado "Published"
- NO es GitHub Pages (ese dominio está muerto)

### SEO / Indexación (auditado hoy en GSC)
- sitemap.xml: **25 URLs** (no 82 — corregido, verificado contando el XML real)
- Propiedad GSC verificada: etias-simulador.netlify.app
- Sitemap enviado: 30 jun 2026 — Estado: Correcto — 25 páginas descubiertas
- **Indexadas: 0 / 25**
- Motivos (GSC → Páginas → Sin indexar):
  - "Descubierta: actualmente sin indexar"
  - "Rastreada: actualmente sin indexar"
- Causa: sitio nuevo (6 días desde envío de sitemap), sin autoridad de
  dominio, sin backlinks, contenido tipo pSEO (Google es cauteloso con
  páginas plantilla hasta que demuestran valor único). NO es un bloqueo
  técnico (robots.txt correcto, sin noindex, rastreo permitido = Sí).

### Simulador
- 7 pasos operativo, PDF legal trilingüe ES/EN/PT
- EmailJS activo: service_hxuq7gn / template_r225rld → dggamino@gmail.com
- Costo mensual: $0

---

## PRÓXIMOS PASOS (sin tocar arquitectura)

1. [ ] Verificar si el simulador (home) enlaza internamente a las 25
       páginas pSEO (mejora descubrimiento más allá del sitemap)
2. [ ] Solicitar indexación manual en GSC para 5-10 URLs/día
       (home + páginas más fuertes primero)
3. [ ] Esperar 2-3 semanas — es el tiempo normal para sitios nuevos
4. [ ] Re-auditar GSC cada semana, no diario (evita ruido/ansiedad de datos)

---

## REGLAS DEL PROYECTO (sin cambios)

### ✅ SÍ HACER
- Documentar cambios reales en AI_CONTEXT/ (verificados, no asumidos)
- Actualizar ESTADO_ACTUAL.md después de cada sesión
- Usar PROMPTS.md con cualquier LLM

### ❌ NO HACER
- NO modificar el simulador (774 líneas funcionando) sin backup
- NO monetizar antes de Q4 2026
- NO agregar features sin validación
- NO asumir datos de infraestructura sin verificarlos (lección de hoy)
