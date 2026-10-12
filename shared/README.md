# Shared research kit

This directory contains reusable research infrastructure and methodological conventions that are independent of any single study.

## Scope

Shared material may define:

- evidence and provenance rules;
- experiment and artifact schemas;
- preregistration conventions;
- reproducibility and repeatability controls;
- adjudication and disagreement handling;
- publication and disclosure conventions;
- reusable tooling.

Study-specific hypotheses, raw observations, analysis and conclusions belong under `studies/<study-id>/`.

## Invariants

1. Preserve original measurements and raw evidence.
2. Separate observation from interpretation and adjudication.
3. Record missing evidence explicitly.
4. Freeze protocols before confirmatory runs.
5. Keep constructed probes distinct from natural observations.
6. Do not treat automated judgment as ground truth without validation.
7. Preserve study boundaries: evidence from one study is not silently promoted into another.

The archived v0.1.0 research preview and its publication manifest remain historical publication artifacts and are not rewritten by this platform organization.
