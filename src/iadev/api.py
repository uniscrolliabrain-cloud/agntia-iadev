"""Optional FastAPI app. Install: pip install -e '.[api]'."""
import os
from pathlib import Path
from .service import KnowledgeService

def create_app(db: Path | None = None):
    try:
        from fastapi import FastAPI, HTTPException, Query
            except ImportError as exc:
        raise RuntimeError("Install optional API dependencies: pip install -e '.[api]'") from exc
    app = FastAPI(title="Agntia IA Dev Knowledge API", version="0.1.0")
    service = KnowledgeService(db or Path(os.getenv("IADEV_DB", "data/indexes/knowledge.sqlite")))

    @app.get("/health")
    def health():
        return {"status": "ok", "llm_configured": False}

    @app.get("/v1/curriculum")
    def curriculum():
        return {"nodes": service.tree()}

    @app.get("/v1/search")
    def search(query: str = Query(min_length=1), limit: int = Query(default=10, ge=1, le=50)):
        return {"hits": service.search(query, limit)}

    @app.get("/v1/sources/{turn_id}")
    def source(turn_id: str):
        result = service.source(turn_id)
        if result is None:
            raise HTTPException(status_code=404, detail="Source not found")
        return result

    @app.post("/v1/context")
    def context(req: dict):
        query = req.get("query", "")
        if not isinstance(query, str) or not query.strip():
            raise HTTPException(status_code=422, detail="query must be a nonempty string")
        return service.context(query)

    @app.post("/v1/answer")
    def answer(req: dict):
        raise HTTPException(status_code=501, detail="LLM provider not wired yet")

    return app

# For uvicorn: uvicorn iadev.api:app
try:
    app = create_app()
except RuntimeError:
    app = None
