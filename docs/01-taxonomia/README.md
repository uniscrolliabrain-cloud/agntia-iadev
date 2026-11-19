# Taxonomía inferida de los prompts del autor — v1

## Principio rector

**La taxonomía se deriva primero de las peticiones y correcciones del usuario en la transcripción, no de una clasificación informática genérica ni únicamente de los títulos redactados por el asistente.** Las respuestas se utilizan como contenido didáctico que debe enlazarse con esas intenciones. La estructura siguiente es una **primera inferencia documentada**, no la taxonomía definitiva ni una auditoría de dominio del usuario.

Fuente canónica: `ChatGPT-Auditar aprendizaje en repositorios-20261119-1135.md`. No alterar el original. En el export aparecen encabezados `## Prompt:` dentro de mensajes del propio usuario; no contar esos marcadores incrustados como turnos nuevos sin verificar contexto.

## Ejes de taxonomía inferidos de prompts sustantivos

| Código | Dominio de intención | Contenido / subdominios | Evidencia en prompts |
| --- | --- | --- | --- |
| T01 | Aprendizaje autobiográfico y auditoría de capacidades | Desde cero; 15 repositorios; inventario; evidencia; niveles de comprensión; cronología | Prompt inicial 18-11 12:38 |
| T02 | Pedagogía radical para principiantes | Qué es software; explicar jerga; analogías; curso accesible; manual previo | 18-11 12:41; 17:15 |
| T03 | Metodología propia de ingeniería | Campañas; fases; audits; diagnósticos; reportes; fixes; hunks; multipatches; bugs | 18-11 13:55; 13:59 |
| T04 | Operación asíncrona con agentes de coding | GPT+humano diseñan; Freebuff ejecuta; Cline testea; Codex revisa e integra; bitácoras; IDs | 18-11 17:25 |
| T05 | Escala, squads y medición del trabajo | 14 repos en paralelo; 3 squads/repo; jornadas equivalentes humanas; cargos y funciones; distinguir algoritmo de agente | 18-11 17:25; 17:34 |
| T06 | Herramientas, stack y proveedores reales | Lenguajes; librerías; CLIs; Linux; PowerShell; GitHub; Doppler; Repomix; proveedores y modelos | 18-11 14:54; 17:25 |
| T07 | Alfabetización de repositorios y archivos | DOM; extensiones; .gitignore; README; folders lógicos; anatomía de código | 18-11 17:40 |
| T08 | Aprendizaje práctico por clonación | Repos públicos; replicar y personalizar; ejercicios con IA; comprobar funcionamiento | 18-11 17:36 |
| T09 | Desarrollo híbrido no-code/low-code + coding | Generación inicial con Lovable; exportar a GitHub; agentes completan; Claude Code skills | 18-11 17:59; 18:00 |
| T10 | Open source aplicado a negocios | Repos plug-and-play; adaptación; agentificación; modelos disponibles; lanzamiento práctico | 18-11 18:31; 18:32 |
| T11 | Monetización y modelos de negocio | Comercialización del conocimiento y del software; oportunidades de monetización | 18-11 18:01 |
| T12 | Publicación, comunidad y narrativa | Challenge de 30 días; ordenar todo el contenido; comunidad desde cero; keywords y explicación | 18-11 18:33; 20:11; 21:18; 21:20 |
| T13 | Pensamiento sistémico y arquitectónico | Sistemas; modelos; patrones; diseño; decisiones; liderazgo; organización | 18-11 22:41 |
| T14 | Metacognición y razonamiento | Transcognición; metacognición; axiomas; deducción; primeros principios; pensamiento crítico, convergente y divergente | 18-11 22:41 |
| T15 | Diseño editorial y progresión del curso | 40 categorías × 3 subcategorías × 10 conceptos; después 30 días × 40 keywords y bonus 7 días; un turno por día | 18-11 12:38; 21:19; 22:43 |
| T16 | Confidencialidad y publicación | No revelar repos privados en material educativo; usar ejemplos ficticios; conservar trazabilidad interna separada | 18-11 13:57 |
| T17 | Conversión a base de conocimiento | Export literal; fichas RAG; metadatos; organización de carpetas; integridad y procedencia | 19-11 11:24 |

**Nota:** los nombres T01–T17 son etiquetas inferidas por el asistente, no términos que el usuario haya declarado como categorías definitivas. No afirmar que son exhaustivas antes de analizar todas las respuestas y las correcciones cruzadas.

## Dimensiones transversales obligatorias

- **Intención:** aprender, investigar, auditar, diseñar, implementar, testear, revisar, publicar, monetizar.
- **Nivel:** principiante, intermedio, avanzado; no confundir explicación recibida con habilidad demostrada.
- **Tipo de conocimiento:** concepto, herramienta, técnica, proceso, rol, patrón, decisión, ejercicio, ejemplo, evidencia.
- **Ciclo operativo:** diagnóstico → campaña → fase → tarea → patch/hunk → test → reporte → review → integración → retrospectiva.
- **Evidencia:** afirmación del chat, documentación, código, test ejecutado, auditoría; no elevar automáticamente niveles.
- **Público:** uso interno o divulgación pública; ejemplos internos deben anonimizarse antes de publicación.
- **Relación pedagógica:** prerrequisito, ejemplo_de, aplica_a, contrasta_con, parte_de, deriva_de.
- **Procedencia:** mensaje, fecha, línea inicial/final, hash de fuente, extracto literal, interpretación separada.

## Reglas de prioridad para agentes taxonomizadores

1. Extraer **todos los prompts sustantivos** y correcciones, en orden cronológico, conservando texto literal.
2. Detectar la evolución de las instrucciones: las correcciones posteriores del usuario prevalecen sobre decisiones editoriales previas incompatibles.
3. Separar **metodología personal**, **temario técnico**, **formato didáctico** y **canales de distribución**. No aplanarlos en una sola lista.
4. Construir un mapa de `prompt_id → intención → decisiones editoriales → respuestas afectadas → fichas derivadas`.
5. Extraer la terminología del autor con variantes y sinónimos; no normalizar de forma que se pierdan términos como *hunks*, *multipatches*, *audits* o *squads*.
6. No atribuir al usuario afirmaciones introducidas únicamente por el asistente.
7. Mantener dos índices: **curricular** (secuencia de días/conceptos) y **semántico** (dominios e intenciones, con clasificación múltiple).
8. Registrar gaps, duplicados y contradicciones. No inventar conceptos para cuadrar cifras.
9. Preparar un corpus público con ejemplos inventados y otro de procedencia interna, sujetos a revisión de privacidad.
10. Antes de procesar masivamente, entregar una muestra auditada de 20 fichas que cubra tanto conceptos técnicos como método de trabajo y pensamiento sistémico.

## Esquema mínimo de ficha

```yaml
id: "rag-000001"
titulo: ""
tipo: "concepto"
concepto_numero: null
dia: null
dominios: ["T03"]
intenciones: ["aprender", "aplicar"]
tags: []
terminos_autor: []
prerrequisitos: []
relacionados: []
fuente_path: "ChatGPT-Auditar aprendizaje en repositorios-20261119-1135.md"
fuente_linea_inicio: null
fuente_linea_fin: null
fuente_sha: "dbd5d1f28a82ee8f6e46ebbec1b060a183f7d220"
prompt_origen_ids: []
respuesta_origen_ids: []
estado_evidencia: "fuente_conversacion"
publicabilidad: "pendiente_revision"
revision_humana: false
version_esquema: 1
```

## Entregables siguientes

`data/manifests/prompts.jsonl`, `data/manifests/turnos.jsonl`, `docs/01-taxonomia/terminologia-autor.yaml`, `docs/01-taxonomia/mapa-intenciones.md`, `knowledge/conceptos/`, `docs/03-auditorias/cobertura.md`.

**Gate:** cada dominio debe enlazar a prompts originales verificables. Ninguna ficha se considera trazable sin rango de fuente válido.
