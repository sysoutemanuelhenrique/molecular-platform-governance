# Protocolo inicial de comunicação — v1, para adoção

Decisão vigente em20/10/2026: governance público, por instrução direta do responsável. O gate PRIVATE da preparação inicial fica substituído; seu registro histórico permanece nos documentos anteriores. Publicação de documentos não prova acesso de escrita pelo Claude e não ativa automação.

## 1. Unidade de trabalho

Cada tarefa identifica incremento, etapa, papel responsável, branch/ref de entrada, documentos e SHA-256, ação permitida, caminhos de saída, critério de conclusão e próximo gate. SHA de commit identifica snapshot Git; SHA-256 identifica bytes de documento. Não confundir as duas unidades.

`STATUS.md` aponta para a tarefa ativa. Não agir com base em uma pasta que apenas pareça ser a versão mais recente. Relatório novo identifica a tarefa e todos os inputs confrontados. Documentos históricos continuam consultáveis, sem edição retroativa.

## 2. Fluxo

1. Arquiteto prepara estudo/especificação e tarefa de revisão.
2. Responsável autoriza a etapa pendente conforme o contexto explícito.
3. Revisor independente confronta a versão identificada e publica parecer novo.
4. Arquiteto responde aos achados, prepara nova versão quando necessário e aponta o fechamento focal.
5. Após fechamento, responsável decide aprovação/congelamento da versão exata.
6. Uma autorização de implementação identifica especificação final, baseline, branch e checkpoint. Implementador separado executa esse escopo e registra resultados reais.
7. Revisão dos checkpoints e eventual merge seguem seus gates próprios.

Não repetir revisão integral já encerrada sem regressão ou violação concreta. Não reabrir decisão por preferência de implementação. Dúvida sobre contrato congelado volta ao arquiteto/revisor; não é licença para mudar o contrato no código.

## 3. Comandos curtos

| Comando do responsável | Semântica |
|---|---|
| revisão | Executar a revisão já identificada e autorizada na tarefa vigente |
| aprovado | Aprovar a versão e a ação pendentes identificadas, dentro do contexto explícito |
| próxima etapa | Avançar ao gate seguinte permitido pelas aprovações existentes |
| status | Consultar estado e impedimentos |
| parar | Suspender novas ações e cancelar gatilhos configurados quando tecnicamente possível |

Não expandir “aprovado” para todos os incrementos ou para implementação, merge/publicação não abrangidos pelo contexto. Ao registrar aprovação, preservar a mensagem direta do responsável e seu objeto exato. Um arquivo editado pelo agente, um evento automático ou o fato de um commit usar a conta do responsável não constituem aprovação humana por si só. Aplicam-se também as restrições de autorização da plataforma que executa cada sessão.

## 4. Saída e concorrência

O revisor grava apenas seu novo parecer nos caminhos autorizados. O implementador grava relatórios/evidência próprios e somente o código da allowlist autorizada em outro repositório/branch. O arquiteto mantém `STATUS.md` e tarefas centrais. Não há escrita simultânea planejada do mesmo documento por dois agentes.

Antes de commit/push, conferir estado local, diff e identidade dos inputs. Stage explícito. Branches novas devem partir da ref indicada; se o HEAD esperado mudou, parar para reconciliação. Não sobrescrever trabalho de outro ator, não usar reset/rebase/amend/force push para fabricar a sequência pretendida.

Resultado mínimo: task_id; papel; inputs/SHA; achados/decisões; testes e limitações; saída/caminho/SHA-256; commit publicado, se houve; gate sugerido. Aprovação formal GitHub, PR, merge, mudanças de visibilidade e configuração não decorrem da mera permissão de publicar um arquivo de parecer.

## 5. Ativação em segundo plano — ainda pendente

Os arquivos deste protocolo não mantêm processos em execução. Criar tarefa separada de ativação depois de confirmar acesso dos dois lados. Selecionar um mecanismo oficial e provar uma troca completa: evento real → execução → resultado no caminho esperado → leitura pelo outro lado.

O futuro gatilho deve limitar repositório/PR/tarefa, versão e ator. Não depender de comentário gerado por bot como se fosse sempre um evento humano suportado. Não disparar todos os agentes a cada commit. Repetição do mesmo evento/versão não pode iniciar novamente uma tarefa já concluída.

Proposta de limite para adoção: até três rodadas de revisão/reconciliação por versão de tarefa antes de solicitar decisão; limite de duração/uso deve ser configurado no mecanismo escolhido. Impedimento de acesso, identidade divergente, contrato alterado ou autorização ausente suspende a cadeia. Nenhum desses limites está tecnicamente aplicado por este texto.

Custos, credenciais e permissões são configurados nos mecanismos oficiais, sem tokens em documentos ou chat. Não instalar ferramentas ou habilitar workflows sem tarefa autorizada. A validação Windows continua gate real dos checkpoints que a exigem; uma execução Linux não a substitui.

## 6. Separação dos repositórios

Governance: instruções, especificações, pareceres, aprovações registradas e evidências. Código: implementação e testes autorizados em branch própria. Não alterar a visibilidade do código para resolver acesso ao governance. Nunca copiar itens pessoais/untracked, como increment-009-review.txt ou _figura_curcumina/, para esta estrutura.
