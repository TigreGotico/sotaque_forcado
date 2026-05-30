"""Example — accent a sentence, then convert it to IPA if phonemizer is present.

Run::

    python examples/06_phonemize.py
"""
import os


def main() -> None:
    try:
        import sotaque_forcado.sotaques as smod
        from sotaque_forcado.sotaques import Sotaque
    except Exception as exc:
        print("skipped: sotaque_forcado not importable:", exc)
        print("install the core requirements: pip install -r requirements.txt")
        return

    presets = os.path.dirname(smod.__file__)
    s = Sotaque(os.path.join(presets, "algarvio.json"))

    sentence = "o meu sotaque é especial e também se percebe bem"
    accented = s.add_accent(sentence)
    print("padrão:  ", sentence)
    print("accented:", accented)

    # phonemize() needs the phonemizer extra plus an espeak-ng backend
    try:
        print("IPA:     ", s.phonemize(sentence))
    except Exception as exc:
        print("IPA:      unavailable (install extras.txt + espeak-ng):", exc)


if __name__ == "__main__":
    main()
