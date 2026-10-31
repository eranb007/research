# Who Validates the AI Validator?

**I Tested the System That Was Judging My AI Models.**

Part 4 — Beyond the Local AI Hype. Editorial review copy for owner text approval; not a publication receipt.

<!-- P4-01 -->

I started this series by asking how much I could trust local AI models with engineering work. By the end, I had to ask the same question about the system judging their answers. A convincing response was not enough, but neither was a reassuring score. Before I could rely on either, I needed to know what the evaluator had checked, what it had failed to establish, and how much uncertainty its verdict concealed.

## What my checks actually measured

<!-- P4-02 -->

The retained editing matrix made that distinction concrete. Selected Coder and Qwen3.8 guarded records each show five admissions and five reference-file matches. GLM's main record and Granite's separate reasoning-off rescue each show five admissions but four matches. Admission and reference agreement were different measurements. The matrix also describes result-shape failures, but the original response and proof bodies were not recovered in the bounded audit. I can report the documentary record; I cannot present those unavailable historical proofs as independently rerun experiments.

<!-- P4-03 -->

The historical audit accounts went further: a comment-sensitive rejection, and a constructed mutant that passed checked inputs but failed a later input. Those accounts pointed to limits worth investigating. Their original validator, control and mutant sources were not recovered, so they remain qualified documentary evidence. The separately recovered public illustrative controls demonstrate their own finite mechanisms. They are neither recovered historical proof nor naturally occurring model responses, and they do not measure how often a validator fails.

<!-- P4-04 -->

That left me with several questions to keep separate. Did the response arrive completely? Did it satisfy the required format and editing boundary? Could the behavior be evaluated under the frozen extraction rule? Did it behave correctly within the stated domain? An answer could satisfy one layer and fail another. If I compressed those layers into a single success label, I would make the checker look more informative than its evidence allowed.

<!-- P4-05 -->

For the separate prospective experiment, I made those distinctions explicit. Family B covered bounded code edits. Family C was test/oracle reasoning: classify the supplied implementations as defective or equivalent over a finite domain, then propose valid test vectors that distinguish all defective implementations without condemning equivalent ones. It was not simply a request to generate a transformation function. Family D covered static dependency analysis over small supplied source graphs. These were deliberately bounded tasks, not a sample of arbitrary engineering work.

<!-- P4-06 -->

The registered design contained seven model/runtime bundles, twelve related cases and seeds 101 and 202: 168 planned scored units. I treated the results as observations of those bundles under recorded conditions. They did not isolate model architecture or weights from the rest of the runtime profile. Two seeds did not turn twelve related cases into 168 independent engineering problems, and ordinary desktop GPU activity was environmental metadata, not a basis for latency or hardware-efficiency comparisons.

## What the scores could not tell me

<!-- P4-07 -->

Execution ended at GLOBAL_STOP after 164 requests. There were 163 delivered, profile-verified outputs, one HTTP 500 and four NOT_EXECUTED units. There were no client retries, although the failing request included an additional internal model-load retry. I retained that distinction: an infrastructure delivery failure is not a demonstrated semantic failure by a model. The four remaining units stayed in the planned registry; I did not fill the gaps with later attempts.

<!-- P4-08 -->

The frozen full-task result was 90 successes out of 168 planned units. That contract included more than behavior alone. The primary behavior record was C102/I47/U0/M19: 102 correct, 47 incorrect, zero explicit unevaluable/unknown judgments and 19 missing behavior results. The missing 19 consisted of fourteen delivered B answers, the HTTP failure and four unexecuted units. I could not turn a missing verdict into incorrect behavior, or quietly remove those rows to make the result look complete.

<!-- P4-09 -->

The B-family gap was especially important for interpreting the evaluator. Fourteen of its 51 delivered answers lacked a primary behavior verdict: twelve NO_CODE and two NO_UNIQUE_EXTRACTION. Those are frozen extraction statuses; NO_CODE does not establish that a response contained no source. Four of the fourteen were sampled for review and ten were not. Overall, 102/149 describes correctness conditional on having a recorded behavior verdict, not accuracy across all 168 planned units. Missing evidence needed to remain visible beside the score.

<!-- P4-10 -->

Review B used the original 42-unit selection. The frozen rule for adding B answers with an explicit unknown judgment added no cases; missing behavior records did not trigger that rule. I cannot recast the sample as a review of all missing B behavior. Task judgments agreed on 42/42 sampled units. Behavior agreed on 38 jointly resolved units, while three were mutually unresolved and one raised an extraction-rule disagreement. Those are the denominators behind the agreement claim, not a certificate that the whole evaluator was correct.

<!-- P4-11 -->

That disagreement was S101-B4-M6. The frozen primary scorer recorded NO_UNIQUE_EXTRACTION; the reviewer accepted the behavior candidate under a weaker literal reading of the extraction rule. The dispute concerns what the rule admits, not a newly discovered gold answer. It remains unresolved, and the frozen controls favor the primary interpretation. I do not call it a proven primary-scoring error. The original result remains authoritative for primary reporting.

<!-- P4-12 -->

I therefore show the alternative only in the frozen conditional sensitivity analysis. Under that interpretation, behavior-correct rises from 29 to 30 in the reviewed sample and from 102 to 103 overall. The behavior-analysis denominator D also changes: from 149 in the primary record (C102+I47) to 153 in the conditional record (C103+I47+U3), where D includes the three explicit unresolved judgments and excludes missing results. The planned denominator remains 168. The conditional record leaves fifteen missing behavior results rather than nineteen. This change in coverage and interpretation does not establish improved model accuracy; the model outputs are unchanged. Full-task successes stay at 90, and the primary C102/I47/U0/M19 remains authoritative.

## Checking the record, too

<!-- P4-13 -->

The review itself also needed limits. It was AI review, nonblind and with prior exposure; substantive reviewer independence was not established. It was not human scientific adjudication. The technical review checked archived evidence and reproduced the frozen analysis outputs, which supports consistency within the retained record. It did not independently repeat the model inference. Nor does that completed review automatically certify the wording I am writing now.

<!-- P4-14 -->

I had to apply the same discipline to my own earlier claims. I withdrew the inventory-script “under a second” comparison because this closure had no primary timing receipt. The later synthetic dependency cases do not independently verify the historical 71/14 inventory or its separately written resolver. A plausible narrative, an agreement between derived records and a new illustrative check are different kinds of support. The published V1 correction record makes those boundaries explicit rather than silently rewriting the old results.

<!-- P4-15 -->

The remaining limits are substantial: twelve related cases, two seeds, incomplete execution, fourteen delivered B outputs without behavior verdicts, ten of them unreviewed, the unresolved extraction interpretation and nonblind AI review. Earlier historical source gaps also remain. This work does not establish a universal model ranking, causal architecture or vendor superiority, production or security reliability, autonomous development, or matched cost savings. It also supplies no latency, throughput or hardware-efficiency comparison.

<!-- P4-16 -->

I came away with a different standard for accepting an evaluator's verdict. I need a chain of checks whose scope I can explain: preserved inputs and outputs, explicit contracts, finite behavioral evidence, source-bound review, disclosed disagreements and honest missingness. Each check can add evidence without supplying a general guarantee. I would trust a verdict only as far as that chain supports it. For me, that is the useful conclusion of this series: keep the evaluator's limits as visible as the model's mistakes.

<!-- P4-17 -->

The [V1 corrections to Parts 1–3](https://github.com/eranb007/research/blob/main/studies/local-llm-reliability/corrections/V1_ERRATA.md) are published on GitHub; their content and public URL were verified after the Phase A merge on 31 October 2026. That is separate from editing the LinkedIn article bodies: the correction notices remain uninserted templates unless separately authorized. The [research companion](../../local-llm-final-completion/README.md) provides the counts, scoring scope and reproducibility boundary. Raw restricted evidence and unpublished reviewer bodies are not distributed; public derived-count checks are not end-to-end experiment reproduction.
