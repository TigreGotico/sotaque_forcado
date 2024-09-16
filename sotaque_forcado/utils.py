import re

from num2words import num2words


def normalize(text):
    text = convert_digits_to_words(text)

    text = replace_patterns(text)

    # remove special chars
    text = remove_special_chars(text)
    # remove double spaces
    text = re.sub(r'\s{2,}', ' ', text)

    # Step 1: Convert the first character to uppercase
    text = re.sub(r'^(.)', lambda match: match.group(1).upper(), text)

    # Step 2: Append a period if the string doesn't end with a period or question mark
    if not re.search(r'[.?]$', text):
        text += '.'

    return text


def convert_digits_to_words(data):
    # taken from https://github.com/my-north-ai/semantic_audio_filtering/blob/main/utils/text_preprocessing_utils.py
    # apache license

    # Define a regex pattern to match digits that might be connected to letters
    digit_pattern = re.compile(r'(\d+)')

    # Function to convert a matched digit to words
    def replace_with_words(match):
        return num2words(int(match.group()), lang='pt')

    # Use re.sub with a lambda to ensure digits are replaced correctly even when connected to letters
    result = digit_pattern.sub(lambda match: ' ' + replace_with_words(match) + ' ', data)

    # Clean up spaces around the digits
    data = re.sub(r'\s+', ' ', result).strip()

    return data


def remove_special_chars(text):
    # taken from https://github.com/my-north-ai/semantic_audio_filtering/blob/main/utils/text_preprocessing_utils.py
    # apache license
    chars = [
        r'ø', r'½', r'¹', r'ß', r'Ô', r'¥', r'æ', r'ë', r'î', r'ò', r'ö', r'\|n', r'§', r'll',
        r'¢', r'©', r'£', r'~', r'º', r"\(", r"\)", r"\̀", r"–", r"~", r"”", r"»", r"“", r"«", r"˙", r"\\",
        r"—", r"@", r"å", r"´",
    ]
    chars_to_delete = '|'.join(chars)
    text = re.sub(chars_to_delete, '', text)
    return text


def replace_patterns(text):
    # taken from https://github.com/my-north-ai/semantic_audio_filtering/blob/main/utils/text_preprocessing_utils.py
    # apache license
    substitutions = {
        r"'([A-Z])": r' \1',
        r"'([a-z])": r'\1',
        r'&': 'e',
        r'ñ': 'n',
        r'ü': 'u',
        r'ž': 'z',
        r'È': 'É',
        r'è': 'é',
        r'ä': 'a',
        r'ï': 'i',
        r'ù': 'u',
        r"d'": "de ",
        r"D'": "De ",
        r"'s": " is",
        r"'e": "é",
        r"'a": "à",
        r"n'uma": "numa",
        r"n'um": "num",
        r"n'outra": "noutra",
        r"c'roa": "coroa",
        r"m'o": "mo",
        r"lh'o": "lho",
        r'"': '',
        r'\~ao': 'ão',
        r'\^e': 'ê',
        r'°c': 'ro',
        r'\^a': 'â',
        r'$': '',
        r'±': '',
        r'ª': '',
        r'\$': '',
        r"I’m": 'I am',
        r"'": '',
        r'³': '',
        r'̂': '',
        r'!': '.',
        r'²': '',
        r'…': '',
        r'`': '',
        r'·': '',
        r'°': '',
        r'º': '',
        r'¡': '',
        r'-': ' ',
        r'  ': ' ',
        r"\+": 'mais',
        r'   ': ' ',
        r' ,': ',',
        r' {2,}': ' ',
    }

    for pattern, replacement in substitutions.items():
        text = re.sub(pattern, replacement, text)

    return text
