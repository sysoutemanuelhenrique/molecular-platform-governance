# Relatório de correção residual — Incremento 021, Checkpoint 2 (R-CP2-01 a R-CP2-04)

Autor: Claude implementador (sessão separada da revisão independente). Data: 25/11/2026, America/Sao_Paulo.

Este relatório é aditivo: corrige os quatro residuais concretos (três MAJOR, um MINOR) levantados
no recebimento arquitetural da conclusão declarada, sem reescrever ou substituir os relatórios
anteriores (`claude-cp2-completion-report.md` em `70f7a14`, sua correção `17e594d`). Nenhum deles
foi editado.

## 1. Identificação da tarefa, autorização e snapshot

- Tarefa: `tasks/021-CHECKPOINT2-COMPLETION.json`, lida no snapshot de governance `1c7906d748a544b26b007faad4d08062008d7fcd`
  (branch de coordenação `docs/020-a-candidate1-review-20261020`) - o commit exatamente informado
  no despacho, confirmado idêntico a `origin/docs/020-a-candidate1-review-20261020` antes de
  qualquer leitura.
- Recebimento arquitetural lido integralmente: `increments/021/37-checkpoint2-completion-receipt/CODEX_INCREMENT_021_CHECKPOINT2_COMPLETION_RECEIPT.md`
  (88 linhas), que triagem três MAJOR (R-CP2-01/02/03) e um MINOR de evidência (R-CP2-04) contra a
  entrega `5be1e443200cedddac0f97707963500a2edc6da6`.
- Autorização: a mesma `authorization_basis` da tarefa original (`"Continue and complete all 79
  original CP2 scenarios/corrections in already approved allowlist and report glob"`), com a
  mesma allowlist de código (`src/molecular/receptor_parsing.py`, `src/molecular/receptor_materialization.py`,
  `tests/test_receptor_parsing.py`, `tests/test_receptor_materialization.py`) e a mesma raiz de
  fixtures - nenhuma nova autorização de escopo inferida, nenhuma fixture nova adicionada nesta
  correção.
- Confirmado antes de editar e reconfirmado depois: `git rev-parse HEAD` no código começou em
  `5be1e443200cedddac0f97707963500a2edc6da6` (exatamente o `continuation_head_rule`/`latest_code_delivery_commit`
  da tarefa); `origin/main` código = `08b797e0985e123ffd4d7ca7e5a5e8f040e63851`; `origin/main`
  governance = `a47183dfec8213c765ed43ae482c8c227760a3d5` - ambos inalterados. Diretório/branch/
  index/diff locais inspecionados primeiro, em modo leitura; nenhum reset/clean/stash/rebase/
  amend/force usado em nenhum momento. Os relatórios/branches parciais anteriores
  (`claude/021-cp2-implementation-report` @ `9aa0762`, `claude/021-cp2-completion-report` @ `17e594d`)
  não foram tocados.

## 2. Ambiente real de execução

```
Python 3.14.7 (venv do próprio projeto, .venv)
pytest (mesmo ambiente dos relatórios anteriores)
gemmi 0.7.5 real - nenhum stub/sentinela nativa em nenhum teste que o exercita
Plataforma: Windows-11-10.0.26300, mesmo checkout Windows do responsável
```

## 3. Disposição dos quatro residuais

### R-CP2-01 (MAJOR/C-05) — contexto e auditoria de posições especiais

**Achado confirmado antes de corrigir:** `_guard_special_position_row` retornava imediatamente
para *qualquer* `label_asym_id` não nulo, sem verificar se correspondia a um `_atom_site.label_asym_id`
real - um probe com `label_asym_id="NO_SUCH_ASYM"` ou `label_seq_id="999"` passava silenciosamente.
Não havia contagem `SpecialPositionSummary` (SCHEMAS §8) em lugar nenhum do CP2, e o aviso
`special-position-annotations-omitted` disparava pela mera presença da categoria, nunca pela
interseção retida real.

**Correção:** `_guard_special_position_row` foi substituída por `_resolve_special_position_row_atoms`,
que resolve cada anotação ao conjunto exato de ordinais `_atom_site` que ela referencia:

- `label_asym_id`, quando presente, precisa ser um asym real (`known_label_asym_ids`); quando
  ausente, `auth_asym_id` precisa resolver a exatamente um `label_asym_id` (lógica original
  preservada).
- Exige identidade de resíduo real (`label_seq_id` ou `auth_seq_id`) - sem nenhuma das duas, a
  anotação não tem como ser resolvida e é recusada.
- A existência do resíduo é verificada contra **todos os modelos** (nunca apenas M) - uma
  referência a um resíduo genuinamente inexistente (ex.: `seq=999` para um asym real) é
  `INVALID_CIF`; uma referência a um resíduo real mas presente apenas em outro modelo é uma
  resolução válida, com interseção zero, nunca um erro.
- `pdb_model_num` e `label_alt_id`, "quando informados" (Section 11), restringem o conjunto final
  de átomos correspondentes - a interseção com os átomos retidos é calculada depois desse filtro.

Uma nova função pura e independente, `compute_special_position_summary()`, calcula as três
contagens congeladas (`source_annotation_count`, `retained_annotation_count`,
`retained_unique_atom_count` - nunca duplicando um átomo retido afetado por anotações
sobrepostas) e é transportada em `MaterializationPlan.special_positions`
(`SpecialPositionSummary`, SCHEMAS §8) - **deliberadamente não** um novo campo em
`CategoryDecision`, o que alteraria `category_decisions_key`/`plan_key` de todo o sistema
(`compute_category_decisions_key` serializa cada `CategoryDecision` inteiro via
`model_dump(mode="json")` - um campo novo, mesmo opcional, mudaria o hash de toda decisão já
existente, quebrando os 92 testes/vetores-áureos CP1 preservados). O aviso agora exige
`retained_annotation_count > 0`, nunca mera presença da categoria.

**Testes:** `test_catalogue_special_position_guard_requires_unambiguous_context` (existente,
corrigido para fornecer identidade de resíduo e estendido com os casos asym desconhecido/sem
identidade/resíduo inexistente); `test_compute_special_position_summary_counts_overlap_removed_and_other_model`
(novo - sobreposição, somente-removida, outro modelo, altloc, categoria ausente, aviso
condicionado à interseção real); a amostra real `test_real_fixture_3dg1_positive_materialization_with_real_special_symmetry`
foi estendida com as três contagens exatas (1/1/1) contra o depósito real.

### R-CP2-02 (MAJOR/C-05) — coerência anisotrópica e família parcial

**Achado confirmado:** `_ANISOTROP_LABEL_AGREEMENT_COLUMNS` cobria apenas três campos
(atom/asym/comp label) - `pdbx_label_seq_id=99` contra um átomo real `label_seq_id=1`, e
`type_symbol='O'` contra um átomo real `type_symbol='C'`, nunca eram comparados. Separadamente,
`_tensor_family_state` retornava `"absent"` sempre que a categoria não declarava as seis colunas
de um tensor como colunas - mesmo quando uma delas carregava um valor numérico real para a linha -
deixando uma família U genuinamente parcial (mas com colunas sequer declaradas) passar como se
fosse simplesmente ausente, desde que B estivesse completo.

**Correção:** `_ANISOTROP_LABEL_AGREEMENT_COLUMNS` passou de 3 para 12 pares - todo campo
`_atom_site_anisotrop` com uma contraparte `_atom_site` real e inequívoca (lida diretamente das
tabelas crude, nunca de `AtomObservation`, que não carrega todos esses campos):
`type_symbol`, `pdbx_pdb_ins_code`, `pdbx_pdb_model_num`, `pdbx_label_atom_id/asym_id/comp_id/seq_id/alt_id`,
`pdbx_auth_asym_id/seq_id/atom_id/comp_id`. Campos sem contraparte literal no catálogo de
`_atom_site` (`pdbx_pdb_residue_name`, `pdbx_pdb_residue_no`, `pdbx_pdb_strand_id`,
`pdbx_auth_alt_id`) foram deliberadamente deixados de fora - mapeá-los exigiria inventar uma
correspondência não literalmente declarada em nenhum dos dois catálogos.

`_tensor_family_state` não interrompe mais antecipadamente por colunas ausentes: lê cada uma das
seis como nula quando a categoria não a declara, exatamente como leria uma célula nula numa coluna
presente - uma família com qualquer valor numérico real em meio a colunas (declaradas ou não)
ausentes é `"partial"`, nunca `"absent"`, e é recusada independentemente do estado da outra
família.

**Testes:** `test_catalogue_anisotrop_rejects_informed_field_disagreement_and_undeclared_partial_tensor`
(novo - `pdbx_label_seq_id`/`type_symbol` divergentes recusados; campos concordantes
genuinamente informados aceitos; U parcial com colunas não declaradas e B completo recusado);
`test_real_fixture_1pfe_anisotrop_field_agreement_against_real_gemmi_tokens` (novo, prova nativa:
todas as linhas reais de `_atom_site_anisotrop` do depósito real 1PFE - que carrega
`pdbx_label_seq_id`/`pdbx_label_alt_id`/`pdbx_auth_*` genuínos, nunca exercidos pelo pipeline
completo porque este depósito já recusa antes, no gate de simetria não relacionado - são
verificadas diretamente contra o DOM real via Gemmi 0.7.5; uma mutação de `pdbx_label_seq_id`
sobre os tokens genuinamente decodificados é então recusada).

### R-CP2-03 (MAJOR/C-03) — verificação fechada da saída e fase real

**Achado confirmado:** `_verify_output_reparse` só percorria as categorias que alguma
`CategoryDecision` nomeava - uma categoria inteiramente não planejada no DOM reparseado (nunca
decidida, seja por um bug do serializador ou por conteúdo externo) passava sem nenhuma checagem.
Toda rejeição nesta função usava `phase="plan"`, nunca `"verify"`, mesmo sendo exatamente a etapa
de reparse independente pós-serialização.

**Correção:** antes do laço por decisão, o universo fechado esperado é calculado uma vez -
`{"entry"}` mais toda categoria que a própria decisão determinou escrever uma tabela não vazia
(`action` fora de `omit`/`guard_then_omit` e `kept_row_ordinals` não vazio). Qualquer categoria do
DOM reparseado fora desse conjunto gera `INVALID_OUTPUT` imediatamente, citando o nome exato da
categoria não planejada. Toda rejeição da função - a nova checagem e as seis já existentes - agora
usa `phase="verify"`.

**Testes:** `test_output_verification_rejects_mutated_token_before_commit` (existente, estendido
para confirmar `phase == "verify"`); `test_output_verification_rejects_entirely_unplanned_extra_category`
(novo - uma categoria `unplanned_category` no DOM reparseado é recusada citando seu próprio nome;
o mesmo reparse sem ela passa, provando que a nova checagem é aditiva, nunca mais estrita que o
necessário).

### R-CP2-04 (MINOR/evidência) — identidades finais e lineage por conteúdo

**Achado confirmado:** o teste de lineage das fixtures comparava apenas a *contagem* de linhas das
categorias não removidas entre original e recortado - uma contagem igual não prova conteúdo
intocado, exatamente como o recebimento aponta.

**Correção:** `test_real_fixture_originals_carry_removed_categories_outside_the_catalogue` agora
compara `RawCifCategory.columns` (os tokens crus, coluna por coluna, linha por linha) de toda
categoria não removida entre o original real e o recortado real - igualdade estrita, não apenas
contagem. O teste passa contra os seis depósitos reais, confirmando que as edições documentadas em
cada `PROVENANCE.json` removeram exatamente as categorias listadas e nada mais.

As identidades finais dos quatro arquivos da allowlist (§5) e a reconciliação de contagens (§6)
abaixo são computadas diretamente do commit publicado nesta correção, nunca reaproveitadas de um
relatório anterior.

## 4. O que foi implementado (apenas a allowlist)

Edição aditiva sobre o commit `5be1e443200cedddac0f97707963500a2edc6da6` (nunca reset/rebase/amend):
`src/molecular/receptor_materialization.py`, `src/molecular/receptor_parsing.py`,
`tests/test_receptor_materialization.py`, `tests/test_receptor_parsing.py`. Nenhum outro arquivo
do repositório tocado; nenhuma fixture nova ou modificada.

## 5. Identidades dos arquivos entregues (bytes do blob Git do commit publicado)

| Caminho | Linhas | Bytes | SHA-256 |
|---|---:|---:|---|
| `src/molecular/receptor_materialization.py` | 4547 | 222.455 | `f3fcdf4068614b626c74921d50daef13d0ca008b465be529b61f41c2d3db0421` |
| `src/molecular/receptor_parsing.py` | 1759 | 73.993 | `e526119706814e6c0b599337e75f7adccd47d368887b343fd6dbaa25cc3b5855` |
| `tests/test_receptor_materialization.py` | 2970 | 160.341 | `fbeadc3dd895862e36168dc515fc6348b193afd2e16c45c4ffb3aff447ba4e1a` |
| `tests/test_receptor_parsing.py` | 1486 | 65.023 | `eeb0e1ab089fa9ff1535f8bb89ef5abd63b87014522dcb4c6d537ef2dabfd2a5` |

Identidades recomputadas diretamente dos arquivos no working tree imediatamente após o commit
abaixo, nunca reaproveitadas do relatório/adendo anterior (que o próprio recebimento já apontou
como divergentes do blob real).

## 6. Reconciliação de coleta, foco, regressão e suíte completa

```
antes desta correção (HEAD 5be1e44):                   1658 coletados (1653 passed, 5 skipped)
após esta correção (HEAD a8d4667):                      1662 coletados (+4: um por R-CP2-01, dois
                                                          por R-CP2-02, um por R-CP2-03; R-CP2-04
                                                          fortaleceu um teste já existente, sem
                                                          adicionar um novo)

tests/test_receptor_parsing.py + tests/test_receptor_materialization.py:
  python -B -m pytest -p no:cacheprovider tests/test_receptor_parsing.py tests/test_receptor_materialization.py -q -rs
  -> 212 passed in ~5s

regressão 020 (inspection/selection/resolution/registry/service):
  python -B -m pytest -p no:cacheprovider tests/test_receptor_inspection.py tests/test_receptor_selection.py tests/test_receptor_resolution.py tests/test_receptor_registry.py tests/test_receptor_service.py -q -rs
  -> 121 passed in ~10s (inalterado)

suíte completa:
  python -B -m pytest -p no:cacheprovider -q -rs
  -> 1657 passed, 5 skipped in 158.92s

Os cinco skips (inalterados, discriminados): tests/test_application.py:1809 e :1847 (RDKit
instalado - comportamento esperado sem a extra), tests/test_atomic.py:1046 (criação de symlink não
permitida neste ambiente Windows - WinError 1314), tests/test_cli.py:4250 e :4303 (exigem ambiente
sem RDKit).
```

`git diff --check`/`git show --check` do commit publicado, limpos. `git diff --name-status` contra
`ea8dac9` (CP1 aprovado) e contra `08b797e` (main código) mostram exatamente os quatro caminhos da
allowlist mais a árvore de fixtures já publicada em `60f9e0d`/`b096af7` - nenhum arquivo novo,
nenhuma fixture tocada nesta correção. Os 92 testes de CP1/13 vetores-áureos e a regressão 020
permanecem intocados (121 passed, mesma contagem de antes).

## 7. Commit e publicação remota do código

```
commit a8d46675e1d1bab83c9f7824225699afae57bd4a
parent  5be1e443200cedddac0f97707963500a2edc6da6
branch  feature/increment-021-receptor-materialization
4 files changed, 515 insertions(+), 33 deletions(-)
```

Push confirmado: `git rev-parse origin/feature/increment-021-receptor-materialization` devolve
`a8d4667...`. `git rev-parse origin/main` (código) continua `08b797e...`; `git rev-parse origin/main`
(governance) continua `a47183d...`. Nenhum PR, merge, tag ou alteração de `main` em nenhum dos dois
repositórios.

## 8. Disposição C-01 a C-07 após esta correção

C-01/C-02/C-06 permanecem como fechados na entrega anterior (`5be1e44`), reconfirmados sem
alteração nesta correção. **C-03 e C-05 avançam de "mapeado" para produção efetivamente provada
nos pontos específicos que o recebimento identificou como pendentes** (verificação fechada de
categoria/fase real para C-03; contexto/contagem real de posições especiais e coerência
anisotrópica completa para C-05) - as demais exigências de C-03/C-05 já cobertas na entrega
anterior permanecem, sem reexame nesta correção estreita. C-04 permanece como fechado (bytes/
checksum/pin/import tardio - este último corrigido na correção anterior, `5be1e44`). C-07
(cobertura dos 79 cenários) não foi reexaminado linha a linha nesta correção estreita - os quatro
residuais instanciam partes concretas de C-05/C-03/C-07 que o recebimento considerou "mapeadas,
não fechadas"; esta correção fecha exatamente essas partes, nunca uma reafirmação genérica de que
os 79 cenários estão agora provados em sua totalidade.

## 9. O que não foi feito (fora do escopo autorizado)

- Nenhum CP3/CP4, nenhuma publicação de `receptor.cif` final, nenhum storage/registry/service/CLI.
- Nenhuma fixture nova além das seis já publicadas; nenhuma alteração do catálogo congelado.
- Nenhuma reexecução ou nova alegação sobre os 26 cenários antes "pendentes explícitos" além do
  que os quatro residuais tocam diretamente.
- `020-A` permanece em stand-by; itens locais protegidos de ambos os repositórios permanecem
  untracked e intocados; relatórios/branches anteriores (`claude/021-cp2-implementation-report`,
  `claude/021-cp2-completion-report`) preservados sem sobrescrita.
- Nenhum PR, merge, tag, release ou alteração de `main` em nenhum dos dois repositórios.
- Nenhum fechamento independente de CP2 é declarado por este relatório.

## 10. Gate sugerido

Os quatro residuais (R-CP2-01 a R-CP2-04) foram corrigidos e provados com testes de domínio puro
mais prova nativa Gemmi real contra os depósitos 1PFE/3DG1, sem alterar contrato, allowlist ou os
seis fixtures já publicados. Recomendo que o arquiteto confira esta correção (o diff
`5be1e44..a8d4667` é isolado aos quatro arquivos listados) e decida se o critério de conclusão do
CP2 está agora satisfeito para a revisão independente final, ou se algum ponto exige mais uma
rodada. Não declaro CP2 aprovado nem solicito avanço a CP3.

```
TASK_ID: 021-CHECKPOINT2-COMPLETION
ROLE: claude-implementer-separate-from-independent-reviewer
SCOPE_EXECUTED: CHECKPOINT2_RESIDUAL_CORRECTION (R-CP2-01 to R-CP2-04)
CODE_BRANCH: feature/increment-021-receptor-materialization
CODE_COMMIT: a8d46675e1d1bab83c9f7824225699afae57bd4a
CODE_COMMIT_PARENT: 5be1e443200cedddac0f97707963500a2edc6da6
READY FOR INDEPENDENT FINAL CP2 REVIEW: NO
CHECKPOINT2 APPROVED: NO
CHECKPOINT3 IMPLEMENTATION AUTHORIZED: NO
```
