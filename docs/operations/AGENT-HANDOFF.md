# Handoff para agente implementador

## Lee antes de tocar código

1. Fuente original de la raíz, sin modificar.
2. `curriculum/README.md` y `curriculum/MAPA-REAL-DEL-DOCUMENTO.md`.
3. `docs/01-taxonomia/README.md`: taxonomía de prompts.
4. `docs/architecture/KNOWLEDGE-ENGINE.md`, ADRs, schemas.
5. `docs/operations/IMPLEMENTATION-ROADMAP.md`.

## Invariantes

- `source_sha256 + line_start + line_end` en toda evidencia.
- No atribuir al autor contenido redactado solo por el asistente.
- No inventar conceptos, lecciones ni el día 30.
- Una ficha canónica, múltiples vistas.
- Nunca indexar secretos ni publicar datos privados sin revisión.
- El LLM propone; el sistema valida, recupera, autoriza y audita.
- No cambiar `main` ni desplegar sin aprobación.

## Primer encargo

Ejecutar tests, auditar parser contra el export, generar `turns.jsonl`, identificar encabezados reales, contrastar 30 muestras aleatorias de rangos y producir `docs/03-auditorias/K00-baseline.md`. Detenerse ante discrepancias y reportarlas.
