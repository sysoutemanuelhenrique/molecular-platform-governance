import importlib.util
import sys

EXPECTED_GIVEN = "96fd3eacd89d16753dbdc5ec22bb79db0740e9f355e6322cb0c4641bc0f3106a"
EXPECTED_REVERSED = "bf820fe14730b4b8ede9d8e007e4c3d32f71def5d8a4747c657d6d76dac562d1"


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def atoms_for(module):
    return (
        module.AtomObservation(ordinal=3, atom_id="a", model=1, label_asym_id="A", entity_id="E1", entity_type="polymer", ccd="ALA", label_seq_id="1"),
        module.AtomObservation(ordinal=1, atom_id="Z", model=1, label_asym_id="A", entity_id="E1", entity_type="polymer", ccd="ALA", label_seq_id="1"),
    )


# 1. Original production (unmutated) - the real test target.
original = load_module(r"C:\Users\Pichau\molecular-platform\src\molecular\receptor_materialization.py", "rm_original")
result_original = original.compute_atom_ids_key(atoms_for(original))
print("original:", "MATCHES expected given-order literal" if result_original == EXPECTED_GIVEN else f"MISMATCH got {result_original}")
assert result_original == EXPECTED_GIVEN, "the new test must pass against the real, unmutated production function"

# 2. Mutant: sort by ordinal.
mutant_ordinal = load_module(r"C:\Users\Pichau\AppData\Local\Temp\claude\C--Users-Pichau-molecular-platform\1888c1cf-1626-40fa-ad73-48471fa6098b\scratchpad\r1_mutants\mutant_ordinal.py", "rm_mutant_ordinal")
result_ordinal = mutant_ordinal.compute_atom_ids_key(atoms_for(mutant_ordinal))
print("mutant_ordinal:", "test would FAIL (detected)" if result_ordinal != EXPECTED_GIVEN else "test would PASS (NOT detected - bug)")
assert result_ordinal != EXPECTED_GIVEN, "the new test must reject the sort-by-ordinal mutant"
print("  mutant_ordinal result equals reversed literal:", result_ordinal == EXPECTED_REVERSED)

# 3. Mutant: sort by atom_id.
mutant_atomid = load_module(r"C:\Users\Pichau\AppData\Local\Temp\claude\C--Users-Pichau-molecular-platform\1888c1cf-1626-40fa-ad73-48471fa6098b\scratchpad\r1_mutants\mutant_atomid.py", "rm_mutant_atomid")
result_atomid = mutant_atomid.compute_atom_ids_key(atoms_for(mutant_atomid))
print("mutant_atomid:", "test would FAIL (detected)" if result_atomid != EXPECTED_GIVEN else "test would PASS (NOT detected - bug)")
assert result_atomid != EXPECTED_GIVEN, "the new test must reject the sort-by-atom_id mutant"
print("  mutant_atomid result equals reversed literal:", result_atomid == EXPECTED_REVERSED)

print("ALL MUTATION CHECKS CONFIRM THE NEW TEST DISCRIMINATES BOTH MUTANTS")
