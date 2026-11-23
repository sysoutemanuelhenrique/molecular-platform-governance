# Incremento 021 — requisitos de preparação do rascunho

Data: 23/11/2026. Autor: Codex arquiteto. Este checklist identifica o trabalho de redação seguinte; não é especificação, schema congelado, implementação ou autorização de sua execução.

Base: estudo/reconciliação e D-01(b)/D-02 aprovadas; parecer focal em 8778b83844fe9bff9b61862743277d5ee3172ac5, SHA-256 231cbbf892a990f2ca4617719e7c468b2ac5d1ce3d97d47cbaae2b90a2f2d463. A prontidão independente para rascunho não fecha os quatro achados parciais nem autoriza implementação.

## 1. Base de escopo e escolhas já aprovadas

- Perfil mínimo recomendado e considerado defensável pelo revisor: materialização no modelo fonte escolhido, consumindo seleção confirmada do 020 e RAW verificado; mmCIF, preservação das alternativas, sem expansão de assembly ou preparo químico. A aprovação expressa do responsável nesta rodada se limita às duas escolhas abaixo.
- D-01(b): exceção metalc/hydrog condicionada e auditada, com parceiro removido inteiro por decisão explícita suportada e cortes covalentes recusados.
- D-02: alcance amplo explicitamente reconhecido e auditado no modelo fonte, sem inferência de pertencimento por auth_asym_id.
- Nenhuma alteração de schema/loader/semântica do 020 para preencher lacunas; nenhuma retomada do 020-A.

## 2. P-1 — decisão explícita e exclusão de cadeias

A redação deve escolher e declarar se a lista S é uma seleção fechada cuja confirmação também reconhece a exclusão de todas as cadeias poliméricas do complemento. Isso precisa de ato e proveniência verificáveis; a mera ausência de um id na lista não deve receber a palavra explícita por interpretação do implementador.

Se o complemento confirmado contar para a exceção, registrar o motivo por ocorrência/conexão, inclusive a remoção de pontes hydrog de pareamento entre fitas de ácido nucleico. Se não contar, definir a recusa e sua consequência para metais mantidos ligados a cadeias excluídas. Ambas as alternativas devem respeitar D-01(b); o rascunho deve apresentar uma única regra implementável, sem fallback implícito.

Critério de completude: todos os exemplos pertinentes têm resultado determinado, origem de decisão e cenário individual de teste.

## 3. P-2 — reconhecimento do alcance amplo

Especificar o mecanismo da declaração que reconhece retenções fora de S. Vincular o ato ao conjunto enumerado de label_asym/entity/CCD/ocorrência/origem e ao snapshot das fontes; pode haver hash canônico, desde que payload e ordenação sejam definidos. A execução deve recusar ausência ou divergência do reconhecimento exigido, e não transformar o aviso de sucesso em consentimento posterior.

Definir o caso em que não há retenções fora de S e o comportamento quando o conjunto muda. Manter declaração e execução conceitualmente separadas, sem inventar uma interação obrigatória na CLI que o serviço não possa representar.

Critério de completude: declaração, validação, mismatch, ausência e apresentação auditável descritos e testáveis; nenhuma aprovação inferida de um log.

## 4. P-3 — unidade não polimérica

Escolher e justificar uniformidade por modelo/asym também para não polímeros com várias chaves, incluindo micro-heterogeneidade de ligante. A recomendação focal é tudo-ou-nada por asym no perfil mínimo; ela ainda precisa virar uma regra única no rascunho. Não confundir chave de disposição (asym, CCD), unidade de ocorrência e unidade física de exclusão.

Critério de completude: combinações S/D/U que gerem exclusão parcial são resolvidas ou recusadas explicitamente; todos os altlocs e variantes têm tratamento coerente; branched permanece tudo-ou-nada.

## 5. P-4 — simetria

Corrigir a justificativa: a mesma isometria conhecida aplicada aos dois endpoints preserva sua relação geométrica. Uma recusa conservadora de iguais não identidade deve ser apresentada como limite de cobertura/fixtures, não impossibilidade geométrica.

Preencher todas as 15 células de uma matriz: extremos retidos {2, 1, 0} × simetria {identidade nos dois lados, iguais não identidade, distintas, nula em um, nula em ambos}. Para cada célula indicar preservar literal, omitir com auditoria ou recusar, além das condições de tipo da conexão e de exclusão inteira que se aplicarem. Não aceitar a frase conexão que afeta o recorte como substituta da matriz.

Definir como estabelecer identidade do operador na fonte, por exemplo n_555 com operador correspondente demonstrado como identidade, e o que fazer quando a tabela estiver ausente, inconsistente ou insuficiente. Não tratar todo índice 1 como identidade sem uma regra declarada.

Critério de completude: matriz sem célula indefinida, identificação de operadores, fixtures das classes e correspondência ao modelo M.

## 6. P-5 — catálogo de saída

Produzir catálogo por tag/categoria com chave, regra de inclusão/filtro, referências cruzadas, nulidade, política de preservação/omissão/recusa e teste associado. Incluir as famílias identificadas na reconciliação: atom_site/anisotrop, entidades/asym e sequências/esquemas poly/nonpoly/branch, conexões/tipos, anotações estruturais, modificações, ausências/ocupância zero, simetria/assembly/NCS e validações do depósito.

Categorias não suportadas precisam de tratamento explícito proporcional ao perfil; o nome da categoria não prova inocuidade referencial. Auditoria de omissão não corrige referências quebradas em categorias preservadas.

Critério de completude: não delegar a decisão de catálogo ao implementador; fixtures reais representativas e integridade pós-seleção verificável.

## 7. NOTE-F1 e demais decisões de redação

O leitor documental próprio deve preservar a semântica dos modelos 1.0 e do carregamento UTF-8/YAML existente, com diretórios reais e igualdade exata dos ids internos. Hashear os bytes capturados, separando esse hash da decodificação/normalização semântica. Cobrir UTF-8 inválido e terminadores de linha pertinentes sem alegar equivalência não testada.

Fechar no rascunho as outras questões já identificadas: formatos dos novos registros, identidade/chave canônica, retry, limites, publicação e recuperação, diagnóstico/tentativas, erros e CLI. Essas questões não desapareceram porque o revisor considerou o estudo pronto.

Enumerar cenários individualmente e reconciliar cenários/funções/itens; não herdar a contagem agrupada 48 como obrigação aritmética. Propor checkpoints/allowlist concretos. Manter o gate Windows/NTFS na implementação correspondente, sem exigência circular de validar código inexistente antes do rascunho.

## 8. Gate de saída

Após autorização para redação, o arquiteto poderá produzir um rascunho completo e sua tarefa de revisão independente, preservando este checklist e todos os pareceres anteriores. O rascunho precisa de revisão própria; sua criação não congela contrato nem autoriza código.

P-1 THROUGH P-5 CLOSED BY THIS CHECKLIST: NO
DRAFT SPECIFICATION PRODUCED: NO
READY FOR IMPLEMENTATION: NO
FINAL SPECIFICATION FROZEN: NO
