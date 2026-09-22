#!/usr/bin/env python3
"""Build the verified manifest for a Clink action release."""
import hashlib, json, os, pathlib

root = pathlib.Path(__file__).resolve().parents[1]
repository = os.environ.get("GITHUB_REPOSITORY", "anti-ltd/clink-actions")
files = [(path, path.read_bytes())
         for path in sorted((root / "Actions").glob("*.clinkext"))
         if not path.name.startswith(".")]

# Each distinct set of bytes gets a permanent release URL. A cached manifest
# must never point at a newer file with a different checksum: a client that
# read the catalog before a release still installs the bytes it was promised.
identity = json.dumps([(path.name, hashlib.sha256(raw).hexdigest()) for path, raw in files],
                      separators=(",", ":"))
version = "actions-" + hashlib.sha256(identity.encode()).hexdigest()

actions = []
for path, raw in files:
    action = json.loads(raw)
    actions.append({"id": path.stem, "name": action["name"], "icon": action.get("icon", ""), "summary": action.get("summary", ""), "version": version, "asset": {
        "path": path.name,
        "url": f"https://github.com/{repository}/releases/download/{version}/{path.name}",
        "sha256": hashlib.sha256(raw).hexdigest(), "byteCount": len(raw)}})
(root / "manifest.json").write_text(json.dumps({"version": version, "actions": actions}, indent=2) + "\n")
print(f"{len(actions)} actions · {version}")
