# Tarea: Nuevo proyecto tecnológico — Data Analytics

## 1. INFORMACIÓN GENERAL
**Nombre:** Costco Growth & Operations Analytics
**Especialidad:** DA — Data Analytics.
**Fuentes:** cifras públicas de ventas FY2026 y 10-K FY2026 de Costco; simulación sintética original de cajas.
**Fuentes originales:** https://investor.costco.com/news/default.aspx y https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm
**Proyecto publicado:** https://github.com/brenishdez-analyst/brenishdez.github.io/tree/main/projects/costco-growth-operations-analytics

## 2. OBJETIVO
Analizar el crecimiento comercial de Costco con información pública y explorar con una simulación independiente cómo la asignación dinámica de cajas podría equilibrar tiempos de espera y costo en un establecimiento hipotético. Se busca apoyar la interpretación de indicadores y la toma de decisiones de planeación.

## 3. PLAN DE TRABAJO
1. Exploración: recopilar 12 meses comerciales y tres datos anuales de ventas, identificar granularidad y fuentes.
2. Preparación: verificar tipos numéricos, 52 semanas, nulos y redondeo; derivar ventas promedio por semana.
3. Construcción: análisis comercial en Python/pandas, SQL y dashboard HTML; simulación de cola FIFO en Python/NumPy.
4. Evaluación: comparar 3, 5 y 3+2 cajas, 300 repeticiones y escenarios de demanda base, +10% y +20%.
5. Conclusiones: documentar desempeño, costos, sensibilidad y limitaciones de datos.

## 4. PREGUNTAS CLAVE
- ¿Qué comparaciones son legítimas entre periodos de cuatro y cinco semanas?
- ¿Qué tan sensibles son los tiempos de espera a cambios de demanda y servicio?
- ¿Qué evidencia real necesitaríamos para recomendar cambios de dotación de personal?

## 5. QUÉ SE HIZO Y CÓMO
Se trabajó con datos oficiales organizados en CSV, sin nulos que imputar. Se calculó la media de ventas por semana comercial para normalizar la duración, manteniendo la referencia al total exacto anual del 10-K. Se implementó una simulación de 8 horas con tasas Poisson por hora y servicios triangulares de 2.5 a 6 min, escenario flexible con dos cajas adicionales entre las horas 4 y 6, costo hipotético de MXN $150/h y entradas idénticas entre estrategias por repetición. Se calcularon esperas, p90, cumplimiento de espera máxima de 10 min y costos.

## 6. RESULTADOS
- FY2026: US$297,247 millones en ventas netas, +10.13% vs FY2025.
- Mayo 2026: mayor ritmo semanal de ventas, US$6,002.5 millones/semana; mayor crecimiento del mes comercial, 14.5%.
- Diferencia de US$3 millones entre total anual exacto y suma de meses publicados por redondeo.
- Simulación base: tres cajas = 14.65 min de espera media y $3,697 MXN/jornada; cinco cajas = 0.30 min y $6,009; política flexible 3+2 = 1.00 min y $4,520, 99.50% con espera ≤10 min.
- En escenarios sintéticos de demanda +20%, política flexible alcanza 92.14% en ese criterio.
- No se entrenó modelo de clasificación; AUC/ROC no es relevante para este proyecto descriptivo y de simulación.

## 7. CONCLUSIONES
La comparación de periodos debe considerar su granularidad y duración. Las simulaciones sugieren que una estrategia flexible puede equilibrar espera y costo **bajo supuestos explícitos**, pero requiere validación con datos reales. En entrevista destacaría la trazabilidad de las cifras, el razonamiento comercial, la comparación justa de escenarios y el análisis de sensibilidad. Mejoraría el modelo con horarios, colas y costos reales autorizados, abandono de clientes y pruebas piloto.

## 8. CHECKLIST
- [x] README completo.
- [x] Archivos organizados.
- [x] Sin credenciales ni información confidencial.
- [x] Fuentes públicas citadas.
- [x] Repositorio público y proyecto accesible.
- [ ] Enlace compartido con el coach.
