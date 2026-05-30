"""Example — syllable splitting and tonic-stress detection.

Run::

    python examples/05_syllables.py
"""


def main() -> None:
    try:
        from sotaque_forcado.silabas import (
            split_into_syllables,
            identify_tonic_syllable,
            get_syllable_info,
        )
    except Exception as exc:  # pyphen missing
        print("skipped: silabas not importable:", exc)
        print("install the core requirements: pip install -r requirements.txt")
        return

    for word in ["trabalho", "coelho", "piscina", "fogo"]:
        syllables = split_into_syllables(word)
        tonic = identify_tonic_syllable(syllables)
        print(f"{word:10} {syllables}  tonic -> {syllables[tonic]!r}")

    print()
    print("syllable info for 'trabalho' (start, end, syllable, is_tonic):")
    for info in get_syllable_info("trabalho"):
        print("  ", info)


if __name__ == "__main__":
    main()
