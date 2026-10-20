# Decisão pendente do responsável — congelamento e Checkpoint 1 do 020-A

Preparado por Codex, arquiteto, em 20/10/2026. **Este documento não registra aprovação já concedida.**

## Objeto exato da decisão

Aprovar a candidate1 revisada, congelar seu contrato em um novo arquivo final e autorizar **somente o Checkpoint 1: DTOs, perfis e adaptador**, incluindo testes, commit/push em branch de implementação própria e publicação da evidência. Não autoriza os Checkpoints 2/3, PR, merge ou alteração de main.

| Entrada | Identidade verificada |
|---|---|
| Repositório de código / baseline main | sysoutemanuelhenrique/molecular-platform @ 08b797e0985e123ffd4d7ca7e5a5e8f040e63851 |
| Governance / snapshot da candidata | sysoutemanuelhenrique/molecular-platform-governance @ 99b181e22663ed53341f131abe26222c41c43795 |
| Candidata | increments/020-A/05-final-candidate/INCREMENT_020_A_FINAL_SPECIFICATION_CANDIDATE.md |
| SHA-256 da candidata | 123596d03947f89321e6e623e3f0e7a2b88f38de42cd510a59f31cfd16d67ad4 |
| Tamanho / linhas da candidata | 70.346 bytes / 575 linhas lógicas |
| Fechamento independente | commit 7f1f75219203eb1a691e454db170900ca81536e8, branch claude/lucid-faraday-xy632t |
| Caminho do parecer | increments/020-A/06-candidate-closure/CLAUDE_CANDIDATE1_CLOSURE_REVIEW.md |
| SHA-256 do parecer | 9064866b6b3f0c2c54d9efc859a964ad314dbf25675ba4c112c97f22044363bd |
| Tamanho / linhas do parecer | 18.902 bytes / 190 linhas, com quebra final |

O arquiteto leu o parecer remoto integral e recalculou sua identidade. Conferiu também a main remota do código na baseline acima e as refs do governance. O fechamento independente registra 0 BLOCKERS, 0 MAJORS, 0 MINORS e 2 NOTES não bloqueantes. Os três MINORs do draft1 estão encerrados. Não há pedido de outra revisão documental integral.

## Disposição das duas NOTES

- NOTE-A, editorial: aceitar sem mudança. O default confId=-1 continua inequívoco; não alterar o perfil ou inserir parâmetros novos para corrigir uma preferência opcional.
- NOTE-B, processo: aceitar o parecer na branch efetivamente autorizada ao Claude, identificada acima. Não mover nem reescrever seus commits.

As duas divergências de contagem do manifesto inicial são 126 linhas lógicas versus 125 caracteres LF em arquivos sem quebra final; bytes e SHA-256 coincidem. Preservar os originais, inclusive CRLF e ausência de quebra final.

## Finalização após aprovação, sem nova decisão científica

1. Registrar a mensagem direta de Emanuel, o objeto desta aprovação e as identidades acima em novo registro de decisão. Um commit de agente não substitui essa mensagem.
2. Criar increments/020-A/08-final-specification/INCREMENT_020_A_FINAL_SPECIFICATION.md a partir da candidate1, preservando o arquivo candidato. Apenas título, apresentação e encerramento de processo/status das seções 1, 19, 21 e 22 podem ser atualizados para registrar o fechamento e a aprovação efetivos. As demais seções permanecem byte-idênticas; nenhuma alteração científica, de API, DTO, limite, gramática, teste ou allowlist está incluída.
3. Produzir diff administrativo e validação mecânica dessa preservação; calcular tamanho, linhas e SHA-256 do novo arquivo final. Não inventar antecipadamente sua identidade.
4. Atualizar a tarefa preparada com a identidade final e o snapshot publicado. Só então mudar seu estado para AUTHORIZED e entregar o comando à sessão separada de Claude implementador.

Enquanto isso não ocorrer, tasks/020-A-CHECKPOINT1.json permanece PREPARED_NOT_AUTHORIZED e nenhum agente deve iniciar código com base nesta solicitação de decisão.

## Checkpoint 1 proposto para autorização

Branch de código: feature/increment-020-a-molecular-characterization, partindo exatamente da baseline indicada. Reconfirmar main remota antes de começar; avanço exige reconciliação, não usar baseline nova silenciosamente. Se a branch já existir, inspecionar seu HEAD e trabalho antes de agir. Não mudar a branch do trabalho anterior ou arquivos não rastreados.

Allowlist restrita deste checkpoint:

- src/molecular/characterization.py, novo: DTOs frozen/estritos, perfis fechados e erros próprios, sem RDKit, CLI ou I/O;
- src/molecular/rdkit_tautomer.py: adições específicas do adaptador de caracterização e fronteira opcional de desenho; preservar enumeração e promoção legadas;
- tests/test_characterization.py, novo;
- tests/test_rdkit_tautomer.py: cobertura nova e regressões pertinentes, preservando testes existentes.

Implementar parsing de bytes SDF/SMILES, elegibilidade do grafo, dez valores, cópia para desenho, SVG opcional e seu validador fechado exatamente conforme o contrato. Sem objeto RDKit na fronteira; sem serviço, leitores novos, CLI ou persistência. A leitura do asset de fonte instalado pertence ao adaptador de desenho, sem expor caminho em DTO. A indisponibilidade do desenho não pode inutilizar cálculo sem figura ou enumeração legada.

Não ampliar para atomic.py, characterization_service.py ou cli.py neste checkpoint. A allowlist total continua sendo os dez arquivos da seção 18; quatro deles compõem este checkpoint. Nenhum pyproject/dependência nova, registry, attempt, schema ou comando público deve ser alterado.

## Verificação exigida ao implementador

- Usar RDKit 2026.03.6 real. Testar produção, sem copiar o script de estudo como implementação ou tomar seus resultados por testes novos.
- Cobrir perfis/DTOs, parsing válido e inválido, limites aplicáveis, preservação científica, dez valores incluindo vetor da cafeína, isotopia/S/P, SVG/segurança e recusa all-or-nothing, sem partial result.
- Testar fronteiras de dependência, motor/versão e desenho opcional; preservar imports e resultados legados.
- Exercitar KeyboardInterrupt e SystemExit separadamente e restauração real dos logs após sucesso, falha e interrupção, usando capfd/subprocesso onde stderr nativo importa.
- Rodar testes focais de characterization e rdkit_tautomer, testes legados pertinentes e suíte completa se o ambiente permitir, reconciliando função, parametrização, itens coletados, skips e resultados. Não predeterminar aumento de passed e não usar pytest.raises(Exception).
- Registrar comandos, ambiente, versões reais, resultados, limitações, diff cumulativo, allowlist, git diff --check e status antes/depois. Não atribuir a execução Linux evidência Windows.
- A prova de leitores Windows 11/NTFS continua obrigatória no Checkpoint 2. Ela não é pré-requisito para o adaptador puro deste Checkpoint 1 nem pode ser declarada concluída por estes testes.

Saída documental do implementador, em branch própria do governance: increments/020-A/09-checkpoint-1/CLAUDE_CHECKPOINT1_IMPLEMENTATION_REPORT.md. Incluir SHA de código inicial/final e identidade da especificação final usada; não editar STATUS.md, tarefa central ou parecer alheio. O arquiteto reconcilia o resultado e prepara revisão independente antes de liberar o Checkpoint 2.

Commit/push autorizáveis restringem-se ao código deste checkpoint e ao relatório/evidências próprios no governance. Conferir refs antes de publicar; stage explícito; sem force, amend, reset, rebase, PR, merge, alteração de main ou configuração. Não tocar em increment-009-review.txt ou _figura_curcumina/.

## Limites da evidência e da apresentação

Claude executou pesquisa independente em Linux/Python 3.13.16 com o binding pinado e moléculas de SMILES; não executou produção, pytest ou leitores Windows. O arquiteto verificou a publicação e a identidade do parecer nesta etapa, sem alegar reexecução dessa sonda.

O Checkpoint 1 isolado não entrega um comando público utilizável pelo professor. Serviço e CLI exigem os checkpoints seguintes e seus próprios gates. A demonstração da versão atual continua como alternativa; não anunciar a caracterização nova como entregue antes da validação correspondente.

## Decisão a solicitar

“Aprovo o congelamento da candidate1 de SHA-256 123596d03947f89321e6e623e3f0e7a2b88f38de42cd510a59f31cfd16d67ad4 e autorizo somente o Checkpoint 1, nos termos desta solicitação e da tarefa preparada.”

Uma resposta direta “aprovado” à apresentação desta solicitação pelo arquiteto pode registrar esse objeto exato, conforme protocol/AGENT_WORKFLOW.md. A necessidade de decisão expressa vem da seção 19 da candidata, do parecer independente seção 9 e do protocolo; nenhuma aprovação foi inferida do parecer favorável.

READY FOR OWNER FREEZE DECISION: YES
OWNER FREEZE APPROVAL RECORDED: NO
CHECKPOINT1 TASK PREPARED: YES
CHECKPOINT1 IMPLEMENTATION AUTHORIZED: NO
READY FOR IMPLEMENTATION: NO
FINAL SPECIFICATION FROZEN: NO
AUTOMATED RELAY ACTIVE: NO
CODE REPOSITORY MODIFIED: NO
