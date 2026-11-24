# Relatório de implementação — Incremento 021, Checkpoint 2

Autor: Claude implementador (sessão separada da revisão independente). Data: 24/11/2026, America/Sao_Paulo.

## 1. Identificação da tarefa e autorização conferida

- Tarefa: `tasks/021-CHECKPOINT2-IMPLEMENTATION.json`, lida no snapshot de governance `399bbbc7bea95fa4eafcc6757bf2d8d8a166df30` (branch de coordenação `docs/020-a-candidate1-review-20261020`), que é exatamente o commit informado pelo arquiteto.
- Antes de agir, confirmei por `git show 399bbbc7...:<path> | sha256sum`/`wc -lc` (bytes do blob Git, nunca os bytes locais em disco — este repositório de governance aplica `core.autocrlf=true`) a identidade dos arquivos normativos:
  - `STATUS.md` confirma `checkpoint1_approved`/código aprovado em `ea8dac9cdc203c337d7f3f9947b54042291f7484` e autoriza exclusivamente o Checkpoint 2 no snapshot acima.
  - `tasks/021-CHECKPOINT2-IMPLEMENTATION.json` — `scope_authorized: "CHECKPOINT2_ONLY"`, `code_allowlist` com exatamente os quatro caminhos usados nesta entrega, `code_head_before_cp2: ea8dac9...`, `code_baseline: 08b797e...`, `expected_governance_main: a47183d...`.
  - `increments/021/34-checkpoint2-preparation/CHECKPOINT2_IMPLEMENTATION_BRIEF.md` (109 linhas) e `increments/021/34-checkpoint2-preparation/evidence/CP2_SCENARIO_SCOPE.csv` (79 cenários, `T021-041` a `T021-090`, `T021-141` a `T021-158`, `T021-162`, `T021-164` a `T021-173`) foram lidos integralmente.
  - A especificação congelada (`INCREMENT_021_FINAL_SPECIFICATION.md`, 377 linhas) e o catálogo anexo (`CATALOG_021.json`) foram reconferidos: `git show 399bbbc7...:increments/021/15-final-specification/evidence/CATALOG_021.json | sha256sum` reproduz exatamente `8561039fd15137811b60316336dff04539df3732710dca6ec4009f23150d6d03`, a constante `CATALOGUE_SHA256` já pinada no código do CP1 — confirmando que o catálogo transcrito nesta entrega é o mesmo arquivo congelado, não uma reconstrução independente.
- Autorização humana: a tarefa registra `owner_implementation_authorization_recorded`/`owner_message_literal` autorizando implementação/teste/commit/push restritos à allowlist, publicação do relatório em branch própria do governance, e proíbe explicitamente CP3/CP4, PR/merge/main, e qualquer retomada do 020-A.

## 2. Conferência de HEAD remoto e estado local antes de agir

- `git rev-parse HEAD` no repositório de código, antes de qualquer edição desta sessão, coincidia com `ea8dac9cdc203c337d7f3f9947b54042291f7484` (o `code_head_before_cp2` exigido pela tarefa) — confirmado também por `git rev-parse origin/feature/increment-021-receptor-materialization` idêntico.
- `git rev-parse origin/main` retornou `08b797e0985e123ffd4d7ca7e5a5e8f040e63851`, a baseline congelada, inalterada.
- `git status --short` mostrava apenas os três itens locais protegidos (`Claude outputs/`, `_figura_curcumina/`, `increment-009-review.txt`) como untracked, sem staging pendente — preservados intocados por toda a sessão.
- Repositório de governance confirmado em `399bbbc7...` (detached HEAD, inalterado por mim); um arquivo local não rastreado (`TBMP_ROADMAP_020_030_AND_FUTURE_PERSPECTIVES.md`) pré-existia e permanece intocado.

## 3. Ambiente real de execução

```
Python 3.14.7
pytest 9.1.1
pydantic 2.13.5 / pydantic_core 2.46.5
PyYAML 6.0.3
gemmi 0.7.5
typer 0.27.2
Plataforma: Windows-11-10.0.26300-SP0, venv do próprio projeto (.venv)
```

Gemmi 0.7.5 real foi usado em todo teste que o exercita — nenhum stub/sentinela de biblioteca nativa. Evidência completa em `evidence/claude-environment.txt`.

## 4. O que foi implementado

Apenas os quatro caminhos da allowlist, todos editados incrementalmente a partir de `ea8dac9` (nenhum arquivo novo fora da allowlist, nenhuma fixture em `tests/fixtures/receptor_materialization/` criada nesta entrega):

### 4.1 `src/molecular/receptor_materialization.py` (domínio puro, sem Gemmi/RDKit)

- **`resolve_connection_decisions`** (Seções 9/10/10.1): resolve ambos os endpoints de cada linha `struct_conn` em M, recusa `ptnr3` não nulo (`UNSUPPORTED_PARTNER`), calcula K (contagem de endpoints retidos) a partir das decisões reais do planner, classifica `IdentityBasis` por endpoint de forma independente de K (ordem ptnr1-então-ptnr2, nunca por ordem de visita de categoria), classifica `SymmetryClass` e aplica a matriz fechada de 15 células (Seção 10) junto da exceção metalc/hydrog em K=1 (parceiro inteiro removido por `chain-complement`/`disposition-remove`, nunca uma remoção parcial). Uma linha recusada nunca produz `ConnectionDecision` parcial — a função inteira levanta e nenhuma decisão é aceita.
- **`compute_category_decisions`** (Seção 11): aplica o catálogo fechado de 94 categorias (constante `_FROZEN_CATALOGUE`, transcrita byte a byte do `CATALOG_021.json` congelado — nunca lida de disco em runtime) categoria a categoria, despachando por `row_rule`: `AUDIT_OMITTED_CATEGORY` (67 categorias + as três famílias `_pdbx_validate_`/`_pdbx_nmr_`/`_em_`), `RETAINED_ENTITY`/`RETAINED_ENTITY_ALL_SEQUENCE`/`RETAINED_ENTITY_ALL_BRANCH` (filtro pela coluna que referencia `_entity.id`, ou a própria chave quando a categoria é `_entity`), a família simétrica `RETAINED_ASYM_*` sobre `_struct_asym.id`, `ATOM_MASK` (ligado 1:1 às `AtomDecision` reais do planner), `CONNECTION_ACTIONS` (ligado 1:1 às `ConnectionDecision` reais), `USED_CONNECTION_TYPES`/`USED_ELEMENTS` (derivados das conexões/átomos retidos, nunca um critério inventado), `SOURCE_FRAME_SINGLETON`/`SOURCE_OPERATORS` (contexto `_cell`/`_symmetry`/tabelas de operador preservados verbatim), `MODIFIED_RESIDUE_CONTEXT`/`MISSING_RESIDUE_CONTEXT`/`MISSING_ATOM_CONTEXT` (resolução de contexto por `label_asym_id` ou, quando ausente, por um índice auth→label construído de todos os átomos — ambiguidade recusa `INVALID_CIF`, nunca é descartada em silêncio), `REFERENCED_CCD_CLOSURE` (união dos CCDs de átomos retidos + sequências/branches preservadas + `parent_comp_id` preservado, calculada por último, depois que todo contribuinte já foi decidido), `ANISOTROP_ATOM_ID` (tensor U/B completo e finito obrigatório por linha-fonte, concordância de campos informados com o `_atom_site` referenciado, filtro pelo id real retido), `NCS_GUARD_THEN_OMIT` e `SPECIAL_POSITION_GUARD_THEN_OMIT` (guarda estrutural antes da omissão auditada). Categoria/tag fora do catálogo recusa (`UNSUPPORTED_CATEGORY`/`UNSUPPORTED_TAG`) antes de qualquer filtro.
- `AtomObservation` ganhou `label_atom_id`/`altloc` (opcionais, default `None` — todo fixture/teste de CP1 continua construindo sem eles); `compute_connection_decisions_key`/`build_materialization_plan` passaram a aceitar o vetor real de `ConnectionDecision` (default vazio preserva o hash/envelope exato do CP1 — reconciliação explícita do brief §2); `MaterializationPlan` ganhou o campo `connection_decisions`; `unavailable_categories`/`warnings` em `build_materialization_plan` agora são computados mecanicamente a partir dos vetores reais de categoria/conexão (nunca um valor fixo ou reconhecimento copiado).

### 4.2 `src/molecular/receptor_parsing.py` (único módulo que importa Gemmi)

- **`parse_receptor_cif_dom021`**: ponto de entrada Gemmi dedicado ao domínio 021 — rejeita BOM UTF-8, encoding inválido, save frames, múltiplos blocos e tags canônicas duplicadas (a última via o próprio `RuntimeError` nativo do parser do Gemmi durante `read_string`, antes mesmo de `check_for_duplicates()` rodar — ver nota de transparência no §6); extrai toda categoria presente via `get_mmcif_category(..., raw=True)` (preserva quoting/marcadores de nulo); aplica os tetos estruturais da Seção 4 (100k átomos, 50k conexões, 256 categorias, 128 tags/categoria, 500k linhas, 4M células, 1 MiB/célula).
- **`serialize_cif_document021`**/**`reparse_and_extract_cif_dom021`**: serialização determinística via `gemmi.cif.Document`/`set_mmcif_category(..., raw=True)` e reparse independente dos bytes recém-escritos pelo mesmo caminho de extração da fonte — nunca confiando no par escritor/leitor da mesma biblioteca sozinho como oráculo.
- **`materialize_receptor_cif021`**: a fronteira do adapter (único lugar que importa `gemmi` **e** chama `molecular.receptor_materialization` — o inverso é proibido por ARCH-01, reverificado no §6). Constrói `AtomObservation` reais a partir de `_atom_site` (resolvendo `entity_type` via `_entity.type`), `RawConnectionRow`/`SymmetryOperatorTables` a partir de `_struct_conn`/`_symmetry_equiv`/`_space_group_symop`, chama o planner, o resolvedor de conexões e o motor de catálogo nessa ordem, deriva `entry_id = "TBMP_<plan_key>"`/nome de bloco `tbmp_<plan_key>` do `plan_key` final, serializa e reparseia/verifica (`INVALID_OUTPUT` em qualquer divergência de contagem/tag entre o plano e o reparse).

Nenhum outro arquivo foi criado, editado ou removido; `receptor_parsing.parse_receptor_raw` (020) não foi tocado nem reutilizado como leitor materializador.

## 5. Decisões de design e seus limites (para a revisão independente)

1. **Prioridade de escopo explícita.** Dados os 79 cenários e o tamanho real do motor (matriz de simetria, 9+2 pares de IdentityBasis, 94 categorias com ~20 regras de linha distintas, aquisição de fixtures reais do PDB), priorizei primeiro o motor algébrico mais fechado e de maior risco de erro silencioso — resolução de conexões/simetria/IdentityBasis (§9/10/10.1) — e em seguida o motor de catálogo (§11), com um teste de integração real-Gemmi de ponta a ponta. **53 dos 79 cenários têm teste real mapeado 1:1 ou N:1** (nunca um teste "promovido" sem asserção específica); os demais 26 permanecem explicitamente pendentes (matriz completa em `evidence/claude-scenario-matrix.json`) — nunca convertidos em skip aprovado, conforme a própria tarefa permite ("79 cenários normativos, não promessa de 79 funções pytest").
2. **Nenhuma fixture real do PDB (5i55/1pfe/3dg1_final/NMR/EM/NCS) foi obtida ou usada nesta sessão.** O teste de integração real-Gemmi (`T021-090`) usa um mmCIF mínimo mas realista, escrito à mão, parseado/serializado/reparseado por Gemmi 0.7.5 real — prova o adapter completo, mas não substitui os cenários D-01(b)/`T021-147`/`T021-162` que exigem proveniência de um depósito real. Isso fica explicitamente pendente.
3. **Resolução de contexto por auth-apenas (`MODIFIED_RESIDUE_CONTEXT`/`MISSING_RESIDUE_CONTEXT`/`MISSING_ATOM_CONTEXT`) é um fallback best-effort**, não a heurística completa que o texto do §11 sugere: quando `label_asym_id` da linha é nulo, resolvo via um índice `auth_asym_id → {label_asym_id}` construído de *todos* os átomos (retidos ou não); ambiguidade (zero ou mais de um `label_asym_id` candidato) recusa `INVALID_CIF` em vez de inferir. Se a coluna `label_asym_id` estiver inteiramente ausente da categoria-fonte, a categoria inteira recusa `UNSUPPORTED_CATEGORY` (incapacidade declarada, nunca omissão silenciosa) — fidelidade exata ao texto "declarar o perfil incapaz de mapear e recusar".
4. **`SPECIAL_POSITION_GUARD_THEN_OMIT`** usa a mesma resolução de contexto (label-ou-auth-unívoco) como guarda antes da omissão auditada; não implementei nenhuma validação adicional de "contagens/aviso corretos" além de garantir que o contexto é resolvível — `special-position-annotations-omitted`/`source-ncs-annotations-omitted` já são emitidos como avisos quando a categoria correspondente está presente nas decisões, mas a integração completa de avisos→`PlanBinding.warnings` cobre apenas os casos mecanicamente derivados do próprio vetor de decisões (ver §4.1); não reimplementei nenhuma lógica de "contagem" adicional não exigida por um cenário específico.
5. **Código NCS desconhecido (`_struct_ncs_oper.code` fora de `given`/`generate`/nulo) recusa `INVALID_CIF`.** Esta correção foi feita durante a própria sessão de implementação ao notar que o enum real de `code` é fechado em duas palavras + nulo (T021-154 agrupa "matriz parcial/NaN" e "código desconhecido" sob a mesma expectativa) — registrado aqui porque não estava explícito antes de eu escrever o primeiro teste guiado por esse cenário.
6. **`ANISOTROP_ATOM_ID`** verifica concordância de `pdbx_label_atom_id`/`pdbx_label_asym_id`/`pdbx_label_comp_id` contra o `_atom_site` referenciado quando esses campos estão presentes; não verifico `pdbx_label_seq_id` por simetria com os três já implementados — isso é um subconjunto do "demais campos informados concordam" do texto normativo, não a verificação exaustiva de todas as ~15 colunas espelhadas.
7. **`git duplicate-tag` é capturado pelo `RuntimeError` nativo do Gemmi durante `read_string`**, antes do `document.check_for_duplicates()` explícito deste código rodar — a rejeição acontece (via `ReceptorParseFailureError`, não `DuplicateCanonicalTagError`), mas a classificação de erro específica (`DuplicateCanonicalTagError`) fica como defesa em profundidade para um caso que o próprio parser do Gemmi não intercepta nativamente (ex.: duas grafias de caixa distintas da mesma tag canônica). Documentado explicitamente no teste correspondente, não "corrigido" por não ser um defeito funcional — a duplicata é recusada de qualquer forma.
8. **Nenhum arquivo final (`receptor.cif`) é publicado** nesta entrega — `materialize_receptor_cif021` produz bytes em memória e os reparseia para verificação; persistência/registry/service são CP3 (fora de escopo), exatamente como a tarefa exige.

## 6. ARCH-01 e a fronteira do adapter

```
python -B -c "
import sys
sys.modules['gemmi'] = None
sys.modules['rdkit'] = None
import molecular.receptor_materialization as rm
print('ARCH-01 OK')
"
-> ARCH-01 OK
```

`receptor_materialization.py` nunca importa `gemmi`/`rdkit`, nem transitivamente — reverificado após toda a nova implementação, com os dois módulos nativos bloqueados em `sys.modules` por um sentinela `None` (que faz qualquer `import` subsequente falhar explicitamente, nunca passar em silêncio). `receptor_parsing.py` permanece o único módulo que importa `gemmi`, e é também o único que importa `molecular.receptor_materialization` *e* `gemmi` ao mesmo tempo — a direção inversa (domínio importando o adapter) nunca ocorre, confirmado por essa mesma verificação.

## 7. Cobertura dos cenários

Matriz completa cenário→teste(s) real(is) em `evidence/claude-scenario-matrix.json`: **53 de 79 cenários cobertos** por teste(s) pytest reais, executados contra produção real (nenhum stub, nenhum `pytest.raises(Exception)` genérico, nenhum hash copiado do próprio algoritmo como única prova). Os **26 cenários restantes permanecem explicitamente pendentes** — nunca convertidos em skip aprovado:

```
Pendentes: T021-041, T021-042, T021-043, T021-065, T021-066, T021-068, T021-069, T021-070,
           T021-071, T021-072, T021-073, T021-074, T021-080, T021-081, T021-086, T021-088,
           T021-089, T021-145, T021-146, T021-147, T021-148, T021-149, T021-155, T021-156,
           T021-157, T021-162
```

Agrupamento dos pendentes, para a triagem do arquiteto:
- **Tokens/coordenadas brutos e endpoint de inserção** (T021-041/042/043): o adapter já preserva esses tokens estruturalmente (nenhuma conversão numérica, nenhuma reparação) mas nenhum teste dedicado isola especificamente esses três cenários.
- **Famílias RETAINED_* restantes** (T021-065/066/068/069/070/071/072/073/074): a *mecânica* (filtro por `_entity.id`/`_struct_asym.id`) já é genérica e testada via T021-061/063/064/067; os 9 cenários individuais de cada categoria específica (`entity_poly`, `entity_poly_seq`, `pdbx_entity_nonpoly`, `pdbx_poly_seq_scheme`, `pdbx_nonpoly_scheme`, `pdbx_entity_branch`, `pdbx_entity_branch_list`, `pdbx_entity_branch_link`, `pdbx_branch_scheme`) não têm teste próprio.
- **Resíduos modificados/ausentes** (T021-080/081): a função está implementada (`MODIFIED_RESIDUE_CONTEXT`/`MISSING_RESIDUE_CONTEXT`/`MISSING_ATOM_CONTEXT`, ver §5.3) mas sem teste dedicado.
- **Auditoria/verificação de saída** (T021-086/088/089): `UNSUPPORTED_CATEGORY` para categoria condicional ausente, auditoria completa com checksum RAW inalterado, e `INVALID_OUTPUT` antes do commit estão implementados (o segundo via o próprio fluxo de `materialize_receptor_cif021`; o terceiro via `_verify_output_reparse`) mas sem teste que force deliberadamente a falha.
- **Fixtures reais** (T021-145/146/147/148/149/162): exigem os inventários 5i55/1pfe/3dg1_final/NMR/EM/NCS reais — nenhuma aquisição de fixture foi feita nesta sessão (ver §5.2).
- **Numéricos su-exponent e altloc** (T021-155/156/157): a gramática numérica do §6 e a resolução de conjunto de endpoint por altloc (`_resolve_endpoint_atoms`/`_resolve_endpoint_altloc`) já existem no código (usadas implicitamente pelos testes de conexão), mas sem teste que isole especificamente esses três cenários.

## 8. Reconciliação da coleta, regressão e fronteira de domínio

```
baseline (ea8dac9, worktree isolado):  python -B -m pytest --collect-only -q  ->  1573 tests collected
após esta entrega (HEAD 0d06ebd):      python -B -m pytest --collect-only -q  ->  1622 tests collected   (+49)
  receptor_materialization: 92 -> 131 (+39)
  receptor_parsing:         31 -> 41  (+10)

tests/test_receptor_parsing.py + tests/test_receptor_materialization.py:
  python -B -m pytest -p no:cacheprovider tests/test_receptor_parsing.py tests/test_receptor_materialization.py -q -rs
  -> 172 passed in 1.91s

regressão 020 (inspection/selection/resolution/registry/service):
  python -B -m pytest -p no:cacheprovider tests/test_receptor_inspection.py tests/test_receptor_selection.py tests/test_receptor_resolution.py tests/test_receptor_registry.py tests/test_receptor_service.py -q -rs
  -> 121 passed in 11.40s

suíte completa:
  python -B -m pytest -p no:cacheprovider -q -rs
  -> 1617 passed, 5 skipped in ~155-165s
```

Os 5 skips já existiam na baseline (RDKit/symlink/ambiente — nenhum novo introduzido pelos quatro arquivos editados). Nenhum teste CP1 existente foi editado ou removido — os 92 testes de CP1 em `test_receptor_materialization.py` continuam exatamente como estavam, inclusive os vetores-áureos (`_GOLDEN_*`) que dependem de `connection_decisions_key` sobre vetor vazio: a mudança de assinatura de `compute_connection_decisions_key`/`build_materialization_plan` usa `decisions: Sequence[ConnectionDecision] = ()` como default, preservando byte a byte o hash do caso vazio do CP1.

`git diff --check` e `git show --check HEAD` não reportaram problema de whitespace. `git diff --name-status ea8dac9...HEAD` e `git diff --name-status 08b797e...HEAD` mostraram exatamente os quatro caminhos da allowlist (evidência completa em `evidence/claude-git-log.txt`), nenhum outro arquivo do repositório tocado.

## 9. Identidades dos arquivos entregues (código, bytes do blob Git do commit publicado)

| Caminho | Linhas | Bytes | SHA-256 |
|---|---:|---:|---|
| `src/molecular/receptor_materialization.py` | 4060 | 192.457 | `0c7451e5b4950644c1e428c98a0c92f35f4aa3ae7753db4715cc292f6afa9947` |
| `src/molecular/receptor_parsing.py` | 1541 | 61.059 | `a620a659b172e418d7ed676b35c2736374f59f4a3db48616d608e868214898fa` |
| `tests/test_receptor_materialization.py` | 2252 | 114.463 | `0aca061820c04cd519c3a9f2c862a521af512a0ab80d0e663f98f353be86b971` |
| `tests/test_receptor_parsing.py` | 830 | 27.785 | `84d1d3091045a416beaa7b1d51a5cd3a4ab019b4a3adfd83bcc4043669e55b10` |

Identidades recomputadas diretamente do blob publicado no commit `0d06ebd4c46c90e5446fec6f0eb72b4a8d2855db` (`git show 0d06ebd...:<path> | sha256sum`/`wc -lc`), nunca dos bytes locais em disco (`core.autocrlf` não altera este repositório de código — confirmado, `git diff --check` limpo).

## 10. Commit e publicação remota do código

- Branch pré-existente `feature/increment-021-receptor-materialization`, `HEAD` confirmado em `ea8dac9...` (o `code_head_before_cp2` exato) antes de qualquer edição.
- Staging explícito de apenas os quatro caminhos (`git add src/molecular/receptor_materialization.py src/molecular/receptor_parsing.py tests/test_receptor_materialization.py tests/test_receptor_parsing.py`) — nunca `git add -A`/`.`.
- Commit normal (sem `--amend`/`--no-verify`/`-c commit.gpgsign=false`):

```
commit 0d06ebd4c46c90e5446fec6f0eb72b4a8d2855db
parent  ea8dac9cdc203c337d7f3f9947b54042291f7484
branch  feature/increment-021-receptor-materialization
4 files changed, 3833 insertions(+), 38 deletions(-)
```

- Push: `git push origin feature/increment-021-receptor-materialization` — **sucesso**, confirmado por `git rev-parse origin/feature/increment-021-receptor-materialization` devolvendo `0d06ebd4c46c90e5446fec6f0eb72b4a8d2855db`. `git rev-parse origin/main` depois do push ainda devolve `08b797e0985e123ffd4d7ca7e5a5e8f040e63851` — main remota **inalterada**.
- **Nenhum PR foi aberto, nenhum merge, nenhuma tag/release, nenhuma aprovação formal no GitHub.**
- Evidência completa (log, diff --name-status, rev-parse antes/depois) em `evidence/claude-git-log.txt`.

## 11. O que não foi feito (fora do escopo autorizado)

- Nenhum CP3/CP4: nenhum storage/reservation/registry/service/CLI, nenhuma publicação de `receptor.cif` final, nenhum `AuditRecord`/`Summary`/`PreviewOutcome`/`ManifestRecord`/`ArtifactOutcome`.
- Nenhuma fixture física criada em `tests/fixtures/receptor_materialization/` — nenhuma aquisição de inventário real (5i55/1pfe/3dg1_final/NMR/EM/NCS) nesta sessão.
- Nenhuma alteração em `pyproject.toml`, dependências, CLI, registries/modelos do 020, módulos de ligante/tautômero.
- `020-A` permanece em stand-by, sem retomada; os itens locais protegidos de ambos os repositórios permanecem untracked e intocados.
- Nenhum PR, merge, tag, release ou alteração de `main` em nenhum dos dois repositórios.
- Nenhum fechamento independente do CP2 é declarado por este relatório — isso é explicitamente reservado à revisão independente/triagem do arquiteto.

## 12. Gate sugerido

Entrega de CP2 **parcial e honesta**: o motor de resolução de conexões/simetria/IdentityBasis (§9/10/10.1) e o motor de catálogo de 94 categorias (§11) estão implementados e verificados contra Gemmi 0.7.5 real, com 53 dos 79 cenários mapeados 1:1 a testes reais passando e os 26 restantes explicitamente listados como pendentes (nunca como skip aprovado). Recomendo que o arquiteto decida entre (a) autorizar uma segunda sessão de implementação para fechar os 26 cenários pendentes e a aquisição de fixtures reais antes da revisão independente, ou (b) encaminhar este estado parcial à revisão independente já, com a lista de pendências do §7 como roteiro explícito. Não solicito nem presumo avanço automático ao CP3.

```
TASK_ID: 021-CHECKPOINT2-IMPLEMENTATION
ROLE: claude-implementer-separate-from-independent-reviewer
SCOPE_EXECUTED: CHECKPOINT2_PARTIAL
CODE_BRANCH: feature/increment-021-receptor-materialization
CODE_COMMIT: 0d06ebd4c46c90e5446fec6f0eb72b4a8d2855db
CODE_PARENT: ea8dac9cdc203c337d7f3f9947b54042291f7484
CODE_PUSH_VERIFIED: YES
CODE_MAIN_MODIFIED: NO
PR_OPENED: NO
MERGE_PERFORMED: NO
CP3_IMPLEMENTATION_AUTHORIZED: NO
SCENARIOS_MAPPED_TO_REAL_TESTS: 53 of 79 (1:1 or N:1, no inflation; 26 explicitly pending, never skipped-approved)
FULL_SUITE_PASSED: YES (1617 passed, 5 skipped, 1622 collected; +49 vs 1573 baseline)
ARCH01_REVERIFIED: YES (gemmi/rdkit blocked via sys.modules sentinel)
NEXT_GATE: ARCHITECT_TRIAGE_THEN_DECISION_ON_CP2_COMPLETION_OR_INDEPENDENT_REVIEW
```
