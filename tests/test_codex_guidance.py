"""Codex guidance in the claude-md-writer skill.

One skill text serves Claude Code, Grok and Codex. Codex reads AGENTS.md and reads
CLAUDE.md only through project_doc_fallback_filenames; it never loads .claude/rules/
by itself. These tests pin those statements and keep the plugin on one manifest.
"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "claude-md-writer" / "SKILL.md"
README = ROOT / "README.md"

FALLBACK_LINE = 'project_doc_fallback_filenames = ["CLAUDE.md"]'
RULES_SENTENCE = "Codex does not load `.claude/rules/` on its own."
PRECEDENCE_SENTENCE = "a folder with both files gives Codex only `AGENTS.md`"


def codex_section(text):
    """The `### Codex` subsection up to the next heading of the same or a higher level."""
    rest = text[text.index("\n### Codex\n") + 1:]
    ends = [i for i in (rest.find("\n### ", 1), rest.find("\n## ", 1)) if i != -1]
    return rest[:min(ends)] if ends else rest


def flat(text):
    """The text on one line, so a phrase check does not depend on line wrapping."""
    return " ".join(text.split())


class CodexSectionTest(unittest.TestCase):
    def setUp(self):
        self.text = SKILL.read_text(encoding="utf-8")
        self.section = flat(codex_section(self.text))

    def test_codex_section_follows_the_agents_md_section(self):
        self.assertLess(self.text.index("\n### AGENTS.md\n"),
                        self.text.index("\n### Codex\n"))

    def test_codex_section_names_the_fallback_line(self):
        self.assertIn(FALLBACK_LINE, self.section)

    def test_codex_section_requires_reading_rules_by_hand(self):
        self.assertIn(RULES_SENTENCE, self.section)

    def test_codex_section_requires_reading_all_unscoped_rules(self):
        self.assertIn("read all rules without `paths:`", self.section)
        self.assertIn("rules whose `paths:` globs match it", self.section)

    def test_codex_section_explains_agents_md_precedence(self):
        self.assertIn(PRECEDENCE_SENTENCE, self.section)

    def test_codex_section_names_the_codex_call(self):
        self.assertIn("$claude-md:claude-md-writer", self.section)

    def test_footer_records_the_codex_change(self):
        footer = flat(self.text.rsplit("\n---\n", 1)[1])
        self.assertIn("Codex section", footer)
        sources = self.text.split("\n## Sources\n", 1)[1]
        self.assertIn("github.com/openai/codex", sources)


class ReadmeTest(unittest.TestCase):
    def test_readme_drops_the_little_to_do_claim(self):
        text = README.read_text(encoding="utf-8")
        self.assertNotIn("has little to do", text)
        self.assertIn("project_doc_fallback_filenames", text)


class SingleManifestTest(unittest.TestCase):
    def test_claude_manifest_is_the_only_manifest(self):
        # Codex reads .claude-plugin/plugin.json itself. A root plugin.json would win
        # over it in Grok, and a catalog file under .agents/ would hide the neighbours.
        self.assertTrue((ROOT / ".claude-plugin" / "plugin.json").is_file())
        for extra in ("plugin.json", ".codex-plugin", ".agents"):
            with self.subTest(extra=extra):
                self.assertFalse((ROOT / extra).exists(), f"extra manifest: {extra}")


if __name__ == "__main__":
    unittest.main()
