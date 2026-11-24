"""Architect domain probes against exact published CP1 source; no pytest or RAW IO."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib, json, platform, sys, types

# Controlled diagnostic only: this does not make the native-free import pass.
# The separate clean import already failed. No Gemmi attribute can be used.
if "--inert-import-only-sentinel" in sys.argv:
    sentinel=types.ModuleType("gemmi")
    def forbidden_native_attribute(name):
        if name.startswith("__"): raise AttributeError(name)
        raise AssertionError("Native Gemmi access forbidden in this conditional domain probe: "+name)
    sentinel.__getattr__=forbidden_native_attribute
    sys.modules["gemmi"]=sentinel

ROOT=Path(__file__).parent
code_src=(Path(sys.argv[sys.argv.index('--code-root')+1])/'src') if '--code-root' in sys.argv else ROOT/'code/src'
sys.path.insert(0,str(code_src))
import pydantic
from molecular.receptor_materialization import (
    AtomObservation, CategoryDecision, Engine, RecordSnapshot, SourceContext,
    build_materialization_plan,
)
from molecular.receptor_inspection import ParserProvenance, compute_inspection_id
from molecular.receptor_resolution import (
    ResolvedChainSelection, ResolvedComponentDisposition, ResolvedReceptorSelection,
)

def digest(b):return hashlib.sha256(b).hexdigest()
raw_documentary_bytes=b'documentary domain probe: no RAW parsing is claimed'
raw=digest(raw_documentary_bytes)
iid=compute_inspection_id(parser_name='gemmi',parser_version='0.7.5',protein_input_id='p1',raw_checksum=raw,raw_format='mmcif')

def resolution(dispositions=()):
    return ResolvedReceptorSelection(schema_version='1.0',resolved_selection_id='s1',policy_selection_id='s1',protein_input_id='p1',inspection_id=iid,raw_checksum=raw,structure_format='mmcif',parser=ParserProvenance(name='gemmi',version='0.7.5'),resolved_model=1,model_resolution_basis='explicitly-selected',resolved_assembly=None,resolved_chains=(ResolvedChainSelection(label_asym_id='A',label_entity_id='E1',model_number=1),),resolved_component_dispositions=dispositions,resolved_at=datetime(2026,11,24,tzinfo=timezone.utc))

def context(r):
    records=[]
    for kind,id in [('protein','p1'),('inspection',iid),('selection','s1'),('resolution','s1')]:
        b=json.dumps({'kind':kind,'id':id,'resolution':r.model_dump(mode='json')},sort_keys=True).encode()
        records.append(RecordSnapshot(kind=kind,id=id,sha256=digest(b),size_bytes=len(b),schema_version=None if kind=='protein' else '1.0'))
    return SourceContext(protein_input_id='p1',selection_id='s1',inspection_id=iid,model=1,records=tuple(records),raw_sha256=raw,raw_size_bytes=len(raw_documentary_bytes),parser=Engine())

def atom(ordinal,atom_id,model,ccd):
    return AtomObservation(ordinal=ordinal,atom_id=atom_id,model=model,label_asym_id='A',entity_id='E1',entity_type='polymer',ccd=ccd,label_seq_id='1',auth_asym_id='A',auth_seq_id='1')

results=[]
for category in ['_cell','_symmetry']:
    common=dict(category=category,action='filter',kept_row_ordinals=(0,),source_rows_key=digest(b'category source row'))
    try:
        CategoryDecision(**common,preserved_tags=('entry_id',))
        control='accepted'
    except Exception as e:
        control=type(e).__name__
    try:
        CategoryDecision(**common,generated_tags=('entry_id',))
        observed={'status':'accepted'}
    except pydantic.ValidationError as e:
        observed={'status':'rejected','type':type(e).__name__,'reason':e.errors()[0]['msg']}
    results.append({'id':'category-filter-generated-'+category,'production':'CategoryDecision','catalogue_action':'filter','catalogue_generate_tags':['entry_id'],'expected':'accepted under frozen catalogue entry_id projection','control_without_generated_tags':control,'observed':observed})

atoms=(atom(0,'a1',1,'ALA'),atom(1,'a2',2,'GLY'))
r=resolution()
control_plan=build_materialization_plan(source_context=context(r),resolved_selection=r,unaddressed_components='preserve',atoms=atoms)
control=[{'atom_id':d.atom_id,'retained':d.retained,'reason':d.reason} for d in control_plan.atom_decisions]
for ccd in ['GLY','ALA']:
    r=resolution((ResolvedComponentDisposition(label_asym_id='A',ccd_code=ccd,classification='modified-polymer-residue',disposition='remove',disposition_source='component_dispositions'),))
    try:
        p=build_materialization_plan(source_context=context(r),resolved_selection=r,unaddressed_components='preserve',atoms=atoms)
        observed={'status':'accepted','decisions':[{'atom_id':d.atom_id,'retained':d.retained,'reason':d.reason} for d in p.atom_decisions]}
    except Exception as e:
        observed={'status':'rejected','type':type(e).__name__,'code':getattr(e,'code',None),'message':str(e)}
    results.append({'id':'polymer-disposition-'+ccd,'production':'build_materialization_plan','input_model':1,'rows':[{'model':1,'ccd':'ALA'},{'model':2,'ccd':'GLY'}],'disposition':{'asym':'A','ccd':ccd,'action':'remove'},'expected':'ignore absent key in M; retain M=1 ALA, exclude M=2' if ccd=='GLY' else 'reject actual remove of selected polymer residue in M','control_without_disposition':control,'observed':observed})

out=dict(code_commit='711f3070765efe67a5799f939f1a18306ed8afdd',role='architect-triage-not-independent-checkpoint-approval',python=sys.version.split()[0],pydantic=pydantic.__version__,platform=platform.system(),dependency_isolation=('Inert import-only gemmi sentinel; any native attribute access raises. This does not validate a Gemmi-free import or native parsing.' if '--inert-import-only-sentinel' in sys.argv else 'Normal installed dependency import; no native operations used by these domain probes.'),dependency_stub_used=('--inert-import-only-sentinel' in sys.argv),scope='Synthetic typed in-memory DTOs only; hashes derive from explicitly declared documentary bytes, not scientific RAW. Production functions imported from exact verified snapshot; no pytest/Gemmi/Windows/materialization.',results=results)
print(json.dumps(out,ensure_ascii=False,indent=2))
