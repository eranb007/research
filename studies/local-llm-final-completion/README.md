# Final local-model comparison: output correctness and evidence limits

Study **LOCAL-LLM-FINAL-COMPLETION**; campaign **FC-SCORED-20261028-R1**. Prepared 30 October 2026 as a proposed public research companion. This is a descriptive, bounded experiment on recorded model-artifact/runtime bundles, not a universal model leaderboard or an independent replication of V1.

## Questions and design

The study asks how the registered bundles satisfy finite engineering contracts, how task compliance differs from behavioral correctness, and where deterministic checks and AI review disagree. Seven bundles each received twelve related purpose-built cases at seeds 101 and 202: **168 planned scored units**. Two seeds do not turn the twelve cases into 168 independent tasks. Tasks, reference answers, scoring contracts and the registry were frozen before scored execution. The earlier closed preparation study is not this executed campaign.

Four B cases test bounded source edits, four C cases test/oracle reasoning, and four D cases static dependency analysis. Family C requires classifying the supplied implementations as defective or equivalent over each stated finite domain and proposing one to eight valid test vectors that collectively distinguish every defective implementation; equivalent implementations must not be mislabeled. These are not transformation-function generation tasks. [Case overview](data/CASE_OVERVIEW.csv) gives the twelve finite scopes. B preserves unrelated source and original sync/async contracts. C is not a security test; D is a small supplied static graph, not a dynamic inventory of a production repository. Historical anchors motivate selected constructs; they do not reproduce unavailable historical responses.

The [bundle identities](data/BUNDLE_IDENTITIES.json) preserve tags, Q4_K_M manifests, layer identities and observed runtime profiles. The environment used an RTX 3090 with 24 GB VRAM and pinned Ollama 0.40.1. [Request conditions](data/REQUEST_CONDITIONS.json) preserve parameter metadata. Fixed request conditions do not make all internal model profiles or historical weights equivalent. Ordinary Windows display activity was recorded as metadata; physical host/GPU exclusivity was not established. No latency, throughput or efficiency comparison is claimed.

The result tables use registered human-readable model labels. Actual request identifiers for M2, M3 and M7 are the content-addressed llamacpp aliases explicitly mapped in BUNDLE_IDENTITIES.json; the other four use their registered tags. The labels must not be mistaken for an unverified live tag resolution or historical artifact equivalence.

Registered profiles retain target-model MTP with draft maximum 4 for Qwen3.8; no equivalent MTP condition is asserted for the others. Batch/ubatch is 1024 for Gemma12B and Devstral, 512 for the other five bundles. These are disclosed bundle conditions, not a matched weights-only or architecture-controlled comparison.

## Execution and primary results

**164 native client model requests were attempted in frozen order: 163 were delivered and profile-verified, one returned HTTP 500, and four remained NOT_EXECUTED.** There were zero client retries, no replay and one owned server. The failing request had one additional internal model-load retry. Its effective profile was not established; allocation failures and concurrent host-memory pressure were recorded, without a proven causal attribution. GLOBAL_STOP is preserved. The four unexecuted units are B1 at seed 202 for M6, M7, M1 and M2. They are retained in the 168-row [primary data](data/PRIMARY_OBSERVATIONS.csv).

Full-task outcomes are **90 K, 74 F and 4 operational U out of 168 planned units**. K means full frozen contract success. F includes 73 delivered task failures and one operational HTTP failure; F is not a semantic incompetence label. Operational U denotes unexecuted units. Primary behavior is **102 C, 47 I, zero explicit semantic U and 19 M out of 168**. C/I are recorded behavior-correct/incorrect; M means missing behavior evidence. The 19 M comprise fourteen delivered B outputs, the HTTP failure and four unexecuted units. These categories must not be conflated.

Thus 102/149 is conditional on having a recorded behavior verdict, not an all-planned accuracy. The frozen planned-denominator behavior interval is [102/168, 121/168]; it is a missingness bound, not a confidence interval. Full-task operational bounds are [90/168, 94/168]. No statistical-significance or population-prevalence claim follows.

## B-family missingness and review

Of **51 delivered B answers**, 37 have a primary behavior verdict (34 correct, 3 incorrect); **14 lack one** (12 NO_CODE, 2 NO_UNIQUE_EXTRACTION). These are frozen extraction statuses: NO_CODE does not prove the response contained no source. Four missing-behavior answers were sampled in Review B; **ten were not reviewed**. Ten of the 37 verdict-bearing B answers were sampled; 27 were not. All three recorded B-incorrect answers were outside that sample. The [missingness table](data/B_MISSING_BEHAVIOR.csv) preserves the distinction; missing evidence is neither a model error nor an explicit unknown judgment.

Review B used the preregistered 42-unit selection, two per model/family stratum, with zero mandatory B-UNKNOWN additions under the literal trigger. AI source-first review agreed with task scoring on 42/42 units. Behavior agreed on 38 jointly resolved units; three remained mutually unresolved. One extraction-rule disagreement, S101-B4-M6, remains unresolved. The frozen primary scorer could not uniquely extract the behavior candidate. The reviewer accepted a weaker literal extraction interpretation. S101-B4-M6 remains an unresolved extraction-rule interpretation, not a proven primary-scoring error. Original primary scores remain authoritative.

Only the frozen **conditional sensitivity** uses that alternative: reviewed-sample behavior-correct 29→30; overall behavior-correct 102→103; full-task correctness unchanged. Conditional U=3 and M=15 do not replace primary U=0 and M=19. The behavior-analysis denominator D changes from 149 to 153 because D includes the three explicit unresolved judgments and excludes missing results; the planned denominator remains 168. This changed coverage does not establish improved model accuracy. This is not a corrected primary result. The conditional structural-proxy disagreement count is 7/39, including one extraction-sensitive result; it is not a general validator error rate.

The same AI reviewer had prior exposure; the review was nonblind and substantive reviewer independence is unestablished. It was not human adjudication. Technical review verified all 36,515 archived payloads on both evidence volumes and reproduced the eleven primary and eleven conditional analysis payloads byte-for-byte. This establishes evidence/analysis consistency within the retained record, not independent model-experiment replication. The newly written companion/article was not itself certified by that earlier review.

## Interpretation and reproducibility

The tables below describe only these observed bundles and tasks. Differences can reflect contract handling, task family, extraction and runtime conditions. The evidence supports separating delivery, structural compliance, behavior and missingness; it does not establish vendor or architecture superiority, production/security reliability, autonomous engineering, measured productivity or savings.

The [scoring and limitations](SCORING_AND_LIMITATIONS.md), [reproducibility boundary](REPRODUCIBILITY.md) and [source identities](EVIDENCE_BOUNDARY.md) are integral to this companion. Public derived counts can be recomputed from the selected-field data. Private raw inputs/outputs, scorers and reviewer bodies are not released, so public end-to-end scoring reproduction is not claimed. The [published V1 corrections](https://github.com/eranb007/research/blob/main/studies/local-llm-reliability/corrections/V1_ERRATA.md) accompany the series; their public content was verified after the Phase A merge. LinkedIn correction notices remain separate, uninserted templates requiring their own authorization. The new results do not fill historical source gaps. Phase B and Part 4 have no publication authorization in this editorial package.

The table keys use the frozen analysis vocabulary: planned, attempted, delivered; K full-task success, F task/operational failure, operational_U unexecuted; C behavior-correct, I behavior-incorrect, M missing behavior. Every model has 24 planned units; each family has 56. Explicit semantic U is zero in every primary group.


## Results by recorded bundle

| model_id | planned | attempted | delivered | K | F | operational_U | C | I | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gemma4:12b | 24 | 23 | 23 | 15 | 8 | 1 | 17 | 6 | 1 |
| gemma4:31b | 24 | 23 | 23 | 23 | 0 | 1 | 23 | 0 | 1 |
| glm-4.7-flash:q4_K_M | 24 | 24 | 24 | 7 | 17 | 0 | 8 | 12 | 4 |
| granite4.2:30b | 24 | 24 | 24 | 8 | 16 | 0 | 10 | 8 | 6 |
| qwen3.8:27b | 24 | 24 | 23 | 22 | 2 | 0 | 22 | 1 | 1 |
| qwen3-coder:30b | 24 | 23 | 23 | 11 | 12 | 1 | 11 | 8 | 5 |
| devstral-small-2:24b | 24 | 23 | 23 | 4 | 19 | 1 | 11 | 12 | 1 |

## Results by family

| family | planned | attempted | delivered | K | F | operational_U | C | I | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B | 56 | 52 | 51 | 27 | 25 | 4 | 34 | 3 | 19 |
| C | 56 | 56 | 56 | 44 | 12 | 0 | 44 | 12 | 0 |
| D | 56 | 56 | 56 | 19 | 37 | 0 | 24 | 32 | 0 |
