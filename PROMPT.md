# Create a Clink action

You are contributing one small text transformation for Clink. Read `README.md`, inspect several examples in `Actions/`, and inspect `tools/build-manifest.py` before editing. Create or update exactly one `.clinkext` file in `Actions/`.

An action is JSON containing a stable id, name, SF Symbol icon, short summary, `input`, `replacesInput`, `enabled`, and a `source` string defining `transform(text)`. Copy the nearest example and keep the transformation narrow, deterministic, offline, and safe for arbitrary Unicode text. The function must return text. Do not use imports, networking, files, time, randomness, UI APIs, or unsupported Python features. Select the input scope and replacement behaviour that match the action’s purpose.

Use a unique filename and id. Keep source readable and concise. Test the source’s intended edge cases (empty input, whitespace, punctuation, and non-ASCII text where relevant), parse the JSON, then run:

```sh
python3 tools/build-manifest.py
```

Commit the generated `manifest.json` if it changes. Do not weaken the trust model or modify workflows. Finish with the action’s behaviour, input/replacement choices, edge cases considered, and validation result.
