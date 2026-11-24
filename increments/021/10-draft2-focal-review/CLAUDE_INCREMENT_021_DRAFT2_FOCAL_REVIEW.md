# Revisão focal — Incremento 021, draft-2

Tarefa: `021-DRAFT2-FOCAL-REVIEW`. Papel: Claude, revisor independente, separado do implementador. Data: 23/11/2026, America/Sao_Paulo.

Escopo: verificar as respostas aos 3 MAJORs e 6 MINORs do parecer `680aef4` e as regressões que elas possam ter causado. Não reabre P-1/P-2/P-3/NOTE-F1, já encerrados, porque não encontrei regressão concreta. Não aprova implementação nem congela contrato. O 020-A segue em STAND-BY.

**Veredito: APPROVE FOR FINAL CANDIDATE PREPARATION.**
- Os 3 MAJORs e os 6 MINORs estão fechados no nível do rascunho.
- Encontrei 2 MINORs novos de redação/determinismo, a absorver no candidato final, e 2 NOTES.
- Não há BLOCKER nem MAJOR novo.

## 1. Gates e identidades

- **HEADs remotos antes do trabalho:**
  - coordenação `7ab557697f78b0b8eb8c1e53997ef6e752f9470e`, igual ao despachado, com pai `b948f60…`;
  - código `main` `08b797e0985e123ffd4d7ca7e5a5e8f040e63851`;
  - parecer anterior `680aef4…`, blob `f609e1d7…`.
- **Draft-2 e anexos:**
  - draft-2: 356/57.694/`c1667d26…`;
  - SCHEMAS: 106/16.181/`51a91b8d…`;
  - CATALOG: 2.045/50.480/`8561039f…`;
  - SCENARIOS: 164/21.048/`04143367…`;
  - reconciliação: 84/11.543/`fc4e9423…`.

  Todos conferem.
- **Manifestos:**
  - manifesto atual (16 itens): conferem em `7ab5576`;
  - `SOURCE_AND_REVIEW_IDENTITIES.json`: 10 itens do governance conferem em `680aef4` e 5 blobs Gemmi em `5cc1c23`.

## 2. Execução própria e evidência fornecida

**Própria:**
- **Diff do corpo:** calculei o diff draft-1 → draft-2 sem usar o patch fornecido. As seções 3, 4, 5, 7, 8, 13, 15, 18 e 21 estão intactas.
- **Catálogo:** validação estrutural das 94 categorias.
- **Cobertura:** reexecução do meu script sobre o catálogo novo e meus inventários (`claude-catalog-coverage-draft2.output.json`), mais conferência à parte das tags das duas categorias com guarda.
- **Gramática numérica:** comparação da regex do draft-2 com `gemmi::cif::is_numb` do pin, em 39 tokens, via sonda C++ (`claude-gemmi-numb-probe.cpp`, `claude-numeric-grammar-compare.*`).
- **Cenários:** comparação linha a linha com o draft-1.

**Fornecida pelo arquiteto e não reexecutada:** consulta a páginas wwPDB; os próprios rechecks dele, que batem com os meus em conteúdo.

**Não houve:** pytest, Gemmi em Python, parsing de novas amostras, materialização, Windows, concorrência ou web. Não havia amostra real com NCS, NMR ou EM.

## 3. Disposição dos achados do parecer anterior

| Achado | Disposição | Base verificada |
|---|---|---|
| MAJOR-1 (identidade `1_555`) | **Fechado** | `1_555` exato vale como identidade sem tabelas, com `identity_basis=pdbx-1_555-convention`. Tabela presente exige operador 1 identidade, sem contradição; nunca há fallback. `1_556`, `2_555`, `01_555` e operadores de assembly continuam recusados (T021-141–143). A matriz de 15 células está inalterada. A recusa de K=2 com códigos distintos agora é justificada como limite de projeção. Não alega impossibilidade geométrica nem que o RAW deveria estar expandido, e a reconciliação admite que três amostras não medem prevalência. 1pfe permanece recusa explícita (T021-144). |
| MAJOR-2 (cobertura do catálogo) | **Fechado no rascunho** | 77 → 94 categorias (+17, nenhuma removida). As tags observadas em `_cell`, `_symmetry` e `_pdbx_unobs_or_zero_occ_atoms` foram incorporadas. Recheck próprio: zero categorias/tags desconhecidas ou obrigatórias ausentes nos três inventários. As famílias `_pdbx_validate_`, `_pdbx_nmr_` e `_em_` são omissões auditadas explícitas, sem alegação de suporte irrestrito. Categoria desconhecida continua recusada; aceito a ressalva do arquiteto de que omissão não prova inocuidade universal, como NCS e posição especial mostram. O §23 exige lineage de entrada real para os positivos D-01(b). |
| MAJOR-3 (NCS) | **Fechado** | `NCS_GUARD_THEN_OMIT` roda antes da máscara e de qualquer omissão. Não identidade com `code ≠ given`, inclusive nulo ou ausente, recusa `UNSUPPORTED_NCS`. Matriz parcial, NaN ou `code` desconhecido recusa `INVALID_CIF`, sem o skip do reader `Structure`. Identidade ou `given` omitem com auditoria e aviso. Isso é coerente com `read_ncs_info` (`src/mmcif.cpp:769–787`) e com `Transform::is_identity` exato (`include/gemmi/math.hpp:408–409`). Casos generate/null/given/identity/inválido estão em T021-150–154. |
| MINOR-1 (gramática numérica) | **Fechado** | O su vem depois do expoente. Em 39 tokens, a regex só diverge do Gemmi em `1.2()` e `+-1`, leniências do Gemmi que a regex corretamente recusa. `1.2e3(4)` aceito e `1.2(4)e3` recusado (T021-155). |
| MINOR-2 (endpoint sem altloc) | **Fechado** | O endpoint é um conjunto ordenado de variantes da mesma ocorrência e `label_atom_id`, com destino uniforme pela P-3. K conta conjuntos. A linha fonte é preservada literal, sem produto cartesiano. Ambiguidade entre ocorrências recusa (T021-156/157). O schema mudou para `tuple[tuple[NativeId],tuple[NativeId]]`. |
| MINOR-3 (`application_version`) | **Fechado** | Fora de `PlanBinding` e de `PolicyRecord`; mantido no `request_key` e no manifesto. Nenhum ciclo novo: `policy_id` nunca o incluiu. A obrigação de versionamento semântico está explícita (T021-035/159/160). |
| MINOR-4 (`omit_tags`) | **Fechado** | Todos os campos de tags são arrays nas 94 categorias. `action=omit` tem arrays vazios. `guard_then_omit` enumera as tags e `required_tags ⊆ omit_tags`. Sem sobreposição (T021-161). |
| MINOR-5 (posição especial) | **Fechado** | `SPECIAL_POSITION_GUARD_THEN_OMIT` resolve por contexto inequívoco, recusa ambiguidade, conta anotações e átomos únicos retidos em `SpecialPositionSummary`, avisa só quando há interseção retida e não altera ocupância. As tags reais do 1pfe estão dentro da lista da guarda (T021-158). |
| MINOR-6 (editorial e órfãos) | **Fechado** | A frase do §17 foi corrigida. O §14 tem um procedimento manual de 5 passos que não remove em caso de incerteza, sem `force-unlock` nem comando genérico (T021-163). |

Cenários: 163 no total (CP1 44 / CP2 68 / CP3 31 / CP4 20). Os 140 ids anteriores foram mantidos, só T021-035/060/079 foram editados e há 23 novos. Confere com o declarado.

## 4. Regressões verificadas

- **P-1/P-2:** envelopes X/O, acks e `policy_id` inalterados; §8 e §13 intactos.
- **P-3:** a uniformidade é a base dos conjuntos de endpoint e não foi relaxada.
- **NOTE-F1:** §5 intacto.
- **Hashes:** a remoção de `application_version` não cria ciclo. `identity_basis` entra em `connection_decisions_key` (ver MINOR-N1).

## 5. Novos achados

**MINOR-N1 — `IdentityBasis` subespecificado para códigos não identidade e para K=0.** O valor faz parte de `ConnectionDecision` e, portanto, de `connection_decisions_key` e do `plan_key`: ambiguidade aqui produz hashes divergentes entre implementações corretas.

O nome e o vocabulário (`pdbx-1_555-convention | source-operator | not-applicable`) descrevem a prova de *identidade*. Duas situações ficam abertas:
- Em K=0, um lado com `3_555` localizado na tabela: é `source-operator` ou `not-applicable`?
- Em K=0, `1_555` sem tabelas: o texto implica a convenção, mas não diz.

**Exigência:** uma regra determinística por lado. Por exemplo:
- `source-operator` quando o código foi resolvido em tabela fonte, identidade ou não;
- `pdbx-1_555-convention` só para `1_555` literal sem tabelas;
- `not-applicable` para nulo, malformado ou não localizado em K=0.

Acrescentar cenário de hash para cada combinação.

**MINOR-N2 — T021-162 no checkpoint errado.** A lineage de fixture real para positivos D-01(b) está em CP1 no CSV, mas o §23 situa a exigência em CP2/CP4 e CP1 não tem adapter nem fixtures CIF. Mover para CP2 (ou CP4) ou dividir em dois cenários. A soma por checkpoint muda de acordo.

**NOTE-N1 — NMR, EM e NCS não têm amostra real.** A cobertura dessas famílias e das guardas é só documental. O §23 já exige lineage e não promete suporte. No gate de implementação, exigir pelo menos uma entrada real NMR multi-modelo e uma com `_struct_ncs_oper`, além do teste do 5i55 como positivo de identidade sem tabela (T021-141).

**NOTE-N2 — consequências da recusa de K=2 com códigos distintos.** A recusa continua excluindo estruturas cujos contatos cristalinos declarados envolvam os átomos retidos (1pfe, por exemplo), mesmo sem corte. Está declarada como escolha de perfil, o que considero aceitável. Reavaliá-la só se o uso real mostrar perda relevante.

## 6. Prontidão

O draft-2 pode virar candidato final de especificação após absorver MINOR-N1 e MINOR-N2. Não está congelado e não autoriza implementação. Os gates reais de CP2 (Gemmi 0.7.5), CP3 (Windows 11/NTFS, concorrência) e de fixtures com lineage continuam obrigatórios.

VERDICT: APPROVE FOR FINAL CANDIDATE PREPARATION
PRIOR FINDINGS: 3/3 MAJOR CLOSED, 6/6 MINOR CLOSED (draft level)
NEW: 0 BLOCKER, 0 MAJOR, 2 MINOR, 2 NOTE
READY FOR IMPLEMENTATION: NO
FINAL SPECIFICATION FROZEN: NO
INCREMENT 020-A: STAND-BY
CODE REPOSITORY MODIFIED: NO
ARCHITECT DOCUMENTS MODIFIED: NO
