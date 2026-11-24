# Revisão independente — Incremento 021, draft-1 da especificação

Tarefa: `021-DRAFT-REVIEW`. Papel: Claude, revisor independente, separado do implementador. Data: 23/11/2026, America/Sao_Paulo.

Escopo: rascunho, SCHEMAS, CATALOG (77 categorias) e as 140 linhas de SCENARIOS, lidos integralmente e confrontados com o código pinado e as fontes primárias do Gemmi 0.7.5. Não é aprovação de implementação, não congela contrato e não retoma o 020-A.

**Veredito: APPROVE FOR REVISED DRAFT PREPARATION.**

O que está sólido no draft-1:
- P-1, P-2, P-3 e NOTE-F1 ficam fechados como proposta.
- Os envelopes de hash não têm ciclos.
- O fluxo plan → declare → run não é circular.
- As garantias de publicação estão escopadas com honestidade.

Três MAJORs impedem tomá-lo como base de congelamento:
- **MAJOR-1** (P-4): a pré-condição de tabela de operadores torna inalcançável a célula de identidade para arquivos do arquivo PDB.
- **MAJOR-2** (P-5): o catálogo recusa os três mmCIFs reais testados.
- **MAJOR-3** (P-5): NCS não expandido é omitido em vez de recusado.

Há também 6 MINORs. Não há BLOCKER.

## 1. Gates e identidades

- **Gates:**
  - coordenação, HEAD remoto `b948f60245b71da71fa4535e8ef7ffa3957b35b4` antes do trabalho, igual ao despachado, com pai `3f0f1342…`;
  - código `main` em `08b797e0985e123ffd4d7ca7e5a5e8f040e63851`.
- **Materiais:** rascunho 344/50.807/`f914d56e…`; SCHEMAS 102/15.093/`6ae0bcc0…`; CATALOG 1.713/41.866/`d35f12c3…`; SCENARIOS 141/17.712/`fb907fbe…`; autorização 22/1.592/`0091f4d8…`. Todos conferem.
- **Manifestos:**
  - atual (10 itens), conferido em `b948f60`;
  - de preparação (6 itens), conferido em `3f0f134`, o próprio commit, sem comparar com arquivos atuais;
  - `SOURCE_AND_INPUT_IDENTITIES.json`: os 7 itens do governance conferem nos commits citados e os 12 do código conferem em `08b797e`.
- **Aprovações preservadas:** D-01(b)/D-02 em `771d1aa` (`8b5cc011…`) e focal anterior em `8778b83` (`231cbbf8…`).

## 2. Execução própria e limites

**Executado por mim, em scratch externo:**

1. **Inventário DOM** (`evidence/claude-cif-inventory-probe.cpp`): C++ só com cabeçalhos do Gemmi 0.7.5, g++ 13.3, Linux. Rodou sobre três mmCIFs reais da tag oficial: `tests/5i55.cif`, `tests/1pfe.cif.gz` (descomprimido em scratch) e `tests/3dg1_final.cif`.
2. **Cobertura do catálogo** (`claude-catalog-coverage.py`, stdlib, `python3 -I`): aplica `CATALOG_021.json` aos inventários.
3. **Equivalência da NOTE-F1** (`claude-notef1-equivalence.py`, PyYAML 6.0.3 do sandbox; o projeto pina `PyYAML>=6.0`): 11 casos sintéticos.

**Também:** checagens de consistência interna entre catálogo, cenários e corpo, e releitura dirigida do código e do Gemmi.

**Não houve:** pytest, Gemmi em Python, materialização, Windows, concorrência ou web. Três arquivos não são estimativa populacional. Os nomes de tag foram conferidos contra arquivos reais e a fonte Gemmi, não contra o DDL completo.

## 3. BLOCKERS

Nenhum.

## 4. MAJORS

### MAJOR-1 — P-4: a célula "identidade" é inalcançável para arquivos do arquivo PDB e do próprio Gemmi

O §10 exige que o operador `n` venha de `_symmetry_equiv` ou `_space_group_symop` da fonte, inclusive para `1_555` ("Isso inclui 1_555 sem operador fonte identificado"). Qualquer conexão com K>0 sem tabela vira `UNSUPPORTED_SYMMETRY`.

**Evidência própria:**
- Nenhum dos três arquivos reais traz qualquer das duas tabelas (`claude-catalog-coverage.output.json`, `operator_tables_present: []`).
- 5i55 tem um `covale 1_555/1_555`, e todo o seu `_struct_conn` é desse tipo; 1pfe tem 16 `covale 1_555/1_555`.

**Fonte primária:**
- O reader mmCIF do Gemmi não lê tabelas de operadores: classifica a mesma ASU por igualdade de códigos (`src/mmcif.cpp:213–217`) e obtém o grupo pelo nome H-M (`:1029`).
- O Gemmi mantém sempre a identidade como `sym_ops[0]` (`include/gemmi/symmetry.hpp:492–494`).
- O writer do Gemmi grava `ptnr1_symmetry = 1_555` sem emitir tabela (`src/to_mmcif.cpp:364–395`).

**Consequência:** ligações de resíduo modificado (MSE), dissulfetos, metais e ligantes covalentes são praticamente onipresentes. Com a regra atual, o perfil recusa quase todo receptor real com conexão retida, inclusive os cenários D-01(b) que o responsável aprovou (água removida/metal mantido exige K=2 nas demais linhas, ou K=1 com identidade).

A recusa é anunciada no §2, mas não está quantificada. A justificativa "não presumir n=1" não se sustenta para `1_555`: na convenção `n_klm`, o operador 1 da listagem padrão é a identidade, e é exatamente essa a convenção que o reader e o writer pinados usam.

**Exigência para o draft-2**, uma das duas opções:

- **(a) Recomendada.** Aceitar `1_555` nos dois lados como identidade pela convenção, sem tabela. Quando houver tabela na fonte, exigir que o operador 1 seja `x,y,z` e recusar contradição. Continuar recusando todos os outros códigos sem tabela.
- **(b)** Manter a regra, mas registrar como decisão expressa do responsável que o perfil não materializa receptores do arquivo PDB com conexões retidas, e retirar dos cenários positivos D-01(b) a pretensão de uso com arquivos reais.

Isso não amplia D-01/D-02: só muda a prova de identidade da P-4.

**Correlato (mesma família):** K=2 com códigos distintos é recusado "por outra imagem não materializada" (§10). O RAW também não materializa essa imagem, logo a razão não distingue derivado de fonte. O caso real 1pfe tem 18 linhas `hydrog 1_555/9_555`: um complexo DNA–droga que seria recusado mesmo sem nenhum corte. O draft-2 deve escolher entre preservar literal com `source_symmetry_only` e omitir com auditoria, ou justificar a recusa por outro motivo.

### MAJOR-2 — P-5: o catálogo recusa os três mmCIFs reais testados

Pela regra "tag desconhecida em categoria filtrada → recusa; categoria fora do catálogo → recusa", nenhum dos três arquivos passa (`claude-catalog-coverage.output.json`):

| Arquivo | Recusas observadas |
|---|---|
| 5i55 (arquivo PDB) | `_cell`: 22 tags desconhecidas (`*_esd`, `volume`, `reciprocal_*`, `details`, `formula_units_z`); `_symmetry.pdbx_full_space_group_name_H-M` |
| 1pfe (arquivo PDB) | as mesmas famílias de `_cell`/`_symmetry`; `_pdbx_unobs_or_zero_occ_atoms.label_alt_id`; 14 categorias fora do catálogo (`_pdbx_entry_details`, `_pdbx_struct_assembly_prop`, `_struct_biol`, `_refine_analyze`, `_pdbx_refine`, `_pdbx_molecule*`, `_entity_name_com`, `_exptl_crystal_grow_comp`, `_database_pdb_matrix`, `_struct_site_keywords`, `_ndb_struct_*`) |
| 3dg1_final (saída de refinamento) | `_pdbx_refine_tls`, `_pdbx_refine_tls_group` |

Por construção, entradas NMR (`_pdbx_nmr_*`) e cryo-EM (`_em_*`) também seriam recusadas. Isso conflita internamente com a maquinaria de modelo M ≠ primeiro (T021-009/019): no PDB, a população multi-modelo é sobretudo NMR.

**Argumento técnico:** a cautela "não inferir inocuidade pelo nome" se aplica a categorias *preservadas*. *Omitir* uma categoria nunca deixa referência stale nas categorias retidas, porque as `references` do catálogo só apontam para `atom_site`, `struct_asym`, `entity`, `chem_comp`, `entity_poly_seq` e `branch_list`. O custo da omissão é perda de informação, que já é auditada.

**Exigência para o draft-2:**
- Incluir as tags observadas acima.
- Decidir explicitamente entre listar mais famílias de metadados como omissão auditada (por exemplo, prefixos fechados `_pdbx_nmr_`, `_em_`, `_pdbx_refine_tls`, `_ndb_struct_`, `_pdbx_struct_conn_angle`) ou declarar NMR/EM fora do perfil e retirar a justificativa multi-modelo.
- Exigir pelo menos um fixture derivado de entrada real por caso positivo D-01(b), não só fixtures sintéticos com tabelas de operadores.

Exceções que *não* podem ser omissões cegas: MAJOR-3 e MINOR-5.

### MAJOR-3 — `_struct_ncs_oper` com `code ≠ given` é omitido, mas significa coordenadas fonte incompletas

O catálogo omite `_struct_ncs_oper` com auditoria (AUDIT_OMITTED_CATEGORY). No Gemmi pinado, operadores NCS não identidade com `code` diferente de `given` indicam cópias **ausentes** de `atom_site` (`src/mmcif.cpp:769–787`; `include/gemmi/model.hpp:1005–1012`, `ncs_not_expanded()`).

Omitir a categoria publica um derivado sem o sinal de que a fonte estava incompleta. O 020 também não detecta isso (nenhuma ocorrência de "ncs" em `src/molecular`).

**Exigência:** recusar no perfil inicial quando houver operador NCS não identidade com `code ≠ given` (inclusive nulo), com código de erro e cenário próprios. Omitir só quando todos os operadores forem identidade ou `given`. Não expandir NCS, porque isso continua excluído.

## 5. MINORS

**MINOR-1 — regex numérica com o su no lugar errado (§6).** A regex põe `(su)` antes do expoente. O Gemmi pinado lê o número inteiro, com expoente, e só então o `(su)` opcional (`include/gemmi/numb.hpp:19–41`). Isso também é a gramática CIF. Do jeito que está, `1.2e3(4)` válido é recusado e `1.2(4)e3` é aceito. Corrigir para `[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?(?:\([0-9]+\))?` e acrescentar um cenário.

**MINOR-2 — endpoint sem altloc (§9).** Recusar quando o altloc é nulo e o átomo tem variantes é desnecessário para calcular K. Pela P-3, todas as variantes da mesma ocorrência têm o mesmo destino, então K está determinado. Proposta:
- resolver para o conjunto de variantes de `(ocorrência, label_atom_id)` em M e preservar a linha literal;
- ajustar `ConnectionDecision.endpoint_atom_ids` para conjunto ordenado;
- manter a recusa para ambiguidade entre ocorrências distintas.

**MINOR-3 — `application_version` dentro de `PlanBinding`/`plan_key`.** Cada atualização da aplicação invalida todas as políticas declaradas e ainda não executadas, mesmo sem mudança científica. Profile, algorithm e catalogue já versionam a semântica. Recomendo manter `application_version` no `request_key` e no manifesto, mas fora do `plan_key`, ou justificar a escolha.

**MINOR-4 — tipo de `omit_tags`.** Nas 52 categorias omitidas, `omit_tags` é a string `"all"`. Nas demais, é uma lista; o corpo (§11) e o SCHEMAS falam em "listas disjuntas". Fechar como enum/sentinela documentado ou lista vazia + `action=omit`.

**MINOR-5 — `_pdbx_struct_special_symmetry` omitido sem aviso.** Átomos em posição especial têm ocupância reduzida por simetria. Os tokens são preservados, mas o derivado perde a explicação. Proposta: contar no audit e emitir um `WarningCode` quando a categoria existir com átomos retidos.

**MINOR-6 — editorial e operação.**
- O §17 contém uma frase truncada ("Input state não se aplica: usar…").
- O §14 deixa reservas órfãs em BUSY permanente sem procedimento documentado: descrever o procedimento manual de diagnóstico e remoção pelo responsável, sem automação.

## 6. Disposições de P-1 a P-5 e NOTE-F1

| Item | Disposição | Base |
|---|---|---|
| P-1 | **Fechado (proposta)** | A exclusão do complemento só vira decisão explícita com `acknowledge_exclusions_key = H(X)`. A exceção de K=1 exige "D=remove ou X reconhecido" (§9), coerente com o registro D-01(b). Exigir ack sempre que X ≠ ∅ é mais estrito do que pedi, mas é compatível com D-02. |
| P-2 | **Fechado (proposta)** | `acknowledge_outside_key` vinculado ao hash completo de O, que inclui `source_context_key` e M; `run` recaptura e recalcula. Sem circularidade: o preview calcula sem ack, a declaração recebe os hashes do usuário e o serviço nunca os copia. |
| P-3 | **Fechado (proposta)** | Uniformidade por asym para todo não polímero (água, macrolídeo, branched, micro-heterogeneidade); a tabela S/D distingue unidade física e chave de disposição. |
| P-4 | **Parcialmente resolvido** | As 15 células estão determinadas e a justificativa foi corrigida. Faltam a pré-condição de identidade (MAJOR-1) e a razão de K=2 distinto. |
| P-5 | **Parcialmente resolvido** | O catálogo é estruturalmente completo: 77 categorias, ações disjuntas, todas com cenário, regras presentes no corpo. A cobertura contra arquivos reais é insuficiente (MAJOR-2) e há o caso NCS (MAJOR-3), além de MINOR-4/5. |
| NOTE-F1 | **Fechado** | Caminhos e ids conferem com o código (`registry._load_input`, `receptor_registry` dirs, RAW em `inputs/proteins/<id>/`). O hash dos bytes antes da decodificação, mais UTF-8 estrito, CRLF/CR→LF, BOM preservado e `safe_load`, é equivalente ao loader 020 nos 11 casos executados (`claude-notef1-equivalence.output.json`). |

## 7. Demais verificações exigidas pela tarefa

- **Hashes:** os envelopes têm `kind`/`version`; `exclusions_key`, `outside_key`, decisões e linhas incluem `source_context_key`; `plan_key = H(PlanBinding)`. `policy_id` exclui `declared_at` e o hash do arquivo. `request_key` inclui `policy_file_sha256`. O manifesto não se auto-hasheia. Não encontrei ciclo. Nulos: os acks são null exatamente quando o conjunto é vazio, e o hash vazio é canônico e exibido.
- **Tokens e modelo:** distinção entre `?`/`.` e versões citadas, inserção canônica, `ptnr3` só nulo, recusa de `model_num` ausente/zero (contrariando o `or 1` do 020) e M explícito. Tudo coerente com o estudo. Sem promoção científica.
- **Publicação:** reserva `xb` real, rename de diretório sem substituição no Windows, proibição de `os.replace`, reuse com reserva órfã sem apagá-la, compensação só de recursos próprios. A garantia está corretamente limitada a escritores cooperantes. Não há falsa promessa de concorrência derivada de precheck.
- **Schemas, CLI e interrupções:** rigidez sem coerção, uma chamada por comando, banners por classe, `PostCommitError` com `committed`, preservação de `KeyboardInterrupt`/`SystemExit` e atividade com um único dono. Adequados como proposta.
- **Allowlist, checkpoints e cenários:** os cenários são distintos de funções e itens coletados, sem resultado fictício. Cenários a acrescentar: NCS `generate`, su com expoente, endpoint sem altloc, positivos com arquivo real e simetria `1_555` sem tabela (conforme a decisão do MAJOR-1).

## 8. Prontidão

O draft-1 é base adequada para um **draft-2** que resolva os MAJORs 1–3 e os MINORs, com a decisão do MAJOR-1 tomada pelo responsável se a opção (b) for preferida. Não está pronto para congelamento nem para implementação.

VERDICT: APPROVE FOR REVISED DRAFT PREPARATION
P-1/P-2/P-3/NOTE-F1: CLOSED AS PROPOSALS; P-4/P-5: PARTIALLY RESOLVED
READY FOR IMPLEMENTATION: NO
FINAL SPECIFICATION FROZEN: NO
INCREMENT 020-A: STAND-BY
CODE REPOSITORY MODIFIED: NO
ARCHITECT DOCUMENTS MODIFIED: NO
