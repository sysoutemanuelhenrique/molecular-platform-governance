import sys; sys.path.insert(0,'/tmp/probes')
from harness import *
from cifgen import *
r = make([row("c1","disulf","B1SD","1_555","B1CE","1_555")], symeq=[("1","x,y,z")], sgop=[("1","'+x, +y, z'")])
o = outcome(lambda: run(r)); d=o["obj"].plan.connection_decisions[0]
print(json.dumps({"case":"op1_in_both_tables_concordant_K0_fixed","basis":d.identity_basis,"class":d.symmetry_class,
   "matches_contract": tuple(d.identity_basis)==("source-operator","source-operator") and d.symmetry_class=="both-identity"}))
# Direct mechanism: decoded "?" re-collapsed by domain
import molecular.receptor_materialization as rm
print("domain treats decoded quoted-? as null:", rm._resolve_symmetry_endpoint("?", rm.SymmetryOperatorTables(None,None)).is_null)
# Same quoted '?' at K=0 vs bare ? -> identical ConnectionDecision (collision of two distinct sources' semantics)
a = run(make([row("c1","disulf","B1SD","'?'","B1CE","1_555")])).plan.connection_decisions[0]
b = run(make([row("c1","disulf","B1SD","?","B1CE","1_555")])).plan.connection_decisions[0]
print(json.dumps({"quoted_vs_bare_same_class": a.symmetry_class==b.symmetry_class, "quoted": a.symmetry_class, "bare": b.symmetry_class,
                  "row_keys_differ": a.row_key!=b.row_key}))
