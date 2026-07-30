# Rule catalogue

The rules in `sotaque_forcado.preprocessors` are the building blocks of every
accent. Each is a pure function: a word in, a transformed word out (two rules also
take context, see below). A preset is just a set of these switched on.

Group them by the kind of change they make.

## Consonant substitutions

| Rule | Effect | Example |
| --- | --- | --- |
| `substituicao_v_por_b` | `v` → `b` | vila → bila |
| `substituicao_de_z_por_j` | `z` → `j`, intensifies `esu` | Jesus → Jejus |
| `substituicao_de_z_por_x` | `z` → `x` | zebra → xebra |
| `substituicao_de_s_por_x` | `ss`/`s`/`c` → `x` | passo → paxo |
| `substituicao_de_ch_por_tch` | strengthen `ch` → `tch` | chão → tchão |
| `substituicao_de_al_por_aur` | `al` → `aur` | alguidar → aurguidar |
| `s_reverso` | `s` → `z` between/after vowels | moço → mozo |
| `z_reverso` | `z` → `s` at word edges | zona → sona |

## Vowel and diphthong changes

| Rule | Effect | Example |
| --- | --- | --- |
| `substituicao_de_ou_por_oi` | `ou` → `oi` | outro → oitro |
| `monotongacao` | collapse diphthongs (`ei`→`ê`, `ou`→`ô`, `ão`→`ã`, …) | maneira → manêra |
| `monotongacao_ei_para_ai` | `ei` → `âi` | leite → lâite |
| `abrir_ditongos` | open diphthongs | mãe → mánhe |
| `acentuacao_ditongos` | accent diphthongs | eu → ieu |
| `ditongacao_vogal_tonica_com_u` | insert `u` before tonic vowel | olho → uôlho |
| `ditongacao_crescente` | rising diphthong | porto → puorto |
| `ditongacao_do_e_para_eu` | `e` between consonants → `eu` | treze → treuze |
| `u_frances` | French-style `u` | tu → tiú |
| `substituicao_a_para_e_antes_de_nasal` | `a` → `ê` before nasals | pestana → pestêna |

## Word endings

| Rule | Effect | Example |
| --- | --- | --- |
| `substituicao_final_de_ar_por_a` | final `ar` → `á` | passar → passá |
| `substituicao_final_de_o_por_e` | final `o` → `e` | osso → osse |
| `substituicao_final_de_oi_por_u` | final `oi` → `û` | boi → bû |
| `substituicao_final_de_am_por_u` | final `am` → `u` | foram → fôru |
| `substituicao_final_de_ao_por_oum` | final `ão` → `oum` | pão → poum |
| `substituicao_final_de_agem_por_aije` | `agem` → `aije` | viagem → viaije |
| `substituicao_final_de_agem_por_age` | `agem` → `age` | viagem → viage |
| `substituicao_de_ae_por_an` | `ães` → `ân` | cães → cãns |
| `substituicao_de_oe_por_on` | `ões` → `ôns` | leões → leôns |
| `substituicao_de_en_por_ein` | `en` → `éin` | casamento → casameinto |
| `paragoge_em_i` | add `i` after final `r` | fazer → fazêri |
| `paragoge_em_e` | keep final `e` in verbs | comer → comêre |
| `paragoge_em_e_apos_z` | add `e` after final `z` | nariz → narize |

## The `elh` family

| Rule | Effect | Example |
| --- | --- | --- |
| `substituicao_de_elh_por_alh` | `elh` → `âlh` | coelho → coâlho |
| `acentuacao_elh` | `elh` → `eilh` | coelho → coeilho |
| `suavizacao_elh` | `elh` → `êlh` | coelho → coêlh |
| `acentuacao_ach` | insert `i` before `ach` | bolacha → bolaicha |

## Deletions and reductions

| Rule | Effect | Example |
| --- | --- | --- |
| `apocope_do_o` | drop final `o` | fogo → fôgue |
| `perda_do_u_final_depois_de_i` | drop final `u` after `i` | viu → vi |
| `perda_do_i_entre_consoantes` | drop `i` between consonants | Filipe → Flipe |
| `perda_silaba_intermedia_palavras_esdruxulas` | drop middle syllable of proparoxytones | capítulo → capito |
| `perda_som_o_masculino_quando_passado_plural` | keep tonic `ô` in plural/feminine | ovos → ôvos |

## Nasal emphasis and whole-word swaps

| Rule | Effect | Example |
| --- | --- | --- |
| `enfase_anasalado_final_com_a` | nasal emphasis with `a` | o quê → o quâ |
| `enfase_anasalado_final_com_e` | nasal emphasis with `e` | bem → bêm |
| `palatizacao_consoante_l_antecedida_por_i` | palatalize `l` after `i` | vila → vilha |
| `substituicao_nao_por_num` | `não` → `num` | não quero → num quero |
| `substituicao_como_por_cumo` | `como` → `cumo` | como → cumo |
| `dezoito_com_acento` | `dezoito` → `dezóito` | dezoito → dezóito |

## Context-aware rules

Two rules take more than one argument because they need neighbouring context:

```python
def monotongacao(w: str, target_dits: Optional[List[str]] = None) -> str
def substituicao_de_z_por_j_ligacoes_palavras_acabadas_s_com_vogal(
        w: str, nextw: Optional[str]) -> str
```

- `monotongacao` accepts `target_dits` to limit which diphthongs are collapsed.
  With no argument it collapses all it knows.
- the liaison rule turns a trailing `s` into `j` only when `nextw` starts with a
  vowel, e.g. `("quis", "entrar")` → `quij`, but `("quis", "falar")` → `quis`.

Inside `add_accent`, the liaison rule is fed the next token automatically. The
others all receive a single word.

## Where next

- [quickstart.md](quickstart.md): the 5-minute tour
- [api.md](api.md): `Sotaque`, helpers, and signatures
- [advanced.md](advanced.md): building presets and calling rules directly

---
[← Advanced](advanced.md) · [Home](../README.md)
