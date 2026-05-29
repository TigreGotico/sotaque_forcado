# Roadmap — sotaque_forcado

A European-Portuguese regional-accent phonemizer. Given standard pt-PT text, the
`Sotaque` class applies an ordered set of ~45 accent-rewrite rules (e.g.
`v`→`b`, `ou`→`oi`, final `ar`→`á`, paragoge, monophthongisation) driven by a
per-accent JSON config, then phonemizes the result to IPA. Accents shipped today
include algarvio, alentejano, minho, minho_central, porto, vimaranes,
transmontano, beirão, viseu, estremenho, madeirense, azores, lisboa, fafe,
famalicão, and a padrão baseline.

## Phase 0 — Hardening

- Add `pyproject.toml` so the package installs (fold `requirements.txt` +
  `extras.txt`; `phonemizer` as an optional extra), add a `LICENSE` (compatible
  with the vendored Apache-2.0 code in `utils.py`, attribution preserved), and add
  a `.gitignore`.
- Add the `OpenVoiceOS/gh-automations@dev` workflow set (build-tests, coverage,
  license_check, release_workflow, publish_stable, conventional-label).
- Repair the broken `test/test_syllables.py` placeholder assertions and bring the
  suite green so it can gate CI.

## Phase 1 — Correctness & coverage

- Add per-rule tests for `preprocessors.py` and per-accent end-to-end tests from
  the README worked examples (text → accented text → IPA).
- Close the three open rule TODOs (`preprocessors.py:239/278/300`): the messy
  transform, the `h`-already-present guard, and the `ái`/`ainda` distinction.
- Document the accent JSON schema and what each rule key toggles, so new accents
  can be added as data.

## Phase 2 — Integration

- Expose it as a `phoonnx` phonemizer backend covering pt-PT regional accents:
  add a module under `phoonnx/phonemizers/` subclassing `BasePhonemizer`, emitting
  `Alphabet.IPA`, selected via extended pt-PT region langcodes (mirroring how
  `tugaphone` already advertises `pt-PT-x-porto`-style variants).
- Coordinate with `tugaphone`, which also models pt-PT regional accents: decide
  whether `sotaque_forcado`'s rewrite rules feed `tugaphone`'s regional layer or
  remain a standalone accent front end, and avoid duplicating accent inventories.
- Align the IPA inventory and syllable handling with `silabificador` (reuse it
  instead of the in-repo `silabas.py`) and with `orthography2ipa`'s pt spec so the
  output validates against its tokenizer.

## Phase 3 — Datasets & publishing

- Build a small gold accent→IPA evaluation set per accent so rule changes can be
  scored rather than eyeballed.
- Release to PyPI through the standard publish workflow after Phase 0.
