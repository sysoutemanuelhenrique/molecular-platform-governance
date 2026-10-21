# Reconciliação e correção focal — Checkpoint 1 do Incremento 020-A

Codex, arquiteto; 20/10/2026 (data local do responsável). Este documento responde ao parecer independente; não o substitui nem declara seus achados fechados.

## Entradas verificadas e autorização

- Código a corrigir: sysoutemanuelhenrique/molecular-platform, branch feature/increment-020-a-molecular-characterization, HEAD f8416b845efe93f9e47deca97f01a355e4e679ba; parent único/main 08b797e0985e123ffd4d7ca7e5a5e8f040e63851, reconfirmados no remoto.
- Contrato final: increments/020-A/08-final-specification/INCREMENT_020_A_FINAL_SPECIFICATION.md no governance, commit 665fb8b9cb4e1c7e0d0b9f1db98ec2adaa63bfed; SHA-256 cfbc6ea4bbb58f987deb3f73e45fc39d5b79d0cfaa2de8e0a7870a9937386e9c; 586 linhas; 71.904 bytes. Sem alteração.
- Parecer original recebido e lido integralmente: increments/020-A/10-checkpoint-1-review/CLAUDE_CHECKPOINT1_ADVERSARIAL_REVIEW.md; SHA-256 72d658ad6184a2411d9cb56dbbb3b49861ccd64621126cdb5d62aa7b048f4399; 153 linhas; 24.918 bytes.
- Evidência original: increments/020-A/10-checkpoint-1-review/evidence/claude-dto-coercion-reproduction.json; SHA-256 8d24af595759154d6c798c11a2afcc44a5c5469faf80abe4bff14f6434540cea; 54 linhas; 2.183 bytes.
- Originais publicados pelo arquiteto, preservados byte a byte e relidos no remoto: commit 5583734475103991fb12ed8b26689cf4ad8a0eba. A falha de push do revisor está registrada na proveniência; seu commit local f6587d43569393bcab01e5e74924c5cd3645371a não é apresentado como publicado.

O parecer registra 0 BLOCKERS / 2 MAJORS / 2 MINORS / 5 NOTES, REQUEST CHANGES. Aceito os quatro achados para correção nesta rodada. A autorização original de Emanuel para implementar/testar/commit/push do CP1, registrada em 85ce45ce5cc635d75035664dd612ca6c0a839dac, abrange essas correções nos mesmos quatro arquivos. Não se cria autorização de CP2/3 nem de alteração científica. A tarefa focal é tasks/020-A-CHECKPOINT1-CORRECTIONS.json.

## Disposição por achado

| Item | Disposição | Critério de fechamento |
|---|---|---|
| MAJOR-1 — tipos não estritos | ACEITO, corrigir | DTOs/perfis recusam tipos coercíveis não permitidos pelo contrato, inclusive constantes booleanas/inteiras; positivos e JSON público preservados |
| MAJOR-2 — interrupções por fase | ACEITO, corrigir | Testes reais/separados de KeyboardInterrupt e SystemExit por fase aplicável ao adaptador; identidade/código preservados, logs/recursos restaurados, nenhum resultado parcial |
| MINOR-1 — restauração dos logs | ACEITO, corrigir nesta rodada | LogWarningMsg posterior com marcador capturado em stderr real após sucesso, falha e as duas interrupções; não usar segundo cálculo como prova nem reativar logs artificialmente depois |
| MINOR-2 — SGroup/estéreo por bytes | ACEITO, corrigir nesta rodada | SDF V3000 real de um registro com SGroup, outro AND e outro OR atravessam bytes→parser real→elegibilidade e são recusados por unsupported-structure, não por entrada inválida |
| NOTE-1 — SVG Z | ACEITA, sem mudança | Manter gramática M/L/Q, recusa explícita e all-or-nothing; manter teste/limitação. Nenhum suporte a Z autorizado |
| NOTE-2 — localização do helper SVG | ACEITA | Manter helper neutro/importável sem RDKit; não deslocá-lo por preferência organizacional |
| NOTE-3 — +680 versus +679 | ACEITA | Novo relatório registra errata do relatório anterior: diff original +679/−1 no adaptador, total +3094/−1. Não editar o relatório original; separar diff corretivo e cumulativo |
| NOTE-4 — limites de execução | ACEITA | Resultados Windows/pytest fornecidos continuam fornecidos; declarar ambiente e execução próprios das correções. Não converter sondas em pytest ou prova Windows |
| NOTE-5 — confirmações positivas | ACEITA | Preservar JSON, métodos científicos, perfis, limites, taxonomia, independência do desenho e comportamento legado |

O MAJOR-2 é falta de evidência contratada, não um defeito de propagação já observado. O mesmo cuidado vale para a restauração dos logs: context manager e ausência de except BaseException são indicativos estruturais, não substituem a prova dinâmica exigida.

## Ressalva técnica importante para MAJOR-1

O achado é correto; a receita sugerida no parecer não deve ser aplicada sem validar seu efeito real. Sonda isolada do arquiteto, Python 3.12.14/Pydantic 2.14.0, fora do projeto:

- ConfigDict(strict=True) ainda aceitou Literal[True] com valor int 1, Literal[0] com bool False e Literal[600] com float 600.0.
- Field(strict=True) aplicado diretamente a Literal[True] produziu RuntimeError na construção da classe: unable to apply constraint strict to schema literal.

Portanto, usar os mecanismos suportados pelo Pydantic instalado que efetivamente imponham os tipos, incluindo validação anterior à igualdade/coerção dos Literals quando necessária. Não prescrever uma refatoração ampla, classe-base universal ou dependência nova; o efeito obrigatório é a recusa demonstrada em testes. Não alterar os modelos legados de outros incrementos.

Cobrir CharacterizationValues e os demais DTOs/perfis novos pertinentes, não apenas os dois exemplos da sonda: contagens/carga/tamanhos inteiros sem strings, floats integrais ou bool; floats sem strings/bool/não-finitos; booleanos literais sem 0/1; constantes inteiras sem bool/float equivalente; IDs/hashs estritos. Preservar valores nativos válidos, regras científicas existentes e o JSON contratado. Não inventar proibição geral de int em campo float além da semântica efetivamente contratada. Confirmar serialização e round-trip JSON válido sem alterar a forma pública.

Evidência: evidence/architect-strict-literal-api-probe.json. Isso é pesquisa de API, não código de produção ou teste do projeto. A reprodução do revisor usou Pydantic 2.13.5 e a do arquiteto 2.14.0; 2.14.1 é o ambiente informado pelo implementador. Não contar a mera declaração desse ambiente como terceira reprodução independente da coerção. Essa precisão não altera o achado.

## Testes de interrupção e logs

Usar o fluxo público de produção e injetar a interrupção no ponto de uso de uma operação real, sem substituir todo o adaptador por mock. Mapear fases do CP1: resolução/entrada quando aplicável; parsing SDF (incluindo iteração) e SMILES; cálculo dos valores; fonte/desenho, coordenadas e preparação; renderização; validação/vínculo SVG e construção do resultado quando aplicável. Justificar a matriz concreta, sem cobrar leitores ou CLI futuros e sem omitir fases do adaptador silenciosamente.

KeyboardInterrupt e SystemExit precisam ser casos separados/parametrizados reais; conferir a mesma instância e, para SystemExit, o código original. Conferir ausência de ficha parcial e de passos posteriores à interrupção. Onde o escopo envolve BlockLogs, a injeção deve atravessar o gerenciador real; depois, emitir rdBase.LogWarningMsg com marcador único e comprovar sua presença via capfd/subprocesso. Preservar o estado anterior: não mascarar falha chamando EnableLog depois da operação.

Manter os testes legados. A nova prova do fluxo de caracterização não pode depender apenas dos testes de enumeração/promoção.

## Caminho viável para MINOR-2 sem SDF manuscrito

O arquiteto confirmou com RDKit real 2026.03.6/Python 3.12.14/Linux uma rota curta usando o writer público do próprio RDKit:

- SGroup: MolFromSmiles("CCO"), CreateMolSubstanceGroup(mol, "SUP"), associar um átomo e LABEL; serializar por MolToMolBlock(forceV3000=True) e acrescentar a linha $$$$.
- AND/OR: RWMol(MolFromSmiles("C[C@H](F)Cl")), CreateStereoGroup com STEREO_AND ou STEREO_OR e átomo quiral 1, SetStereoGroups; serializar da mesma forma.
- ForwardSDMolSupplier(BytesIO(data), sanitize=True, removeHs=False, strictParsing=True) leu um registro válido e reteve o grupo em cada caso. O adaptador público exato do HEAD f8416b8 recusou os três por unsupported-structure, atravessando o caminho completo de bytes.

O estudo mostra viabilidade sem mudar a produção. Não substitui os testes de integração exigidos: o implementador deverá reproduzir e acrescentar asserts ao código de testes autorizado, sem monkeypatch do parser/elegibilidade para fabricar essa recusa. Verificar que o parser recupera o grupo esperado, para não confundir ausência de grupo ou erro de sintaxe com a política científica. Manter controles de estrutura válida/estéreo absoluto conforme o contrato.

Sondas e três fixtures sintéticas estão em evidence/. A provenance é construção sintética por APIs RDKit, não PubChem nem MolecularState persistido. Podem orientar fixtures em memória nos testes; não criar arquivos de dados no repositório de código fora da allowlist. Não exigir hashes idênticos de Molfile gerado em outro ambiente como novo contrato. A pesquisa não é execução de pytest nem prova Windows.

## Execução autorizada e saída

Partir do HEAD remoto f8416b845efe93f9e47deca97f01a355e4e679ba, na mesma branch; main deve continuar 08b797e0985e123ffd4d7ca7e5a5e8f040e63851. Novo commit corretivo descendente do HEAD revisado, sem amend/rebase/reset/force. Se algum gate divergir, parar para reconciliação.

Allowlist permanece exatamente: src/molecular/characterization.py; src/molecular/rdkit_tautomer.py; tests/test_characterization.py; tests/test_rdkit_tautomer.py. Não alterar motor, gramáticas, perfis, API/JSON, dependências, serviço, atomic.py, CLI, registries ou schemas. Se um ajuste de produção for necessário para satisfazer o contrato e os testes focalizados, limitar-se aos módulos novos/adicionados do CP1; não refatorar comportamento legado.

Rodar testes focais e suíte completa se o ambiente permitir. Informar comandos, versões, coleta/pass/fail/skip reais e razões; reconciliar contagem antes/depois sem fixar número esperado de itens novos. Registrar resultados com/sem opcionais que forem executados incluindo failed, distinguindo problemas preexistentes da baseline. Não corrigir testes CLI fora da allowlist para limpar falha anterior sem RDKit.

Relatório novo: increments/020-A/11-checkpoint-1-corrections/CLAUDE_CHECKPOINT1_CORRECTIONS_REPORT.md, em branch própria do implementador no governance. Evidências próprias podem ficar sob evidence/claude-*. Não editar parecer original, relatório anterior, reconciliação, tarefas ou STATUS.md. Incluir achado→mudança→teste/item→resultado, SHA inicial/final, diff corretivo/cumulativo, allowlist, diff-check, working tree, commits/refs e identidade do relatório. Commit/push do código nesta branch e do relatório próprio estão cobertos pela autorização original de CP1.

Depois da entrega: reverificação independente focal dos quatro achados e das regressões concretas. Não repetir a revisão documental nem liberar CP2/3 automaticamente. Nenhum PR/merge/configuração/main autorizado. Preservar increment-009-review.txt e _figura_curcumina/.

FULL REVIEW RECEIVED AND VERIFIED: YES
REVIEW ORIGINALS MODIFIED: NO
REVIEW VERDICT: REQUEST CHANGES
ACCEPTED CORRECTION ITEMS: 2 MAJORS / 2 MINORS
CORRECTIONS AUTHORIZED: YES — existing Checkpoint 1 scope only
FROZEN SPECIFICATION MODIFIED: NO
CHECKPOINT 1 APPROVED: NO
CHECKPOINT 2 AUTHORIZED: NO
CHECKPOINT 3 AUTHORIZED: NO
CODE REPOSITORY MODIFIED BY ARCHITECT: NO
