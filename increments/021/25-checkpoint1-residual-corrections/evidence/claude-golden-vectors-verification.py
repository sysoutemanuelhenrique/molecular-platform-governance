import hashlib
import molecular.receptor_materialization as rm

results = {}

# 1. canonical_json
payload = {"version": "1.0", "kind": "k", "s": "éÅ", "l": [2, 1], "n": None, "b": True}
results["canonical_json"] = rm.compute_materialization_hash(payload)

# 2. legacy_inspection_id
results["legacy_inspection_id"] = rm._compute_legacy_inspection_id(
    parser_name="gemmi", parser_version="0.7.5", protein_input_id="protein-1",
    raw_checksum="a" * 64, raw_format="mmcif",
)

# 3. source_context_key
sc = rm.SourceContext(
    protein_input_id="protein-1", selection_id="sel-1",
    inspection_id="2b367d0134006b35c4f878984e6b0cc613f5a27db5e00bc20b42044381b1b3f6", model=1,
    records=(
        rm.RecordSnapshot(kind="protein", id="protein-1", sha256="1bffa22ef057ae13d72de8812a363194cd35c0fa1b136bd24faa37b322a843b1", size_bytes=66, schema_version=None),
        rm.RecordSnapshot(kind="inspection", id="2b367d0134006b35c4f878984e6b0cc613f5a27db5e00bc20b42044381b1b3f6", sha256="64b982b230587eb5983408d68105abd62c45c879830f53754232694639230d83", size_bytes=124, schema_version="1.0"),
        rm.RecordSnapshot(kind="selection", id="sel-1", sha256="409ea1325548b16b3de5ef6312e43cf70d247a3a30565a5612e01fa2c08a3ba5", size_bytes=64, schema_version="1.0"),
        rm.RecordSnapshot(kind="resolution", id="sel-1", sha256="02fb0364edff743c45709d19f707afd25e242f569109b951992b16abbcbbcf3d", size_bytes=65, schema_version="1.0"),
    ),
    raw_sha256="d020364a30da702323fe02b6b5d10f1861dbb7c6817c61b34a2648037b3b5927", raw_size_bytes=61,
    raw_format="mmcif", inspection_schema="1.0", inspection_profile="1.0", parser=rm.Engine(name="gemmi", version="0.7.5"),
)
results["source_context_key"] = rm.compute_source_context_key(sc)

# 4. occurrence_key
identity = rm.OccurrenceIdentity(model=1, label_asym_id="W", entity_id="EW", ccd="HOH", label_seq_id=None, auth_asym_id="W", auth_seq_id="17", insertion_token=None)
results["occurrence_key"] = rm.compute_occurrence_key(identity)

# 5. atom_ids_key
atoms = (rm.AtomObservation(ordinal=1, atom_id="b1", model=1, label_asym_id="A", entity_id="E1", entity_type="polymer", ccd="ALA", label_seq_id="1"),)
results["atom_ids_key"] = rm.compute_atom_ids_key(atoms)

# 6. exclusions_key
sck = "783c1d30f99898be83fef40c069294d9219c25db45218474c1fabad7a14520df"
xentry = rm.XEntry(model=1, label_asym_id="B", entity_id="E2", atom_count=1, atom_ids_key="1696038f38afba311d8944dc19e698f2bcbeb2453bd3fb0c5a32b4ccd29445a8")
results["exclusions_key"] = rm.compute_exclusions_key(source_context_key=sck, model=1, entries=(xentry,))

# 7. outside_key
outside_identity = rm.OccurrenceIdentity(model=1, label_asym_id="W", entity_id="EW", ccd="HOH", label_seq_id=None, auth_asym_id="W", auth_seq_id="17", insertion_token=None)
oentry = rm.OutsideEntry(identity=outside_identity, occurrence_key="022d3a1316ffa9b93217161e5e004eef03c3bf500184d06042134bd016269a4e",
                          decision_source="unaddressed-preserve", atom_count=1, atom_ids_key="8eeed5d55f10287690bf61adfaffbec360b1dd75af6cb380872e1c3c7fd1eb13",
                          author_id_coincidence="none")
results["outside_key"] = rm.compute_outside_key(source_context_key=sck, model=1, entries=(oentry,))

# 8. atom_decisions_key
decisions = (
    rm.AtomDecision(ordinal=0, atom_id="a1", occurrence_key="c7be110af90a4a6028070621a83de375e8fc75c67f16d67f7df84115e66e147d", retained=True, reason="selected-asym"),
    rm.AtomDecision(ordinal=1, atom_id="b1", occurrence_key="c130a69653371b5fd775a994dc3fde9e2f892a147478289054f8cc1b5367bd57", retained=False, reason="chain-complement"),
    rm.AtomDecision(ordinal=2, atom_id="w1", occurrence_key="022d3a1316ffa9b93217161e5e004eef03c3bf500184d06042134bd016269a4e", retained=True, reason="unaddressed-preserve"),
)
results["atom_decisions_key"] = rm.compute_atom_decisions_key(source_context_key=sck, decisions=decisions)

# 9. connection_decisions_key
results["connection_decisions_key"] = rm.compute_connection_decisions_key(source_context_key=sck)

# 10. category_decisions_key
cat_decision = rm.CategoryDecision(category="_atom_site", action="filter", kept_row_ordinals=(0, 2), omitted_row_ordinals=(1,),
                                    preserved_tags=("id",), omitted_tags=(), generated_tags=(), source_rows_key="69d7a6a8fe0baba92f59dad6a6930ea5e9ad78ce6372833af7cfe1a4a073c2a6")
results["category_decisions_key"] = rm.compute_category_decisions_key(source_context_key=sck, decisions=(cat_decision,))

# 11. plan_key
plan = rm.PlanBinding(
    catalogue_sha256=rm.CATALOGUE_SHA256, engine=rm.Engine(name="gemmi", version="0.7.5"), sources=sc,
    source_context_key=sck, selected_asym_ids=("A",), unaddressed_components="preserve",
    exclusions=(xentry,), outside=(oentry,),
    exclusions_key="01c461514e8a9915d3fd9feadd2565d11ced78dafb04bc61ba9151d9aa2fe06d",
    outside_key="cafba614ae1dbc9c41f7e727926198d995d9ae3611e09664d7957b407c739e32",
    atom_decisions_key="cc0fb129f56d061a165e94774d323be510a46fa7f22a1cd816734bb0c5849850",
    connection_decisions_key="67c0c45369f339bdebbbf2fbc1ee26e20f699f9fe2b93f2edf88c68e3ed85889",
    category_decisions_key="7fc88d1a1d5deec637359849766c989e04832753ce943bb7a9bdccdfd03661df",
    unavailable_categories=(), warnings=("outside-selected-asym-retained",),
)
results["plan_key"] = rm.compute_plan_key(plan)

# 12. policy_id
results["policy_id"] = rm.compute_policy_id(
    plan_key="00b8734e5e21f85208f9578ef62ffb6e8cf077dc26b771443186bb049805e2da",
    acknowledge_plan_key="00b8734e5e21f85208f9578ef62ffb6e8cf077dc26b771443186bb049805e2da",
    acknowledge_exclusions_key="01c461514e8a9915d3fd9feadd2565d11ced78dafb04bc61ba9151d9aa2fe06d",
    acknowledge_outside_key="cafba614ae1dbc9c41f7e727926198d995d9ae3611e09664d7957b407c739e32",
    declared_by="documentary scientist",
)

# 13. request_key
results["request_key"] = rm.compute_request_key(
    policy_id="3bd864722608e2a83ecf71627cd0400380d0ad0828016bb8705c2cd62aae8d02",
    policy_file_sha256="9111f3e2210af7359155992b55b689f67f77a195e29e6a979c28a55e679a1d63",
    source_context_key=sck, plan_key="00b8734e5e21f85208f9578ef62ffb6e8cf077dc26b771443186bb049805e2da",
    profile="1.0", algorithm="1.0", catalogue_sha256=rm.CATALOGUE_SHA256, engine=rm.Engine(name="gemmi", version="0.7.5"),
    application_version="0.0.0-documentary",
)

expected = {
    "canonical_json": "14332640256b6a761e453eb0beba1ba7cb1c005ab6d7c01a8eb51dfbe0cc4994",
    "legacy_inspection_id": "1c217d99e7b2b09d9c31a0c8f9daf056c48aa916bdf957cae83df449ad68e80c",
    "source_context_key": "783c1d30f99898be83fef40c069294d9219c25db45218474c1fabad7a14520df",
    "occurrence_key": "022d3a1316ffa9b93217161e5e004eef03c3bf500184d06042134bd016269a4e",
    "atom_ids_key": "1696038f38afba311d8944dc19e698f2bcbeb2453bd3fb0c5a32b4ccd29445a8",
    "exclusions_key": "01c461514e8a9915d3fd9feadd2565d11ced78dafb04bc61ba9151d9aa2fe06d",
    "outside_key": "cafba614ae1dbc9c41f7e727926198d995d9ae3611e09664d7957b407c739e32",
    "atom_decisions_key": "cc0fb129f56d061a165e94774d323be510a46fa7f22a1cd816734bb0c5849850",
    "connection_decisions_key": "67c0c45369f339bdebbbf2fbc1ee26e20f699f9fe2b93f2edf88c68e3ed85889",
    "category_decisions_key": "7fc88d1a1d5deec637359849766c989e04832753ce943bb7a9bdccdfd03661df",
    "plan_key": "00b8734e5e21f85208f9578ef62ffb6e8cf077dc26b771443186bb049805e2da",
    "policy_id": "3bd864722608e2a83ecf71627cd0400380d0ad0828016bb8705c2cd62aae8d02",
    "request_key": "5b1de4a13571f147a84520042b4830235e7b4a611ab7b6b1b972c60027510095",
}

all_ok = True
for name, value in results.items():
    ok = value == expected[name]
    all_ok &= ok
    print(name, "OK" if ok else f"MISMATCH got={value} expected={expected[name]}")

print("ALL 13/13 MATCH:", all_ok)
