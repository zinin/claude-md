# claude-md

Best practices for writing and refactoring `CLAUDE.md` files: size budgets, the three-tier
`CLAUDE.md` → `.claude/rules/` → co-located layout, `paths:` frontmatter for conditional
loading, a quality checklist. One skill, `/claude-md:claude-md-writer`. Split out of
claude-mesh 0.15.0.

The skill is about Claude Code's memory files; Grok reads `CLAUDE.md` too. Codex reads
`AGENTS.md`, so the plugin installs there but has little to do.

## Install

- **Claude Code:** `/plugin marketplace add zinin/agent-plugins`, then
  `/plugin install claude-md@zinin`.
- **Grok:** loaded from the Claude Code install; without Claude Code,
  `grok plugin marketplace add zinin/agent-plugins` and `grok plugin install claude-md --trust`.
- **Codex:** `codex plugin marketplace add zinin/agent-plugins`, then
  `codex plugin add claude-md@zinin`.

## Credits

`skills/claude-md-writer/` is vendored from
[serejaris/personal-corp-os](https://github.com/serejaris/personal-corp-os/tree/main/skills/claude-md-writer)
(MIT), then corrected against the current Claude Code docs — the upstream copy had drifted
since it was written. The skill's own footer lists every change. Upstream still maintains it;
to see what has moved there, diff against
`https://raw.githubusercontent.com/serejaris/personal-corp-os/main/skills/claude-md-writer/SKILL.md`,
expecting our corrections to show up as differences.

## License

MIT — see [LICENSE](LICENSE).
