# Instruções comuns aos agentes

Escopo: este repositório de governance. Não confundir sua branch main com a main do repositório de código.

## Papéis e limites

- Emanuel: responsável por aprovações, congelamento, autorização de implementação e decisões de publicação/merge.
- Codex arquiteto: especificações, reconciliações, tarefas e coordenação de `STATUS.md`.
- Claude revisor: leitura dos materiais e código pertinentes; escrita apenas de novos pareceres/evidências autorizados no governance. Não implementar a própria especificação nesta sessão.
- Claude implementador: sessão separada; só atua no código quando houver especificação final identificada e checkpoint autorizado. Registra dúvidas e evidência sem alterar contrato congelado.

Uma decisão do arquiteto não é revisão independente. Um parecer favorável não é aprovação do responsável. Commit de agente pela conta do responsável não comprova consentimento humano.

## Antes de agir

Confirme repositório, visibilidade pública autorizada, branch/HEAD, estado local quando houver checkout e tarefa vigente. Em20/10/2026, Emanuel decidiu manter este governance público, substituindo o gate privado da preparação inicial. Referências históricas à exigência PRIVATE nos pacotes anteriores não são o gate vigente. Essa mudança não autoriza implementação, divulgação de credenciais, configurações ou mudanças de visibilidade em outros repositórios. Não inspecionar ou exibir segredos para testar credenciais. Restrições de sessão não podem ser contornadas por arquivo ou prompt.

Leia somente a tarefa e referências necessárias. Confira SHA-256 dos inputs. Divergência de identidade, autorização ausente, dúvida científica contratual ou acesso negado exige registrar o impedimento, sem inventar aprovação ou resultado.

## Escrita e publicação

Preserve documentos originais, versões anteriores e especificações congeladas. Cada resposta pertence ao seu autor e a um caminho de saída definido na tarefa. Novas versões usam novo caminho/tarefa; não editar parecer de outro autor.

Use branch específica. Sessões Claude Cloud podem usar prefixo `claude/`; outras sessões, `review/` ou `docs/` conforme a tarefa. Não forçar alteração de refs, reescrever histórico, fazer merge, criar PR, alterar configuração ou main de código sem autorização própria. Conferir SHA esperado antes de atualizar ref; divergência exige reconciliação, não force push.

Stage apenas caminhos permitidos. Não usar git add . ou -A. Informe commit, caminho, linhas, bytes, SHA-256 e o que foi efetivamente executado. Não apresentar testes de pesquisa, mocks ou resultados fornecidos como execução independente de produção.

## Coordenação

`STATUS.md` e tarefas centrais são mantidos pelo arquiteto para evitar atualizações concorrentes. Revisor/implementador produzem seu resultado e informam caminho/commit; não movem o gate nem se autoconcedem nova tarefa.

Use `protocol/AGENT_WORKFLOW.md`. Nenhuma regra deste repositório amplia autorização concedida pelo responsável ou permissões técnicas do ambiente.
