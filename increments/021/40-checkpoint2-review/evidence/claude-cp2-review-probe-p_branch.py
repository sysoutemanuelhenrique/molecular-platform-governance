import sys; sys.path.insert(0,'/tmp/probes')
from harness import *
B = BASE
res=[]
G = B.replace("E2 polymer\n", "E2 polymer\nE3 branched\n").replace("B E2\n", "B E2\nC E3\n")
G = G.replace("ATOM 5 S SD . MET B E2 1 B 1 ? 1 9.000 9.000 9.000 1.00 12.00\n",
  "ATOM 5 S SD . MET B E2 1 B 1 ? 1 9.000 9.000 9.000 1.00 12.00\n"
  "HETATM 6 C C1 . NAG C E3 . A 501 ? 1 4.000 4.000 4.000 1.00 20.00\n"
  "HETATM 7 C C1 . BMA C E3 . A 502 ? 1 4.500 4.000 4.000 1.00 20.00\n")
G = G.replace("MET 'L-peptide linking'\n", "MET 'L-peptide linking'\nNAG 'D-saccharide'\nBMA 'D-saccharide'\nMAN 'D-saccharide'\n")
BR = ("#\nloop_\n_pdbx_entity_branch.entity_id\n_pdbx_entity_branch.type\nE3 oligosaccharide\n"
      "#\nloop_\n_pdbx_entity_branch_list.entity_id\n_pdbx_entity_branch_list.comp_id\n_pdbx_entity_branch_list.num\nE3 NAG 1\nE3 BMA 2\nE3 MAN 3\n"
      "#\nloop_\n_pdbx_entity_branch_link.link_id\n_pdbx_entity_branch_link.entity_id\n_pdbx_entity_branch_link.entity_branch_list_num_1\n_pdbx_entity_branch_link.comp_id_1\n_pdbx_entity_branch_link.atom_id_1\n_pdbx_entity_branch_link.leaving_atom_id_1\n_pdbx_entity_branch_link.entity_branch_list_num_2\n_pdbx_entity_branch_link.comp_id_2\n_pdbx_entity_branch_link.atom_id_2\n_pdbx_entity_branch_link.leaving_atom_id_2\n_pdbx_entity_branch_link.value_order\n"
      "1 E3 2 BMA C1 O1 1 NAG O4 HO4 sing\n2 E3 3 MAN C1 O1 2 BMA O3 HO3 sing\n"
      "#\nloop_\n_pdbx_branch_scheme.asym_id\n_pdbx_branch_scheme.entity_id\n_pdbx_branch_scheme.mon_id\n_pdbx_branch_scheme.num\nC E3 NAG 1\nC E3 BMA 2\nC E3 MAN 3\n")
def go(label, raw, exp, sel=(("A","E1",1),), **kw):
    o = outcome(lambda: run(raw, sel=sel, **kw)); good = o["result"]==exp; res.append(good)
    extra={}
    if o["result"]=="ACCEPTED":
        r=o["obj"]; cd={d.category:d for d in r.plan.category_decisions}
        extra={k: list(cd[k].kept_row_ordinals) for k in ("_pdbx_entity_branch_list","_pdbx_entity_branch_link","_pdbx_branch_scheme","_chem_comp") if k in cd}
    print(json.dumps({"probe":label,"expected":exp,"got":o["result"] if o["result"]=="ACCEPTED" else "REFUSED:"+str(o.get("code") or o.get("type")),"matches_contract":good,**extra}))
go("T021-071..074 branched retained by U=preserve, whole branch incl. unobserved MAN kept", G + BR, "ACCEPTED")
go("T021-086 branched retained but branch_scheme missing", G + BR.split("#\nloop_\n_pdbx_branch_scheme")[0], "REFUSED")
go("T021-073 link references unknown list num", G + BR.replace("2 E3 3 MAN C1 O1 2 BMA", "2 E3 9 MAN C1 O1 2 BMA"), "REFUSED")
go("T021-072 list comp/num mismatch vs atoms (NAG at 2)", G + BR.replace("E3 NAG 1\nE3 BMA 2", "E3 BMA 1\nE3 NAG 2"), "REFUSED")
go("P-3 NAG remove/BMA keep nonuniform", G + BR, "REFUSED",
   dispositions=(ResolvedComponentDisposition(label_asym_id="C", ccd_code="NAG", classification="other-non-polymer", disposition="remove"),
                 ResolvedComponentDisposition(label_asym_id="C", ccd_code="BMA", classification="other-non-polymer", disposition="keep")))
print("SUMMARY", sum(res), "/", len(res))
