"""Non-normative test vectors, derived only from frozen payload definitions.
No production imports, RDKit/Gemmi, parsing, file publication or scientific claims.
"""
import hashlib
import json
import pathlib

ROOT=pathlib.Path(__file__).resolve().parent
V=[]
def canonical(d):return json.dumps(d,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False)
def h(d):return hashlib.sha256(canonical(d).encode('utf-8')).hexdigest()
def add(name,payload,function):
 text=canonical(payload);key=h(payload)
 V.append({'name':name,'production_entry_point':function,'payload':payload,'canonical_utf8':text,'expected_sha256_literal':key})
 return key
def env(kind,**kw):return {'kind':kind,'version':'1.0',**kw}

add('canonical_json',{'version':'1.0','kind':'k','s':'éÅ','l':[2,1],'n':None,'b':True},'compute_materialization_hash')
legacy={'inspection_schema_version':'1.0','inspection_profile_version':'1.0','parser_name':'gemmi','parser_version':'0.7.5','protein_input_id':'protein-1','raw_checksum':'a'*64,'raw_format':'mmcif'}
legacy_id=add('legacy_inspection_id',legacy,'_compute_legacy_inspection_id')
assert legacy_id=='1c217d99e7b2b09d9c31a0c8f9daf056c48aa916bdf957cae83df449ad68e80c'

raw_bytes=b'documentary CP1 hash fixture only; no CIF geometry or parsing'
raw_sha=hashlib.sha256(raw_bytes).hexdigest()
source_inspection_id=h({**legacy,'raw_checksum':raw_sha})
records=[]
record_descriptions=[]
for kind,identity in [('protein','protein-1'),('inspection',source_inspection_id),('selection','sel-1'),('resolution','sel-1')]:
 documentary=canonical({'fixture':'cp1-documentary-v1','kind':kind,'id':identity}).encode()
 records.append({'kind':kind,'id':identity,'sha256':hashlib.sha256(documentary).hexdigest(),'size_bytes':len(documentary),'schema_version':None if kind=='protein' else '1.0'})
 record_descriptions.append({'kind':kind,'documentary_bytes_utf8':documentary.decode()})
sources={'protein_input_id':'protein-1','selection_id':'sel-1','inspection_id':source_inspection_id,'model':1,'records':records,'raw_sha256':raw_sha,'raw_size_bytes':len(raw_bytes),'raw_format':'mmcif','inspection_schema':'1.0','inspection_profile':'1.0','parser':{'name':'gemmi','version':'0.7.5'}}
source_key=add('source_context_key',env('receptor-materialization-sources',sources=sources),'compute_source_context_key')
def occurrence(asym,entity,ccd,seq,authseq):
 return {'model':1,'label_asym_id':asym,'entity_id':entity,'ccd':ccd,'label_seq_id':seq,'auth_asym_id':asym,'auth_seq_id':authseq,'insertion_token':None}
oa=occurrence('A','E1','ALA','1','1');ob=occurrence('B','E2','ALA','1','1');ow=occurrence('W','EW','HOH',None,'17')
occ_w=add('occurrence_key',env('receptor-materialization-occurrence',identity=ow),'compute_occurrence_key')
occ_a=h(env('receptor-materialization-occurrence',identity=oa));occ_b=h(env('receptor-materialization-occurrence',identity=ob))
ids_b=[{'ordinal':1,'id':'b1'}];ids_w=[{'ordinal':2,'id':'w1'}]
b_key=add('atom_ids_key',env('receptor-materialization-atom-ids',atoms=ids_b),'compute_atom_ids_key')
w_key=h(env('receptor-materialization-atom-ids',atoms=ids_w))
xs=[{'model':1,'label_asym_id':'B','entity_id':'E2','atom_count':1,'atom_ids_key':b_key}]
outside=[{'identity':ow,'occurrence_key':occ_w,'decision_source':'unaddressed-preserve','atom_count':1,'atom_ids_key':w_key,'author_id_coincidence':'none'}]
x_key=add('exclusions_key',env('receptor-materialization-exclusions',source_context_key=source_key,model=1,entries=xs),'compute_exclusions_key')
o_key=add('outside_key',env('receptor-materialization-outside',source_context_key=source_key,model=1,entries=outside),'compute_outside_key')
atoms=[{'ordinal':0,'atom_id':'a1','occurrence_key':occ_a,'retained':True,'reason':'selected-asym'},{'ordinal':1,'atom_id':'b1','occurrence_key':occ_b,'retained':False,'reason':'chain-complement'},{'ordinal':2,'atom_id':'w1','occurrence_key':occ_w,'retained':True,'reason':'unaddressed-preserve'}]
atom_key=add('atom_decisions_key',env('receptor-materialization-atom-decisions',source_context_key=source_key,decisions=atoms),'compute_atom_decisions_key')
conn_key=add('connection_decisions_key',env('receptor-materialization-connection-decisions',source_context_key=source_key,decisions=[]),'compute_connection_decisions_key')
# Source rows only seed an existing CategoryDecision field. CP1 is not asked
# to implement source-row/category parsing or hash functions reserved for CP2.
rows=[h(env('receptor-materialization-source-row',source_context_key=source_key,category='_atom_site',ordinal=i,tokens=[{'tag':'id','token':v}])) for i,v in enumerate(['a1','b1','w1'])]
rows_key=h(env('receptor-materialization-source-category',source_context_key=source_key,category='_atom_site',rows=rows))
categories=[{'category':'_atom_site','action':'filter','kept_row_ordinals':[0,2],'omitted_row_ordinals':[1],'preserved_tags':['id'],'omitted_tags':[],'generated_tags':[],'source_rows_key':rows_key}]
cat_key=add('category_decisions_key',env('receptor-materialization-category-decisions',source_context_key=source_key,decisions=categories),'compute_category_decisions_key')
catalogue='8561039fd15137811b60316336dff04539df3732710dca6ec4009f23150d6d03'
plan=env('receptor-materialization-plan',profile='1.0',algorithm='1.0',catalogue_sha256=catalogue,engine={'name':'gemmi','version':'0.7.5'},sources=sources,source_context_key=source_key,selected_asym_ids=['A'],unaddressed_components='preserve',exclusions=xs,outside=outside,exclusions_key=x_key,outside_key=o_key,atom_decisions_key=atom_key,connection_decisions_key=conn_key,category_decisions_key=cat_key,unavailable_categories=[],warnings=['outside-selected-asym-retained'])
plan_key=add('plan_key',plan,'compute_plan_key')
policy_payload=env('receptor-materialization-policy',plan_key=plan_key,acknowledge_plan_key=plan_key,acknowledge_exclusions_key=x_key,acknowledge_outside_key=o_key,declared_by='documentary scientist')
policy_key=add('policy_id',policy_payload,'compute_policy_id')
policy_record={'kind':'receptor-materialization-policy','schema_version':'1.0','profile_version':'1.0','algorithm_version':'1.0','catalogue_sha256':catalogue,'engine':{'name':'gemmi','version':'0.7.5'},'policy_id':policy_key,'sources':sources,'source_context_key':source_key,'plan_key':plan_key,'unaddressed_components':'preserve','exclusions_key':x_key,'outside_key':o_key,'excluded_polymer_asym_count':1,'outside_occurrence_count':1,'acknowledge_plan_key':plan_key,'acknowledge_exclusions_key':x_key,'acknowledge_outside_key':o_key,'declared_by':'documentary scientist','declared_at':'2026-01-01T00:00:00.000000Z'}
policy_bytes=(canonical(policy_record)+'\n').encode()
request=env('receptor-materialization-request',policy_id=policy_key,policy_file_sha256=hashlib.sha256(policy_bytes).hexdigest(),source_context_key=source_key,plan_key=plan_key,profile='1.0',algorithm='1.0',catalogue_sha256=catalogue,engine={'name':'gemmi','version':'0.7.5'},application_version='0.0.0-documentary')
add('request_key',request,'compute_request_key')
out={'status':'NON_NORMATIVE_DOCUMENTARY_TEST_VECTORS','generator':'stdlib hashlib/json only; no production import','basis':'Frozen specification §13 and SCHEMAS §2/3/4/6; legacy seven-field projection independently read from baseline020','scientific_execution_claimed':False,'notes':['No scientific RAW or native parsing. Declared raw and record byte strings are documentary test material, not valid receptor files or historical020 records.','Plan/Policy DTO fixtures test hashing of valid fields; they are not a claim that a native adapter emitted this plan.','policy_file_sha256 hashes the explicitly supplied JSON documentary policy bytes with one LF; this is not a production YAML serializer golden.','Copy vectors as literals into the allowed test file; no runtime download/catalogue/file dependency or new fixture file.','Source rows are documentary seed metadata only; no CP2 functions are required.'],'documentary_material':{'raw_bytes_utf8':raw_bytes.decode(),'record_bytes':record_descriptions,'policy_record':policy_record,'policy_bytes_utf8':policy_bytes.decode()},'vectors':V}
assert len(V)==13
(ROOT/'DOCUMENTARY_GOLDEN_VECTORS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'vector_count':len(V),'legacy_literal':legacy_id,'production_imported':False},indent=2))
