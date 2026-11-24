# Coordenação — Incremento 021: CP1 requer correções

Atualizado em 24/11/2026 por Codex arquiteto. Parecer independente recebido e reconciliado. CP1 não aprovado; nenhum avanço para CP2.

| Campo | Estado |
|---|---|
| Branch de coordenação | docs/020-a-candidate1-review-20261020 |
| Snapshot de entrada desta reconciliação | d577b0dfddd3c71f9287b4c9cdcc783ea0865654 |
| Código / branch | feature/increment-021-receptor-materialization @ 711f3070765efe67a5799f939f1a18306ed8afdd |
| Baseline / main código | 08b797e0985e123ffd4d7ca7e5a5e8f040e63851, inalterada |
| Main governance | a47183dfec8213c765ed43ae482c8c227760a3d5, inalterada |
| Relatório original | 51752b4ce7603d1f14677b0b030edc176b9df13f, preservado |
| Parecer independente | 2e36222b087134f9ba725bc2ad96c3ba39fb8801 na branch claude/021-cp1-adversarial-review-20261124 |
| Veredito recebido | REQUEST CHANGES |
| Contagem cumulativa | 0 BLOCKER / 4 MAJOR / 8 MINOR / 3 NOTE; ARCH e achados independentes sem dupla contagem |
| Reconciliação | increments/021/20-checkpoint1-reconciliation/CODEX_INCREMENT_021_CHECKPOINT1_RECONCILIATION.md |
| Tarefa ativa | tasks/021-CHECKPOINT1-CORRECTIONS.json — READY_FOR_MANUAL_HANDOFF_WITHIN_AUTHORIZED_CP1 |
| Autorização aplicável | CP1 já autorizado pelo responsável; mesma branch/dois arquivos, sem nova aprovação alegada |
| Correções | Domínio sem nativo; projeção D em M; cruzamentos de fonte; integridade de policy; invariantes DTO/hash/testes |
| Ressalva arquitetural | Import tardio de inspection no builder sozinho não satisfaz caminho puro; preservar hash 020 via backend puro compatível |
| Provas próprias | Import limpo falha; 23 sondas condicionais e golden do revisor reproduzidos; códigos inválidos aceitos sob -O |
| Limitações próprias | Sem pytest/Gemmi reais/Windows/concorrência; sentinela só em lógica pura, não na prova de import |
| Próximo ator | Claude implementador em sessão separada do revisor |
| Próximo gate | Receber correção/relatório reais e preparar revisão focal independente |
| CP1 aprovado / CP2 autorizado | Não / Não |
| Especificação / 020-A | Congelada preservada / STAND-BY |
| Relay automático | Não configurado, nenhum agente acionado |

O parecer e seus arquivos permanecem na branch própria, lidos por commit; nenhuma branch de relatório/revisão foi mesclada. As correções cabem nos dois arquivos já autorizados; nenhuma modificação de código foi feita pelo arquiteto. Nenhum achado está fechado independentemente só porque aceito nesta resposta. Cinco skips do implementador precisam ser identificados no próximo relatório; resultados históricos não viram execução nova.

ARCHITECT RECONCILIATION COMPLETE: YES
INDEPENDENT CHECKPOINT1 REVIEW COMPLETE: YES
CHECKPOINT1 APPROVED: NO
CHECKPOINT2 IMPLEMENTATION AUTHORIZED: NO
FINAL SPECIFICATION FROZEN: YES
CODE REPOSITORY MODIFIED BY ARCHITECT: NO
AUTOMATED DISPATCH: NO
