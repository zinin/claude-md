# claude-md (plugin source)

This file is for work inside this repository. It is not a plugin component.

- Load the working tree in Claude Code with `claude --plugin-dir "$PWD"` (disable a marketplace
  copy first); in Grok with `grok plugin install "$PWD" --trust`, one snapshot at a time.
- The skill is vendored: see Credits in README.md before editing it.
- Do not bump `.claude-plugin/plugin.json` on a feature branch; a release is a separate
  `chore(release): X.Y.Z` commit on master with an annotated tag `claude-md--vX.Y.Z`.
