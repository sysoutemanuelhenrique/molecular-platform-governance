"""Reviewer scratch script: evaluate CATALOG_021.json category/tag coverage against inventories
produced by cif_inventory (Gemmi 0.7.5 DOM). Reads only; prints JSON."""
import json, sys
cat_path, *invs = sys.argv[1:]
c = json.load(open(cat_path))
cats = {k.lower(): v for k, v in c['categories'].items()}
prefixes = [p.lower() for p in c['allowed_omission_prefixes']]
out = {}
for inv in invs:
    res = {'categories': 0, 'unknown_categories': [], 'unknown_tags_in_filtered': {}, 'missing_required_tags': {},
           'operator_tables_present': [], 'struct_conn_symmetry': {}}
    for line in open(inv):
        p = line.split()
        if p[0] == 'CAT':
            name = p[1].rstrip('.').lower(); tags = [t.lower() for t in p[3:]]
            res['categories'] += 1
            if name in ('_symmetry_equiv', '_space_group_symop'): res['operator_tables_present'].append(name)
            e = cats.get(name)
            if e is None:
                if not any(name.startswith(x) for x in prefixes): res['unknown_categories'].append(name)
                continue
            if e['action'] == 'filter':
                known = set(map(str.lower, e.get('preserve_tags', []) + e.get('omit_tags', []) + e.get('generate_tags', [])))
                unk = [t for t in tags if t not in known]
                if unk: res['unknown_tags_in_filtered'][name] = unk
                miss = [t for t in map(str.lower, e.get('required_tags', [])) if t not in tags]
                if miss: res['missing_required_tags'][name] = miss
        elif p[0] == 'CONN':
            k = f'{p[2]} {p[3]} {p[4]}'; res['struct_conn_symmetry'][k] = res['struct_conn_symmetry'].get(k, 0) + 1
    out[inv.rsplit('/', 1)[-1]] = res
print(json.dumps(out, indent=1))
