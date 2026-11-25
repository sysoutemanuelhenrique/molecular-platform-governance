import sys; sys.path.insert(0,'/tmp/probes')
from harness import *
from cifgen import *
ok = []
# K endpoints: K2: A1CA-A1N ; K1: A2SG-B1SD (B removed by chain-complement) ; K0: B1SD-B1CE
K = {2: ("A1CA","A1N","disulf"), 1: ("A2SG","B1SD","metalc"), 0: ("B1SD","B1CE","disulf")}
CELLS = {"both-identity": ("1_555","1_555"), "same-nonidentity": ("2_555","2_555"), "different": ("2_555","3_555"),
         "one-null": (".","1_555"), "both-null": (".","?")}
EXP = {2: {"both-identity": "preserve"}, 1: {"both-identity": "omit"}, 0: {c: "omit" for c in CELLS}}
sid = {(2,c): f"T021-0{45+i}" for i,c in enumerate(CELLS)} | {(1,c): f"T021-0{50+i}" for i,c in enumerate(CELLS)} | {(0,c): f"T021-0{55+i}" for i,c in enumerate(CELLS)}
for k,(e1,e2,ct) in K.items():
    for cell,(s1,s2) in CELLS.items():
        raw = make([row("c1", ct, e1, s1, e2, s2)], symeq=STD)
        o = outcome(lambda: run(raw))
        exp = EXP[k].get(cell, "REFUSE")
        if o["result"] == "ACCEPTED":
            d = o["obj"].plan.connection_decisions[0]
            got = d.action; detail = {"symmetry_class": d.symmetry_class, "basis": d.identity_basis, "reason": d.reason, "K": d.retained_endpoints}
        else:
            got = "REFUSE"; detail = {"code": o["code"]}
        ok.append(got == exp)
        print(json.dumps({"scenario": sid[(k,cell)], "K": k, "cell": cell, "tables": "symmetry_equiv", "expected": exp, "got": got, **detail}))
# K=1 covalent must refuse (COVALENT_CUT) at identity
o = outcome(lambda: run(make([row("c1","disulf","A2SG","1_555","B1SD","1_555")], symeq=STD)))
print(json.dumps({"scenario":"T021-050b","K":1,"type":"disulf","expected":"REFUSE COVALENT_CUT","got":o.get("code") or o["result"]})); ok.append(o.get("code")=="COVALENT_CUT")
# same 15 cells without tables where only 1_555 can be identity (convention)
for k,(e1,e2,ct) in K.items():
    s1,s2 = ("1_555","1_555")
    o = outcome(lambda: run(make([row("c1", ct, e1, s1, e2, s2)])))
    d = o["obj"].plan.connection_decisions[0] if o["result"]=="ACCEPTED" else None
    print(json.dumps({"scenario":"T021-141","K":k,"no_tables":True,"got": d.action if d else o.get("code"), "basis": d.identity_basis if d else None}))
    ok.append(d is not None and d.identity_basis==("pdbx-1_555-convention","pdbx-1_555-convention"))
print("SUMMARY", sum(ok), "/", len(ok))
