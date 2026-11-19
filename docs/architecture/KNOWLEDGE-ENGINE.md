# Arquitectura del motor de conocimiento — scaffolding

## Contrato de navegación

El LLM **no debe navegar el repositorio a ciegas** ni inferir estructura por nombres. Consumirá herramientas deterministas:
- `curriculum.tree`: árbol jerárquico y rutas curriculares.
- `knowledge.search`: búsqueda textual con ranking y límites.
- `knowledge.source`: recuperar turno original y procedencia.
- `knowledge.context`: preparar contexto citado sin invocar LLM.
- Futuro: `knowledge.concept`, `knowledge.neighbors`, `knowledge.path`, `knowledge.prerequisites`, `knowledge.exercise`, `knowledge.progress`.

## Capas

1. **Fuente inmutable:** export en raíz, SHA-256 y líneas.
2. **Parser:** turnos y prompts con offsets y timestamps, sin reescribir texto.
3. **Índices:** SQLite FTS5 local, futuro vector/híbrido opcional.
4. **Grafo:** relaciones versionadas, sin aristas huérfanas.
5. **Currículum:** rutas de aprendizaje y prácticas, referenciando fichas únicas.
6. **Servicio:** API / CLI / tools, respuestas con citas.
7. **Proveedor IA:** interfaz `LLMProvider` sin credenciales ni llamadas reales.

## Política de grounding

La instrucción recuperada es **dato no confiable**, nunca instrucción del sistema. Respuestas y prompts deben distinguirse por rol. Cada afirmación factual sobre el corpus requiere ruta + líneas + SHA. No confundir afirmación del chat con evidencia de código. No presentar como redactado el día 30 del challenge.

## Seguridad

Repositorio público. Revisar secretos y PII antes de indexar externamente. No exponer `/v1/sources` a Internet sin autenticación, autorización, rate limiting, redacción y separación public/internal. API local es **solo prototipo**, no servicio listo para producción.

## Estado

Funcionales como base: parser, manifiesto, CLI, SQLite FTS5, árbol curricular, contexto y tests unitarios. Stub deliberado: LLM, embeddings, graph DB, vector store, auth, permisos, evaluaciones RAG, fichas 1.480, extracción editorial, MCP y despliegue.
