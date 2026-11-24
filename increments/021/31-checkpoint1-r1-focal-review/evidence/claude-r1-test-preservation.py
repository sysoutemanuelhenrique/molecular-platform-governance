"""Reviewer AST comparison of tests/test_receptor_materialization.py between bbd491e and ea8dac9 (read-only git show).
Run from a clone of molecular-platform with both commits available."""
import ast, json, re, subprocess
def load(rev):
    s = subprocess.check_output(["git", "show", f"{rev}:tests/test_receptor_materialization.py"]).decode(); t = ast.parse(s)
    f = {n.name: ast.get_source_segment(s, n) for n in t.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
    imps = [ast.get_source_segment(s, n) for n in t.body if isinstance(n, (ast.Import, ast.ImportFrom))]
    assigns = [ast.get_source_segment(s, n) for n in t.body if isinstance(n, (ast.Assign, ast.AnnAssign))]
    return s, f, imps, assigns
s0, f0, i0, a0 = load("bbd491e"); s1, f1, i1, a1 = load("ea8dac9")
t0 = {k for k in f0 if k.startswith("test_")}; t1 = {k for k in f1 if k.startswith("test_")}
NEW = "test_atom_ids_key_preserves_given_order_against_ordinal_and_id_sorting"
out = {"test_functions": [len(t0), len(t1)], "removed_functions": sorted(set(f0) - set(f1)), "added_functions": sorted(set(f1) - set(f0)),
       "modified_functions": sorted(k for k in f0 if k in f1 and f0[k] != f1[k]), "imports_identical": i0 == i1, "module_assignments_identical": a0 == a1,
       "golden_literal_constants": [len(re.findall(r"^_GOLDEN_[A-Z_]+_SHA256 = ", s, re.M)) for s in (s0, s1)],
       "parametrize_count": [s.count("pytest.mark.parametrize") for s in (s0, s1)],
       "T021_ids": [len(set(re.findall(r"T021-\d{3}", s))) for s in (s0, s1)],
       "old_text_is_prefix_suffix_preserved": s1.replace(f1[NEW] + "\n\n\n", "", 1) == s0}
print(json.dumps(out, indent=1))
