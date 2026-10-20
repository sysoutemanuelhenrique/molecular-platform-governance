# Aprovação do responsável — congelamento do 020-A e autorização do Checkpoint 1

Registrado por Codex, arquiteto, em 20/10/2026. Fonte: mensagem direta de Emanuel Henrique da Silva nesta conversa, imediatamente após a apresentação da solicitação identificada abaixo.

## Mensagem recebida e objeto aprovado

> aprovado

O contexto apresentado ao responsável foi: congelar a candidate1 revisada; autorizar somente DTOs, perfis, adaptador RDKit e testes do Checkpoint 1 nos quatro arquivos delimitados; permitir commit/push em branch própria e publicação de evidência, sem PR/merge. A mensagem não foi inferida de um parecer, arquivo ou commit de agente. Não há identificador de mensagem exportado nesta sessão; este registro documenta fielmente a mensagem e seu contexto, sem inventar assinatura ou aprovação formal GitHub.

Solicitação: increments/020-A/07-owner-decision/INCREMENT_020_A_FREEZE_AND_CP1_DECISION_REQUEST.md no snapshot 11e571a856c2e0dc6b169160a79f9f5eeb4805e3; SHA-256 fdaed67a4dbdae946d0c92f41f2be9ab71c36555addfc2e3aacf9a6d3841ca09.

Candidata aprovada: increments/020-A/05-final-candidate/INCREMENT_020_A_FINAL_SPECIFICATION_CANDIDATE.md, snapshot revisado 99b181e22663ed53341f131abe26222c41c43795; SHA-256 123596d03947f89321e6e623e3f0e7a2b88f38de42cd510a59f31cfd16d67ad4; 70.346 bytes; 575 linhas. Original preservado.

Parecer independente: increments/020-A/06-candidate-closure/CLAUDE_CANDIDATE1_CLOSURE_REVIEW.md no commit 7f1f75219203eb1a691e454db170900ca81536e8; SHA-256 9064866b6b3f0c2c54d9efc859a964ad314dbf25675ba4c112c97f22044363bd; 18.902 bytes; 190 linhas. Resultado: 0 BLOCKERS, 0 MAJORS, 0 MINORS e 2 NOTES não bloqueantes aceitas. Parecer preservado na branch do revisor.

## Finalização executada pelo arquiteto

Novo arquivo final: increments/020-A/08-final-specification/INCREMENT_020_A_FINAL_SPECIFICATION.md.

- SHA-256: cfbc6ea4bbb58f987deb3f73e45fc39d5b79d0cfaa2de8e0a7870a9937386e9c
- Bytes: 71904
- Linhas lógicas: 586
- Mudanças: apenas título/apresentação e registros de processo/status das seções 1, 19, 21 e 22.
- Preservação byte a byte: seções 2–18 e 20, incluindo APIs, ciência, gramáticas, DTOs, limites, taxonomia, CLI, matriz de 80 cenários, allowlist e checkpoints.

Diff administrativo e JSON de verificação acompanham este registro. Não houve mudança científica nem nova implementação. Nenhum resultado de pesquisa foi renomeado como teste de produção.

## Autorização delimitada

Código: sysoutemanuelhenrique/molecular-platform; baseline main reconfirmada em 08b797e0985e123ffd4d7ca7e5a5e8f040e63851; branch de implementação feature/increment-020-a-molecular-characterization, ainda inexistente no remoto no preflight desta decisão. Tarefa: tasks/020-A-CHECKPOINT1.json. O implementador deve aguardar a publicação dessa tarefa como AUTHORIZED, com final identificado, e reconfirmar os gates antes de começar.

Exatamente quatro arquivos autorizados neste checkpoint:

- src/molecular/characterization.py (novo);
- src/molecular/rdkit_tautomer.py;
- tests/test_characterization.py (novo);
- tests/test_rdkit_tautomer.py.

Permissões: implementar o Checkpoint 1, testar, criar commit e push nessa branch de código, publicar relatório/evidências próprios em branch do governance sob increments/020-A/09-checkpoint-1/. Stage por caminhos explícitos, confirmação das refs e sem sobrescrever trabalho alheio. O implementador não edita STATUS.md/tarefas centrais. O fechamento exige revisão independente antes de liberar o Checkpoint 2.

Não autorizados: Checkpoints 2/3; serviço/leitores/CLI novos nesta etapa; 020-B/020-C/021; expansão de allowlist ou alteração de contrato; PR/merge; mudanças de main, configuração ou visibilidade; force push, amend, reset ou rebase. Preservar increment-009-review.txt e _figura_curcumina/. Automação não ativada.

Esta autorização não declara entrega ao professor: o Checkpoint 1 isolado não oferece o novo comando público. A prova dos leitores Windows11/NTFS permanece no Checkpoint 2.

OWNER APPROVAL RECORDED: YES
FINAL SPECIFICATION FROZEN: YES
AUTHORIZED CHECKPOINT: 1
CHECKPOINT 2 AUTHORIZED: NO
CHECKPOINT 3 AUTHORIZED: NO
PULL REQUEST AUTHORIZED: NO
MERGE AUTHORIZED: NO
AUTOMATED RELAY ACTIVE: NO
CODE REPOSITORY MODIFIED BY ARCHITECT: NO
