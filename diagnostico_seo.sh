#!/bin/bash
# DIAGNÓSTICO SEO — ETIAS Simulator
# Uso: bash diagnostico_seo.sh https://tu-dominio-real.com
# Corre en Termux. Tarda ~30 segundos. Sin dependencias nuevas (solo curl).

if [ -z "$1" ]; then
  echo "Uso: bash diagnostico_seo.sh https://tu-dominio-real.com"
  exit 1
fi

DOMAIN="$1"
echo "════════════════════════════════════════"
echo " DIAGNÓSTICO SEO: $DOMAIN"
echo "════════════════════════════════════════"

echo ""
echo "── 1. robots.txt — ¿el dominio coincide?"
echo "----------------------------------------"
curl -s "$DOMAIN/robots.txt"
echo ""
echo "→ Verifica a mano: ¿el dominio en 'Sitemap:' es EXACTAMENTE $DOMAIN?"

echo ""
echo "── 2. ¿Hay <h1> real en el HTML fuente? (sin ejecutar JS)"
echo "----------------------------------------"
H1_COUNT=$(curl -s "$DOMAIN/" | grep -o "<h1" | wc -l)
echo "Ocurrencias de <h1> en HTML crudo: $H1_COUNT"
if [ "$H1_COUNT" -eq 0 ]; then
  echo "⚠️  PROBLEMA: no hay <h1> en el HTML inicial. El contenido depende de JS."
else
  echo "✅ Hay al menos un <h1> en el HTML fuente."
fi

echo ""
echo "── 3. Canonical tag"
echo "----------------------------------------"
CANON=$(curl -s "$DOMAIN/" | grep -o '<link[^>]*canonical[^>]*>')
if [ -z "$CANON" ]; then
  echo "⚠️  PROBLEMA: no se encontró <link rel=canonical>"
else
  echo "✅ Canonical encontrado:"
  echo "$CANON"
fi

echo ""
echo "── 4. Meta description"
echo "----------------------------------------"
META=$(curl -s "$DOMAIN/" | grep -o '<meta[^>]*name="description"[^>]*>')
if [ -z "$META" ]; then
  echo "⚠️  PROBLEMA: no hay meta description"
else
  echo "✅ Meta description encontrada:"
  echo "$META"
fi

echo ""
echo "── 5. Título de página"
echo "----------------------------------------"
curl -s "$DOMAIN/" | grep -o '<title>[^<]*</title>'

echo ""
echo "── 6. Sitemap accesible y bien formado"
echo "----------------------------------------"
SITEMAP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$DOMAIN/sitemap.xml")
echo "HTTP status de sitemap.xml: $SITEMAP_STATUS"
if [ "$SITEMAP_STATUS" = "200" ]; then
  URL_COUNT=$(curl -s "$DOMAIN/sitemap.xml" | grep -o "<url>" | wc -l)
  echo "URLs declaradas en sitemap: $URL_COUNT"
  echo "Primeras 3 URLs del sitemap:"
  curl -s "$DOMAIN/sitemap.xml" | grep -o "<loc>[^<]*</loc>" | head -3
else
  echo "⚠️  PROBLEMA: sitemap.xml no responde 200"
fi

echo ""
echo "── 7. ¿Las URLs del sitemap usan el MISMO dominio que estamos probando?"
echo "----------------------------------------"
SITEMAP_DOMAIN=$(curl -s "$DOMAIN/sitemap.xml" | grep -o "<loc>[^<]*</loc>" | head -1 | sed 's/<loc>//;s/<\/loc>//')
echo "Dominio probado:        $DOMAIN"
echo "Dominio en sitemap:     $SITEMAP_DOMAIN"
echo "→ Si no coinciden EXACTAMENTE (incluyendo http vs https, www vs no-www), ese es tu problema principal."

echo ""
echo "── 8. Indexación real en Google (requiere navegador, no curl)"
echo "----------------------------------------"
echo "Corre esto a mano en el navegador del teléfono:"
echo "  site:$(echo $DOMAIN | sed 's|https://||;s|http://||;s|/$||')"
echo "Si da 0 resultados después de 2+ semanas de sitemap enviado, confirma el problema de indexación."

echo ""
echo "════════════════════════════════════════"
echo " FIN DEL DIAGNÓSTICO"
echo "════════════════════════════════════════"
