<p align="center">
  <img src="https://raw.githubusercontent.com/anti-ltd/clink-language-packs/main/icon-1024.png" width="96" alt="Clink app icon">
</p>

<h1 align="center">Clink actions</h1>

<p align="center">Open text transformations for Clink keyboards.</p>

Actions transform text directly from the keyboard, such as changing case, reversing a word, formatting a title, or inserting a small reply. They use Clink's constrained `transform(text)` format and require explicit repository trust before download.

## Official Clink repositories

[Language packs](https://github.com/anti-ltd/clink-language-packs) · [Layouts](https://github.com/anti-ltd/clink-layouts) · [Profiles](https://github.com/anti-ltd/clink-profiles) · [Themes](https://github.com/anti-ltd/clink-themes) · [Panels](https://github.com/anti-ltd/clink-panels) · [Actions](https://github.com/anti-ltd/clink-actions) · [Fonts](https://github.com/anti-ltd/clink-fonts) · [Sounds](https://github.com/anti-ltd/clink-sounds)

## Included actions

The official repository currently includes:

| Action | What it does |
|---|---|
| Uppercase | Capitalizes the current word. |
| Reverse | Reverses the current word. |
| Title case | Formats text as a title. |
| Snake case | Formats text_for_code. |
| Shrug | Inserts a shrug. |
| Word count | Counts words before the cursor. |

The files live in [`Actions/`](Actions). They are small and readable, so they are a good place to start when making your own.

## Make your first action

1. Fork this repository.
2. Copy an `.clinkext` file in [`Actions/`](Actions), rename it, and update its name, summary, input, and `transform(text)` function.
3. Import it into Clink to test it.
4. Run the repository validation tools if they are present.
5. Push to `main`. GitHub Actions publishes the actions and manifest to the `latest` release.

## Add your repository to Clink

Open **General → Repositories** in Clink and add `owner/repository`. Then open **Tools → Custom Actions** and select your repository. Clink asks for explicit permission before downloading action logic.

## Make an action with an AI agent

[`PROMPT.md`](PROMPT.md) is a ready-to-use brief for an AI coding agent. Fork the repository, open the fork in your agent, and say:

```text
Read PROMPT.md and create an action that [describe the text transformation].
```

The prompt restricts the agent to Clink's small `transform(text)` contract and asks it to consider edge cases. Review the generated source and test it in Clink before publishing; action repositories require a separate trust decision from people who install them.

## What Clink verifies

Clink accepts only public HTTPS GitHub release files from the repository you added. It verifies the manifest, SHA-256 hash, byte count, `.clinkext` type, and constrained `transform(text)` contract.

Actions contain executable-style logic, so adding a repository is a stronger trust decision than adding data-only packs. Only add repositories whose code and release process you trust.

## Publishing is automatic

Keep `Actions/`, `tools/`, and `.github/workflows/` in your fork. Add or update an action and push to `main`. GitHub Actions validates the files and refreshes the `latest` release.
