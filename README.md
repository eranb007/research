# Applied AI research

An independent personal applied AI research portfolio maintained by [Eran Baruch (GitHub: eranb007)](https://github.com/eranb007). The research was conducted under his direction, with AI-assisted research, analysis, code generation, documentation and review.

Under what conditions can language models take meaningful software-engineering responsibilities, and what evidence is needed before people rely on their outputs?

[Local LLM reliability in software-engineering workflows](studies/local-llm-reliability/README.md) is the first study. It draws on project-derived fixtures, repository excerpts and deterministic audits from a private development environment. This research preview presents selected historical observations, methods, explicit limits and offline aggregate checks. Primary experimental artifacts remain restricted.

## Published versions and citation

The **current series-closure archive** is published at Zenodo as [**v0.2.0-series-closure**](https://zenodo.org/records/23846229) — **[version DOI 10.5281/zenodo.23846229](https://doi.org/10.5281/zenodo.23846229)**, with publication date shown as 31 October 2026. The DOI represents the sanitized ZIP archive, not an independently reproduced inference experiment. The active [CITATION.cff](CITATION.cff) on `main` now cites this version and identifies its frozen source commit [`b29489e45f65`](https://github.com/eranb007/research/commit/b29489e45f6597a36c7cdb4ee3d42d7fa89c80b5). No GitHub Release or tag for v0.2.0 is asserted.

The v0.2.0 archive was assembled from 60 public allowlisted source files at the pinned commit with version-specific metadata. One absolute local Ollama blob path (`models[3].ordered_layers[0].from`) was removed *only from the distributed derivative* of `studies/local-llm-final-completion/data/BUNDLE_IDENTITIES.json`; its adjacent model layer digest and all scientific results were retained. The release-validation ZIP SHA-256 was reported as `3cd3aec782b083b28ac704a99b45aa48ce63bb8e266c113c0e324ec2f60eaf13`; the Zenodo-hosted bytes were not separately downloaded and hashed in this repository update. The frozen `docs/publication-manifest.json` remains the historic v0.1.0 manifest, not a v0.2.0 file list.

The first research preview is permanently archived at Zenodo: **[version DOI 10.5281/zenodo.23277567](https://doi.org/10.5281/zenodo.23277567)**. To cite this exact release, use the version DOI. The [concept DOI 10.5281/zenodo.23277566](https://doi.org/10.5281/zenodo.23277566) identifies the series of archived versions.

**Research author:** [Eran Baruch (ORCID: 0009-0005-6098-6283)](https://orcid.org/0009-0005-6098-6283). The repository records associate that archive with the [v0.1.0 GitHub release](https://github.com/eranb007/research/releases/tag/v0.1.0-research-preview), commit [`97ff53dcd75a`](https://github.com/eranb007/research/commit/97ff53dcd75aca2d81cc538652e2d42a2044a50c).

The [publication manifest](docs/publication-manifest.json) refers to the frozen v0.1.0 release payload. Subsequent citation-only updates on `main` do not alter that archived payload or its recorded hashes. Original experimental inference has not been independently reproduced. Exact Zenodo archive-byte equivalence was not independently verified by this bounded documentation closure; existing DOI/citation records are retained rather than replaced.

## Findings within the available evidence

- **Admission did not establish correctness.** The recovered derived matrix records five admissions but four exact reference matches for GLM's main guarded proposal and Granite's reasoning-off rescue in the selected five-target editing task. This is checked documentary agreement, not independent verification of the unavailable original responses or proofs. The retained matrix describes selected result-shape failures: reading a promise before awaiting it, or returning an envelope instead of its array. Original proof bodies were not recovered and were not independently rerun. Other selected proposals matched all five reference files; those matches do not certify behavior beyond the supplied task and checks. [Records and qualifications](studies/local-llm-reliability/results/README.md) (CLM-003, CLM-005).
- **Documented validator boundaries and separate illustrations.** Retained historical documentation reports a later constructed, zero-inference audit of a target-only admission gap and comment-sensitive rejection; its original validator/control source was not recovered or independently replayed. The recovered public invented examples demonstrate only their separately constructed finite mechanisms. Neither the historical documentary account nor those illustrative controls establish a natural model-failure prevalence. A rejected proposal was not thereby proven semantically wrong. [Methods and controls](studies/local-llm-reliability/experiments.md) (CLM-007, CLM-022, CLM-023).
- **A finite oracle could miss an input-dependent failure.** Retained documentation describes a constructed mutant that passed a checked input and failed a second-input challenge. The exact historical mutant/oracle source was not recovered; the public invented example is a separate illustration. The retained account documents a historical coverage claim, not independent verification of the missing historical mutant or oracle. The recovered public illustrative control establishes a coverage gap only in its own invented example; it does not reproduce that historical source or measure global reliability. [Evidence limits](studies/local-llm-reliability/limitations.md) (CLM-008).
- **Verification must address the task contract.** These observations motivate separate checks of delivery, exact scope, source and caller contracts, behavior and oracle coverage before human acceptance. A local PASS, a reference match or reviewer agreement cannot supply missing evidence. The public scripts check aggregate invariants and invented analogues; they do not reproduce original inference or certify historical source truth. [Reproducibility](studies/local-llm-reliability/reproducibility/README.md) (CLM-013, CLM-014, CLM-024, CLM-025).

At reconciliation v1.25, all 585 selected differing fields have bounded dispositions, with zero unreviewed selected fields and 152 bounded assessment units. This is curation progress, not 585 defects, independent samples or complete historical adjudication. Small, selected and correlated observations, unequal settings and incomplete scorer evidence prevent universal model rankings, causal prompt claims, production guarantees or measured savings.

Start with the [qualified results](studies/local-llm-reliability/results/README.md), [methodology](studies/local-llm-reliability/methodology.md), [limitations](studies/local-llm-reliability/limitations.md) and [article register](studies/local-llm-reliability/articles/README.md).

## Research principles

Preserve original measurements. Separate model observations, reviewer judgments, constructed counterexamples and infrastructure tests. Record missing evidence and disagreements. Verify mechanisms against source contracts. Interpret cost, latency and resources within their recorded conditions. Human owners remain accountable for integration and disclosure decisions.

RAG optimization, agent architectures and autonomous systems are future directions, not completed studies. Prospective Benchmark V2 is inactive and has no official result in this preview.

[Release notes](RELEASE_NOTES.md) · [Citation metadata](CITATION.cff) · [License scope](LICENSES/README.md) · [Publication policy](docs/publication-policy.md) · [Contributing](CONTRIBUTING.md)


## V1 evidence-availability correction record

The [V1 errata](studies/local-llm-reliability/corrections/V1_ERRATA.md) qualify the historical summaries above. The Git commit and ref containing this record identify its repository version. Availability on GitHub does not itself verify a LinkedIn article-body correction, an external correction URL or a publication event date. Those require separate evidence. The earlier Part 4 HOLD has been superseded by an author-reported LinkedIn publication on 31 October 2026; see the [article register](studies/local-llm-reliability/articles/README.md). In particular, original source bytes were not recovered for 42 catalog entries (35 distinct hashes). Retained matrices and invented offline analogues do not establish recovery or replay of those originals. Earlier narrative statements about inspected proofs or restricted original evidence must be read with this correction. The archived v0.1.0 release is preserved unchanged.


## Final prospective comparison — separate from V1

The [final research companion](studies/local-llm-final-completion/README.md) reports a separate seven-bundle, twelve-case, two-seed experiment: 168 planned units, 164 attempts, 163 delivered outputs, one HTTP 500 and four unexecuted units. Primary full-task successes are 90/168; primary behavior is 102 correct, 47 incorrect and 19 missing. Fourteen delivered B outputs lack behavior verdicts. Review is AI/nonblind; the extraction-sensitive alternative is conditional only. These observations do not establish a general ranking, production reliability, hardware performance or independent replication. V1 corrections accompany the series closure.


## Part 4 — LinkedIn publication

The author confirmed publishing [**Who Validates the AI Validator?**](https://www.linkedin.com/pulse/who-validates-ai-validator-eran-baruch-zexnf) as Part 4 of *Beyond the Local AI Hype* on **31 October 2026**. The [article register](studies/local-llm-reliability/articles/README.md) records the supplied destination and separates this owner-confirmed event from independent verification of the exact LinkedIn article body and timestamp. This publication does not change frozen scientific results, earlier release/DOI artifacts or the status of uninserted LinkedIn V1 correction notices.
