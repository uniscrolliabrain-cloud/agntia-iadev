"""SQLite FTS5 lexical index, deterministic and offline by default."""
import json
import sqlite3
from pathlib import Path
from .models import Turn, KnowledgeHit

DDL = """
CREATE TABLE IF NOT EXISTS turns (
 id TEXT PRIMARY KEY, role TEXT NOT NULL, timestamp TEXT,
 content TEXT NOT NULL, source_path TEXT NOT NULL, source_sha256 TEXT NOT NULL,
 line_start INTEGER NOT NULL, line_end INTEGER NOT NULL
);
CREATE VIRTUAL TABLE IF NOT EXISTS turns_fts USING fts5(id UNINDEXED, content, tokenize='unicode61');
CREATE TABLE IF NOT EXISTS metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL);
"""

def connect(db: Path) -> sqlite3.Connection:
    db.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db))
    conn.row_factory = sqlite3.Row
    conn.executescript(DDL)
    return conn

def replace_turns(db: Path, turns: list[Turn]) -> int:
    with connect(db) as conn:
        conn.execute("DELETE FROM turns")
        conn.execute("DELETE FROM turns_fts")
        for t in turns:
            conn.execute("INSERT INTO turns VALUES (?,?,?,?,?,?,?,?)",
                         (t.id, t.role, t.timestamp, t.content, t.source.path,
                          t.source.sha256, t.source.line_start, t.source.line_end))
            conn.execute("INSERT INTO turns_fts(id,content) VALUES (?,?)", (t.id, t.content))
        conn.execute("INSERT OR REPLACE INTO metadata VALUES (?,?)", ("turn_count", str(len(turns))))
    return len(turns)

def search(db: Path, query: str, limit: int = 10) -> list[KnowledgeHit]:
    if not query.strip():
        return []
    limit = max(1, min(limit, 50))
    # Use quoted tokens to avoid FTS operator injection and syntax errors.
    import re
    tokens = re.findall(r"[^\W_]+", query, flags=re.UNICODE)
    if not tokens:
        return []
    expression = " OR ".join('"' + tok.replace('"', '""') + '"' for tok in tokens[:12])
    with connect(db) as conn:
        rows = conn.execute("""
          SELECT t.*, bm25(turns_fts) AS rank FROM turns_fts
          JOIN turns t ON t.id=turns_fts.id
          WHERE turns_fts MATCH ? ORDER BY rank LIMIT ?
        """, (expression, limit)).fetchall()
    return [KnowledgeHit(r["id"], r["id"], r["content"][:1200], r["source_path"],
                         r["line_start"], r["line_end"], float(-r["rank"])) for r in rows]

def get_turn(db: Path, ident: str) -> dict | None:
    with connect(db) as conn:
        row = conn.execute("SELECT * FROM turns WHERE id=?", (ident,)).fetchone()
    return dict(row) if row else None
