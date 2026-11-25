import sys; sys.path.insert(0,'/tmp/probes')
from harness import *
import molecular.receptor_parsing as rp, molecular.receptor_materialization as rm
B = BASE
run(B)  # warm: ensures gemmi imported
G = rp.gemmi
# ---- interruptions at real CP2 boundaries, both classes, identity preserved
boundaries = {
 "parse(gemmi.cif.read_string)": (G.cif, "read_string"),
 "plan(rm.build_materialization_plan)": (rm, "build_materialization_plan"),
 "plan(rm.resolve_connection_decisions)": (rm, "resolve_connection_decisions"),
 "plan(rm.compute_category_decisions)": (rm, "compute_category_decisions"),
 "serialize(rp.serialize_cif_document021)": (rp, "serialize_cif_document021"),
 "verify(rp.reparse_and_extract_cif_dom021)": (rp, "reparse_and_extract_cif_dom021"),
 "verify(rp._verify_output_reparse)": (rp, "_verify_output_reparse"),
}
for label, (owner, attr) in boundaries.items():
    for cls in (KeyboardInterrupt, SystemExit):
        inst = cls(7) if cls is SystemExit else cls()
        orig = getattr(owner, attr)
        def boom(*a, **k): raise inst
        setattr(owner, attr, boom)
        try:
            run(B); got = "NO-RAISE"
        except BaseException as e:
            got = "same-instance" if e is inst else f"other:{type(e).__name__}"
        finally:
            setattr(owner, attr, orig)
        print(json.dumps({"interrupt": label, "class": cls.__name__, "propagated": got}))
# ---- taxonomy of CP2 failures (spec §16 / brief §5)
big = B.encode() + b"#" * (16*1024*1024 + 1 - len(B.encode()))
cases = {
 "raw_over_16MiB": big,
 "gzip_magic": b"\x1f\x8b" + B.encode(),
 "bom": b"\xef\xbb\xbf" + B.encode(),
 "two_blocks": (B + "\ndata_two\n_entry.id x\n").encode(),
 "syntax_error": (B + "\nloop_\n_x.a\n_x.b\n1\n").encode(),
 "entity_missing_for_atom": B.replace("E2 polymer\n", "").encode(),
 "unknown_category": (B + "\n_zzz_unknown.tag 1\n").encode(),
}
for label, raw in cases.items():
    o = outcome(lambda: run(raw))
    print(json.dumps({"taxonomy": label, "type": o.get("type"), "code": o.get("code"), "phase": o.get("phase"),
                      "is_021_execution_error": o.get("type") == "MaterializationExecutionError"}))
