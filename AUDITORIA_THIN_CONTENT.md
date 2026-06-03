# AUDITORÍA THIN CONTENT — 5 abril 2026

## Resultado general
- 175 páginas en disco
- 95 URLs en sitemap (enviado a GSC el 3 abril)
- 80 páginas fuera del sitemap — Google no las ha visto
- 3,830 pares con similitud ≥80% → thin content confirmado
- Checkpoint GSC: 8 abril — NO tocar sitemap hasta entonces

## Causa raíz
`generar_cluster_b.py` y scripts por país tienen dos bloques
fijos idénticos en todas las páginas:

1. `faqs_base` — 4 FAQs hardcodeadas (costo, días, visa, definición)
2. `pasos` — 4 pasos idénticos en todas las páginas

Estos bloques representan ~60% del contenido visible.
Los datos únicos (intro, perfil, faq_extra) solo aportan ~40%.

## Páginas saludables (agregar al sitemap post-8 abril)
- etias-medicos-mexicanos.html — 21% similitud ✅
- etias-freelancers-nomadas.html — 20% similitud ✅
- etias-argentina.html — 29-32% similitud ✅

## Páginas críticas (NO agregar sin corregir)
- etias-estudiantes.html ↔ etias-luna-de-miel.html — 97.6% ❌
- etias-menores-de-edad.html ↔ etias-viajar-italia.html — 98.0% ❌
- etias-viajar-italia.html ↔ etias-viajar-espana.html — 98.4% ❌
- Todos los etias-viajar-*.html entre sí — 98.8% ❌
- etias-baja-california.html ↔ etias-baja-california-sur.html — 98.8% ❌

## Corrección pendiente (ejecutar post-8 abril)
En generar_cluster_b.py:
- Mover faqs_base al diccionario de cada página (personalizar por perfil)
- Mover pasos al diccionario de cada página (personalizar por perfil)
- Objetivo: bajar similitud a <40% entre páginas del mismo cluster

En generar_brasil.py y demás scripts por país:
- Verificar si tienen el mismo patrón de bloques fijos
- Aplicar misma corrección

## Flujo post-8 abril
1. Revisar GSC — ¿cuántas de las 95 URLs indexadas?
2. Corregir generar_cluster_b.py
3. Corregir scripts por país
4. Regenerar páginas corregidas
5. Ejecutar auditor_pseo.py — verificar similitud <40%
6. Actualizar sitemap con las 175 URLs
7. Resubmitir sitemap a GSC
