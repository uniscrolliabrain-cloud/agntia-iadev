# Voz y avatar: ElevenLabs + Anam + kernel

## Modos
1. Voz de laboratorio en ChatGPT con 5–20 tarjetas precargadas para probar contenido sin APIs de voz propias: NO es retrieval automático por cada turno ni integración nativa persistente.
2. Pipeline propio texto Fast-LLM → ElevenLabs TTS → Anam avatar, controlado por kernel. Requiere confirmar modo concreto de ingestión de audio externo de Anam y compatibilidad de streaming/SDK en la cuenta.
3. Narración humana grabada → lip-sync/avatar para vídeos maestros, preferible si se busca conservar exactamente prosodia humana.
4. Audio transformado o TTS desde transcripción cuando haga falta voz diferente: la prosodia NO está garantizada, evaluar.

## Orquestación de un turno
`speechTurnId` con segmentos N; slow-LLM prefetch; Fast-LLM entrega texto incremental por frases; ElevenLabs WebSocket multicontexto TTS soporta varios contextos y flush; avatar consume audio externo si la integración específica lo permite; reproductor mantiene una intervención única. Separar `audio_generated`, `audio_played` y `avatar_rendered`; orden/ack por `segment_id`; sincronización AV y jitter buffer. Hacer cancelación de audio buffered y generación futura ante barge-in. Timeout y fallback a voz sin avatar o texto.

## Restricciones reales de proveedor
Documentación ElevenLabs confirma endpoint TTS multi-stream `/v1/text-to-speech/{voice_id}/multi-stream-input`, contextos independientes, `flush`, `close_context`, y recomendación de frases completas. No confundir con los modelos Eleven v3/v4: compatibilidad de endpoint depende de la familia. Referencias en `10-investigacion`.
Anam publica API y planes con límites de sesiones y duración; verificar técnicamente audio passthrough en SDK y condiciones de vídeo pregenerado, captura, comercialización, marca de agua y reutilización antes de prometer flujo. **Una pausa de 3 s con sesión Anam abierta puede seguir facturándose**; el precio depende del tiempo de sesión, no solo de la voz activa.

## Identidad y expresión
Avatar docente consistente (cara, iluminación, encuadre, identidad), variación de ropa por lección, sincronía labial y expresiones; vestuario/escena versionados. El fundador puede prestar su voz y estilo, siempre con consentimiento y licencias adecuadas. No afirmar que la sincronización será perfecta sin prueba. Audio limpio, control de ruido, loudness y pronunciación técnica. Subtítulos alineados.

## Prueba de 60 segundos
Una intervención explicando tres conceptos con dos cambios de tarjetas. Variantes A: fijo; B: segmentado; C: prefetch; D: avatar. Medir pausas audibles, interrupciones, coherencia semántica, lag audio-vídeo, latencia y coste. Gates de integración: demostración de audio externo y de cancelación; si falla, usar audio/avatar generado offline o voz sin vídeo.
