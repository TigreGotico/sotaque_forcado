"""Tests for sotaque_forcado.silabas against a real Portuguese gold set.

``split_into_syllables`` wraps Pyphen's ``pt_PT`` hyphenation dictionary. A
hyphenation dictionary is not a syllabifier: it marks the places a typesetter
may break a line, and Portuguese hyphenation rules forbid some breaks that
syllabification makes. The tests below measure that difference against gold
instead of asserting the wrapper's own output back at itself.

The gold is ``test/gold_sample.json``: 500 words from
TigreGotico/portuguese-unified-pronunciation-lexicon, kept only where Infopedia
and the Portal da Lingua Portuguesa give the same split and the syllables join
back to the headword. It is the held-out half, and this library tunes nothing
on it.
"""
import json
import pathlib
import unittest

from sotaque_forcado.silabas import (get_syllable_info, identify_tonic_syllable,
                                     identify_tonic_vowel,
                                     split_into_syllables)

GOLD_PATH = pathlib.Path(__file__).parent / "gold_sample.json"

#: Measured at 403 of 500 (0.8060) on 2026-09-26 with pyphen's pt_PT
#: dictionary. The floor sits below that so one borderline word cannot turn the
#: suite red, and far enough above it that a real regression can.
MATCH_FLOOR = 0.78


def load_gold():
    with open(GOLD_PATH, encoding="utf-8") as fh:
        return json.load(fh)["entries"]


class TestGoldSyllabification(unittest.TestCase):
    """The gold set, as a measurement and as two invariants."""

    @classmethod
    def setUpClass(cls):
        cls.gold = load_gold()
        cls.results = [(e["word"],
                        [s.lower() for s in e["syllables"]],
                        split_into_syllables(e["word"]))
                       for e in cls.gold]

    def test_gold_sample_is_the_size_it_claims(self):
        self.assertEqual(len(self.gold), 500)

    def test_exact_match_rate_holds_the_floor(self):
        hits = sum(1 for _, gold, got in self.results if got == gold)
        rate = hits / len(self.results)
        self.assertGreaterEqual(
            rate, MATCH_FLOOR,
            f"exact-match rate fell to {rate:.4f} ({hits} of {len(self.results)})")

    def test_every_split_joins_back_to_the_word(self):
        """A syllabification that loses or invents a letter is wrong whatever
        the boundaries are. This holds for all 500 words, gold agreement or
        not, so it is an oracle the match rate cannot give."""
        for word, _, got in self.results:
            self.assertEqual("".join(got), word.lower(), word)

    def test_the_wrapper_never_splits_where_the_gold_does_not(self):
        """Every miss is the hyphenation dictionary joining syllables the gold
        separates, never cutting one the gold keeps whole. Measured: all 97
        misses have fewer syllables than gold, 0 have more. A miss with MORE
        syllables than gold would be a different defect and needs its own
        analysis, so it fails here rather than passing quietly."""
        over = [(w, gold, got) for w, gold, got in self.results
                if len(got) > len(gold)]
        self.assertEqual(over, [], f"{len(over)} word(s) split past the gold")


class TestKnownHyphenationDivergence(unittest.TestCase):
    """The two conventions that account for every miss, each with a word.

    Of the 97 misses measured on 2026-09-26: 61 are a one-letter vowel
    syllable at the start of the word, which Portuguese hyphenation refuses to
    leave alone on a line; 33 are a vowel sequence the dictionary keeps in one
    syllable where the gold puts a hiatus; 3 combine both.
    """

    def test_leading_one_letter_vowel_is_not_separated(self):
        # Gold: a-ca-sa-la-do. Hyphenation may not strand a single letter.
        self.assertEqual(split_into_syllables("acasalado"),
                         ["aca", "sa", "la", "do"])

    def test_hiatus_is_kept_in_one_syllable(self):
        # Gold: ca-res-ti-a. The dictionary reads <ia> as one nucleus.
        self.assertEqual(split_into_syllables("carestia"),
                         ["ca", "res", "tia"])

    def test_a_word_both_conventions_touch(self):
        # Gold: e-go-is-mo, with the stressed <i> its own nucleus.
        self.assertEqual(split_into_syllables("egoísmo"), ["egoís", "mo"])


class TestSyllableAccessors(unittest.TestCase):
    """The accessors, on words the gold and the wrapper agree about.

    Each expected value is the gold split, so these do not restate the
    wrapper's output: a change in the wrapper turns them red.
    """

    def test_split_matches_gold_word_by_word(self):
        # Every pair here is an entry of gold_sample.json, agreed by both
        # sources, and the wrapper reproduces it.
        for word, expected in [("moqueca", ["mo", "que", "ca"]),
                               ("toga", ["to", "ga"]),
                               ("geladeira", ["ge", "la", "dei", "ra"]),
                               ("boletim", ["bo", "le", "tim"]),
                               ("embalsamar", ["em", "bal", "sa", "mar"]),
                               ("cosmógrafo", ["cos", "mó", "gra", "fo"])]:
            self.assertEqual(split_into_syllables(word), expected, word)

    def test_a_single_letter_word_is_one_syllable(self):
        self.assertEqual(split_into_syllables("o"), ["o"])

    def test_get_syllable_info_spans_cover_the_word(self):
        """Each span must index the syllable it carries, and the spans must
        tile the word end to end with no gap and no overlap."""
        for word in ["moqueca", "geladeira", "embalsamar", "o"]:
            info = get_syllable_info(word)
            self.assertEqual([s for _, _, s, _ in info],
                             split_into_syllables(word), word)
            cursor = 0
            for start, end, syllable, _ in info:
                self.assertEqual(start, cursor, word)
                self.assertEqual(word.lower()[start:end], syllable, word)
                cursor = end
            self.assertEqual(cursor, len(word), word)

    def test_exactly_one_syllable_is_marked_tonic(self):
        for word in ["moqueca", "geladeira", "embalsamar", "cosmógrafo", "o"]:
            info = get_syllable_info(word)
            self.assertEqual(sum(1 for *_, tonic in info if tonic), 1, word)

    def test_an_empty_syllable_list_is_refused(self):
        with self.assertRaises(ValueError):
            identify_tonic_syllable([])
        with self.assertRaises(ValueError):
            identify_tonic_vowel([])

    def test_tonic_vowel_points_at_a_vowel_of_the_tonic_syllable(self):
        for word in ["moqueca", "geladeira", "cosmógrafo", "boletim"]:
            syllables = split_into_syllables(word)
            idx, vowel_idx = identify_tonic_vowel(syllables)
            self.assertEqual(idx, identify_tonic_syllable(syllables), word)
            self.assertIn(syllables[idx][vowel_idx], "aeiouáéíóúâêîôûãõà", word)


if __name__ == "__main__":
    unittest.main()
