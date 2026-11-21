# Estudo arquitetural — Incremento 021
## Materialização da Seleção de Receptor

Data: 21/11/2026, America/Sao_Paulo. Autor: Codex, arquiteto. Versão: estudo v1, para confronto independente por Claude revisor separado do implementador.

Este documento contém fatos verificados, inferências explicitadas e recomendações provisórias. Não é especificação, não congela schemas, não autoriza implementação e não representa aprovação independente. A recomendação de escopo pode ser alterada pela revisão e pela decisão de Emanuel Henrique da Silva.

## 1. Snapshot, autoridade e método

| Material | Identidade conferida |
|---|---|
| Código, `sysoutemanuelhenrique/molecular-platform`, main remota | `08b797e0985e123ffd4d7ca7e5a5e8f040e63851` |
| Governance, branch `docs/020-a-candidate1-review-20261020`, snapshot de entrada | `6a85b79a33bce419c0ebd2bde6793732ef4f0388` |
| Main do governance, somente preservação | `a47183dfec8213c765ed43ae482c8c227760a3d5` |
| Especificação final do 020 | 1.975 linhas; 210.880 bytes; SHA-256 `cf6cb534f9267d51e718052c7b36a2293c522bc566c99cf3bb2ef5909385a0a6` |
| Gemmi empregado na baseline | Pin `gemmi==0.7.5`, extra `structure`, em `pyproject.toml` |
| Fonte primária Gemmi analisada | Tag `v0.7.5`, objeto tag `f73148f53f779fa9d9e78b014667928243b5c2a8`, commit `5cc1c23c6007e0e6cbd69289c6f7c0bff50e943e` |

Os HEADs remotos de entrada coincidiram com os exigidos antes do estudo. A especificação foi recuperada do pacote histórico `MolecularGovernance.zip`, apenas pelo caminho `MolecularGovernance/increments/020/13-final-specification/INCREMENT_020_FINAL_SPECIFICATION.md`; foi conferida pelos três gates e lida integralmente, linhas 1–1975. Uma cópia byte-idêntica acompanha este estudo em `references/INCREMENT_020_FINAL_SPECIFICATION.md`, para o revisor não depender de um ZIP ou de um disco Windows. Nenhum outro conteúdo do ZIP é publicado.

Foi consultada a árvore atual do GitHub e conferido o Git blob de cada um dos 66 arquivos rastreados contra uma cópia local externa de leitura. Os arquivos-fonte usados são da baseline main; não são arquivos do worktree 020-A. As evidências contêm hashes, caminhos relativos e referências públicas. Não contêm checkout, ambientes virtuais, arquivos pessoais ou credenciais.

As instruções `AGENTS.md`, `protocol/AGENT_WORKFLOW.md`, `CLAUDE.md` e `STATUS.md` foram lidas no snapshot de entrada. `README.md`/`CLAUDE.md` ainda têm apontamentos de bootstrap; sua existência não torna uma tarefa histórica vigente. Nesta publicação, o STATUS e a nova tarefa identificam o estudo do 021 e o stand-by do 020-A, por instrução direta do responsável. Não se altera nenhum documento histórico do 020-A nem se encerra seu parecer por inferência.

Legenda: **F** = fato observado em documento/código/fonte primária; **I** = inferência arquitetural; **R** = recomendação a revisar; **Q** = decisão necessária antes de uma especificação final. Links Cxx/Gxx/Wxx estão na seção 20. Recomendações deste estudo não são capacidades já existentes.

## 2. Resultado e delimitação inicial

**R — recomendar a opção B: materialização controlada no referencial do modelo de origem, mmCIF→mmCIF, sem expansão de assembly nesta primeira entrega.** Ela aplica seleções confirmadas e decisões adicionais explicitamente declaradas, produzindo arquivo novo e registro verificável. O produto deve ser apresentado como estrutura selecionada, sem alegar preparo químico ou prontidão para docking.

O 020 §34.2 lista possibilidades do 021, incluindo expansão de assembly; não congela uma especificação do 021 nem exige que todas as possibilidades sejam implementadas juntas. A redução proposta é uma decisão de escopo a submeter ao revisor e ao responsável, não uma descrição retroativa do 020. Se o responsável exigir assemblies nesta entrega, a opção C deve ser escolhida explicitamente e estudada até fechar mapeamento de cópias e conectividade; B não poderá ser anunciada como cobertura integral de assemblies.

**F — nada do 021 está implementado nesta baseline.** O alinhamento local à main foi informado pelo implementador; não é um teste de materialização. Este estudo não executou pytest, Gemmi ou uma demonstração científica. Sua prontidão é para revisão do estudo, não para implementação.

## 3. O que o Incremento 020 efetivamente entrega

**F — o Incremento 020 foi concluído e integrado no escopo aprovado.** O PR #7 está fechado e merged, com HEAD `1e68a1ef9482b5f480b06d286bc4512ef3a438cc`, merge `d25974d90540c955dd8b95440d8b218689cf74a3`, integrado à main examinada. A consulta atual ao GitHub confirmou esse estado; ela não é reexecução da suíte histórica. O 020-A é outra entrega, de caracterização molecular, e continua em stand-by sem integração. A ausência de materialização no 020 é seu limite contratual explícito, não um checkpoint esquecido.

| Capacidade observada | Implementação e testes consultados | Consequência para o 021 |
|---|---|---|
| Registro de `ProteinInput` e arquivo RAW, com aquisição/checksum | C01; `tests/test_registry.py` | RAW é evidência original; artefato derivado deve ter armazenamento separado |
| Parsing de mmCIF/PDB e rejeições de extensão/compressão/tamanho/checksum | C02; `tests/test_receptor_parsing.py` | Reutilizar regras e taxonomia compatíveis; não prometer segurança adicional sem implementação e teste |
| Inventário e relatório persistido por `inspection_id` | C03/C06; testes de inspeção/registry | Identidade de parser/profile participa do id; não substituir por inspeção atual |
| Política declarada com modelo, assembly, cadeias e disposições | C04; testes de seleção | É intenção imutável; não contém política de altloc nem arquivo de saída |
| Resolução lógica ligada a uma inspeção fixa | C05/C07; testes de resolução/serviço | Confirma identificadores, mas não constrói coordenadas nem resolve membership de assembly |
| Sete funções de serviço e comandos de consulta/seleção | C07/C08; testes de serviço/CLI | Preservar os comandos e seus banners; adicionar operação nova separadamente |

**F — detalhes importantes do código real, relevantes à proposta:**

1. `ParsedAtom` contém nome, altloc, ocupância, elemento e serial; não contém x/y/z. `ParsedReceptorDocument` e `ReceptorInspectionReport` não são fontes de coordenadas. `_parse_mmcif_document` preserva expressões de assembly e listas de asym ids, mas não persiste as matrizes de `_pdbx_struct_oper_list`. A inspeção não basta para reconstruir um assembly ou um arquivo atômico. [C02/C03]
2. `_resolve_assembly` confirma apenas a existência do id. `_resolve_chains` verifica cadeias no modelo resolvido; a associação cadeia↔assembly não é conferida. Seleção vazia de cadeias é legal no 020 e produz tupla vazia; não significa automaticamente todas as cadeias. [C07; N020 §25.5]
3. `_resolve_component_dispositions` aplica os baldes água/metal antes das entradas nomeadas; usa `seen` por `(label_asym_id, ccd_code)`. Uma entrada nomeada sob uma chave já tratada não a substitui. O resultado confirmado é a autoridade do 021; reaplicar a intenção original com outra precedência mudaria uma decisão já persistida. [C07]
4. Componentes de inspeção podem representar diversas ocorrências com a mesma chave `(label_asym_id, ccd_code)`, sem identidade por resíduo em `ResolvedComponentDisposition`. Água compartilha frequentemente um asym id; materialização por molécula individual não está especificada pelo 020. [C03/C05]
5. `_group_atom_site_into_residues` agrupa por contexto de modelo/identificadores de autor, registra `comp_id` da primeira linha e aplica `... or Decimal("1")` à ocupância. Isso não é representação lossless dos tokens atômicos do RAW: por exemplo, zero é falso nessa expressão. Para o 021, ocupância e coordenadas devem vir dos tokens do RAW verificado, não ser reconstruídas pelo inventário. Este estudo não corrige nem reabre o 020; delimita a autoridade dos dados usados pela nova operação. [C02]
6. `selection_capability="full"` atesta identidade suficiente no relatório; os tetos podem introduzir `parser-limitation`. Essa capacidade não é certificado de inventário completo nem de geometria cientificamente válida. [C03; N020 §32]

## 4. Contratos preservados e fronteiras científicas

**R — preservar integralmente os modelos 1.0 do 020:** nenhuma edição de políticas/resoluções já persistidas, nenhum campo novo obrigatório retroativo, nenhum `inspection_snapshot`, nenhuma migração silenciosa de profile/parser, nenhum fallback de label id para auth id. Identificadores científicos continuam sensíveis à caixa; comparação casefold permanece exclusivamente de armazenamento.

A cadeia nova deve estender, por referência, a cadeia existente:

`ProteinInput → ReceptorInspectionReport → ReceptorSelectionPolicy → ResolvedReceptorSelection → decisão de materialização → artefato estrutural derivado`.

O 021 não deverá registrar automaticamente ScientificEntity, MolecularState ou Conformer. Uma extração de átomos de um modelo estrutural, com eventuais cortes, não demonstra identidade química completa, protonação, conformação validada ou potencial mínimo. `StateTransformationRecord.operation` permanece `protonation|tautomerization`; `ExecutionAttempt` permanece específico do tautomerismo. [C09/C10/C11]

**R — vocabulário próprio e pequeno para materialização**, sem generalizar esses dois modelos existentes. O nome histórico `PreparedReceptorArtifact` do roadmap não deve resultar em CLI que diga quimicamente preparado. Nome provisório preferido: `ReceptorMaterializationArtifact`, com estágio estrutural explícito. Nome, shape e versão serão decididos no rascunho; não são schemas congelados por este estudo.

Mantêm-se fora de escopo hidrogênios, protonação, pKa, cargas, reparo de átomos/resíduos/loops, capping de valências, minimização, conversão para PDBQT, docking, GUI, banco de dados, scheduler e nuvem. Hidrogênios/deutérios já presentes são retidos se seus átomos forem selecionados; não são removidos por conveniência.

## 5. Consumo dos registros e validação do vínculo

**R — sequência de resolução anterior a qualquer publicação:**

1. Validar ids e parâmetros, resolver o experimento e carregar a resolução pelo `selection_id` fornecido. Não chamar `resolve_receptor_selection` novamente como fallback.
2. Carregar a política por `policy_selection_id`, a inspeção pelo exato `inspection_id` da resolução e o ProteinInput pelo `protein_input_id`. Usar as APIs públicas de leitura de C01/C06/C07; distinguir ausência, YAML inválido, incompatibilidade e falha de armazenamento.
3. Cruzar ids, protein_input_id, raw_checksum, formato e proveniência de parser entre os registros; política e resolução devem referenciar a mesma inspeção. Validar o próprio `inspection_id` com o payload do profile suportado. Modelo/entidade/cadeia devem existir na inspeção fixada; payload válido por Pydantic isoladamente não prova essas relações.
4. Medir hashes dos bytes de metadados carregados para proveniência da execução. Resolver cada registro em uma leitura controlada; não montar o contexto a partir de leituras sucessivas que possam misturar versões. Nenhuma procura por latest, listagem/diff de attempts ou reconstrução por timestamp.
5. Exigir mmCIF, capacidade full, schema/profile reconhecidos e parser efetivo Gemmi 0.7.5 compatível com o referenciado. Versão distinta deve produzir erro específico no 021, sem modificar a inspeção antiga. Isso não ressuscita `ReceptorResolutionParserVersionConflictError` no 020: trata-se de um consumidor novo que precisa reinterpretar coordenadas com perfil conhecido.
6. Revalidar os bytes atuais do RAW contra o checksum de aquisição e contra os registros fixados. A leitura usada para planejar/materializar deve ser exatamente a que teve o hash verificado, por snapshot privado/bytes controlados; não verificar um caminho e depois passar outro conteúdo mutável ao parser.
7. Exigir inventário suficiente para o domínio selecionado. `parser-limitation` torna o perfil B inadmissível até que a completude seja demonstrada; no v1 recomenda-se recusa conservadora. Ausência de categorias opcionais vira evidência de indisponibilidade, não ausência química. Categorias essenciais ao plano não podem ser inventadas.

O serviço não deve executar `inspect_receptor` como reparo, atualizar uma política ou tratar inspeção ausente/corrompida como autorização para uma nova. Nova seleção exige ação explícita pelo fluxo já existente.

## 6. Opções de escopo e recomendação

| Dimensão | A — extração mínima do modelo | B — materialização controlada, recomendada | C — materialização geral com assemblies |
|---|---|---|---|
| Núcleo | Modelo/cadeias; componentes/altlocs preservados | Modelo/cadeias + disposições efetivas + complemento explícito + altloc + auditoria | B + expansão de operadores, identidade de cópias, remapeamento completo |
| Entrada/saída sugerida | mmCIF/mmCIF | mmCIF/mmCIF | mmCIF/mmCIF; PDB seria decisão adicional |
| Assembly não nulo | Recusa | Recusa explícita; nunca ignora seleção | Exige membership, operadores e mapeamento verificados |
| Implementabilidade | Menor esforço; atende pouco da seleção de componentes | Esforço médio; decisões novas limitadas e testáveis | Esforço alto; gramática, cópias, conectividade/simetria e expansão potencialmente grandes |
| Coerência com 020 | Boa, com limites anunciados | Boa, sem mudar schemas 1.0 | Boa somente se não perder as identidades e conexões que o 020 preservou |
| Atomicidade/idempotência | Bundle e identidade explícitos ainda necessários | Bundle e reserva exclusiva propostos na seção 13 | Mesmo protocolo com artefatos maiores e proveniência de operações |
| Rollback/concorrência | Mesmo cuidado de propriedade do bundle | Serialização por chave e compensação privada | Mesmo problema com maior custo de expansão/staging |
| Migração | Nenhuma do 020 | Novos registros separados; nenhuma do 020 | Novos registros e plano de cópias mais extensos; não alterar o RAW |
| Compatibilidade com 017 | Sem tocar tautomerismo | Sem tocar tautomerismo | Possível, mas superfície de regressão maior |
| Risco científico | Baixo se não alegar decisões não aplicadas | Controlável; cortes e ambiguidades são declarados | Maior: expansão pode perder conexões ou alterar identidade de cópias |
| Capacidade de teste | Boa, mas alcance reduzido | Boa com fixtures reais de categorias e publicação | Exige produtos de operadores, colisões, conectividade entre cópias e limites de expansão |
| Tamanho real | Pequeno a médio | Médio; não é uma simples função de exportação | Grande; inadequado tratar como ajuste de um comando |

**R — B oferece avanço observável sem vender fidelidade geral que o writer/expansor não garante.** A é aceitável se o responsável quiser um incremento menor, porém não aplica plenamente as disposições já resolvidas. C é legítima, mas requer estudo/fixtures específicos antes de especificação final. Nenhuma opção inclui química; acrescentá-la descaracterizaria o objetivo.

**Q-01 — o revisor deve confrontar explicitamente se a recusa de assemblies em B é aceitável para a entrega chamada 021.** Não esconder esse limite em rodapé. Caso B seja rejeitada por cobertura insuficiente, estudar C; não alterar B silenciosamente na implementação.

## 7. Regras propostas de seleção física

### 7.1 Modelo, assembly e cadeias

**R:** selecionar exatamente `resolved_model`, nunca modelo 1 por conveniência nem primeiro item do arquivo. Em B, `resolved_assembly` deve ser `None`; um id não nulo gera recusa tipada antes da escrita. A política nova declara explicitamente o contexto `source-model-frame`: nenhuma operação de assembly, NCS ou simetria é aplicada. A presença de assemblies no RAW, por si só, não impede materializar no referencial original se a seleção confirmada não escolheu nenhum.

`resolved_chains=()` deve ser recusado em B. O 020 continua aceitando essa declaração; o 021 apenas informa que ela não define um recorte materializável deste perfil. Não convertê-la em todas as cadeias ou em saída vazia. Uma nova política 020 poderá declarar as cadeias pretendidas.

O plano físico usa `label_asym_id` e o modelo como autoridade, com `label_entity_id` para verificação. Não selecionar por `auth_asym_id` isolado nem pelo nome de cadeia do objeto Structure. Preservar label/auth tokens e a associação de entidade; nenhuma renumeração ou normalização de caixa. Se NFC usado pelo 020 fizer dois tokens RAW distintos colidirem, bloquear a correspondência ambígua; não fundir átomos.

Cadeias poliméricas não selecionadas saem por consequência da lista explícita. Componentes não-poliméricos no modelo são tratados pela política de componentes, não apagados simplesmente porque têm outro asym id. Se o usuário selecionou explicitamente uma cadeia que também recebe disposição remove, registrar conflito; não escolher uma precedência nova.

### 7.2 Componentes, água, metal e disposições ausentes

**R:** construir o universo de ocorrências a partir das linhas atômicas do modelo fonte, vinculado ao inventário completo da inspeção fixada. Aplicar cada `ResolvedComponentDisposition` como decisão efetiva. A chave `(label_asym_id, ccd_code)` aplica-se a todas as ocorrências desse componente no contexto suportado; nunca prometer seleção de uma molécula de água individual se a identidade fornecida não a distingue.

Não reavaliar a tabela de metais do 020 sob novas regras, não transformar unknown em ligante/cofator e não reaplicar `ComponentDisposition.role` como classificador. Conflito entre intenção original e resolução efetiva deve ser exibido para nova declaração, sem override pelo 021.

Para ocorrências sem disposição confirmada, exigir uma decisão complementar explícita: preservar todas as ocorrências não abordadas, ou recusar até completar a seleção. O perfil não terá um default silencioso de remoção nem fabricará um papel biológico para permitir keep/remove. A opção de preservação é uma escolha registrada do cientista; não uma inferência do software. B não permite que esse complemento reverta um keep/remove já confirmado no 020.

Resíduo polimérico modificado continua parte da cadeia. Remoção por chave de componente que cortaria o interior do polímero deve ser recusada em B; não usar uma classificação de inventário como autorização para criar uma lacuna no backbone. A cadeia inteira pode ser excluída por seleção de cadeias. Glicanos/componentes branched exigem classificação e referências suficientes; quando isso não for demonstrável, bloquear ou preservar por decisão explícita, sem removê-los por serem HETATM.

### 7.3 Altlocs, micro-heterogeneidade e ocupância

**R:** dois modos explícitos para B: preservar todas as alternativas; ou selecionar labels por grupo de resíduo identificado sem ambiguidade. Preservar alternativas não significa produzir um conformer único e deve ser anunciado assim. Selecionar labels exige declaração para cada grupo afetado, retenção dos átomos comuns e comprovação de que nenhuma mistura incompatível foi criada. Não assumir que label A de dois resíduos descreve um estado global correlacionado.

Não escolher maior ocupância, primeiro átomo ou A automaticamente. Se há micro-heterogeneidade de comp_id no mesmo sítio ou grupos que o modelo proposto não distingue, B deve recusar a seleção parcial em vez de colapsar as variantes. O modo preservar pode manter os tokens se a saída e suas referências permanecem válidas.

Ocupância e B-factor são preservados da fonte, inclusive zero e tokens de ausência. Não renormalizar ocupâncias a 1 após escolher uma alternativa; não preencher valores desconhecidos porque o dicionário possui default. Uma representação selecionada continua com os valores observados da fonte e com aviso explícito sobre sua interpretação. Coordenadas devem ser finitas e presentes no perfil materializável; dado inválido é recusa, não reparo.

## 8. Conectividade, cortes e metadados

**R — tratar `_struct_conn` como referências declaradas, não como grafo químico completo.** O 020 particiona qualquer conn_type não vazio diferente de disulf/metalc no balde covalent; o 021 não deve concluir que todos esses tipos têm a mesma semântica química. Preservar o conn_type literal e a fonte.

| Situação de uma conexão | Tratamento proposto em B |
|---|---|
| Dois endpoints inequivocamente retidos, no contexto original | Preservar linha e todos os campos declarados, inclusive altloc, symmetry, distância/ordem/role/details |
| Dois endpoints removidos pela seleção | Omitir linha na saída e registrar sua remoção no relatório do plano |
| Exatamente um endpoint removido | Recusar, salvo reconhecimento explícito daquela conexão como corte autorizado da seleção; nunca capear, reparar ou declarar valência corrigida |
| Referência ambígua, endpoint ausente ou incompatível com altloc selecionado | Recusar no perfil; não apagar silenciosamente |
| Simetria não-identidade cujo parceiro não está materializado | Recusar B; sem expansão cristalográfica nem alegação de conectividade interna completa |
| Categoria ausente na fonte | Registrar indisponibilidade; não gerar ligação nem certificar ausência química |

O reconhecimento de corte, se aceito pelo revisor, deve nomear a conexão por id fonte inequívoco ou por chave estável de linha+hash da fonte quando id não existir; precisa de justificativa atribuída ao cientista. Se essa superfície for considerada excessiva, alternativa menor é bloquear todo corte em B. **Q-02:** escolher uma dessas duas políticas antes do rascunho final. A recomendação provisória é permitir reconhecimento explícito por conexão, com falha quando a identidade da conexão não for inequívoca.

A materialização deve construir um bloco derivado por política de categorias, não copiar o bloco inteiro e apagar apenas `_atom_site`. Isso evitará referências antigas a átomos/cadeias removidos e metadados que façam o derivado parecer um novo depósito experimental.

| Categorias | Regra de estudo para B |
|---|---|
| `_atom_site` | Reter linhas escolhidas e todas as colunas suportadas; preservar ids, valores e tokens fonte; rejeitar ids duplicados/ausentes que impeçam proveniência inequívoca |
| `_atom_site_anisotrop` | Reter somente registros associados a átomos sobreviventes, com cross-check de id/contexto; não converter nem recalcular tensores |
| `_struct_asym`, `_entity`, `_entity_poly`, `_entity_poly_seq`, `_pdbx_poly_seq_scheme`, `_chem_comp` | Preservar relações pertinentes às identidades sobreviventes; sequência declarada pode incluir resíduos não observados e não deve ser confundida com átomos presentes |
| `_struct_conn` | Regras por endpoint acima; pós-validação referencial obrigatória |
| `_pdbx_unobs_or_zero_occ_*` | Só reter sob filtro de modelo/cadeia bem definido; manter ausência/limitação quando o contexto não puder ser determinado |
| `_cell`, `_symmetry`/`_space_group` | Preservação apenas como referencial original; nunca apresentar nova simetria inferida ou usar P1 como placeholder inventado |
| `_entry`/título do derivado | Identificação local do derivado; accession original fica na proveniência, sem alegar novo experimento/deposição |
| Categorias de assembly/NCS e demais categorias experimentais/anotações | Não copiar instruções acionáveis ou referências stale para o recorte; listar categorias omitidas e motivos, mantendo o RAW integral como evidência |

Esta tabela é desenho de perfil, não uma promessa de preservar todas as categorias mmCIF. **Q-03:** fechar no rascunho o catálogo exato de categorias/colunas, chaves e checks de integridade. Na implementação, uma categoria desconhecida referencialmente relevante exige recusa do perfil ou tratamento aprovado; não autoriza introduzir um filtro ad hoc silencioso. A auditoria de perdas e o RAW preservado não substituem a obrigação de preservar as categorias declaradas como suportadas.

## 9. Formatos: por que mmCIF como saída inicial

**F:** o 020 já restringe seleção confirmada à identidade nativa full; PDB legado permanece inspection-only. Logo um caminho 021 que parte exclusivamente de seleção confirmada não precisa promover PDB legado artificialmente. [N020 §12/20; C02/C04/C07]

**R:** aceitar mmCIF detectado por conteúdo e produzir mmCIF UTF-8, arquivo novo com nome fixo dentro de bundle controlado. Não usar nome externo de arquivo como caminho de saída, não aceitar URL e não descomprimir. Preservar tokens científicos e valores numéricos dos átomos retidos, embora whitespace/comentários/ordem da serialização não precisem reproduzir o RAW byte a byte. O hash do artefato é dos bytes efetivamente produzidos; identidade científica e checksum de arquivo continuam distintos.

PDB legado como saída foi considerado e não recomendado em B: acrescentaria mapeamentos de cadeia/serial/CCD, limitações de campos e política de perdas, além dos formatos já existentes. O formato PDBQT permanece excluído. A representação central deve continuar independente do motor futuro de docking. [W01/W02]

## 10. Gemmi 0.7.5 — capacidade confirmada e limites

Verificação por código-fonte oficial pinado, não somente por uma documentação que possa ter mudado:

| Capacidade | Evidência primária | Consequência |
|---|---|---|
| `gemmi.cif.read_string` tem overload Python para bytes e str | G01, linhas 25–32 | É viável parsear bytes já verificados sem reabrir o RAW pelo parser. Confirmação posterior ao 020, não alteração retroativa de seu fluxo |
| Document/Block, `sole_block`, `init_loop`, `Loop.add_row`, `as_string` | G02 | É viável construir saída no DOM CIF de baixo nível, sem reconstruir coordenadas pela inspeção |
| `make_mmcif_document`/`make_mmcif_block`/`update_mmcif_block` e grupos de saída | G03/G06 | Existem; não equivalem a preservação automática de todas as categorias fonte |
| `make_assembly`, `transform_to_assembly`, `HowToNameCopiedChain` | G04/G05 | Existem e são expostos ao Python; não são por si um contrato de lineage/fidelidade TBMP |
| Expansão altera nomes de chain/subchain e posições/ADP | G05, implementação `make_assembly_` | Exige mapeamento de cópias, operadores e identidades derivadas para C |
| Expansão tem caminho que perde conexões com simetria diferente da identidade; limpa assemblies e pode mudar cell/spacegroup | G05, `finalize_expansion`/`transform_to_assembly` | Não recomendar wrapper de uma linha nem anunciar preservação geral |
| `transform_to_assembly` expõe `merge_dist=0.2` como default Python | G04 | Não aceitar fusão geométrica por default como decisão científica da plataforma |
| Rotinas `remove_waters`, `remove_alternative_conformations` e `setup_entities` | G04; documentação oficial | Não usar em B para impor política ou fabricar identidade |

Foram conferidos 12 blobs da tag contra a árvore Git oficial, registrados em `evidence/gemmi-source-identities.json`. A licença raiz dessa versão contém MPL-2.0; o estudo não fornece parecer jurídico de distribuição nem altera licenças do projeto. Nenhuma dependência nova é proposta.

**Limite de evidência:** Gemmi e pytest não estão instalados neste ambiente Python 3.12.14. Nenhum wheel foi instalado, nenhum teste científico ou spike Gemmi foi executado. As superfícies acima foram verificadas no binding Python e na implementação C++ da versão exata. É suficiente para confrontar o estudo; não comprova resultado científico, determinismo do writer em Windows ou segurança de publicação. Esses serão gates de implementação.

## 11. Arquitetura proposta, sem schemas congelados

**R — responsabilidades mínimas:**

- Domínio novo: intenção de materialização, plano de átomos/conexões/categorias e descrição do artefato. DTOs imutáveis/fechados, tipos efetivamente verificados e invariantes explícitas; não assumir que `frozen=True` elimina coerção. Essa recomendação não depende de ler ou integrar o 020-A.
- Fronteira Gemmi: manter imports e objetos Gemmi restritos a `receptor_parsing.py`, por entrada aditiva para bytes controlados/geração de derivado. Não mudar `parse_receptor_raw` nem fazer seus caminhos de inspeção chamar a nova rotina de transformação. O novo caminho pode construir um DOM novo; os métodos de conveniência proibidos no 020 continuam proibidos em seus caminhos. Forma exata de função será decidida na especificação.
- Registry/storage novo: persistir bundle e decisões novas, sem ampliar diretórios/responsabilidades do registry 020. Não alterar o layout dos registros 1.0 antigos.
- Serviço novo: carregar referências, verificar vínculos, capturar bytes, resolver plano, publicar e retornar resultado tipado; proprietário único dos eventos operacionais. CLI apresenta, nunca faz seleção científica nem compensa.
- CLI aditiva, sem interação obrigatória: intenção de comando semelhante a `molecular receptor materialize`, além de consulta do artefato. Nome/opções ainda propostos; devem mapear 1:1 ao serviço e exigir as decisões faltantes.

Uma declaração nova de materialização é necessária porque o 020 não expressa altloc, contexto físico e política para componentes não abordados. Recomenda-se persistir a declaração como registro imutável próprio para permitir revisão por id, depois produzir um ou mais artefatos referenciando-a. Alterar a intenção cria novo id de política, sem sobrescrever a anterior; mecanismo genérico supersedes não é necessário nesta fase. **Q-04:** decidir se um comando declara+executa ou se a CLI expõe dois comandos, preservando a mesma separação de domínio.

Para o artefato, considerar: referências às quatro fontes; decisão materializada; contexto/modelo; parser e perfil observados; versão da aplicação; checksum e tamanho da saída; contagens antes/depois; mapeamento de átomos/linhas fonte, conexões removidas e categorias omitidas; autoria declarada e timestamp. O mapeamento completo pode ser arquivo de auditoria com hash no manifesto, sem tornar o YAML principal proporcional a milhões de átomos.

## 12. Identidade, proveniência e idempotência

**R:** distinguir id autoral da política, chave determinística da requisição e checksum do artefato. Payload da chave inclui os ids e hashes dos registros lidos, checksum do RAW, decisões efetivas completas, versão do perfil/materializador e versão observada do Gemmi. Excluir timestamps e textos de apresentação do algoritmo de equivalência, salvo justificativa explícita. JSON canônico/hash podem reaproveitar mecanismo existente por disciplina; payload e vocabulário são próprios.

Pinagem dos hashes de metadados é deliberadamente identidade do snapshot documental, não deduplicação universal de semântica química: uma edição externa de YAML com mesmos valores pode mudar o hash. A especificação deve dizer se isso é novo snapshot ou violação de create-once; recomendação: recusar alteração de registro já referenciado em um retry, sem redefinir silenciosamente a equivalência. **Q-05:** fixar a regra de comparação e o versionamento antes da implementação.

Retry idêntico só retorna reused depois de validar integridade de manifesto, artefato e auditoria e a consistência do contexto fixado. Arquivo ausente, tamanho/hash divergente ou manifesto inválido gera erro de integridade, nunca reconstrução ou sobrescrita automática. Uma requisição distinta gera nova chave/artefato; alteração de formato/profile/engine não reutiliza resultado antigo por coincidência de nome.

Nada procura um artefato por timestamp ou usa semelhança de nomes. O RAW nunca é a saída. A materialização não recalcula identity/role/classification de inspeção nem substitui a política confirmada. Lineage deve continuar recuperável mesmo quando a saída tem menos átomos e um novo checksum.

## 13. Publicação, concorrência, falhas e compensação

**F:** `atomic_write_text` grava temporário e usa `os.replace`; sozinho não é create-once. `check_storage_identity_conflict` é uma verificação com janela TOCTOU, não mutex. `publish_staged_directory` usa precheck seguido de `os.rename`; seus próprios comentários declaram diferenças de plataforma e ausência de serialização geral. Nenhum desses três, isoladamente, prova publicação multi-arquivo segura sob escritores concorrentes. [C12]

**F:** `create_verified_raw_snapshot` é restrito a `inputs/ligands/<input_id>/` e à plataforma Windows/NTFS validada. Não basta chamá-lo com ProteinInput. `LigandPromotionAttempt` e suas compensações também têm semântica de ligante/entidade/estado que não deve ser copiada por nome. [C12/C13]

**R — recomendação para detalhar no rascunho:** bundle autocontido de saída, preparado em staging privado no mesmo volume, com manifesto+estrutura+auditoria verificados antes da publicação. Uma chave lowercase hex evita aliases de casefold na identidade técnica. Não usar id autoral de seleção ou nome de arquivo externo como nome arbitrário de diretório.

Uma reserva exclusiva por chave (criação de arquivo com exclusividade real) deve preceder a publicação para serializar requisições iguais; os demais writers recebem busy/conflict ou reused verificado após a publicação. Não usar check-then-write como lock, não expirar nem roubar reserva de outro processo automaticamente. Reservas órfãs após crash ficam diagnosticáveis, sem limpeza destrutiva automática. Chaves diferentes não devem compartilhar staging.

Primeiro perfil de publicação proposto: Windows 11, volume NTFS local, processo(s) cooperantes com o protocolo; publicação por rename de bundle sob reserva, com recusa real de destino existente. Testes devem exercitar a semântica efetiva do Windows, não inferi-la de POSIX. Para outras plataformas, testes puros podem rodar, mas o serviço de publicação falha fechado até validação própria. Uma reserva não protege contra um usuário externo malicioso que substitui diretórios; essa ameaça não deve ser descrita como resolvida por ela.

Um layout conceitual possível, ainda sem compromisso de schema, é `scientific/receptor_materialization_policies/` para decisões, `scientific/receptor_materializations/.staging/<attempt-uuid>/` e `scientific/receptor_materializations/<request-key>/` para bundles publicados. O manifesto fica dentro do bundle: evita anunciar sucesso por um YAML separado antes de o arquivo existir. A política já declarada é independente e nunca é apagada porque uma execução falhou.

| Momento da falha | Comportamento proposto |
|---|---|
| Antes de criar recursos privados | Erro tipado; nenhuma publicação; preservar todas as fontes |
| Durante leitura/planejamento/serialização/validação | Limpar só recursos cuja criação e identidade pertencem à tentativa; manter a declaração |
| Antes do commit do bundle | Sem sucesso observável; nunca remover diretório preexistente ou resultado de outro writer |
| No ponto de publicação, resultado incerto | Conferir o destino/identidade antes de decidir; nunca apagá-lo por suposição de propriedade |
| Após bundle publicado | Considerar artefato comprometido; falha de log/apresentação não o remove nem provoca nova execução |
| Limpeza falhou | Preservar e identificar resíduos relativos não confirmados; erro principal e causa continuam acessíveis |
| KeyboardInterrupt/SystemExit | Propagar mesma instância/código; apenas unwind/limpeza privada com repropagação; nunca converter em sucesso/falha química |
| Processo morreu abruptamente | Não prometer compensação Python; staging/reserva órfãos não são artefatos concluídos |

**Q-06:** validar a primitiva exata de reserva/publicação e política de recuperação antes de congelar o contrato. A especificação deverá distinguir atomicidade de visibilidade, persistência após queda de energia e recuperação; rename/fsync isolados não são garantia universal de durabilidade. Não prometer segurança concorrente nos registros antigos do 020; o novo protocolo cobre somente suas próprias saídas.

**R:** avaliar um registro pequeno de tentativa próprio da materialização para relatar fase/erro/resíduos e recuperação. Não generalizar `ExecutionAttempt` nem reutilizar `LigandPromotionAttempt`. Se adotado, registrar a relação entre commit do bundle e atualização terminal: resultado publicado prevalece sobre falha posterior de apresentação/persistência de status, com erro específico que informe commit confirmado/indeterminado. **Q-07:** escolher no rascunho entre esse registro novo e um protocolo menor de manifesto final + diagnóstico de reserva; qualquer escolha deve cobrir a matriz de falhas, sem estado genérico universal.

## 14. Segurança e limites proporcionais

**R:** derivar RAW apenas do ProteinInput verificado, sob `inputs/proteins/<id>/`; validar caminhos relativos lexicalmente, componentes de traversal, containment por componentes de Path e identidades de diretórios/arquivo, rejeitando links/reparse points conforme o perfil validado. A leitura deve produzir snapshot/bytes que tenham o checksum esperado. Não passar caminho arbitrário, URL ou conteúdo comprimido ao Gemmi. Nenhum fallback para leitura menos segura se a primitiva falhar.

O leitor de snapshot de proteínas precisa de autorização/implementação própria: pode adaptar um helper privado comum de atomic.py com raízes fechadas por tipo, se isso não alterar o comportamento de ligantes, ou implementar helper específico na nova camada de storage. **Q-08:** decidir o menor reuso demonstravelmente seguro; a allowlist inclui atomic.py somente se esse reuso for escolhido e coberto por regressões da promoção de ligantes. Não copiar cegamente a Root Template de ligantes nem prometer suporte Linux/NTFS baseado em arquivo .cif de teste.

Limitar bytes de entrada, átomos/linhas examinadas, bytes de saída e auditoria e profundidade/tamanho de categorias antes de alocar grandes estruturas. Em B, o subconjunto não cresce por expansão, mas categorias/auditoria ainda consomem memória. Tetos numéricos e comportamento ao exceder devem ser fechados no rascunho, com erro antes de publicar; o teto herdado de 1 GiB não torna seguro materializar todo arquivo dessa dimensão em RAM.

CLI deve usar templates tipados, ids/contagens/checksums e caminhos relativos controlados. Não imprimir exceção nativa, traceback ou caminho absoluto do usuário. O serviço é dono do logging; a CLI não duplica atividade nem executa compensação. Nenhum logger ou output científico novo exige alterar comandos antigos. Falhas apenas de apresentação após commit devem dizer que o arquivo foi publicado, sem alegar nova falha da transformação ou tentar de novo.

## 15. Testes propostos e aceitação

Os ids abaixo são **cenários propostos de estudo**, não uma matriz congelada, não testes escritos, não contagem de pytest. Parametrizações podem gerar mais itens; reconciliar funções/casos/itens no rascunho e em cada entrega.

| Grupo | Ids propostos | Comprovação exigida |
|---|---|---|
| Vínculo e identidade | P021-01–06 | Leitura da inspeção exata; ids/checksums cruzados; ausência/corrupção sem fallback; versão/profile; inspeção incompleta; caminho inválido |
| Modelo/assembly/cadeias | P021-07–12 | Modelo escolhido não é primeiro; recusa de assembly não nulo em B; labels distintos de auth; cadeia ausente; seleção vazia; RAW com múltiplos modelos |
| Componentes | P021-13–19 | Keep/remove efetivos; precedência já resolvida não reinterpretada; água em múltiplas ocorrências; ausência exige decisão; unknown preservado por escolha; modificado em polímero; conflito de cadeia e componente |
| Altloc/ocupância | P021-20–25 | Preservação de alternativas; seleção explícita com átomos comuns; grupo incompleto/ambíguo; micro-heterogeneidade; ocupância zero/parcial/ausente e B-factor; H/D preservados |
| Conexões/metadados/saída | P021-26–33 | Ambos retidos; ambos removidos; corte reconhecido versus recusado; altloc/simetria; anisotrop; integridade de entidades/seq; categorias omitidas auditadas; saída mmCIF relida e conferida contra plano |
| Publicação e retry | P021-34–41 | Bundle indivisível; falha em cada escrita/rename; mesmo id concorrente; chave diferente; resíduos próprios; preexistentes intactos; reused com hash; resultado corrompido nunca reconstruído |
| Interrupção/CLI/regressão | P021-42–48 | KeyboardInterrupt e SystemExit por fase; falha de logging; falha de apresentação pós-commit; mensagens/exit codes; imports opcionais; sem efeitos no 017/018/020 |

Total proposto: **48 cenários** = 6+6+7+6+8+8+7, ids 01–48 sem lacuna. O cenário P021-42 deve gerar injeções independentes dos dois tipos em validação, carga, snapshot, parsing, plano, serialização, verificação, reserva, publicação e apresentação; não aceitar “cada fase” como frase sem enumerá-las. Esses itens não foram executados.

Fixtures devem usar mmCIFs reais em bytes com coordenadas, todos os campos label/auth necessários e conexões retidas pelo parser real. Algumas fixtures existentes do 020 são propositalmente mínimas (ex.: expressão de assembly sem matrizes operacionais) e não provam capacidade de materialização. Writer e reader da mesma biblioteca podem concordar num erro: conferir também plano/linhas/Decimal/checksums e valores esperados independentes, não apenas sucesso de parsing.

Para B, exigir igualdade numérica/token dos campos científicos preservados do RAW; nenhum deslocamento, remoção por geometria ou arredondamento oculto. O checksum do RAW antes/depois é invariável. Testes de CLI têm de chamar serviço real em integração representativa; mocks somente no ponto de falha/injeção, nunca fabricando saída química. Testes Windows 11/NTFS cobrem publicação/contenção/reservas de verdade, inclusive dois processos independentes e reparse points quando suportados; skips precisam de motivo explícito e não contam como validação.

Aceitação candidata: refs e schema fixados; plano completo sem decisão científica implícita; arquivo e auditoria verificáveis; RAW/política/inspeção/resolução intactos; idempotência e propriedade de compensação comprovadas; nenhum sucesso parcial; comandos legados preservados; ambiente suportado declarado. Aceitar o estudo não significa satisfazer esses critérios de implementação.

## 16. Checkpoints e allowlist preliminares

| Checkpoint proposto | Entrega | Gate de evidência |
|---|---|---|
| CP1 — domínio e plano | DTOs, vínculo, políticas complementares, casos aceitos/recusados | Revisão de semântica sem filesystem complexo; fixtures reais de linhas/conexões |
| CP2 — adapter e saída | Entrada aditiva no adapter Gemmi, filtro de categorias/átomos, auditoria e reparse | Gemmi 0.7.5 real; valores fonte preservados; nenhuma mudança no caminho de inspeção 020 |
| CP3 — storage e serviço | Snapshot de proteína, reserva, bundle, retry/falhas/resíduos | Windows 11/NTFS obrigatório; concorrência real; falhas por fase e compensação por propriedade |
| CP4 — CLI e regressão cumulativa | Novos comandos, apresentação tipada, testes ponta a ponta | Uma chamada por operação; falha pós-commit; suíte existente e sem RDKit/Gemmi opcionais conforme fronteiras |

Allowlist candidata, a reduzir/fechar no rascunho: novos `src/molecular/receptor_materialization.py`, `receptor_materialization_registry.py`, `receptor_materialization_service.py` e, se necessário, `receptor_materialization_storage.py`; adições delimitadas em `receptor_parsing.py` e `cli.py`; `atomic.py` somente sob Q-08 com regressões específicas. Novos testes espelhados dos módulos novos, mais adições em `tests/test_receptor_parsing.py` e `tests/test_cli.py`; `tests/test_atomic.py`/`tests/test_promotion_service.py` apenas se o helper compartilhado for alterado.

Não se prevê alterar os schemas/registries/serviços do 020, ScientificEntity/MolecularState/Conformer, transformação ou execução de tautômeros. `pyproject.toml` não precisa de dependência adicional; atualização do pin Gemmi não faz parte de B. Nomes são provisórios: não criar arquivo até a especificação final e a autorização do checkpoint. Nenhuma branch de código foi criada por este estudo.

## 17. Questões para fechar antes da especificação final

| Questão | Recomendação provisória | O que a revisão deve decidir |
|---|---|---|
| Q-01 escopo B versus C | B com recusa explícita de assembly | A entrega restrita é suficiente? Se não, exigir estudo C antes de autorizar código |
| Q-02 conexões cruzadas | Reconhecimento por conexão, nunca silencioso | Aceitar esse complemento ou bloquear todo corte no perfil inicial |
| Q-03 categorias e integridade | Catálogo fechado e auditoria de perdas | Fechar chaves, filtro e comportamento para categorias desconhecidas relevantes |
| Q-04 declaração versus execução CLI | Política persistida separada do artefato | Dois comandos ou fachada única com intenção registrada, sem acoplamento químico |
| Q-05 chave e equivalência | Identidade de snapshot e decisões completas | Canonicalização, hashes de fontes e comportamento de retry após alteração externa |
| Q-06 protocolo de publicação | Bundle completo sob reserva exclusiva | Garantias Windows/NTFS, recuperação e ponto de commit precisos |
| Q-07 tentativa persistida | Avaliar registro mínimo próprio | Escolher mecanismo proporcional que explique falhas, interrupções e resíduos |
| Q-08 leitor de proteína | Reuso privado seguro ou helper específico | Evitar hardcode de ligante e preservar contratos/validação da promoção existente |
| Q-09 limites e apresentação | Tetos operacionais sem defaults científicos | Números, perfil de memória/saída, categorias de erro e campos de sucesso |

Essas questões não impedem a revisão do estudo; impedem tratá-lo como contrato final pronto para implementar. Nenhuma deve ser resolvida por improviso do implementador. As escolhas devem aparecer na reconciliação e depois no rascunho, distinguindo ciência de engenharia.

## 18. Evidências observadas, não executadas e limites

Observado nesta sessão: HEADs remotos; 66 Git blobs da baseline conferidos; identidade e leitura integral da especificação; leitura dos contratos e dos caminhos relevantes de produção/testes; contagem AST de 152 funções `test_` nos seis arquivos `test_receptor_*`; fontes primárias Gemmi e dicionário wwPDB; os limites de assembly e de snapshot de ligante descritos acima. O índice de funções não é coleta pytest nem cobertura medida.

Não executado: pytest, teste científico Gemmi, instalação limpa, transformação de receptor, teste Windows/NTFS, ensaio concorrente, medição de desempenho ou confiabilidade após crash. Nenhuma contagem histórica de suíte foi reapresentada como resultado atual. Python observado é 3.12.14; Gemmi/pytest indisponíveis. Não se solicitou sonda ao implementador porque a capacidade necessária ao confronto arquitetural pôde ser verificada na fonte primária; testes de produção continuam futuros gates reais.

Somente referências e novos documentos deste estudo são publicados no governance, além da atualização autorizada de STATUS. Contratos congelados e documentos anteriores permanecem byte-idênticos; a referência N020 é cópia exata, não versão corrigida. O estudo aponta limites do consumidor 021 sem transformar preferências de implementação em defeitos do 020 aprovado.

## 19. Encaminhamento e decisão de prontidão

O estudo está completo como proposta confrontável e **pronto para revisão independente**, com questões abertas enumeradas. O revisor deve avaliar a suficiência de B, procurar perda silenciosa de identidade/conectividade e verificar se o protocolo proposto realmente evita remover resultado preexistente. Pode recomendar outra opção com fundamento. Não precisa repetir a revisão do 020-A, interpretar seu stand-by como encerramento, nem executar implementação para aprovar um estudo.

Resultado esperado: parecer novo com BLOCKERS/MAJORS/MINORS/NOTES, referências verificáveis, disposição sobre Q-01–Q-09 e veredito REJECT / REQUEST CHANGES / APPROVE FOR DRAFT SPECIFICATION. Parecer favorável permite decisão sobre rascunho, não congelamento nem implementação. O implementador aguarda.

## 20. Referências verificáveis

N020: [especificação final do 020, cópia exata no pacote deste estudo](references/INCREMENT_020_FINAL_SPECIFICATION.md), especialmente §§7, 10–12, 14–18, 20–28, 32–35 e 38. Identidade integral na seção 1 e no manifesto de evidências.

Todos os links Cxx abaixo fixam a baseline `08b797e0985e123ffd4d7ca7e5a5e8f040e63851`:

- C01: [registry.py](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/src/molecular/registry.py) e [inputs.py](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/src/molecular/inputs.py).
- C02: [receptor_parsing.py](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/src/molecular/receptor_parsing.py), ParsedAtom/ParsedReceptorDocument; `_parse_mmcif_document`; `_group_atom_site_into_residues`; `parse_receptor_raw`.
- C03: [receptor_inspection.py](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/src/molecular/receptor_inspection.py), `compute_inspection_id`, inventários, truncamentos e `build_receptor_inspection_report`.
- C04: [receptor_selection.py](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/src/molecular/receptor_selection.py).
- C05: [receptor_resolution.py](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/src/molecular/receptor_resolution.py).
- C06: [receptor_registry.py](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/src/molecular/receptor_registry.py).
- C07: [receptor_service.py](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/src/molecular/receptor_service.py), declarações/resolução e helpers `_resolve_*`.
- C08: [cli.py](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/src/molecular/cli.py) e [activity.py](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/src/molecular/activity.py).
- C09: [scientific.py](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/src/molecular/scientific.py) e [scientific_registry.py](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/src/molecular/scientific_registry.py).
- C10: [transformation.py](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/src/molecular/transformation.py).
- C11: [execution.py](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/src/molecular/execution.py).
- C12: [atomic.py](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/src/molecular/atomic.py), `atomic_write_text`, `check_storage_identity_conflict`, `publish_staged_directory` e `create_verified_raw_snapshot`.
- C13: [promotion_service.py](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/src/molecular/promotion_service.py).
- C14: [pyproject.toml](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/pyproject.toml).
- Testes: [diretório tests da baseline](https://github.com/sysoutemanuelhenrique/molecular-platform/tree/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/tests); índice por função/linha em `evidence/receptor-test-index.json`. Consultados em particular T-003, T-011, T-056, T-063, T-124–130, T-133–137 e as correções de logging/selection_id.

Fontes oficiais do Gemmi, todas no commit da tag 0.7.5 acima:

- G01: [python/read.cpp](https://github.com/project-gemmi/gemmi/blob/5cc1c23c6007e0e6cbd69289c6f7c0bff50e943e/python/read.cpp).
- G02: [python/cif.cpp](https://github.com/project-gemmi/gemmi/blob/5cc1c23c6007e0e6cbd69289c6f7c0bff50e943e/python/cif.cpp).
- G03: [python/write.cpp](https://github.com/project-gemmi/gemmi/blob/5cc1c23c6007e0e6cbd69289c6f7c0bff50e943e/python/write.cpp) e [include/gemmi/to_mmcif.hpp](https://github.com/project-gemmi/gemmi/blob/5cc1c23c6007e0e6cbd69289c6f7c0bff50e943e/include/gemmi/to_mmcif.hpp).
- G04: [python/mol.cpp](https://github.com/project-gemmi/gemmi/blob/5cc1c23c6007e0e6cbd69289c6f7c0bff50e943e/python/mol.cpp).
- G05: [src/assembly.cpp](https://github.com/project-gemmi/gemmi/blob/5cc1c23c6007e0e6cbd69289c6f7c0bff50e943e/src/assembly.cpp) e [include/gemmi/assembly.hpp](https://github.com/project-gemmi/gemmi/blob/5cc1c23c6007e0e6cbd69289c6f7c0bff50e943e/include/gemmi/assembly.hpp).
- G06: [documentação versionada mol.rst](https://github.com/project-gemmi/gemmi/blob/5cc1c23c6007e0e6cbd69289c6f7c0bff50e943e/docs/mol.rst), [cif.rst](https://github.com/project-gemmi/gemmi/blob/5cc1c23c6007e0e6cbd69289c6f7c0bff50e943e/docs/cif.rst) e [src/to_mmcif.cpp](https://github.com/project-gemmi/gemmi/blob/5cc1c23c6007e0e6cbd69289c6f7c0bff50e943e/src/to_mmcif.cpp).
- G07: [LICENSE.txt da versão](https://github.com/project-gemmi/gemmi/blob/5cc1c23c6007e0e6cbd69289c6f7c0bff50e943e/LICENSE.txt).

Fontes primárias de semântica estrutural, consultadas em 21/11/2026:

- W01: [wwPDB — label_asym_id](https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_atom_site.label_asym_id.html).
- W02: [wwPDB — correspondências PDB/mmCIF](https://mmcif.wwpdb.org/docs/pdb_to_pdbx_correspondences.html).
- W03: [wwPDB — expressões de assembly](https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_pdbx_struct_assembly_gen.oper_expression.html), incluindo composição de grupos em ordem definida pelo dicionário, não um split ingênuo por vírgulas.
- W04: [wwPDB — altloc](https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_atom_site.label_alt_id.html).
- W05: [wwPDB — ocupância](https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_atom_site.occupancy.html).

STUDY COMPLETE: YES
READY FOR INDEPENDENT STUDY REVIEW: YES
READY FOR IMPLEMENTATION: NO
FINAL SPECIFICATION FROZEN: NO
CODE REPOSITORY MODIFIED: NO
