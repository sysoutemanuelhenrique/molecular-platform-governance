#!/bin/sh
# Reviewer mutation check on disposable scratch copies (production tree untouched). Runs the EXACT new pytest node
# and the full test file against: original production, and mutants of compute_atom_ids_key that sort by ordinal,
# sort by atom_id, reverse, and sort by ordinal descending. Inert gemmi sentinel on PYTHONPATH only to import 020 DTOs.
# args: <src dir> <test file> <sentinel dir>
set -e
SRC=$1; T=$2; SENT=$3; W=$(mktemp -d)
cp -r "$SRC" "$W/src"; mkdir "$W/tests"; cp "$T" "$W/tests/test_rm.py"
F="$W/src/molecular/receptor_materialization.py"; ORIG=$(cat "$F")
OLD='"atoms": [{"ordinal": atom.ordinal, "id": atom.atom_id} for atom in atoms],'
NODE="tests/test_rm.py::test_atom_ids_key_preserves_given_order_against_ordinal_and_id_sorting"
for M in original "sorted(atoms, key=lambda a: a.ordinal)" "sorted(atoms, key=lambda a: a.atom_id)" "reversed(tuple(atoms))" "sorted(atoms, key=lambda a: -a.ordinal)"; do
  if [ "$M" = original ]; then printf '%s\n' "$ORIG" > "$F"; else
    printf '%s\n' "$ORIG" | python3 -I -c "import sys;s=sys.stdin.read();o=sys.argv[1];assert s.count(o)==1;print(s.replace(o,o.replace('for atom in atoms','for atom in '+sys.argv[2])),end='')" "$OLD" "$M" > "$F"; fi
  N=$(cd "$W" && PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$W/src:$SENT" python3 -B -m pytest -p no:cacheprovider -q "$NODE" 2>&1 | tail -1)
  A=$(cd "$W" && PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$W/src:$SENT" python3 -B -m pytest -p no:cacheprovider -q tests/test_rm.py 2>&1 | tail -1)
  FAILED=$(cd "$W" && PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$W/src:$SENT" python3 -B -m pytest -p no:cacheprovider -q -rf tests/test_rm.py 2>&1 | grep '^FAILED' | sed 's/ - .*//' | tr '\n' ' ')
  echo "mutant=[$M] | exact_new_node: $N | whole_file: $A | failed: ${FAILED:-none}"
done
rm -rf "$W"
