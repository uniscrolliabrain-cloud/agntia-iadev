# Currículo IADEV, artifacts y aprendizaje verificable

## Fuente y planes de contenido
Tomar fichas IADEV versionadas y aprobadas editorialmente, no respuestas inventadas del LLM. Relacionar cada lección con `card_ids`, prerequisitos, objetivos, ejemplos, evaluación y fuentes. El corpus histórico tiene 1.440 fichas extraídas pendientes de revisión; C02 «Coding with AI» editorial vendor-neutral debe ser colección aparte, sin fingir que procede de la transcripción histórica. Diseñar 20 lecciones inicialmente, agrupadas en módulos, no limitar el producto a 20 de por vida.

## Estructura de lección
`lesson_id`, versión, título, objetivo observable, tarjetas aprobadas, requisitos previos, guion hablado, vídeo maestro, slots de personalización, lecturas, slides, artifacts, rúbrica, quiz, ejercicio práctico, Q&A SOP, estimación temporal, política de reintentos y criterios de finalización. El profesor puede proponer profundización sin alterar objetivos obligatorios.

## Ejercicios React
Componentes/artefactos interactivos compilados de forma controlada: prompt builder, clasificación de tareas, ordenación de pasos, diagrama de agentes, simulación de tool-calling, revisión de código, editor de JSON/schema, prueba de permisos, depuración de workflows. Soportar lectura y presentación combinadas con interacción. Cada artifact declara `artifact_id`, `artifact_version`, entradas, schema de resultados, validador determinista, rúbrica, hints, accesibilidad y modo offline si aplica.

## Seguridad del código de alumnos
NO ejecutar JS arbitrario en el mismo origen privilegiado. Sandboxing de previews/iframes con CSP, permisos mínimos, sin secretos ni tokens de backend, sin red por defecto, límites CPU/memoria/tiempo, sanitización y rate limiting. Para ejercicios que requieren ejecución de código real, usar sandbox aislado efímero con cuotas, nunca `eval` en el servidor principal. Valorar compilación previa de artifacts revisados en vez de compilación dinámica no confiable.

## Evaluación
Guardar intentos exactos y resultados estructurados: `attempt_id`, `lesson_id`, `artifact_version`, `score`, `mistake_codes`, `feedback`, `completed_at`. El LLM puede explicar y adaptar, pero la calificación crítica debe proceder de reglas y tests reproducibles. El Q&A usa resultados reales para profundizar y puede generar microejercicios; registrar resultados y trazabilidad.

## Calidad
Fichas con citas verificables; lecciones que no dependan de un proveedor; ejemplos de ingeniería reales, gradualidad, práctica activa, recuperación espaciada, criterios claros de dominio. Accesibilidad: subtítulos, transcripciones, teclado, alternativas al avatar y control de velocidad.
