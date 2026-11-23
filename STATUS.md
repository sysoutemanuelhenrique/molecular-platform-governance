# Coordenação — Incremento 021: draft-1 publicado para revisão independente

Atualizado em 23/11/2026 por Codex arquiteto, após autorização expressa de Emanuel para redigir o rascunho incorporando P-1 a P-5 e NOTE-F1, publicar no governance e preparar revisão, sem implementar ou congelar contrato.

| Campo | Estado |
|---|---|
| Branch de coordenação | docs/020-a-candidate1-review-20261020 — nome histórico preservado |
| Entrada desta redação | 3f0f13427ff347acc53e56951f077cf0b29e4925 |
| Código main, read-only | 08b797e0985e123ffd4d7ca7e5a5e8f040e63851 |
| Main do governance preservada | a47183dfec8213c765ed43ae482c8c227760a3d5 |
| 020 / 020-A | 020 concluído no escopo integrado; 020-A em STAND-BY, sem retomada |
| D-01(b)/D-02 | Escolhas de escopo aprovadas no registro próprio, sem aprovação geral de implementação |
| Focal anterior | 8778b83844fe9bff9b61862743277d5ee3172ac5; 11 itens fechados/4 parciais |
| Autorização desta etapa | increments/021/06-draft-specification/evidence/OWNER_DRAFT_AUTHORIZATION.md |
| Rascunho | increments/021/06-draft-specification/INCREMENT_021_DRAFT_SPECIFICATION.md |
| Anexos do rascunho | evidence/SCHEMAS_021.md, evidence/CATALOG_021.json, evidence/SCENARIOS_021.csv |
| Manifesto atual | increments/021/06-draft-specification/evidence/FILE_IDENTITIES.json |
| Tarefa de redação | tasks/021-DRAFT-SPECIFICATION.json — COMPLETED_DRAFT_PUBLISHED_FOR_REVIEW |
| Próxima tarefa | tasks/021-DRAFT-REVIEW.json — READY_FOR_DISPATCH, NOT_DISPATCHED |
| P-1 a P-5 / NOTE-F1 | Soluções propostas no draft-1; não fechadas independentemente por sua redação |
| Cenários | 140 propostos: CP1 40 / CP2 50 / CP3 30 / CP4 20; nenhum executado nesta etapa |
| Catálogo | 77 categorias; tags/chaves/ações e testes propostos; restrições de cobertura explícitas |
| Próximo ator | Claude revisor independente, separado do implementador, quando acionado com o SHA exato |
| Implementador | Aguarda; nenhum checkpoint de código autorizado |
| Relay automático | Não configurado |

## Soluções e pontos que a revisão deve confrontar

P-1 exige reconhecimento do complemento X antes que exclusão de cadeia conte como decisão explícita para materialização. P-2 exige reconhecimento vinculado do conjunto O fora de S. P-3 exige uniformidade integral também para asyms não poliméricos com micro-heterogeneidade. P-4 tem matriz 3×5 e critério fonte de identidade, com justificativa conservadora corrigida. P-5 tem catálogo por tags/relações/ações/testes. NOTE-F1 separa hash dos bytes e decodificação/normalização YAML, preservando caminhos/ids reais do 020.

Limitação importante: o perfil pode recusar mmCIFs válidos sem contexto explícito de operador para conexões sobreviventes ou com categorias/tags fora do catálogo. O revisor deve avaliar a suficiência desse recorte; não está autorizado a ampliar ciência silenciosamente nem tratar a restrição como capacidade geral já demonstrada.

## Preservação e evidência

Nenhum estudo, parecer, reconciliação, aprovação anterior ou manifesto histórico foi editado. Cada manifesto histórico permanece vinculado ao seu commit; o manifesto de preparação é de 3f0f134, não da versão atual de STATUS/tarefas. Os novos documentos são um rascunho e anexos revisáveis.

Reverificados 66 blobs da baseline e sua sintaxe Python; validada consistência documental de JSON/CSV/catálogo/cenários/whitespace. Não houve instalação, pytest, Gemmi executado, transformação científica, Windows ou concorrência. Análise de fonte e geração de documentação não são testes de produção. Nenhum agente foi acionado automaticamente.

OWNER DRAFT WRITING AUTHORIZATION RECORDED: YES
DRAFT SPECIFICATION COMPLETE: YES
READY FOR INDEPENDENT DRAFT REVIEW: YES
INDEPENDENT DRAFT REVIEW COMPLETE: NO
READY FOR IMPLEMENTATION: NO
FINAL SPECIFICATION FROZEN: NO
CODE REPOSITORY MODIFIED: NO
AUTOMATED RELAY ACTIVE: NO
