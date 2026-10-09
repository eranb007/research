# Local LLM reliability in software-engineering workflows

Local execution made it possible to explore coding models within a real development setting. The goal was to understand which responsibilities could be delegated, which failures remained hidden and how verification should constrain integration. The private host application supplied realistic contracts; the experiments did not certify live production behavior.

## What was investigated

The original September experiments covered cross-file defect review, bounded edits, adversarial test proposals, dependency navigation, Hebrew wording judgments and advisory migration review. Six historical Q4_K_M model artifacts are listed in [models.json](results/models.json); request-specific conditions govern each observation. October work added synthetic gap experiments, small real-source tasks, a zero-inference validator audit and separately preserved reviewer assessments.

[Selected results](results/README.md) show why admission is an incomplete success criterion: some admitted proposals matched reference files, while other admitted proposals returned the wrong result shape. A fixed-order pair changed strict admission from zero to four of five targets; the evidence does not establish a causal prompt effect. A truncated response remains unevaluable rather than being assigned a semantic failure rate.

Later constructed challenges exposed comment-sensitive rejection and finite-oracle coverage gaps. They are audit counterexamples, not model outputs or population error estimates. Some reviewer disagreements concern different assessment targets or missing context; voting cannot supply missing evidence.

The selected reconciliation ledger is fully reviewed at v1.25: 585 selected fields, zero unreviewed selected fields, 152 bounded assessment units and a separate 152-ID source join. Full historical adjudication remains incomplete. These units are not interchangeable with requests, task counts or defects. See the [coverage data](results/reconciliation-coverage.csv).

## Navigate the study

- [Research questions](research-questions.md) and [methodology](methodology.md).
- [Experiment groups and conditions](experiments.md).
- [Results, failure modes and evidence limits](results/README.md).
- [Limitations](limitations.md) and [offline reproducibility](reproducibility/README.md).
- [Figures](figures/README.md), [articles](articles/README.md) and [roadmap](roadmap.md).

Public reproduction currently covers aggregate checks, figure derivation and invented boundary demonstrations. It does not reproduce original inference, the private application or the original validator. Future matched experiments need a frozen protocol and separate execution authorization. No workflow benefit, global model ranking, production safety, statistical significance or measured cost saving is established.
