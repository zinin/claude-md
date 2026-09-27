# claude-md (plugin source)

This file is for work inside this repository. It is not a plugin component.

- Load the working tree in Claude Code with `claude --plugin-dir "$PWD"` (disable a marketplace
  copy first, re-enable it afterwards); in Grok with `grok plugin install "$PWD" --trust` — a
  snapshot copy: after a change, `grok plugin uninstall claude-md --confirm`, install again and
  start a new session. Keep one snapshot at a time.
- The skill is vendored: see Credits in README.md before editing it.
- Do not bump `.claude-plugin/plugin.json` on a feature branch; a release is a separate
  `chore(release): X.Y.Z` commit on master with an annotated tag `claude-md--vX.Y.Z`.
- Before a PR: `git rm -r docs/superpowers/` when it exists, and commit.
