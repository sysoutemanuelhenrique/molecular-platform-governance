"""Read-only constructor probes against an exact fetched source snapshot.

Not pytest, not an RDKit/scientific run, and not a Windows validation.
"""
from pathlib import Path
import ast
import hashlib
import json
import platform
import sys
import types
from typing import get_args

import pydantic
from pydantic import BaseModel, ValidationError

HERE = Path(__file__).resolve().parent
BASELINE = Path('tmp/academic_rehearsal_20261019/molecular-platform/src/molecular').resolve()
pkg = types.ModuleType('molecular')
pkg.__path__ = [str(HERE), str(BASELINE)]
sys.modules['molecular'] = pkg
from molecular import characterization as c

values = dict(formula='C2H6O', molar_mass_g_mol=46.069,
              exact_mass_da=46.0419, formal_charge_e=0, heavy_atom_count=3,
              hbd_count=1, hba_count=1, rotatable_bond_count=0,
              tpsa_a2=20.2, clogp_wildman_crippen=-0.3)
parameters = c.CharacterizationEffectiveParameters(parser=c.SmilesParserParameters())
provenance = dict(input_state_id='caffeine-1', entity_id='caffeine',
                  state_record_sha256_observed='a' * 64,
                  representation_path='scientific/artifacts/states/caffeine-1/rep.smi',
                  representation_format_declared='smiles', representation_format_resolved='smiles',
                  representation_checksum_expected='A' * 64,
                  representation_checksum_observed='a' * 64,
                  representation_size_bytes=10, engine_version='2026.03.6',
                  application_version='0.1.0', effective_parameters=parameters)
svg = '<svg xmlns="http://www.w3.org/2000/svg"/>\n'
drawing = dict(font_name='Telex-Regular.ttf', font_sha256_observed='a' * 64,
               svg_sha256=hashlib.sha256(svg.encode()).hexdigest(),
               svg_size_bytes=len(svg.encode()), xml_parser_version_observed='expat_2.6.0')
values_obj = c.CharacterizationValues(**values)
provenance_obj = c.CharacterizationProvenance(**provenance)
drawing_obj = c.DrawingResult(**drawing)
bases = {
    'CharacterizationValues': values,
    'DrawingResult': drawing,
    'CharacterizationProvenance': provenance,
    'MolecularCharacterizationResult': dict(values=values_obj, provenance=provenance_obj,
        warnings=c._RESULT_WARNINGS_BASE + (c._WARNING_WITH_SVG,), drawing=drawing_obj, svg=svg),
    'RDKitCharacterizationOutcome': dict(engine_version='2026.03.6',
        representation_format_resolved='smiles', values=values_obj, effective_parameters=parameters,
        warnings=c._ADAPTER_WARNINGS_BASE + (c._WARNING_WITH_SVG,), drawing=drawing_obj, svg=svg),
}
inventory = []
for name, cls in vars(c).items():
    if isinstance(cls, type) and issubclass(cls, BaseModel) and cls.__module__ == c.__name__:
        for field_name, field in cls.model_fields.items():
            if field.annotation is str or str in get_args(field.annotation):
                inventory.append((name, field_name))
assert set(name for name, _ in inventory) == set(bases)
assert len(inventory) == 17

results = []
for name, field in inventory:
    cls, base = getattr(c, name), bases[name]
    native = cls(**base)
    assert type(getattr(native, field)) is str
    assert cls.model_validate_json(native.model_dump_json()) == native
    trials = []
    for input_type in (bytes, bytearray):
        raw = input_type(base[field].encode())
        for entry in ('constructor', 'model_validate'):
            payload = dict(base, **{field: raw})
            try:
                out = cls(**payload) if entry == 'constructor' else cls.model_validate(payload)
            except ValidationError as exc:
                assert any(e['loc'] == (field,) for e in exc.errors()), exc
                trials.append(dict(input_type=input_type.__name__, entry=entry,
                                   rejected_at_field=True, errors=[e['type'] for e in exc.errors()]))
            else:
                assert getattr(out, field) == base[field]
                trials.append(dict(input_type=input_type.__name__, entry=entry,
                                   rejected_at_field=False, output_type=type(getattr(out, field)).__name__,
                                   silently_coerced=True))
    results.append(dict(model=name, field=field, native_str_accepted=True,
                        valid_json_roundtrip=True, trials=trials))

null_provenance = c.CharacterizationProvenance(**dict(provenance, application_version=None))
null_result = c.MolecularCharacterizationResult(values=values_obj, provenance=provenance_obj,
                                                warnings=c._RESULT_WARNINGS_BASE)
null_outcome = c.RDKitCharacterizationOutcome(engine_version='2026.03.6',
    representation_format_resolved='smiles', values=values_obj, effective_parameters=parameters,
    warnings=c._ADAPTER_WARNINGS_BASE)
assert null_provenance.application_version is None
assert null_result.svg is None and null_result.drawing is None
assert null_outcome.svg is None and null_outcome.drawing is None

data = dict(code_repository='sysoutemanuelhenrique/molecular-platform',
            code_head='36682074b55596d5632800bea98aff778eee885f',
            source_path='src/molecular/characterization.py',
            source_sha256=hashlib.sha256((HERE / 'characterization.py').read_bytes()).hexdigest(),
            python=platform.python_version(), pydantic=pydantic.__version__,
            method='Exact fetched production module with unchanged baseline inputs dependency; isolated calls, no pytest',
            limitations=['No RDKit execution', 'No Windows execution', 'No scientific or SVG profile validation claimed',
                         '17 fields are ordinary str or str|None in newly defined BaseModel DTOs; Literal/enum excluded'],
            ordinary_string_fields=len(results),
            fields_rejecting_all_four_trials=sum(all(t['rejected_at_field'] for t in r['trials']) for r in results),
            fields_accepting_all_four_trials=sum(all(not t['rejected_at_field'] for t in r['trials']) for r in results),
            positive_str_and_json_controls=17, nullable_controls=3, results=results)
out = HERE / 'architect-complete-string-matrix.json'
out.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps({k:v for k,v in data.items() if k != 'results'}, indent=2))
print('Still coercing:')
for row in results:
    if any(not t['rejected_at_field'] for t in row['trials']):
        print(row['model'] + '.' + row['field'])
