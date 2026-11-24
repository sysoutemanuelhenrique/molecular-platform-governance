# Relatório de implementação — Incremento 021, Checkpoint 1

Autor: Claude implementador (sessão separada da revisão independente). Data: 24/11/2026, America/Sao_Paulo.

## 1. Identificação da tarefa e autorização conferida

- Tarefa: `tasks/021-CHECKPOINT1-IMPLEMENTATION.json`, status `AUTHORIZED`, lida no snapshot de governance `3cda329b0e19a972d9858e26b58052873655ac07` (branch `docs/020-a-candidate1-review-20261020`), que é exatamente o HEAD remoto dessa branch no momento em que esta sessão começou a agir.
- Antes de agir, confirmei por `git show HEAD:<path> | sha256sum` (bytes do blob Git, sem conversão de final de linha) que os nove arquivos normativos coincidem byte a byte com os manifests:
  - `STATUS.md` — 37 linhas, 3.322 bytes, SHA-256 `98b26299697637c620e9f39709c3b068160f4c1ca162cf4adab02e27b85201c8`.
  - `tasks/021-CHECKPOINT1-IMPLEMENTATION.json` — 176 linhas, 8.244 bytes, SHA-256 `32efad47323a465da8b4270251968bdfbc67560c796f859670afd0ccda425f06`.
  - `increments/021/16-checkpoint1-preparation/OWNER_CHECKPOINT1_IMPLEMENTATION_AUTHORIZATION.md` — 55 linhas, 4.625 bytes, SHA-256 `589eb02982413e6461a59d8ec72ab468986b8d677bf3120cf43a88eaea756f18`.
  - `increments/021/16-checkpoint1-preparation/CHECKPOINT1_IMPLEMENTATION_BRIEF.md` — 64 linhas, 8.731 bytes, SHA-256 `c1c33e8eb206302399658f6bd5011655ee68a9f628aa49aff6d1108895c8bd64`.
  - `increments/021/15-final-specification/INCREMENT_021_FINAL_SPECIFICATION.md` — 377 linhas, 64.746 bytes, SHA-256 `5de705d609eaf158b0b29a99a0d02e24be4ed0b19d8e127c7e8d70c93aca1bd8`.
  - Quatro anexos normativos (`SCHEMAS_021.md`, `CATALOG_021.json`, `SCENARIOS_021.csv`, `IDENTITY_BASIS_CASES.json`) — todos coincidentes com `FROZEN_PACKAGE.json`/a tarefa, hashes já listados na tarefa e conferidos integralmente.
- Autorização humana: `OWNER_CHECKPOINT1_IMPLEMENTATION_AUTHORIZATION.md` registra a mensagem literal de Emanuel Henrique da Silva autorizando "implementação, testes, commit e push apenas dos dois arquivos permitidos, na branch feature/increment-021-receptor-materialization, partindo da baseline 08b797e0985e123ffd4d7ca7e5a5e8f040e63851", e a publicação do relatório em branch própria do governance. Reconheço explicitamente, como o próprio AGENTS.md instrui, que o uso da conta do responsável no commit de código (autor local configurado nesta máquina) não é, por si, prova de consentimento humano — esse consentimento está registrado textualmente no documento acima, não inferido do commit.

## 2. Conferência de HEAD remoto e estado local antes de agir

- `git ls-remote origin main` no repositório de código devolveu `08b797e0985e123ffd4d7ca7e5a5e8f040e63851`, idêntico ao baseline autorizado.
- `git ls-remote origin feature/increment-021-receptor-materialization` não retornou nada antes da implementação: a branch não existia nem local nem remotamente, confirmando que eu a criei.
- `git status --porcelain=v1` no repositório de código mostrou apenas os três itens locais protegidos (`Claude outputs/`, `_figura_curcumina/`, `increment-009-review.txt`), sem alterações rastreadas/staged. Esses três itens permanecem untracked e intocados após toda a sessão.
- `python -m pytest --collect-only -q` na baseline coletou **1481 testes**, 0 erros — evidência completa em `evidence/claude-baseline-pytest-collect.txt`.
- `src/molecular/receptor_materialization.py` e `tests/test_receptor_materialization.py` não existiam no baseline (`git show 08b797e...:<path>` retornou "does not exist").
- `src/molecular/receptor_inspection.py` (1012 linhas), `receptor_selection.py` (150 linhas), `receptor_resolution.py` (135 linhas) existem no baseline e foram lidos integralmente antes de implementar — não foram tocados por este checkpoint.

## 3. Ambiente real de execução

```
Python 3.14.7
pytest 9.1.1
pydantic 2.13.5 / pydantic_core 2.46.5
PyYAML 6.0.3
gemmi 0.7.5
rdkit 2026.3.6
typer 0.27.2
Plataforma: Windows 11 x64, venv do próprio projeto (.venv), sem instalação global/mudança de pin.
```

Ambiente completo em `evidence/claude-environment.txt`. Gemmi/RDKit estão instalados no venv do projeto mas **não são importados** pelo módulo novo (ver §6).

## 4. O que foi implementado

Apenas os dois caminhos da allowlist, ambos novos a partir da baseline:

- `src/molecular/receptor_materialization.py` — DTOs fechados/imutáveis/estritos (`strict=True` + `frozen=True` + `extra="forbid"` em todas as classes — necessário porque o modo lax do Pydantic v2 sozinho aceita `bool` em campo `int` e `bytes` em campo `str`, o que violaria a §12 do contrato), canonicalização/hash H(payload), e um planner puro que deriva S/D/U/X/O e constrói `PolicyRecord` com verificação de acknowledgements. Nenhum import de `gemmi`/`rdkit`, nenhuma leitura de arquivo, nenhuma chamada a `open()`/`Path()` em nenhuma linha de código do módulo (verificado por regex sobre o próprio texto-fonte no teste T021-040, evidência em `evidence/claude-new-tests-verbose.txt`).
- `tests/test_receptor_materialization.py` — 43 funções de teste, uma por cenário, chamando as funções/classes de produção reais com oráculos explícitos (nenhum `pytest.raises(Exception)`, nenhuma fachada de serviço, nenhum hash copiado do próprio algoritmo como única prova).

Nenhum outro arquivo do repositório de código foi criado, editado ou removido.

### 4.1 Decisões de design e seus limites (para a revisão independente)

Este checkpoint é estritamente domínio/DTO/planner puro — sem adapter Gemmi, sem leitura de RAW/YAML, sem storage. Isso exigiu decisões de fronteira que registro aqui com total transparência, para que o revisor as confronte deliberadamente contra o contrato congelado:

1. **`AtomObservation`** é o DTO de fronteira que o futuro adapter Gemmi (CP2) vai construir a partir do RAW; nesta entrega, apenas os testes de domínio o constroem diretamente em memória. Ele carrega exatamente os campos que o planner precisa para S/D/U/X/O (ordinal, atom_id, model, label_asym_id, entity_id, entity_type, ccd, label_seq_id, auth_asym_id, auth_seq_id, insertion_token) — não carrega coordenadas, ocupância, altloc ou B-factor, porque nenhuma decisão de CP1 depende desses campos (a uniformidade de altloc é estrutural: a decisão é por ocorrência/asym, nunca por átomo).
2. **`build_source_context`** faz a conferência cruzada de identidades (§5-6, T021-006/007/008) recebendo os quatro registros 020 já carregados em memória (incluindo `ReceptorInspectionReport` real) — nunca abre arquivo, nunca chama loader do 020. `raw_size_bytes` e os quatro `RecordSnapshot` (sha256/size_bytes dos bytes do YAML/RAW) são recebidos como parâmetros explícitos, porque medir esses bytes é responsabilidade do leitor de storage do CP2/CP3 (NOTE-F1, §5) — este checkpoint não promete tê-los medido de um arquivo real.
3. **Conexões (§9-10) não são computadas nesta entrega.** `PlanBinding.connection_decisions_key` é sempre o hash canônico de um vetor vazio (ainda assim dependente de `source_context_key`, de modo que o campo participa do hash de forma honesta). Nenhum cenário dos 43 de CP1 exige struct_conn/simetria — isso é explicitamente CP2 (T021-041 em diante). `ConnectionDecision`/`IdentityBasis`/`SymmetryClass` não foram implementados.
4. **`CategoryDecision`** foi implementado (para T021-161) apenas como DTO com suas invariantes de fechamento (arrays disjuntos, `action="omit"` com arrays vazios válido sem sentinela, `guard_then_omit` exige `omitted_tags` não vazio antes de aceitar a omissão). Nenhuma leitura real de catálogo/linha existe — isso é CP2 (§11).
5. Para os três códigos de erro onde o texto do CSV não nomeia explicitamente qual código da taxonomia do §16 se aplica (T021-020 "U=require-disposition sem disposição"; T021-013 colisão NFC; T021-039 tipo de entidade não suportado), usei `SELECTION_CONFLICT` e `UNSUPPORTED_REQUEST` por proximidade semântica dentro do conjunto fechado de `MaterializationInputError`. Não é ambiguidade de contrato científico — é apenas a escolha do código específico dentro de um taxonomia já fechada pelo próprio contrato; sinalizo explicitamente para a revisão independente confirmar ou propor outro código dentro do mesmo conjunto fechado, sem que isso implique reabrir o contrato.
6. `catalogue_sha256` é a constante fixa `8561039fd15137811b60316336dff04539df3732710dca6ec4009f23150d6d03` (os bytes exatos de `CATALOG_021.json`, conferido via `git show <freeze-commit>:.../CATALOG_021.json | sha256sum`), fixada no módulo — não lida de diretório corrente, não alterável pelo chamador.

Nenhuma dessas decisões altera o contrato congelado; todas ficam dentro do escopo que o §19/brief reservou a CP1 ("DTOs podem representar decisões/campos futuros, mas não implementar antecipadamente... loaders ou funções públicas de service dos CP2-4").

## 5. Cobertura dos 43 cenários

Matriz completa cenário→teste→alvo de produção→asserção→limite em `evidence/claude-scenario-matrix.json` (43 entradas, conferidas programaticamente contra a lista exata de IDs da tarefa: T021-001 a T021-040 e T021-159–161, sem duplicata e sem lacuna). Resumo por item executado nesta sessão:

```
python -m pytest tests/test_receptor_materialization.py -v
...
43 passed in 0.43s
```

(saída completa em `evidence/claude-new-tests-verbose.txt`). **43 cenários → 43 itens pytest coletados, 1:1, sem parametrização** — reconciliado explicitamente, não um número herdado.

## 6. Reconciliação da coleta, regressão e fronteira de domínio

```
baseline:        python -m pytest --collect-only -q  ->  1481 tests collected
após a entrega:  python -m pytest --collect-only -q  ->  1524 tests collected   (+43, exatamente os novos)
suíte completa:  python -m pytest -q                  ->  1519 passed, 5 skipped in 161.00s
```

Os 5 skips já existiam na baseline (nenhum skip novo introduzido pelos dois arquivos novos — os 43 itens novos todos passaram, 0 skip). Evidência completa em `evidence/claude-full-suite-after.txt`. Nenhum teste existente foi editado; a regressão cumulativa (017/018/019/020 e os demais 1481 itens da baseline) passou integralmente nesta mesma execução real, sem contagem herdada.

`git diff --check` não reportou problema de whitespace. `git diff --name-status 08b797e0985e123ffd4d7ca7e5a5e8f040e63851 feature/increment-021-receptor-materialization` mostrou exatamente:

```
A	src/molecular/receptor_materialization.py
A	tests/test_receptor_materialization.py
```

— nenhum outro arquivo (nenhum `atomic.py`, `pyproject.toml`, registries/modelos do 020, `activity.py`, módulos de ligante/tautômero) foi tocado.

## 7. Identidades dos arquivos entregues (código)

| Caminho | Linhas | Bytes | SHA-256 |
|---|---:|---:|---|
| `src/molecular/receptor_materialization.py` | 1418 | 60.988 | `b4a596965f80b5a2a8e5e6ceabff55db72f649f7a23241e816e4be04b51b0357`... *(ver nota)* |
| `tests/test_receptor_materialization.py` | 791 | 38.848 | `5fd9a8bd1cad78ca5d81db3dd9c64d82426fef1ec629280c2b397fcca8bcd618`... *(ver nota)* |

**Nota de correção de contagem de bytes:** os valores acima vêm de `wc -lc`/`sha256sum` sobre o arquivo já materializado no disco Windows deste checkout (sem `core.autocrlf` aplicado neste repositório de código — confirmado: `git diff --check` limpo e `git show <commit>:<path> | wc -lc` abaixo reproduz os mesmos bytes do blob Git, portanto não há divergência CRLF/LF neste repositório, ao contrário do que se observou no repositório de governance). Os hashes exatos, recomputados diretamente do blob publicado no commit `711f3070765efe67a5799f939f1a18306ed8afdd`, são:

```
git show 711f3070765efe67a5799f939f1a18306ed8afdd:src/molecular/receptor_materialization.py | sha256sum
  -> b4a596965f80b5a2a8e5e6ceabff55db72f649f7a23241e816e4be04b51b0357
git show 711f3070765efe67a5799f939f1a18306ed8afdd:tests/test_receptor_materialization.py | sha256sum
  -> 5fd9a8bd1cad78ca5d81db3dd9c64d82426fef1ec629280c2b397fcca8bcd618
```

## 8. Commit e publicação remota do código

- Branch criada a partir da baseline exata (`git branch feature/increment-021-receptor-materialization` com `HEAD == 08b797e0985e123ffd4d7ca7e5a5e8f040e63851` no momento da criação).
- Staging explícito de apenas os dois caminhos (`git add src/molecular/receptor_materialization.py tests/test_receptor_materialization.py`) — nunca `git add -A`/`.`.
- Commit normal (sem `--amend`/`--no-verify`/`-c commit.gpgsign=false`):

```
commit 711f3070765efe67a5799f939f1a18306ed8afdd
parent 08b797e0985e123ffd4d7ca7e5a5e8f040e63851 (= baseline exata)
branch feature/increment-021-receptor-materialization
2 files changed, 2209 insertions(+), 0 deletions(-)
```

- Push: `git push origin feature/increment-021-receptor-materialization` — **sucesso**, confirmado por `git ls-remote origin feature/increment-021-receptor-materialization` devolvendo `711f3070765efe67a5799f939f1a18306ed8afdd`. `git ls-remote origin main` depois do push ainda devolve `08b797e0985e123ffd4d7ca7e5a5e8f040e63851` — main remota **inalterada**.
- **Nenhum PR foi aberto, nenhum merge, nenhuma tag/release, nenhuma aprovação formal no GitHub.** O link de "Create a pull request" que o próprio `git push` imprime no console não foi utilizado.
- Evidência completa (log, diff --name-status, ls-remote antes/depois) em `evidence/claude-git-log.txt`.

## 9. O que não foi feito (fora do escopo autorizado)

- Nenhum CP2/CP3/CP4: nenhum adapter Gemmi, nenhuma leitura de `struct_conn`/simetria, nenhum storage/registry/service/CLI, nenhuma fixture física em `tests/fixtures/receptor_materialization/`.
- Nenhuma alteração em `pyproject.toml`, `atomic.py`, `activity.py`, registries/modelos do 020, módulos de ligante/tautômero.
- `020-A` permanece em stand-by, sem retomada; `Claude outputs/`, `_figura_curcumina/`, `increment-009-review.txt` permanecem untracked e intocados.
- Nenhum PR, merge, tag, release ou alteração de `main` em nenhum dos dois repositórios.
- Nenhuma automação/dispatch foi configurada ou acionada.

## 10. Identidades deste próprio relatório e das evidências

Calculadas após a escrita final deste arquivo e publicadas separadamente em `evidence/claude-report-and-evidence-identities.json` (o próprio relatório não pode se autoidentificar antes de terminar de ser escrito — por isso o manifesto de identidades é um arquivo irmão, não uma seção editada post-hoc deste documento).

## 11. Gate sugerido

Entrega de CP1 completa e publicada conforme a autorização exata recebida. Próximo gate, conforme a própria tarefa: **triagem do arquiteto e revisão independente do CP1 em sessão separada deste implementador** — não solicito nem presumo avanço automático ao CP2. Os itens da §4.1 acima (escolhas de código de erro dentro do taxonomia fechada; `AtomObservation` como fronteira de teste; conexões/catálogo não computados) são os pontos que mais se beneficiam de atenção explícita da revisão independente, por não estarem nomeados literalmente pelo CSV/contrato com uma única leitura possível.

```
TASK_ID: 021-CHECKPOINT1-IMPLEMENTATION
ROLE: claude-implementer-separate-from-independent-reviewer
SCOPE_EXECUTED: CHECKPOINT1_ONLY
CODE_BRANCH: feature/increment-021-receptor-materialization
CODE_COMMIT: 711f3070765efe67a5799f939f1a18306ed8afdd
CODE_PARENT: 08b797e0985e123ffd4d7ca7e5a5e8f040e63851
CODE_PUSH_VERIFIED: YES
CODE_MAIN_MODIFIED: NO
PR_OPENED: NO
MERGE_PERFORMED: NO
CP2_IMPLEMENTATION_AUTHORIZED: NO
43_SCENARIOS_MAPPED_TO_REAL_TESTS: YES (1:1, no inflation)
FULL_SUITE_PASSED: YES (1519 passed, 5 skipped, 1524 collected; +43 vs 1481 baseline)
NEXT_GATE: ARCHITECT_TRIAGE_THEN_INDEPENDENT_CP1_REVIEW_SEPARATE_SESSION
```
