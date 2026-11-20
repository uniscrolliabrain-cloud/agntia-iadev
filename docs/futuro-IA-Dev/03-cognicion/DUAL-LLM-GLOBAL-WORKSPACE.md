# Arquitectura cognitiva: dos LLM y contexto RAG vivo

## Separación funcional
Slow-LLM + JEV: interpretación de intención, atención, selección y anticipación de fichas, estimación de dificultad y siguiente concepto. Kernel determinista: PDP, presupuestos, snapshots, verificación de procedencia, filtro de privacidad, autorización, versionado y publicación de contexto. Fast-LLM: interfaz conversacional de baja latencia, con acceso SOLO al contexto aprobado; no decide permisos ni ejecuta acciones fuera de SOP. IADEV: conocimiento global versionado. Memoria alumno: estado privado, no corpus editorial. El Global Workspace es una metáfora de diseño operacional, no una afirmación de consciencia.

## Context pack
`context_pack_id`, `version`, `speech_turn_id`, `segment_id`, `lesson_id`, `student_id` pseudonimizado, `card_refs[]` (id/version/hash/score/source), `learning_state_ref`, `continuity_summary`, `token_budget`, `issued_at`, `expires_at`, `policy_decision_id`. Nunca introducir datos privados de otro alumno.

## Ciclo de atención
`candidate → retrieved → validated → active → displaced → archived`. Estrategia: top-k inicial 5–20 fichas; selección híbrida lexical/semántica + grafo de prerequisitos; diversidad, novedad y penalización de redundancia; snapshots de tarjetas activas; retiradas no destruyen el resumen de lo ya dicho. Ponderar confianza y procedencia; el kernel puede decidir `NO_CHANGE`.

## Cambio de tarjetas durante una intervención de voz
El fast-LLM no admite cambiar arbitrariamente su prompt dentro de una generación ya iniciada. Dividir una intervención en segmentos cortos de frases completas, cada segmento es una nueva generación con context pack actualizado. Conservar `speech_turn_id` durante los segmentos, emitir `turn.completed` solo al final. Tipos de pausa: prosódica (solo audio), semántica (posible actualización), cognitiva (espera información). Hipótesis inicial 8–15 s por segmento; medir y ajustar. No introducir pausas artificiales si el conocimiento no cambia.

## Prefetch anticipatorio
Mientras se reproduce audio de segmento N, slow-LLM calcula candidatos para N+1; kernel valida, fast-LLM genera N+1, TTS lo prepara, reproductor ordena sin solapamientos. Si predicción falla, mantener contexto anterior y continuar; no bloquear el audio ni inventar tarjeta. Detectar interrupción del alumno y cancelar generación/audio pendientes; nueva intención y nuevo turno con causalidad. Si alumno habla, prioridad a barge-in y VAD/STT; no confundir pausa de TTS con cesión de turno.

## Observabilidad
Eventos append-only `context.candidates_proposed`, `context.pack_approved`, `speech.segment_started`, `speech.segment_finished`, `speech.turn_completed`, `speech.interrupted`, `cards.prefetch_hit`, `cards.prefetch_miss`. Medir latencia p50/p95, continuidad, cobertura, alucinación, precisión de anticipación, costo tokens, token budget y satisfacción. Comparar A/B contexto fijo, segmentado, anticipatorio. No atribuir capacidades ya implementadas al repositorio actual.
