"""Reviewer probes for the CP1 residual corrections (unmodified production source at bbd491e).
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
MM = (InspectionWarning(code="declared-format-mismatch", detail="declared pdb vs detected mmcif"),)
def fmt(acq, dec, warn=()):
    return ctx(prot=protein(fmt=acq), rep=report(declared=dec, warnings=warn)).raw_format
# MAJOR-A residual
for acq, dec, exp in [("pdb", "pdb", "INVALID_RECORD"), ("mmcif", "pdb", "INVALID_RECORD"), ("pdb", "mmcif", "INVALID_RECORD"),
                      ("xyz", "xyz", "INVALID_RECORD"), ("xyz", "mmcif", "INVALID_RECORD"), ("mmcif", "xyz", "INVALID_RECORD"),
                      ("ent", "pdb", "INVALID_RECORD"), ("cif", "mmcif", "accepted mmcif"), ("mmcif", "cif", "accepted mmcif"),
                      ("cif", "cif", "accepted mmcif"), ("mmcif", "mmcif", "accepted mmcif"), (" MMCIF ", "Cif\t", "accepted mmcif (020 strip/lower)"),
                      ("mm cif", "mmcif", "INVALID_RECORD"), ("   ", "mmcif", "INVALID_RECORD")]:
    w = MM if (acq, dec) == ("pdb", "pdb") else ()
    pr[f"A_fmt_acq={acq!r}_dec={dec!r}" + ("_with_mismatch_warning" if w else "")] = (exp, run(lambda a=acq, d=dec, w=w: fmt(a, d, w)))
def _unchanged():
    p = protein(fmt=" MMCIF "); r = report(declared="Cif\t"); ctx(prot=p, rep=r)
    return {"acq_after": p.acquisition.raw_artifact.format, "declared_after": r.raw_format_declared}
pr["A_source_strings_unchanged"] = ("' MMCIF ' and 'Cif\\t' unchanged", run(_unchanged))
pr["A_order_engine_still_first"] = ("ENGINE_VERSION", run(lambda: ctx(prot=protein(fmt="pdb"), rep=report(ver="0.7.4", declared="pdb")).raw_format))
pr["A_order_identity_vs_format"] = ("report which wins (order note)", run(lambda: ctx(prot=protein(fmt="pdb", pid="protein-2"), rep=report(declared="pdb")).raw_format))
pr["A_order_checksum_vs_format"] = ("report which wins (order note)", run(lambda: ctx(prot=protein(fmt="pdb", checksum="b"*64), rep=report(declared="pdb")).raw_format))
pr["A_order_format_vs_capability"] = ("INVALID_RECORD before INCOMPLETE_INSPECTION", run(lambda: ctx(prot=protein(fmt="pdb"), rep=report(declared="pdb", selection_capability="inspection-only")).raw_format))
# MINOR-3 residual
CD = rm.CategoryDecision; K = "0" * 64
def cd(**kw): return run(lambda: CD(**kw).category)
pr["C_kept_dup"] = ("refused", cd(category="_atom_site", action="filter", kept_row_ordinals=(0, 0), source_rows_key=K))
pr["C_omitted_dup"] = ("refused", cd(category="_struct_conf", action="omit", omitted_row_ordinals=(0, 0), source_rows_key=K))
pr["C_kept_dup_nonadjacent"] = ("refused", cd(category="_atom_site", action="filter", kept_row_ordinals=(0, 1, 0), source_rows_key=K))
pr["C_overlap_kept_omitted"] = ("refused", cd(category="_atom_site", action="filter", kept_row_ordinals=(0,), omitted_row_ordinals=(0,), source_rows_key=K))
pr["C_negative"] = ("refused", cd(category="_atom_site", action="filter", kept_row_ordinals=(-1,), source_rows_key=K))
pr["C_bool_ordinal"] = ("refused (strict)", cd(category="_atom_site", action="filter", kept_row_ordinals=(True,), source_rows_key=K))
pr["C_unique_ok"] = ("accepted", cd(category="_atom_site", action="filter", kept_row_ordinals=(0, 2), omitted_row_ordinals=(1,), source_rows_key=K))
pr["C_empty_omit"] = ("accepted", cd(category="_struct_conf", action="omit", source_rows_key=K))
pr["C_cell_filter_generate"] = ("accepted", cd(category="_cell", action="filter", kept_row_ordinals=(0,), preserved_tags=("length_a",), generated_tags=("entry_id",), source_rows_key=K))
pr["C_generate_null_source"] = ("accepted", cd(category="_entry", action="generate", generated_tags=("id",)))
for name, exp in [("_em_example\n", "refused"), ("_em_", "refused"), ("_pdbx_validate_", "refused"), ("_pdbx_nmr_", "refused"),
                  ("_pdbx_nmr_ x", "refused"), ("_em_entity.id", "refused"), ("_EM_x", "refused"), ("_em_X", "refused"),
                  ("_em_x\x00", "refused"), ("_em_x\t", "refused"), ("\n_em_x", "refused"), ("_em_é", "refused"),
                  ("_em_3d_fitting", "accepted"), ("_pdbx_validate_close_contact", "accepted"), ("_pdbx_nmr_spectrometer", "accepted"), ("_em_x_", "accepted")]:
    pr[f"C_family_{name!r}"] = (exp, cd(category=name, action="omit", source_rows_key=K))
pr["C_family_filter_still_refused"] = ("refused", cd(category="_em_x", action="filter", source_rows_key=K))
pr["C_noncatalogue_still_refused"] = ("refused", cd(category="_made_up", action="omit", source_rows_key=K))
cat = rm._CATALOGUE_CATEGORY_NAMES
def _all94():
    ok = 0
    for c in sorted(cat):
        CD(category=c, action="omit", source_rows_key=K); ok += 1
    return {"count": len(cat), "accepted_as_omit": ok, "catalogue_names_matching_family_regex": sorted(c for c in cat if rm._CATALOGUE_OMISSION_FAMILY_PATTERN.fullmatch(c))}
pr["C_all_94_catalogue_names_preserved"] = ("94 accepted", run(_all94))
def _catalogue_file_names():
    import json as _j, pathlib
    d = _j.loads(pathlib.Path(sys.argv[1]).read_bytes()); names = set(d["categories"])
    return {"annex_categories": len(names), "code_minus_annex": sorted(cat - names), "annex_minus_code": sorted(names - cat),
            "annex_allowed_omission_prefixes": d["allowed_omission_prefixes"]}
pr["C_catalogue_set_vs_annex"] = ("code set == annex set", run(_catalogue_file_names))
print(json.dumps({"python": sys.version.split()[0], "gemmi_module_doc": (getattr(sys.modules.get("gemmi"), "__doc__", "") or "")[:30],
                  "probes": {k: {"expected": v[0], "observed": v[1]} for k, v in pr.items()}}, indent=1, ensure_ascii=True))
