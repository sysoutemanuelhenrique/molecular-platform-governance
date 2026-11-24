# Revisão focal de fechamento — Incremento 021, candidate-1

Tarefa: `021-CANDIDATE1-FOCAL-REVIEW`. Papel: Claude, revisor independente, separado do implementador. Data: 24/11/2026, America/Sao_Paulo.

Escopo: MINOR-N1, MINOR-N2, NOTE-N1 e NOTE-N2 do parecer `b3df694`, mais as regressões que as mudanças possam ter causado. Não reabri achados encerrados, porque não encontrei regressão concreta. Este parecer não congela a especificação nem autoriza implementação. O 020-A segue em STAND-BY.

**Veredito: APPROVE WITH NON-BLOCKING NOTES.**
- MINOR-N1 e MINOR-N2 estão fechados; as duas NOTES foram incorporadas.
- Não há regressão.
- Restam duas ambiguidades de redação, estreitas, no próprio §10.1 (NB-1, NB-2). Recomendo uma frase para cada antes do congelamento. Se o responsável preferir, podem ser fixadas pelo T021-173 no CP2. Não exigem nova rodada de revisão além da conferência do diff.

## 1. Gates e identidades

- **HEADs remotos antes do trabalho:**
  - coordenação: `ec38f578ced987969cd8f58c9c7ee4567e7fdd52` (despachado; pai `7ab5576…`);
  - código `main`: `08b797e0985e123ffd4d7ca7e5a5e8f040e63851`;
  - parecer anterior: `b3df694…`, blob `de3b8685…`.
- **Identidades:** conferem.

  | Item | Linhas | Bytes | SHA-256 |
  |---|---|---|---|
  | candidata | 373 | 63.606 | `041830ca…` |
  | SCHEMAS | 106 | 16.601 | `649b4334…` |
  | CATALOG | 2.045 | 50.480 | `8561039f…` |
  | SCENARIOS | 174 | 23.307 | `ca5c8830…` |
  | IDENTITY_BASIS_CASES | 173 | 6.937 | `14636992…` |
  | resposta do arquiteto | 65 | 7.010 | `c8389a47…` |

- **Manifesto:** os 12 itens conferem em `ec38f57`.
- **Catálogo:** byte-idêntico ao do draft-2 (`cmp` contra `7ab5576`).

## 2. Execução própria e limites

**Feito por mim nesta rodada:**
- diff draft-2 → candidata, do corpo e dos SCHEMAS, calculado por mim sem usar o patch fornecido;
- comparação linha a linha dos cenários;
- modelo em stdlib da regra da §10.1 (`evidence/claude-identity-basis-model.*`): recalcula os 7 hashes de projeção documental e classifica uma grade de 512 entradas (8 contextos de tabela × 8 códigos × 8 códigos).

O modelo é a minha leitura do texto, não código de produção. As projeções documentais não são hashes de RAW nem `plan_key`, como a própria candidata declara.

**Não houve:** pytest, Gemmi, parsing, hashes de produção, materialização, Windows, concorrência ou web.

## 3. Disposições

| Item | Disposição | Evidência concreta |
|---|---|---|
| MINOR-N1 | **Fechado** | A §10.1 define a base por endpoint, independente de K, na ordem ptnr1, ptnr2, antes da matriz: (1) ausente, null real ou malformado (incluindo `'?'`/`'.'` citados e `01_555`) → `not-applicable`; (2) sem tabelas, só `1_555` exato → convenção; (3) com tabela, sem fallback: lookup único e concordante → `source-operator`, inclusive quando não identidade; senão → `not-applicable`. Lookup e prova de identidade estão separados; as recusas de K>0 (§10) e a matriz de 15 células seguem inalteradas, e o diff não toca a matriz. O schema impõe a regra, a ordem sem sort e a rejeição dos dois pares mistos antes do hash. **Modelo próprio:** os 7 hashes de projeção reproduzem com JSON canônico (`sort_keys`, separadores compactos, UTF-8); na grade, a regra produz exatamente os 7 pares declarados e nunca os pares convenção/source. Os casos K=0 que o parecer anterior deixou abertos estão resolvidos: `3_555` localizado → `source-operator`; `1_555` sem tabelas → convenção. |
| MINOR-N2 | **Fechado** | Em T021-162 só o campo `checkpoint` mudou (CP1 → CP2); alvo, estímulo e expectativa são idênticos. Os 163 ids do draft-2 foram preservados e há 10 novos (T021-164–173). Totais 43/79/31/20 = 173, coerentes com §19, §20 e §23. |
| NOTE-N1 | **Incorporada** | O §23 exige no CP2 ao menos uma entrada real NMR multi-modelo, uma EM e uma com `_struct_ncs_oper`, com origem, checksum e lineage. O resultado esperado segue os bytes reais (recusa de generate ou omissão de given/identidade), e a cobertura atual é declarada documental. Nenhum sucesso é alegado. |
| NOTE-N2 | **Incorporada** | A recusa de K=2 não identidade é mantida como limite explícito; 1pfe continua negativo. |

**Preservação:** nenhuma regressão em P-1, P-2, P-3, NOTE-F1 nem nos 9 achados do draft-1. As mudanças se limitam a identificação, uma frase do §10, a nova §10.1, tabela e contagens das §19/§20 e texto de estado e gate das §21–23. Catálogo, NCS, CLI, publicação e compensação estão intactos.

## 4. Notas não bloqueantes

**NB-1 — "duplicação do id" no passo 3.** Com as duas tabelas presentes, o mesmo id aparece uma vez em cada uma. A leitura literal "duplicação do id" poderia classificar o operador padrão como `not-applicable`, o que contradiz a frase seguinte ("todas as referências presentes … concordantes → source-operator"). Isso mudaria o hash entre implementações. **Fixar:** "duplicação dentro da mesma tabela; um id em cada tabela com expressões concordantes é referência válida". O modelo adotou essa leitura.

**NB-2 — `symmetry_class` em K=0 com o operador 1 confirmado em só uma de duas tabelas presentes.** A base é `source-operator` nos dois lados, e a expressão encontrada é `x,y,z`. O §10.1 diz que, nesse caso, `1_555` não passa a prova de identidade de K>0, mas não diz se em K=0 a classe é `both-identity` (pela expressão encontrada) ou `unsupported-discarded` (prova insuficiente). Como `symmetry_class` entra em `connection_decisions_key`, isso precisa de uma regra.

Recomendo usar o mesmo critério de identidade do K>0 para classificar em K=0: confirmação em todas as tabelas presentes, senão `unsupported-discarded`. O caso é raro (exige as duas tabelas e uma incompleta) e cabe em T021-173.

## 5. Prontidão

A candidate-1 atende ao escopo desta tarefa. A decisão de congelamento é exclusiva do responsável. Recomendo incorporar NB-1 e NB-2 por redação antes de congelar, ou registrar que serão fixadas pelo T021-173 no CP2. Os gates de CP2 (Gemmi 0.7.5, fixtures reais com lineage, hashes de produção) e de CP3 (Windows 11/NTFS) seguem obrigatórios e não são pré-requisito desta revisão.

VERDICT: APPROVE WITH NON-BLOCKING NOTES
MINOR-N1: CLOSED; MINOR-N2: CLOSED; NOTE-N1/N2: INCORPORATED
NEW: 0 BLOCKER, 0 MAJOR, 0 MINOR, 2 NON-BLOCKING NOTES
READY FOR IMPLEMENTATION: NO
FINAL SPECIFICATION FROZEN: NO
INCREMENT 020-A: STAND-BY
CODE REPOSITORY MODIFIED: NO
ARCHITECT DOCUMENTS MODIFIED: NO
