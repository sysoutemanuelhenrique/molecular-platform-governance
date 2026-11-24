"""Reviewer conditional domain probes for Increment 021 CP1 (unmodified production source).
Requires an importable `gemmi` ONLY to get past the transitive import (ARCH-01); with the inert
sentinel no native code can run. Each probe records expected (contract) vs observed."""
import json, sys, unicodedata
from datetime import datetime, timezone
from pydantic import ValidationError
from molecular.receptor_inspection import ParserProvenance, ReceptorInspectionReport, ModelDescriptor, compute_inspection_id
from molecular.receptor_resolution import ResolvedReceptorSelection, ResolvedChainSelection, ResolvedComponentDisposition
import molecular.receptor_materialization as rm

P, S, RAW = "protein-1", "sel-1", "a" * 64
def iid(ver="0.7.5", fmt="mmcif", raw=RAW, prot=P):
    return compute_inspection_id(parser_name="gemmi", parser_version=ver, protein_input_id=prot, raw_checksum=raw, raw_format=fmt)
def report(ver="0.7.5", fmt="mmcif", **kw):
    d = dict(inspection_id=iid(ver, fmt), inspection_schema_version="1.0", inspection_profile_version="1.0", protein_input_id=P,
             raw_checksum=RAW, raw_format_declared=fmt, structure_format=fmt, parser=ParserProvenance(name="gemmi", version=ver),
             selection_capability="full", models=(ModelDescriptor(model_number=1),), assemblies=(), entities=(), chains=(),
             altloc_observations=(), occupancy_observations=(), missing_residues=(), missing_atoms=(), disulfide_bonds=(),
             covalent_connections=(), metal_coordinations=(), non_polymer_components=(), explicit_hydrogens_present=False,
             explicit_hydrogen_count=0, unavailable_categories=(), warnings=())
    d.update(kw); return ReceptorInspectionReport(**d)
def resolution(chains=(("A", "E1", 1),), disp=(), model=1, ver="0.7.5", fmt="mmcif", inspection_id=None):
    return ResolvedReceptorSelection(schema_version="1.0", resolved_selection_id=S, policy_selection_id=S, protein_input_id=P,
        inspection_id=inspection_id or iid(), raw_checksum=RAW, structure_format=fmt, parser=ParserProvenance(name="gemmi", version=ver),
        resolved_model=model, model_resolution_basis="only-model-present", resolved_assembly=None,
        resolved_chains=tuple(ResolvedChainSelection(label_asym_id=a, label_entity_id=e, model_number=m) for a, e, m in chains),
        resolved_component_dispositions=tuple(ResolvedComponentDisposition(label_asym_id=a, ccd_code=c, classification=k, disposition=v,
            disposition_source="component_dispositions") for a, c, k, v in disp), resolved_at=datetime.now(timezone.utc))
def records(inspection_id=None):
    R = rm.RecordSnapshot
    return (R(kind="protein", id=P, sha256="1"*64, size_bytes=1, schema_version=None), R(kind="inspection", id=inspection_id or iid(), sha256="2"*64, size_bytes=1, schema_version="1.0"),
            R(kind="selection", id=S, sha256="3"*64, size_bytes=1, schema_version="1.0"), R(kind="resolution", id=S, sha256="4"*64, size_bytes=1, schema_version="1.0"))
def ctx(rep=None, res=None, rec=None):
    rep = rep or report(); res = res or resolution()
    return rm.build_source_context(protein_input_id=P, inspection_report=rep, policy_selection_id=S, policy_inspection_id=rep.inspection_id,
        policy_raw_checksum_observed=RAW, resolved_selection=res, raw_size_bytes=10, records=rec or records())
def atom(o, aid, model=1, asym="A", ent="E1", et="polymer", ccd="ALA", seq="1", auth="A", aseq="1", ins=None):
    return rm.AtomObservation(ordinal=o, atom_id=aid, model=model, label_asym_id=asym, entity_id=ent, entity_type=et, ccd=ccd,
                              label_seq_id=seq, auth_asym_id=auth, auth_seq_id=aseq, insertion_token=ins)
def run(fn):
    try:
        r = fn(); return {"outcome": "accepted", "detail": r}
    except rm.MaterializationInputError as e: return {"outcome": "MaterializationInputError", "code": e.code}
    except rm.MaterializationConfigurationError as e: return {"outcome": "MaterializationConfigurationError", "code": e.code}
    except ValidationError as e: return {"outcome": "ValidationError", "msg": e.errors()[0]["msg"]}
    except Exception as e: return {"outcome": type(e).__name__, "msg": str(e)[:160]}
def plan(res, atoms, U="preserve"):
    p = rm.build_materialization_plan(source_context=ctx(res=res), resolved_selection=res, unaddressed_components=U, atoms=atoms)
    return {d.atom_id: [d.retained, d.reason] for d in p.atom_decisions}

two_model = (atom(0, "a1", 1, ccd="ALA"), atom(1, "a2", 2, ccd="GLY"))
probes = {}
# ARCH-02 family: keys whose CCD is absent from M must have no effect on M (§7)
probes["ARCH02_control_no_disposition"] = ("retain ALA in M=1", run(lambda: plan(resolution(), two_model)))
probes["ARCH02_remove_key_absent_from_M_on_selected_polymer"] = ("no effect: retain ALA in M=1",
    run(lambda: plan(resolution(disp=(("A", "GLY", "modified-polymer-residue", "remove"),)), two_model)))
probes["ARCH02_remove_key_present_in_M_on_selected_polymer"] = ("SELECTION_CONFLICT",
    run(lambda: plan(resolution(disp=(("A", "ALA", "modified-polymer-residue", "remove"),)), two_model)))
b_atoms = (atom(0, "a1"), atom(1, "b1", model=1, asym="B", ent="E2", ccd="ALA", auth="B"), atom(2, "b2", model=2, asym="B", ent="E2", ccd="MSE", auth="B"))
probes["ARCH02_keep_key_absent_from_M_on_unselected_polymer"] = ("no effect: B excluded by chain-complement",
    run(lambda: plan(resolution(disp=(("B", "MSE", "modified-polymer-residue", "keep"),)), b_atoms)))
probes["ARCH02_keep_key_present_in_M_on_unselected_polymer"] = ("SELECTION_CONFLICT",
    run(lambda: plan(resolution(disp=(("B", "ALA", "modified-polymer-residue", "keep"),)), b_atoms)))
probes["ARCH02_keep_key_on_asym_absent_from_M"] = ("no effect",
    run(lambda: plan(resolution(disp=(("Z", "HOH", "water", "keep"),)), (atom(0, "a1"),))))
# ARCH-03: catalogue filter categories with generate_tags (_cell/_symmetry entry_id)
for cat, keep in (("_cell", ("length_a",)), ("_symmetry", ("space_group_name_h-m",))):
    probes[f"ARCH03_filter_with_generated_entry_id_{cat}"] = ("accepted (catalogue: filter + generate_tags=['entry_id'])",
        run(lambda cat=cat, keep=keep: rm.CategoryDecision(category=cat, action="filter", kept_row_ordinals=(0,), preserved_tags=keep, generated_tags=("entry_id",)).action))
probes["ARCH03_generate_entry"] = ("accepted (_entry generate id)",
    run(lambda: rm.CategoryDecision(category="_entry", action="generate", generated_tags=("id",)).action))
# Independent: omitted category must keep no row (SCHEMAS §4)
probes["IND_omit_with_kept_rows"] = ("rejected: 'nenhuma tag/linha sobrevive'",
    run(lambda: rm.CategoryDecision(category="_struct_conf", action="omit", kept_row_ordinals=(0,)).kept_row_ordinals))
probes["IND_guard_then_omit_with_kept_rows"] = ("rejected", run(lambda: rm.CategoryDecision(category="_struct_ncs_oper", action="guard_then_omit",
    kept_row_ordinals=(0,), omitted_tags=("id",)).kept_row_ordinals))
# Independent: §5 requires inspection parser gemmi 0.7.5; resolution parser alone is checked
probes["IND_inspection_parser_0.7.4_resolution_0.7.5"] = ("MaterializationConfigurationError ENGINE_VERSION",
    run(lambda: ctx(rep=report(ver="0.7.4"), res=resolution(inspection_id=iid("0.7.4")), rec=records(iid("0.7.4"))).parser.model_dump()))
probes["IND_resolution_format_pdb_inspection_mmcif"] = ("rejected (format cross-check)",
    run(lambda: ctx(res=resolution(fmt="pdb")).raw_format))
# Independent: §6 NFC correspondence must be injective among source tokens involved
comp, decomp = unicodedata.normalize("NFC", "Á"), "Á"
probes["IND_nfc_outside_vs_polymer_distinct_tokens"] = ("refuse collision (never merge)",
    run(lambda: [e.author_id_coincidence for e in rm.build_materialization_plan(source_context=ctx(res=resolution(disp=(("W", "HOH", "water", "keep"),))),
        resolved_selection=resolution(disp=(("W", "HOH", "water", "keep"),)), unaddressed_components="preserve",
        atoms=(atom(0, "a1", auth=comp), atom(1, "w1", asym="W", ent="EW", et="water", ccd="HOH", seq=None, auth=decomp, aseq="1"))).plan.outside]))
# Independent: AtomDecision must cover each source ordinal exactly once; atom_site.id unique (§6, SCHEMAS §4)
probes["IND_duplicate_ordinal"] = ("rejected", run(lambda: plan(resolution(), (atom(0, "a1"), atom(0, "a2")))))
probes["IND_duplicate_atom_id"] = ("rejected", run(lambda: [(d.ordinal, d.atom_id, d.retained) for d in rm.build_materialization_plan(source_context=ctx(), resolved_selection=resolution(), unaddressed_components="preserve", atoms=(atom(0, "a1"), atom(1, "a1", seq="2", aseq="2"))).atom_decisions]))
probes["IND_duplicate_ordinal_decision_count"] = ("rejected", run(lambda: len(rm.build_materialization_plan(source_context=ctx(), resolved_selection=resolution(), unaddressed_components="preserve", atoms=(atom(0, "a1"), atom(0, "a2", seq="2", aseq="2"))).atom_decisions)))
# Independent: contradictory entity_id within one asym in M (§6 'vínculo inequívoco')
probes["IND_contradictory_entity_id_same_asym"] = ("rejected", run(lambda: plan(resolution(), (atom(0, "a1", ent="E1"), atom(1, "a2", ent="E9", seq="2", aseq="2")))))
# Independent: selected asym absent from M
probes["IND_selected_asym_absent_from_M"] = ("rejected or flagged", run(lambda: plan(resolution(chains=(("A", "E1", 1), ("Q", "E1", 1))), (atom(0, "a1"),))))
# Independent: catalogue divergence accepted by PlanBinding (T021-005 'catalogue divergente')
def _plan_cat():
    p = rm.build_materialization_plan(source_context=ctx(), resolved_selection=resolution(), unaddressed_components="preserve", atoms=(atom(0, "a1"),)).plan
    return rm.PlanBinding(**{**{k: getattr(p, k) for k in rm.PlanBinding.model_fields}, "catalogue_sha256": "f" * 64}).catalogue_sha256[:8]
probes["IND_planbinding_divergent_catalogue"] = ("rejected with configuration error", run(_plan_cat))
# Independent: existing policy integrity/equivalence (§13)
def _existing():
    mp = rm.build_materialization_plan(source_context=ctx(), resolved_selection=resolution(), unaddressed_components="preserve", atoms=(atom(0, "a1"),))
    first = rm.build_policy_record(materialization_plan=mp, acknowledge_plan_key=mp.plan_key, acknowledge_exclusions_key=None,
                                   acknowledge_outside_key=None, declared_by="scientist", declared_at="2026-01-01T00:00:00.000000Z")
    tampered = rm.PolicyRecord(**{**{k: getattr(first, k) for k in rm.PolicyRecord.model_fields}, "unaddressed_components": "require-disposition"})
    second = rm.build_policy_record(materialization_plan=mp, acknowledge_plan_key=mp.plan_key, acknowledge_exclusions_key=None,
                                    acknowledge_outside_key=None, declared_by="scientist", declared_at="2099-01-01T00:00:00.000000Z", existing=tampered)
    selfcheck = rm.PolicyRecord(**{**{k: getattr(first, k) for k in rm.PolicyRecord.model_fields}, "policy_id": "e" * 64}).policy_id[:8]
    return {"tampered_existing_accepted": True, "returned_declared_at": second.declared_at,
            "returned_unaddressed": second.unaddressed_components, "policy_id_not_selfchecked_value": selfcheck}
probes["IND_existing_policy_tampered_same_policy_id"] = ("integrity/equivalence verified; mismatch refused", run(_existing))
# Independent: lone surrogate in NativeId reaches hashing
probes["IND_lone_surrogate_native_id"] = ("typed rejection at DTO", run(lambda: rm.compute_occurrence_key(rm.OccurrenceIdentity(model=1, label_asym_id="A\ud800", entity_id="E", ccd="ALA", label_seq_id="1"))))
# Independent: structure_format != mmcif error code
probes["IND_format_pdb_code"] = ("configuration error (not host platform)", run(lambda: ctx(rep=report(fmt="pdb"), res=resolution(fmt="pdb", inspection_id=iid(fmt="pdb")), rec=records(iid(fmt="pdb")))))
print(json.dumps({"python": sys.version.split()[0], "gemmi_module": getattr(sys.modules.get("gemmi"), "__doc__", "")[:40],
                  "probes": {k: {"expected": v[0], "observed": v[1]} for k, v in probes.items()}}, indent=1, ensure_ascii=True))
