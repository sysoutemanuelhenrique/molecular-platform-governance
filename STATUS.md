# Coordenação — Incremento 021: parecer recebido; reconciliação pendente

Atualizado em 23/11/2026 por Codex arquiteto. O parecer de Claude foi recebido, lido integralmente e conferido no remoto. A comunicação documental passa pelas entregas no governance; o chat pode conter apenas um recibo de branch/commit/caminho. Não há execução automática de agentes.

| Campo | Estado |
|---|---|
| Branch de coordenação | docs/020-a-candidate1-review-20261020 — nome histórico preservado |
| Entrada original do estudo | 6a85b79a33bce419c0ebd2bde6793732ef4f0388 |
| Publicação v1 preservada | 599a6873b2a55d09c3497780d99794fe337a08e8 |
| Código de referência | main @ 08b797e0985e123ffd4d7ca7e5a5e8f040e63851 |
| Main do governance preservada | a47183dfec8213c765ed43ae482c8c227760a3d5 |
| Incremento 020 | Concluído no escopo de inspeção/seleção/resolução lógica; integrado pelo PR #7 |
| Incremento 020-A | STAND-BY; sem aprovação, cancelamento ou retomada |
| Fase do 021 | Revisão independente entregue; reconciliação arquitetural pendente; sem especificação final |
| Estudo original | increments/021/01-study/INCREMENT_021_RECEPTOR_MATERIALIZATION_STUDY.md — preservado |
| Complemento vigente | increments/021/01-study/continuation/INCREMENT_021_MINIMAL_CORE_STUDY.md |
| Manifesto do complemento | increments/021/01-study/continuation/FILE_IDENTITIES.json |
| Tarefa de revisão V2 | Entrega recebida por mensagem do responsável; arquivo histórico da tarefa preservado |
| Parecer recebido | claude/021-study-review-v2-20261123 @ debeba6f4370c6f5dd77d2273420abf8a828e9f8 |
| Recibo de leitura | increments/021/02-study-review-receipt/CODEX_REVIEW_RECEIPT_20261123.md |
| Achados do parecer | 0 BLOCKERS / 4 MAJORS / 5 MINORS / 3 NOTES — recebidos, ainda não reconciliados |
| Tarefa ativa do arquiteto | tasks/021-STUDY-RECONCILIATION.json — READY |
| Orientação ao revisor/implementador | communications/GOVERNANCE_DELIVERY_INSTRUCTIONS_20261123.md |
| Tarefa v1 | Preservada; substituída operacionalmente pela V2, não executar isoladamente |
| Recomendação mais recente | Perfil mínimo de B: mmCIF no modelo fonte; keep/remove efetivos; todos os altlocs retidos; recusa de assemblies e cortes de conexão declarada |
| Próximo gate | Reconciliação dos achados pelo arquiteto; decisões explícitas de escopo quando necessárias; eventual revisão focal e decisão sobre rascunho |
| Implementador | Sem nova tarefa de código autorizada |
| Relay automático | Não configurado; publicar uma tarefa não executa um agente |

## Preservação e limites

Todos os documentos históricos, inclusive o estudo v1, sua tarefa e a referência congelada do 020, permanecem intactos. Esta atualização substitui somente o apontamento operacional de STATUS. AGENTS.md e protocol/AGENT_WORKFLOW.md continuam vigentes; apontamentos de bootstrap para o 020-A não autorizam retomá-lo.

O 020-A mantém seu último HEAD conhecido cc903d8ebbfe1916c3fce195d20fc97b206a5f54 e seus achados/pareceres históricos, sem disposição nova. Não tocar em seu código/worktree/documentos/tarefas antigas. A trilha B/C de demonstração não é pré-requisito do estudo 021.

Foram verificadas as identidades e fontes descritas nos dois pacotes de estudo. Nesta rodada não houve pytest, execução Gemmi, transformação científica, instalação, teste Windows ou concorrente. Os cenários são propostas de estudo, sem contagem de testes executados. Não há revisão independente substituída por autoavaliação do arquiteto.

Catálogo de categorias, política de falhas/tentativas, chave de equivalência, primitivas de publicação e limites ainda precisam ser fechados no rascunho e confrontados antes de implementação. Um núcleo menor não dispensa RAW íntegro, referências exatas, publicação verificável ou compensação por propriedade.

STUDY COMPLETE: YES
INDEPENDENT STUDY REVIEW DELIVERED: YES
READY FOR IMPLEMENTATION: NO
FINAL SPECIFICATION FROZEN: NO
INCREMENT 020-A: STAND-BY
REVIEW RECEIVED AND IDENTITY VERIFIED: YES
RECONCILIATION COMPLETE: NO
AUTOMATED RELAY ACTIVE: NO
CODE REPOSITORY MODIFIED: NO

## Recebimento de 23/11/2026

O revisor registrou APPROVE FOR DRAFT SPECIFICATION condicionado a resolver os quatro MAJORs antes ou dentro do rascunho. O recebimento não fecha achados nem substitui decisão do responsável. As opções a/b do MAJOR-1 e a política de abrangência do MAJOR-2 ainda não foram escolhidas pelo responsável. O arquiteto deverá apresentar recomendação concreta na reconciliação antes de solicitar essas decisões.

A branch do revisor não foi mesclada; parecer e evidências são lidos pelo commit exato. Nenhuma tarefa histórica foi editada para fabricar um despacho automático. Não houve implementação ou reprodução dos ensaios C++/Windows/pytest por este recibo.
