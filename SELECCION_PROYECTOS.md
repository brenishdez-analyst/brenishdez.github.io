# Selección del portafolio — Brenis Hernández

Se revisaron 15 proyectos únicos: los 13 adjuntos, Online Retail y el caso Coppel existente. Las copias de Megaline y Zuber corresponden a los casos que ya estaban publicados; no se duplican.

La portada muestra seis casos principales. Un bloque desplegable conserva otros seis proyectos útiles. Se dejan fuera únicamente tres ejercicios iniciales de Python, cuyo contenido ya está demostrado en los proyectos más completos.

| Proyecto | Ubicación | Motivo |
| --- | --- | --- |
| Online Retail / RetailPulse | Principal | Cadena completa Python, SQL, RFM, cohortes y Tableau; evidencia organizada. |
| Coppel Puebla | Principal | Volumen de datos y KPIs operativos; gráfica interactiva con resultados guardados. |
| CallMeMaybe | Principal | Métricas por cliente–operador y dashboard; se aclara el carácter heurístico de las señales. |
| Embudo y A/A/B de alimentos | Principal | Análisis de producto y pruebas de proporciones; se distingue embudo secuencial de alcance por evento. |
| Priorización ICE/RICE y A/B | Principal | Priorización de hipótesis, anomalías y sensibilidad; se aclaran denominadores y diferencias observadas. |
| Model Fitness | Principal | Añade scikit-learn, comparación de modelos y clustering; narrativa de clústeres corregida. |
| Zuber Chicago | Complementario | SQL y estadística aplicada a movilidad; evidencia ya publicada. |
| Megaline | Complementario | Integración de cinco tablas, facturación y comparación de tarifas; evidencia ya publicada. |
| Instacart | Complementario | Preparación de tablas, recompra y exploración de compras. |
| Ice / videojuegos | Complementario | Segmentación regional y mercado histórico; no se presenta como recomendación vigente. |
| YouTube / Sprint 13 | Complementario | Presentación y CSV verificables; el TXT de enlace está vacío, por lo que no se enlaza un dashboard. |
| Showz / marketing | Complementario | Cohortes, ingresos observados y CAC; extracto limitado a análisis histórico, sin secciones experimentales ajenas. |
| Música en dos ciudades | Excluido | Ejercicio introductorio, con menor profundidad que los casos seleccionados. |
| Proyecto inicial Python 1 | Excluido | Fundamentos de Python ya demostrados por los proyectos principales. |
| Proyecto inicial Python 2 | Excluido | Fundamentos de Python ya demostrados por los proyectos principales. |

## Tratamiento de evidencias

Los archivos adjuntos originales no se modifican. Las copias para el portafolio omiten mensajes de revisión académica y conservan el código y las explicaciones. Se retiraron todas las salidas originales de las copias públicas para evitar divulgar registros o identificadores. Las métricas de las fichas proceden de las salidas originales revisadas. No se ejecutaron de nuevo con los datasets originales. En Model Fitness se corrige únicamente la descripción de etiquetas según la tabla guardada: clúster 3 = 57.29% y clúster 2 = 2.20%. En CallMeMaybe se evita presentar las pruebas sobre métricas de clasificación como validación independiente. Showz conserva las secciones previas a la priorización de hipótesis; su alcance es histórico y descriptivo.

## Mejoras futuras

- Model Fitness: validación temporal o cruzada, calibración, matriz de confusión y curva ROC/AUC antes de usar predicciones operativamente.
- CallMeMaybe: validar señales con periodos posteriores y contexto operativo; examinar atribución de registros sin operador.
- A/B: revisar denominadores agregados y establecer el criterio de cierre antes del experimento.
- YouTube: recuperar el enlace público de Tableau y pulir la presentación.
- Online Retail: corregir en la ficha del repositorio la referencia antigua a Power BI para que coincida con el dashboard de Tableau publicado.
