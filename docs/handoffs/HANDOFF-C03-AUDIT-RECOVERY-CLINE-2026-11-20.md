# HANDOFF C03 — Auditoría, recuperación y finalización de IADEV tras Cline

**Fecha de auditoría remota:** 2026-11-20. **Repositorio:** `uniscrolliabrain-cloud/agntia-iadev`. **Destino:** nuevo agente ejecutor en GitHub Codespaces. **Base auditada:** `main` en `e6b7401e812c38a174e3ed5d5bda225a9526c404`. **Carácter:** diagnóstico basado en código publicado, NO certificación de ejecución local ni atribución personal de trabajo a Cline.

## 0. Contexto del producto y dirección

IADEV es una biblioteca educativa y un servicio de conocimiento RAG de ingeniería de software, aprendizaje de desarrollo con IA y sistemas agénticos. La fuente histórica es `ChatGPT-Auditar aprendizaje en repositorios-20261119-1135.md` (~1,26 MB), preservada en la raíz del repositorio. La estructura curricular histórica incluye ocho etapas con 1.200 conceptos objetivo, una vista alternativa de treinta días sobre esos mismos conceptos, y siete días bonus con 280 conceptos adicionales. No duplicar los 1.200 conceptos por tener dos vistas.

La extracción previa publicó **1.440 fichas Markdown**: 1.160 `knowledge/cards/core/` y 280 `knowledge/cards/bonus/`. Las fichas principales 1111–1160 proceden de síntesis más breves. Los números 1161–1200 (40) no tienen entradas individuales encontradas y **no se deben inventar como citas**. Cada ficha inicial tiene estado `source_extracted` y revisión pendiente: NO equivale a ficha pedagógica aprobada ni a hecho contrastado. Revisar `knowledge/cards/README.md`.

IADEV debe ofrecer conocimiento editorial global y versionado a AgntiaPro: **usuario → chat/runtime de AgntiaPro → SDK TypeScript IADEV → API Python IADEV → recuperación RAG y grafo → corpus**. AgntiaPro es responsable de LLM conversacional, autorización por tenant/actor y memoria; IADEV NO debe duplicar el chat, la orquestación ni convertirse en fuente de autoridad. El conocimiento recuperado es `untrusted_data`, nunca una instrucción ejecutable. El host conserva políticas deny-by-default/fail-closed, versionado, auditoría, revocación y revalidación de procedencia.

La alineación se define en `docs/campaigns/C01-CLINE-RAG-FOUR-PHASES/HANDOFF-MAESTRO.md`. Leer íntegro antes de editar. Consultar **solo en lectura** el repositorio `uniscrolliabrain-cloud/agente` y sus contratos de cognition-v2, cognitive-reference, card-ontology, context, rag, memory y authz/pdp citados allí. Las KnowledgeCards editoriales NO son CognitiveRecords ni memoria privada. No modificar `agente`.

El futuro módulo «Coding with AI» debe ser **ampliación editorial separada** (C02, identificadores propios, sin alterar el histórico), con conocimiento general e independiente de Meta, OpenAI o Anthropic. Su diseño no debe retrasar la finalización verificable de C01. No consta C02 publicado en `main` en el árbol auditado; comprobar de nuevo antes de trabajar.

## 1. Evidencia remota comprobada el 20-11-2026

- `main` HEAD: `e6b7401e812c...`, commit «docs(cards): document 1440 extracted cards and 40 source gaps» (19-11-2026).
- Ramas remotas detectadas: `main`, `docs/curriculum-arbol-completo`, `feat/knowledge-engine-scaffold`, `feat/typescript-knowledge-sdk`. **NO se encontró** `feat/cline-c01-rag-production`.
- PR #1 («docs: incorporar árbol curricular completo») fusionado 19-11-2026; PR #2 («Integrar motor de conocimiento y SDK TypeScript en main») fusionado 19-11-2026. No se encontró PR C01 nuevo.
- Árbol `main`: 1.561 archivos, 1.440 fichas + README, tres tests Python (`test_curriculum.py`, `test_ingest.py`, `test_storage.py`) y un test TypeScript (`typescript/test/client.test.mjs`). No se encontró carpeta `reports/C01/` ni contenido C02.
- GitHub Actions: 13 ejecuciones observadas de `knowledge-ci`, últimas con conclusión `success`; workflow `.github/workflows/knowledge-ci.yml` ejecuta solo Python 3.11, `pip install -e '.[dev]'` y `pytest -q`. **No certifica** compilación TS, E2E, seguridad, retrieval ni C01.
- No se pudo inspeccionar el filesystem local de Codespaces: **la ausencia de rama remota no demuestra ausencia de trabajo local**. Tampoco permite atribuir inequívocamente los commits anteriores a Cline.

Evidencia navegable:
- https://github.com/uniscrolliabrain-cloud/agntia-iadev/tree/main
- https://github.com/uniscrolliabrain-cloud/agntia-iadev/blob/main/docs/campaigns/C01-CLINE-RAG-FOUR-PHASES/HANDOFF-MAESTRO.md
- https://github.com/uniscrolliabrain-cloud/agntia-iadev/blob/main/knowledge/cards/README.md
- https://github.com/uniscrolliabrain-cloud/agntia-iadev/actions
- https://github.com/uniscrolliabrain-cloud/agntia-iadev/pull/1
- https://github.com/uniscrolliabrain-cloud/agntia-iadev/pull/2

## 2. Evaluación provisional del código PUBLICADO (no de Cline)

| Área | Nota indicativa | Evidencia y límite |
|---|---:|---|
| Arquitectura y fronteras | 8/10 | Servicio Python y cliente TS separados; host conserva autorización |
| Ingestión/trazabilidad inicial | 7/10 | Parser conservador, SHA-256 y líneas; faltan auditoría de anclas y roundtrip |
| Biblioteca educativa | 6/10 | 1.440 extracciones, sin enriquecimiento y aprobación editorial sistemáticos |
| Recuperación RAG | 4/10 | FTS5 sobre turnos, no motor híbrido sobre fichas |
| API Python | 4/10 | Endpoints básicos, sin verificación bearer |
| SDK TypeScript | 7/10 | Zod, validación origen, timeout, límite tamaño y errores |
| Grafo | 1/10 | Sin implementación funcional comprobada |
| Seguridad extremo a extremo | 3/10 | Backend no autentica; acceso a fuentes peligroso si se expone |
| Tests/CI | 5/10 | CI Python verde, sin E2E API↔SDK ni build TS en workflow |

**Valoración agregada orientativa: 6/10 como scaffold/prototipo; C01 NO EVALUABLE hasta recuperar sus evidencias.** Las notas son juicio de revisión estática y deben recalibrarse con pruebas y commits reales.

### Hallazgos concretos por archivo

1. `src/iadev/api.py`: FastAPI expone `/health`, `/v1/curriculum`, `/v1/search`, `/v1/sources/{turn_id}`, `/v1/context`; `/v1/answer` devuelve 501. No se observa middleware/dependencia de autenticación, scopes, rate limits ni autorización. **P0** antes de publicar API o proxy.
2. `src/iadev/storage.py`: tablas `turns`, `turns_fts` y `metadata`; búsqueda BM25/FTS5 sobre texto de turnos, no sobre fichas pedagógicas. Los parámetros FTS se normalizan a tokens entrecomillados, buena base. Requiere indexado versionado de fichas, filtros, invalidación y grafo.
3. `src/iadev/ingest.py`: detecta `## Prompt:`/`## Response:` solo con timestamp; genera SHA y spans; necesita pruebas contra falsos marcadores, fences, saltos de línea, export truncado, contenido previo/posterior, offsets y cobertura total. No reescribir fuente original.
4. `src/iadev/service.py`: servicio ofrece árbol, búsqueda, fuente y contexto; todavía no ofrece ficha individual, vecinos, rutas ni currículo enlazado a fichas.
5. `typescript/src/client.ts`: cliente server-only, Zod, approvedOrigins, bearer, timeout, max 1 MiB, no redirect, errores tipados. El hecho de enviar bearer **no autentica** el backend.
6. `typescript/src/hono.ts`: adaptador confía en que `resolve(c)` autorice previamente; documentar y testear fail-closed del host. No instalar proxy público sin PDP real.
7. `typescript/src/agent-tools.ts`: cuatro herramientas read-only (curriculum.tree, knowledge.search, knowledge.source, knowledge.context). No hay todavía cards/neighbors/learning-path.
8. `.github/workflows/knowledge-ci.yml`: CI limitada a Python; extender a TypeScript, contratos y E2E sin credenciales de pago.
9. `knowledge/cards/core/0001.md`: ejemplo de ficha `source_extracted` con título, extracto y rango; no es todavía la KnowledgeCard rica con campos pedagógicos, estado editorial y hashes validados.
10. `docs/architecture/KNOWLEDGE-ENGINE.md` y `typescript/README.md` reconocen explícitamente stubs y falta de autenticación. No presentar el scaffold como producto terminado.

### Riesgos P0/P1

- **P0 privacidad:** repositorio público con transcripción original; inspeccionar secretos, PII, identificadores, direcciones, emails, credenciales y datos sensibles antes de indexar, publicar más, exportar embeddings o permitir acceso remoto. Si hay exposición, detener publicación, comunicar al owner y acordar remediación (incluida rotación de secretos si procede). No borrar ni reescribir fuente unilateralmente.
- **P0 API:** proteger todas las rutas de corpus, incluido sources; validar bearer real, scopes/audience/exp o secreto de servicio seguro, limitar petición y rate; pruebas negativas 401/403/429. No exponer el prototipo.
- **P0 integración:** impedir que contenido documental actúe como instrucciones del runtime o conceda autoridad.
- **P1 editorial:** validar anclas de las 1.440 fichas contra SHA/rango/texto; separar cita literal, paráfrasis, ampliación pedagógica e inferencia; cola de revisión y métricas por sección.
- **P1 robustez:** índices reproducibles/idempotentes, sin enlaces huérfanos, sin ciclos de prerequisitos, invalidación de revisiones, límites de memoria/tiempo/coste, errores tipados y abstención.

## 3. PRIMERA ACCIÓN DEL NUEVO AGENTE: recuperar trabajo real de Cline

No empezar programando a ciegas. Ejecutar en Codespaces:

```bash
pwd
git remote -v
git status --short
git branch -avv
git log --all --date=iso -15 --format='%h %ad %d %s'
git fetch origin --prune
git ls-remote --heads origin
git worktree list
git stash list
find . -maxdepth 3 -type d \( -name reports -o -name .git \) -print
```

Inspeccionar si Cline creó cambios sin commit, commits locales no empujados, worktrees, stashes, otra rama, otro repositorio o un Codespace distinto. **No hacer `git reset --hard`, `git clean -fd`, `git checkout -f` ni borrar archivos** hasta recuperar trabajo. Si hay trabajo local, hacer backup/snapshot seguro, atribuirlo por commit/fecha y contrastarlo con la campaña C01. Si no hay cambios, registrar evidencia y continuar desde el HEAD real.

Leer íntegramente `docs/campaigns/C01-CLINE-RAG-FOUR-PHASES/HANDOFF-MAESTRO.md`, el handoff de usuario, `knowledge/cards/README.md`, `docs/01-taxonomia/README.md`, arquitectura, schemas, tests y los 1.440 archivos de fichas por procesamiento programático. No confundir ausencia de un archivo en directorio local con ausencia en `origin/main`: usar `git show origin/main:<path>`.

## 4. PLAN DE EJECUCIÓN — Completar C01 sin rehacer lo que funciona

Trabajar en rama nueva `feat/c03-recovery-c01-production` desde el commit correcto tras auditar y preservar trabajo de Cline. Si hay una rama de implementación existente, continuarla o integrarla de forma controlada en lugar de duplicar. **No merge a main ni deploy sin autorización**. La autorización actual para escribir este handoff en main no autoriza fusionar código de implementación.

### F0 — Baseline y recuperación
- Inventariar ramas, commits, worktrees, stashes, PR y CI; identificar autoría y estado por evidencia.
- Registrar SHA, Python/Node/pnpm, comandos y resultados; ejecutar suites existentes y reproducir fallos.
- Crear `reports/C03/F0-BASELINE.md` y `reports/C03/RECOVERY.md` con inventario de cambios recuperados.
- Gate: baseline reproducible y trabajo previo preservado.

### F1 — Integridad, contratos y corpus
- Validar las 1.440 fichas, IDs, rango de líneas, roles, SHA, fragmentos, contenido, duplicados, truncamientos y 40 gaps.
- Introducir contratos JSON Schema/Python/TS versionados para KnowledgeCard, SourceAnchor, Edge, CurriculumView, ExtractionRun; conservar fuente y Markdown originales.
- Separar `source_text`, `paraphrase`, `teaching_expansion`, `inference`, `unknown`; estados proposed/approved/rejected y revisión humana.
- Producir manifest y cobertura exacta por core/bonus/etapa/día con tests automáticos.
- Gate: anclas comprobables, sin afirmaciones inventadas, incidencias cuantificadas.

### F2 — Enriquecimiento pedagógico y grafo
- Convertir extractos en fichas atómicas útiles: definición, explicación principiante/técnica, ejemplos, uso/no uso, errores frecuentes, prerequisitos, ejercicios, preguntas.
- No rellenar por cuota; ampliaciones nuevas con `teaching_expansion` y estado `proposed`; no autocertificar verificaciones.
- Construir grafo tipado y versionado, edges con evidencia o `proposed`, detectar referencias huérfanas/ciclos y generar vistas curriculares sin duplicación.
- Cola de revisión y evaluación de calidad editorial estratificada.
- Gate: cobertura y calidad reales documentadas; separar código completo de revisión humana pendiente.

### F3 — Motor RAG, API, SDK, auth
- FTS5 sobre fichas/chunks con IDs y anclas; embeddings/vector opcional y recuperación híbrida con fallback offline; ranking, deduplicación, filtros y neighbors.
- Endpoints versionados cards, neighbors, learning-path, search, context, curriculum, sources; respuestas tipadas y paginadas.
- Backend con autenticación service-to-service real, scopes, límites, timeouts, control de origen y protección de contenido; no depender de que el SDK mande token.
- SDK TS con herramientas read-only nuevas; integración por contrato versionado, sin importar módulos internos de `agente`; adapter documentado para policyRevision, tenant/actor y sourceVersion.
- E2E real Node SDK ↔ FastAPI local con 200,401,403,404,422,429, timeout, malformed, stale, injection.
- Gate: respuesta real con ficha y citas verificables, permisos negativos comprobados.

### F4 — QA, evaluación, documentación y PR
- Dataset reproducible con preguntas literales, semánticas, multi-hop, ambiguas, sin respuesta, falsos hechos verificados, injection y corpus obsoleto.
- Medir recall@k, MRR/nDCG cuando haya labels, precision de citas, abstención, latencias y costes; no inventar métricas.
- Tests de idempotencia, reproducibilidad, migraciones, revisión, invalidación, concurrencia, crash recovery, límites y secretos.
- CI Python + Node 22/pnpm build/tests + E2E sin proveedor de pago; registrar logs y SHA.
- Guías de instalación, Codespaces, API, SDK, actualización de corpus, seguridad, runbook, rollback e integración con `agente`.
- `reports/C03/FINAL-ACCEPTANCE.md`: requisito→archivo→test→evidencia→PASS/PARTIAL/FAIL; PR publicado a main, sin merge.
- Gate: demo reproducible, resultados medidos y pendientes explícitos.

## 5. Protocolo de ejecución y entregables

1. Inspeccionar antes de modificar. Priorizar recuperación de trabajo local y seguridad.
2. Implementar por waves pequeñas; tests y corrección antes de avanzar; commits trazables; checkpoints en `reports/C03/PROGRESS.md`.
3. No depender de LLM/embeddings externos para tests; si faltan claves, continuar con modo determinista y dejar adapter opcional.
4. No ejecutar costes, despliegues, merges, cambios en `agente`, borrado de fuente ni acciones irreversibles sin aprobación.
5. Registrar evidencias reales; nunca declarar PASS sin pruebas; no atribuir a Cline commits sin prueba de autoría.
6. Mantener el histórico original y las 1.440 fichas; migrar por proyecciones versionadas y conservar procedencia.
7. Entregar rama, commits, PR, reportes, inventario de incidencias, pruebas ejecutadas y handoff siguiente.

## 6. Criterio final de aceptación

Una petición desde SDK TS obtiene, vía API Python autenticada, una ficha educativa real y versionada con citas correctas y relaciones navegables; una petición sin permisos se deniega; el índice se regenera de forma determinista; la fuente original no se altera ni puede inyectar instrucciones; las 1.440 fichas están auditadas con incidencias explícitas; los 40 gaps se reconocen sin falsificar procedencia; hay métricas y CI E2E; el PR queda listo para revisión humana. **No confundir entrega técnica con aprobación editorial de todo el corpus.**

## 7. Instrucción inmediata para el nuevo agente

> Trabaja en `uniscrolliabrain-cloud/agntia-iadev` desde Codespaces. Lee íntegramente este handoff C03 y el C01 existente. Primero recupera cualquier trabajo local o remoto de Cline, sin borrar ni sobrescribir nada, y establece baseline reproducible. Después ejecuta F1–F4 y los gates de C01, preservando fuente y fichas, corrigiendo los P0 de privacidad/autenticación antes de exposición. Publica implementación y reportes en rama con PR, sin merge ni despliegue. No te limites a documentar: implementa, prueba, corrige y registra evidencias. Si algo depende de credenciales o autorización, continúa el resto y documenta el bloqueo.
