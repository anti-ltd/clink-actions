# Verify this Clink actions repository

Read `README.md`, `PROMPT.md`, every file in `Actions/`, and `tools/build-manifest.py`. Audit the repository; do not change files unless asked to fix a specific problem.

Run `python3 tools/build-manifest.py`, then inspect the resulting diff. Every action must be a valid `.clinkext` JSON file with a unique stable id, name, SF Symbol icon, concise summary, valid input/replacement settings, enabled state, and a `source` string defining `transform(text)`.

For each source, verify that it is deterministic and offline; accepts arbitrary Unicode text; returns text; and has no imports, networking, file access, time, randomness, UI APIs, or unsupported Python features. Reason through empty input, whitespace, punctuation, and non-ASCII text. Confirm the generated `manifest.json` exactly represents the action files and that no unexpected files or workflow/security-policy changes are present.

Report the commands run, pass/fail result for each action, manifest status, and any issue with a precise file path and recommended fix. Do not claim success if a required check could not run.
