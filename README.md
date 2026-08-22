<p align="center">
  <img src="https://raw.githubusercontent.com/anti-ltd/clink-language-packs/main/icon-1024.png" width="96" alt="Clink app icon">
</p>

<h1 align="center">Clink actions</h1>

<p align="center">Open text transformations for Clink.</p>

Actions transform text directly from the keyboard: uppercase a word, reverse text, format a title, or generate a small reply. They use Clink's constrained `transform(text)` action format and need explicit repository trust before downloading.

## Official Clink repositories

[Language packs](https://github.com/anti-ltd/clink-language-packs) · [Layouts](https://github.com/anti-ltd/clink-layouts) · [Profiles](https://github.com/anti-ltd/clink-profiles) · [Themes](https://github.com/anti-ltd/clink-themes) · [Panels](https://github.com/anti-ltd/clink-panels) · [Actions](https://github.com/anti-ltd/clink-actions)

## Included actions

| Action | What it does |
|---|---|
| 🔠 Uppercase | Capitalises the current word. |
| ↔️ Reverse | Reverses the current word. |
| 📝 Title case | Formats text as a title. |
| 🐍 Snake case | Formats text_for_code. |
| 🤷 Shrug | Inserts a shrug. |
| 🔢 Word count | Counts words before the cursor. |

## Make your first action

1. Fork this repository.
2. Copy an `.clinkext` file in [`Actions/`](Actions), rename it, and update its name, summary, input, and `transform(text)` function.
3. Import it into Clink to test it.
4. Push to `main` after the repository release workflow is in place.

## Add your repository to Clink

Open **General → Repositories**, add `owner/repository`, then open **Tools → Custom Actions** and select your repository. Clink asks for explicit permission before it downloads action logic.

## What Clink verifies

Clink accepts only public HTTPS GitHub release files from the repository the person added. It verifies the manifest, SHA-256 hash, byte count, `.clinkext` type, and constrained `transform(text)` contract. Actions are executable-style content, so only add repositories you trust.
