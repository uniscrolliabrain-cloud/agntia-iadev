"""Conservative parser for the exported conversation.

Only recognizes ## Prompt: / ## Response: when followed by an export timestamp.
Other occurrences remain part of the surrounding message.
"""
import hashlib
import json
import re
from pathlib import Path
from .models import SourceSpan, Turn

MARKER = re.compile(r"^## (Prompt|Response):\s*$")
TIMESTAMP = re.compile(r"^\d{1,2}/\d{1,2}/\d{4},\s+\d{1,2}:\d{2}:\d{2}\s*[AP]M(?:\s*·.*)?\s*$")

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def parse_export(path: Path) -> list[Turn]:
    lines = path.read_text(encoding="utf-8-sig").splitlines(keepends=True)
    digest = sha256_file(path)
    markers = []
    for i, line in enumerate(lines):
        match = MARKER.match(line.rstrip("\r\n"))
        if not match:
            continue
        j = i + 1
        while j < len(lines) and not lines[j].strip() and j <= i + 2:
            j += 1
        if j < len(lines) and TIMESTAMP.match(lines[j].strip()):
            markers.append((i, j, "user" if match.group(1) == "Prompt" else "assistant"))
    turns = []
    for n, (start, stamp, role) in enumerate(markers):
        end = markers[n + 1][0] if n + 1 < len(markers) else len(lines)
        content_start = stamp + 1
        while content_start < end and not lines[content_start].strip():
            content_start += 1
        content = "".join(lines[content_start:end]).rstrip("\r\n")
        turns.append(Turn(
            id=f"turn-{n + 1:05d}",
            role=role,
            timestamp=lines[stamp].strip(),
            content=content,
            source=SourceSpan(str(path), digest, content_start + 1, end),
        ))
    return turns

def write_manifest(turns: list[Turn], destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8") as f:
        for turn in turns:
            f.write(json.dumps(turn.to_dict(), ensure_ascii=False) + "\n")

def audit_export(path: Path) -> dict:
    turns = parse_export(path)
    raw = path.read_bytes()
    return {
        "path": str(path),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "bytes": len(raw),
        "lines": len(raw.decode("utf-8-sig").splitlines()),
        "turns_detected": len(turns),
        "user_turns": sum(t.role == "user" for t in turns),
        "assistant_turns": sum(t.role == "assistant" for t in turns),
        "warning": "Parser is conservative; manually review marker anomalies and exported UI omissions.",
    }
