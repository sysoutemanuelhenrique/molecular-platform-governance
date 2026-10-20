# FINAL SPECIFICATION — INCREMENTO 020-A

## Molecular characterization and static 2D depiction

Autor: Codex, arquiteto. Data: 20/10/2026. Versão documental: final1. Natureza: contrato final congelado após fechamento independente pelo Claude e aprovação explícita de Emanuel Henrique da Silva.

**Especificação congelada. Implementação autorizada exclusivamente para o Checkpoint 1, conforme registro de aprovação e tarefa próprios.** O conteúdo normativo da candidate1 foi adotado sem alteração científica. Os termos históricos “candidato”, “rascunho” e “proposto” nos trechos preservados registram sua origem documental; o estado vigente e o checkpoint autorizado são os desta apresentação e da seção 22. Não executar checkpoints posteriores sem sua autorização própria.

## 1. Decisão de processo e histórico preservado

O responsável decidiu em 20/10/2026 continuar **somente com a revisão independente do Claude nesta etapa**. Essa decisão substitui, para a passagem deste gate do020-A, a espera anteriormente prevista por um segundo revisor. Não reescreve pareceres ou regras históricas de outros incrementos.

O adendo do Claude fecha a arquitetura V2: 0 BLOCKERS, 0 MAJORS, 0 MINORS, 1 NOTE documental não bloqueante e READY FOR DRAFT SPECIFICATION:YES quanto à sua linha de revisão. O presente rascunho incorpora A-01–A-14 e os complementos C-01/C-02/C-03 aceitos. O revisor não aprovou a implementação nem a especificação final.

A revisão independente do draft1 recebida em 20/10/2026 registrou 0 BLOCKERS, 0 MAJORS, 3 MINORS e 6 NOTES, com avanço condicionado às correções textuais. Esta candidata responde aos três MINORs e às notas na resposta acompanhante. O arquiteto endereçou os itens e o Claude encerrou independentemente os três MINORs no parecer de commit 7f1f75219203eb1a691e454db170900ca81536e8: 0 BLOCKERS, 0 MAJORS, 0 MINORS e 2 NOTES não bloqueantes. O draft1, a candidate1 e os pareceres recebidos permanecem preservados byte a byte.

Gate atual: **arquitetura → rascunho → revisão adversarial do rascunho → candidata final → aprovação/congelamento explícitos → implementação autorizada → checkpoints e evidência Windows → revisão cumulativa**. Os leitores de produção não serão implementados para poder aprovar a redação do contrato que os autorizará. Um spike anterior só será solicitado se houver dúvida concreta de viabilidade que impeça especificar esse contrato.

NOTE documental preservada: o roadmap provisório antigo de conformeros atribui outro escopo ao020. O contrato final020 posterior prevalece para o que foi entregue e para a interface reservada ao021. Corrigir o enquadramento do roadmap em trabalho documental separado, preservando a trilha histórica; não alterar os originais neste incremento.

Em 20/10/2026, Emanuel respondeu diretamente “aprovado” à solicitação de congelamento da candidate1 (SHA-256 123596d03947f89321e6e623e3f0e7a2b88f38de42cd510a59f31cfd16d67ad4) e autorização restrita ao Checkpoint 1, preparada no snapshot 11e571a856c2e0dc6b169160a79f9f5eeb4805e3. As duas NOTES foram aceitas sem mudança do perfil. A allowlist e os checkpoints da seção 18 ficam adotados; a tarefa de implementação limita esta autorização a quatro caminhos e exige o registro de execução real. Não há autorização de Checkpoints 2/3, PR ou merge.

## 2. Baseline e fontes fixadas

Repositório: `sysoutemanuelhenrique/molecular-platform`. Branch de referência: `main`. SHA de estudo e baseline candidata: **08b797e0985e123ffd4d7ca7e5a5e8f040e63851**. HEAD remoto reconfirmado neste ciclo; clone no mesmo SHA, working tree limpa e diff-check sem erros nas verificações de estudo. Antes de autorizar implementação, reconfirmar a baseline; qualquer avanço exige reconciliação explícita, não implementação contra alvo móvel.

Fontes da decisão arquitetural:

| Material | Identidade fixada ou origem |
|---|---|
| Proposta revisada V2 | SHA-256 eb3ffdbe07a6939363a6f82114a21e761fffcac405b7b3224dd3989f3b17ad8d; 314 linhas; 44.445 bytes |
| Resposta V2/C-01–C-03 | SHA-256 fa820311083a9d204f0e1d7858a935c3a617cf3f1201c80c551d217118247713; 138 linhas; 14.876 bytes |
| Pacote resposta V2 | SHA-256 58234663a93e36c8c84c7fc90c2eaa7f3c56daf0ea2a612a6565dc34267fcbfd; 372.328 bytes |
| Final020 | SHA-256 cf6cb534f9267d51e718052c7b36a2293c522bc566c99cf3bb2ef5909385a0a6; 1.975 linhas; 210.880 bytes |
| Validação CP4 do020 | SHA-256 69ece589ca25ddaa1e3286b33dd1a0e76e5245043cf8f633559383389e918785; 365 linhas; 25.318 bytes |
| Adendo de fechamento Claude | Texto integral fornecido pelo responsável nesta conversa; sem atribuição fictícia de hash de arquivo original |
| Decisão de revisor único | Mensagem expressa do responsável nesta conversa, 20/10/2026 |
| Draft1 preservado | SHA-256 b0c8532282ac90cf41c9958b8af06ef3aea142777794af6b058e3ba558c6397d; 542 linhas; 62.532 bytes |
| Revisão independente do draft1 | Anexo original `Texto colado(20261020-160803).txt`; identidade e cópia integral no pacote desta candidata |

O pacote de resposta contém os originais pertinentes dos contratos016–020, fontes de governance, pareceres e ensaios. Estes materiais continuam sendo a base de rastreabilidade; o rascunho não os substitui. Código primário: `https://github.com/sysoutemanuelhenrique/molecular-platform/tree/08b797e0985e123ffd4d7ca7e5a5e8f040e63851`.

Classificação de evidências: fatos de source são SOURCE_VERIFIED; conteúdo de normas/pareceres é DOCUMENTED; resultados de sondas controladas são EXPERIMENTALLY_VERIFIED. As decisões deste rascunho são propostas arquiteturais, não novos fatos medidos. Não se alega leitura integral de toda a governance histórica nem execução de testes de uma funcionalidade inexistente.

## 3. Objetivo e exclusões

Adicionar uma consulta de caracterização de **um MolecularState registrado**, que calcula dez valores, devolve proveniência da observação e pode gerar SVG2D estático. No âmbito dos dados científicos do estado, o serviço deve ler somente o registro e a representação autorizados, verificar os bytes que serão analisados e devolver dados neutros. A resolução de experimento e a consulta de metadados da instalação mantêm suas responsabilidades distintas.

Não há escrita científica, publicação, cache, histórico interno de consulta ou activity log novo. Não criar ScientificEntity, MolecularState, Conformer, StateTransformationRecord, ExecutionAttempt, LigandPromotionAttempt ou registry de caracterização. Não alterar nenhum desses schemas.

Ficam excluídos: aquisição PubChem nova; promoção; normalização de estado; neutralização; protonação/pKa/pH; dessalinização; tautomerização nova ou comparação de tautômeros; grupos funcionais; similaridade/fingerprints; drug-likeness; geração3D; otimização; campos de força; cargas parciais; receptor/docking; GUI, wizard e novos aliases. 020-B/020-C continuam estudos separados;021 continua reservado segundo o final020.

## 4. Arquitetura e APIs candidatas

Responsabilidades:

| Camada | Responsabilidade |
|---|---|
| characterization.py, novo | DTOs imutáveis/estritos, perfis fechados e erros próprios; sem RDKit, CLI ou I/O |
| atomic.py, adição específica | Duas leituras verificadas, algoritmo privado compartilhado; funções existentes intactas |
| rdkit_tautomer.py, adição | Único ponto de imports RDKit; parsing, valores, desenho e validação do SVG; funções de enumeração/promoção intactas |
| characterization_service.py, novo | Validar pedido, coordenar leitores e adaptador, construir/verificar proveniência e resultado |
| cli.py, adição | Comando fino, resolução de experimento e apresentação; sem química duplicada |

APIs candidatas, sem objetos RDKit na fronteira:

```text
read_verified_state_metadata(project_dir, *, state_id) -> VerifiedBytes
read_verified_state_representation(project_dir, *, state_id,
    relative_path, expected_checksum) -> VerifiedBytes
characterize_molecule_rdkit(representation_bytes, *, input_format,
    input_state_id, representation_sha256, include_svg=False) -> neutral adapter result
characterize_state(project_dir, *, input_state_id,
    include_svg=False) -> MolecularCharacterizationResult
```

`VerifiedBytes` é estrutura interna frozen com data:bytes, sha256:str e size_bytes:int; size_bytes=len(data), hash calculado a partir de data. Não é artefato de domínio persistido. Os nomes internos de estruturas auxiliares podem ser ajustados na revisão; as responsabilidades, JSON público e invariantes deste texto não podem ser alterados silenciosamente.

Os dois wrappers do atomic DEVEM compartilhar o mesmo algoritmo privado de verificação de acesso/identidade/leitura. Cada wrapper fixa raiz, limite e política de checksum; não há raiz arbitrária fornecida pelo chamador externo. Não refatorar os leitores legados por essa razão. Pode haver seams explícitos para injetar falhas nos testes, com defaults reais de produção; nenhum seam pode contornar validações.

## 5. Identificadores e autorização lexical

Antes de construir paths ou fazer I/O do experimento, serviço e entradas públicas de leitura devem usar `molecular.inputs.validate_input_id` para state_id. Autoridade atual: regex `^[A-Za-z0-9][A-Za-z0-9_-]*$`, por fullmatch, valor str. Não strip, casefold, transliterar, substituir caracteres ou aceitar outro token em seu lugar. Não alterar esse validador compartilhado.

O ID carregado do YAML deve ser exatamente igual ao solicitado, com comparação sensível a case. entity_id carregado também deve passar no validador atual. A chamada não precisa abrir registro de entidade para mostrar seu nome. Referência ausente ou incoerente no estado não será reparada automaticamente.

**Validade lexical não é elegibilidade de filename Windows.** CON/NUL/LPT1 passam na regra de ID, mas o leitor deve recusar seus filenames antes de abri-los. Para componentes construídos/usados no caminho específico, recusar:

- vazio, `.`/`..`, NUL, controles U+0001–U+001F e os caracteres `< > : " / \\ | ? *` dentro de um componente;
- nomes com espaço ou ponto final; namespace de dispositivo/ADS; absolutos POSIX, drive, drive-relative e UNC quando relativos forem exigidos;
- stem, antes do primeiro ponto e ignorando espaços finais desse stem, igual por casefold a CON/PRN/AUX/NUL, COM1–COM9 ou LPT1–LPT9, inclusive variantes COM/LPT com os dígitos¹²³; recusar também CONIN$/CONOUT$ neste perfil conservador.

Aplicar o controle ao filename do registro, por exemplo CON.yaml, e ao leaf da representação. Não confundir essa proteção com uma mudança na identidade dos modelos. Não restringir letras Unicode ou espaços internos em leaf válido apenas por estética. O state_id continua ASCII pelo validador atual.

Referência de representação: exigir string POSIX relativa exatamente `scientific/artifacts/states/<state_id>/<leaf>`; cinco componentes, um único leaf, nenhum segmento vazio/traversal, nenhuma barra invertida. Comparar componentes, não startswith textual; não aceitar alias de outro estado. Não resolver primeiro um path que poderia esconder link para só depois verificar segurança. Extensão não determina formato.

## 6. Plataforma, limites e leitura verificada

Perfil candidato de serviço: **Windows11, volume local fixo NTFS**, como escolha expressa do020-A. Deve haver detecção efetiva da versão Windows e do volume/drive; os.name==nt sozinho não basta. A detecção deve usar informação do SO e falhar se não puder confirmar esse perfil. Reaproveitar primitivas adequadas existentes sem alterar seus contratos; a identificação específica de Windows11 deverá ser demonstrada por source/API e testes do checkpoint, incluindo recusa de Windows10/Server/versão indeterminada. Não inferir suporte de um mock que retorna sucesso.

Pergunta de implementação registrada pela NOTE-1 do parecer: o checkpoint2 deve identificar a fonte/API efetivamente usada para distinguir Windows11 cliente de Windows10/Server, justificar eventual critério de build e apresentar seus testes positivos/negativos. Esta candidata não aprova um limiar de build como contrato universal/futuro da Microsoft. O ponto não exige implementar ou executar os leitores antes do congelamento; a prova do detector permanece condicionante da aprovação do checkpoint2.

Outros SOs, FAT/exFAT, share de rede e plataforma/volume indeterminados falham antes da abertura do registro/representação. Reparse points de pastas de sincronização também são recusados. Não se promete identificar toda solução de sincronização externa que se apresente como arquivo regular sem reparse; esse não é um mecanismo de imutabilidade do disco.

Limites fechados candidatos, em bytes e contagens inclusivos:

| Limite | Valor |
|---|---:|
| Registro YAML | 1.048.576 bytes |
| Representação | 10.485.760 bytes |
| Átomos totais após parsing, incluindo H explícitos | 4.096 |
| Ligações após parsing | 8.192 |
| SVG retornado em UTF-8 | 16.777.216 bytes |

Arquivos de tamanho zero são recusados. Exatamente o limite é permitido se o conteúdo for válido; um byte/item além é recusado. Os limites são técnicos, não definição de validade química nem garantia de tempo/memória do parser nativo. Os tetos de átomos/ligações são verificados após parsing; não podem ser apresentados como proteção pré-alocação.

Protocolo comum obrigatório para os dois arquivos autorizados:

1. Validar ID e referência lexical; confirmar plataforma. Caminho do metadata é fixo `scientific/states/<state_id>.yaml`.
2. Construir a cadeia de componentes do caminho absoluto ancorado no projeto sem seguir links como mecanismo de autorização. Inspecionar os componentes de diretório pertinentes, inclusive projeto e seus ancestrais até o volume, por lstat; exigir diretórios e recusar symlink, junction ou qualquer reparse point. Inspecionar o arquivo final por lstat; exigir arquivo regular, atributos disponíveis e tamanho dentro do limite.
3. Capturar identidade st_dev/st_ino e atributos relevantes. Ausência/indeterminação dos atributos de Windows exigidos falha de forma fechada. Revalidar a cadeia imediatamente antes da abertura.
4. Abrir um único handle binário somente de leitura. Conferir tipo/identidade por fstat contra o que foi capturado; revalidar cadeia após abertura. Não reabrir o arquivo pelo path para calcular hash ou fazer parsing.
5. Ler blocos de até65.536 bytes pelo handle, acumulando buffer/hash. Interromper ao exceder o limite; não confiar só no tamanho inicial. Fechar o handle em todas as saídas.
6. Conferir quantidade efetiva contra o tamanho capturado; revalidar arquivo/ancestrais ao final e sua identidade. Desaparecimento, substituição ou mudança relevante detectada causa recusa.
7. Para representação: checksum esperado deve ser hex64, podendo conter A–F maiúsculos; comparação case-insensitive com o hash observado lowercase. Preservar no DTO a grafia esperada do registro, sem editar o YAML. Divergência causa falha antes do RDKit. Para metadata não há checksum autoritativo armazenado: retornar o observado sem fingir autenticação.

O serviço usa o primeiro buffer para decodificar UTF-8 estrito, yaml.safe_load e MolecularState.model_validate. Rejeitar YAML inválido, múltiplos documentos, tipos/schema inválidos, ID divergente ou formato não suportado. Não ler novamente o YAML para “confirmar” um checksum que não existe. Ler a representação autorizada pelo registro capturado e entregar esse buffer ao adaptador.

**Garantia limitada:** o resultado corresponde aos bytes e metadados capturados, não a uma transação atômica do experimento. As verificações reduzem/detectam cenários de substituição; não eliminam toda corrida por caminho. Alteração transitória por escritor hostil, modificação posterior à leitura e substituição entre verificações não recebem promessa de detecção universal. Hard link não prova imutabilidade. Não introduzir locks, snapshots em disco, retry ou protocolos de escrita para ampliar essa garantia neste recorte.

## 7. Gramática de entrada

Formato resolvido = representation.format.strip().lower(), exclusivamente sdf ou smiles. Preservar formato declarado na proveniência. Não adivinhar por extensão, sniffing ou tentativa alternada. O checksum cobre o arquivo integral, incluindo newline e SD data; validar gramática sem normalizar esses bytes.

### 7.1 SDF

UTF-8 estrito, sem BOM e sem NUL. LF ou CRLF, sem CR isolado. Exatamente um registro físico V2000 ou V3000, com **uma linha exata `$$$$` como última linha física**. Essa linha pode terminar em EOF, LF ou CRLF; nada pode vir depois, inclusive nova linha em branco ou whitespace extra. Uma propriedade contendo a substring $$$$ não é delimitador; contar por linha exata.

Usar `Chem.ForwardSDMolSupplier(BytesIO(bytes), sanitize=True, removeHs=False, strictParsing=True)` e exigir exatamente um item válido, não None. Não filtrar itens inválidos antes de decidir cardinalidade; válido+inválido é recusa. A contagem física e a cardinalidade do supplier são controles cumulativos. Não aceitar arquivo MOL sem terminador sob o rótulo sdf.

sanitize=True/strictParsing=True coincidem com defaults Python observados no pin; removeHs=False diverge do default True. A gramática externa não é garantida só pelo strictParsing. SD data Unicode pode ser carregado pelo motor, mas não vira dado químico de domínio, legenda, markup ou identidade.

### 7.2 SMILES

ASCII estrito, sem BOM, NUL, DEL ou controles. Permitir um token não vazio, sem whitespace inicial/interno/final, opcionalmente seguido de **um LF ou um CRLF**. Recusar CR isolado, newline duplo, segunda linha, coluna de nome ou CXSMILES. Não strip da entrada para fazê-la passar.

Usar SmilesParserParams com sanitize=True, removeHs=False, parseName=False e allowCXSMILES=False; todos quatro defaults observados são True. Exigir Mol não None. Não chamar assinatura de construtor com kwargs cuja existência não foi comprovada: criar parâmetros e atribuir os quatro campos suportados.

### 7.3 Elegibilidade do grafo

Mol não vazio, limites da§6, um componente conectado. Rejeitar átomo dummy/atomic number0, query em átomo/ligação, SGroup/estrutura polimérica e estereogrupos enhanced AND/OR. Não escolher fragmento, neutralizar, desprotonar, dessalinizar, gerar tautômero ou atribuir novo estereoisômero a centro indefinido. Estereoquímica explícita, isótopos e cargas são interpretados pelo parser pinado sob o perfil declarado e devem ser preservados.

A rejeição de uma forma salina desconectada não autoriza sugerir ácido/base livre como se fosse o mesmo estado. Mensagem pública deve mencionar a exigência de um componente e que nenhum componente foi selecionado/removido. Não modificar a representação ou o RAW original.

## 8. Perfil científico fechado

Identificador: `molecular-characterization-v1`. Engine name rdkit; versão efetivamente observada obrigatória **2026.03.6**; declaração de dependência continua rdkit==2026.3.6. Versão ausente/incompatível recusa configuração, sem usar outro motor. Não instanciar TautomerEnumerator ou reutilizar seus parâmetros para resolver caracterização.

| Campo de Values | Método explícito | Tipo/unidade | Default Python do pin versus escolha |
|---|---|---|---|
| formula | rdMolDescriptors.CalcMolFormula(mol, separateIsotopes=True, abbreviateHIsotopes=False) | str não vazia | Defaults False/True; ambos desvios deliberados para explicitar isótopos, sem abreviar D/T |
| molar_mass_g_mol | Descriptors.MolWt(mol) | float finito positivo; g/mol | Nenhum kwarg fornecido; wrapper público conserva o default interno onlyHeavy=False do pin |
| exact_mass_da | rdMolDescriptors.CalcExactMolWt(mol, onlyHeavy=False) | float finito positivo; Da | onlyHeavy=False coincide com default |
| formal_charge_e | Chem.GetFormalCharge(mol) | int estrito, com sinal; carga elementar | Nenhum parâmetro opcional fornecido |
| heavy_atom_count | mol.GetNumHeavyAtoms() | int estrito não negativo | Nenhum parâmetro opcional fornecido |
| hbd_count | rdMolDescriptors.CalcNumHBD(mol) | int estrito não negativo | Nenhum parâmetro opcional fornecido |
| hba_count | rdMolDescriptors.CalcNumHBA(mol) | int estrito não negativo | Nenhum parâmetro opcional fornecido |
| rotatable_bond_count | rdMolDescriptors.CalcNumRotatableBonds(mol, strict=rdMolDescriptors.NumRotatableBondsOptions.Strict) | int estrito não negativo | Overload enum tem default Default; Strict é seleção explícita, sem afirmar resultado diferente de Default no pin |
| tpsa_a2 | rdMolDescriptors.CalcTPSA(mol, force=True, includeSandP=False) | float finito não negativo; Å² | force=True desvia de False para recalcular; includeSandP=False coincide com default |
| clogp_wildman_crippen | rdMolDescriptors.CalcCrippenDescriptors(mol, includeHs=True, force=True)[0] | float finito com sinal; adimensional | includeHs=True coincide com default; force=True desvia de False para recalcular |

A tabela documenta todos os parâmetros opcionais efetivamente selecionados neste perfil e os métodos sem kwargs fornecidos. Não implica que toda a configuração interna da biblioteca foi transformada em parâmetros públicos. Defaults são do binding Python2026.03.6, não de C++ puro ou de documentação de outra versão. Os desvios de force controlam recálculo/cache; não são uma preparação química.

`Descriptors.MolWt` é a API pública escolhida para massa molar média; no pin, seu source Python encaminha a `_rdMolDescriptors._CalcMolWt`. O nome com underscore é evidência de implementação, não API privada autorizada ao novo adaptador. Não exigir namespace único artificial: carga formal pertence a Chem e contagem de átomos ao Mol, como já consta da tabela. Conservar a API pública MolWt; não substituir por CalcExactMolWt, que calcula outra grandeza.

Namespace Crippen.CalcCrippenDescriptors não será usado. HBD/HBA são os métodos também chamados por Lipinski.NumHDonors/NumHAcceptors no pin; não rotular como contagem de ligações N–H/O–H nem substituir por NHOHCount/NOCount. Fórmula distingue isótopos de H sem abreviação D/T.
Não arredondar dados de máquina antes do DTO/JSON. Valores não finitos, tipos incoerentes ou falha em qualquer descritor encerram a operação; não substituir por zero/null nem retornar ficha parcial. Caches internos do RDKit podem ser preenchidos; conectividade, isótopos, cargas e estereoquímica do grafo de entrada não podem ser modificados por pré-processamento oculto.

Condições experimentais **não são carregadas nem consumidas**. Informar experimental_conditions_consumption="not-consumed". Não inferir pH, pKa, logD, solubilidade, atividade/toxicidade ou adequação para docking. MolWt respeita a política do RDKit para isótopos marcados; massa média/molar e massa exata não são m/z experimental ou de aduto. Carga formal não é carga parcial. Os valores pertencem ao estado analisado, podendo mudar entre estados.

## 9. Perfil de desenho

Somente quando include_svg=True. Perfil `molecular-depiction-v1`, canvas600×400. Mol de desenho é cópia de trabalho; coordenadas de apresentação não são novo Conformer nem geometria experimental. Não escrever SDF com essas coordenadas.

| Etapa/superfície real | Parâmetros/atributos fixos | Default Python do pin versus escolha |
|---|---|---|
| rdDepictor.Compute2DCoords(mol, ...) | canonOrient=True, clearConfs=True, coordMap={}, nFlipsPerSample=0, **nSample=0**, sampleSeed=0, permuteDeg4Nodes=False, bondLength=-1.0, forceRDKit=True, useRingTemplates=False | Todos coincidem com defaults, exceto forceRDKit=True, que desvia de False para usar RDKit mesmo se CoordGen estiver preferido |
| rdMolDraw2D.PrepareMolForDrawing(mol, ...), cópia com coordenadas | kekulize=False, addChiralHs=False, wedgeBonds=True, forceCoords=False, wavyBonds=False | kekulize/addChiralHs desviam de True/True para evitar essas preparações; os outros três coincidem com defaults |
| Construtor rdMolDraw2D.MolDraw2DSVG | width=600, height=400, panelWidth=-1, panelHeight=-1, noFreetype=False | width/height são obrigatórios, sem default; os três opcionais coincidem com defaults |
| drawer.drawOptions(), atribuições após construir drawer | prepareMolsBeforeDrawing=False, includeMetadata=False, includeAtomTags=False, addAtomIndices=False, addBondIndices=False | Os dois primeiros desviam de True/True; os três últimos coincidem com defaults False |
| drawer.drawOptions().fontFile | Caminho interno fixado pela política Telex descrita abaixo | Default observado é string vazia; desvio explícito para asset da instalação, sem entrada de usuário |
| drawer.DrawMolecule(mol, legend="") | Mol preparado, legend=""; nenhum highlight fornecido | legend vazio coincide com default; não é parâmetro do construtor nem de MolDrawOptions |

As superfícies não são intercambiáveis: não passar atributos de MolDrawOptions ou legend como kwargs de MolDraw2DSVG. Construir drawer, configurar options/fontFile, chamar DrawMolecule, finalizar desenho e obter o SVG. Demais opções gráficas não selecionadas ficam nos defaults do pin, sem modificação de configuração global; não se promete reprodutibilidade entre versões/builds/SOs por enumerar estes parâmetros.

`coordMap={}` deve ser mapa vazio novo por chamada, sem ancoragem recebida do cientista; bondLength=-1.0 seleciona a política padrão de comprimento do backend pinado, não fixa uma distância física experimental. Ambos coincidem com defaults reais, agora explícitos. **usePathAngleExpansion não pertence ao binding Python2026.03.6 observado e não deve ser passado nem declarado como parâmetro efetivo.** A documentação atual2026.09.1 expõe esse nome; não importar sua assinatura para o pin nem fazer fallback por tentativa/erro.
Preservar H explícitos/isotópicos. Não usar AddHs/RemoveHs ou kekulização como preparação escondida; permitir wedges como apresentação da estereoquímica já definida. Omitir na cópia apenas propriedades de anotação atomLabel, _displayLabel, _displayLabelW, molFileAlias, atomNote, bondNote e _MolFileRLabel. Não alterar campos químicos ou apagar estereogrupo para aceitar entrada inelegível. Não inserir nome/título/SD data como texto, legenda ou markup.

Comparar assinatura do grafo antes/depois da preparação: átomos por índice, números atômicos, isótopos, cargas formais, contagens de H explícitos/implícitos e conectividade/ordens aromáticas; preservar estereoquímica semântica por checagem canônica isomérica nos casos aplicáveis. Direções gráficas de wedge e conformer interno de desenho podem mudar; os elementos químicos não. Inconsistência implica erro de desenho, sem resultado parcial. O Mol de cálculo permanece cientificamente inalterado.

Fonte: arquivo `Path(RDConfig.RDDataDir)/"Fonts"/"Telex-Regular.ttf"` da instalação RDKit; não receber caminho de fonte do usuário. Exigir arquivo regular disponível, observar SHA-256 de seus bytes e atribuir fontFile explicitamente. O arquivo observado no estudo tem38.940 bytes e hash eeaa2d17d105b6b46e5368ecd990f5b19c50131ff922dbf79bfb9bb45c249871. Esse hash é evidência Linux, não prova automática do wheel Windows. Registrar o hash efetivo no resultado; não inventá-lo, não fixar um hash diferente por SO sem registro e não usar fallback silencioso. Ausência da fonte/backend de desenho é CONFIGURATION ERROR somente quando figura solicitada.

Não adicionar PNG, navegador, HTML, fonte remota ou dependência gráfica externa. A fonte existente tem licença fornecida SIL OFL1.1; o incremento não redistribui fonte ou motor à parte. Não prometer SVG byte-idêntico entre SOs/builds. A figura pode ficar carregada por H explícitos; não simplificar quimicamente para torná-la mais bonita.

## 10. SVG validado por perfil fechado

O SVG do produtor RDKit é saída ainda não liberada ao usuário. Validar antes de devolver/serializar o resultado. Não importar SVG externo nem construir sanitizador geral.

Parser: `xml.parsers.expat`, com instância nova por documento e namespace processing habilitado. Instalar recusas em StartDoctypeDeclHandler, EntityDeclHandler e ExternalEntityRefHandler; SetParamEntityParsing(XML_PARAM_ENTITY_PARSING_NEVER) deve ser bem-sucedido e UseForeignDTD(False) deve permanecer. O handler externo nunca abre arquivo/rede nem cria child parser. Recusar processing instructions além da declaração XML; comentários podem ser ignorados e não serão copiados. Texto entre elementos deve ser apenas whitespace ASCII. Não desativar proteções nativas de tokens/reparse deferral quando presentes. Falta da configuração necessária é CONFIGURATION ERROR para figura, sem fallback de parser.

Uma busca textual de DOCTYPE/ENTITY pode ser diagnóstico adicional, mas não é a garantia principal. DTD é recusada pelo callback antes de processar declarações; entidades XML predefinidas são permitidas somente se o valor resultante continuar dentro da gramática do atributo. Não fazer segunda leitura por parser permissivo. Limitar o buffer antes do parse e o SVG final serializado. O limite de bytes e a configuração não provam imunidade universal a DoS.

A string produzida pelo motor é tratada como Unicode, alimentada ao parser em UTF-8 com encoding explicitamente fixado. A declaração histórica ISO-8859-1 do produtor é tolerada neste fluxo, pois os campos/valores permitidos pelo perfil são ASCII; rejeitar conteúdo não ASCII nos valores liberados. Serializar a estrutura validada de saída como UTF-8, com declaração coerente UTF-8. Não copiar uma declaração de encoding incompatível para o usuário.

### 10.1 Elementos, atributos e geometria

Somente elementos svg/rect/path no namespace `http://www.w3.org/2000/svg`. Raiz única svg; seus filhos podem ser rect/path, ambos sem filhos. Não permitir texto, foreignObject, image, use, script, animação ou elemento de outro namespace. Declarações xmlns/xlink não usadas do produtor não causam acesso remoto; seus atributos href/xlink:href continuam proibidos. Namespace URI não é recurso a baixar.

| Elemento | Atributos do produtor permitidos |
|---|---|
| svg | version, baseProfile, width, height, viewBox, xml:space |
| rect | x, y, width, height, style, fill |
| path | d, class, style, fill |

Exigir raiz version=1.1, width=600px, height=400px e viewBox numérico0 0 600 400. baseProfile, se presente, full; xml:space, se presente, preserve. Campos geométricos do rect são números finitos, width/height não negativos, sem unidades inesperadas. fill deve ser none ou cor hexadecimal de seis dígitos. class, se presente, é sequência de tokens `atom-N`/`bond-N`, separados por espaços ASCII, N inteiro não negativo; não aceitar classes arbitrárias.

`d` usa o perfil reduzido observado deste produtor/fonte: comandos absolutos **M, L, Q**, com números finitos e separadores ASCII de whitespace/vírgula. Número: sinal opcional, decimal com pelo menos um dígito e expoente e/E opcional. M/L recebem pares de coordenadas; Q recebe grupos de quatro; o primeiro comando deve ser M, com pelo menos um par. Permitir grupos repetidos segundo essas aridades, sem tokens residuais, comandos relativos ou outros comandos. Não avaliar expressões. Este recorte foi confrontado com os cinco desenhos disponíveis; saída que exija comando não coberto falha explicitamente, sem ampliar o perfil silenciosamente. O checkpoint Windows deverá verificar sua compatibilidade real. Em T-020A-051, incluir pelo menos um canário policíclico aromático fundido fora dos cinco exemplos originais: antraceno, SMILES `c1ccc2cc3ccccc3cc2c1`. O ensaio Linux desta resposta observou apenas M/L nesse caso; ele não comprova o backend/validador de produção Windows. Qualquer incompatibilidade deve ser relatada, sem ampliar silenciosamente a gramática.

style é lista de declarações nome:valor separadas por `;`, com whitespace ASCII opcional e um terminador vazio final permitido. Recusar duplicação de propriedade, declaração vazia interna, escapes, comentários, variáveis, funções, @import, url(...) e propriedade desconhecida. Vocabulário fechado:

| Propriedade | Valor permitido |
|---|---|
| fill, stroke | none ou #RRGGBB, dígitos hex |
| opacity, stroke-opacity | número finito em[0,1] |
| fill-rule | evenodd ou nonzero |
| stroke-width | número finito não negativo, com px opcional |
| stroke-linecap | butt, round, square |
| stroke-linejoin | miter, round, bevel |
| stroke-dasharray | none ou lista não vazia de números finitos não negativos, com pelo menos um positivo |
| stroke-miterlimit | número finito >=1 |

Qualquer atributo não enumerado, event handler, href, URI em valor que não seja namespace declarado ou conteúdo ativo resulta em recusa. Não remover apenas o trecho indevido e afirmar sucesso.

### 10.2 Vínculo e serialização

O adaptador recebe contexto neutro, validado pelo serviço: input_state_id e checksum observado da representação. Deve incluir na raiz final, sem paths absolutos:

- data-state-id: ID validado;
- data-representation-sha256: hash observado lowercase;
- data-engine-version: versão real do motor;
- data-profile: molecular-depiction-v1.

Esses quatro atributos são próprios, acrescentados por código controlado; nenhum valor pode vir de SD data ou de chave livre de usuário. O adaptador confere o hash fornecido contra os bytes recebidos; não confunde esse controle em memória com nova leitura de arquivo. Gerar/validar/serializar dentro da mesma chamada. Pode-se construir árvore neutra pelo fluxo protegido e usar somente serialização XML, sem nova etapa de parsing. Escapar atributos corretamente; nenhuma concatenação de texto de origem livre como markup.

O SHA-256 e tamanho do SVG no DTO correspondem aos bytes UTF-8 **finais**, já com os quatro atributos. Verificar novamente tamanho final. Não alegar que o hash do SVG puro de um spike antigo é o hash desse novo SVG vinculado ao estado. O SVG isolado contém vínculo básico; a proveniência completa é obtida em JSON, não há arquivo acompanhante criado automaticamente.

## 11. Contrato dos dados retornados

DTOs públicos frozen, extra=forbid, com validação estrita, sem dict científico irrestrito e sem objetos do motor. Usar modelos fechados também nos blocos de parâmetros/drawing. Nomes privados auxiliares não são a identidade de domínio; o JSON público é o descrito abaixo.

MolecularCharacterizationResult possui exatamente estas chaves de primeiro nível:

| Chave | Valor |
|---|---|
| schema_version | Literal"1.0", apenas schema novo da resposta |
| values | Os dez campos fechados da§8 |
| provenance | Objeto abaixo |
| warnings | Lista ordenada de códigos do vocabulário abaixo |
| drawing | null sem figura, objeto fechado com figura |
| svg | null sem figura, string com figura |

Provenance:

| Campo | Restrição |
|---|---|
| input_state_id, entity_id | IDs validados; sujeitos ao registro capturado |
| state_schema_version | Schema do estado validado,1.0 nesta baseline |
| state_record_sha256_observed | Hex64 lowercase do buffer YAML observado |
| representation_path | Referência relativa autorizada; não source path externo |
| representation_format_declared | Valor original do registro |
| representation_format_resolved | Literal sdf/smiles |
| representation_checksum_expected | Hex64 na grafia do registro |
| representation_checksum_observed | Hex64 lowercase, igualdade com expected por case-insensitive |
| representation_size_bytes | Inteiro positivo, tamanho do buffer verificado |
| engine_name | Literal rdkit |
| engine_version | Versão real observada,2026.03.6 neste perfil |
| application_version | Versão instalada da distribuição molecular-platform, str não vazia ou null se PackageNotFoundError; não executar git em produção para preenchê-la |
| characterization_profile_id | Literal molecular-characterization-v1 |
| effective_parameters | Objeto fechado com formato resolvido, opções de parsing e de todos os métodos da§8; nomes/valores fixos reproduzíveis, sem extras |
| experimental_conditions_consumption | Literal not-consumed |

effective_parameters contém, em blocos tipados: parser(format/sanitize/removeHs/strictParsing para sdf OU format/sanitize/removeHs/parseName/allowCXSMILES para smiles); formula(separateIsotopes/abbreviateHIsotopes); exact_mass(onlyHeavy); rotatable_bonds(option="Strict"); tpsa(force/includeSandP); crippen(includeHs/force). Demais métodos têm seu nome de método fixo no perfil; não inventar parâmetros de requested/resolved de tautomerização. O discriminante de formato determina o bloco parser, sem campos não operantes do outro formato.

drawing, quando presente, contém: profile_id=molecular-depiction-v1; width_px=600; height_px=400; font_name=Telex-Regular.ttf; font_sha256_observed; svg_sha256; svg_size_bytes; xml_parser="xml.parsers.expat"; xml_parser_version_observed. Seu effective_parameters contém exatamente os blocos fechados abaixo, separando as superfícies da§9:

| Bloco | Campos e valores |
|---|---|
| compute2d | canonOrient=True, clearConfs=True, coordMap={}, nFlipsPerSample=0, nSample=0, sampleSeed=0, permuteDeg4Nodes=False, bondLength=-1.0, forceRDKit=True, useRingTemplates=False |
| prepare | kekulize=False, addChiralHs=False, wedgeBonds=True, forceCoords=False, wavyBonds=False |
| drawer | width=600, height=400, panelWidth=-1, panelHeight=-1, noFreetype=False |
| draw_options | prepareMolsBeforeDrawing=False, includeMetadata=False, includeAtomTags=False, addAtomIndices=False, addBondIndices=False, font_policy="rdkit-data-fonts-telex" |
| draw_molecule | legend="" |
| svg_validation_profile | Literal svg-static-v1 |

Cada bloco é DTO frozen/extra=forbid; coordMap é objeto vazio fechado, também frozen/extra=forbid e sem campos, serializado como `{}` — não dict arbitrário ou mapa mutável compartilhado. As constantes usam tipos estritos. font_policy identifica a resolução interna da§9; a identificação efetiva da fonte usa font_name/font_sha256_observed de drawing. Não serializar o caminho absoluto efetivamente atribuído a fontFile. Nenhum campo usePathAngleExpansion é aceito. Identificadores/hashs são estritos; bool não é aceito como inteiro de contagem.

Warnings, na ordem: derived-computational-values; conditions-not-consumed; no-durable-query-record; tpsa-no-additional-s-p; acrescentar generated-2d-not-conformer somente se houver SVG. O renderer text explica esses códigos em linguagem clara. Não copiar warnings nativos arbitrários do motor como mensagem pública.

Invariantes cruzadas: sem SVG ⇒ drawing=null; com SVG ⇒ ambos presentes, hash/tamanho corretos, perfil/atributos vinculados ao input e ao motor. Propriedade faltante/inválida de adaptador é falha, não valor default científico. Hash do YAML não comprova autenticidade ou todo o lineage; application_version não é prova de identidade do commit. Não criar identificador persistente/timestamp de execução.

## 12. Fluxo do serviço e precedência

API pública no módulo novo:

```text
characterize_state(project_dir, *, input_state_id, include_svg=False)
```

include_svg é bool estrito. O fluxo, sem retry:

1. Validar pedido/ID; entradas malformadas não abrem arquivos nem invocam motor.
2. Ler metadata pelo primeiro leitor verificado; interpretar/validar registro, identidade e formato.
3. Validar referência/checksum; ler representação pelo segundo leitor. Nomes reservados e reparse points valem também no primeiro arquivo.
4. Chamar **uma vez** `characterize_molecule_rdkit` com representation_bytes, input_format resolvido, include_svg e contexto neutro(input_state_id/representation_sha256_observed). Essa extensão explícita da assinatura da§4 serve somente ao vínculo gráfico da§10.2, não fornece ao motor capacidade de carregar registros.
5. No adaptador: resolver dependência/versão; validar gramática; parsear uma vez; checar elegibilidade/limites; calcular os dez valores; se pedido, produzir/preparar/validar/vincular SVG. Não reabrir arquivo nem instanciar enumerador.
6. Serviço valida o outcome neutro, captura application_version quando disponível e constrói resultado/proveniência fechados a partir dos buffers/registro capturados. Não confiar em IDs ou checksums arbitrários retornados por engine para substituir os da entrada.
7. Retornar somente o resultado completo. Não fazer reload de estado, de attempt ou de transformação; não procurar arquivo/registro alternativo.

Precedência observável: ID/pedido inválido antecede plataforma/I/O; metadata antecede formato/referência; representação verificada antecede engine; parsing antecede cálculos; cálculos antecedem desenho; montagem/validação completa antecede saída. Se dois defeitos coexistirem, aparece o primeiro alcançado por esse fluxo. Não exigir resolução de engine para rejeitar bytes que já falharam na leitura verificada.

## 13. Taxonomia de falhas proposta

Erros próprios, definidos incondicionalmente em characterization.py e utilizáveis sem RDKit. Base CharacterizationError; subclasses de categoria CharacterizationInputError, CharacterizationConfigurationError, CharacterizationStorageError e CharacterizationExecutionError. Cada uma possui reason do vocabulário fechado desta tabela e input_state_id somente quando já validado. Preservar causa original por exception chaining; não construir mensagem pública de str(cause).

| Categoria/banner | reason | Situação |
|---|---|---|
| INPUT ERROR | invalid-request | ID de formato inválido, include_svg inválido, format/combinação CLI inválidos |
| CONFIGURATION ERROR | unsupported-platform | SO/volume não suportado ou indeterminado |
| CONFIGURATION ERROR | invalid-state-record | UTF-8/YAML/schema/ID do registro inválido |
| CONFIGURATION ERROR | unsupported-format | Formato resolvido não aceito |
| CONFIGURATION ERROR | invalid-reference | Path/checksum de forma inválida, nome reservado/inválido |
| CONFIGURATION ERROR | engine-unavailable | Dependência de cálculo ausente/incompatível ou versão não verificável |
| CONFIGURATION ERROR | drawing-unavailable | Fonte/backend/parser exigido para figura ausente ou não configurável |
| STORAGE ERROR | missing-artifact | Metadata ou representação ausente |
| STORAGE ERROR | unreadable-artifact | OSError/PermissionError na abertura/leitura/checagem, não abrangido acima |
| STORAGE ERROR | unsafe-or-changed-artifact | Reparse, tipo não regular, identidade/ancestral substituído ou atributos de segurança ausentes |
| STORAGE ERROR | checksum-mismatch | Hash da representação divergente |
| STORAGE ERROR | artifact-size-invalid | Arquivo vazio, tamanho excedido ou quantidade lida divergente |
| EXECUTION ERROR | invalid-chemical-input | Gramática/codificação química inválida, parsing None ou cardinalidade incompatível |
| EXECUTION ERROR | unsupported-structure | Grafo desconectado/vazio/query/dummy/SGroup/estereogrupo não aceito |
| EXECUTION ERROR | molecular-size-limit | Átomos/ligações excedem limite |
| EXECUTION ERROR | descriptor-failure | Método falha ou valor não finito/tipado corretamente |
| EXECUTION ERROR | depiction-failure | Desenho, invariantes do grafo, XML/vocabulário/limite de SVG inválidos |
| EXECUTION ERROR | invalid-engine-result | DTO inconsistente ou resultado neutro divergente das entradas |
| EXECUTION ERROR | internal-failure | Exceção inesperada na borda pública do comando, sem resultado parcial |

O reason identifica uma falha, não máquina de estados de attempt. Mensagens públicas são templates controlados por reason; incluir Input state quando validado e instrução acionável sem detalhes sensíveis. Não incluir traceback, path absoluto, texto de SDF/YAML, versão ilegível arbitrária ou exceção nativa bruta. Retain chaining em memória não autoriza serializar causa no JSON público.

Handlers tipados precedem guard final `except Exception` restrito ao corpo do novo comando: ele serve somente para emitir internal-failure sem vazar traceback de falha inesperada. Não tratar isso como sucesso, fallback, retry ou persistência de falha científica. Não adicionar esse guard aos outros comandos. KeyboardInterrupt/SystemExit/GeneratorExit não entram nessa captura.

Recursos são fechados por context manager/finally. Captura de BaseException é admissível só para liberar recurso próprio e relançar, preservando a interrupção; não usar para classificação de negócio. Nenhuma compensação de registros/artefatos existentes é executada. Logs RDKit são suprimidos por escopos mínimos de chamada de biblioteca no caminho novo, com restauração em sucesso/exceção/interrupção; bloco Enumerate legado permanece exclusivo da enumeração. Sem DisableLog global no import ou alteração global permanente. A execução síncrona CLI por processo não promete segurança de logger em uso concorrente por threads.

## 14. CLI e apresentação

Novo subcomando, mantendo resolução atual por ID lógico:

```text
molecular state characterize <experiment_id> --input-state <state_id> [--format text|json|svg] [--include-svg]
```

Default text. Valores de format são strings validadas pelo handler novo para produzir INPUT ERROR/exit1 em escolha inválida; não normalizar case/whitespace da opção para aceitar algo não declarado. include-svg é flag bool aceita somente com format=json. format=svg implica include_svg=True; text e json sem flag implicamFalse. Validar combinação/ID antes da resolução do experimento; resolver pelo context.resolve_experiment atual a partir do diretório-base, sem reinterpretar experiment_id como path.

Para um pedido válido/resolvido, chamar characterize_state exatamente uma vez. Comando não lê representação, não calcula descritor nem inspeciona execution_attempts. Falha de resolução usa as categorias existentes: experimento ausente/ambíguo→INPUT ERROR; configuração recuperável inválida→CONFIGURATION ERROR; falha de acesso ao base_dir→STORAGE ERROR. Não alterar o resolver compartilhado. Mensagens desse caminho novo também usam templates controlados, sem interpolar experiment_id arbitrário ou str(error) que possa conter um path; a validade do experiment_id não é presumida pela regex de state_id.

stdout:

| Modo | Conteúdo |
|---|---|
| text | Ficha completa, identidade, engine/perfil, dez valores e unidades, checksum observado, avisos explicados |
| json | Um objeto da§11; sem banner de sucesso, preâmbulo ou log |
| svg | Um documento SVG final, sem cabeçalho de terminal ou outro texto |

Preparar toda a string de saída antes da primeira escrita. text segue ordem da§8; massas3 casas, TPSA2, cLogP4, contagens inteiras, fórmula sem arredondamento. JSON preserva precisão de máquina; unidades são determinadas pelo schema e nomes de campos. O SVG final deve terminar com exatamente um LF, já incluído em seu hash/tamanho; a CLI escreve essa string sem acrescentar outro terminador. Text/JSON terminam com um LF fora dos valores de máquina.

Erros de negócio: stdout vazio; stderr começa pelo banner, seguido de Reason e, se validado, Input state. Exit0 sucesso, exit1 falha de negócio. Erros sintáticos do framework anteriores à entrada no handler (por exemplo opção desconhecida) preservam o comportamento existente do framework; o contrato0/1 não é uma alteração global do Click/Typer. Ausência dos parâmetros declarados obrigatórios segue essa mesma distinção de uso. --help continua funcionando sem RDKit.

Sem “salvo”, “registrado”, “attempt succeeded” ou “conformero gerado”. A operação devolve uma consulta, não persiste o que o cientista viu. Quebra do pipe durante a escrita não admite rollback do stdout; não prometer ausência de toda escrita parcial do SO. Não abrir browser, escolher output path ou gerar multifile; redirecionamento é captura externa do usuário.

## 15. Imports, persistência e compatibilidade

Manter Python>=3.11 e os extras atuais; não editar pyproject.toml. Todo import direto RDKit novo permanece em rdkit_tautomer.py, atrás de fronteira opcional. A falta de módulos de desenho NÃO deve tornar a enumeração existente indisponível ou impedir text/JSON sem figura. Separar a disponibilidade de cálculo daquela de desenho e não sobrescrever _RDKIT_IMPORT_ERROR legado por um import novo de Draw/RDConfig. Nenhum Mol ou tipo nativo aparece nos DTOs, serviço, atomic ou CLI.

A operação não cria diretório, snapshot/staging temporário ou arquivo de saída no experimento. O adaptador pode ler a fonte tipográfica conhecida da instalação confiada; isso não é autorização para ler outro arquivo científico externo. Não alterar activity logs/attempts nem gravar falha/sucesso de consulta. Consultas simultâneas em processos separados não disputam IDs de saída; não chamar isso de reuse persistente ou transação idempotente. Não suportar concorrência de threads como novo contrato.

Preservar integralmente os contratos016/017: resolução/enumeração e parâmetros científicos, error handoff, persistência terminal, compensação, logger e CLI atuais. Preservar promoção018, declarações019 e receptor020. Não alterar schemas persistidos, migrar YAML ou corrigir o roadmap no código. Reprodutibilidade depende da captura de resultado e preservação externa de entrada/ambiente; não há garantia de histórico durável da consulta.

## 16. Matriz candidata de verificação

Os IDs abaixo são **cenários contratuais**, não uma promessa de quantidade de funções ou itens pytest. Parametrizações devem ser reconciliadas no checkpoint por coleta real. Um cenário pode exigir mais de um teste; um teste não comprova cenários que seus asserts não exercitam. Não usar pytest.raises(Exception) genérico ou mock de toda a operação como prova do comportamento real.

| ID | Cenário a exercitar | Resultado exigido |
|---|---|---|
| T-020A-001 | Values, Provenance, Result e blocos internos com campo extra | Recusa tipada, sem campo silenciosamente ignorado |
| T-020A-002 | Tentativa de mutar DTO após construção | DTO imutável |
| T-020A-003 | NaN/inf, bool como contagem, contagem negativa | Recusa; cLogP negativo e carga com sinal continuam válidos |
| T-020A-004 | svg/drawing presentes em combinação inconsistente | Recusa do resultado |
| T-020A-005 | Hash/tamanho SVG ou hash esperado/observado incoerentes | Recusa antes de apresentação |
| T-020A-006 | Instalação sem extra RDKit; imports e --help | Base/CLI existentes funcionam; pedido de cálculo falha configuração |
| T-020A-007 | Versão RDKit ausente/incompatível | CONFIGURATION ERROR, sem parse/cálculo/fallback |
| T-020A-008 | Draw/RDConfig/fonte indisponível, cálculo disponível | text/JSON sem figura funcionam; figura falha configuração; enumeração preservada |
| T-020A-009 | IDs vazios, separadores, traversal, ponto, whitespace, Unicode e tipo não-string | Validador real recusa antes de I/O/engine |
| T-020A-010 | ID válido com hífen/underscore e case | Mesmo token preservado, sem normalização |
| T-020A-011 | CON/NUL/COM/LPT e variantes com extensão | Validade lexical distinguida; leitor recusa filename antes de abrir |
| T-020A-012 | Path de representação absoluto POSIX, drive, drive-relative ou UNC | CONFIGURATION ERROR, sem acesso externo |
| T-020A-013 | Prefixo parecido, outro state_id, nested leaf, segmento vazio ou traversal | Confinamento por componentes recusa |
| T-020A-014 | Leaf com espaço interno/Unicode permitido versus caracteres/trailing inválidos | Aceitar o válido, recusar o inválido sem renomear |
| T-020A-015 | Windows10/Server/versão indeterminada ou SO não Windows | Gate de plataforma recusa antes de arquivo científico |
| T-020A-016 | NTFS local fixo versus FAT/exFAT/share/volume indeterminado | Só perfil confirmado prossegue |
| T-020A-017 | Symlink/junction/outro reparse em arquivo e em cada posição da cadeia | Recusa tanto no YAML como na representação |
| T-020A-018 | Atributos de segurança ausentes, arquivo não regular ou ancestral não diretório | Falha fechada, sem presumir suporte |
| T-020A-019 | Substituição detectada antes/depois de open, entre fstat/lstat ou após leitura | STORAGE ERROR e handle fechado |
| T-020A-020 | Size anunciado diverge, arquivo cresce ou limite é excedido durante streaming | Recusa; não confiar apenas em stat inicial |
| T-020A-021 | Arquivo vazio e limites exatamente N versus N+1, nos dois leitores | Limite inclusivo; vazio/excedido recusado |
| T-020A-022 | Metadata/representação ausente ou PermissionError/OSError | Categoria/reason corretos, causa preservada sem path público |
| T-020A-023 | Hash esperado malformado, uppercase válido e divergente | Forma inválida→config; uppercase equivalente aceita; divergência→storage |
| T-020A-024 | Reabertura no adaptador ou segunda leitura da representação | Teste proíbe efetivamente; só buffer verificado é consumido |
| T-020A-025 | YAML com UTF-8 inválido, schema/extras/tipo inválidos ou ID diferente | CONFIGURATION ERROR; sem representação/engine |
| T-020A-026 | representation.format com normalização aceita, formato desconhecido e extensão enganosa | Decidir pelo campo; sem sniffing/fallback |
| T-020A-027 | SDF real promovido, V2000/V3000 | Um Mol válido, H explícitos preservados |
| T-020A-028 | Dois registros válidos SDF | Recusa, sem escolher primeiro |
| T-020A-029 | Válido+inválido e inválido+válido SDF | Ambos recusados, sem filtrar None |
| T-020A-030 | Sem delimitador, dois delimitadores, delimitador com espaços ou garbage extra | Recusa pela gramática física |
| T-020A-031 | SDF LF/CRLF, EOF válido versus CR isolado/whitespace após registro | Comportamento exato da§7.1 |
| T-020A-032 | BOM, NUL, UTF-8 inválido e SD data Unicode válido | Recusar inválidos; dados válidos não viram markup/metadado químico |
| T-020A-033 | Substring $$$$ em propriedade e linha exata de delimitador | Contagem por linha, sem contagem ingênua de substring |
| T-020A-034 | SMILES de estado filho real da enumeração, com LF | Aceitar sem perder identidade do estado/entidade |
| T-020A-035 | SMILES sem terminador ou com um CRLF | Aceitar mesma química sob perfil |
| T-020A-036 | CR isolado, newline duplo, segunda linha, espaços, nomes/colunas ou CXSMILES | Recusar, sem strip/parseName implícito |
| T-020A-037 | ASCII inválido/BOM/NUL/DEL/controle no SMILES | Recusa antes de parsing químico |
| T-020A-038 | Mol None, grafo vazio, desconectado/sal | EXECUTION ERROR; nenhum fragmento removido/substituído |
| T-020A-039 | Dummy/query em átomo/ligação, SGroup ou AND/OR | Recusa do perfil, sem apagar para aceitar |
| T-020A-040 | Átomos/ligações exatamente no teto versus teto+1 | Perfil/erro corretos; não mascarar como tempo limite do motor |
| T-020A-041 | Cafeína de fixture fixada | Dez valores de referência com unidade e precisão de máquina |
| T-020A-042 | Ácido rosmarínico, imidacloprido, diclofenaco e atrazina, entradas fixadas | Caracterização não enumera tautômeros; valores/proveniência verificáveis |
| T-020A-043 | H isotópico e13C | Fórmula distingue isótopos e massas correspondem ao perfil |
| T-020A-044 | Amônio/acetato e formas carregadas | Carga formal preservada; sem neutralização nem m/z experimental |
| T-020A-045 | Metilamina/amônia/diamina | HBD=1/1/2 nas APIs escolhidas; não trocar por NHOHCount=2/3/4 |
| T-020A-046 | Fixture discriminante Strict versus NonStrict | Resultado do Strict explícito comprovado, sem apenas ler nome do preset |
| T-020A-047 | S/P nas fixtures do estudo | TPSA do perfilFalse; varianteTrue difere, comprovando parâmetro |
| T-020A-048 | Método de descritor falha ou retorna não finito | Operação falha, sem zeros/null/resultado parcial |
| T-020A-049 | Centros definidos/indefinidos e E/Z | Preservação; não enumerar/atribuir estado novo |
| T-020A-050 | Arquivo/Mol antes e depois dos cálculos | Bytes/grafo preservados; cache interno não confundido com mutação científica |
| T-020A-051 | Desenho nos cinco exemplos, sondas de carga/isótopo/estereo e canário antraceno fora do conjunto original | SVG válido no perfil, parâmetros das superfícies corretas e inspeção visual Windows registrada |
| T-020A-052 | Preparação gráfica com H explícito/isotópico e centro quiral | Sem H novo/removido; invariantes do grafo e estereo preservados |
| T-020A-053 | Preferência global CoordGen diferente | forceRDKit=True continua efetivo; sem toggle global do processo |
| T-020A-054 | Fonte real localizada, hash e configuração fontFile | Evidência Windows do arquivo usado; sem hash inventado/fallback |
| T-020A-055 | atomLabel/atomNote/bondNote/SD title hostis | Omitidos na cópia; nenhum markup/label livre reaparece |
| T-020A-056 | Texto/JSON sem SVG e falha injetada só no drawing | Desenhador não é chamado; cálculo independente continua |
| T-020A-057 | DTD interna/externa, entidade externa, DOCTYPE em encoding alternativo | Recusa no parser; nenhum recurso externo aberto |
| T-020A-058 | Entidades XML predefinidas e entidade indefinida | Predefinida sujeita à gramática; indefinida recusada |
| T-020A-059 | Elemento/namespace/atributo ativo, href, PI ou texto não permitido | Recusa, sem limpeza parcial com sucesso |
| T-020A-060 | CSS url/import/escape/duplicado/propriedade desconhecida | Recusa; estilos estáticos válidos passam |
| T-020A-061 | Path d com token/arity/valor não finito/comando fora do perfil | Recusa; M/L/Q válidos passam |
| T-020A-062 | SVG no limite e limite+1 antes/depois do vínculo | Respeitar teto final UTF-8 |
| T-020A-063 | Vínculo de origem na raiz e metadados drawing | IDs/hash/engine/perfil conferem com entrada; sem caminho absoluto |
| T-020A-064 | Qualquer falha de desenho/validação quando SVG foi pedido | Nenhuma ficha/sucesso parcial retornado |
| T-020A-065 | Serialização XML normalizada | UTF-8 coerente, root/atributos válidos, hash inclui bytes finais exatos |
| T-020A-066 | Serviço completo com registro real e leitores/adaptador de produção | DTO corresponde aos buffers; fixture não troca motor inteiro por mock tautológico |
| T-020A-067 | Contagem de invocações e resultados de fonte divergentes | Adaptador uma vez; recusar outcome inválido; nenhum reload/retry |
| T-020A-068 | Consulta repetida/simultânea em processos diferentes | Sem arquivo/registro/attempt/log novo ou alteração de existentes |
| T-020A-069 | Declaração de condições presente versus ausente | Não carregada/consumida; nenhum pH inferido; metadado not-consumed |
| T-020A-070 | CLI text completo | Dez valores/unidades/avisos, ordem e arredondamento só de apresentação |
| T-020A-071 | CLI JSON sem/com figura | Um JSON parseável, sem preâmbulo/log e precisão preservada |
| T-020A-072 | CLI SVG | Documento isolado; hash/tamanho correspondem ao que é emitido |
| T-020A-073 | --include-svg com text/svg, formato inválido ou ID inválido | INPUT ERROR/exit1 antes do serviço; ausência de required args segue framework |
| T-020A-074 | Cada categoria tipada de falha e erro inesperado no comando novo | stderr controlado, stdout vazio, exit1; nenhuma exceção arbitrária pública |
| T-020A-075 | Erros que contêm Windows/POSIX paths e texto químico/URLs na causa | Mensagem por template não vaza causa nem precisa corromper texto com regex genérica |
| T-020A-076 | KeyboardInterrupt durante cada fase | Interrupção preservada; handles/logs restaurados; sem compensação/persistência |
| T-020A-077 | SystemExit durante cada fase, separadamente | Mesma garantia verificada por teste separado/parametrização real |
| T-020A-078 | LogWarningMsg após sucesso, exceção e interrupção | capfd/subprocesso comprova restauração de logs RDKit |
| T-020A-079 | Imports e comandos antigos sob dependências completas e opcionais ausentes | Fronteiras e comportamentos legados preservados |
| T-020A-080 | Regressões cumulativas016–020 e estado do projeto após consulta/falha | Sem mudança científica, handler legado, attempt/status, registry ou contrato antigo |

A fonte/proveniência das fixtures deve estar identificada, com valores esperados justificados. Não confundir scripts de pesquisa da arquitetura com asserts de código de produção. Testes de filesystem críticos devem parametrizar os dois leitores. Capfd/subprocesso, não CliRunner.output misturado, comprova stderr nativo/logs. Mocks são apropriados para substituir stat/erro no ponto de uso, mas não substituem o teste real no perfil Windows aceito.

Reconciliar no relatório: cenário→arquivo/função→parâmetros→itens coletados→resultado. Não somar funções com itens coletados como se fossem a mesma unidade. Não fixar incremento esperado de passed antes da implementação/coleta real. Registrar skips e seu motivo; casos Windows indisponíveis em Linux não comprovam suporte por skip.

## 17. Vetores e limites da evidência disponível

As sondas arquiteturais usaram RDKit2026.03.6/Python3.12.14/Linux, fora do clone: cinco RAWs identificados por hash, descritores, SVGs, 17 casos SMILES, oito casos SDF sintéticos e sondas adicionais. A reconciliação confirmou nSample, arquivo Telex,21 entradas do validador real e sete casos de política XML. Isso fundamenta chamadas e escolhas; não executou o serviço, leitor ou CLI futuros nem pytest desta funcionalidade.

A sonda adicional `verify_draft_review.py` desta resposta executou o binding2026.03.6, registrou docstrings/defaults/source de MolWt, comprovou recusa do kwarg usePathAngleExpansion e confirmou que os cinco SVGs continuam byte-idênticos no mesmo ambiente ao explicitar coordMap/bondLength e os defaults do construtor/legend. Também recalculou os dez valores de cafeína e inspecionou comandos do desenho de antraceno. Evidência em `draft-review-verification.json`; não equivale a teste do serviço/validador Windows nem a execução de pytest de produção.

Vetor de referência do estudo para a fixture de cafeína, condicionado aos bytes/sha do RAW registrado na evidência: fórmulaC8H10N4O2, molar_mass194.194, exact_mass194.08037556, formal_charge0, heavy_atoms14, HBD0, HBA3, rotatable0, TPSA61.82, cLogP−1.0293. Nos floats, usar tolerância absoluta documentada de1e−8 para comparação do vetor, mantendo o valor de máquina no resultado; inteiros/fórmula exatos. Isso é referência computacional do perfil, não dado experimental. As fixtures S/P e de isótopos estão no pacote de evidência, com métodos/valores explícitos.

A implementação deve exercitar também um **MolecularState SDF realmente registrado** e um **MolecularState SMILES realmente publicado pela enumeração**; chamar o adaptador sobre RAW não é substituto dessa integração. Para Windows, registrar OS/build, Python, FS/drive, versões RDKit/Expat, fonte e checksums. Não reutilizar resultados de teste do020 como execução independente do020-A.

## 18. Allowlist candidata e checkpoints

Allowlist proposta para implementação futura, a revisar antes do congelamento:

| Produção | Testes |
|---|---|
| src/molecular/characterization.py, novo | tests/test_characterization.py, novo |
| src/molecular/characterization_service.py, novo | tests/test_characterization_service.py, novo |
| src/molecular/atomic.py | tests/test_atomic.py |
| src/molecular/rdkit_tautomer.py | tests/test_rdkit_tautomer.py |
| src/molecular/cli.py | tests/test_cli.py |

Exatamente dez caminhos candidatos. Não alterar application.py, scientific.py, registries, execution.py, promotion/conditions/receptor, context.py, pyproject.toml ou documentação pública por conveniência. Se o rascunho revelar necessidade real fora dessa lista, propor ao revisor com motivo antes de freeze; não alterar lista na implementação sem autorização. Bibliotecas padrão usadas não são nova dependência.

Checkpoints propostos:

1. **DTOs/perfis/adaptador:** parsing, dez valores e desenho/validador, disponibilidade opcional e ausência de regressão da enumeração. Testes puros podem rodar em Linux; não presumir aprovação do serviço Windows.
2. **Leitores/serviço:** contrato comum de leitura, identidade e proveniência; integração com registros reais; evidência Windows11/NTFS para ambos os leitores e falhas/interrupções. Sem essa evidência, não aprovar esse checkpoint.
3. **CLI e validação cumulativa:** formatos/falhas/sigilo, uma chamada por pedido, regressões, coletagem reconciliada e ensaio científico de apresentação. Não criar wizard020-C.

Esses checkpoints são proposta de execução depois da especificação final e autorização, não instrução para começar agora. Integração mínima necessária para testes pode ser disponibilizada nos checkpoints antecedentes sem introduzir comando futuro. Cada relatório deve registrar diff cumulativo, allowlist, git diff --check, working tree e quais testes foram realmente executados. Não tocar em untracked históricos do usuário.

## 19. Critérios de aceite da especificação candidata

Os critérios cumulativos abaixo permanecem para avaliar a candidata. A rodada focal atual deve verificar as correções do draft1 e eventual regressão concreta, sem repetir por preferência os pontos já encerrados:

- coerência entre APIs candidatas, contexto de vínculo gráfico e DTOs/JSON, sem objetos RDKit atravessando fronteira;
- detecção efetiva do perfil Windows11/NTFS, cobertura de nomes reservados e limites honestos de concorrência por path;
- gramáticas SDF/SMILES/SVG exatas, inclusive a compatibilidade do perfil reduzido de path com o backend Windows;
- distinção entre consulta sem histórico e execução científica persistida, sem misuse de attempts;
- matriz de falhas, precedência, tratamento de interrupções e convenção de uso do framework versus falha de negócio;
- suficiência dos cenários e da allowlist/checkpoints sem ampliação de escopo.

São detalhamentos novos de um rascunho: nomes/campos de DTO, códigos reason, limites e gramática formal de atributos/path, regras de saída e lista de caminhos. Não alegar que o fechamento arquitetural do Claude já aprovou cada um desses detalhes. Eventual mudança científica do perfil ou expansão de garantia deve voltar explicitamente à revisão.

Gates de congelamento cumpridos em 20/10/2026: identidade da candidate1 confirmada; fechamento independente publicado, sem BLOCKERS/MAJORS/MINORS remanescentes; aprovação explícita do responsável registrada. O documento candidato permanece preservado. Esta versão final altera somente apresentação e registros de processo/status, mantendo byte a byte as seções 2–18 e 20. A autorização de implementação abrange somente o Checkpoint 1; alteração científica ou ampliação de contrato exige decisão própria e revisão pertinente.

## 20. Fontes primárias e rastreabilidade do contrato

| Requisito candidato | Base arquitetural/normativa |
|---|---|
| Consulta, sem novos objetos/attempts/registry | A-01/A-12; execution.py; final016§§10–11; final020§§24–27; cláusulas específicas, sem inferir regra universal |
| Fronteira RDKit/opcionalidade/legado | A-04/A-06; final016§6; rdkit_tautomer.py; final017§§8/11/12 |
| Roots e protocolo específico novo | A-07/A-08, C-01/C-02; atomic.py e final018§8 como fonte de primitivas/limites, não leitor genérico já existente |
| Condições não consumidas | A-03; final019§21, sem mudar schema persistido |
| Parsing e desenho | A-09/A-10/A-11, C-03; scripts e JSON de evidência do pin |
| Numeração pós-020 e slot021 | A-02; final020§§7/34; estratégia antiga§11 explicitamente provisória |
| CLI técnica e esforço | A-13/A-14; context.py e taxonomia de falhas existente |
| Revisor único nesta etapa | Decisão expressa do responsável, posterior ao adendo do Claude |

Documentação primária RDKit: https://www.rdkit.org/docs/source/rdkit.Chem.rdMolDescriptors.html ; https://www.rdkit.org/docs/source/rdkit.Chem.rdDepictor.html ; https://www.rdkit.org/docs/source/rdkit.Chem.Draw.rdMolDraw2D.html . O site consultado é versão posterior ao pin; APIs efetivamente propostas foram confrontadas com binding/source Python instalado2026.03.6 e execução controlada.

XML: https://docs.python.org/3.12/library/pyexpat.html e https://docs.python.org/3.12/library/xml.html#xml-vulnerabilities . Não tratar defaults como proteção universal. Nomes Windows: https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file . As recusas adicionais do perfil são candidatas explícitas, não declaração de que a biblioteca atual já as implementa.

## 21. Fechamento independente e decisão do responsável

Tarefa de revisão 020-A-CANDIDATE1-CLOSURE encerrada pelo Claude. Parecer: increments/020-A/06-candidate-closure/CLAUDE_CANDIDATE1_CLOSURE_REVIEW.md, no governance, commit 7f1f75219203eb1a691e454db170900ca81536e8; SHA-256 9064866b6b3f0c2c54d9efc859a964ad314dbf25675ba4c112c97f22044363bd; 190 linhas e 18.902 bytes. O arquiteto leu o arquivo remoto integral e verificou esses bytes e hash. Os três MINORs do draft1 foram encerrados, incluindo a correção da premissa sobre usePathAngleExpansion no pin.

NOTE-A aceita sem mudança: confId não fornecido mantém o default inequívoco −1, sem novo parâmetro no perfil/DTO. NOTE-B aceita: a branch efetiva claude/lucid-faraday-xy632t estava autorizada, e seus commits permanecem preservados. Nenhuma NOTE condiciona o congelamento.

O parecer confirma prontidão para decisão do responsável, não execução de produção. Sua sonda independente usou Linux/Python 3.13.16 e RDKit2026.03.6, com moléculas de SMILES; não leu o repositório de código, não executou pytest e não validou leitores Windows. Esses limites permanecem, e a prova Windows continua no Checkpoint 2.

A mensagem direta “aprovado” de Emanuel, em resposta ao objeto delimitado em increments/020-A/07-owner-decision/INCREMENT_020_A_FREEZE_AND_CP1_DECISION_REQUEST.md, autoriza este congelamento e somente o Checkpoint 1. Registro em OWNER_FREEZE_AND_CP1_AUTHORIZATION.md, ao lado deste arquivo. A sessão implementadora deve conferir a versão final e a tarefa AUTHORIZED publicadas, sem se autoconceder a etapa seguinte.

## 22. Estado documental

DRAFT SPECIFICATION COMPLETE: YES — original draft1 preserved
DOCUMENT STATUS: FINAL SPECIFICATION FROZEN
DOCUMENT VERSION: final1
BASELINE REFERENCED: 08b797e0985e123ffd4d7ca7e5a5e8f040e63851
REVIEWER FOR THIS STAGE: CLAUDE
SECOND REVIEWER REQUIRED FOR THIS STAGE: NO — explicit project-owner decision
ARCHITECTURAL REVIEW CLOSED: YES
DRAFT REVIEW COMPLETE: YES
REVIEW MINORS INDEPENDENTLY CLOSED: YES
FINAL CANDIDATE INDEPENDENTLY APPROVED: YES — within focal review scope
OWNER FREEZE APPROVAL RECORDED: YES
READY FOR IMPLEMENTATION: YES
FINAL SPECIFICATION FROZEN: YES
IMPLEMENTATION AUTHORIZED: YES
AUTHORIZED CHECKPOINT: 1 — DTOs/profiles/adapter and their tests only
CHECKPOINT 2 AUTHORIZED: NO
CHECKPOINT 3 AUTHORIZED: NO
WINDOWS PRODUCTION READERS VALIDATED: NO — required at checkpoint2
CODE OR TESTS IMPLEMENTED: NO — research probes only at publication of this specification
ORIGINAL DRAFT CANDIDATE AND REVIEWS MODIFIED: NO
GOVERNANCE COORDINATION UPDATED: YES
AUTOMATED RELAY ACTIVE: NO
CODE REPOSITORY MODIFIED: NO
