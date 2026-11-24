"""Reviewer probe (ARCH-01/MINOR-6/MINOR-7): run in a FRESH process with gemmi and rdkit blocked by
sys.modules=None (no stub). Exercises the unmodified production module's pure path. inspection/resolution
objects here are documentary SimpleNamespace stand-ins (the 020 classes cannot be imported without gemmi);
ProteinInput and ReceptorSelectionPolicy are real 020 DTOs."""
import sys
sys.modules["gemmi"] = None; sys.modules["rdkit"] = None
sys.path.insert(0, sys.argv[1])
import hashlib, json
from datetime import datetime, timezone
from types import SimpleNamespace as NS
import molecular.receptor_materialization as rm
from molecular.inputs import AcquisitionRecord, ProteinInput, RawArtifact
from molecular.receptor_selection import ReceptorSelectionPolicy
out = {"optimize": sys.flags.optimize, "loaded_native_or_020_parser_modules": sorted(m for m in sys.modules if m in (
    "molecular.receptor_inspection", "molecular.receptor_resolution", "molecular.receptor_parsing") or m.split(".")[0] in ("gemmi", "rdkit") and sys.modules[m] is not None)}
RAW = "a" * 64
# independent hand-written legacy seven-field canonical bytes (NFC, sorted keys, compact, UTF-8)
legacy_bytes = ('{"inspection_profile_version":"1.0","inspection_schema_version":"1.0","parser_name":"gemmi",'
                '"parser_version":"0.7.5","protein_input_id":"protein-1","raw_checksum":"' + RAW + '","raw_format":"mmcif"}').encode()
LEGACY_LITERAL = hashlib.sha256(legacy_bytes).hexdigest()
out["legacy_hand_sha256"] = LEGACY_LITERAL
out["legacy_helper_equals_hand"] = rm._compute_legacy_inspection_id(parser_name="gemmi", parser_version="0.7.5",
    protein_input_id="protein-1", raw_checksum=RAW, raw_format="mmcif") == LEGACY_LITERAL
prot = ProteinInput(id="protein-1", name="P", acquisition=AcquisitionRecord(method="uploaded", acquired_at=datetime.now(timezone.utc),
        raw_artifact=RawArtifact(path="inputs/proteins/protein-1/raw.cif", format="mmcif", checksum=RAW)))
pol = ReceptorSelectionPolicy(schema_version="1.0", selection_id="sel-1", protein_input_id="protein-1", inspection_id=LEGACY_LITERAL,
        raw_checksum_observed=RAW, declared_by="s", declared_at=datetime.now(timezone.utc))
parser = NS(name="gemmi", version="0.7.5")
insp = NS(inspection_id=LEGACY_LITERAL, inspection_schema_version="1.0", inspection_profile_version="1.0", protein_input_id="protein-1",
          raw_checksum=RAW, raw_format_declared="mmcif", structure_format="mmcif", parser=parser, selection_capability="full", warnings=())
res = NS(resolved_selection_id="sel-1", policy_selection_id="sel-1", protein_input_id="protein-1", inspection_id=LEGACY_LITERAL,
         raw_checksum=RAW, structure_format="mmcif", parser=parser, resolved_model=1, resolved_assembly=None,
         resolved_chains=(NS(label_asym_id="A", label_entity_id="E1", model_number=1),), resolved_component_dispositions=())
R = rm.RecordSnapshot
recs = (R(kind="protein", id="protein-1", sha256="1"*64, size_bytes=1, schema_version=None), R(kind="inspection", id=LEGACY_LITERAL, sha256="2"*64, size_bytes=1, schema_version="1.0"),
        R(kind="selection", id="sel-1", sha256="3"*64, size_bytes=1, schema_version="1.0"), R(kind="resolution", id="sel-1", sha256="4"*64, size_bytes=1, schema_version="1.0"))
try:
    sc = rm.build_source_context(protein_input=prot, inspection_report=insp, policy=pol, resolved_selection=res, raw_size_bytes=10, records=recs)
    plan = rm.build_materialization_plan(source_context=sc, resolved_selection=res, unaddressed_components="preserve",
        atoms=(rm.AtomObservation(ordinal=0, atom_id="a1", model=1, label_asym_id="A", entity_id="E1", entity_type="polymer", ccd="ALA", label_seq_id="1"),))
    pr = rm.build_policy_record(materialization_plan=plan, acknowledge_plan_key=plan.plan_key, acknowledge_exclusions_key=None,
        acknowledge_outside_key=None, declared_by="s", declared_at="2026-01-01T00:00:00.000000Z")
    out["pure_pipeline"] = {"source_context_key": sc and rm.compute_source_context_key(sc)[:12], "plan_key": plan.plan_key[:12], "policy_id": pr.policy_id[:12]}
except Exception as e:
    out["pure_pipeline"] = f"{type(e).__name__}: {e}"
for cls in (rm.MaterializationInputError, rm.MaterializationConfigurationError):
    try: cls("NOT_A_CODE", "x"); out[cls.__name__ + "_unknown"] = "accepted"
    except ValueError as e: out[cls.__name__ + "_unknown"] = "rejected: " + type(e).__name__
out["valid_code_phase"] = [rm.MaterializationInputError("INVALID_ID", "x").phase, rm.MaterializationConfigurationError("INVALID_RECORD", "x").phase]
out["after_run_native_or_020_parser_modules"] = sorted(m for m in sys.modules if m in ("molecular.receptor_inspection", "molecular.receptor_resolution", "molecular.receptor_parsing"))
print(json.dumps(out, indent=1))
