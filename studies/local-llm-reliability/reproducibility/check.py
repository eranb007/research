"""Offline aggregate schema/invariant checks; do not certify historical source truth."""
import argparse
import csv
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
EDIT_COLUMNS = ("observation_id,model,condition,context_tokens,output_cap,temperature,seed,"
    "top_p,top_k,repeat_penalty,think,delivery,required_targets,proposed,admitted,"
    "rejected,exact_reference_matches,application_writes,behavioral_evidence,evidence_id").split(",")
COVERAGE_COLUMNS = ("checkpoint,source_ids,selected_fields,reviewed_fields,unreviewed_fields,"
    "bounded_assessment_units,full_historical_adjudication_complete,"
    "new_model_observations,evidence_id").split(",")
# Fixed record identities for this release, not a general benchmark schema.
IDENTITIES = [
    ("gemma4:12b", "main guarded", "32768", "NOT RECORDED", "no evaluable delivery"),
    ("gemma4:31b", "main guarded", "16384", "NOT RECORDED", "evaluable proposal"),
    ("glm-4.7-flash:q4_K_M", "main guarded", "32768", "NOT RECORDED", "evaluable proposal"),
    ("granite4.2:30b", "main guarded", "16384", "NOT RECORDED", "no evaluable delivery"),
    ("qwen3.8:27b", "main guarded", "32768", "NOT RECORDED", "evaluable proposal"),
    ("qwen3-coder:30b", "main guarded", "32768", "NOT RECORDED", "evaluable proposal"),
    ("gemma4:31b", "paired prompt; both constrained", "16384", "NOT RECORDED", "evaluable proposal"),
    ("gemma4:12b", "separate reasoning-off rescue", "32768", "false", "evaluable proposal"),
    ("granite4.2:30b", "separate reasoning-off rescue", "16384", "false", "evaluable proposal"),
]
COUNT_COLUMNS = ("proposed", "admitted", "rejected", "exact_reference_matches")


class ValidationError(ValueError):
    """Malformed or contradictory aggregate input."""


def require(condition, message):
    if not condition:
        raise ValidationError(message)


def integer(value, label):
    require(isinstance(value, str) and re.fullmatch(r"0|[1-9][0-9]*", value) is not None,
            label + ": expected canonical nonnegative integer")
    require(len(value) <= 9, label + ": out of supported range")
    return int(value)


def read_csv(path, columns):
    with pathlib.Path(path).open(encoding="utf-8", newline="") as stream:
        reader = csv.reader(stream, strict=True)
        require(next(reader, None) == columns, pathlib.Path(path).name + ": exact header required")
        rows = []
        for line, values in enumerate(reader, start=2):
            require(len(values) == len(columns), f"{pathlib.Path(path).name}:{line}: wrong column count")
            require(all(v != "" and v == v.strip() and "\x00" not in v for v in values),
                    f"{pathlib.Path(path).name}:{line}: empty/unclean field")
            rows.append(dict(zip(columns, values)))
        return rows


def validate_edits(rows):
    require(len(rows) == 9, "expected nine selected records")
    require({r["observation_id"] for r in rows} == {f"OBS-{i:02}" for i in range(1, 10)},
            "duplicate, missing or unknown observation identity")
    for r in rows:
        label = r["observation_id"]
        identity = IDENTITIES[int(label[-2:]) - 1]
        require(tuple(r[k] for k in ("model", "condition", "context_tokens", "think", "delivery"))
                == identity, label + ": inconsistent identity/condition/delivery")
        require(r["evidence_id"] == "EVID-" + label, label + ": inconsistent evidence identity")
        fixed = {"output_cap": "4096", "temperature": "0.1", "seed": "926061",
                 "top_p": "0.95", "top_k": "40", "repeat_penalty": "1.0", "required_targets": "5"}
        require(all(r[k] == v for k, v in fixed.items()), label + ": unexpected request/target setting")
        behavior = ("selected result-shape failure in supplied fixture" if label in ("OBS-03", "OBS-09")
                    else "not independently certified for all targets")
        require(r["behavioral_evidence"] == behavior, label + ": unsupported behavioral label")
        if r["delivery"] == "no evaluable delivery":
            require(all(r[k] == "UNKNOWN" for k in COUNT_COLUMNS),
                    label + ": unevaluable counts must stay UNKNOWN")
            require(r["application_writes"] == "NOT RECORDED",
                    label + ": unevaluable write evidence must stay NOT RECORDED")
        else:
            proposed, admitted, rejected, matches = [integer(r[k], label + "/" + k)
                                                     for k in COUNT_COLUMNS]
            require(proposed == admitted + rejected, label + ": proposed != admitted + rejected")
            require(0 <= matches <= admitted <= proposed <= 5, label + ": count bounds violated")
            require(r["application_writes"] == "0", label + ": application writes contradict scope")
            if label in ("OBS-03", "OBS-09"):
                require(matches < admitted, label + ": selected failure contradicts perfect matches")
    return rows


def validate_coverage(rows):
    require([r["checkpoint"] for r in rows] == ["v1.23", "v1.24", "v1.25"],
            "expected exactly three ordered coverage checkpoints")
    for r, residual, units in zip(rows, (69, 58, 0), (115, 120, 152)):
        v = {k: integer(r[k], r["checkpoint"] + "/" + k) for k in
             ("source_ids", "selected_fields", "reviewed_fields", "unreviewed_fields",
              "bounded_assessment_units", "new_model_observations")}
        require(v["reviewed_fields"] + v["unreviewed_fields"] == v["selected_fields"],
                r["checkpoint"] + ": coverage sum contradicts selected denominator")
        require(v["source_ids"] == 152 and v["selected_fields"] == 585, "fixed denominators changed")
        require(v["unreviewed_fields"] == residual and v["bounded_assessment_units"] == units,
                r["checkpoint"] + ": coverage contradicts recorded checkpoint")
        require(v["new_model_observations"] == 0, "curation is not a new model experiment")
        require(r["full_historical_adjudication_complete"] == "false",
                "selected-ledger coverage cannot establish complete historical adjudication")
        require(r["evidence_id"] == "EVID-RECON-" + r["checkpoint"], "wrong coverage evidence identity")
    return rows


def check(data_dir=None):
    data_dir = pathlib.Path(data_dir) if data_dir is not None else ROOT / "results"
    edits = validate_edits(read_csv(data_dir / "selected-edits.csv", EDIT_COLUMNS))
    coverage = validate_coverage(read_csv(data_dir / "reconciliation-coverage.csv", COVERAGE_COLUMNS))
    return {"status": "PASS", "selected_edit_records": len(edits),
            "historical_model_tags": len({r["model"] for r in edits}),
            "unevaluable_records": sum(r["delivery"] == "no evaluable delivery" for r in edits),
            "coverage_checkpoints": len(coverage), "final_selected_fields": 585,
            "final_unreviewed_selected_fields": 0, "historical_experiment_reproduced": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=pathlib.Path, help="aggregate input directory (read only)")
    args = parser.parse_args()
    try:
        result = check(args.data_dir)
    except (ValidationError, OSError, UnicodeError, csv.Error) as error:
        print(json.dumps({"status": "FAIL", "error": str(error)}, sort_keys=True))
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
