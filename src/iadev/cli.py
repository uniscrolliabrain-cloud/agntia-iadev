"""iadev: audit, ingest, search, tree and context."""
import argparse
import json
import os
from pathlib import Path
from .ingest import parse_export, audit_export, write_manifest
from .storage import replace_turns
from .service import KnowledgeService

def main(argv=None):
    parser = argparse.ArgumentParser(prog="iadev")
    parser.add_argument("--db", default=os.getenv("IADEV_DB", "data/indexes/knowledge.sqlite"))
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("audit", "ingest"):
        p = sub.add_parser(name)
        p.add_argument("source", type=Path)
        if name == "ingest":
            p.add_argument("--manifest", type=Path, default=Path("data/generated/turns.jsonl"))
    p = sub.add_parser("search")
    p.add_argument("query")
    p.add_argument("--limit", type=int, default=10)
    sub.add_parser("tree")
    p = sub.add_parser("context")
    p.add_argument("query")
    args = parser.parse_args(argv)
    db = Path(args.db)
    if args.command == "audit":
        result = audit_export(args.source)
    elif args.command == "ingest":
        turns = parse_export(args.source)
        write_manifest(turns, args.manifest)
        result = {"indexed": replace_turns(db, turns), "manifest": str(args.manifest)}
    else:
        svc = KnowledgeService(db)
        if args.command == "search":
            result = svc.search(args.query, args.limit)
        elif args.command == "tree":
            result = svc.tree()
        else:
            result = svc.context(args.query)
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
