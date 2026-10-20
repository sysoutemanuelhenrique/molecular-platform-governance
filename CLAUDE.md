# Entrada para Claude

Leia `AGENTS.md`, `protocol/AGENT_WORKFLOW.md`, `STATUS.md` e a tarefa ativa. Esta entrada não concede acesso GitHub: a conta/sessão precisa ter o repositório autorizado pela integração suportada.

Nesta rodada, seu papel é **revisor independente** do020-A. Não atuar como implementador. A tarefa inicial é `tasks/020-A-CANDIDATE1-CLOSURE.json`.

Se o repositório estiver indisponível, não insistir com tokens rejeitados nem tentar contornar o sandbox. Registre `BLOCKED_ACCESS` com diagnóstico sem credenciais; o responsável deve configurar acesso e selecionar o repositório em uma sessão adequada. Depois de inicializado, use uma sessão vinculada ao governance; o código pode ser referência somente de leitura quando a tarefa o exigir.

No fechamento atual, o pacote e os dados brutos bastam para a verificação documental focal; se não puder executar RDKit ou consultar o código, declare essa limitação. Não exigir implementação dos leitores Windows antes de aprovar a redação do contrato.

Não iniciar /loop, /schedule, GitHub App, Actions ou agente implementador por este arquivo. A ativação terá tarefa separada, com escopo, gatilho e teste verificável. Não considerar a sessão atual automaticamente migrada ou continuamente ativa.
