import sys; sys.path.insert(0,'/tmp/probes')
from harness import *
B = BASE
res = []
# baseline control
o = outcome(lambda: run(B)); res.append(show("control_minimal", o, "ACCEPTED"))
# C-06 genuine save frames that bypass the column-0 / lowercase regex
for label, frag in [("savefr_indented", "\n  save_fr\n_x.y 1\nsave_\n"), ("savefr_uppercase", "\nSAVE_fr\n_x.y 1\nSAVE_\n"),
                    ("savefr_lowercase_col0", "\nsave_fr\n_x.y 1\nsave_\n")]:
    o = outcome(lambda: run(B + frag)); res.append(show(label, o, "REFUSED"))
    if o["result"] == "ACCEPTED":
        print("   frame content in output?", b"_x.y" in o["obj"].output_bytes, "| x in plan categories?",
              any(d.category == "_x" for d in o["obj"].plan.category_decisions))
# C-01 numeric lexical grammar: quoted numerics / integer grammar
def sub(old, new, s=B): 
    assert old in s, old; return s.replace(old, new, 1)
line1 = "ATOM 1 C CA . ALA A E1 1 A 1 ? 1 1.000 2.000 3.000 1.00 10.00"
probes = {
 "quoted_cartn_x": line1.replace("1.000 2.000", "'1.000' 2.000"),
 "quoted_occupancy": line1.replace("1.00 10.00", "'1.00' 10.00"),
 "quoted_b_iso": line1.replace("1.00 10.00", "1.00 '10.00'"),
 "su_before_exponent_cartn": line1.replace("1.000 2.000", "1.2(4)e3 2.000"),
 "underscore_cartn": line1.replace("1.000 2.000", "1_000 2.000"),
 "quoted_model_num": line1.replace("? 1 1.000", "? '1' 1.000"),
 "plus_model_num": line1.replace("? 1 1.000", "? +1 1.000"),
 "underscore_model_num_equal_to_1": None,
}
for label, newline in probes.items():
    if newline is None: continue
    o = outcome(lambda: run(sub(line1, newline))); res.append(show(label, o, "REFUSED"))
# model num with Unicode digit '١' (Arabic-Indic one) applied to all model columns of chain rows
u = B.replace(" ? 1 1.", " ? ١ 1.").replace(" ? 1 9.", " ? ١ 9.")
o = outcome(lambda: run(u)); res.append(show("unicode_digit_model_num_all_rows", o, "REFUSED"))
# formal charge grammar
fc = B.replace("_atom_site.B_iso_or_equiv\n", "_atom_site.B_iso_or_equiv\n_atom_site.pdbx_formal_charge\n")
rows = [l for l in fc.splitlines() if l.startswith("ATOM ")]
for label, val in [("formal_charge_nonnumeric", "abc"), ("formal_charge_decimal", "1.5"), ("formal_charge_quoted", "'1'")]:
    t = fc
    for i, l in enumerate(rows):
        t = t.replace(l, l + " " + (val if i == 0 else "0"), 1)
    o = outcome(lambda: run(t)); res.append(show(label, o, "REFUSED"))
t = fc
for l in rows: t = t.replace(l, l + " ?", 1)
o = outcome(lambda: run(t)); res.append(show("formal_charge_null_control", o, "ACCEPTED"))
t = fc
for l in rows: t = t.replace(l, l + " -1", 1)
o = outcome(lambda: run(t)); res.append(show("formal_charge_int_control", o, "ACCEPTED"))
print("SUMMARY matches", sum(res), "of", len(res))
