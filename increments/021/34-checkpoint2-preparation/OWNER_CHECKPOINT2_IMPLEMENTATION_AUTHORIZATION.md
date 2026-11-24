# Autorização de implementação — Incremento 021, Checkpoint 2

Responsável: Emanuel Henrique da Silva. Registro por Codex arquiteto em 24/11/2026, America/Sao_Paulo, de mensagem direta do responsável nesta conversa. Este registro não é assinatura eletrônica ou certificação externa; a autorização decorre da mensagem humana literal, não da conta usada para publicar o commit.

## 1. Mensagem literal do responsável

```text
Autorizo somente o Checkpoint 2 do Incremento 021,
conforme tasks/021-CHECKPOINT2-IMPLEMENTATION.json
publicada no commit
a0b6083dfcaa456bcebb288120d198e3de2bf5be.

Autorizo implementação, testes, commit e push apenas
na allowlist da tarefa, na branch
feature/increment-021-receptor-materialization,
partindo de ea8dac9cdc203c337d7f3f9947b54042291f7484.

Autorizo o relatório nos caminhos definidos,
em branch própria do governance.

Não autorizo CP3, alteração do contrato congelado,
PR, merge ou alteração de main.
```

## 2. Objeto exato aprovado

- Repositório governance: sysoutemanuelhenrique/molecular-platform-governance.
- Branch de coordenação: docs/020-a-candidate1-review-20261020; snapshot preparado aprovado e confirmado remotamente: a0b6083dfcaa456bcebb288120d198e3de2bf5be.
- Tarefa aprovada: tasks/021-CHECKPOINT2-IMPLEMENTATION.json; SHA-256 dos bytes da versão preparada: 0cef77b76039071cb0d24ac20cd7ae9aa27e4db4767424074996442eaf303f1e.
- Brief preservado: increments/021/34-checkpoint2-preparation/CHECKPOINT2_IMPLEMENTATION_BRIEF.md, 109 linhas/20.421 bytes, SHA-256 9bab402c9bb103ab5da0d127bf2c966a0382bae944c8d8178c09efc82dffe4b3.
- Contrato congelado 1.0: increments/021/15-final-specification/INCREMENT_021_FINAL_SPECIFICATION.md e quatro anexos identificados na tarefa; nenhum byte normativo é alterado.
- Repositório de código: sysoutemanuelhenrique/molecular-platform; branch feature/increment-021-receptor-materialization; início exato ea8dac9cdc203c337d7f3f9947b54042291f7484, CP1 aprovado.
- Main código confirmada em 08b797e0985e123ffd4d7ca7e5a5e8f040e63851; main governance em a47183dfec8213c765ed43ae482c8c227760a3d5. Ambas preservadas.

## 3. Escopo de escrita autorizado

1. src/molecular/receptor_parsing.py
2. src/molecular/receptor_materialization.py
3. tests/test_receptor_parsing.py
4. tests/test_receptor_materialization.py
5. Novas fixtures somente sob tests/fixtures/receptor_materialization/, com os conteúdos e limites definidos na tarefa.

Implementação/testes e commit/push normais desses caminhos na mesma feature, preservando o CP1 e os fechamentos/NOTES. São os 79 cenários e as fronteiras do CP2 congelado; nenhuma permissão adicional sobre módulos existentes decorre desta lista. Preservar estado local e itens não rastreados; não reescrever histórico nem usar reset/clean/stash/rebase/amend/force para fabricar a baseline.

Relatório próprio autorizado em increments/021/35-checkpoint2-implementation/CLAUDE_INCREMENT_021_CHECKPOINT2_IMPLEMENTATION_REPORT.md e evidence/claude-*, em branch Claude própria do governance a partir do commit deste despacho autorizado. Não editar STATUS/tarefas centrais, pareceres ou documentos históricos. Confirmar publicação por consulta remota e informar SHA completo/identidades/resultados reais.

## 4. Interpretação de fase e restrições preservadas

O brief e o manifesto originais de preparação são preservados no snapshot a0b6083dfcaa456bcebb288120d198e3de2bf5be; seus marcadores de implementação não autorizada descrevem aquela fase histórica. Este registro e o estado autorizado da tarefa cumprem o gate antes ausente, sem reescrever os requisitos do brief. Para executar, usar o SHA completo da publicação desta autorização fornecido no comando de encaminhamento; não usar o SHA histórico de preparação como se já contivesse a autorização.

A tarefa autorizada é exclusivamente CP2: adapter DOM/tokens/endpoints/simetria/catálogo/saída/validação com Gemmi 0.7.5 real e extensões puras necessárias. CP3/storage/leitores Windows/publicação concorrente/registry/service e CP4/CLI permanecem excluídos. Não alterar contrato congelado, pyproject/dependências, main, visibilidade/configurações; sem PR, merge, tag, release, aprovação formal ou comentários GitHub. 020-A segue STAND-BY e os itens locais protegidos permanecem intocados.

Nenhum agente foi iniciado automaticamente; o responsável encaminha manualmente o comando ao Claude implementador, em sessão separada do revisor. O arquiteto apenas registra a autorização e publica a tarefa. A existência desta autorização não afirma implementação iniciada/concluída, execução de testes ou aprovação do CP2.

CHECKPOINT1 APPROVED BY OWNER: YES
CHECKPOINT2 IMPLEMENTATION AUTHORIZED: YES
CHECKPOINT2 CODE COMMIT AND PUSH AUTHORIZED: YES, ONLY APPROVED ALLOWLIST/BRANCH
CHECKPOINT2 OWN GOVERNANCE REPORT AUTHORIZED: YES, ONLY DEFINED OUTPUT PATHS/OWN BRANCH
CHECKPOINT2 IMPLEMENTATION STARTED BY ARCHITECT: NO
CHECKPOINT2 APPROVED: NO
CHECKPOINT3 IMPLEMENTATION AUTHORIZED: NO
FINAL SPECIFICATION FROZEN: YES
CODE REPOSITORY MODIFIED BY ARCHITECT: NO
AUTOMATED DISPATCH: NO
