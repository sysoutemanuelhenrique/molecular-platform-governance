"""Reviewer's own recomputation of the 13 MINOR-7 envelopes from the frozen spec section 13 and SCHEMAS
(envelope table lines 23/27/45/47/53-60, spec lines 227/229/231). Stdlib only: no production import,
no architect generator import. The only inputs taken from the test file are documentary input values."""
import hashlib, json, sys
def C(d): return json.dumps(d, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")
def H(d): return hashlib.sha256(C(d)).hexdigest()
def E(kind, **kw): d = {"kind": kind, "version": "1.0"}; d.update(kw); return d
mine = {}
mine["canonical_json"] = H({"version": "1.0", "kind": "k", "s": "éÅ", "l": [2, 1], "n": None, "b": True})
leg = {"inspection_schema_version": "1.0", "inspection_profile_version": "1.0", "parser_name": "gemmi", "parser_version": "0.7.5",
       "protein_input_id": "protein-1", "raw_checksum": "a" * 64, "raw_format": "mmcif"}
mine["legacy_inspection_id"] = H(leg)
raw = b"documentary CP1 hash fixture only; no CIF geometry or parsing"
raw_sha = hashlib.sha256(raw).hexdigest(); insp = H({**leg, "raw_checksum": raw_sha})
recs = []
for kind, rid in (("protein", "protein-1"), ("inspection", insp), ("selection", "sel-1"), ("resolution", "sel-1")):
    b = C({"fixture": "cp1-documentary-v1", "kind": kind, "id": rid})
    recs.append({"kind": kind, "id": rid, "sha256": hashlib.sha256(b).hexdigest(), "size_bytes": len(b), "schema_version": None if kind == "protein" else "1.0"})
src = {"protein_input_id": "protein-1", "selection_id": "sel-1", "inspection_id": insp, "model": 1, "records": recs, "raw_sha256": raw_sha,
       "raw_size_bytes": len(raw), "raw_format": "mmcif", "inspection_schema": "1.0", "inspection_profile": "1.0", "parser": {"name": "gemmi", "version": "0.7.5"}}
sck = mine["source_context_key"] = H(E("receptor-materialization-sources", sources=src))
def occ(a, e, c, s, au): return {"model": 1, "label_asym_id": a, "entity_id": e, "ccd": c, "label_seq_id": s, "auth_asym_id": a, "auth_seq_id": au, "insertion_token": None}
oa, ob, ow = occ("A", "E1", "ALA", "1", "1"), occ("B", "E2", "ALA", "1", "1"), occ("W", "EW", "HOH", None, "17")
kw = mine["occurrence_key"] = H(E("receptor-materialization-occurrence", identity=ow))
ka, kb = H(E("receptor-materialization-occurrence", identity=oa)), H(E("receptor-materialization-occurrence", identity=ob))
ib = mine["atom_ids_key"] = H(E("receptor-materialization-atom-ids", atoms=[{"ordinal": 1, "id": "b1"}]))
iw = H(E("receptor-materialization-atom-ids", atoms=[{"ordinal": 2, "id": "w1"}]))
X = [{"model": 1, "label_asym_id": "B", "entity_id": "E2", "atom_count": 1, "atom_ids_key": ib}]
O = [{"identity": ow, "occurrence_key": kw, "decision_source": "unaddressed-preserve", "atom_count": 1, "atom_ids_key": iw, "author_id_coincidence": "none"}]
xk = mine["exclusions_key"] = H(E("receptor-materialization-exclusions", source_context_key=sck, model=1, entries=X))
ok = mine["outside_key"] = H(E("receptor-materialization-outside", source_context_key=sck, model=1, entries=O))
AD = [{"ordinal": 0, "atom_id": "a1", "occurrence_key": ka, "retained": True, "reason": "selected-asym"},
      {"ordinal": 1, "atom_id": "b1", "occurrence_key": kb, "retained": False, "reason": "chain-complement"},
      {"ordinal": 2, "atom_id": "w1", "occurrence_key": kw, "retained": True, "reason": "unaddressed-preserve"}]
ak = mine["atom_decisions_key"] = H(E("receptor-materialization-atom-decisions", source_context_key=sck, decisions=AD))
ck = mine["connection_decisions_key"] = H(E("receptor-materialization-connection-decisions", source_context_key=sck, decisions=[]))
rows = [H(E("receptor-materialization-source-row", source_context_key=sck, category="_atom_site", ordinal=i, tokens=[{"tag": "id", "token": v}])) for i, v in enumerate(("a1", "b1", "w1"))]
rk = H(E("receptor-materialization-source-category", source_context_key=sck, category="_atom_site", rows=rows))
CDs = [{"category": "_atom_site", "action": "filter", "kept_row_ordinals": [0, 2], "omitted_row_ordinals": [1], "preserved_tags": ["id"], "omitted_tags": [], "generated_tags": [], "source_rows_key": rk}]
gk = mine["category_decisions_key"] = H(E("receptor-materialization-category-decisions", source_context_key=sck, decisions=CDs))
CAT = "8561039fd15137811b60316336dff04539df3732710dca6ec4009f23150d6d03"; ENG = {"name": "gemmi", "version": "0.7.5"}
pk = mine["plan_key"] = H(E("receptor-materialization-plan", profile="1.0", algorithm="1.0", catalogue_sha256=CAT, engine=ENG, sources=src, source_context_key=sck,
    selected_asym_ids=["A"], unaddressed_components="preserve", exclusions=X, outside=O, exclusions_key=xk, outside_key=ok, atom_decisions_key=ak,
    connection_decisions_key=ck, category_decisions_key=gk, unavailable_categories=[], warnings=["outside-selected-asym-retained"]))
pid = mine["policy_id"] = H(E("receptor-materialization-policy", plan_key=pk, acknowledge_plan_key=pk, acknowledge_exclusions_key=xk, acknowledge_outside_key=ok, declared_by="documentary scientist"))
PFS = "9111f3e2210af7359155992b55b689f67f77a195e29e6a979c28a55e679a1d63"  # documentary input value, used as given
mine["request_key"] = H(E("receptor-materialization-request", policy_id=pid, policy_file_sha256=PFS, source_context_key=sck, plan_key=pk, profile="1.0",
    algorithm="1.0", catalogue_sha256=CAT, engine=ENG, application_version="0.0.0-documentary"))
inputs = {"inspection_id": insp, "raw_sha256": raw_sha, "raw_size": len(raw), "records": [[r["sha256"], r["size_bytes"]] for r in recs], "rows_key": rk, "w_atom_ids_key": iw, "occ_a": ka, "occ_b": kb}
test_src = open(sys.argv[1], encoding="utf-8").read()
import re
lit = dict(re.findall(r'^_GOLDEN_([A-Z_]+)_SHA256 = "([0-9a-f]{64})"', test_src, re.M))
name = {"CANONICAL_JSON": "canonical_json", "LEGACY_INSPECTION_ID": "legacy_inspection_id", "SOURCE_CONTEXT_KEY": "source_context_key", "OCCURRENCE_KEY": "occurrence_key",
        "ATOM_IDS_KEY": "atom_ids_key", "EXCLUSIONS_KEY": "exclusions_key", "OUTSIDE_KEY": "outside_key", "ATOM_DECISIONS_KEY": "atom_decisions_key",
        "CONNECTION_DECISIONS_KEY": "connection_decisions_key", "CATEGORY_DECISIONS_KEY": "category_decisions_key", "PLAN_KEY": "plan_key", "POLICY_ID": "policy_id", "REQUEST_KEY": "request_key"}
cmp = {name[k]: {"test_literal": v, "reviewer": mine[name[k]], "equal": v == mine[name[k]]} for k, v in lit.items()}
inputs_in_test = {k: (str(v) in test_src) for k, v in {"inspection_id": insp, "raw_sha256": raw_sha, "rows_key": rk, "w_atom_ids_key": iw, "occ_a": ka, "occ_b": kb,
    **{f"record_{i}": r["sha256"] for i, r in enumerate(recs)}}.items()}
print(json.dumps({"literal_count": len(lit), "all_equal": all(c["equal"] for c in cmp.values()), "comparison": cmp, "documentary_inputs_present_in_test": inputs_in_test,
                  "record_sizes": [r["size_bytes"] for r in recs], "raw_size": len(raw)}, indent=1))
