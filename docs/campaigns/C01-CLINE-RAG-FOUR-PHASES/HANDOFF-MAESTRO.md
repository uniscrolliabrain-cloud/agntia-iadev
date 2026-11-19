# C01 — Campaña integral de fichas RAG, grafo y motor IADEV (Cline, 4 fases)

**Ejecutor:** un único agente Cline. **Repositorio:** `uniscrolliabrain-cloud/agntia-iadev`. **Base:** `main`. **Alcance:** implementar y verificar, no solo documentar. **Referencia externa de lectura:** `uniscrolliabrain-cloud/agente` (NO modificar). **No desplegar ni fusionar a main sin aprobación del usuario.**

## Misión y resultado

Transformar el export íntegro e inmutable `ChatGPT-Auditar aprendizaje en repositorios-20261119-1135.md` en una biblioteca educativa RAG de alta fidelidad, con fichas atómicas, trazabilidad a líneas y turnos, relaciones navegables, índices consultables, API Python y SDK TypeScript funcionales. La estructura prevista es **8 etapas × 150 = 1.200 conceptos**, **7 bonus × 40 = 280**; los **30 días × 40** son una *vista alternativa* de los mismos 1.200, no otros 1.200 conceptos. **No fabricar conceptos para cumplir cuotas**: publicar cobertura real, huecos y pendientes de revisión. Las fichas se fundamentan en el texto y se distinguen las solicitudes del usuario de las respuestas del asistente.

## Contratos de alineación con `agente` (lectura de código de main, 2026-11-19)

Releer en el HEAD actual antes de implementar:
- `packages/domain/src/cognition-v2.ts`: `cognitiveRecordSchema` v2, `epistemicSchema` (reported_fact/inference/hypothesis/unknown/contradicted/verified_fact), evidencia obligatoria, revisiones, lifecycle, visibilidad tenant/actor/policyRevision; `verified_fact` **requiere receipt**. Las cinco memorias son episodic/semantic/procedural/autobiographical/working; working exige expiración.
- `packages/domain/src/cognitive-reference.ts`: refs tipadas tenantId/kind/id/revision; no enlaces cruzados entre tenants.
- `packages/domain/src/card-ontology.ts` y `apps/server/src/engine/cognition/chromatic/card-ontology.ts`: ontología aprobada `agntiapro.cards@1.0.0`, familias observation/hypothesis/risk/opportunity/procedure/decision/outcome/knowledge_gap; tres pares explore/apply, generate/verify, expand/protect; dimensiones con `null` para desconocidos; assessments `review: proposed`, consenso y disputas; no simular aprobación ni recibos.
- `apps/server/src/engine/cognition/v2/context.ts`: `ContextServingFacade` valida membership/policy, visibilidad, evidencia, revocaciones y revisiones antes de servir; segmentos marcados `untrusted_data`, snapshot con watermark, digest y TTL; nunca confiar en el prompt como autorización.
- `apps/server/src/engine/cognition/v2/rag.ts`: `PreparedRagContext` reutiliza RAG existente fuera del Fast path; descarta fuentes stale/unverified, revalida sourceVersion; crea proyecciones semánticas privadas por tenant, **no** datos globales de autoridad.
- `apps/server/src/engine/cognition/v2/memory.ts`: `FiveMemories` usa bus y proyecciones; memoria procedural requiere receipt de SOP, semanticFromCard no hereda certificación verified_fact, la memoria nunca es SOP ejecutable.
- `apps/server/src/kernel/cognition/card-builder.ts` y `card-store.ts`: tarjetas cognitivas de pensamientos con ID idempotente, evidence y lifecycle propios. **No confundirlas** con fichas documentales IADEV.
- `apps/server/src/engine/authz/pdp.ts`: deny-by-default/deny-overrides, ABAC tenant y rol; la autoridad reside en `agente`.
- `docs/implementation/cognition-v2/C05/ADR-CHROMATIC-ONTOLOGY.md`: diseño aprobado con gates de integración/calidad pendientes. No afirmar que la ontología está completamente certificada.

**Regla de frontera:** `IADEV KnowledgeCard` es contenido editorial global y versionado, NO un `CognitiveRecord` ni una memoria del tenant. El host `agente` decide si proyecta fragmentos autorizados a contexto temporal o memoria semántica privada; la proyección debe retener source/version/evidence, no heredar verificación y revalidar política. Nunca importar directamente módulos internos de `agente` desde IADEV; usar contratos versionados y SDK.

## Invariantes no negociables

1. Fuente canónica inmutable; hashes SHA-256, archivo, rango de líneas, turno, rol, timestamp cuando exista. Cada afirmación sustancial y ejemplo derivado debe apuntar a evidencia. Ninguna cita inventada.
2. Separar `source_text`, `paraphrase`, `teaching_expansion`, `inference`, `editorial_note` y `unknown`. Una expansión pedagógica NO es una cita literal. La respuesta de ChatGPT en el export NO es una verdad verificada por sí misma.
3. Propuestas del LLM = datos no confiables; validación determinista, Zod/JSON Schema/Pydantic o equivalentes, revisión y estado `proposed/approved/rejected`; nunca autocertificación.
4. IDs estables basados en fuente+ancla+versión, normalización determinista, reingesta idempotente, actualización por revisión y manifiesto de cambios; no duplicar por reintentos.
5. El grafo educativo tiene tipos `prerequisite`, `explains`, `example_of`, `related_to`, `contrasts_with`, `applied_in`, `derived_from`; cada arista con evidencia o `proposed`. No mezclar con `cognitiveEdgeSchema` de tenant.
6. Corpus global en IADEV, sin datos personales de alumnos. Progreso, preferencias, memorias y anotaciones privadas viven en `agente` y sujetos a sus permisos.
7. Recuperación y salida con `trust: untrusted_data`; el texto indexado no puede cambiar system prompt, invocar herramientas, modificar políticas o emitir SOPs. Fail-closed.
8. Presupuestos de tokens, tamaño de documento, concurrencia, reintentos, cancelación, rate limit, timeouts, límites de resultados; logs sin secretos ni export íntegro.
9. No ejecutar acciones externas, merges, despliegues, facturación ni cambios en `agente` sin autorización. No introducir dependencias de red obligatorias para tests.

## FASE 1 — Baseline, parser, contratos y taxonomía

**Objetivo:** corpus auditable, sin pérdida de contenido. **Waves:**
- **W1.0:** crear rama `feat/cline-c01-rag-production` desde main; inventario de fuente, docs, scripts, schemas, Python/TS; registrar HEAD y baseline de pruebas. No reescribir el export.
- **W1.1:** corregir parser de `src/iadev/ingest.py` con fixtures reales y casos borde: timestamps, marcadores, headings anidados, fences, Unicode, CRLF, duplicados, truncamiento. Manifestar cada bloque y línea; reporte de cobertura de bytes/líneas y errores. Reconciliar turnos con fuente.
- **W1.2:** formalizar `schemas/knowledge-card.schema.json`, `source-anchor.schema.json`, `knowledge-edge.schema.json`, `curriculum-view.schema.json`, `extraction-run.schema.json`; modelos Python y contratos TS equivalentes; versionar. Campos mínimos: id, schemaVersion, revision, kind, title, definition, explanation, example(s), prerequisites, misconceptions, exerciseRefs, taxonomy, stageRefs, challengeRefs, bonusRefs, provenance[], epistemic, trust, status, confidence nullable, contentDigest, createdAt, updatedAt. SourceAnchor: source SHA, path, turnId, role, lineStart/lineEnd, exactQuote opcional, digest. Separar evidencia y elaboración.
- **W1.3:** extraer catálogo real de etapas/días/bonus, construir matriz source→curriculum y curriculum→source. Los 30 días referencian IDs de los mismos 1.200 conceptos. Vacíos se reportan, no se rellenan.
- **W1.4:** tests de roundtrip, hashes, line spans, invariantes, schema validation, determinismo, no pérdida; producir `reports/C01/F1-BASELINE.md`, `F1-COVERAGE.json`, `F1-TESTS.md`.

**Gate F1:** parser reproducible; cobertura de fuente medida y explicada; ningún ancla fuera de rango; fixtures reales y sintéticos verdes; matriz de contenido sin afirmaciones ficticias.

## FASE 2 — Generación de fichas RAG y control editorial

**Objetivo:** fichas útiles y fieles al corpus, no chunks arbitrarios disfrazados de conceptos. **Waves:**
- **W2.0:** definir criterios de atomicidad (una idea enseñable por ficha), granularidad, deduplicación y tipos concept/technique/pattern/example/exercise/question/decision/knowledge_gap. Registrar prompt de extracción, versión de modelo, input/output digest y costes si aplica.
- **W2.1:** pipeline por lotes con checkpoints reanudables, dry-run, límite de coste/tokens, retries y quarantine. Primero extracción determinista de títulos/anclas; LLM opcional para candidatos, siempre con evidencia verificable. Sin API: modo determinista produce candidatos anclados y gaps; no inventar explicaciones.
- **W2.2:** completar fichas pedagógicas con definición, intuición, ejemplo software/IA, cuándo usar, cuándo no, error frecuente, prerrequisitos, ejercicio, prueba de comprensión, tags, referencias. Cada campo generado declara origen `source` o `teaching_expansion`; lo no soportado queda `unknown` o `proposed`.
- **W2.3:** validadores automáticos: citas comprobables contra líneas originales; prohibir `verified_fact` sin receipt externo válido; no duplicados semánticos/ID; consistencia de referencias, lenguaje, longitud y clasificación; revisión de muestras estratificadas por etapa y bonus. Mantener estados y lista de revisión humana.
- **W2.4:** persistir fichas legibles en `knowledge/cards/<stage-or-bonus>/<id>.json` o JSONL particionado más manifiesto; índices regenerables, nunca fuente de verdad. Publicar métricas `target/produced/approved/proposed/missing/duplicate/rejected` por sección, sin declarar 1.480 completadas si no lo están. Reportes `F2-CARDS.json`, `F2-QUALITY.md`, `F2-REVIEW-QUEUE.jsonl`.

**Gate F2:** toda ficha con source anchor válido, origen de campos, ID y revisión; ninguna cita falsa; cobertura cuantificada; revisión de calidad reproducible; ningún placeholder presentado como ficha final.

## FASE 3 — Grafo, retrieval, API y SDK

**Objetivo:** navegar y recuperar fichas con citas y relaciones. **Waves:**
- **W3.0:** construir grafo versionado con aristas evidenciadas; detección de ciclos en `prerequisite`, dangling refs, contradicciones, enlaces entre etapas y crosswalk de challenge. Los edges sugeridos sin evidencia quedan `proposed`.
- **W3.1:** índice léxico FTS5 (existente) + adaptador opcional de embeddings/vector store; retrieval híbrido configurable con fallback léxico, ranking determinista y límites. Separar fuente original, fichas y ejemplos; snippets con citas.
- **W3.2:** ampliar `KnowledgeService` y FastAPI: `/v1/cards/{id}`, `/v1/cards/{id}/neighbors`, `/v1/learning-path`, `/v1/search`, `/v1/context`, `/v1/curriculum`; contratos, errores tipados, paginación y versionado. Conservar endpoints actuales.
- **W3.3:** implementar autenticación service-to-service real (bearer verificado, JWT con issuer/audience/exp/scopes o token estático de alta entropía validado de forma segura para entorno controlado), rechazar ausencias, origen no aprobado, límites y fallos. No aceptar el bearer solo porque el SDK lo envía. Health pública solo si no revela datos.
- **W3.4:** extender `typescript/src/contracts.ts`, `client.ts`, `agent-tools.ts`, `hono.ts`; las capacidades son read-only, host autentica y autoriza `knowledge.read`, no proxies públicos sin guard. Tests HTTP reales contra FastAPI local + negativos (401,403,404,429, stale, malformed, timeout, huge payload, injection). Mantener Node 22+, pnpm y compatibilidad con Hono/Zod de `agente`; no introducir import runtime a `agente`.
- **W3.5:** preparar `integrations/agente/ADAPTER-CONTRACT.md` y ejemplos de instalación, identidad, policyRevision, correlación, trazabilidad, cache invalidation y `untrusted_data`. **Solo contrato y fixture aquí**, sin tocar el repo de `agente`. Reportes `F3-RETRIEVAL.md`, `F3-CONTRACT-TESTS.md`, `F3-SECURITY.md`.

**Gate F3:** consultas devuelven resultados correctos con evidencia y relaciones, endpoints tipados y autenticados, tests de integración Python↔TS verdes, sin bypass de permisos.

## FASE 4 — Evaluación, hardening y entrega a integración

**Objetivo:** listo para instalar como capacidad educativa en `agente`, sin proclamar certificaciones inexistentes. **Waves:**
- **W4.0:** dataset de evaluación reproducible: preguntas literales, sinónimos, multi-hop, prerrequisitos, trampas, inexistentes, confusión prompt/response, falsos verified_fact, prompt injection, idioma español, cambios de fuente, fuentes revocadas.
- **W4.1:** medir recall@k, MRR/nDCG cuando haya gold labels, citation precision, unsupported-claim rate, tasa de abstención, p50/p95 latency y memoria/coste; registrar baseline y deltas, no inventar métricas.
- **W4.2:** testear idempotencia, reproducibilidad de hashes, reingesta, upgrade de schema, invalidación de índices, concurrency, crash recovery, límites, token leaks, archivos enormes, path traversal y respuesta degradada.
- **W4.3:** ejecutar `python -m pytest`, `python -m compileall src`, `pnpm --dir typescript install`, `pnpm --dir typescript build`, `pnpm --dir typescript test` (adaptar scripts reales), E2E API+SDK, CI; registrar comando, versión, duración, salida y SHA. No reportar verde sin ejecución.
- **W4.4:** completar docs `docs/operations/QUICKSTART.md`, `docs/operations/DEPLOYMENT.md`, `docs/operations/AGENTE-INTEGRATION.md`, `docs/operations/RUNBOOK.md`; env/secrets, rollback, migraciones, límites y ejemplos; checklist de integración con `agente`.
- **W4.5:** informe final `reports/C01/FINAL-ACCEPTANCE.md` con matriz requisito→archivo→test→evidencia→estado; problemas abiertos, SHA, commits, cambios, riesgos y próxima acción. Crear PR a main, **no mergear sin aprobación**.

**Gate F4:** CI y E2E reales verdes, no hay fugas ni citas falsas conocidas, cobertura y métricas publicadas, SDK utilizable y handoff de integración comprobable.

## Instrucciones operativas para Cline

Ejecuta las cuatro fases **secuencialmente** sin detenerte a pedir confirmación entre waves cuando no haya bloqueos. Mantén un solo branch y un solo ejecutor; commits pequeños por wave, cada uno con pruebas y reportes. No delegues a otros agentes. Relee los archivos del repo antes de editarlos, conserva compatibilidad, no hagas refactorizaciones laterales. Antes de cualquier acción con coste externo, secret, despliegue o merge, solicita autorización. Si falta una API de LLM, implementa el modo determinista, deja adapter pluggable y reporta la limitación; **no generes 1.480 ficciones para rellenar la cuota**.

**Formato de checkpoints:** `reports/C01/PROGRESS.md` con fecha, branch, SHA, wave, archivos creados/modificados, comandos/tests, cobertura real, bloqueos, decisiones y próximo paso. Al terminar cada fase registra gate PASS/FAIL/PARTIAL y por qué. Ante FAIL, corrige y reejecuta; no avances declarando PASS ficticio. Conserva el export original sin editar.

**Criterio de terminado:** se puede hacer una consulta desde el SDK TS a la API Python local, obtener fichas educativas reales con citas de líneas correctas, navegar el grafo y las vistas curriculares, y demostrar con pruebas que un actor sin permiso no recibe datos y que la fuente no se ejecuta como instrucción. Si no se alcanza, entrega el trabajo honesto con bloqueos precisos.

## Prompt de arranque para Cline

> Trabaja en `uniscrolliabrain-cloud/agntia-iadev`. Lee íntegramente `docs/campaigns/C01-CLINE-RAG-FOUR-PHASES/HANDOFF-MAESTRO.md` y ejecuta las cuatro fases, con sus waves y gates, sin resumir ni limitarte a documentación. Consulta en modo lectura los contratos de kernel/cognition/policy de `uniscrolliabrain-cloud/agente` enumerados aquí; no los modifiques. Crea una rama de implementación, ejecuta y documenta pruebas, genera fichas RAG únicamente con evidencia real y publica un PR sin merge a main. Sigue el protocolo de checkpoints y no declares gates verdes sin pruebas.
