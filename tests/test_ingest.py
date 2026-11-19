from pathlib import Path
from iadev.ingest import parse_export, audit_export

def test_parser_preserves_embedded_marker(tmp_path: Path):
    source = tmp_path / "chat.md"
    source.write_text(
        "# Chat\n## Prompt:\n11/18/2026, 12:00:00 PM\n\n"
        "Texto\n## Prompt:\nno es timestamp\n"
        "## Response:\n11/18/2026, 12:00:01 PM · gpt-6\n\nRespuesta\n",
        encoding="utf-8",
    )
    turns = parse_export(source)
    assert len(turns) == 2
    assert turns[0].role == "user"
    assert "no es timestamp" in turns[0].content
    assert turns[1].source.line_start > turns[0].source.line_start
    assert audit_export(source)["turns_detected"] == 2
