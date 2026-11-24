# Reconciliação arquitetural — revisão do draft-1 do Incremento 021

Autor: Codex, arquiteto. Data: 23/11/2026, America/Sao_Paulo. Objeto: resposta concreta aos 3 MAJORs e 6 MINORs, acompanhada de draft-2 revisável. Não é implementação, congelamento ou fechamento independente.

## 1. Snapshot e autoridade

Governance de entrada: docs/020-a-candidate1-review-20261020 @ b948f60245b71da71fa4535e8ef7ffa3957b35b4. Parecer recebido: claude/021-draft-review-20261123 @ 680aef4eecc3852fff78a70c75691993d51849b6. Código main permanece 08b797e0985e123ffd4d7ca7e5a5e8f040e63851; main do governance a47183dfec8213c765ed43ae482c8c227760a3d5. HEADs remotos conferidos antes do trabalho.

Parecer integral lido e identidade confirmada: 155 linhas, 14.751 bytes, SHA-256 ede42c4f7455973a0947deed8948dabb03618d338e341ae87bb0e5135f76a59c. Os nove arquivos de evidência também foram conferidos contra os blobs do commit recebido. O parecer continua intacto na branch do revisor; esta publicação não o edita nem faz merge dessa branch.

A autorização vigente de Emanuel permite redigir/publicar rascunho e preparar revisão, sem implementar ou congelar. A revisão do próprio rascunho é continuação dessa etapa; não se registra nova aprovação humana nem se converte o parecer em consentimento do responsável. D-01(b)/D-02 ficam preservadas. 020-A permanece STAND-BY.

## 2. Disposições individuais

| Achado | Disposição do arquiteto | Resposta proposta no draft-2 | Prova a exigir |
|---|---|---|---|
| MAJOR-1 | Aceito no impedimento; generalização populacional não demonstrada | Opção (a): 1_555 sem tabelas reconhecido explicitamente por convenção; tabela presente deve confirmar identidade, sem contradição. Outros operadores não recebem fallback | T021-141–144, 045–060/079; audit identity_basis |
| MAJOR-2 | Aceito quanto à cobertura; argumento de omissão universal aceito apenas parcialmente | Acrescentar tags/categorias observadas, famílias NMR/EM delimitadas, audit integral, manter rejeição de categorias fora do catálogo e guardas NCS/posição especial | T021-145–149/162 e catálogo; recheck documental das três amostras |
| MAJOR-3 | Aceito | Guarda NCS anterior à omissão: não identidade com code diferente de given recusa; matriz incompleta/valor inválido recusa; identidade/given só omite auditado | T021-150–154; novo UNSUPPORTED_NCS |
| MINOR-1 | Aceito, correção factual | su final após expoente; aceitar 1.2e3(4), recusar 1.2(4)e3 | T021-155 e sonda documental de regex |
| MINOR-2 | Aceito como redução segura de recusa | Endpoint pode ser conjunto de variantes da mesma ocorrência/atom name, com destino uniforme; não fundir ocorrências nem expandir conexões | T021-156–157; schema endpoint_atom_ids |
| MINOR-3 | Recomendação aceita, não falha científica demonstrada | application_version sai de plano/policy; fica no request/manifesto. Mudanças semânticas exigem versões/profile/catalogue adequados | T021-159–160; ausência de ciclo de hash |
| MINOR-4 | Aceito | omit_tags sempre array; action=omit define omissão total. Guarda semântica precede guard_then_omit | T021-161; validação estrutural de todas as categorias |
| MINOR-5 | Aceito com precisão científica | Posições especiais podem explicar ocupâncias; não inferir multiplicidade só da ocupância. Mapear contexto, contar linhas/átomos retidos, avisar perda de anotação sem mudar tokens | T021-158 e SpecialPositionSummary |
| MINOR-6 | Aceito | Frase CLI corrigida; procedimento manual de diagnóstico de órfãos documentado, sem comando automático/force-unlock | §14/17 e T021-163 |

Todas as disposições acima são respostas do arquiteto. Os 3 MAJORs e 6 MINORs aguardam verificação independente das soluções; não apresentar contagem zero de achados fechados pelo revisor.

## 3. P-4: identidade e conexões entre imagens

Adotada para o rascunho a opção (a) recomendada, sem exigir a aprovação de uma exclusão adicional de uso do PDB (opção b não adotada). É decisão técnica proposta, não aprovação humana de novo contrato. O writer oficial do Gemmi 0.7.5 emite 1_555 para o primeiro parceiro sem exigir tabela. Isso sustenta a compatibilidade escolhida. O item wwPDB define n_klm por referência a operador e tradução; não prova sozinho que todo CIF numere a identidade como 1. Por isso a exceção é literal, explícita e limitada ao perfil PDBx, com base registrada na auditoria. Se houver tabela incompatível, ela não é ignorada.

Fonte: [writer Gemmi pinado](https://github.com/project-gemmi/gemmi/blob/5cc1c23c6007e0e6cbd69289c6f7c0bff50e943e/src/to_mmcif.cpp), write_struct_conn; [definição wwPDB de ptnr1_symmetry](https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_struct_conn.ptnr1_symmetry.html).

O correlato K=2 com códigos distintos continua recusado por um limite explícito de projeção de relações entre imagens, e não porque o RAW devesse conter átomos expandidos ou por impossibilidade geométrica. Assim, 1pfe continua negativo operacional no perfil inicial; seu catálogo pode ser aceito sem prometer materialização. A revisão focal deve avaliar essa justificativa, conforme a alternativa permitida no próprio achado. Preservar indiscriminadamente ou omitir esses vínculos mudaria o perfil; não o fiz silenciosamente.

Não adotar a frase “quase todo receptor” como estatística: três amostras comprovam três recusas e a existência do defeito de utilidade, sem medir prevalência no arquivo PDB.

## 4. P-5: catálogo e perdas controladas

Draft-2: 94 categorias, sendo 24 filter, 1 generate, 67 omit e 2 guard_then_omit. Foram adicionadas as 16 categorias fora do catálogo apontadas nas amostras e pdbx_struct_conn_angle; o corpo explicita as três famílias de omissão auditada validate/NMR/EM. Tags observadas em cell, symmetry e unobs atoms foram incorporadas. Os arrays são homogêneos; as guardas têm campos reconhecidos e não recebem omissão cega.

Omissão completa evita exportar referências de uma categoria retirada, mas isso não prova inocuidade semântica universal. Metadados podem declarar transformações, cópias ou contexto físico, como NCS e posição especial demonstram. Portanto, rejeição default de categoria desconhecida foi preservada; não usar a observação do grafo de foreign keys como prova de segurança para apagar qualquer categoria futura.

As famílias NMR/EM são perdas explícitas de informação experimental do depósito; não se afirma que o derivado representa ensemble, mapa ou qualidade experimental. A fonte RAW permanece íntegra e todos os descartes são auditados. Os casos reais são gates de teste futuros com lineage, não decoração documental. Fixtures editadas devem declarar cada edição; não apresentá-las como depósitos intactos.

**Reexecução própria limitada:** executei o script de cobertura do revisor, após lê-lo, contra o catálogo novo e os inventários publicados por ele. Resultado: zero categorias/tags/requisitos de coluna não reconhecidos nos três inventários. Isso reproduz a checagem de cobertura, não o parsing C++ original nem a materialização; não mede distribuição de casos reais nem testa guardas por conteúdo.

## 5. NCS e posição especial

O reader Gemmi conserva transformações não identidade code!=given como não expandidas e ignora algumas linhas incompletas. O novo adapter proposto não pode usar esse skip como aceitação: validar o DOM original e recusar dados de transformação insuficientes. Code generate significa que o operador gera coordenadas além das fornecidas; não é prova de ausência de átomos da ASU selecionada nem autorização para expandir assembly.

Fonte: [read_ncs_info](https://github.com/project-gemmi/gemmi/blob/5cc1c23c6007e0e6cbd69289c6f7c0bff50e943e/src/mmcif.cpp); [semântica oficial code](https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_struct_ncs_oper.code.html). A guarda é conservadora e ocorre antes da seleção/omissão, conforme o recorte solicitado.

Posição especial: [categoria oficial](https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Categories/pdbx_struct_special_symmetry.html). Mapear anotação por contexto inequívoco, registrar quantas intersectam átomos retidos e quantos átomos únicos; warn se houver interseção. Não usar ocupância reduzida como diagnóstico universal nem normalizá-la. Ambiguidade continua erro, não perda silenciosa.

## 6. Endpoints, versões e exceções

Altlocs da mesma ocorrência compartilham o destino pela P-3, permitindo decidir K sem escolher uma variante. O schema usa dois conjuntos ordenados, não um par arbitrário nem produto cartesiano. Ambiguidade entre resíduos/ocorrências segue recusada.

Remover application_version de plan_key é conveniência de evolução, não evidência de erro científico no draft-1. A implementação deverá cumprir versionamento semântico: não usar versão de distribuição como substituta da versão do algoritmo. request/manifesto ainda distinguem o executável instalado, sem alegar Git SHA de build inexistente.

Rigidez dos DTOs, hashes de fontes, reconhecimentos X/O, erros pós-commit, preservação de interrupções e limites de compensação não foram relaxados. As seções 3/4/5/7/8/15/18/21 foram comparadas e permanecem byte-idênticas ao draft-1.

## 7. Evidências, cenários e limites

Os 140 ids anteriores permanecem. Somente T021-035/060/079 tiveram textos de expectativa/estímulo alterados para as decisões revisadas; nenhum cenário foi apagado. Há 23 cenários adicionais: total 163; CP1=44, CP2=68, CP3=31, CP4=20. IDs não equivalem a funções ou itens pytest. O catálogo e a matriz de 15 células continuam rastreáveis.

Executado pelo arquiteto nesta rodada: consultas de refs/blobs; conferência SHA-256/Git dos arquivos recebidos; releitura de cinco fontes Gemmi pinadas e páginas primárias wwPDB/IUCr; script documental de cobertura sobre inventários de terceiro; dez casos de regex extraída do rascunho; consistência JSON/CSV, seções preservadas e whitespace.

Não executado pelo arquiteto: pytest, import Gemmi Python, parsing C++/CIF novo, materialização, Windows, concorrência, instalação de pacote. A equivalência YAML 11/11 continua evidência do revisor, não execução nova minha. A aceitação de metadados não substitui teste de coordenadas/átomos/conexões reais.

## 8. Próximo gate e decisões

Publicar draft-2/anexos em increments/021/09-revised-draft/, preservando draft-1 e parecer. Revisão focal em tarefa própria: nove achados e regressões diretamente decorrentes; não repetir P-1/P-2/P-3/NOTE-F1 encerrados sem evidência concreta. A revisão deve conferir especialmente a regra 1_555, a guarda NCS, a amplitude das omissões NMR/EM, o significado dos conjuntos de altloc e a manutenção da recusa não identidade em 1pfe.

Nenhuma decisão humana de congelamento/implementação foi registrada. Se o responsável preferir a opção (b) de MAJOR-1, a exclusão expressa de uso ainda exigirá sua decisão; ela não é necessária ao draft-2 proposto, que usa (a). Após revisão e reconciliação seguintes, aprovação de versão/congelamento continua gate do responsável. Não há agente acionado automaticamente.

RECONCILIATION COMPLETE: YES
DRAFT2 PREPARED FOR INDEPENDENT REVIEW: YES
INDEPENDENT FINDING CLOSURE CLAIMED: NO
READY FOR IMPLEMENTATION: NO
FINAL SPECIFICATION FROZEN: NO
CODE REPOSITORY MODIFIED: NO
