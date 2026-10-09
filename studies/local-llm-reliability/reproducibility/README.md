# Reproducibility inventory

| Component | Demonstrated scope | Required material / limits |
| --- | --- | --- |
| September bounded edits | Level 1 qualified summary | Released selected CSV; original prompts, outputs, fixtures and scorer restricted |
| October experiments / source tasks | Level 1 methodology summary | Designs and limits inspectable; private snapshots and original oracles withheld |
| Reconciliation ledger | Level 1 aggregate summary | Coverage and evidence identities; original judgments/source join not publicly replayable |
| Aggregate checks | Level 2 for this derived procedure | Python 3.11+, standard library; schema, record identities, domains and cross-field invariants only |
| Boundary analogue | Level 2 for invented examples | Three mechanisms and counterpart controls; no model, original scorer or private application |
| Coverage figure | Level 2 for this derived figure | Python 3.11+, matplotlib 3.9.2, validated coverage CSV |
| Original independent experiment reproduction | Level 3 not demonstrated | Rights-cleared tasks, exact artifacts, runtime, audited scorers and an independent rerun would be required |

From the repository root:

~~~sh
python -B studies/local-llm-reliability/reproducibility/check.py
python -B -O studies/local-llm-reliability/reproducibility/check.py
python -B studies/local-llm-reliability/reproducibility/boundary_demo.py
python -B studies/local-llm-reliability/reproducibility/test_validation.py
python -B -O studies/local-llm-reliability/reproducibility/test_validation.py
~~~

[expected.json](expected.json) gives valid-data outputs. The tests invoke the checker as a separate process under both normal Python and Python -O, mutating temporary copies only. Invalid input must exit nonzero, emit status FAIL and never emit PASS. Positive controls preserve documented UNKNOWN values. Boundary-control regressions must also fail in both modes. Tests use unittest checks, which remain active with optimization; runtime scripts contain no assertion-based validation.

check.py accepts an optional --data-dir directory and only reads it. It refuses wrong/duplicate headers, absent/surplus columns or records, malformed counts, unsupported identities/settings and cross-field contradictions. A structurally consistent fabricated count could still pass: this is not an authenticity check or a substitute for evidence review. Exact payload hashes detect changes against the sealed package. The boundary analogue is invented and establishes no historical model result.

Python 3.11.4 was used for local verification; other versions are not claimed tested. These checks require no GPU, network or dependency installation and write no evidence.

Optional regeneration, using the pinned requirement in your own environment:

~~~sh
python -B studies/local-llm-reliability/reproducibility/plot_coverage.py
~~~

The plotter validates the coverage CSV before writing the two figure exports. Fonts/platforms can change rendering and output bytes. It uses already available matplotlib 3.9.2; no third-party source, font binary or branding asset is distributed.
