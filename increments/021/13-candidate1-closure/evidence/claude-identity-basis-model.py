"""Reviewer scratch model of candidate-1 §10.1 (documentary, not production code).
1) Recompute documentary projection SHA-256 of IDENTITY_BASIS_CASES.json under canonical JSON.
2) Enumerate a grid of (table context, ptnr1 code, ptnr2 code) and classify each endpoint per §10.1,
   checking: per-endpoint determinism, reachable pair set, the two mixed pairs never arise."""
import json, hashlib, itertools, re, sys
cases = json.load(open(sys.argv[1]))
canon = lambda o: json.dumps(o, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
proj = {c["scenario_id"]: (hashlib.sha256(canon(c["documentary_projection"])).hexdigest() == c["documentary_projection_sha256"])
        for c in cases["cases"] if c["documentary_projection"]}
CODE = re.compile(r"([1-9][0-9]*)_([1-9])([1-9])([1-9])")
# table contexts: None=absent; dict id->list of expressions (duplicates allowed)
tables = {
  "none": (None, None),
  "equiv_only_std": ({"1": ["x,y,z"], "2": ["-x,y+1/2,-z"]}, None),
  "both_std": ({"1": ["x,y,z"], "2": ["-x,y+1/2,-z"]}, {"1": ["x,y,z"], "2": ["-x,y+1/2,-z"]}),
  "both_op1_one_table": ({"1": ["x,y,z"]}, {"2": ["-x,y+1/2,-z"]}),
  "contradict": ({"1": ["x,y,z"]}, {"1": ["-x,-y,z"]}),
  "dup_in_table": ({"1": ["x,y,z", "x,y,z"]}, None),
  "op1_nonidentity": ({"1": ["-x,-y,z"]}, None),
  "empty_present": ({}, None),
}
codes = [None, "1_555", "2_555", "3_555", "1_556", "01_555", "'?'", "abc"]
def basis(code, ctx):
    t1, t2 = ctx
    if code is None or not CODE.fullmatch(code): return "not-applicable"
    if t1 is None and t2 is None: return "pdbx-1_555-convention" if code == "1_555" else "not-applicable"
    n = CODE.fullmatch(code).group(1); matches = []
    for t in (t1, t2):
        if t is None: continue
        exprs = t.get(n, [])
        if len(exprs) > 1: return "not-applicable"  # duplicate within one table
        matches += exprs
    if not matches or any(not e for e in matches) or len(set(matches)) > 1: return "not-applicable"
    return "source-operator"
pairs = set(); runs = {}
for (tn, ctx), c1, c2 in itertools.product(tables.items(), codes, codes):
    p = (basis(c1, ctx), basis(c2, ctx)); pairs.add(p)
    assert p == (basis(c1, ctx), basis(c2, ctx))  # determinism (pure function)
    runs.setdefault(p, []).append((tn, c1, c2))
mixed = {("pdbx-1_555-convention", "source-operator"), ("source-operator", "pdbx-1_555-convention")}
print(json.dumps({"projection_hash_matches": proj, "grid_size": len(tables) * len(codes) ** 2,
                  "reachable_pairs": sorted(map(list, pairs)), "reachable_count": len(pairs),
                  "mixed_pairs_reached": sorted(map(list, pairs & mixed)),
                  "example_per_pair": {"/".join(k): v[0] for k, v in sorted(runs.items())},
                  "interpretation_note": "duplicate = same id twice within one table; same id once in each of two tables with equal expression = concordant"}, indent=1))
