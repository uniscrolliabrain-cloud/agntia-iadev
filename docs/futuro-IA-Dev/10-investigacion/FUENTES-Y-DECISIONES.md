# Investigación de proveedores y decisiones pendientes (20-11-2026)

## Fuentes verificadas
- Anam pricing: https://anam.ai/pricing — API, planes, límites de sesión y minutos; cobra desde inicio de sesión hasta final, incluso en silencios. Free 30 min no comercial; Starter $12/mes, 50 min, overage $0.16/min, sesiones hasta 5 min; Explorer $49/mes, 250 min, overage $0.14/min, sesiones hasta 10 min. Verificar términos de grabación, generación de vídeo offline y redistribución antes de producción.
- ElevenLabs multi-context WebSocket: https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/multi-context-web-socket — contexto TTS, streaming, flush, barge-in, timeout y límite de contextos.
- ElevenLabs TTS API: https://elevenlabs.io/docs/api-reference/text-to-speech/v-1-text-to-speech-voice-id-multi-stream-input
- ElevenLabs TTS vs TTD: https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/tts-vs-ttd-websockets — modelos compatibles distintos según endpoint.

## No verificado aún: tareas explícitas de investigación
1. Anam: modo exacto audio passthrough, API/SDK, formatos PCM/Opus, streaming de audio externo, latency y lip sync, acceso por plan, términos de grabación/reutilización, API de generación de vídeo, avatars con vestuario variable. No darlo por certificado por un comentario de chat.
2. ElevenLabs: coste real de TTS en el modelo seleccionado, transformación speech-to-speech y preservación prosódica, licencia comercial y límites de concurrencia.
3. Vídeo: player HLS/DASH o playlist con inserts, crossfade, sincronía y almacenamiento privado; alternativas open-source FFmpeg, Remotion (comprobar licencia), MediaSource según navegador.
4. Artifacts: React sandbox y compilación aislada, paquetes autorizados, CSP, iframe origins, evaluación determinista, accesibilidad.
5. Datos: RLS multi-tenant, RGPD, base legal/consentimiento, retención de voz/transcripciones y normativa fiscal de formación.
6. Distribución: identificar exactamente los tres repos de distribución y sus licencias, contratos y deployment.

## Decisiones ADR propuestas
ADR-FUT-001: contenido global IADEV separado de memoria del alumno.
ADR-FUT-002: segmentación de turno de voz con context packs versionados.
ADR-FUT-003: vídeo maestro + microinserciones, fallback y caché.
ADR-FUT-004: evaluación determinista y tutor LLM explicativo.
ADR-FUT-005: interfaz de proveedores intercambiable y presupuestos fail-closed.
ADR-FUT-006: modo alumno y modo observador, métricas educativas y técnicas.
