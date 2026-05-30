"""Example — load a bundled accent and rewrite a sentence.

Run::

    python examples/01_first_accent.py
"""
import os


def main() -> None:
    try:
        import sotaque_forcado.sotaques as smod
        from sotaque_forcado.sotaques import Sotaque
    except Exception as exc:  # core deps (pyphen / num2words / quebra_frases) missing
        print("skipped: sotaque_forcado not importable:", exc)
        print("install the core requirements: pip install -r requirements.txt")
        return

    presets = os.path.dirname(smod.__file__)
    s = Sotaque(os.path.join(presets, "algarvio.json"))
    print("loaded:", repr(s))

    sentences = [
        "o Ronaldo deixou cair o chouriço ao chão",
        "isso dá azar",
        "que deus te ajude que Jesus já não consegue",
    ]
    for sent in sentences:
        print(f"{sent}\n  -> {s.add_accent(sent)}")


if __name__ == "__main__":
    main()
