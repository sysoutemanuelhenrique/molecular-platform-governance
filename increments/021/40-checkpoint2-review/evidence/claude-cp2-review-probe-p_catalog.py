import sys; sys.path.insert(0,'/tmp/probes')
from harness import *
B = BASE
ok=[]
def chk(label, raw, exp, code=None, extra=None):
    o = outcome(lambda: run(raw))
    good = o["result"]==exp and (code is None or o.get("code")==code)
    ok.append(good)
    rec = {"probe":label,"expected":exp if code is None else f"{exp}:{code}","got":o["result"] if o["result"]=="ACCEPTED" else f"REFUSED:{o.get('code') or o.get('type')}","matches_contract":good}
    if extra and o["result"]=="ACCEPTED": rec.update(extra(o["obj"]))
    print(json.dumps(rec)); return o
def ncs(rows, code_col=True):
    cols = ["id"] + (["code"] if code_col else []) + [f"matrix[{i}][{j}]" for i in (1,2,3) for j in (1,2,3)] + [f"vector[{i}]" for i in (1,2,3)]
    s = "#\nloop_\n" + "".join(f"_struct_ncs_oper.{c}\n" for c in cols)
    for r in rows: s += " ".join(r) + "\n"
    return B + s
I = ["1","0","0","0","1","0","0","0","1","0","0","0"]
R = ["-1","0","0","0","-1","0","0","0","1","10.0","0","0"]
warn = lambda r: {"warnings": list(r.plan.plan.warnings)}
chk("T021-150 ncs nonidentity generate", ncs([["1","generate",*R]]), "REFUSED", "UNSUPPORTED_NCS")
chk("T021-151 ncs nonidentity null code", ncs([["1","?",*R]]), "REFUSED", "UNSUPPORTED_NCS")
chk("T021-151b ncs nonidentity code column absent", ncs([["1",*R]], code_col=False), "REFUSED", "UNSUPPORTED_NCS")
chk("T021-152 ncs nonidentity given", ncs([["1","given",*R]]), "ACCEPTED", extra=warn)
chk("T021-153 ncs identity generate", ncs([["1","generate",*I]]), "ACCEPTED", extra=warn)
chk("T021-153b ncs identity null", ncs([["1",".",*I]]), "ACCEPTED", extra=warn)
chk("T021-153c ncs near-identity 1e-7 generate", ncs([["1","generate",*I[:9],"0.0000001","0","0"]]), "REFUSED", "UNSUPPORTED_NCS")
chk("T021-154 ncs partial matrix", ncs([["1","given",*I[:8],"?",*I[9:]]]), "REFUSED", "INVALID_CIF")
chk("T021-154b ncs code unknown", ncs([["1","weird",*I]]), "REFUSED", "INVALID_CIF")
chk("T021-154c ncs quoted numeric", ncs([["1","given","'1'",*I[1:]]]), "REFUSED", "INVALID_CIF")
chk("ncs duplicate id", ncs([["1","given",*R],["1","given",*R]]), "REFUSED")
# anisotrop
def an(cols, vals):
    return B + "#\nloop_\n" + "".join(f"_atom_site_anisotrop.{c}\n" for c in cols) + " ".join(vals) + "\n"
U = [f"U[{i}][{j}]" for i,j in ((1,1),(1,2),(1,3),(2,2),(2,3),(3,3))]
BB = [f"B[{i}][{j}]" for i,j in ((1,1),(1,2),(1,3),(2,2),(2,3),(3,3))]
chk("T021-062 aniso complete U ok", an(["id","type_symbol",*U], ["1","C","0.1","-0.01","0.02","0.1","0.0","0.1"]), "ACCEPTED")
chk("T021-062 aniso complete B with esd ok", an(["id",*BB,"B[1][1]_esd"], ["1","1","-1","0","1","0","1","0.1"]), "ACCEPTED")
chk("T021-062 aniso partial U", an(["id",*U[:5]], ["1","0.1","0","0","0.1","0"]), "REFUSED", "INVALID_CIF")
chk("T021-062 aniso partial U + full B", an(["id","U[1][1]",*BB], ["1","0.1","1","0","0","1","0","1"]), "REFUSED", "INVALID_CIF")
chk("T021-062 aniso type contradiction", an(["id","type_symbol",*U], ["1","O","0.1","0","0","0.1","0","0.1"]), "REFUSED", "INVALID_CIF")
chk("T021-062 aniso label_seq contradiction", an(["id","pdbx_label_seq_id",*U], ["1","99","0.1","0","0","0.1","0","0.1"]), "REFUSED", "INVALID_CIF")
chk("T021-062 aniso id not in atom_site", an(["id",*U], ["999","0.1","0","0","0.1","0","0.1"]), "REFUSED")
chk("T021-062 aniso quoted tensor value", an(["id",*U], ["1","'0.1'","0","0","0.1","0","0.1"]), "REFUSED", "INVALID_CIF")
o = chk("T021-062 aniso removed atom row dropped", an(["id",*U], ["5","0.1","0","0","0.1","0","0.1"]), "ACCEPTED",
        extra=lambda r: {"aniso_kept": list(next(d for d in r.plan.category_decisions if d.category=="_atom_site_anisotrop").kept_row_ordinals)})
# catalogue closure
chk("T021-084 unknown category", B + "\n_zzz.a 1\n", "REFUSED", "UNSUPPORTED_CATEGORY")
chk("T021-084b validate family omitted", B + "\n_pdbx_validate_close_contact.id 1\n", "ACCEPTED")
chk("T021-084c family prefix near-miss", B + "\n_pdbx_validatex.id 1\n", "REFUSED", "UNSUPPORTED_CATEGORY")
chk("T021-085 unknown tag in filtered", B.replace("_atom_type.symbol\n", "_atom_type.symbol\n_atom_type.zz_unknown\n").replace("\nC\nN\nS\n", "\nC 1\nN 1\nS 1\n"), "REFUSED", "UNSUPPORTED_TAG")
chk("T021-085b unknown tag in omitted", B.replace("_audit_author.name\n'Doe, J.'", "_audit_author.name\n_audit_author.zz_unknown\n'Doe, J.' 1"), "ACCEPTED")
chk("T021-086 missing entity_poly_seq for retained polymer", B.replace("loop_\n_entity_poly_seq.entity_id\n_entity_poly_seq.num\n_entity_poly_seq.mon_id\nE1 1 ALA\nE1 2 CYS\n", ""), "REFUSED")
chk("T021-086b missing struct_conn_type with preserved conn", B.replace("loop_\n_struct_conn_type.id\ndisulf\nmetalc\n", ""), "REFUSED")
chk("T021-086c missing required chem_comp row for retained CCD", B.replace("ALA 'L-peptide linking'\n", ""), "REFUSED")
chk("T021-087 duplicate atom_site.id", B.replace("ATOM 4 N N  .", "ATOM 3 N N  ."), "REFUSED")
chk("T021-087b duplicate entity.id", B.replace("E2 polymer\n", "E2 polymer\nE1 polymer\n"), "REFUSED")
chk("T021-087c duplicate chem_comp.id", B.replace("MET 'L-peptide linking'\n", "MET 'L-peptide linking'\nALA 'L-peptide linking'\n"), "REFUSED")
chk("entity_poly_seq mismatch label_comp for retained atom", B.replace("E1 2 CYS\n", "E1 2 SER\n"), "REFUSED")
chk("entity.type unknown on retained", B.replace("E1 polymer", "E1 unknown"), "REFUSED")
r = run(B)
ent = next(d for d in r.plan.category_decisions if d.category=="_entry")
cell = r.reparsed.categories["cell"]
print(json.dumps({"T021-082": {"entry_action": ent.action, "generated": list(ent.generated_tags), "source_rows_key_present": ent.source_rows_key is not None,
     "entry_id_out": r.reparsed.categories["entry"].get(0,"id"), "block": r.reparsed.block_name,
     "cell_entry_id_generated": cell.get(0,"entry_id")==f"tbmp_{r.plan.plan_key}", "symmetry_out": r.reparsed.categories["symmetry"].columns}}))
print("SUMMARY", sum(ok), "/", len(ok))
