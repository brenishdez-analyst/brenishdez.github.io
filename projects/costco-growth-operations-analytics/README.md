# Costco Growth & Operations Analytics

**Proyecto de Data Analytics**

Dos módulos distintos: **análisis comercial con fuentes públicas reales** y **simulación hipotética de cajas con datos sintéticos**. Este proyecto no está afiliado a Costco y no utiliza datos internos ni personales.

## Dashboard interactivo
[Ver dashboard público](./index.html) — alterna ventas, crecimiento y sensibilidad de demanda.

## Preguntas de negocio
1. ¿Cómo evolucionó el crecimiento de Costco y qué periodos presentan mayor ritmo semanal de ventas?
2. Bajo supuestos sintéticos, ¿qué equilibrio existe entre costo de cajeros y espera de clientes?

## Fuentes reales y hallazgos
- Costco [Form 10-K FY2026](https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm): US$297,247 M en ventas netas FY2026, +10.13% calculado respecto a FY2025.
- Mayo FY2026: US$6,002.5 M por semana en promedio, mayor de los doce periodos comerciales; crecimiento interanual del periodo +14.5%.
- Cada mes comercial tiene 4–5 semanas. El promedio semanal **no** equivale a ventas de una semana observada.
- El acumulado de informes mensuales (US$297,250 M) difiere del dato anual exacto en US$3 M por redondeo. Se usa el Form 10-K para totales anuales.
- Fuentes por cada periodo: [comunicados mensuales](https://investor.costco.com/news/default.aspx), URLs detalladas en el CSV.

## Simulación 
Supuestos: una fila FIFO, 8 horas, tasas Poisson por hora `[25,30,35,50,55,52,40,30]` clientes/hora, servicio triangular 2.5–3.5–6 min por cliente, costo laboral hipotético MXN $150 por hora y 300 repeticiones por estrategia/nivel de demanda. Se simulan las mismas llegadas y duraciones por repetición en cada configuración.

| Política · demanda base | Espera media | P90 espera | Esperan ≤10 min | Costo jornada MXN |
|---|---:|---:|---:|---:|
| 3 cajas fijas | 14.65 min | 32.39 min | 50.53% | $3,697 |
| 5 cajas fijas | 0.30 min | 1.19 min | 100.00% | $6,009 |
| 3 fijas + 2 pico | 1.00 min | 3.42 min | 99.50% | $4,520 |

Se probaron escenarios de demanda base, +10% y +20% con 300 repeticiones por escenario y nivel. En el caso base, la estrategia flexible redujo ~93% la espera media frente a tres cajas, costando ~25% menos que cinco cajas fijas. **Es un resultado condicionado a supuestos, no una propuesta operativa validada para Costco.**

## Archivos
- `index.html`: dashboard interactivo sin servicios externos.
- `data/ventas_mensuales_fy2026.csv`: información pública, fuente individual por fila.
- `scripts/simulacion.py`: generador reproducible de escenarios.
- `docs/tarea_coach.md`: entrega en ocho apartados.

## Limitaciones
No contamos con transacciones ni tráfico de clientes de Costco, tiempos de caja observados o información de nómina. No inferimos operaciones reales a partir de las ventas de la compañía. No se entrenó un modelo predictivo supervisado; AUC/ROC no aplica. Para una decisión real serían necesarios datos de campo, costos verificables, validación y pruebas de sensibilidad adicionales.

**Trabajo independiente de aprendizaje · noviembre de 2026**
