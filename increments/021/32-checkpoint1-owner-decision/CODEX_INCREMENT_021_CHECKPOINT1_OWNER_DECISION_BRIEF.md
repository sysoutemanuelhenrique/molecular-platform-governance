# Incremento 021 — recebimento do fechamento R-1 e decisão sobre CP1

Autor: Codex arquiteto. Data: 24/11/2026, America/Sao_Paulo. Natureza: recebimento documental do parecer independente e preparação da decisão do responsável; não é aprovação humana ou nova execução de testes.

## 1. Entradas verificadas

| Objeto | Snapshot |
|---|---|
| Coordenação de entrada | docs/020-a-candidate1-review-20261020 @ 828bf806e2f16ae9fee5896ae6f9719a9e1dc5cf |
| Parecer R-1 | claude/021-cp1-r1-focal-review-20261124 @ a9b146d5a355e4c15ad596b851136efdde208cdb |
| Código CP1 avaliado | feature/increment-021-receptor-materialization @ ea8dac9cdc203c337d7f3f9947b54042291f7484 |
| Relatório do implementador | claude/021-cp1-r1-test-correction-20261124 @ b35bb8e9d32e6fb4bc95e903f786fa0c1240e2d2 |
| Main código | 08b797e0985e123ffd4d7ca7e5a5e8f040e63851, preservada |
| Main governance | a47183dfec8213c765ed43ae482c8c227760a3d5, preservada |

Os HEADs foram conferidos diretamente no remoto. O parecer tem 116 linhas, 7.227 bytes, SHA-256 `a1d99b0d56ae73e1a006878483c2f61f7dffa36a447d686178c6bd7cc9420736`. Li integralmente o parecer e as oito evidências. As oito entradas do manifesto conferem em linhas/bytes/SHA-256; os nove blobs, inclusive o manifesto, conferem com a árvore Git remota. O commit do revisor é filho da coordenação de entrada e adiciona somente os nove arquivos permitidos. Não há alteração do STATUS/tarefas centrais pelo revisor.

## 2. Disposição recebida

**R-1: fechado independentemente — APPROVE.** O teste novo chama a função de produção, usa dois átomos fora de ordem e os hashes literais corretos. O revisor executou o nó pytest exato e o arquivo completo na produção e em quatro cópias com mutações de ordem: ordinal crescente, ID, inversão e ordinal decrescente. Todas as mutações falharam apenas no teste novo; produção teve 1 passed no nó e 92 passed no arquivo. A segunda asserção detecta a ordenação decrescente, que preservaria o primeiro vetor. Os 91 testes anteriores, treze goldens e 43 cenários estão preservados; nenhuma regressão nova foi identificada pelo revisor.

O delta continua somente teste (+31/-0). O código de produção não mudou nesta rodada: SHA-256 `d8fc55db900f761f0debe4cea29f05cade1502ea1299937f123c6c883e30431d`. O diff cumulativo permanece nos dois arquivos autorizados do CP1. A conferência detalhada desse código e dos logs já está no recebimento anterior, identificado no snapshot de entrada; não a repeti como se fosse nova execução.

Os doze achados funcionais fechados anteriormente permanecem fechados, agora acompanhados pelo fechamento de R-1. **Pendências contratuais abertas: zero BLOCKERs, zero MAJORs, zero MINORs.** As três NOTES são preservadas: o plano CP1 não é artefato final reutilizável; manter estritez/ordem/chaining; reexaminar CLI/import/help sem opcionais no gate CP4. Os 43 cenários permanecem classificados em 40 provados, 3 parciais por desenho e zero lacunas — os três parciais não são reinterpretados como execução física já concluída.

## 3. Evidência e limites

A execução independente recebida é Linux, sem Gemmi/RDKit nativos e sem Windows. O sentinela inerte de Gemmi foi usado apenas para importar DTOs legados do 020; não prova parsing, materialização ou importação nativa. A suíte Windows de 1.568 passed e 5 skipped é execução fornecida pelo implementador, não reexecutada pelo revisor nem pelo arquiteto. A coleta fornecida é 1.573 itens, consistente com +1 teste e sem remoção. Os cinco skips anteriores continuam identificados.

Neste recebimento não executei pytest, scripts do revisor, motores científicos ou instalações. Executei verificação de identidades/árvores/diff de publicação, leitura integral e conferência de consistência das evidências. A auditoria anterior do arquiteto também permanece distinta: função nova via AST e dois wrappers ordenados, não pytest completo ou validação Windows. Não há alegação de validação nativa adicional neste documento.

## 4. Decisão proposta ao responsável

Recomendo aceitar o **Checkpoint 1 do Incremento 021 no commit exato ea8dac9cdc203c337d7f3f9947b54042291f7484**, com as três NOTES e os limites documentados. O parecer independente permite essa decisão; não a substitui. A aprovação precisa vir de Emanuel, conforme AGENTS.md e o protocolo de coordenação. Não foi recebida aprovação humana do CP1 nesta entrega.

A tarefa `tasks/021-OWNER-CHECKPOINT1-DECISION.json` está aguardando a decisão. Se o responsável aprovar esse snapshot, o arquiteto registra a mensagem literal em documento novo e pode preparar o brief/allowlist/testes/tarefa do CP2 sob o contrato já congelado. **Preparação documental não autoriza implementação de CP2.** Essa execução exige sua tarefa concreta e autorização própria; PR, merge, tag, release e alteração de main continuam fora de escopo.

Nenhuma nova revisão integral é solicitada: o gate independente de R-1 foi concluído. O 020-A permanece STAND-BY; seus documentos/código e os itens locais protegidos não foram tocados. Nenhum agente foi acionado automaticamente.

R1 INDEPENDENTLY CLOSED: YES
OPEN BLOCKERS: 0
OPEN MAJORS: 0
OPEN MINORS: 0
PRESERVED NOTES: 3
READY FOR OWNER CP1 DECISION: YES
CHECKPOINT1 APPROVED BY OWNER: NO
CHECKPOINT2 IMPLEMENTATION AUTHORIZED: NO
FINAL SPECIFICATION FROZEN: YES
CODE REPOSITORY MODIFIED BY ARCHITECT: NO
AUTOMATED DISPATCH: NO
