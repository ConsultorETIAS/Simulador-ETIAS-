# ESTADO ACTUAL — ETIAS SIMULATOR
**Fecha**: 2026-03-25
**Última actualización**: 18:30 CST

---

## ✅ COMPLETADO HOY (2026-03-25)

- [x] Arreglado sitemap.xml roto (estructura XML inválida)
- [x] Creado generar_sitemap.py — genera sitemap desde archivos reales
- [x] Generadas 13 páginas Chile (spokes: requisitos, costo, Santiago, España, etc.)
- [x] Generadas 12 páginas Venezuela (spokes: requisitos, costo, España, diáspora, etc.)
- [x] Sitemap limpio con 207 URLs deployado en un solo commit
- [x] Sitemap enviado a Google Search Console ✅
- [x] Verificación agendada en calendario: 8 abril y 15 abril

**Commit**: f20a1ce → 72eb6b1
**URLs en sitemap**: 207
**Sitemap enviado a GSC**: 25 mar 2026 ✅

---

## 🚫 REGLA CRÍTICA HASTA 8 ABRIL

**NO modificar sitemap.xml.**
Google necesita verlo estable 2-3 semanas para indexar.
El problema anterior era exactamente ese: cambios diarios = 0 indexación.

---

## 📊 COBERTURA ACTUAL POR PAÍS

| País | Hub | Spokes | Estado |
|------|-----|--------|--------|
| México | ✅ | 32 estados + segmentos | Profundo |
| Argentina | ✅ | ~18 spokes | Profundo |
| Brasil | ✅ | ~20 spokes | Profundo |
| Colombia | ✅ | ~19 spokes | Profundo |
| Chile | ✅ | 13 spokes nuevos | ✅ Hoy |
| Venezuela | ✅ | 12 spokes nuevos | ✅ Hoy |
| Bolivia | ✅ | 0 spokes | Solo hub |
| Ecuador | ✅ | 0 spokes | Solo hub |
| Costa Rica | ✅ | 0 spokes | Solo hub |
| Perú | ❌ | — | PRÓXIMO BATCH |

---

## 🔥 PRÓXIMO BATCH (semana 8 abril — post verificación)

1. Perú (hub nuevo + spokes: Lima, requisitos, costo, turismo)
2. Nuevo León (estado mexicano faltante, alta prioridad)
3. Puebla (estado mexicano faltante)
4. Quintana Roo (Cancún, turismo alto)

**Flujo fijo para cualquier batch:**
```bash
cd ~/ETIAS-simulador
python3 generar_[país].py
python3 generar_sitemap.py
git add . && git commit -m "Add [país] + sitemap" && git push
```

---

## 📋 SCRIPTS DISPONIBLES EN REPO

```
generar_argentina.py
generar_brasil.py
generar_colombia.py
generar_chile.py       ← nuevo hoy
generar_venezuela.py   ← nuevo hoy
generar_cluster_a.py
generar_cluster_b.py
generar_sitemap.py     ← nuevo hoy — USAR SIEMPRE AL FINAL
```

---

## 📅 AGENDA

| Fecha | Acción |
|-------|--------|
| 25 mar 2026 | Sitemap 207 URLs enviado a GSC ✅ |
| 8 abr 2026 | Verificar indexación GSC — ¿cuántas URLs? |
| 15 abr 2026 | Segunda verificación si indexación parcial |
| Post 8 abr | Batch Perú + Nuevo León + Puebla |

---

## 🚫 REGLAS ESTRICTAS

- ❌ NO tocar sitemap.xml hasta 8 abril
- ❌ NO monetizar antes de Q4 2026
- ❌ NO modificar index.html (774 líneas funcionando)
- ✅ SÍ ejecutar generar_sitemap.py después de cada batch
- ✅ SÍ respetar flujo: generar → sitemap → push
