# Fechamento focal — Candidate1, Incremento 020-A

Tarefa: `020-A-CANDIDATE1-CLOSURE`. Revisor: Claude, papel de revisor independente (não implementador). Data: 20/10/2026.

Natureza: fechamento focal das três correções e das seis NOTES do parecer sobre o draft1. Não é revisão integral, não repete A-01–A-14/C-01–C-03 nem os 80 cenários, não aprova implementação e não congela especificação. Um parecer favorável não é aprovação do responsável.

## 1. Entradas e identidade

Governance: `sysoutemanuelhenrique/molecular-platform-governance`, ref `docs/020-a-candidate1-review-20261020`, snapshot observado **99b181e22663ed53341f131abe26222c41c43795** (igual ao informado no comando de entrada). `main` do governance observada em `a47183dfec8213c765ed43ae482c8c227760a3d5`, não alterada. Arquivos lidos diretamente do objeto Git do snapshot, sem checkout da branch do arquiteto.

Os 21 arquivos do `FILE_IDENTITIES.json` raiz foram conferidos por SHA-256 e tamanho em bytes: **21/21 coincidem**. A contagem de linhas também coincide em 19/21. As duas cópias de `CLAUDE_DRAFT_REVIEW_ORIGINAL.txt` (em `04-draft-review/` e `05-final-candidate/prior/`) têm 125 caracteres `\n`, porque a última das 126 linhas não termina em quebra. Hash e tamanho coincidem, então isso não é divergência de identidade.

| Input da tarefa | SHA-256 esperado | Observado |
|---|---|---|
| `05-final-candidate/INCREMENT_020_A_FINAL_SPECIFICATION_CANDIDATE.md` | 123596d03947f89321e6e623e3f0e7a2b88f38de42cd510a59f31cfd16d67ad4 | coincide; 70.346 bytes; 575 linhas |
| `05-final-candidate/INCREMENT_020_A_DRAFT_REVIEW_RESPONSE.md` | b545b965552e858f080285dc22148c38f4728a160ca061808593a5dc34229d9a | coincide; 11.494 bytes |
| `04-draft-review/CLAUDE_DRAFT_REVIEW_ORIGINAL.txt` | f2215080d4dc091db31cf4c7583ab915918da382388058700e1a0b17e2e56a8b | coincide; 20.981 bytes; CRLF preservado |
| `03-draft/INCREMENT_020_A_DRAFT_SPECIFICATION.md` | b0c8532282ac90cf41c9958b8af06ef3aea142777794af6b058e3ba558c6397d | coincide; 62.532 bytes; idêntico byte a byte à cópia em `prior/` |
| `tasks/020-A-CANDIDATE1-CLOSURE.json` | a63d1aa0ef0eac25f58971d3827b2f399643bffde72cafbe5dd9f3a887101aca | coincide |

Integridade do diff: aplicar `changes/draft1-to-candidate1.diff` (SHA-256 75ef41f0…789a) sobre o draft1 reproduz a candidate1 **byte a byte**. Por comparação independente das seções, as seções 3, 4, 5, 7, 12, 13, 14, 15, 18 e 20 são idênticas ao draft1, o que coincide com `evidence/document-validation.json`. As seções alteradas são 1, 2, 6, 8, 9, 10, 11, 16, 17, 19, 21 e 22, todas dentro do escopo declarado na resposta do arquiteto, §7. Restam 22 seções numeradas e 80 identificadores únicos, de T-020A-001 a T-020A-080. A §18 (allowlist) permanece byte-idêntica.

## 2. Execução e limites deste revisor

Executado nesta sessão: sonda própria, escrita por este revisor e independente do `verify_draft_review.py`, que não foi executado. Ambiente: venv isolada no scratchpad da sessão, fora de qualquer repositório, com **RDKit 2026.03.6** instalado de PyPI, **Python 3.13.16**, Linux x86_64. Identidades da sonda: script SHA-256 465b3dd9bfba492077ebe0de348ef93562f7adbedc65e653216f5abcec28653f; saída SHA-256 5f93d49082e8dc77ad2c3746d7ea784cab34cdce7aae79090d0acc5e368e7d24. O script consta do Apêndice A, e esses arquivos não foram publicados.

Limites:

- Python 3.13.16, e não o 3.12.14 do estudo. As assinaturas expostas pelo binding são as mesmas da evidência do arquiteto, mas o ambiente não é idêntico.
- Os cinco compostos foram construídos a partir de SMILES escritos por este revisor, não dos RAWs SDF do estudo. Os ZIPs internos de `context/` não foram extraídos. Os hashes de SVG, portanto, não são comparáveis aos da evidência; comparei apenas a identidade antes/depois dentro do meu ambiente.
- Somente Linux. Nenhum leitor, serviço, CLI, DTO ou validador SVG de produção existe ou foi executado. Não rodei pytest.
- O repositório de código `molecular-platform` não está no escopo desta sessão e não foi lido. A tarefa permite essa limitação ("read-only if needed; declare limitations"), e o fechamento focal é documental.

## 3. MINOR-1 — superfícies construtor / MolDrawOptions / DrawMolecule e DTO

**Encerrado.**

- A §9 agora separa seis linhas: Compute2DCoords; PrepareMolForDrawing; construtor `MolDraw2DSVG(width=600, height=400, panelWidth=-1, panelHeight=-1, noFreetype=False)`; atribuições em `drawer.drawOptions()`; `fontFile`; e `DrawMolecule(mol, legend="")`. A ordem construir → configurar → DrawMolecule → finalizar → obter SVG está explícita, assim como a proibição de passar atributos de opções ou `legend` como kwargs do construtor.
- Verificação independente no pin: `MolDraw2DSVG(600, 400, includeMetadata=False)` e `MolDraw2DSVG(600, 400, legend="")` são **recusados com ArgumentError**; o construtor com os cinco parâmetros reais é aceito. A docstring de `DrawMolecule` mostra `legend=''` como kwarg do método. O defeito apontado no draft1 era real e a nova redação o corrige.
- §11, DTO: `effective_parameters` de `drawing` passou de "todos os parâmetros da §9" para seis blocos fechados (`compute2d`, `prepare`, `drawer`, `draw_options`, `draw_molecule`, `svg_validation_profile`), cada um frozen/extra=forbid, que espelham exatamente as superfícies da §9. Isso elimina a propagação do erro ao JSON público apontada no parecer. `fontFile` é representado por `font_policy`, e a identidade efetiva fica em `font_name`/`font_sha256_observed`, sem serializar caminho absoluto. Essa decisão é coerente e não deixa lacuna.

## 4. MINOR-2 — defaults versus desvios

**Encerrado.**

As tabelas da §8 e da §9 ganharam uma coluna "Default Python do pin versus escolha". Conferi cada célula contra as docstrings do binding 2026.03.6 nesta sessão:

| Item | Defaults observados | Rotulagem na candidata |
|---|---|---|
| CalcMolFormula | separateIsotopes=False, abbreviateHIsotopes=True | ambos desvios — correto |
| CalcExactMolWt | onlyHeavy=False | coincide — correto |
| MolWt | wrapper `lambda` → `_CalcMolWt(onlyHeavy=False)` | sem kwargs; helper privado não autorizado — correto |
| CalcNumRotatableBonds | overload enum, default `NumRotatableBondsOptions.Default` | Strict como seleção explícita, sem alegar resultado diferente — correto |
| CalcTPSA | force=False, includeSandP=False | force desvio, S/P coincide — correto |
| CalcCrippenDescriptors | includeHs=True, force=False | includeHs coincide, force desvio — correto |
| Compute2DCoords | todos os 10 conforme a candidata; forceRDKit=False | só forceRDKit é desvio — correto |
| PrepareMolForDrawing | kekulize=True, addChiralHs=True, wedgeBonds=True, forceCoords=False, wavyBonds=False | kekulize/addChiralHs desvios; os outros três coincidem — correto |
| MolDraw2DSVG | panelWidth=-1, panelHeight=-1, noFreetype=False | coincidem — correto |
| drawOptions (objeto real) | prepareMolsBeforeDrawing=True, includeMetadata=True, demais False, fontFile="" | dois desvios mais o desvio de fontFile — correto |

Valores selecionados idênticos ao draft1; nenhuma política científica foi alterada. A prosa da docstring de `CalcNumRotatableBonds` chama Strict de "(default)", mas a assinatura do overload enum usa Default. A redação cautelosa da candidata ("seleção explícita, sem afirmar resultado diferente de Default") é a correta diante dessa inconsistência interna do upstream.

## 5. MINOR-3 — coordMap/bondLength e usePathAngleExpansion

**Encerrado, com correção da premissa do meu parecer anterior.**

- `coordMap={}` e `bondLength=-1.0` agora estão fixados na §9 e no bloco `compute2d` da §11. A exigência de "mapa vazio novo por chamada" é pertinente: a assinatura C++ mostra `boost::python::dict {lvalue} coordMap={}`, um default compartilhado. O DTO fecha `coordMap` como objeto vazio sem campos, e `bondLength=-1.0` fica descrito como política padrão, não como distância física. Chamada explícita com ambos aceita no pin.
- **Verificação independente de usePathAngleExpansion no binding 2026.03.6:**
  - A primeira linha da docstring expõe exatamente 10 kwargs nomeados, em ordem: canonOrient, clearConfs, coordMap, nFlipsPerSample, nSample, sampleSeed, permuteDeg4Nodes, bondLength, forceRDKit, useRingTemplates. A docstring inteira não contém `usePathAngleExpansion`.
  - `Compute2DCoords(mol, usePathAngleExpansion=True)` e `=False` são ambos **recusados com ArgumentError** (`Python argument types in rdkit.Chem.rdDepictor.Compute2DCoords(Mol) did not match C++ signature`).
  - Esses resultados coincidem com `evidence/draft-review-verification.json`, cuja mensagem de erro preservada enumera a mesma assinatura C++ de 11 parâmetros (mol mais 10). O registro do arquiteto está correto. Não o aceitei por autoridade: reproduzi o resultado em instalação independente, por dois canais (introspecção e despacho real).
- O meu parecer do draft1 listou `usePathAngleExpansion=True` como kwarg da função com base na documentação web, cuja versão eu não consegui casar com o pin. A premissa estava errada para 2026.03.6. A disposição da candidata é a correta: não passar o kwarg, não declará-lo em `effective_parameters`, recusar o campo no DTO e não usar fallback por tentativa/erro. Não verifiquei de forma independente a afirmação de que o nome aparece na documentação 2026.09.1; ela é irrelevante para o contrato pinado e não altera esta conclusão.
- Regressão de desenho: nos cinco compostos e no antraceno, construídos por SMILES, o SVG com os parâmetros recém-explicitados (coordMap, bondLength, opcionais do construtor, `legend=""`) é **byte-idêntico** ao SVG sem eles, no mesmo ambiente: 6/6. Isso confirma que explicitar os parâmetros não mudou o comportamento no pin.

## 6. Disposição das NOTES

| NOTE | Disposição na candidata | Fechamento |
|---|---|---|
| NOTE-1 — Windows 11 | §6 registra a pergunta e exige fonte/API, critério de build justificado e testes positivos/negativos no checkpoint2, sem aprovar limiar universal | Aceita. A prova fica corretamente no checkpoint2; não exijo leitores agora |
| NOTE-2 — Descriptors.MolWt | §8 justifica a API pública e registra que o wrapper encaminha a `_CalcMolWt`, que não fica autorizado ao adaptador. Confirmei o source `lambda` e o default `onlyHeavy=False` | Aceita |
| NOTE-3 — canário fundido | Antraceno (`c1ccc2cc3ccccc3cc2c1`) incluído em §10.1 e T-020A-051, com evidência Windows exigida e gramática não ampliada. Reproduzi a observação: só M/L no antraceno (M/L/Q nos outros cinco), dentro do perfil | Aceita |
| NOTE-4 — grafia de versão | Encerrada no parecer original | Sem ação |
| NOTE-5 — vetor cafeína | Agora executei: fórmula C8H10N4O2, MolWt 194.194, exata 194.08037556, carga 0, pesados 14, HBD 0, HBA 3, rotacionáveis (Strict) 0, TPSA 61.82, cLogP −1.0293. Os quatro floats ficam dentro de 1e−8 do vetor da §17, a partir de SMILES e não do RAW | Encerrada quanto ao limite deste revisor. T-020A-041 de produção continua exigido |
| NOTE-6 — confirmações positivas | Preservadas; a correção de usePathAngleExpansion não reabre A-01–A-14/C-01–C-03 | Aceita |

Fonte Telex no meu ambiente: 38.940 bytes, SHA-256 eeaa2d17d105b6b46e5368ecd990f5b19c50131ff922dbf79bfb9bb45c249871, igual à §9. Continua sendo evidência Linux, como a própria candidata ressalva.

## 7. Regressões concretas

Nenhuma encontrada. As alterações ficaram restritas a tabelas, texto e status nas seções mapeadas no §1 deste parecer. Arquitetura, valores científicos, parsing, gramática SVG, limites, taxonomia, CLI, allowlist e numeração de cenários estão preservados. Os originais estão preservados byte a byte.

## 8. Contagem

**BLOCKERS: 0 / MAJORS: 0 / MINORS: 0 / NOTES: 2**

**NOTE-A (editorial, opcional, não bloqueante):** a linha de `DrawMolecule` declara "nenhum highlight fornecido", mas não menciona `confId`, cujo default é −1. Como `clearConfs=True` deixa um único conformer na cópia de desenho, o default é inequívoco e não muda o resultado. Se o responsável quiser simetria total com a disciplina do MINOR-2, basta acrescentar "confId não fornecido (default −1)" em uma futura revisão. Não condiciona o congelamento.

**NOTE-B (processo):** a tarefa sugere a branch `claude/020-a-candidate1-closure`. Este parecer foi publicado na branch `claude/lucid-faraday-xy632t`, a única autorizada pelo ambiente desta sessão e indicada pelo responsável no comando de entrada. A branch preserva o commit do teste de conexão `befdc444fe015286b1508b60c107c7e9f5c23dd3`.

## 9. Parecer

MINOR-1, MINOR-2 e MINOR-3 do draft1 estão encerrados. As seis NOTES têm disposição adequada, e nenhuma regressão concreta foi encontrada. A correção sobre `usePathAngleExpansion` está fundamentada em evidência primária do binding pinado e foi reproduzida independentemente.

A candidate1, identificada pelo SHA-256 123596d03947f89321e6e623e3f0e7a2b88f38de42cd510a59f31cfd16d67ad4, pode ser apresentada ao responsável para decisão explícita de aprovação/congelamento. Este parecer não é essa decisão.

MINOR-1 CLOSED: YES
MINOR-2 CLOSED: YES
MINOR-3 CLOSED: YES — pinned-API correction verified independently
NOTES DISPOSITION ACCEPTED: YES
CONCRETE REGRESSION FOUND: NO
INPUT IDENTITIES VERIFIED: YES
INDEPENDENT CLOSURE BY THIS REVIEWER: YES
READY FOR OWNER FREEZE DECISION: YES
READY FOR IMPLEMENTATION: NO
FINAL SPECIFICATION FROZEN: NO
IMPLEMENTATION AUTHORIZED: NO
WINDOWS PRODUCTION READERS VALIDATED: NO — required at checkpoint2
CODE REPOSITORY READ OR MODIFIED: NO
ORIGINALS OR CENTRAL STATUS/TASKS MODIFIED: NO
AUTOMATED RELAY ACTIVE: NO

## Apêndice A — sonda independente deste revisor

SHA-256 465b3dd9bfba492077ebe0de348ef93562f7adbedc65e653216f5abcec28653f; executada com `python -I` numa venv isolada, fora de qualquer repositório. Pesquisa, não código de produção.

```python
import hashlib, json, re, sys, platform
from pathlib import Path
from rdkit import Chem, RDConfig, rdBase
from rdkit.Chem import Descriptors, rdDepictor, rdMolDescriptors
from rdkit.Chem.Draw import rdMolDraw2D
out = {"python": platform.python_version(), "platform": platform.platform(), "rdkit": rdBase.rdkitVersion}
doc = rdDepictor.Compute2DCoords.__doc__
sig = doc.strip().splitlines()[0]
out["compute2d_kwargs"] = re.findall(r"\(\w+\)(\w+)=", sig)
out["compute2d_doc_has_usePathAngleExpansion"] = "usePathAngleExpansion" in doc
def tryit(fn):
    try: fn(); return "accepted"
    except Exception as e: return type(e).__name__ + ": " + str(e).splitlines()[0]
m = Chem.MolFromSmiles("CCO")
out["usePathAngleExpansion_True"] = tryit(lambda: rdDepictor.Compute2DCoords(Chem.Mol(m), usePathAngleExpansion=True))
out["usePathAngleExpansion_False"] = tryit(lambda: rdDepictor.Compute2DCoords(Chem.Mol(m), usePathAngleExpansion=False))
out["compute2d_explicit_coordMap_bondLength"] = tryit(lambda: rdDepictor.Compute2DCoords(Chem.Mol(m), coordMap={}, bondLength=-1.0))
out["ctor_with_option_kwarg"] = tryit(lambda: rdMolDraw2D.MolDraw2DSVG(600, 400, includeMetadata=False))
out["ctor_with_legend_kwarg"] = tryit(lambda: rdMolDraw2D.MolDraw2DSVG(600, 400, legend=""))
out["ctor_full_kwargs"] = tryit(lambda: rdMolDraw2D.MolDraw2DSVG(600, 400, panelWidth=-1, panelHeight=-1, noFreetype=False))
o = rdMolDraw2D.MolDraw2DSVG(600, 400).drawOptions()
out["draw_option_defaults"] = {k: getattr(o, k) for k in ["prepareMolsBeforeDrawing","includeMetadata","includeAtomTags","addAtomIndices","addBondIndices","fontFile"]}
out["signatures"] = {n: f.__doc__.strip().splitlines()[0] for n, f in dict(
    PrepareMolForDrawing=rdMolDraw2D.PrepareMolForDrawing, CalcMolFormula=rdMolDescriptors.CalcMolFormula,
    CalcExactMolWt=rdMolDescriptors.CalcExactMolWt, CalcTPSA=rdMolDescriptors.CalcTPSA,
    CalcCrippenDescriptors=rdMolDescriptors.CalcCrippenDescriptors, ctor=rdMolDraw2D.MolDraw2DSVG.__init__).items()}
out["rotb_signatures"] = [l.strip() for l in rdMolDescriptors.CalcNumRotatableBonds.__doc__.splitlines() if l.strip().startswith("CalcNumRotatableBonds(")]
font = Path(RDConfig.RDDataDir) / "Fonts" / "Telex-Regular.ttf"
fb = font.read_bytes(); out["font"] = {"size": len(fb), "sha256": hashlib.sha256(fb).hexdigest()}
def render(mol, complete):
    w = Chem.Mol(mol)
    p = dict(canonOrient=True, clearConfs=True, nFlipsPerSample=0, nSample=0, sampleSeed=0, permuteDeg4Nodes=False, forceRDKit=True, useRingTemplates=False)
    if complete: p.update(coordMap={}, bondLength=-1.0)
    rdDepictor.Compute2DCoords(w, **p)
    pr = rdMolDraw2D.PrepareMolForDrawing(w, kekulize=False, addChiralHs=False, wedgeBonds=True, forceCoords=False, wavyBonds=False)
    d = rdMolDraw2D.MolDraw2DSVG(600, 400, panelWidth=-1, panelHeight=-1, noFreetype=False) if complete else rdMolDraw2D.MolDraw2DSVG(600, 400)
    op = d.drawOptions()
    for k in ["prepareMolsBeforeDrawing","includeMetadata","includeAtomTags","addAtomIndices","addBondIndices"]: setattr(op, k, False)
    op.fontFile = str(font)
    d.DrawMolecule(pr, legend="") if complete else d.DrawMolecule(pr)
    d.FinishDrawing(); return d.GetDrawingText()
smi = {"caffeine":"Cn1cnc2c1c(=O)n(C)c(=O)n2C",
 "rosmarinic-acid":"O=C(O)[C@@H](Cc1ccc(O)c(O)c1)OC(=O)/C=C/c1ccc(O)c(O)c1",
 "imidacloprid":"O=[N+]([O-])/N=C1/NCCN1Cc1ccc(Cl)nc1",
 "diclofenac":"OC(=O)Cc1ccccc1Nc1c(Cl)cccc1Cl",
 "atrazine":"CCNc1nc(Cl)nc(NC(C)C)n1",
 "anthracene":"c1ccc2cc3ccccc3cc2c1"}
out["svg_old_vs_explicit_identical"] = {}; out["path_commands"] = {}
for n, s in smi.items():
    mol = Chem.MolFromSmiles(s); a, b = render(mol, False), render(mol, True)
    out["svg_old_vs_explicit_identical"][n] = a == b
    out["path_commands"][n] = sorted(set(c for d_ in re.findall(r' d=.([^\'"]*)', b) for c in re.findall(r"[A-DF-Za-df-z]", d_)))
    out.setdefault("has_metadata_element", {})[n] = "<metadata" in b
caf = Chem.MolFromSmiles(smi["caffeine"])
out["caffeine"] = dict(formula=rdMolDescriptors.CalcMolFormula(caf, separateIsotopes=True, abbreviateHIsotopes=False),
  molwt=Descriptors.MolWt(caf), exact=rdMolDescriptors.CalcExactMolWt(caf, onlyHeavy=False), charge=Chem.GetFormalCharge(caf),
  heavy=caf.GetNumHeavyAtoms(), hbd=rdMolDescriptors.CalcNumHBD(caf), hba=rdMolDescriptors.CalcNumHBA(caf),
  rotb_strict=rdMolDescriptors.CalcNumRotatableBonds(caf, strict=rdMolDescriptors.NumRotatableBondsOptions.Strict),
  tpsa=rdMolDescriptors.CalcTPSA(caf, force=True, includeSandP=False),
  clogp=rdMolDescriptors.CalcCrippenDescriptors(caf, includeHs=True, force=True)[0])
exp = dict(molwt=194.194, exact=194.08037556, tpsa=61.82, clogp=-1.0293)
out["caffeine_float_within_1e-8"] = {k: abs(out["caffeine"][k]-v) <= 1e-8 for k, v in exp.items()}
print(json.dumps(out, indent=1, ensure_ascii=False))
```
