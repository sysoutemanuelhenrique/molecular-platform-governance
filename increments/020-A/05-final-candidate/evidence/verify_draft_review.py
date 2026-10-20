"""Bounded research probe, not production code or a checkpoint pytest run.

Usage: python verify_draft_review.py --raw-root DIR --output FILE
Requires an already installed RDKit 2026.03.6. Installs nothing.
Reads five fixed study RAWs and the installed Telex font; writes only the
requested evidence JSON outside the code repository.
"""
import argparse
import hashlib
import inspect
import io
import json
import platform
import re
from pathlib import Path
import xml.etree.ElementTree as ET

from rdkit import Chem, RDConfig, rdBase
from rdkit.Chem import Descriptors, rdDepictor, rdMolDescriptors
from rdkit.Chem.Draw import rdMolDraw2D


def sha(data):
    return hashlib.sha256(data).hexdigest()


def render(mol, font, complete):
    work = Chem.Mol(mol)
    params = dict(canonOrient=True, clearConfs=True, nFlipsPerSample=0,
                  nSample=0, sampleSeed=0, permuteDeg4Nodes=False,
                  forceRDKit=True, useRingTemplates=False)
    if complete:
        params.update(coordMap={}, bondLength=-1.0)
    rdDepictor.Compute2DCoords(work, **params)
    prepared = rdMolDraw2D.PrepareMolForDrawing(
        work, kekulize=False, addChiralHs=False, wedgeBonds=True,
        forceCoords=False, wavyBonds=False)
    if complete:
        drawer = rdMolDraw2D.MolDraw2DSVG(
            600, 400, panelWidth=-1, panelHeight=-1, noFreetype=False)
    else:
        drawer = rdMolDraw2D.MolDraw2DSVG(600, 400)
    options = drawer.drawOptions()
    for name, value in dict(prepareMolsBeforeDrawing=False,
                            includeMetadata=False, includeAtomTags=False,
                            addAtomIndices=False, addBondIndices=False).items():
        setattr(options, name, value)
    options.fontFile = str(font)
    if complete:
        drawer.DrawMolecule(prepared, legend="")
    else:
        drawer.DrawMolecule(prepared)
    drawer.FinishDrawing()
    return drawer.GetDrawingText()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-root", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    assert rdBase.rdkitVersion == "2026.03.6", rdBase.rdkitVersion
    font = Path(RDConfig.RDDataDir) / "Fonts" / "Telex-Regular.ttf"
    font_data = font.read_bytes()
    options = rdMolDraw2D.MolDraw2DSVG(600, 400).drawOptions()
    option_names = ["prepareMolsBeforeDrawing", "includeMetadata",
                    "includeAtomTags", "addAtomIndices", "addBondIndices",
                    "fontFile"]
    functions = dict(
        Compute2DCoords=rdDepictor.Compute2DCoords,
        MolDraw2DSVG_constructor=rdMolDraw2D.MolDraw2DSVG.__init__,
        PrepareMolForDrawing=rdMolDraw2D.PrepareMolForDrawing,
        DrawMolecule=rdMolDraw2D.MolDraw2DSVG.DrawMolecule,
        CalcMolFormula=rdMolDescriptors.CalcMolFormula,
        CalcExactMolWt=rdMolDescriptors.CalcExactMolWt,
        CalcNumRotatableBonds=rdMolDescriptors.CalcNumRotatableBonds,
        CalcTPSA=rdMolDescriptors.CalcTPSA,
        CalcCrippenDescriptors=rdMolDescriptors.CalcCrippenDescriptors,
        MolWt=Descriptors.MolWt,
        private_CalcMolWt_for_source_evidence_only=rdMolDescriptors._CalcMolWt,
    )
    evidence = dict(
        nature="research probe; not production readers/service/CLI or pytest",
        python_version=platform.python_version(), platform=platform.platform(),
        rdkit_version=rdBase.rdkitVersion,
        docstrings={name: fn.__doc__ for name, fn in functions.items()},
        draw_option_defaults={name: getattr(options, name) for name in option_names},
        molwt_python_source=inspect.getsource(Descriptors.MolWt),
        font=dict(name=font.name, size_bytes=len(font_data), sha256=sha(font_data)),
    )
    assert "usePathAngleExpansion" not in rdDepictor.Compute2DCoords.__doc__
    try:
        rdDepictor.Compute2DCoords(Chem.MolFromSmiles("CCO"), usePathAngleExpansion=True)
    except Exception as exc:
        evidence["unsupported_kwarg_probe"] = dict(
            kwarg="usePathAngleExpansion", exception_type=type(exc).__name__,
            message=str(exc), rejected=True)
    else:
        raise AssertionError("Unexpected API surface for the pinned version")
    cases = []
    for name, cid in [("caffeine", 2519), ("rosmarinic-acid", 5281792),
                      ("imidacloprid", 86287518), ("diclofenac", 3033),
                      ("atrazine", 2256)]:
        relative = Path(name + "-pubchem") / f"pubchem_cid_{cid}_2d.sdf"
        raw = (args.raw_root / relative).read_bytes()
        molecules = list(Chem.ForwardSDMolSupplier(
            io.BytesIO(raw), sanitize=True, removeHs=False, strictParsing=True))
        assert len(molecules) == 1 and molecules[0] is not None
        mol = molecules[0]
        first = render(mol, font, False)
        second = render(mol, font, True)
        assert first == second, name
        cases.append(dict(name=name, cid=cid, raw_path=str(relative),
                          raw_sha256=sha(raw), svg_sha256=sha(second.encode()),
                          old_and_explicit_parameters_svg_identical=True))
        if name == "caffeine":
            values = dict(
                formula=rdMolDescriptors.CalcMolFormula(mol, separateIsotopes=True,
                                                       abbreviateHIsotopes=False),
                molar_mass_g_mol=Descriptors.MolWt(mol),
                exact_mass_da=rdMolDescriptors.CalcExactMolWt(mol, onlyHeavy=False),
                formal_charge_e=Chem.GetFormalCharge(mol),
                heavy_atom_count=mol.GetNumHeavyAtoms(),
                hbd_count=rdMolDescriptors.CalcNumHBD(mol),
                hba_count=rdMolDescriptors.CalcNumHBA(mol),
                rotatable_bond_count=rdMolDescriptors.CalcNumRotatableBonds(
                    mol, strict=rdMolDescriptors.NumRotatableBondsOptions.Strict),
                tpsa_a2=rdMolDescriptors.CalcTPSA(mol, force=True, includeSandP=False),
                clogp_wildman_crippen=rdMolDescriptors.CalcCrippenDescriptors(
                    mol, includeHs=True, force=True)[0],
            )
            expected = dict(formula="C8H10N4O2", molar_mass_g_mol=194.194,
                            exact_mass_da=194.08037556, formal_charge_e=0,
                            heavy_atom_count=14, hbd_count=0, hba_count=3,
                            rotatable_bond_count=0, tpsa_a2=61.82,
                            clogp_wildman_crippen=-1.0293)
            for key, value in expected.items():
                if isinstance(value, float):
                    assert abs(values[key] - value) <= 1e-8, (key, values[key])
                else:
                    assert values[key] == value, (key, values[key])
            evidence["caffeine_reference"] = dict(
                raw_sha256=sha(raw), values=values, comparison_abs_tol=1e-8,
                reference_matches=True)
    evidence["five_raw_cases"] = cases
    smiles = "c1ccc2cc3ccccc3cc2c1"
    mol = Chem.MolFromSmiles(smiles)
    assert mol is not None
    svg = render(mol, font, True)
    # This trusted-producer research inspection does not implement or prove
    # the proposed Expat validator. No external SVG is parsed here.
    root = ET.fromstring(svg)
    commands = set()
    for node in root.iter():
        if node.tag == "{http://www.w3.org/2000/svg}path":
            commands.update(re.findall(r"[A-DF-Za-df-z]", node.get("d", "")))
    assert commands <= {"M", "L", "Q"}, commands
    evidence["fused_aromatic_canary"] = dict(
        molecule="anthracene", smiles=smiles,
        formula=rdMolDescriptors.CalcMolFormula(mol),
        path_commands=sorted(commands), svg_sha256=sha(svg.encode()),
        commands_within_proposed_subset=True,
        windows_production_validator_test=False,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(evidence, indent=2, ensure_ascii=False) + "\n",
                           encoding="utf-8")
    print(json.dumps({"rdkit": rdBase.rdkitVersion,
                      "unsupported_kwarg_rejected": True,
                      "five_drawing_comparisons_passed": len(cases),
                      "caffeine_reference_matches": True,
                      "canary_commands": sorted(commands)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
