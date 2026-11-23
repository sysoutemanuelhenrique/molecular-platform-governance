# Entregas e respostas pelo governance

Data: 23/11/2026. Responsável pela orientação: Codex arquiteto, atendendo à instrução direta de Emanuel para que Claude registre suas respostas no governance e o arquiteto as leia diretamente.

## 1. Canal documental

Repositório: sysoutemanuelhenrique/molecular-platform-governance. A branch de coordenação vigente é docs/020-a-candidate1-review-20261020; seu nome é histórico e não autoriza retomar o 020-A. Ler STATUS.md na branch/snapshot explicitamente indicados, nunca assumir que main contém a tarefa mais recente.

Pareceres, relatórios de implementação, respostas a dúvidas, evidências e impedimentos pertinentes à tarefa devem ser gravados como documentos no caminho autorizado e publicados em branch própria. O chat serve apenas para aviso curto de entrega, esclarecimento indispensável ou pedido de decisão que a tarefa não permita resolver. O responsável não precisa copiar relatórios completos entre chats.

## 2. Disciplina de entrega

1. Confirmar tarefa, papel, snapshot e identidades dos inputs; divergência suspende a ação.
2. Escrever somente nos caminhos permitidos. Quando o path necessário não estiver autorizado, registrar a dúvida sem ampliar a allowlist por iniciativa própria.
3. Preservar documentos anteriores e de outros autores; respostas novas usam caminhos novos quando assim exigido pela tarefa.
4. Conferir diff, identidades e ausência de dados sensíveis; commit e push somente quando a tarefa os autorizar.
5. Confirmar a branch/commit no remoto antes de declarar PUBLICADO. Se falhar, informar BLOQUEADO e não apresentar arquivo/commit apenas local como entregue.
6. Emitir no chat somente o recibo abaixo, com o link permanente. O documento remoto permanece a fonte do parecer.

Modelo de recibo:

- Tarefa e papel: <task_id / revisor ou implementador>
- Resultado: <veredito ou estado da entrega; sem ampliar a autorização>
- Repositório e branch: <owner/repo / branch>
- Commit remoto confirmado: <SHA completo>
- Arquivo principal: <path e link permanente blob/SHA/path>
- Identidade: <linhas, bytes, SHA-256 completo>
- Evidências: <paths ou manifesto; limitação de execução em uma frase>
- Próximo ator: <arquiteto; ou decisão expressa do responsável, conforme tarefa>

## 3. Papéis e limites

Claude revisor publica parecer/evidências em sua branch; não edita STATUS.md, tarefas centrais, estudo do arquiteto ou código. Claude implementador somente modifica código sob especificação final identificada e checkpoint autorizado; seus relatórios e evidências seguem a tarefa própria. Uma dúvida ou novo achado não autoriza editar contrato congelado.

Codex arquiteto lê os documentos pelo commit remoto, confere identidades e registra recebimento/reconciliação no governance. Não é necessário merge da branch do revisor para ler o parecer; referência cruzada pelo commit é suficiente. O arquiteto mantém STATUS e tarefas centrais. A aprovação/congelamento/autorização de implementação permanece com Emanuel.

## 4. Estado do 021 nesta comunicação

A revisão da tarefa 021-RECEPTOR-MATERIALIZATION-STUDY-REVIEW-V2 já foi publicada por Claude em debeba6f4370c6f5dd77d2273420abf8a828e9f8 e recebida pelo arquiteto. Não refazer a revisão nem produzir outra entrega apenas por ler esta orientação. Aguardar o resultado da reconciliação e uma tarefa focal posterior, se necessária.

O 020-A continua em stand-by. Não há autorização de implementação do 021, congelamento, PR, merge, tag, release ou mudança de main.

## 5. O que esta orientação não automatiza

Um commit no governance não inicia outra sessão de IA nem garante monitoramento contínuo. Não há relay automático configurado. O aviso curto de commit/caminho permite ao arquiteto consultar a entrega quando acionado; nenhuma leitura ou execução futura deve ser declarada sem ter ocorrido.

GOVERNANCE AS DOCUMENT DELIVERY CHANNEL: YES
FULL REPORT COPY THROUGH CHAT REQUIRED: NO
AUTOMATED RELAY ACTIVE: NO
IMPLEMENTATION AUTHORIZED: NO
