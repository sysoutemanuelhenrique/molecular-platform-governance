# Reconciliação arquitetural — estudo do Incremento 021

Data: 23/11/2026, America/Sao_Paulo. Autor: Codex, arquiteto. Tarefa: `021-STUDY-RECONCILIATION`.

Natureza: resposta arquitetural ao parecer de Claude sobre o estudo v1 e o complemento. Este documento não é especificação final, implementação, aprovação do responsável ou fechamento independente. Preserva todos os documentos confrontados.

## 1. Snapshot e identidades

Os gates remotos coincidiram com o comando do responsável antes do trabalho:

| Referência | SHA |
|---|---|
| Governance, `docs/020-a-candidate1-review-20261020` | `f1656badb35a67942b8318b6f6744b0c71f01de6` |
| Parecer, `claude/021-study-review-v2-20261123` | `debeba6f4370c6f5dd77d2273420abf8a828e9f8` |
| Código, main | `08b797e0985e123ffd4d7ca7e5a5e8f040e63851` |
| Main do governance, preservada | `a47183dfec8213c765ed43ae482c8c227760a3d5` |
| Gemmi, tag 0.7.5 | `5cc1c23c6007e0e6cbd69289c6f7c0bff50e943e` |

Identidades reconferidas: estudo v1, 365 linhas/55.594 bytes/SHA-256 `5048c5012548ee1169f58e6bb644ecf8b5d76a59c6569400d67db0987f7dfa56`; complemento, 157/20.979/`f5e407704e9b104e7ba224f750c3bbcebd8b109ab26016b48442087d897e9b5f`; parecer, 198/20.580/`649c67b0f72186504a083d6041b53d7f5becf8d4f27ac89c1885c5a32843708e`; referência congelada 020, 1.975/210.880/`cf6cb534f9267d51e718052c7b36a2293c522bc566c99cf3bb2ef5909385a0a6`.

Os 66 blobs locais de referência foram novamente comparados à árvore Git remota da baseline, incluindo todos os arquivos Python, cuja sintaxe foi analisada por AST. Isso comprova a identidade dos arquivos lidos, não execução da aplicação ou da suíte. As instruções AGENTS, protocolo, STATUS e tarefa foram lidas no snapshot indicado. A referência normativa do 020 foi preservada; foram relidas as passagens pertinentes, especialmente §34.

Legenda: **F** fato observado; **I** inferência; **R** recomendação; **D** decisão pendente do responsável. Fontes permanentes e método estão na seção 14 e nas evidências anexas.

## 2. Resultado e disposição geral

O parecer contém 0 BLOCKERS, 4 MAJORS, 5 MINORS e 3 NOTES. As correções C-1/C-2/C-3 não são contadas novamente como achados adicionais. O veredito do revisor foi favorável ao rascunho, condicionado à absorção dos MAJORs; não foi aprovação de um recorte fechado.

**R — manter o perfil mínimo de B**, no referencial do modelo fonte, mmCIF, todas as alternativas conformacionais preservadas, sem expansão de assembly e sem preparo químico. Rever a recomendação anterior de recusa indiferenciada de todos os cortes: recomendo a opção **(b)** limitada da seção 3 e o alcance de componentes explicitamente declarado da seção 4.

| Item | Disposição do arquiteto | Dependência remanescente |
|---|---|---|
| MAJOR-1 | Aceito; proposta (b) com tipos fechados, condições e auditoria | Escolha D-01 do responsável + confronto focal |
| MAJOR-2 | Aceito quanto à lacuna; tabela completa proposta | Escolha D-02 sobre alcance; ressalva sobre auth_asym_id + confronto focal |
| MAJOR-3 | Aceito quanto a tokens/colunas/ptnr3/modelo; parcialmente aceito quanto à equivalência de simetria | Confronto focal da solução e do limite conservador |
| MAJOR-4 | Aceito; leitor próprio do 021 para bytes e modelos fixados | Confronto focal de compatibilidade e garantias |
| MINOR-1 | Aceito para cadeia mantida; esclarecido para cadeia inteira removida | Conferência focal |
| MINOR-2 | Aceito; branched tudo-ou-nada por asym/modelo | Conferência focal |
| MINOR-3 | Aceito; plano de catálogo ampliado | Catálogo por campo no rascunho |
| MINOR-4 | Aceito; qualquer parser-limitation bloqueia o perfil inicial | Conferência focal |
| MINOR-5 | Aceito; proposta agrupada não é matriz normativa | Enumeração individual no rascunho |
| NOTE-1 | Incorporada como limite de evidência | Binding/Windows só nos checkpoints próprios |
| NOTE-2 | Incorporada como precedente, não garantia suficiente | Protocolo e prova de publicação no CP3 |
| NOTE-3 | Incorporada; declaração e execução separadas | Ergonomia CLI no rascunho |
| C-1 | Aceita a inconsistência; explicação de falso positivo reproduzida | Errata nova; histórico não reescrito |
| C-2 | Confirmada por código e fontes primárias | Limitação conhecida, sem corrigir o 020 nesta etapa |
| C-3 | Confirmada; report.chains inclui asyms não poliméricos | Tabela usa entity.type da fonte |

Nenhum item desta tabela está declarado fechado independentemente. O documento responde tecnicamente; o revisor ainda pode contestar a resposta e duas escolhas de escopo dependem do responsável.

## 3. MAJOR-1 — cortes e tipos de conexão

**F:** os baldes de água/metal percorrem todo o inventário e precedem entradas nomeadas; não recebem uma lista de cadeias selecionadas. **I:** portanto, os três contraexemplos do revisor decorrem da composição dessas regras: água removida/metal mantido; cadeia polimérica removida/metal mantido; ligante removido/metal mantido. A recusa indiferenciada anterior limitaria casos usuais possíveis, mesmo sem medir sua frequência no arquivo PDB.

**F:** o dicionário oficial diferencia ligação covalente, ponte dissulfeto, ligação de hidrogênio e coordenação metálica. A categoria de conexão do relatório 020 não deve substituir o conn_type literal: o 020 coloca tipos diferentes de disulf/metalc em seu balde covalent. O novo leitor deve consultar os tokens brutos. Não é necessário alterar a classificação antiga para decidir o novo tratamento.

**R — opção (b), com alcance deliberadamente restrito:**

| Extremos após o plano | Tipo literal reconhecido | Resultado proposto |
|---|---|---|
| Ambos retidos | Tipo suportado e contexto inequívoco | Preservar linha e tokens; validar referências |
| Ambos removidos | Identidades conhecidas e exclusão comprovada | Omitir com motivo e linha/hash fonte na auditoria |
| Exatamente um retido | covale, covale_base, covale_phosphate, covale_sugar, modres ou disulf | Recusar; não capear nem reparar |
| Exatamente um retido | metalc ou hydrog | Omitir apenas se o parceiro sair como parte de componente/asyms integralmente excluídos por decisão explícita suportada; auditar |
| Exatamente um retido | metalc/hydrog com retirada parcial, ambiguidade ou sem decisão explícita | Recusar |
| Tipo não coberto, desconhecido ou nulo que afete o recorte | Qualquer outro | Recusar no perfil inicial; não inferir que é interação não covalente |

O conjunto covalente é uma lista declarada, não regex covale* que aceite extensões desconhecidas. O dicionário também define saltbr e mismat; não são adicionados à exceção de metalc/hydrog sem decisão específica. Comparação pode reconhecer a natureza ucode do tipo; o token original permanece na saída/auditoria.

Na opção proposta, remoção de água íntegra por water_disposition=remove permite omitir sua coordenação metalc com metal mantido. Remoção parcial de átomos da água não é permitida. Um ligante removido inteiro permite omitir metalc, mas uma ligação covale ligante–proteína ainda causa recusa. A origem e a abrangência da remoção são verificadas antes de invocar a exceção; a CLI não oferece um botão genérico ignorar ligação.

Omitir uma coordenação declarada não equivale a demonstrar estabilidade do metal remanescente. A auditoria e a apresentação devem avisar sobre as coordenações/interações omitidas e dizer que não houve reconstrução do ambiente químico. O resultado continua sendo estrutura derivada, não receptor preparado para docking.

**D-01 — pendente:** escolher (a), recusa de todo corte com cobertura limitada explicitamente documentada, ou (b), esta distinção auditada. Recomendo **(b)** por permitir extrações úteis sem tratar coordenação como corte covalente. Se (a) for escolhida, os três exemplos acima serão recusas esperadas, com conexão e causa identificadas; nenhuma extensão será introduzida silenciosamente.

## 4. MAJOR-2 e C-3 — universo e tabela de precedência

**F:** `_build_chains` agrupa todos os resíduos por modelo/label/auth, sem filtro polymer. `NonPolymerComponent` não traz model_number; portanto, sua resolução não fornece uma decisão independente por ocorrência/modelo. **R:** projetar a decisão efetiva sobre as ocorrências do modelo fonte selecionado, sem aplicar a saída a outros modelos ou reinterpretar a precedência do 020.

Definições propostas: M é o modelo resolvido; S indica label_asym_id explicitamente listado em resolved_chains; D é a disposição efetiva keep/remove, quando presente para a chave confirmada; U é o complemento explícito preservar não abordados ou exigir cobertura. O tipo contextual vem do vínculo atom_site → struct_asym → entity.type, não do fato de a linha ter sido apresentada como cadeia pelo 020. Nenhum tipo novo é gravado no relatório antigo.

Pré-condições: vínculo inequívoco da ocorrência, ids nativos compatíveis e ausência de parser-limitation. Tipo/contexto desconhecido ou contraditório relevante ao recorte provoca recusa; HETATM não substitui o vínculo de entidade. Modelo ausente não é automaticamente 1 no novo perfil: o primeiro perfil deve recusar ausência/nulo/mistura de model_num que impeça a correspondência explícita; essa restrição adicional do consumidor deve ser anunciada, sem editar o comportamento do 020. Zero não é convertido para 1; o perfil suporta apenas modelos compatíveis com os registros do 020.

| Contexto | S | D | U | Resultado proposto |
|---|---:|---|---|---|
| Fora de M | qualquer | qualquer | qualquer | Excluir por modelo; não produzir outro modelo |
| Polymer em M | sim | ausente ou keep | qualquer | Incluir cadeia inteira e todos os altlocs |
| Polymer em M | sim | remove de componente/resíduo da cadeia | qualquer | Recusar; não retirar resíduo, inclusive terminal |
| Polymer em M | não | ausente ou remove | qualquer | Excluir cadeia inteira; remove de resíduo não executa uma edição parcial |
| Polymer em M | não | keep de componente/resíduo da cadeia | qualquer | Recusar conflito explícito; não ignorar keep nem reintroduzir cadeia silenciosamente |
| Não polímero/water/macrolide em M | sim | ausente ou keep | qualquer | Incluir asym por seleção explícita; ausência de D não é falta de decisão |
| Não polímero/water/macrolide em M | sim | remove | qualquer | Recusar conflito seleção explícita versus disposição efetiva |
| Não polímero/water/macrolide em M | não | keep | qualquer | Incluir componente inteiro; alcance amplo explicitamente assumido |
| Não polímero/water/macrolide em M | não | remove | qualquer | Excluir componente inteiro |
| Não polímero/water/macrolide em M | não | ausente | preservar não abordados | Incluir componente inteiro com origem da decisão U |
| Não polímero/water/macrolide em M | não | ausente | exigir cobertura | Recusar até existir decisão explícita |
| Branched em M | qualquer | combinações por ocorrência | qualquer | Aplicar base não polimérica e exigir resultado uniforme do asym inteiro; mistura incluir/excluir ou conflito provoca recusa |
| Tipo/contexto não suportado em M | qualquer | qualquer | qualquer | Recusar antes de publicar |

Em polymer, a seleção de cadeia já cobre resíduos comuns/modificados; U não autoriza recolocar uma cadeia excluída. Um remove efetivo sobre resíduo modificado só é redundante e aceitável quando a cadeia inteira já sai por seleção; ele não permite editar uma cadeia mantida. Para branched, NAG removido/BMA mantido no mesmo asym é recusa, mesmo que a ligação glicosídica interna não apareça em struct_conn.

**R — alcance explícito dos componentes:** os baldes continuam amplos, no modelo fonte escolhido. A política de materialização deve registrar que componentes mantidos por D/U podem ter label_asym_id fora da lista S. Não reduzir o balde por proximidade geométrica ou auth_asym_id. Uma escolha de cadeia polimérica não significa automaticamente selecionar seu entorno.

O relatório deve enumerar essas retenções por label_asym_id, entity_id, CCD/ocorrência e motivo (S/D/U), com contagens e auth_asym_id fonte quando disponível. Deve indicar se o auth id coincide com algum polímero retido, só com polímeros excluídos, com vários ou com nenhum. Isso é comparação de identificadores, não atribuição de propriedade ou de interação biológica. O dicionário define auth_asym_id como identificador alternativo do autor; não certifica que uma água ou ligante pertence cientificamente a uma cadeia.

**D-02 — pendente:** recomendo preservar o alcance amplo, com reconhecimento explícito e auditoria de todos os componentes retidos fora de S. Alternativa mais restrita: exigir seleção explícita por label para todo componente retido fora das cadeias poliméricas selecionadas, recusando os demais. Não recomendo a regra auth_asym_id diferente = remover/recusar como se fosse prova de pertencimento biológico.

Exemplo: polímero A selecionado, B excluído, metal Z kept pelo balde. A proposta retém Z com origem D e aviso de alcance, mesmo que seu auth id coincida com B. Se a conexão de Z com B ficar cruzada, aplica-se D-01: (a) recusa; (b) metalc pode ser omitida quando B sai integralmente por seleção explícita, com auditoria e aviso químico. Nenhuma dessas escolhas já foi aprovada pelo responsável.

## 5. MAJOR-3 e C-2 — conexões a partir do RAW

**F confirmado:** a baseline lê ptnr1_PDB_ins_code/ptnr2_PDB_ins_code, enquanto o dicionário, o reader oficial do Gemmi e a amostra 5i55 usam pdbx_ptnr1_PDB_ins_code/pdbx_ptnr2_PDB_ins_code. Os testes receptor examinados não contêm a coluna canônica. O parser usa colunas opcionais e retorna ausência, o que pode perder o código de inserção. A amostra 5i55 tem os campos, mas seus valores de inserção/terceiro parceiro nesse registro são nulos: ela comprova a grafia, não uma frequência de falhas ou um terceiro parceiro efetivamente preenchido.

**R:** novo caminho do 021 lê atom_site e struct_conn dos mesmos bytes verificados, diretamente pelo DOM. Não usar ParsedConnection, `_STRUCT_CONN_COLUMNS` ou o snapshot de conexões do relatório como fonte suficiente de correspondência. A inspeção permanece autoridade da referência e da seleção; o RAW verificado é a fonte dos tokens estruturais necessários à nova operação.

Quando essa leitura expuser o código de inserção que não consta do relatório antigo, registrar a origem RAW e a limitação conhecida; não atualizar a inspeção, recomputar seu conteúdo como reparo ou fingir que o campo foi originalmente confirmado pelo 020. O vínculo ao mesmo checksum e os campos usados pelo 021 precisam permanecer verificáveis na auditoria.

Chave/contexto a detalhar no rascunho: modelo M + label_asym + label_comp + label_atom + label_seq quando informado + altloc; auth_seq/auth_asym e código de inserção canônico desambiguam ocorrências não poliméricas com label_seq nulo. Não cruzar espaços label/auth por adivinhação. Um endpoint pode ser aceito somente quando suas restrições informadas convergem para uma ocorrência atômica inequívoca. Nulo/desconhecido não é wildcard que permita escolher o primeiro candidato. Endpoints insuficientes ou contraditórios causam recusa.

`ptnr1_label_entity_id` não deve ser exigido como coluna padrão: a relação de entidade deve vir das linhas atômicas e de struct_asym. O reader novo deve usar os nomes de coluna efetivamente definidos, incluindo os códigos de inserção e altlocs, preservando extensões/aliases apenas quando uma política explícita os suportar. Aspas e marcadores de ausência continuam distintos.

Terceiro parceiro: aceitar presença de colunas pdbx_ptnr3_* se todos os seus valores forem marcadores nulos reais; qualquer valor textual/não nulo torna a linha não suportada no perfil mínimo. A cadeia citada '?' não é marcador nulo. Não projetar uma conexão ternária em duas por conveniência. O catálogo deverá dizer se a recusa abrange todo o arquivo ou apenas uma linha comprovadamente relevante; recomendação inicial conservadora: recusar a materialização com terceiro parceiro preenchido, sem tentar avaliar seu efeito parcialmente.

Modelo: a categoria struct_conn consultada não possui uma coluna padrão de modelo. Avaliar a correspondência no M explicitamente selecionado, não no primeiro modelo nem pela união de todos. Endpoint inexistente/ambíguo em M não é automaticamente não aplicável: recusar a linha relevante; não apagar a referência para obter saída válida. Coluna estendida de modelo só pode ser aceita por perfil que a reconheça, não ignorada silenciosamente.

### Ressalva sobre simetria

**Aceito parcialmente.** O Gemmi compara os dois códigos conhecidos para classificar Same/Different ASU. Isso confirma que testar isoladamente endpoint diferente de 1_555 é simplista. Porém, igualdade das strings é uma classificação relativa, não demonstra por si só que a representação escolhida contém os parceiros nem valida operadores desconhecidos. O reader verifica primeiro se os dois campos estão presentes e não nulos.

**R:** para conexão que afetará o recorte, exigir contexto simétrico conhecido. Códigos distintos, ausentes/desconhecidos ou que dependam de imagem não materializada são recusados no perfil inicial. Dois códigos não identidade iguais não serão aceitos apenas por igualdade textual: a opção conservadora é recusá-los com diagnóstico, até existir demonstração explícita de equivalência no referencial fonte. Aceitar identidade exige interpretação coerente com o operador declarado, não presumir universalmente que qualquer índice 1 representa matriz identidade. Essa restrição é uma preferência de perfil justificada pelo escopo sem expansão, não uma afirmação de que a representação fonte esteja errada.

O rascunho deve fechar os códigos/contextos aceitos e fixtures de operadores, incluindo o caso de iguais não identidade e de ausência em apenas um ou ambos os lados. A recomendação do revisor de igualdade relativa permanece útil como dado, sem virar uma garantia de materialização completa. Esse é um ponto específico de confronto focal.

## 6. MAJOR-4 — leitura única de metadados e identidade exata

**F:** os loaders públicos atuais retornam só modelos Pydantic após read_text/yaml/model_validate. Hashear antes/depois por outro open não é o mesmo snapshot documental. A recomendação anterior de usar exclusivamente esses loaders e simultaneamente hashear a mesma leitura era inconsistente. Aceito o achado.

**R — escolher (i), leitor próprio do storage 021:** validar o id solicitado com a autoridade lexical existente; derivar caminho fechado do tipo de registro; capturar bytes uma única vez sob os controles de contenção/identidade necessários; calcular hash desses bytes; decodificar e validar com os modelos schema 1.0 existentes, sem alterar os loaders ou os schemas do 020. Retornar um contexto interno com modelo validado e hash/proveniência da captura. Nenhuma segunda leitura de metadados deve ser usada para fabricar a mesma proveniência.

Para cada objeto, comparar o id interno exatamente, com caixa, ao id solicitado/referenciado: ProteinInput.id, inspection.inspection_id, policy.selection_id e resolution.resolved_selection_id. Conferir também os vínculos cruzados e o policy_selection_id correto da resolução, que no schema 1.0 deve ser igual a resolved_selection_id. Esses são os nomes reais da baseline, não campos novos input_id/selection_id inventados para os dois modelos. A abertura de A.yaml no NTFS não prova que o registro interno A corresponde a um pedido a. Casefold é disciplina de armazenamento, não igualdade científica.

Esta solução não altera o contrato público de leitura do 020; usa a forma schema 1.0 que o §34 permite consumir e explicita uma captura adicional necessária ao novo consumidor. Não apresentar a API existente como modificada ou o leitor novo como já implementado. A inclusão permanece nos novos módulos de storage/registry do 021, dentro da allowlist proposta.

Uma leitura de cada registro não é transação simultânea de todos os arquivos. Após capturar, validar vínculos/ids/hashes da composição; nenhuma procura latest ou substituição silenciosa. Em retry, comparar o contexto fixado e verificar o bundle existente. Registro que mudou externamente não autoriza sobrescrever resultado ou recalcular a seleção para fazê-la caber na chave antiga.

O RAW segue captura própria para proteínas, com checksum dos mesmos bytes entregues ao parser, sem herdar o padrão de reabrir o caminho em checksum/parser/CIF. Reparse da saída para verificação usa bytes da saída produzida, não uma nova inspeção do RAW.

## 7. MINORs — respostas e soluções

**MINOR-1 — aceito com delimitação.** Em cadeia polimérica mantida, qualquer remoção de resíduo modificado, inclusive terminal, é recusada. Se a cadeia inteira é excluída pela seleção, suas linhas saem juntas e uma disposição remove não executa remoção de resíduo isolado. Disposição keep conflitante em cadeia excluída provoca recusa conforme a tabela, em vez de resgatar átomos isolados. Isso evita a leitura literal que impediria excluir uma cadeia inteira por conter MSE removível.

**MINOR-2 — aceito.** Branched deve ser tudo-ou-nada por modelo/label_asym_id. Não depender exclusivamente de struct_conn para detectar ligações internas: usar entity.type e preservar, filtrar ou recusar os vínculos das categorias branch conforme catálogo. NAG remove/BMA keep no mesmo asym provoca recusa mesmo sem struct_conn. Conflitos não serão resolvidos pelo algoritmo escolhendo o maior fragmento.

**MINOR-3 — aceito.** O rascunho deve classificar explicitamente as categorias abaixo; a tabela é proposta de tratamento por família, não um catálogo de colunas já congelado:

| Família | Tratamento arquitetural proposto |
|---|---|
| atom_site/anisotrop, struct_asym, entity, entity_poly/seq, esquemas poly/nonpoly/branch e chem_comp necessários | Preservação filtrada por identidades sobreviventes e checagem de referências; incapacidade de tratar campo obrigatório suportado causa recusa |
| pdbx_entity_branch* e vínculos internos de glicanos | Preservar relações do asym completo ou excluir o grupo completo; sem poda parcial |
| struct_conn/struct_conn_type e atom_type | Filtrar referências/tipos efetivamente usados; aplicar a política de conexões; não gerar tipo/ligação ausente |
| struct_conf, struct_sheet_range, struct_mon_prot_cis, struct_site/struct_site_gen | Omitir no perfil mínimo com auditoria de perda, salvo quando o catálogo fechado aprovar preservação por chave; não deixar referências stale |
| pdbx_struct_mod_residue e unobs/zero_occ | Propor preservação filtrada do contexto mantido; declarar a semântica de ausências, sem inventar coordenadas |
| pdbx_struct_special_symmetry e instruções assembly/NCS | Sem copiar instruções acionáveis incompatíveis; auditar omissão e recusar quando o recorte depender delas para interpretar conexões/átomos |
| pdbx_validate_* e validações do depósito | Omitir com auditoria; não atribuir ao derivado uma validação experimental que não foi refeita |
| Categoria desconhecida/referências não interpretáveis | Decisão explícita do catálogo entre omissão auditada permitida e recusa; nunca inferir inocuidade pelo nome |

Para todo tratamento preservado, especificar tags, chave, regra de filtro, relações e teste. Omitir anotações não faz do arquivo um depósito experimental novo, e preservar o RAW não dispensa as referências corretas do derivado. O catálogo completo continua condição para autorizar o writer, não decisão delegada ao implementador.

**MINOR-4 — aceito.** Recusar o perfil quando houver qualquer warning parser-limitation, sem usar selection_capability=full como certificado de completude. Não permitir ignorar o warning por ele vir de categoria aparentemente não selecionada enquanto não houver prova de cobertura adequada. Essa limitação do consumidor não modifica a inspeção existente.

**MINOR-5 — aceito.** Os 48 números agrupados do estudo não serão promovidos automaticamente para testes normativos. O rascunho deve enumerar cenários individualmente e registrar substituições; os casos novos de precedência, inserção, tokens, simetria e leitores não cabem numa promessa de manter exatamente 48 itens. Contagem de cenários, funções e parametrizações será reconciliada sem inventar coleta pytest.

## 8. Correções factuais e NOTES

**C-1 — inconsistência aceita e explicação reproduzida.** O JSON antigo tem gemmi_available=true, enquanto o texto diz não instalado. A sonda atual, sem importar/executar Gemmi, encontrou: nenhuma distribuição Gemmi registrada no ambiente neutro; nenhum spec no contexto neutro; mas um spec de namespace, sem loader/origin, ao consultar o diretório do script histórico, que contém a pasta de fontes gemmi. Logo find_spec(...) is not None não comprova instalação nem binding funcional. Aquele método podia produzir exatamente esse falso positivo.

Errata: a disponibilidade de um engine/binding Gemmi não foi demonstrada pelo estudo v1; seu booleano não deve ser citado como instalação funcional. A presente reprodução não restaura o estado completo do ambiente de 21/11; a versão/distribuição histórica permanece não comprovada. O estudo não produziu evidência de execução científica, e esta reconciliação também não a produz. Não substituir o booleano antigo nem afirmar retroativamente que um wheel definitivamente existia/não existia. Ver evidence/ENVIRONMENT_EVIDENCE_CORRECTION.md.

**C-2 — confirmada, limitada.** A grafia das colunas diverge e falta a fixture canônica nos testes consultados. Isso não autoriza correção do 020 sob esta tarefa nem comprova que todo arquivo real tenha perdido informação: o efeito depende de código de inserção informado. A nova operação lê a coluna canônica diretamente. Não reabrir o contrato do 020, que não especifica essa grafia, nem vender a ausência do campo como ausência de inserção.

**C-3 — confirmada.** A lista chains é mais ampla que polímeros. A tabela da seção 4 substitui essa suposição do estudo por contexto de entidade explícito, sem editar o texto histórico.

**NOTE-1 — incorporada.** A sonda C++/saída do revisor foi lida como evidência fornecida. Ela não foi reexecutada pelo arquiteto, nem valida Python/Windows/materialização. Permanecem os gates CP2/CP3 e a proibição de quote sobre tokens brutos já citados.

**NOTE-2 — incorporada.** open(..., xb) e os.link exclusivos existem no snapshot de ligantes. São precedentes úteis; não demonstram que uma reserva de longa duração, bundle ou recuperação já exista. O registry do 020 continua check-then-write e os.replace; sua docstring create-once não é mutex nem primitiva segura para concorrência nova. Q-06 exige protocolo próprio e teste Windows real.

**NOTE-3 — incorporada.** Manter declaração e execução como operações separadas e uma entrega vertical útil. Nenhum scaffolding vazio ou interface genérica futura foi criado.

## 9. Q-01–Q-09 após a resposta

| Q | Situação arquitetural |
|---|---|
| Q-01 | Perfil mínimo B continua recomendado; o revisor já o considerou defensável; nenhuma implementação é autorizada |
| Q-02 | Recomendar D-01(b), com limites e tipos da seção 3; aguarda decisão expressa |
| Q-03 | Famílias e critérios ampliados; catálogo de tags/relações ainda deve ser fechado no rascunho |
| Q-04 | Duas operações de serviço mantidas; fachada CLI não é prioridade de escopo |
| Q-05 | Captura documental própria e comparação exata; canonicalização/chave e retry serão detalhados no rascunho |
| Q-06 | Reserva e bundle continuam proposta; não há protocolo de publicação testado ou congelado |
| Q-07 | Preferência inicial por reserva diagnosticável + erro estruturado + activity; adotar tentativa persistida própria só se a matriz exigir; decidir no rascunho |
| Q-08 | Storage de proteína específico, sem alteração padrão de atomic.py; leitor próprio de metadados esclarecido |
| Q-09 | Bloqueio de truncamento e modelo fonte explícito; tetos e templates de erro ainda a fixar sem alegar benchmark |

Estas disposições são suficientes para confronto focal das respostas e para uma decisão posterior sobre rascunho. Não resolvem automaticamente o conteúdo de uma especificação final. O comando atual proíbe produzi-la e essa proibição foi preservada.

## 10. Cenários concretos que o rascunho deverá discriminar

- Água removida/metal mantido: contrastar (a) recusa e (b) omissão de metalc com auditoria, sem remoção do metal.
- Ligante covalente removido/proteína mantida: recusa em ambas as opções, sem reparo.
- Polímero A mantido/B removido/metal Z mantido: tabela de alcance e conexão cruzada, com autoria de cada decisão.
- Asym não polimérico explicitamente selecionado e sem disposição: inclusão por S; U não deve causar recusa espúria.
- Asym explicitamente selecionado e remove: recusa de conflito, sem precedência inventada.
- Componente kept fora de S com auth id igual/diferente/ambíguo: auditoria sem inferência de associação biológica.
- Polymer não selecionado com modified keep: conflito; cadeia inteira excluída com remove: exclusão conjunta, sem edição de resíduo.
- Branched misto NAG remove/BMA keep: recusa com e sem struct_conn interno.
- Model_num ausente/nulo/zero/misturado; modelo resolvido diferente do primeiro; conexão avaliada apenas em M.
- Códigos de inserção 52/52A, altlocs e label_seq nulo em água: endpoint inequívoco ou recusa, nunca primeiro candidato.
- ptnr3 com colunas só nulas versus valor preenchido e valor textual citado '?'.
- Simetria conhecida identidade, distinta, ambos iguais não identidade, ausente de um/ambos os lados.
- Tipos covalentes enumerados, metalc/hydrog condicionais, saltbr/mismat/unknown fora da exceção.
- Registro pedido a com id interno A em filesystem insensível à caixa: recusa; hashes calculados dos mesmos bytes validados.
- Metadado mudando entre duas aberturas injetadas: não deve existir uma segunda abertura como origem da mesma proveniência; links cruzados incoerentes provocam recusa.
- parser-limitation com full; bundle corrompido em retry; erro só de apresentação pós-commit; propriedade da compensação; KeyboardInterrupt e SystemExit separados por fase.

São requisitos de estudo para a futura matriz, não testes implementados/executados. A validação desta documentação não substitui esses testes.

## 11. Separação das responsabilidades de fechamento

**Respondido pelo arquiteto:** propostas de mecanismo para os quatro MAJORs; tabela de precedência; leitura direta canônica; esclarecimentos de simetria e modelo; leitor próprio de metadados; errata de ambiente; disposições de todos os MINORs/NOTES e plano de cenários.

**Dependente do responsável:** D-01 (recusa total ou exceção auditada por tipo) e D-02 (alcance amplo explícito ou cobertura adicional por seleção de labels). Nenhuma escolha foi registrada como aprovada nesta reconciliação. Não se solicita aprovação de código inexistente; as propostas concretas e suas consequências estão acima.

**Dependente do revisor:** verificar se as respostas fecham os achados originais e confrontar as ressalvas parciais. A tarefa focal preparada cobre apenas essa resposta e suas consequências, sem nova revisão do 020-A ou repetição integral por preferência. Pode avaliar recomendações condicionalmente, mas não fechar decisões do responsável que ainda não chegaram.

**Dependente do rascunho/implementação futura:** catálogo por tags, esquema/ids/chave, limites, erro/publicação/recuperação e provas reais de writer/Python/Windows/concorrência. Não chamar essa enumeração de implementação autorizada.

## 12. Evidências e limites desta execução

Execução própria: conferência de refs e blobs; hashes de inputs; AST dos arquivos Python; sonda de descoberta/distribuição Python para o ambiente; validação de JSON/links/whitespace desta entrega. Não houve instalação, pytest, import/execução Gemmi, C++ recompilado, arquivo científico materializado, Windows ou ensaio concorrente. A sonda Python não importa o namespace nem chama API científica.

Confronto de fonte: parsing, inspeção, resolução, registries e atomic da baseline; reader Gemmi pinado e amostra 5i55; documentação oficial wwPDB consultada nesta sessão. Nenhuma frequência populacional foi estimada a partir de uma amostra ou das estatísticas resumidas do dicionário. O defeito de coluna foi constatado estaticamente, sem apresentar uma execução do parser 020 como realizada.

## 13. Estado e próximo gate

A resposta arquitetural está concluída para o escopo solicitado, com D-01/D-02 explicitamente pendentes. Isso não equivale a fechar independentemente 4 MAJORs/5 MINORs. A tarefa focal está preparada como próxima etapa, sem dispatch automático e sem exigir que o responsável copie relatórios no chat.

STATUS e a tarefa de reconciliação registram a entrega; os materiais originais permanecem intactos. A main do código e a main do governance não são destinos desta publicação. O 020-A permanece em stand-by, sem aprovação/cancelamento/retomada.

## 14. Referências verificáveis

- [Parecer de Claude, commit debeba6](https://github.com/sysoutemanuelhenrique/molecular-platform-governance/blob/debeba6f4370c6f5dd77d2273420abf8a828e9f8/increments/021/02-study-review/CLAUDE_INCREMENT_021_STUDY_WITH_CONTINUATION_REVIEW.md).
- [Estudo v1](https://github.com/sysoutemanuelhenrique/molecular-platform-governance/blob/f1656badb35a67942b8318b6f6744b0c71f01de6/increments/021/01-study/INCREMENT_021_RECEPTOR_MATERIALIZATION_STUDY.md), [complemento](https://github.com/sysoutemanuelhenrique/molecular-platform-governance/blob/f1656badb35a67942b8318b6f6744b0c71f01de6/increments/021/01-study/continuation/INCREMENT_021_MINIMAL_CORE_STUDY.md) e [N020 §34](https://github.com/sysoutemanuelhenrique/molecular-platform-governance/blob/f1656badb35a67942b8318b6f6744b0c71f01de6/increments/021/01-study/references/INCREMENT_020_FINAL_SPECIFICATION.md).
- [receptor_parsing.py](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/src/molecular/receptor_parsing.py): colunas/conexões 352–535, modelo/ocupância 613–647.
- [receptor_inspection.py](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/src/molecular/receptor_inspection.py): chains 382–411; componentes 427–478; conexão 529–572; truncamento 601–612; capacidade 838–843.
- [receptor_service.py](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/src/molecular/receptor_service.py): resolução e baldes 503–629.
- [receptor_registry.py](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/src/molecular/receptor_registry.py), [registry.py](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/src/molecular/registry.py) e [atomic.py](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/src/molecular/atomic.py): leitores, check-then-write, xb e os.link.
- [Gemmi 0.7.5, reader mmcif.cpp](https://github.com/project-gemmi/gemmi/blob/5cc1c23c6007e0e6cbd69289c6f7c0bff50e943e/src/mmcif.cpp), 185–240; [amostra 5i55.cif](https://github.com/project-gemmi/gemmi/blob/5cc1c23c6007e0e6cbd69289c6f7c0bff50e943e/tests/5i55.cif), 694–733.
- [wwPDB: tipo de conexão](https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_struct_conn_type.id.html), [inserção](https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_struct_conn.pdbx_ptnr1_PDB_ins_code.html), [simetria](https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_struct_conn.ptnr1_symmetry.html), [tipo de entidade](https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_entity.type.html), [auth_asym_id](https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_atom_site.auth_asym_id.html), [categoria struct_conn](https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Categories/struct_conn.html). Páginas mutáveis consultadas em 23/11/2026; fatos e limitações registrados sem extrapolar frequência.

ARCHITECTURAL RECONCILIATION COMPLETE: YES
OWNER DECISIONS D-01/D-02 RECORDED AS APPROVED: NO
INDEPENDENT FINDING CLOSURE COMPLETE: NO
READY FOR FOCAL REVIEW PREPARATION: YES
FOCAL REVIEWER DISPATCHED: NO
READY FOR IMPLEMENTATION: NO
FINAL SPECIFICATION FROZEN: NO
CODE REPOSITORY MODIFIED: NO
