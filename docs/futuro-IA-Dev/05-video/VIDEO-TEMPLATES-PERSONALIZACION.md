# Vídeo maestro + microinserciones personalizadas

## Concepto
Cada lección usa vídeo maestro reutilizable de ~4–5 min. Puntos de inserción naturales, por ejemplo 00:45, 02:30, 04:20; en conjunto ~20 s de clips personalizados por lección (no 20 s cada uno salvo configuración explícita). Menciones del nombre, progreso, error concreto, último tema o próxima tarea. Evitar afirmar recuerdos no verificados. El objetivo es una experiencia personalizada a coste marginal reducido, no engañar sobre vídeo en directo.

## Template versionado
`video_template_id`, `lesson_version`, `master_asset_id`, `slots[{id, start_ms, max_duration_ms, transition_type, intent, fallback_asset_id}]`, `avatar_identity_id`, `wardrobe_id`, `voice_profile_id`, `audio_profile`, `captions_asset_id`, `license`. No colocar inserts en medio de palabras o frases; guion maestro redactado con transiciones de entrada/salida.

## Generación
Al abrir lección, cargar progreso estructurado con consentimiento; SOP produce `personalization_facts` auditables y plantillas lingüísticas. Slow-LLM propone redacción, validador de facts y límites de duración aprueba. Generar clip solo si personalización aporta valor; caché por alumno+versión lección+versión hechos+idioma+avatar; TTL e invalidación al cambiar progreso. Si no llega a tiempo, servir fallback neutro sin detener vídeo.

## Reproducción
Preferir playlist/manifest con segmentos maestro + insert y prebuffer sobre renderizar MP4 completo por alumno. Mantener un reloj único, sincronía AV, crossfades o cortes de cámara naturales, loudness uniforme, continuidad de vestuario, subtítulos por clip y captions concatenados. Opción render final bajo demanda y caché para replay; comprobar condiciones del proveedor para almacenar/reutilizar activos. No exponer URLs de alumnos a terceros; assets privados y URLs firmadas.

## Producción docente
El fundador graba narración con móvil y micro/audio adecuado, conserva oralidad y pausas. Pipeline de toma → selección → edición → transcripción → alineación → avatar/lip-sync → QA humano → publicación. Variar ropa por día/lección con avatar estable. Registrar revisiones y derecho de uso de voz/imagen. Diferenciar grabación humana original, síntesis, transformación de voz y generación de imagen: son pipelines distintos.

## Pruebas
20 inserciones sobre una lección piloto; tiempos de preparación, tasa de cache hit, errores de nombres, hechos inventados, audio clipping, saltos visuales, reproducción móvil Android, conectividad lenta, subtítulos y reproducción repetida.
