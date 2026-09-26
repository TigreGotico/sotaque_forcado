"""Tests for the stress functions, against the written Portuguese stress rule.

The oracle is not the implementation and not a gold file. Portuguese marks
stress in the spelling: a word with an acute, circumflex, grave or tilde is
stressed on that syllable; a word without one is stressed on the last syllable
when it ends in -l, -r, -z, -i, -u, -im, -um, -ns or a nasal diphthong, and on
the second-to-last syllable otherwise. That rule is what the accent marks exist
to encode, and it decides every word below by counting letters, with no
reference to what this library returns.

``identify_tonic_syllable`` takes the syllable list, so the rule is applied to
the same list the function sees. Where the wrapper's split differs from a
dictionary's, both sides differ together and the comparison stays fair.
"""
import unittest

from sotaque_forcado.silabas import (identify_tonic_syllable,
                                     identify_tonic_vowel,
                                     split_into_syllables)

ACCENTS = "áéíóúâêîôûàãõ"
OXYTONE_ENDINGS = ("l", "r", "z", "i", "u", "im", "um", "ins", "uns",
                   "ns", "ão", "ões", "ãs")


def stressed_index(syllables):
    """The written rule, computed from the letters alone."""
    for idx, syllable in enumerate(syllables):
        if any(letter in ACCENTS for letter in syllable):
            return idx
    if syllables[-1].endswith(OXYTONE_ENDINGS):
        return len(syllables) - 1
    return max(0, len(syllables) - 2)


#: Words the rule and the implementation agree on. Each is here because the
#: rule places the stress, not because the function does.
AGREED = ["café", "português", "árvore", "falar", "feliz", "comum", "jardim",
          "bonita", "médico", "rápido", "cantar", "papel", "menina", "lápis",
          "fácil", "útil", "ananás", "irmã", "coração"]

#: One word per accent letter, each chosen so the accent is the only thing that
#: decides: the accent sits away from the last syllable, and with the accent
#: ignored the function's fallbacks return a different index. Dropping a single
#: letter from the accent set turns these red, which the words above do not.
ACCENT_DECIDES = ["métrico", "sétimo", "célebre", "genético", "sábado",
                  "término", "íntimo", "pêssego", "ângulo", "ótimo", "último",
                  "côncavo", "fôlego", "mágico"]

#: Words the rule places and the implementation does not. Measured 2026-09-26.
#: The function has no paroxytone default: it falls through to a search for a
#: "strong" consonant and returns whatever syllable holds one. Filed as its own
#: task (T-5362); frozen here so a fix turns this test red and has to delete
#: the row.
KNOWN_WRONG = {
    "casa": 1,           # rule: 0, ca-sa ends in -a
    "extra": 1,          # rule: 0, ex-tra ends in -a
    "cidade": 2,         # rule: 1, ci-da-de ends in -e
    "telefone": 3,       # rule: 2, te-le-fo-ne ends in -e
    "hospital": 1,       # rule: 2, hos-pi-tal ends in -l
    "animal": 0,         # rule: 1, ani-mal ends in -l
    "universidade": 0,   # rule: 3, uni-ver-si-da-de ends in -e
}


class TestStressAgainstTheWrittenRule(unittest.TestCase):

    def test_the_rule_and_the_function_agree_on_these(self):
        for word in AGREED + ACCENT_DECIDES:
            syllables = split_into_syllables(word)
            self.assertEqual(identify_tonic_syllable(syllables),
                             stressed_index(syllables), word)

    def test_an_accented_syllable_always_wins(self):
        """The one part of the rule the implementation applies first. A word
        with a written accent cannot be stressed anywhere else."""
        for word in ["café", "árvore", "médico", "ananás", "cosmógrafo",
                     "coração"] + ACCENT_DECIDES:
            syllables = split_into_syllables(word)
            idx = identify_tonic_syllable(syllables)
            self.assertTrue(any(a in syllables[idx] for a in ACCENTS), word)
            self.assertEqual(idx, stressed_index(syllables), word)

    def test_the_index_is_a_position_in_the_list(self):
        """The docstring says "index (from the end)" and the function returns a
        forward index. The forward index is what every caller in this package
        uses, so the behaviour is what the test pins; the docstring is the
        thing that is wrong."""
        for word in AGREED:
            syllables = split_into_syllables(word)
            idx = identify_tonic_syllable(syllables)
            self.assertIn(idx, range(len(syllables)), word)
            self.assertEqual(syllables[idx],
                             syllables[stressed_index(syllables)], word)

    def test_a_one_syllable_word_is_stressed_on_itself(self):
        for syllables in [["o"], ["pão"], ["mais"]]:
            self.assertEqual(identify_tonic_syllable(syllables), 0)

    def test_tonic_vowel_agrees_with_tonic_syllable(self):
        for word in AGREED:
            syllables = split_into_syllables(word)
            idx, _ = identify_tonic_vowel(syllables)
            self.assertEqual(idx, identify_tonic_syllable(syllables), word)


class TestKnownStressDefect(unittest.TestCase):
    """The paroxytone default is missing. These rows state the defect.

    Do not read this class as the specification. Each row records what the
    function returns today next to what the rule requires, so the size of the
    defect is visible and a fix cannot land unnoticed.
    """

    def test_the_defect_is_exactly_these_words(self):
        for word, current in KNOWN_WRONG.items():
            syllables = split_into_syllables(word)
            self.assertEqual(
                identify_tonic_syllable(syllables), current,
                f"{word}: behaviour moved; the rule wants "
                f"{stressed_index(syllables)}, this row expected {current}")
            self.assertNotEqual(current, stressed_index(syllables), word)


if __name__ == "__main__":
    unittest.main()
