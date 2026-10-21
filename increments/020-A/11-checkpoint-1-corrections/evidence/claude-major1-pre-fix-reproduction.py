import sys, json, platform
sys.path.insert(0, r"C:\Users\Pichau\AppData\Local\Temp\claude\C--Users-Pichau-molecular-platform\22a4bf49-a173-4e9d-a4f3-91aa48e16729\scratchpad\prefix_check")
import pydantic
from molecular import characterization as c

base = dict(
    formula="C2H6O", molar_mass_g_mol=46.069, exact_mass_da=46.0419,
    formal_charge_e=0, heavy_atom_count=3, hbd_count=1, hba_count=1,
    rotatable_bond_count=0, tpsa_a2=20.2, clogp_wildman_crippen=-0.3,
)

results = []

def probe(dto, field, value):
    try:
        if dto == "CharacterizationValues":
            obj = c.CharacterizationValues(**{**base, field: value})
        else:
            obj = c.SdfParserParameters(**{field: value})
        got = getattr(obj, field)
        results.append({"dto": dto, "field": field, "supplied_repr": repr(value),
                         "supplied_type": type(value).__name__, "accepted": True,
                         "result_type": type(got).__name__, "result_repr": repr(got)})
    except pydantic.ValidationError as e:
        results.append({"dto": dto, "field": field, "supplied_repr": repr(value),
                         "supplied_type": type(value).__name__, "accepted": False})

probe("CharacterizationValues", "heavy_atom_count", "3")
probe("CharacterizationValues", "heavy_atom_count", 3.0)
probe("CharacterizationValues", "formal_charge_e", "0")
probe("CharacterizationValues", "molar_mass_g_mol", "46.069")
probe("SdfParserParameters", "sanitize", 1)

output = {
    "method": "Direct import of molecular.characterization from the exact pre-fix "
              "HEAD source (f8416b845efe93f9e47deca97f01a355e4e679ba), no pytest, "
              "re-executed independently in the corrections session before writing "
              "the fix - not copied from the review's evidence JSON",
    "python": platform.python_version(),
    "pydantic": pydantic.VERSION,
    "results": results,
}
print(json.dumps(output, indent=2))
with open(r"C:\Users\Pichau\AppData\Local\Temp\claude\C--Users-Pichau-molecular-platform\22a4bf49-a173-4e9d-a4f3-91aa48e16729\scratchpad\prefix_check\output.json", "w") as f:
    json.dump(output, f, indent=2)
