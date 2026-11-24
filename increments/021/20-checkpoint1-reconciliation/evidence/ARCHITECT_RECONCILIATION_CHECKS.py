"""Read-only architect reconciliation probes; runs no pytest or native Gemmi."""
import hashlib
import argparse
import importlib.util
import json
import pathlib
import subprocess
import sys
import pydantic

HERE = pathlib.Path(__file__).resolve().parent
args = argparse.ArgumentParser()
args.add_argument('--code-root', required=True)
args.add_argument('--review-evidence-dir', required=True)
args.add_argument('--output', required=True)
opts = args.parse_args()
SRC = pathlib.Path(opts.code_root).resolve() / 'src'
REVIEW = pathlib.Path(opts.review_evidence_dir).resolve()
for filename, expected in {
    'claude-domain-probes.py': '17cd9717b737686d093e24a1b95fd5d78dc9a1e7',
    'claude-canonical-and-strict.py': '364194e8143d4708e133e3cc1e4116fe5d71eec6',
}.items():
    b = (REVIEW / filename).read_bytes()
    actual = hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()
    if actual != expected: raise ValueError('Reviewer script identity mismatch: ' + filename)

def run(script, *, sentinel=False, optimize=False):
    # Source bytes are unmodified. The optional import-only diagnostic sentinel
    # is explicitly labelled and cannot service any native attribute access.
    prefix = 'import sys,types,runpy;sys.path.insert(0,' + repr(str(SRC)) + ');'
    if sentinel:
        prefix += "g=types.ModuleType('gemmi');g.__doc__='Architect inert import-only sentinel';\n"
        prefix += "def fail(n):\n if n.startswith('__'): raise AttributeError(n)\n raise AssertionError('native access forbidden: '+n)\n"
        prefix += "g.__getattr__=fail;sys.modules['gemmi']=g;\n"
    code = prefix + script
    p = subprocess.run([sys.executable, '-I', '-B', *(['-O'] if optimize else []), '-c', code], capture_output=True, text=True)
    return {'returncode': p.returncode, 'stdout': p.stdout, 'stderr': p.stderr, 'sentinel': sentinel, 'optimized': optimize}

out = {'python': sys.version.split()[0], 'pydantic': pydantic.__version__, 'scope': 'architect reconciliation, not independent review closure',
       'source_commit': '711f3070765efe67a5799f939f1a18306ed8afdd',
       'gemmi_available': importlib.util.find_spec('gemmi') is not None,
       'pytest_available': importlib.util.find_spec('pytest') is not None,
       'pytest_executed': False, 'source_modified': False}
out['clean_import'] = run('import molecular.receptor_materialization')
payload = {'inspection_schema_version':'1.0','inspection_profile_version':'1.0','parser_name':'gemmi','parser_version':'0.7.5','protein_input_id':'p1','raw_checksum':'a'*64,'raw_format':'mmcif'}
pure = run("import json;from molecular.promotion import compute_semantic_key;print(json.dumps({'inspection_id':compute_semantic_key("+repr(payload)+"),'gemmi_loaded':'gemmi' in sys.modules}))")
old = run("from molecular.receptor_inspection import compute_inspection_id;print(compute_inspection_id(parser_name='gemmi',parser_version='0.7.5',protein_input_id='p1',raw_checksum='a'*64,raw_format='mmcif'))",sentinel=True)
if pure['returncode'] or old['returncode']:raise RuntimeError('Legacy backend compatibility diagnostic failed')
comparison=json.loads(pure['stdout'])
out['legacy_pure_backend_compatibility']={'payload':payload,'pure_backend_result':comparison,'old_helper_id_with_import_sentinel':old['stdout'].strip(),'hashes_match':comparison['inspection_id']==old['stdout'].strip(),'note':'Pure backend was imported without sentinel; old inspection helper comparison used import-only sentinel, not native parsing.'}
for name in ['claude-domain-probes.py', 'claude-canonical-and-strict.py']:
    r = run('runpy.run_path(' + repr(str(REVIEW / name)) + ",run_name='__main__')", sentinel=True)
    if r['returncode'] != 0: raise RuntimeError(r['stderr'])
    data = json.loads(r.pop('stdout'))
    expected = json.loads((REVIEW / name.replace('.py', '.output.json')).read_text())
    comparable = 'probes' if 'domain' in name else 'golden'
    r['same_results_as_published_review'] = data[comparable] == expected[comparable]
    r['result'] = data
    out[name] = r

extra = '''
from pydantic import ValidationError
import molecular.receptor_materialization as r
import json
def attempt(fn):
 try:
  v=fn();return {'accepted':True,'value':str(v)}
 except Exception as e:
  return {'accepted':False,'error':type(e).__name__,'message':str(e)}
tests={
 'omit_kept_row':lambda:r.CategoryDecision(category='_struct_conf',action='omit',kept_row_ordinals=(0,)),
 'filter_negative_ordinal':lambda:r.CategoryDecision(category='_atom_site',action='filter',kept_row_ordinals=(-1,)),
 'filter_rows_without_source_hash':lambda:r.CategoryDecision(category='_atom_site',action='filter',kept_row_ordinals=(0,)),
 'unknown_input_code':lambda:r.MaterializationInputError('NOT_A_CODE','probe'),
 'unknown_config_code':lambda:r.MaterializationConfigurationError('NOT_A_CODE','probe'),
}
print(json.dumps({k:attempt(fn) for k,fn in tests.items()}))
'''
for optimized in [False, True]:
    rr = run(extra, sentinel=True, optimize=optimized)
    rr['results'] = json.loads(rr.pop('stdout'))
    out['additional_optimized' if optimized else 'additional_normal'] = rr

pathlib.Path(opts.output).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'clean_import_returncode':out['clean_import']['returncode'],
 'domain_probes_count':len(out['claude-domain-probes.py']['result']['probes']),
 'domain_results_match':out['claude-domain-probes.py']['same_results_as_published_review'],
 'golden_results_match':out['claude-canonical-and-strict.py']['same_results_as_published_review'],
 'python':out['python'],'pytest_executed':False},indent=2))
