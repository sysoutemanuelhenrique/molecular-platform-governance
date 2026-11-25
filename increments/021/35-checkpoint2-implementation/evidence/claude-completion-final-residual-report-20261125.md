# Relatório final residual — Incremento 021, Checkpoint 2 (R-CP2-01/R-CP2-03 restantes, R-CP2-04 por bytes Git)

Autor: Claude implementador (sessão separada da revisão independente). Data: 25/11/2026, America/Sao_Paulo.

Aditivo aos relatórios já publicados (`claude-cp2-completion-report.md` em `70f7a14`, sua correção
`17e594d`, e o relatório residual `claude-completion-residual-correction-report-20261125.md` em
`2c50be1`). Nenhum deles foi editado.

## 1. Identidade e procedência

- Coordenação de entrada: `1c7906d748a544b26b007faad4d08062008d7fcd` (branch
  `docs/020-a-candidate1-review-20261020`), confirmada idêntica a
  `origin/docs/020-a-candidate1-review-20261020` antes de qualquer leitura.
- Recebimento focal complementar, lido integralmente por SHA (ainda não na ponta da branch de
  coordenação no momento da leitura, conforme informado no despacho):
  `increments/021/38-checkpoint2-residual-receipt/CODEX_INCREMENT_021_CHECKPOINT2_RESIDUAL_RECHECK.md`
  no commit `377534786c3ad390d08641c137d0d54681911fb8`.
- Tarefa `tasks/021-CHECKPOINT2-COMPLETION.json` lida na mesma revisão (`status:
  AUTHORIZED_FINAL_COMPLETION_OF_PARTIAL_R01_R03_AND_GIT_EVIDENCE`), mesma allowlist de código e
  raiz de fixtures já autorizadas.
- Confirmado antes de editar e reconfirmado depois: `git rev-parse HEAD` no código começou em
  `a8d46675e1d1bab83c9f7824225699afae57bd4a` (o `continuation_input_code_head`/
  `latest_code_delivery_commit` exatos da tarefa); `origin/main` código =
  `08b797e0985e123ffd4d7ca7e5a5e8f040e63851`; `origin/main` governance =
  `a47183dfec8213c765ed43ae482c8c227760a3d5` - ambos inalterados. Nenhum reset/clean/stash/rebase/
  amend/force usado. Os relatórios/branches anteriores
  (`claude/021-cp2-implementation-report`, `claude/021-cp2-completion-report`,
  `claude/021-cp2-residual-correction-report-20261125`) não foram tocados.

## 2. Ambiente real de execução

```
Python 3.14.7 (venv do próprio projeto, .venv) / gemmi 0.7.5 real / pytest
Plataforma: Windows-11-10.0.26300
```

## 3. Disposição dos residuais

### R-CP2-01 — parcial restante: componente informado contraditório (corrigido)

**Achado do recebimento focal:** `_resolve_special_position_row_atoms` comparava apenas
cadeia+sequência - com um átomo fonte real `A/seq1/ALA`, a própria `compute_special_position_summary`
aceitava uma anotação `A/seq1/GLY` e contava o átomo como afetado (1/1/1). O ramo por
`label_seq_id` também ignorava `auth_seq_id`/`pdb_ins_code` contraditórios quando informados junto.

**Correção:** `_same_residue` (dentro de `_resolve_special_position_row_atoms`) agora exige, além
de cadeia+sequência:
- Quando `label_seq_id` é a chave primária, um `auth_seq_id`/`pdb_ins_code` genuinamente informado
  junto precisa concordar com o átomo casado - nunca mais ignorado silenciosamente.
- `label_comp_id`/`auth_comp_id`, quando informados, precisam concordar com o `ccd` real do átomo
  casado.

Uma contradição (componente ou auth/inserção informados que não combinam com o único átomo real
que casa por cadeia+sequência) agora resulta em `INVALID_CIF` pelo mesmo caminho da checagem de
existência já existente - nunca mais um casamento silencioso por cadeia+sequência isolados. Casos
de interseção zero genuínos (outro modelo/altloc/átomo não retido) permanecem inalterados.

**Testes:** `test_catalogue_special_position_guard_requires_unambiguous_context` (estendido com os
casos contraditórios de componente e de auth_seq_id); nova asserção em
`test_compute_special_position_summary_counts_overlap_removed_and_other_model` reproduzindo
exatamente o contra-exemplo do recebimento (A/seq1/ALA real vs. anotação A/seq1/GLY, agora
recusada em vez de 1/1/1); novo teste nativo
`test_real_fixture_3dg1_special_position_rejects_contradicting_real_component` - mutando
`auth_comp_id` da linha real `_pdbx_struct_special_symmetry` do depósito 3DG1 (positivo 1/1/1
preservado como controle antes da mutação) e confirmando a recusa contra o átomo real via Gemmi
0.7.5.

### R-CP2-03 — parcial restante: `_entry` e identidade do bloco (corrigido)

**Achado do recebimento focal:** o verificador real aceitava `_entry.unplanned` ao lado de um id
correto - o ramo especial de `_entry` só conferia contagem/id, nunca o fechamento de tags que as
demais categorias já recebem. `ParsedCifDom021` não transportava o nome do bloco, então nenhum
confronto pós-reparse do bloco gerado contra `tbmp_<plan_key>` ocorria.

**Correção:**
- `ParsedCifDom021` ganhou o campo `block_name` (preenchido em `parse_receptor_cif_dom021` a partir
  do `block.name` real do Gemmi - já sem o prefixo `data_`, que a própria API do Gemmi remove).
- `_verify_output_reparse` recebe agora `block_name` (o nome esperado, `tbmp_<plan_key>`) e recusa
  `INVALID_OUTPUT(phase='verify')` quando o bloco reparseado difere.
- O ramo `_entry` aplica o mesmo fechamento de tags que as demais categorias (`output_categories.get("entry", {"id": [entry_id]})`
  contra as colunas reparseadas) antes de conferir o id - uma tag `_entry` nunca decidida agora
  recusa.

**Testes:** novo `test_output_verification_rejects_unplanned_entry_tag_and_wrong_block_name` - tag
`_entry` extra recusada (id correto preservado), o mesmo reparse sem a tag passa, e um nome de
bloco corrompido recusa citando o nome real divergente. Os testes existentes de categoria
extra/token mutado foram atualizados para fornecer/conferir `block_name` também.

### R-CP2-02 — sem nova demanda de implementação

O recebimento focal confirma explicitamente: "R-CP2-02 não gera nova demanda de implementação
neste recebimento." Nenhuma alteração adicional foi feita; a correção e os testes da entrega
anterior (`a8d4667`) permanecem intocados.

### R-CP2-04 — identidades finais por bytes Git reais (não working tree)

**Achado do recebimento focal:** os quatro tamanhos/hashes do relatório anterior correspondem
exatamente aos arquivos locais reconstruídos em CRLF; os blobs Git reais estão em LF - uma
diferença de superfície mecanicamente confirmada, não uma falha de identidade.

**Correção:** executei o helper fornecido e inspecionado,
`increments/021/38-checkpoint2-residual-receipt/evidence/GENERATE_GIT_BLOB_IDENTITIES.py`
(somente leitura - confirmei por leitura do seu próprio texto que não faz checkout/staging/escrita
de referência, apenas `git rev-parse`/`git show`/`git ls-tree` via subprocess), fora da árvore de
código, redirecionando stdout apenas para
`increments/021/35-checkpoint2-implementation/evidence/claude-completion-final-git-blob-identities-20261125.json`
(este caminho, dentro do próprio glob autorizado). O helper confirma `HEAD` == `a807b03f44089eb3cbacc14f871b63689a21aec9`
e verifica o SHA-1 de cada blob antes de calcular o SHA-256 - nenhum mismatch foi relatado.

| Caminho (bytes reais do blob Git, LF) | Linhas LF | Bytes | SHA-256 |
|---|---:|---:|---|
| `src/molecular/receptor_materialization.py` | 4577 | 219.765 | `7bfe7c5699ade464fa822fec938be616115feb41ecb628bedb32b12a12e8c330` |
| `src/molecular/receptor_parsing.py` | 1795 | 74.148 | `58ebd796eb4b4d896e74af79424a6b625e0e152ea2371c51519165c1faf43e8a` |
| `tests/test_receptor_materialization.py` | 3007 | 159.580 | `68e192c0e32477d31e683b55096c20ad7a10629d0c6800d46d8a580f9be33a5b` |
| `tests/test_receptor_parsing.py` | 1588 | 68.990 | `334cea0b4a2394af61688b980e8571e60e11bc301711133cfbe029183323c410` |

Estes números diferem dos relatórios anteriores (que usavam `wc -l`/`sha256sum` sobre o checkout
Windows em CRLF) precisamente pela causa já confirmada pelo arquiteto - os bytes acima são os
bytes reais do objeto Git (`git show <commit>:<path>`), nunca do working tree. O manifesto completo
(os quatro arquivos mais toda a árvore de fixtures) está em
`evidence/claude-completion-final-git-blob-identities-20261125.json`, gerado pelo próprio helper,
sem edição manual.

## 4. O que foi implementado (apenas a allowlist)

Edição aditiva sobre o commit `a8d46675e1d1bab83c9f7824225699afae57bd4a` (nunca reset/rebase/amend):
`src/molecular/receptor_materialization.py`, `src/molecular/receptor_parsing.py`,
`tests/test_receptor_materialization.py`, `tests/test_receptor_parsing.py`. Nenhum outro arquivo
do repositório tocado; nenhuma fixture nova ou modificada.

## 5. Reconciliação de coleta, foco, regressão e suíte completa

```
antes desta correção (HEAD a8d4667):                   1662 coletados (1657 passed, 5 skipped)
após esta correção (HEAD a807b03):                      1664 coletados (+2: um teste nativo R-CP2-01,
                                                          um teste de adapter R-CP2-03; R-CP2-02 sem
                                                          nova demanda)

tests/test_receptor_parsing.py + tests/test_receptor_materialization.py:
  python -B -m pytest -p no:cacheprovider tests/test_receptor_parsing.py tests/test_receptor_materialization.py -q -rs
  -> 214 passed in ~5s

regressão 020 (inspection/selection/resolution/registry/service):
  python -B -m pytest -p no:cacheprovider tests/test_receptor_inspection.py tests/test_receptor_selection.py tests/test_receptor_resolution.py tests/test_receptor_registry.py tests/test_receptor_service.py -q -rs
  -> 121 passed in ~5s (inalterado)

suíte completa:
  python -B -m pytest -p no:cacheprovider -q -rs
  -> 1659 passed, 5 skipped in 173.21s

Os cinco skips (inalterados, discriminados): tests/test_application.py:1809 e :1847 (RDKit
instalado), tests/test_atomic.py:1046 (symlink não permitido - WinError 1314), tests/test_cli.py:4250
e :4303 (exigem ambiente sem RDKit).
```

`git diff --check`/`git show --check` do commit publicado, limpos. `git diff --name-status` contra
`ea8dac9` (CP1 aprovado) mostra exatamente os quatro caminhos da allowlist mais a árvore de
fixtures já publicada - nenhum arquivo novo, nenhuma fixture tocada nesta correção.

## 6. Commit e publicação remota do código

```
commit a807b03f44089eb3cbacc14f871b63689a21aec9
parent  a8d46675e1d1bab83c9f7824225699afae57bd4a
branch  feature/increment-021-receptor-materialization
4 files changed, 222 insertions(+), 17 deletions(-)
```

Push confirmado: `git rev-parse origin/feature/increment-021-receptor-materialization` devolve
`a807b03...`. `git rev-parse origin/main` (código) continua `08b797e...`; `git rev-parse origin/main`
(governance) continua `a47183d...`. Nenhum PR, merge, tag ou alteração de `main` em nenhum dos dois
repositórios.

## 7. Disposição final honesta

R-CP2-01 e R-CP2-03 têm agora, especificamente, os dois pontos concretos apontados no recebimento
focal corrigidos e provados (incluindo prova nativa real para R-CP2-01). R-CP2-02 permanece sem
nova demanda, conforme o próprio recebimento declara. R-CP2-04 está resolvido pela causa raiz
confirmada (CRLF do working tree vs. LF do blob Git) com o manifesto gerado pelo helper fornecido,
lendo bytes diretamente do Git.

Isto não é uma alegação de fechamento integral e independente dos 79 cenários nem de C-01–C-07 em
sua totalidade - esta correção tem escopo estreito e deliberado (os dois pontos concretos do
recebimento focal mais a correção documental de R-CP2-04). Não declaro CP2 aprovado. Não solicito
avanço a CP3. Recomendo que o arquiteto confira esta entrega (diff `a8d4667..a807b03`, isolado aos
quatro arquivos listados, mais o manifesto Git-byte) e decida se o critério de conclusão do CP2
está agora satisfeito para a revisão independente final, ou se algum ponto exige mais uma rodada.

```
TASK_ID: 021-CHECKPOINT2-COMPLETION
ROLE: claude-implementer-separate-from-independent-reviewer
SCOPE_EXECUTED: CHECKPOINT2_FINAL_RESIDUAL_CORRECTION (R-CP2-01/R-CP2-03 remaining, R-CP2-04 Git-byte evidence)
CODE_BRANCH: feature/increment-021-receptor-materialization
CODE_COMMIT: a807b03f44089eb3cbacc14f871b63689a21aec9
CODE_COMMIT_PARENT: a8d46675e1d1bab83c9f7824225699afae57bd4a
READY FOR INDEPENDENT FINAL CP2 REVIEW: NO
CHECKPOINT2 APPROVED: NO
CHECKPOINT3 IMPLEMENTATION AUTHORIZED: NO
```
