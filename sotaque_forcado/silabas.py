from typing import List, Tuple

from pyphen import Pyphen


def split_into_syllables(word: str) -> List[str]:
    """
    Splits a word into syllables based on common patterns of vowels and consonants.

    Args:
        word (str): The word to be split into syllables.

    Returns:
        List[str]: A list where each element is a syllable of the input word.
    """
    word = word.lower()
    dic = Pyphen(lang='pt_PT')
    return dic.inserted(word).split('-')


def identify_tonic_syllable(syllables: List[str]) -> int:
    """
    Identifies which syllable is tonic (stressed) based on common Portuguese stress rules and accent marks.

    Args:
        syllables (List[str]): Syllables of the word whose tonic syllable needs to be identified.

    Returns:
        int: The index (from the end) of the tonic syllable.
    """
    if isinstance(syllables, str):
        syllables = split_into_syllables(syllables)
    if len(syllables) == 0:
        raise ValueError("empty list of syllables!")
    if len(syllables) == 1:
        return 0

    for idx, s in enumerate(syllables):
        # Check for accent marks that indicate stress
        if any(a in s for a in 'áéíóúâêîôûãõ'):
            return idx

    for idx, s in enumerate(syllables):
        # Check for accent marks that indicate stress
        if any(a in s for a in ["oi", "ei", "ui", "ai"]):  # ditongos
            return idx


    for idx, s in enumerate(syllables):  # "strong" vowels
        if any(a + "i" in s for a in ["n", "t", "m", "p", "l", "s", "g"]):
            return  idx

    for idx, s in enumerate(syllables[::-1]):  # last syllable with "strong" letter consonant
        if any(a in s for a in ["n", "t", "m", "p", "l", "s", "g"]):
            return len(syllables) - 1 - idx

    return len(syllables) - 1


def identify_tonic_vowel(syllables: List[str]) -> Tuple[int, int]:
    """
    Identifies the index of the syllable containing the tonic vowel based on common Portuguese stress rules.

    Args:
        syllables (List[str]): Syllables of the word.

    Returns:
        Tuple[int, int]: A tuple containing the index of the syllable (in list) and the index of the vowel (in syllable string).
    """
    if len(syllables) == 0:
        raise ValueError("empty list of syllables!")

    tonic_syllable = identify_tonic_syllable(syllables)
    s = syllables[tonic_syllable]
    print()
    tonic_vowels = 'áéíóúãõâêîôûà'
    for idx, c in enumerate(s):
        if c in tonic_vowels:
            return tonic_syllable, idx

    vowels = 'aeiou'
    for idx, c in enumerate(s):
        if c in vowels:
            return tonic_syllable, idx

    return tonic_syllable, -1


def get_syllable_info(word: str) -> List[Tuple[int, int, str, bool]]:
    """
    Gets information about each syllable in the word, including start and end positions, and whether it is tonic.

    Args:
        word (str): The word to analyze.

    Returns:
        List[Tuple[int, int, str, bool]]: Each tuple contains the start index, end index, syllable string, and a boolean indicating if it is tonic.
    """
    syllables = split_into_syllables(word)
    tonic_index = identify_tonic_syllable(syllables)

    syllable_info = []
    start = 0
    for i, syllable in enumerate(syllables):
        end = start + len(syllable)
        # Check if this syllable is the tonic one
        is_tonic = i == tonic_index
        syllable_info.append((start, end, syllable, is_tonic))
        start = end

    return syllable_info
