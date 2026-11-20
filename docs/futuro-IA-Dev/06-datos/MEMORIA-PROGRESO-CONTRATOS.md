# Estado del alumno, memoria y contratos

## Modelo conceptual
`Course`, `Module`, `Lesson`, `KnowledgeCardRef`, `MediaTemplate`, `PersonalizationSlot`, `ArtifactDefinition`, `ExerciseAttempt`, `AssessmentResult`, `LearningCheckpoint`, `TutorSession`, `ContextPack`, `SpeechTurn`, `SpeechSegment`, `SOPExecution`, `Consent`, `CostLedgerEntry`, `AuditEvent`. Cada entidad versionada, con IDs opacos, timestamps, tenant scope, actor scope y trazabilidad.

## Persistencia exacta vs RAG
SQL/Postgres como verdad para matrículas, progreso, puntuaciones, lección actual, intentos, duración, compras, consentimiento y gasto. Memoria RAG privada solo para resúmenes semánticos de preferencias/dificultades e interacciones relevantes, vinculados a evidencias. IADEV mantiene tarjetas editoriales globales; no indexar automáticamente datos privados de alumnos en el corpus común. Aislamiento por tenant/student, RLS/PDP, minimización, retención, borrado/exportación y GDPR.

## SOP del profesor
`start_lesson`: verificar acceso, resolver checkpoint, cargar tarjetas aprobadas, generar saludo basado en facts. `present_video`: resolver template y clips. `evaluate_exercise`: validador determinista y rúbrica, guardar intento. `start_tutor`: límite de tiempo y gasto, tarjetas de lección, errores reales y objetivos. `resume_course`: reintroducción contextual. `finish_lesson`: checkpoint y próxima lección. `handle_barge_in`: cancelar TTS/segmentos y reasignar turno. El LLM propone contenido, el kernel autoriza acciones.

## Seguridad
Roles owner/autor/alumno/tutor/operador; authn/authz; no confiar en `student_id` enviado por cliente; validar enrolment server-side. Secrets solo servidor, scopes mínimos y rotación; evitar PII en logs de voz, prompts y eventos; consentimiento específico para voz, transcripción y analítica; retención y borrado. Prompt injection desde tarjetas, ejercicios y respuestas: tratar como datos no confiables. Control de reintentos, cuotas, idempotencia, circuit breakers y dead-letter.

## API propuesta (versionar)
`GET /v1/courses/:id`; `POST /v1/lessons/:id/start`; `GET /v1/lessons/:id/playlist`; `POST /v1/attempts`; `GET /v1/progress`; `POST /v1/tutor-sessions`; `POST /v1/tutor-sessions/:id/interrupt`; `POST /v1/tutor-sessions/:id/finish`; `GET /v1/learning-events` (privado). Contratos TS Zod + Python Pydantic/JSON Schema, OpenAPI, tests cruzados. API de conocimiento IADEV y API privada de aprendizaje pueden residir en repos distintos; NO mezclar credenciales ni responsabilidades.
