"""Reviewer recomputation of the two R-1 literals with stdlib only (SCHEMAS section 4 atom_ids envelope);
no production import, no architect vector import. Also checks the given order against both sort orders."""
import hashlib, json, sys
def C(d): return json.dumps(d, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")
def env(atoms): return {"kind": "receptor-materialization-atom-ids", "version": "1.0", "atoms": [{"ordinal": o, "id": i} for o, i in atoms]}
given = [(3, "a"), (1, "Z")]
by_ord, by_id = sorted(given), sorted(given, key=lambda t: t[1])
gb, rb = C(env(given)), C(env(list(reversed(given))))
src = open(sys.argv[1], encoding="utf-8").read()
out = {"given_bytes": gb.decode(), "given_sha256": hashlib.sha256(gb).hexdigest(), "reversed_sha256": hashlib.sha256(rb).hexdigest(),
       "given_differs_from_ordinal_sort": given != by_ord, "given_differs_from_ascii_id_sort": given != by_id,
       "ordinal_sort_equals_id_sort": by_ord == by_id, "reversed_equals_both_sorts": list(reversed(given)) == by_ord == by_id,
       "test_file_contains_given_bytes": repr(gb)[2:-1] in src, "test_file_contains_reversed_bytes": repr(rb)[2:-1] in src,
       "expected_given": "96fd3eacd89d16753dbdc5ec22bb79db0740e9f355e6322cb0c4641bc0f3106a", "expected_reversed": "bf820fe14730b4b8ede9d8e007e4c3d32f71def5d8a4747c657d6d76dac562d1"}
out["given_matches_task_literal"] = out["given_sha256"] == out["expected_given"]; out["reversed_matches_task_literal"] = out["reversed_sha256"] == out["expected_reversed"]
print(json.dumps(out, indent=1))
