"""Pure/documentary probes only, fixed to a807b03. No pytest/native parsing.
Usage: python -B ARCHITECT_CP2_RESIDUAL_RECHECK.py /disposable/exact-code/src
"""
import hashlib
import importlib.abc
import json
import pathlib
import sys

src=pathlib.Path(sys.argv[1]).resolve()
for p,digest in {
    'molecular/receptor_materialization.py':'7bfe7c5699ade464fa822fec938be616115feb41ecb628bedb32b12a12e8c330',
    'molecular/receptor_parsing.py':'58ebd796eb4b4d896e74af79424a6b625e0e152ea2371c51519165c1faf43e8a',
}.items():
    if hashlib.sha256((src/p).read_bytes()).hexdigest()!=digest:
        raise SystemExit('Unexpected source identity: '+p)

attempts=[]
class NativeBlocker(importlib.abc.MetaPathFinder):
    def find_spec(self,fullname,path=None,target=None):
        if fullname.split('.')[0] in {'gemmi','rdkit'}:
            attempts.append(fullname)
            raise ModuleNotFoundError('Native import blocked for pure architectural recheck')
sys.meta_path.insert(0,NativeBlocker())
sys.path.insert(0,str(src))
from molecular import receptor_materialization as rm
from molecular import receptor_parsing as rp

observed={'native_attempts_at_import':list(attempts)}
def outcome(fn):
    try:
        result=fn()
    except (rm.MaterializationExecutionError,rm.MaterializationConfigurationError) as e:
        return {'accepted':False,'code':e.code,'phase':getattr(e,'phase',None)}
    return {'accepted':True,'result':result}
observed['entry_engine_absent']=outcome(lambda:rp.parse_receptor_cif_dom021(b'data_x'))
atom=rm.AtomObservation(ordinal=0,atom_id='a1',model=1,label_asym_id='A',entity_id='E1',entity_type='polymer',ccd='ALA',label_seq_id='1',auth_asym_id='A',auth_seq_id='1',label_atom_id='CA')
decision=rm.AtomDecision(ordinal=0,atom_id='a1',occurrence_key=rm.compute_occurrence_key(rm._build_occurrence_identity(atom)),retained=True,reason='selected-asym')
for name,fields in [
    ('special_unknown_asym',{'label_asym_id':('NO_SUCH_ASYM',),'label_seq_id':('1',)}),
    ('special_valid_residue',{'label_asym_id':('A',),'label_seq_id':('1',),'label_comp_id':('ALA',)}),
    ('special_wrong_component',{'label_asym_id':('A',),'label_seq_id':('1',),'label_comp_id':('GLY',)}),
]:
    table=rm.RawCategoryTable(columns={'id':('sp1',),**fields})
    def call(table=table):
        s=rm.compute_special_position_summary(categories={'_pdbx_struct_special_symmetry':table},atoms_by_ordinal={0:atom},atom_decisions_by_ordinal={0:decision})
        return s.model_dump()
    observed[name]=outcome(call)

source=rm.RawCategoryTable(columns={'label_seq_id':('1',),'type_symbol':('C',)})
for field,value in [('pdbx_label_seq_id','99'),('type_symbol','O')]:
    t=rm.RawCategoryTable(columns={field:(value,)})
    observed['anisotrop_'+field]=outcome(lambda t=t:rm._validate_anisotrop_field_agreement('_atom_site_anisotrop',t,0,source,0,frozenset(t.columns)))
t=rm.RawCategoryTable(columns={'u[1][1]':('0.1',),**{c:('0.1',) for c in rm._ANISOTROP_B_COLUMNS}})
observed['partial_u_complete_b']=outcome(lambda:rm._validate_anisotrop_tensor_row('_atom_site_anisotrop',t,0,frozenset(t.columns)))

entry_id='tbmp_documentary'
cat_decisions=(rm.CategoryDecision(category='_entry',action='generate',generated_tags=('id',)),rm.CategoryDecision(category='_atom_site',action='filter',kept_row_ordinals=(0,),preserved_tags=('id',),source_rows_key='a'*64))
expected={'entry':{'id':[entry_id]},'atom_site':{'id':['a1']}}
for name,extra_entry,extra_category in [('output_control',False,False),('output_extra_category',False,True),('output_extra_entry_column',True,False)]:
    cats={'entry':rp.RawCifCategory(name='entry',row_count=1,columns={'id':(entry_id,),**({'unplanned':('extra',)} if extra_entry else {})}),'atom_site':rp.RawCifCategory(name='atom_site',row_count=1,columns={'id':('a1',)})}
    if extra_category:cats['unplanned']=rp.RawCifCategory(name='unplanned',row_count=1,columns={'id':('extra',)})
    dom=rp.ParsedCifDom021(category_names=tuple(cats),categories=cats,parser_name='gemmi',parser_version='0.7.5',block_name=entry_id)
    observed[name]=outcome(lambda dom=dom:rp._verify_output_reparse(category_decisions=cat_decisions,entry_id=entry_id,block_name=entry_id,output_categories=expected,reparsed=dom))
wrong_block=rp.ParsedCifDom021(category_names=('entry',),categories={'entry':rp.RawCifCategory(name='entry',row_count=1,columns={'id':(entry_id,)})},parser_name='gemmi',parser_version='0.7.5',block_name='wrong_block')
observed['output_wrong_block']=outcome(lambda:rp._verify_output_reparse(category_decisions=cat_decisions[:1],entry_id=entry_id,block_name=entry_id,output_categories=expected,reparsed=wrong_block))
observed['reparsed_dom_has_block_identity']='block_name' in rp.ParsedCifDom021.__dataclass_fields__
print(json.dumps({'code_commit':'a807b03f44089eb3cbacc14f871b63689a21aec9','python':sys.version,'optimized':not __debug__,'pytest_executed':False,'native_execution':False,'observed':observed},ensure_ascii=False,indent=2))
