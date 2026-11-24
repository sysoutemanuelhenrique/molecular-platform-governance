# Coordenação — Incremento 021: três correções residuais do CP1

Atualizado em 24/11/2026 por Codex arquiteto. Parecer focal recebido e reconciliado; nove achados fechados preservados, três MINORs impedem aprovação. Sem novo estudo ou avanço para CP2.

| Campo | Estado |
|---|---|
| Branch de coordenação | docs/020-a-candidate1-review-20261020 |
| Snapshot de entrada | 155661115851c2a5fb70f5d905425baeb4d23c9f |
| Código | feature/increment-021-receptor-materialization @ 42b4804b5f4ea01ddf320c45473d8b4f980ea67e |
| Main código / baseline | 08b797e0985e123ffd4d7ca7e5a5e8f040e63851, preservada |
| Main governance | a47183dfec8213c765ed43ae482c8c227760a3d5, preservada |
| Parecer focal | claude/021-cp1-focal-review-20261124 @ 854ae336621116f7047033b5146c7c4834ebf9c2 |
| Veredito / resíduos | REQUEST CHANGES; 0 BLOCKER/0 MAJOR/3 MINOR; MAJOR-A é rótulo histórico com resíduo MINOR |
| Fechados independentemente | ARCH-01/02/03, MAJOR-B, MINOR-1/2/4/5/6 |
| Corrigir agora | MAJOR-A formato, MINOR-3 ordinais/nomes, MINOR-7 golden literais/teste novo legado |
| Reconciliação | increments/021/24-checkpoint1-residual-reconciliation/CODEX_INCREMENT_021_CHECKPOINT1_RESIDUAL_RECONCILIATION.md |
| Tarefa ativa | tasks/021-CHECKPOINT1-RESIDUAL-CORRECTIONS.json — READY_FOR_MANUAL_HANDOFF_WITHIN_AUTHORIZED_CP1 |
| Regra de formato | Aliases020 preservados; contraditório/desconhecido recusa INVALID_RECORD; sem reescrever proveniência |
| Apoio ao teste | 13 vetores documentais independentes com bytes/digests literais, conferidos separadamente contra produção |
| Resultados observados | Parecer/manifesto/blobs conferem; sonda pura repetida;13/13 vetores coincidem, sem Gemmi/RDKit |
| Limitações | Sem pytest, Windows, parsing nativo ou suíte completa pelo arquiteto |
| Cenários | Fechamento independente40 provados/3 parciais por desenho/0 lacunas,43 IDs preservados |
| Próximo ator | Claude implementador separado do revisor, correção focal dentro do CP1 já autorizado |
| Próximo gate | Receber código/relatório e preparar revisão final curta dos três resíduos |
| CP1 aprovado / CP2 autorizado | Não / Não |
| Contrato / 020-A | Congelado preservado / STAND-BY |
| Relay automático | Não configurado, nenhum agente acionado |

As nove disposições fechadas não serão reabertas por preferência; somente regressão concreta no novo delta justifica reexame. Pareceres e históricos ficam preservados em seus snapshots, sem merge de branches de agentes. O arquiteto não alterou o repositório de código nem executou pytest. Os três resíduos só se encerram com prova e parecer independente, não com esta instrução.

FOCAL REVIEW RECEIVED: YES
RESIDUAL CORRECTION TASK PREPARED: YES
CHECKPOINT1 APPROVED: NO
CHECKPOINT2 IMPLEMENTATION AUTHORIZED: NO
FINAL SPECIFICATION FROZEN: YES
CODE REPOSITORY MODIFIED BY ARCHITECT: NO
AUTOMATED DISPATCH: NO
