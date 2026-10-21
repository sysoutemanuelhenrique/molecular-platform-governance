# Complemento do MAJOR-1 — Checkpoint 1, Incremento 020-A

Claude implementador, sessão separada da revisão. 21/10/2026.

Escopo exclusivo desta entrega: `tasks/020-A-CHECKPOINT1-MAJOR1-COMPLEMENT.json`
(status `AUTHORIZED`), restrito à remanescência do MAJOR-1 identificada pela
sonda do arquiteto sobre o HEAD publicado em 9ccdb98. Este relatório é um
complemento novo, em caminho próprio; o relatório de 514 linhas anterior
(`CLAUDE_CHECKPOINT1_CORRECTIONS_REPORT.md`, commit `a2c463f`) não foi editado
e permanece preservado. Nenhum dos quatro achados originais é declarado
fechado por este documento — essa é a reverificação independente focal ainda
pendente, fora do escopo desta entrega.

## 1. Identidades confirmadas antes de agir

Toda leitura de governance abaixo foi feita por `git show <sha>:<path>` no
snapshot imutável indicado pela tarefa, nunca pela main do governance:

| Insumo | Commit/SHA | SHA-256 do conteúdo | Linhas/bytes |
|---|---|---|---|
| `AGENTS.md`, `CLAUDE.md` | snapshot `2d0cd563...` | lidos integralmente | — |
| `STATUS.md` | snapshot `2d0cd563...` | `766ad9ad...003dc53fa` | 35/3079 |
| `tasks/020-A-CHECKPOINT1-MAJOR1-COMPLEMENT.json` | snapshot `2d0cd563...` | `ad30dac9...a70568eb5` | 93/6169 |
| `ARCHITECT_CORRECTIONS_RECEIPT_AND_MAJOR1_COMPLEMENT.md` | `2d0cd563...` | `202cd825...6bbe585cd45` | 54/6380 |
| `evidence/architect-post-correction-dto-probe.json` | `2d0cd563...` | `21ed216c...979874d98419614510` | 103/3221 |
| `CLAUDE_CHECKPOINT1_CORRECTIONS_REPORT.md` (preservado) | `a2c463f9bd4fd331c0338ed9b4d993e23a6bafa5` | `31bd9bc0...0e91eab649c5` | 514/31129 |
| `INCREMENT_020_A_FINAL_SPECIFICATION.md` (contrato congelado) | `665fb8b9cb4e1c7e0d0b9f1db98ec2adaa63bfed` | `cfbc6ea4...a9937386e9c` | 586/71904 |

Todos os seis SHA-256 acima foram recalculados nesta sessão sobre o
conteúdo efetivamente lido (`sha256sum`) e coincidem byte a byte com os
valores declarados em `MAJOR1_COMPLEMENT_IDENTITIES.json` e em
`tasks/020-A-CHECKPOINT1-MAJOR1-COMPLEMENT.json`. Nenhuma divergência de
identidade encontrada; nenhum impedimento registrado.

Confirmado também: `task.json.status == "AUTHORIZED"`,
`authorization_scope == "EXISTING_CHECKPOINT_1_MAJOR1_COMPLETION_ONLY"`,
`checkpoint1_approved/checkpoint2_authorized/checkpoint3_authorized == false`.
Não houve, portanto, nenhuma leitura ou revisão documental repetida além do
estritamente necessário para esta remanescência — o estudo e a revisão
adversarial original (`CLAUDE_CHECKPOINT1_ADVERSARIAL_REVIEW.md`) e a seção
completa do relatório corretivo anterior não foram relidos integralmente;
apenas a Seção 5.1 (a afirmação específica a corrigir) foi localizada e
citada.

### 1.1 Seção 11 do contrato congelado (trecho pertinente)

Linha 276: `input_state_id, entity_id | IDs validados; sujeitos ao registro
capturado`. Linhas 278/282/283: os três hashes de proveniência definidos como
hex64 (grafia do registro para o esperado, lowercase para os observados).
Linha 305: **"Identificadores/hashs são estritos; bool não é aceito como
inteiro de contagem."** Esta é a cláusula textual que a sonda do arquiteto e
a tarefa de complemento invocam; nenhuma interpretação nova foi necessária.

## 2. Gates e estado do worktree isolado do código — sem divergência

| Campo | Esperado pela tarefa | Observado |
|---|---|---|
| HEAD inicial do branch de código | `9ccdb9817a78f8de34c085c16443293b1ab99fd9` | Idêntico (worktree isolado `molecular-platform-020a-cp1`, antes de qualquer edição) |
| Main do código | `08b797e0985e123ffd4d7ca7e5a5e8f040e63851` | Idêntico (`origin/main` após fetch) |
| Branch de código | `feature/increment-020-a-molecular-characterization` | Idêntico |
| Allowlist deste complemento | `src/molecular/characterization.py`, `tests/test_characterization.py` | Respeitado — único diff |

Worktree isolado, sem checkout concorrente de outra tarefa; únicos
untracked eram os dois venvs locais (`.venv020a/`, `.venv020a-base/`),
nunca staged. Nenhuma divergência encontrada; a implementação procedeu.

## 3. Reprodução da remanescência, antes de qualquer edição

Comando e ambiente (worktree isolado, HEAD = `9ccdb98`):

```
.venv020a/Scripts/python.exe -c "<construção direta dos DTOs com bytes/bytearray>"
# Python 3.11.9 / Pydantic 2.14.1 / rdkit 2026.03.6
```

Resultado idêntico, em ambiente próprio, ao da sonda isolada do arquiteto
(`evidence/architect-post-correction-dto-probe.json`, Python
3.12.14/Pydantic 2.14.0): os seis campos abaixo aceitaram `bytes` de
conteúdo válido como string e os converteram silenciosamente para `str`.
Testado adicionalmente com `bytearray` (não cobrto pela sonda do
arquiteto, mas exigido pela tarefa) com o mesmo resultado.

| DTO.campo | `bytes` aceito? | `bytearray` aceito? |
|---|---|---|
| `CharacterizationValues.formula` | Sim → `str` | Sim → `str` |
| `CharacterizationProvenance.input_state_id` | Sim → `str` | Sim → `str` |
| `CharacterizationProvenance.entity_id` | Sim → `str` | — |
| `CharacterizationProvenance.state_record_sha256_observed` | Sim → `str` | Sim → `str` |
| `CharacterizationProvenance.representation_checksum_expected` | Sim → `str` | — |
| `CharacterizationProvenance.representation_checksum_observed` | Sim → `str` | — |

Evidência completa:
`evidence/claude-major1-complement-pre-fix-reproduction.json`
(79 linhas/3521 bytes, SHA-256 `97094cdb...0a836c44413d1e206`).

### 3.1 Errata da afirmação anterior sobre rejeição nativa de bytes

`CLAUDE_CHECKPOINT1_CORRECTIONS_REPORT.md` (commit `a2c463f`, preservado sem
edição), Seção 5.1, linhas 160–163, afirma: *"campos `str` simples já
rejeitam `int`/`bytes` nativamente no pydantic instalado, confirmado por
sonda própria antes de decidir não tocá-los — ver Seção 5.1.1"*. A Seção
5.1.1 (linha 174) declara que aquela sonda própria rodou em **Python
3.11.9/Pydantic 2.14.1** contra o HEAD então revisado `f8416b8` — o mesmo
par interpretador/pydantic desta reprodução, não apenas uma versão
compatível.

A reprodução desta sessão, no mesmo par Python/Pydantic, sobre o HEAD
publicado `9ccdb98` (descendente direto de `f8416b8`), **não confirma**
aquela afirmação para os seis campos acima: todos aceitaram `bytes` e
`bytearray`. A afirmação anterior não estava certa para esses campos
específicos, nesse mesmo ambiente — não é uma diferença de versão do
pydantic. Isto é um adendo a este novo relatório; o relatório de 514
linhas e sua Seção 5.1/5.1.1 não foram alterados.

É provável que a sonda própria original de `a2c463f` tenha testado apenas
os cinco exemplos literais/numéricos do achado original (os únicos
efetivamente corrigidos naquela entrega) e generalizado a conclusão "campos
`str` simples" sem testar `bytes`/`bytearray` contra os campos de
ID/hash especificamente — esta sessão não tem acesso ao código daquela
sonda para confirmar a causa exata, apenas ao resultado publicado e à sua
contradição direta pela reprodução acima.

## 4. Correção aplicada

Único mecanismo em `src/molecular/characterization.py`: um novo helper de
módulo `_require_strict_str`, seguindo exatamente o mesmo padrão já usado
por `_require_strict_bool`/`_require_strict_int`/`_require_strict_float`
(já presentes desde a correção anterior) — um `field_validator(...,
mode="before")` que verifica `type(value) is not str` e rejeita antes de
qualquer coerção/decodificação lax do pydantic ou de qualquer validador
`after` já existente (`validate_input_id`, verificação hex64).

Campos cobertos (exatamente os seis da tabela da Seção 3, nenhum além):

- `CharacterizationValues.formula`
- `CharacterizationProvenance.input_state_id`
- `CharacterizationProvenance.entity_id`
- `CharacterizationProvenance.state_record_sha256_observed`
- `CharacterizationProvenance.representation_checksum_expected`
- `CharacterizationProvenance.representation_checksum_observed`

Nenhuma mudança nos validadores `after` já existentes
(`_validate_id_format`, `_validate_observed_hash`,
`_validate_expected_hash_form`, `_validate_checksum_case_insensitive_match`),
nenhuma normalização de ID, nenhuma decodificação de bytes aceita, nenhum
protocolo geral de entrada externa introduzido, nenhuma dependência nova,
nenhum campo `Literal`/numérico tocado. `font_sha256_observed` e
`svg_sha256` (DrawingResult) usam o mesmo padrão de validador `after`
hex64 e **não foram tocados** nesta entrega: não constam do achado
reproduzido pela sonda do arquiteto nem da tabela da tarefa, e tocá-los
seria inventar um achado novo fora da autorização existente — registrado
aqui apenas como observação, sem ação de código.

## 5. Reprodução após a correção

Mesmo ambiente (`.venv020a`, Python 3.11.9/Pydantic 2.14.1/rdkit
2026.03.6), novo HEAD `3668207` (`36682074b55596d5632800bea98aff778eee885f`):
todos os seis campos agora levantam `pydantic.ValidationError` para
`bytes` e para `bytearray`; todos os controles positivos equivalentes em
`str` nativo continuam construindo e com round-trip JSON
(`model_dump_json`/`model_validate_json`) preservado. Evidência completa:
`evidence/claude-major1-complement-post-fix-reproduction.json`
(21 linhas/2396 bytes, SHA-256 `e03ce16c...4a4cf6a7a3bb3fecc13`).

Confirmado explicitamente, nesta reprodução e nos testes da Seção 6:
case-sensibilidade de `input_state_id`/`entity_id` preservada; grafia do
`representation_checksum_expected` preservada (incluindo `"AB"*32`
maiúsculo); `application_version=None` continua aceito; valores
científicos de `CharacterizationValues` (ex.: `molar_mass_g_mol`)
inalterados; nenhuma mudança de forma do JSON público.

## 6. Testes

### 6.1 Testes novos/reforçados (focais)

Arquivo: `tests/test_characterization.py`, seção nova "Checkpoint 1
MAJOR-1 complement" (comentário-cabeçalho explícito no arquivo).

| Função de teste | Parametrização | Itens coletados |
|---|---|---:|
| `test_values_formula_rejects_bytes_and_bytearray` | bytes, bytearray (loop interno) | 1 |
| `test_values_formula_accepts_native_str_control` | — | 1 |
| `test_provenance_id_and_hash_fields_reject_bytes_and_bytearray` | 5 campos × {bytes, bytearray} | 10 |
| `test_provenance_id_and_hash_fields_accept_native_str_control` | 5 campos | 5 |
| `test_major1_complement_preserves_contracted_invariants` | — | 1 |

Total de itens novos: **18**. Comando e resultado, isolados por `-k`:

```
.venv020a/Scripts/python.exe -m pytest tests/test_characterization.py \
  -k "bytes or formula_rejects or complement_preserves or native_str_control" -v
# 21 passed in 0.39s
```

(21 = os 18 itens novos + 3 itens pré-existentes cujo nome também casa com
o filtro `-k`, confirmados na saída real do pytest, não uma contagem
arredondada.)

### 6.2 `tests/test_characterization.py` completo

```
.venv020a/Scripts/python.exe -m pytest tests/test_characterization.py -v
# 173 passed in 0.49s          (com RDKit instalado)

.venv020a-base/Scripts/python.exe -m pytest tests/test_characterization.py -v
# 173 passed in 0.90s          (ambiente base, sem RDKit — T-020A-006 preservado)
```

Nenhum teste pré-existente de MAJOR-2/MINOR-1/MINOR-2 foi alterado; todos
permanecem na suíte e passam.

### 6.3 Suíte completa do projeto

```
.venv020a/Scripts/python.exe -m pytest
# 1757 passed, 5 skipped in 113.40s (0:01:53)
```

Python 3.11.9, pytest 9.1.1, pydantic 2.14.1, rdkit 2026.03.6 — versões
reais do ambiente de execução, declaradas, não assumidas. A base
reportada pelo implementador anterior para `9ccdb98` era 1739
passed/5 skipped (não reexecutada de forma independente pelo arquiteto,
conforme o próprio receipt). O delta observado nesta sessão é exatamente
+18 (1739 → 1757), coincidindo item a item com a contagem da Seção 6.1;
nenhum incremento foi predeterminado antes da coleta real.

## 7. Diffs e estado do working tree

```
git diff 9ccdb98..HEAD --stat
 src/molecular/characterization.py |  41 ++++++++++++++++
 tests/test_characterization.py    | 100 ++++++++++++++++++++++++++++++++++++++
 2 files changed, 141 insertions(+)
```

Exatamente os dois caminhos permitidos por este complemento; nenhum outro
arquivo tocado.

```
git diff f8416b8..HEAD --stat -- src/molecular/characterization.py \
  src/molecular/rdkit_tautomer.py tests/test_characterization.py \
  tests/test_rdkit_tautomer.py
 src/molecular/characterization.py | 247 ++++++++++++++++++++++++++--
 tests/test_characterization.py    | 284 ++++++++++++++++++++++++++++++++
 tests/test_rdkit_tautomer.py      | 337 +++++++++++++++++++++++++++++++++++++-
 3 files changed, 852 insertions(+), 16 deletions(-)
```

Diff cumulativo do incremento (desde o `feat` original `f8416b8`) sobre o
allowlist de quatro arquivos; `src/molecular/rdkit_tautomer.py` tem diff
vazio (0 linhas) desde `f8416b8` até este HEAD — inalterado, confirmado
também isoladamente (`git diff 9ccdb98..HEAD -- src/molecular/rdkit_tautomer.py
tests/test_rdkit_tautomer.py` vazio).

`git diff --check` sobre o diff deste complemento: sem erro de
whitespace; apenas os avisos de normalização de fim de linha LF/CRLF do
Git no Windows (`autocrlf`), não um erro de conteúdo.

`git status --short` no worktree isolado, pós-commit: apenas os dois
venvs locais untracked (`.venv020a/`, `.venv020a-base/`); nenhum outro
arquivo pendente; `increment-009-review.txt` e `_figura_curcumina/` do
usuário continuam intocados (não existem nesse worktree isolado) e, no
worktree principal do usuário, não foram tocados por esta sessão.

## 8. Commit e publicação

Novo commit, filho direto de `9ccdb9817a78f8de34c085c16443293b1ab99fd9`,
sem amend/rebase/reset/force:

```
commit 36682074b55596d5632800bea98aff778eee885f
parent 9ccdb9817a78f8de34c085c16443293b1ab99fd9
branch feature/increment-020-a-molecular-characterization
"fix: reject bytes/bytearray on characterization DTO str IDs and hashes
 (increment 020-A, checkpoint 1 MAJOR-1 complement)"
```

Push: `git push origin feature/increment-020-a-molecular-characterization`
→ `9ccdb98..3668207  feature/increment-020-a-molecular-characterization
-> feature/increment-020-a-molecular-characterization` (fast-forward, sem
force). Refs remotos verificados após `git fetch` subsequente:
`origin/feature/increment-020-a-molecular-characterization` =
`36682074b55596d5632800bea98aff778eee885f`; `origin/main` permanece
`08b797e0985e123ffd4d7ca7e5a5e8f040e63851`, inalterada.

Este relatório e as duas evidências novas são publicados em branch
própria do governance, `claude/020-a-checkpoint1-major1-complement-20261021`,
baseada no mesmo commit-raiz (`a47183dfec8213c765ed43ae482c8c227760a3d5`)
usado pela branch anterior do implementador (`claude/
020-a-checkpoint1-corrections-20261021`) — nunca na main do governance,
nunca sobrescrevendo a branch de revisão `docs/020-a-candidate1-review-
20261020`. Nenhum PR, merge, aprovação formal ou alteração de
configuração/visibilidade foi feito ou solicitado. `STATUS.md` e as
tarefas centrais do governance não foram editados por esta sessão.

## 9. Identidades de saída deste relatório

| Arquivo | Linhas | Bytes | SHA-256 |
|---|---:|---:|---|
| `evidence/claude-major1-complement-pre-fix-reproduction.json` | 79 | 3521 | `97094cdbc9c66d905c5ed133af18405d361bb740adb1fc06a836c44413d1e206` |
| `evidence/claude-major1-complement-post-fix-reproduction.json` | 21 | 2396 | `e03ce16cb828210cfc45ed9fd361ba58f87fd833a30da4a4cf6a7a3bb3fecc13` |
| `src/molecular/characterization.py` (estado final, código) | 1281 | 48908 | `135f4a34a0a4fa775f191ca1c9fc5180e38239298d38df6fad01da625eed62f8` |
| `tests/test_characterization.py` (estado final, código) | 1002 | 35213 | `1401604c05f9ef4d8450fdbbe26b8acaa658a3c666a3c1c3a7021b6791214054` |

(As linhas/bytes/SHA-256 deste próprio arquivo markdown serão os do commit
publicado; não auto-referenciados aqui para evitar um valor calculado
antes do conteúdo final do próprio arquivo.)

## 10. Declaração de não fechamento

Este complemento resolve exclusivamente a remanescência do MAJOR-1
reproduzida na Seção 3 (bytes/bytearray em IDs e hashes dos DTOs novos).
Nenhum dos quatro achados originais (MAJOR-1, MAJOR-2, MINOR-1, MINOR-2) é
declarado fechado por esta sessão. A reverificação independente focal dos
quatro achados contra este novo HEAD permanece o próximo gate, a cargo do
arquiteto/responsável — não iniciada nem presumida aqui.
`CHECKPOINT 1 APPROVED`, `CHECKPOINT 2 AUTHORIZED` e
`CHECKPOINT 3 AUTHORIZED` continuam `NO`.

---

**MAJOR-1 COMPLEMENT DELIVERED: YES**
**BYTES/BYTEARRAY REPRODUCTION (PRE-FIX): CONFIRMED**
**PRIOR "STR FIELDS REJECT BYTES NATIVELY" CLAIM: CORRECTED BY ERRATA (SECTION 3.1), PREVIOUS REPORT NOT EDITED**
**BYTES/BYTEARRAY REJECTION (POST-FIX): CONFIRMED, NATIVE STR CONTROLS AND JSON ROUND-TRIP PRESERVED**
**DIFF RESTRICTED TO ALLOWED PATHS: YES**
**NEW COMMIT DIRECT CHILD OF 9ccdb98, NO AMEND/REBASE/RESET/FORCE: YES**
**MAJOR-1 INDEPENDENTLY CLOSED: NO**
**FOCAL REVERIFICATION READY: PENDING ARCHITECT/RESPONSÁVEL — NOT DECLARED HERE**
**CHECKPOINT 1 APPROVED: NO**
**CHECKPOINT 2 AUTHORIZED: NO**
**CHECKPOINT 3 AUTHORIZED: NO**
