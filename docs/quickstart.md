# Quickstart — zero to sotaque

`sotaque_forcado` rewrites standard pt-PT text into a regional Portuguese accent,
then (optionally) turns the accented text into IPA. The core idea is a single
class — `Sotaque` — driven by a flat JSON file of rule switches.

## 1. Install

The package is used in-tree (import `sotaque_forcado`), not pip-installed:

```bash
pip install -r requirements.txt   # num2words, quebra_frases, pyphen
pip install -r extras.txt         # phonemizer — only for phonemize(), pulls an espeak backend
```

`add_accent()` works with the core requirements alone. `phonemize()` additionally
needs `phonemizer` plus a system `espeak-ng` backend.

## 2. The one thing to understand

A `Sotaque` is a bundle of rules. Each rule is a small text transformation
(`v` → `b`, final `ar` → `á`, …). You point `Sotaque` at a JSON file that turns
rules on or off; `add_accent()` then walks the text word by word and applies every
enabled rule in a fixed order.

```python
import os
import sotaque_forcado.sotaques as smod
from sotaque_forcado.sotaques import Sotaque

# the bundled presets live next to the Sotaque class
presets = os.path.dirname(smod.__file__)

s = Sotaque(os.path.join(presets, "algarvio.json"))
print(repr(s))                                   # Sotaque(algarvio)
print(s.add_accent("o Ronaldo deixou cair o chouriço ao chão"))
# O Ronald dêxô caíri o chôriç ao chã .
```

`add_accent()` always normalizes first: digits become words, the text is
capitalized, and a trailing `.` is added if there is no `.`/`?` already. So the
output is a clean, punctuated sentence.

## 3. First real call

Pick any bundled accent and run a sentence through it:

```python
import os
import sotaque_forcado.sotaques as smod
from sotaque_forcado.sotaques import Sotaque

presets = os.path.dirname(smod.__file__)
s = Sotaque(os.path.join(presets, "transmontano.json"))

for sent in ["isso dá azar", "faz boa viagem", "que deus te ajude"]:
    print(sent, "->", s.add_accent(sent))
```

## 4. From accent to IPA

`phonemize()` runs `add_accent()` and then hands the result to `phonemizer`
(`language="pt"`), so you get IPA for the *accented* text, not the standard form:

```python
s = Sotaque(os.path.join(presets, "algarvio.json"))
print(s.phonemize("o meu sotaque é especial"))
# ʊ me sutakɨ ɛ ʃpesiɑl ...
```

If `phonemizer`/`espeak-ng` is not installed, the import inside `phonemize()`
raises — `add_accent()` keeps working regardless.

## 5. Roll your own accent

A preset is just a flat `{"rule_name": true}` map. Copy the all-false template
`sotaques/padrao.json`, flip the rules you want, and load it:

```python
import json, tempfile, os
from sotaque_forcado.sotaques import Sotaque

cfg = {"substituicao_v_por_b": True, "acentuacao_ditongos": True}
path = os.path.join(tempfile.mkdtemp(), "meu_sotaque.json")
with open(path, "w") as f:
    json.dump(cfg, f)

s = Sotaque(path)
print(s.add_accent("a vila tem um velho varão"))
```

## Where next

- [api.md](api.md) — `Sotaque`, every rule key, and the syllable helpers with real signatures
- [advanced.md](advanced.md) — building custom presets, rule ordering, and gotchas
- [rules.md](rules.md) — the catalogue of transformation functions, grouped
