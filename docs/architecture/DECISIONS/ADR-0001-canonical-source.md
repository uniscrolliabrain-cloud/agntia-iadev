# ADR-0001: fuente canónica e índices derivados

Estado: aceptado para scaffolding.

Decisión: conservar la transcripción literal en raíz; no modificarla. Los índices, currículum, grafo, embeddings y fichas son proyecciones regenerables. Cada derivado lleva procedencia a líneas y hash. Se distinguen prompt del autor y respuesta del asistente.

Consecuencia: el pipeline debe soportar reindexado completo, versiones y auditoría de cobertura. El repositorio es público: la publicación externa de derivados exige revisión de privacidad.
