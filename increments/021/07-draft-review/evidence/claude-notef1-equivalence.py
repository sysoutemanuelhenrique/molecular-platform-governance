"""Reviewer scratch probe: compare the 020 loader text path (Path.read_text(utf-8) + yaml.safe_load)
with the draft-1 NOTE-F1 path (bytes once -> strict UTF-8 -> CRLF/CR->LF -> yaml.safe_load).
Synthetic YAML only; writes in a temporary directory; no project code imported."""
import json, tempfile, hashlib
from pathlib import Path
import yaml

def draft_path(b: bytes):
    t = b.decode("utf-8")  # strict
    t = t.replace("\r\n", "\n").replace("\r", "\n")
    return yaml.safe_load(t)

base = "id: Prot-A\nname: \"x\\u00e9\"\nlist:\n  - 1\n  - two\nnested: {a: 1}\nblock: |\n  line1\n  line2\n"
cases = {
    "lf": base.encode(),
    "crlf": base.replace("\n", "\r\n").encode(),
    "cr": base.replace("\n", "\r").encode(),
    "mixed": base.replace("\n", "\r\n", 3).encode(),
    "bom_lf": b"\xef\xbb\xbf" + base.encode(),
    "bom_crlf": b"\xef\xbb\xbf" + base.replace("\n", "\r\n").encode(),
    "trailing_cr": base.encode() + b"\r",
    "block_scalar_crlf_inside": b"block: |\r\n  a\r\n  b\r\n",
    "invalid_utf8": b"id: \xff\n",
    "nel_u0085": "id: a\u0085b\n".encode(),
    "ls_u2028": "id: a b\n".encode(),
}
out = {"pyyaml": yaml.__version__, "cases": {}}
with tempfile.TemporaryDirectory(prefix="claude021_notef1_") as d:
    for name, b in cases.items():
        p = Path(d, name + ".yaml"); p.write_bytes(b)
        res = {"sha256": hashlib.sha256(b).hexdigest()}
        try:
            a = yaml.safe_load(p.read_text(encoding="utf-8")); res["loader020"] = ["ok", repr(a)]
        except Exception as e:
            res["loader020"] = ["error", type(e).__name__]
        try:
            c = draft_path(b); res["draft"] = ["ok", repr(c)]
        except Exception as e:
            res["draft"] = ["error", type(e).__name__]
        res["equivalent"] = res["loader020"] == res["draft"]
        out["cases"][name] = res
out["all_equivalent"] = all(v["equivalent"] for v in out["cases"].values())
print(json.dumps(out, indent=1, ensure_ascii=False))
