import sys, os; sys.path.insert(0,'/tmp/probes')
from harness import *
from cifgen import *
ok=[]
def k0(s1,s2,**t): return make([row("c1","disulf","B1SD",s1,"B1CE",s2)], **t)
def k2(s1,s2,**t): return make([row("c1","disulf","A1CA",s1,"A1N",s2)], **t)
cases = [
 # label, K0 raw, K2 raw, expected K0 basis, expected K0 class, expected K2 outcome
 ("quoted_question_mark", k0("'?'","1_555"), k2("'?'","1_555"), ("not-applicable","pdbx-1_555-convention"), "unsupported-discarded", "REFUSE"),
 ("quoted_dot", k0("'.'","1_555"), k2("'.'","1_555"), ("not-applicable","pdbx-1_555-convention"), "unsupported-discarded", "REFUSE"),
 ("leading_zero_01_555", k0("01_555","1_555"), k2("01_555","1_555"), ("not-applicable","pdbx-1_555-convention"), "unsupported-discarded", "REFUSE"),
 ("2_555_no_tables", k0("2_555","2_555"), k2("2_555","2_555"), ("not-applicable","not-applicable"), "unsupported-discarded", "REFUSE"),
 ("1_556_no_tables", k0("1_556","1_555"), k2("1_556","1_555"), ("not-applicable","pdbx-1_555-convention"), "unsupported-discarded", "REFUSE"),
 ("not_located_4_555", k0("4_555","1_555",symeq=STD), k2("4_555","1_555",symeq=STD), ("not-applicable","source-operator"), "unsupported-discarded", "REFUSE"),
 ("dup_id_same_table", k0("1_555","1_555",symeq=[("1","x,y,z"),("1","x,y,z")]), k2("1_555","1_555",symeq=[("1","x,y,z"),("1","x,y,z")]), ("not-applicable","not-applicable"), "unsupported-discarded", "REFUSE"),
 ("contradiction_between_tables", k0("1_555","1_555",symeq=[("1","x,y,z")],sgop=[("1","-x,y,z")]), k2("1_555","1_555",symeq=[("1","x,y,z")],sgop=[("1","-x,y,z")]), ("not-applicable","not-applicable"), "unsupported-discarded", "REFUSE"),
 ("op1_nonidentity", k0("1_555","1_555",symeq=[("1","-x,-y,z")]), k2("1_555","1_555",symeq=[("1","-x,-y,z")]), ("source-operator","source-operator"), "unsupported-discarded", "REFUSE"),
 ("op1_only_in_one_of_two_tables", k0("1_555","1_555",symeq=[("1","x,y,z")],sgop=[("2","-x,-y,z")]), k2("1_555","1_555",symeq=[("1","x,y,z")],sgop=[("2","-x,-y,z")]), ("source-operator","source-operator"), "unsupported-discarded", "REFUSE"),
 ("op1_in_both_tables_concordant", k0("1_555","1_555",symeq=[("1","x,y,z")],sgop=[("1"," +x, +y, z")]), k2("1_555","1_555",symeq=[("1","x,y,z")],sgop=[("1","'+x, +y, +z'")]), ("source-operator","source-operator"), "both-identity", "preserve"),
 ("x_plus_0_identity_outside_grammar", k0("1_555","1_555",symeq=[("1","x+0,y,z")]), k2("1_555","1_555",symeq=[("1","x+0,y,z")]), ("source-operator","source-operator"), "unsupported-discarded", "REFUSE"),
 ("assembly_oper_list_not_a_symmetry_table", k0("1_555","1_555") + "#\nloop_\n_pdbx_struct_oper_list.id\n_pdbx_struct_oper_list.type\n1 'identity operation'\n", None, ("pdbx-1_555-convention","pdbx-1_555-convention"), "both-identity", None),
]
for label, r0, r2, b0, c0, e2 in cases:
    o = outcome(lambda: run(r0))
    if o["result"]=="ACCEPTED":
        d=o["obj"].plan.connection_decisions[0]; g0=(tuple(d.identity_basis), d.symmetry_class)
    else: g0=("REFUSED", o["code"])
    good0 = g0==(b0,c0)
    g2=None; good2=True
    if r2 is not None:
        o2 = outcome(lambda: run(r2))
        g2 = o2["obj"].plan.connection_decisions[0].action if o2["result"]=="ACCEPTED" else "REFUSE"
        good2 = g2==e2
        if g2=="REFUSE": g2 += ":"+str(o2["code"])
    ok.append(good0 and good2)
    print(json.dumps({"case":label,"K0_expected":[b0,c0],"K0_got":g0,"K2_expected":e2,"K2_got":g2,"matches_contract":good0 and good2}))
print("SUMMARY",sum(ok),"/",len(ok))
