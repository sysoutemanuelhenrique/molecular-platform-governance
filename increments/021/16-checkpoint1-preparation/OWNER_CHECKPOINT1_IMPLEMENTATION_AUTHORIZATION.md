# Autorização do responsável — implementação do Checkpoint 1, Incremento 021

Registro em 24/11/2026, America/Sao_Paulo, por Codex arquiteto. Fonte: instrução direta de Emanuel Henrique da Silva nesta conversa. O registro preserva a mensagem humana; não é assinatura eletrônica ou certificação de terceiro, e não se infere autorização só pela conta usada no commit.

## Mensagem literal

> Autorizo o Claude implementador a executar somente o
> Checkpoint 1 do Incremento 021, conforme a tarefa
> 021-CHECKPOINT1-IMPLEMENTATION publicada no commit
> e617717bd8db707737c9c5cba8f404776ae2d260.
>
> Autorizo implementação, testes, commit e push apenas
> dos dois arquivos permitidos, na branch
> feature/increment-021-receptor-materialization,
> partindo da baseline
> 08b797e0985e123ffd4d7ca7e5a5e8f040e63851.
>
> Autorizo publicar o relatório nos caminhos definidos
> da tarefa, em branch própria do governance.
>
> Não autorizo CP2, alteração do contrato congelado,
> PR, merge ou alteração de main.

## Objeto identificado

Tarefa aprovada: tasks/021-CHECKPOINT1-IMPLEMENTATION.json no commit e617717bd8db707737c9c5cba8f404776ae2d260, 160 linhas, 6.715 bytes, SHA-256 65ab09435da8d89b2e3229e60c962a68f4b0cdc68a883e629feb3e3736af3531. Brief aprovado: increments/021/16-checkpoint1-preparation/CHECKPOINT1_IMPLEMENTATION_BRIEF.md, 64 linhas, 8.731 bytes, SHA-256 c1c33e8eb206302399658f6bd5011655ee68a9f628aa49aff6d1108895c8bd64. Essas versões de preparação permanecem preservadas em seu snapshot; suas frases históricas de autorização pendente não anulam esta instrução posterior.

Código: sysoutemanuelhenrique/molecular-platform, baseline main @ 08b797e0985e123ffd4d7ca7e5a5e8f040e63851. Branch permitida ao implementador: feature/increment-021-receptor-materialization. Na consulta remota desta autorização, main coincide e a branch proposta não existe; o implementador deve revalidar antes de criar/trabalhar. O arquiteto não a criou.

Contrato congelado: increments/021/15-final-specification/INCREMENT_021_FINAL_SPECIFICATION.md no commit b0e60f6528f6fcb828aa6dd5577824e08c7c9fac; 377 linhas, 64.746 bytes, SHA-256 5de705d609eaf158b0b29a99a0d02e24be4ed0b19d8e127c7e8d70c93aca1bd8. Quatro anexos e normative package key d1726d1ae0ae5929e6f8a97f9bb0916e3e205af6d841246b7fba58972570f69b permanecem intactos. A autorização não muda o contrato.

## Permissões limitadas ao CP1

- Implementação e testes pelo Claude implementador, separado da sessão de revisão.
- Apenas src/molecular/receptor_materialization.py e tests/test_receptor_materialization.py no diff de código; ambos novos a partir da baseline indicada.
- Commit normal e push desses dois caminhos apenas na branch permitida; staging explícito, sem force/rebase/amend/reset e sem tocar main.
- Relatório em increments/021/17-checkpoint1-implementation/CLAUDE_INCREMENT_021_CHECKPOINT1_IMPLEMENTATION_REPORT.md e evidências em increments/021/17-checkpoint1-implementation/evidence/claude-*, publicados em branch própria do governance conforme a tarefa. Não editar STATUS, tarefas, contrato ou pareceres pelo implementador.

Mantidos os 43 cenários, fronteira pura do domínio, preflight, verificações e limites da tarefa aprovada. Escopo restrito a CP1; não implementar adapter Gemmi, storage, registry, service ou CLI dos CP2–4. Não instalar Python globalmente, mudar pins ou contornar restrição de sessão. Ambiguidade contratual volta ao arquiteto, não autoriza alterar a especificação congelada.

Não autorizados: CP2 ou posteriores, PR, merge, tag/release, aprovação formal no GitHub, alteração de main/configuração/visibilidade ou automação. Preservar 020-A em stand-by e Claude outputs/, _figura_curcumina/ e increment-009-review.txt. O próximo gate após a entrega é triagem do arquiteto e revisão independente do CP1; não há avanço automático de checkpoint.

## Estado do encaminhamento

Autorização registrada, tarefa marcada AUTHORIZED e pronta para encaminhamento manual. Nenhum agente foi acionado automaticamente. Este registro não afirma que implementação, testes, commit/push de código ou entrega já ocorreram. O arquiteto somente publicou documentos de coordenação no governance.

OWNER CHECKPOINT1 AUTHORIZATION RECORDED: YES
CHECKPOINT1 IMPLEMENTATION AUTHORIZED: YES
CHECKPOINT1 CODE COMMIT AND PUSH AUTHORIZED: YES
CHECKPOINT1 GOVERNANCE REPORT PUBLICATION AUTHORIZED: YES
CHECKPOINT2 IMPLEMENTATION AUTHORIZED: NO
FINAL SPECIFICATION FROZEN: YES
IMPLEMENTATION STARTED BY ARCHITECT: NO
CODE REPOSITORY MODIFIED BY ARCHITECT: NO
AUTOMATED DISPATCH: NO
