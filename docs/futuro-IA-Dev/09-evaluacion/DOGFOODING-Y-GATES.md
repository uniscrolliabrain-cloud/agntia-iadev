# Plan de pruebas, dogfooding y calidad

## Laboratorio sin coste externo
Seleccionar 5, 10 o 20 tarjetas reales de IADEV, precargarlas en conversación ChatGPT, usar modo voz y comprobar fidelidad. No equivale a integración en tiempo real de API IADEV. Preguntas con respuesta, preguntas fuera de corpus, contraejemplos, recuperación de prerequisitos y explicación progresiva.

## Laboratorio voz/avatar
Prueba A: contexto fijo; B: segmentado; C: prefetch slow; D: avatar sincronizado. Mismo tema, tres conceptos, ~60 s, dos cambios de tarjetas. Medir latencia de primera voz, pausa entre segmentos, interrupción, lip sync, repeticiones, contradicciones, tasa de citas correctas, coste y cancelación. Criterios iniciales a calibrar: cero fugas de datos, cero tarjetas sin fuente tratadas como verificadas, cero sesiones sin hard cap, cero clips con hechos inventados. Registrar mediciones reales, no números inventados.

## Dogfooding fundador
Completar como alumno real 20 lecciones sin soporte manual: abrir, ver vídeo, hacer artifact, recibir nota, Q&A, cerrar, volver después de días, comprobar saludo contextual, historial y siguiente lección. Después entrar en modo observador técnico para inspeccionar eventos, context packs, gastos y errores. Mantener separación de modos: no contaminar experiencia del alumno con debug.

## Pruebas de resiliencia
Pérdida de conexión, doble click, repetición de intento, alumno interrumpe, latencia TTS, Anam caído, clips sin generar, audio truncado, tarjetas retiradas, fallo del slow-LLM, gasto máximo, usuario sin matrícula, revocación de permiso, borrado de datos, múltiples alumnos simultáneos. Fallar cerrado en permisos y degradar con gracia en multimedia.

## Evidencias y gates
Cada campaña reporta SHA, test output, screenshots/samples autorizadas, costes reales, cobertura, latencias p50/p95, resultados educativos y pendientes. Gate final: contenido pedagógico satisfactorio, experiencia natural, memoria fiel, privacidad, facturación controlada y aprobación del fundador. No confundir «funciona en demo» con «listo para vender».
