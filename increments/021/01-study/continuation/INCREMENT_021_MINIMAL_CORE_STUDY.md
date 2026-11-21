# Incremento 021 — Continuação do estudo: núcleo mínimo funcional

Data: 21/11/2026. Autor: Codex, arquiteto. Natureza: complemento arquitetural do estudo v1; não é especificação nem revisão independente.

## 1. Objeto, autoridade e identidades

O responsável pediu que o 021 comece por um “esqueleto” e receba capacidades específicas posteriormente; em seguida, esclareceu que o arquiteto deve continuar o estudo conforme o comando original, sem depender do encaminhamento manual ao revisor. Este documento interpreta esqueleto como uma primeira operação completa, limitada e verificável, não como módulos vazios ou autorização de implementação.

| Referência | Identidade verificada |
|---|---|
| Código, main | `08b797e0985e123ffd4d7ca7e5a5e8f040e63851` |
| Governance, entrada desta continuação | `599a6873b2a55d09c3497780d99794fe337a08e8` |
| Governance, entrada original preservada | `6a85b79a33bce419c0ebd2bde6793732ef4f0388` |
| Estudo v1 preservado | 365 linhas; 55.594 bytes; SHA-256 `5048c5012548ee1169f58e6bb644ecf8b5d76a59c6569400d67db0987f7dfa56` |
| Especificação final do 020, preservada | 1.975 linhas; 210.880 bytes; SHA-256 `cf6cb534f9267d51e718052c7b36a2293c522bc566c99cf3bb2ef5909385a0a6` |
| Gemmi, fonte oficial | 0.7.5; commit `5cc1c23c6007e0e6cbd69289c6f7c0bff50e943e` |

Os HEADs remotos foram reconferidos antes desta continuação. O avanço do governance de 6a85b79 para 599a687 foi a publicação autorizada do próprio estudo, não uma divergência externa do gate inicial. A main do código e a main do governance continuam, respectivamente, em 08b797e e a47183d. Nenhum documento do 020-A foi alterado ou reavaliado.

O estudo v1 continua sendo a análise ampla das opções A/B/C. Este complemento torna mais restrita a recomendação inicial e explicita os pontos em que ela difere de B. Não muda retroativamente o texto v1. Em caso de diferença sobre o recorte recomendado, a recomendação mais recente está neste complemento; nenhuma das duas versões é um contrato congelado.

Legenda: **F** fato verificado no código/documento/fonte oficial; **R** recomendação; **Q** decisão ainda necessária no rascunho. As referências C02/C07/C12/G01/G02/G06/N020 são as mesmas referências permanentes da seção 20 do estudo v1.

## 2. Conclusão arquitetural do aprofundamento

**R — começar por um perfil mínimo da opção B:** no referencial do modelo de origem, com saída mmCIF, disposições efetivas do 020, preservação de todas as alternativas conformacionais e bloqueio de cortes de conectividade declarada. Não implementar agora seleção parcial de altlocs nem reconhecimento manual de cortes por conexão.

Esse recorte continua produzindo um resultado útil: o cientista pode selecionar um modelo e cadeias e aplicar keep/remove já confirmados para componentes, desde que a extração seja demonstravelmente coerente com as referências estruturais suportadas. Não se trata apenas de copiar o RAW ou de exportar um inventário sem coordenadas.

| Aspecto | Estudo v1, B | Recomendação para o perfil mínimo |
|---|---|---|
| Assembly selecionado | Recusar | Preservado: recusar explicitamente assembly não nulo |
| Altloc | Preservar ou selecionar labels explicitamente | Somente preservar todas as alternativas; não oferecer seleção parcial |
| Corte em conexão declarada | Reconhecimento individual proposto, sujeito a Q-02 | Recusar qualquer corte declarado que atravesse átomos mantidos/removidos |
| Componentes sem disposição | Complemento explícito | Mantido: escolha explícita preservar todos os não abordados ou exigir cobertura completa |
| Categorias mmCIF | Catálogo fechado a detalhar | Mantido: catálogo e integridade são necessários mesmo na primeira entrega |
| Publicação e proveniência | Bundle verificável | Mantidas: não são opcionais por chamar a entrega de esqueleto |
| Química | Fora de escopo | Fora de escopo; nenhuma adição/reparo/protonação |

**R:** não substituir esse perfil pela opção A sem anunciar a perda de cobertura das disposições já confirmadas. Uma extração que ignora remove/keep não é materialização daquela seleção. Uma entrada recusada pelo perfil não é defeito por si; o limite deve constar da CLI, dos registros e dos testes.

## 3. Contrato científico mínimo proposto

1. Carregar a resolução solicitada e as referências exatas: política, inspeção e ProteinInput. Não escolher inspeção mais recente, reexecutar resolução ou produzir nova inspeção em fallback.
2. Exigir seleção suportada, modelo identificado, pelo menos uma cadeia explícita, identidade label inequívoca e inventário suficiente. Manter os limites do 020: o 021 não transforma inspeção parcial em identidade completa.
3. Exigir `resolved_assembly=None`. Não aplicar simetria, NCS, transformações de assembly, alinhamento ou fusão por distância. As coordenadas de saída permanecem no referencial original.
4. Aplicar as disposições efetivas confirmadas. Ocorrências sem disposição só sobrevivem por escolha complementar explícita; não presumir que a ausência significa remover ou preservar.
5. Preservar todas as alternativas nos sítios mantidos. Preservar H/D existentes, ocupância zero/parcial/ausente, B-factor e coordenadas fonte; não escolher A/maior ocupância, renormalizar, arredondar ou reparar.
6. Conferir as conexões declaradas. Reter ambas as extremidades exige correspondência inequívoca e contexto suportado; remover ambas permite omitir a conexão com auditoria; reter somente uma causa recusa. Não inferir ligações químicas ausentes do arquivo.
7. Produzir estrutura, manifesto e auditoria novos; validar o conteúdo contra o plano antes de publicar. Não criar ScientificEntity, MolecularState, Conformer ou receptor quimicamente preparado automaticamente.

**F:** o inventário do 020 não contém as coordenadas em `ParsedAtom`; também não preserva todos os tokens necessários à saída. As coordenadas precisam vir dos bytes do RAW capturados e verificados. A reinterpretação estrutural pelo 021 é operação nova; não modifica a inspeção referenciada. [C02]

**R — distinção importante:** ausência de `_struct_conn` não comprova ausência de ligação ou de problema químico no recorte. Registrar que a fonte não oferece esse conjunto de evidências. O perfil verifica referências declaradas e contexto polimérico suportado, sem certificar um grafo químico completo. Componentes covalentemente ligados, glicanos e polímeros modificados só entram em remoção se a identidade/contexto e a ausência de corte proibido puderem ser demonstrados; caso contrário, recusar a remoção, sem classificação geométrica improvisada.

## 4. Esclarecimento sobre a precedência do 020

**F:** `_resolve_component_dispositions` aplica os baldes de água e metal antes das entradas nomeadas e usa `seen` para não sobrescrever uma chave já resolvida. Portanto, uma intenção nomeada diferente de um balde pode coexistir com uma resolução efetiva válida na baseline. [C07]

**R — esclarecer o §7.2 do estudo v1:** uma diferença explicada por essa precedência existente não deve ser transformada pelo 021 em veto automático ou exigência de nova seleção. A materialização aplica a resolução efetiva e informa sua origem. O 021 não reaplica a intenção com outra ordem nem tenta corrigir a decisão.

Um conflito físico distinto continua recusável: por exemplo, a mesma ocorrência inequívoca receber simultaneamente a obrigação de permanecer por uma cadeia explicitamente selecionada e de sair por disposição efetiva. A especificação deve distinguir esse conflito de requisitos do simples fato de o resolved subset refletir a precedência já implementada. A justificativa da recusa deve apontar a incompatibilidade concreta, sem invalidar genericamente os registros do 020.

## 5. Esqueleto de responsabilidades, sem fixar APIs ou schemas

| Camada | Responsabilidade nova | O que não deve fazer |
|---|---|---|
| Domínio | Decisão mínima, plano de inclusão/exclusão, descrição do resultado | Importar Gemmi, abrir arquivos, modificar modelos 020 |
| Adapter em `receptor_parsing.py` | Ler bytes verificados e transcrever tokens/coordenadas para o novo fluxo; construir/validar mmCIF | Alterar `parse_receptor_raw`, reclassificar cientificamente componentes ou chamar helpers de preparação |
| Storage específico | Snapshot de proteína, staging privado, reserva, publicação e leitura íntegra | Reaproveitar a raiz fixa de ligantes como se aceitasse proteínas |
| Registry novo | Persistir decisão própria e consultar bundles/identidades | Reescrever seleção/inspeção ou anunciar arquivo ainda não publicado |
| Application Service novo | Orquestrar uma operação e devolver resultado/erro tipado | Usar CLI como compensador ou executar motor científico novamente após commit |
| CLI aditiva | Coletar escolhas explícitas, chamar serviço uma vez e mostrar artefato/proveniência | Inferir decisão química, duplicar activity log ou apresentar sucesso parcial |

**R:** domínio e plano podem ser testados antes do filesystem complexo. Entretanto, a primeira entrega pública de materialização só existe quando esse fluxo vertical está completo; CP1 isolado não deve ser anunciado como receptor materializado.

**R:** manter duas operações conceituais: declarar decisão e executar materialização. Isso permite identificar o que foi aprovado sem acoplar a decisão ao sucesso da escrita. A CLI pode oferecer uma fachada composta futuramente, mas o serviço precisa distinguir declaração existente de bundle publicado. A persistência da declaração não participa do rollback do artefato.

Não há nomes de classes, assinaturas Python, enumerações de erro, paths definitivos ou JSON público congelados aqui. O esqueleto é de responsabilidades e invariantes. Não há autorização para gerar arquivos de código vazios ou scaffolding nesta etapa.

## 6. A parte que não pode ficar para depois: fidelidade dos tokens

**F:** a documentação versionada de Gemmi explica que o DOM CIF guarda strings brutas, inclusive aspas; `as_string` retira a representação de quoting, e `Loop.add_row` espera strings adequadamente representadas como tokens CIF. Os overloads Python de `cif.read_string` aceitam bytes e str na tag 0.7.5. [G01/G02/G06]

**R:** separar representação de identificação/validação da representação de serialização. O plano pode interpretar um número para verificar finitude e comparar identidades, mas a saída de campos preservados usa os tokens fonte, não `float → str` ou `Decimal → str` como mecanismo de reconstituição. Não aplicar `quote_list` indiscriminadamente a tokens que já estão representados em CIF.

Os casos `?`, `.`, `'?'` e `'.'` não devem ser colapsados num único null: os dois primeiros são marcadores CIF; os dois últimos são valores textuais citados. O writer pode reorganizar whitespace do arquivo, mas não converter valor textual citado em marcador de ausência nem inventar ocupância a partir de default. Valores numéricos também não podem ganhar arredondamento silencioso.

**Q:** fechar no rascunho o tratamento de valores numéricos com incerteza, identificadores citados e categorias/colunas estendidas. Aceitar token requer semântica de campo compatível; preservar bytes não torna valor inválido cientificamente aceitável. A evidência de fonte demonstra viabilidade do mecanismo, não demonstra que uma implementação ainda inexistente acerte todos esses casos.

## 7. Catálogo de saída e referências

**R:** a redução de escopo não autoriza copiar todo o bloco e remover somente linhas de `_atom_site`. O catálogo da saída precisa definir as categorias suportadas, suas chaves e as relações com átomos/modelos/cadeias/entidades sobreviventes. `_atom_site_anisotrop`, sequência declarada, entidades e conexões continuam demandando tratamento explícito quando presentes.

Categorias não cobertas não recebem um filtro genérico baseado em conter a palavra atom ou chain. A política deve distinguir: categorias de preservação obrigatória; categorias opcionalmente omitidas com auditoria e limite declarado; e situações não suportadas que exigem recusa. Não é possível afirmar que uma categoria desconhecida é referencialmente inofensiva só por seu nome. Também não é necessário prometer preservar todo metadado experimental para produzir um recorte identificado como derivado.

**Q:** o catálogo exato continua pendente de rascunho/revisão. Ele é uma condição para autorizar implementação do writer, não uma questão delegável ao implementador. O primeiro perfil pode ser deliberadamente estreito e recusar arquivos fora dele. Fixtures representativas precisam demonstrar que esse perfil não aceita apenas um mmCIF sintético vazio de metadados relevantes.

## 8. Snapshot, identidade e publicação

**F:** o helper atual de snapshot de RAW é fechado para `inputs/ligands/{input_id}`; o perfil de plataforma é Windows/NTFS. O helper de publicação de diretório e `os.replace` não fornecem, isoladamente, toda a garantia concorrente proposta. [C12]

**R:** preferir inicialmente um leitor/storage específico de proteína, sem generalizar `atomic.py`, a menos que a especificação demonstre que o reuso privado reduz duplicação sem ampliar o contrato dos ligantes. A allowlist mínima deixa a alteração de `atomic.py` fora do caminho padrão; escolhê-la exige decisão e regressões próprias.

Uma requisição deve estar vinculada aos registros fixados, ao checksum do RAW e ao perfil da operação. A chave técnica não é deduplicação química. Em retry, um bundle existente só é reused após verificação de integridade e equivalência; não se deve reexecutar o writer para corrigir resultado corrompido.

**R — fluxo conceitual:** validar referências e escolhas → capturar RAW verificado → obter chave da requisição → reservar exclusivamente a chave ou validar resultado existente → planejar/materializar em staging próprio → verificar arquivo/manifesto/auditoria → publicar bundle completo → retornar resultado. A forma concreta deve permitir verificar o vínculo da saída com o snapshot sem reabrir um caminho RAW mutável.

O ponto de commit é a publicação confirmada do bundle, não uma linha de log ou saída da CLI. Falha de apresentação posterior retorna erro de apresentação/armazenamento conforme a causa, identifica o resultado já publicado e não compensa nem executa novamente. Antes do commit, a limpeza atinge apenas recursos cuja propriedade tenha sido comprovada. Resultado indeterminado de publicação exige reconciliação por identidade; não permite apagar o destino por suposição.

**Q:** a especificação precisa escolher se as falhas pré-commit serão representadas por tentativa persistida própria ou por reserva diagnosticável + erro estruturado + activity log. Este estudo não escolhe um modelo universal de execução. Nenhuma opção pode perder o erro principal, esconder resíduos ou declarar falha científica quando só falhou a apresentação. Crash de processo pode deixar staging/reserva órfãos; não há promessa de limpeza automática ou durabilidade após queda de energia sem evidência.

## 9. Proposta de encaminhamento das decisões Q-01–Q-09

| Questão do estudo v1 | Posição arquitetural após aprofundamento | Fechamento ainda necessário |
|---|---|---|
| Q-01 escopo | Perfil mínimo de B, assemblies explicitamente recusados | Confronto independente da suficiência e decisão de escopo para o rascunho |
| Q-02 conexões cruzadas | Bloquear todo corte declarado no primeiro perfil | Definir endpoint/contexto suportados e mensagens; não oferecer reconhecimento manual nesta entrega |
| Q-03 categorias | Catálogo fechado, filtros por chaves e auditoria | Tabela completa por categoria/coluna e fixtures; não delegar a decisão ao implementador |
| Q-04 declaração/execução | Separadas conceitualmente, registros próprios | Fechar ergonomia dos comandos sem duplicar serviço |
| Q-05 equivalência | Snapshot documental e decisões completas | Canonicalização/versionamento e tratamento de edição externa de registro |
| Q-06 publicação | Bundle sob reserva exclusiva, commit verificável | Primitivas, recuperação e provas Windows/NTFS no checkpoint de implementação |
| Q-07 falhas/tentativas | Mecanismo específico mínimo, sem generalização | Escolher a menor opção que satisfaça a matriz de falhas, com tradeoff explícito |
| Q-08 leitor | Preferência por storage de proteína específico | Comparar custo de duplicação/reuso seguro antes do contrato final |
| Q-09 limites/CLI | Tetos de entrada/saída/auditoria e templates tipados | Valores e taxonomia ainda não fixados; não alegar desempenho medido |

As recomendações acima tornam o estudo mais concreto, mas não fingem que catálogo, protocolo e limites já estejam congelados. O estudo pode ser revisto com essas questões abertas; a implementação não pode ser autorizada com essas decisões indefinidas.

## 10. Testes propostos para o núcleo e o que passa a ser recusa

Os 48 cenários do estudo v1 continuam sendo uma proposta, não itens pytest nem evidência executada. No grupo P021-20–25, substituir a aceitação de seleção parcial de altloc por cenários de recusa e preservar os casos positivos de retenção das alternativas. No grupo P021-26–33, substituir a aceitação de corte reconhecido pela recusa mesmo diante de reconhecimento fornecido. A matriz definitiva deve discriminar cada id, sem reutilizar uma descrição que prometa capacidade retirada do recorte.

Adicionar à matriz do rascunho casos explícitos para os quatro tipos de token nulo/textual, valor numérico com precisão preservada, ocupância zero e precedência bucket versus entrada nomeada sem veto indevido. Testar ambas as extremidades retidas/removidas, uma removida, simetria não materializada, conexão ambígua e categorias fora do perfil. Não confundir ausência de `_struct_conn` com prova de conectividade química completa.

**Q:** a tabela agrupada v1 não associa univocamente cada comportamento a um id individual dentro de P021-20–25/P021-26–33. Assim, este complemento não atribui números individuais por inferência. Antes do congelamento, enumerar todos os cenários um a um e reconciliar funções, parametrizações e itens coletados.

Os quatro checkpoints propostos permanecem úteis: domínio/plano; adapter/arquivo; storage/serviço; CLI/regressão. As capacidades retiradas não precisam de implementação placeholder: devem ter recusa explícita comprovada. Segurança de snapshot e publicação continua exigindo evidência Windows real no checkpoint correspondente, sem bloquear por circularidade a redação do estudo/especificação.

## 11. Crescimento posterior, sem numeração antecipada

Assemblies físicos, seleção parcial de altlocs, autorização de cortes e formatos adicionais só entram por decisões/specs posteriores que avaliem identidade e proveniência próprias. Não se atribui agora número de incremento nem se autoriza criação de interfaces genéricas “para o futuro”. Protonação, cargas, reparo, minimização e docking seguem fora desta rodada.

O 020 é uma fundação concluída de inspeção/seleção lógica. O 020-A permanece suspenso; B/C da antiga trilha de demonstração não são pré-requisitos do 021. Esclarecer essa separação não cancela nem aprova etapas pendentes da trilha suspensa.

## 12. Evidência e conclusão do estudo

Nesta continuação foram reconferidos os HEADs remotos e relidos os trechos de produção referentes à resolução, precedência, representação de átomos e snapshot; as fontes oficiais pinadas do Gemmi esclarecem o comportamento de tokens/DOM e do binding de leitura. As identidades dos arquivos consultados e os locais de evidência estão em `evidence/continuation-verification.json`; os hashes de todos os blobs da baseline continuam no pacote v1.

Não houve pytest, instalação, execução Gemmi, ensaio científico, transformação de arquivo ou validação Windows/concorrente. Não foi enviado comando ao Claude nem iniciado revisor/implementador em segundo plano. Esta é análise do arquiteto; não substitui revisão independente.

Conclusão: o estudo do 021 está completo como proposta arquitetural confrontável, com uma primeira entrega menor e útil. O próximo artefato de implementação não será criado nesta etapa. A tarefa de revisão fica preparada no governance, sem exigir ação imediata do responsável ou alegar que o revisor já começou.

STUDY COMPLETE: YES
READY FOR INDEPENDENT STUDY REVIEW: YES
READY FOR IMPLEMENTATION: NO
FINAL SPECIFICATION FROZEN: NO
CODE REPOSITORY MODIFIED: NO
