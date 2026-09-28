# Changelog

All notable changes to claude-md will be documented here.

## [0.17.0] - 2026-09-28

### Added
- **Codex section in `claude-md-writer`.** How Codex reads `CLAUDE.md` through
  `project_doc_fallback_filenames`, why `AGENTS.md` in the same folder hides it, and that
  `.claude/rules/` are read by hand. Invoked in Codex as `$claude-md:claude-md-writer`.

## [0.16.0] - 2026-09-27

### Changed
- **Split out of claude-mesh 0.15.0.** The `claude-md-writer` skill moved here with its history.
  The skill keeps its name and is invoked as `/claude-md:claude-md-writer`.
