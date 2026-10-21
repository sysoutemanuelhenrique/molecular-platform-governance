# Checkpoint 1 corrections report — Increment 020-A

Autor: Claude (Sonnet 5), sessão implementadora separada da revisão. Data: 2026-10-21.
Natureza: relatório de execução real da correção focal dos quatro achados da revisão
adversarial independente do Checkpoint 1, conforme autorização registrada em
`tasks/020-A-CHECKPOINT1-CORRECTIONS.json` (status `AUTHORIZED`,
`authorization_scope="CHECKPOINT_1_CORRECTIONS_ONLY"`). Não é revisão independente;
aguarda reverificação independente focal antes de qualquer liberação do Checkpoint 2.
Este relatório não substitui nem edita `increments/020-A/09-checkpoint-1/
CLAUDE_CHECKPOINT1_IMPLEMENTATION_REPORT.md`, o parecer adversarial original, a
evidência original ou a reconciliação do arquiteto.

## 1. Identidade e autorização confirmadas antes da correção

Lido integralmente, byte a byte, no snapshot de governance
`0db9b5af2b3f7cd00a8de70b6685114cbe604450` (branch
`docs/020-a-candidate1-review-20261020`), antes de qualquer alteração de código:

| Item | SHA-256 esperado | Observado | Linhas/bytes |
|---|---|---|---|
| `AGENTS.md`, `CLAUDE.md`, `STATUS.md` | — (lidos integralmente) | idênticos | — |
| `tasks/020-A-CHECKPOINT1-CORRECTIONS.json` | — (lido integralmente) | `status="AUTHORIZED"` confirmado | — |
| Especificação final congelada | `cfbc6ea4bbb58f987deb3f73e45fc39d5b79d0cfaa2de8e0a7870a9937386e9c` | idêntico | 586/71.904 |
| `CLAUDE_CHECKPOINT1_ADVERSARIAL_REVIEW.md` | `72d658ad6184a2411d9cb56dbbb3b49861ccd64621126cdb5d62aa7b048f4399` | idêntico | 153/24.918 |
| `evidence/claude-dto-coercion-reproduction.json` | `8d24af595759154d6c798c11a2afcc44a5c5469faf80abe4bff14f6434540cea` | idêntico | 54/2.183 |
| `INCREMENT_020_A_CP1_REVIEW_RECONCILIATION.md` | `20f1705e92e7d60d24ac61b699dcd0c91fbdfd555c01ff04506f1b628009392c` | idêntico | — |

Todos os quatro hashes acima foram recalculados localmente (`git show
<commit>:<path> \| sha256sum`) sobre o blob lido do snapshot pinado, não aceitos por
afirmação. A especificação congelada foi reconfirmada inalterada (mesmo commit
`665fb8b9cb4e1c7e0d0b9f1db98ec2adaa63bfed`, mesmo hash da etapa anterior — nenhuma
releitura de estudo foi refeita). Também foram lidos integralmente, como pesquisa de
apoio (não pytest, não aprovação de produção): `evidence/
architect-strict-literal-api-probe.json`, `evidence/
architect-synthetic-v3000-roundtrip-probe.json` e as três fixtures sintéticas V3000
(`architect-sgroup-synthetic-v3000.sdf`, `architect-and-synthetic-v3000.sdf`,
`architect-or-synthetic-v3000.sdf`).

A revisão adversarial original (0 BLOCKERS / 2 MAJORS / 2 MINORS / 5 NOTES, REQUEST
CHANGES) e a reconciliação do arquiteto não foram refeitas nem contestadas — os
quatro achados aceitos (MAJOR-1, MAJOR-2, MINOR-1, MINOR-2) foram corrigidos
exatamente como disposto; as cinco NOTES foram aceitas sem mudança (NOTE-1: gramática
SVG `d` permanece M/L/Q com recusa de `Z`; NOTE-2: localização do validador SVG
mantida em `characterization.py`; NOTE-3: errata registrada na Seção 6 abaixo;
NOTE-4/NOTE-5: sem ação de código).

## 2. Repositório de código — preflight

- Remoto confirmado: `https://github.com/sysoutemanuelhenrique/molecular-platform.git`.
- `HEAD` inicial do worktree isolado: **`f8416b845efe93f9e47deca97f01a355e4e679ba`** —
  idêntico ao exigido pela tarefa (`expected_code_head_before_correction`). Confirmado
  por `git rev-parse HEAD` antes de qualquer edição.
- `origin/main`: **`08b797e0985e123ffd4d7ca7e5a5e8f040e63851`** — idêntico à baseline
  exigida; reconfirmado por `git fetch origin main` + `git rev-parse` tanto antes
  quanto depois da correção.
- `origin/feature/increment-020-a-molecular-characterization` antes do push desta
  sessão: `f8416b845efe93f9e47deca97f01a355e4e679ba` — idêntico ao HEAD local,
  nenhuma divergência.
- Worktree isolado reaproveitado desta mesma linha de trabalho
  (`C:\Users\Pichau\molecular-platform-020a-cp1`), preservando sem alteração o
  checkout original do usuário (`C:\Users\Pichau\molecular-platform`) e seus
  untracked (`_figura_curcumina/`, `increment-009-review.txt`, e um novo `Claude
  outputs/` observado nesta rodada — nenhum dos três foi tocado, lido para conteúdo,
  nem referenciado por este trabalho). Nenhuma divergência foi encontrada; a execução
  prosseguiu sem interrupção.

## 3. Escopo corrigido — exatamente dentro da allowlist de quatro arquivos

Nenhum ajuste de produção foi necessário em `src/molecular/rdkit_tautomer.py` nesta
rodada — os quatro achados foram corrigíveis inteiramente em
`src/molecular/characterization.py` (MAJOR-1) e nos dois arquivos de teste (MAJOR-2,
MINOR-1, MINOR-2). `src/molecular/rdkit_tautomer.py` permanece byte a byte idêntico
ao HEAD revisado `f8416b8` — confirmado por `git diff f8416b845e...
-- src/molecular/rdkit_tautomer.py` vazio.

| Caminho | Tocado nesta rodada | Inserções/remoções (vs. `f8416b8`) |
|---|---|---:|
| `src/molecular/characterization.py` | sim | +196 / −10 |
| `src/molecular/rdkit_tautomer.py` | **não** | 0 / 0 |
| `tests/test_characterization.py` | sim | +184 / −0 |
| `tests/test_rdkit_tautomer.py` | sim | +331 / −6 |

`git diff --stat f8416b845e...` (diff corretivo, esta rodada apenas): **3 files
changed, 711 insertions(+), 16 deletions(-)**. Nenhum caminho fora da allowlist foi
tocado; `increment-009-review.txt` e `_figura_curcumina/` não aparecem no diff.

### 3.1 Errata do relatório anterior (NOTE-3) — sem editar o relatório original

O relatório anterior (`increments/020-A/09-checkpoint-1/
CLAUDE_CHECKPOINT1_IMPLEMENTATION_REPORT.md`, preservado sem edição) registrou "+680
inserções, −1" para `src/molecular/rdkit_tautomer.py` na Seção 3. O parecer
adversarial (NOTE-3) e a reconciliação do arquiteto confirmam, de forma
independente, que o valor correto é **+679/−1**. Reconfirmado agora, nesta sessão,
por `git diff --numstat 08b797e0985e123ffd4d7ca7e5a5e8f040e63851
f8416b845efe93f9e47deca97f01a355e4e679ba -- src/molecular/rdkit_tautomer.py`:

```
679	1	src/molecular/rdkit_tautomer.py
```

O total do `git diff --stat` completo daquela etapa (`3094 insertions(+), 1
deletion(-)`) permanece correto — apenas a célula individual dessa linha da tabela
continha um erro de contagem de um. Este é registro de errata, não edição do
documento original.

## 4. Ambiente de validação desta rodada

```
Python: 3.11.9 (CPython, Windows, MSC v.1938 64 bit AMD64) — mesmo venv reaproveitado
rdkit (pip):      2026.3.6
rdkit.rdBase.rdkitVersion (observado em runtime): 2026.03.6
pydantic:         2.14.1
pytest:           9.1.1
SO: Windows-10-10.0.26200-SP0 (Windows 11 Pro, build 26200)
```

Mesmo venv do Checkpoint 1 original, reaproveitado e reverificado nesta rodada (RDKit
e pydantic reconfirmados pela execução real abaixo, não assumidos do relatório
anterior). Um segundo venv, deliberadamente sem o extra `rdkit`, foi reaproveitado
para reconfirmar a fronteira opcional após a correção.

RDKit real, não mock, executado localmente nesta sessão. Nenhuma sonda do arquiteto
(`architect-strict-literal-api-probe.json`,
`architect-synthetic-v3000-roundtrip-probe.json`) foi apresentada como execução
própria desta sessão — cada sonda referenciada abaixo é identificada como pesquisa de
apoio, e os valores de hash/bytes das fixtures V3000 foram **reproduzidos de forma
independente** pelo código desta correção (Seção 5.4), não copiados do JSON de
evidência.

## 5. Achado → correção → teste → resultado

### 5.1 MAJOR-1 — tipos não estritos nos DTOs/perfis

**Achado**: `ConfigDict(frozen=True, extra="forbid")` não rejeita strings numéricas,
floats integrais ou bool/int equivalentes em campos `int`/`float`/`Literal`.
Reproduzido de forma independente pelo revisor em Pydantic 2.13.5 (terceira versão
distinta), convergindo com a sonda do arquiteto em 2.14.0 e com o ambiente do
implementador em 2.14.1.

**Ressalva técnica da reconciliação, confirmada nesta sessão antes de corrigir**: a
sonda do arquiteto (`architect-strict-literal-api-probe.json`) mostrou que
`ConfigDict(strict=True)` no modelo **não** propaga estrictez para campos `Literal`
(ainda aceita `Literal[True]` com `1`, `Literal[0]` com `False`, `Literal[600]` com
`600.0`), e que `Field(strict=True)` aplicado a um campo `Literal` produz
`RuntimeError: Unable to apply constraint 'strict' to schema of type 'literal'` —
confirmado nesta sessão por reprodução direta antes de escrever a correção
definitiva (ver Seção 5.1.1 abaixo), não apenas aceito da sonda.

**Correção**: quatro funções auxiliares de módulo em `characterization.py`
(`_require_strict_bool`, `_require_strict_int`, `_require_numeric_not_bool_or_str`,
`_require_strict_float`), cada uma inspecionando `type(value)` diretamente, aplicadas
via `field_validator(..., mode="before")` — isto é, **antes** da coerção/igualdade
`Literal` do próprio pydantic, que é exatamente o ponto em que a estrictez do modelo
falhava. Aplicadas em `CharacterizationValues` (os dez campos científicos) e em todo
campo `Literal`/`int` booleano/inteiro/float pertinente de `SdfParserParameters`,
`SmilesParserParameters`, `FormulaParameters`, `ExactMassParameters`,
`TpsaParameters`, `CrippenParameters`, `Compute2DParameters`, `PrepareParameters`,
`DrawerConstructorParameters`, `DrawOptionsParameters`, `DrawingResult` e
`CharacterizationProvenance.representation_size_bytes`. Campos `Literal[str]` (por
exemplo `format="sdf"`) não receberam validador extra: nenhuma lacuna de coerção foi
demonstrada para eles (campos `str` simples já rejeitam `int`/`bytes` nativamente no
pydantic instalado, confirmado por sonda própria antes de decidir não tocá-los — ver
Seção 5.1.1). Nenhuma mudança de forma do JSON público, de nome de campo ou de regra
científica.

**Decisão de escopo explícita**: campos `float` (`molar_mass_g_mol`, `exact_mass_da`,
`tpsa_a2`, `clogp_wildman_crippen`) continuam aceitando um `int` nativo — a
reconciliação é explícita que a exigência é "floats sem strings/bool/não-finitos",
não uma proibição de `int`; não foi inventada uma regra mais restritiva do que a
contratada.

#### 5.1.1 Sonda própria antes de corrigir (não é execução de produção, é diagnóstico)

Executada nesta sessão, Python 3.11.9/Pydantic 2.14.1, contra o código exato do HEAD
revisado `f8416b8`, antes de qualquer edição — reproduzindo cada um dos cinco
exemplos exatos do JSON de evidência do revisor:

```
heavy_atom_count="3"      (str)   -> aceito, coagido para int 3
heavy_atom_count=3.0      (float) -> aceito, coagido para int 3
formal_charge_e="0"       (str)   -> aceito, coagido para int 0
molar_mass_g_mol="46.069" (str)   -> aceito, coagido para float 46.069
SdfParserParameters(sanitize=1) (int) -> aceito, coagido para bool True
```

Resultado: idêntico ao relatado pelo revisor e pelo arquiteto — quarta reprodução
independente (Python 3.11.9/Pydantic 2.14.1), em ambiente ligeiramente diferente dos
três anteriores (3.13.16/2.13.5 do revisor; 3.12.14/2.14.0 do arquiteto; 3.11.9/2.14.1
já citado como ambiente do implementador original). Script preservado em
`evidence/claude-major1-pre-fix-reproduction.py`, saída em
`evidence/claude-major1-pre-fix-reproduction.json` (ambos publicados nesta rodada, sob
o caminho autorizado de evidência).

#### 5.1.2 Testes (produção/teste → parâmetros → itens coletados → resultado)

| Função de teste | Arquivo:linha aproximada | Parametrização | Itens coletados | Resultado |
|---|---|---|---:|---|
| `test_int_fields_reject_numeric_strings_and_integral_floats` | `test_characterization.py` | 6 casos (`heavy_atom_count`/`formal_charge_e`/`hbd_count`/`hba_count`/`rotatable_bond_count` × string/float) | 6 | Todos rejeitados |
| `test_float_fields_reject_numeric_strings` | idem | 4 campos float × string | 4 | Todos rejeitados |
| `test_float_fields_still_accept_a_native_int` | idem | — | 1 | Aceito, coagido para float (preserva valor nativo válido) |
| `test_sdf_parser_parameters_literal_bool_rejects_int_one` | idem | reprodução exata do exibit do revisor | 1 | Rejeitado |
| `test_literal_bool_fields_reject_int_zero_or_one` | idem | 19 combinações DTO×campo×0/1 em 9 classes | 19 | Todos rejeitados |
| `test_literal_int_fields_reject_bool_and_float_equivalents` | idem | 6 combinações | 6 | Todos rejeitados |
| `test_literal_float_field_rejects_int_and_bool_equivalents` | idem | `bond_length` × int/bool | 1 | Rejeitado (dois `pytest.raises` no mesmo teste) |
| `test_drawing_result_int_fields_reject_bool_float_and_str` | idem | 3 campos × 3 tipos indevidos | 3 | Todos rejeitados |
| `test_provenance_representation_size_bytes_rejects_bool_float_and_str` | idem | 3 tipos indevidos | 1 | Rejeitado (loop interno no mesmo teste) |
| `test_strict_fixes_preserve_valid_json_round_trip` | idem | — | 1 | JSON round-trip preservado para `CharacterizationValues`/`CharacterizationEffectiveParameters`/`DrawMoleculeParameters` |
| `test_all_default_profile_blocks_still_construct_with_no_arguments` | idem | — | 1 | Todos os doze blocos padrão continuam construindo sem argumento |

Total: 11 funções novas, **44 itens coletados** — reconciliado exatamente com
`pytest tests/test_characterization.py -q --collect-only` (155 itens totais após a
correção, 111 antes; 155−111=44) e com a contagem de funções (`grep -c "^def test_"`:
62 depois, 51 antes; 62−51=11).

### 5.2 MAJOR-2 — ausência de testes dedicados de KeyboardInterrupt/SystemExit por fase

**Achado**: nenhum teste dedicado injetava `KeyboardInterrupt`/`SystemExit` no
adaptador de caracterização, apesar de T-020A-076/077 exigirem isso explicitamente
para este checkpoint; a garantia estrutural (nenhum `except BaseException`, uso de
`with rdBase.BlockLogs()`) existia mas não era comprovada dinamicamente.

**Correção**: oito fases do adaptador foram mapeadas e cada uma recebeu uma injeção
que substitui exatamente **uma** chamada real de produção em seu ponto de uso — nunca
o adaptador inteiro por mock:

| Fase | Ponto de injeção real patcheado |
|---|---|
| Validação de entrada | `molecular.inputs.validate_input_id` (acessado via `rdkit_tautomer_module.validate_input_id`) |
| Parsing SDF (incluindo iteração) | `Chem.ForwardSDMolSupplier` retorna um iterável real cujo `__iter__` levanta a exceção — mesmo padrão já estabelecido no projeto para `SDMolSupplier` (`test_supplier_iteration_never_catches_keyboard_interrupt`), generalizado aqui para `ForwardSDMolSupplier` |
| Parsing SMILES | `Chem.MolFromSmiles` |
| Cálculo dos valores | `rdMolDescriptors.CalcTPSA` |
| Coordenadas/preparação do desenho | `rdDepictor.Compute2DCoords` |
| Renderização | `rdMolDraw2D.MolDraw2DSVG` (construtor) |
| Validação/vínculo do SVG | `characterization.validate_and_bind_depiction_svg` (acessado via `rdkit_tautomer_module.validate_and_bind_depiction_svg`) |
| Construção do resultado | `RDKitCharacterizationOutcome` (acessado via `rdkit_tautomer_module.RDKitCharacterizationOutcome`) |

Leitores/serviço/CLI (Checkpoint2/3) não foram incluídos — fora de escopo, como a
própria reconciliação instrui.

Cada uma das oito fases é exercitada **duas vezes**, por duas parametrizações
genuinamente separadas (`KeyboardInterrupt()` real e `SystemExit(42)` real,
funções de teste distintas) — nunca uma única parametrização genérica por "qualquer
exceção". Para cada caso: a mesma instância da exceção é comparada por identidade
(`excinfo.value is exc`), nenhuma ficha/resultado parcial é retornada (a própria
semântica de `pytest.raises` já exige isso), e para `SystemExit` o atributo `.code`
original é conferido.

#### 5.2.1 Testes

| Função de teste | Parametrização | Itens coletados | Resultado |
|---|---|---:|---|
| `test_keyboard_interrupt_propagates_unconverted_by_adapter_phase` | 8 fases | 8 | `KeyboardInterrupt` propaga, mesma instância, em todas as 8 fases |
| `test_system_exit_propagates_unconverted_by_adapter_phase` | 8 fases | 8 | `SystemExit` propaga, mesma instância, `.code==42`, em todas as 8 fases |
| `test_adapter_never_raises_except_basexception_itself` | — (estático, AST) | 1 | Corrobora estaticamente a garantia estrutural (nenhum `except BaseException` em `rdkit_tautomer.py`) — não substitui os 16 testes dinâmicos acima, apenas os reforça |

Total: 2 funções dinâmicas + 1 estática, **17 itens coletados**.

### 5.3 MINOR-1 — prova de restauração de log não seguia o padrão já estabelecido

**Achado**: o teste existente usava uma segunda chamada bem-sucedida como prova
indireta de restauração, em vez do padrão de marcador explícito
(`rdBase.LogWarningMsg` + `capfd`) já estabelecido pelo Incremento017.

**Correção**: o teste único anterior
(`test_native_rdkit_logs_are_suppressed_and_restored`) foi substituído por dois
testes que seguem exatamente o padrão legado
(`test_enumeration_logs_are_suppressed_and_restored_after_incomplete_status`/
`test_successful_enumeration_restores_rdkit_logs`): `capfd.readouterr()` para limpar
o buffer, a operação real, `capfd.readouterr()` para capturar sua saída, e então
`rdBase.LogWarningMsg(marcador único)` seguido de nova `capfd.readouterr()` conferindo
o marcador em `captured.err`. Nenhuma chamada a `EnableLog` foi adicionada — a
restauração depende inteiramente do `__exit__` do próprio `rdBase.BlockLogs()`.

Os cenários de sucesso e falha (não-interrupção) têm, agora, prova direta própria.
Os cenários de interrupção (`KeyboardInterrupt`/`SystemExit`) têm a mesma prova de
marcador embutida diretamente em `_run_interruption_case` (Seção 5.2), para cada uma
das cinco fases que de fato executam dentro de um escopo `with rdBase.BlockLogs():`
(parsing SDF/SMILES, cálculo dos valores, coordenadas/preparação, renderização) — as
três fases que não usam `BlockLogs` (validação de entrada, validação/vínculo do SVG,
construção do resultado) não recebem essa prova de log, porque não haveria log
nativo RDKit suprimido para restaurar ali; essa distinção é verificada pelo próprio
código do teste (`uses_blocklogs`), não omitida silenciosamente.

#### 5.3.1 Testes

| Função de teste | Itens coletados | Resultado |
|---|---:|---|
| `test_native_rdkit_logs_are_suppressed_on_failure_and_restored_with_marker` | 1 | Marcador presente em stderr após falha de negócio |
| `test_native_rdkit_logs_are_suppressed_on_success_and_restored_with_marker` | 1 | Marcador presente em stderr após sucesso |
| (embutido) marcador em `test_keyboard_interrupt_propagates_unconverted_by_adapter_phase`/`test_system_exit_propagates_unconverted_by_adapter_phase`, condicionado a `uses_blocklogs` | 5+5 das 8+8 fases | Marcador presente em stderr após interrupção, nas 5 fases que usam `BlockLogs` |

A função anterior (`test_native_rdkit_logs_are_suppressed_and_restored`, 1 item) foi
removida nesta rodada — não preservada como teste redundante, porque suas duas
asserções (ausência de "ERROR"; segundo cálculo funciona) estão ambas estritamente
subsumidas pelas duas novas funções, que adicionam a prova direta de marcador sem
perder nenhuma asserção original.

### 5.4 MINOR-2 — SGroup/estereogrupo testados só por objeto direto, não por bytes reais

**Achado**: os testes de elegibilidade para SGroup e grupos estéreo AND/OR
chamavam `_validate_graph_eligibility(mol)` diretamente sobre um `Mol` construído via
API, não através do caminho completo bytes→`ForwardSDMolSupplier`→elegibilidade.

**Correção**: três funções de fixture (`_v3000_sgroup_sdf_bytes`,
`_v3000_stereo_group_sdf_bytes`) constroem bytes SDF V3000 reais pela mesma rota que
a pesquisa do arquiteto verificou — `Chem.MolFromSmiles` → `Chem.RWMol` →
`Chem.CreateMolSubstanceGroup`/`Chem.CreateStereoGroup` → `Chem.MolToMolBlock(
forceV3000=True)` + `"$$$$\n"` — **reproduzidas independentemente nesta sessão, no
código desta correção**, não copiadas do JSON de evidência. Os bytes produzidos
foram conferidos **byte-idênticos** aos da pesquisa do arquiteto por tamanho e
SHA-256 exatos (428 bytes/`1ec45e31...` para SGroup; 496 bytes/`74040ab4...` para AND;
496 bytes/`8a5f0741...` para OR — os três hashes batem exatamente com
`architect-synthetic-v3000-roundtrip-probe.json`).

Cada fixture é então exercitada em duas etapas, nunca pulando a primeira: (1) parse
direto via `Chem.ForwardSDMolSupplier(..., sanitize=True, removeHs=False,
strictParsing=True)` real, confirmando que o SGroup/grupo estéreo esperado foi de
fato retido pelo parser real (e nenhum outro) — evitando confundir ausência de grupo
ou erro de sintaxe com a política científica, exatamente como a reconciliação
instrui; (2) só então, a chamada ao **adaptador público completo**
(`characterize_molecule_rdkit`, bytes→parsing→elegibilidade real, nenhum monkeypatch
do parser ou da elegibilidade), confirmando `unsupported-structure`. Um caso de
controle (`STEREO_ABSOLUTE`, mesma rota de construção, sem grupo AND/OR) confirma que
a recusa é específica da política AND/OR, não um artefato incidental da construção
V3000/`CreateStereoGroup`.

Os testes unitários diretos anteriores (`_validate_graph_eligibility(mol)` chamado
diretamente) foram **preservados sem alteração** — a correção acrescenta a
integração por bytes, não a substitui.

#### 5.4.1 Testes

| Função de teste | Parametrização | Itens coletados | Resultado |
|---|---|---:|---|
| `test_v3000_sgroup_fixture_bytes_match_the_research_evidence_hash` | — | 1 | 428 bytes, SHA-256 idêntico à pesquisa do arquiteto |
| `test_v3000_and_fixture_bytes_match_the_research_evidence_hash` | — | 1 | 496 bytes, SHA-256 idêntico |
| `test_v3000_or_fixture_bytes_match_the_research_evidence_hash` | — | 1 | 496 bytes, SHA-256 idêntico |
| `test_v3000_sgroup_bytes_parse_with_the_group_retained_before_adapter_rejection` | — | 1 | Parser real retém exatamente 1 SGroup, 0 grupos estéreo |
| `test_v3000_stereo_group_bytes_parse_with_the_group_retained_before_adapter_rejection` | AND, OR | 2 | Parser real retém exatamente o grupo esperado (`STEREO_AND`/`STEREO_OR`), 0 SGroups |
| `test_v3000_sgroup_bytes_are_rejected_by_the_full_public_adapter_as_unsupported_structure` | — | 1 | Adaptador completo recusa por `unsupported-structure` |
| `test_v3000_enhanced_stereo_bytes_are_rejected_by_the_full_public_adapter_as_unsupported_structure` | AND, OR | 2 | Idem, para ambos os grupos |
| `test_v3000_absolute_stereo_bytes_are_not_rejected_by_the_full_public_adapter` | — | 1 | Controle: `STEREO_ABSOLUTE` pela mesma rota caracteriza normalmente (`C2H4ClF`) |

Total: 8 funções novas, **10 itens coletados**.

## 6. Reconciliação de itens coletados — antes/depois, por arquivo

| Arquivo | Funções antes (`f8416b8`) | Funções depois | Itens coletados antes | Itens coletados depois |
|---|---:|---:|---:|---:|
| `tests/test_characterization.py` | 51 | 62 (+11) | 111 | 155 (+44) |
| `tests/test_rdkit_tautomer.py` | 116 | 128 (+12 netas: +13 novas, −1 removida) | 142 | 170 (+28) |

Comandos exatos usados para esta reconciliação:

```
pytest tests/test_characterization.py -q --collect-only   -> 155 tests collected
pytest tests/test_rdkit_tautomer.py -q --collect-only      -> 170 tests collected
grep -c "^def test_" tests/test_characterization.py        -> 62
grep -c "^def test_" tests/test_rdkit_tautomer.py           -> 128
git show f8416b8:tests/test_characterization.py | grep -c "^def test_"  -> 51
git show f8416b8:tests/test_rdkit_tautomer.py | grep -c "^def test_"    -> 116
```

Nenhum número de itens esperado foi fixado antes da coleta real; os valores acima
são a contagem real, reconciliada função a função contra a soma dos itens das
tabelas 5.1.2/5.2.1/5.3.1/5.4.1 (44 e 28, exatamente).

## 7. Comandos executados e resultados — suíte completa

### 7.1 Suítes focais (ambiente com RDKit real)

```
pytest tests/test_characterization.py -q
→ 155 passed in 0.81s   (111 passed antes desta correção)

pytest tests/test_rdkit_tautomer.py -q
→ 170 passed in 3.31s   (142 passed antes desta correção)
```

### 7.2 Suíte completa do projeto

```
pytest tests/ -q
→ 1739 passed, 5 skipped in 89.39s
```

Antes desta correção (mesmo HEAD `f8416b8`, mesmo ambiente, suíte completa, já
registrado no relatório anterior e reconfirmado nesta sessão antes de editar
qualquer arquivo): **1667 passed, 5 skipped**. Delta: **+72 testes aprovados**, **0
regressões**, **0 skips novos/removidos**. 72 = 44 (`test_characterization.py`) + 28
(`test_rdkit_tautomer.py`), reconciliado exatamente com a Seção 6.

### 7.3 Ambiente sem o extra `rdkit` (fronteira opcional, reconfirmada após a correção)

```
pytest tests/test_characterization.py -q   (venv sem rdkit)
→ 155 passed in 1.11s   (idêntico ao ambiente com rdkit — nenhuma das 44 novas
  asserções de MAJOR-1 depende de RDKit, por construção)

pytest tests/test_rdkit_tautomer.py -q   (venv sem rdkit)
→ 1 skipped   (arquivo inteiro pulado via pytest.importorskip("rdkit") de escopo
  de módulo, comportamento inalterado)
```

Nenhuma correção desta rodada exigiu ou introduziu nova dependência, nem tocou a
fronteira opcional de import (`_RDKIT_IMPORT_ERROR`/`_RDKIT_DRAWING_IMPORT_ERROR`
permanecem exatamente como no HEAD revisado — nenhuma linha correspondente aparece
no diff desta rodada).

### 7.4 Higiene de diff e árvore de trabalho

```
git diff --check   → saída vazia, exit code 0 (sem erros de whitespace)
git status (antes da correção) → working tree limpa no HEAD revisado f8416b8,
                                   só os venvs locais (.venv020a*, não versionados,
                                   reaproveitados da etapa anterior) como untracked
git status (depois, antes do commit) → exatamente os 3 arquivos desta rodada
                                   modificados (characterization.py,
                                   test_characterization.py, test_rdkit_tautomer.py);
                                   rdkit_tautomer.py não listado (sem alteração)
```

Staging explícito por caminho (`git add src/molecular/characterization.py
tests/test_characterization.py tests/test_rdkit_tautomer.py`) — nunca `git add .`
nem `-A`. `increment-009-review.txt`, `_figura_curcumina/` e o novo `Claude outputs/`
observado no checkout original do usuário não aparecem em nenhum `git status` desta
sessão, em nenhum dos dois repositórios/checkouts tocados.

## 8. Identidade e SHAs publicados

### 8.1 Código

- **Commit corretivo publicado**: **`9ccdb9817a78f8de34c085c16443293b1ab99fd9`**, na
  branch `feature/increment-020-a-molecular-characterization`, repositório
  `sysoutemanuelhenrique/molecular-platform`. Parent direto, único:
  `f8416b845efe93f9e47deca97f01a355e4e679ba` (o HEAD revisado exato) — confirmado por
  `git log -1 --format='%H %P'`. Nenhum `amend`, `rebase`, `reset` ou `force push`
  foi usado; o `git push` foi um fast-forward simples.
- `origin/feature/increment-020-a-molecular-characterization` após o push aponta para
  o mesmo SHA, confirmado por `git rev-parse`.
- `origin/main` permanece em `08b797e0985e123ffd4d7ca7e5a5e8f040e63851` — confirmado
  por novo `git fetch` + `git rev-parse` ao final da sessão. Nenhum PR, merge, force
  push, amend, reset ou rebase foi executado; nenhuma configuração ou visibilidade
  foi alterada.

### 8.2 Diff corretivo (esta rodada, `f8416b8` → `9ccdb98`)

```
 src/molecular/characterization.py | 196 insertions(+), 10 deletions(-)
 tests/test_characterization.py    | 184 insertions(+), 0 deletions(-)
 tests/test_rdkit_tautomer.py      | 331 insertions(+), 6 deletions(-)
 3 files changed, 711 insertions(+), 16 deletions(-)
```

### 8.3 Diff cumulativo (baseline `08b797e` → `9ccdb98`, allowlist completa)

```
 src/molecular/characterization.py | 1240 insertions(+), 0 deletions(-)
 src/molecular/rdkit_tautomer.py   |  679 insertions(+), 1 deletion(-)
 tests/test_characterization.py    |  902 insertions(+), 0 deletions(-)
 tests/test_rdkit_tautomer.py      |  968 insertions(+), 0 deletions(-)
 4 files changed, 3789 insertions(+), 1 deletion(-)
```

(A linha de `rdkit_tautomer.py`, +679/−1, confirma a errata da Seção3.1 — a mesma
contagem que o revisor e o arquiteto já haviam apontado, agora recomputada
diretamente nesta sessão a partir do diff real.)

### 8.4 Este relatório

Publicado no repositório de governance
`sysoutemanuelhenrique/molecular-platform-governance`, branch própria
`claude/020-a-checkpoint1-corrections-20261021` (ramificada de `origin/main` do
governance, SHA `a47183dfec8213c765ed43ae482c8c227760a3d5`, preservando esse SHA
intacto), no caminho exato
`increments/020-A/11-checkpoint-1-corrections/CLAUDE_CHECKPOINT1_CORRECTIONS_REPORT.md`
exigido pela tarefa. Evidências próprias publicadas sob
`increments/020-A/11-checkpoint-1-corrections/evidence/claude-major1-pre-fix-reproduction.{py,json}`.
Nenhuma edição a `STATUS.md`, a tarefas centrais, ao parecer adversarial original, à
evidência original, ao relatório de implementação anterior ou à reconciliação do
arquiteto foi feita nesta sessão.

## 9. Disposição das NOTES (sem mudança de código)

- **NOTE-1** (gramática SVG `Z`): mantida sem alteração. Nenhuma linha de
  `_D_COMMAND_ARITY` ou da gramática `d` foi tocada nesta rodada — confirmado pelo
  diff vazio em `src/molecular/rdkit_tautomer.py` e pela ausência de qualquer menção
  a `"Z"` no diff de `characterization.py`. O teste
  `test_filled_wedge_triangle_z_command_is_an_unresolved_profile_gap` permanece
  inalterado e passando.
- **NOTE-2** (localização do validador SVG em `characterization.py`): mantida sem
  alteração.
- **NOTE-3**: errata registrada na Seção 3.1/8.3 acima.
- **NOTE-4/NOTE-5**: sem ação de código necessária; os limites de execução desta
  sessão estão declarados na Seção 4 e nenhuma sonda de pesquisa é apresentada como
  teste de produção (Seção 5.1.1 identifica explicitamente sua própria natureza
  diagnóstica).

## 10. Não realizado nesta etapa

Checkpoints 2 e 3 **não foram implementados nem iniciados**. Nenhum PR foi aberto;
nenhum merge foi solicitado ou executado. `increment-009-review.txt` e
`_figura_curcumina/` não foram tocados. A falha pré-existente, não relacionada a este
diff, em `tests/test_cli.py` (dois testes que importam `rdkit` diretamente sem
`importorskip`, já registrada no relatório anterior, Seção 6.4, item 4) não foi
"corrigida" fora da allowlist — permanece exatamente como estava, fora do escopo
desta tarefa.

## 11. Pedido de reverificação independente focal

Este checkpoint está pronto para a reverificação independente focal dos quatro
achados (MAJOR-1/2, MINOR-1/2) e de regressões concretas sobre o novo HEAD
`9ccdb98`, conforme o próprio `next_gate` da tarefa. Nenhum Checkpoint subsequente
foi iniciado por esta sessão.
