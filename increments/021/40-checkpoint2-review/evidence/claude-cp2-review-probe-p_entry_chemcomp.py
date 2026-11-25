import sys; sys.path.insert(0,'/tmp/probes')
from harness import *
B = BASE
res=[]
def chk(label, raw, exp, extra=None):
    o = outcome(lambda: run(raw)); good = o["result"]==exp; res.append(good)
    rec={"probe":label,"expected":exp,"got":o["result"] if o["result"]=="ACCEPTED" else f"REFUSED:{o.get('code') or o.get('type')}","matches_contract":good}
    if extra and o["result"]=="ACCEPTED": rec.update(extra(o["obj"]))
    print(json.dumps(rec))
cc = lambda r: {"chem_comp_out_rows": r.reparsed.categories["chem_comp"].row_count, "chem_comp_out_ids": list(r.reparsed.categories["chem_comp"].columns["id"])}
chk("chem_comp duplicate id (T021-087)", B.replace("MET 'L-peptide linking'\n", "MET 'L-peptide linking'\nALA 'L-peptide linking'\n"), "REFUSED", cc)
chk("chem_comp null id row", B.replace("MET 'L-peptide linking'\n", "MET 'L-peptide linking'\n? 'L-peptide linking'\n"), "REFUSED", cc)
ent = lambda r: {"entry_decision": {k: (list(v) if isinstance(v, tuple) else v) for k, v in next(d for d in r.plan.category_decisions if d.category=="_entry").model_dump().items()}}
chk("entry unknown source tag (unknown_tag_action=reject)", B.replace("_entry.id 5XYZ\n", "_entry.id 5XYZ\n_entry.zz_unknown 1\n"), "REFUSED", ent)
chk("entry duplicate id rows", B.replace("_entry.id 5XYZ\n", "loop_\n_entry.id\n5XYZ\n5XYZ\n"), "REFUSED", ent)
r = run(B); d = next(x for x in r.plan.category_decisions if x.category=="_entry")
print(json.dumps({"entry_with_source_row": {"source_rows_key": d.source_rows_key, "kept": list(d.kept_row_ordinals), "omitted": list(d.omitted_row_ordinals),
      "schemas_requires_nonnull_key_and_row_coverage": True, "matches_contract": d.source_rows_key is not None and len(d.kept_row_ordinals)+len(d.omitted_row_ordinals)==1}}))
print("SUMMARY", sum(res), "/", len(res))
