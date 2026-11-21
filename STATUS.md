# Coordenação — Incremento 021: estudo e revisão independente

Atualizado em 21/11/2026, por Codex arquiteto, conforme instrução direta de Emanuel Henrique da Silva. Esta é a entrada operacional atual da branch documental; os apontamentos iniciais de README/CLAUDE.md para tarefas do 020-A são históricos, não tarefas vigentes desta rodada.

| Campo | Estado atual |
|---|---|
| Branch de coordenação | docs/020-a-candidate1-review-20261020 (nome histórico preservado) |
| Snapshot anterior preservado no histórico | 6a85b79a33bce419c0ebd2bde6793732ef4f0388 |
| Main do governance | a47183dfec8213c765ed43ae482c8c227760a3d5 — não alterar |
| Código de referência | molecular-platform, main @ 08b797e0985e123ffd4d7ca7e5a5e8f040e63851 |
| Incremento 020 | Concluído e integrado pelo PR #7; inspeção/seleção/resolução lógica, sem materialização por contrato |
| Incremento ativo | 021 — Materialização da Seleção de Receptor, somente estudo |
| Tarefa ativa | tasks/021-RECEPTOR-MATERIALIZATION-STUDY-REVIEW.json — AUTHORIZED |
| Próximo ator | Claude revisor independente, separado do implementador |
| Estudo | increments/021/01-study/INCREMENT_021_RECEPTOR_MATERIALIZATION_STUDY.md |
| Evidências/identidades | increments/021/01-study/FILE_IDENTITIES.json |
| Registro da instrução do responsável | increments/021/00-owner-decision/OWNER_STUDY_AUTHORIZATION.md |
| Recomendação provisória | Opção B: mmCIF, referencial do modelo original, decisões explícitas; assembly não nulo recusado |
| Próximo gate após parecer | Reconciliação pelo arquiteto e decisão do responsável sobre rascunho |
| Implementador | Aguarda: nenhuma tarefa nova de código autorizada |
| Relay automático | Não configurado; encaminhamento manual com SHA publicado |

## Stand-by explícito do Incremento 020-A

Por decisão direta do responsável, o 020-A fica suspenso. Não alterar, integrar ou retomar seu código, worktree, documentos históricos ou tarefas antigas. Seus arquivos, autorizações e pareceres anteriores são preservados como histórico; não devem ser executados como tarefa ativa enquanto durar esta suspensão. Esta decisão não aprova o CP1, não cancela o incremento e não autoriza CP2/CP3.

Último HEAD conhecido/preservado do 020-A: cc903d8ebbfe1916c3fce195d20fc97b206a5f54. Seu parecer focal recebido por anexo e a questão de cobertura de interrupções permanecem pendências históricas, sem disposição nova por este estudo. Nenhum arquivo de increments/020-A ou de tasks/020-A-* foi alterado nesta publicação.

## Limites da rodada do 021

A especificação final do 020 foi conferida e lida integralmente: 1.975 linhas, 210.880 bytes, SHA-256 cf6cb534f9267d51e718052c7b36a2293c522bc566c99cf3bb2ef5909385a0a6. A referência byte-idêntica acompanha o estudo. Conferidos 66 blobs da baseline e fontes oficiais do Gemmi 0.7.5. A evidência é documental/estática; não houve pytest, execução Gemmi, instalação, teste Windows ou implementação do 021. Os 48 cenários propostos não são testes executados.

O revisor publica apenas seu novo parecer/evidências nos caminhos da tarefa, em branch própria, e informa commit/caminho. Não altera STATUS nem se concede a etapa seguinte. O arquiteto lerá a entrega no GitHub quando acionado; publicação de tarefa não inicia um agente em segundo plano.

STUDY COMPLETE: YES
READY FOR INDEPENDENT STUDY REVIEW: YES
READY FOR IMPLEMENTATION: NO
FINAL SPECIFICATION FROZEN: NO
INCREMENT 020-A: STAND-BY
AUTOMATED RELAY ACTIVE: NO
CODE REPOSITORY MODIFIED: NO
