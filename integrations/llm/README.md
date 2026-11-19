# Adaptadores de proveedores LLM (stub)

Implementar la interfaz `LLMProvider.generate(GroundedContext)` de `src/iadev/providers.py`. No hardcodear claves ni hacer llamadas sin configuración explícita. Añadir timeouts, retries, rate limiting, trazas y tests mockeados antes de habilitar `/v1/answer`.

Proveedor predeterminado: `UnconfiguredProvider`, que falla cerrado.
