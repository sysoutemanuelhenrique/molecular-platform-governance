import sys, re; sys.path.insert(0,'/tmp/probes')
from harness import *
import molecular.receptor_parsing as rp
B = BASE
ctrl = run(B); text = ctrl.output_bytes.decode()
orig_ser = rp.serialize_cif_document021
def mutated(fn):
    def wrapper(**kw):
        return fn(orig_ser(**kw).decode()).encode()
    return wrapper
def first_atom_line(t): return next(l for l in t.splitlines() if l.startswith("ATOM 1 "))
muts = {
 "coord_changed": lambda t: t.replace("1.000 2.000 3.000", "1.001 2.000 3.000", 1),
 "rows_swapped": lambda t: (lambda a,b: t.replace(a,"@@").replace(b,a).replace("@@",b))(first_atom_line(t), next(l for l in t.splitlines() if l.startswith("ATOM 2 "))),
 "row_dropped": lambda t: t.replace(first_atom_line(t)+"\n", "", 1),
 "null_marker_swapped": lambda t: t.replace(first_atom_line(t), first_atom_line(t).replace(" . ALA", " ? ALA", 1), 1),
 "quoted_lookalike": lambda t: t.replace(first_atom_line(t), first_atom_line(t).replace(" . ALA", " '.' ALA", 1), 1),
 "extra_category": lambda t: t + "_zz_extra.x 1\n",
 "block_renamed": lambda t: re.sub(r"^data_\S+", "data_tbmp_other", t, count=1, flags=re.M),
 "struct_conn_token": lambda t: t.replace("disulf", "covale", 1),
 "chem_comp_id": lambda t: t.replace("\nALA 'L-peptide linking'", "\nALB 'L-peptide linking'", 1),
}
for label, m in muts.items():
    probe = m(text)
    if probe == text: print(json.dumps({"mutation": label, "skipped": "no-op"})); continue
    rp.serialize_cif_document021 = mutated(m)
    try:
        o = outcome(lambda: run(B))
    finally:
        rp.serialize_cif_document021 = orig_ser
    print(json.dumps({"mutation": label, "result": o["result"], "code": o.get("code"), "phase": o.get("phase"),
                      "matches_contract": o["result"] == "REFUSED" and o.get("code") == "INVALID_OUTPUT" and o.get("phase") == "verify"}))
print("--- serialized control output (first 40 lines) ---")
print("\n".join(text.splitlines()[:40]))
