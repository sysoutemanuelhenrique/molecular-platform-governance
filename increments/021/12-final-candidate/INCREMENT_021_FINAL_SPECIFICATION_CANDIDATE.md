# Incremento 021 — Candidata final de especificação
## Materialização da Seleção de Receptor

Versão: candidate-1 (candidata final, não congelada). Data: 23/11/2026. Autor: Codex arquiteto. Estado: proposta completa para revisão independente; **não congelada e não autorizadora de implementação**. O emprego de deve/proibido define a proposta a confrontar, não altera a autorização da etapa atual.

## 1. Autoridade, snapshots e documentos integrantes

Redação autorizada diretamente por Emanuel Henrique da Silva: incorporar P-1 a P-5 e NOTE-F1, publicar no governance e preparar revisão independente, sem implementação nem congelamento. O registro literal permanece em increments/021/06-draft-specification/evidence/OWNER_DRAFT_AUTHORIZATION.md, no snapshot original identificado; a candidata não cria uma nova autorização.

| Referência | Snapshot |
|---|---|
| Código, molecular-platform, main | 08b797e0985e123ffd4d7ca7e5a5e8f040e63851 |
| Governance de entrada desta candidata, docs/020-a-candidate1-review-20261020 | 7ab557697f78b0b8eb8c1e53997ef6e752f9470e |
| Revisão focal do draft-2 | b3df694b96cc0c425c12c73c9678c2b7dd090112 |
| Revisão independente do draft-1 | 680aef4eecc3852fff78a70c75691993d51849b6 |
| Revisão focal | 8778b83844fe9bff9b61862743277d5ee3172ac5 |
| Reconciliação | d5580b162e0fe5ebec8bedd0b986f767f4f3194a |
| Aprovação D-01(b)/D-02 | 771d1aa2e6218188113aad4e54849c103219a25c |
| Main do governance, preservar | a47183dfec8213c765ed43ae482c8c227760a3d5 |
| Fonte Gemmi 0.7.5 | 5cc1c23c6007e0e6cbd69289c6f7c0bff50e943e |

Referência N020: INCREMENT_020_FINAL_SPECIFICATION.md, 1.975 linhas, 210.880 bytes, SHA-256 cf6cb534f9267d51e718052c7b36a2293c522bc566c99cf3bb2ef5909385a0a6. O arquivo permanece no caminho já publicado increments/021/01-study/references/, sem edição.

Integram esta candidata: **evidence/CATALOG_021.json**, **evidence/SCHEMAS_021.md**, **evidence/SCENARIOS_021.csv** e **evidence/IDENTITY_BASIS_CASES.json**. O catálogo é dado documental de contrato, não configuração editável pelo cientista nem código implementado. A matriz CSV contém cenários propostos individualmente, não resultados pytest. evidence/FILE_IDENTITIES.json identifica os bytes da entrega, excluindo a si próprio. Manifestos históricos só devem ser verificados em seus commits históricos.

Precedência proposta: corpo deste documento para algoritmo/ordem/erros; SCHEMAS para os campos fechados; CATALOG para tags e ações; SCENARIOS para comprovação. Inconsistência entre anexos é achado de revisão a resolver antes de congelamento, nunca licença de escolha do implementador. O 020-A continua em stand-by.

## 2. Objetivo e limites científicos

Produzir novo mmCIF derivado da seleção confirmada pelo 020, preservando RAW, identidade das decisões e coordenadas dos átomos retidos. O produto é **estrutura materializada**, não receptor quimicamente preparado, geometria experimental nova, conformer único, estrutura minimizada ou entrada validada para docking.

Incluído: modelo fonte explícito, asyms nativos, disposições efetivas, decisões complementares explícitas, todos os altlocs dos asyms retidos, filtragem referencial, arquivo/manifesto/auditoria, idempotência e publicação limitada ao perfil de plataforma qualificado.

Excluído: expansão de assembly/NCS/cela, seleção parcial de altloc, escolha por ocupância, remoção/adição de H/D por conveniência, protonação/pKa/cargas, reparo/capping/loops, minimização, PDB/PDBQT, docking, GUI, scheduler/nuvem, migração do 020, universalização de ExecutionAttempt ou ExperimentalConditions. ScientificEntity/MolecularState/Conformer não são criados automaticamente.

**Limite deliberado de cobertura:** categorias/tags desconhecidas fora das omissões aprovadas continuam recusadas. O código literal 1_555 é reconhecido pela convenção PDBx adotada pelo perfil mesmo sem tabela; tabelas presentes não podem contradizê-lo. Outros operadores precisam de contexto fonte suportado. O perfil ainda recusa conexões retidas envolvendo imagens não identidade e NCS não expandido. Não anunciar suporte geral ao arquivo PDB, NMR ou EM. 5i55 pode ser fixture real para identidade sem tabela; 1pfe continua sendo caso de recusa por conexões 1_555/9_555, não por simples cobertura do catálogo. O inventário de três arquivos não prova materialização.

## 3. Compatibilidade e fronteiras

Preservar código, schemas 1.0, perfis, resultados, comandos e taxonomia do 020; nada reexecuta inspect/resolve para reparar referência. Preservar 017/018/019 e seus serviços. Não corrigir no parser de inspeção antigo a grafia de inserção constatada no estudo. O novo caminho lê os tokens corretos e registra sua origem RAW.

Única fronteira Gemmi: entradas aditivas em receptor_parsing.py, sem alterar o comportamento de parse_receptor_raw nem seus DTOs. Nenhum objeto Gemmi atravessa a fronteira. Fora dela, domínio/registry/storage/service/CLI usam DTOs próprios e bytes/índices. Não usar setup_entities, remoções automáticas, transform_to_assembly ou inferência geométrica.

Gemmi permanece dependência opcional, exatamente 0.7.5. Import tardio no adapter; falta/versão divergente gera erro de configuração, sem impedir --help/import de módulos puros. Não adicionar dependência, alias tbmp ou pin novo em pyproject.toml. molecular e tbohr continuam os entry points existentes.

## 4. Perfil operacional e limites fechados propostos

Leitura/publicação de produção deste incremento: Windows 11 x64, NTFS local em disco fixo, escritores cooperantes com o protocolo e diretórios de experimento sob controle do responsável. Detectar esse perfil antes de criar recursos. Outros ambientes recebem erro de configuração nas operações plan/declare/run; validações puras e testes de adapter podem rodar em Linux. show/show-policy também usam leitor validado no perfil inicial. Não prometer resistência a administrador malicioso ou durabilidade contra queda de energia.

| Limite | Valor; excesso é recusa antes de publicação |
|---|---|
| RAW | 16 MiB, inclusive, contado nos bytes capturados; rejeitar compressão por extensão e magic antes de Gemmi |
| Cada registro YAML 020 | 16 MiB; nenhuma leitura ilimitada |
| policy.yaml/manifest.yaml novos | 1 MiB cada |
| Átomos fonte | 100.000 linhas atom_site |
| Conexões fonte | 50.000 linhas struct_conn |
| Categorias / tags por categoria | 256 / 128 |
| Linhas somadas de categorias / células somadas | 500.000 / 4.000.000 após parsing, antes de planejar/serializar |
| Valor de célula CIF | 1 MiB UTF-8; rejeitar antes de duplicá-lo na saída/auditoria |
| Saída receptor.cif / audit.json / preview serializado | 32 MiB cada, inclusive |
| Política nova: declared_by | 1–200 caracteres, str real, não apenas whitespace, sem controles C0/C1 |

MiB = 1.048.576 bytes. Os números são limites de escopo, não desempenho medido. Verificar tamanho de entrada antes do parsing limita bytes entregues à biblioteca; não se alega limite rígido de RAM ou isolamento do parser nativo. Tetos de DOM não evitam alocação interna durante parsing. Não descomprimir, baixar URL ou buscar recursos externos.

## 5. Captura das fontes e NOTE-F1

Carregar quatro registros fixos: ProteinInput, ReceptorInspectionReport, ReceptorSelectionPolicy e ResolvedReceptorSelection. Layout real: inputs/proteins/<id>.yaml; scientific/receptor_inspections/<inspection_id>.yaml; scientific/receptor_selections/<selection_id>.yaml; scientific/receptor_selections/resolved/<selection_id>.yaml.

Leitor próprio do storage 021 captura cada arquivo em bytes uma vez, sob contenção/identidade, calcula SHA-256 desses bytes e só então decodifica UTF-8 estrito. Para equivalência com read_text(encoding="utf-8"), aplica newline universal ao texto (CRLF→LF e CR→LF) antes de yaml.safe_load e model_validate do modelo existente. BOM UTF-8, quando presente, continua caractere BOM na decodificação e é entregue ao parser YAML como hoje; não removê-lo por uma segunda leitura. Hash não é do texto normalizado. UTF-8/YAML/Pydantic inválido é erro de configuração com cause preservada, sem imprimir o conteúdo.

Não chamar loaders públicos do 020 e depois reabrir os caminhos para hashear. Não alterar aqueles loaders. Essa captura não promete transação simultânea de quatro arquivos: compor um contexto exige validar relações entre os snapshots realmente capturados.

Comparações exatas de ids: ProteinInput.id; inspection.inspection_id; policy.selection_id; resolution.resolved_selection_id e policy_selection_id. A igualdade dos dois últimos já é invariante do schema 1.0; conferir também contra o id solicitado. Conferir protein_input_id, inspection_id, checksums acquisition/raw_checksum_observed/raw_checksum, formato e parser. Recalcular a identidade de inspeção pelos sete campos do perfil 020; não reconstruir seu inventário. NTFS/casefold não autoriza a~A como identidade científica.

Exigir mmcif, full, schema/profile conhecidos 1.0, parser gemmi 0.7.5 e **nenhum parser-limitation**, em qualquer categoria. resolved_chains deve ser não vazio; resolved_assembly deve ser None. Conteúdo incompatível não dispara fallback, inspeção nova, resolução nova ou troca de registro.

RAW somente do caminho relativo acquisition.raw_artifact.path, sob inputs/proteins/<ProteinInput.id>/. Validar lexicalmente id/caminho e containment por componentes; recusar absoluto, traversal, link/reparse point e nomes Windows reservados. Não confundir validate_input_id com prova de elegibilidade de caminho Windows. O leitor de proteína é próprio; não invocar o helper fechado inputs/ligands como se suportasse proteínas.

Capturar bytes do RAW por uma abertura controlada, verificando arquivo regular, identidade do arquivo/diretórios e estabilidade antes/depois; no perfil Windows, impedir escrita/substituição cooperante enquanto o handle estiver aberto. Revalidar cadeia de diretórios e recusá-la se mudar. Não seguir reparse points nem usar fallback de open menos seguro. Falha em obter as garantias do leitor resulta em erro de configuração/armazenamento. Parser recebe exatamente os bytes cujo hash foi conferido contra todos os registros; não o caminho reaberto. Copiar bytes para temporário privado só é permitido se mantiver a mesma identidade, hash e propriedade de limpeza.

## 6. Identidades estruturais e validação do RAW

Um único data block; sem save frames, duplicação de tags canônicas ou categorias malformadas. RAW deve ser UTF-8 válido; BOM do arquivo estrutural é recusado neste perfil. Gemmi cif.read_string(bytes) faz parsing; não escrever parser CIF em Python. A comparação de nomes de tags é ASCII case-insensitive; valores científicos mantêm caixa e tokens originais.

Cada atom_site.id é não nulo e único globalmente no arquivo. Todos os model_num são inteiros positivos informados; ausente/nulo/zero ou mistura sem contexto é recusa, sem or 1. Selecionar M=resolved_model, nunca o primeiro modelo. label_asym/entity/comp/atom não nulos; vínculo atom_site→struct_asym→entity inequívoco. Uma normalização NFC já usada pelo 020 só pode servir à correspondência se for injetiva entre tokens fonte envolvidos; colisão de tokens distintos é recusa, nunca fusão. Não renumerar ids/cadeias/resíduos.

Coordenadas presentes e finitas; ocupância e B-factor preservados como tokens, inclusive 0, frações e null. Quando ocupância for numérica, exigir finita e ≥0; não normalizar para 1. Não preencher ausências. Numeric tokens com incerteza, quando admitidos pelo campo, preservam o token; não converter via float para serializar. Um valor desconhecido não é evidência de zero. H e D existentes acompanham os átomos selecionados.

Para a validação numérica necessária a esse perfil, aceitar tokens não citados que casem integralmente com `[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?(?:\([0-9]+\))?`. Aceitar 1.2e3(4) e recusar 1.2(4)e3. Remover apenas o su final entre parênteses para validar o valor central por Decimal finito; nunca usar essa conversão para escrever o token. Coordenadas não aceitam null; occupancy/B_iso aceitam null real, ou esse número finito (occupancy não negativa). model_num e formal_charge, se informada, usam inteiro decimal não citado; formal_charge pode ser null. Outros descritores copiados não recebem validação química universal por esta operação.

Ocorrência de resíduo: (M,label_asym,label_comp,label_seq quando não nulo; senão auth_seq + código de inserção) com auth_asym como restrição de consistência, não propriedade biológica. Se faltarem tanto label_seq quanto auth_seq de forma que a ocorrência não seja distinguível, recusar. Micro-heterogeneidade não permite fundir variantes comp_id: preservar todas sob a regra uniforme por asym. Átomos sem altloc e variantes são todos mantidos/removidos juntos.

## 7. Tabela S/D/U e P-3

S = label_asym explicitamente selecionado no 020; D = disposição efetiva resolvida por chave (asym,CCD), sem reaplicar baldes ou mudar sua precedência; U = escolha obrigatória preserve ou require-disposition para componentes não abordados. Resolução ampla é projetada sobre M; chave ausente em M não tem efeito e é auditada como não aplicável ao modelo, sem aplicar decisão a outro modelo.

| Contexto em M | S | D | Resultado |
|---|---:|---|---|
| Polymer | sim | ausente/keep | Incluir asym inteiro |
| Polymer | sim | remove sobre resíduo/componente | Recusar, inclusive remoção terminal |
| Polymer | não | ausente/remove | Excluir asym inteiro por complemento de S |
| Polymer | não | keep | Recusar conflito; não resgatar só o resíduo |
| Water/non-polymer/macrolide/branched | sim | ausente/keep | Incluir por S |
| Water/non-polymer/macrolide/branched | sim | remove | Recusar conflito |
| Water/non-polymer/macrolide/branched | não | keep/remove | Incluir/excluir por D |
| Water/non-polymer/macrolide/branched | não | ausente | Incluir por U=preserve; recusar por U=require-disposition |
| Fora de M | qualquer | qualquer | Excluir por modelo; não é remoção química |

Tipo vem de entity.type da fonte, não de report.chains ou do indicador HETATM. Tipos unknown/unrecognized e vínculos contraditórios relevantes a M são recusados neste perfil, sem reclassificar o relatório antigo.

**P-3 fechado propositivamente:** para todo asym não polimérico, incluindo water/macrolide/branched, computar as decisões de todas as suas ocorrências em M. Exigir uniformidade total incluir ou excluir; mistura de decisões é erro de entrada. Não escolher a maior parte, primeiro CCD ou maior ocupância. Assim, NAG remove/BMA keep e variantes de ligante com decisões diferentes são recusadas mesmo sem struct_conn interno. Seleção de asym é uma unidade física, enquanto D continua sendo chave de disposição do 020; não confundir as duas coisas.

Ausência de disposição sobre um asym explicitamente selecionado não requer U: S já é a escolha explícita de retenção. Ausência de S para polymer é exclusão de complemento, sujeita ao reconhecimento P-1. Nenhum componente é ligado biologicamente a cadeia por auth_asym_id ou distância.

## 8. Plano verificável, P-1 e P-2

Há uma operação de preview que não publica registros científicos: plan carrega/captura fontes, constrói decisões e retorna os conjuntos e hashes. Pode criar recursos temporários próprios e um evento de atividade; não é promessa de zero escrita operacional. Não gerar coordenadas novas nem publicar artefato nessa operação.

No preview, ações dependentes de reconhecimento são propostas condicionais, não consentimento já existente. O planner pode calcular a exclusão do complemento e a omissão candidata de metalc/hydrog para produzir os hashes; declare/run só aceitam materializá-las depois de validar os acknowledgements recebidos. Não existe dependência circular que exija o hash para obter o próprio preview.

**X:** lista de asyms polymer presentes em M e excluídos pelo complemento da lista S, com entity_id, número de átomos e hash da lista ordenada de atom_site.id/ordinal fonte. **O:** todas as ocorrências retidas de asyms fora de S por D ou U, com M,label_asym,entity,CCD,identidade da ocorrência, origem D/U, contagem e hash dos átomos, além do auth_asym fonte e sua classificação de coincidência com polímeros retidos/excluídos/vários/nenhum. auth_asym não muda o resultado.

Ordenação: valores decodificados, sem casefold de identificadores, por sequência de code points Unicode, com null antes de str; ocorrências de mesma chave usam ordinal fonte. Arrays de ids atômicos seguem ordinal fonte. Hashes X/O incluem source_context_key e M, não só nomes. plan_key inclui esses hashes e todas as decisões de átomos/conexões/categorias, engine/profile/catalogue e U. O conjunto de preview não pode ser uma amostra truncada; limites provocam recusa.

**P-1:** S é tratado como seleção fechada de asyms polymer **somente depois** que o cientista declara acknowledge_exclusions_key igual ao hash de X quando X não é vazio. A declaração converte a exclusão integral de cada cadeia de X em decisão explícita suportada; a auditoria mantém reason=chain-complement e o acknowledgement correspondente como prova separada do ato. A lista S sozinha não autoriza essa interpretação. Se X vazio, o campo deve ser null. Ausência, hash incorreto ou hash de conjunto anterior é erro de entrada, sem execução.

Uma cadeia de ácido nucleico em X reconhecido também sai inteira. Conexões hydrog de pareamento com fita retida podem ser omitidas nas condições de §10; a auditoria enumera cada linha e o aviso não sugere que a fita restante seja duplex intacto. Se o cientista não reconhecer X, a política não é declarada; não há fallback para interpretação implícita.

**P-2:** se O não vazio, exigir acknowledge_outside_key igual ao hash integral de O. Se vazio, exigir null. Esse ato pertence à declaração e vincula-se ao snapshot efetivo. Aviso na tela, activity log e sucesso da operação não substituem o reconhecimento. run recaptura fontes e recalcula o plano; qualquer diferença de fonte/hash/conjunto invalida o reconhecimento e recusa a execução. Não atualizar a política ou gerar outro preview aceito automaticamente.

Além de X/O, acknowledge_plan_key é sempre obrigatório e deve coincidir com plan_key. O preview informa os três valores e as contagens; o comando de declaração exige que o usuário os forneça. O serviço não copia hashes calculados por ele para campos de reconhecimento ausentes. Atos são registrados com declared_by e timestamp, sem alegar assinatura eletrônica ou certificação de terceiros.

## 9. Conexões e origem dos endpoints

Ler struct_conn do RAW capturado, com nomes canônicos pdbx_ptnr{1,2}_PDB_ins_code e altlocs. Não usar ParsedConnection/lista de colunas do 020 como verdade estrutural suficiente. Registrar na auditoria que a inserção vem do RAW, sem editar/reinspecionar o relatório que a perdeu. As restrições de endpoint devem convergir para uma única ocorrência e label_atom_id em M; o endpoint pode conter variantes de altloc dessa mesma identidade, nunca ocorrências distintas. Não escolher o primeiro match nem usar null como wildcard ilimitado. Usar label e, quando necessário para água com label_seq nulo, auth_seq/inserção da mesma ocorrência; nunca trocar namespace por heurística.

Dois códigos de altloc informados por aliases de coluna devem concordar; contradição é recusa. Altloc ausente/nulo resolve o conjunto ordenado de variantes de (ocorrência,label_atom_id). Todos os átomos desse endpoint devem ter o mesmo destino pela uniformidade P-3; contradição é erro. Altloc explícito restringe esse conjunto, com aliases concordantes. Mais de uma ocorrência candidata continua ambiguidade. Não gerar produto cartesiano nem novas linhas de conexão: preservar literalmente a linha fonte quando permitida; registrar os dois conjuntos de ids na auditoria. K conta endpoints retidos, não o número de variantes.

Todo pdbx_ptnr3_* deve ser marcador nulo real (. ou ?); coluna ausente é equivalente a não declarado, mas string citada '?' não é null. Terceiro parceiro preenchido recusa o perfil inteiro. id de conexão não nulo/único; conn_type literal reconhecido, sem classificação pela categoria covalent do relatório. Fonte sem struct_conn registra indisponibilidade e não certifica ausência química de ligações.

Todas as conexões são resolvidas no M escolhido antes de aplicar máscara. Se um endpoint nem existe ou é ambíguo em M, recusar, em vez de apagar a linha como não aplicável. Só depois calcular K=0/1/2 extremos retidos. Diferentes modelos não são unidos para completar uma conexão.

Tipos covalentes fechados: covale, covale_base, covale_phosphate, covale_sugar, modres, disulf. Tipos de exceção: metalc, hydrog. saltbr/mismat e tipos desconhecidos são fora do perfil quando K>0; quando K=0, omitir com auditoria e token literal, sem atribuir semântica ao tipo. Case de ucode pode ser reconhecida para a classificação; preservar token fonte.

K=1 com tipo covalente é sempre recusa. K=1 com metalc/hydrog só permite omissão se o átomo removido pertence a um asym inteiro excluído por D=remove ou X reconhecido, com identidade/decisão documentadas. Não usar a exceção para exclusão só por outro modelo, remoção parcial, erro de match, categoria desconhecida ou falta de reconhecimento. K=2 preserva a linha apenas sob o contexto de simetria permitido. K=0 omite e audita ambos removidos.

## 10. P-4 — regra de simetria e matriz completa

A mesma isometria conhecida aplicada a ambos os endpoints preserva sua relação geométrica. A recusa abaixo de iguais não identidade é um limite conservador de cobertura do perfil, não impossibilidade geométrica. Nenhuma transformação espacial é aplicada.

Código suportado sintaticamente: n_klm, n inteiro positivo e k/l/m dígitos de 1 a 9. Null é . ou ? não citado/coluna ausente. Exceto pela regra explícita de 1_555 abaixo, operador n vem de symmetry_equiv(id,pos_as_xyz) ou space_group_symop(id,operation_xyz) da própria fonte, nunca do namespace de operadores de assembly. Se as duas tabelas declararem o mesmo n, exigir expressões concordantes após remoção de whitespace ASCII e de sinais + iniciais em cada coordenada; nenhuma tabela tem precedência silenciosa.

Identidade: tradução 555 e tripla exatamente x,y,z, admitindo + em cada eixo e whitespace ASCII. O token decodificado exatamente 1_555 é identidade pela convenção PDBx deste perfil quando ambas as tabelas estão ausentes; registrar identity_basis=pdbx-1_555-convention. Essa é uma regra explícita do perfil alinhada ao writer Gemmi pinado, não um teorema para qualquer CIF. Para aceitar 1_555 como identidade em K>0, se alguma tabela existir, exigir operador 1 presente e identidade nas tabelas presentes, sem duplicações/contradição; registrar identity_basis=source-operator. Não aplicar a exceção a 1_556, 2_555, 01_555 ou operadores de assembly; não avaliar expressão arbitrária. x+0,y,z pode ser uma identidade matemática, mas está fora da gramática de comprovação deste perfil e provoca recusa se necessária. Não consultar nome de grupo espacial para fabricar tabela ausente.

Para K>0, código não nulo malformado, operador não localizado ou duplicado/contraditório é UNSUPPORTED_SYMMETRY antes da matriz. A exceção é exatamente 1_555 sem nenhuma das duas tabelas, reconhecido conforme a regra anterior. Se K=0, esses dados podem ser omitidos com a linha inteira e o motivo auditado, sem validar imagem que não será preservada.

| K | Identidade nos dois lados | Iguais não identidade conhecidos | Distintas conhecidas | Null em um lado | Null nos dois |
|---:|---|---|---|---|---|
| 2 | Preservar tokens e referências | Recusar por limite conservador | Recusar por limite de projeção de conexões não identidade | Recusar | Recusar |
| 1 | Omitir com auditoria apenas metalc/hydrog e exclusão inteira reconhecida; demais recusam | Recusar | Recusar | Recusar | Recusar |
| 0 | Omitir com auditoria | Omitir com auditoria | Omitir com auditoria | Omitir com auditoria | Omitir com auditoria |

As 15 células têm ação determinada. A recusa de K=2 com operadores distintos ou iguais não identidade é escolha conservadora do perfil de projeção: preservar referências a imagens cristalográficas sem garantir o contexto correspondente fica fora desta entrega, embora o RAW possa legitimamente conter essas referências. Não afirmar que o RAW já deveria conter átomos expandidos, nem que a relação geométrica seja impossível. 1pfe sem cortes continua recusado por essa escolha; sua aprovação como caso positivo não é alegada. Dados incorretos/ambíguos de endpoint ainda falham antes da matriz. Preservar uma linha não reescreve symmetry para 1_555. Tabelas de operadores e cell/symmetry preservadas são contexto fonte, não nova demonstração de simetria do recorte; audit.source_symmetry_only=true. Nenhum P1/cela fictícia é criado.

### 10.1. MINOR-N1 — IdentityBasis por endpoint, com precedência fechada

IdentityBasis mantém o vocabulário de três valores. O nome histórico do tipo não significa que todo source-operator seja identidade: ele identifica a origem da resolução do código, que pode indicar operação não identidade. O cálculo é independente de K e executado por lado na ordem ptnr1,ptnr2, antes da aplicação da matriz. Não escolher valores diferentes por otimização, por K=0 ou pela ordem de visita às categorias.

1. Se o campo estiver ausente, for null CIF real, ou seu valor decodificado não tiver a grafia canônica n_klm suportada (sem zero inicial em n), atribuir not-applicable. '?' ou '.' citados são valores literais malformados, não null.
2. Para código bem formado, verificar as duas categorias de operadores no DOM fonte, sem abrir/parsing novo do RAW. Categorias presentes vazias contam como presentes. Se ambas estiverem ausentes, atribuir pdbx-1_555-convention somente ao valor decodificado exatamente 1_555; qualquer outro código recebe not-applicable.
3. Havendo ao menos uma tabela, não há fallback de convenção. Procurar o texto decimal canônico de n por igualdade exata com o id decodificado, sem conversão numérica que funda 1 e 01. Reunir os matches das tabelas presentes. Primeiro, se não houver match, ou houver duplicação do id, expressão nula/vazia ou contradição entre matches, atribuir not-applicable. Caso contrário, há referência única válida em ao menos uma tabela e todas as referências presentes são não nulas/concordantes: atribuir source-operator. Usar a comparação de expressões já definida no §10. Uma referência presente em só uma das duas tabelas pode dar source-operator; isso não dispensa o requisito adicional de confirmação em todas as tabelas presentes para aceitar 1_555 como identidade em K>0.
4. source-operator vale para identidade e não identidade localizadas. Por exemplo, 3_555 localizado recebe source-operator também em K=0; 1_555 sem tabelas recebe pdbx-1_555-convention também em K=0. 1_555 com operador 1 localizado mas não identidade recebe source-operator como origem da referência, porém não passa a validação de identidade de K>0. A classificação não certifica a geometria da expressão nem autoriza uma linha que a matriz recusa.

Após classificar os dois lados, aplicar as validações anteriores e a matriz de K. Em K>0, falta de prova, contradição de identidade ou código não suportado continua recusada conforme o §10; planos recusados não têm ConnectionDecision persistida. Em K=0, not-applicable é permitido e a linha é omitida auditada. Se qualquer lado não nulo for malformado/não localizado/contraditório, symmetry_class=unsupported-discarded; com nulls reais e nenhum lado assim, aplicar one-null/both-null normalmente. Se as duas referências forem conhecidas, usar both-identity/same-nonidentity/different. As validações globais do RAW/catálogo ainda podem recusar dados inválidos antes da emissão de decisão; not-applicable não contorna chaves duplicadas ou categorias malformadas.

O par ordenado identity_basis conserva a ordem dos parceiros, sem sort. Como a presença de tabelas é contexto comum do mesmo RAW, os pares (pdbx-1_555-convention,source-operator) e (source-operator,pdbx-1_555-convention) são impossíveis e devem ser rejeitados na validação de ConnectionDecision, antes da canonicalização. Não gerar hash aceito para um DTO internamente contraditório. Todos os demais pares têm caso válido em K=0. Em K>0 aceito, ambos os lados têm prova de identidade e a mesma base: convenção/convenção sem tabelas, ou source/source com tabelas.

O anexo evidence/IDENTITY_BASIS_CASES.json enumera os nove pares, sete alcançáveis e dois inválidos, com T021-164–172. Para cada par alcançável, o futuro teste de produção usa contexto RAW fixo e hashes verdadeiros de suas fixtures para comparar connection_decisions_key/plan_key em repetições e ordens de visita diferentes. Dois pares inválidos devem falhar na validação, sem hash aceito. T021-173 cobre nulos citados, códigos malformados/não localizados, duplicação/contradição, tabela vazia e distinção entre lookup e prova de identidade. Os checksums de projeções documentais do anexo não são hashes de RAW, ConnectionDecision completo ou plan_key de produção.

## 11. P-5 — catálogo fechado e fechamento referencial

CATALOG_021.json define 94 categorias: 24 filtradas, uma gerada, 67 omitidas e duas guard_then_omit. Permite também omissão auditada das famílias explícitas _pdbx_validate_, _pdbx_nmr_ e _em_. Estas duas últimas retiram metadados experimentais e de ensemble/reconstrução do depósito, sem transferir suas conclusões ao recorte. Não significam suporte irrestrito a NMR/EM; todas as outras precondições de modelo, coordenadas e categorias continuam vigentes. Categoria não listada é recusa. Em categoria filtrada, tag desconhecida é recusa; em categoria explicitamente omitida, todas as tags saem juntas e são auditadas. Não classificar uma categoria desconhecida como inofensiva por seu nome.

O catalogue_sha256 é dos bytes exatos do anexo publicado. A implementação futura incorpora a constante e as regras correspondentes nos módulos autorizados; não lê um catálogo arbitrário do diretório corrente nem permite que o usuário altere silenciosamente o perfil. Uma mudança de regra exige versão/revisão própria e novo checksum.

preserve_tags/omit_tags/generate_tags são sempre arrays disjuntos. Em action=omit, os arrays vazios e a ação significam retirar todas as tags/linhas fonte, não uma sentinela textual all. Em guard_then_omit, omit_tags enumera as tags reconhecidas a validar/retirar e required_tags pode ser subconjunto de omit_tags; a guarda tem precedência sobre a omissão. Em filter/generate, required_tags continua subconjunto das tags preservadas/geradas. required_tags exige presença da coluna, não valor não nulo universal; key e relações obrigatórias exigem não null. Preservar valores como tokens CIF, não quote_list sobre tokens já citados, não float→str. Saída usa tags canônicas lowercase e ordem alfabética de categorias/tags; mantém ordem fonte das linhas sobreviventes. Sem reordenar átomos por geometria ou renumerar ids. Auditar toda linha/tag/categoria retirada; categoria opcional ausente não é fabricada.

Regras de linha, a implementar apenas após aprovação futura:

- ATOM_MASK: manter exatamente os ordinais do plano em M.
- ANISOTROP_ATOM_ID: manter ids retidos; id precisa corresponder inequivocamente a átomo fonte e demais campos informados concordam. Quando existir a categoria, exigir ao menos um tensor U ou B com seus seis componentes numéricos finitos; família com algum valor numérico e outros componentes faltantes/null é recusada. Esd é opcional. Preservar tokens, inclusive sinais dos termos fora da diagonal, sem converter U↔B nem alegar validação física da distribuição térmica.
- RETAINED_ASYM: manter id/asym_id cujo asym sobrevive. RETAINED_ENTITY: manter entidade referenciada por asym sobrevivente.
- RETAINED_ENTITY_ALL_SEQUENCE/RETAINED_ASYM_ALL_SEQUENCE: manter toda a sequência declarada da entidade/asym sobrevivente, inclusive posições sem coordenadas. Não afirmar que sequência declarada equivale a átomos presentes.
- RETAINED_ENTITY_ALL_BRANCH/RETAINED_ASYM_ALL_BRANCH: manter todos os monômeros/links do grupo sobrevivente. Cada link referencia entidade/lista/CCD válidos; um leaving_atom_id ausente de coordenadas não é reconstruído ou considerado erro só por ser leaving atom declarado.
- REFERENCED_CCD_CLOSURE: união dos CCDs dos átomos retidos, sequências/branches preservadas e parent_comp_id preservados. Exigir linhas chem_comp correspondentes, sem nova busca CCD. Campos formula/charge são copiados quando suportados, não calculados.
- CONNECTION_ACTIONS: preservar/omitir pela ação §9–10; USED_CONNECTION_TYPES mantém só os tipos preservados, sem fabricar critérios ausentes. USED_ELEMENTS mantém símbolos usados se atom_type existir; sua ausência é auditada, não preenchida.
- SOURCE_FRAME_SINGLETON/SOURCE_OPERATORS: manter valores fonte do contexto suportado; campos entry_id são derivados da nova entry. Tabelas de operadores mantêm linhas fonte completas, sem aplicar operações. Não criar categorias fonte ausentes.
- MODIFIED_RESIDUE_CONTEXT: resolver contexto de resíduo por label quando informado, ou auth/inserção inequívocos em M; manter anotação do resíduo sobrevivente. parent_comp_id entra no fechamento CCD. Modelo nulo só é aceitável se o contexto for inequívoco no único M de saída, sem inferir outro modelo.
- MISSING_RESIDUE_CONTEXT/MISSING_ATOM_CONTEXT: filtrar por modelo/cadeia explicitamente identificáveis; ausência de coordenadas é a própria anotação e não exige atom_site correspondente. Manter referência de cadeia/seq/CCD existente ou declarar o perfil incapaz de mapear e recusar; não omitir silenciosamente uma anotação preservável.
- AUDIT_OMITTED_CATEGORY: retirar inteiramente, registrando nomes/tags/contagens/hash das linhas retiradas. Isso inclui validações do depósito, anotações de estrutura secundária/sítios, metadados experimentais e instruções de assembly/NCS listadas. Não transferir validação experimental ao derivado.
- NCS_GUARD_THEN_OMIT: antes da máscara e de qualquer omissão, ler struct_ncs_oper com id único e os 12 números de matriz/vetor finitos. Code é given/generate quando informado; nulo/ausente não prova given. Identidade é matriz exatamente I e vetor exatamente zero pelos valores Decimal, sem tolerância arbitrária. Operador não identidade com code diferente de given (inclusive null) recusa UNSUPPORTED_NCS; code desconhecido ou matriz/vetor ausente/inválido recusa INVALID_CIF. Se todos os operadores forem identidade ou given, omitir com auditoria e aviso source-ncs-annotations-omitted. Não expandir e não usar o parser Structure para pular linha incompleta silenciosamente. A regra não afirma que faltam átomos na ASU escolhida; impede apagar a indicação de cópias NCS geráveis neste perfil.
- SPECIAL_POSITION_GUARD_THEN_OMIT: resolver cada anotação pelo modelo/label ou auth/inserção inequívocos e altloc quando informado, sem gerar átomos. Contexto ambíguo/inválido é recusa, não omissão cega. Contar linhas fonte, linhas com interseção de átomos retidos e átomos retidos únicos afetados; gravar em special_positions da auditoria. Omitir as anotações com hash/ordinais, sem mudar ocupância. Havendo interseção retida, emitir special-position-annotations-omitted; categoria vazia ou somente ocorrências removidas não exige esse aviso.
- DERIVED_ENTRY: gerar somente _entry.id e nome do novo block como tbmp_<plan_key>; original entry vai na proveniência, sem alegar nova deposição experimental. Tokens gerados usam quoting Gemmi apropriado; tokens preservados não são recitados.

Se categoria condicional do catálogo for necessária a entidade/ligação retida e estiver ausente, recusar. Em pdbx_entity_branch_link ausente, registrar indisponibilidade, sem inventar ligações internas; a unidade inteira branched é preservada, não certificada como grafo completo. Validar coerência de asym↔entity↔seq/branch↔CCD e endpoints/anisotrop na fonte relevante e na saída. Para cada átomo polimérico retido, (label_entity_id,label_seq_id,label_comp_id) deve encontrar (entity_id,num,mon_id) em entity_poly_seq; num compartilhado por variantes exige comp_id correspondente. Referências de branch usam entity_id/num/comp_id em conjunto, nunca num isolado. Nulos de label_seq de não polímeros não são convertidos em números fictícios. IDs duplicados de chaves do perfil recusam; chaves do perfil são regras desta projeção, não declaração de equivalência com todo o DDL wwPDB.

## 12. Plano, política, manifesto e auditoria

SCHEMAS_021.md fecha os campos propostos. Todos os novos DTOs/records são imutáveis/fechados e rejeitam coerção: str/bytes, bool/int, int/str e enum inválido não passam por conversão conveniente. Arrays viram tuplas internas por construção explícita do parser JSON/YAML de fronteira; isso não autoriza coerção de elementos. Não usar frozen como sinônimo de estrito. Registros antigos continuam validados pelos modelos antigos, sem retrofit.

Versões propostas: schema 1.0 para novos records; profile 1.0; algoritmo 1.0; catalogue 1.0 com seu SHA-256; engine gemmi/0.7.5 observado. Capturar application_version da distribuição molecular-platform instalada (ausência é configuração inválida), sem inventar Git SHA de build não fornecido. Registrar runtime_python no manifesto como versão observada; a versão da aplicação participa de request_key/manifesto, não de PlanBinding/plan_key ou PolicyRecord. Versionar independentemente do schema do 020. Campos de tempo novos são strings UTC no formato YYYY-MM-DDTHH:MM:SS.ffffffZ, validadas como data real, sem datetime ingênuo. Valores de origem CIF na auditoria são tokens/strings, sem float JSON.

SourceContext contém ids e quatro hashes/tamanhos dos snapshots documentais, raw_sha256/tamanho, schema/profile/parser da inspeção e modelo M. Não contém caminho absoluto nem URI escolhida como saída. PlanBinding contém esse contexto, S/U, X/O, máscaras/ações e versões científicas. application_version sai de PlanBinding e do PolicyRecord no draft-2: atualizar apenas a distribuição não invalida reconhecimento semântico se algoritmo/profile/catalogue/engine e plano permanecerem iguais. A versão observada continua no request_key e ManifestRecord. Qualquer mudança de regra deve alterar versão semântica/catalogue, não ficar escondida em patch de aplicação. PrivateParsedMaterialization é DTO próprio, não extensão de ParsedReceptorDocument.

PolicyRecord persiste o ato declarado, acknowledgements, declared_by/declared_at e plan_key/source_context. Manifest liga policy_id/hash dos bytes de policy.yaml, seleção/inspeção/ProteinInput, plan_key, request_key, engine/versões, hashes/tamanhos de receptor.cif e audit.json e created_at. Não contém hash de si mesmo nem campo running/failed/succeeded herdado de tautomerismo.

Audit contém todos os atom_site.id/ordinais fonte com keep/remove/motivo; ocorrências e origem S/D/U/X; X/O e reconhecimento; cada conexão com linha/id/hash/tipo/extremos/ação/motivo; categorias/tags/linhas omitidas e hashes dos tokens; advertências de perda, coordenações omitidas e source_symmetry_only. O hash de uma linha é do vetor canônico de pares tag/token em ordem canonicalizada; não é byte offset do arquivo. Tudo referente ao mesmo RAW/hash. Não armazenar traceback ou mensagens nativas livres na auditoria.

## 13. Canonicalização, ids e idempotência

H(payload)=SHA-256 do JSON UTF-8 com sort_keys=true, separators=(',',':'), ensure_ascii=false e allow_nan=false, sem LF final. Cada payload tem kind e version explícitos. JSON só usa null/bool/int/str/arrays/objetos; sem floats. Ordem das listas é definida pelo significado, não por sort_keys. Identificadores científicos não sofrem casefold ou alteração Unicode para hashing; eventuais mapas NFC são evidência de correspondência, preservando tokens fonte.

source_context_key=H({kind:'receptor-materialization-sources',version:'1.0',sources:SourceContext}). exclusions_key/outside_key e hashes dos vetores/linhas têm envelopes exatos no anexo SCHEMAS, inclusive para conjuntos vazios (o preview exibe hash, mas o acknowledgement é null quando conjunto vazio). plan_key=H(PlanBinding), incluindo U e hashes das ações de todas as categorias. Não inclui tempo, actor, UUID de staging ou strings de apresentação.

policy_id=H({kind:'receptor-materialization-policy',version:'1.0',plan_key,acknowledge_plan_key,acknowledge_exclusions_key,acknowledge_outside_key,declared_by}). Não inclui declared_at, gerado apenas no primeiro create-once. Declaração repetida retorna a política existente depois de verificar integridade e equivalência; preserva timestamp original. Timestamp ou edição externa não autoriza overwrite.

request_key e artifact_id são o mesmo H({kind:'receptor-materialization-request',version:'1.0',policy_id,policy_file_sha256,source_context_key,plan_key,profile,algorithm,catalogue_sha256,engine,application_version}). Todos ids técnicos são 64 hex lowercase. Não são identidade química nem deduplicação universal. show usa id técnico, não procura por nomes/latest/timestamps.

run recaptura fontes e plano e compara exatamente à política antes de reutilizar ou escrever. Metadado YAML semanticamente equivalente mas bytes alterados muda o snapshot e é recusado, não normalizado para reuse. Resultado existente só é reused se manifesto/arquivos/auditoria e vínculo forem válidos. Falta/corrupção gera erro de integridade, sem rebuild, overwrite, compensação do preexistente ou nova execução científica automática. Imutabilidade/create-once são pressupostos; não se promete detectar apagamento externo completo de todo histórico.

## 14. Layout e publicação concorrente

Novos caminhos sob scientific/, sem alterar roots do 020:

```text
scientific/receptor_materialization_policies/<policy_id>/policy.yaml
scientific/receptor_materializations/<artifact_id>/manifest.yaml
scientific/receptor_materializations/<artifact_id>/receptor.cif
scientific/receptor_materializations/<artifact_id>/audit.json
scientific/receptor_materialization_work/<uuid>/...
scientific/receptor_materialization_locks/policy-<policy_id>.lock
scientific/receptor_materialization_locks/artifact-<artifact_id>.lock
```

Criar diretórios compartilhados de forma idempotente, validando que sejam diretórios regulares sob o experimento, sem reparse. Nunca remover diretórios compartilhados na compensação. Work UUID v4 e nonce de propriedade não participam da identidade científica; colisão de nome existente provoca erro, sem reuso ou nova tentativa silenciosa.

Uma reserva por chave é criada com exclusividade real (xb), não exists+write. Registrar kind/key/nonce/identidade da tentativa; tamanho máximo 4 KiB. Existência de reserva sem resultado íntegro gera BUSY, sem wait/retry, expiração, roubo ou force-unlock. Resultado final já íntegro pode ser reused mesmo com reserva órfã; a operação não apaga essa reserva de outro dono. Staging de tentativas diferentes não é compartilhado.

Sob reserva, construir bundle completo em work privado no mesmo NTFS, fechar/flushear arquivos e verificar seus bytes/hashes/schema/plano antes de publicar. Diretório de política contém só policy.yaml; diretório de artefato só os três arquivos fixos. Extra arquivo/reparse é recusa de integridade no reader; não executar ou seguir conteúdo extra.

Ponto de commit: rename atômico do diretório preparado para o diretório final ausente, usando semântica Windows que recuse destino já existente. Nunca os.replace para destino científico. Revalidar identidades de ancestrais e staging antes da publicação. A reserva serializa writers cooperantes da mesma chave; não é defesa universal contra administrador adversarial. Não usar publish_staged_directory existente isoladamente como prova de concorrência. Uma política já declarada não é removida porque run falhou.

Se destino apareceu, validar contexto/bytes: equivalente e íntegro permite reused sem remover o vencedor; divergente/corrompido gera conflito/integridade. Se rename produzir resultado incerto, reconciliar identidade no destino; um destino não comprovadamente próprio nunca é apagado. Leitores ignoram work/locks e só reconhecem diretório final completo e íntegro. Nenhum YAML separado anuncia sucesso antes do arquivo.

Esta é atomicidade de visibilidade e exclusividade sob o perfil. flush/fsync não é promessa de persistência após falta de energia; crash pode deixar work/reserva órfãos. Não implementar limpeza automática ou daemon. Procedimento manual fora da CLI: (1) parar novos escritores e confirmar o encerramento de todos os processos envolvidos; (2) registrar chave, nonce, identidade, bytes da reserva/work e integridade do destino; (3) se houver processo ativo, identidade incerta, destino incompleto ou origem não comprovada, não remover; preservar evidência e investigar; (4) só o responsável, em intervenção externa expressa e com escritores suspensos, pode remover a reserva/work identificado após arquivar seu diagnóstico; (5) verificar novamente o destino antes de repetir a operação original. Isso não é autorização ao service para roubar lock, nem prova de que idade da reserva significa abandono. Não fornecer comando genérico de remoção recursiva. Diagnóstico apresenta apenas caminhos relativos controlados e propriedade conhecida; remoção manual externa não é parte do incremento.

## 15. Falhas, interrupções e atividade

Antes do commit, limpar somente arquivos/diretórios privados criados pela tentativa e cuja identidade/propriedade continue comprovada. Nunca remover RAW, registros 020, política existente, reserva alheia ou bundle preexistente. Limpeza que falhe preserva resíduos e erro primário; erro contém unconfirmed_removals relativos, não afirma remoção confirmada.

KeyboardInterrupt e SystemExit preservam mesma instância/código. finally ou captura BaseException somente em unwind de recursos próprios, com repropagação incondicional. Sem handler genérico que converta essas interrupções em falha científica. Após commit, nunca compensar artefato nem retry do writer por erro de apresentação/log.

Activity é registrada uma vez por operação pelo service, usando activity.record_activity e dataclass nova com command/status/ids/contagens/código fixo. CLI não duplica. Antes de o service ser chamado, CLI pode registrar seu erro de entrada como já fazem os comandos existentes; após delegar, não registra outra linha.

Falha de activity em sucesso pós-commit gera MaterializationPostCommitError, com committed=true, artifact_id/policy_id quando aplicável e causa de storage, exit 1. Resultado permanece publicado. Se já há erro primário, falha adicional de log é anexada como campo secundário e não o substitui. Em interrupção, tentativa de log/limpeza nunca troca KeyboardInterrupt/SystemExit por outro erro.

Se uma operação sem erro primário falhar ao limpar work/reserva próprios, não declarar limpeza confirmada: antes de commit, StorageError IO_ERROR em phase=cleanup; depois de commit, PostCommitError CLEANUP_AFTER_COMMIT, sem remover resultado. Se já houver erro/interrupção, anexar resíduos e preservar o primário. Não listar reserva alheia como remoção que a tentativa prometeu fazer.

Não existe registro persistido de tentativa universal nesta entrega. Reserva/work e erro estruturado explicam falhas pré-commit; manifesto final representa resultado publicado. Não anunciar estados não terminais como succeeded. A ausência de evento em crash não é prova de ausência de execução. Leitura/show nunca recompõe o bundle para fazê-lo parecer íntegro.

## 16. Taxonomia de erros e saída

Erros novos do domínio/service, com causas encadeadas por from quando aplicável e campos tipados (code, phase, ids, committed, unconfirmed_removals, secondary_activity_error). Nomes abaixo constituem proposta de API; não reutilizar classe de tautomerismo.

| Classe | Situações/códigos principais | Banner CLI |
|---|---|---|
| MaterializationInputError | INVALID_ID, MISSING_ACK, ACK_MISMATCH, SELECTION_CONFLICT, NONUNIFORM_ASYM, EMPTY_SELECTION, UNSUPPORTED_REQUEST | INPUT ERROR |
| MaterializationConfigurationError | INVALID_RECORD, IDENTITY_MISMATCH, SOURCE_CHANGED, CHECKSUM_MISMATCH, INCOMPLETE_INSPECTION, ENGINE_UNAVAILABLE, ENGINE_VERSION, UNSUPPORTED_PLATFORM | CONFIGURATION ERROR |
| MaterializationExecutionError | INVALID_CIF, LIMIT_EXCEEDED, UNSUPPORTED_CATEGORY/TAG/MODEL/SYMMETRY, UNSUPPORTED_NCS, AMBIGUOUS_ENDPOINT, UNSUPPORTED_PARTNER/TYPE, COVALENT_CUT, INVALID_OUTPUT | EXECUTION ERROR |
| MaterializationStorageError | IO_ERROR, UNSAFE_PATH, RESERVATION_BUSY, ID_CONFLICT, ARTIFACT_INTEGRITY | STORAGE ERROR |
| MaterializationPostCommitError | LOG_AFTER_COMMIT, PRESENTATION_AFTER_COMMIT, CLEANUP_AFTER_COMMIT, PUBLICATION_UNCERTAIN | STORAGE ERROR, com estado confirmado/indeterminado explícito |

Preflight opcional/host/ids ocorre antes de criar work. A ordem de validação principal é ids→host/engine→captura/vínculos→RAW/DOM/limites→seleção→reconhecimentos→publicação; dentro de uma etapa, ordem fonte/field order do schema. Não prometer um erro de cut quando o arquivo já falhou antes por simetria/modelo.

Handlers CLI não imprimem str(exc), traceback ou caminhos nativos/absolutos. Usar templates fixos, ids validados, contagens e índices fonte; valores CIF livres só em preview/auditoria JSON escapado, nunca concatenados em mensagem nativa. Não alterar sanitização/comportamento de outros comandos nem introduzir redator genérico de URLs/SMILES.

Exit code 0 para preview/declaração/run/show válidos, incluindo reused. Exit 1 para erros tratados. Interrupções propagam a semântica existente de Python/Typer. Sucesso completo só é renderizado após todas as leituras/verificações de apresentação necessárias; se falharem depois de commit, dizer que a materialização foi publicada e a apresentação falhou, identificar artifact/policy/input e sair 1 sem rerun/reload de tentativa ou nova compensação.

## 17. Serviços e comandos propostos

Funções públicas novas (project_dir é experimento resolvido): preview_receptor_materialization(selection_id,unaddressed_components); declare_receptor_materialization(selection_id,unaddressed_components,acknowledge_plan_key,acknowledge_exclusions_key,acknowledge_outside_key,declared_by); materialize_receptor_selection(policy_id); load_receptor_materialization_policy(policy_id); load_receptor_materialization_artifact(artifact_id). Cada comando chama sua função uma vez. Helpers privados podem compartilhar o mesmo planner; não duplicar ciência na CLI nem ler RAW por funções de inspeção.

```text
molecular receptor materialization plan <experiment> --selection <id> --unaddressed-components <preserve|require-disposition>
molecular receptor materialization declare <experiment> --selection <id> --unaddressed-components <preserve|require-disposition> --acknowledge-plan <hex64> [--acknowledge-exclusions <hex64>] [--acknowledge-outside <hex64>] --declared-by <name>
molecular receptor materialization run <experiment> --policy <hex64>
molecular receptor materialization show-policy <experiment> <policy-id>
molecular receptor materialization show <experiment> <artifact-id>
```

O argumento experiment conserva a resolução de identificador de experimento da CLI atual; não estender suporte a paths absolutos/GUI nesta tarefa. Ausência de acknowledge_exclusions/outside é None; não aceitar string null como reconhecimento. Não adicionar flags unsafe/force/ignore-connection, default científico U ou execução automática após declarar.

Preview imprime plan_key, source_context_key, M/S/U, X/O completos até o teto (sem truncamento silencioso), hashes de reconhecimento, contagens e warnings de perdas/conexões. Não imprime um comando declare já preenchido com acknowledgements que possa passar por consentimento automático. Cientista fornece os hashes após examinar o plano.

Declaração imprime Policy ID, Plan key, Protein input, Selection ID e reused quando verdadeiro. run/show apresentam Artifact ID, Policy ID, Protein input, Selection/Inspection IDs, Model, contagens antes/depois, SHA-256 e caminho relativo da estrutura/auditoria, além dos avisos de escopo amplo e coordenações omitidas. Nunca usar o título Prepared for docking.

## 18. Verificação da saída e auditabilidade

Reparse com Gemmi dos bytes gerados antes do commit. Comparar independentemente os vetores esperados do plano com as linhas atom_site reais, tokens dos campos preservados, ids/ordinais, contagens e relações do catálogo. Não basta writer e reader da mesma biblioteca aceitarem o arquivo. Campos gerados entry/block são os únicos ids novos dentro do mmCIF.

Receptor.cif e audit.json são UTF-8; não aplicar tradução de newline de arquivo de texto do sistema a bytes já serializados. Tokens de texto multilinha não são globalmente normalizados por replace. Não é exigida identidade byte a byte com o RAW: whitespace/tags omitidas mudam; tokens científicos preservados e hashes de arquivos são verificados separadamente. Espera-se determinismo do serializer para mesmo payload/pin/profile no host suportado; isso terá teste real, não foi demonstrado por este rascunho.

Ao carregar bundle, validar nomes fixos, não links, schema/campos fechados, artifact_id/request_key/caminho/id interno e hashes/tamanhos dos dois payloads. Verificar coerência dos resumos da auditoria com manifesto. show não precisa reexecutar RAW; integridade do bundle não certifica disponibilidade externa atual das fontes, que é conferida de novo apenas em run/reused. Sem checksum do próprio manifesto, não prometer assinatura/autenticidade contra edição coordenada maliciosa de todos os arquivos.

## 19. Checkpoints e allowlist proposta

| CP | Entrega | Cenários |
|---|---|---|
| 1 | Domínio/DTOs/planner, canonicalização, S/D/U/X/O e reconhecimentos | T021-001–040 e 159–161 |
| 2 | Adapter DOM, tokens, endpoints, simetria, catálogo/saída e validação | T021-041–090, 141–158, 162 e 164–173 |
| 3 | Leitores/snapshot/storage/registry/service, reserva/bundle/falhas | T021-091–120 e 163 |
| 4 | CLI/apresentação, integrações cumulativas e dependências opcionais | T021-121–140 |

Allowlist total proposta: novos src/molecular/receptor_materialization.py, receptor_materialization_storage.py, receptor_materialization_registry.py, receptor_materialization_service.py; adições em src/molecular/receptor_parsing.py e src/molecular/cli.py; novos tests/test_receptor_materialization.py, test_receptor_materialization_storage.py, test_receptor_materialization_registry.py, test_receptor_materialization_service.py; adições em tests/test_receptor_parsing.py e tests/test_cli.py; fixtures novas somente em tests/fixtures/receptor_materialization/. Não alterar atomic.py, registries/modelos do 020, activity.py, pyproject.toml ou módulos de ligantes/tautômeros. Helpers novos de storage devem provar suas garantias, não copiar código sem teste.

CP1: primeiro módulo/teste novos; CP2: adapter/testes/fixtures e ajustes do módulo novo necessários a DTOs do adapter; CP3: storage/registry/service e seus testes, fixtures de I/O; CP4: CLI/testes e correções restritas aos novos módulos quando revisão exigir. Nenhum checkpoint está autorizado por esta tabela. Testes existentes fora da allowlist podem ser executados, não editados.

## 20. Matriz individual de comprovação

SCENARIOS_021.csv enumera **173 cenários**: CP1=43, CP2=79, CP3=31 e CP4=20. Os 163 IDs do draft-2 são preservados; T021-162 passa de CP1 a CP2 e há dez novos casos de CP2 (T021-164–173), com id/CP/alvo/estímulo/resultado. São cenários, não promessa de 173 funções ou itens pytest. Parametrizações de interrupção/falha por fase podem produzir mais itens; contar funções, casos e itens na implementação e explicar skips. Nenhum cenário foi executado por esta redação.

Casos que dizem por fase devem enumerar captura, parsing, plano, serialização, verificação, reserva, publicação e apresentação; KeyboardInterrupt e SystemExit têm provas separadas. Usar produção real nas integrações; mocks somente para injetar a falha na fronteira correta. Não pytest.raises(Exception), não fixtures de checksum fictício, não snapshot/diff de attempts.

CP2 deve usar Gemmi 0.7.5 real. CP3 exige Windows 11/NTFS e dois processos reais disputando a mesma chave, destinos preexistentes intactos, reparse points quando tecnicamente disponível e falhas por fase. Skips Linux não provam o gate Windows. Fixtures positivas precisam de coordenadas/categorias/operadores suficientes; a amostra 020 mínima e a sonda C++ de tokens não provam materialização.

Regressão cumulativa: 017, promoção 018, condições 019 e receptor 020 preservados; imports/help sem opcionais; git diff --check e allowlist. Contagens históricas de testes não são reexecução. Critérios de aceitação só podem ser satisfeitos por evidência de implementação real posteriormente.

## 21. Rastreio P-1–P-5 e NOTE-F1

| Item | Solução proposta | Local de prova |
|---|---|---|
| P-1 | Complemento de cadeias vira explícito apenas com hash reconhecido X | §8; T021-021–024 |
| P-2 | Reconhecimento obrigatório de O não vazio, com snapshot/plan e recusa de mismatch | §8/13; T021-025–028/038/103 |
| P-3 | Uniformidade por modelo/asym de todo não polímero, não só branched | §7; T021-016–020 |
| P-4 | Mesma isometria não é impossibilidade; matriz de 15 células, contexto fonte fechado | §10; T021-045–059 |
| P-5 | Catálogo anexo por tags/chaves/referências/ações e testes | §11; T021-061–090 |
| NOTE-F1 | Bytes únicos, hash antes de UTF-8/newline/YAML e paths/id reais | §5; T021-091–096 |

Os pareceres independentes anteriores fecharam os achados do estudo e do draft-1 no nível de proposta. Nesta candidata, MINOR-N1/N2 ainda aguardam fechamento focal; os critérios de aceitação da implementação continuam pendentes de prova nos checkpoints.

## 22. Evidência da redação e revisão seguinte

Conferidos refs/identidades e código pinado; consultados binding/fonte Gemmi e documentação oficial wwPDB. As assinaturas de DOM foram verificadas estaticamente, não executadas. A sonda anterior de namespace não é teste de Gemmi. Nesta redação não houve instalação, pytest, transformação científica, teste Windows ou concorrência. No draft-1 houve verificações documentais/hash/AST. No draft-2 houve conferência de identidades/fontes e recomputação de cobertura de catálogo sobre os inventários do revisor, não novo parsing CIF. Nesta candidata houve apenas conferência de inputs, precedência documental, pares, projeções canônicas, contagens e preservação das regras. O patch documental não implementa o materializador.

Fontes: estudo v1/complemento/reconciliação/revisão focal e aprovação nos commits da §1; receptor_* / inputs.py / registry.py / atomic.py / activity.py / CLI e testes na baseline; Gemmi python/read.cpp, python/cif.cpp, docs/cif.rst e src/mmcif.cpp no pin; páginas oficiais wwPDB de struct_conn, tipos/inserção/simetria, entity/branch/schemes e anisotrop. O documento histórico increments/021/06-draft-specification/evidence/SOURCE_AND_INPUT_IDENTITIES.json registra links e hashes no seu snapshot; os inputs desta candidata estão em ../11-draft2-reconciliation/evidence/CANDIDATE_DOCUMENT_CHECKS.json. Nenhuma preferência é apresentada como capacidade já implementada.

Próximo gate: revisão focal desta candidate-1 e anexos por Claude revisor separado do implementador, restrita a MINOR-N1/N2, NOTES e regressões concretas decorrentes. Publicar parecer em caminho novo. O revisor pode apontar mudanças necessárias; não alterar este rascunho, código ou STATUS. O parecer independente do draft-2 fecha os 3 MAJORs e 6 MINORs anteriores no nível do rascunho. Esta candidata responde somente aos novos MINOR-N1/N2 e incorpora as NOTES; a aceitação pelo arquiteto não encerra essas duas correções independentemente. Após revisão/reconciliação, só o responsável decide promoção/congelamento/autorização de checkpoint, em mensagens próprias. Não há relay automático.


## 23. Fixtures reais e regressão específica do draft-2

Em CP2/CP4, cada caso positivo D-01(b) exige fixture com lineage de uma entrada real: origem/commit ou URL/data/checksum, seleção M/S/D/U e resultado esperado atômico/conexões. Se houver recorte ou edição para isolar metal–água ou pares hydrog, identificar todas as alterações em manifesto de fixture; não chamar o exemplo editado de depósito intacto. Preservar o original/hashes e testar também a versão real não editada quando suportada. Não basta adicionar artificialmente tabelas de operadores aos exemplos.

5i55, 1pfe e 3dg1_final são amostras de cobertura, não três materializações positivas prometidas. Todos devem passar a checagem documental de categorias/tags após as mudanças; 1pfe ainda deve recusar no gate de simetria 1_555/9_555. 5i55/3dg1_final só se tornam provas operacionais quando o adapter/seleção efetivamente rodarem. No gate CP2, exigir ao menos uma entrada real NMR multi-modelo, uma EM e uma com struct_ncs_oper, todas com origem/checksum/lineage. Para NCS, o resultado pode ser a recusa esperada de generate ou a omissão auditada de given/identidade, conforme os bytes reais; não prometer sucesso para entrada que deve recusar. NMR/EM devem mostrar perda de metadados auditada e M explícito, sem afirmar conformer representativo ou qualidade experimental do recorte. Amostras com edits de isolamento preservam o original e enumeram as alterações. A cobertura atual dessas famílias é documental, não execução comprovada em arquivo real.

As linhas T021-001–163 e seus IDs permanecem rastreáveis; T021-162 conserva o mesmo cenário e apenas muda para CP2, coerente com §23 e sua integração posterior no CP4. Cenários que antes dependiam da regra restritiva antiga de 1_555 ou do campo application_version no plano devem ler a expectativa conforme esta versão; o CSV registra a alteração explicitamente. Os novos T021-141–163 cobrem a reconciliação, sem alegação de execução científica.

FINAL CANDIDATE PREPARED: YES
READY FOR INDEPENDENT CANDIDATE FOCAL REVIEW: YES
READY FOR OWNER FREEZE DECISION: NO
READY FOR IMPLEMENTATION: NO
FINAL SPECIFICATION FROZEN: NO
CODE REPOSITORY MODIFIED: NO
