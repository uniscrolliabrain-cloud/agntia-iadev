# Contratos de herramientas para agentes

| Tool | Input | Output | Estado |
| --- | --- | --- | --- |
| `curriculum.tree` | ninguno | nodos `id,label,parent_id,path,kind` | implementado |
| `knowledge.search` | `query,limit` | hits `id,title,text,path,line_start,line_end,score` | implementado, FTS5 |
| `knowledge.source` | `turn_id` | turno original con rol, timestamp, SHA y líneas | implementado |
| `knowledge.context` | `query` | pasajes y reglas de grounding | implementado |
| `knowledge.answer` | `query` | respuesta citada | **501 / stub** |
| `knowledge.concept` | `concept_id` | ficha y evidencias | pendiente |
| `knowledge.neighbors` | `concept_id,relation_types,depth` | grafo validado | pendiente |
| `knowledge.learning_path` | `goal,level` | secuencia curricular | pendiente |

Las rutas HTTP son `GET /v1/curriculum`, `GET /v1/search`, `GET /v1/sources/{turn_id}`, `POST /v1/context`, `POST /v1/answer`.

No llamar al endpoint `answer` hasta configurar un proveedor y pasar evaluaciones de grounding.
