# TODO — sotaque_forcado

A European-Portuguese regional-accent phonemizer. The `Sotaque` class loads a
per-accent JSON config (algarvio, alentejano, minho, porto, transmontano,
madeirense, azores, and more), applies ~45 ordered accent-rewrite rules
(`preprocessors.py`), then phonemizes the accented text to IPA.

## Hardening (CI / packaging / hygiene)

- [ ] Add packaging: there is no `pyproject.toml` or `setup.py`, so the package is not installable. Dependencies are split across `requirements.txt` (`num2words`, `quebra_frases`, `pyphen`) and `extras.txt` (`phonemizer`) — fold them into `pyproject.toml` (the `phonemizer` backend as an optional extra).
- [ ] Add the standard `OpenVoiceOS/gh-automations@dev` workflows: `build-tests`, `coverage`, `license_check`, `release_workflow`, `publish_stable`, `conventional-label`. The repo has no `.github/workflows/`.
- [ ] Add a `LICENSE` file. `sotaque_forcado/utils.py` vendors Apache-2.0 code from `my-north-ai/semantic_audio_filtering`; the chosen license must be compatible and the vendored attribution preserved.
- [ ] Add a `.gitignore` (`__pycache__`, build/dist, egg-info).

## Correctness gaps

- [ ] The test suite is broken: `test/test_syllables.py::test_split_into_syllables` asserts `olho`, `livro`, and `formiga` all equal `['ca', 'fé']` (placeholder copy-paste). Fix the expected values so the suite passes.
- [ ] Coverage is thin: only syllable / ditongation helpers are tested. The ~45 accent rules in `preprocessors.py` and the `Sotaque` class (`add_accent`, `phonemize`) are untested — add per-rule and per-accent tests from the README worked examples.
- [ ] `test.py` at the repo root is an unstructured demo, not part of the suite; fold its sentences into the test suite or move it under `examples/`.

## Code TODOs

- [ ] `sotaque_forcado/preprocessors.py:239` — rule "can be improved" (cleanup of the messy transform).
- [ ] `sotaque_forcado/preprocessors.py:278` — don't insert `h` if the next letter is already `h`.
- [ ] `sotaque_forcado/preprocessors.py:300` — distinguish `ái`→`á` from the `ai` in `ainda` (must not be modified).
