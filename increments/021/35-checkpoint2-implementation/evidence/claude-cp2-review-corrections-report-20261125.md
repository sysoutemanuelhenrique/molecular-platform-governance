# Relatório de correções da revisão independente — Incremento 021, Checkpoint 2

Autor: Claude implementador (sessão separada do revisor independente). Data: 25/11/2026, America/Sao_Paulo.

Aditivo aos relatórios já publicados (`claude-cp2-completion-report.md` em `70f7a14`, sua correção
`17e594d`, o relatório residual `claude-completion-residual-correction-report-20261125.md` em
`2c50be1`, e o relatório final residual `claude-completion-final-residual-report-20261125.md` em
`81a6503`). Nenhum deles foi editado, nem o parecer independente (`increments/021/40-checkpoint2-review/`
na branch `claude/021-cp2-adversarial-review-20261125`) ou a reconciliação arquitetural
(`increments/021/41-checkpoint2-review-reconciliation/`).

## 1. Identidade e procedência

- Coordenação de entrada obrigatória: `fca6b8b57f78fc255609d5211c5c495de45a2a56` (branch
  `docs/020-a-candidate1-review-20261020`), confirmada idêntica a
  `origin/docs/020-a-candidate1-review-20261020` antes de qualquer leitura.
- Lidos integralmente: `AGENTS.md`, `protocol/AGENT_WORKFLOW.md`, `STATUS.md` nesse snapshot, a
  tarefa `tasks/021-CHECKPOINT2-REVIEW-CORRECTIONS.json` (status
  `AUTHORIZED_CORRECTIONS_WITHIN_EXISTING_CP2_SCOPE`), o parecer adversarial independente completo
  (`increments/021/40-checkpoint2-review/CLAUDE_INCREMENT_021_CHECKPOINT2_ADVERSARIAL_REVIEW.md`,
  214 linhas, na branch própria do revisor `claude/021-cp2-adversarial-review-20261125` @
  `85c605e04ae61b2dad39f7d65d4531db860f71d4`) e a reconciliação arquitetural completa
  (`increments/021/41-checkpoint2-review-reconciliation/CODEX_INCREMENT_021_CHECKPOINT2_REVIEW_RECONCILIATION.md`,
  221 linhas).
- Autorização: a mesma autorização humana original do CP2 (commit `399bbbc`), mesma allowlist de
  código (`src/molecular/receptor_parsing.py`, `src/molecular/receptor_materialization.py`,
  `tests/test_receptor_parsing.py`, `tests/test_receptor_materialization.py`) e raiz de fixtures
  (`tests/fixtures/receptor_materialization/`) já autorizadas - nenhuma nova aprovação humana
  inferida, conforme a própria tarefa declara.
- Confirmado antes de editar e reconfirmado depois: `git rev-parse HEAD` no código começou em
  `a807b03f44089eb3cbacc14f871b63689a21aec9` (o `code_head_before_corrections` exato da tarefa);
  `origin/main` código = `08b797e0985e123ffd4d7ca7e5a5e8f040e63851`; `origin/main` governance =
  `a47183dfec8213c765ed43ae482c8c227760a3d5` - ambos inalterados. Nenhum reset/clean/stash/rebase/
  amend/force usado em nenhum momento. Os relatórios/branches anteriores (parecer do revisor
  incluído) não foram tocados.

## 2. Ambiente real de execução

```
Python 3.14.7 (venv do próprio projeto, .venv) / gemmi 0.7.5 real / pydantic 2.13.5 / pytest
Plataforma: Windows-11-10.0.26300
```

Esta é evidência Windows fornecida pelo implementador - não substitui nem contradiz a execução
nativa Linux do revisor independente (Gemmi 0.7.5 compilado do mesmo pin, `5cc1c23`), que continua
sendo a prova de produção independente dos 13 achados antes desta correção.

## 3. Ressalva interpretativa sobre inteiros (aplicada em todo o código)

Conforme a reconciliação §3: o §6 exige um inteiro decimal **não citado** e modelo positivo, mas
não exige grafia canônica sem sinal/zeros à esquerda. `"+1"` e `"01"` são portanto grafias válidas
de inteiros não citados sob a gramática oficial `[+-]?[0-9]+` (consultada nos dicionários wwPDB de
`pdbx_PDB_model_num`/`pdbx_formal_charge`), e devem ser aceitos quando representam o modelo
correto - nunca recusados apenas pela grafia. Isso não estende a interpretação a identificadores/
operadores (`01_555` e ids de tabela de simetria continuam sujeitos à igualdade textual exata do
§10.1) e não autoriza números citados, não-ASCII, floats ou cargas calculadas. Esta ressalva foi
aplicada de modo coeso em MAJOR-2 e MINOR-5 (ver §4), nunca registrada como concordância do
revisor - o fechamento focal decidirá a interpretação.

## 4. Disposição dos 13 achados + 4 NOTES

### MAJOR-1 — ACCEPTED: save frames escapam da guarda de coluna/caixa

**Correção:** `_reject_save_frames` não usa mais regex (`^save_\S`, sensível a caixa/coluna);
agora itera os `Item`s do bloco Gemmi real (`item.frame`), recusando qualquer frame genuíno -
`SAVE_x`, indentado ou não - antes da extração de categorias. Nenhum parser CIF artesanal; a
distinção entre frame real e conteúdo textual/citado que apenas parece um frame continua garantida
pela própria gramática nativa do Gemmi (comprovada contra o pin `5cc1c23`).

**Testes:** `test_parse_cif_dom021_rejects_save_frame_case_and_indentation_variants` (novo - três
variantes: maiúscula, indentada minúscula, indentada maiúscula, todas recusadas via Gemmi real);
os dois controles positivos existentes (texto multilinha/token citado com `save_`) permanecem
válidos sem alteração.

### MAJOR-2 — PARTIALLY_ACCEPTED (conforme ressalva de inteiros): gramática numérica sobre valor decodificado; inteiros/formal_charge sem gramática

**Correção:** todo validador numérico (`_validate_numeric_token`, usado por coordenadas/occupancy/
B_iso, tensores U/B do anisotrop, e componentes de matriz/vetor NCS) agora recebe o token **cru**
(`RawCategoryTable.raw_value`), nunca o já decodificado pelo Gemmi - um `'1.000'` citado falha a
gramática pelo próprio caractere de aspas, nunca mais indistinguível do valor genuíno. A detecção
de null permanece na visão decodificada (nunca confundida com string numérica citada). Novo
`_validate_ascii_integer_token`/`_ASCII_SIGNED_INTEGER_PATTERN` (`[+-]?[0-9]+`, nunca o `int()`
laxo do Python, que aceita sublinhados/dígitos unicode/espaços) valida `pdbx_PDB_model_num` (lido
cru em `receptor_parsing.py`) e o novo `pdbx_formal_charge` (nulo-ou-inteiro assinado, sem faixa
química calculada - integridade, nunca química).

**Testes:** `test_materialize_receptor_cif021_rejects_quoted_coordinate` (nativo - `Cartn_x`
citado real recusado); `test_materialize_receptor_cif021_model_num_integer_spellings` (nativo -
`+1`/`01` aceitos como modelo 1; `'1'`/`1.0`/`abc` recusados); `test_catalogue_anisotrop_...`
(estendido com U/B citados); `_guard_ncs_row` (NCS citado); `_validate_atom_site_numeric_row`
(coordenada/occupancy/B_iso citados, `pdbx_formal_charge` nulo/válido/citado/float/não-ASCII).

### MAJOR-3 — ACCEPTED: '?'/'.' citados em ptnr*_symmetry recolapsados a null

**Correção:** `_resolve_symmetry_endpoint` parava de reaplicar `_raw_cif_token_to_optional` sobre
um valor **já decodificado** pelo adaptador (`RawConnectionEndpointTokens` já documenta essa
garantia) - essa segunda checagem redundante confundia um `'?'` citado (que decodifica para a
string literal `"?"`) com um null real. Removida; `_raw_cif_token_to_optional` (agora inteiramente
não utilizada) foi apagada. `None` é a única condição de null real a partir de agora; um `"?"`/`"."`
literal cai naturalmente em `_parse_symmetry_code`, falha a gramática `n_klm` e resolve
corretamente como não-nulo porém sem prova (§10.1: `unsupported-discarded`), nunca `one-null`.

**Testes:** `test_quoted_null_look_alike_symmetry_token_is_not_real_null` (puro - `"?"`/`"."`
citados vs. null real, K=0); `test_materialize_receptor_cif021_quoted_null_look_alike_symmetry_not_real_null`
(nativo - conn1 real do `_MINIMAL_CIF` mutado para `'?'`, K>0, recusa `UNSUPPORTED_SYMMETRY`
corretamente em vez de aceitar como se fosse null).

### MAJOR-4 — ACCEPTED: `_chem_comp`/`_entry` sem guardas genéricas

**Correção:** ambas categorias eram puladas do laço genérico antes de qualquer checagem de
tag/chave. Agora recebem, antes de seu tratamento especial: rejeição de tag desconhecida
(`unknown_tag_action: reject`), tags obrigatórias, e `_validate_key_integrity` (chave nunca nula,
nunca duplicada). `_entry` ganhou um teto explícito de singleton (uma linha real, nunca duas - o
catálogo não tem campo de cardinalidade próprio). A decisão de `_entry` agora carrega
`source_rows_key`/`omitted_row_ordinals` reais quando uma linha fonte existe (hash/cobertura da
linha original substituída pelo novo `tbmp_<plan_key>`), nunca mais `source_rows_key=None`
indiscriminadamente.

**Testes:** `test_catalogue_chem_comp_and_entry_receive_generic_guards_before_special_handling`
(novo - `_chem_comp.id` duplicado/nulo recusados; `_entry` com tag desconhecida/duas linhas
recusado; controle positivo sem `_entry` fonte e com `_entry` fonte presente, confirmando
`source_rows_key`/`omitted_row_ordinals` corretos em ambos os casos).

### MAJOR-5 — ACCEPTED: referências compostas de branch não validadas

**Correção:** nova validação incondicional (toda linha fonte, não apenas as retidas) do par
`_pdbx_entity_branch_link.entity_branch_list_num_{1,2}`/`comp_id_{1,2}` contra
`_pdbx_entity_branch_list(entity_id,num,comp_id)`, e de `_pdbx_branch_scheme.num`/`mon_id` contra
o mesmo alvo - a chave composta que o checador genérico de referência simples não consegue
expressar, espelhando a lógica já existente para `entity_poly_seq`. Nenhuma reconstrução de
grafo/leaving-atom/coordenadas; nenhum `num` inventado de `auth_seq`.

**Testes:** `test_branch_compound_references_reject_wrong_endpoint_and_swapped_scheme` (novo -
`entity_branch_list_num_1` inexistente recusado; `comp_id_1` divergente recusado; esquema com
`mon_id` trocado em relação à lista real - NAG/BMA - recusado; controle positivo válido aceito).

### MAJOR-6 — ACCEPTED: ocorrências indistinguíveis fundidas num endpoint

**Correção:** `_resolve_endpoint_atoms` agora recusa `AMBIGUOUS_ENDPOINT` quando dois átomos do
endpoint final compartilham a mesma ocorrência, o mesmo `label_atom_id` **e** o mesmo altloc
(incluindo ambos nulos) - fisicamente indistinguíveis, nunca mais silenciosamente aceitos como um
conjunto de dois átomos. Variantes de altloc genuinamente distintas continuam válidas (Seção 9).
Corrigido de passagem um duplicado latente no próprio fixture compartilhado `_MINIMAL_CIF` (dois
átomos "CA" idênticos na mesma residue) que este achado expôs - renomeado para "CB", sem afetar
nenhuma asserção existente por `atom_id`.

**Testes:** `test_struct_conn_endpoint_rejects_physically_indistinguishable_duplicate_atoms` (novo
- duas águas idênticas recusadas; controle positivo com altlocs A/B genuinamente distintos aceito
como endpoint de dois átomos, prova que a correção não restringe o caso legítimo).

### MAJOR-7 — ACCEPTED: falhas de RAW/parse fora da taxonomia 021

**Correção:** `materialize_receptor_cif021` agora traduz, na própria fronteira pública, todas as
exceções RAW/parse/adapter nativas do `receptor_parsing.py`
(`InvalidCifEncodingError`→`INVALID_CIF`/raw, `CifStructuralLimitExceededError`→`LIMIT_EXCEEDED`/
raw ou parse conforme o ponto de detecção, `MultipleDataBlocksError`/`DuplicateCanonicalTagError`/
`CifSaveFrameRejectedError`/`ReceptorParseFailureError`→`INVALID_CIF`/parse,
`MaterializationAdapterError`→seu próprio `code`/plan) em `MaterializationExecutionError` tipado,
com `phase` correta e causa original preservada (`from error`) - nunca uma classe crua sem
`code`/`phase`. O leitor 020 (`parse_receptor_cif_dom021` chamado isoladamente, `parse_receptor_raw`)
permanece inteiramente intocado; só a fronteira pública 021 traduz. Um `source_context.parser`
divergente do pin agora resulta em `IDENTITY_MISMATCH`, nunca mais `ENGINE_UNAVAILABLE` (o motor
instalado está presente e correto - é a identidade declarada da fonte que diverge).

**Testes:** `test_materialize_receptor_cif021_translates_raw_and_parse_failures_to_021_taxonomy`
(novo - gzip/BOM/dois blocos/sintaxe malformada/entidade inexistente, cada um com `code`/`phase`/
`__cause__` corretos); `test_materialize_receptor_cif021_source_context_parser_mismatch_is_identity_mismatch`
(novo); `test_materialize_receptor_cif021_rejects_raw_over_16mib_before_gemmi_parses` (atualizado
para o novo tipo/código/fase).

### MINOR-1 — ACCEPTED: tags de saída fora de ordem alfabética

**Correção:** `_build_output_category_tokens` agora ordena as chaves do dicionário de tags antes
de entregá-las ao serializador - a ordem de escrita do Gemmi segue a ordem de iteração do dicionário
Python (confirmado empiricamente), nunca mais a ordem do catálogo/fonte. Nenhuma linha, token ou
hash canônico é afetado - apenas a ordem de colunas na saída.

**Testes:** `test_materialize_receptor_cif021_output_tags_in_alphabetical_order` (nativo -
reparseia os bytes reais de saída e confirma ordem alfabética de tags em toda categoria, incluindo
`_entry`).

### MINOR-2 — ACCEPTED: snapshots documentais fictícios nas integrações

**Correção:** `_cp2_source_context()`/`_real_fixture_materialize()` (testes) agora constroem os
quatro `RecordSnapshot` a partir dos bytes reais `yaml.safe_dump(model.model_dump(mode="json"),
sort_keys=False)` - o formato exato que a camada real de persistência 020
(`receptor_registry.py`/`registry.py`) usa - nunca mais `sha256="1"*64.../size_bytes=1`. Um
timestamp fixo e real (não `datetime.now()`) substitui o anterior, preservando a determinação do
`plan_key` entre execuções repetidas (os registros agora entram de fato no hash).

**Testes:** `test_cp2_source_context_record_snapshots_are_real_document_bytes` (novo - confirma
tamanhos/hashes reais, nunca os antigos placeholders; confirma que um documento genuinamente
diferente muda `plan_key`).

### MINOR-3 — ACCEPTED: nenhum teste permanente de interrupção

**Correção:** nenhuma mudança de produção necessária - o comportamento já estava correto (catches
estreitos, nunca `except Exception`/`BaseException` genérico). Adicionada a prova permanente que
faltava.

**Testes:** `test_materialize_receptor_cif021_preserves_interruption_instance_at_every_boundary`
(novo, parametrizado - 7 fronteiras reais × {KeyboardInterrupt, SystemExit} = 14 combinações,
cada uma confirmando a **mesma instância** propaga, nunca uma reembalada/perdida).

### MINOR-4 — ACCEPTED: prova nativa de IdentityBasis sintética

**Correção:** nenhuma mudança de produção necessária. O teste parametrizado existente
(`test_identity_basis_pairs_k0_reachable_pairs`) construía os mesmos DTOs duas vezes no mesmo
processo - prova nada sobre independência de hash seed, já que a ordem de visita de dict/set é
fixa por processo. Adicionado o teste que faltava.

**Testes:** `test_identity_basis_plan_key_stable_across_hash_seeds` (novo, parametrizado pelos
7 pares alcançáveis - cada um reconstruído do zero em subprocessos genuinamente novos sob
`PYTHONHASHSEED=0` e `PYTHONHASHSEED=12345`, confrontado contra `plan_key`/`connection_decisions_key`
literais, independentemente fixados - nunca derivados chamando a própria função sob teste).

### MINOR-5 — PARTIALLY_ACCEPTED (conforme ressalva de inteiros): contexto de posição especial inválido vira interseção zero

**Correção:** `_resolve_special_position_row_atoms` comparava `pdb_model_num` como
`str(atom.model) == model_token` - uma grafia numericamente válida como `"01"` não batia com o
inteiro real `1`. Agora valida o token cru como inteiro ASCII assinado
(`_validate_ascii_integer_token`) e compara **numericamente**; um token citado/não-inteiro/
não-positivo recusa `INVALID_CIF` (contexto genuinamente inválido), nunca mais tratado como "sem
filtro de modelo". Um `label_alt_id` informado que não corresponde a nenhum altloc real do resíduo
casado agora recusa também, em vez de silenciosamente resolver para zero sobreposição.

**Testes:** cobertos pelos mesmos testes do R-CP2-01 final mais a nova validação de modelo/altloc
inválido (testes de posição especial em `test_receptor_materialization.py`); os casos legítimos de
zero-sobreposição (outro modelo real, átomo removido) permanecem preservados sem alteração.

### MINOR-6 — ACCEPTED: evidência de pipeline completo NCS real

**Correção:** como não há acesso de rede/ferramenta web disponível nesta sessão para qualificar
uma nova entrada real cujo NCS alcance o pipeline completo sem bloqueio, foi usado o caminho
alternativo explicitamente autorizado pela reconciliação (§23): um derivado de isolamento
rastreado do 1A2P pinado. `1A2P_ncs_isolated.cif` remove **exatamente** a única linha
`_struct_conn` bloqueadora não relacionada (`metalc2`, A-D, `ptnr1_symmetry='3_675'`) que impedia
o pipeline completo de `1A2P_trimmed.cif` de sequer alcançar `_struct_ncs_oper` - toda outra linha,
incluindo as duas operações NCS reais, permanece byte-idêntica. A recusa honesta original de
`1A2P_trimmed.cif` (`UNSUPPORTED_SYMMETRY`) permanece testada e preservada sem alteração; nenhuma
regra de produção foi flexibilizada, nenhum operador foi fabricado.

**Testes:** `test_real_fixture_1a2p_ncs_isolated_full_pipeline_reaches_real_ncs_guard` (novo -
pipeline completo real alcança `_struct_ncs_oper`, `action='guard_then_omit'`, ambas as linhas
reais `code='given'` omitidas-auditadas, sem recusa).

### NOTE-1 a NOTE-4 — preservadas sem alteração de código

- **NOTE-1 (ACCEPTED_CARRIED):** whitespace de depósito exclusivamente nos `.cif` originais/
  derivados - nenhum RAW reescrito; `git diff --check`/`git show --check` do commit publicado
  permanecem limpos para fontes/testes (os avisos de whitespace do novo `1A2P_ncs_isolated.cif`
  são herdados do depósito real, idênticos em espírito aos já documentados nos outros 12 `.cif`).
- **NOTE-2 (ACCEPTED_WITH_FACTUAL_CLARIFICATION):** nenhuma mudança de catálogo; a distinção
  original/recortado/inventário histórico permanece como documentada nos `PROVENANCE.json`
  existentes - esta correção acrescenta apenas uma nova entrada de derivado (`1A2P_ncs_isolated.cif`),
  rotulada honestamente, nunca confundida com o original ou com `1A2P_trimmed.cif`.
- **NOTE-3 (ACCEPTED_CARRIED_TO_CP3_GATE):** ordem de precedência preflight/conexão/catálogo
  preservada sem alteração - nenhuma correção deste conjunto a exigiu.
- **NOTE-4 (ACCEPTED_PRESERVE):** a conservadorismo de operador não-identidade (`2_555`/operador
  2) permanece preservado; a matriz de 15 células e os controles de base não mudaram, exceto o
  fechamento específico de null citado (MAJOR-3).

## 5. Atualização da matriz dos 79 cenários

Os 15 cenários que o parecer independente classificou `PARTIAL` agora têm correção de produção e
teste dedicado publicados nesta entrega:

| Cenário | Achado que o fechava | Disposição após esta correção |
|---|---|---|
| T021-041 | MAJOR-3 | Corrigido e testado (puro + nativo) |
| T021-062 | MAJOR-2 | Corrigido e testado (nativo + anisotrop) |
| T021-067 | MAJOR-4 | Corrigido e testado |
| T021-072/073/074 | MAJOR-5 | Corrigido e testado |
| T021-082/085/087/088 | MAJOR-4 | Corrigido e testado |
| T021-084 | MAJOR-1 | Corrigido e testado |
| T021-154 | MAJOR-2 | Corrigido e testado |
| T021-157 | MAJOR-6 | Corrigido e testado |
| T021-158 | MINOR-5 | Corrigido e testado |
| T021-173 | MAJOR-3 | Corrigido e testado |

Os 64 cenários já `COVERED` pelo parecer independente não foram reexaminados nesta correção
estreita - nenhuma regressão concreta foi encontrada ou é esperada, e os 92 testes CP1/13 goldens/
R-1/3 NOTES permanecem intocados (confirmado pela suíte completa, §6). **Esta tabela é a disposição
do próprio implementador, não uma segunda classificação independente** - o fechamento focal do
revisor é quem decide se cada cenário agora está genuinamente `COVERED` sob seus próprios critérios
(mapeamento de nome de teste não é aceito como prova, conforme o parecer original já declarou).

## 6. Reconciliação de coleta, foco, regressão e suíte completa

```
antes desta correção (HEAD a807b03):                   1664 coletados (1659 passed, 5 skipped)
após esta correção (HEAD 2410e12):                      1698 coletados (1693 passed, 5 skipped)

tests/test_receptor_parsing.py + tests/test_receptor_materialization.py:
  python -B -m pytest -p no:cacheprovider tests/test_receptor_parsing.py tests/test_receptor_materialization.py -q -rs
  -> 248 passed in ~13s

regressão 020 (inspection/selection/resolution/registry/service):
  python -B -m pytest -p no:cacheprovider tests/test_receptor_inspection.py tests/test_receptor_selection.py tests/test_receptor_resolution.py tests/test_receptor_registry.py tests/test_receptor_service.py -q -rs
  -> 121 passed in ~3-5s (inalterado)

suíte completa:
  python -B -m pytest -p no:cacheprovider -q -rs
  -> 1693 passed, 5 skipped in 91.07s
```

Os cinco skips (inalterados, discriminados): `tests/test_application.py:1809` e `:1847` (RDKit
instalado - comportamento esperado sem a extra), `tests/test_atomic.py:1046` (criação de symlink
não permitida neste ambiente Windows - WinError 1314), `tests/test_cli.py:4250` e `:4303` (exigem
ambiente sem RDKit). Esta é a reexecução real desta sessão - os números fornecidos anteriormente
(`1659 passed/5 skipped` em `a807b03`) não são reapresentados como execução desta correção.

`git diff --check`/`git show --check` do commit publicado, limpos (os únicos avisos de trailing
whitespace são no `.cif` depositado novo, conforme NOTE-1). `git diff --name-status` contra
`ea8dac9` (CP1 aprovado) mostra exatamente os quatro caminhos da allowlist mais a árvore de
fixtures (incluindo o novo `1A2P_ncs_isolated.cif` e seu `PROVENANCE.json` atualizado) - nenhum
arquivo fora do escopo autorizado.

## 7. Commit e publicação remota do código

```
commit 2410e1220febd79cfc81f348720429bb1ac28cfe
parent  a807b03f44089eb3cbacc14f871b63689a21aec9
branch  feature/increment-021-receptor-materialization
6 files changed, 9776 insertions(+), 99 deletions(-)
```

Push confirmado: `git rev-parse origin/feature/increment-021-receptor-materialization` devolve
`2410e12...`. `git rev-parse origin/main` (código) continua `08b797e...`; `git rev-parse origin/main`
(governance) continua `a47183d...`. Nenhum PR, merge, tag ou alteração de `main` em nenhum dos dois
repositórios.

## 8. Identidades finais (bytes reais do blob Git, gerados pelo helper fornecido)

Executado `GENERATE_GIT_BLOB_IDENTITIES.py` (o mesmo helper somente-leitura já inspecionado e
usado na correção anterior) contra o commit publicado `2410e122...`, fora da árvore de código. O
helper confirmou `HEAD` e verificou o SHA-1 de cada blob antes de calcular o SHA-256 - nenhum
mismatch relatado. O manifesto completo (os quatro arquivos permitidos mais toda a árvore de
fixtures, incluindo o novo `1A2P_ncs_isolated.cif`) está em
`evidence/claude-review-corrections-git-blob-identities-20261125.json`.

| Caminho (bytes reais do blob Git, LF) | Linhas LF | Bytes | SHA-256 |
|---|---:|---:|---|
| `src/molecular/receptor_materialization.py` | 4816 | 233.406 | `0103f56fee20b8023ff9b24025b95b93dac215439a987852ba181e132383524a` |
| `src/molecular/receptor_parsing.py` | 1853 | 77.669 | `c39d15eef4051d9fcff9cd32971e3ab6c47e838f1e4cbe57dd0224d9e2afbc05` |
| `tests/test_receptor_materialization.py` | 3344 | 177.923 | `96e1495b85f01dc21a1dc994deaf7fc7c0e7d5ccec595d38a44369a8f7facf55` |
| `tests/test_receptor_parsing.py` | 1923 | 86.602 | `94309089c76d5b21dada2a01c4f12975b6a6663a9fce74cbfd1f2682dd03e218` |

O novo fixture `1A2P_ncs_isolated.cif` tem blob SHA-256 `e470c25f8f002958955f2d97656b41e90609796d5836a8f7340a030b54d5774d`,
613.947 bytes - idêntico ao valor citado em `PROVENANCE.json` e ao que os testes verificam contra
os bytes reais do arquivo.

## 9. O que não foi feito / pendências honestas

- Esta correção não constitui fechamento independente dos 13 achados nem dos 79 cenários - essa é
  tarefa exclusiva da revisão focal separada do revisor independente, explicitamente reservada
  pela reconciliação (§6).
- A ressalva interpretativa sobre inteiros (§3) foi **aplicada** no código conforme a orientação
  arquitetural, mas permanece sujeita a confronto do revisor no fechamento focal - não é
  apresentada aqui como acordo do revisor.
- MINOR-6 permanece, pela própria natureza do caminho escolhido, uma qualificação por **derivado
  de isolamento**, não por uma nova entrada real intacta cujo NCS alcance o pipeline sozinho - o
  revisor deverá confirmar se esse caminho satisfaz a prova exigida, conforme a reconciliação já
  antecipa.
- Nenhum CP3/CP4, nenhuma publicação de `receptor.cif` final, nenhum storage/registry/service/CLI.
  Nenhuma alteração ao contrato congelado, ao catálogo, aos cinco normativos ou a `main` em
  qualquer repositório. `020-A` permanece em stand-by; itens locais protegidos permanecem
  untracked e intocados; todos os relatórios/branches anteriores preservados sem sobrescrita.
- Nenhum fechamento independente de CP2 é declarado por este relatório; não solicito avanço a CP3.

## 10. Gate sugerido

Os 7 MAJORS e 6 MINORS foram corrigidos e testados (nativo onde aplicável), as 4 NOTES preservadas,
e os 15 cenários antes parciais agora têm prova de produção dedicada. Recomendo que o arquiteto
receba esta entrega e prepare a revisão focal separada do mesmo revisor independente, que fecha os
achados/ressalvas e verifica regressões - sem repetir decisões já aprovadas por preferência,
conforme o protocolo já estabelece. CP2 não aprovado. CP3 não solicitado.

```
TASK_ID: 021-CHECKPOINT2-REVIEW-CORRECTIONS
ROLE: claude-implementer-separate-from-independent-reviewer
SCOPE_EXECUTED: CHECKPOINT2_REVIEW_CORRECTIONS (7 MAJOR + 6 MINOR, 4 NOTES preserved)
CODE_BRANCH: feature/increment-021-receptor-materialization
CODE_COMMIT: 2410e1220febd79cfc81f348720429bb1ac28cfe
CODE_COMMIT_PARENT: a807b03f44089eb3cbacc14f871b63689a21aec9
INDEPENDENT_REVIEW_INPUT: claude/021-cp2-adversarial-review-20261125 @ 85c605e04ae61b2dad39f7d65d4531db860f71d4
READY FOR OWNER CP2 DECISION: NO
CHECKPOINT2 APPROVED: NO
CHECKPOINT3 IMPLEMENTATION AUTHORIZED: NO
INDEPENDENT FOCAL REVIEW REQUIRED: YES
```
