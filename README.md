# Applied AI research

An independent personal applied AI research portfolio maintained by [Eran Baruch (GitHub: eranb007)](https://github.com/eranb007). The research was conducted under his direction, with AI-assisted research, analysis, code generation, documentation and review.

Under what conditions can language models take meaningful software-engineering responsibilities, and what evidence is needed before people rely on their outputs?

[Local LLM reliability in software-engineering workflows](studies/local-llm-reliability/README.md) is the first study. It draws on project-derived fixtures, repository excerpts and deterministic audits from a private development environment. This research preview presents selected historical observations, methods, explicit limits and offline aggregate checks. Primary experimental artifacts remain restricted.

## Archived release and citation

The first research preview is permanently archived at Zenodo: **[version DOI 10.5281/zenodo.23277567](https://doi.org/10.5281/zenodo.23277567)**. To cite this exact release, use the version DOI. The [concept DOI 10.5281/zenodo.23277566](https://doi.org/10.5281/zenodo.23277566) identifies the series of archived versions.

**Research author:** [Eran Baruch (ORCID: 0009-0005-6098-6283)](https://orcid.org/0009-0005-6098-6283). The archived snapshot corresponds to the [v0.1.0 GitHub release](https://github.com/eranb007/research/releases/tag/v0.1.0-research-preview), commit [`97ff53dcd75a`](https://github.com/eranb007/research/commit/97ff53dcd75aca2d81cc538652e2d42a2044a50c).

The [publication manifest](docs/publication-manifest.json) refers to the frozen v0.1.0 release payload. Subsequent citation-only updates on `main` do not alter that archived payload or its recorded hashes. Original experimental inference has not been independently reproduced.

## Findings within the available evidence

- **Admission did not establish correctness.** In the selected five-target editing task, GLM's main guarded proposal and Granite's reasoning-off rescue each had five admissions but four exact reference matches. Their selected assignments edits had result-shape failures: reading a promise before awaiting it, or returning an envelope instead of its array. Other selected proposals matched all five reference files; those matches do not certify behavior beyond the supplied task and checks. [Records and qualifications](studies/local-llm-reliability/results/README.md) (CLM-003, CLM-005).
- **Validators had bounded failure modes.** A later constructed, zero-inference audit exposed a target-only admission gap and comment-sensitive rejection. These were deliberately constructed probes, not new model responses or estimates of natural failure prevalence. A rejected proposal was not thereby proven semantically wrong. [Methods and controls](studies/local-llm-reliability/experiments.md) (CLM-007, CLM-022, CLM-023).
- **A finite oracle could miss an input-dependent failure.** A constructed mutant passed the checked input, then returned zero rows where a second controlled input required two. This establishes that particular coverage gap; it does not measure global reliability. [Evidence limits](studies/local-llm-reliability/limitations.md) (CLM-008).
- **Verification must address the task contract.** These observations motivate separate checks of delivery, exact scope, source and caller contracts, behavior and oracle coverage before human acceptance. A local PASS, a reference match or reviewer agreement cannot supply missing evidence. The public scripts check aggregate invariants and invented analogues; they do not reproduce original inference or certify historical source truth. [Reproducibility](studies/local-llm-reliability/reproducibility/README.md) (CLM-013, CLM-014, CLM-024, CLM-025).

At reconciliation v1.25, all 585 selected differing fields have bounded dispositions, with zero unreviewed selected fields and 152 bounded assessment units. This is curation progress, not 585 defects, independent samples or complete historical adjudication. Small, selected and correlated observations, unequal settings and incomplete scorer evidence prevent universal model rankings, causal prompt claims, production guarantees or measured savings.

Start with the [qualified results](studies/local-llm-reliability/results/README.md), [methodology](studies/local-llm-reliability/methodology.md), [limitations](studies/local-llm-reliability/limitations.md) and [article register](studies/local-llm-reliability/articles/README.md).

## Research principles

Preserve original measurements. Separate model observations, reviewer judgments, constructed counterexamples and infrastructure tests. Record missing evidence and disagreements. Verify mechanisms against source contracts. Interpret cost, latency and resources within their recorded conditions. Human owners remain accountable for integration and disclosure decisions.

RAG optimization, agent architectures and autonomous systems are future directions, not completed studies. Prospective Benchmark V2 is inactive and has no official result in this preview.

[Release notes](RELEASE_NOTES.md) · [Citation metadata](CITATION.cff) · [License scope](LICENSES/README.md) · [Publication policy](docs/publication-policy.md) · [Contributing](CONTRIBUTING.md)
