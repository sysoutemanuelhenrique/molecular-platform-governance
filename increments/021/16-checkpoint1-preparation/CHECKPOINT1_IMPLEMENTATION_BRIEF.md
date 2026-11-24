# Preparação do Checkpoint 1 — Incremento 021

Data: 24/11/2026. Arquiteto: Codex. Esta preparação é documental e não autoriza execução. A aprovação anterior congelou a especificação e excluiu implementação; o pedido “proximo passo” não é tratado como autorização de código.

## 1. Objeto concreto para autorização

Tarefa: 021-CHECKPOINT1-IMPLEMENTATION, a executar apenas por Claude implementador em sessão separada do revisor, depois de autorização direta do responsável para essa tarefa exata. Base de código: main @ 08b797e0985e123ffd4d7ca7e5a5e8f040e63851. Branch proposta de código: feature/increment-021-receptor-materialization, criada dessa base somente quando autorizada. Não criar branch agora.

Contrato: increments/021/15-final-specification/INCREMENT_021_FINAL_SPECIFICATION.md no commit de governance b0e60f6528f6fcb828aa6dd5577824e08c7c9fac; 377 linhas, 64.746 bytes, SHA-256 5de705d609eaf158b0b29a99a0d02e24be4ed0b19d8e127c7e8d70c93aca1bd8. Os quatro anexos identificados em FROZEN_PACKAGE.json integram o contrato, sem depender de main do governance. A tarefa JSON identifica cada arquivo. Cabeçalhos históricos dos anexos não anulam o congelamento formal do pacote.

## 2. Allowlist fechada do CP1

Somente dois arquivos novos no repositório de código:

- src/molecular/receptor_materialization.py
- tests/test_receptor_materialization.py

Nenhum src/test existente, pyproject.toml, adapter, storage, registry, service ou CLI pode ser alterado neste checkpoint. Nenhuma fixture física nova: o diretório de fixtures pertence aos próximos checkpoints. Não tocar no 020-A, seus documentos/worktree/branch nem em Claude outputs/, _figura_curcumina/ ou increment-009-review.txt.

## 3. Entrega de domínio

Implementar DTOs e records novos necessários ao domínio, validações estritas/imutáveis/fechadas do SCHEMAS, serialização/canonicalização/envelopes de hash e regras puras de plano S/D/U/X/O e reconhecimentos. Não confundir frozen/extra=forbid com ausência de coerção; cobrir os campos novos e elementos de coleções, inclusive str/bytes, bool/int, enums, datas e nulls. A conversão explícita de arrays para tuplas só ocorre nas fronteiras declaradas.

O planner recebe DTOs próprios em memória e os registros/contextos tipados pertinentes. Não abre RAW/YAML, não importa Gemmi/RDKit, não baixa arquivos e não cria recursos. Define decisões de retenção/uniformidade, conjuntos completos X/O, acks e hashes sem assumir pertencimento biológico por auth_asym. Não preencher consentimento automaticamente, inventar geometria, converter entrada 020 em nova inspeção ou executar serviços científicos.

Reutilizar compute_inspection_id de receptor_inspection.py para a identidade 020 de sete campos: parser_name, parser_version, protein_input_id, raw_checksum, raw_format e as constantes existentes de schema/profile. Não editar o helper antigo nem reconstruir o inventário como substituto da inspeção referenciada. ReceptorSelectionPolicy e ResolvedReceptorSelection existentes continuam com seus contratos atuais.

A versão da aplicação é entrada observada pela futura camada de aplicação, não descoberta pelo domínio via I/O científico. Preservar sua exclusão de plan_key/policy e sua inclusão no request conforme o contrato. Os DTOs puros podem representar decisões/campos futuros, mas não implementar antecipadamente parsing DOM, filtros de catálogo/serializer mmCIF, reservas NTFS, publicação, loaders ou funções públicas de service dos CP2–4.

Não simular dependências ausentes para apresentar um fluxo final funcionando. Campos que só serão fornecidos pelo adapter real devem receber DTOs de entrada declarados nos testes do domínio, sem stubs que retornem “sucesso científico” constante. O corpo completo da especificação tem precedência sobre esta instrução de checkpoint.

## 4. Prova dos 43 cenários

T021-001–040 e T021-159–161. A lista literal está na tarefa JSON; estímulos e resultados são os do CSV congelado. Nenhum desses IDs é removido e T021-162 permanece no CP2.

Para T021-030, CP1 prova identidade/equivalência de política e preservação do record/timestamp por funções puras, se receber record existente; não afirma create-once persistente ou reuse real de registry, que só será provado no CP3. T021-024/038 provam a parte pura de exclusão/ack e condicionamento do plano; a leitura de conexões do RAW e a matriz de simetria real continuam no CP2. T021-161 prova a representação/validação de arrays/action do domínio, sem fingir que um serializer já omitiu categorias reais.

Testes devem chamar funções/classes reais do módulo de produção novo com oráculos explícitos. Não copiar o algoritmo para produzir expected, não montar uma fachada de Application Service em helpers de teste, não pytest.raises(Exception), não mock excessivo nem usar a própria chave produzida como única prova de seu valor esperado. Para vetores de hash, usar bytes/payloads explícitos e golden values independentes; checksums vinculados a fixtures devem derivar dos bytes reais apresentados, nunca alegar que um hash arbitrário prova RAW verificado.

Manter uma matriz cenário→teste→assertion→limite da prova, distinguindo cenário, função, parametrização e item coletado. Os 43 cenários não exigem exatamente 43 itens pytest. Não apresentar teste de DTO como validação de produção de Windows, Gemmi, proveniência de arquivo ou persistência.

## 5. Verificações locais quando a tarefa estiver autorizada

Preflight: confirmar repositório/origin, branch/HEAD local, main remota, working tree e índice. Se houver alterações rastreadas/staged ou colisão dos dois caminhos novos, parar e reportar, sem limpar/stash/reset. Itens não rastreados preservados não devem ser lidos, movidos, adicionados ou removidos. Não inferir estado local a partir deste chat. Usar a pasta original molecular-platform no Windows quando for o checkout disponível; não retomar o worktree 020-A.

Conferir o snapshot exato de autorização no governance e os cinco hashes normativos antes de implementar. Mudança remota inesperada, nome de branch já existente ou restrição do ambiente exige reconciliação, não force/contorno. Não atualizar main local/remota para obter a branch de trabalho e não usar rebase/amend/reset.

Usar ambiente Python compatível com pyproject.toml (>=3.11) e dependências existentes/venv do projeto. Não instalar Python globalmente ou mudar pins. Se indispensável instalar dependências, fazê-lo somente em venv externo ao conteúdo rastreado e com o pyproject verificado; relatar ambiente e pacotes. CP1 não depende de executar Gemmi. Não inventar resultado se a suíte depender de pacote ausente; registrar skips/limites.

Coletar a baseline antes das mudanças com python -m pytest --collect-only -q para reconciliar IDs/itens novos. Após implementar, executar python -m pytest tests/test_receptor_materialization.py -q e a suíte completa uma vez com python -m pytest -q. Repetir apenas por alteração/falha/risco concreto. Verificar git diff --check, diff completo e allowlist antes de qualquer commit. Contagens históricas não substituem execução atual. Não criar testes de outros checkpoints para forçar um número de itens.

## 6. Entrega e publicação após autorização própria

Quando o responsável autorizar expressamente implementação, testes, commit e push desta tarefa, o implementador poderá publicar somente a branch de código proposta, com commit normal e staging explícito dos dois caminhos. Nenhum push antes dessa autorização. Não abrir PR, fazer merge, aprovar no GitHub, tocar main ou iniciar CP2.

Relatório no governance: increments/021/17-checkpoint1-implementation/CLAUDE_INCREMENT_021_CHECKPOINT1_IMPLEMENTATION_REPORT.md e evidências próprias em evidence/claude-*. Usar branch própria do implementador baseada no snapshot de autorização; não editar STATUS/tarefas/especificação. Informar inputs/hash, SHA de código/parent/base, matriz dos 43 cenários, comandos/versões/resultados reais, reconciliação da coleta, diff/allowlist, limitações e identidades completas. Se push falhar, não declarar publicação nem contornar restrição de sessão.

Próximo gate após entrega: triagem do arquiteto e revisão independente do CP1 por sessão separada do implementador. A aprovação do CP1 não autoriza CP2 automaticamente. Nenhum agente foi acionado pela preparação desta tarefa.

CHECKPOINT1 TASK PREPARED: YES
OWNER IMPLEMENTATION AUTHORIZATION RECORDED: NO
IMPLEMENTATION AUTHORIZED: NO
FINAL SPECIFICATION FROZEN: YES
CODE REPOSITORY MODIFIED: NO
