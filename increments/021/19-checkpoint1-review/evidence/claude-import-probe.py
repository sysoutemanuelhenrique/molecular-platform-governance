"""Reviewer probe (ARCH-01): fresh-process import of unmodified production modules, no gemmi installed,
no stub. Runs each import in its own subprocess with -I semantics and PYTHONDONTWRITEBYTECODE."""
import json, subprocess, sys, os
src = sys.argv[1]
mods = ["molecular.inputs", "molecular.receptor_selection", "molecular.receptor_resolution",
        "molecular.receptor_inspection", "molecular.receptor_parsing", "molecular.receptor_materialization"]
env = {"PYTHONPATH": src, "PYTHONDONTWRITEBYTECODE": "1", "PATH": os.environ["PATH"]}
out = {"python": sys.version.split()[0], "src": src, "gemmi_importable": False, "results": {}}
for m in mods:
    code = ("import importlib,sys\n"
            f"importlib.import_module({m!r})\n"
            "print('gemmi' in sys.modules)")
    p = subprocess.run([sys.executable, "-B", "-c", code], capture_output=True, text=True, env=env, cwd="/tmp")
    err = p.stderr.strip().splitlines()[-1] if p.returncode else None
    out["results"][m] = {"returncode": p.returncode, "last_stderr_line": err,
                         "gemmi_in_sys_modules": p.stdout.strip() or None}
chain = subprocess.run([sys.executable, "-B", "-X", "importtime", "-c", "import molecular.receptor_materialization"],
                       capture_output=True, text=True, env=env, cwd="/tmp")
out["importtime_tail_molecular_lines"] = [l for l in chain.stderr.splitlines() if "molecular" in l][-12:]
print(json.dumps(out, indent=1))
