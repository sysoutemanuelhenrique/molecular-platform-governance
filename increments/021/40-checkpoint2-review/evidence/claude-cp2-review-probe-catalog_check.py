import json, sys, hashlib
sys.path.insert(0, '/tmp/run/src')
import molecular.receptor_materialization as rm
p = sys.argv[1]
b = open(p,'rb').read()
print('CATALOGUE_SHA256 const == annex bytes:', rm.CATALOGUE_SHA256 == hashlib.sha256(b).hexdigest())
c = json.loads(b)['categories']
mism = []
fields = ['action','key','required_tags','preserve_tags','omit_tags','generate_tags','row_rule','references']
for name, d in c.items():
    f = rm._FROZEN_CATALOGUE.get(name)
    if f is None: mism.append((name,'missing')); continue
    for k in fields:
        a = d.get(k); bb = f.get(k)
        if isinstance(a, list): a = tuple(a)
        if k=='references' and a is not None: a = dict(a)
        if a != bb: mism.append((name,k,a,bb))
extra = set(rm._FROZEN_CATALOGUE) - set(c)
print('categories', len(c), 'embedded', len(rm._FROZEN_CATALOGUE), 'extra', extra)
print('mismatches', len(mism)); [print(' ', m) for m in mism[:10]]
j = json.loads(b)
print('required eq', tuple(j['required_categories']) == rm._CATALOGUE_REQUIRED_CATEGORIES)
print('conditional eq', {k:tuple(v) for k,v in j['conditional_categories'].items()} == rm._CATALOGUE_CONDITIONAL_CATEGORIES)
print('omission family pattern', rm._CATALOGUE_OMISSION_FAMILY_PATTERN.pattern)
print('extra fields in annex categories', sorted({k for d in c.values() for k in d} - set(fields)))
