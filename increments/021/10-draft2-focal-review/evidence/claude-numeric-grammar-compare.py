"""Reviewer scratch: compare draft-2 numeric regex with Gemmi 0.7.5 cif::is_numb (via numb_probe)."""
import re, subprocess, sys, json
rx = re.compile(r"[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?(?:\([0-9]+\))?")
toks = ["1", "-1", "+1", "1.", ".5", "-.5", "1.25", "0.000", "1.2e3", "1.2E-3", "1.2e3(4)", "1.2(4)e3", "1.20(3)",
        "1(2)", ".5(1)", "5.(1)", "1e5", "e5", ".", "-", "+", "1.2.3", "1,2", "1.2(", "1.2()", "1.2(a)", "nan", "inf",
        "-inf", "0x10", "1_000", " 1", "1 ", "1.2e", "1.2e+", "--1", "+-1", "1.2e3(4)5", "9" * 40]
p = subprocess.run([sys.argv[1]], input="\n".join(toks) + "\n", capture_output=True, text=True, check=True)
gem = dict(l.split("\t") for l in p.stdout.splitlines())
rows = [{"token": t, "draft2_regex": bool(rx.fullmatch(t)), "gemmi_is_numb": gem[t] == "1"} for t in toks]
diff = [r for r in rows if r["draft2_regex"] != r["gemmi_is_numb"]]
print(json.dumps({"cases": rows, "disagreements": diff}, indent=1))
