# Revisão adversarial independente — Incremento 021, Checkpoint 2

Claude revisor independente, sessão separada da implementação. 25/11/2026, America/Sao_Paulo. Tarefa `tasks/021-CHECKPOINT2-ADVERSARIAL-REVIEW.json`. **Parecer de revisão, não aprovação do CP2 nem autorização de CP3.** Código revisado estritamente em leitura; nenhuma correção implementada.

## 1. Gates de snapshot e identidades

| Ref | Esperado | Observado no remoto |
|---|---|---|
| Governance `docs/020-a-candidate1-review-20261020` (despacho) | c9e02f0290cd522c8b94b0ade3998ca59976b048 | idem; pai 3775347 → 1c7906d (cadeia do arquiteto, não drift) |
| Governance `main` | a47183dfec8213c765ed43ae482c8c227760a3d5 | idem |
| Relatório final `claude/021-cp2-final-residual-report-20261125` | 81a650379d2374081176f9df0b37263e56e2b578 | idem |
| Código `feature/increment-021-receptor-materialization` | a807b03f44089eb3cbacc14f871b63689a21aec9, pai a8d46675 | idem |
| Código `main` | 08b797e0985e123ffd4d7ca7e5a5e8f040e63851 | idem |
| CP1 aprovado / baseline | ea8dac9 / 08b797e | ambos ancestrais de a807b03 |

- Os 11 inputs da tarefa (handoff, verificação, sonda, manifesto, especificação, 4 anexos, brief, autorização) conferem em linhas LF, bytes, SHA-256 e blob Git. A especificação e os anexos não mudam desde o commit de congelamento b0e60f6.
- Todas as 41 entradas de `INDEPENDENT_CP2_REVIEW_INPUT_IDENTITIES.json` foram verificadas por `git show <commit>:<path>` (bytes, linhas, SHA-256, blob): 41/41 OK, inclusive os 22 arquivos de código/fixtures em a807b03. R-CP2-04 está fechado.
- A chave do pacote normativo foi recalculada pela canonicalização 021: `d1726d1ae0ae5929e6f8a97f9bb0916e3e205af6d841246b7fba58972570f69b`, igual.
- A constante `CATALOGUE_SHA256` é igual aos bytes do anexo. A projeção `_FROZEN_CATALOGUE` coincide com as 94 categorias do anexo em `action/key/required/preserve/omit/generate/row_rule/references`, com 0 divergências. `required_categories` e `conditional_categories` também coincidem.

## 2. Método, materiais e limites

Li integralmente a especificação congelada, os quatro anexos, o brief CP2 e os recebimentos 36/37/38/39. Revisei o código real em a807b03: os trechos 021 de `receptor_parsing.py` (l.1030–1795) e o motor CP2 de `receptor_materialization.py` (conexões/simetria l.1861–2321, catálogo l.3450–4577). Os relatórios do implementador serviram só como rastreio.

**Execução própria (não é evidência fornecida):**
- **Gemmi 0.7.5 nativo real**, compilado do pin `project-gemmi/gemmi@5cc1c23c6007e0e6cbd69289c6f7c0bff50e943e` (tag v0.7.5) com nanobind v2.9.2, num diretório isolado `/tmp` e via PYTHONPATH. Não houve instalação global nem stub. `gemmi.__version__ == "0.7.5"`. O SHA-256 do módulo está no log de sondas.
- Ambiente: Linux x86_64, Python 3.13.18, pytest 9.1.1, pydantic 2.13.5. typer/click/rich e dependências puras vieram de tags GitHub, também no PYTHONPATH isolado, só para coletar a suíte. RDKit ausente.
- Cópia externa por `git archive` de cada SHA. O repositório original não foi modificado.
- 14 scripts de sonda chamam funções de produção. Os contraexemplos passam pela entrada real `materialize_receptor_cif021`, com SourceContext construído a partir dos bytes reais de cada sonda (hash e tamanho verdadeiros).

**Leitura do log de sondas:** duas linhas `matches_contract:false` em `p_identity_basis` são erros de expectativa do revisor, não do código:
- `dup_id_same_table` recusa INVALID_CIF, o que o §10.1 permite na última frase (not-applicable não contorna chaves duplicadas).
- `op1_in_both_tables_concordant` em K=0 usou uma expressão não citada com espaços, que é CIF malformado; o caso foi refeito em `p_ib2` e está conforme.

As demais 24 linhas `false` sustentam os achados da §4.

**Limites:** não há Windows/NTFS/concorrência (gate do CP3), nem RDKit. Não refiz o download RCSB: a origem externa das fixtures não está certificada; conferi manifestos e linhagem. Python 3.13 aqui, contra 3.14.7 no Windows do implementador. A execução nativa é Linux. Ela prova o adapter, não o perfil de produção Windows.

## 3. Escopo, allowlist e whitespace

- `git diff --name-status` CP1..HEAD e baseline..HEAD: exatamente os 4 caminhos permitidos mais 18 fixtures/manifestos sob `tests/fixtures/receptor_materialization/`. Não há CP3 (storage/registry/service), CLI, `pyproject.toml`, `atomic.py`, `activity.py` nem módulos 020 alterados.
- As fixtures contêm só `.cif` e `PROVENANCE.json`, sem código executável.
- `git diff --check`: 56.400 avisos de trailing whitespace, **todos** nos 12 `.cif` depositados. Fontes e testes estão limpos, e `git show --check HEAD` também. É formatação de depósito, não defeito; reescrever RAW seria violação (NOTE-1).
- Fronteira Gemmi: domínio e adapter importam sem carregar Gemmi/RDKit, em modo normal e `-O`, com finder bloqueador real. Com o motor bloqueado, a primeira entrada dá `ENGINE_UNAVAILABLE`. Com o motor real, o parse funciona. Não há `assert` em produção.

## 4. Achados

### BLOCKERS: 0

### MAJOR-1 — C-06: save frames genuínos escapam da guarda e seu conteúdo some sem recusa

`receptor_parsing.py:1033` usa `^save_\S`, sensível a caixa e só na coluna 0. A gramática do Gemmi 0.7.5 (`include/gemmi/cif.hpp:75`, `TAOCPP_PEGTL_ISTRING("save_")`) aceita `SAVE_x` e `save_x` indentado. O Gemmi guarda o frame como item separado, e `get_mmcif_category_names()` não o enumera.

Contraexemplo nativo pela produção: acrescentar `\n  save_fr\n_x.y 1\nsave_\n` (ou `SAVE_fr`) ao RAW. O resultado é ACCEPTED, sem `_x` no plano, na saída ou na auditoria. O controle em coluna 0 minúscula recusa.

Isso viola o §6 ("sem save frames") e o fechamento do catálogo (§11: categoria não listada é recusa), além de produzir perda não auditada. Correção esperada: detectar frames no DOM Gemmi (itens frame do bloco) ou com gramática equivalente, sem parser artesanal; preservar os positivos de texto multilinha e token citado.

### MAJOR-2 — C-01: gramática numérica aplicada a valores decodificados; inteiros e formal_charge sem gramática

O §6 exige tokens numéricos **não citados** casando a regex, e `model_num`/`formal_charge` como inteiro decimal não citado. As validações (l.3794–3827, 3829–3852, 3727–3745) recebem a visão decodificada (`_build_category_tables`, parsing l.1497–1500), em que `'1.000'` vira `1.000`. `model_num` usa `int()` (parsing l.1388), que aceita `'1'` decodificado e `+1`. `pdbx_formal_charge` não tem validação nenhuma.

Contraexemplos nativos ACCEPTED: `Cartn_x='1.000'`, `occupancy='1.00'`, `B_iso='10.00'`, `model_num='1'`, `model_num=+1`, `formal_charge=abc`/`1.5`/`'1'`, componente NCS `'1'`, componente de tensor U `'0.1'`.

Corretos: `1.2(4)e3` e `1_000` recusam; NCS identidade exata Decimal; translação 1e-7 com generate recusa. Validar sobre o token cru após o teste de null real, sem converter tokens para escrita.

### MAJOR-3 — C-02/T021-173/T021-041: '?' e '.' citados em ptnr*_symmetry viram null no domínio

O adapter decodifica corretamente (`'?'` → string `?`). Mas `_resolve_symmetry_endpoint` (l.1980) reaplica `_raw_cif_token_to_optional` sobre o valor **decodificado** e o trata como null real.

Contraexemplo nativo em K=0: `ptnr1_symmetry='?'` com `ptnr2 1_555` sem tabelas dá `symmetry_class=one-null`. O §10.1 passo 1 e T021-173 exigem valor literal malformado, logo `unsupported-discarded`. A ConnectionDecision, `connection_decisions_key` e `plan_key` ficam iguais aos de `?` cru (só `row_key` difere). Em K>0 o resultado final ainda é recusa, por outro motivo. O mesmo vale para `'.'`. Deve-se transportar a distinção null-real versus literal até o resolver.

### MAJOR-4 — C-05/T021-067/082/085/087/088: `_chem_comp` e `_entry` contornam as guardas genéricas

Ambas as categorias saem do laço genérico (l.4130–4133). Para `_chem_comp`, não se chama `_validate_key_integrity`; para `_entry`, não se verifica tag nem chave.

Contraexemplos nativos ACCEPTED:
- `_chem_comp.id` duplicado (ALA duas vezes): a saída escrita contém ALA, CYS, ALA.
- `_chem_comp.id` nulo: a linha é filtrada como omitida, sem recusa (o anexo diz `nonnull_key: true`).
- `_entry.zz_unknown` aceito, embora o anexo diga `unknown_tag_action: reject`.
- `_entry` com duas linhas aceito.
- A linha `_entry` fonte gera CategoryDecision com `source_rows_key=null` e listas de linhas vazias. SCHEMAS §4 só admite null para categoria ausente ou gerada **sem fonte**, e exige cobrir as linhas presentes. A linha original não fica auditada.

### MAJOR-5 — C-05/T021-072–074: referências compostas de branch não validadas

O comentário em l.3595–3599 e l.4177–4182 remete a uma "lógica específica" para referências compostas. Para branch, essa lógica não existe: não há validação de `entity_branch_list_num_{1,2}` → `pdbx_entity_branch_list(entity_id,num,comp_id_{1,2})`, nem de `pdbx_branch_scheme.num` → lista, nem dos átomos retidos contra a lista (entity,num,comp).

Contraexemplos nativos ACCEPTED: um link com `num_1=9` inexistente; e uma lista com NAG/BMA trocados em relação aos átomos. O §11 exige "cada link referencia entidade/lista/CCD válidos" e diz que as referências de branch usam entity_id/num/comp_id em conjunto. Os positivos (lista inteira mantida, MAN não observado preservado, categoria ausente recusa, P-3 NAG remove/BMA keep recusa) estão corretos.

### MAJOR-6 — T021-157/§6/§9: ocorrências indistinguíveis fundidas num mesmo conjunto de endpoint

Duas águas em `C` com o mesmo `auth_seq=52`, inserção `?` e átomo `O`, sem altloc, recebem a mesma chave de ocorrência (l.742–747). O endpoint resolve o conjunto `{6,7}` (dois átomos físicos distintos) e o plano é aceito.

O §6 manda recusar ocorrência não distinguível, e o §9 diz que um endpoint contém variantes de altloc da mesma identidade, "nunca ocorrências distintas". O teste mapeado (`test_altloc_endpoint_missing_variant_rejects`) declara cobrir só a "metade alcançável"; o contraexemplo nativo mostra que a outra metade é alcançável. Correção esperada: recusar átomos repetidos (ocorrência, label_atom_id, altloc) e ocorrências indistinguíveis antes de formar conjuntos.

### MAJOR-7 — §16 / brief §5: falhas de RAW/parse fora da taxonomia 021

Pela produção nativa, só a categoria desconhecida sai como `MaterializationExecutionError`. Os demais casos levantam classes `ValueError`/`RuntimeError` próprias, sem `code`/`phase`:

| Caso | Classe levantada |
|---|---|
| RAW > 16 MiB | `CifStructuralLimitExceededError` (deveria ser LIMIT_EXCEEDED) |
| magic gzip | `CompressedRawContentError` |
| BOM | `InvalidCifEncodingError` |
| dois blocos | `MultipleDataBlocksError` |
| erro de sintaxe | `ReceptorParseFailureError` |
| atom_site → entity inexistente | `MaterializationAdapterError` com `code=INVALID_CIF`, mas sem ser `MaterializationExecutionError` |

O brief diz: "Falha de parsing → taxonomia 021, causa preservada". Além disso, o parser de `source_context` divergente do pin gera `ENGINE_UNAVAILABLE` em vez de um código de versão ou identidade. A correção é mecânica, mas é contratual: CP3/CP4 dependem da classe para fase, banner e saída.

### MINOR-1 — §11: tags de saída não estão em ordem alfabética

Categorias saem ordenadas, mas as tags seguem a ordem do catálogo/fonte. Na saída real: `_atom_site.group_pdb, id, type_symbol, …` e `_cell.length_a … entry_id`. O §11 e o brief §7 pedem ordem alfabética de categorias **e** tags. A saída é determinística (os bytes coincidem em reexecução).

### MINOR-2 — C-04 (evidência): snapshots documentais fictícios nas integrações

Todos os testes de integração (`_cp2_source_context`, `_real_fixture_materialize`, `test_receptor_parsing.py:618–621, 952–957`) usam `RecordSnapshot` com `sha256="1"*64…"4"*64` e `size_bytes=1`. O hash e o tamanho do RAW são reais. O brief §8 e C-04 pedem hashes e tamanhos reais "dos quatro documentos". O plan_key integrado incorpora esses valores fictícios.

### MINOR-3 — interrupções: nenhum teste CP2 de KeyboardInterrupt/SystemExit

O comportamento está correto: injetei as duas classes em 7 fronteiras reais (`gemmi.cif.read_string`, `build_materialization_plan`, `resolve_connection_decisions`, `compute_category_decisions`, `serialize_cif_document021`, `reparse_and_extract_cif_dom021`, `_verify_output_reparse`), e a mesma instância propagou nas 14 combinações. A suíte, porém, não contém essa prova separada por classe e fase, exigida pelo §20 e pelo brief §9.

### MINOR-4 — T021-164/166/168–172: prova do repositório sintética

O teste usa DTOs com contexto fixo (sem RAW), duas construções idênticas, sem ordens de visita diferentes nem goldens literais independentes. O §10.1 e o anexo pedem contexto RAW fixo, hashes verdadeiros e ordens de visita diferentes. Minha execução nativa supre a observação: RAW real, bases exatas, e `plan_key`/`connection_decisions_key` idênticos sob PYTHONHASHSEED 0/1/12345. Mas isso não substitui a prova no repositório.

### MINOR-5 — R-CP2-01 residual de borda: contexto inválido vira interseção zero

Em `_resolve_special_position_row_atoms` (l.3979–3987), `pdb_model_num='01'` (comparado como `str(atom.model)`) e um `label_alt_id` inexistente no resíduo resultam em contagens 1/0/0, sem aviso e sem recusa. Os demais casos estão corretos: retido 1/1/3, só removido 1/0/0 sem aviso, sobreposição 2/2/3, outro modelo, componente contraditório e asym desconhecido.

### MINOR-6 — §23 NCS: entrada real só no guard isolado

Nenhuma seleção do 1A2P pode atingir o guard NCS no pipeline completo, porque cada cadeia tem metalc não identidade (3_675/3_565/3_665) ao seu zinco. A limitação declarada é real. Os 2 operadores reais são `given` e foram exercitados apenas pela função de guarda. A regra NCS foi provada nativamente pelas minhas sondas sintéticas de pipeline completo, mas não há desfecho NCS de pipeline completo em entrada real.

### NOTES

- **NOTE-1:** whitespace exclusivamente em RAW depositado (§3); não reescrever.
- **NOTE-2:** os downloads RCSB atuais diferem dos inventários pinados (5i55 57 versus 54 categorias, 1pfe 73 versus 72, 3dg1 50 versus 35 do `3dg1_final`). Os originais intactos são recusados com UNSUPPORTED_CATEGORY por categorias posteriores ao catálogo, o que é legítimo. Verifiquei os derivados: removem exatamente as categorias declaradas, e todas as demais categorias são idênticas ao original token a token. Os 18 hashes conferem.
- **NOTE-3:** o 1PFE original com cadeia A recusa COVALENT_CUT antes da cobertura de catálogo, porque as conexões são resolvidas antes das categorias. Não há violação explícita, mas convém fixar a ordem do §16 no CP3.
- **NOTE-4:** `2_555` com operador 2 = `x,y,z` é tratado como não identidade. É conservador e coerente com a matriz; não é achado.

## 5. Disposição C-01–C-07 e R-CP2-01–04

| Item | Disposição | Evidência |
|---|---|---|
| C-01 | PARCIAL | Decimal exato/NCS/su-expoente fechados; MAJOR-2 aberto |
| C-02 | PARCIAL | Envelopes row_key/source_rows_key conforme SCHEMAS; visão crua × decodificada existe; MAJOR-3 aberto |
| C-03 / R-CP2-03 | FECHADO | 9 mutações que preservam forma (coordenada, troca e remoção de linha, `.`→`?`, `'.'` citado, categoria extra, bloco, token de struct_conn, chem_comp) → INVALID_OUTPUT, phase=verify; universo fechado de categoria/tag/`_entry`/bloco |
| C-04 | PARCIAL | Import tardio, pin, ENGINE_UNAVAILABLE/VERSION, hash/tamanho/16 MiB/compressão fechados; MAJOR-7 e MINOR-2 abertos |
| C-05 / R-CP2-01 / R-CP2-02 | PARCIAL | Anisotrop (seq, tipo, U parcial+B, id) fechado salvo citado; posições especiais fechadas salvo MINOR-5; MAJOR-4/5 abertos |
| C-06 | PARCIAL | `tbmp_` minúsculo em entry e bloco; literais multilinha/citados sobrevivem; MAJOR-1 aberto |
| C-07 | PARCIAL | 15 células e 7 pares corretos nativamente (próprio); MAJOR-3, MAJOR-6, MINOR-4 |
| R-CP2-04 | FECHADO | 41/41 identidades por bytes Git |

## 6. Os 79 cenários

A tabela integral está em `evidence/claude-cp2-review-scenario-reconciliation.csv`, com classificação, evidência e achado por ID. **COVERED 64, PARTIAL 15, GAP 0.** "COVERED" significa desfecho observado conforme o contrato por sonda própria nativa e/ou teste do repositório executado por mim. Mapeamento de nome de teste não foi aceito como prova.

| Grupo | Resultado independente |
|---|---|
| 041–044 | 042/043/044 COVERED (tokens literais, 52/52A, ptnr3 null real × citado); 041 PARTIAL (MAJOR-3) |
| 045–059 (matriz 15 células) | 15/15 COVERED por execução nativa própria (K=2/1/0 × 5 classes; K=1 covalente COVALENT_CUT) |
| 060, 141–144 | COVERED nativamente (precondições, convenção, contradição, outros operadores, 1PFE 1_555/9_555) |
| 061–090 catálogo | COVERED: 061, 063–066, 068–071, 075–081, 083, 086, 089, 090. PARTIAL: 062 (MAJOR-2), 067/082/085/087/088 (MAJOR-4), 072–074 (MAJOR-5), 084 (MAJOR-1) |
| 145–149, 162 | COVERED (147 com NOTE-2) |
| 150–155 | 150–153 e 155 COVERED (regra nativa; MINOR-6 para entrada real); 154 PARTIAL (MAJOR-2) |
| 156–158 | 156 COVERED; 157 PARTIAL (MAJOR-6); 158 PARTIAL (MINOR-5) |
| 164–172 | 7 pares alcançáveis COVERED por evidência própria determinística (MINOR-4 na prova do repositório); 165/167 COVERED (validador do DTO; inalcançáveis pelo resolver) |
| 173 | PARTIAL (MAJOR-3) |

## 7. Preservação do CP1 e regressões

- As 92 funções de teste CP1 são idênticas por AST, os 13 goldens e helpers estão inalterados (só a lista de import cresceu), e o vetor R-1 está preservado. As 31 funções preexistentes de `test_receptor_parsing.py` são idênticas à baseline.
- Mesma execução do ambiente em 3 SHAs: 1.480 testes comuns CP1→HEAD e 1.388 baseline→HEAD com **0 mudanças de desfecho e 0 remoções**; os 91 testes novos passam.
- ARCH-01 (domínio sem import nativo) foi verificado por sonda própria, normal e `-O`. As demais disposições CP1 (ARCH-02/03, MAJOR-A/B, MINOR-1–7, R-1) não mostram regressão concreta; não foram reabertas.
- NOTE-1: não há persistência de plano parcial (sem storage). NOTE-2: DTOs novos `frozen/extra=forbid/strict`, sem `pytest.raises(Exception)` em código novo. NOTE-3: CLI/020 inalterados.

## 8. Execução própria × evidência fornecida

| Medida | Própria (Linux, Gemmi nativo do pin) | Fornecida (Windows 11, Python 3.14.7) |
|---|---|---|
| Foco parser+materialização | **214 passed** (e 214 sob `-O`) | 214 |
| Regressão 020 | **121 passed** | 121 |
| Coleta total | 1.569 itens; 95 itens ocultos por 2 módulos importorskip rdkit (33+62 funções por AST) | 1.664 |
| Suíte completa | 1.497 passed, 67 failed, 5+2 skipped; as 67 falhas (65 `test_atomic` no-follow/`cmd` exclusivos do Windows, 2 `test_cli` RDKit) são idênticas na baseline e no CP1 | 1.659 passed, 5 skipped |
| Skips | 5 por item, todos "requires RDKit" (test_application:1881, test_cli:4261/4329/4603/6698) + 2 de módulo | 5 |

A contagem fornecida 1.664 = 1.569 + 95 é aritmeticamente coerente. A minha suíte completa **não** substitui a do Windows, e não apresento 1.659/5 como execução minha.

## 9. Saídas publicadas

Os arquivos estão em `increments/021/40-checkpoint2-review/` na branch própria `claude/021-cp2-adversarial-review-20261125`, criada a partir de c9e02f0. Linhas, bytes e SHA-256 de cada saída constam de `evidence/claude-cp2-review-output-identities.json` (exceto desse próprio arquivo) e da mensagem final da sessão. Os scripts de sonda estão publicados para reprodução e não alteram nenhum repositório. Não há segredos nem caminhos nativos do responsável.

## 10. Veredito

**REQUEST CHANGES.** São 0 BLOCKERS, 7 MAJORS, 6 MINORS e 4 NOTES. A matriz de simetria, a verificação de saída, o pin/import tardio, a linhagem das fixtures e a preservação do CP1 estão sólidos e foram provados independentemente. Os sete MAJORS são violações concretas do contrato congelado com contraexemplo de produção nativo, todas corrigíveis dentro da allowlist CP2 sem mudar o contrato.

O CP2 não está pronto para a decisão do responsável. Próximo gate: o arquiteto reconcilia os achados e despacha as correções; depois cabe uma revisão focal.

INCREMENT021CHECKPOINT2ADVERSARIALREVIEWCOMPLETE: YES
HEADREVIEWED: a807b03f44089eb3cbacc14f871b63689a21aec9
SPECIFICATIONSHAVERIFIED: YES
CUMULATIVEALLOWLISTVERIFIED: YES
SCENARIOS79RECONCILED: YES (COVERED 64 / PARTIAL 15 / GAP 0)
INDEPENDENTNATIVEEXECUTION: YES (Gemmi 0.7.5 compilado do pin, Linux; não Windows)
BLOCKERS: 0
MAJORS: 7
MINORS: 6
NOTES: 4
VERDICT: REQUEST CHANGES
READYFOROWNERCP2DECISION: NO
CHECKPOINT2APPROVED: NO
CP3IMPLEMENTATIONAUTHORIZED: NO
MAINMODIFIED: NO
CODEREPOSITORYMODIFIED: NO
