# FUTURO IADEV — Academia audiovisual agéntica personalizada
Estado: visión y plan, NO implementación. Rama: `IA-Dev-futuro-curso`. Fecha 2026-11-20.

## Propósito
Convertir IADEV —biblioteca educativa RAG de ingeniería, coding with AI, vibe coding, pensamiento sistémico y arquitectura de sistemas— en una academia propia desplegada sobre la plataforma del fundador. El producto es una experiencia completa de vídeos con avatar, artefactos React interactivos, lecturas, presentaciones, ejercicios, evaluación y tutoría audiovisual individual con memoria longitudinal. El fundador es autor, docente, ingeniero, primer alumno y responsable de QA. No depender de Udemy para la experiencia; Udemy es una posible referencia comercial, no un requisito técnico. La existencia de competencia no constituye un veto de producto.

## Documentación por dominios
- [01-visión/PRODUCTO-Y-EXPERIENCIA.md](01-vision/PRODUCTO-Y-EXPERIENCIA.md): relato íntegro, experiencia, currículo, docencia y dogfooding.
- [02-pedagogia/CURRICULO-Y-EJERCICIOS.md](02-pedagogia/CURRICULO-Y-EJERCICIOS.md): fichas, módulos, artifacts, evaluación.
- [03-cognicion/DUAL-LLM-GLOBAL-WORKSPACE.md](03-cognicion/DUAL-LLM-GLOBAL-WORKSPACE.md): JEV, fast/slow, selección dinámica de tarjetas.
- [04-voz-avatar/VOICE-AVATAR-PIPELINE.md](04-voz-avatar/VOICE-AVATAR-PIPELINE.md): ElevenLabs, Anam, pausas, avatar, voz y autoría.
- [05-video/VIDEO-TEMPLATES-PERSONALIZACION.md](05-video/VIDEO-TEMPLATES-PERSONALIZACION.md): vídeo maestro, inserts, render y continuidad.
- [06-datos/MEMORIA-PROGRESO-CONTRATOS.md](06-datos/MEMORIA-PROGRESO-CONTRATOS.md): datos, contratos, seguridad, SOP.
- [07-negocio/ECONOMIA-Y-DISTRIBUCION.md](07-negocio/ECONOMIA-Y-DISTRIBUCION.md): precios, hipótesis y costes.
- [08-ingenieria/ARQUITECTURA-Y-CAMPANAS.md](08-ingenieria/ARQUITECTURA-Y-CAMPANAS.md): especificaciones y campañas de código.
- [09-evaluacion/DOGFOODING-Y-GATES.md](09-evaluacion/DOGFOODING-Y-GATES.md): métricas, experimentos, criterios de aceptación.
- [10-investigacion/FUENTES-Y-DECISIONES.md](10-investigacion/FUENTES-Y-DECISIONES.md): documentación externa y cuestiones abiertas.
- [HANDOFF-AGENTE.md](HANDOFF-AGENTE.md): instrucciones para el próximo agente.

## Contexto del repositorio existente
Leer primero `docs/handoffs/HANDOFF-C03-AUDIT-RECOVERY-CLINE-2026-11-20.md` y `docs/campaigns/C01-CLINE-RAG-FOUR-PHASES/HANDOFF-MAESTRO.md`. IADEV cuenta con 1.440 fichas extraídas (1.160 core, 280 bonus), con 40 huecos 1161–1200 sin fuente individual; no confundir `source_extracted` con revisión editorial aprobada. Python FastAPI/SQLite FTS5 y SDK TS son un scaffold, no un RAG híbrido terminado. C01 y ampliación Coding with AI C02 son dependencias, no se deben bloquear ni reescribir desde esta rama. Mantener conocimiento global separado de memoria privada de alumnos.

## Principios
1. Vídeo maestro reutilizable; solo se personalizan inserts cortos y tutoría.
2. El profesor audiovisual reproduce el estilo oral humano del fundador, no un guion genérico redactado por IA.
3. Slow-LLM/JEV proponen tarjetas; kernel valida y dispone; fast-LLM habla.
4. Memoria y progreso persistentes, tipados y aislados por alumno/tenant; RAG semántico no sustituye registros exactos.
5. Voz segmentada dentro de un mismo turno con posibilidad de interrupción del alumno.
6. El alumno puede cursar toda la formación sin necesitar intervención manual del fundador.
7. Contratos versionados, permisos deny-by-default, observabilidad y límites de gasto.
8. Documentación de FUTURO: no declarar implementadas capacidades aún no verificadas.
