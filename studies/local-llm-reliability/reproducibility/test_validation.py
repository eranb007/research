"""Black-box regression tests. Mutate temporary copies; never edit released data."""
import copy
import csv
import io
import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent / "results"
EDIT = "selected-edits.csv"
COVER = "reconciliation-coverage.csv"


def table(name):
    with (DATA / name).open(encoding="utf-8", newline="") as stream:
        return list(csv.reader(stream))


def encode(rows):
    stream = io.StringIO(newline="")
    csv.writer(stream).writerows(rows)
    return stream.getvalue().encode("utf-8")


def fixtures():
    """Each case is an independently named invalid input with a specified rejection."""
    baseline = {EDIT: table(EDIT), COVER: table(COVER)}
    cases = []

    def changed(name, file, row, field, value):
        rows = copy.deepcopy(baseline[file])
        rows[row][rows[0].index(field)] = value
        cases.append((name, file, encode(rows)))

    # Boundaries and contradictions, including a non-first unevaluable record.
    for field in ("proposed", "admitted", "rejected", "exact_reference_matches"):
        for bad in ("-1", "1.5", "NaN", "UNKNOWN", "", " 5", "+5", "05", "1e0", "9" * 100):
            changed("edit-" + field + "-" + repr(bad[:12]), EDIT, 2, field, bad)
        changed("unevaluable-has-" + field, EDIT, 1, field, "0")
        changed("second-unevaluable-has-" + field, EDIT, 4, field, "0")
    for name, row, field, value in [
        ("sum", 2, "rejected", "0"), ("too-many", 2, "proposed", "6"),
        ("matches-exceed-admissions", 2, "exact_reference_matches", "5"),
        ("failure-now-perfect", 3, "exact_reference_matches", "5"),
        ("writes", 2, "application_writes", "1"),
        ("unevaluable-write-claim", 1, "application_writes", "0"),
        ("unknown-delivery", 2, "delivery", "maybe"),
        ("delivery-contradicts-condition", 1, "delivery", "evaluable proposal"),
        ("model-identity", 2, "model", "invented-model"),
        ("duplicate-id", 2, "observation_id", "OBS-01"),
        ("unknown-id", 2, "observation_id", "OBS-99"),
        ("wrong-evidence", 2, "evidence_id", "EVID-OBS-03"),
        ("wrong-condition", 2, "condition", "main"),
        ("wrong-context", 2, "context_tokens", "32768"),
        ("wrong-think", 2, "think", "false"),
        ("unsupported-behavior", 2, "behavioral_evidence", "correct"),
        ("required-targets", 2, "required_targets", "6"),
        ("output-cap", 2, "output_cap", "8192"),
        ("temperature", 2, "temperature", "NaN"),
        ("seed", 2, "seed", "1"), ("top-p", 2, "top_p", "1"),
        ("top-k", 2, "top_k", "0"), ("repeat", 2, "repeat_penalty", "0"),
    ]:
        changed(name, EDIT, row, field, value)
    for name, row, field, value in [
        ("coverage-sum", 3, "reviewed_fields", "584"),
        ("coverage-denominator", 3, "selected_fields", "595"),
        ("source-ids", 3, "source_ids", "153"),
        ("residual", 3, "unreviewed_fields", "1"),
        ("unit-count", 2, "bounded_assessment_units", "121"),
        ("historical-complete", 3, "full_historical_adjudication_complete", "true"),
        ("boolean-spelling", 3, "full_historical_adjudication_complete", "False"),
        ("model-experiments", 3, "new_model_observations", "1"),
        ("coverage-id", 3, "evidence_id", "EVID-RECON-v1.24"),
        ("duplicate-checkpoint", 3, "checkpoint", "v1.24"),
        ("coverage-negative", 3, "reviewed_fields", "-1"),
        ("coverage-fraction", 3, "unreviewed_fields", "0.0"),
    ]:
        changed(name, COVER, row, field, value)
    # Even self-consistent alternative checkpoint totals cannot impersonate the frozen facts.
    rows = copy.deepcopy(baseline[COVER])
    rows[2][rows[0].index("reviewed_fields")] = "528"
    rows[2][rows[0].index("unreviewed_fields")] = "57"
    cases.append(("consistent-but-wrong-checkpoint", COVER, encode(rows)))
    for file in (EDIT, COVER):
        original = baseline[file]
        for label, transform in [
            ("empty", lambda r: []), ("header-only", lambda r: r[:1]),
            ("missing-row", lambda r: r[:-1]), ("extra-row", lambda r: r + [r[-1]]),
            ("duplicate-header", lambda r: [r[0][:-1] + [r[0][0]]] + r[1:]),
            ("missing-header", lambda r: r[1:]),
            ("extra-column", lambda r: r[:1] + [r[1] + ["unexpected"]] + r[2:]),
            ("missing-column", lambda r: r[:1] + [r[1][:-1]] + r[2:]),
            ("blank-row", lambda r: r + [[]]),
            ("reordered-header", lambda r: [list(reversed(r[0]))] + r[1:]),
        ]:
            cases.append((file + "-" + label, file, encode(transform(copy.deepcopy(original)))))
        cases.append((file + "-bad-utf8", file, encode(original) + b"\xff"))
        cases.append((file + "-unterminated-quote", file, encode(original[:1]) + b'"unterminated\n'))
        cases.append((file + "-missing-file", file, None))
    return cases


class AggregateCLI(unittest.TestCase):
    def run_checker(self, directory, optimized):
        command = [sys.executable, "-B"] + (["-O"] if optimized else [])
        return subprocess.run(command + [str(HERE / "check.py"), "--data-dir", str(directory)],
                              capture_output=True, text=True, encoding="utf-8", timeout=10)

    def test_valid_baseline_and_documented_unknowns(self):
        expected = json.loads((HERE / "expected.json").read_text(encoding="utf-8"))["check"]
        for optimized in (False, True):
            with self.subTest(optimized=optimized):
                result = self.run_checker(DATA, optimized)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(json.loads(result.stdout), expected)

    def test_all_invalid_inputs_fail_in_both_modes(self):
        with tempfile.TemporaryDirectory(prefix="aggregate-negative-") as temp:
            directory = pathlib.Path(temp)
            for name, file, payload in fixtures():
                for optimized in (False, True):
                    with self.subTest(case=name, optimized=optimized):
                        for original in (EDIT, COVER):
                            (directory / original).write_bytes((DATA / original).read_bytes())
                        if payload is None:
                            (directory / file).unlink()
                        else:
                            (directory / file).write_bytes(payload)
                        result = self.run_checker(directory, optimized)
                        self.assertNotEqual(result.returncode, 0, result.stdout)
                        output = json.loads(result.stdout)
                        self.assertEqual(output.get("status"), "FAIL", result.stdout)
                        self.assertNotIn("PASS", result.stdout)

    def test_boundary_controls_refuse_regression(self):
        # Break each invented mechanism in memory and require explicit refusal under -O too.
        mutations = [
            "m.textual_gate = lambda text: True",
            "m.narrow_admission = lambda operation, target: False",
            "m.mutant = m.reference",
        ]
        for optimized in (False, True):
            for mutation in mutations:
                with self.subTest(optimized=optimized, mutation=mutation):
                    code = ("import sys; sys.path.insert(0, " + repr(str(HERE)) + "); "
                            "import boundary_demo as m; " + mutation + "; m.demo()")
                    command = [sys.executable, "-B"] + (["-O"] if optimized else [])
                    result = subprocess.run(command + ["-c", code], capture_output=True,
                                            text=True, encoding="utf-8", timeout=10)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn("ValueError", result.stderr)
                    self.assertNotIn("PASS", result.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
