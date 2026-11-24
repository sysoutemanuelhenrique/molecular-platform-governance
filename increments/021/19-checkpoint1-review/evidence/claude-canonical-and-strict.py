"""Reviewer probe: (1) independent golden SHA-256 of canonical JSON bytes written by hand per §13, compared
with production compute_materialization_hash and two envelope builders; (2) strictness sweep over all new DTOs."""
import hashlib, json, sys, typing
from pydantic import ValidationError
import molecular.receptor_materialization as rm
H = lambda b: hashlib.sha256(b).hexdigest()
gold = {}
# hand-written canonical bytes (sorted keys, compact, UTF-8, no LF) - not produced by json.dumps
cases = [({"version": "1.0", "kind": "k", "s": "éÅ", "l": [2, 1], "n": None, "b": True},
          '{"b":true,"kind":"k","l":[2,1],"n":null,"s":"éÅ","version":"1.0"}'.encode("utf-8")),
         ({"kind": "receptor-materialization-atom-ids", "version": "1.0", "atoms": [{"ordinal": 3, "id": "Z"}, {"ordinal": 1, "id": "a"}]},
          b'{"atoms":[{"id":"Z","ordinal":3},{"id":"a","ordinal":1}],"kind":"receptor-materialization-atom-ids","version":"1.0"}')]
for i, (payload, raw) in enumerate(cases):
    gold[f"case{i}"] = {"hand_sha256": H(raw), "production": rm.compute_materialization_hash(payload), "equal": H(raw) == rm.compute_materialization_hash(payload)}
a = (rm.AtomObservation(ordinal=3, atom_id="Z", model=1, label_asym_id="A", entity_id="E", entity_type="polymer", ccd="ALA", label_seq_id="1"),
     rm.AtomObservation(ordinal=1, atom_id="a", model=1, label_asym_id="A", entity_id="E", entity_type="polymer", ccd="ALA", label_seq_id="1"))
gold["atom_ids_key_preserves_given_order"] = rm.compute_atom_ids_key(a) == H(cases[1][1])
idn = rm.OccurrenceIdentity(model=1, label_asym_id="A", entity_id="E", ccd="ALA", label_seq_id="1")
raw_occ = ('{"identity":{"auth_asym_id":null,"auth_seq_id":null,"ccd":"ALA","entity_id":"E","insertion_token":null,'
           '"label_asym_id":"A","label_seq_id":"1","model":1},"kind":"receptor-materialization-occurrence","version":"1.0"}').encode()
gold["occurrence_key_envelope"] = rm.compute_occurrence_key(idn) == H(raw_occ)
raw_empty = b'{"decisions":[],"kind":"receptor-materialization-connection-decisions","source_context_key":"' + b"0" * 64 + b'","version":"1.0"}'
gold["empty_connection_key_envelope"] = rm.compute_connection_decisions_key(source_context_key="0" * 64) == H(raw_empty)
# strictness sweep
models = [rm.Engine, rm.RecordSnapshot, rm.OccurrenceIdentity, rm.AtomObservation, rm.XEntry, rm.OutsideEntry, rm.AtomDecision,
          rm.CategoryDecision, rm.PlanBinding, rm.MaterializationPlan, rm.PolicyRecord, rm.SourceContext]
sweep = {}
for m in models:
    cfg = m.model_config
    sweep[m.__name__] = {"strict": cfg.get("strict"), "frozen": cfg.get("frozen"), "extra": cfg.get("extra")}
# targeted coercion attempts on concrete fields
def tries(fn):
    try: fn(); return "accepted"
    except ValidationError: return "rejected"
t = {}
t["XEntry.atom_count=True"] = tries(lambda: rm.XEntry(model=1, label_asym_id="A", entity_id="E", atom_count=True, atom_ids_key="0"*64))
t["XEntry.model='1'"] = tries(lambda: rm.XEntry(model="1", label_asym_id="A", entity_id="E", atom_count=1, atom_ids_key="0"*64))
t["RecordSnapshot.size_bytes=1.0"] = tries(lambda: rm.RecordSnapshot(kind="protein", id="p", sha256="0"*64, size_bytes=1.0))
t["CategoryDecision.kept_row_ordinals=[0]"] = tries(lambda: rm.CategoryDecision(category="_x", action="omit", kept_row_ordinals=[0]))
t["CategoryDecision.kept_row_ordinals=(True,)"] = tries(lambda: rm.CategoryDecision(category="_x", action="filter", kept_row_ordinals=(True,)))
t["CategoryDecision.kept_row_ordinals=(-1,)"] = tries(lambda: rm.CategoryDecision(category="_x", action="filter", kept_row_ordinals=(-1,)))
t["CategoryDecision.preserved_tags=(b'x',)"] = tries(lambda: rm.CategoryDecision(category="_x", action="filter", preserved_tags=(b"x",)))
t["CategoryDecision.category='_X' (non-canonical)"] = tries(lambda: rm.CategoryDecision(category="_ATOM_SITE", action="filter"))
t["CategoryDecision.category='not-in-catalogue'"] = tries(lambda: rm.CategoryDecision(category="_made_up", action="omit"))
t["AtomObservation.insertion_token=b'A'"] = tries(lambda: rm.AtomObservation(ordinal=0, atom_id="a", model=1, label_asym_id="A", entity_id="E", entity_type="polymer", ccd="ALA", label_seq_id="1", insertion_token=b"A"))
t["RecordSnapshot.id 'protein-1' vs 'Protein-1' distinct"] = "n/a"
print(json.dumps({"golden": gold, "model_config": sweep, "coercion_attempts": t}, indent=1))
