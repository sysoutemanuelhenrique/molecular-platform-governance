"""Separate comparison after independent fixture generation; production read-only."""
import json
import pathlib
import sys

sys.modules['gemmi']=None
sys.modules['rdkit']=None
sys.path.insert(0,str(pathlib.Path(sys.argv[1]).resolve()/'src'))
import molecular.receptor_materialization as m
data=json.loads(pathlib.Path(sys.argv[2]).read_text())
out=[]
def model(cls,d):return cls.model_validate_json(json.dumps(d,ensure_ascii=False))
for v in data['vectors']:
 p=v['payload'];name=v['name']
 if name=='canonical_json':got=m.compute_materialization_hash(p)
 elif name=='legacy_inspection_id':got=m._compute_legacy_inspection_id(**{k:p[k] for k in ['parser_name','parser_version','protein_input_id','raw_checksum','raw_format']})
 elif name=='source_context_key':got=m.compute_source_context_key(model(m.SourceContext,p['sources']))
 elif name=='occurrence_key':got=m.compute_occurrence_key(model(m.OccurrenceIdentity,p['identity']))
 elif name=='atom_ids_key':
  atoms=tuple(m.AtomObservation(ordinal=x['ordinal'],atom_id=x['id'],model=1,label_asym_id='B',entity_id='E2',entity_type='polymer',ccd='ALA',label_seq_id='1') for x in p['atoms'])
  got=m.compute_atom_ids_key(atoms)
 elif name in ['exclusions_key','outside_key']:
  cls=m.XEntry if name=='exclusions_key' else m.OutsideEntry
  fun=m.compute_exclusions_key if name=='exclusions_key' else m.compute_outside_key
  got=fun(source_context_key=p['source_context_key'],model=p['model'],entries=tuple(model(cls,x) for x in p['entries']))
 elif name in ['atom_decisions_key','category_decisions_key']:
  cls=m.AtomDecision if name=='atom_decisions_key' else m.CategoryDecision
  fun=m.compute_atom_decisions_key if name=='atom_decisions_key' else m.compute_category_decisions_key
  got=fun(source_context_key=p['source_context_key'],decisions=tuple(model(cls,x) for x in p['decisions']))
 elif name=='connection_decisions_key':got=m.compute_connection_decisions_key(source_context_key=p['source_context_key'])
 elif name=='plan_key':got=m.compute_plan_key(model(m.PlanBinding,p))
 elif name=='policy_id':got=m.compute_policy_id(**{k:value for k,value in p.items() if k not in ['kind','version']})
 elif name=='request_key':
  kw={k:value for k,value in p.items() if k not in ['kind','version']};kw['engine']=model(m.Engine,kw['engine']);got=m.compute_request_key(**kw)
 else:raise ValueError(name)
 out.append({'name':name,'production_matches_independent_literal':got==v['expected_sha256_literal'],'expected':v['expected_sha256_literal'],'actual':got})
 assert got==v['expected_sha256_literal'],name
model(m.PolicyRecord,data['documentary_material']['policy_record'])
print(json.dumps({'code_commit':'42b4804b5f4ea01ddf320c45473d8b4f980ea67e','scope':'architect comparison, not new tests or independent checkpoint closure','production_source_modified':False,'native_modules_blocked_without_stub':True,'vectors':out},ensure_ascii=False,indent=2))
