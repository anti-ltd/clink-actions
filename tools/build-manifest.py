#!/usr/bin/env python3
"""Build the verified manifest for a Clink action release."""
import hashlib, json, os, pathlib

root = pathlib.Path(__file__).resolve().parents[1]
repository = os.environ.get("GITHUB_REPOSITORY", "anti-ltd/clink-actions")
actions = []
for path in sorted((root / "Actions").glob("*.clinkext")):
    raw = path.read_bytes()
    action = json.loads(raw)
    actions.append({"id": path.stem, "name": action["name"], "version": "latest", "asset": {
        "path": path.name,
        "url": f"https://github.com/{repository}/releases/download/latest/{path.name}",
        "sha256": hashlib.sha256(raw).hexdigest(), "byteCount": len(raw)}})
(root / "manifest.json").write_text(json.dumps({"version": "latest", "actions": actions}, indent=2) + "\n")
