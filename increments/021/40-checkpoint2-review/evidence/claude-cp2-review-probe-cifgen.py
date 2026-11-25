import sys; sys.path.insert(0,'/tmp/probes')
from harness import BASE
HEAD, rest = BASE.split("loop_\n_struct_conn.id", 1)
TAIL = rest.split("#\nloop_\n_struct_conn_type.id", 1)[1]
TAIL = "#\nloop_\n_struct_conn_type.id" + TAIL
TAIL = TAIL.replace("_struct_conn_type.id\ndisulf\nmetalc\n", "_struct_conn_type.id\ncovale\ndisulf\nhydrog\nmetalc\nsaltbr\n")
HEAD = HEAD.replace("ATOM 5 S SD . MET B E2 1 B 1 ? 1 9.000 9.000 9.000 1.00 12.00\n",
                    "ATOM 5 S SD . MET B E2 1 B 1 ? 1 9.000 9.000 9.000 1.00 12.00\n"
                    "ATOM 6 C CE . MET B E2 1 B 1 ? 1 9.500 9.000 9.000 1.00 12.00\n")
EP = {"A1CA": "A ALA 1 CA", "A1N": "A ALA 1 N", "A2SG": "A CYS 2 SG", "B1SD": "B MET 1 SD", "B1CE": "B MET 1 CE"}
def conn_loop(rows, extra_cols=()):
    cols = ["id","conn_type_id","ptnr1_label_asym_id","ptnr1_label_comp_id","ptnr1_label_seq_id","ptnr1_label_atom_id",
            "ptnr1_symmetry","ptnr2_label_asym_id","ptnr2_label_comp_id","ptnr2_label_seq_id","ptnr2_label_atom_id","ptnr2_symmetry", *extra_cols]
    s = "loop_\n" + "".join(f"_struct_conn.{c}\n" for c in cols)
    for r in rows: s += r + "\n"
    return s
def row(cid, ctype, e1, s1, e2, s2, extra=()):
    return " ".join([cid, ctype, EP[e1], s1, EP[e2], s2, *extra])
def tables(symeq=None, sgop=None):
    s = ""
    if symeq is not None:
        s += "#\nloop_\n_symmetry_equiv.id\n_symmetry_equiv.pos_as_xyz\n" + "".join(f"{i} {e}\n" for i, e in symeq)
    if sgop is not None:
        s += "#\nloop_\n_space_group_symop.id\n_space_group_symop.operation_xyz\n" + "".join(f"{i} {e}\n" for i, e in sgop)
    return s
def make(rows, symeq=None, sgop=None, extra_cols=()):
    return HEAD + conn_loop(rows, extra_cols) + TAIL + tables(symeq, sgop)
STD = [("1", "x,y,z"), ("2", "-x,-y,z"), ("3", "-x,y,-z")]
