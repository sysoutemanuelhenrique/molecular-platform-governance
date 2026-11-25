"""Independent reviewer harness: real Gemmi 0.7.5 (built from pin 5cc1c23) +
production entry point materialize_receptor_cif021 at a807b03. Builds the
SourceContext from the exact probe bytes (real raw hash/size)."""
import sys, hashlib, importlib.util, json, traceback
sys.path.insert(0, '/tmp/run/src')
spec = importlib.util.spec_from_file_location('tparse', '/tmp/run/tests/test_receptor_parsing.py')
tp = importlib.util.module_from_spec(spec); spec.loader.exec_module(tp)
import molecular.receptor_parsing as rp
import molecular.receptor_materialization as rm
from molecular.receptor_resolution import ResolvedChainSelection, ResolvedComponentDisposition
assert rp.gemmi is None or True

BASE = tp._MINIMAL_CIF

def chains(*specs):
    return tuple(ResolvedChainSelection(label_asym_id=a, label_entity_id=e, model_number=m) for a, e, m in specs)

def run(raw: str | bytes, *, model=1, sel=(("A","E1",1),), unaddressed="preserve", dispositions=(), basis="only-model-present"):
    b = raw.encode('utf-8') if isinstance(raw, str) else raw
    return tp._real_fixture_materialize(pdbid="PROBE", raw_bytes=b, resolved_model=model,
        resolved_chains=chains(*sel), model_basis=basis, unaddressed=unaddressed, dispositions=dispositions)

def outcome(fn):
    try:
        r = fn()
        return {"result": "ACCEPTED", "plan_key": r.plan.plan_key, "obj": r}
    except BaseException as e:
        if isinstance(e, (KeyboardInterrupt, SystemExit)): raise
        return {"result": "REFUSED", "type": type(e).__name__, "code": getattr(e, "code", None),
                "phase": getattr(e, "phase", None), "cause": type(e.__cause__).__name__ if e.__cause__ else None}

def show(label, o, expect):
    keep = {k: v for k, v in o.items() if k != "obj"}
    ok = (o["result"] == expect)
    print(json.dumps({"probe": label, "expected": expect, **keep, "matches_contract": ok}))
    return ok
