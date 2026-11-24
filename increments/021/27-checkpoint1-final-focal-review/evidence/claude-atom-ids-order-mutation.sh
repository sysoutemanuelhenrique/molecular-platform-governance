#!/bin/sh
# Reviewer mutation check (scratch copies only; production tree untouched).
# Two mutants of compute_atom_ids_key in a scratch copy of bbd491e src:
#   sort_ordinal: atoms re-sorted by source ordinal; sort_id: atoms re-sorted by atom_id.
# Each mutant is run against the bbd491e test file (91 tests) and the 42b4804 test file (75 tests),
# with the inert gemmi sentinel on PYTHONPATH only so the 020 DTO classes import.
set -e
SRC=$1; NEWT=$2; OLDT=$3; SENT=$4; W=$(mktemp -d)
cp -r "$SRC" "$W/src"; mkdir "$W/tests"; cp "$NEWT" "$W/tests/test_new.py"; cp "$OLDT" "$W/tests/test_old.py"
cp "$(dirname "$NEWT")"/conftest.py "$W/tests/" 2>/dev/null || true
F="$W/src/molecular/receptor_materialization.py"; ORIG=$(cat "$F")
OLD='"atoms": [{"ordinal": atom.ordinal, "id": atom.atom_id} for atom in atoms],'
for KEY in ordinal atom_id; do
  printf '%s' "$ORIG" | python3 -I -c "import sys;s=sys.stdin.read();o=sys.argv[1];assert s.count(o)==1;print(s.replace(o,o.replace('for atom in atoms','for atom in sorted(atoms, key=lambda a: a.$KEY)')),end='')" "$OLD" > "$F"
  for T in new old; do (cd "$W" && PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$W/src:$SENT" python3 -B -m pytest -p no:cacheprovider -q tests/test_$T.py | tail -1 | sed "s/^/mutant=sort_$KEY tests=$T : /"); done
done
rm -rf "$W"
