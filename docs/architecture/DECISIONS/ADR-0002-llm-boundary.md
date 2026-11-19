# ADR-0002: motor determinista y proveedor LLM intercambiable

Estado: aceptado para scaffolding.

Decisión: separar navegación, búsqueda, verificación y permisos del proveedor generativo. El proveedor solo recibe pasajes recuperados con trazabilidad y reglas de citación. No se configura proveedor por defecto.

Consecuencia: el servicio es útil sin IA y permite cambiar de modelo sin alterar el corpus ni sus IDs.
