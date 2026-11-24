"""Architect pure-boundary diagnostic only. Usage: python -I -B [-O] PURE_DOMAIN_PROBE.py <exact-code-checkout>. No pytest, native parser, source edits or scientific RAW."""
import pathlib,sys
SRC=str(pathlib.Path(sys.argv[1]).resolve()/"src")

import hashlib,json,sys,types
sys.modules['gemmi']=None
sys.modules['rdkit']=None
sys.path.insert(0,SRC)
import pydantic
from molecular.inputs import ProteinInput,AcquisitionRecord,RawArtifact
from molecular.receptor_selection import ReceptorSelectionPolicy
import molecular.receptor_materialization as r
from datetime import datetime,timezone
NS=types.SimpleNamespace
def attempt(fn):
 try:
  v=fn();return {'status':'accepted','value':v}
 except (ValueError,TypeError) as e:
  return {'status':'rejected','type':type(e).__name__,'code':getattr(e,'code',None),'detail':str(e).splitlines()[0]}
raw='a'*64
payload=dict(inspection_schema_version='1.0',inspection_profile_version='1.0',parser_name='gemmi',parser_version='0.7.5',protein_input_id='p1',raw_checksum=raw,raw_format='mmcif')
legacy=r._compute_legacy_inspection_id(parser_name='gemmi',parser_version='0.7.5',protein_input_id='p1',raw_checksum=raw,raw_format='mmcif')
records=tuple(r.RecordSnapshot(kind=k,id=(legacy if k=='inspection' else 'p1' if k=='protein' else 's1'),sha256=str(i)*64,size_bytes=1,schema_version=None if k=='protein' else '1.0') for i,k in enumerate(['protein','inspection','selection','resolution'],1))
sc=r.SourceContext(protein_input_id='p1',selection_id='s1',inspection_id=legacy,model=1,records=records,raw_sha256=raw,raw_size_bytes=1,parser=r.Engine())
def res(d=()):return NS(resolved_model=1,resolved_chains=(NS(label_asym_id='A',label_entity_id='E1',model_number=1),),resolved_component_dispositions=d,resolved_assembly=None,protein_input_id='p1',parser=NS(name='gemmi',version='0.7.5'),structure_format='mmcif',policy_selection_id='s1',resolved_selection_id='s1',inspection_id=legacy,raw_checksum=raw)
def atom(o,aid,model=1,asym='A',ccd='ALA',ent='E1'):
 return r.AtomObservation(ordinal=o,atom_id=aid,model=model,label_asym_id=asym,entity_id=ent,entity_type='polymer',ccd=ccd,label_seq_id='1')
def pl(rr,atoms):return r.build_materialization_plan(source_context=sc,resolved_selection=rr,unaddressed_components='preserve',atoms=atoms)
def mask(rr,atoms):return [[x.atom_id,x.retained,x.reason] for x in pl(rr,atoms).atom_decisions]
def category(**kw):return r.CategoryDecision(**kw).model_dump(mode='json')
probes={}
for name in ['_cell','_symmetry']:
 probes['filter_generate_'+name]=attempt(lambda name=name:category(category=name,action='filter',generated_tags=('entry_id',),kept_row_ordinals=(0,),source_rows_key='b'*64))
for arr in ['kept_row_ordinals','omitted_row_ordinals']:
 probes['repeated_category_'+arr]=attempt(lambda arr=arr:category(category='_atom_site',action='filter',source_rows_key='b'*64,**{arr:(0,0)}))
probes['canonical_family_control']=attempt(lambda:category(category='_em_example',action='omit',source_rows_key='b'*64))
probes['family_name_with_control']=attempt(lambda:category(category='_em_example\n',action='omit',source_rows_key='b'*64))
for ccd in ['GLY','ALA']:
 rr=res((NS(label_asym_id='A',ccd_code=ccd,disposition='remove'),))
 probes['disposition_remove_'+ccd]=attempt(lambda rr=rr:mask(rr,(atom(0,'a1'),atom(1,'a2',model=2,ccd='GLY'))))
def context(fmt='mmcif',declared='mmcif'):
 pi=ProteinInput(id='p1',name='documentary fixture',acquisition=AcquisitionRecord(method='uploaded',acquired_at=datetime(2026,11,24,tzinfo=timezone.utc),raw_artifact=RawArtifact(path='inputs/proteins/p1/raw.cif',format=fmt,checksum=raw)))
 policy=ReceptorSelectionPolicy(schema_version='1.0',selection_id='s1',protein_input_id='p1',inspection_id=legacy,raw_checksum_observed=raw,declared_by='documentary actor',declared_at=datetime(2026,11,24,tzinfo=timezone.utc))
 rep=NS(parser=NS(name='gemmi',version='0.7.5'),inspection_schema_version='1.0',inspection_profile_version='1.0',structure_format='mmcif',raw_format_declared=declared,selection_capability='full',warnings=(),protein_input_id='p1',inspection_id=legacy,raw_checksum=raw)
 return r.build_source_context(protein_input=pi,inspection_report=rep,policy=policy,resolved_selection=res(),raw_size_bytes=1,records=records).raw_format
probes['source_context_valid']=attempt(context)
probes['acquisition_format_pdb_inspection_mmcif']=attempt(lambda:context(fmt='pdb'))
probes['declared_format_pdb_observed_mmcif']=attempt(lambda:context(declared='pdb'))
probes['legacy_hash_pure_backend']={'hash':legacy,'independent_documentary_hash':hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()}
for cls in [r.MaterializationInputError,r.MaterializationConfigurationError]:
 probes[cls.__name__+'_invalid_code']=attempt(lambda cls=cls:cls('NOT_A_CODE','message'))
print(json.dumps({'python':sys.version.split()[0],'pydantic':pydantic.__version__,'optional_modules_blocked_without_stub':True,'legacy_source_records':'ProteinInput/policy real DTOs; inspection/resolution documentary namespaces for pure-boundary diagnostics, not native parsing or 020 validation','probes':probes},ensure_ascii=False))
