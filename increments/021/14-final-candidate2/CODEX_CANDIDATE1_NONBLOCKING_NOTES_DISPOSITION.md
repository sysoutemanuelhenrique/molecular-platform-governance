# Disposição das notas NB-1/NB-2 e preparação da decisão de congelamento

Autor: Codex arquiteto. Data: 24/11/2026, America/Sao_Paulo. Continuação documental da especificação 021; nenhuma implementação ou congelamento autorizado por este documento.

## 1. Parecer e snapshots

Recebido o parecer 021-CANDIDATE1-FOCAL-REVIEW da branch claude/021-candidate1-focal-review-20261124, commit 4759abff9f7deeb921cfb944b1e6cd3fc914d4fa. Identidade conferida: 73 linhas, 6.564 bytes, SHA-256 6550fdb2ea4a50b075efbe163b8f0525357dd671be4759619bcfdaeb0357590b. Três arquivos acompanhantes conferidos pelos blobs Git. Coordenação de entrada ec38f578ced987969cd8f58c9c7ee4567e7fdd52; código main 08b797e0985e123ffd4d7ca7e5a5e8f040e63851; governance main a47183dfec8213c765ed43ae482c8c227760a3d5. HEADs remotos conferidos antes de trabalhar.

O revisor fechou MINOR-N1 e MINOR-N2, incorporou NOTE-N1/N2, não encontrou regressão e emitiu APPROVE WITH NON-BLOCKING NOTES: 0 BLOCKER / 0 MAJOR / 0 MINOR / 2 notas. O parecer permanece intacto e vale para a candidate-1, não para uma versão nova inventada retrospectivamente.

## 2. Disposição das duas notas

| Nota | Disposição do arquiteto | Redação aplicada exclusivamente em §10.1 |
|---|---|---|
| NB-1 | Aceita e incorporada conforme a leitura do revisor | Duplicação é dentro da mesma tabela. Um id uma vez em cada tabela, com expressões concordantes, não é duplicação e fornece referência válida |
| NB-2 | Aceita a recomendação de coerência da prova | Em K=0, endpoint 1_555 com tabela presente exige confirmação de identidade em todas as tabelas presentes para classe de identidade. Prova insuficiente → unsupported-discarded com precedência; lookup bem-sucedido continua source-operator |

Exemplo NB-1: ambas as tabelas contêm id 1 uma vez, x,y,z concordante → lookup válido, basis source-operator, e ambos os endpoints 1_555 comprovados podem ter classe both-identity. Duas linhas id 1 dentro da mesma tabela continuam duplicação; não deduplicar por conteúdo.

Exemplo NB-2: tabela A tem id 1=x,y,z, tabela B está presente mas só tem id 2; ambos os endpoints são 1_555 e K=0 → identity_basis=(source-operator,source-operator), symmetry_class=unsupported-discarded, ação de omissão auditada. Em K>0 a prova insuficiente continua recusada. A regra também torna explícita a falta de comprovação quando op 1 localizado não é identidade. Não troca a base por not-applicable depois de lookup válido.

As duas precisões cabem no T021-173 já existente. Não alterei sua linha nem acrescentei cenário, enum, campo, comando, tipo de artefato ou permissão científica. O catálogo, os SCHEMAS, os cenários e os casos de base foram copiados byte a byte. Permanecem 173 cenários: 43/79/31/20.

## 3. Diff e escopo da conferência

Candidate-2 é arquivo novo; candidate-1, pareceres e manifestos históricos permanecem intocados. Em §10.1 o delta é exatamente NB-1 e NB-2. As demais alterações do corpo são identificação/data/snapshots/estado e o próximo gate humano. As seções 2–9 e 11–21 permanecem byte-idênticas; o texto científico/fixtures da §23 também permanece, mudando apenas o bloco de estado final. A matriz de 15 células não mudou, nem P-1/P-2/P-3/NOTE-F1, NCS, publicação, compensação ou fronteira da CLI.

O parecer diz literalmente: “Não exigem nova rodada de revisão além da conferência do diff.” A conferência do delta está documentada; não inicio outro ciclo integral de revisão nem declaro que um revisor externo leu a candidate-2. O responsável recebe o parecer favorável da candidate-1 junto das duas precisões rastreáveis e pode solicitar conferência adicional se preferir.

## 4. Verificações e limites

Conferidos os 12 itens do manifesto de entrada, o parecer e três evidências, JSON/CSV, os quatro anexos iguais e o diff restrito. Li o modelo stdlib do revisor antes de executá-lo em scratch: a reexecução reproduz os sete hashes documentais e a grade de 512 entradas. Esse modelo testa identity_basis, não symmetry_class; portanto não o apresento como teste de produção nem prova operacional de NB-2. A regra de NB-2 foi conferida como redação contratual, devendo ser exercitada pelo materializador no CP2/T021-173.

Não executei pytest, Gemmi, parsing RAW, hashes de produção, materialização, Windows, concorrência ou instalação. Não alterei o repositório de código nem itens locais preservados. O 020-A permanece STAND-BY.

## 5. Decisão pendente do responsável

Tarefa preparada: tasks/021-OWNER-FREEZE-DECISION.json. Seu estado é PREPARED_AWAITING_OWNER_DECISION. O pacote identifica candidate-2 e os quatro anexos por hashes exatos, mais esta disposição e o parecer da candidate-1.

Opções do responsável: aprovar congelamento somente dessa versão, solicitar ajuste ou pedir conferência adicional do delta. Nenhuma escolha foi registrada em seu nome. Aprovar congelamento não autoriza implementação, criação de branch de código, checkpoint, PR ou merge; autorização de implementação deverá ser própria e identificar a especificação congelada e o checkpoint permitido.

OWNER FREEZE DECISION PACKAGE PREPARED: YES
READY FOR OWNER FREEZE DECISION: YES
OWNER APPROVAL RECORDED: NO
INDEPENDENT CANDIDATE2 REVIEW CLAIMED: NO
READY FOR IMPLEMENTATION: NO
FINAL SPECIFICATION FROZEN: NO
CODE REPOSITORY MODIFIED: NO
