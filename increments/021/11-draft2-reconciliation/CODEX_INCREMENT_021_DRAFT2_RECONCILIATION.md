# Reconciliação focal do draft-2 — preparação da candidata final 021

Autor: Codex arquiteto. Data: 23/11/2026, America/Sao_Paulo. Tarefa: 021-CANDIDATE1-PREPARATION. Nenhuma implementação, alteração de contrato congelado ou aprovação de implementação.

## 1. Inputs e verificação

Coordenação: docs/020-a-candidate1-review-20261020 @ 7ab557697f78b0b8eb8c1e53997ef6e752f9470e. Parecer: claude/021-draft2-focal-review-20261123 @ b3df694b96cc0c425c12c73c9678c2b7dd090112. Código main read-only: 08b797e0985e123ffd4d7ca7e5a5e8f040e63851. Main do governance preservada: a47183dfec8213c765ed43ae482c8c227760a3d5. HEADs conferidos remotamente.

Parecer integral: increments/021/10-draft2-focal-review/CLAUDE_INCREMENT_021_DRAFT2_FOCAL_REVIEW.md, 98 linhas, 9.193 bytes, SHA-256 11261d70312b9b32bc05a67e8545d3cbcfb12687ece67b67103e8d52d3ced954. Identidade confirmada. Os cinco arquivos acompanhantes conferem com os blobs do commit do revisor. Os 16 itens do manifesto de entrada conferem em 7ab5576; os originais não foram editados.

A candidata é continuação da redação/reconciliação documental autorizada, conforme o fluxo vigente. O veredito do revisor não é autorização humana de freeze/implementação. Não registrei nova aprovação do responsável e não transformei candidate-1 em especificação congelada.

## 2. Disposição do parecer

| Item | Disposição do arquiteto | Resposta verificável |
|---|---|---|
| 3 MAJORs / 6 MINORs anteriores | Fechamento independente recebido no nível do rascunho | Parecer b3df694; sem reabrir decisões por preferência |
| MINOR-N1 | Aceito | §10.1 define precedência por endpoint, independente de K; schema exige a mesma regra e ordem ptnr1/ptnr2; nove pares e testes de determinismo |
| MINOR-N2 | Aceito | T021-162 passa de CP1 para CP2, mantendo id, estímulo e expectativa; tabela/CSV/totais sincronizados |
| NOTE-N1 | Incorporada como gate futuro | §23 exige entradas reais NMR multi-modelo, EM e NCS no CP2, com lineage e resultado correto de aceitação/recusa; nenhuma cobertura operacional alegada agora |
| NOTE-N2 | Registrada, sem mudança científica | Recusa de K=2 não identidade preservada como limite explícito; 1pfe não passa a positivo |

As duas correções novas aguardam fechamento independente. O arquiteto não declara MINOR-N1/N2 encerrados pela simples publicação da resposta.

## 3. Regra determinística de IdentityBasis

Classificar cada lado antes da matriz de K, sempre na ordem ptnr1,ptnr2. Fonte e tokens são os do mesmo RAW capturado; não há nova leitura ou inspeção.

- Código ausente/null real/malformado: not-applicable.
- Nenhuma tabela de operadores presente: só 1_555 exato recebe pdbx-1_555-convention; outros recebem not-applicable.
- Havendo tabela, lookup único, não nulo e concordante recebe source-operator, seja a operação identidade ou não. Duplicação/contradição/lookup insuficiente recebe not-applicable; não há fallback de convenção quando tabela existe.
- Lookup e comprovação geométrica são distintos: source-operator não afirma identidade. K>0 ainda exige as provas/recusas do §10; K=0 mantém a base calculada, sem substituir todas as bases por not-applicable.

Assim, 3_555 localizado em K=0 fica source-operator, e 1_555 sem tabelas em K=0 fica pdbx-1_555-convention. Nulos citados continuam diferentes de null real. A regra explica classificação de op 1 localizado mas não identidade, tabelas vazias e a precedência das validações globais do catálogo.

Dois dos nove pares cartesianos são impossíveis em um mesmo RAW: convenção/source e source/convenção, pois a convenção exige ausência das duas tabelas, e source exige presença de pelo menos uma. Explicitamente recusá-los evita inventar sete mais dois casos científicos válidos. Os outros sete têm exemplos alcançáveis em K=0. Schema, tabela de casos e T021-164–172 registram isso. T021-173 verifica os casos de precedência/lookup.

O anexo IDENTITY_BASIS_CASES.json inclui projeções documentais canônicas e sete SHA-256 dessas projeções. Isso não é teste do modelo, hash de RAW, connection_decisions_key ou plan_key de produção. O gate CP2 exige comparar hashes completos calculados pelo código real sobre fixtures fixas com checksums verdadeiros, cobrindo repetições, ordem de visita e a rejeição dos dois pares impossíveis.

## 4. Checkpoints e contagens

Nenhum dos 163 IDs do draft-2 foi excluído. Só T021-162 muda de checkpoint (CP1→CP2), sem mudar alvo/estímulo/expectativa. Acrescentados dez cenários de CP2 para o MINOR-N1: T021-164–173. Total 173, CP1=43 / CP2=79 / CP3=31 / CP4=20. Isso é contagem de cenários, não funções pytest nem itens coletados.

A prova de lineage da fixture fica em CP2, onde existem adapter/fixtures, com uso cumulativo em CP4. A regra de fonte real é mantida, sem deslocar execução científica para o CP1. O catálogo tem as mesmas 94 categorias e os mesmos bytes do draft-2; não houve ampliação de ciência, omissões ou política de simetria.

## 5. Preservação e evidência

As seções 2/3/4/5/6/7/8/9/11/12/13/14/15/16/17/18 são byte-idênticas ao draft-2. Mudanças concentram-se em identificação/estado da candidata, §10.1, schema IdentityBasis, tabela e contagem de cenários, §23 e próximo gate. No §21 só se atualiza o estado do fechamento independente já recebido; no §1/22 corrigem-se referências históricas relativas e a separação da evidência por rodada. Em particular P-1/P-2/P-3/NOTE-F1, NCS, catálogos, CLI, publication, compensação e interrupções não foram reformulados.

Verificado nesta rodada: refs remotos; identidade do parecer/evidências; manifesto de entrada; JSON/CSV; nove pares e sete hashes documentais; preservação das seções/catalogue; diff/whitespace. Não executei pytest, Gemmi Python/C++, novo parsing RAW, materialização, Windows, concorrência ou instalação. Os 39 tokens comparados ao Gemmi e seus dois casos de leniência são evidência do revisor, não reexecução minha.

## 6. Próximo gate

Candidata nova: increments/021/12-final-candidate/INCREMENT_021_FINAL_SPECIFICATION_CANDIDATE.md, acompanhada de schemas/catalogue/scenarios/casos e manifesto. Os documentos anteriores, parecer e 020-A em stand-by são preservados.

Tarefa 021-CANDIDATE1-FOCAL-REVIEW: fechar apenas MINOR-N1/N2 e incorporação das NOTES; conferir a preservação do que já foi fechado e apontar somente regressão concreta. Sem revisão integral repetida por preferência. Não há agente acionado automaticamente.

Depois de fechamento independente favorável, o responsável decide aprovação/congelamento da versão exata. Esta publicação não o faz; não prepara tarefa de implementação autorizada nem checkpoint de código.

CANDIDATE1 PREPARED: YES
READY FOR INDEPENDENT CANDIDATE FOCAL REVIEW: YES
READY FOR OWNER FREEZE DECISION: NO
READY FOR IMPLEMENTATION: NO
FINAL SPECIFICATION FROZEN: NO
CODE REPOSITORY MODIFIED: NO
