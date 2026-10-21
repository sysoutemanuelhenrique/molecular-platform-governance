# Fechamento do MAJOR-1 — matriz completa de 17 campos, Checkpoint 1, Incremento 020-A

Claude implementador, sessão separada do revisor independente. 21/10/2026.

Escopo exclusivo desta entrega: `tasks/020-A-CHECKPOINT1-MAJOR1-STRING-CLOSURE.json`
(status `AUTHORIZED`), que substitui `020-A-CHECKPOINT1-MAJOR1-COMPLEMENT` como
tarefa ativa para o mesmo MAJOR-1 — não um achado novo, não uma ampliação de
escopo. Este relatório é um documento novo, em caminho próprio; nenhum
relatório anterior (o de 514 linhas `a2c463f` e o de 332 linhas `07185ab`)
foi editado, e ambos permanecem preservados e citados abaixo. Nenhum dos
quatro achados originais é declarado fechado aqui.

## 1. Identidades confirmadas antes de agir

Leitura feita por `git show <sha>:<path>` sobre o snapshot imutável
`0b499f8aee9273ea4df6825cf760d8ca5c665e56`, nunca pela main do governance:

| Insumo | SHA-256 recalculado nesta sessão | Linhas/bytes |
|---|---|---|
| `STATUS.md` | `3582cfebee7f65ad08ba6e4fe22004efa69a9e911520cc4d9a16def6467fbb9a` | 35/2865 |
| `tasks/020-A-CHECKPOINT1-MAJOR1-STRING-CLOSURE.json` | `7d66136f4c6e0442133628e9105a3fa5277a5293eae426c5ad0f15c9e7372eb1` | 132/8015 |
| `ARCHITECT_MAJOR1_COMPLEMENT_RECEIPT_AND_COMPLETE_STRING_MATRIX.md` | `6f8534349160230c7edcafe2ea4fe096f38006dde49085a5f34246f0fdc0436c` | 66/7842 |
| `evidence/architect-complete-string-matrix.json` | `2b8ea026f56f98eda11da234d1ab33d17ef21629ce0dfc14bf9c43bfeda5b3fb` | 658/17218 |
| `evidence/architect-complete-string-matrix-probe.py` | `2d4dff1a02101386e7d455d0f5bc673a91272fb6ef1c7b15830e16a6cdfb4cbc` | 116/6473 |

Todos os cinco SHA-256 coincidem byte a byte com
`MAJOR1_STRING_CLOSURE_IDENTITIES.json` e com os valores embutidos na
própria tarefa. Confirmado: `status == "AUTHORIZED"`,
`authorization_scope == "EXISTING_CHECKPOINT_1_MAJOR1_COMPLETION_ONLY"`,
`supersedes_active_task == "020-A-CHECKPOINT1-MAJOR1-COMPLEMENT; previous
delivery preserved, partial for same finding"`, os três
`checkpointN_authorized` em `false`. Nenhuma divergência; nenhum
impedimento registrado. O relatório do complemento anterior (`07185ab`,
332 linhas/17.224 bytes, SHA-256 `cc9d9ada...`) e o recibo anterior do
arquiteto também foram relidos por referência de identidade (já
verificados na sessão anterior, não reabertos aqui); apenas a Seção 4 do
relatório anterior foi relocalizada para a clarificação da Seção 3 abaixo.

## 2. Gates do código — sem divergência

| Campo | Esperado pela tarefa | Observado |
|---|---|---|
| HEAD inicial do branch | `36682074b55596d5632800bea98aff778eee885f` | Idêntico (worktree isolado, antes de qualquer edição) |
| Parent esperado do HEAD inicial | `9ccdb9817a78f8de34c085c16443293b1ab99fd9` | Idêntico |
| Main do código | `08b797e0985e123ffd4d7ca7e5a5e8f040e63851` | Idêntico (`origin/main`) |
| Allowlist | `src/molecular/characterization.py`, `tests/test_characterization.py` | Respeitado — único diff |

Únicos untracked no worktree isolado: os dois venvs locais (`.venv020a/`,
`.venv020a-base/`), nunca staged. `increment-009-review.txt` e
`_figura_curcumina/` do usuário não existem nesse worktree e não foram
tocados em nenhum momento desta sessão.

## 3. Clarificação sobre a interpretação anterior (hashes do DrawingResult)

O relatório do complemento anterior (`07185ab`, Seção 4) decidiu **não**
corrigir `DrawingResult.font_sha256_observed`/`svg_sha256`, por entender
que isso "seria inventar um achado novo fora da autorização existente",
já que a tabela da sonda anterior listava apenas seis campos.

O recibo do arquiteto para esta tarefa (`ARCHITECT_MAJOR1_COMPLEMENT_
RECEIPT_AND_COMPLETE_STRING_MATRIX.md`, Seção "Disposição da entrega e do
escopo") contesta essa leitura: a tarefa anterior exigia textualmente
*"applicable ordinary-str fields in the new DTOs, particularly IDs and
all hashes"* e testes para *"other applicable ordinary-string DTO
fields"* — os seis exemplos demonstrados não eram uma allowlist de
campos a corrigir, apenas os exemplos então reproduzidos; a allowlist de
**escrita** era (e continua sendo) os dois arquivos, nunca um subconjunto
de campos do DTO. A especificação congelada, §11, já exigia DTOs públicos
estritos e "Identificadores/hashs são estritos" sem qualificar "hash" a
um subconjunto.

Esta sessão concorda com essa correção de leitura: a decisão de escopo do
relatório anterior não estava certa. Os dois hashes de `DrawingResult`
são corrigidos nesta entrega (Seção 5), junto com os outros nove campos
remanescentes que a tarefa torna explícitos. Isso não reabre o relatório
anterior nem o edita — é um esclarecimento publicado aqui, no documento
novo autorizado para esta rodada.

## 4. Reprodução da remanescência completa, antes de qualquer edição

Comando e ambiente (worktree isolado, HEAD = `36682074...`, Python
3.11.9/Pydantic 2.14.1/rdkit 2026.03.6): construção direta de cada um dos
11 campos remanescentes com `bytes`/`bytearray` de conteúdo válido como
string, por **construtor e por `model_validate(dict)`** (4 ensaios por
campo, mesma metodologia da sonda do arquiteto, módulo real, sem
monkeypatch, sem `model_construct`).

| DTO.campo | Resultado observado |
|---|---|
| `DrawingResult.font_name` | Converte nos 4 ensaios |
| `DrawingResult.font_sha256_observed` | Converte nos 4 ensaios |
| `DrawingResult.svg_sha256` | Converte nos 4 ensaios |
| `DrawingResult.xml_parser_version_observed` | Converte nos 4 ensaios |
| `CharacterizationProvenance.representation_path` | Converte nos 4 ensaios |
| `CharacterizationProvenance.representation_format_declared` | Converte nos 4 ensaios |
| `CharacterizationProvenance.engine_version` | Converte nos 4 ensaios |
| `CharacterizationProvenance.application_version` | Converte nos 4 ensaios |
| `MolecularCharacterizationResult.svg` | Converte nos 4 ensaios |
| `RDKitCharacterizationOutcome.engine_version` | Converte nos 4 ensaios |
| `RDKitCharacterizationOutcome.svg` | Converte nos 4 ensaios |

44/44 ensaios aceitaram o tipo indevido e retornaram `str`, confirmando
exatamente `evidence/architect-complete-string-matrix.json`
(`fields_rejecting_all_four_trials: 6`,
`fields_accepting_all_four_trials: 11`) no ambiente próprio do
implementador. Evidência completa:
`evidence/claude-major1-string-closure-pre-fix-reproduction.json`
(26 linhas/3517 bytes, SHA-256 `652dfde7...508e015f8036ec`).

Os seis campos já corrigidos no complemento anterior (`3668207`) foram
reconfirmados como já recusando `bytes`/`bytearray`, sem regressão —
não repetidos nesta tabela.

## 5. Correção aplicada

Mesmo mecanismo das entregas anteriores em `src/molecular/
characterization.py`: `field_validator(..., mode="before")` usando o
helper já existente `_require_strict_str`, agora também aplicado a:

- `DrawingResult.font_name`, `font_sha256_observed`, `svg_sha256`,
  `xml_parser_version_observed`
- `CharacterizationProvenance.representation_path`,
  `representation_format_declared`, `engine_version`

Para os três campos contratualmente nulos (`str | None`), um novo helper
`_require_strict_str_or_none` (passa `None` adiante; delega a
`_require_strict_str` para qualquer valor não nulo), aplicado a:

- `CharacterizationProvenance.application_version`
- `MolecularCharacterizationResult.svg`
- `RDKitCharacterizationOutcome.svg`

`RDKitCharacterizationOutcome.engine_version` recebeu o mesmo
`_require_strict_str` (não nulo). Nenhum validador `after` existente foi
alterado; nenhum campo `Literal`/numérico tocado; nenhuma normalização de
conteúdo introduzida; nenhum protocolo geral de entrada externa; nenhuma
dependência nova; nenhuma mudança na forma do JSON público, no adaptador,
nos leitores, no serviço ou na CLI.

Com esta entrega, os 17 campos de `evidence/architect-complete-string-
matrix.json` estão todos cobertos: os 6 do complemento anterior
(preservados, reconfirmados, Seção 4) e os 11 desta tarefa.

## 6. Reprodução após a correção

Mesmo ambiente, novo HEAD `cc903d8` (`cc903d8ebbfe1916c3fce195d20fc97b206a5f54`):
todos os 44 ensaios (11 campos × {bytes, bytearray} × {construtor,
model_validate}) agora levantam `pydantic.ValidationError`, com o erro
localizado exatamente no campo-alvo (`error["loc"] == (field,)`, a mesma
asserção de localização que a sonda do arquiteto usa). Todos os 11
controles positivos em `str` nativa continuam construindo, com round-trip
JSON preservado; os três controles de null contratado
(`application_version=None`;
`MolecularCharacterizationResult.svg`/`drawing=None`;
`RDKitCharacterizationOutcome.svg`/`drawing=None`) continuam aceitos;
grafia/case de IDs e do checksum esperado inalterados; valores
científicos inalterados. Evidência completa:
`evidence/claude-major1-string-closure-post-fix-reproduction.json`
(26 linhas/1656 bytes, SHA-256 `7bb0fcb5...9f16f99c3c7b07ac60cd104`).

## 7. Testes

### 7.1 Testes novos (regressão da matriz completa)

Arquivo: `tests/test_characterization.py`, nova seção "Checkpoint 1
MAJOR-1 string closure".

| Função de teste | Parametrização | Itens coletados |
|---|---|---:|
| `test_complete_17_field_string_matrix_rejects_bytes_and_bytearray_everywhere` | 17 campos (os 6 já corrigidos + os 11 desta entrega), cada um exercitando `bytes`/`bytearray` × construtor/`model_validate` internamente, mais controle de str nativa + round-trip JSON | 17 |
| `test_string_closure_three_contracted_null_controls_still_accepted` | — | 1 |

Total de itens novos: **18**. Nenhum teste anterior de MAJOR-1 (seis
campos), MAJOR-2, MINOR-1 ou MINOR-2 foi removido ou enfraquecido; todos
permanecem na suíte e passam.

Comando e resultado:

```
.venv020a/Scripts/python.exe -m pytest tests/test_characterization.py \
  -k "17_field or string_closure" -v
# 18 passed in 0.25s
```

### 7.2 `tests/test_characterization.py` completo

```
.venv020a/Scripts/python.exe -m pytest tests/test_characterization.py -v
# 191 passed in 0.34s          (com RDKit instalado)

.venv020a-base/Scripts/python.exe -m pytest tests/test_characterization.py -v
# 191 passed in 0.55s          (ambiente base, sem RDKit — T-020A-006 preservado)
```

### 7.3 Suíte completa do projeto

```
.venv020a/Scripts/python.exe -m pytest
# 1775 passed, 5 skipped in 49.79s
```

Python 3.11.9, pytest 9.1.1, pydantic 2.14.1, rdkit 2026.03.6 — versões
reais, declaradas, não assumidas. A base no HEAD anterior (`3668207`) era
1757 passed/5 skipped (reportada pelo implementador anterior, não
reexecutada de forma independente pelo arquiteto). O delta observado
nesta sessão é exatamente +18 (1757 → 1775), coincidindo item a item com
a Seção 7.1; nenhum incremento foi predeterminado antes da coleta real.

## 8. Diffs e estado do working tree

```
git diff 3668207..HEAD --stat
 src/molecular/characterization.py |  53 +++++++++
 tests/test_characterization.py    | 166 +++++++++++++++++++++++++
 2 files changed, 219 insertions(+)
```

Exatamente os dois caminhos permitidos; nenhum outro arquivo tocado.

```
git diff f8416b8..HEAD --stat -- src/molecular/characterization.py \
  src/molecular/rdkit_tautomer.py tests/test_characterization.py \
  tests/test_rdkit_tautomer.py
 src/molecular/characterization.py | 300 +++++++++++++++++++++-
 tests/test_characterization.py    | 450 +++++++++++++++++++++++++++++++++++++
 tests/test_rdkit_tautomer.py      | 337 +++++++++++++++++++++++++++-
 3 files changed, 1071 insertions(+), 16 deletions(-)
```

Diff cumulativo do incremento sobre o allowlist de quatro arquivos;
`src/molecular/rdkit_tautomer.py` permanece com diff vazio desde
`f8416b8` — inalterado nesta entrega e nas duas anteriores.

`git diff --check`: sem erro de whitespace; apenas os avisos de
normalização de fim de linha LF/CRLF do Git no Windows (`autocrlf`).

`git status --short` no worktree isolado, pós-commit: apenas os dois
venvs locais untracked; nenhum outro arquivo pendente; nenhum item
pessoal/untracked do usuário tocado.

## 9. Commit e publicação

Novo commit, filho direto de `36682074b55596d5632800bea98aff778eee885f`,
sem amend/rebase/reset/force:

```
commit cc903d8ebbfe1916c3fce195d20fc97b206a5f54
parent 36682074b55596d5632800bea98aff778eee885f
branch feature/increment-020-a-molecular-characterization
"fix: close the full 17-field strict-str matrix on characterization DTOs
 (increment 020-A, checkpoint 1 MAJOR-1 string closure)"
```

Push: `git push origin feature/increment-020-a-molecular-characterization`
→ `3668207..cc903d8` (fast-forward, sem force). Refs remotos verificados
após `git fetch` subsequente: `origin/feature/increment-020-a-molecular-
characterization` = `cc903d8ebbfe1916c3fce195d20fc97b206a5f54`;
`origin/main` permanece `08b797e0985e123ffd4d7ca7e5a5e8f040e63851`,
inalterada.

Este relatório e as duas evidências novas são publicados em branch
própria do governance, `claude/020-a-checkpoint1-major1-string-closure-
20261021`, baseada diretamente no snapshot imutável fornecido
(`0b499f8aee9273ea4df6825cf760d8ca5c665e56`) — a release do governance
indicada pela própria tarefa, não a main nem um commit-raiz arbitrário.
Nenhum arquivo central (`STATUS.md`, tarefas) foi escrito nesta branch;
apenas os dois caminhos de saída autorizados. Nenhum PR, merge, aprovação
formal ou alteração de configuração/visibilidade foi feito ou solicitado.

## 10. Identidades de saída deste relatório

| Arquivo | Linhas | Bytes | SHA-256 |
|---|---:|---:|---|
| `evidence/claude-major1-string-closure-pre-fix-reproduction.json` | 26 | 3517 | `652dfde76f51f6bd58291891e0712fc98bf408600393d9d2ad508e015f8036ec` |
| `evidence/claude-major1-string-closure-post-fix-reproduction.json` | 26 | 1656 | `7bb0fcb5d8ce32f0995087aa36eb9dbc6691ba99b9d16f99c3c7b07ac60cd104` |
| `src/molecular/characterization.py` (estado final, código) | 1334 | 51065 | `6bf1a90887276f499ba832d92990e901ab279f886a5dcb58b791d89a040ad747` |
| `tests/test_characterization.py` (estado final, código) | 1168 | 41764 | `cd286b73ca829abc5abd59cfadf62b3c6ba7afcf75478feff59592acd5402668` |

(As linhas/bytes/SHA-256 deste próprio arquivo markdown não são
auto-referenciados, pelo mesmo motivo registrado no relatório anterior:
evitar um valor calculado antes do conteúdo final do próprio arquivo.)

## 11. Declaração de não fechamento

Esta entrega fecha a matriz finita de 17 campos do MAJOR-1 (seis já
corrigidos, preservados; onze corrigidos agora). Nenhum dos quatro
achados originais (MAJOR-1, MAJOR-2, MINOR-1, MINOR-2) é declarado
fechado por esta sessão, nem o CP1 é declarado aprovado. A reverificação
independente focal permanece o próximo gate, a cargo do
arquiteto/responsável — não iniciada nem presumida aqui.

---

**MAJOR-1 STRING CLOSURE DELIVERED: YES**
**11-FIELD / 44-TRIAL REPRODUCTION (PRE-FIX): CONFIRMED**
**PRIOR REPORT'S "DRAWINGRESULT HASHES OUTSIDE AUTHORIZATION" READING: CLARIFIED AS INCORRECT (SECTION 3), PREVIOUS REPORT NOT EDITED**
**44/44 TRIALS REJECTED (POST-FIX), NATIVE STR/JSON/NULL CONTROLS PRESERVED: CONFIRMED**
**FULL 17-FIELD MATRIX NOW CLOSED: YES**
**DIFF RESTRICTED TO ALLOWED PATHS: YES**
**NEW COMMIT DIRECT CHILD OF 36682074..., NO AMEND/REBASE/RESET/FORCE: YES**
**MAJOR-1 INDEPENDENTLY CLOSED: NO**
**FOCAL REVERIFICATION READY: PENDING ARCHITECT/RESPONSÁVEL — NOT DECLARED HERE**
**CHECKPOINT 1 APPROVED: NO**
**CHECKPOINT 2 AUTHORIZED: NO**
**CHECKPOINT 3 AUTHORIZED: NO**
