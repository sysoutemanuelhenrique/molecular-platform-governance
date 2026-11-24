# Relatório de correção R-1 — Incremento 021, Checkpoint 1

Autor: Claude implementador (sessão separada da revisão independente e das sessões implementadoras anteriores). Data: 24/11/2026, America/Sao_Paulo.

## 1. Identificação da tarefa e confirmação de snapshots

- Tarefa: `tasks/021-CHECKPOINT1-R1-TEST-CORRECTION.json`, status `READY_FOR_MANUAL_HANDOFF_WITHIN_AUTHORIZED_CP1`, lida no snapshot de governance exato `771ae24f6289e41a2f8c7e17906bf294925bd375` (branch `docs/020-a-candidate1-review-20261020`) — HEAD remoto confirmado por `git ls-remote` antes de agir, sem divergência. `AGENTS.md`/`protocol/AGENT_WORKFLOW.md` conferidos byte a byte idênticos ao snapshot anterior via `diff` direto.
- Li a revisão final focal independente (`claude/021-cp1-final-focal-review-20261124 @ edb8764b4d4ee56e49ff849b65b950e5e430fae0`) e a resposta do arquiteto para R-1 (`increments/021/28-checkpoint1-r1-test-correction/CODEX_INCREMENT_021_CHECKPOINT1_R1_TEST_CORRECTION.md`), além do vetor documental `evidence/R1_ORDER_GOLDEN_VECTOR.json`.
- Código: `feature/increment-021-receptor-materialization` com HEAD **inicial** desta sessão em `bbd491e1a0b3fcb913c3549b004120693212df62` (confirmado por `git ls-remote` — coincide exatamente com `code_head_before_r1_correction` da tarefa). Main do código confirmada em `08b797e0985e123ffd4d7ca7e5a5e8f040e63851`, inalterada.
- Baseline local conferida: `git status --porcelain=v1` mostrou apenas os três itens protegidos; `020-A` não foi tocado.
- Coleta antes de qualquer edição: **1572 testes** (evidência em `evidence/claude-collect-before-r1-correction.txt`).

Nenhuma divergência de snapshot foi encontrada; a execução prosseguiu.

## 2. Ambiente real de execução

```
Python 3.14.7 | pytest 9.1.1 | pydantic 2.13.5 / pydantic_core 2.46.5
PyYAML 6.0.3 | gemmi 0.7.5 | rdkit 2026.3.6 | typer 0.27.2
Windows 11 x64, venv do próprio projeto (.venv) — o mesmo ambiente de todas as sessões anteriores deste CP1.
```

Evidência em `evidence/claude-environment.txt`.

## 3. Os doze fechamentos funcionais — preservados, não reabertos

Esta tarefa corrige exclusivamente **R-1**. Os doze achados fechados independentemente (ARCH-01, ARCH-02, ARCH-03, MAJOR-A, MAJOR-B, MINOR-1 a 7) e as três NOTES permanecem intactos — nenhuma linha fora de `tests/test_receptor_materialization.py` foi tocada. Os 13 goldens literais existentes e os 91 testes anteriores não foram modificados ou removidos.

## 4. R-1 — o que foi corrigido e por quê

A rodada de correções residuais anterior havia substituído, no teste `test_minor7_golden_atom_ids_key_preserves_given_order_independent_of_production`, o vetor original de dois átomos fora de ordem por um vetor de um único átomo — o nome do teste continuou afirmando preservação de ordem, mas a propriedade deixou de ser exercida. A revisão final focal confirmou, por mutação em cópia externa, que um mutante que ordena por `ordinal` dentro de `compute_atom_ids_key` deixou de ser detectado pelos 91 testes.

**Correção:** adicionei exatamente um teste novo, `test_atom_ids_key_preserves_given_order_against_ordinal_and_id_sorting`, em `tests/test_receptor_materialization.py`, mantendo o golden de um átomo e os 13 goldens literais existentes intocados. O novo teste usa o vetor documental do arquiteto — `(ordinal=3, atom_id="a")` seguido de `(ordinal=1, atom_id="Z")` — cuja ordem dada difere tanto da ordenação por `ordinal` quanto por `atom_id` (ASCII). Os bytes canônicos escritos à mão e os dois literais SHA-256 (`96fd3eac…` para a ordem dada, `bf820fe1…` para a ordem invertida — que é o resultado de **ambas** as ordenações indevidas, já que elas coincidem neste vetor) foram copiados exatamente do anexo `increments/021/28-checkpoint1-r1-test-correction/evidence/R1_ORDER_GOLDEN_VECTOR.json`, nunca calculados chamando produção.

Nenhuma linha de `src/molecular/receptor_materialization.py` foi alterada; sua identidade permanece exatamente `d8fc55db900f761f0debe4cea29f05cade1502ea1299937f123c6c883e30431d` (1.724 linhas, 78.807 bytes), conferida diretamente no blob do commit final (§6).

## 5. Prova de mutação — em cópia externa descartável, nada commitado

Antes de considerar o teste suficiente, construí duas cópias do arquivo de produção **fora do repositório** (`$SCRATCHPAD/r1_mutants/`), cada uma com uma única mutação em `compute_atom_ids_key`:

- `mutant_ordinal.py`: ordena o vetor por `ordinal` antes de montar o payload.
- `mutant_atomid.py`: ordena o vetor por `atom_id` antes de montar o payload.

Um script (`evidence/claude-r1-mutation-check.py`) carrega as três versões (produção original intocada + os dois mutantes) via `importlib`, sem tocar `sys.path` do projeto, e chama `compute_atom_ids_key` com o vetor exato do teste novo:

```
original:        MATCHES expected given-order literal
mutant_ordinal:   test would FAIL (detected); resultado == literal invertido
mutant_atomid:    test would FAIL (detected); resultado == literal invertido
```

Saída completa em `evidence/claude-r1-mutation-check.output.txt`. **Nenhum mutante foi commitado** — ambos os arquivos existem apenas na pasta de scratch desta sessão, nunca em `src/` nem staged no git.

## 6. Execução real, coleta e regressão

```
antes desta rodada:  python -B -m pytest --collect-only -q           -> 1572 tests collected
depois desta rodada: python -B -m pytest --collect-only -q           -> 1573 tests collected   (+1)
arquivo isolado:      python -B -m pytest tests/test_receptor_materialization.py -v
                                                                        -> 92 passed (91 anteriores + 1 novo, 0 parametrizações)
suíte completa:        python -B -m pytest -p no:cacheprovider -q -rs -> 1568 passed, 5 skipped, 103.55s
```

Os **5 skips são os mesmos de sempre**, nomeados (evidência em `evidence/claude-full-suite-after-r1-correction.txt`): dois em `test_application.py`, um em `test_atomic.py` (symlink sem privilégio neste host), dois em `test_cli.py`. Nenhum skip novo. Aritmética: 1572 + 1 = 1573 = 1568 passed + 5 skipped. `git diff --check` e `git show --check` limpos.

Diff restrito confirmado:

```
git diff --name-status bbd491e1a0b3fcb913c3549b004120693212df62..ea8dac9cdc203c337d7f3f9947b54042291f7484
  M  tests/test_receptor_materialization.py

git diff --name-status 08b797e0985e123ffd4d7ca7e5a5e8f040e63851..ea8dac9cdc203c337d7f3f9947b54042291f7484
  A  src/molecular/receptor_materialization.py
  A  tests/test_receptor_materialization.py
```

Nenhum outro arquivo foi tocado; `src/molecular/receptor_materialization.py` permanece com a mesma identidade de `bbd491e` em todo o histórico cumulativo. Evidência completa (log, stat, diff --name-status, ls-remote antes/depois) em `evidence/claude-git-log.txt`.

## 7. Identidades dos blobs commitados

| Caminho | Commit | Linhas | Bytes | SHA-256 |
|---|---|---:|---:|---|
| `src/molecular/receptor_materialization.py` (inalterado) | `ea8dac9c…` | 1.724 | 78.807 | `d8fc55db900f761f0debe4cea29f05cade1502ea1299937f123c6c883e30431d` |
| `tests/test_receptor_materialization.py` | `ea8dac9c…` | 1.676 | 83.570 | `9f72301ece6e55ef11d78d589f20822673887af10eeee1365d209099c3658ada` |

## 8. Commit e publicação remota

Um commit aditivo normal na **mesma branch existente**, com pai direto exatamente o HEAD inicial desta sessão:

```
commit ea8dac9cdc203c337d7f3f9947b54042291f7484   (parent bbd491e1a0b3fcb913c3549b004120693212df62)
  test: restore atom_ids_key order-preservation regression (R-1, increment 021)
  1 file changed, 31 insertions(+)
```

Staging explícito de apenas `tests/test_receptor_materialization.py` (nunca `git add -A`/`.`). Push normal, sem `--force`, fast-forward confirmado. `git ls-remote origin feature/increment-021-receptor-materialization` devolve `ea8dac9cdc203c337d7f3f9947b54042291f7484`. `git ls-remote origin main` continua devolvendo `08b797e0985e123ffd4d7ca7e5a5e8f040e63851` — **main inalterada**. Nenhum PR, merge, tag ou release.

## 9. O que não foi feito (fora do escopo autorizado)

- Nenhuma alteração em `src/molecular/receptor_materialization.py` — identidade byte a byte preservada.
- Nenhuma reabertura dos doze fechamentos funcionais, dos 43 cenários ou das três NOTES.
- Nenhum CP2/CP3/CP4; nenhum arquivo de fixture novo nem dependência nova.
- `020-A` permanece em stand-by; `Claude outputs/`, `_figura_curcumina/`, `increment-009-review.txt` permanecem untracked e intocados.
- Nenhum PR, merge, tag, release ou alteração de `main`; `STATUS.md`/tarefas centrais do governance não foram editados.
- R-1 **não** é declarado fechado independentemente por este relatório — essa é responsabilidade exclusiva da próxima reverificação independente, em sessão separada, restrita a R-1 e ao delta somente-teste.

## 10. Identidades deste relatório e das evidências

Publicadas em `evidence/claude-report-and-evidence-identities.json`, em commit separado — um arquivo não pode descrever seu próprio hash de commit antes de existir esse commit.

## 11. Gate sugerido

Correção pontual de R-1 entregue conforme a tarefa exata recebida, no único arquivo autorizado, na mesma branch, com a autorização humana original de CP1 já registrada. Próximo gate, conforme a própria tarefa: **o arquiteto recebe este código/relatório e prepara uma reverificação independente restrita a R-1 e ao delta somente-teste** — não presumo aprovação do CP1 nem avanço ao CP2.

```
TASK_ID: 021-CHECKPOINT1-R1-TEST-CORRECTION
ROLE: claude-implementer-separate-from-independent-reviewer
SCOPE_EXECUTED: R1_TEST_ONLY_WITHIN_AUTHORIZED_CP1
CODE_BRANCH: feature/increment-021-receptor-materialization
CODE_HEAD_BEFORE: bbd491e1a0b3fcb913c3549b004120693212df62
CODE_HEAD_AFTER: ea8dac9cdc203c337d7f3f9947b54042291f7484
PRODUCTION_FILE_SHA256_UNCHANGED: YES (d8fc55db900f761f0debe4cea29f05cade1502ea1299937f123c6c883e30431d)
CODE_PUSH_VERIFIED: YES
CODE_MAIN_MODIFIED: NO
PR_OPENED: NO
MERGE_PERFORMED: NO
TWELVE_PRIOR_CLOSED_FINDINGS_REOPENED: NO
R1_IMPLEMENTED: YES (one new test, literal vector, mutation-verified in external disposable copy)
R1_INDEPENDENTLY_CLOSED: NO
FULL_SUITE_PASSED: YES (1568 passed, 5 skipped, 1573 collected; +1 vs 1572 pre-round baseline)
CP2_IMPLEMENTATION_AUTHORIZED: NO
NEXT_GATE: ARCHITECT_RECEIPT_THEN_R1_ONLY_INDEPENDENT_REVERIFICATION_SEPARATE_SESSION
```
