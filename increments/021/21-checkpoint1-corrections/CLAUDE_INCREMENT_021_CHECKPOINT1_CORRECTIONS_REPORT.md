# Relatório de correções — Incremento 021, Checkpoint 1

Autor: Claude implementador (sessão separada da revisão independente e da sessão de implementação original). Data: 24/11/2026, America/Sao_Paulo.

## 1. Identificação da tarefa e confirmação de snapshots

- Tarefa: `tasks/021-CHECKPOINT1-CORRECTIONS.json`, status `READY_FOR_MANUAL_HANDOFF_WITHIN_AUTHORIZED_CP1`, lida no snapshot de governance exato `521500c18272a379dc4fa2557754d9fa30d60cb7` (branch `docs/020-a-candidate1-review-20261020`) — HEAD remoto confirmado por `git ls-remote origin docs/020-a-candidate1-review-20261020` antes e durante o trabalho, sem divergência.
- Li integralmente, no mesmo snapshot: `AGENTS.md`, `protocol/AGENT_WORKFLOW.md`, `STATUS.md`, a tarefa, `increments/021/18-checkpoint1-architect-triage/CODEX_INCREMENT_021_CHECKPOINT1_TRIAGE.md`, `increments/021/20-checkpoint1-reconciliation/CODEX_INCREMENT_021_CHECKPOINT1_RECONCILIATION.md` e `evidence/DISPOSITIONS.json`. O parecer independente (`increments/021/19-checkpoint1-review/CLAUDE_INCREMENT_021_CHECKPOINT1_ADVERSARIAL_REVIEW.md` e suas cinco evidências) vive na branch própria do revisor `claude/021-cp1-adversarial-review-20261124 @ 2e36222b087134f9ba725bc2ad96c3ba39fb8801`, lido via `git show 2e36222...:<path>` — nunca mesclado, nunca editado por mim.
- Código: `feature/increment-021-receptor-materialization` com HEAD **antes** desta sessão em `711f3070765efe67a5799f939f1a18306ed8afdd` (confirmado por `git ls-remote origin` antes de agir — coincide exatamente com `code_head_before_corrections` da tarefa). Main do código confirmada em `08b797e0985e123ffd4d7ca7e5a5e8f040e63851`, inalterada.
- Baseline local do código conferida: `git status --porcelain=v1` mostrou apenas os três itens protegidos (`Claude outputs/`, `_figura_curcumina/`, `increment-009-review.txt`), sem alterações rastreadas/staged; `020-A` não foi tocado.
- `python -B -m pytest --collect-only -q` antes de qualquer edição: **1524 testes coletados** (evidência completa em `evidence/claude-baseline-collect-before-corrections.txt`), reconciliando exatamente com `supplied_original_cp1_collected` da tarefa.

Nenhuma divergência de snapshot foi encontrada; a execução prosseguiu.

## 2. Ambiente real de execução

```
Python 3.14.7
pytest 9.1.1
pydantic 2.13.5 / pydantic_core 2.46.5
PyYAML 6.0.3 | gemmi 0.7.5 | rdkit 2026.3.6 | typer 0.27.2
Windows 11 x64, venv do próprio projeto (.venv) — o mesmo ambiente aprovado da entrega original; nenhuma instalação global, nenhuma mudança de pin.
```

Evidência completa em `evidence/claude-environment.txt`.

## 3. O que foi corrigido

Exclusivamente nos dois arquivos já autorizados. Nenhum outro arquivo do repositório de código foi tocado (§6). Resumo por achado — disposição completa, localização exata da correção, testes e evidência independente de reprodução em `evidence/claude-findings-dispositions.json` (13 entradas: 4 MAJOR, 8 MINOR, 3 NOTE). **Nenhum achado é declarado fechado independentemente por este relatório** — cada um está marcado `IMPLEMENTED_NOT_INDEPENDENTLY_CLOSED`; o fechamento pertence à próxima revisão focal independente, em sessão separada.

| Achado | Severidade | O que mudou (resumo) |
|---|---|---|
| ARCH-01 | MAJOR | `receptor_inspection`/`receptor_resolution` movidos para `if TYPE_CHECKING:`; `compute_inspection_id` reimplementado localmente (`_compute_legacy_inspection_id`) sobre `promotion.compute_semantic_key` — mesmo backend/payload do helper antigo, sem acoplar o domínio ao Gemmi. |
| ARCH-02 | MAJOR | Chaves de disposição `(asym, CCD)` ausentes de M deixam de afetar a decisão polimérica em M; `present_asym_ccd_pairs` filtra antes da agregação por asym. |
| ARCH-03 | MINOR | `CategoryDecision.action="filter"` pode gerar tags (ex.: `_cell`/`_symmetry` com `generate_tags=['entry_id']`, exatamente como o catálogo congelado declara). |
| MAJOR-A | MAJOR | `build_source_context` passa a receber `ProteinInput`/`ReceptorSelectionPolicy` tipados; confere também o parser da inspeção, `structure_format` cruzado resolução×inspeção e o checksum de `acquisition.raw_artifact` contra o `raw_checksum` observado. |
| MAJOR-B | MAJOR | `PolicyRecord` autovalida `policy_id` contra H() do próprio payload; `build_policy_record` compara todos os campos de um `existing` com mesmo `policy_id` (exceto `declared_at`) antes de reutilizá-lo, recusando com `SOURCE_CHANGED` em caso de divergência. |
| MINOR-1 | MINOR | Guardas sobre o vetor de átomos: ordinal/atom_id globalmente únicos, `entity_id` sem contradição por asym, todo asym de S resolvido em M. |
| MINOR-2 | MINOR | Injetividade NFC estendida a todos os tokens `auth_asym_id` envolvidos em M (água/ligante inclusive), não só polímeros. |
| MINOR-3 | MINOR | `CategoryDecision`: categoria canônica do catálogo ou família de omissão aprovada (com `action="omit"`); ordinais não negativos; `omit`/`guard_then_omit` nunca retêm linha; `source_rows_key` obrigatório para `filter`/`omit`/`guard_then_omit`. |
| MINOR-4 | MINOR | `catalogue_sha256` fixado via `Literal` em `PlanBinding` e `PolicyRecord`; sensibilidade de `compute_request_key` a profile/algorithm/catalogue/engine testada explicitamente. |
| MINOR-5 | MINOR | Formato não-mmCIF na inspeção usa `INVALID_RECORD`, nunca `UNSUPPORTED_PLATFORM`. |
| MINOR-6 | MINOR | `assert` trocado por `raise` explícito nos dois construtores de erro — sobrevive a `python -O`. |
| MINOR-7 | MINOR | Testes com bytes canônicos escritos à mão, independentes da função de produção, para os envelopes de hash e para o `inspection_id` legado. |
| NOTE-1/2/3 | NOTE | Preservados como estavam — nenhuma mudança de contrato, nenhuma regressão de estritez, CLI/020 intocados (ver §9). |

### 3.1 Ressalva de ARCH-01 — observada e seguida

A reconciliação do arquiteto registrou explicitamente: *"Import tardio do módulo inspection dentro de build_source_context, sozinho, não basta para manter a função pura"* e recomendou tipos antigos apenas sob `TYPE_CHECKING` mais um backend puro compatível para o payload de sete campos. É exatamente o que foi implementado — nenhum import de `receptor_inspection`/`receptor_resolution` acontece em tempo de execução deste módulo, em nenhum ponto, condicional ou não; o backend de hash do `inspection_id` legado (`promotion.compute_semantic_key`) é o mesmo que `receptor_inspection.compute_inspection_id` já usava na baseline, confirmado byte a byte por teste (`test_minor7_golden_legacy_inspection_id_matches_the_020_production_helper`).

## 4. Prova independente de reprodução (antes de aceitar cada achado como corrigido)

Para cada achado, reproduzi primeiro o comportamento *com defeito* (sobre o código em `711f307`, antes de editar) usando os mesmos estímulos exatos do parecer independente, depois confirmei o comportamento *corrigido* sobre o código editado, antes de escrever qualquer teste permanente. Essas reproduções ad-hoc (scripts Python diretos, não pytest) estão resumidas em `evidence/claude-findings-dispositions.json`; os comandos/saídas completos de duas delas — a prova dinâmica de ARCH-01 e a prova de MINOR-6 sob `python -O` — estão em `evidence/claude-arch01-fresh-subprocess-check.txt` e `evidence/claude-minor6-python-O-check.txt`, por serem as duas únicas exigidas literalmente como `required_checks` da tarefa fora do pytest.

## 5. Reconciliação dos 43 cenários após as correções

Classificação do parecer independente antes desta sessão: **31 provados / 10 parciais / 2 lacunas**. Após as correções:

- **Lacunas fechadas (2 → 0):** T021-019 (ARCH-02, agora com teste bidirecional + controles) e T021-040 (ARCH-01, agora com prova dinâmica de subprocesso).
- **Parciais que avançam a provados (7):** T021-005/006 (MAJOR-A completo), T021-029 (bytes exercitado explicitamente), T021-030 (MAJOR-B completo), T021-035/160 (MINOR-4 completo), T021-161 (MINOR-3/ARCH-03 completos).
- **Parciais que permanecem parciais por desenho deliberado do CP1, não por defeito (3):** T021-018 (sem campo de altloc no DTO — uniformidade já é estrutural, por ocorrência, não por átomo; o próprio parecer independente chamou isso "aceitável no CP1"), T021-024 e T021-038 (a parte de `hydrog`/`metalc` depende de `struct_conn` real, que é CP2 — o parecer independente também classificou como "aceitável"). Nenhuma dessas três é um achado da lista de `required_changes`; não foram alteradas.

Resultado: **40 provados / 3 parciais-por-desenho / 0 lacunas**, dos mesmos 43 cenários, nenhum removido ou substituído.

## 6. Execução real, coleta e regressão

```
antes das correções:  python -B -m pytest --collect-only -q          -> 1524 tests collected
depois das correções: python -B -m pytest --collect-only -q          -> 1556 tests collected   (+32)
arquivo novo isolado: python -B -m pytest tests/test_receptor_materialization.py -v
                                                                       -> 75 passed (43 originais + 32 novos)
suíte completa:       python -B -m pytest -p no:cacheprovider -q -rs -> 1551 passed, 5 skipped, 157.27s
```

Os **5 skips são os mesmos da entrega original**, nominalmente identificados (evidência completa em `evidence/claude-full-suite-after-corrections.txt`):

1. `tests/test_application.py:1809` — só é significativo em instalação sem o extra `rdkit`.
2. `tests/test_application.py:1847` — mesma razão; nota explícita de que o import real de `rdkit` pelo `cli.py` não é o mesmo problema que `import rdkit` direto fora de `rdkit_tautomer.py`.
3. `tests/test_atomic.py:1046` — criação de symlink não permitida neste host Windows (`WinError 1314`, falta de privilégio).
4. `tests/test_cli.py:4250` — exige ambiente sem RDKit.
5. `tests/test_cli.py:4303` — exige ambiente sem RDKit.

Nenhum skip novo, nenhuma contagem herdada: 1524 (antes) + 32 (novos) = 1556 = 1551 passed + 5 skipped. `git diff --check` limpo em ambos os commits (`3ba2fa9` e `42b4804`), confirmado por `git show --check`.

## 7. Diff restrito e identidade dos blobs commitados

```
git diff --name-status 711f3070765efe67a5799f939f1a18306ed8afdd..42b4804b5f4ea01ddf320c45473d8b4f980ea67e
  M  src/molecular/receptor_materialization.py
  M  tests/test_receptor_materialization.py

git diff --name-status 08b797e0985e123ffd4d7ca7e5a5e8f040e63851..42b4804b5f4ea01ddf320c45473d8b4f980ea67e
  A  src/molecular/receptor_materialization.py
  A  tests/test_receptor_materialization.py
```

Nenhum outro arquivo (nenhum `pyproject.toml`, `atomic.py`, `cli.py`, `receptor_parsing.py`, `receptor_inspection.py`, `receptor_resolution.py`, registries/modelos do 020) foi tocado. Identidades dos blobs **realmente commitados** (via `git show <commit>:<path> | sha256sum`, não bytes de disco Windows com CRLF — ver nota de identidade no relatório original desta tarefa):

| Caminho | Commit | Linhas | Bytes | SHA-256 |
|---|---|---:|---:|---|
| `src/molecular/receptor_materialization.py` | `42b4804b…` | 1.669 | 75.461 | `ef38b524adbbe7432e83171d63c675856e3b21777322faec001efab530704fb1` |
| `tests/test_receptor_materialization.py` | `42b4804b…` | 1.421 | 67.030 | `7064aa8d7e36902f9e85a3ae4e075b118f8b5dd391029bf9652a53cbdd883eb8` |

## 8. Commits e publicação remota

Dois commits aditivos normais na **mesma branch existente**, a partir de `711f307` (sem reset/rebase/amend/force):

```
commit 3ba2fa91eaa95cae070d0aea7dba0d1918d9fd33   (parent 711f3070765efe67a5799f939f1a18306ed8afdd)
  fix: apply CP1 corrections from architect reconciliation (increment 021)
  2 files changed, 925 insertions(+), 67 deletions(-)

commit 42b4804b5f4ea01ddf320c45473d8b4f980ea67e   (parent 3ba2fa91eaa95cae070d0aea7dba0d1918d9fd33)
  test: strengthen MINOR-4/T021-029 evidence (increment 021 CP1 corrections)
  1 file changed, 23 insertions(+)
```

Push normal (`git push origin feature/increment-021-receptor-materialization`), sem `--force`, confirmado fast-forward em ambos os pushes. `git ls-remote origin feature/increment-021-receptor-materialization` devolve `42b4804b5f4ea01ddf320c45473d8b4f980ea67e`. `git ls-remote origin main` continua devolvendo `08b797e0985e123ffd4d7ca7e5a5e8f040e63851` — **main inalterada**. Nenhum PR, merge, tag ou release. Evidência completa (log, stat, diff --name-status, ls-remote antes/depois) em `evidence/claude-git-log.txt`.

## 9. O que não foi feito (fora do escopo autorizado)

- Nenhum CP2/CP3/CP4; nenhum adapter Gemmi; nenhuma leitura real de `struct_conn`/simetria/catálogo físico.
- Nenhuma alteração em `pyproject.toml`, `atomic.py`, `activity.py`, `cli.py`, `receptor_parsing.py`, registries/modelos do 020, módulos de ligante/tautômero.
- `020-A` permanece em stand-by; `Claude outputs/`, `_figura_curcumina/`, `increment-009-review.txt` permanecem untracked e intocados.
- Nenhum PR, merge, tag, release ou alteração de `main` em nenhum dos dois repositórios; `STATUS.md`/tarefas centrais do governance não foram editados.
- NOTE-3 (import do CLI com Gemmi na baseline 020) permanece registrada para o gate próprio do CP4, não corrigida aqui.
- Nenhum achado foi declarado fechado independentemente; essa é responsabilidade exclusiva da próxima revisão focal, em sessão separada.

## 10. Identidades deste relatório e das evidências

Publicadas em `evidence/claude-report-and-evidence-identities.json`, em commit separado deste mesmo arquivo — pela mesma razão da entrega original: um arquivo não pode descrever seu próprio hash de commit antes de existir esse commit.

## 11. Gate sugerido

Correções entregues conforme a tarefa exata recebida, nos mesmos dois arquivos, na mesma branch, com autorização humana já registrada (sem nova aprovação alegada). Próximo gate, conforme a própria tarefa: **o arquiteto recebe este código/relatório e prepara a revisão focal independente em snapshots imutáveis exatos, em sessão separada deste implementador** — não presumo avanço automático ao CP2, nem declaro o CP1 aprovado.

```
TASK_ID: 021-CHECKPOINT1-CORRECTIONS
ROLE: claude-implementer-separate-from-independent-reviewer
SCOPE_EXECUTED: CORRECTIONS_WITHIN_AUTHORIZED_CP1_ONLY
CODE_BRANCH: feature/increment-021-receptor-materialization
CODE_HEAD_BEFORE: 711f3070765efe67a5799f939f1a18306ed8afdd
CODE_HEAD_AFTER: 42b4804b5f4ea01ddf320c45473d8b4f980ea67e
CODE_PUSH_VERIFIED: YES
CODE_MAIN_MODIFIED: NO
PR_OPENED: NO
MERGE_PERFORMED: NO
FINDINGS_INDEPENDENTLY_CLOSED: NO
ALL_11_REQUIRED_CHANGES_IMPLEMENTED: YES (4 MAJOR + 8 MINOR, counting ARCH-01/02/03 among them)
SCENARIO_RECONCILIATION: 40_PROVED / 3_PARTIAL_BY_DESIGN / 0_GAP of 43
FULL_SUITE_PASSED: YES (1551 passed, 5 skipped, 1556 collected; +32 vs 1524 pre-correction baseline)
CP2_IMPLEMENTATION_AUTHORIZED: NO
NEXT_GATE: ARCHITECT_RECEIPT_THEN_INDEPENDENT_FOCAL_REVIEW_SEPARATE_SESSION
```
