from pathlib import Path
from iadev.models import SourceSpan, Turn
from iadev.storage import replace_turns, search, get_turn

def test_fts_and_provenance(tmp_path: Path):
    db = tmp_path / "test.sqlite"
    t = Turn("turn-00001", "user", "timestamp", "Aprender GitHub y ramas",
             SourceSpan("source.md", "abc", 10, 15))
    assert replace_turns(db, [t]) == 1
    hits = search(db, "GitHub", 5)
    assert len(hits) == 1
    assert hits[0].line_start == 10
    assert get_turn(db, t.id)["role"] == "user"
    assert search(db, "") == []
