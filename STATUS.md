# Coordenação — Incremento 021: CP1 aprovado; CP2 preparado, não autorizado

Atualizado em 24/11/2026 por Codex arquiteto, após mensagem expressa de Emanuel. O CP1 no commit ea8dac9cdc203c337d7f3f9947b54042291f7484 está aprovado, com as três NOTES preservadas. A aprovação autoriza apenas preparar a tarefa do CP2; não implementar.

| Campo | Estado |
|---|---|
| Branch de coordenação | docs/020-a-candidate1-review-20261020 |
| Snapshot de entrada | fceadfe20ba7d3d63081e4d4a0682bffcd197374 |
| Código CP1 aprovado | feature/increment-021-receptor-materialization @ ea8dac9cdc203c337d7f3f9947b54042291f7484 |
| Registro literal do responsável | increments/021/33-checkpoint1-acceptance/OWNER_CHECKPOINT1_ACCEPTANCE.md |
| Parecer independente R-1 | a9b146d5a355e4c15ad596b851136efdde208cdb, APPROVE; doze achados anteriores e R-1 fechados |
| Achados CP1 abertos / NOTES | 0 BLOCKER / 0 MAJOR / 0 MINOR; 3 NOTES preservadas |
| CP1 aprovado | YES, pelo responsável no commit exato |
| Tarefa ativa | tasks/021-CHECKPOINT2-IMPLEMENTATION.json — AWAITING_EXPLICIT_OWNER_IMPLEMENTATION_AUTHORIZATION |
| Brief CP2 | increments/021/34-checkpoint2-preparation/CHECKPOINT2_IMPLEMENTATION_BRIEF.md |
| Escopo CP2 | Adapter DOM/token/endpoints/simetria/catálogo/saída e validação com Gemmi0.7.5 real; 79 cenários |
| Allowlist CP2 proposta | receptor_parsing.py, receptor_materialization.py, seus dois testes e tests/fixtures/receptor_materialization/ |
| CP2 implementação / commit-push / relatório | NO / NO / NO; aguardando autorização própria |
| Próximo ator | Emanuel: decidir autorização da tarefa CP2 concreta |
| Main código | 08b797e0985e123ffd4d7ca7e5a5e8f040e63851, preservada |
| Main governance | a47183dfec8213c765ed43ae482c8c227760a3d5, preservada |
| Contrato / 020-A | Congelado preservado / STAND-BY |
| Verificação da preparação | Especificação e quatro anexos lidos/identificados; pacote e 79 IDs reconciliados; código/parser e limites CP1 confrontados; sem pytest/nativos/Windows |
| Execução automática | Nenhuma; nenhum agente acionado |

CP2 não inclui publicação concorrente, leitores Windows/storage/registry/service ou CLI. Essas etapas continuam nos CP3/CP4. Não usar o plano parcial CP1 como artefato final. Preparação documental não é autorização de implementação; não editar código nem produzir relatório de implementação nesta etapa. A futura execução deve receber novo despacho autorizado com SHA imutável, em vez de reutilizar o snapshot de preparação como se autorizasse escrita.

CHECKPOINT1 APPROVED BY OWNER: YES
CHECKPOINT2 TASK PREPARED: YES
CHECKPOINT2 IMPLEMENTATION AUTHORIZED: NO
CHECKPOINT3 IMPLEMENTATION AUTHORIZED: NO
FINAL SPECIFICATION FROZEN: YES
CODE REPOSITORY MODIFIED BY ARCHITECT: NO
AUTOMATED DISPATCH: NO
