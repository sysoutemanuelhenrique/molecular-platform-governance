"""Read-only, pure/documentary probes for code commit 5be1e44.
Usage: python -B ARCHITECT_CP2_COMPLETION_PROBES.py /disposable/exact-code/src
Requires only existing base dependencies. No pytest, Gemmi, RDKit, CIF parsing,
installation, source modification or production persistence is performed.
"""
import ast
import hashlib
import importlib.abc
import json
import pathlib
import sys

src = pathlib.Path(sys.argv[1]).resolve()
for rel, digest in {
    "molecular/receptor_materialization.py": "3ec96abf14c05ce29e285d389e386a189b6b69f9244e307756003260ca8f9ba3",
    "molecular/receptor_parsing.py": "54abf400cb500dd18fc825d616c8faf22e637db7d1cdcec396329d06244471f7",
}.items():
    if hashlib.sha256((src / rel).read_bytes()).hexdigest() != digest:
        raise SystemExit("Unexpected code snapshot: " + rel)

attempts = []
class NativeBlocker(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.split(".")[0] in {"gemmi", "rdkit"}:
            attempts.append(fullname)
            raise ModuleNotFoundError("Native import blocked for documentary probe: " + fullname)

sys.meta_path.insert(0, NativeBlocker())
sys.path.insert(0, str(src))
from molecular import receptor_materialization as rm
from molecular import receptor_parsing as rp

probes = {"module_import_native_attempts": list(attempts)}
try:
    rp.parse_receptor_cif_dom021(b"data_x\n")
except rm.MaterializationConfigurationError as exc:
    probes["first_entry_native_attempt"] = {"attempts": list(attempts), "code": exc.code}

# Execute actual production helpers directly; these are not native CIF tests.
source = rm.RawCategoryTable(columns={"label_seq_id": ("1",), "type_symbol": ("C",)})
for field, value in [("pdbx_label_seq_id", "99"), ("type_symbol", "O")]:
    anisotrop = rm.RawCategoryTable(columns={field: (value,)})
    try:
        rm._validate_anisotrop_field_agreement("_atom_site_anisotrop", anisotrop, 0, source, 0, frozenset(anisotrop.columns))
    except rm.MaterializationExecutionError as exc:
        probes["anisotrop_" + field] = {"accepted": False, "code": exc.code}
    else:
        probes["anisotrop_" + field] = {"accepted": True, "expected": "INVALID_CIF for contradiction with referenced source atom"}

special = rm.RawCategoryTable(columns={"id": ("sp1",), "label_asym_id": ("NO_SUCH_ASYM",), "label_seq_id": ("999",)})
try:
    rm._guard_special_position_row("_pdbx_struct_special_symmetry", special, 0, frozenset(special.columns), {"A": {"A"}})
except rm.MaterializationExecutionError as exc:
    probes["special_nonexistent_label_context"] = {"accepted": False, "code": exc.code}
else:
    probes["special_nonexistent_label_context"] = {"accepted": True, "scope": "Actual guard returns immediately for any non-null label_asym_id"}

partial_u_complete_b = rm.RawCategoryTable(columns={"u[1][1]": ("0.1",), **{c: ("0.1",) for c in rm._ANISOTROP_B_COLUMNS}})
try:
    rm._validate_anisotrop_tensor_row("_atom_site_anisotrop", partial_u_complete_b, 0, frozenset(partial_u_complete_b.columns))
except rm.MaterializationExecutionError as exc:
    probes["anisotrop_partial_u_complete_b"] = {"accepted": False, "code": exc.code}
else:
    probes["anisotrop_partial_u_complete_b"] = {"accepted": True, "expected": "INVALID_CIF for a populated but incomplete U family even if B is complete"}

# Confirm the same gaps through the public catalogue function, not just helpers.
atom = rm.AtomObservation(ordinal=0, atom_id="a1", model=1, label_asym_id="A", entity_id="E1", entity_type="polymer", ccd="ALA", label_seq_id="1", auth_asym_id="A", auth_seq_id="1", label_atom_id="CA")
ad = rm.AtomDecision(ordinal=0, atom_id="a1", occurrence_key=rm.compute_occurrence_key(rm._build_occurrence_identity(atom)), retained=True, reason="selected-asym")
cols = {"id": ("a1",), "type_symbol": ("C",), "label_atom_id": ("CA",), "label_alt_id": (None,), "label_comp_id": ("ALA",), "label_asym_id": ("A",), "label_entity_id": ("E1",), "label_seq_id": ("1",), "auth_asym_id": ("A",), "auth_seq_id": ("1",), "pdbx_pdb_ins_code": (None,), "pdbx_pdb_model_num": ("1",), "cartn_x": ("1.0",), "cartn_y": ("1.0",), "cartn_z": ("1.0",), "occupancy": ("1.0",), "b_iso_or_equiv": ("10.0",)}
base = {"_atom_site": rm.RawCategoryTable(columns=cols), "_entity": rm.RawCategoryTable(columns={"id": ("E1",), "type": ("polymer",)}), "_struct_asym": rm.RawCategoryTable(columns={"id": ("A",), "entity_id": ("E1",)}), "_chem_comp": rm.RawCategoryTable(columns={"id": ("ALA",), "type": ("L-peptide linking",)}), "_entity_poly": rm.RawCategoryTable(columns={"entity_id": ("E1",), "type": ("polypeptide(L)",)}), "_entity_poly_seq": rm.RawCategoryTable(columns={"entity_id": ("E1",), "num": ("1",), "mon_id": ("ALA",)}), "_pdbx_poly_seq_scheme": rm.RawCategoryTable(columns={"asym_id": ("A",), "entity_id": ("E1",), "seq_id": ("1",), "mon_id": ("ALA",)})}
tensor = {c: ("0.1" if c in {"u[1][1]", "u[2][2]", "u[3][3]"} else "0",) for c in rm._ANISOTROP_U_COLUMNS}
for name, category, table in [
    ("special_nonexistent_label", "_pdbx_struct_special_symmetry", special),
    ("anisotrop_wrong_seq", "_atom_site_anisotrop", rm.RawCategoryTable(columns={"id": ("a1",), "pdbx_label_seq_id": ("99",), **tensor})),
]:
    try:
        ds = rm.compute_category_decisions(source_context_key=hashlib.sha256(b"documentary-context-not-scientific-input").hexdigest(), categories={**base, category: table}, retained_entity_ids=frozenset({"E1"}), retained_asym_ids=frozenset({"A"}), resolved_model=1, atoms_by_ordinal={0: atom}, atom_decisions_by_ordinal={0: ad}, connection_decisions=())
    except rm.MaterializationExecutionError as exc:
        probes["catalogue_" + name] = {"accepted": False, "code": exc.code}
    else:
        d = next(d for d in ds if d.category == category)
        probes["catalogue_" + name] = {"accepted": True, "action": d.action, "kept": d.kept_row_ordinals, "omitted": d.omitted_row_ordinals}

decision = rm.CategoryDecision(category="_atom_site", action="filter", kept_row_ordinals=(0,), preserved_tags=("id", "cartn_x"), source_rows_key="a" * 64)
expected = {"atom_site": {"id": ["a1"], "cartn_x": ["1.0"]}}
def dom(atom_id="a1", extra=False):
    cats = {"atom_site": rp.RawCifCategory(name="atom_site", row_count=1, columns={"id": (atom_id,), "cartn_x": ("1.0",)})}
    if extra:
        cats["unplanned"] = rp.RawCifCategory(name="unplanned", row_count=1, columns={"id": ("extra",)})
    return rp.ParsedCifDom021(category_names=tuple(cats), categories=cats, parser_name="gemmi", parser_version="0.7.5")
for name, parsed in [("changed_atom_id", dom("CHANGED")), ("extra_unplanned_category", dom(extra=True))]:
    try:
        rp._verify_output_reparse(category_decisions=(decision,), entry_id="tbmp_documentary", output_categories=expected, reparsed=parsed)
    except rm.MaterializationExecutionError as exc:
        probes["output_" + name] = {"accepted": False, "code": exc.code, "phase": exc.phase}
    else:
        probes["output_" + name] = {"accepted": True}

probes["pure_numeric"] = {v: rm._finite_numeric_token(v) for v in ["1.2e3(4)", "1.2(4)e3", "1_000", "NaN"]}
print(json.dumps({"code_commit": "5be1e443200cedddac0f97707963500a2edc6da6", "python": sys.version, "optimized": not __debug__, "pytest_executed": False, "native_execution": False, "probes": probes}, ensure_ascii=False, indent=2))
