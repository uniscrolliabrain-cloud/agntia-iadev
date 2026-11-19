# Roadmap de implementación

- **K00 Baseline:** verificar export, hashes, conteo de turnos y anomalías; tests del parser.
- **K01 Parser:** extracción conservadora de prompts/respuestas; manifiesto y QA de offsets.
- **K02 Currículum:** leer títulos reales de capítulos/días y generar manifiesto de correspondencias; resolver divergencias sin inventar.
- **K03 Conceptos:** 1.480 fichas canónicas solo si el corpus demuestra cada una; estados `stub/extracted/reviewed/verified`.
- **K04 Grafo:** aristas tipadas, validación de nodos y fuentes.
- **K05 Recuperación:** evaluación BM25, luego híbrida y embeddings opcionales.
- **K06 API y agente:** implementar tools, adapter LLM, prompts resistentes a inyección, citas y abstención.
- **K07 Seguridad:** auth, RBAC, rate limit, redacción, límites de contexto, separación interno/público.
- **K08 Calidad:** datasets de preguntas, métricas de retrieval y groundedness, regresiones.
- **K09 Publicación:** glosario, challenge, prácticas y rutas educativas sin duplicación.

Cada fase: cambios, tests, auditoría, reporte, decisión de aprobación. Sin merge a main ni despliegue automático.
