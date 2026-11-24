"""Reviewer conditional probes for the CP1 corrections (unmodified production source at 42b4804).
Uses the INERT gemmi sentinel only so the real 020 DTO classes can be imported; no native code can run.
Each probe records the contract expectation and the observed outcome."""
import json, sys, unicodedata
from datetime import datetime, timezone
from pydantic import ValidationError
from molecular.inputs import AcquisitionRecord, ProteinInput, RawArtifact
from molecular.receptor_selection import ReceptorSelectionPolicy
from molecular.receptor_inspection import ParserProvenance, ReceptorInspectionReport, ModelDescriptor, InspectionWarning, compute_inspection_id
from molecular.receptor_resolution import ResolvedReceptorSelection, ResolvedChainSelection, ResolvedComponentDisposition
import molecular.receptor_materialization as rm

P, S, RAW = "protein-1", "sel-1", "a" * 64
def iid(ver="0.7.5", fmt="mmcif"): return compute_inspection_id(parser_name="gemmi", parser_version=ver, protein_input_id=P, raw_checksum=RAW, raw_format=fmt)
def report(ver="0.7.5", fmt="mmcif", declared="mmcif", warnings=(), **kw):
    d = dict(inspection_id=iid(ver, fmt), inspection_schema_version="1.0", inspection_profile_version="1.0", protein_input_id=P, raw_checksum=RAW,
             raw_format_declared=declared, structure_format=fmt, parser=ParserProvenance(name="gemmi", version=ver), selection_capability="full",
             models=(ModelDescriptor(model_number=1),), assemblies=(), entities=(), chains=(), altloc_observations=(), occupancy_observations=(),
             missing_residues=(), missing_atoms=(), disulfide_bonds=(), covalent_connections=(), metal_coordinations=(), non_polymer_components=(),
             explicit_hydrogens_present=False, explicit_hydrogen_count=0, unavailable_categories=(), warnings=warnings)
    d.update(kw); return ReceptorInspectionReport(**d)
def resolution(chains=(("A", "E1", 1),), disp=(), ver="0.7.5", fmt="mmcif", inspection_id=None):
    return ResolvedReceptorSelection(schema_version="1.0", resolved_selection_id=S, policy_selection_id=S, protein_input_id=P,
        inspection_id=inspection_id or iid(), raw_checksum=RAW, structure_format=fmt, parser=ParserProvenance(name="gemmi", version=ver), resolved_model=1,
        model_resolution_basis="only-model-present", resolved_assembly=None,
        resolved_chains=tuple(ResolvedChainSelection(label_asym_id=a, label_entity_id=e, model_number=m) for a, e, m in chains),
        resolved_component_dispositions=tuple(ResolvedComponentDisposition(label_asym_id=a, ccd_code=c, classification=k, disposition=v,
            disposition_source="component_dispositions") for a, c, k, v in disp), resolved_at=datetime.now(timezone.utc))
def protein(fmt="mmcif", checksum=RAW, pid=P):
    return ProteinInput(id=pid, name="P", acquisition=AcquisitionRecord(method="uploaded", acquired_at=datetime.now(timezone.utc),
        raw_artifact=RawArtifact(path="inputs/proteins/protein-1/raw.cif", format=fmt, checksum=checksum)))
def policy(pid=P, inspection_id=None):
    return ReceptorSelectionPolicy(schema_version="1.0", selection_id=S, protein_input_id=pid, inspection_id=inspection_id or iid(),
        raw_checksum_observed=RAW, declared_by="s", declared_at=datetime.now(timezone.utc))
def records(inspection_id=None):
    R = rm.RecordSnapshot
    return (R(kind="protein", id=P, sha256="1"*64, size_bytes=1, schema_version=None), R(kind="inspection", id=inspection_id or iid(), sha256="2"*64, size_bytes=1, schema_version="1.0"),
            R(kind="selection", id=S, sha256="3"*64, size_bytes=1, schema_version="1.0"), R(kind="resolution", id=S, sha256="4"*64, size_bytes=1, schema_version="1.0"))
def ctx(prot=None, rep=None, pol=None, res=None, rec=None):
    rep = rep or report(); return rm.build_source_context(protein_input=prot or protein(), inspection_report=rep, policy=pol or policy(inspection_id=rep.inspection_id),
        resolved_selection=res or resolution(inspection_id=rep.inspection_id), raw_size_bytes=10, records=rec or records(rep.inspection_id))
def atom(o, aid, model=1, asym="A", ent="E1", et="polymer", ccd="ALA", seq="1", auth="A", aseq="1"):
    return rm.AtomObservation(ordinal=o, atom_id=aid, model=model, label_asym_id=asym, entity_id=ent, entity_type=et, ccd=ccd, label_seq_id=seq, auth_asym_id=auth, auth_seq_id=aseq)
def run(fn):
    try: return {"outcome": "accepted", "detail": fn()}
    except rm.MaterializationInputError as e: return {"outcome": "MaterializationInputError", "code": e.code}
    except rm.MaterializationConfigurationError as e: return {"outcome": "MaterializationConfigurationError", "code": e.code}
    except ValidationError as e: return {"outcome": "ValidationError", "msg": e.errors()[0]["msg"][:110]}
    except Exception as e: return {"outcome": type(e).__name__, "msg": str(e)[:140]}
def mplan(res, atoms, U="preserve"):
    return rm.build_materialization_plan(source_context=ctx(res=res), resolved_selection=res, unaddressed_components=U, atoms=atoms)
def plan(res, atoms, U="preserve"): return {d.atom_id: [d.retained, d.reason] for d in mplan(res, atoms, U).atom_decisions}
pr = {}
pr["LEGACY_old_helper_equals_reviewer_literal_1c217d99"] = ("true", run(lambda: iid() == "1c217d99e7b2b09d9c31a0c8f9daf056c48aa916bdf957cae83df449ad68e80c"))
# ARCH-02
two = (atom(0, "a1", 1, ccd="ALA"), atom(1, "a2", 2, ccd="GLY"))
pr["ARCH02_remove_absent_in_M_selected"] = ("ALA retained", run(lambda: plan(resolution(disp=(("A", "GLY", "modified-polymer-residue", "remove"),)), two)))
pr["ARCH02_remove_present_in_M_selected"] = ("SELECTION_CONFLICT", run(lambda: plan(resolution(disp=(("A", "ALA", "modified-polymer-residue", "remove"),)), two)))
bat = (atom(0, "a1"), atom(1, "b1", asym="B", ent="E2", auth="B"), atom(2, "b2", model=2, asym="B", ent="E2", ccd="MSE", auth="B"))
pr["ARCH02_keep_absent_in_M_unselected"] = ("B excluded chain-complement", run(lambda: plan(resolution(disp=(("B", "MSE", "modified-polymer-residue", "keep"),)), bat)))
pr["ARCH02_keep_present_in_M_unselected"] = ("SELECTION_CONFLICT", run(lambda: plan(resolution(disp=(("B", "ALA", "modified-polymer-residue", "keep"),)), bat)))
pr["ARCH02_model_filter_preserved"] = ("a2 model-filter", run(lambda: plan(resolution(), two)["a2"]))
# MAJOR-A
pr["A_inspection_parser_074"] = ("ENGINE_VERSION", run(lambda: ctx(rep=report(ver="0.7.4")).parser.version))
pr["A_resolution_parser_074"] = ("ENGINE_VERSION", run(lambda: ctx(res=resolution(ver="0.7.4")).parser.version))
pr["A_resolution_format_pdb"] = ("INVALID_RECORD", run(lambda: ctx(res=resolution(fmt="pdb")).raw_format))
pr["A_inspection_format_pdb_coherent_everywhere"] = ("INVALID_RECORD (MINOR-5)", run(lambda: ctx(rep=report(fmt="pdb", declared="pdb"), res=resolution(fmt="pdb", inspection_id=iid(fmt="pdb")), prot=protein(fmt="pdb")).raw_format))
pr["A_acquisition_checksum_diverges"] = ("CHECKSUM_MISMATCH", run(lambda: ctx(prot=protein(checksum="b"*64)).raw_sha256[:6]))
pr["A_policy_protein_id_diverges"] = ("IDENTITY_MISMATCH", run(lambda: ctx(pol=policy(pid="protein-2")).protein_input_id))
pr["A_protein_input_id_diverges"] = ("IDENTITY_MISMATCH", run(lambda: ctx(prot=protein(pid="protein-2")).protein_input_id))
pr["A_order_engine_before_identity"] = ("ENGINE_VERSION first", run(lambda: ctx(rep=report(ver="0.7.4"), pol=policy(pid="protein-2")).protein_input_id))
pr["A_acq_cif_alias_declared_cif"] = ("accepted (020 alias cif->mmcif)", run(lambda: ctx(prot=protein(fmt="cif"), rep=report(declared="cif")).raw_format))
pr["A_acq_pdb_declared_pdb_detected_mmcif"] = ("contract decision: declared/observed format contradiction", run(lambda: ctx(prot=protein(fmt="pdb"),
    rep=report(declared="pdb", warnings=(InspectionWarning(code="declared-format-mismatch", detail="declared pdb vs detected mmcif"),))).raw_format))
pr["A_acq_mmcif_vs_inspection_declared_pdb"] = ("refuse: records disagree on the declared format", run(lambda: ctx(prot=protein(fmt="mmcif"), rep=report(declared="pdb")).raw_format))
pr["A_acq_xyz_vs_declared_xyz"] = ("refuse or explicit rule", run(lambda: ctx(prot=protein(fmt="xyz"), rep=report(declared="xyz")).raw_format))
pr["A_duck_typed_inspection_object"] = ("note: no runtime type check", run(lambda: type(rm.build_source_context.__annotations__["inspection_report"]).__name__))
# MAJOR-B
def _mp(): return mplan(resolution(), (atom(0, "a1"),))
def _first(mp): return rm.build_policy_record(materialization_plan=mp, acknowledge_plan_key=mp.plan_key, acknowledge_exclusions_key=None, acknowledge_outside_key=None, declared_by="s", declared_at="2026-01-01T00:00:00.000000Z")
def _repeat():
    mp = _mp(); f = _first(mp)
    s2 = rm.build_policy_record(materialization_plan=mp, acknowledge_plan_key=mp.plan_key, acknowledge_exclusions_key=None, acknowledge_outside_key=None, declared_by="s", declared_at="2099-01-01T00:00:00.000000Z", existing=f)
    return {"same_object": s2 is f, "declared_at": s2.declared_at}
pr["B_legit_repeat"] = ("existing returned, original timestamp", run(_repeat))
def _tamper(field, value):
    mp = _mp(); f = _first(mp); t = rm.PolicyRecord(**{**{k: getattr(f, k) for k in rm.PolicyRecord.model_fields}, field: value})
    return rm.build_policy_record(materialization_plan=mp, acknowledge_plan_key=mp.plan_key, acknowledge_exclusions_key=None, acknowledge_outside_key=None, declared_by="s", declared_at="2099-01-01T00:00:00.000000Z", existing=t).declared_at
pr["B_tamper_unaddressed"] = ("refused", run(lambda: _tamper("unaddressed_components", "require-disposition")))
pr["B_tamper_source_context_key"] = ("refused", run(lambda: _tamper("source_context_key", "9"*64)))
pr["B_tamper_outside_count"] = ("refused", run(lambda: _tamper("outside_occurrence_count", 3)))
pr["B_invalid_policy_id_in_dto"] = ("ValidationError", run(lambda: rm.PolicyRecord(**{**{k: getattr(_first(_mp()), k) for k in rm.PolicyRecord.model_fields}, "policy_id": "e"*64}).policy_id))
# ARCH-03 / MINOR-3
CD = rm.CategoryDecision; K = "0" * 64
pr["C_cell_filter_generate"] = ("accepted", run(lambda: CD(category="_cell", action="filter", kept_row_ordinals=(0,), preserved_tags=("length_a",), omitted_tags=("details",), generated_tags=("entry_id",), source_rows_key=K).action))
pr["C_symmetry_filter_generate"] = ("accepted", run(lambda: CD(category="_symmetry", action="filter", kept_row_ordinals=(0,), preserved_tags=("space_group_name_h-m",), generated_tags=("entry_id",), source_rows_key=K).action))
pr["C_generate_entry_no_source"] = ("accepted with null key", run(lambda: CD(category="_entry", action="generate", generated_tags=("id",)).source_rows_key))
pr["C_omit_empty_source"] = ("accepted", run(lambda: CD(category="_struct_conf", action="omit", source_rows_key=K).action))
pr["C_omit_kept_row"] = ("refused", run(lambda: CD(category="_struct_conf", action="omit", kept_row_ordinals=(0,), source_rows_key=K).action))
pr["C_duplicate_kept_ordinals"] = ("refused (unique)", run(lambda: CD(category="_atom_site", action="filter", kept_row_ordinals=(0, 0), source_rows_key=K).kept_row_ordinals))
pr["C_duplicate_omitted_ordinals"] = ("refused (unique)", run(lambda: CD(category="_struct_conf", action="omit", omitted_row_ordinals=(0, 0), source_rows_key=K).omitted_row_ordinals))
pr["C_overlap_kept_omitted"] = ("refused", run(lambda: CD(category="_atom_site", action="filter", kept_row_ordinals=(0,), omitted_row_ordinals=(0,), source_rows_key=K).action))
pr["C_negative_ordinal"] = ("refused", run(lambda: CD(category="_atom_site", action="filter", kept_row_ordinals=(-1,), source_rows_key=K).action))
pr["C_family_ok"] = ("accepted", run(lambda: CD(category="_em_3d_fitting", action="omit", source_rows_key=K).action))
pr["C_family_with_LF"] = ("refused (non-canonical name)", run(lambda: CD(category="_em_example\n", action="omit", source_rows_key=K).category))
pr["C_family_bare_prefix"] = ("refused (no category after prefix)", run(lambda: CD(category="_em_", action="omit", source_rows_key=K).category))
pr["C_family_with_space"] = ("refused", run(lambda: CD(category="_pdbx_nmr_ x", action="omit", source_rows_key=K).category))
pr["C_family_with_dot_tag"] = ("refused (category, not item)", run(lambda: CD(category="_em_entity.id", action="omit", source_rows_key=K).category))
pr["C_family_filter"] = ("refused", run(lambda: CD(category="_em_x", action="filter", source_rows_key=K).action))
pr["C_noncatalogue"] = ("refused", run(lambda: CD(category="_made_up", action="omit", source_rows_key=K).action))
pr["C_uppercase_catalogue"] = ("refused", run(lambda: CD(category="_ATOM_SITE", action="filter", source_rows_key=K).action))
pr["C_filter_no_source"] = ("refused", run(lambda: CD(category="_atom_site", action="filter").action))
pr["C_generate_with_rows_no_source"] = ("refused", run(lambda: CD(category="_entry", action="generate", kept_row_ordinals=(0,), generated_tags=("id",)).action))
# MINOR-1
pr["M1_dup_ordinal"] = ("INVALID_ID", run(lambda: plan(resolution(), (atom(0, "a1"), atom(0, "a2", seq="2", aseq="2")))))
pr["M1_dup_atom_id_across_models"] = ("INVALID_ID", run(lambda: plan(resolution(), (atom(0, "a1"), atom(1, "a1", model=2)))))
pr["M1_entity_contradiction"] = ("INVALID_ID", run(lambda: plan(resolution(), (atom(0, "a1"), atom(1, "a2", ent="E9", seq="2", aseq="2")))))
pr["M1_S_absent_in_M"] = ("INVALID_ID", run(lambda: plan(resolution(chains=(("A", "E1", 1), ("Q", "E1", 1))), (atom(0, "a1"),))))
pr["M1_S_present_only_other_model"] = ("refused", run(lambda: plan(resolution(chains=(("A", "E1", 1), ("Q", "E1", 1))), (atom(0, "a1"), atom(1, "q1", model=2, asym="Q", auth="Q")))))
pr["M1_valid_multimodel_ordinals_kept"] = ("accepted, source ordinals", run(lambda: [d.ordinal for d in mplan(resolution(), (atom(7, "a1"), atom(3, "a9", model=2))).atom_decisions]))
pr["M1_resolution_entity_vs_atom_entity"] = ("note: chain label_entity_id vs atoms", run(lambda: plan(resolution(chains=(("A", "E7", 1),)), (atom(0, "a1", ent="E1"),))))
# MINOR-2
W = ("W", "HOH", "water", "keep"); comp, decomp = unicodedata.normalize("NFC", "Á"), "Á"
pr["N2_water_nfd_vs_polymer_nfc"] = ("refused", run(lambda: plan(resolution(disp=(W,)), (atom(0, "a1", auth=comp), atom(1, "w1", asym="W", ent="EW", et="water", ccd="HOH", seq=None, auth=decomp)))))
pr["N2_ligand_nfd_vs_polymer_nfc"] = ("refused", run(lambda: plan(resolution(disp=(("L", "HEM", "other-non-polymer", "keep"),)), (atom(0, "a1", auth=comp), atom(1, "l1", asym="L", ent="EL", et="non-polymer", ccd="HEM", seq=None, auth=decomp)))))
pr["N2_identical_token_multiple"] = ("multiple", run(lambda: [e.author_id_coincidence for e in mplan(resolution(chains=(("A", "E1", 1), ("A2", "E1", 1)), disp=(W,)),
    (atom(0, "a1", auth="M"), atom(1, "a2", asym="A2", auth="M"), atom(2, "w1", asym="W", ent="EW", et="water", ccd="HOH", seq=None, auth="M"))).plan.outside]))
pr["N2_identical_token_retained_excluded"] = ("retained-polymer / excluded-polymer", run(lambda: [e.author_id_coincidence for e in mplan(resolution(disp=(W, ("V", "HOH", "water", "keep"))),
    (atom(0, "a1", auth="A"), atom(1, "b1", asym="B", ent="E2", auth="B"), atom(2, "w1", asym="W", ent="EW", et="water", ccd="HOH", seq=None, auth="A"),
     atom(3, "v1", asym="V", ent="EW", et="water", ccd="HOH", seq=None, auth="B", aseq="2"))).plan.outside]))
pr["N2_selected_ligand_nfd_vs_polymer_nfc_no_O"] = ("scope question: token not in O", run(lambda: plan(resolution(chains=(("A", "E1", 1), ("L", "EL", 1))),
    (atom(0, "a1", auth=comp), atom(1, "l1", asym="L", ent="EL", et="non-polymer", ccd="HEM", seq=None, auth=decomp)))))
# MINOR-4
pr["M4_catalogue_planbinding"] = ("refused", run(lambda: rm.PlanBinding(**{**{k: getattr(_mp().plan, k) for k in rm.PlanBinding.model_fields}, "catalogue_sha256": "f"*64}).catalogue_sha256))
pr["M4_catalogue_policy"] = ("refused", run(lambda: rm.PolicyRecord(**{**{k: getattr(_first(_mp()), k) for k in rm.PolicyRecord.model_fields}, "catalogue_sha256": "f"*64}).catalogue_sha256))
pr["M4_engine_literal"] = ("refused", run(lambda: rm.Engine(name="gemmi", version="0.7.6").version))
def _bind():
    p = _mp().plan; d = p.model_dump(mode="json"); base = rm.compute_materialization_hash(d)
    res = {}
    for f, v in (("profile", "9.9"), ("algorithm", "9.9"), ("catalogue_sha256", "f"*64), ("engine", {"name": "gemmi", "version": "0.0.0"}), ("atom_decisions_key", "f"*64)):
        res[f] = rm.compute_materialization_hash({**d, f: v}) != base
    res["plan_key_is_H_of_dump"] = rm.compute_materialization_hash(d) == _mp().plan_key
    return res
pr["M4_plan_key_binds_fields_documentary"] = ("all true (documentary dict variations)", run(_bind))
print(json.dumps({"python": sys.version.split()[0], "gemmi_module_doc": (getattr(sys.modules.get("gemmi"), "__doc__", "") or "")[:30],
                  "probes": {k: {"expected": v[0], "observed": v[1]} for k, v in pr.items()}}, indent=1, ensure_ascii=True))
