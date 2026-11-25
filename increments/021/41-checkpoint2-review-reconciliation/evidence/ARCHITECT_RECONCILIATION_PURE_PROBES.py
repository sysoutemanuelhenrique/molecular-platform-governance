"""Pure/read-only corroboration against a807b03; not native CIF execution.
Usage: python -B ARCHITECT_RECONCILIATION_PURE_PROBES.py /external/exact-code/src
"""
import hashlib,json,pathlib,sys
SRC=pathlib.Path(sys.argv[1]).resolve()
for p,h in {'molecular/receptor_materialization.py':'7bfe7c5699ade464fa822fec938be616115feb41ecb628bedb32b12a12e8c330','molecular/receptor_parsing.py':'58ebd796eb4b4d896e74af79424a6b625e0e152ea2371c51519165c1faf43e8a'}.items():
    if hashlib.sha256((SRC/p).read_bytes()).hexdigest()!=h:raise SystemExit('Unexpected source identity')
sys.dont_write_bytecode=True
sys.modules['gemmi']=None;sys.modules['rdkit']=None
sys.path.insert(0,str(SRC))
from molecular import receptor_materialization as rm
from molecular import receptor_parsing as rp
observed={}
def probe(name,fn):
    try:r=fn()
    except (rm.MaterializationExecutionError,rm.MaterializationConfigurationError,ValueError) as e:observed[name]={'accepted':False,'type':type(e).__name__,'code':getattr(e,'code',None)}
    else:observed[name]={'accepted':True,'result':r}

num=rm.RawCategoryTable(columns={'cartn_x':('1.000',),'cartn_y':('2',),'cartn_z':('3',),'occupancy':('1',),'b_iso_or_equiv':('10',),'pdbx_formal_charge':('abc',)},raw_columns={'cartn_x':("'1.000'",),'cartn_y':('2',),'cartn_z':('3',),'occupancy':('1',),'b_iso_or_equiv':('10',),'pdbx_formal_charge':('abc',)})
probe('decoded_numeric_helper_ignores_quoted_raw_and_invalid_charge',lambda:rm._validate_atom_site_numeric_row(num,0,frozenset(num.columns)))
observed['decoded_literal_question_mark_symmetry']=rm._resolve_symmetry_endpoint('?',rm.SymmetryOperatorTables(symmetry_equiv=None,space_group_symop=None))._asdict()
for token in ['+1','01']:
    observed['integer_lexical_interpretation_'+token]={'decimal_int':int(token),'positive':int(token)>0,'scope':'Interpretation of unquoted signed ASCII decimal integer, not an independent native run'}
for name,s in [('indented','data_x\n  save_fr\n_x.y 1\nsave_\n'),('uppercase','data_x\nSAVE_fr\n_x.y 1\nSAVE_\n')]:
    probe('preparse_guard_'+name,lambda s=s:rp._reject_save_frames(s))

atom=rm.AtomObservation(ordinal=0,atom_id='a1',model=1,label_asym_id='A',entity_id='E1',entity_type='polymer',ccd='ALA',label_seq_id='1',auth_asym_id='A',auth_seq_id='1',label_atom_id='CA')
ad=rm.AtomDecision(ordinal=0,atom_id='a1',occurrence_key=rm.compute_occurrence_key(rm._build_occurrence_identity(atom)),retained=True,reason='selected-asym')
cols={'id':('a1',),'type_symbol':('C',),'label_atom_id':('CA',),'label_alt_id':(None,),'label_comp_id':('ALA',),'label_asym_id':('A',),'label_entity_id':('E1',),'label_seq_id':('1',),'auth_asym_id':('A',),'auth_seq_id':('1',),'pdbx_pdb_ins_code':(None,),'pdbx_pdb_model_num':('1',),'cartn_x':('1.0',),'cartn_y':('1.0',),'cartn_z':('1.0',),'occupancy':('1.0',),'b_iso_or_equiv':('10.0',)}
base={'_atom_site':rm.RawCategoryTable(columns=cols),'_entity':rm.RawCategoryTable(columns={'id':('E1',),'type':('polymer',)}),'_struct_asym':rm.RawCategoryTable(columns={'id':('A',),'entity_id':('E1',)}),'_chem_comp':rm.RawCategoryTable(columns={'id':('ALA',),'type':('L-peptide linking',)}),'_entity_poly':rm.RawCategoryTable(columns={'entity_id':('E1',),'type':('polypeptide(L)',)}),'_entity_poly_seq':rm.RawCategoryTable(columns={'entity_id':('E1',),'num':('1',),'mon_id':('ALA',)}),'_pdbx_poly_seq_scheme':rm.RawCategoryTable(columns={'asym_id':('A',),'entity_id':('E1',),'seq_id':('1',),'mon_id':('ALA',)})}
def catalogue(extra):
    ds=rm.compute_category_decisions(source_context_key=hashlib.sha256(b'documentary-corroboration-only').hexdigest(),categories={**base,**extra},retained_entity_ids=frozenset({'E1'}),retained_asym_ids=frozenset({'A'}),resolved_model=1,atoms_by_ordinal={0:atom},atom_decisions_by_ordinal={0:ad},connection_decisions=())
    return [d.model_dump() for d in ds if d.category in ('_entry','_chem_comp')]
probe('duplicate_chem_comp',lambda:catalogue({'_chem_comp':rm.RawCategoryTable(columns={'id':('ALA','ALA'),'type':('x','x')})}))
probe('unvalidated_entry_source_and_missing_audit',lambda:catalogue({'_entry':rm.RawCategoryTable(columns={'id':('original',),'zz_unknown':('1',)})}))
water=rm.AtomObservation(ordinal=6,atom_id='6',model=1,label_asym_id='C',entity_id='E3',entity_type='water',ccd='HOH',label_seq_id=None,auth_asym_id='A',auth_seq_id='52',label_atom_id='O')
water2=water.model_copy(update={'ordinal':7,'atom_id':'7'})
ep=rm.RawConnectionEndpointTokens(label_asym_id='C',label_comp_id='HOH',label_seq_id=None,label_atom_id='O',auth_seq_id='52',insertion_token=None,altloc_aliases=(),symmetry_token='1_555')
probe('indistinguishable_endpoint',lambda:[a.atom_id for a in rm._resolve_endpoint_atoms(ep,[water,water2])])
sp=rm.RawCategoryTable(columns={'id':('1',),'label_asym_id':('A',),'label_seq_id':('1',),'label_alt_id':('Q',)})
probe('nonexistent_special_altloc',lambda:rm.compute_special_position_summary(categories={'_pdbx_struct_special_symmetry':sp},atoms_by_ordinal={0:atom},atom_decisions_by_ordinal={0:ad}).model_dump())
print(json.dumps({'code_sha':'a807b03f44089eb3cbacc14f871b63689a21aec9','python':sys.version,'optimized':not __debug__,'native_executed':False,'pytest_executed':False,'observed':observed},ensure_ascii=False,indent=2))
