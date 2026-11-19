# @agntia/iadev — SDK TypeScript (alpha)

Adaptación del patrón server-only de `agntia-ciberseguridad/typescript` al motor educativo. No se copian rutas de auditoría ni tokens delegados: las operaciones de conocimiento son lecturas.

## Uso previsto desde agente

```ts
import { KnowledgeClient } from "@agntia/iadev";
const client = new KnowledgeClient({
  baseUrl: process.env.IADEV_BASE_URL!,
  approvedOrigins: [new URL(process.env.IADEV_BASE_URL!).origin],
  credential: async () => process.env.IADEV_SERVICE_TOKEN!,
});
const result = await client.search({query:"pensamiento sistémico",limit:5});
```

La credencial debe venir de un secreto de servidor. El host debe autenticar sesión, autorizar `knowledge.read` y aplicar límites por tenant/actor antes de crear el cliente. Nunca confiar en IDs o credenciales enviados por el navegador.

## Contrato actual

Implementado en el scaffold Python: `GET /health`, `GET /v1/curriculum`, `GET /v1/search?query=&limit=`, `GET /v1/sources/{turn_id}`, `POST /v1/context`.

**Bloqueo de integración:** la API Python actual no valida todavía el bearer token. El SDK sí lo envía, pero eso NO constituye autenticación del servicio. Implementar verificación de credenciales/JWT con audiencia y scopes antes de exponer el servicio. No habilitar el proxy Hono a usuarios finales hasta entonces.

No se han implementado todavía fichas individuales, grafo, ejercicios, progreso ni búsqueda vectorial. No afirmar que las capacidades futuras están operativas.

## Validación

`cd typescript && npm install && npm test`. No se ha ejecutado esta suite en GitHub todavía. Los tests usan un fetch simulado y no prueban un servidor Python real.
