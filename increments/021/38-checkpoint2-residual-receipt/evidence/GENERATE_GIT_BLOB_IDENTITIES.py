"""Generate final CP2 source/fixture identities from Git blob bytes, not checkout.
Usage: python -B GENERATE_GIT_BLOB_IDENTITIES.py /path/to/code-repo EXPECTED_HEAD
Redirect stdout only to the implementer's allowed governance evidence path.
Read-only: no checkout, staging, source edits or Git reference updates.
"""
import hashlib
import json
import pathlib
import re
import subprocess
import sys

repo=pathlib.Path(sys.argv[1]).resolve()
expected=sys.argv[2]
if re.fullmatch(r'[0-9a-f]{40}',expected) is None:
    raise SystemExit('EXPECTED_HEAD must be a full lowercase commit SHA')
def git(*args):
    return subprocess.check_output(['git','-C',str(repo),*args])
head=git('rev-parse','--verify','HEAD').decode('ascii').strip()
if head!=expected:
    raise SystemExit('Unexpected local HEAD: '+head)
allowed=['src/molecular/receptor_materialization.py','src/molecular/receptor_parsing.py','tests/test_receptor_materialization.py','tests/test_receptor_parsing.py']
fixture_root='tests/fixtures/receptor_materialization/'
paths=git('ls-tree','-r','--name-only',head,'--',*allowed,fixture_root).decode('utf-8').splitlines()
if not set(allowed).issubset(paths):
    raise SystemExit('Missing mandatory CP2 code paths')
files=[]
for path in sorted(paths):
    if path not in allowed and not path.startswith(fixture_root):
        raise SystemExit('Unexpected output path: '+path)
    raw=git('show',head+':'+path)
    blob=git('rev-parse',head+':'+path).decode('ascii').strip()
    computed=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    if computed!=blob:
        raise SystemExit('Git blob mismatch: '+path)
    files.append({'path':path,'lines_lf':raw.count(b'\n'),'size_bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'git_blob_sha':blob})
print(json.dumps({'code_commit':head,'method':'subprocess git show of immutable commit:path; stdout bytes; never working-tree bytes or newline-normalized text','files':files},ensure_ascii=False,indent=2))
