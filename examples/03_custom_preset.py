"""Example — build a custom accent from the all-false template and load it.

Run::

    python examples/03_custom_preset.py
"""
import json
import os
import tempfile


def main() -> None:
    try:
        import sotaque_forcado.sotaques as smod
        from sotaque_forcado.sotaques import Sotaque
    except Exception as exc:
        print("skipped: sotaque_forcado not importable:", exc)
        print("install the core requirements: pip install -r requirements.txt")
        return

    presets = os.path.dirname(smod.__file__)
    with open(os.path.join(presets, "padrao.json")) as f:
        cfg = json.load(f)

    # a small northern flavour: v -> b, plus diphthong accenting
    cfg["substituicao_v_por_b"] = True
    cfg["acentuacao_ditongos"] = True
    cfg["abrir_ditongos"] = True

    path = os.path.join(tempfile.mkdtemp(), "norte.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False)

    s = Sotaque(path)
    print("loaded:", repr(s))
    for sent in ["a velha vila do varão", "as mães foram passear com os cães"]:
        print(f"{sent}\n  -> {s.add_accent(sent)}")


if __name__ == "__main__":
    main()
