"""Service boundary used by CLI, HTTP API and future agent tools."""
from pathlib import Path
from .catalog import curriculum_nodes
from .storage import search, get_turn
from .providers import make_context, LLMProvider, UnconfiguredProvider

class KnowledgeService:
    def __init__(self, db: Path, provider: LLMProvider | None = None):
        self.db = db
        self.provider = provider or UnconfiguredProvider()

    def tree(self) -> list[dict]:
        return [n.to_dict() for n in curriculum_nodes()]

    def search(self, query: str, limit: int = 10) -> list[dict]:
        return [hit.to_dict() for hit in search(self.db, query, limit)]

    def source(self, turn_id: str) -> dict | None:
        return get_turn(self.db, turn_id)

    def context(self, query: str, limit: int = 6) -> dict:
        ctx = make_context(query, self.search(query, limit))
        return {"query": ctx.query, "instructions": ctx.instructions, "passages": ctx.passages}

    def answer(self, query: str) -> str:
        ctx = make_context(query, self.search(query, 6))
        return self.provider.generate(ctx)
