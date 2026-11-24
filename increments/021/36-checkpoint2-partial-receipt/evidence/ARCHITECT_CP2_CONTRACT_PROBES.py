"""Architect pure-helper documentary probes for exact CP2 partial commit 0d06ebd.
Usage: python -B ARCHITECT_CP2_CONTRACT_PROBES.py /path/to/disposable/code-copy/src
Requires project base dependencies already installed. No installations, pytest,
native Gemmi/RDKit, scientific file parsing, repository writes or persistence.
The exact adapter helper bodies are extracted by AST; this is not native validation.
"""
import ast,dataclasses,hashlib,importlib.util,json,pathlib,re,sys,typing,__future__
SRC=pathlib.Path(sys.argv[1]).resolve()
for rel,expected in {
 'molecular/receptor_materialization.py':'0c7451e5b4950644c1e428c98a0c92f35f4aa3ae7753db4715cc292f6afa9947',
 'molecular/receptor_parsing.py':'a620a659b172e418d7ed676b35c2736374f59f4a3db48616d608e868214898fa',
}.items():
 if hashlib.sha256((SRC/rel).read_bytes()).hexdigest()!=expected:
  raise SystemExit('Unexpected snapshot; use exact 0d06ebd sources')
sys.modules['gemmi']=None;sys.modules['rdkit']=None
sys.path.insert(0,str(SRC))
spec=importlib.util.spec_from_file_location('architect_cp2_partial_domain',SRC/'molecular/receptor_materialization.py')
rm=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rm;spec.loader.exec_module(rm)
probes={}
vals={k:('1' if k in ['matrix[1][1]','matrix[2][2]','matrix[3][3]'] else '0',) for k in rm._NCS_MATRIX_COLUMNS+rm._NCS_VECTOR_COLUMNS}
vals.update({'id':('n1',),'code':('generate',),'vector[1]':('0.0000001',)})
try:rm._guard_ncs_row('_struct_ncs_oper',rm.RawCategoryTable(columns=vals),0)
except Exception as e:probes['ncs_small_nonidentity_generate']={'accepted':False,'error_class':type(e).__name__,'code':getattr(e,'code',None)}
else:probes['ncs_small_nonidentity_generate']={'accepted':True,'contract_expected':'UNSUPPORTED_NCS; exact nonzero translation, not identity'}
probes['numeric_helper']={s:rm._finite_numeric_token(s) for s in ['1.2e3(4)','1.2(4)e3','1_000','1.0','NaN']}
# Independently compute the frozen row/category envelope, not the implementation's helper.
ctx=hashlib.sha256(b'documentary non-scientific probe context').hexdigest()
raw_token='?'
row={'kind':'receptor-materialization-source-row','version':'1.0','source_context_key':ctx,'category':'_audit_conform','ordinal':0,'tokens':[{'tag':'dict_name','token':raw_token}]}
H=lambda p:hashlib.sha256(json.dumps(p,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
expected_category=H({'kind':'receptor-materialization-source-category','version':'1.0','source_context_key':ctx,'category':'_audit_conform','rows':[H(row)]})
actual_category=rm.compute_source_rows_key(source_context_key=ctx,category='_audit_conform',table=rm.RawCategoryTable(columns={'dict_name':(raw_token,)}))
probes['source_rows_envelope']={'expected_frozen_envelope':expected_category,'actual':actual_category,'matches':actual_category==expected_category,'documentary_only':True}
# Execute only exact non-native adapter classes/helpers extracted unchanged by AST.
adapter_src=(SRC/'molecular/receptor_parsing.py').read_text();adapter_ast=ast.parse(adapter_src)
selected_names={'RawCifCategory','ParsedCifDom021','CifSaveFrameRejectedError','_reject_save_frames','_verify_output_reparse','raw_cif_null_to_optional_str','_build_category_tables'}
selected=[n for n in adapter_ast.body if isinstance(n,(ast.ClassDef,ast.FunctionDef)) and n.name in selected_names]
ns={'__name__':'architect_cp2_non_native_helpers','rm':rm,'dataclass':dataclasses.dataclass,'re':re,'Tuple':typing.Tuple,'Optional':typing.Optional,'Dict':typing.Dict,'_SAVE_FRAME_PATTERN':re.compile(r'^save_\S',re.MULTILINE)}
import types
ns_module=types.ModuleType(ns['__name__']);sys.modules[ns['__name__']]=ns_module;ns_module.__dict__.update(ns);ns=ns_module.__dict__
exec(compile(ast.Module(body=selected,type_ignores=[]),'<exact adapter helper extraction>','exec',flags=__future__.annotations.compiler_flag),ns)
decision=rm.CategoryDecision(category='_atom_site',action='filter',kept_row_ordinals=(0,),omitted_row_ordinals=(),preserved_tags=('id','cartn_x'),source_rows_key=H(row))
bad=ns['ParsedCifDom021'](category_names=('atom_site',),categories={'atom_site':ns['RawCifCategory'](name='atom_site',row_count=1,columns={'id':('CHANGED_ID',),'cartn_x':('NaN',)})},parser_name='gemmi',parser_version='0.7.5')
try:ns['_verify_output_reparse'](category_decisions=(decision,),entry_id='tbmp_documentary',reparsed=bad)
except Exception as e:probes['output_wrong_tokens']={'accepted':False,'error_class':type(e).__name__,'code':getattr(e,'code',None)}
else:probes['output_wrong_tokens']={'accepted':True,'scope':'Shape helper accepts changed atom ID and NaN coordinate; not native CIF materialization'}
for token in ['?','.']:
 dom=ns['ParsedCifDom021'](category_names=('audit_conform',),categories={'audit_conform':ns['RawCifCategory'](name='audit_conform',row_count=1,columns={'dict_name':(token,)})},parser_name='gemmi',parser_version='0.7.5')
 tab=ns['_build_category_tables'](dom)['_audit_conform']
 probes['raw_marker_'+token]={'transcribed_value':tab.columns['dict_name'][0],'source_rows_key':rm.compute_source_rows_key(source_context_key=ctx,category='_audit_conform',table=tab)}
multiline='data_x\n_entity.pdbx_description\n;\nsave_literal_inside_text\n;\n'
try:ns['_reject_save_frames'](multiline)
except Exception as e:probes['save_marker_inside_multiline']={'rejected':True,'class':type(e).__name__,'native_parser_tested':False}
else:probes['save_marker_inside_multiline']={'rejected':False}
probes['entry_case_static']={'actual_assignment':'entry_id = f"TBMP_{plan.plan_key}"','required_prefix':'tbmp_','present_in_source':'entry_id = f"TBMP_{plan.plan_key}"' in adapter_src}
atom=rm.AtomObservation(ordinal=0,atom_id='a1',model=1,label_asym_id='A',entity_id='E1',entity_type='polymer',ccd='ALA',label_seq_id='1',auth_asym_id='A',auth_seq_id='1',label_atom_id='CA')
ad=rm.AtomDecision(ordinal=0,atom_id='a1',occurrence_key=rm.compute_occurrence_key(rm._build_occurrence_identity(atom)),retained=True,reason='selected-asym')
columns={'id':('a1',),'type_symbol':('C',),'label_atom_id':('CA',),'label_alt_id':(None,),'label_comp_id':('ALA',),'label_asym_id':('A',),'label_entity_id':('E1',),'label_seq_id':('1',),'auth_asym_id':('A',),'auth_seq_id':('1',),'pdbx_pdb_ins_code':(None,),'pdbx_pdb_model_num':('1',),'cartn_x':('1.0',),'cartn_y':('1.0',),'cartn_z':('1.0',),'occupancy':('1.0',),'b_iso_or_equiv':('10.0',)}
cats={'_atom_site':rm.RawCategoryTable(columns=columns),'_entity':rm.RawCategoryTable(columns={'id':('E1',),'type':('polymer',)}),'_struct_asym':rm.RawCategoryTable(columns={'id':('A',),'entity_id':('E1',)}),'_chem_comp':rm.RawCategoryTable(columns={'id':('ALA',),'type':('L-peptide linking',)})}
try:rm.compute_category_decisions(source_context_key=ctx,categories=cats,retained_entity_ids=frozenset({'E1'}),retained_asym_ids=frozenset({'A'}),resolved_model=1,atoms_by_ordinal={0:atom},atom_decisions_by_ordinal={0:ad},connection_decisions=())
except Exception as e:probes['missing_polymer_conditional_categories']={'accepted':False,'code':getattr(e,'code',None),'class':type(e).__name__}
else:probes['missing_polymer_conditional_categories']={'accepted':True,'missing':['_entity_poly','_entity_poly_seq','_pdbx_poly_seq_scheme'],'scope':'Direct catalogue function, documentary DTO fixture; no native parse'}
print(json.dumps({'documentary_pure_probes_only':True,'pytest_executed':False,'native_executed':False,'probes':probes},ensure_ascii=False,indent=2))
