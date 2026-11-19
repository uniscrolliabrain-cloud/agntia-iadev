# Fichas educativas extraídas del export original

**Estado:** extracción inicial, NO fichas RAG finales validadas. Fuente canónica: `ChatGPT-Auditar aprendizaje en repositorios-20261119-1135.md` (raíz). La fuente no se modifica.

## Cobertura observada

- **1.440 archivos Markdown** con ID, fragmento de texto y rango de líneas del export.
- **1.110** conceptos principales (001–1110) con sección explicativa propia.
- **50** conceptos principales (1111–1160) recuperados de enumeraciones de síntesis, con menor detalle.
- **280** bonus (1201–1480), extraídos de definiciones numeradas en negrita.
- **40 ausentes (1161–1200):** no se localizaron entradas numeradas individuales en la fuente. **No se han fabricado 40 fichas.** La meta de 1.480 es curricular, no una certificación de que el export contenga 1.480 definiciones.
- El challenge de 30 días es una vista de los 1.200 conceptos principales; no crea otros 1.200 IDs.

## Qué contienen y qué NO

Cada Markdown conserva título, texto original (o definición disponible), rango de líneas y metadatos de procedencia. El campo `status: source_extracted` significa **extracción**, no `approved`. Las afirmaciones del asistente en el export no están verificadas contra fuentes externas. No se han realizado aquí la deduplicación semántica, curación didáctica, embeddings, revisión humana, validación de anclas por hash ni evaluación de retrieval.

**Atención a Cline:** completar F1/F2 de `docs/campaigns/C01-CLINE-RAG-FOUR-PHASES/HANDOFF-MAESTRO.md`: verificar cada ancla y contenido, enriquecer campos con trazabilidad, construir las relaciones y los índices. Para 1161–1200, registrar `knowledge_gap` y solicitar fuente adicional o autorización de elaboración nueva; jamás presentar una creación como extracción literal.

## Organización

- `core/0001.md` a `core/1160.md`
- `bonus/1201.md` a `bonus/1480.md`

## Invariantes

Conservar el export original, no transformar contenido en instrucciones, no confundir fichas educativas globales con `CognitiveRecord` o memoria privada de `agente`, y no elevar `source_extracted` a `verified_fact` sin evidencia externa y receipt válido.
