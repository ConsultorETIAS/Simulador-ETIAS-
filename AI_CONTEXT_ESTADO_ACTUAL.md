# ESTADO_ACTUAL.md — Actualización Simulador ETIAS
## Fecha: 2026-03-18

---

## CAMBIO IMPLEMENTADO: Captura URL params en boot del simulador

### Problema resuelto
El simulador arrancaba siempre en `step:0` sin leer contexto de la URL.
Usuarios que llegaban desde páginas programáticas SEO tenían que re-escribir
su consulta manualmente → fricción → abandono.

### Solución aplicada
Parche en la sección BOOT de `index.html` (línea ~769).
El simulador ahora lee parámetros URL al arrancar:

| Parámetro | Función | Ejemplo |
|-----------|---------|---------|
| `?q=`     | Consulta libre completa | `?q=soy mexicano viajo a españa julio` |
| `?pais=`  | Nacionalidad pre-cargada en S.tv.nationality | `?pais=brasil` |
| `?destino=` | Destino pre-cargado en S.tv.destination | `?destino=portugal` |
| `?lang=`  | Idioma forzado (es/en/pt) | `?lang=pt` |

### Flujo con parámetro ?q=
1. Boot detecta `?q=`
2. Llama a la API para obtener saludo del bot
3. Inyecta saludo + mensaje del usuario como historial
4. Llama a la API con el historial completo
5. Si la respuesta incluye `INICIAR_SIMULADOR` → avanza a paso 2 automáticamente
6. Si incluye `ESCALAR_CONSULTOR` → muestra alerta de escalada
7. Si es respuesta normal → la muestra en el chat, usuario continúa

### Flujo con parámetros ?pais + ?destino
Pre-carga `S.tv.nationality` y `S.tv.destination`.
El usuario no repite lo que la página ya sabe.
Boot normal sigue con `initStep(0)`.

---

## ARCHIVO NUEVO: etias-widget.html

Widget embebible para páginas programáticas del repo SEO.
Contiene:
- Widget estándar ES
- Variante PT para páginas Brasil
- Variante contextual con pais+destino pre-cargado

**Dónde colocar el widget en cada página programática:**
```html
<!-- Después del H1 y párrafo introductorio, antes del contenido extenso -->
<!-- Include etias-widget.html o copiar el bloque directamente -->
```

---

## URLS DE EJEMPLO FUNCIONALES (post-deploy)

```
# Búsqueda larga mexicano
https://consultoretias.github.io/Simulador-ETIAS-/?q=soy+mexicano+y+viajo+a+espa%C3%B1a+en+julio

# Brasil PT
https://consultoretias.github.io/Simulador-ETIAS-/?q=sou+brasileiro+e+vou+para+portugal&lang=pt

# Con contexto pre-cargado (sin q=)
https://consultoretias.github.io/Simulador-ETIAS-/?pais=argentina&destino=italia

# Menor de edad
https://consultoretias.github.io/Simulador-ETIAS-/?q=mi+hijo+menor+necesita+etias+para+viajar+a+francia
```

---

## DEPLOY EN TERMUX

```bash
# En el repo Simulador-ETIAS-
cp etias-simulador-nuevo.html index.html
git add index.html etias-widget.html
git commit -m "feat: URL params boot — captura búsqueda larga desde SEO programático"
git push origin main
# GitHub Pages publica en ~60 segundos
```

---

## SIGUIENTE PASO

Añadir el widget en las páginas programáticas del repo SEO (el otro repo).
Prioridad por volumen de búsqueda:
1. etias-mexico.html → widget estándar ES
2. etias-brasil-*.html → widget variante PT
3. etias-argentina.html → widget estándar ES
4. etias-*-espana.html → widget contextual con destino=españa pre-cargado

---

## MÉTRICAS A MONITOREAR

- Google Search Console: CTR páginas programáticas (antes vs después del widget)
- Google Form: expedientes creados por semana
- EmailJS: emails recibidos en dggamino@gmail.com
- Fuente de tráfico: parámetro `?q=` indica llegada desde widget externo

---

## ESTADO DE PROYECTOS PARALELOS (sin cambio)

- DCT Kit: pendiente producción de contenido
- AI4US/LLM4US: estructura programática activa, sin cambios
- NFC CDMX / LATAM Digital Identity: en pausa
