"""Example — run one sentence through several bundled accents side by side.

Run::

    python examples/02_compare_accents.py
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
    accents = ["lisboa", "porto", "algarvio", "transmontano", "madeirense"]
    loaded = {a: Sotaque(os.path.join(presets, f"{a}.json")) for a in accents}

    sentence = "o boi passou a correr porque viu a vaca a pastar"
    print("padrão:", sentence)
    print("-" * 40)
    for name, s in loaded.items():
        print(f"{name:14} {s.add_accent(sentence)}")


if __name__ == "__main__":
    main()
