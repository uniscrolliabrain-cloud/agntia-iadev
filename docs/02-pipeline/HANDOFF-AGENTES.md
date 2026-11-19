# Handoff: ingesta de transcripción a fichas RAG

## Objetivo

Convertir la transcripción canónica en un corpus navegable, reproducible y auditable. Nunca sobrescribir el original.

## Fases y gates

**P0 — Baseline:** leer el archivo íntegro en streaming; registrar bytes, SHA-256, número de líneas, número de turnos, encabezados, bloques de código y anomalías del export. No inferir integridad del chat solo por tamaño.

**P1 — Segmentación:** detectar límites de mensajes `## Prompt:` y `## Response:`, conservar rangos de líneas y orden; generar manifiesto JSONL por turno. Cuidado con marcadores que aparezcan dentro de código o citas.

**P2 — Inventario:** extraer títulos, días, numeración de conceptos y talleres; detectar duplicados, saltos, inconsistencias y conceptos no desarrollados. No rellenar lagunas silenciosamente.

**P3 — Taxonomía:** asignar dominios y etiquetas con vocabulario controlado; registrar confianza y justificación, sin alterar el texto fuente.

**P4 — Fichas:** crear Markdown con YAML frontmatter, explicación pedagógica, ejemplos y referencias exactas a líneas. Separar fragmentos literales de paráfrasis y aportaciones nuevas.

**P5 — Grafo:** producir relaciones tipadas `prerequisite_of`, `related_to`, `part_of`, `contrasts_with`, `applied_in`; prohibir referencias huérfanas.

**P6 — Validación:** comprobar esquema, IDs únicos, rangos válidos, cobertura por turnos, enlaces internos, consistencia de numeración y ausencia de contenido inventado. Generar informe de gaps.

**P7 — Recuperación:** construir índice BM25 y/o vectorial; evaluar preguntas de recuperación con referencias a fuente, métricas de precisión y análisis de errores. No declarar éxito sin pruebas.

## Estructura objetivo

- `data/manifests/`: turnos, cobertura y checksums.
- `knowledge/conceptos/`: fichas Markdown.
- `knowledge/relaciones/`: aristas JSONL.
- `docs/01-taxonomia/`: categorías y esquemas.
- `docs/03-auditorias/`: informes de validación.
- `scripts/`: ingesta, extracción y tests.

## Reglas de ejecución

Trabajar en rama nueva; PR antes de integrar. No hacer merge ni desplegar sin autorización. Ejecutar una muestra piloto de 20 fichas y auditarla antes de procesar todo el corpus. Mantener una tabla de cobertura que permita rastrear cada ficha a su origen.
