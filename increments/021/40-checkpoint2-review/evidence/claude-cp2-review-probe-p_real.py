import sys, os; sys.path.insert(0,'/tmp/probes')
from harness import *
import gemmi
from molecular.receptor_resolution import ResolvedComponentDisposition
R = '/tmp/run/tests/fixtures/receptor_materialization'
def cats(p):
    d = gemmi.cif.read(p); b = d.sole_block(); return set(n.lower().rstrip('.') for n in b.get_mmcif_category_names())
out = {}
for sub in sorted(os.listdir(R)):
    prov = json.load(open(f'{R}/{sub}/PROVENANCE.json'))
    names = list(prov['files'])
    orig, trim = [f'{R}/{sub}/{n}' for n in names]
    hashes_ok = all(hashlib.sha256(open(f'{R}/{sub}/{n}','rb').read()).hexdigest()==v['sha256'] and os.path.getsize(f'{R}/{sub}/{n}')==v['size_bytes'] for n,v in prov['files'].items())
    co, ct = cats(orig), cats(trim)
    removed_declared = set(c.lower() for c in prov['files'][names[1]].get('categories_removed', []))
    # lineage: every surviving category in trimmed equals original by raw tokens
    bo = gemmi.cif.read(orig).sole_block(); bt = gemmi.cif.read(trim).sole_block()
    diff_tokens = [c for c in ct if bo.get_mmcif_category(c+'.', raw=True) != bt.get_mmcif_category(c+'.', raw=True)]
    out[sub] = {"hashes_match_manifest": hashes_ok, "orig_categories": len(co), "trim_categories": len(ct),
                "removed_exactly_declared": (co - ct) == removed_declared and ct <= co, "surviving_categories_token_identical": not diff_tokens,
                "orig_vs_trim_block": (bo.name, bt.name)}
    # full native run on the ORIGINAL (unedited) bytes
    raw = open(orig,'rb').read()
    su = prov["scenario_usage"]
    if "resolved_chains" not in su:
        out[sub]["original_unedited_full_run"] = "n/a (no chain selection in manifest: " + json.dumps(su)[:160] + ")"; continue
    ch = tuple((c['label_asym_id'], c['label_entity_id'], su.get('resolved_model',1)) for c in su['resolved_chains'])
    o = outcome(lambda: run(raw, model=su.get('resolved_model',1), sel=ch, basis=su.get('model_resolution_basis','only-model-present')))
    out[sub]["original_unedited_full_run"] = o["result"] if o["result"]=="ACCEPTED" else f"REFUSED:{o.get('code') or o.get('type')}"
print(json.dumps(out, indent=1))
