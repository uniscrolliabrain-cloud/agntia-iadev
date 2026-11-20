# Arquitectura técnica y campañas de implementación

## Fronteras de repos
`agntia-iadev`: cards, grafo, catálogo de lecciones, fuentes, evaluación de retrieval, contratos públicos del conocimiento. `agente`: kernel, JEV/slow-LLM, fast-LLM, SOPs, memoria privada, seguridad, eventos, runtime voz, tenants. Repos de distribución/UI: descubrir los tres repos reales, no inventarlos; frontend React de curso, artifacts, player y billing pueden residir allí según auditoría. Integración por SDK/HTTP/contratos versionados; no importar archivos internos de otros repos. Esta rama contiene SOLO documentación, no cambiar `agente` sin autorización.

## Árbol de código PROPUESTO (no existente)
`src/iadev/curriculum/`: schemas, lesson catalog, card linking, prerequisites.
`src/iadev/retrieval/`: card index, graph, rerank, context pack suggestions.
`typescript/src/contracts/course.ts`, `lesson.ts`, `artifact.ts`, `tutor.ts`, `media.ts`.
`docs/futuro-IA-Dev/`: specs y evidencias.
En repo host: `engine/learning/`, `engine/context-packs/`, `engine/speech-turns/`, `engine/media/`, `engine/student-memory/` (rutas tentativas: auditar árbol real antes de crear). Frontend: `CoursePlayer`, `InteractiveArtifact`, `TutorVideoSession`, `ProgressDashboard`, `LessonResume`.

## Campañas ejecutables, 1 rama por campaña, PR y gates
**FUT-00 Baseline y dependencias.** Auditar main/ramas/worktrees de IADEV, agente y tres repos de distribución; inventario APIs/secretos/proveedores; ADR fronteras; no inventar rutas. Entrega `reports/FUT-00/{baseline,dependencies,risks}.md`. Gate: SHA, comandos y tests reproducibles.

**FUT-01 Contratos y modelo curricular.** JSON Schema/Zod/Pydantic para Course/Module/Lesson/KnowledgeCardRef/Artifact/Attempt/Checkpoint, migrations propuestas, OpenAPI, versión de curriculum. Tests fixtures y compatibilidad. Gate: TS/Python parity y golden fixtures.

**FUT-02 Cards y recuperación.** C01/C02 revisadas, indexar cards aprobadas, prerequisitos, vecinos, provenance, context pack, ranker y evaluación; abstención ante falta de fuente. Gate: retrieval tests y no fuga de datos.

**FUT-03 Motor de ejercicios React.** Renderer sandbox, librería artifacts, validación determinista, persistencia intentos, accesibilidad, mobile. Gate: ejercicio end-to-end sin JS privilegiado.

**FUT-04 Pipeline de autoría y vídeos maestros.** Ingesta audio humano, transcripción/alineación, avatar, vestuario, subtítulos, assets, revisión editorial, versionado y almacenamiento. Gate: lección 5 min publicada con QA visual y licencias.

**FUT-05 Personalización audiovisual.** Templates, slots, facts verificables, generación clip, cache/invalidation, manifest player, fallback. Gate: 3 inserts sin nombres/recuerdos falsos, continuidad AV.

**FUT-06 Tutor en directo.** Fast-LLM + ElevenLabs + Anam adapter; STT/VAD, streaming, cancel, backpressure, audio passthrough (validar compatibilidad); modo solo texto/voz fallback. Gate: 3 min Q&A con barge-in y control de gasto.

**FUT-07 Global Workspace y tarjetas dinámicas.** JEV/slow-LLM propone; kernel autoriza; segmentación con `speechTurnId`, prefetch, context pack snapshots, A/B fixed/segmented/predictive. Gate: turno continuo con dos cambios de tarjetas y sin pérdida de continuidad.

**FUT-08 Memoria y SOP educativas.** Enrollment, authz, student progress, consent, RLS, resume, evaluación, personalización, privacidad. Gate: Juan retoma tras 3 días con hechos correctos, otro alumno no puede acceder a sus datos.

**FUT-09 Experiencia curso y distribución.** Player, ejercicios, slides, lecturas, tutor, progreso, pagos, acceso, demo, responsive y observabilidad. Gate: flujo completo lección 1→20 en staging.

**FUT-10 Evaluación, costes y dogfooding.** Métricas, replay, QA audiovisual, pruebas E2E, presupuesto, security, accessibility, founder as student, reporte. Gate: decisión explícita go/no-go y aprobación antes de merge/deploy.

## Secuencia de entrega
Primero vertical slice 1 lección (FUT-00,01,03,04,06,08 mínimos), después inserts y segmentación; luego currículo completo. Piezas de una semana cuando sea posible; no crear 20 vídeos antes de validar un template. PRs independientes, tests y docs, sin merge automático.

## Contrato de ejecución del agente
Leer C03/C01; inspeccionar código real; no asumir endpoints/SDK listos; reportar `implemented/tested/not_tested/blocked`; commits en ramas de campaña, no `main`; no desplegar, no gastar APIs ni modificar repo padre sin aprobación; guardar evidencias y costes por campaña.
