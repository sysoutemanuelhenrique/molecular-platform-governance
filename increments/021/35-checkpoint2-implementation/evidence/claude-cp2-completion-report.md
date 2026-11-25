# Relatório de conclusão — Incremento 021, Checkpoint 2

Autor: Claude implementador (sessão separada da revisão independente). Data: 25/11/2026, America/Sao_Paulo.

## 1. Identificação da tarefa e autorização conferida

- Tarefa: `tasks/021-CHECKPOINT2-COMPLETION.json`, lida no snapshot de governance `7cd8ab3c5c2ec53e4630a41a6e7362e30fbe5edd` (branch de coordenação `docs/020-a-candidate1-review-20261020`), exatamente o commit informado pelo arquiteto e confirmado idêntico a `origin/docs/020-a-candidate1-review-20261020` antes de qualquer leitura. Durante a sessão, a coordenação avançou para `625e538a01335829ee3f29ebf0e04758aa8f5fab` (adendo de orientação de retomada, ver §3-bis) — conferido em modo leitura, nunca tratado como nova autorização de escopo; este relatório é publicado a partir do snapshot original `7cd8ab3` conforme a própria política de branch da tarefa ("Own branch from exact new dispatch").
- Autorização: a tarefa confirma `authorization_basis: "Continue and complete all 79 original CP2 scenarios/corrections in already approved allowlist and report glob; no new checkpoint/scope or fresh human approval inferred"`, com a mesma allowlist de código (`src/molecular/receptor_parsing.py`, `src/molecular/receptor_materialization.py`, `tests/test_receptor_parsing.py`, `tests/test_receptor_materialization.py`) e a mesma raiz de fixtures (`tests/fixtures/receptor_materialization/`) já autorizadas em `021-CHECKPOINT2-IMPLEMENTATION.json`.
- Li integralmente: `AGENTS.md`, `STATUS.md`, o recebimento do arquiteto (`increments/021/36-checkpoint2-partial-receipt/CODEX_INCREMENT_021_CHECKPOINT2_PARTIAL_RECEIPT_AND_COMPLETION_PLAN.md`, 68 linhas), seu script de sondas (`ARCHITECT_CP2_CONTRACT_PROBES.py`), seu JSON de verificação (`ARCHITECT_CP2_PARTIAL_RECEIPT_VERIFICATION.json`), a matriz de escopo de conclusão (`CP2_COMPLETION_SCENARIO_SCOPE.csv`) e reconferi o brief/especificação/anexos originais. O campo `conditional_categories`/`required_categories`/`global_rules` do `CATALOG_021.json` — top-level, nunca transcrito no literal Python do CP1/CP2 parcial — foi lido integralmente desta vez (ver §3 C-05).
- Confirmado antes de editar: `git rev-parse HEAD` no código = `0d06ebd4c46c90e5446fec6f0eb72b4a8d2855db` (o `code_head_before_completion` exato); `origin/main` código = `08b797e0985e123ffd4d7ca7e5a5e8f040e63851`; `origin/main` governance = `a47183dfec8213c765ed43ae482c8c227760a3d5` — ambos inalterados, confirmados de novo ao final. A branch parcial `claude/021-cp2-implementation-report` e seu relatório não foram tocados nem sobrescritos.

## 2. Ambiente real de execução

```
Python 3.14.7
pytest 9.1.1
pydantic 2.13.5 / pydantic_core 2.46.5
PyYAML 6.0.3
gemmi 0.7.5
typer 0.27.2
Plataforma: Windows-11-10.0.26300-SP0, venv do próprio projeto (.venv)
```

Gemmi 0.7.5 real em todo teste que o exercita — nenhum stub/sentinela nativa. Evidência em `evidence/claude-completion-environment.txt`.

## 3. Disposição dos pontos C-01 a C-07 da triagem do arquiteto

**C-01 — numéricos e NCS exato (corrigido).** `_validate_numeric_token` (novo, substitui `_finite_numeric_token`) implementa a gramática fechada do §6 via `Decimal` (`^[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?(?:\([0-9]+\))?$`, strip apenas do su final para validar o valor central). `_guard_ncs_row` agora compara `Decimal` exato contra a matriz identidade (sem tolerância float): reexecutei a sonda exata do arquiteto (`vector[1]='0.0000001'`, `code='generate'`) e o guard agora recusa `UNSUPPORTED_NCS` (antes aceitava). `_validate_numeric_token('1.2e3(4)')`/`'1.2(4)e3'`/`'1_000'` reproduzem exatamente `Decimal('1.2E+3')`/`None`/`None` (a sonda do arquiteto esperava os dois primeiros invertidos e `1_000` aceito — ambos corrigidos). Estendi a mesma validação Decimal a `cartn_x/y/z` (nunca nulas) e `occupancy`/`b_iso_or_equiv` (nulas ou finitas, occupancy não negativa) em `_atom_site`, não só NCS/anisotrop.

**C-02 — hashes e duas visões do token (corrigido).** `compute_source_rows_key` agora calcula exatamente o envelope `SCHEMAS §4`: cada linha vira um `row_key` real (`compute_row_key`, envelope `source-row`) e `source_rows_key` é o hash do envelope `source-category` sobre o vetor desses `row_key`s — reexecutei a sonda documental exata do arquiteto e o resultado agora bate byte a byte com o envelope congelado (`1d0cf07c...`). `RawCategoryTable` ganhou um segundo campo `raw_columns` (a visão literal, nunca colapsada) — `receptor_parsing._build_category_tables` agora popula os dois: a visão decodificada (`.`/`?` → `None`) para toda busca/filtro do domínio, e a crua para hashing; reexecutei a sonda `raw_marker_?`/`raw_marker_.` e os dois agora produzem `source_rows_key` **diferentes** (antes idênticos). Também corrigi a decodificação de identificadores citados: um novo `_decoded_token` (null-check na forma crua, `gemmi.cif.as_string()` só depois) substitui a decodificação direta em `_build_atom_observations`, `_build_connection_rows`, `_build_entity_type_lookup`, `_build_symmetry_operator_tables` e na visão decodificada de `_build_category_tables` — sem efeito sobre nenhum identificador já não citado (os seis fixtures reais confirmam isso: nenhuma mudança de resultado), mas corrige o caso (não exercido por nenhum dos seis depósitos reais, documentado como tal) de um identificador citado no CIF fonte.

**C-03 — verificação independente da saída (corrigido).** `_verify_output_reparse` recebe agora `output_categories` (o vetor de tokens esperado, derivado independentemente do plano/fonte, nunca do próprio reparse) e compara célula a célula (id/ordem/tokens/coordenadas, inclusive recusa de tags extras) contra o DOM reparseado — reexecutei a sonda exata do arquiteto (`id=CHANGED_ID`, `cartn_x=NaN`) com a nova assinatura e o verificador agora recusa `INVALID_OUTPUT` (antes aceitava, provando só a forma).

**C-04 — RAW/pin/proveniência (corrigido).** `materialize_receptor_cif021` agora verifica, antes de qualquer parse: o pin do engine instalado (`gemmi.__version__`) e do `source_context.parser` contra `ENGINE_VERSION`/`ENGINE_NAME` (recusa `ENGINE_VERSION`/`ENGINE_UNAVAILABLE`); o tamanho e o SHA-256 reais dos `raw_bytes` recebidos contra `source_context.raw_size_bytes`/`raw_sha256` (recusa `SOURCE_CHANGED`/`CHECKSUM_MISMATCH`); o teto de 1 GiB; e a assinatura de conteúdo comprimido. A docstring não afirma mais um import "tardio" que nunca existiu — documenta explicitamente que este é o módulo adapter dedicado com import eager, e que o pin acontece nesta função, não no import do módulo. O teste de integração real (`test_materialize_receptor_cif021_real_gemmi_end_to_end`) e todos os seis testes de fixture real usam agora SHA-256/tamanho genuínos computados dos bytes reais (`hashlib.sha256(raw_bytes).hexdigest()`/`len(raw_bytes)`), nunca `"a"*64`/`10`.

**C-05 — integridade de catálogo, contextos e auditoria (corrigido).** Transcrevi os três campos de nível superior do catálogo nunca antes capturados — `_CATALOGUE_REQUIRED_CATEGORIES` (`_atom_site`/`_struct_asym`/`_entity`/`_chem_comp`, sempre obrigatórias) e `_CATALOGUE_CONDITIONAL_CATEGORIES` (`retained_polymer_entity`→`_entity_poly`/`_entity_poly_seq`/`_pdbx_poly_seq_scheme`; `retained_branched_entity`→`_pdbx_entity_branch`/`_pdbx_entity_branch_list`/`_pdbx_branch_scheme`; `retained_struct_conn`→`_struct_conn_type`) — e `compute_category_decisions` agora recusa `INVALID_CIF` quando uma entidade polimérica/ramificada retida, ou uma conexão preservada, não tem a categoria condicional correspondente. Reexecutei a sonda exata do arquiteto (entidade polimérica retida sem `_entity_poly`/`_entity_poly_seq`/`_pdbx_poly_seq_scheme`) e agora recusa (antes aceitava). Adicionei também: `_validate_key_integrity` (chave nunca nula, nunca duplicada, para toda categoria não-omitida) e `_validate_simple_references` (referência simples de uma coluna — `asym_id`→`_struct_asym.id` etc. — recusa referência pendente quando a categoria alvo está presente; referências compostas, como `(label_entity_id,label_seq_id,label_comp_id)`→`entity_poly_seq(entity_id,num,mon_id)`, são validadas por lógica própria, não pelo checador genérico). Uma nuance tratada com cuidado: `_pdbx_struct_mod_residue.parent_comp_id` fica fora do checador genérico de referência simples (que roda sobre toda linha fonte, retida ou não) porque uma anotação não preservada nunca entra no fechamento CCD e não deve exigir linha alguma; mas quando a linha *é* preservada, uma verificação dedicada de completude do fechamento (ver §3-bis) ainda exige a linha `_chem_comp` correspondente — corrigindo, nesta mesma sessão, uma isenção incondicional que eu mesmo introduzi antes de confrontá-la com o adendo de governance e com o depósito real 5I55.

**C-06 — identidade gerada e save frames (corrigido).** `entry_id`/nome de bloco usam agora `tbmp_<plan_key>` minúsculo em ambos (antes `TBMP_` maiúsculo só no id); o teste que replicava a expectativa errada foi corrigido junto. `_reject_save_frames` agora rastreia campos de texto delimitados por `;` linha a linha e só aplica o padrão `^save_\S` fora deles — reproduzi o exemplo exato do arquiteto (`save_literal_inside_text` dentro de um campo `;...;`) e confirmei com Gemmi 0.7.5 real que o mesmo texto é um único bloco de dados com um valor de texto multilinha, nunca um save frame — e que um save frame real fora de qualquer campo de texto continua recusado.

**C-07 — reavaliação completa e fechamento dos 79 (concluído).** Os pares de IdentityBasis (T021-164/166/168-172) agora constroem um `MaterializationPlan` real (via `build_materialization_plan`, com `SourceContext` real e `connection_decisions` wired) e comparam dois `plan_key` independentemente derivados — nunca mais hashear o mesmo objeto já construído duas vezes. T021-141 e T021-144 usam agora as entradas reais exigidas (5I55 e 1PFE, respectivamente — ver §5). T021-158 ganhou um teste com a linha real de `_pdbx_struct_special_symmetry` de 3DG1, confirmando a guarda sobre dado genuíno (a contagem completa de interseção retida/átomos únicos para múltiplas linhas mistas, quando a categoria carrega mais de uma, permanece um refinamento não implementado nesta sessão — ver §6). Os 26 cenários pendentes (T021-041/042/043/065/066/068-074/080/081/086/088/089/145/146/147/148/149/155/156/157/162) foram todos mapeados a asserções de produção reais — nenhum convertido em skip aprovado.

## 3-bis. Disposição do adendo de orientação de retomada (625e538, 2026-11-24)

Durante a sessão, antes da publicação deste relatório, a coordenação recebeu `CODEX_CP2_LOCAL_PROGRESS_RESUME_GUARDRAILS.md`, revisando um relato de progresso local anterior a esta publicação e apontando quatro pontos concretos — todos corrigidos nesta entrega, em um segundo commit aditivo (`60f9e0d`) sobre o primeiro (`b096af7`):

- **§3.1 (parent_comp_id e o fechamento CCD).** Minha exceção original em `_validate_simple_references` isentava `_pdbx_struct_mod_residue.parent_comp_id` incondicionalmente — o adendo apontou corretamente que isso contraria REFERENCED_CCD_CLOSURE quando a referência *entra no fechamento* (linha preservada). Corrigido: a exceção genérica permanece (correta para linhas não preservadas, que nunca entram no fechamento), mas uma nova verificação dedicada, após o fechamento `_chem_comp` ser calculado, recusa `INVALID_CIF` quando qualquer membro do fechamento — vindo de átomos, sequências/branches OU `parent_comp_id` preservado — não tem linha `_chem_comp` correspondente. Isso reclassificou a fixture real 5I55: a materialização completa agora recusa corretamente (MSE é uma construção de fasagem por selenometionina cujo depósito real nunca lista MET em `_chem_comp`) — um achado honesto, não um bug a esconder. Testei os três casos que o adendo pediu explicitamente: pai preservado com linha presente (`test_modified_residue_context_resolves_by_label_and_enters_ccd_closure`), pai preservado ausente (`test_modified_residue_preserved_parent_without_ccd_row_rejects`, e a própria 5I55 real), e anotação não preservada (`test_modified_residue_not_preserved_never_requires_parent_ccd_row`).
- **§3.2 (teto RAW de 16 MiB).** O preflight de bytes usava `MAX_RAW_ARTIFACT_SIZE_BYTES` (1 GiB, constante do leitor 020). Criei `MAX_CIF_RAW_ARTIFACT_SIZE_BYTES` (16 MiB, §4) e migrei o preflight do CP2 para usá-la exclusivamente — o teto do leitor 020 permanece intocado para `parse_receptor_raw`. Dois testes de fronteira: um arquivo de 16 MiB+1 recusa antes de qualquer parse Gemmi; um arquivo de exatamente 16 MiB passa o próprio portão de tamanho (falhando depois, por outro motivo estrutural, nunca pelo teto).
- **§3.3 (import tardio e engine ausente).** `import gemmi` no topo do módulo agora está em `try/except ImportError`, armazenando a falha num sentinela; toda entrada pública do CP2 (`parse_receptor_cif_dom021`, `materialize_receptor_cif021`, `serialize_cif_document021`) chama `_require_engine_available()` primeiro, convertendo a ausência em `MaterializationConfigurationError(ENGINE_UNAVAILABLE)` limpo — nunca um `ImportError`/`AttributeError` cru. Provado por um subprocesso real com `sys.modules['gemmi']=None` antes de qualquer import deste módulo (não um processo que já importou gemmi com sucesso). O comportamento/API do leitor 020 (`parse_receptor_raw`) não foi tocado.
- **§3.4 (visão decodificada vs. colapso de nulos).** Já corrigido na minha própria sessão antes deste adendo chegar (`_decoded_token`, ver C-02) — reconfirmado consistente com o texto do adendo (null-check na forma bruta, decodificação Gemmi só depois, `'?'`/`'.'` citados nunca colapsam a `None`).
- **§3.5 (recorte de fixtures e detector de save frame).** Adicionei prova permanente em pytest (antes só verificação ad-hoc): um campo de texto multilinha real contendo o literal `"save_..."` é aceito como conteúdo comum (`test_parse_cif_dom021_accepts_multiline_text_field_containing_save_substring`) e um token citado `'save_x'` é aceito como valor literal (`test_parse_cif_dom021_accepts_quoted_token_equal_to_save_prefix`), ao lado do teste já existente de recusa de um save frame real.

## 4. O que foi implementado (apenas a allowlist)

Edição aditiva sobre o commit `0d06ebd` (nunca reset/rebase/amend): `src/molecular/receptor_materialization.py`, `src/molecular/receptor_parsing.py`, `tests/test_receptor_materialization.py`, `tests/test_receptor_parsing.py`, mais `tests/fixtures/receptor_materialization/` (seis entradas reais do PDB documentadas em `PROVENANCE.json` próprios — §5). Nenhum outro arquivo do repositório tocado (confirmado em `evidence/claude-completion-git-log.txt`).

### 4.1 Decisões de design e seus limites (transparência para a revisão independente)

1. **`_pdbx_struct_mod_residue.parent_comp_id`** exige linha própria em `_chem_comp` exatamente quando a linha que o carrega é preservada/entra no fechamento (ver §3-bis) — a versão anterior desta mesma sessão isentava isso incondicionalmente; corrigida após o adendo de governance, confrontada com os três casos (presente/ausente/não-preservado) e com o depósito real 5I55 antes de aceitá-la como definitiva.
2. **A decodificação de identificador citado (`_decoded_token`)** é um no-op comprovado para todo identificador já não citado (os seis depósitos reais não mudam de resultado); não foi exercida por nenhum identificador genuinamente citado em nenhuma das seis fixtures reais — permanece uma correção defensiva, não uma prova positiva de que algum depósito real a exercite.
3. **`SPECIAL_POSITION_GUARD_THEN_OMIT`** continua resolvendo o contexto (label-ou-auth-unívoco) como guarda antes da omissão auditada, agora comprovado contra a linha real de 3DG1; a contagem de interseção retida/átomos únicos entre *múltiplas* linhas mistas (algumas em contexto retido, outras não) não foi implementada — nenhuma das fixtures reais disponíveis carrega mais de uma linha dessa categoria para testar essa contagem.
4. **`ANISOTROP_ATOM_ID`** continua verificando concordância de `pdbx_label_atom_id`/`pdbx_label_asym_id`/`pdbx_label_comp_id` (não `pdbx_label_seq_id`) contra o `_atom_site` referenciado — subconjunto do "demais campos informados concordam", não a verificação exaustiva de todas as colunas espelhadas.
5. **Nenhuma das seis fixtures reais exercita uma referência composta além da já implementada (`entity_poly_seq`)** — `pdbx_entity_branch_link`'s par `(entity_branch_list_num_1,comp_id_1)`/`(entity_branch_list_num_2,comp_id_2)` tem cobertura só via DTO sintético (T021-073), nunca um depósito real com entidade ramificada.
6. **Nenhum arquivo final (`receptor.cif`) é publicado** nesta entrega — persistência/registry/service continuam CP3.

## 5. Fixtures reais e proveniência (Seção 23)

Seis entradas públicas do PDB, baixadas por HTTPS direto (nunca um arquivo sintético escrito à mão), documentadas em `tests/fixtures/receptor_materialization/*/PROVENANCE.json` (origem, data, SHA-256 do original intocado, e — quando aplicável — a edição exata e listada que produziu o derivado `_trimmed.cif`, verificada por reparse Gemmi real comparando os conjuntos de categorias antes/depois):

| Entrada | Papel | Resultado real |
|---|---|---|
| **5I55** | T021-090/141/147 negativo honesto + conexão isolada | `materialize_receptor_cif021` recusa `INVALID_CIF`: construção de selenometionina cujo `parent_comp_id='MET'` entra no fechamento CCD, mas o depósito real nunca lista MET em `_chem_comp` (só MSE) — achado real, não defeito (ver §3-bis). O `covale1` (`both-identity`, `1_555`/`1_555` sem tabelas — T021-141) é comprovado isoladamente via `resolve_connection_decisions()` sobre os tokens reais, independente dessa recusa. |
| **1PFE** | T021-144/147 negativo | `materialize_receptor_cif021` recusa `UNSUPPORTED_SYMMETRY`: os 18 `hydrog` reais do depósito declaram `ptnr1_symmetry=1_555`/`ptnr2_symmetry=9_555` inteiramente dentro da cadeia retida A, sem tabelas de operador — nunca convertido em caso positivo, exatamente como o brief original exige. |
| **3DG1** | T021-147/158 positivo | Materialização completa; a linha real de `_pdbx_struct_special_symmetry` passa pela guarda com contexto resolvido. |
| **2JOF** | T021-149/162 NMR real | Seleciona o modelo 3 de 28 conformers reais explicitamente (nunca o primeiro); `other-models-excluded` auditado; 284 de 7952 linhas `atom_site` retidas — exatamente o próprio modelo 3. |
| **7DWU** | T021-149 EM real | Materialização completa de um depósito cryo-EM real (proteína do envelope + Fab), sem contexto cristalográfico. |
| **1A2P** | T021-150-154 NCS real | As duas linhas reais de `_struct_ncs_oper` (`code='given'`) são extraídas do depósito e executadas pelo guard puro diretamente — comprovadas sem recusa. **Limitação honesta, documentada em `PROVENANCE.json`:** a materialização completa desta entrada (selecionando só a cadeia A) é bloqueada por uma linha `struct_conn` real e não relacionada (`metalc2`, operador de simetria cristalográfica genuíno `3_675` sem tabela de prova) — um achado real sobre esta cristalografia específica, não um defeito do tratamento de NCS; o teste correspondente comprova exatamente essa recusa pelo código certo. |

`evidence/claude-completion-scenario-matrix.json` (derivada mecanicamente por AST + `pytest --collect-only`, nunca digitada à mão) mapeia os 79 IDs normativos a funções/itens de teste reais.

## 6. Cobertura dos 79 cenários

**79 de 79 cenários têm teste real mapeado** (função de produção real exercitada, nenhum `pytest.raises(Exception)` genérico, nenhuma asserção tautológica). Isso não é uma segunda alegação de "fechamento independente" — o arquiteto já advertiu que mapeamento não é prova integral nem aprovação; é o resultado honesto desta sessão, com as limitações explícitas do §4.1 e as seguintes notas de granularidade:

- Para os quatro cenários de matriz parametrizada (T021-051-054, T021-055-059, T021-164/166/168-172), a matriz de evidência lista todos os itens `pytest` da mesma função parametrizada sob cada ID — não um item único isolado por ID; cada item individual tem seu próprio `scenario_id` como parâmetro, verificável na saída de `--collect-only`.
- T021-147 (catalog-three-real) está marcado a partir dos três resultados de 5I55/1PFE/3DG1 em conjunto, nunca um substituto sintético único.

## 7. Reconciliação da coleta, regressão e limites

```
antes desta continuação (HEAD 0d06ebd, já reportado):  1622 coletados
após esta continuação (HEAD 60f9e0d):                   1655 coletados   (+33)

tests/test_receptor_parsing.py + tests/test_receptor_materialization.py:
  python -B -m pytest -p no:cacheprovider tests/test_receptor_parsing.py tests/test_receptor_materialization.py -q -rs
  -> 205 passed in ~5-10s

regressão 020 (inspection/selection/resolution/registry/service):
  -> 121 passed in ~10s

suíte completa:
  python -B -m pytest -p no:cacheprovider -q -rs
  -> 1650 passed, 5 skipped in 174.00s (evidence/claude-completion-full-suite.txt, capturada após o commit 60f9e0d)
```

`git diff --check`/`git show --check` limpos. `git diff --name-status ea8dac9...HEAD` e `...08b797e...HEAD` mostram exatamente os quatro caminhos de código mais a árvore nova de fixtures — evidência completa em `evidence/claude-completion-git-log.txt`. Os 92 testes de CP1, os 13 vetores-áureos e a regressão 020 permanecem intocados.

## 8. Identidades dos arquivos entregues (bytes do blob Git do commit publicado)

| Caminho | Linhas | Bytes | SHA-256 |
|---|---:|---:|---|
| `src/molecular/receptor_materialization.py` | 4381 | 209.266 | `3ec96abf14c05ce29e285d389e386a189b6b69f9244e307756003260ca8f9ba3` |
| `src/molecular/receptor_parsing.py` | 1703 | 69.418 | `51346d777c51866f51a17cd14689840b053969cec61bf72fb0e7a585f95a4ddd` |
| `tests/test_receptor_materialization.py` | 2787 | 146.902 | `67104670202d4887bb2f76287448604c8d4a81fc7c3913ec80c3ef3e1c47a286` |
| `tests/test_receptor_parsing.py` | 1258 | 50.965 | `25a11310ce08ed59ed857b0883d3ea8ba04a8aeaafbcf8ac189d54fa9523f49e` |

Fixtures reais: hashes completos em `evidence/claude-completion-file-identities.json`, recomputados do blob publicado.

## 9. Commit e publicação remota do código

```
commit b096af7ca8d47fd72cb739e0f5d90771ea07a112
parent  0d06ebd4c46c90e5446fec6f0eb72b4a8d2855db
branch  feature/increment-021-receptor-materialization
22 files changed, 58320 insertions(+), 80 deletions(-)

commit 60f9e0da5c67c3820747242a033db2f5d49b1817  (correções do adendo de governance, §3-bis)
parent  b096af7ca8d47fd72cb739e0f5d90771ea07a112
branch  feature/increment-021-receptor-materialization
5 files changed, 306 insertions(+), 37 deletions(-)
```

Push confirmado: `git rev-parse origin/feature/increment-021-receptor-materialization` devolve `60f9e0d...`; `git rev-parse origin/main` (código) continua `08b797e...`. Nenhum PR, merge, tag ou alteração de main.

## 10. O que não foi feito (fora do escopo autorizado)

- Nenhum CP3/CP4, nenhuma publicação de `receptor.cif` final, nenhum storage/registry/service/CLI.
- Nenhuma fixture adicional alem das seis listadas; nenhuma alteração do catálogo congelado (as correções do §3 operam inteiramente dentro do literal já pinado).
- `020-A` permanece em stand-by; itens locais protegidos de ambos os repositórios permanecem untracked e intocados; relatório/branch parcial do CP2 (`claude/021-cp2-implementation-report`) preservados sem sobrescrita.
- Nenhum PR, merge, tag, release ou alteração de `main` em nenhum dos dois repositórios.
- Nenhum fechamento independente de CP2 é declarado por este relatório.

## 11. Gate sugerido

Os seis grupos de correção (C-01 a C-06) e os quatro pontos do adendo de orientação de retomada (§3-bis) foram corrigidos e reverificados contra as sondas exatas do arquiteto; os 79 cenários normativos têm teste real mapeado, com as limitações explícitas do §4.1/§6 — não omitidas, não convertidas em aprovação tácita. Recomendo que o arquiteto confira esta entrega e decida se o critério de conclusão do CP2 está satisfeito para encaminhar à revisão independente final, ou se alguma das limitações declaradas (§4.1) exige mais uma rodada. Não declaro CP2 aprovado nem solicito avanço a CP3.

```
TASK_ID: 021-CHECKPOINT2-COMPLETION
ROLE: claude-implementer-separate-from-independent-reviewer
SCOPE_EXECUTED: CHECKPOINT2_COMPLETION
CODE_BRANCH: feature/increment-021-receptor-materialization
CODE_COMMIT: 60f9e0da5c67c3820747242a033db2f5d49b1817
CODE_PARENT: b096af7ca8d47fd72cb739e0f5d90771ea07a112 (itself child of 0d06ebd4c46c90e5446fec6f0eb72b4a8d2855db)
CODE_PUSH_VERIFIED: YES
CODE_MAIN_MODIFIED: NO
PR_OPENED: NO
MERGE_PERFORMED: NO
CP3_IMPLEMENTATION_AUTHORIZED: NO
C01_TO_C07_DISPOSITION: FIXED_AND_REVERIFIED_AGAINST_ARCHITECT_PROBES
GOVERNANCE_GUARDRAIL_ADDENDUM_625E538_DISPOSITION: ALL_FOUR_POINTS_FIXED_AND_REVERIFIED
SCENARIOS_MAPPED_TO_REAL_TESTS: 79 of 79 (declared limitations in Section 4.1/6, never hidden, never skipped-approved)
FULL_SUITE_PASSED: YES (1650 passed, 5 skipped - see evidence/claude-completion-full-suite.txt)
ARCH01_REVERIFIED: YES (gemmi/rdkit blocked via sys.modules sentinel)
PARTIAL_REPORT_AND_BRANCH_PRESERVED: YES (not overwritten)
READY_FOR_INDEPENDENT_FINAL_CP2_REVIEW: ARCHITECT_TO_DECIDE
CHECKPOINT2_APPROVED: NO
NEXT_GATE: ARCHITECT_RECEIPT_THEN_DECISION_ON_INDEPENDENT_FINAL_CP2_REVIEW
```
