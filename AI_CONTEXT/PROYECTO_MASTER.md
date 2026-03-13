# PROYECTO ETIAS CONSULTANT SIMULATOR
**Última actualización**: 2026-03-12 21:45 (Daniel vía Claude + Termux)

---

## 🎯 OBJETIVO PRINCIPAL

**Dominar el mercado ETIAS México antes de Q4 2026.**

Posicionarse como la #1 plataforma de verificación ETIAS para viajeros latinoamericanos ANTES de que ETIAS sea obligatorio (octubre 2026).

**NO es un negocio activo hoy. Es construcción de ventanilla para Q4 2026.**

---

## 📊 ESTADO ACTUAL DEL PROYECTO

### ✅ LO QUE TENEMOS FUNCIONANDO

1. **Simulador web completo** (~1,150 líneas según Kimi AI)
   - URL: https://consultoretias.github.io/Simulador-ETIAS-/
   - 3 idiomas: ES/EN/PT
   - 6 pasos: Representación → Pasaporte → Datos → Validación → Revisión → Confirmación
   - Genera PDF de Declaración de Representación (compliance UE 2018/1240)
   - Email intermediario: consultor.etias@proton.me
   - Stack: Vanilla JS (sin frameworks), 1 dependencia (jsPDF 2.5.1)

2. **GitHub repo público + Termux funcionando**
   - Repo: ConsultorETIAS/Simulador-ETIAS-
   - Git configurado en Termux
   - Branch main sincronizado
   - Files: index.html, README.md

3. **Bot Telegram**
   - Username: @ETIAS_BOT
   - Link: https://t.me/ETIAS_BOT
   - QR code profesional generado
   - Estado: Funcionó 1 vez, actualmente inactivo

4. **Artefactos adicionales**
   - 45 HTMLs de iteraciones previas (en Telegram)
   - PDFs generados funcionales (ej: ETIAS-MMO1J67J.pdf)

### ❌ LO QUE NO TENEMOS

1. **SEO**: Sitio NO indexado en Google
2. **Leads**: Sin captura de emails para Q4 2026
3. **Tráfico**: 0 usuarios reales probando el simulador
4. **Distribución**: Sin estrategia de marketing activa
5. **Programmatic SEO**: Sin páginas automáticas (nacionalidad × destino)

---

## 🚫 PROBLEMA RESUELTO HOY

### Problema técnico principal
**Pérdida de contexto entre LLMs free (Claude, ChatGPT, Moonshot, Kimi)**
- Cada sesión empezaba desde cero
- Respuestas contradictorias entre modelos
- Implementaciones infinitas sin conclusión
- Parálisis por análisis (>1 año sin lanzamiento)

### Solución implementada
**Este archivo (PROYECTO_MASTER.md) = memoria externa**
- Todos los LLMs leen este contexto al inicio
- Continuidad garantizada entre sesiones
- Decisiones documentadas en DECISIONES.md

---

## 📋 ENTORNO TÉCNICO

**Hardware/Software:**
- Device: Android 14
- Terminal: Termux (git configurado)
- LLMs: Claude.ai (free tier), ChatGPT, Moonshot AI, Kimi AI
- Integraciones Claude: Gmail, Google Drive, Google Calendar

**Stack del proyecto:**
- Frontend: HTML puro (~1,150 líneas)
- Hosting: GitHub Pages (free)
- Domain: consultoretias.github.io/Simulador-ETIAS-/
- Backend: Ninguno (todo client-side JavaScript)
- Persistence: LocalStorage + PDF generation (jsPDF client-side)

**Costos actuales:**
- Total: $0 USD/mes
- GitHub Pages: Free
- LLMs: Free tiers
- Dominio: Ninguno (usando subdomain de GitHub)

---

## 🎯 ESTRATEGIA Q4 2026

**Timeline:**
AHORA - Junio 2026:
├─ Optimización SEO (1000 páginas pSEO)
├─ Captura de leads (waitlist 1000 emails)
├─ Partnerships con agencias de viaje
└─ Inversión: $50 (dominio etias-mexico.com)
Julio - Septiembre 2026:
├─ Refinar simulador
├─ Pre-lanzamiento con early adopters
└─ Ajustar pricing
Octubre 2026 (ETIAS LANZA):
├─ 1000 páginas SEO → tráfico masivo
├─ 1000 emails waitlist → conversión
├─ 5 agencias partner → volumen
└─ DOMINIO MERCADO MEXICANO
**Por qué esto funciona:**
- ETIAS no es obligatorio hasta Q4 2026
- Competidores NO están construyendo ahora
- Ventaja first-mover en SEO (6 meses anticipación)
- Cuando ETIAS lance, YA estamos posicionados #1

---

## 🚀 PRIORIDADES ACTUALES (MARZO 2026)

### PRIORIDAD 1: SEO básico (esta semana)
- [ ] Crear sitemap.xml
- [ ] Crear robots.txt  
- [ ] Página /etias-mexico.html (keyword exacta)
- [ ] Optimizar meta tags en index.html (opcional)
- [ ] Submit a Google Search Console

### PRIORIDAD 2: Captura de leads (próxima semana)
- [ ] Agregar formulario waitlist al simulador
- [ ] Conectar con Google Sheets
- [ ] Mensaje: "ETIAS lanza Q4 2026 - déjanos tu email"

### PRIORIDAD 3: Programmatic SEO (2 semanas)
- [ ] Script genera 100 páginas (nacionalidad × destino)
- [ ] GitHub Actions automatiza generación
- [ ] Deploy automático a GitHub Pages

---

## 📚 DOCUMENTOS RELACIONADOS

- **ESTADO_ACTUAL.md**: Qué hacer HOY (tareas específicas)
- **PROMPTS.md**: Cómo iniciar cualquier LLM con este proyecto
- **DECISIONES.md**: Historial de cambios importantes
- **index.html**: Código del simulador (~1,150 líneas)

---

## 🔒 REGLAS DEL PROYECTO

1. **NO implementar sin documentar**: Cualquier cambio va a DECISIONES.md
2. **NO construir features nuevas**: Solo SEO + captura leads hasta Q4 2026
3. **NO monetizar ahora**: ETIAS no existe, enfoque en posicionamiento
4. **NO sobre-optimizar**: Lanzar imperfecto > iterar 6 meses más
5. **SÍ actualizar este archivo**: Después de cada sesión con cualquier LLM

---

## 📧 CONTACTO

- Email intermediario: consultor.etias@proton.me
- GitHub: ConsultorETIAS
- Telegram Bot: @ETIAS_BOT

---

**INSTRUCCIÓN PARA LLMs:**
Cuando Daniel te comparta este archivo, PRIMERO léelo completo, LUEGO pregunta: "¿Qué tarea específica de las PRIORIDADES quieres hacer hoy?" NO sugieras cambios arquitectónicos. NO propongas "mejoras". Solo ejecuta las tareas listadas.
