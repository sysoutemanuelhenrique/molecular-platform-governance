# Relatório de correções residuais — Incremento 021, Checkpoint 1

Autor: Claude implementador (sessão separada da revisão independente e das duas sessões implementadoras anteriores). Data: 24/11/2026, America/Sao_Paulo.

## 1. Identificação da tarefa e confirmação de snapshots

- Tarefa: `tasks/021-CHECKPOINT1-RESIDUAL-CORRECTIONS.json`, status `READY_FOR_MANUAL_HANDOFF_WITHIN_AUTHORIZED_CP1`, lida no snapshot de governance exato `1bf4d4d1eefad1aa0ce3c693bf8738ab32344f54` (branch `docs/020-a-candidate1-review-20261020`) — HEAD remoto confirmado por `git ls-remote` antes de agir, sem divergência.
- Li integralmente, no mesmo snapshot: `AGENTS.md`, `protocol/AGENT_WORKFLOW.md` (ambos byte a byte idênticos ao snapshot anterior, conferido por `diff` direto), `STATUS.md`, a tarefa, a revisão focal independente (`claude/021-cp1-focal-review-20261124 @ 854ae336621116f7047033b5146c7c4834ebf9c2`) e a reconciliação residual do arquiteto (`increments/021/24-checkpoint1-residual-reconciliation/CODEX_INCREMENT_021_CHECKPOINT1_RESIDUAL_RECONCILIATION.md`), além dos 13 vetores de `evidence/DOCUMENTARY_GOLDEN_VECTORS.json`.
- Código: `feature/increment-021-receptor-materialization` com HEAD **inicial** desta sessão em `42b4804b5f4ea01ddf320c45473d8b4f980ea67e` (confirmado por `git ls-remote` antes de agir — coincide exatamente com `code_head_before_residual_corrections` da tarefa). Main do código confirmada em `08b797e0985e123ffd4d7ca7e5a5e8f040e63851`, inalterada.
- Baseline local conferida: `git status --porcelain=v1` mostrou apenas os três itens protegidos (`Claude outputs/`, `_figura_curcumina/`, `increment-009-review.txt`); `020-A` não foi tocado.
- Coleta antes de qualquer edição: **1556 testes** (evidência em `evidence/claude-collect-before-residual-corrections.txt`), reconciliando exatamente com `previous_supplied_results.total_collected` da tarefa.

Nenhuma divergência de snapshot foi encontrada; a execução prosseguiu.

## 2. Ambiente real de execução

```
Python 3.14.7 | pytest 9.1.1 | pydantic 2.13.5 / pydantic_core 2.46.5
PyYAML 6.0.3 | gemmi 0.7.5 | rdkit 2026.3.6 | typer 0.27.2
Windows 11 x64, venv do próprio projeto (.venv) — o mesmo ambiente de todas as sessões anteriores deste CP1; nenhuma instalação global, nenhuma mudança de pin.
```

Evidência completa em `evidence/claude-environment.txt`.

## 3. Os nove fechamentos independentes — preservados, não reabertos

Conforme a reconciliação residual, os seguintes achados permanecem **fechados**, sem qualquer alteração de código nesta sessão: **ARCH-01, ARCH-02, ARCH-03, MAJOR-B, MINOR-1, MINOR-2, MINOR-4, MINOR-5, MINOR-6**. As observações não bloqueantes do parecer focal (cruzamento `entity_id`/`label_entity_id` para o CP2, abrangência atual do índice NFC, duck typing coerente com ARCH-01) não geraram nenhuma mudança — são, pelo próprio parecer, não bloqueantes e fora do escopo desta tarefa. Os três NOTES (1/2/3) permanecem preservados sem edição. Os 43 cenários T021 continuam presentes com os mesmos nomes.

## 4. As três correções residuais

Exclusivamente nos dois arquivos já autorizados; nenhum outro arquivo tocado (§8). **Nenhuma destas correções é declarada fechada independentemente** — cada uma permanece `IMPLEMENTED_NOT_INDEPENDENTLY_CLOSED`; o fechamento pertence à próxima revisão focal curta, em sessão separada. Disposição completa com localização exata, testes e evidência de reprodução em `evidence/claude-residual-findings-dispositions.json`.

### 4.1 MAJOR-A residual — conferência de formato acquisition/declarado/detectado

`build_source_context` agora compara `protein_input.acquisition.raw_artifact.format` e `inspection_report.raw_format_declared`, ambos normalizados por `strip().lower()` e pelo mesmo mapa de quatro aliases que `receptor_inspection.py` já usa na baseline (`cif→mmcif, mmcif→mmcif, pdb→pdb, ent→pdb`) — projetado localmente no módulo puro novo (`_DECLARED_FORMAT_ALIASES`), nunca importado do 020 (preserva ARCH-01). Exige que os dois rótulos sejam reconhecidos, concordem entre si e com o `mmcif` detectado; qualquer contradição ou rótulo desconhecido recusa com `MaterializationConfigurationError(code="INVALID_RECORD")`. O aviso `declared-format-mismatch` que o 020 já pode carregar nunca é lido como autorização para materializar com proveniência contraditória; nada é reescrito ou reclassificado.

Reproduzi antes de corrigir, sobre o código intacto em `42b4804`, os nove estímulos exatos do parecer focal (pdb/pdb com detectado mmcif e o aviso presente; mmcif vs pdb nas duas direções; xyz/xyz; desconhecido só de um lado; aliases cif/mmcif cruzados; rótulos com espaço/maiúscula; controle coerente mmcif) e depois sobre o código corrigido — todos com o resultado esperado. Cinco testes permanentes cobrem esses casos.

### 4.2 MINOR-3 residual — unicidade intra-tupla e gramática de nomes de família

`CategoryDecision` agora recusa um ordinal repetido **dentro** de `kept_row_ordinals` ou de `omitted_row_ordinals` (antes só a sobreposição *entre* as duas tuplas era verificada — `(0,0)` passava). A validação de família de omissão trocou de `startswith(prefix)` para `re.fullmatch(r'(?:_pdbx_validate_|_pdbx_nmr_|_em_)[a-z0-9_]+', category)` — recusando prefixo nu, LF final, espaço embutido, nome de item (contém `.`), maiúsculas e caracteres de controle, nenhum dos quais `startswith` sozinho teria recusado. Não há deduplicação silenciosa, ordenação de reparo, parser CIF genérico ou campo novo.

Reproduzi os seis casos malformados exatos do parecer focal (mais um controle de caractere de controle) e os positivos nas três famílias, além dos controles que devem continuar válidos (omit vazio com fonte, filter com tag gerada, generate sem fonte). Três testes permanentes cobrem esses casos.

### 4.3 MINOR-7 residual — SHA-256 literais, envelopes completos, teste legado não tautológico

Os quatro testes golden pré-existentes comparavam `hashlib.sha256(bytes_escritos_à_mão).hexdigest()` **calculado em tempo de execução do teste** contra a produção — não um literal independente, exatamente como o parecer focal apontou. Agora cada um compara a produção contra uma constante de módulo (`_GOLDEN_*_SHA256`), com o `hashlib` sobre os bytes à mão usado apenas como conferência interna adicional, nunca como fonte do valor esperado da comparação principal. Nove testes novos cobrem os envelopes antes ausentes: `source_context_key`, `exclusions_key`, `outside_key`, `atom_decisions_key`, `category_decisions_key`, `plan_key`, `policy_id` e `request_key` — usando exatamente os 13 vetores documentais de `evidence/DOCUMENTARY_GOLDEN_VECTORS.json` (verificados 13/13 contra a produção intacta antes de escrever qualquer teste permanente; script e saída em `evidence/claude-golden-vectors-verification.py`/`.output.txt`).

O teste do `inspection_id` legado era tautológico: comparava o helper **antigo** (`receptor_inspection.compute_inspection_id`) contra uma constante de módulo também produzida por esse mesmo helper antigo — nunca chamava `_compute_legacy_inspection_id` (o helper novo). Agora ele chama o helper novo diretamente com os insumos exatos do vetor e compara ao literal independente `1c217d99e7b2b09d9c31a0c8f9daf056c48aa916bdf957cae83df449ad68e80c`; o helper antigo permanece como controle adicional, não substituto.

Nenhum algoritmo de hash foi alterado — o resíduo era de prova regressiva nos testes, não de produção, exatamente como a reconciliação determinou. Nenhuma dependência ou arquivo de fixture novo foi adicionado; os 13 vetores foram copiados como literais dentro do próprio arquivo de testes autorizado.

## 5. Execução real, coleta e regressão

```
antes desta rodada:  python -B -m pytest --collect-only -q           -> 1556 tests collected
depois desta rodada: python -B -m pytest --collect-only -q           -> 1572 tests collected   (+16)
arquivo isolado:      python -B -m pytest tests/test_receptor_materialization.py -v
                                                                        -> 91 passed (75 anteriores + 16 novos, 0 parametrizações)
suíte completa:        python -B -m pytest -p no:cacheprovider -q -rs -> 1567 passed, 5 skipped, 123.55s
```

Os **5 skips são os mesmos de sempre**, nomeados (evidência completa em `evidence/claude-full-suite-after-residual-corrections.txt`): dois em `test_application.py` (extra `rdkit` ausente), um em `test_atomic.py` (symlink sem privilégio neste host Windows), dois em `test_cli.py` (exigem ambiente sem RDKit). Nenhum skip novo. Aritmética: 1556 + 16 = 1572 = 1567 passed + 5 skipped. `git diff --check` e `git show --check` limpos.

Verificações adicionais exigidas pela tarefa, fora do pytest:

- **Import puro bloqueado, Gemmi e RDKit, sem stub, processo novo `-I -B`:** importa o módulo, instancia `AtomObservation`, calcula hash, constrói `SourceContext` e executa `build_materialization_plan` de ponta a ponta — `OK`, exit 0. Evidência em `evidence/claude-arch01-fresh-subprocess-check.txt`.
- **Conjunto fechado de códigos sob `python` normal e `-O`:** código desconhecido recusado nas duas classes de erro, nos dois modos; códigos válidos preservam `code`/`phase`. Evidência em `evidence/claude-minor6-python-O-check.txt`.

## 6. Diff restrito e identidade dos blobs commitados

```
git diff --name-status 42b4804b5f4ea01ddf320c45473d8b4f980ea67e..bbd491e1a0b3fcb913c3549b004120693212df62
  M  src/molecular/receptor_materialization.py
  M  tests/test_receptor_materialization.py

git diff --name-status 08b797e0985e123ffd4d7ca7e5a5e8f040e63851..bbd491e1a0b3fcb913c3549b004120693212df62
  A  src/molecular/receptor_materialization.py
  A  tests/test_receptor_materialization.py
```

Nenhum outro arquivo foi tocado. Identidades dos blobs **realmente commitados** (via `git show <commit>:<path> | sha256sum`, nunca bytes de disco Windows com CRLF):

| Caminho | Commit | Linhas | Bytes | SHA-256 |
|---|---|---:|---:|---|
| `src/molecular/receptor_materialization.py` | `bbd491e1…` | 1.724 | 78.807 | `d8fc55db900f761f0debe4cea29f05cade1502ea1299937f123c6c883e30431d` |
| `tests/test_receptor_materialization.py` | `bbd491e1…` | 1.645 | 81.362 | `e67539e76be9d174e7ef2c93cf971faa6bfba3316ef996f5e4a55c9345a90d69` |

## 7. Commit e publicação remota

Um commit aditivo normal na **mesma branch existente**, com pai direto exatamente o HEAD inicial desta sessão (sem reset/rebase/amend/force):

```
commit bbd491e1a0b3fcb913c3549b004120693212df62   (parent 42b4804b5f4ea01ddf320c45473d8b4f980ea67e)
  fix: apply three residual CP1 corrections from focal review (increment 021)
  2 files changed, 325 insertions(+), 46 deletions(-)
```

Push normal (`git push origin feature/increment-021-receptor-materialization`), sem `--force`, fast-forward confirmado. `git ls-remote origin feature/increment-021-receptor-materialization` devolve `bbd491e1a0b3fcb913c3549b004120693212df62`. `git ls-remote origin main` continua devolvendo `08b797e0985e123ffd4d7ca7e5a5e8f040e63851` — **main inalterada**. Nenhum PR, merge, tag ou release. Evidência completa (log, stat, diff --name-status, ls-remote antes/depois) em `evidence/claude-git-log.txt`.

## 8. O que não foi feito (fora do escopo autorizado)

- Nenhuma reabertura dos nove fechamentos independentes nem dos 43 cenários/3 NOTES — apenas as três correções residuais listadas na tarefa.
- Nenhum CP2/CP3/CP4; nenhum adapter Gemmi; nenhuma leitura real de `struct_conn`/simetria/catálogo físico/DOM.
- Nenhuma alteração em `pyproject.toml`, `atomic.py`, `activity.py`, `cli.py`, `receptor_parsing.py`, `receptor_inspection.py`, `receptor_resolution.py`, registries/modelos do 020.
- Nenhum arquivo de fixture novo nem dependência nova; os 13 vetores documentais foram copiados como literais no único arquivo de teste autorizado, nunca lidos do governance em tempo de teste.
- `020-A` permanece em stand-by; `Claude outputs/`, `_figura_curcumina/`, `increment-009-review.txt` permanecem untracked e intocados.
- Nenhum PR, merge, tag, release ou alteração de `main` em nenhum dos dois repositórios; `STATUS.md`/tarefas centrais do governance não foram editados.
- Nenhuma das três correções residuais foi declarada fechada independentemente; essa é responsabilidade exclusiva da próxima revisão focal, em sessão separada.

## 9. Identidades deste relatório e das evidências

Publicadas em `evidence/claude-report-and-evidence-identities.json`, em commit separado — um arquivo não pode descrever seu próprio hash de commit antes de existir esse commit.

## 10. Gate sugerido

Três correções residuais entregues conforme a tarefa exata recebida, nos mesmos dois arquivos, na mesma branch, com a autorização humana original de CP1 já registrada (sem nova aprovação alegada). Próximo gate, conforme a própria tarefa: **o arquiteto recebe este código/relatório e prepara uma revisão final curta, independente, dos três resíduos e de eventuais regressões no delta** — não presumo aprovação do CP1 nem avanço ao CP2.

```
TASK_ID: 021-CHECKPOINT1-RESIDUAL-CORRECTIONS
ROLE: claude-implementer-separate-from-independent-reviewer
SCOPE_EXECUTED: THREE_RESIDUAL_MINORS_ONLY_WITHIN_AUTHORIZED_CP1
CODE_BRANCH: feature/increment-021-receptor-materialization
CODE_HEAD_BEFORE: 42b4804b5f4ea01ddf320c45473d8b4f980ea67e
CODE_HEAD_AFTER: bbd491e1a0b3fcb913c3549b004120693212df62
CODE_PUSH_VERIFIED: YES
CODE_MAIN_MODIFIED: NO
PR_OPENED: NO
MERGE_PERFORMED: NO
NINE_PRIOR_CLOSED_FINDINGS_REOPENED: NO
THREE_RESIDUALS_IMPLEMENTED: YES (MAJOR-A format cross-check, MINOR-3 ordinal/family grammar, MINOR-7 literal goldens + non-tautological legacy test)
RESIDUALS_INDEPENDENTLY_CLOSED: NO
FULL_SUITE_PASSED: YES (1567 passed, 5 skipped, 1572 collected; +16 vs 1556 pre-round baseline)
CP2_IMPLEMENTATION_AUTHORIZED: NO
NEXT_GATE: ARCHITECT_RECEIPT_THEN_SHORT_INDEPENDENT_FOCAL_REVIEW_OF_THREE_RESIDUALS_SEPARATE_SESSION
```
