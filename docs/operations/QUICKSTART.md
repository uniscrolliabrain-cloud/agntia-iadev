# Quickstart local

Requiere Python 3.11+ y SQLite con FTS5.

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e '.[dev,api]'
iadev audit "ChatGPT-Auditar aprendizaje en repositorios-20261119-1135.md"
iadev ingest "ChatGPT-Auditar aprendizaje en repositorios-20261119-1135.md"
iadev tree
iadev search "pensamiento sistémico"
iadev context "¿Qué es un agente de programación?"
pytest -q
uvicorn iadev.api:app --host 127.0.0.1 --port 8000
```

Probar `GET http://127.0.0.1:8000/v1/curriculum` y `GET /v1/search?query=GitHub`.

**No desplegar** esta API sin autenticación, separación de corpus público/privado, límites, sanitización y revisión de seguridad. El endpoint `/v1/answer` devuelve 501 intencionalmente.
