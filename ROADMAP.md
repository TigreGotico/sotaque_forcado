# Roadmap — sotaque_forcado

A **forced-dialect** phonemizer: given standard text, it coerces the output toward a
target regional accent/dialect. It pursues this two complementary ways:

1. **Text-level** — rewrite the orthographic text *before* G2P (an ordered set of
   ~45 accent-rewrite rules, e.g. `v`→`b`, `ou`→`oi`, final `ar`→`á`, paragoge,
   monophthongisation, driven by a per-accent JSON config), then run standard
   phonemization on the result. This is what ships today.
2. **Phoneme-level** — transform the *phonemes directly* after G2P (allophonic /
   dialectal substitutions on the IPA), independent of spelling. This is the second
   goal, and it maps directly onto [`orthography2ipa`](https://github.com/TigreGotico/orthography2ipa)'s
   allophone-map + dialect-transform machinery — so it should be built on that,
   not reinvented.

Accents shipped today: algarvio, alentejano, minho, minho_central, porto,
vimaranes, transmontano, beirão, viseu, estremenho, madeirense, azores, lisboa,
fafe, famalicão, and a padrão baseline.

**Why this exists — the research thesis.** Forced-dialect output is a *data
generator*. Paired with existing TTS models / `phoonnx`, it lets us **synthesize
speech in a target dialect or accent we have no recordings for**, producing
synthetic training corpora for **low-resource languages and dialects**. That is the
point of the project: data augmentation for under-resourced varieties, and a bridge
between the phonetics stack (`orthography2ipa`) and the synthesis stack (`phoonnx`).

## Phase 0 — Hardening

- Add `pyproject.toml` so the package installs (fold `requirements.txt` +
  `extras.txt`; `phonemizer` as an optional extra), add a `LICENSE` (compatible
  with the vendored Apache-2.0 code in `utils.py`, attribution preserved), and a
  `.gitignore`.
- Add the `OpenVoiceOS/gh-automations@dev` workflow set (build-tests, coverage,
  license_check, release_workflow, publish_stable, conventional-label).
- Repair the broken `test/test_syllables.py` placeholder assertions and bring the
  suite green so it can gate CI.

## Phase 1 — Correctness & coverage (text-level mode)

- Per-rule tests for `preprocessors.py` and per-accent end-to-end tests from the
  README worked examples (text → accented text → IPA).
- Close the three open rule TODOs (`preprocessors.py:239/278/300`): the messy
  transform, the `h`-already-present guard, and the `ái`/`ainda` distinction.
- Document the accent JSON schema and what each rule key toggles, so new accents
  can be added as data.

## Phase 2 — The phoneme-level mode (built on orthography2ipa)

- Add the second transformation path: apply dialect/allophone transforms **on the
  IPA**, reusing `orthography2ipa`'s allophone-map and dialect-transform model
  rather than a parallel rule engine. Each accent becomes an `orthography2ipa`
  dialect spec / transform set; `sotaque_forcado` orchestrates it.
- Keep both modes selectable and composable (text-level, phoneme-level, or both),
  with a clear API for "force accent X on this text/IPA."
- Align the IPA inventory and syllable handling with `silabificador` (reuse it
  instead of the in-repo `silabas.py`) and with `orthography2ipa`'s pt spec so the
  output validates against its tokenizer.
- Expose both modes as a `phoonnx` pt-PT regional-accent phonemizer backend
  (subclass `BasePhonemizer`, emit `Alphabet.IPA`, select via extended pt-PT region
  langcodes); coordinate with `tugaphone` so accent inventories aren't duplicated.

## Phase 3 — Synthetic data for low-resource languages (the payoff)

- Build the pipeline: **forced-dialect G2P → `phoonnx` synthesis → synthetic
  dialect/accent corpus → train** a dialect or low-resource voice. Document it as a
  reusable recipe (which base voice, which transform set, how much synthetic data).
- Generalize beyond pt-PT accents: any language pair where a well-resourced base +
  a transform set approximates an under-resourced variety (this is the engine
  behind regional Miro & Dii voices and endangered-language coverage).
- Per-accent / per-variety gold accent→IPA evaluation sets so transforms are scored,
  not eyeballed; measure synthetic-data quality against any real samples available.

## Phase 4 — Research & whitepapers

- Write up forced-dialect synthesis as a **low-resource data-augmentation method**:
  the two modes, when each is appropriate (text-level vs phoneme-level), and an
  evaluation of synthetic-data quality for training dialect/low-resource voices.
- Connect to the existing research line: the Lusophone phonemics series and the
  hybrid synthetic-TTS-dataset whitepaper — this is the dialect/low-resource
  companion method. File the draft under the workspace `research/` and cross-link
  `orthography2ipa` (phoneme transforms) and `phoonnx` (synthesis).

## Publishing

- Release to PyPI through the standard publish workflow after Phase 0.
