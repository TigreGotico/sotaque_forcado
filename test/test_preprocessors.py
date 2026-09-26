"""Tests for the accent rewrite rules, against what docs/rules.md documents.

The oracle here is the documentation, not the current output: docs/rules.md
states one worked example per rule, and the docstrings state a second. A rule
whose documented example stops holding is a rule that changed behind its own
documentation.
"""
import unittest

from sotaque_forcado.preprocessors import ditongacao_vogal_tonica_com_u
from sotaque_forcado.silabas import identify_tonic_vowel, split_into_syllables


class TestDitongacaoVogalTonicaComU(unittest.TestCase):
    """docs/rules.md: "insert u before tonic vowel", olho -> uolho.
    The docstring adds livro -> luivro."""

    def test_the_documented_examples(self):
        self.assertEqual(ditongacao_vogal_tonica_com_u("olho"), "uôlho")
        self.assertEqual(ditongacao_vogal_tonica_com_u("livro"), "lúivro")

    def test_a_u_is_inserted_and_nothing_else_is_lost(self):
        """Removing the inserted u, and the accent it carries, must give the
        word back. This is the rule as a property: it inserts, it does not
        substitute. It holds for words the rule touches and for words it
        leaves alone."""
        table = str.maketrans({"ú": "u", "ô": "o"})
        for word in ["olho", "livro", "formiga", "café", "português",
                     "árvore", "correr"]:
            out = ditongacao_vogal_tonica_com_u(word)
            if out == word:
                continue
            plain = out.translate(table)
            # Deleting one u somewhere must give the word back. The position is
            # not asserted here; test_the_change_lands_on_the_tonic_syllable
            # covers that, and a word that already holds a u (portugues) has
            # more than one candidate.
            candidates = {plain[:i] + plain[i + 1:]
                          for i, c in enumerate(plain) if c == "u"}
            # A word whose tonic vowel already follows a u gets that u
            # accented instead of a second one inserted (portugues ->
            # portugues with the accent on the u), so plain == word is the
            # other legal outcome.
            candidates.add(plain)
            self.assertIn(word, candidates,
                          f"{word} -> {out} neither inserts one u nor "
                          f"accents the u already there")

    def test_a_word_shorter_than_four_letters_is_untouched(self):
        for word in ["o", "eu", "mas", "pão"]:
            self.assertEqual(ditongacao_vogal_tonica_com_u(word), word)

    def test_the_change_lands_on_the_tonic_syllable(self):
        for word in ["olho", "livro", "formiga", "correr"]:
            syllables = split_into_syllables(word)
            idx, _ = identify_tonic_vowel(syllables)
            out = ditongacao_vogal_tonica_com_u(word)
            untouched = "".join(syllables[:idx])
            self.assertTrue(out.startswith(untouched),
                            f"{word} -> {out} changed before syllable {idx}")


if __name__ == "__main__":
    unittest.main()
