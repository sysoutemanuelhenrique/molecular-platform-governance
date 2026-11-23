# Parecer independente — Incremento 021, estudo v1 + complemento de núcleo mínimo

Tarefa: `021-RECEPTOR-MATERIALIZATION-STUDY-REVIEW-V2`. Papel: Claude, revisor independente, separado do implementador. Data: 23/11/2026, America/Sao_Paulo.

Este parecer confronta o estudo e o complemento com o código pinado e a fonte oficial do Gemmi. Não é aprovação do responsável, não congela contrato e não autoriza implementação. O 020-A permanece em STAND-BY e não foi lido nem tocado.

**Veredito: APPROVE FOR DRAFT SPECIFICATION, com quatro MAJORs que a reconciliação deve absorver antes ou dentro do rascunho.** Nenhum BLOCKER impede usar o estudo como base do rascunho. Os MAJORs impedem tratar o primeiro recorte como fechado. Ver §8.

## 1. Gates e identidades

| Item | Esperado | Observado |
|---|---|---|
| Governance, branch `docs/020-a-candidate1-review-20261020` | snapshot despachado `e6848903b1d0b342470fed59e43d39e4482a471a` | HEAD remoto no clone = `e6848903…`; sem avanço |
| Código, `main` | `08b797e0985e123ffd4d7ca7e5a5e8f040e63851` | idem, clone raso somente leitura fora do governance |
| Gemmi | tag `v0.7.5`, objeto `f73148f5…`, commit `5cc1c23c…` | idem, clone raso da tag oficial |
| Despacho | tarefa `PREPARED / NOT_DISPATCHED` | acionada por mensagem direta do responsável nesta sessão; a tarefa não foi editada |

Todos os inputs da tarefa conferem byte a byte (linhas, bytes, SHA-256): estudo v1 `5048c501…` (365 linhas; 55.594 bytes); referência 020 `cf6cb534…` (1.975; 210.880); complemento `f5e40770…` (157; 20.979); quatro evidências v1 e `continuation-verification.json` `e99ddacf…`. Os itens do manifesto da continuação também conferem: STATUS `c733981a…`, registro do responsável `918e12a8…` e tarefa `73a8c075…`. Os quatro arquivos-fonte que reli conferem com os SHA-256 de `continuation-verification.json`: `atomic.py`, `receptor_parsing.py`, `receptor_resolution.py` e `receptor_service.py`. Contagens independentes: 66 arquivos rastreados e 152 funções `test_` nos seis `tests/test_receptor_*.py` (contagem por AST, sem coleta pytest). Os sete blobs Gemmi que reutilizei conferem com `gemmi-source-identities.json`.

`CLAUDE.md` ainda aponta o bootstrap do 020-A. Segui `STATUS.md` e a tarefa V2, como a própria tarefa determina.

## 2. Método e limites da minha execução

- **Leitura integral**: estudo v1, complemento, registros do responsável e as seções do N020 exigidas (§§7, 14, 16, 18, 20–25, 33–34; demais por busca dirigida).
- **Confronto estático**: código pinado em `receptor_parsing.py`, `receptor_inspection.py`, `receptor_selection.py`, `receptor_resolution.py`, `receptor_service.py`, `receptor_registry.py`, `registry.py`, `atomic.py`, `pyproject.toml` e testes de receptor.
- **Fonte Gemmi 0.7.5**: `python/read.cpp`, `python/cif.cpp`, `python/mol.cpp`, `docs/cif.rst`, `include/gemmi/cifdoc.hpp`, `src/assembly.cpp`. Consultei também, além do conjunto do estudo, `src/mmcif.cpp` (blob `1da0854c…`) e a amostra oficial `tests/5i55.cif`.
- **Execução própria**: uma sonda C++ só com cabeçalhos do DOM CIF do Gemmi 0.7.5, compilada em scratch externo (g++ 13.3, Linux). Fonte e saída estão em `evidence/claude-gemmi-cif-token-probe.*`. Ela exercita `read_memory`, `is_null`, `as_string`, `quote`, `Loop::add_row` e `write_cif_to_stream`. Não é o wheel/binding Python, não é Windows e não é materialização.
- **Não executado**: pytest, Gemmi em Python (indisponível aqui; instalação não autorizada), Windows/NTFS, concorrência, transformação científica.
- **Sem web**: os pedidos de acesso a páginas wwPDB/RCSB ficaram sem resposta. Afirmações que dependeriam do arquivo PDB público ficam marcadas como "não verificado nesta sessão".

## 3. O que conferiu (afirmações F do estudo)

Conferem com o código pinado as seguintes afirmações:

- §3.1: `ParsedAtom` não tem coordenadas; `_pdbx_struct_oper_list` não é lido.
- §3.2: `_resolve_assembly` só confirma o id; `_resolve_chains` não verifica membership de assembly; `selected_chains=()` é legal.
- §3.3: baldes água/metal precedem as entradas nomeadas com `seen` por `(label_asym_id, ccd_code)` (`receptor_service.py` 561–627).
- §3.5: `or Decimal("1")` em `receptor_parsing.py:641`; ocupância zero vira 1, e `_build_altloc_and_occupancy_observations` então não a registra.
- §3.6: `selection_capability` não considera truncamento (`receptor_inspection.py:838`); `parser-limitation` é só um warning de `_truncate_with_limit_warning`.
- §13: `atomic_write_text` + `os.replace`; `publish_staged_directory` = precheck + `os.rename`; `_AUTHORIZED_ROOT_TEMPLATE = "inputs/ligands/{input_id}"`; perfil Windows/NTFS.
- `inspection_id`: o payload inclui schema/profile/parser/protein/raw/format.

Conferem com a fonte Gemmi:

- G01: overloads `read_string(str)` e `read_string(bytes)`.
- G02/G06: o DOM guarda tokens brutos com aspas; `add_row` espera tokens já citados.
- G04: `transform_to_assembly(..., merge_dist=0.2)`.
- G05: `finalize_expansion` só copia conexões `Asu::Same` (ou NCS), limpa assemblies e, sem `keep_spacegroup`, impõe `"P 1"` e zera a cela.

A sonda confirmou empiricamente, no C++, o núcleo da continuação §6:

- `?` e `.` são nulos; `'?'` e `'.'` não são.
- Copiar tokens brutos via `add_row`, serializar e reler preserva os tokens de forma idêntica, inclusive `0.000`, `1.20(3)`, `"it's"` e campo de texto multilinha.
- `quote()` aplicado a token bruto corrompe o valor: `'?'` vira `"'?'"`, e o nulo `?` vira o texto `'?'`.

Isso reforça a proibição de `quote_list` sobre tokens já representados.

## 4. Correções factuais

**C-1 (evidência inconsistente):** `evidence/study-verification.json` registra `"gemmi_available": true`, mas o estudo diz em §10 e §18 que Gemmi não estava instalado e que nenhuma execução Gemmi ocorreu. Uma das duas afirmações está errada. A reconciliação deve corrigi-la em artefato novo, sem editar o histórico. Não afeta conclusões, porque nenhuma delas depende de execução.

**C-2 (limitação do 020 não declarada, relevante ao 021):** o 020 lê `_struct_conn.ptnr1_PDB_ins_code` e `ptnr2_PDB_ins_code` (`receptor_parsing.py:386,398,512,527`). O nome no dicionário e nos arquivos wwPDB é `pdbx_ptnr1_PDB_ins_code` / `pdbx_ptnr2_PDB_ins_code`:

- é o que o reader oficial do Gemmi 0.7.5 usa (`src/mmcif.cpp:206`);
- é o que aparece na amostra oficial `tests/5i55.cif:704,712`;
- a coluna lida pelo 020 não aparece nessa amostra.

Consequência: em arquivos reais, `StructConnEndpoint.insertion_code` do 020 tende a ser sempre `None`. O N020 não nomeia a coluna (busca sem ocorrência) e nenhum teste do 020 usa código de inserção em `_struct_conn`. É defeito de implementação do 020, não de contrato. Este parecer não o reabre. O estudo, porém, não o menciona, e o 021 depende de "correspondência inequívoca" de endpoints (ver MAJOR-3).

**C-3 (precisão):** `report.chains` não é só de cadeias poliméricas. `_build_chains` agrupa todo `(model, label_asym_id, auth_asym_id)`, inclusive asyms de água, ligante e glicano. Já `NonPolymerComponent` não tem `model_number`. As frases do estudo "cadeias poliméricas não selecionadas saem por consequência" (§7.1) e "universo a partir das linhas do modelo fonte" (§7.2) supõem uma separação que o 020 não faz (MAJOR-2).

## 5. BLOCKERS

Nenhum.

## 6. MAJORS

### MAJOR-1 — "Recusar todo corte declarado" colide com os baldes ASU-amplos; a utilidade alegada do perfil mínimo não foi demonstrada

O complemento (§2, §3.6) recusa qualquer conexão com exatamente um endpoint retido e afirma que o recorte "continua produzindo um resultado útil". O 020, porém, resolve os baldes sobre todo o inventário, sem escopo de cadeia nem de modelo (`receptor_service.py:583`). Uma entrada nomeada não substitui um balde já aplicado (`seen`). Daí decorrem recusas sistemáticas, sem remédio dentro de uma política que use baldes:

- **Água removida + metal mantido** com `metalc` metal–HOH declarado: um endpoint removido, logo recusa.
- **Uma cadeia de um oligômero + `metal_disposition=keep`**: metais coordenados pela cadeia não selecionada são mantidos pelo balde e seus `metalc` cortam. Recusa, e o cientista só escapa abandonando o balde e nomeando cada metal.
- **Ligante removido + metal mantido** coordenado pelo ligante: recusa.

Não pude medir a frequência no arquivo PDB nesta sessão (sem web). A ocorrência de `metalc` envolvendo HOH e de metais em interfaces é padrão conhecido de anotação, mas aqui fica como **não verificada**. O próprio estudo v1 (§8) reconhece que `conn_type` não tem semântica uniforme. Ainda assim, o complemento trata `covale`/`disulf` (valência aberta) e `metalc`/`hydrog` (coordenação ou contato declarado) do mesmo modo.

**Exigência para o rascunho**, uma das duas opções, por decisão explícita do responsável:

- **(a)** Manter a recusa total, mas declarar a cobertura perdida como limite do perfil, com diagnóstico tipado que nomeie a linha de conexão e o remédio (ex.: política sem balde). Testar os três casos acima como recusas esperadas.
- **(b)** Distinguir por tipo. `covale*`/`disulf` com um endpoint removido: recusa incondicional. `metalc`/`hydrog` cujo endpoint removido pertence a um componente removido inteiro por disposição efetiva: omitir a linha com auditoria, sem reparo e sem alegação de valência.

Recomendo (b) por fidelidade científica, mas isso é decisão de escopo, não exigência deste revisor. Em qualquer caso, a afirmação de utilidade do §2 do complemento deve vir acompanhada dos casos que o perfil recusa.

### MAJOR-2 — O universo de ocorrências e a precedência cadeia × disposição × complemento não estão definidos de forma implementável

Pelo código do 020, o mesmo `label_asym_id` não polimérico pode aparecer em `resolved_chains` (seletor de cadeia aceito), receber disposição por balde ou por nome, ou não ter nenhuma. Os baldes valem para todas as cadeias e todos os modelos. O estudo fixa só fragmentos:

- conflito "cadeia selecionada + remove" (v1 §7.1; complemento §4);
- complemento explícito para ocorrências sem disposição (v1 §7.2).

Ficam sem regra:

1. Um asym não polimérico listado como cadeia e **sem** disposição: retido pela seleção ou tratado como não abordado?
2. Um asym polimérico **não** selecionado que contém resíduo modificado com disposição `keep`, ou uma água/ligante cujo `auth_asym_id` pertence a uma cadeia não selecionada e que `keep` ou "preservar não abordados" retém.
3. Asyms `branched` (glicanos), que o 020 classifica resíduo a resíduo como `other-non-polymer`.
4. `pdbx_PDB_model_num` ausente, caso em que o 020 assume modelo 1 (`or 1`).

O caso 2 produz um derivado com águas e ligantes que circundam uma cadeia ausente. Isso é cientificamente enganoso, ainda que fiel à resolução.

**Exigência:** o rascunho precisa de uma tabela de decisão fechada. Para cada ocorrência (linha de `_atom_site` no modelo resolvido), ela classifica o asym pela `_entity.type` da fonte e define a combinação seleção de cadeia × disposição efetiva × complemento → incluir / excluir / recusar, com justificativa. O relatório do artefato deve contar e listar as ocorrências retidas cujo `auth_asym_id` pertence a cadeia não selecionada, ou declarar explicitamente que o escopo dos baldes é a ASU inteira. A tabela não pode reinterpretar a resolução 020 (complemento §4 continua válido); deve apenas tornar visível o efeito.

### MAJOR-3 — Correspondência de endpoints de conexão: fonte dos tokens, colunas e casos não cobertos

O plano de conexões (v1 §8; complemento §3.6) exige endpoints "inequívocos", mas não diz de onde vêm nem quais colunas formam a chave. Pela C-2, reutilizar `ParsedConnection`/`StructureConnection` ou a lista `_STRUCT_CONN_COLUMNS` do 020 perde o código de inserção. Com isso, resíduos `52` e `52A` ficam indistinguíveis: a correspondência fica ambígua (recusa espúria) ou, pior, errada se a chave usar só auth ids.

O rascunho deve exigir que o 021 leia `_struct_conn` diretamente dos tokens brutos do RAW verificado, com o conjunto de colunas do dicionário: `pdbx_ptnr{1,2}_PDB_ins_code`, `pdbx_ptnr{1,2}_label_alt_id`, label e auth. Deve também:

- registrar a divergência do 020 como limitação conhecida, sem corrigi-lo no 021;
- incluir fixture com código de inserção em `_struct_conn`.

Lacunas adicionais a decidir no rascunho:

- **Terceiro parceiro:** colunas `pdbx_ptnr3_*` existem em arquivos reais (`5i55.cif`). Recomendo recusar linhas com qualquer `pdbx_ptnr3_*` não nulo no perfil mínimo.
- **Simetria:** deve ser definida como no reader Gemmi, por comparação `ptnr1_symmetry == ptnr2_symmetry` (`src/mmcif.cpp:216`), e não "cada endpoint ≠ 1_555". Simetria ausente (`?`) num dos lados deve ser contexto não suportado, portanto recusa, e não "mesma ASU".
- **NMR:** `_struct_conn` não tem coluna de modelo. A regra deve dizer que a conexão é avaliada no modelo resolvido.

### MAJOR-4 — Sequência de vínculo do §5 é internamente inconsistente com a allowlist

O v1 §5 pede ao mesmo tempo "usar as APIs públicas de leitura" (passo 2) e "medir hashes dos bytes carregados … em uma leitura controlada; não montar o contexto a partir de leituras sucessivas" (passo 4). Os loaders públicos do 020 (`receptor_registry.py:107,195,298`; `registry.load_protein`) fazem `read_text` + `model_validate` e devolvem só o modelo, sem bytes. Hashear os bytes exige uma segunda leitura, o que é exatamente a mistura de versões que o passo 4 proíbe. Alterar os loaders do 020 está fora da allowlist (v1 §16).

O rascunho deve escolher um mecanismo:

- **(i)** Leitor próprio do 021, que lê os bytes uma vez, valida com o mesmo modelo Pydantic 1.0 e hasheia os mesmos bytes, sem chamar nem alterar o loader 020.
- **(ii)** Abandonar o hash de metadados na chave e documentar a janela.

Em ambos os casos, exigir igualdade exata (sensível à caixa) entre o id solicitado e o id gravado no registro carregado. Em NTFS, `…/<id>.yaml` é resolvido sem distinção de caixa, e os loaders 020 não conferem o id interno contra o pedido. A mesma disciplina vale para o RAW: o v1 §5.6 e o complemento §8 já exigem bytes capturados, o que está correto. Note que o próprio 020 lê o RAW três vezes por caminho (checksum, `read_structure`, `cif.read`; `receptor_parsing.py:889,907`), e o 021 não deve herdar esse padrão.

## 7. MINORS e NOTES

**MINOR-1 — Resíduo polimérico modificado.** O v1 recusa remoção que "cortaria o interior". Recomendo a regra mais simples e verificável: no perfil mínimo, recusar qualquer `remove` efetivo de componente classificado `modified-polymer-residue`, inclusive nas extremidades. A remoção terminal também altera a relação com `_entity_poly_seq`/`_pdbx_poly_seq_scheme`. A cadeia inteira continua removível por seleção.

**MINOR-2 — Glicanos/branched.** O 020 cria um `NonPolymerComponent` por resíduo de um asym `branched`. Remover `(asym, NAG)` e manter `(asym, BMA)` parte o oligossacarídeo. Não verifiquei nesta sessão se as ligações glicosídicas internas aparecem em `_struct_conn` ou só em categorias de entidade ramificada. Se não aparecerem, a checagem de cortes não detecta a quebra. Recomendo tudo-ou-nada por asym `branched` no perfil mínimo.

**MINOR-3 — Catálogo (Q-03).** Além das categorias da tabela do v1 §8, o catálogo deve classificar explicitamente categorias que referenciam resíduos/átomos e ficariam stale num recorte:

- `_struct_conf`, `_struct_sheet_range`, `_struct_mon_prot_cis`, `_struct_site`/`_struct_site_gen`;
- `_pdbx_struct_mod_residue`, `_pdbx_nonpoly_scheme`, `_pdbx_branch_scheme`, `_pdbx_entity_branch*`;
- `_pdbx_struct_special_symmetry`, `_struct_conn_type`, `_atom_type`;
- `_pdbx_validate_*`.

Gemmi escreve várias delas a partir de `Structure` (`to_mmcif.cpp`), mas o caminho DOM proposto não as gera. Cada uma deve ser preservada-filtrada por chave, omitida com auditoria ou motivo de recusa.

**MINOR-4 — `parser-limitation` como gate normativo.** Como `selection_capability="full"` independe de truncamento, a checagem do v1 §5.7 deve ser o warning `parser-limitation` em qualquer categoria. Um exemplo concreto: com mais de 50.000 entradas não poliméricas (uma por resíduo de água), os baldes são resolvidos sobre lista truncada na ordem de parse.

**MINOR-5 — Matriz de cenários.** O complemento mantém 48 ids com semântica trocada em P021-20–25/26–33 e pede reenumeração. Concordo. O rascunho deve emitir ids novos ou declarar a substituição por id, e acrescentar os casos dos MAJORs 1–3 e da C-2.

**NOTE-1.** A sonda mostra que a preservação de tokens pela via DOM é viável e determinística na serialização do C++ em Linux. Não prova o binding Python, o comportamento em Windows (fim de linha) nem a correção de uma implementação futura. Esses ficam para o CP2/CP3.

**NOTE-2.** `atomic.py:868` já usa criação exclusiva (`"xb"`) dentro do snapshot de ligantes. É precedente local para a reserva por chave da Q-06, sem implicar reuso do helper.

**NOTE-3.** A separação declaração × execução do complemento §5 resolve bem a Q-04. A proibição de scaffolding vazio é coerente com o registro do responsável.

## 8. Opções A/B/C e disposição Q-01–Q-09

**A vs B vs C.** A ignora disposições já confirmadas e não materializa a seleção. Concordo em rejeitá-la como primeira entrega, salvo pedido explícito do responsável. C exige mapeamento de cópias, operadores e conexões que o Gemmi não fornece com fidelidade: o `finalize_expansion` descarta conexões entre ASUs diferentes, limpa assemblies e impõe P1 (G05, confirmado). Estudá-la agora alargaria o escopo sem fixtures. O perfil mínimo de B (referencial do modelo fonte, todos os altlocs, sem cortes) é defensável e coerente com o N020 §34.2, que lista possibilidades e não obrigações, desde que os MAJORs 1–2 tornem visíveis os casos recusados e o escopo dos baldes.

| Q | Disposição do revisor | Natureza |
|---|---|---|
| Q-01 | Aceita: B mínimo com recusa tipada de `resolved_assembly` não nulo, anunciada na CLI e no registro | Fechada para o rascunho |
| Q-02 | Aceita a ausência de reconhecimento manual por conexão; a definição de "corte" e a cobertura ficam pendentes da escolha (a)/(b) do MAJOR-1 | Decisão do responsável no rascunho |
| Q-03 | Aberta; condição para autorizar o writer; incluir MINOR-3 e as colunas do MAJOR-3 | Rascunho |
| Q-04 | Aceita: duas operações no serviço; fachada CLI opcional | Fechada para o rascunho |
| Q-05 | Aberta; depende do mecanismo do MAJOR-4; recusa de registro referenciado alterado é adequada | Rascunho |
| Q-06 | Aberta; reserva exclusiva + bundle por rename; prova real em Windows/NTFS no CP3 | Rascunho + gate de implementação |
| Q-07 | Aberta; recomendo começar por reserva diagnosticável + erro estruturado + activity, e só adotar registro de tentativa se a matriz de falhas exigir | Rascunho |
| Q-08 | Aceita a preferência por storage específico de proteína, sem alterar `atomic.py` por padrão | Fechada para o rascunho |
| Q-09 | Aberta; incluir o gate `parser-limitation` (MINOR-4) | Rascunho |

Nenhuma questão aberta impede o rascunho. Todas impedem implementação enquanto abertas, como o próprio estudo declara.

## 9. Veredito e próximos passos

**APPROVE FOR DRAFT SPECIFICATION.** O estudo e o complemento estão factualmente corretos nas afirmações centrais, salvo as correções C-1 a C-3. O recorte mínimo é implementável e não alega fidelidade experimental geral nem preparo químico. A preservação de tokens tem base verificada.

O recorte ainda não está completo o bastante para ser congelado. A reconciliação do arquiteto deve responder aos MAJOR-1 a 4 antes de o rascunho ser apresentado ao responsável, ou incorporá-los como seções obrigatórias dele.

Perguntas que restam ao responsável:

1. Escolha (a) ou (b) do MAJOR-1.
2. Se o escopo ASU-amplo dos baldes deve apenas ser declarado ou também gerar recusa quando ocorrências retidas pertencem a cadeias não selecionadas (MAJOR-2).

READY FOR DRAFT SPECIFICATION: YES, conditioned on MAJOR-1–4 reconciliation
READY FOR IMPLEMENTATION: NO
FINAL SPECIFICATION FROZEN: NO
INCREMENT 020-A: STAND-BY
CODE REPOSITORY MODIFIED: NO
ARCHITECT DOCUMENTS MODIFIED: NO
