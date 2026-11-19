# Taxonomía y esquema de conocimiento

Dos índices separados:

1. **Curricular:** orden pedagógico de 37 días y hasta 1.480 conceptos, sujeto a comprobación contra la fuente.
2. **Temático:** jerarquía de dominios, categorías, subcategorías y etiquetas; admite pertenencia múltiple.

No asumir que los 1.480 conceptos están todos explícitamente desarrollados sin un inventario verificable.

Cada ficha propuesta debe tener frontmatter YAML con: `id`, `titulo`, `tipo`, `concepto_numero` (opcional), `dia` (opcional), `dominios`, `tags`, `prerrequisitos`, `relacionados`, `fuente_path`, `fuente_linea_inicio`, `fuente_linea_fin`, `fuente_sha`, `estado_evidencia`, `revision_humana`, `version_esquema`.

Estados de evidencia: `fuente_conversacion`, `documentado_repo`, `implementado_codigo`, `verificado_tests`. No equiparar afirmaciones del chat con pruebas de implementación.
