# API reference

Everything you import lives under three modules: `sotaque_forcado.sotaques`
(the driver), `sotaque_forcado.preprocessors` (the rule functions), and
`sotaque_forcado.silabas` / `sotaque_forcado.utils` (helpers).

## `sotaque_forcado.sotaques.Sotaque`

```python
class Sotaque:
    def __init__(self, config_file: str)
    def add_accent(self, text: str) -> str
    def phonemize(self, text: str) -> str
```

### `Sotaque(config_file)`

`config_file` is a path to a JSON file holding a flat `{rule_name: bool}` map.
The file is read once at construction and kept on `self.rules` (a `dict`); the
path is kept on `self.path`. `repr(s)` is `Sotaque(<basename without .json>)`.

```python
import os
import sotaque_forcado.sotaques as smod
from sotaque_forcado.sotaques import Sotaque

presets = os.path.dirname(smod.__file__)        # bundled .json presets
s = Sotaque(os.path.join(presets, "porto.json"))
s.rules            # {'substituicao_v_por_b': True, 'acentuacao_ditongos': True, ...}
repr(s)            # 'Sotaque(porto)'
```

### `add_accent(text) -> str`

The main entry point. Pipeline:

1. `utils.normalize(text)` — digits → words (`num2words`, `lang="pt"`), special
   chars stripped, first letter capitalized, trailing `.` added if no `.`/`?`.
2. `quebra_frases.word_tokenize` splits into tokens.
3. Each enabled rule is applied to every token, in a fixed internal order. One
   rule (`substituicao_de_z_por_j_ligacoes_palavras_acabadas_s_com_vogal`) also
   sees the next token, so cross-word liaisons work.
4. Tokens are re-joined with spaces.

Returns the rewritten, punctuated sentence:

```python
s.add_accent("quis entrar na piscina")     # 'Quij entrari nã piscinã .'  (algarvio)
```

Only the core requirements (`num2words`, `quebra_frases`, `pyphen`) are needed —
no `phonemizer`.

### `phonemize(text) -> str`

Runs `add_accent(text)`, then `phonemizer.phonemize(accented, language="pt")` and
returns the IPA string. The `phonemizer` import is local to the method, so it only
fails if you actually call `phonemize()` without the extra installed.

```python
s.phonemize("o meu sotaque é especial")     # 'ʊ me sutakɨ ɛ ʃpesiɑl ...'
```

## Bundled presets

`sotaque_forcado/sotaques/*.json` ships ready-made accents. Resolve their
directory from the module, never hardcode a path:

```python
import os, sotaque_forcado.sotaques as smod
presets = os.path.dirname(smod.__file__)
```

Available: `minho`, `minho_central`, `vimaranes`, `fafe`, `famalicao`, `porto`,
`viseu`, `lisboa`, `estremenho`, `beirao`, `alentejano`, `algarvio`, `azores`,
`madeirense`, `transmontano`, and `padrao` (the all-false template).

## `sotaque_forcado.preprocessors`

Each rule is a standalone function. Most take and return a single word:

```python
def substituicao_v_por_b(w: str) -> str          # 'vila' -> 'bila'
def substituicao_final_de_ar_por_a(w: str) -> str # 'passar' -> 'passá'
def apocope_do_o(w: str) -> str                   # 'fogo' -> 'fôgue'
def suavizacao_elh(w: str) -> str                 # 'coelho' -> 'coêlh'
```

Two signatures differ from the one-arg norm:

```python
def monotongacao(w: str, target_dits: Optional[List[str]] = None) -> str
def substituicao_de_z_por_j_ligacoes_palavras_acabadas_s_com_vogal(
        w: str, nextw: Optional[str]) -> str
```

- `monotongacao` collapses diphthongs (`ei`→`ê`, `ou`→`ô`, `ão`→`ã`, …). Pass
  `target_dits` to restrict which ones are touched.
- the liaison rule turns a trailing `s` into `j` when the next word starts with a
  vowel (`quis entrar` → `quij entrar`); hence the second `nextw` argument.

These are pure functions on plain strings — you can call them directly, outside
any `Sotaque`:

```python
from sotaque_forcado.preprocessors import substituicao_v_por_b, monotongacao
substituicao_v_por_b("a vila do velho varão".replace(" ", "_"))  # operate per word
monotongacao("maneira")                                          # 'manêra'
```

See [rules.md](rules.md) for the full catalogue.

## `sotaque_forcado.silabas`

Syllable utilities built on `pyphen` (`pt_PT`):

```python
def split_into_syllables(word: str) -> List[str]
def identify_tonic_syllable(syllables: List[str]) -> int
def identify_tonic_vowel(syllables: List[str]) -> Tuple[int, int]
def get_syllable_info(word: str) -> List[Tuple[int, int, str, bool]]
```

- `split_into_syllables("trabalho")` → `['tra', 'ba', 'lho']`.
- `identify_tonic_syllable` returns the index of the stressed syllable; it also
  accepts a word string and splits it for you.
- `identify_tonic_vowel` returns `(syllable_index, vowel_index_in_syllable)`.
- `get_syllable_info` returns one `(start, end, syllable, is_tonic)` tuple per
  syllable, with character offsets into the word.

```python
from sotaque_forcado.silabas import split_into_syllables, get_syllable_info
split_into_syllables("trabalho")     # ['tra', 'ba', 'lho']
get_syllable_info("trabalho")        # [(0, 3, 'tra', False), (3, 5, 'ba', True), ...]
```

## `sotaque_forcado.utils`

```python
def normalize(text: str) -> str
def convert_digits_to_words(data: str) -> str
def remove_special_chars(text: str) -> str
def replace_patterns(text: str) -> str
```

`normalize` is what `add_accent` calls first; the others are its stages.
`convert_digits_to_words` uses `num2words(..., lang="pt")`, so `"tenho 3 cães"`
becomes `"tenho três cães"`.

```python
from sotaque_forcado.utils import normalize
normalize("tenho 3 cães")            # 'Tenho três cães.'
```

## Where next

- [quickstart.md](quickstart.md) — the 5-minute tour
- [advanced.md](advanced.md) — custom presets, ordering, and gotchas
- [rules.md](rules.md) — every transformation function grouped by effect
