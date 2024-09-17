import unittest

from sotaque_forcado.preprocessors import ditongacao_vogal_tonica_com_u
from sotaque_forcado.silabas import *


class TestSyllableFunctions(unittest.TestCase):

    def test_split_into_syllables(self):
        self.assertEqual(split_into_syllables("olho"), ['ca', 'fé'])
        self.assertEqual(split_into_syllables("livro"), ['ca', 'fé'])
        self.assertEqual(split_into_syllables("formiga"), ['ca', 'fé'])
        self.assertEqual(split_into_syllables("café"), ['ca', 'fé'])
        self.assertEqual(split_into_syllables("português"), ['por', 'tu', 'guês'])
        self.assertEqual(split_into_syllables("árvore"), ['ár', 'vo', 're'])
        self.assertEqual(split_into_syllables("universidade"), ['uni', 'ver', 'si', 'da', 'de'])
        self.assertEqual(split_into_syllables("extra"), ['ex', 'tra'])
        self.assertEqual(split_into_syllables("o"), ['o'])  # Single letter

    def test_identify_tonic_syllable(self):
        self.assertEqual(identify_tonic_syllable(["ca", "fé"]), 1)
        self.assertEqual(identify_tonic_syllable(["ca", "fé"]), 1)
        self.assertEqual(identify_tonic_syllable(["por", "tu", "guês"]), 2)
        self.assertEqual(identify_tonic_syllable(["ár", "vo", "re"]), 0)
        self.assertEqual(identify_tonic_syllable(["uni", "ver", "si", "da", "de"]), 2)
        self.assertEqual(identify_tonic_syllable(["ex", "tra"]), 1)
        self.assertEqual(identify_tonic_syllable(["créditos"]), 0)

    def test_identify_tonic_vowel(self):
        self.assertEqual(identify_tonic_vowel(["ca", "fé"]), (1, 1))
        self.assertEqual(identify_tonic_vowel(["por", "tu", "guês"]), (2, 2))
        self.assertEqual(identify_tonic_vowel(["ár", "vo", "re"]), (0, 0))
        self.assertEqual(identify_tonic_vowel(["uni", "ver", "si", "da", "de"]), (2, 1))
        self.assertEqual(identify_tonic_vowel(["ex", "tra"]), (1, 2))
        self.assertEqual(identify_tonic_vowel(["créditos"]), (0, 2))

    def test_get_syllable_info(self):
        self.assertEqual(get_syllable_info("café"), [(0, 2, 'ca', False),
                                                     (2, 4, 'fé', True)])
        self.assertEqual(get_syllable_info("português"),
                         [(0, 3, 'por', False),
                          (3, 5, 'tu', False),
                          (5, 9, 'guês', True)])
        self.assertEqual(get_syllable_info("árvore"), [(0, 2, 'ár', True),
                                                       (2, 4, 'vo', False),
                                                       (4, 6, 're', False)])
        self.assertEqual(get_syllable_info("universidade"), [(0, 3, 'uni', False),
                                                             (3, 6, 'ver', False),
                                                             (6, 8, 'si', True),
                                                             (8, 10, 'da', False),
                                                             (10, 12, 'de', False)])
        self.assertEqual(get_syllable_info("extra"), [(0, 2, 'ex', False), (2, 5, 'tra', True)])
        self.assertEqual(get_syllable_info("o"), [(0, 1, 'o', True)])  # Single letter

    def test_ditongacao_vogal_tonica_com_u(self):
        self.assertEqual(ditongacao_vogal_tonica_com_u("correr"), "corrúer")
        self.assertEqual(ditongacao_vogal_tonica_com_u("olho"), "uôlho")
        self.assertEqual(ditongacao_vogal_tonica_com_u("livro"), "lúivro")
        self.assertEqual(ditongacao_vogal_tonica_com_u("formiga"), "formúiga")
        self.assertEqual(ditongacao_vogal_tonica_com_u("café"), "cafúé")
        self.assertEqual(ditongacao_vogal_tonica_com_u("português"), "portugúês")
        self.assertEqual(ditongacao_vogal_tonica_com_u("árvore"), "úárvore")
        self.assertEqual(ditongacao_vogal_tonica_com_u("universidade"), "universidade")
        self.assertEqual(ditongacao_vogal_tonica_com_u("extra"), "extra")
        self.assertEqual(ditongacao_vogal_tonica_com_u("o"), "o")


if __name__ == '__main__':
    unittest.main()
