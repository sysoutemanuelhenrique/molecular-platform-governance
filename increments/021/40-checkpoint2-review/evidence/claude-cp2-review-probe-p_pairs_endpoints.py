import sys; sys.path.insert(0,'/tmp/probes')
from harness import *
from cifgen import *
out = {}
def k0(s1,s2,**t): return make([row("c1","disulf","B1SD",s1,"B1CE",s2)], **t)
pairs = {
 "T021-164": (k0("1_555","1_555"), ("pdbx-1_555-convention","pdbx-1_555-convention")),
 "T021-166": (k0("1_555","."), ("pdbx-1_555-convention","not-applicable")),
 "T021-168": (k0("2_555","2_555",symeq=STD), ("source-operator","source-operator")),
 "T021-169": (k0("2_555","?",symeq=STD), ("source-operator","not-applicable")),
 "T021-170": (k0(".","1_555"), ("not-applicable","pdbx-1_555-convention")),
 "T021-171": (k0("?","3_555",symeq=STD), ("not-applicable","source-operator")),
 "T021-172": (k0("4_555","4_555",symeq=STD), ("not-applicable","not-applicable")),
}
for sid,(raw,exp) in pairs.items():
    r = run(raw); d = r.plan.connection_decisions[0]
    # reversed partner order must give reversed bases (no sort)
    out[sid] = {"basis": list(d.identity_basis), "basis_ok": tuple(d.identity_basis)==exp, "plan_key": r.plan.plan_key,
                "connection_decisions_key": r.plan.plan.connection_decisions_key, "raw_sha256": hashlib.sha256(raw.encode()).hexdigest()}
# endpoints: insertion code distinction for waters (label_seq null) 52 vs 52A
W = BASE.replace("E2 polymer\n", "E2 polymer\nE3 water\n").replace("B E2\n", "B E2\nC E3\n")
W = W.replace("ATOM 5 S SD . MET B E2 1 B 1 ? 1 9.000 9.000 9.000 1.00 12.00\n",
  "ATOM 5 S SD . MET B E2 1 B 1 ? 1 9.000 9.000 9.000 1.00 12.00\n"
  "HETATM 6 O O . HOH C E3 . A 52 ? 1 5.000 5.000 5.000 1.00 20.00\n"
  "HETATM 7 O O . HOH C E3 . A 52 A 1 6.000 6.000 6.000 1.00 20.00\n").replace("MET 'L-peptide linking'\n","MET 'L-peptide linking'\nHOH non-polymer\n")
def wconn(ins, sym="1_555", ptnr3=None):
    cols = ("ptnr1_label_asym_id ptnr1_label_comp_id ptnr1_label_seq_id ptnr1_label_atom_id ptnr1_symmetry "
            "ptnr2_label_asym_id ptnr2_label_comp_id ptnr2_label_seq_id ptnr2_label_atom_id ptnr2_auth_seq_id pdbx_ptnr2_PDB_ins_code ptnr2_symmetry").split()
    extra = []
    if ptnr3 is not None: cols.append("pdbx_ptnr3_label_atom_id"); extra=[ptnr3]
    s = "loop_\n_struct_conn.id\n_struct_conn.conn_type_id\n" + "".join(f"_struct_conn.{c}\n" for c in cols)
    s += " ".join(["c1","metalc","A","CYS","2","SG",sym,"C","HOH",".","O","52",ins,sym,*extra]) + "\n"
    head, rest = W.split("loop_\n_struct_conn.id",1)
    return head + s + "#\nloop_\n_struct_conn_type.id" + rest.split("#\nloop_\n_struct_conn_type.id",1)[1]
for label, ins, exp_ids in [("ins_none", "?", ("6",)), ("ins_A", "A", ("7",))]:
    r = run(wconn(ins)); d = r.plan.connection_decisions[0]
    out["T021-043:"+label] = {"endpoint2": list(d.endpoint_atom_ids[1]), "ok": tuple(d.endpoint_atom_ids[1])==exp_ids, "action": d.action}
for label, v, exp in [("ptnr3_bare_null", "?", "ACCEPTED"), ("ptnr3_dot", ".", "ACCEPTED"), ("ptnr3_quoted_q", "'?'", "REFUSED"), ("ptnr3_filled", "O", "REFUSED")]:
    o = outcome(lambda: run(wconn("?", ptnr3=v)))
    out["T021-044:"+label] = {"result": o["result"], "code": o.get("code"), "ok": o["result"]==exp}
# altloc sets: endpoint without altloc on atom with A/B variants in same occurrence
AL = BASE.replace("ATOM 2 S SG . CYS A E1 2 A 2 ? 1 1.500 2.500 3.500 1.00 11.00\n",
   "ATOM 2 S SG A CYS A E1 2 A 2 ? 1 1.500 2.500 3.500 0.50 11.00\nATOM 8 S SG B CYS A E1 2 A 2 ? 1 1.600 2.500 3.500 0.50 11.00\n")
r = run(AL); d = [x for x in r.plan.connection_decisions if x.id=="conn2"][0]
out["T021-156"] = {"endpoint1_set": list(d.endpoint_atom_ids[0]), "K": d.retained_endpoints, "ok": tuple(d.endpoint_atom_ids[0])==("2","8") and d.retained_endpoints==1}
sc = [x for x in r.plan.category_decisions if x.category=="_struct_conn"][0]
out["T021-156:literal_rows"] = {"struct_conn_kept": list(sc.kept_row_ordinals), "conn_rows_total": len(r.plan.connection_decisions)}
# ambiguous occurrence: same atom name SD in two occurrences matched by endpoint lacking seq (water-like path) -> use two HOH with same auth_seq/ins
AMB = W.replace("HETATM 7 O O . HOH C E3 . A 52 A 1", "HETATM 7 O O . HOH C E3 . A 52 ? 1")
o = outcome(lambda: run(wconn("?").replace(W.split('loop_\n_struct_conn.id')[0], AMB.split('loop_\n_struct_conn.id')[0])))
out["T021-157"] = {"result": o["result"], "code": o.get("code"), "ok": o.get("code") in ("AMBIGUOUS_ENDPOINT","INVALID_CIF")}
print(json.dumps(out, sort_keys=True))
