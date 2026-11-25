import sys; sys.path.insert(0,'/tmp/probes')
from harness import *
B = BASE
res=[]
def rec(label, good, **kw): res.append(good); print(json.dumps({"probe":label,"matches_contract":good,**kw}))
# T021-041/042: raw tokens survive literally (quoted ?, bare ?, '.', precision, 0 occupancy, null B, D atom)
L1 = "ATOM 1 C CA . ALA A E1 1 A 1 ? 1 1.000 2.000 3.000 1.00 10.00"
t = B.replace(L1, "ATOM 1 C CA . ALA A E1 1 A 1 '?' 1 1.0000001 -2.000e0 3.000(4) 0 ?")
t = t.replace("ATOM 4 N N  . ALA A E1 1 A 1 ? 1 1.200 2.200 3.200 1.00 10.20", "ATOM 4 D D  . ALA A E1 1 A 1 . 1 1.200 2.200 3.200 0.33 .")
t = t.replace("_atom_type.symbol\nC\nN\nS\n", "_atom_type.symbol\nC\nD\nS\n").replace("loop_\n_audit_author.name\n'Doe, J.'\n", "_struct_conn_type.criteria ;\nline one\n  'quoted' ; inside\n;\n")
t = t.replace("loop_\n_struct_conn_type.id\ndisulf\nmetalc\n", "loop_\n_struct_conn_type.id\n_struct_conn_type.criteria\ndisulf\n;\nline one\n  'quoted' ; inside\n;\nmetalc ?\n").replace("_struct_conn_type.criteria ;\nline one\n  'quoted' ; inside\n;\n","")
t = t.replace("conn1 disulf A ALA 1 CA 1_555 A ALA 1 N 1_555", "conn1 disulf A ALA 1 CA 1_555 A ALA 1 D 1_555")
o = outcome(lambda: run(t))
if o["result"]=="ACCEPTED":
    a = o["obj"].reparsed.categories["atom_site"]; sct = o["obj"].reparsed.categories["struct_conn_type"]
    row0 = {c: a.get(0,c) for c in ("pdbx_pdb_ins_code","cartn_x","cartn_y","cartn_z","occupancy","b_iso_or_equiv")}
    row3 = {c: a.get(3,c) for c in ("type_symbol","pdbx_pdb_ins_code","occupancy","b_iso_or_equiv")}
    good = row0 == {"pdbx_pdb_ins_code":"'?'","cartn_x":"1.0000001","cartn_y":"-2.000e0","cartn_z":"3.000(4)","occupancy":"0","b_iso_or_equiv":"?"} and row3=={"type_symbol":"D","pdbx_pdb_ins_code":".","occupancy":"0.33","b_iso_or_equiv":"."}
    ml = sct.get(0,"criteria")
    rec("T021-041/042 literal tokens (quoted ?, bare ?, ., su, exponent, 0, null B, D atom)", good, row0=row0, row3=row3)
    rec("T021-041 multiline text token survives literally", ml == ";\nline one\n  'quoted' ; inside\n;" or ("'quoted' ; inside" in (ml or "")), multiline=ml)
else: rec("T021-041/042 literal tokens", False, outcome=o.get("code") or o.get("type"))
# T021-158 special positions
def sp(rows, cols=("id","label_asym_id","label_comp_id","label_seq_id","auth_seq_id","pdb_model_num","label_alt_id")):
    return B + "#\nloop_\n" + "".join(f"_pdbx_struct_special_symmetry.{c}\n" for c in cols) + "".join(" ".join(r)+"\n" for r in rows)
def summ(r): s=r.plan.special_positions if hasattr(r.plan,'special_positions') else None; return s
for label, rows, exp in [
  ("retained hit", [["1","A","ALA","1","1","1","?"]], ("ACCEPTED",(1,1,3),True)),
  ("removed only (chain B complement)", [["1","B","MET","1","1","1","?"]], ("ACCEPTED",(1,0,0),False)),
  ("overlap two rows same residue", [["1","A","ALA","1","1","1","?"],["2","A","ALA","1","1","1","?"]], ("ACCEPTED",(2,2,3),True)),
  ("other model", [["1","A","ALA","1","1","2","?"]], ("ACCEPTED",(1,0,0),False)),
  ("component contradiction", [["1","A","GLY","1","1","1","?"]], ("REFUSED",None,None)),
  ("unknown asym", [["1","Z","ALA","1","1","1","?"]], ("REFUSED",None,None)),
  ("malformed model token '01'", [["1","A","ALA","1","1","01","?"]], ("REFUSED",None,None)),
  ("altloc absent from residue", [["1","A","ALA","1","1","1","Q"]], ("REFUSED",None,None)),
]:
    o = outcome(lambda: run(sp(rows)))
    if o["result"]=="ACCEPTED":
        p=o["obj"].plan; s=p.special_positions; got=(s.source_annotation_count,s.retained_annotation_count,s.retained_unique_atom_count)
        w = "special-position-annotations-omitted" in p.plan.warnings
        good = exp[0]=="ACCEPTED" and got==exp[1] and w==exp[2]
        rec("T021-158 "+label, good, counts=got, warning=w)
    else:
        rec("T021-158 "+label, exp[0]=="REFUSED", got=o.get("code") or o.get("type"))
print("SUMMARY", sum(res), "/", len(res))
