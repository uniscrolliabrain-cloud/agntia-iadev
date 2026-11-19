"""Stable domain contracts. External payloads must be validated at API boundaries."""
from dataclasses import dataclass, asdict
from typing import Literal

@dataclass(frozen=True)
class SourceSpan:
    path: str
    sha256: str
    line_start: int
    line_end: int

@dataclass(frozen=True)
class Turn:
    id: str
    role: Literal["user", "assistant"]
    timestamp: str | None
    content: str
    source: SourceSpan

    def to_dict(self) -> dict:
        return asdict(self)

@dataclass(frozen=True)
class KnowledgeHit:
    id: str
    title: str
    text: str
    path: str
    line_start: int
    line_end: int
    score: float

    def to_dict(self) -> dict:
        return asdict(self)
