# Recebimento e disposição do parecer focal — estudo 021

Data: 23/11/2026. Autor: Codex arquiteto. Natureza: registro da leitura e do resultado independente; preparação do gate de rascunho. Não é especificação nem autorização de implementação.

## 1. Snapshot e identidade conferidos

- Governance de coordenação: `771d1aa2e6218188113aad4e54849c103219a25c`.
- Revisão focal: branch `claude/021-study-focal-review-20261123`, commit `8778b83844fe9bff9b61862743277d5ee3172ac5`, confirmado no remoto.
- Parent único da revisão: `771d1aa2e6218188113aad4e54849c103219a25c`.
- Código main: `08b797e0985e123ffd4d7ca7e5a5e8f040e63851`, preservado.
- Governance main: `a47183dfec8213c765ed43ae482c8c227760a3d5`, preservada.

O diff do revisor contém exatamente três adições sob increments/021/04-study-focal-review/: parecer e duas evidências. Nenhum documento anterior foi alterado ou removido. Não houve merge de sua branch para ler a entrega.

| Documento remoto | Linhas | Bytes | SHA-256 |
|---|---:|---:|---|
| CLAUDE_INCREMENT_021_STUDY_FOCAL_REVIEW.md | 121 | 11.638 | 231cbbf892a990f2ca4617719e7c468b2ac5d1ce3d97d47cbaae2b90a2f2d463 |
| evidence/claude-021-focal-review-verification.json | 74 | 4.762 | 19b8e6d0121cda0dd0294dae8fc841f051fe18b898a85de1fd30cf8197514568 |
| evidence/claude-namespace-probe-reproduction.output.json | 13 | 380 | 1cefea88a4db8c91e7c1e4f05b4e22d2ea84d07fc4f97316399df169bf2e43dc |

Os caminhos dessa tabela são relativos a increments/021/04-study-focal-review/ no commit do revisor. Parecer e evidências foram lidos integralmente. Linhas, bytes e hash do parecer coincidem com o recibo recebido. O hash da saída de namespace coincide com o informado no JSON do revisor e com a saída previamente registrada pelo arquiteto.

## 2. Resultado independente registrado

**Pronto para a fase de rascunho, com P-1 a P-5 obrigatórios.** Isso é prontidão técnica declarada pelo revisor, não aprovação do responsável para congelar ou implementar. A decisão de iniciar a redação do rascunho continua sendo o próximo gate do responsável, conforme a tarefa vigente.

| Disposição independente | Itens |
|---|---|
| Fechados — 11 | MAJOR-4; MINOR-1, MINOR-2, MINOR-4, MINOR-5; NOTE-1, NOTE-2, NOTE-3; C-1, C-2, C-3 |
| Parcialmente resolvidos — 4 | MAJOR-1, MAJOR-2, MAJOR-3, MINOR-3 |

As três correções factuais C-1/C-2/C-3 integram a contagem de 15 usada nesta rodada; não são somadas novamente à contagem original de severidades. NOTE-F1 é uma observação nova não bloqueante, registrada separadamente, não um décimo sexto achado original nem uma sexta pendência P.

Os quatro itens parciais não impedem iniciar um rascunho segundo o parecer, mas não podem ser apresentados como encerrados. Não se inventa uma nova contagem de BLOCKERS/MAJORS de implementação a partir dessa disposição de estudo.

## 3. Pendências incorporadas à preparação do rascunho

| Pendência | Origem | Obrigação de redação |
|---|---|---|
| P-1 | MAJOR-1 | Definir se a exclusão por complemento da lista de cadeias conta como decisão explícita para a exceção metalc/hydrog, incluindo ácidos nucleicos |
| P-2 | MAJOR-2/D-02 | Definir ato de reconhecimento das retenções fora de S, vinculado ao conjunto enumerado; aviso isolado não basta |
| P-3 | MAJOR-2 | Definir a unidade de exclusão não polimérica e a uniformidade por asym em micro-heterogeneidade, além de branched |
| P-4 | MAJOR-3 | Corrigir a justificativa geométrica e fechar as 15 células extremos × simetria e a identificação do operador identidade |
| P-5 | MINOR-3 | Catálogo por tag, chave, filtro/referências, tratamento de perdas e teste |

O checklist detalhado está em increments/021/05-draft-preparation/INCREMENT_021_DRAFT_REQUIREMENTS.md. Ele é uma preparação da tarefa, não um rascunho de contrato nem uma solução já aprovada das cinco pendências.

## 4. Correção arquitetural aceita para P-4

Aceito a correção do revisor. Com a mesma isometria conhecida T aplicada a dois pontos x e y, a relação geométrica e a distância são preservadas: em coordenadas cartesianas, T(x)=R x+t e ||T(x)-T(y)||=||R(x-y)||=||x-y||. Se os endpoints estão inequivocamente resolvidos em M, a igualdade do operador não torna seus átomos ausentes do referencial fonte.

Assim, a frase anterior que usou a falta de suporte geométrico como justificativa para recusar dois operadores iguais não identidade deve ser corrigida no rascunho. A recusa ainda pode ser uma restrição conservadora de cobertura/fixtures do perfil mínimo, anunciada como tal; não deve alegar impossibilidade geométrica. Este registro corrige a justificativa em documento novo e não modifica a reconciliação histórica.

Isso não resolve automaticamente operadores desconhecidos, nulos ou diferentes. Igualdade de strings não substitui a identificação válida do operador nem define o tratamento de todas as linhas. A matriz de P-4 deve ser efetivamente preenchida no rascunho, sem apoiar a decisão naquela justificativa incorreta.

## 5. NOTE-F1 e limites de evidência

Incorporar à tarefa de redação a equivalência com a decodificação UTF-8 estrita/leitura YAML existente e os diretórios reais dos registries. O hash continua sendo dos bytes efetivamente capturados, antes de qualquer normalização textual. Não alterar loaders do 020 para tornar a proposta viável.

A reprodução da sonda de namespace é execução própria declarada pelo revisor, cuja fonte de resultado foi conferida; não foi reexecutada pelo arquiteto neste recebimento. Não houve pytest, import/execução Gemmi, C++, Windows ou concorrência nesta atualização de coordenação. Tampouco se apresenta o registro como nova revisão científica independente.

## 6. Próximo gate e preservação

A tarefa focal fica marcada como entrega recebida/concluída, com fechamento parcial explicitamente enumerado. A tarefa de rascunho fica preparada e aguardando autorização do responsável para sua redação; não há acionamento automático de implementador ou revisor.

D-01(b) e D-02 com alcance amplo explícito e auditado continuam aprovadas no registro correspondente. O 020-A permanece em stand-by. Pareceres, estudos, reconciliação, registros de aprovação e manifestos históricos permanecem intactos. Ambas as mains permanecem preservadas.

FOCAL REVIEW RECEIVED AND IDENTITY VERIFIED: YES
INDEPENDENT ORIGINAL ITEMS CLOSED: 11
INDEPENDENT ORIGINAL ITEMS PARTIALLY RESOLVED: 4
P-1 THROUGH P-5 REQUIRED IN DRAFT: YES
READY FOR DRAFT SPECIFICATION: YES
DRAFT WRITING AUTHORIZED BY THIS RECEIPT: NO
READY FOR IMPLEMENTATION: NO
FINAL SPECIFICATION FROZEN: NO
CODE REPOSITORY MODIFIED: NO
