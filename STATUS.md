# Coordenação — correção focal do Checkpoint 1 do 020-A

Atualizado em 20/10/2026, data local do responsável. Parecer integral/evidência recebidos, lidos, identidades verificadas e originais publicados sem alteração. Resultado: REQUEST CHANGES; CP1 não aprovado.

| Campo | Estado |
|---|---|
| Branch documental | docs/020-a-candidate1-review-20261020 |
| Main do governance preservada | a47183dfec8213c765ed43ae482c8c227760a3d5 |
| Código revisado CP1 | f8416b845efe93f9e47deca97f01a355e4e679ba |
| Main/baseline do código | 08b797e0985e123ffd4d7ca7e5a5e8f040e63851 |
| Branch de código | feature/increment-020-a-molecular-characterization |
| Final congelado | 665fb8b9cb4e1c7e0d0b9f1db98ec2adaa63bfed |
| Parecer/evidência originais publicados pelo arquiteto | 5583734475103991fb12ed8b26689cf4ad8a0eba |
| Revisão independente | 0 BLOCKERS / 2 MAJORS / 2 MINORS / 5 NOTES; REQUEST CHANGES |
| Tarefa ativa | tasks/020-A-CHECKPOINT1-CORRECTIONS.json — AUTHORIZED |
| Autorização | Escopo original CP1 aprovado por Emanuel, snapshot 85ce45ce5cc635d75035664dd612ca6c0a839dac; sem expansão |
| Próximo ator | Claude implementador, sessão separada da revisão |
| Próximo gate | Reverificação independente focal dos quatro achados e regressões concretas após novo HEAD |
| Relay automático | Não configurado; entregar comando manual ao implementador |

Contrato SHA-256 cfbc6ea4bbb58f987deb3f73e45fc39d5b79d0cfaa2de8e0a7870a9937386e9c, 586 linhas/71.904 bytes, permanece intacto. Parecer: 72d658ad6184a2411d9cb56dbbb3b49861ccd64621126cdb5d62aa7b048f4399, 153 linhas/24.918 bytes. Evidência: 8d24af595759154d6c798c11a2afcc44a5c5469faf80abe4bff14f6434540cea, 54 linhas/2.183 bytes. As duas cópias remotas foram relidas e comparadas aos anexos byte a byte. O commit local f6587d4 do revisor continua não apresentado como publicado; há proveniência separada.

Reconciliação: increments/020-A/11-checkpoint-1-corrections/INCREMENT_020_A_CP1_REVIEW_RECONCILIATION.md. Corrigir os dois MAJORs (estriteza real dos DTOs/literais; interrupções por fase) e os dois MINORs (marcador real de restauração de logs; SGroup/AND/OR por bytes). A recusa de Z e a localização do helper SVG permanecem aceitas; não alterar o contrato. Novo relatório deve trazer errata de +679/−1 do adaptador original, sem editar relatório anterior.

Pesquisa do arquiteto confirmou que strict=True sozinho não resolve Literal neste Pydantic e demonstrou rota RDKit V3000 para fixtures reais. Também exercitou os três buffers no adaptador exato do CP1: unsupported-structure. Essas são sondas Linux, não pytest, testes novos ou evidência Windows. Não foi executada suíte independente pelo arquiteto/revisor.

Manifestos anteriores identificam seus snapshots históricos. O manifesto em increments/020-A/11-checkpoint-1-corrections/FILE_IDENTITIES.json identifica esta liberação. Pareceres, evidência e relatórios originais preservados. Implementador publica somente novo relatório/evidências próprios nos caminhos da tarefa.

FULL INDEPENDENT REVIEW VERIFIED: YES
FINAL SPECIFICATION FROZEN: YES
CHECKPOINT 1 CORRECTIONS AUTHORIZED: YES
CHECKPOINT 1 APPROVED: NO
CHECKPOINT 2 AUTHORIZED: NO
CHECKPOINT 3 AUTHORIZED: NO
AUTOMATED RELAY ACTIVE: NO
CODE REPOSITORY MODIFIED BY ARCHITECT: NO
