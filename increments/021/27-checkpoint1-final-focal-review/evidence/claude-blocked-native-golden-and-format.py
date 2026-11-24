"""Fresh process, gemmi/rdkit blocked via sys.modules=None (no stub). Calls the unmodified production entry points
at bbd491e on the documentary MINOR-7 inputs and compares with the 13 literals parsed from the test file; also runs
the residual MAJOR-A format check on the pure path. argv: <src> <test_file>."""
import sys
sys.modules["gemmi"] = None; sys.modules["rdkit"] = None
sys.path.insert(0, sys.argv[1])
import json, re
from datetime import datetime, timezone
from types import SimpleNamespace as NS
import molecular.receptor_materialization as rm
from molecular.inputs import AcquisitionRecord, ProteinInput, RawArtifact
from molecular.receptor_selection import ReceptorSelectionPolicy
WATCH = ("molecular.receptor_inspection", "molecular.receptor_resolution", "molecular.receptor_parsing")
def loaded(): return sorted(m for m in sys.modules if (m in WATCH or m.split(".")[0] in ("gemmi", "rdkit")) and sys.modules[m] is not None)
out = {"optimize": sys.flags.optimize, "loaded_before": loaded()}
L = dict(re.findall(r'^_GOLDEN_([A-Z_]+)_SHA256 = "([0-9a-f]{64})"', open(sys.argv[2], encoding="utf-8").read(), re.M))
E = rm.Engine(name="gemmi", version="0.7.5"); R = rm.RecordSnapshot
sc = rm.SourceContext(protein_input_id="protein-1", selection_id="sel-1", inspection_id="2b367d0134006b35c4f878984e6b0cc613f5a27db5e00bc20b42044381b1b3f6", model=1,
    records=(R(kind="protein", id="protein-1", sha256="1bffa22ef057ae13d72de8812a363194cd35c0fa1b136bd24faa37b322a843b1", size_bytes=66, schema_version=None),
             R(kind="inspection", id="2b367d0134006b35c4f878984e6b0cc613f5a27db5e00bc20b42044381b1b3f6", sha256="64b982b230587eb5983408d68105abd62c45c879830f53754232694639230d83", size_bytes=124, schema_version="1.0"),
             R(kind="selection", id="sel-1", sha256="409ea1325548b16b3de5ef6312e43cf70d247a3a30565a5612e01fa2c08a3ba5", size_bytes=64, schema_version="1.0"),
             R(kind="resolution", id="sel-1", sha256="02fb0364edff743c45709d19f707afd25e242f569109b951992b16abbcbbcf3d", size_bytes=65, schema_version="1.0")),
    raw_sha256="d020364a30da702323fe02b6b5d10f1861dbb7c6817c61b34a2648037b3b5927", raw_size_bytes=61, raw_format="mmcif", inspection_schema="1.0", inspection_profile="1.0", parser=E)
SCK = rm.compute_source_context_key(sc)
ow = rm.OccurrenceIdentity(model=1, label_asym_id="W", entity_id="EW", ccd="HOH", label_seq_id=None, auth_asym_id="W", auth_seq_id="17", insertion_token=None)
oa = rm.OccurrenceIdentity(model=1, label_asym_id="A", entity_id="E1", ccd="ALA", label_seq_id="1", auth_asym_id="A", auth_seq_id="1", insertion_token=None)
ob = rm.OccurrenceIdentity(model=1, label_asym_id="B", entity_id="E2", ccd="ALA", label_seq_id="1", auth_asym_id="B", auth_seq_id="1", insertion_token=None)
kw, ka, kb = (rm.compute_occurrence_key(i) for i in (ow, oa, ob))
def A(o, a, **kw2): return rm.AtomObservation(ordinal=o, atom_id=a, model=1, **kw2)
ib = rm.compute_atom_ids_key((A(1, "b1", label_asym_id="B", entity_id="E2", entity_type="polymer", ccd="ALA", label_seq_id="1"),))
iw = rm.compute_atom_ids_key((A(2, "w1", label_asym_id="W", entity_id="EW", entity_type="water", ccd="HOH", label_seq_id=None, auth_seq_id="17"),))
x = rm.XEntry(model=1, label_asym_id="B", entity_id="E2", atom_count=1, atom_ids_key=ib)
o = rm.OutsideEntry(identity=ow, occurrence_key=kw, decision_source="unaddressed-preserve", atom_count=1, atom_ids_key=iw, author_id_coincidence="none")
xk = rm.compute_exclusions_key(source_context_key=SCK, model=1, entries=(x,)); okk = rm.compute_outside_key(source_context_key=SCK, model=1, entries=(o,))
D = rm.AtomDecision
ak = rm.compute_atom_decisions_key(source_context_key=SCK, decisions=(D(ordinal=0, atom_id="a1", occurrence_key=ka, retained=True, reason="selected-asym"),
     D(ordinal=1, atom_id="b1", occurrence_key=kb, retained=False, reason="chain-complement"), D(ordinal=2, atom_id="w1", occurrence_key=kw, retained=True, reason="unaddressed-preserve")))
ck = rm.compute_connection_decisions_key(source_context_key=SCK)
gk = rm.compute_category_decisions_key(source_context_key=SCK, decisions=(rm.CategoryDecision(category="_atom_site", action="filter", kept_row_ordinals=(0, 2), omitted_row_ordinals=(1,),
     preserved_tags=("id",), omitted_tags=(), generated_tags=(), source_rows_key="69d7a6a8fe0baba92f59dad6a6930ea5e9ad78ce6372833af7cfe1a4a073c2a6"),))
plan = rm.PlanBinding(catalogue_sha256=rm.CATALOGUE_SHA256, engine=E, sources=sc, source_context_key=SCK, selected_asym_ids=("A",), unaddressed_components="preserve",
    exclusions=(x,), outside=(o,), exclusions_key=xk, outside_key=okk, atom_decisions_key=ak, connection_decisions_key=ck, category_decisions_key=gk, unavailable_categories=(), warnings=("outside-selected-asym-retained",))
pk = rm.compute_plan_key(plan)
pid = rm.compute_policy_id(plan_key=pk, acknowledge_plan_key=pk, acknowledge_exclusions_key=xk, acknowledge_outside_key=okk, declared_by="documentary scientist")
rq = rm.compute_request_key(policy_id=pid, policy_file_sha256="9111f3e2210af7359155992b55b689f67f77a195e29e6a979c28a55e679a1d63", source_context_key=SCK, plan_key=pk,
    profile="1.0", algorithm="1.0", catalogue_sha256=rm.CATALOGUE_SHA256, engine=E, application_version="0.0.0-documentary")
prod = {"CANONICAL_JSON": rm.compute_materialization_hash({"version": "1.0", "kind": "k", "s": "éÅ", "l": [2, 1], "n": None, "b": True}),
        "LEGACY_INSPECTION_ID": rm._compute_legacy_inspection_id(parser_name="gemmi", parser_version="0.7.5", protein_input_id="protein-1", raw_checksum="a" * 64, raw_format="mmcif"),
        "SOURCE_CONTEXT_KEY": SCK, "OCCURRENCE_KEY": kw, "ATOM_IDS_KEY": ib, "EXCLUSIONS_KEY": xk, "OUTSIDE_KEY": okk, "ATOM_DECISIONS_KEY": ak,
        "CONNECTION_DECISIONS_KEY": ck, "CATEGORY_DECISIONS_KEY": gk, "PLAN_KEY": pk, "POLICY_ID": pid, "REQUEST_KEY": rq}
out["production_vs_literal"] = {k: prod[k] == L[k] for k in L}; out["literal_count"] = len(L)
out["derived_inputs_match_test_values"] = {"w_atom_ids_key": iw == "8eeed5d55f10287690bf61adfaffbec360b1dd75af6cb380872e1c3c7fd1eb13",
    "occ_a": ka == "c7be110af90a4a6028070621a83de375e8fc75c67f16d67f7df84115e66e147d", "occ_b": kb == "c130a69653371b5fd775a994dc3fde9e2f892a147478289054f8cc1b5367bd57"}
# MAJOR-A residual on the pure path (documentary NS inspection/resolution; real ProteinInput/policy)
LIT = L["LEGACY_INSPECTION_ID"]; RAW = "a" * 64; P = NS(name="gemmi", version="0.7.5")
def fmt(acq, dec):
    prot = ProteinInput(id="protein-1", name="P", acquisition=AcquisitionRecord(method="uploaded", acquired_at=datetime.now(timezone.utc),
        raw_artifact=RawArtifact(path="inputs/proteins/protein-1/raw.cif", format=acq, checksum=RAW)))
    pol = ReceptorSelectionPolicy(schema_version="1.0", selection_id="sel-1", protein_input_id="protein-1", inspection_id=LIT, raw_checksum_observed=RAW, declared_by="s", declared_at=datetime.now(timezone.utc))
    insp = NS(inspection_id=LIT, inspection_schema_version="1.0", inspection_profile_version="1.0", protein_input_id="protein-1", raw_checksum=RAW,
              raw_format_declared=dec, structure_format="mmcif", parser=P, selection_capability="full", warnings=())
    res = NS(resolved_selection_id="sel-1", policy_selection_id="sel-1", protein_input_id="protein-1", inspection_id=LIT, raw_checksum=RAW, structure_format="mmcif",
             parser=P, resolved_model=1, resolved_assembly=None, resolved_chains=(NS(label_asym_id="A", label_entity_id="E1", model_number=1),), resolved_component_dispositions=())
    recs = (R(kind="protein", id="protein-1", sha256="1"*64, size_bytes=1, schema_version=None), R(kind="inspection", id=LIT, sha256="2"*64, size_bytes=1, schema_version="1.0"),
            R(kind="selection", id="sel-1", sha256="3"*64, size_bytes=1, schema_version="1.0"), R(kind="resolution", id="sel-1", sha256="4"*64, size_bytes=1, schema_version="1.0"))
    try: return rm.build_source_context(protein_input=prot, inspection_report=insp, policy=pol, resolved_selection=res, raw_size_bytes=10, records=recs).raw_format
    except rm.MaterializationConfigurationError as e: return e.code
out["pure_format_check"] = {f"{a}/{d}": fmt(a, d) for a, d in (("mmcif", "mmcif"), ("cif", "mmcif"), ("mmcif", "cif"), ("pdb", "pdb"), ("mmcif", "pdb"), ("xyz", "xyz"))}
out["loaded_after"] = loaded()
print(json.dumps(out, indent=1))
