# Advanced

Recipes, gotchas, and the mechanics behind `add_accent`.

## Build a preset from the template

`sotaques/padrao.json` is the all-false template. Copy it, flip the rules you
want, and load it — nothing else is needed to define a new accent.

```python
import json, os, tempfile
import sotaque_forcado.sotaques as smod
from sotaque_forcado.sotaques import Sotaque

with open(os.path.join(os.path.dirname(smod.__file__), "padrao.json")) as f:
    cfg = json.load(f)

cfg["substituicao_v_por_b"] = True
cfg["acentuacao_ditongos"] = True
cfg["abrir_ditongos"] = True

path = os.path.join(tempfile.mkdtemp(), "norte.json")
with open(path, "w") as f:
    json.dump(cfg, f, ensure_ascii=False)

s = Sotaque(path)
print(s.add_accent("a velha vila do varão"))
```

Unknown keys are harmless — `add_accent` only reads keys it knows via
`self.rules.get(...)`, so a typo silently does nothing rather than erroring.

## Rule ordering matters

Rules are applied in a single fixed order inside `Sotaque.add_accent`, not in the
order they appear in your JSON. Each rule sees the output of the previous one, so
combinations compose. For example, with both `substituicao_de_ch_por_tch` and a
later rule enabled, the `tch` produced by the first is what the next rule sees.

If you are designing an accent and a transformation seems to "not fire", check
whether an earlier-ordered rule already consumed the pattern it was looking for.

## Comparing accents side by side

Because a `Sotaque` is cheap to construct, loading several and diffing their
output is the fastest way to characterize a rule set:

```python
import os
import sotaque_forcado.sotaques as smod
from sotaque_forcado.sotaques import Sotaque

presets = os.path.dirname(smod.__file__)
accents = ["lisboa", "porto", "algarvio", "transmontano"]
loaded = {a: Sotaque(os.path.join(presets, f"{a}.json")) for a in accents}

sentence = "o boi passou a correr porque viu a vaca"
for name, s in loaded.items():
    print(f"{name:14} {s.add_accent(sentence)}")
```

## Calling rules directly

Every entry in `preprocessors` is a pure function on strings, so you can probe a
single transformation without a `Sotaque` at all — handy for testing or for
composing your own pipeline:

```python
from sotaque_forcado.preprocessors import (
    substituicao_de_ou_por_oi, monotongacao,
    substituicao_de_z_por_j_ligacoes_palavras_acabadas_s_com_vogal as liaison,
)

substituicao_de_ou_por_oi("outro")     # 'oitro'
monotongacao("leite")                  # 'lête'
liaison("quis", "entrar")              # 'quij'  (next word starts with a vowel)
liaison("quis", "falar")               # 'quis'  (next word starts with a consonant)
```

Note these operate on a single already-tokenized word; `add_accent` handles
tokenization, normalization, and ordering for you.

## Syllables and stress

`silabas` exposes the stress model the diphthong rules rely on. It is useful on
its own for any pt-PT syllable/stress task:

```python
from sotaque_forcado.silabas import (
    split_into_syllables, identify_tonic_syllable, get_syllable_info,
)

split_into_syllables("trabalho")      # ['tra', 'ba', 'lho']
identify_tonic_syllable("trabalho")   # index of the stressed syllable
get_syllable_info("trabalho")         # [(start, end, syllable, is_tonic), ...]
```

## Phonemization is a separate tier

`add_accent` needs only the core requirements. `phonemize` additionally imports
`phonemizer` (lazily, inside the method) and needs a system `espeak-ng` backend.
Guard for it so the accenting path keeps working everywhere:

```python
s = Sotaque(os.path.join(presets, "algarvio.json"))
accented = s.add_accent("o meu sotaque é especial")
try:
    print(s.phonemize("o meu sotaque é especial"))
except Exception as exc:        # phonemizer / espeak-ng not installed
    print("IPA unavailable:", exc, "-- accented text:", accented)
```

## Gotchas

- **Normalization is implicit.** `add_accent` always capitalizes and appends a
  `.`/keeps a `?`, and rewrites digits to words. Output is a full sentence, not a
  verbatim echo of your input casing.
- **Paths to presets.** Resolve `os.path.dirname(sotaque_forcado.sotaques.__file__)`
  rather than hardcoding `sotaque_forcado/sotaques/...`, so it works regardless of
  the current working directory.
- **`phonemize` raises late.** Missing `phonemizer`/`espeak-ng` only bites when
  you call `phonemize`; everything else is independent of it.
- **Rules are token-local.** Apart from the liaison rule, each rule sees one word
  at a time, so multi-word context beyond the immediate next token is not modelled.

## Where next

- [quickstart.md](quickstart.md) — the 5-minute tour
- [api.md](api.md) — full signatures and return shapes
- [rules.md](rules.md) — the transformation catalogue
