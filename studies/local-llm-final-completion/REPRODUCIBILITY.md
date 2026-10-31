# Public reproducibility boundary

This disclosure contains newly written summary prose and sanitized derived counts, not a public inference/re-scoring kit. No prompt, model output, private application source, gold-answer implementation, full scorer or unpublished reviewer body is distributed. Identity hashes alone do not provide access.

To audit the published counts without inference:

1. Read PRIMARY_OBSERVATIONS.csv using a CSV parser, not line counting. Check 168 unique unit_id and attempt_id values, seven model labels, twelve case IDs and seeds 101/202. Preserve four NOT_EXECUTED rows.
2. Group by model_id, family or case_id. Count attempt_status=YES; delivery_valid=True; original_task_correctness=True; operational classes K/F/U and semantic classes C/I/U/M. Compare the result to the respective released tables and SUMMARY.json. These CSV boolean tokens are case-sensitive strings, not truthy nonempty values.
3. The planned denominator remains 168 (24 per model; 56 per family). Confirm overall 164 attempts, 163 deliveries, K90/F74/U4 and C102/I47/U0/M19. This arithmetic verifies consistency, not raw-source authenticity or scorer correctness.
4. Use B_MISSING_BEHAVIOR.csv to check fourteen delivered B missing entries, four reviewed and ten unreviewed. Do not infer individual review opinions from the selection flags. Conditional summary counts are a separate retained result; this selected-field export does not independently reconstruct unpublished review reasoning.

Historical scripts under ../local-llm-reliability/reproducibility retain their original narrow two-CSV/constructed-example scope and do not validate the new data or restore V1 originals. Their previous content manifests and historical release stay unchanged.

Private custodial verification established raw-evidence and analysis identities; an AI reviewer recomputed eleven primary and eleven conditional analysis files. That deterministic re-analysis is not a second model inference experiment. Public readers cannot reproduce original model outputs or independently verify private effective-profile evidence from this companion alone. An independent prospective replication would require separately accepted rights-cleared tasks, references, scorer/runtime/model identities and a new authorized protocol. None is authorized by this documentation proposal.

Status fields retained in derived exports describe the frozen source snapshot; they are not merge/publication receipts. The published Phase A errata are separate from this proposed Phase B disclosure. No new scorer, inference or independent scientific review is introduced by this editorial alignment.
