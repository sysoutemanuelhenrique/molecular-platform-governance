# FINAL SPECIFICATION — INCREMENTO 020
## Receptor Preparation Foundation

**Natureza: Final Specification, especificação final e congelada do Incremento 020, produzida promovendo a Final Specification Candidate (`11-final-specification-candidate`) mediante a aplicação exclusiva das três correções mecânicas e localizadas listadas na Allowlist de Correções (Seção 19) da Final Short Review (`12-final-review`): (MINOR-01) correção da referência cruzada obsoleta na Seção 40 (Questões Abertas), de `READY FOR SHORT REVISED DRAFT REVIEW: YES` para `READY FOR FINAL SHORT REVIEW: YES`; (MINOR-02) correção da contagem do fluxo seguro de leitura (Seção 11.3), de "nove passos" para "dez passos (Passo 0–9)", nas duas passagens herdadas que ainda citavam a contagem antiga (Seções 4 e 41); (MINOR-03) correção da aritmética do parágrafo de cobertura de tetos (Seção 32.2), de "cinco limites"/"quatro tetos restantes" para "seis limites"/"cinco tetos restantes", refletindo corretamente as seis linhas já existentes na tabela de limites daquela seção. A candidata, por sua vez, já havia promovido o Corrected Revised Draft Specification (`09-corrected-revised-draft`) mediante a aplicação exclusiva das sete correções mecânicas e localizadas listadas na Allowlist de Correções (Seção 19) da Corrected Revised Draft Confirmation (`10-correction-confirmation`): (m-02) justificativa textual explícita, na Seção 32.2, para a ausência de cenário dedicado nos tetos de contagem restantes, preservando a matriz em 137 cenários; (m-04) passo explícito ("Passo 0") na Seção 11.3 nomeando a rejeição por extensão (Seção 11.2) como a primeira verificação do fluxo seguro de leitura; (m-05) regra de comparação `casefold()`/`.lower()` entre a extensão declarada e a lista fechada de extensões rejeitadas, na Seção 11.2; (m-06) substituição de "um parceiro classificado `metal-ion`" por "pelo menos um parceiro classificado `metal-ion`" nas Seções 12.3 e 18.3, eliminando a ambiguidade do caso de ponte metal-metal; (n-01) adição do validador `_validate_origin_consistency` a `NonPolymerComponent` (Seção 17.4); (n-02) correção da etiqueta de T-061 de `[PRESERVADO]` para `[REESCRITO — mecanismo]` (Seção 35.4), sem alteração do texto do cenário; (n-03) padronização da terminologia "pelo menos um" em toda ocorrência análoga às Seções 12.3/15.6/18.3, aplicada em conjunto com m-06. Nenhuma decisão científica ou arquitetural é reaberta, nem pela candidata, nem por este congelamento; nenhum contrato técnico, modelo, identidade, parser ou escopo além do estritamente autorizado por essas dez correções mecânicas (sete da candidata, três deste congelamento) é alterado; a matriz normativa permanece em 137 cenários (T-001–T-137), sem renumeração, remoção ou consolidação, distribuídos em quatro checkpoints (70+46+21+0=137); a allowlist de arquivos permanece preservada sem alteração. Preserva integralmente, sem alteração, os quatro achados MAJOR (F-01–F-04), os seis achados MINOR originais (F-05–F-10), as dez NOTES (N-01–N-10) e os sete achados residuais (m-02, m-04, m-05, m-06, n-01, n-02, n-03) já resolvidos/reconciliados pela cadeia de governança anterior e reconfirmados pela Final Short Review. É a especificação final e congelada deste incremento: o contrato técnico está fechado, a implementação é autorizada a partir deste documento, e nenhuma implementação foi, até o momento, realizada.**

---

## 1. Identidade e Baseline

- **Incremento:** 020 — "Receptor Preparation Foundation."
- **Papel do documento:** décimo-terceiro artefato de governança da linhagem do Incremento 020 (estágio `13-final-specification`), produzido promovendo a Final Specification Candidate (`11-final-specification-candidate`) mediante a aplicação exclusiva das três correções autorizadas pela Seção 19 da Final Short Review (`12-final-review`). Correção mecânica, final, pontual — especificação final, congelada, contrato técnico fechado, implementação autorizada.
- **Repositório:** `C:\Users\Pichau\molecular-platform` (remote `sysoutemanuelhenrique/molecular-platform`).
- **Branch confirmada:** `main`.
- **HEAD local confirmado:** `23a3a8e35fe16fceb22cb28ea2a777ab196c4f54` — via `git rev-parse HEAD`.
- **`origin/main` confirmado:** `23a3a8e35fe16fceb22cb28ea2a777ab196c4f54` — via `git rev-parse origin/main`. Idêntico ao HEAD local.
- **`git status --short`:** apenas `?? _figura_curcumina/` e `?? increment-009-review.txt` — ambos untracked pertencentes ao usuário, não lidos, não alterados, não movidos, não adicionados ao Git, não tratados como parte do Incremento 020.
- **`git diff --check`:** limpo (sem saída, exit 0), confirmado antes da escrita.
- **Baseline de testes herdada (não reexecutada):** 1.315 aprovados, 5 ignorados, 0 falhas. `pytest` **não** foi executado para produzir este documento.
- **Nenhum arquivo do repositório foi criado, modificado ou removido para produzir este documento.** Trabalho estritamente read-only sobre o código; nenhuma dependência instalada (Gemmi permanece não instalado); nenhum spike executado.

---

## 2. Natureza e Status

Esta é a **Final Specification** do Incremento 020 — especificação final, congelada, que autoriza implementação. Ela:

- promove a Final Specification Candidate (`11-final-specification-candidate`), que já herdava integralmente os quatro achados MAJOR corrigidos (F-01–F-04), os seis achados MINOR corrigidos (F-05–F-10) e as dez NOTES reconciliadas (N-01–N-10) da Adversarial Review original (`06-draft-review`), os três achados (M-01, F-06, F-09) corrigidos sobre o Revised Draft Specification (`07-revised-draft-specification`), e que já aplicava as sete correções mecânicas e localizadas (m-02, m-04, m-05, m-06, n-01, n-02, n-03) autorizadas pela Seção 19 da Corrected Revised Draft Confirmation (`10-correction-confirmation`);
- aplica **exclusivamente** as três correções mecânicas e localizadas que a Final Short Review (`12-final-review`, Seção 19) autorizou sobre os três achados MINOR que aquela revisão identificou como efeitos colaterais puramente textuais, nunca técnicos, introduzidos pela própria promoção à candidata: MINOR-01 (referência cruzada obsoleta, Seção 40), MINOR-02 (contagem do fluxo seguro de leitura, Seções 4 e 41), MINOR-03 (aritmética dos tetos de contagem, Seção 32.2) (Seção 45.5 desta especificação detalha cada correção e sua seção normativa final) — por correção mecânica e localizada, nunca por reabertura de arquitetura, modelo ou mecanismo;
- herda integralmente a arquitetura central do Draft original (`05-draft-specification`) e de toda a cadeia de governança anterior (Revised Discovery, Short Adversarial Review, Revised Draft Specification, Short Adversarial Review do Revised Draft, Corrected Revised Draft Specification, Corrected Revised Draft Confirmation, Final Specification Candidate, Final Short Review): o Incremento 020 permanece uma fundação read-only de inspeção e seleção lógica de receptor, sem materialização estrutural e sem `PreparedReceptorArtifact`;
- preserva F-01–F-04, F-05–F-10, N-01–N-10 e as sete correções m-02/m-04/m-05/m-06/n-01/n-02/n-03 integralmente, sem reabertura — nenhuma das três correções deste congelamento toca qualquer um desses achados já resolvidos/reconciliados;
- preserva T-001–T-137 sem renumeração, remoção ou consolidação — nenhum cenário novo foi acrescentado por este congelamento; a única mudança dentro da matriz normativa em toda a linhagem permanece a correção da etiqueta de T-061 (n-02, Seção 35.4), já aplicada pela candidata, sem alteração do texto do cenário;
- **congela o contrato** — nenhuma revisão adicional é esperada antes da implementação; nenhuma decisão científica ou arquitetural permanece aberta;
- **autoriza implementação** — o Checkpoint 1 (Seção 38) pode começar a partir deste documento; nenhum código, teste ou dependência foi, até o momento, criado, alterado ou instalado por este documento ou pelo trabalho que o produziu.

---

## 3. Documentos Normativos

| Documento | Linhas | Bytes UTF-8 | SHA-256 | Resultado |
|---|---|---|---|---|
| Final Specification Candidate (`11-final-specification-candidate`) | 1.943 | 203.710 | `c25690681ac1a3a194c8645d0c44479b321b1c3881b2238e0c4c784f18a8dd23` | **Confirmado, idêntico ao esperado** |
| Final Short Review (`12-final-review`) | 214 | 22.762 | `7f0096f5340fec04c375cc819871346b5a2d38e25fc0665d01c4b8490175dcbd` | **Confirmado, idêntico ao esperado** |
| Corrected Revised Draft Specification (`09-corrected-revised-draft`) | 1.884 | 189.242 | `4db4836fbf9c1315dc742e99aa96844642068a6aac3b0d8863ee4164b7d74862` | **Confirmado, idêntico ao esperado** |
| Corrected Revised Draft Confirmation (`10-correction-confirmation`) | 326 | 32.063 | `11875eecbe11ce683586d779dffe2cf3c3a96eb0a1ec12f7052745ad0123532c` | **Confirmado, idêntico ao esperado** |
| Short Adversarial Review do Revised Draft (`08-revised-draft-review`) | 364 | 41.001 | `5a93bebfd3100927e558c3b70fef46b925601cb56aab342fe2a79fe686f1d1b3` | **Confirmado, idêntico ao esperado** |
| Revised Draft Specification (`07-revised-draft-specification`) | 1.833 | 175.425 | `e9902984eea55c742ba2710d62e6675b2b51ea52a95760049ddf9244c79cc883` | **Confirmado, idêntico ao esperado** |
| Draft Specification (`05-draft-specification`) | 1.439 | 122.557 | `766d7b12cfae901dbc2c9a4522c31afc2824410d79fbcc6f7d3f8541d93278f4` | **Confirmado, idêntico ao esperado** |
| Adversarial Review do Draft (`06-draft-review`) | 632 | 80.404 | `007751931ead9ebb4dea1b8c7a9a97ac34033604ebae8de4a7059c3886010c63` | **Confirmado, idêntico ao esperado** |
| Revised Discovery (`03-revised-discovery`) | 767 | 68.886 | `b5589f6488984a1f9e79ee1cba98d768fae23353f2f8909e1b06231b594cfc78` | **Confirmado, idêntico ao esperado** |
| Short Adversarial Review (`04-revised-discovery-review`) | 324 | 27.936 | `5d8b084bebf7608f036c1de875c778b8e8314e9049849ebecd88bc82ac707fdb` | **Confirmado, idêntico ao esperado** |

Todas as dez identidades foram confirmadas por leitura direta (`wc -l`, `wc -c`, `sha256sum`) antes da leitura de conteúdo e antes da escrita deste documento. A Final Specification Candidate e a Final Short Review foram lidas integralmente, do início ao bloco terminal, antes de qualquer correção — com atenção especial à Seção 19 da Final Short Review, autoridade exclusiva das três correções aplicadas neste congelamento. Nenhum dos dez documentos foi modificado por este trabalho — reconfirmado byte a byte na Seção 45.

A Final Specification Candidate e a Final Short Review são o par de entrada direto desta especificação final — a primeira é o documento promovido, a segunda é o parecer que determina exaustivamente, em sua Seção 19, quais correções são autorizadas neste congelamento. As identidades do Corrected Revised Draft Specification (`09-corrected-revised-draft`), da Corrected Revised Draft Confirmation (`10-correction-confirmation`), da Short Adversarial Review do Revised Draft (`08-revised-draft-review`) e do Revised Draft Specification (`07-revised-draft-specification`) foram reconfirmadas byte a byte, por rastreabilidade — seu conteúdo não foi relido para produzir este congelamento, por não ser necessário a uma correção puramente mecânica e localizada sobre a candidata. A Adversarial Review do Draft (`06-draft-review`), o Draft original (`05-draft-specification`), o Revised Discovery e a Short Adversarial Review daquele estágio são herdados sem releitura, pelo mesmo motivo. Nenhuma questão já resolvida por aquela cadeia é reaberta aqui.

---

## 4. Resumo Executivo

Esta especificação corrige os quatro achados MAJOR da Adversarial Review por redesenho direto de modelo e mecanismo, não por ajuste cosmético — correção herdada integralmente do Corrected Revised Draft Specification, não reaberta por esta promoção:

- **F-01 (identidade de entidade/cadeia em PDB legado):** `label_asym_id`/`label_entity_id` tornam-se `Optional[str]`, cada um acompanhado de um campo `*_origin: IdentityOrigin` (`"source"` | `"parser-derived"` | `"unavailable"`) que nunca permite que uma identidade derivada pelo parser substitua silenciosamente uma identidade declarada pela fonte. Um novo campo `selection_capability` (`"full"` | `"inspection-only"`) classifica cada inspeção; `ReceptorSelectionPolicy`/`ResolvedReceptorSelection` exigem `selection_capability="full"` e falham com um erro tipado quando isso não se verifica. `Gemmi.setup_entities()` e qualquer outra inferência geométrica de entidades são explicitamente proibidos como fonte de identidade factual.
- **F-02 (entrada comprimida):** o 020 **rejeita toda entrada comprimida**, por extensão (`.gz`, `.bz2`, `.xz`, `.zip`, entre outras) e por magic bytes do conteúdo real, independentemente da extensão declarada — nenhuma descompressão jamais ocorre, nenhum caminho comprimido é entregue ao Gemmi. Um fluxo seguro de dez passos (Passo 0–9) substitui a verificação de tamanho ingênua anterior.
- **F-03 (`StructConnEndpoint` incompleto):** o endpoint de conexão agora preserva treze campos (incluindo `label_alt_id` e `symmetry`, os dois itens que a revisão encontrou faltando), e um novo modelo unificado `StructureConnection` substitui os três modelos anteriores (`DisulfideBond`/`CovalentConnection`/`MetalCoordination`), preservando distância, ordem de valor, papel, detalhes e flag de átomo que sai, sem jamais inventar um valor para um campo que o formato não declara.
- **F-04 (duplicação do snapshot de inspeção):** `ReceptorInspectionReport` passa a ser **persistido create-once**, identificado por um `inspection_id` determinístico (SHA-256 sobre um payload canônico). `ReceptorSelectionPolicy` referencia esse `inspection_id` explicitamente; `ResolvedReceptorSelection` referencia o mesmo id em vez de embutir uma cópia completa do relatório — eliminando a duplicação que a revisão identificou, e eliminando por construção a necessidade de `ReceptorResolutionParserVersionConflictError` (Seção 24).

Os seis achados MINOR (F-05–F-10) são corrigidos individualmente (Seção 42) e as dez NOTES (N-01–N-10) são reconciliadas individualmente (Seção 43). A Opção B, a camada química, a ausência de materialização estrutural e a ausência de preparação química permanecem integralmente preservadas — nenhuma correção desta revisão abre um caminho para química real ou para um novo arquivo de coordenadas (Seção 7).

A matriz normativa cresce de 94 para **137 cenários** (T-001–T-137): os 94 originais são preservados sem renumeração (alguns reescritos para refletir o modelo corrigido, declarado explicitamente onde ocorre); 43 cenários novos (T-095–T-137) cobrem exclusivamente as áreas que as correções introduziram. A allowlist permanece com os mesmos sete módulos novos mais as duas extensões aditivas já existentes — nenhum arquivo novo foi necessário. Os quatro checkpoints são redistribuídos e suas contagens reconciliadas mecanicamente (Seção 38), fechando definitivamente o erro aritmético do achado F-05.

---

## 5. Reconciliação da Revisão — Visão Geral

| Categoria | Quantidade | Status |
|---|---|---|
| MAJOR (F-01–F-04) | 4 | **4/4 RESOLVED** (Seção 41) |
| MINOR (F-05–F-10) | 6 | **6/6 RESOLVED** (Seção 42) |
| NOTE (N-01–N-10) | 10 | **10/10 RECONCILED** (Seção 43) |

Nenhum achado foi omitido, suavizado sem justificativa, ou reclassificado para evitar correção. Cada um é tratado em detalhe nas seções temáticas correspondentes (referenciadas nas tabelas de reconciliação) e novamente, de forma consolidada, nas Seções 41–43.

---

## 6. Escopo

Decisão normativa desta especificação, preservando integralmente a Seção 6 do Draft original:

1. **Inspeção determinística e read-only do `ProteinInput` RAW** — leitura via o parser escolhido (Seção 10), produzindo um `ReceptorInspectionReport` factual.
2. **Relatório de inspeção persistido create-once** (Seção 14) — correção de F-04; substitui a decisão anterior de snapshot embutido sem persistência própria.
3. **Inventário estrutural e químico** completo (Seções 16–19), classificado em categorias seguras, nunca em juízo de função biológica, com fidelidade completa de conectividade (Seção 18, correção de F-03) e identidade de entidade/cadeia honesta mesmo quando a fonte não a declara (Seção 15, correção de F-01).
4. **`ReceptorSelectionPolicy`** — declaração explícita do cientista, agora vinculada a um `inspection_id` e a um `raw_checksum_observed` (Seção 21), create-once, imutável.
5. **`ResolvedReceptorSelection`** — resolução determinística da política contra o RAW e contra o relatório de inspeção referenciado, create-once, sem máquina de attempt multi-fase, sem duplicar o inventário completo (Seção 22, correção de F-04).
6. **Rejeição ativa de entrada comprimida** (Seção 11, correção de F-02) como parte do próprio contrato de formatos, não como um detalhe de segurança isolado.
7. **Provenance, identidade e idempotência** completas para os quatro objetos agora persistidos (inspeção, política, resolução, e o `ProteinInput` RAW já existente).
8. **Comandos CLI observáveis** — inspecionar (criar-ou-reutilizar), mostrar inspeção, declarar seleção, resolver seleção, mostrar seleção, mostrar resolução, listar seleções.

---

## 7. Fora de Escopo

Herdado e reafirmado do Draft original e do Revised Discovery, sem alteração — nenhuma correção desta revisão amplia o escopo em direção a química ou materialização:

### Transformação estrutural — fora do 020 (fica para o 021)
Materializar assembly; extrair cadeias; resolver/remover altlocs fisicamente; remover água/ligante/cofator/metal fisicamente; reconstruir componente; gerar novo mmCIF/PDB; produzir `PreparedReceptorArtifact`.

### Preparação química — fora do 020 (fica para 022–024 ou posterior)
Adicionar hidrogênios; atribuir protonação; calcular pKa; corrigir orientação de His/Asn/Gln; construir átomos ou resíduos; reparar loops; atribuir cargas; minimizar geometria; solvatar; adicionar membrana.

### Itens já fora de escopo, reafirmados sem alteração
Docking; search space; scoring; `Pose`; ranking; execução Vina; PDBQT como modelo central; redocking; RMSD de validação; conformer generation; ETKDG; otimização de geometria; campos de força; MOPAC; HF; DFT; STO/GTO; enumeração de microestados; seleção automática da melhor estrutura; GUI; banco de dados; scheduler; execução em nuvem; IA para decisões científicas; recomendações automáticas; simulação de membrana; dinâmica molecular; cascatas intracelulares.

### Explicitamente não resolvido por esta especificação, por decisão (não por omissão)
- Determinação automática de função biológica de qualquer componente não-polimérico além de água/íon metálico (Seção 17).
- Resolução de membership de cadeia dentro de um assembly declarado (assemblies são apenas listados, nunca resolvidos).
- Qualquer mecanismo de revisão/supersedes para `ReceptorSelectionPolicy` ou `ResolvedReceptorSelection`.
- Qualquer identidade secundária derivada de conteúdo (`semantic_key`-like) para `ResolvedReceptorSelection` — distinta e não confundida com o `inspection_id` determinístico introduzido por esta revisão para `ReceptorInspectionReport` (Seção 23.1 explica a distinção).
- Re-resolução de uma política contra uma inspeção diferente da que foi originalmente referenciada — eliminada como possibilidade por construção (Seção 24), não apenas proibida por regra.
- Materialização física de qualquer registro legado de conectividade PDB (`SSBOND`/`LINK`/`CONECT`) — apenas inventariados (Seção 18.4).

---

## 8. Terminologia Normativa

Herdada da Seção 8 do Draft original, com três entradas novas desta revisão:

| Termo | Definição normativa |
|---|---|
| **RAW receptor artifact** | O `ProteinInput`/`RawArtifact` já registrado — imutável, nunca reescrito por este incremento. |
| **`ReceptorInspectionReport`** | Resultado factual e determinístico da leitura read-only do RAW. **Persistido create-once** (Seção 14), identificado por `inspection_id`. |
| **`inspection_id`** *(novo nesta revisão)* | Identidade determinística e derivada de conteúdo de um `ReceptorInspectionReport`, calculada sobre um payload canônico fixo (Seção 15). Nunca escolhida pelo cientista; nunca "latest". |
| **`identity_origin`** *(novo nesta revisão)* | Classificação de proveniência de um identificador estrutural (`label_asym_id`/`label_entity_id`): `"source"` (declarado pelo formato), `"parser-derived"` (reservado, nunca produzido por este incremento), `"unavailable"` (a fonte não declara, e nenhuma inferência é feita). |
| **`selection_capability`** *(novo nesta revisão)* | `"full"` quando toda cadeia/entidade relevante tem `identity_origin="source"`; `"inspection-only"` caso contrário. Seleção e resolução exigem `"full"`. |
| **`ReceptorSelectionPolicy`** | Declaração explícita e imutável do cientista — modelo, assembly, cadeias, disposições, **vinculada a um `inspection_id` e a um `raw_checksum_observed`**. Create-once, identidade autoral. |
| **`ResolvedReceptorSelection`** | Resolução determinística e create-once da política contra o RAW e contra o relatório de inspeção referenciado por `inspection_id`. **Nunca embute o relatório completo** (Seção 22). Não é uma representação molecular; não contém nenhuma coordenada nova. |
| **Materialização estrutural** | Produzir um novo arquivo de coordenadas. Fora do 020. |
| **Preparação química** | Hidrogênios, protonação, pKa, cargas, minimização, solvatação, membrana. Fora do 020. |
| **Disposição (`disposition`)** | A intenção declarada do cientista (`keep`/`remove`) para um componente ou classe de componente, registrada e confirmada logicamente pelo 020, nunca executada fisicamente. |
| **Classificação (`classification`)** | O resultado mecânico, derivado apenas de sinais já declarados pelo formato/dicionário químico, de qual balde seguro um componente não-polimérico ocupa (Seção 17). Nunca um juízo de função biológica. |
| **Papel (`role`)** | A etiqueta científica (`cofactor`/`crystallographic_ligand`) que o próprio cientista atribui a um componente nomeado via `component_dispositions` — nunca inferida pelo 020. |

Fronteiras semânticas herdadas (Draft original, Seção 8), preservadas integralmente:

```
Experimental structure ≠ Prepared receptor
RAW receptor artifact ≠ Derived representation
ExperimentalConditions ≠ PreparationPolicy
PreparationPolicy ≠ EngineParameters
RequestedParameters ≠ ResolvedParameters
EngineParameters ≠ ExecutionResult
ScientificEntity ≠ MolecularState ≠ Conformer ≠ Pose
PDB/mmCIF experimental record ≠ PDBQT docking artifact
Crystallization pH ≠ Assay pH ≠ Physiological pH ≠ Preparation pH
Receptor preparation ≠ Protonation
Receptor preparation ≠ SearchSpace
Receptor preparation ≠ Docking
Observation of missing coordinates ≠ Authorization to repair
Observation of missing coordinates ≠ Repair policy
Observation of missing coordinates ≠ Repaired artifact
Inspection ≠ Logical selection ≠ Structural materialization ≠ Chemical preparation
ReceptorInspectionReport ≠ ReceptorSelectionPolicy ≠ ResolvedReceptorSelection ≠ PreparedReceptorArtifact
Evidence ≠ ExperimentalConditions ≠ ScientificPolicy ≠ EngineParameters ≠ ExecutionResult
Classification ≠ Role ≠ Disposition ≠ Physical removal
```

---

## 9. Fronteiras Semânticas Adicionais

Herdadas da Seção 9 do Draft original, mais duas fronteiras novas desta revisão:

```
gemmi.* (objeto de biblioteca) ≠ ReceptorInspectionReport.* (modelo de domínio)
Inventory classification (water / metal-ion / modified-polymer-residue / other-non-polymer / unknown) ≠ Biological function
Declared selection (ReceptorSelectionPolicy) ≠ Confirmed selection (ResolvedReceptorSelection) ≠ Materialized selection (021, fora de escopo)
Source identity (identity_origin="source") ≠ Parser-derived identity (identity_origin="parser-derived", reservado, nunca produzido no 020) ≠ Unavailable identity (identity_origin="unavailable")
Compressed RAW content ≠ Acceptable RAW content — nenhuma descompressão, nenhuma exceção, nenhum caminho comprimido entregue ao parser
```

A primeira fronteira é arquitetural: nenhum tipo de `gemmi` aparece em qualquer assinatura pública de `receptor_inspection.py`, `receptor_selection.py`, `receptor_resolution.py`, `receptor_registry.py`, `receptor_service.py` ou `cli.py`. A tradução ocorre inteiramente dentro de `receptor_parsing.py` (Seção 10.5).

A segunda fronteira é científica: a classificação mecânica de um componente não-polimérico nunca é apresentada como uma afirmação sobre o papel biológico desse componente.

A terceira fronteira é de ciclo de vida: declarada → confirmada → materializada (021, fora de escopo), nunca confundidas.

A quarta fronteira, **nova nesta revisão** (corrige F-01): a identidade de um identificador estrutural é sempre rastreável à sua origem exata. `"parser-derived"` existe no vocabulário por completude — para uma eventual regra de derivação futura que seja segura e explicitamente especificada — mas este incremento nunca produz esse valor; qualquer identificador não declarado pela fonte é `"unavailable"`, nunca inventado.

A quinta fronteira, **nova nesta revisão** (corrige F-02): conteúdo comprimido nunca é uma entrada aceitável para o 020, independentemente de extensão declarada, de magic bytes, ou de qualquer capacidade de descompressão que a biblioteca escolhida possa oferecer.

---

## 10. Gemmi

### 10.1 Decisão preservada

**Gemmi 0.7.5** (ou a versão estável mais recente verificada contra o índice oficial do PyPI no momento do Checkpoint 1) permanece o parser escolhido. A Adversarial Review (`06-draft-review`, Seção 6) confirmou contra fontes oficiais exclusivas (índice JSON do PyPI, `gemmi.readthedocs.io`) que a biblioteca satisfaz licença (MPL-2.0/LGPLv3), manutenção (CCP4/Global Phasing Ltd.), disponibilidade para Windows (`win_amd64`, `cp39`–`cp314`), acesso de baixo nível a categorias mmCIF (`Block.find_mmcif_category`/`Block.find`), ausência de conversão automática para PDB, e documentação oficial. Nenhum destes pontos é reaberto aqui.

### 10.2 Classificação atualizada

**VALIDATED WITH CHANGES — CHANGES INCORPORATED.**

A classificação anterior (`VALIDATED WITH CHANGES`) refletia que a escolha da biblioteca era correta mas seu uso específico tinha duas lacunas concretas (F-01: derivação de identidade para PDB legado; F-02: tratamento de entrada comprimida). Esta revisão incorpora as mudanças exigidas — a biblioteca permanece a mesma, o adapter permanece isolado, e as duas lacunas são corrigidas por decisão normativa explícita (Seções 12 e 15). Nenhuma nova lacuna foi introduzida; a classificação avança para o estado final que a Seção 33 da Adversarial Review definia como condição de saída.

### 10.3 Proibições explícitas (novas nesta revisão)

Além das proibições já herdadas (nenhuma conversão para PDB, nenhuma química automática, nenhuma rede, nenhum subprocesso), esta revisão acrescenta, fechando F-01 e o achado MINOR F-08:

- **Nenhuma chamada a `Gemmi.setup_entities()` (ou a qualquer uma de suas quatro operações internas — `add_entity_types()`, `assign_subchains()`, `ensure_entities()`, `deduplicate_entities()`) para produzir identidade factual.** A documentação oficial do Gemmi descreve `setup_entities()` como heurística (usa distância entre resíduos para inferir limites de entidade) e como produtora de identificadores de subchain inventados pela própria biblioteca (ex. `"Axp"`, `"Ax0"`, `"Axw"`) — nenhum dos dois é uma identidade declarada pela fonte, e `receptor_parsing.py` nunca invoca essas funções em nenhum caminho de código deste incremento.
- **Nenhuma leitura de conteúdo comprimido**, por nenhum mecanismo da biblioteca (Seção 11).
- **Nenhuma chamada aos métodos mutantes de conveniência da biblioteca** — `remove_hydrogens()`, `remove_waters()`, `remove_ligands_and_waters()`, `remove_alternative_conformations()`, ou qualquer outro método que modifique um `Structure` em memória. A Adversarial Review (F-08) observou que estes métodos mapeiam quase 1:1 sobre operações que a Seção 7 declara fora de escopo; `receptor_parsing.py` nunca os invoca, exatamente pela mesma disciplina que já justifica a rejeição do PDBFixer como parser central (Seção 10.6 do Draft original, preservada sem alteração).
- **`KeyboardInterrupt`/`SystemExit` nunca são capturados** por nenhum bloco de tradução de exceção dentro de `receptor_parsing.py` — apenas subtipos específicos de `Exception` levantados pela própria biblioteca são traduzidos para a taxonomia deste domínio (Seção 31); uma interrupção de processo sempre propaga sem modificação.
- **Toda exceção traduzida preserva `__cause__`** — nenhuma exceção nativa do Gemmi é descartada ou resumida sem rastro.

### 10.4 Fronteira interna (inalterada em espírito, reforçada em detalhe)

- `receptor_parsing.py` permanece o **único** módulo deste incremento, e de todo o repositório, a executar `import gemmi`.
- A função pública de topo (`parse_receptor_raw`) permanece a única porta de entrada; nenhum tipo `gemmi.*` atravessa essa fronteira (Seção 9).
- A versão efetiva (`gemmi.__version__`) é sempre capturada em tempo de execução e registrada no `ReceptorInspectionReport` persistido — nunca copiada do pin de `pyproject.toml`.

### 10.5 Se Gemmi exigir caminho de arquivo (decisão sobre a API, sem inventar capacidade)

A documentação oficial do Gemmi expõe sua API primária de leitura por **caminho de arquivo** (`cif.read(path)`, `read_structure(path)`); esta especificação não assume nem promete uma API de leitura a partir de um buffer de bytes em memória, porque isso não foi confirmado contra a documentação oficial consultada, e inventar essa capacidade violaria a regra desta tarefa de não inventar capacidade.

**Decisão:** o fluxo seguro (Seção 11.3) valida o conteúdo completo do arquivo RAW — tamanho, magic bytes, ausência de compressão, checksum — lendo-o diretamente via E/S padrão do Python, **antes** de qualquer chamada ao Gemmi. Somente depois que essa validação completa é bem-sucedida, o **mesmo caminho de arquivo já validado** (nunca um caminho alternativo, nunca um arquivo temporário descomprimido, nunca um caminho fornecido por um chamador) é entregue ao Gemmi para parsing. Como a validação dos passos anteriores já leu e verificou os bytes completos do arquivo, a leitura subsequente do Gemmi sobre o mesmo caminho não reabre nenhuma das proteções já aplicadas — sob a mesma garantia de processo único já aceita pela Seção 29.1/21.3 do Draft original (preservada, Seção 32 deste documento).

---

## 11. Formatos e Compressão

### 11.1 Formatos aceitos

- **PDBx/mmCIF** é o formato informacional principal. Extensões reconhecidas: `.cif`, `.mmcif`.
- **PDB legado** é suportado como via de entrada de compatibilidade limitada (Seção 12). Extensões reconhecidas: `.pdb`, `.ent`.
  - **Justificativa para `.ent`:** esta é a convenção de nomenclatura histórica usada pelos espelhos de distribuição FTP do wwPDB e por ferramentas amplamente usadas (Biopython, PyMOL) para o mesmo formato textual de PDB legado — não é um formato novo, é um alias de extensão para o mesmo conteúdo que `.pdb` já designa. Tratado de forma idêntica a `.pdb` em todo o pipeline, nunca como uma via de entrada distinta.
- O formato real (mmCIF vs. PDB legado) é sempre **detectado por conteúdo** (via a própria detecção do Gemmi ao abrir o arquivo), nunca apenas pela extensão declarada ou pelo campo `RawArtifact.format` já persistido — herdado sem alteração da Seção 11 do Draft original.

### 11.2 Entrada comprimida — rejeitada integralmente (corrige F-02)

**Decisão vinculante desta revisão: o 020 não aceita nenhum formato de entrada comprimido, sob nenhuma circunstância.**

- **Extensões rejeitadas** (lista fechada, verificada antes de qualquer outra validação): `.gz`, `.bz2`, `.xz`, `.zip`. Qualquer RAW cuja extensão declarada (a última extensão do nome de arquivo, exatamente como `Path.suffix` a reporta) pertença a esta lista é rejeitado **imediatamente**, com `CompressedExtensionRejectedError` (Seção 31), **antes** de o arquivo ser aberto para qualquer outra verificação. Esta rejeição é **incondicional** — nunca é revertida mesmo que o conteúdo real não esteja de fato comprimido (T-103): a extensão por si só já é motivo suficiente de rejeição, por disciplina de defesa em profundidade.
- **Comparação de extensão normalizada por `casefold()` (correção m-05 desta promoção):** a extensão declarada é sempre comparada contra a lista fechada acima via `Path.suffix.casefold()` (equivalentemente, `.lower()` para os quatro literais ASCII desta lista) — nunca por comparação sensível a caixa. `.GZ`, `.Gz`, `.gZ` e qualquer outra variação de caixa de `.gz`/`.bz2`/`.xz`/`.zip` são rejeitadas de forma idêntica a `.gz`/`.bz2`/`.xz`/`.zip`, sem exceção — sem exigir, por si só, um cenário normativo dedicado adicional (a correção m-05 não está listada na Seção 19 da Corrected Revised Draft Confirmation como exigindo extensão da matriz T-001–T-137; T-096/T-102/T-103 já exercitam a rejeição por extensão, agora sob a regra `casefold()` explícita). Esta é uma regra de comparação de sufixo de nome de arquivo, exclusivamente — nenhuma normalização de case é aplicada a nenhum conteúdo científico (identificadores mmCIF permanecem case-sensitive, Seção 23.2).
- **Magic bytes rejeitados, independentemente da extensão declarada.** Mesmo quando a extensão é uma das reconhecidas (`.cif`, `.mmcif`, `.pdb`, `.ent`), os primeiros bytes do conteúdo real são verificados contra as assinaturas públicas e estáveis de cada formato de compressão, antes de qualquer tentativa de parsing:

| Formato | Assinatura (magic bytes) | Fonte |
|---|---|---|
| gzip | `0x1F 0x8B` | RFC 1952 |
| bzip2 | `0x42 0x5A 0x68` (ASCII `"BZh"`) | Especificação pública do formato bzip2 |
| xz | `0xFD 0x37 0x7A 0x58 0x5A 0x00` | Especificação pública do formato `.xz` |
| zip | `0x50 0x4B 0x03 0x04` (local file header; também `0x50 0x4B 0x05 0x06`/`0x50 0x4B 0x07 0x08`) | Especificação pública do formato ZIP |

  Uma correspondência com qualquer uma destas assinaturas, em qualquer arquivo RAW aceito pela extensão, levanta `CompressedRawContentError` (Seção 31). Isso cobre explicitamente: um arquivo nomeado `estrutura.cif` cujo conteúdo real é gzip (T-101); um arquivo originalmente `.gz` renomeado para `.cif` (T-102) — o mesmo mecanismo de detecção por conteúdo captura ambos os casos de forma idêntica, porque a verificação nunca confia na extensão para decidir se o conteúdo está comprimido.
- **Nenhuma descompressão jamais ocorre** em nenhum ponto do pipeline do 020 — nem automática, nem sob demanda, nem como conveniência. Rejeitar é a única resposta a conteúdo comprimido.
- **Nenhum caminho comprimido é passado ao Gemmi.** A rejeição ocorre inteiramente dentro da validação própria do 020 (Seção 11.3), antes de qualquer chamada ao adaptador Gemmi — o Gemmi nunca vê um arquivo comprimido, bem-sucedido ou não.
- **Nenhum acesso por URL. Nenhum stream de rede. Nenhum arquivo temporário descomprimido é criado** em nenhuma circunstância — reafirmado sem exceção.

### 11.3 Fluxo seguro de leitura (novo nesta revisão)

Substitui integralmente a verificação de tamanho isolada da Seção 29.2 do Draft original. Executado inteiramente dentro de `receptor_parsing.py`, antes de qualquer chamada ao Gemmi:

0. **Rejeitar por extensão (correção m-04 desta promoção; Seção 11.2)** — a extensão declarada do RAW é comparada, via `casefold()` (Seção 11.2), contra a lista fechada de extensões comprimidas; correspondência → `CompressedExtensionRejectedError`, **antes** de o arquivo ser aberto para qualquer outra verificação, incluindo o Passo 1. Este é o primeiro passo do fluxo seguro, explicitamente numerado para eliminar a lacuna entre a prosa da Seção 11.2 (que já descrevia esta rejeição como ocorrendo "antes de o arquivo ser aberto") e a enumeração mecânica abaixo, que anteriormente não a listava.
1. **Validar caminho e identidade de storage** — o caminho do RAW é sempre derivado do registro já existente do `ProteinInput` (`project_dir/inputs/proteins/<id>/<raw_file>`), nunca aceito como argumento livre; a identidade de storage já foi estabelecida no momento de `protein add` (Seção 32.1, herdada sem alteração).
2. **Abrir o RAW pelas primitivas seguras da plataforma** — `open(path, "rb")` simples, sobre o caminho já validado no passo 1; nenhuma nova camada de reparse-point detection é adicionada (justificativa inalterada, Seção 32.1).
3. **Verificar tamanho** — `path.stat().st_size` comparado contra o teto configurado (1 GiB, Seção 32.2); excedido → `RawArtifactTooLargeError` (Seção 31), antes de ler qualquer byte do conteúdo.
4. **Verificar magic bytes** — ler os primeiros 6 bytes do arquivo e comparar contra as quatro assinaturas da Seção 11.2; correspondência → `CompressedRawContentError`, leitura abortada imediatamente.
5. **Rejeitar compressão** — decorrência direta dos passos anteriores; nenhum passo subsequente executa se qualquer um dos passos 3–4 rejeitar.
6. **Calcular checksum** — SHA-256 computado sobre os bytes efetivamente lidos, em streaming, exatamente como `compute_sha256` já faz em `atomic.py` (reutilizado, não duplicado).
7. **Ler conteúdo não comprimido sob limites** — o restante do arquivo é lido por completo (já comprovadamente não comprimido e dentro do teto de tamanho), respeitando os tetos de contagem da Seção 32.2 durante a construção do inventário (não durante esta leitura bruta, que é byte a byte).
8. **Entregar conteúdo controlado ao adapter** — o caminho já validado (Seção 10.5) é entregue ao Gemmi para parsing real; o checksum e o tamanho já confirmados nos passos 3 e 6 tornam essa chamada segura.
9. **Confirmar checksum/identidade conforme protocolo definido** — o checksum computado no passo 6 é comparado contra `RawArtifact.checksum` já persistido; divergência → `RawChecksumMismatchError` (herdado, Seção 31), antes de qualquer resultado ser retornado ou persistido.

Este fluxo é a única via de leitura do RAW em todo o 020 — usada identicamente por `inspect_receptor` e por qualquer caminho interno que `declare_receptor_selection` invoque.

### 11.4 Preservação e limitações, herdadas sem alteração

- RAW sempre preservado byte a byte; aberto exclusivamente em modo leitura.
- Nenhuma conversão automática mmCIF→PDB ou PDB→mmCIF. Nenhuma normalização destrutiva. Nenhum round-trip.
- `label_asym_id`/`label_entity_id` nativos não existem no formato PDB legado — tratados pela Seção 15 (identidade honesta), não mais por um único booleano (`label_asym_id_is_auth_equivalent`, retirado — Seção 15.4 explica a simplificação).
- Ausência de informação nunca se torna valor científico inventado — toda ausência resulta em `None`/coleção vazia/`identity_origin="unavailable"`/warning estruturado, nunca em um valor padrão silenciosamente assumido.

### 11.5 Divergência `raw_format_declared`/`structure_format` — corrige F-10

Quando o formato detectado por conteúdo (`structure_format`) diverge do formato originalmente declarado em `RawArtifact.format` (`raw_format_declared`), a detecção por conteúdo prevalece (herdado, inalterado) — mas agora um warning estruturado novo é emitido: `declared-format-mismatch` (Seção 19.1, décimo-quinto código do vocabulário, estendido de 14 para 15 entradas por esta revisão). Isso corrige a lacuna que F-10 identificou: a divergência deixa de ser uma correção silenciosa e passa a ser uma condição observável e testável (T-012, reescrito).

---

## 12. PDB Legado

Consolidação completa da política, corrigindo F-01 e reconciliando as NOTES N-10 (SSBOND/LINK/CONECT; REMARK 465/470) que a Adversarial Review registrou como observações não corretivas, mas recomendou decidir explicitamente.

### 12.1 Princípio geral

PDB legado **pode sempre ser inspecionado** — nunca é rejeitado como formato de entrada. As limitações nativas do formato são sempre estruturadas (nunca texto livre), e nenhuma delas vira um erro impeditivo de inspeção. O que PDB legado **não pode**, em geral, é originar uma seleção resolvida (Seção 12.4).

### 12.2 Identidade estrutural

- `label_asym_id` e `label_entity_id` **não existem nativamente** no formato PDB legado. O 020 nunca os reconstrói, nunca os deriva por heurística, nunca os promove silenciosamente a partir de `auth_asym_id`.
- Para toda cadeia/entidade cuja origem seja PDB legado: `label_asym_id = None`, `label_entity_id = None`, cada um com seu campo `*_origin = "unavailable"` (Seção 15).
- `auth_asym_id` preserva exatamente o identificador de cadeia disponível no arquivo PDB (coluna de chain ID) — sempre populado quando o formato o declara.
- **Nenhum fallback para `auth_asym_id` sozinho ocorre em nenhuma circunstância** — `auth_asym_id` nunca se torna, por conveniência, um substituto silencioso de `label_asym_id` em nenhum campo que declare explicitamente carregar identidade canônica (Seção 20.1, `ChainSelector`).

### 12.3 Conectividade legada — `SSBOND`, `LINK`, `CONECT` (reconciliando N-10, parte 1)

Diferente do Draft original, que deixava implícita a possibilidade de que toda conectividade de um PDB legado desaparecesse do inventário, esta revisão decide explicitamente: **`SSBOND`, `LINK` e `CONECT` são preservados quando o Gemmi os expõe através de sua própria API estruturada para o modelo `Structure` de alto nível** (a mesma API já usada para o restante do inventário de PDB legado — nenhuma nova capacidade é inventada; nenhum parsing manual de texto bruto é feito por este incremento). Mapeamento mecânico para os três baldes já existentes (Seção 18.3):

| Registro legado | Balde de destino | `source_category` |
|---|---|---|
| `SSBOND` | `disulfide_bonds` | `"legacy-pdb-ssbond"` |
| `LINK`, nenhum parceiro classificado `"metal-ion"` | `covalent_connections` | `"legacy-pdb-link"` |
| `LINK`, pelo menos um parceiro classificado `"metal-ion"` | `metal_coordinations` | `"legacy-pdb-link"` |
| `CONECT`, nenhum parceiro classificado `"metal-ion"` | `covalent_connections` | `"legacy-pdb-conect"` |
| `CONECT`, pelo menos um parceiro classificado `"metal-ion"` | `metal_coordinations` | `"legacy-pdb-conect"` |

**Correção m-06/n-03 desta promoção:** as duas linhas de `LINK`/`CONECT` acima usam explicitamente "pelo menos um parceiro classificado", substituindo "um parceiro classificado" — eliminando a ambiguidade entre "exatamente um" e "pelo menos um" para o caso de ponte metal-metal (ambos os parceiros classificados `"metal-ion"`). Sob a redação corrigida, um registro com dois parceiros metálicos é classificado `metal_coordinations` de forma determinística, pela mesma regra que já classifica o caso de um único parceiro metálico — nenhum balde de destino novo é introduzido, nenhum redesenho de modelo é necessário. A mesma terminologia "pelo menos um" já era usada na Seção 15.6 (`selection_capability`); esta correção padroniza as Seções 12.3/18.3 para a mesma convenção (n-03).

Cada `StructureConnection` resultante (Seção 18.2) carrega `source_category` explicitamente, de modo que um consumidor nunca confunde uma conexão declarada por `_struct_conn` (mmCIF) com uma inferida de registros legados. Os campos de endpoint que o PDB legado não declara nativamente (`label_*`, `label_alt_id`, `symmetry`) permanecem `None` — apenas os campos em espaço de autor (`auth_asym_id`, `auth_seq_id`, `auth_comp_id`, `auth_atom_id`) são populados a partir de registros legados.

### 12.4 Coordenadas ausentes legadas — `REMARK 465`/`470` (reconciliando N-10, parte 2)

**Decisão condicionada à capacidade real do parser, nunca a uma suposição:** `REMARK 465`/`470` só populam `missing_residues`/`missing_atoms` quando o Gemmi expõe essas informações através de uma API estruturada e documentada para o modelo de alto nível (o mesmo padrão de "usar apenas o que a biblioteca expõe estruturadamente" já aplicado em toda esta especificação). O 020 **nunca** faz parsing manual de texto de `REMARK` dentro de `receptor_parsing.py` — isso seria introduzir um segundo parser ad hoc fora da fronteira Gemmi sancionada (Seção 9), exatamente o risco que a fronteira existe para eliminar.

- Se a API estruturada expõe os dados: `missing_residues`/`missing_atoms` são populados exatamente como no caminho mmCIF (T-121).
- Se não expõe (confirmável apenas na implementação real do Checkpoint 1): a categoria permanece em `unavailable_categories`, com um warning `category-unavailable` nomeando `"REMARK465"`/`"REMARK470"` como o identificador de categoria — nunca tratado como "nenhum resíduo ausente" (T-120).

Esta é uma decisão condicional explícita, não um TBD: o comportamento está completamente especificado para ambos os casos possíveis; apenas qual dos dois casos se aplica depende de uma capacidade de biblioteca a confirmar no Checkpoint 1 — exatamente como a Seção 10.6 do Draft original já tratava o dígito exato do pin de versão do Gemmi (uma decisão fechada cujo valor concreto depende do momento de implementação, nunca uma decisão em aberto).

### 12.5 `selection_capability` para PDB legado

Toda inspeção de origem PDB legado tem `selection_capability = "inspection-only"` — nunca `"full"` (Seção 15.5 define a regra geral; para PDB legado, `label_asym_id`/`label_entity_id` são sempre `"unavailable"` para toda cadeia/entidade, o que força `"inspection-only"` por construção).

### 12.6 Nenhuma conversão automática, nenhuma heurística

- Nenhuma conversão automática de PDB legado para mmCIF ocorre em nenhum ponto do 020.
- Nenhuma chamada a `setup_entities()` ou equivalente heurístico é feita para produzir identidade factual (Seção 10.3) — reafirmado especificamente para este caminho, onde a tentação de usá-lo seria maior.

---

## 13. Modelos de Domínio

Visão geral da cadeia de modelos deste incremento, todos `pydantic.BaseModel` com `model_config = ConfigDict(frozen=True, extra="forbid")`, seguindo o padrão já estabelecido por `conditions.py`/`scientific.py`/`transformation.py`. Atualizada em relação à Seção 12 do Draft original para refletir a persistência create-once do relatório de inspeção (corrige F-04):

```
ProteinInput (já existente, inputs.py)
  ↓ (referenciado por id, nunca modificado)
ReceptorInspectionReport (persistido create-once; identidade determinística via inspection_id — Seção 14/15)
  ↓ (referenciado por inspection_id)
ReceptorSelectionPolicy (declarado pelo cientista; create-once; identidade autoral; referencia inspection_id)
  ↓ (resolvido contra o RAW + o relatório referenciado por inspection_id)
ResolvedReceptorSelection (create-once; 1:1 com a política que resolve; referencia inspection_id, nunca embute o relatório completo)
```

Nenhum destes modelos cria um `StateTransformationRecord` (Seção 26). Nenhum destes modelos representa coordenadas transformadas ou um arquivo de estrutura derivado (Seção 27.2).

Modelos renomeados nesta revisão, por exigência explícita da tarefa que a originou, sem mudança de responsabilidade:

| Nome anterior (Draft original) | Nome nesta revisão | Módulo |
|---|---|---|
| `EntityDescriptor` | `EntityInventoryEntry` | `receptor_inspection.py` |
| `ChainDescriptor` | `ChainInventoryEntry` | `receptor_inspection.py` |
| `DisulfideBond`, `CovalentConnection`, `MetalCoordination` | `StructureConnection` (modelo único, Seção 18.2) | `receptor_inspection.py` |

Todas as demais classes (`ModelDescriptor`, `AssemblyDescriptor`, `AssemblyOperationExpression`, `NonPolymerComponent`, `ReceptorSelectionPolicy`, `ChainSelector`, `ComponentDisposition`, `ResolvedReceptorSelection`, `ResolvedChainSelection`, `ResolvedComponentDisposition`) mantêm o nome do Draft original.

---

## 14. ReceptorInspectionReport Persistido (corrige F-04)

### 14.1 Decisão de persistência — substituída integralmente

**O Draft original decidia (Seção 13.1 daquele documento) que `ReceptorInspectionReport` não seria persistido como registry create-once — seria computado sob demanda e embutido como snapshot completo dentro de `ResolvedReceptorSelection`, com um cache opcional endereçado por conteúdo.** A Adversarial Review (F-04) identificou que essa decisão, embora razoável em princípio, produzia duplicação completa do inventário a cada resolução, sem reconhecimento de custo e sem limite.

**Esta revisão substitui essa decisão integralmente: `ReceptorInspectionReport` é agora persistido create-once**, como um registro de primeira classe, identificado por um `inspection_id` determinístico (Seção 15). Não é uma máquina de attempts — é um registro simples, create-once, exatamente no mesmo espírito do padrão já validado por `ScientificConditionsDeclaration` (Incremento 019), apenas com uma identidade derivada de conteúdo em vez de autoral (justificativa completa na Seção 15.6).

### 14.2 Fluxo corrigido

```
ProteinInput (RAW imutável)
  → ReceptorInspectionReport persistido (create-once, identificado por inspection_id)
  → ReceptorSelectionPolicy (referencia inspection_id, protein_input_id, raw_checksum_observed)
  → ResolvedReceptorSelection (referencia inspection_id; nunca embute o relatório completo)
```

### 14.3 Regras de persistência (vinculantes)

1. **Uma inspeção é persistida uma vez.** Dado um `inspection_id`, o arquivo correspondente é escrito exatamente uma vez, na primeira vez em que aquele `inspection_id` é computado; toda chamada subsequente com o mesmo `inspection_id` é um *hit* de create-once, nunca uma reescrita.
2. **Múltiplas políticas podem referenciar a mesma inspeção.** Nenhum limite é imposto a quantas `ReceptorSelectionPolicy` referenciam o mesmo `inspection_id` — exatamente o padrão de múltiplas seleções sobre o mesmo RAW já endossado pelo Revised Discovery (Seção 9 daquele documento), agora estendido para múltiplas políticas compartilharem uma única inspeção persistida.
3. **Múltiplas resoluções não duplicam o inventário completo.** Cada `ResolvedReceptorSelection` referencia `inspection_id` por valor de string; o inventário completo existe em exatamente um lugar — o registro de inspeção persistido — independentemente de quantas resoluções o referenciam (T-130 prova isso diretamente).
4. **`ResolvedReceptorSelection` referencia `inspection_id`** — nunca embute o relatório completo (Seção 22.1).
5. **`ResolvedReceptorSelection` pode conter apenas o subconjunto resolvido necessário** — as cadeias e disposições efetivamente confirmadas (já bounded pela seleção do cientista, nunca o inventário inteiro).
6. **O relatório completo permanece na fonte de verdade persistida** — qualquer consumidor (incluindo o futuro 021) que precise do inventário completo o carrega por `inspection_id`, nunca a partir de uma cópia embutida em outro objeto.
7. **Nenhuma reescrita do relatório** — um `ReceptorInspectionReport` persistido é imutável; nenhuma operação deste incremento o modifica após a criação.
8. **Mudança do RAW produz uma nova inspeção.** Como `raw_checksum` participa do payload canônico (Seção 15.2), um RAW diferente produz, por construção, um `inspection_id` diferente — nunca uma colisão, nunca uma substituição do registro anterior.
9. **Mudança de parser/version produz uma nova inspeção.** `parser_name`/`parser_version` participam do payload canônico — uma atualização do Gemmi instalado produz um `inspection_id` novo na próxima chamada, coexistindo pacificamente com o registro anterior (que permanece válido e carregável para sempre).
10. **Mudança do schema/profile produz uma nova inspeção.** `inspection_schema_version`/`inspection_profile_version` participam do payload canônico (Seção 15.1) — uma revisão futura das regras de classificação do 020 (por exemplo, `METAL_ION_CCD_CODES_V2`) é expressa como um incremento de `INSPECTION_PROFILE_VERSION`, produzindo um `inspection_id` novo, nunca uma reinterpretação silenciosa de um registro já persistido.
11. **Registros anteriores permanecem imutáveis** — nenhuma das regras 8–10 jamais apaga, substitui ou reinterpreta um `ReceptorInspectionReport` já persistido.

### 14.4 Layout de persistência

```
project_dir/
  scientific/
    receptor_inspections/
      <inspection_id>.yaml        # ReceptorInspectionReport, create-once, identidade determinística
    receptor_selections/
      <selection_id>.yaml         # ReceptorSelectionPolicy, create-once, identidade autoral
      resolved/
        <selection_id>.yaml       # ResolvedReceptorSelection, create-once, 1:1 com a política
```

Caminho exato para relatórios de inspeção: `project_dir/scientific/receptor_inspections/<inspection_id>.yaml` — substituindo o caminho de cache por conteúdo composto (`<raw_checksum>__<parser_name>-<parser_version>.yaml`) do Draft original por um único identificador determinístico que já incorpora todos os componentes relevantes (Seção 15.2), e que agora é um registro de primeira classe, não um cache opcional.

### 14.5 `protein inspect` — criar ou reutilizar, nunca inferir por timestamp

`protein inspect` (via `inspect_receptor`, Seção 25) sempre:

1. computa o `inspection_id` determinístico para o `protein_input_id` dado, contra o RAW e o parser atualmente instalados;
2. verifica se um registro com esse `inspection_id` já existe;
3. se existe: carrega-o, retorna-o com `created=False`/`reused=True` — este fato é **sempre** o resultado factual e explícito da própria chamada ao registry (presença/ausência do arquivo antes da escrita), **nunca inferido de uma comparação de timestamp** ou de qualquer heurística lateral;
4. se não existe: invoca o fluxo seguro de leitura (Seção 11.3) e o parser, constrói o relatório, persiste-o, retorna-o com `created=True`/`reused=False`;
5. registra atividade coerente com o resultado factual (Seção 29) em ambos os casos.

---

## 15. Inspection Identity

### 15.1 Payload canônico

A identidade de um `ReceptorInspectionReport` é determinística, derivada de conteúdo, calculada sobre o seguinte payload mínimo — exatamente sete chaves, nenhuma opcional, nenhum campo autoral:

```python
INSPECTION_SCHEMA_VERSION = "1.0"     # versão do shape Pydantic de ReceptorInspectionReport
INSPECTION_PROFILE_VERSION = "1.0"    # versão das REGRAS de inspeção/classificação deste incremento
                                        # (inclui, entre outras, a versão da tabela de íons metálicos,
                                        # Seção 17.1, e o vocabulário de warnings, Seção 19.1)

payload = {
    "inspection_schema_version": INSPECTION_SCHEMA_VERSION,
    "inspection_profile_version": INSPECTION_PROFILE_VERSION,
    "parser_name": parser_name,        # "gemmi"
    "parser_version": parser_version,  # gemmi.__version__ observado em tempo de execução
    "protein_input_id": protein_input_id,
    "raw_checksum": raw_checksum,       # RawArtifact.checksum, reverificado (Seção 11.3)
    "raw_format": raw_format,           # "mmcif" | "pdb", detectado por conteúdo
}
```

`inspection_schema_version` e `inspection_profile_version` são duas versões **distintas e independentes**: a primeira versiona o formato Pydantic do próprio `ReceptorInspectionReport` (mudanças estruturais de schema); a segunda versiona as **regras de negócio** da inspeção (quais códigos CCD contam como metal, qual vocabulário de warnings está em vigor, como a conectividade legada é mapeada) — uma mudança em qualquer uma delas, isoladamente, já é suficiente para produzir um `inspection_id` novo.

### 15.2 Algoritmo de canonicalização

Idêntico, em mecanismo, ao algoritmo `canonicalize_payload`/`compute_semantic_key` já existente em `promotion.py` (Incremento 018) — reaproveitado por disciplina de consistência de engenharia, **nunca pelo mesmo payload ou para o mesmo propósito** (este `inspection_id` nunca é confundido com o `semantic_key` de promoção de ligante, que continua sem equivalente em `ResolvedReceptorSelection`, Seção 23.1):

1. normalizar recursivamente toda string-folha do payload para Unicode NFC;
2. rejeitar qualquer valor `None` no payload (nenhum dos sete campos é opcional — um valor ausente é um erro de construção do chamador, nunca serializado como `null`);
3. serializar via `json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)` — chaves ordenadas alfabeticamente, separadores compactos, não-ASCII preservado, `NaN`/`Infinity` nunca produzidos (nenhum campo do payload é um `float`);
4. codificar o JSON canônico resultante em UTF-8;
5. `inspection_id = hashlib.sha256(canonical_utf8_bytes).hexdigest()` — 64 caracteres hexadecimais em minúsculas.

### 15.3 Vetor golden normativo (verificado)

Payload de exemplo:

```json
{"inspection_profile_version":"1.0","inspection_schema_version":"1.0","parser_name":"gemmi","parser_version":"0.7.5","protein_input_id":"demo-protein","raw_checksum":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","raw_format":"mmcif"}
```

- **Comprimento do JSON canônico:** 254 bytes UTF-8 (verificado programaticamente).
- **`inspection_id` resultante:** `73090f1a141de86e358c79f051b0245df0ca32287425935632e624d15078adf4`
- **Comprimento do `inspection_id`:** 64 caracteres hexadecimais (verificado programaticamente, `len(hashlib.sha256(...).hexdigest()) == 64`).

Este vetor foi computado e verificado com as mesmas primitivas padrão de Python (`json.dumps`, `hashlib.sha256`, `unicodedata.normalize`) descritas na Seção 15.2, antes da escrita deste documento — nunca inventado manualmente. T-122 (Seção 36.2) exige que a implementação real reproduza exatamente este dígito para este payload.

### 15.4 `label_asym_id_is_auth_equivalent` — retirado, substituído por `identity_origin`

O Draft original usava um único campo booleano (`label_asym_id_is_auth_equivalent`) para marcar quando `label_asym_id` era, na verdade, o identificador de autor promovido. Esta revisão retira esse campo e o substitui por um mecanismo mais geral e mais honesto: `identity_origin` (Seção 15.5), aplicado tanto a `label_asym_id` quanto a `label_entity_id`, em `ChainInventoryEntry`, `EntityInventoryEntry` e `NonPolymerComponent`.

Esta substituição é possível, e correta, porque `ResolvedChainSelection` (Seção 22.1) só é produzido quando `selection_capability = "full"` — ou seja, no momento em que uma resolução ocorre, **todo** `label_asym_id` envolvido já tem `identity_origin = "source"` por construção (Seção 15.5/20.4). O campo booleano antigo, aplicado a `ResolvedChainSelection`, seria sempre `False` sob a nova arquitetura — informação morta. Ele é removido de `ResolvedChainSelection` (Seção 22.1) sem perda, e o conceito geral sobrevive, mais forte, apenas nos modelos de inspeção onde é genuinamente informativo.

### 15.5 `IdentityOrigin`

```python
IdentityOrigin = Literal["source", "parser-derived", "unavailable"]
```

- `"source"` — o identificador foi declarado explicitamente pelo formato de origem (ex. `_atom_site.label_asym_id` em mmCIF).
- `"parser-derived"` — **reservado; nunca produzido por este incremento.** Existe no vocabulário para completude e para uma eventual regra de derivação futura que seja segura e explicitamente especificada em uma revisão posterior — este incremento não implementa nenhuma tal regra, porque a única candidata conhecida (`Gemmi.setup_entities()`) é heurística e geométrica, e é explicitamente proibida como fonte de identidade factual (Seção 10.3).
- `"unavailable"` — a fonte não declara o identificador, e nenhuma inferência é feita; o campo correspondente é `None`.

**Regra vinculante:** identidade `"parser-derived"` nunca substitui silenciosamente identidade `"source"` — e, de fato, sob este incremento, `"parser-derived"` nunca é produzida, tornando essa regra uma garantia estrutural, não apenas uma disciplina de implementação.

### 15.6 `selection_capability`

```python
SelectionCapability = Literal["full", "inspection-only"]
```

Computado pelo próprio `inspect_receptor` ao construir o relatório, e persistido como campo de primeira classe em `ReceptorInspectionReport`:

- `"full"` — toda `ChainInventoryEntry`/`EntityInventoryEntry` enumerada tem `label_asym_id_origin = "source"` (para cadeias) e `label_entity_id_origin = "source"` (para entidades). Seleção e resolução são permitidas.
- `"inspection-only"` — pelo menos uma cadeia ou entidade relevante tem `identity_origin` diferente de `"source"` (na prática, sempre `"unavailable"`, já que `"parser-derived"` nunca é produzida). Inspeção funciona plenamente; declaração e resolução de seleção são bloqueadas (Seção 21.4/25.4).

Todo PDB legado tem `selection_capability = "inspection-only"` por construção (Seção 12.5). Um mmCIF que declara `label_asym_id`/`label_entity_id` para todas as suas cadeias/entidades tem `selection_capability = "full"`. Um mmCIF degenerado que omite esses campos para algumas de suas cadeias (um caso raro, mas estruturalmente possível) também recebe `"inspection-only"` — a regra é sobre a presença real do dado, nunca sobre o formato declarado em si.

### 15.7 Avaliação de necessidade de identidade derivada de conteúdo — por que aqui, e não em `ResolvedReceptorSelection`

A Seção 19.1 do Draft original explica, com justificativa que esta revisão preserva integralmente (Seção 23.1), por que `ResolvedReceptorSelection` **não** precisa de uma identidade secundária derivada de conteúdo (`semantic_key`-like): sua identidade autoral (`resolved_selection_id`) já é 1:1 determinística com sua própria política. `ReceptorInspectionReport`, ao contrário, **não tem** identidade autoral alguma — não há cientista declarando um id para ele, e múltiplas chamadas independentes (de `protein inspect`, ou internamente de `declare_receptor_selection`) precisam convergir deterministicamente para o mesmo registro quando o RAW, o parser e o profile são os mesmos. É exatamente esse problema — convergência determinística sem identidade autoral — que o algoritmo de `inspection_id` resolve, e é por isso que a identidade derivada de conteúdo pertence a este objeto, e não a `ResolvedReceptorSelection`.

---

## 16. Inventário Estrutural

Cobertura obrigatória, herdada da Seção 14 do Draft original, com os campos de identidade atualizados para refletir `identity_origin` (Seção 15.5):

| Item exigido | Campo |
|---|---|
| Modelos estruturais presentes | `models: tuple[ModelDescriptor, ...]` |
| Assemblies declarados e expressões de operação (listados, nunca resolvidos) | `assemblies: tuple[AssemblyDescriptor, ...]` |
| Entidades e composição | `entities: tuple[EntityInventoryEntry, ...]` |
| Cadeias, em ambos os espaços de identificadores, com origem rastreável | `chains: tuple[ChainInventoryEntry, ...]` |
| Contagem de resíduos/átomos por cadeia | `ChainInventoryEntry.residue_count`/`atom_count` |
| Altloc presentes | `altloc_observations` |
| Ocupância | `occupancy_observations` (apenas não-trivial, Seção 32.3) |
| Resíduos/átomos não observados | `missing_residues`/`missing_atoms` |
| Pontes dissulfeto e conectividade covalente, com fidelidade completa | `disulfide_bonds`/`covalent_connections`/`metal_coordinations` (agora `tuple[StructureConnection, ...]`, Seção 18) |
| Identificadores CCD | `NonPolymerComponent.ccd_code` |
| Capacidade de seleção da inspeção | `selection_capability` (Seção 15.6) |

Nenhum item desta lista é resolvido, decidido ou materializado pelo 020 — todos são apenas relatados, herdado sem alteração.

### 16.1 `EntityInventoryEntry` (renomeado de `EntityDescriptor`)

```python
EntityType = Literal["polymer", "non-polymer", "macrolide", "water", "branched", "unrecognized"]

class EntityInventoryEntry(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    label_entity_id: Optional[str] = Field(default=None, min_length=1)     # None quando identity_origin != "source"
    label_entity_id_origin: IdentityOrigin
    entity_type: EntityType
    description: Optional[str] = None

    @model_validator(mode="after")
    def _validate_origin_consistency(self):
        # label_entity_id is None iff label_entity_id_origin != "source"
        ...
```

### 16.2 `ChainInventoryEntry` (renomeado de `ChainDescriptor`)

```python
class ChainInventoryEntry(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    label_asym_id: Optional[str] = Field(default=None, min_length=1)      # None quando identity_origin != "source"
    label_asym_id_origin: IdentityOrigin
    auth_asym_id: Optional[str] = None                                     # preservado quando o formato o declara
    label_entity_id: Optional[str] = Field(default=None, min_length=1)
    label_entity_id_origin: IdentityOrigin
    model_number: int = Field(ge=1)
    residue_count: int = Field(ge=0)
    atom_count: int = Field(ge=0)

    @model_validator(mode="after")
    def _validate_origin_consistency(self):
        # label_asym_id is None iff label_asym_id_origin != "source"
        # label_entity_id is None iff label_entity_id_origin != "source"
        ...
```

`label_asym_id_is_auth_equivalent` (Draft original) é retirado deste modelo — substituído por `label_asym_id_origin` (Seção 15.4).

### 16.3 Assemblies, modelos, altloc, ocupância, coordenadas ausentes

Herdados sem alteração de conteúdo da Seção 14 do Draft original — `ModelDescriptor`, `AssemblyDescriptor`, `AssemblyOperationExpression`, `AltlocObservation`, `OccupancyObservation`, `MissingResidueObservation`, `MissingAtomObservation` mantêm exatamente o shape já especificado; nenhum destes foi afetado pelos quatro achados MAJOR.

---

## 17. Inventário Químico

Herdado da Seção 15 do Draft original, com uma correção de precisão (evitando falsos negativos silenciosos na tabela de metais, conforme exigido pela tarefa que originou esta revisão) e identidade de entidade atualizada (Seção 15.5).

### 17.1 Classificação mecânica e segura — refinada

O 020 **não determina função biológica**. A classificação de cada `NonPolymerComponent` deriva exclusivamente de sinais já declarados pelo próprio formato/dicionário químico:

| `classification` | Regra mecânica | `classification_basis` |
|---|---|---|
| `"water"` | `ccd_code` ∈ `{"HOH", "DOD"}` | `"format-declared"` |
| `"metal-ion"` | Entidade não-polimérica, monoatômica (`atom_count == 1`), **e** `ccd_code` pertence à tabela fechada de códigos CCD de íons metálicos monoatômicos | `"closed-dictionary-match"` |
| `"modified-polymer-residue"` | Resíduo ligado a uma entidade polimérica cujo `mon_id` não pertence ao vocabulário padrão de 20 aminoácidos / 5 nucleotídeos | `"format-declared"` |
| `"other-non-polymer"` | Componente **poliatômico** (`atom_count > 1`) não-polimérico que não se encaixa em nenhuma das três categorias acima | `"closed-dictionary-match"` |
| `"unknown"` | **(a)** o próprio parser não determinou `entity_type`/`ccd_code`; **ou (b), novo nesta revisão:** componente **monoatômico** não-polimérico cujo `ccd_code` não está na tabela de metais e não é `"HOH"`/`"DOD"` | `"undetermined"` |

**Correção de precisão (nova nesta revisão):** um componente monoatômico que não corresponde a nenhuma entrada da tabela de metais **nunca** cai em `"other-non-polymer"` — cai em `"unknown"`. A tabela de códigos CCD de íons metálicos (Seção 17.2) é, por declaração explícita, **não exaustiva**; tratá-la como exaustiva produziria um falso negativo silencioso exatamente da forma que a tarefa que originou esta revisão instrui a evitar: um componente monoatômico que *poderia* ser um íon metálico simplesmente não listado seria erroneamente classificado no mesmo balde seguro usado para ligantes/cofatores poliatômicos, obscurecendo a real incerteza. Um componente poliatômico fora das três primeiras categorias, ao contrário, nunca é um íon metálico monoatômico por definição — `"other-non-polymer"` permanece correto e seguro para ele.

Esta distinção preserva integralmente os cenários T-027–T-042 do Draft original (nenhum deles testava um componente monoatômico fora da tabela de metais) e é exercitada por um cenário novo (T-106, Seção 36.1).

### 17.2 Tabela de íons metálicos — explicitamente não exaustiva

A tabela (mantida em `receptor_inspection.py`, versionada como `METAL_ION_CCD_CODES_V1`, participando de `INSPECTION_PROFILE_VERSION` — Seção 15.1) permanece pequena, fechada e baseada em códigos CCD padrão do wwPDB (`ZN`, `MG`, `CA`, `NA`, `K`, `MN`, `FE`, `FE2`, `CU`, `CU1`, `NI`, `CO`, `CD`, `HG`, entre outros). Esta revisão declara explicitamente, por exigência normativa:

- A tabela é **não exaustiva por declaração** — nunca apresentada ou documentada como uma lista completa de todos os íons metálicos possíveis.
- O fallback para qualquer componente monoatômico não listado é **sempre `"unknown"`**, nunca `"other-non-polymer"` (Seção 17.1).
- A tabela **nunca define, por si só, o destino científico de um componente** — ela apenas alimenta uma classificação mecânica; a disposição (manter/remover) permanece exclusivamente uma decisão do cientista (Seção 21), nunca inferida da classificação.
- Uma revisão futura da tabela (`V2`, `V3`, ...) é uma mudança de `INSPECTION_PROFILE_VERSION` (Seção 15.1), produzindo `inspection_id`s novos — nunca uma reinterpretação silenciosa de uma inspeção já persistida (Seção 14.3, regra 10).

### 17.3 `cofactor`/`crystallographic_ligand` — nunca classificações automáticas

Herdado sem alteração da Seção 15.2 do Draft original: estas são etiquetas de papel (`role`) que só existem quando o próprio cientista as declara nomeadamente via `ComponentDisposition.role` (Seção 21.1) — nunca inferidas pelo 020. A declaração do cientista é sempre anotação/política futura, nunca uma reescrita do fato estrutural: `ComponentDisposition`/`ResolvedComponentDisposition.role` nunca alteram `classification`.

### 17.4 `NonPolymerComponent` — identidade atualizada

```python
class NonPolymerComponent(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    label_asym_id: Optional[str] = Field(default=None, min_length=1)
    label_asym_id_origin: IdentityOrigin
    auth_asym_id: Optional[str] = None
    label_entity_id: Optional[str] = Field(default=None, min_length=1)
    label_entity_id_origin: IdentityOrigin
    ccd_code: str = Field(min_length=1, max_length=10)
    atom_count: int = Field(ge=1)
    classification: NonPolymerClassification
    classification_basis: ClassificationBasis

    @model_validator(mode="after")
    def _validate_origin_consistency(self):
        # label_asym_id is None iff label_asym_id_origin != "source"
        # label_entity_id is None iff label_entity_id_origin != "source"
        ...
```

**Correção n-01 desta promoção:** o validador `_validate_origin_consistency` acima é adicionado a `NonPolymerComponent`, replicando literalmente o mesmo padrão já presente em `EntityInventoryEntry` (Seção 16.1) e `ChainInventoryEntry` (Seção 16.2) — os dois modelos estruturalmente análogos, com a mesma obrigação de consistência campo↔origem. Antes desta correção, era possível construir uma instância de `NonPolymerComponent` com um campo presente e sua origem `"unavailable"` (ou vice-versa), uma combinação logicamente inconsistente que os dois modelos análogos já impediam; o validador fecha essa lacuna de contrato sem introduzir nenhuma inferência química nova e sem alterar nenhum comportamento observável do pipeline principal.

### 17.5 Hidrogênios explícitos, cobertura completa, `HETATM` nunca descartável

Herdados sem alteração da Seção 15.3/15.4/15.5 do Draft original — `explicit_hydrogens_present`/`explicit_hydrogen_count` puramente descritivos; `_struct_conn` (e, agora, conectividade legada — Seção 12.3) particionado nos três baldes mecânicos; nenhum componente não-polimérico é removido, transformado ou presumido irrelevante.

### 17.6 Não-assunções reafirmadas

- Água nunca é removível automaticamente.
- pH de cristalização nunca é automaticamente pH biológico/de protonação (Seção 28).
- Ausência de `_struct_conn` nunca é prova de ausência química — é `category-unavailable` (Seção 19.1).
- Solvente/buffer não reconhecido, se poliatômico, permanece `"other-non-polymer"`; se monoatômico e fora da tabela de metais, permanece `"unknown"` (Seção 17.1) — em ambos os casos, nunca classificado com confiança falsa, e nunca removido.

---

## 18. `StructConnEndpoint` e `StructureConnection` (corrige F-03)

### 18.1 `StructConnEndpoint` — completo

Substitui integralmente o modelo de quatro campos do Draft original. Preserva, quando presentes, todos os treze itens exigidos pela tarefa que originou esta revisão:

```python
class StructConnEndpoint(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    label_asym_id: Optional[str] = None
    auth_asym_id: Optional[str] = None
    label_entity_id: Optional[str] = None          # quando aplicável (Seção 15.5)
    label_seq_id: Optional[str] = None              # token bruto, nunca interpretado como int
    auth_seq_id: Optional[str] = None               # token bruto, nunca interpretado como int
    insertion_code: Optional[str] = None
    label_comp_id: Optional[str] = None
    auth_comp_id: Optional[str] = None
    label_atom_id: Optional[str] = None
    auth_atom_id: Optional[str] = None              # quando presente
    label_alt_id: Optional[str] = None              # altloc do parceiro — AUSENTE no Draft original (F-03)
    symmetry: Optional[str] = None                   # operador de simetria — AUSENTE no Draft original (F-03)
    model_number: Optional[int] = Field(default=None, ge=1)   # contexto de modelo, quando disponível
```

Todo campo é `Optional`, por construção — um `StructConnEndpoint` de um registro legado de PDB (`SSBOND`/`LINK`/`CONECT`, Seção 12.3) só popula os campos em espaço de autor; um `StructConnEndpoint` de `_struct_conn` (mmCIF) popula todos os campos que a categoria declarar para aquela linha especificamente, e deixa `None` qualquer campo que a linha não declare — nenhum valor é inventado para preencher um campo ausente (`"campos desconhecidos como unknown, sem inventar valor"`, satisfeito literalmente por `None`, que é a representação Pydantic de "desconhecido/ausente" em todo este domínio).

### 18.2 `StructureConnection` — modelo unificado (substitui `DisulfideBond`/`CovalentConnection`/`MetalCoordination`)

```python
ConnectionCategory = Literal[
    "disulfide", "metal-coordination", "covalent",
    "legacy-pdb-ssbond", "legacy-pdb-link-covalent", "legacy-pdb-link-metal",
    "legacy-pdb-conect-covalent", "legacy-pdb-conect-metal",
]
SourceCategory = Literal["struct_conn", "legacy-pdb-ssbond", "legacy-pdb-link", "legacy-pdb-conect"]

class StructureConnection(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    struct_conn_id: Optional[str] = None            # _struct_conn.id, quando presente
    conn_type: str = Field(min_length=1)             # conn_type_id bruto, preservado literalmente
    category: ConnectionCategory                     # balde mecânico (determina em qual tupla de
                                                       # ReceptorInspectionReport esta conexão aparece)
    source_category: SourceCategory                  # proveniência do registro (Seção 12.3)
    partner_a: StructConnEndpoint
    partner_b: StructConnEndpoint
    distance: Optional[Decimal] = Field(default=None, ge=0)
    value_order: Optional[str] = None                 # pdbx_value_order bruto, quando presente
    role: Optional[str] = None                          # pdbx_role bruto, quando presente
    details: Optional[str] = None
    leaving_atom_flag: Optional[str] = None             # pdbx_leaving_atom_flag bruto, quando presente;
                                                          # ao nível da conexão, nunca inventado por endpoint
                                                          # além do que a categoria declara nesta granularidade
```

- `conn_type` permanece preservado literalmente, exatamente como no Draft original.
- `distance`/`value_order`/`role`/`details`/`leaving_atom_flag` são sempre `None` quando a categoria de origem não os declara — nunca fabricados (T-116).
- `label_alt_id` e `symmetry`, em cada endpoint, são preservados quando `_struct_conn` os declara (T-114, T-115) — a correção central de F-03.

### 18.3 Partição mecânica — preservada e estendida

`ReceptorInspectionReport` mantém exatamente os três campos de tupla já existentes no Draft original, agora tipados por `StructureConnection`:

```python
disulfide_bonds: tuple[StructureConnection, ...]
covalent_connections: tuple[StructureConnection, ...]
metal_coordinations: tuple[StructureConnection, ...]
```

Regra de partição, estendida da Seção 15.4 do Draft original para cobrir também conectividade legada (Seção 12.3):

| `conn_type`/origem | `category` | Tupla de destino |
|---|---|---|
| `_struct_conn.conn_type_id == "disulf"` | `"disulfide"` | `disulfide_bonds` |
| `_struct_conn.conn_type_id == "metalc"` | `"metal-coordination"` | `metal_coordinations` |
| `_struct_conn.conn_type_id` qualquer outro valor não vazio | `"covalent"` | `covalent_connections` |
| `SSBOND` legado | `"legacy-pdb-ssbond"` | `disulfide_bonds` |
| `LINK` legado, nenhum parceiro `"metal-ion"` | `"legacy-pdb-link-covalent"` | `covalent_connections` |
| `LINK` legado, pelo menos um parceiro `"metal-ion"` | `"legacy-pdb-link-metal"` | `metal_coordinations` |
| `CONECT` legado, nenhum parceiro `"metal-ion"` | `"legacy-pdb-conect-covalent"` | `covalent_connections` |
| `CONECT` legado, pelo menos um parceiro `"metal-ion"` | `"legacy-pdb-conect-metal"` | `metal_coordinations` |

`_struct_conn.conn_type_id` ausente/vazio → `StructConnMalformedError` (Seção 31) — nunca silenciosamente descartado, nunca adivinhado.

### 18.4 Nada é descartado

Reafirmado: altloc, simetria, conexão covalente, ponte dissulfeto, coordenação metálica, e a relação com o componente químico correspondente (via `label_comp_id`/`auth_comp_id` em cada endpoint) são todos preservados quando declarados. Nenhuma ligação é inferida geometricamente — apenas as declaradas explicitamente pelo formato (herdado, inalterado).

### 18.5 Ordenação determinística e limites

Ordenação (estende a Seção 30.1 do Draft original, agora Seção 33.1 deste documento): `(partner_a.label_asym_id ou auth_asym_id, partner_a.auth_seq_id, partner_b.label_asym_id ou auth_asym_id, partner_b.auth_seq_id)` — usando `auth_asym_id`/`auth_seq_id` como critério de ordenação de desempate quando `label_*` é `None` (PDB legado), nunca deixando a ordenação indefinida. Limite: o teto de 5.000 warnings (Seção 32.2) é acompanhado por um teto análogo de 50.000 `StructureConnection`s totais por relatório — mesmo comportamento de falha honesta ao exceder (warning `parser-limitation`, enumeração interrompida, nunca truncamento silencioso).

---

## 19. Warnings

### 19.1 Vocabulário — estendido de 14 para 15 códigos (corrige F-10)

```
multiple-models
multiple-assemblies
alternate-locations-present
partial-occupancy-present
missing-residues-reported
missing-atoms-reported
explicit-hydrogens-absent
unknown-chemical-component
covalent-connection-present
metal-coordination-present
legacy-pdb-information-limited
category-unavailable
ambiguous-author-chain-id
parser-limitation
declared-format-mismatch        # NOVO nesta revisão — corrige F-10 (Seção 11.5)
```

O código novo (`declared-format-mismatch`) é a única adição ao vocabulário fechado nesta revisão — adicionada por necessidade normativa direta (T-012 exercitava uma condição real sem warning correspondente), não por expansão arbitrária.

### 19.2 Modelo estruturado — inalterado em shape, campos de assunto reaproveitados

```python
InspectionWarningCode = Literal[
    "multiple-models", "multiple-assemblies", "alternate-locations-present",
    "partial-occupancy-present", "missing-residues-reported", "missing-atoms-reported",
    "explicit-hydrogens-absent", "unknown-chemical-component", "covalent-connection-present",
    "metal-coordination-present", "legacy-pdb-information-limited", "category-unavailable",
    "ambiguous-author-chain-id", "parser-limitation", "declared-format-mismatch",
]

class InspectionWarning(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    code: InspectionWarningCode
    model_number: Optional[int] = None
    label_asym_id: Optional[str] = None
    auth_asym_id: Optional[str] = None
    ccd_code: Optional[str] = None
    category_name: Optional[str] = None
    residue_identifier: Optional[str] = None
    detail: str = Field(min_length=1, max_length=500)
```

`declared-format-mismatch` popula nenhum campo de assunto estrutural (não se refere a uma cadeia/resíduo específico) — apenas `detail`, nomeando o formato declarado e o formato detectado.

### 19.3 Severidade, ordenação, warning nunca é decisão científica

Herdado sem alteração da Seção 16.3/16.4/16.5 do Draft original: nenhum `InspectionWarning` é bloqueante; as únicas condições que impedem uma operação são modeladas como falhas tipadas (Seção 31), nunca como warnings; ordenação e deduplicação especificadas na Seção 33 (Determinismo).

---

## 20. Selection Capability

### 20.1 Definição e cálculo

Já definido em detalhe na Seção 15.6 — repetido aqui, em sua própria seção dedicada, por exigência explícita da tarefa que originou esta revisão:

```python
SelectionCapability = Literal["full", "inspection-only"]
```

`selection_capability` é um campo de primeira classe de `ReceptorInspectionReport`, computado no momento da inspeção, nunca recalculado posteriormente pela política ou pela resolução (ambas apenas leem o valor já persistido, via `inspection_id`).

### 20.2 Consequência para seleção e resolução

| `selection_capability` | `declare_receptor_selection` | `resolve_receptor_selection` |
|---|---|---|
| `"full"` | Procede normalmente (Seção 21) | Procede normalmente (Seção 22) |
| `"inspection-only"` | `InspectionSelectionUnsupportedError` (Seção 31) — nenhuma `ReceptorSelectionPolicy` é persistida | Inalcançável — nenhuma política jamais existe sob uma inspeção `"inspection-only"` |

### 20.3 Nenhum fallback

Reafirmado de forma absoluta: **nenhuma seleção é declarada ou resolvida com identidade de cadeia ambígua ou ausente.** `auth_asym_id` nunca se torna, por si só, um seletor válido (Seção 12.2) — mesmo sob `"inspection-only"`, onde seria o único identificador disponível, a resposta é recusar a operação inteira, nunca degradar silenciosamente o critério de seleção.

### 20.4 Por que isso é seguro sob `ResolvedChainSelection`

Como `declare_receptor_selection` já recusa qualquer inspeção `"inspection-only"` antes de construir qualquer `ReceptorSelectionPolicy`, e `resolve_receptor_selection` só opera sobre políticas já persistidas, **toda** `ResolvedChainSelection` existente no sistema é, por construção, produto de uma inspeção `"full"` — esta é a garantia estrutural que permite a simplificação da Seção 15.4 (remoção de `label_asym_id_is_auth_equivalent` de `ResolvedChainSelection`).

---

## 21. ReceptorSelectionPolicy

### 21.1 Submodelos — inalterados

```python
class ChainSelector(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    label_asym_id: str = Field(min_length=1, max_length=10)   # identidade canônica, sempre obrigatória
    auth_asym_id: Optional[str] = Field(default=None, max_length=10)   # preservado, nunca o único seletor

ComponentRole = Literal["cofactor", "crystallographic_ligand"]
Disposition = Literal["keep", "remove"]

class ComponentDisposition(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    label_asym_id: str = Field(min_length=1, max_length=10)
    ccd_code: str = Field(min_length=1, max_length=10)
    role: ComponentRole
    disposition: Disposition
```

`ChainSelector.label_asym_id` permanece obrigatório (`str`, não `Optional`) — isso é intencional e correto mesmo após a introdução de `identity_origin`: uma política só é construída quando `selection_capability = "full"`, momento em que `label_asym_id` já existe com `identity_origin = "source"` para toda cadeia relevante; não há cenário em que uma política precise declarar um `label_asym_id` ausente.

### 21.2 Modelo principal — campos novos (corrige F-04, fecha a janela declaração-resolução)

```python
ReceptorSelectionPolicySchemaVersion = Literal["1.0"]

class ReceptorSelectionPolicy(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    schema_version: ReceptorSelectionPolicySchemaVersion
    selection_id: str = Field(min_length=1)
    protein_input_id: str = Field(min_length=1)
    inspection_id: str = Field(min_length=64, max_length=64)       # NOVO — referência obrigatória
    raw_checksum_observed: str = Field(min_length=64, max_length=64)   # NOVO — checksum no momento da declaração
    selected_model: Optional[int] = Field(default=None, ge=1)
    selected_assembly: Optional[str] = Field(default=None, min_length=1, max_length=50)
    selected_chains: tuple[ChainSelector, ...] = ()
    water_disposition: Optional[Disposition] = None
    metal_disposition: Optional[Disposition] = None
    component_dispositions: tuple[ComponentDisposition, ...] = ()
    declared_by: str = Field(min_length=1, max_length=200)
    label: Optional[str] = Field(default=None, max_length=200)
    rationale: Optional[str] = Field(default=None, max_length=4000)
    declared_at: datetime

    @field_validator("selection_id", "protein_input_id")
    @classmethod
    def _validate_id_format(cls, value): return validate_input_id(value)

    @field_validator("inspection_id", "raw_checksum_observed")
    @classmethod
    def _validate_hex64_format(cls, value):
        # 64 caracteres hexadecimais em minúsculas — mesmo padrão de validate_semantic_key (promotion.py),
        # reaproveitado por disciplina, nunca confundido com semantic_key em si (Seção 23.1)
        ...

    @field_validator("declared_by")
    @classmethod
    def _validate_declared_by_not_blank(cls, value): ...

    @field_validator("label", "rationale")
    @classmethod
    def _validate_not_blank_when_present(cls, value): ...

    @field_validator("declared_at")
    @classmethod
    def _validate_timezone_aware(cls, value): ...

    @model_validator(mode="after")
    def _validate_no_duplicate_chains(self):
        # nenhum label_asym_id duplicado em selected_chains

    @model_validator(mode="after")
    def _validate_no_duplicate_component_dispositions(self):
        # nenhum par (label_asym_id, ccd_code) duplicado em component_dispositions
```

`inspection_id` e `raw_checksum_observed` são **sempre** preenchidos pela Application Service (Seção 25.2), nunca aceitos de um chamador livre — `declare_receptor_selection` invoca `inspect_receptor` internamente (create-or-reuse) antes de construir o candidato, e copia o `inspection_id`/`raw_checksum` do resultado factual dessa chamada. Nenhum caminho permite a um cientista declarar manualmente um `inspection_id` arbitrário.

### 21.3 Decisões explícitas sobre campos não incluídos — herdadas

- **Nenhum `altloc_policy`.** Inalterado (Seção 17.3 do Draft original).
- **Nenhum `cofactor_policy`/`crystallographic_ligand_policy` de balde.** Inalterado — `component_dispositions` nomeado por componente permanece o mecanismo.
- **Nenhum `supersedes_id`/mecanismo de revisão.** Inalterado.

### 21.4 Regras de seleção de cadeia — reforçadas

- `label_asym_id` é sempre a identidade canônica e obrigatória; `auth_asym_id` é preservado quando o cientista o fornece, mas nunca é, por si só, um seletor válido.
- **Nova nesta revisão:** `declare_receptor_selection` verifica `selection_capability` do `inspection_id` resultante **antes** de validar qualquer campo de `selected_chains`/`component_dispositions` — uma tentativa de declarar contra uma inspeção `"inspection-only"` falha com `InspectionSelectionUnsupportedError` (Seção 31) antes mesmo de a sintaxe da seleção de cadeia ser examinada.
- Nenhuma conversão automática entre espaços de identificador é feita na política — a reconciliação completa ocorre exclusivamente na resolução (Seção 22).

---

## 22. ResolvedReceptorSelection

### 22.1 Submodelos — `ResolvedChainSelection` simplificado (corrige F-04, decorrência de F-01)

```python
class ResolvedChainSelection(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    label_asym_id: str              # sempre presente — toda resolução ocorre sob selection_capability="full"
    auth_asym_id: Optional[str]
    label_entity_id: str             # sempre presente, pela mesma razão
    model_number: int

# label_asym_id_is_auth_equivalent RETIRADO (Seção 15.4) — campo morto sob a nova arquitetura

DispositionSource = Literal["water_disposition", "metal_disposition", "component_dispositions"]

class ResolvedComponentDisposition(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    label_asym_id: str
    ccd_code: str
    classification: NonPolymerClassification
    disposition: Optional[Disposition] = None
    disposition_source: Optional[DispositionSource] = None
```

### 22.2 Modelo principal — não embute mais o relatório completo (corrige F-04)

```python
ResolvedReceptorSelectionSchemaVersion = Literal["1.0"]

class ResolvedReceptorSelection(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    schema_version: ResolvedReceptorSelectionSchemaVersion
    resolved_selection_id: str            # self-identidade; sempre == policy_selection_id
    policy_selection_id: str              # referência explícita a ReceptorSelectionPolicy.selection_id
    protein_input_id: str
    inspection_id: str = Field(min_length=64, max_length=64)   # NOVO — referência, nunca embute o relatório
    raw_checksum: str                      # pequeno campo essencial, redundante por auditabilidade direta
    structure_format: StructureFormat      # idem
    parser: ParserProvenance                # idem — pequeno, nunca o inventário completo
    resolved_model: int
    model_resolution_basis: ModelResolutionBasis
    resolved_assembly: Optional[str] = None
    resolved_chains: tuple[ResolvedChainSelection, ...]
    resolved_component_dispositions: tuple[ResolvedComponentDisposition, ...]
    resolved_at: datetime

    # inspection_snapshot: ReceptorInspectionReport  — REMOVIDO (Draft original, Seção 18.2) — corrige F-04

    @model_validator(mode="after")
    def _validate_internal_consistency(self):
        # resolved_selection_id == policy_selection_id
        # nenhum label_asym_id duplicado em resolved_chains
        # (consistência contra o relatório referenciado é responsabilidade do Service — Seção 25.3,
        #  nunca mais um cross-check contra um campo embutido que não existe mais neste modelo)
```

`resolved_chains`/`resolved_component_dispositions` permanecem o **subconjunto resolvido necessário** — já bounded pela seleção do cientista (nunca o inventário inteiro), satisfazendo literalmente a regra 5 da Seção 14.3. `inspection_id`, `raw_checksum`, `structure_format`, `parser` são os únicos campos de proveniência "essenciais" copiados por conveniência de auditoria direta — nenhum deles se aproxima, em tamanho, do inventário completo que o Draft original embutia.

### 22.3 O que o objeto prova — atualizado

- **O que foi pedido** — via `policy_selection_id`.
- **Contra qual RAW** — `raw_checksum` + `protein_input_id`.
- **Contra qual inspeção** — `inspection_id` (novo; permite a qualquer consumidor, incluindo o 021, carregar o relatório completo por referência, nunca por cópia).
- **O que foi encontrado** — `resolved_model`, `resolved_assembly`, `resolved_chains`, `resolved_component_dispositions`.
- **Quais ambiguidades permaneceram** — carregando o `ReceptorInspectionReport` persistido via `inspection_id` e lendo `warnings` ali (nunca mais um campo embutido neste objeto).
- **Que nenhuma coordenada foi modificada** — por construção, reafirmado (Seção 7).

### 22.4 Nenhum representation path de estrutura derivada

Reafirmado, confirmado por inspeção do schema acima: nenhum campo nomeia um arquivo de saída.

---

## 23. Identidade e Idempotência

### 23.1 Tabela de identidade — atualizada

| Objeto | Identidade | Mecanismo |
|---|---|---|
| `ProteinInput` | `input_id` (autoral) + `RawArtifact.checksum` | Já existente, não tocado |
| `ReceptorInspectionReport` | `inspection_id` — **derivado de conteúdo, determinístico** (Seção 15) | **Create-once** (corrige F-04; não é mais um cache opcional) |
| `ReceptorSelectionPolicy` | `selection_id` (autoral, escolhido pelo cientista) | Create-once, `validate_input_id` |
| `ResolvedReceptorSelection` | `resolved_selection_id` (sempre == `policy_selection_id`) | Create-once, 1:1 com a política |

**Nenhum `semantic_key` em `ResolvedReceptorSelection` — decisão preservada sem alteração.** O argumento da Seção 19.1 do Draft original permanece integralmente válido e é explicitamente reconfirmado aqui (Seção 43, N-02): `ResolvedReceptorSelection` é, por construção, 1:1 determinística com sua própria política; não há duas identidades autorais independentes que precisem convergir, então uma identidade derivada de conteúdo no estilo `semantic_key` continua sem propósito real para este objeto específico. **O `inspection_id` introduzido por esta revisão não é esse `semantic_key`** — resolve um problema estrutural diferente (convergência determinística de um objeto sem identidade autoral alguma, Seção 15.7), e aplica-se a `ReceptorInspectionReport`, nunca a `ResolvedReceptorSelection`.

### 23.2 Comparação de retry, timestamps, normalização — herdado, com uma adição

- `declared_at`/`resolved_at` permanecem excluídos de qualquer comparação de retry-vs-conflito. `inspected_at` é retirado como campo independente — a "data de inspeção" deixa de ser um campo solto do relatório sem papel na identidade e passa a ser, implicitamente, o momento de criação do registro persistido (metadado de arquivo/registro, nunca parte do payload canônico de identidade, Seção 15.1).
- Versão do parser e versão do profile **participam diretamente** da identidade de `ReceptorInspectionReport` (Seção 15.1) — não apenas "são comparadas na resolução" como no Draft original, mas são literalmente parte do hash.
- Identificadores mmCIF permanecem comparados case-sensitive, nunca casefold-normalizados — distinto da normalização casefold de `check_storage_identity_conflict`, que é uma regra de camada de armazenamento, nunca de identidade científica.

### 23.3 Retry — tabela completa por operação

| Operação | Retry idêntico | Divergência |
|---|---|---|
| `inspect_receptor` (mesmo payload de inspeção) | `reused=True`, nenhuma reescrita (T-125) | — (um payload diferente produz um `inspection_id` diferente, nunca uma divergência sob o mesmo id — Seção 15.1 torna "o mesmo id com conteúdo diferente" estruturalmente impossível) |
| `inspect_receptor`, parser/version diferente | Produz um **novo** `inspection_id`; `created=True` sob esse novo id; o antigo permanece intacto (T-128) | Não aplicável — nunca é tratado como retry do id antigo |
| `inspect_receptor`, `raw_checksum` diferente | Produz um **novo** `inspection_id` (T-127) | Idem |
| `inspect_receptor`, `inspection_profile_version` diferente | Produz um **novo** `inspection_id` (T-129) | Idem |
| `declare_receptor_selection` (`selection_id` add) | Retry idêntico (todos os campos comparados, excluindo `declared_at`) → `reused=True` | Conteúdo divergente sob o mesmo `selection_id` → `ReceptorSelectionConflictError` |
| `resolve_receptor_selection` (`selection_id` resolve) | Retry idêntico → `reused=True`, nenhuma reescrita | Relatório referenciado corrompido → `ReceptorInspectionRecordInvalidError`; RAW alterado → `RawChecksumMismatchError` |
| `load_receptor_selection`/`load_resolved_receptor_selection`/`load_receptor_inspection` | Leitura pura, sempre idempotente, nunca escreve | Registro inexistente → `*NotFoundError`; corrompido → `*RecordInvalidError` |
| `list_receptor_selections` | Leitura pura, ordenação determinística `(declared_at, selection_id)` | — |

**Nenhum uso de "latest" em nenhuma linha desta tabela** — toda convergência é determinística (mesmo payload → mesmo id) ou é, por definição, um registro novo e independente, nunca uma substituição do mais recente.

---

## 24. Persistência

### 24.1 Layout exato

```
project_dir/
  scientific/
    receptor_inspections/
      <inspection_id>.yaml                  # ReceptorInspectionReport, create-once, identidade determinística
    receptor_selections/
      <selection_id>.yaml                    # ReceptorSelectionPolicy, create-once, identidade autoral
      resolved/
        <selection_id>.yaml                  # ResolvedReceptorSelection, create-once, 1:1 com a política
```

Nenhum diretório `inputs/receptor` é usado ou modificado por este incremento — herdado sem alteração (Seção 21.1 do Draft original).

### 24.2 Mecanismo — `receptor_inspections/` atualizado para create-once real

- **`receptor_inspections/<inspection_id>.yaml`**: escrita via `atomic_write_text`, agora guardada por `check_storage_identity_conflict` (casefold-normalizado, mesmo primitivo de `conditions_registry.register_conditions_declaration`) — levanta `ReceptorInspectionIdentityConflictError` (subclasse de `FileExistsError`) em colisão. Diferente do cache por conteúdo do Draft original, que apenas verificava existência informalmente: este é agora um registro create-once de primeira classe, com a mesma disciplina de identidade de armazenamento de todo o resto do repositório. Uma colisão aqui só pode significar, na prática, o `inspection_id` já existente para o mesmo payload (visto que o nome do arquivo é o próprio hash do conteúdo) — tratado por `inspect_receptor` como *hit* de create-once (`reused=True`), nunca como erro, exceto na janela TOCTOU residual já aceita (Seção 24.3).
- **`receptor_selections/<selection_id>.yaml`**: inalterado — `ReceptorSelectionIdentityConflictError`.
- **`receptor_selections/resolved/<selection_id>.yaml`**: inalterado — `ReceptorResolutionIdentityConflictError`.
- **Nenhum estágio de staging** em nenhum dos três caminhos — inalterado, mesma justificativa (documento YAML estrutural único, sem artefato binário externo).
- **Leitura tipada**: `yaml.safe_load` + `Model.model_validate(data)`, com `yaml.YAMLError`/`pydantic.ValidationError` traduzidos para o `*RecordInvalidError` correspondente, `__cause__` preservado — agora também aplicado a `receptor_inspections/` (`ReceptorInspectionRecordInvalidError`, novo).
- **Ordenação determinística de listagem**: inalterada para `list_receptor_selections`.
- **Corrupção distinta de ausência**: estendida a `receptor_inspections/` — arquivo inexistente → `ReceptorInspectionNotFoundError`; presente mas ilegível/inválido → `ReceptorInspectionRecordInvalidError`.
- **Sem banco de dados** — inalterado.

### 24.3 Concorrência cross-process — inalterado, agora explicitamente estendido a inspeções

A mesma renúncia de concorrência da Seção 21.3 do Draft original se aplica igualmente a `receptor_inspections/`: cada um dos três primitivos de persistência é usado por um único processo por vez; nenhum deles escreve um artefato binário externo que exigiria o protocolo pesado do Incremento 018. A janela TOCTOU residual entre a verificação de existência e a escrita é a mesma já aceita em todo o repositório — e, para `receptor_inspections/` especificamente, é ainda menos consequente do que para os outros dois, porque duas escritas concorrentes do mesmo `inspection_id` produziriam, por determinismo (Seção 33), conteúdo byte-idêntico (exceto por nenhum campo variável remanescente — `inspected_at` foi retirado como campo de payload, Seção 23.2).

---

## 25. Application Service

### 25.1 Funções públicas — sete funções (adiciona `load_receptor_inspection`)

```python
def inspect_receptor(
    project_dir: Path, *, protein_input_id: str
) -> ReceptorInspectionOutcome:          # dataclass frozen: report, created: bool
    ...

def load_receptor_inspection(
    project_dir: Path, inspection_id: str
) -> ReceptorInspectionReport: ...

def declare_receptor_selection(
    project_dir: Path, *, selection_id: str, protein_input_id: str,
    selected_model: Optional[int], selected_assembly: Optional[str],
    selected_chains: tuple[ChainSelector, ...],
    water_disposition: Optional[Disposition], metal_disposition: Optional[Disposition],
    component_dispositions: tuple[ComponentDisposition, ...],
    declared_by: str, label: Optional[str], rationale: Optional[str],
) -> ReceptorSelectionOutcome:            # dataclass frozen: policy, reused: bool
    ...

def resolve_receptor_selection(
    project_dir: Path, *, selection_id: str
) -> ReceptorResolutionOutcome:           # dataclass frozen: resolution, reused: bool
    ...

def load_receptor_selection(project_dir: Path, selection_id: str) -> ReceptorSelectionPolicy: ...
def load_resolved_receptor_selection(project_dir: Path, selection_id: str) -> ResolvedReceptorSelection: ...
def list_receptor_selections(project_dir: Path) -> tuple[ReceptorSelectionPolicy, ...]: ...
```

`list_receptor_inspections` **não** é adicionada — decisão explícita de manter a menor superfície suficiente (Seção 29.1 explica a mesma decisão para a CLI correspondente); um `inspection_id` só é útil quando já conhecido (via uma política que o referencia, ou via o resultado direto de `inspect_receptor`), e listar todas as inspeções persistidas para um `protein_input_id` não tem um caso de uso concreto identificado nesta fase.

### 25.2 `inspect_receptor` — redesenhado (corrige F-04)

1. valida `protein_input_id` via `validate_input_id`;
2. carrega o `ProteinInput` (propaga `ReceptorInputNotFoundError`/`ReceptorInputRecordInvalidError` — corrige F-07, Seção 31);
3. executa o fluxo seguro de leitura do RAW (Seção 11.3) — rejeita compressão, verifica tamanho, calcula checksum;
4. captura `gemmi.__version__`;
5. computa `inspection_id` (Seção 15.1-15.2) a partir de `(INSPECTION_SCHEMA_VERSION, INSPECTION_PROFILE_VERSION, "gemmi", gemmi.__version__, protein_input_id, raw_checksum, raw_format)`;
6. verifica se `receptor_inspections/<inspection_id>.yaml` já existe — se sim, carrega, retorna `created=False`;
7. se não existe: invoca `receptor_parsing.parse_receptor_raw` sobre o caminho já validado (Seção 10.5), constrói o `ReceptorInspectionReport` completo (incluindo `selection_capability`, Seção 15.6), persiste-o create-once, retorna `created=True`;
8. loga atividade best-effort (Seção 29) com o resultado factual de `created`.

### 25.3 `declare_receptor_selection` — invoca `inspect_receptor` internamente

1. valida `selection_id`/`protein_input_id` antes de qualquer I/O;
2. invoca `inspect_receptor` internamente (create-or-reuse) — nunca reimplementa esse fluxo separadamente;
3. verifica `selection_capability` do resultado — `"inspection-only"` → `InspectionSelectionUnsupportedError`, nenhuma política construída (Seção 21.4);
4. constrói o candidato `ReceptorSelectionPolicy`, preenchendo `inspection_id`/`raw_checksum_observed` a partir do resultado do passo 2 — nunca de um valor fornecido pelo chamador;
5. tenta persistir create-once; em conflito de identidade, compara campos (excluindo `declared_at`) e decide reused-vs-`ReceptorSelectionConflictError`;
6. loga atividade best-effort.

### 25.4 `resolve_receptor_selection` — redesenhado (corrige F-04, fecha a janela)

1. carrega a `ReceptorSelectionPolicy` pelo `selection_id` (propaga `ReceptorSelectionNotFoundError`/`ReceptorSelectionRecordInvalidError`);
2. carrega o `ReceptorInspectionReport` pelo **exato** `inspection_id` pinado na política (`load_receptor_inspection`) — nunca recalcula, nunca substitui por uma inspeção mais nova; ausente → `ReceptorInspectionNotFoundError`; corrompido → `ReceptorInspectionRecordInvalidError`;
3. revalida o checksum **atual** do RAW contra `raw_checksum` já registrado no relatório carregado — divergência → `RawChecksumMismatchError`, nenhuma resolução persistida;
4. resolve cada identificador declarado (`selected_model`/`selected_assembly`/`selected_chains`/disposições) contra o inventário do relatório carregado — mesmas regras de borda da Seção 25.5;
5. se tudo confirmado: constrói e persiste `ResolvedReceptorSelection` (referenciando `inspection_id`, nunca embutindo o relatório), `reused=False`; se já existe um registro para este `selection_id`: compara e decide reused-vs-falha (Seção 23.3);
6. se qualquer identificador não for confirmado: nenhuma persistência ocorre, erro tipado específico é levantado (Seção 31) — tudo-ou-nada, reafirmado;
7. loga atividade best-effort.

**Eliminação de `ReceptorResolutionParserVersionConflictError`:** como toda resolução está permanentemente fixada ao `inspection_id` gravado na política no momento da declaração, não há mais nenhum cenário de "retry sob uma versão de parser diferente" — esse cenário inteiro deixa de existir por construção. A classe é retirada da taxonomia (Seção 31); seu papel é inteiramente absorvido pela arquitetura de pinagem de `inspection_id`.

### 25.5 Regras de resolução (edge cases) — herdadas, uma linha removida

| Condição | Comportamento |
|---|---|
| `selected_model=None`, relatório com exatamente 1 modelo | Resolvido transparentemente; `model_resolution_basis="only-model-present"` |
| `selected_model=None`, relatório com >1 modelo | `AmbiguousModelSelectionError` |
| `selected_model` declarado, ausente do relatório | `ModelNotFoundError` |
| `selected_assembly=None` | Sempre legal; `resolved_assembly=None` |
| `selected_assembly` declarado, ausente do relatório | `AssemblyNotFoundError` |
| `selected_chains=()` | Sempre legal; `resolved_chains=()` |
| Cadeia declarada ausente do modelo resolvido | `ChainNotFoundError` — tudo-ou-nada |
| Cadeia fora do assembly declarado | Não verificado (decisão explícita, inalterada) |
| Múltiplas cadeias declaradas | Suportado, ordem canônica |
| `auth_asym_id` ambíguo | Warning no relatório; nunca bloqueia resolução |

*(Linha removida: "PDB legado → `label_asym_id_is_auth_equivalent=True`" — inalcançável sob a nova arquitetura, porque PDB legado nunca atinge `resolve_receptor_selection` — Seção 20.)*

---

## 26. Attempts

### 26.1 Confirmação vinculante, reavaliada à luz de F-04

**Nenhuma máquina de attempts nova é criada — confirmado, agora explicitamente reavaliado contra a persistência create-once do relatório de inspeção.** Persistir `ReceptorInspectionReport` como registro create-once (Seção 14) não introduz uma máquina de estados: é um registro simples, sem transições, sem fases `resolution`/`execution`, exatamente no mesmo espírito do padrão já validado por `ScientificConditionsDeclaration` — a única diferença sendo identidade derivada de conteúdo em vez de autoral (Seção 15.7), o que não introduz estado algum, apenas uma regra de nomeação de arquivo determinística.

- Inspeção, agora persistida, continua sendo o resultado de uma função pura (RAW, parser, profile) → relatório — a persistência é um efeito colateral de create-once sobre esse resultado puro, não uma fase adicional de um processo com estado.
- Declaração permanece um registro create-once simples.
- Resolução permanece uma função determinística → sucesso-ou-falha, agora mais simples (Seção 25.4) por não precisar mais considerar divergência de versão de parser como um caso de retry.

`ExecutionAttempt` permanece hard-coded para `TautomerEnumerationPolicy`, não tocado. `LigandPromotionAttempt` não é reutilizado semanticamente — inalterado.

---

## 27. Lineage

### 27.1 Cadeia de referências explícitas — atualizada

```
ProteinInput (input_id, RawArtifact.checksum)
  → ReceptorInspectionReport (inspection_id)                [persistido, create-once — corrige F-04]
  → ReceptorSelectionPolicy (selection_id, protein_input_id, inspection_id, raw_checksum_observed)
  → ResolvedReceptorSelection (resolved_selection_id == policy_selection_id, inspection_id, raw_checksum)
```

Lineage é agora preservado por referência explícita entre **quatro** objetos (antes, três — o relatório de inspeção entra formalmente na cadeia de lineage, porque agora tem identidade própria e persistida).

### 27.2 Nenhum `StateTransformationRecord`

Confirmado, sem alteração: inspeção não é transformação; declaração de seleção não é transformação; resolução lógica não é transformação química. O vocabulário fechado `Literal["protonation", "tautomerization"]` de `transformation.py` não é ampliado.

---

## 28. ExperimentalConditions

### 28.1 Integração — decisão mínima, preservada

**`ReceptorSelectionPolicy` não referencia `ScientificConditionsDeclaration`.** Inalterado da Seção 25.1 do Draft original — nenhum acoplamento obrigatório com `conditions_id` é introduzido por esta revisão. A justificativa original permanece válida sem alteração: um campo não-operante adicionaria superfície de schema sem benefício observável nesta fase; quando um incremento futuro precisar cruzar seleção de receptor com condições experimentais, isso é expresso por referência explícita naquele incremento, sem exigir mudança retroativa no `schema_version="1.0"` deste.

### 28.2 Fronteiras preservadas, sem alteração

- pH de cristalização permanece **Evidence**, nunca uma `ScientificPolicy`.
- Nenhuma promoção automática de pH de cristalização para pH de protonação.
- Nenhuma inferência de pH. Nenhum default pH 7, em lugar nenhum. Nenhuma protonação no 020.
- `ScientificConditionsDeclaration.purpose` permanece fixo em `Literal["simulation_input"]`, não tocado.
- Ausência de uma condição declarada nunca gera um valor científico — herdado, reafirmado.

---

## 29. CLI

### 29.1 Comandos — sete comandos (adiciona `receptor inspection show`)

```
molecular protein inspect <experiment> <protein-input-id>

molecular receptor inspection show <experiment> <inspection-id>

molecular receptor select <experiment> <selection-id> \
    --source <protein-input-id> \
    [--model <int>] [--assembly <str>] \
    [--chain <label>[:<auth>]] ...                      (repetível) \
    [--water keep|remove] [--metal keep|remove] \
    [--component <ccd>:<label>:cofactor|crystallographic_ligand:keep|remove] ...  (repetível) \
    --declared-by <str> [--label <str>] [--rationale <str>]

molecular receptor resolve <experiment> <selection-id>

molecular receptor show-selection <experiment> <selection-id>
molecular receptor show-resolution <experiment> <selection-id>
molecular receptor list-selections <experiment> [--source <protein-input-id>]
```

`receptor inspection show` é **novo** nesta revisão — necessário porque, com a inspeção agora persistida e referenciada por `inspection_id`, um cientista/operador precisa de uma via direta para carregar uma inspeção específica (por exemplo, a referenciada por uma política antiga) sem depender de `protein inspect` recalcular/reutilizar a inspeção **atual**, que pode já ser outra sob um parser atualizado (Seção 23.3). `receptor inspection list` **não** é adicionado — decisão explícita (Seção 25.1) de manter a menor superfície suficiente.

`protein inspect` permanece no `protein_app` já existente; os seis comandos `receptor *` permanecem/entram em `receptor_app`.

### 29.2 Sintaxe das opções repetíveis — inalterada

Herdado sem alteração da Seção 26.2 do Draft original.

### 29.3 Banners, exit codes, redaction — tabela atualizada

| Banner | Condição | Exit code |
|---|---|---|
| `INPUT ERROR` | id malformado; sintaxe de `--chain`/`--component` inválida; `ReceptorSelectionValidationError` | 1 |
| `NOT FOUND` | `ReceptorInputNotFoundError`; `ReceptorInspectionNotFoundError`; `ReceptorSelectionNotFoundError`; `ReceptorResolutionNotFoundError` | 1 |
| `RECORD INVALID` | `ReceptorInputRecordInvalidError`; `ReceptorInspectionRecordInvalidError`; `ReceptorSelectionRecordInvalidError`; `ReceptorResolutionRecordInvalidError` | 1 |
| `CONFLICT` | `ReceptorSelectionConflictError` | 1 |
| `PARSE ERROR` | `ReceptorParseFailureError`; `UnsupportedStructureFormatError`; `StructConnMalformedError`; `InspectionFailureError` | 1 |
| `COMPRESSED INPUT REJECTED` *(novo)* | `CompressedExtensionRejectedError`; `CompressedRawContentError` | 1 |
| `SELECTION UNSUPPORTED` *(novo)* | `InspectionSelectionUnsupportedError` | 1 |
| `CHECKSUM MISMATCH` | `RawChecksumMismatchError` | 1 |
| `SIZE LIMIT EXCEEDED` *(novo)* | `RawArtifactTooLargeError` | 1 |
| `RESOLUTION FAILED` | `ModelNotFoundError`; `AmbiguousModelSelectionError`; `AssemblyNotFoundError`; `ChainNotFoundError` | 1 |
| `STORAGE ERROR` | `ReceptorPersistenceError`; `RawArtifactUnavailableError`; qualquer `OSError` inesperado | 1 |

`ReceptorResolutionParserVersionConflictError` removida da tabela (classe eliminada, Seção 25.4). Todas as três classes que a Adversarial Review encontrou sem banner mapeado (F-06: `RawArtifactTooLargeError`, `RawArtifactUnavailableError`, `InspectionFailureError`) agora têm linha explícita — `InspectionFailureError` cai sob `PARSE ERROR` (é, por definição, uma falha inesperada após um parse bem-sucedido, tratada com a mesma severidade de uma falha de parsing).

Toda mensagem de erro passa por `_sanitize_cli_error_text`, herdado sem alteração. Sucesso sempre inclui, agora, `inspection_id` e `selection_capability` no corpo da saída (Seção 29.4).

**Contrato normativo completo de `InspectionFailureError` (corrige F-06 — correção mecânica desta versão):** a Short Adversarial Review (`08-revised-draft-review`, m-01) encontrou esta classe ausente da linha `PARSE ERROR` da tabela acima, apesar de a prosa imediatamente seguinte já afirmar o mapeamento; a linha já corrigida acima inclui `InspectionFailureError` explicitamente, fechando essa lacuna. Por disciplina de completude normativa, o contrato completo — seguindo exatamente o mesmo padrão já aplicado a toda outra classe desta taxonomia — é:

- **Classe capturada:** `InspectionFailureError` (Seção 30.1 — base `RuntimeError`, camada `receptor_inspection.py`/Service, `__cause__` preservado).
- **Banner exibido:** `PARSE ERROR`.
- **Exit code:** `1`.
- **Mensagem exibida:** sempre sanitizada via `_sanitize_cli_error_text` — nunca o texto cru da exceção original, nunca um traceback Python (regra geral desta seção, aplicada sem excepcionalidade a esta classe).
- **Caminho absoluto:** nunca aparece na mensagem (Seção 30.1, regra geral reafirmada aqui para esta classe especificamente).
- **`KeyboardInterrupt`/`SystemExit`:** nunca são capturados por este ou por nenhum outro bloco de tradução (Seção 10.3) — uma interrupção de processo durante uma operação que poderia levantar `InspectionFailureError` sempre propaga sem modificação, nunca é traduzida para esta classe.
- **Registro falso de sucesso:** estruturalmente impossível — a CLI só emite o banner de sucesso (Seção 29.4) após a chamada à Application Service retornar sem exceção (Seção 25.2, tudo-ou-nada); levantar `InspectionFailureError` impede, por construção, qualquer saída de sucesso para a mesma invocação.

### 29.4 Saída de sucesso — campos obrigatórios (corrige F-06, F-07, e atende à exigência desta revisão)

Toda saída de sucesso de `protein inspect`, `receptor select` e `receptor resolve` inclui explicitamente:

- `created`/`reused` (nunca inferido pelo leitor a partir de um timestamp);
- `inspection_id`;
- `parser` (nome e versão);
- `raw_checksum`;
- `selection_capability`;
- `warnings` (lista, possivelmente vazia);
- um inventário resumido (contagem de modelos/cadeias/entidades/componentes, nunca o inventário completo linha a linha).

**Nenhuma opção de visualização detalhada é adicionada** — decisão explícita: o inventário completo já está disponível, estruturado, via `receptor inspection show <inspection-id>` (saída YAML completa do relatório persistido); duplicar esse detalhe dentro do banner de sucesso de `protein inspect` não tem benefício adicional identificado nesta fase.

### 29.5 Garantias gerais — herdadas

Nenhuma interação durante a execução de qualquer comando. Nenhum comando escolhe um valor pelo cientista. Retry reutilizado é sempre anunciado explicitamente, nunca indistinguível de uma criação nova.

### 29.6 Propriedade dos eventos de activity logging — regra normativa explícita (corrige F-09 — correção mecânica desta versão)

A Adversarial Review original (`06-draft-review`, F-09) identificou como indefinido o comportamento de logging para falhas de sintaxe de `--chain`/`--component` ocorridas antes de qualquer chamada à Application Service. O Revised Draft (`07-revised-draft-specification`) já formulava a decisão corretamente na Seção 42 (tabela de reconciliação), mas a Short Adversarial Review (`08-revised-draft-review`, m-03) encontrou que esta Seção 29 — o local que a própria tabela citava como destino ("incorporada ao comportamento geral dos comandos") — não continha de fato esse texto em nenhuma de suas subseções. Esta subseção transcreve a decisão para o local normativo correto, sem alterar nenhum comportamento técnico já especificado:

- **O Application Service é o único proprietário dos eventos operacionais `started`/`succeeded`/`error`** de `inspect_receptor`/`declare_receptor_selection`/`resolve_receptor_selection` (Seção 31.1) — a CLI nunca registra uma segunda entrada para um evento que o Service já registra (Seção 31.2, "Nenhum duplo log entre CLI e Service").
- **A CLI apenas apresenta ao usuário o resultado já produzido pelo Service** — banner, exit code, e os campos de saída da Seção 29.4 — nunca reconstrói, reinterpreta ou registra de novo esse resultado.
- **Exceção normativa, já estabelecida desde o Draft original:** falhas de sintaxe puramente da CLI — de `--chain`/`--component`, ou de qualquer outra opção — que ocorrem **antes** de qualquer chamada à Application Service seguem o mesmo padrão já estabelecido por `_validate_id_or_exit`: logam uma entrada `error` diretamente, quando `project_dir`/`command` já são conhecidos no ponto da falha (ambos sempre conhecidos aqui, já que a resolução do experimento precede a análise de `--chain`/`--component`). Esta entrada **não é uma duplicata** de nenhum evento do Service — é a única entrada que esta falha específica jamais produz, porque a falha nunca alcança o Service.
- **`created`/`reused` em qualquer evento de sucesso é sempre o resultado factual já computado pela própria chamada ao registry** (Seção 14.5/31.2) — nunca inferido pela CLI ou pelo helper de logging a partir de uma comparação de timestamp.
- **Falha de logging é sempre best-effort** (`except Exception: pass`, Seção 31.1) **e nunca mascara o resultado principal da operação** — uma falha ao escrever a entrada de atividade nunca impede, reverte ou altera o resultado já produzido pelo Service/CLI.
- **`KeyboardInterrupt`/`SystemExit` nunca são capturados como erro operacional** em nenhum ponto deste fluxo — nem pela tradução de exceção (Seção 10.3), nem pelo helper de logging best-effort, nem pela CLI; uma interrupção de processo propaga sem produzir nenhuma entrada `error` fabricada.
- **Nenhuma falha anterior ao início real de uma operação pode produzir um falso evento `succeeded`** — o Service só persiste e só loga sucesso após a operação completar integralmente (tudo-ou-nada, Seções 25.2–25.4); uma falha de sintaxe pré-Service, por definição, nunca alcança esse ponto, e portanto nunca pode gerar um `succeeded` fabricado.
- **Nenhuma operação produz logs duplicados pela combinação Service + CLI** — a regra da exceção acima (a CLI loga apenas o que o Service nunca poderia logar, porque a falha nunca o alcança) é a própria razão pela qual essa exceção não viola a propriedade exclusiva do Service sobre os eventos operacionais.

---

## 30. Erros

### 30.1 Taxonomia completa

| Classe | Base | Camada | `__cause__` | Exit CLI | Activity error | Persistência parcial? |
|---|---|---|---|---|---|---|
| `ReceptorInputNotFoundError` | `FileNotFoundError` | Service | sim | 1 | sim | não |
| `ReceptorInputRecordInvalidError` *(novo — corrige F-07)* | `RuntimeError` | Service | sim | 1 | sim | não |
| `RawArtifactUnavailableError` | `OSError` | Service/parsing | sim | 1 | sim | não |
| `RawArtifactTooLargeError` *(agora na taxonomia central — corrige F-06)* | `OSError` | `receptor_parsing.py` | não | 1 | sim | não |
| `CompressedExtensionRejectedError` *(novo — corrige F-02)* | `ValueError` | `receptor_parsing.py` | não | 1 | sim | não |
| `CompressedRawContentError` *(novo — corrige F-02)* | `ValueError` | `receptor_parsing.py` | não | 1 | sim | não |
| `RawChecksumMismatchError` | `ValueError` | Service | não | 1 | sim | não |
| `UnsupportedStructureFormatError` | `ValueError` | `receptor_parsing.py` | não | 1 | sim | não |
| `ReceptorParseFailureError` | `RuntimeError` | `receptor_parsing.py` | sim | 1 | sim | não |
| `StructConnMalformedError` *(novo — corrige F-03, Seção 18.3)* | `RuntimeError` | `receptor_parsing.py` | não | 1 | sim | não |
| `InspectionFailureError` | `RuntimeError` | `receptor_inspection.py`/Service | sim | 1 | sim | não |
| `ReceptorInspectionIdentityConflictError` *(novo)* | `FileExistsError` | `receptor_registry.py` | não | — (capturada pelo Service) | — | não |
| `ReceptorInspectionRecordInvalidError` *(novo)* | `RuntimeError` | `receptor_registry.py` | sim | 1 | sim | não |
| `ReceptorInspectionNotFoundError` *(novo)* | `FileNotFoundError` | `receptor_registry.py` | não | 1 | sim | não |
| `InspectionSelectionUnsupportedError` *(novo — corrige F-01)* | `RuntimeError` | Service | não | 1 | sim | não |
| `ReceptorSelectionValidationError` | `ValueError` | Service | sim | 1 | sim | não |
| `ReceptorSelectionIdentityConflictError` | `FileExistsError` | `receptor_registry.py` | não | — (capturada pelo Service) | — | não |
| `ReceptorSelectionConflictError` | `RuntimeError` | Service | não | 1 | sim | não |
| `ReceptorSelectionRecordInvalidError` | `RuntimeError` | `receptor_registry.py` | sim | 1 | sim | não |
| `ReceptorSelectionNotFoundError` | `FileNotFoundError` | `receptor_registry.py` | não | 1 | sim | não |
| `ModelNotFoundError` | `RuntimeError` | Service | não | 1 | sim | não |
| `AmbiguousModelSelectionError` | `RuntimeError` | Service | não | 1 | sim | não |
| `AssemblyNotFoundError` | `RuntimeError` | Service | não | 1 | sim | não |
| `ChainNotFoundError` | `RuntimeError` | Service | não | 1 | sim | não |
| `ReceptorResolutionIdentityConflictError` | `FileExistsError` | `receptor_registry.py` | não | — (capturada pelo Service) | — | não |
| `ReceptorResolutionRecordInvalidError` | `RuntimeError` | `receptor_registry.py` | sim | 1 | sim | não |
| `ReceptorResolutionNotFoundError` | `FileNotFoundError` | `receptor_registry.py` | não | 1 | sim | não |
| `ReceptorPersistenceError` | `OSError` | `receptor_registry.py`/Service | sim | 1 | sim | possível (diretório órfão vazio, nunca registro corrompido) |

**Removida:** `ReceptorResolutionParserVersionConflictError` (Seção 25.4 explica a eliminação por construção).

Nenhuma classe inclui caminho absoluto em sua mensagem. Toda classe com `__cause__`=sim preserva a exceção original via `raise X(...) from error`. `KeyboardInterrupt`/`SystemExit` nunca são capturados por nenhum bloco de tradução (Seção 10.3).

---

## 31. Activity Logging

### 31.1 Operações registradas — detalhes tipados atualizados

```python
@dataclass(frozen=True)
class ReceptorInspectActivityDetails:
    protein_input_id: str
    inspection_id: str
    created: bool = False       # NOVO nome, substitui "reused" invertido — created é o fato primário aqui

@dataclass(frozen=True)
class ReceptorSelectionActivityDetails:
    selection_id: str
    protein_input_id: str
    inspection_id: str           # NOVO
    declared_by: str
    reused: bool = False

@dataclass(frozen=True)
class ReceptorResolutionActivityDetails:
    selection_id: str
    inspection_id: str           # NOVO
    reused: bool = False
```

Comandos: `receptor-inspect`, `receptor-selection-declare`, `receptor-selection-resolve`. Cada um registra `started`/`success`/`error`, via o mesmo helper best-effort (`except Exception: pass`) usado em todo o repositório.

### 31.2 Garantias — herdadas, uma precisão nova

- Logging é sempre best-effort.
- Nenhum duplo log entre CLI e Service.
- Nenhum valor científico é inventado apenas para fins de log.
- Nenhum segredo, nenhum caminho absoluto, aparece em nenhum campo logado — apenas ids de domínio e checksums (hashes, não caminhos).
- **Novo:** `created`/`reused` registrado em todo evento de sucesso é **sempre** o resultado factual já computado pela própria chamada ao registry — nunca inferido pelo helper de logging a partir de uma comparação de timestamp (Seção 14.5).

---

## 32. Segurança

### 32.1 Por que o protocolo "Route B endurecida" do Incremento 018 não é reutilizado

Herdado sem alteração da Seção 29.1 do Draft original: a inspeção do 020 lê um `ProteinInput` RAW já registrado via `register_protein`, cuja segurança/identidade já foi estabelecida na borda de registro; o 020 nunca recebe um caminho de arquivo arbitrário de fora do projeto. Esta revisão reafirma essa justificativa e a estende explicitamente ao novo fluxo seguro de leitura (Seção 11.3), que opera sobre o mesmo caminho já confiável.

### 32.2 Limites de tamanho e contagem — atualizados

| Limite | Valor | Comportamento ao exceder |
|---|---|---|
| Tamanho do arquivo RAW antes de inspecionar (verificado sobre o conteúdo real, nunca sobre um tamanho declarado) | 1 GiB | `RawArtifactTooLargeError`, antes de qualquer leitura de conteúdo além dos primeiros bytes de magic (Seção 11.3, passo 3) |
| Modelos inspecionados | 1.000 | Warning `parser-limitation`; enumeração interrompida |
| Cadeias inspecionadas | 10.000 | Idem |
| Componentes não-poliméricos detalhados | 50.000 | Idem |
| `StructureConnection`s totais | 50.000 *(novo)* | Idem |
| Warnings retidos (após deduplicação) | 5.000 | Idem |

Nenhum destes números é uma afirmação científica. **Diferente do Draft original, este teto de tamanho é agora efetivo contra descompressão**, porque a Seção 11.2/11.3 rejeita todo conteúdo comprimido antes mesmo de medir o tamanho do que seria o resultado de uma descompressão que nunca ocorre — o vetor que F-02 identificou (um `.gz` pequeno que descomprimiria para algo arbitrariamente grande) deixa de existir, porque o 020 nunca descomprime nada.

**Cobertura normativa dos tetos — justificativa explícita (correção m-02 desta promoção):** dos seis limites acima, apenas o teto de tamanho de arquivo RAW tem cenário de teste dedicado (T-104). Os cinco tetos restantes (modelos, cadeias, componentes não-poliméricos, `StructureConnection`s, e o teto de warnings retidos) não recebem, cada um, um cenário normativo próprio — decisão deliberada, não uma lacuna: o comportamento ao exceder qualquer um dos seis limites é idêntico e inequívoco (warning `parser-limitation`, Seção 19.1; enumeração interrompida, nunca truncamento silencioso, nunca erro impeditivo), de modo que T-104 já prova esse comportamento genérico de forma completa e sem ambiguidade para o caso representativo; os cinco tetos restantes compartilham exatamente o mesmo mecanismo, sem nenhuma variação de regra entre eles. A ausência de cenário dedicado por teto afeta apenas cobertura/testabilidade redundante, nunca a clareza do contrato — o comportamento em si já está completamente especificado, idêntico e testável para todos os seis limites. Esta nota preserva a matriz normativa em 137 cenários (T-001–T-137): nenhum cenário `T-138+` é acrescentado por esta promoção.

### 32.3 Fail-closed — tabela completa

- **RAW fora do projeto:** impossível por construção, inalterado.
- **Symlink/junction/reparse point:** cobertos transitivamente, inalterado.
- **Entrada comprimida, por extensão ou por conteúdo:** rejeitada em todos os casos (Seção 11.2) — **novo**, fecha F-02.
- **Arquivo alterado durante a leitura:** detectado pela recomputação de checksum no fluxo seguro (Seção 11.3, passos 6/9), inalterado em mecanismo.
- **Checksum inconsistente, incluindo contra uma inspeção já persistida:** `RawChecksumMismatchError`, agora também verificado no momento da resolução contra o checksum gravado no relatório referenciado (Seção 25.4) — **estendido**.
- **Categoria/conexão excessivamente grande:** coberto pelos limites da Seção 32.2.
- **YAML malformado, em qualquer um dos três registros persistidos:** `*RecordInvalidError`, nunca um crash não tratado — **estendido** a `receptor_inspections/`.
- **Path traversal:** `validate_input_id`, inalterado.
- **ID inválido, incluindo `inspection_id` malformado:** rejeitado na fronteira do modelo (Seção 21.2) antes de qualquer I/O.
- **Seleção sobre inspeção incapaz:** `InspectionSelectionUnsupportedError` (Seção 20.2) — **novo**, fecha F-01.

---

## 33. Determinismo

### 33.1 Ordenação canônica — tabela estendida

| Coleção | Chave de ordenação |
|---|---|
| `models` | `model_number` ascendente |
| `assemblies` | `assembly_id` (ordem ordinal Unicode) |
| `entities` | `label_entity_id` quando `identity_origin="source"`; entidades `"unavailable"` ordenadas após todas as `"source"`, entre si por ordem de primeira ocorrência no arquivo *(regra nova, necessária porque `label_entity_id` pode agora ser `None`)* |
| `chains` | `(model_number, label_asym_id ou auth_asym_id quando label_asym_id é None)` *(regra estendida)* |
| `non_polymer_components` | `(label_asym_id ou auth_asym_id, ccd_code)` *(regra estendida)* |
| `missing_residues`/`missing_atoms` | `(label_asym_id ou auth_asym_id, residue_identifier[, atom_name])` |
| `disulfide_bonds`/`covalent_connections`/`metal_coordinations` (agora `StructureConnection`) | `(partner_a.label_asym_id ou auth_asym_id, partner_a.auth_seq_id, partner_b.label_asym_id ou auth_asym_id, partner_b.auth_seq_id)` (Seção 18.5) |
| `altloc_observations`/`occupancy_observations` | `(label_asym_id ou auth_asym_id, residue_identifier[, atom_name])` |
| `warnings` | `(code, model_number, label_asym_id, auth_asym_id, ccd_code, category_name, residue_identifier)`, `None` ordenado antes de qualquer valor presente |
| `resolved_chains`/`resolved_component_dispositions` | mesma chave de `chains`/`non_polymer_components` (sempre `label_asym_id` não-`None`, Seção 20.4) |

A regra "usar `auth_asym_id` como critério de ordenação quando `label_asym_id` é `None`" é a única extensão de comportamento desta seção, necessária diretamente pela introdução de `identity_origin` (Seção 15.5) — nunca deixa uma coleção com ordenação indefinida.

### 33.2 Deduplicação, tokens, Unicode, números — herdados sem alteração

Toda coleção é deduplicada por igualdade estrutural completa antes da ordenação. Tokens `.`/`?` do mmCIF colapsam para `None`. Toda string é normalizada para NFC na fronteira do parser. `occupancy`/`distance` são sempre `Decimal`, nunca `float`.

### 33.3 Timestamps excluídos de identidade — reafirmado, com `inspected_at` retirado

`declared_at`/`resolved_at` nunca participam de nenhuma comparação de retry ou conflito. `inspected_at` deixa de existir como campo de payload (Seção 23.2) — a data de criação de um registro de inspeção é metadado de arquivo (mtime), nunca um campo que participe de identidade ou de comparação de conteúdo.

---

## 34. Integração com o Incremento 021

### 34.1 Contrato de leitura — atualizado

```python
load_protein(project_dir, protein_input_id) -> ProteinInput                              # já existente
load_resolved_receptor_selection(project_dir, selection_id) -> ResolvedReceptorSelection   # Seção 25
load_receptor_inspection(project_dir, inspection_id) -> ReceptorInspectionReport           # NOVO, Seção 25
```

O 021 carrega `ResolvedReceptorSelection` por `selection_id` para obter a seleção confirmada (`resolved_model`/`resolved_assembly`/`resolved_chains`/`resolved_component_dispositions`), e, quando precisar do inventário completo (por exemplo, para decidir como materializar componentes não cobertos pela seleção explícita), carrega o `ReceptorInspectionReport` completo por `inspection_id` — nunca a partir de uma cópia embutida, porque essa cópia não existe mais (Seção 22.2). Isso é uma melhoria direta sobre o contrato do Draft original: o 021 agora tem acesso ao inventário completo por referência estável, sem a penalidade de armazenamento que a duplicação impunha.

### 34.2 O que o 021 poderá fazer — inalterado, fora de escopo deste documento

Materializar o assembly declarado; extrair fisicamente as cadeias selecionadas; resolver fisicamente altloc; aplicar fisicamente as disposições de água/metal/componente; produzir o primeiro `PreparedReceptorArtifact`; decidir se estende `StateTransformationRecord.operation` ou introduz vocabulário próprio.

### 34.3 Compatibilidade de schema

`schema_version="1.0"` em todos os quatro modelos (agora incluindo `ReceptorInspectionReport` como objeto persistido de primeira classe) permanece um compromisso: o 021 pode depender da forma exata descrita neste documento enquanto ela permanecer `"1.0"`. `INSPECTION_PROFILE_VERSION` (Seção 15.1) é um versionamento **adicional e independente**, específico às regras de classificação da inspeção — uma mudança nele nunca invalida `schema_version="1.0"`, e vice-versa.

---

## 35. Matriz Normativa

T-001–T-094 preservados sem renumeração. Cenários cujo modelo subjacente mudou por força de uma correção MAJOR foram **reescritos** (mesmo número, mesmo arquivo, escopo conceitual reconhecível) — marcados explicitamente `[REESCRITO]` abaixo; os demais são `[PRESERVADO]`, reproduzidos verbatim do Draft original. T-095–T-137 são inteiramente novos, acrescentados exclusivamente ao final.

### 35.1 `test_receptor_parsing.py` — T-001–T-012 (preservado/reescrito) + T-095–T-105 (novo) = 23

- **T-001** `[PRESERVADO]` — mmCIF válido, modelo único, sem assembly: parse bem-sucedido, `structure_format="mmcif"`.
- **T-002** `[PRESERVADO]` — mmCIF válido, múltiplos modelos: todos os modelos listados.
- **T-003** `[PRESERVADO]` — mmCIF válido, assembly declarado: `AssemblyDescriptor`/`AssemblyOperationExpression` populados com o texto bruto, nunca avaliado.
- **T-004** `[REESCRITO]` — PDB legado válido: `structure_format="pdb"`; toda `ChainInventoryEntry` com `label_asym_id=None`, `label_asym_id_origin="unavailable"`, `label_entity_id=None`, `label_entity_id_origin="unavailable"`, `auth_asym_id` populado; `selection_capability="inspection-only"` no relatório.
- **T-005** `[PRESERVADO]` — Formato não reconhecido por nenhum dos dois parsers suportados: `UnsupportedStructureFormatError`.
- **T-006** `[PRESERVADO]` — Arquivo CIF malformado (sintaxe inválida): `ReceptorParseFailureError`, `__cause__` preservado.
- **T-007** `[PRESERVADO]` — Arquivo truncado no meio de uma categoria: `ReceptorParseFailureError`.
- **T-008** `[PRESERVADO]` — Categoria `_pdbx_struct_assembly` ausente do mmCIF: `assemblies=()`, `"pdbx_struct_assembly"` em `unavailable_categories`.
- **T-009** `[PRESERVADO]` — Categoria `_struct_conn` ausente: `disulfide_bonds=covalent_connections=metal_coordinations=()`, categoria nomeada em `unavailable_categories`.
- **T-010** `[PRESERVADO]` — `parser.version` registrado é exatamente `gemmi.__version__` observado em tempo de execução, nunca a string do pin de `pyproject.toml`.
- **T-011** `[PRESERVADO]` — Nenhum tipo `gemmi.*` é alcançável a partir do valor de retorno de `parse_receptor_raw` fora de `receptor_parsing.py`.
- **T-012** `[REESCRITO]` — `RawArtifact.format` registrado como `"pdb"` mas conteúdo real é mmCIF (ou vice-versa): detecção por conteúdo prevalece; `structure_format` reflete o conteúdo real; **warning `declared-format-mismatch` emitido** (corrige F-10).
- **T-095** `[NOVO]` — `receptor_parsing.py` nunca invoca `setup_entities()`/`add_entity_types()`/`assign_subchains()`/`ensure_entities()`/`deduplicate_entities()` do Gemmi em nenhum caminho de código, inclusive ao processar PDB legado (verificação de boundary/disciplina, análoga a T-011; corrige F-01).
- **T-096** `[NOVO]` — RAW com extensão `.gz`: `CompressedExtensionRejectedError`, antes de qualquer abertura para parsing (representativo; o mesmo mecanismo de lista fechada de extensões cobre `.bz2`/`.xz`/`.zip` de forma idêntica).
- **T-097** `[NOVO]` — Conteúdo do RAW começa com os magic bytes de gzip (`0x1F 0x8B`): `CompressedRawContentError`.
- **T-098** `[NOVO]` — Conteúdo do RAW começa com os magic bytes de bzip2 (`"BZh"`): `CompressedRawContentError`.
- **T-099** `[NOVO]` — Conteúdo do RAW começa com os magic bytes de xz (`0xFD 0x37 0x7A 0x58 0x5A 0x00`): `CompressedRawContentError`.
- **T-100** `[NOVO]` — Conteúdo do RAW começa com os magic bytes de zip (`"PK\x03\x04"`): `CompressedRawContentError`.
- **T-101** `[NOVO]` — Arquivo nomeado `estrutura.cif` cujo conteúdo real é gzip-comprimido: `CompressedRawContentError` (extensão permitida, conteúdo comprimido).
- **T-102** `[NOVO]` — Arquivo originalmente `.gz`, renomeado para `.cif`: `CompressedRawContentError` (mesma detecção por conteúdo de T-101, framing explícito exigido pela tarefa).
- **T-103** `[NOVO]` — Arquivo com extensão `.gz` cujo conteúdo **não** está de fato comprimido: ainda assim `CompressedExtensionRejectedError` — a rejeição por extensão é incondicional, nunca contingente ao conteúdo sniffado (prova de defesa em profundidade independente).
- **T-104** `[NOVO]` — RAW cujo tamanho em disco excede 1 GiB: `RawArtifactTooLargeError`, antes de qualquer leitura de conteúdo além do necessário para `stat()` (corrige a lacuna de cobertura de F-06).
- **T-105** `[NOVO]` — RAW alterado (fixture injetando uma mudança de conteúdo entre a verificação inicial e a leitura completa): divergência de checksum detectada, `RawChecksumMismatchError`, nenhuma inspeção parcial persistida.

### 35.2 `test_receptor_inspection.py` — T-013–T-042 (preservado/reescrito) + T-106–T-122 (novo) = 47

- **T-013** `[PRESERVADO]` — Múltiplos modelos: warning `multiple-models` emitido.
- **T-014** `[PRESERVADO]` — Múltiplos assemblies: warning `multiple-assemblies` emitido.
- **T-015** `[PRESERVADO]` — Altloc presente em um resíduo: `AltlocObservation` populado; warning `alternate-locations-present`.
- **T-016** `[PRESERVADO]` — Ocupância parcial (`!= 1`) em um átomo: `OccupancyObservation` populado; warning `partial-occupancy-present`.
- **T-017** `[PRESERVADO]` — Todos os átomos com ocupância exatamente 1: `occupancy_observations=()` — nenhum warning de ocupância.
- **T-018** `[PRESERVADO]` — Resíduos não observados: `MissingResidueObservation` populado; warning `missing-residues-reported`.
- **T-019** `[PRESERVADO]` — Átomos não observados: `MissingAtomObservation` populado; warning `missing-atoms-reported`.
- **T-020** `[PRESERVADO]` — `auth_asym_id` mapeia para múltiplos `label_asym_id`: warning `ambiguous-author-chain-id`.
- **T-021** `[PRESERVADO]` — Contagem de resíduos/átomos por cadeia corresponde exatamente à contagem bruta do arquivo.
- **T-022** `[REESCRITO]` — `label_entity_id` (origem `"source"`) compartilhado por duas cadeias (cópias idênticas na unidade assimétrica): ambas as `ChainInventoryEntry` referenciam o mesmo `label_entity_id`, sem duplicação de `EntityInventoryEntry` (renomeado de `EntityDescriptor`).
- **T-023** `[REESCRITO]` — PDB legado: `unavailable_categories` contém `"pdbx_struct_assembly"`, `"struct_conn"`, `"pdbx_unobs_or_zero_occ_residues"`, `"pdbx_unobs_or_zero_occ_atoms"` (categorias exclusivamente mmCIF); **porém** `disulfide_bonds`/`covalent_connections`/`metal_coordinations` podem estar não-vazios quando o arquivo declara `SSBOND`/`LINK`/`CONECT` e o Gemmi os expõe estruturadamente (Seção 12.3) — corrige a leitura excessivamente ampla que a Adversarial Review registrou em N-10; warning `legacy-pdb-information-limited` sempre presente.
- **T-024** `[PRESERVADO]` — Nenhum resíduo/átomo ausente declarado no arquivo: `missing_residues=missing_atoms=()`, nenhum warning correspondente.
- **T-025** `[PRESERVADO]` — Token mmCIF `?` em um campo opcional: campo correspondente é `None`.
- **T-026** `[PRESERVADO]` — Token mmCIF `.` em um campo opcional: campo correspondente é `None`.
- **T-027** `[PRESERVADO]` — Componente `HOH`: `classification="water"`, `classification_basis="format-declared"`.
- **T-028** `[PRESERVADO]` — Componente `DOD`: `classification="water"`.
- **T-029** `[PRESERVADO]` — Componente `ZN` monoatômico: `classification="metal-ion"`, `classification_basis="closed-dictionary-match"`.
- **T-030** `[REESCRITO — precisão de framing, mesmo resultado]** — Componente **poliatômico** não-polimérico orgânico fora da tabela de metais e fora de `HOH`/`DOD` (ex. um ligante com múltiplos átomos): `classification="other-non-polymer"`; warning `unknown-chemical-component`. (O qualificador "poliatômico" é explicitado para permanecer distinto de T-106, que cobre o caso monoatômico não listado.)
- **T-031** `[PRESERVADO]` — Resíduo polimérico modificado (código fora do vocabulário padrão de 20/5): `classification="modified-polymer-residue"`.
- **T-032** `[PRESERVADO]` — Componente cujo `entity_type` o parser não conseguiu determinar: `classification="unknown"`, `classification_basis="undetermined"`.
- **T-033**, **T-034**, **T-035** `[REESCRITOS — modelo subjacente mudou]** — `_struct_conn` com `conn_type_id="disulf"`/`"metalc"`/`"covale"`: particiona em `disulfide_bonds`/`metal_coordinations`/`covalent_connections` respectivamente, agora como instâncias de `StructureConnection` (Seção 18.2) com `source_category="struct_conn"` e `category` correspondente; warnings `metal-coordination-present`/`covalent-connection-present` emitidos conforme já especificado.
- **T-036** `[PRESERVADO]` — Hidrogênios explícitos presentes (`type_symbol` H/D no `_atom_site`): `explicit_hydrogens_present=True`, contagem correta.
- **T-037** `[PRESERVADO]` — Nenhum hidrogênio explícito: `explicit_hydrogens_present=False`; warning `explicit-hydrogens-absent`.
- **T-038** `[PRESERVADO]` — `HETATM`/componente não-polimérico nunca é omitido do inventário, mesmo quando `classification="unknown"`.
- **T-039** `[PRESERVADO]` — Dois registros `_struct_conn` idênticos no arquivo de origem: deduplicados para uma única entrada.
- **T-040** `[PRESERVADO]` — Componente metálico com múltiplos átomos nunca é classificado `"metal-ion"` (regra `atom_count==1`); cai em `"other-non-polymer"`.
- **T-041** `[PRESERVADO]` — Disposição/classificação nunca se cruzam automaticamente: um componente `"other-non-polymer"` nunca recebe `role`/`disposition` da inspeção.
- **T-042** `[PRESERVADO]` — CCD code com 5 caracteres (extended CCD): aceito sem erro.
- **T-106** `[NOVO]` — Componente **monoatômico** não-polimérico cujo `ccd_code` não está na tabela de metais e não é `"HOH"`/`"DOD"`: `classification="unknown"`, `classification_basis="undetermined"` — **nunca** `"other-non-polymer"` (corrige o risco de falso negativo exigido pela tarefa; distinto de T-030).
- **T-107** `[NOVO]` — Estrutura PDB legado: `ReceptorInspectionReport.selection_capability="inspection-only"`.
- **T-108** `[NOVO]` — mmCIF degenerado que omite `label_asym_id`/`label_entity_id` para uma cadeia/entidade específica (mas os declara para as demais): aquela cadeia/entidade recebe `identity_origin="unavailable"`; `selection_capability` do relatório inteiro torna-se `"inspection-only"`.
- **T-109** `[NOVO]` — `ChainInventoryEntry.label_asym_id` é `None` com `label_asym_id_origin="unavailable"` para toda cadeia de um PDB legado; `auth_asym_id` permanece populado.
- **T-110** `[NOVO]` — `EntityInventoryEntry.label_entity_id` é `None` com `label_entity_id_origin="unavailable"` para toda entidade de um PDB legado.
- **T-111** `[NOVO]` — `IdentityOrigin` rejeita qualquer valor fora de `{"source", "parser-derived", "unavailable"}` (validação de `Literal`).
- **T-112** `[NOVO]` — `_struct_conn` com `pdbx_ptnr1_label_alt_id`/`pdbx_ptnr2_label_alt_id` declarados: `StructConnEndpoint.label_alt_id` preservado em ambos os parceiros (corrige F-03).
- **T-113** `[NOVO]` — `_struct_conn` com `pdbx_ptnr1_symmetry`/`pdbx_ptnr2_symmetry` declarando uma operação de simetria cristalográfica: `StructConnEndpoint.symmetry` preservado em ambos os parceiros (corrige F-03).
- **T-114** `[NOVO]` — `_struct_conn` declarando `pdbx_dist_value`/`pdbx_value_order`/`pdbx_role`/`details`: `StructureConnection.distance`/`value_order`/`role`/`details` preservados; quando a categoria omite qualquer um desses itens para uma linha, o campo correspondente permanece `None`, nunca fabricado.
- **T-115** `[NOVO]` — Linha de `_struct_conn` com `conn_type_id` ausente/vazio: `StructConnMalformedError`.
- **T-116** `[NOVO]` — Registro `SSBOND` presente em um PDB legado, exposto estruturadamente pelo Gemmi: mapeado para `disulfide_bonds`, `source_category="legacy-pdb-ssbond"`, campos `label_*`/`label_alt_id`/`symmetry` dos endpoints permanecem `None`.
- **T-117** `[NOVO]` — Registro `LINK` presente, nenhum parceiro classificado `"metal-ion"`: mapeado para `covalent_connections`, `source_category="legacy-pdb-link"`, `category="legacy-pdb-link-covalent"`.
- **T-118** `[NOVO]` — Registro `LINK` presente, um parceiro classificado `"metal-ion"`: mapeado para `metal_coordinations`, `category="legacy-pdb-link-metal"`.
- **T-119** `[NOVO]` — Registro `CONECT` presente: mapeado para `covalent_connections` ou `metal_coordinations` pela mesma regra de parceiro-metálico, `source_category="legacy-pdb-conect"`.
- **T-120** `[NOVO]` — `REMARK 465`/`470` presentes em um PDB legado, **não** expostos estruturadamente pela API do Gemmi na fixture de teste: categoria permanece em `unavailable_categories`, nomeando `"REMARK465"`/`"REMARK470"`; nenhum parsing manual de texto é tentado.
- **T-121** `[NOVO]` — `REMARK 465`/`470` expostos estruturadamente pela API do Gemmi na fixture de teste: `missing_residues`/`missing_atoms` populados exatamente como no caminho mmCIF.
- **T-122** `[NOVO]` — Vetor golden de `inspection_id`: o payload canônico exato da Seção 15.3 produz exatamente `73090f1a141de86e358c79f051b0245df0ca32287425935632e624d15078adf4` (reprodutibilidade byte a byte).

### 35.3 `test_receptor_selection.py` — T-043–T-056 (preservado) + T-123 (novo) = 15

- **T-043** `[REESCRITO — campos obrigatórios novos]** — Construção válida mínima: agora inclui `inspection_id` (64 hex) e `raw_checksum_observed` (64 hex) como campos obrigatórios adicionais; sucesso quando todos os campos obrigatórios (incluindo os dois novos) são fornecidos.
- **T-044** `[PRESERVADO]` — `selection_id` malformado: `ValueError` de `validate_input_id`.
- **T-045** `[PRESERVADO]` — `selected_chains` com `label_asym_id` duplicado: `ValueError` do `model_validator`.
- **T-046** `[PRESERVADO]` — `component_dispositions` com par `(label_asym_id, ccd_code)` duplicado: `ValueError`.
- **T-047** `[PRESERVADO]` — `declared_by` em branco (apenas espaços): `ValueError`.
- **T-048** `[PRESERVADO]` — `label`/`rationale` em branco quando fornecidos: `ValueError`.
- **T-049** `[PRESERVADO]` — `declared_at` sem timezone: `ValueError`.
- **T-050** `[PRESERVADO]` — `selected_model=0` ou negativo: `ValueError` (`ge=1`).
- **T-051** `[PRESERVADO]` — `extra="forbid"`: campo desconhecido no payload é rejeitado.
- **T-052** `[PRESERVADO]` — Modelo é `frozen=True`: tentativa de reatribuição de campo levanta erro.
- **T-053** `[PRESERVADO]` — `ChainSelector` com apenas `label_asym_id` (sem `auth_asym_id`): válido.
- **T-054** `[PRESERVADO]` — `ChainSelector` com `label_asym_id` vazio: `ValueError` (`min_length=1`).
- **T-055** `[PRESERVADO]` — `ComponentDisposition.role` fora de `{"cofactor","crystallographic_ligand"}`: `ValueError`.
- **T-056** `[PRESERVADO]` — Nenhum campo `altloc_policy`/`cofactor_policy`/`crystallographic_ligand_policy` existe no schema.
- **T-123** `[NOVO]` — `ChainSelector` nunca aceita um seletor baseado somente em `auth_asym_id` (nenhum caminho de construção permite omitir `label_asym_id` enquanto fornece `auth_asym_id`) — reconfirmação explícita sob a arquitetura de `selection_capability` (Seção 20.3).

### 35.4 `test_receptor_resolution.py` — T-057–T-068 (reescrito) + T-124 (novo) = 13

- **T-057** `[REESCRITO]** — Construção válida mínima: sucesso; `resolved_selection_id == policy_selection_id`; `inspection_id` presente e bem formado (64 hex); nenhum campo `inspection_snapshot` existe mais no construtor (retirado, Seção 22.2).
- **T-058** `[PRESERVADO]** — `resolved_selection_id != policy_selection_id`: `ValueError` do `model_validator`.
- **T-059** `[REESCRITO — concern realocado]** — `inspection_id` malformado (não 64 caracteres hexadecimais): `ValueError` na fronteira do campo — substitui o cross-check anterior contra um `inspection_snapshot.raw_checksum` embutido, que não existe mais; a consistência entre `raw_checksum`/`parser`/`structure_format` do objeto e os do relatório referenciado passa a ser responsabilidade do Service (Seção 25.4), nunca mais um validator deste modelo isolado.
- **T-060** `[REESCRITO]** — `parser.version` vazio/malformado: `ValueError` na fronteira do campo (`ParserProvenance`, inalterado).
- **T-061** `[REESCRITO — mecanismo]` *(etiqueta corrigida nesta promoção, n-02; texto do cenário inalterado)* — `resolved_chains` contém um `label_asym_id` que o Service não confirmou (verificado por integração, não mais por cross-check contra um snapshot embutido): `ChainNotFoundError` é levantado pelo Service antes de qualquer construção deste modelo (Seção 25.4) — este cenário migra de "validador de modelo" para "comportamento de Service", mesmo número, mesmo escopo conceitual ("uma cadeia não confirmada nunca aparece em `resolved_chains`").
- **T-062** `[PRESERVADO]** — `resolved_chains` com `label_asym_id` duplicado: `ValueError`.
- **T-063** `[PRESERVADO]** — Nenhum campo do modelo, ou de qualquer submodelo referenciado, nomeia um caminho de arquivo de estrutura de saída.
- **T-064** `[PRESERVADO]** — `resolved_assembly=None` é válido mesmo quando o relatório referenciado declara assemblies.
- **T-065** `[PRESERVADO]** — `model_resolution_basis="only-model-present"` só ocorre quando o relatório referenciado tem exatamente um modelo (verificado pelo Service).
- **T-066** `[PRESERVADO]** — `ResolvedComponentDisposition.disposition_source="water_disposition"` implica `classification="water"`.
- **T-067** `[PRESERVADO]** — Serialização round-trip preserva igualdade estrutural completa.
- **T-068** `[PRESERVADO]** — Nenhum campo `semantic_key` existe no schema.
- **T-124** `[NOVO]** — Introspecção de schema: nenhum campo de `ResolvedReceptorSelection`, ou de qualquer submodelo que referencia, é do tipo `ReceptorInspectionReport` ou contém qualquer uma de suas coleções de inventário — prova direta de que a duplicação que F-04 identificou foi eliminada, não apenas reduzida.

### 35.5 `test_receptor_registry.py` — T-069–T-080 (preservado/reescrito) + T-125–T-130 (novo) = 18

- **T-069** `[PRESERVADO]` — `register_receptor_selection` cria o arquivo em `scientific/receptor_selections/<id>.yaml`.
- **T-070** `[PRESERVADO]` — Colisão casefold de `selection_id` contra um registro existente: `ReceptorSelectionIdentityConflictError`.
- **T-071** `[PRESERVADO]` — `load_receptor_selection` de um id inexistente: `ReceptorSelectionNotFoundError`.
- **T-072** `[PRESERVADO]` — `load_receptor_selection` de um YAML malformado: `ReceptorSelectionRecordInvalidError`, `__cause__` preservado.
- **T-073** `[PRESERVADO]` — `load_receptor_selection` de um YAML sintaticamente válido mas que não valida contra o schema Pydantic: `ReceptorSelectionRecordInvalidError`.
- **T-074** `[PRESERVADO]` — `list_receptor_selections` retorna `()` quando o diretório não existe ainda.
- **T-075** `[PRESERVADO]` — `list_receptor_selections` ordena por `(declared_at, selection_id)`.
- **T-076** `[PRESERVADO]` — `register_resolved_receptor_selection` cria o arquivo em `scientific/receptor_selections/resolved/<id>.yaml`.
- **T-077** `[REESCRITO]** — Duas chamadas de `inspect_receptor` com o mesmo `inspection_id` (mesmo RAW/parser/profile): o arquivo `receptor_inspections/<inspection_id>.yaml` não é reescrito na segunda chamada (verificado por mtime e por conteúdo byte-idêntico) — substitui a linguagem de "cache hit" do Draft original por "create-once hit", refletindo que a inspeção é agora um registro de primeira classe (Seção 14.1).
- **T-078** `[REESCRITO]** — Chave diferente (`inspection_id` diferente, por RAW, parser ou profile diferentes) produz um arquivo separado, sem colidir com o anterior; o anterior permanece inalterado e carregável.
- **T-079** `[PRESERVADO]** — Nenhum diretório `.staging` é criado sob nenhum dos três caminhos de persistência, incluindo `receptor_inspections/`.
- **T-080** `[PRESERVADO]** — `atomic_write_text` subjacente é de fato atômico para os três caminhos.
- **T-125** `[NOVO]** — Primeira chamada de `inspect_receptor` para um `(protein_input_id, raw_checksum, parser, profile)` inédito: cria `receptor_inspections/<inspection_id>.yaml`, `created=True`.
- **T-126** `[NOVO]** — Segunda chamada idêntica: `created=False` (ou, equivalentemente, `reused=True` na perspectiva do chamador), nenhuma reescrita — o fato é lido diretamente da verificação de existência do registry, nunca inferido de um timestamp.
- **T-127** `[NOVO]** — `raw_checksum` diferente (fixture com um segundo `ProteinInput`): `inspection_id` diferente; o registro de inspeção anterior permanece intacto e carregável por seu próprio `inspection_id`.
- **T-128** `[NOVO]** — `parser_version` diferente (fixture monkey-patchando `gemmi.__version__` observado): `inspection_id` diferente; `created=True` sob o novo id; nenhum conflito é levantado; o registro anterior permanece intacto.
- **T-129** `[NOVO]** — `INSPECTION_PROFILE_VERSION` diferente (fixture monkey-patchando a constante): `inspection_id` diferente; mesmo comportamento de T-128.
- **T-130** `[NOVO]** — Duas `ResolvedReceptorSelection` distintas (dois `selection_id`s diferentes) referenciando o mesmo `inspection_id`: o arquivo `receptor_inspections/<inspection_id>.yaml` é escrito exatamente uma vez, nunca reescrito pela segunda resolução — prova direta de que múltiplas resoluções não duplicam o inventário (Seção 14.3, regra 3).

### 35.6 `test_receptor_service.py` — T-081–T-090 (preservado/reescrito) + T-131–T-135 (novo) = 15

- **T-081**, **T-082** `[PRESERVADOS]** — inalterados (`protein_input_id` inexistente → `ReceptorInputNotFoundError`; checksum divergente no momento da inspeção → `RawChecksumMismatchError`, nenhum registro persistido).
- **T-083**, **T-084** `[PRESERVADOS]** — inalterados (retry idêntico de `declare_receptor_selection` → `reused=True`; conteúdo divergente sob o mesmo `selection_id` → `ReceptorSelectionConflictError`).
- **T-085**, **T-086** `[PRESERVADOS]** — inalterados (`selected_model=None` sobre relatório multi-modelo → `AmbiguousModelSelectionError`; cadeia inexistente → `ChainNotFoundError`; em ambos, nenhuma `ResolvedReceptorSelection` persistida).
- **T-087** `[PRESERVADO]** — Retry idêntico de `resolve_receptor_selection` → `reused=True`, nenhuma reescrita.
- **T-088** `[REESCRITO — mecanismo, mesmo resultado]** — Retry de `resolve_receptor_selection` após o RAW ter sido alterado: a revalidação de checksum contra o `raw_checksum` gravado no relatório referenciado (Seção 25.4, passo 3) detecta a divergência; `RawChecksumMismatchError`; o registro de inspeção referenciado permanece intacto.
- **T-089** `[REESCRITO — classe de erro eliminada, cenário redirecionado]** — Uma nova chamada a `inspect_receptor` sob uma versão de parser diferente da que produziu um `inspection_id` anteriormente persistido produz um **novo** `inspection_id` (`created=True`); o `inspection_id` antigo, e qualquer `ReceptorSelectionPolicy`/`ResolvedReceptorSelection` que o referencia, permanecem intactos e carregáveis; **nenhum `ReceptorResolutionParserVersionConflictError` é levantado** — a classe foi eliminada (Seção 25.4), porque este cenário nunca mais se apresenta como um conflito de retry.
- **T-090** `[PRESERVADO]** — Activity log registra exatamente uma entrada `started` e uma entrada terminal por chamada de serviço.
- **T-131** `[NOVO]** — `declare_receptor_selection` contra um `protein_input_id` cuja inspeção atual tem `selection_capability="inspection-only"`: `InspectionSelectionUnsupportedError`; nenhuma `ReceptorSelectionPolicy` persistida (corrige F-01).
- **T-132** `[NOVO]** — `declare_receptor_selection` bem-sucedida: a `ReceptorSelectionPolicy` persistida tem `inspection_id`/`raw_checksum_observed` idênticos aos retornados pela chamada interna a `inspect_receptor` — nunca a um valor fornecido pelo chamador (que a assinatura pública nem aceita).
- **T-133** `[NOVO]** — `resolve_receptor_selection` quando o `inspection_id` pinado pela política foi removido do disco (fixture simulando perda do registro): `ReceptorInspectionNotFoundError`; nenhuma `ResolvedReceptorSelection` persistida.
- **T-134** `[NOVO]** — `resolve_receptor_selection` quando o registro de inspeção pinado existe mas falha validação Pydantic/YAML: `ReceptorInspectionRecordInvalidError`, `__cause__` preservado; nenhuma persistência parcial.
- **T-135** `[NOVO]** — `resolve_receptor_selection` revalida o checksum atual do RAW contra o `raw_checksum` gravado no relatório pinado (fixture com divergência fabricada): `RawChecksumMismatchError`; nem a resolução nem o relatório de inspeção são modificados.

### 35.7 `test_cli.py` — T-091–T-094 (preservado/reescrito) + T-136–T-137 (novo) = 6

- **T-091** `[REESCRITO]** — `protein inspect` sobre um id válido: banner de sucesso, exit 0, saída inclui `inspection_id`, `created`/`reused` factual, `raw_checksum`, `selection_capability`, e a lista de warnings (se houver) — corrige F-06/F-07 na superfície da CLI.
- **T-092** `[PRESERVADO]** — `receptor select` seguido de `receptor resolve`: fluxo completo produz um `ResolvedReceptorSelection` carregável por `receptor show-resolution`.
- **T-093** `[PRESERVADO]** — Qualquer erro de resolução produz o banner `RESOLUTION FAILED`, exit 1, mensagem sanitizada via `_sanitize_cli_error_text`.
- **T-094** `[PRESERVADO]** — `receptor list-selections --source <protein-input-id>` filtra corretamente por origem, sem reordenar além de `(declared_at, selection_id)`.
- **T-136** `[NOVO]** — `receptor inspection show <experiment> <inspection-id>` carrega e exibe um relatório de inspeção já persistido, sem reinvocar o parser.
- **T-137** `[NOVO]** — Toda saída de sucesso de `protein inspect`/`receptor select`/`receptor resolve` inclui `selection_capability` e `inspection_id` explicitamente (Seção 29.4).

### 35.8 Reconciliação mecânica

| Grupo | Faixas | Subtotal |
|---|---|---|
| Parser/formato (`test_receptor_parsing.py`) | T-001–012, T-095–105 | 12 + 11 = **23** |
| Inventário estrutural+químico (`test_receptor_inspection.py`) | T-013–042, T-106–122 | 30 + 17 = **47** |
| `ReceptorSelectionPolicy` (`test_receptor_selection.py`) | T-043–056, T-123 | 14 + 1 = **15** |
| `ResolvedReceptorSelection` (`test_receptor_resolution.py`) | T-057–068, T-124 | 12 + 1 = **13** |
| Persistência (`test_receptor_registry.py`) | T-069–080, T-125–130 | 12 + 6 = **18** |
| Application Service (`test_receptor_service.py`) | T-081–090, T-131–135 | 10 + 5 = **15** |
| CLI (`test_cli.py`) | T-091–094, T-136–137 | 4 + 2 = **6** |
| **Total** | **T-001–137** | **23+47+15+13+18+15+6 = 137** |

Verificação da soma: `23+47 = 70`; `70+15 = 85`; `85+13 = 98`; `98+18 = 116`; `116+15 = 131`; `131+6 = 137`. Contagem de ids únicos: 94 (originais, nenhum removido) + 43 (T-095–T-137) = 137. **Soma de subtotais == total == contagem de ids únicos == 137.** Nenhuma lacuna (T-001–T-137 contíguo), nenhuma duplicata, nenhuma renumeração.

---

## 36. Critérios de Aceite da Especificação Final

Esta Final Specification satisfaz, de forma integral e verificada, todos os critérios abaixo:

1. Nenhum item de química proibida (Seção 7) foi introduzido em qualquer modelo (Seções 13–22). **Satisfeito** — confirmado por busca exaustiva (Seção 7).
2. Nenhuma materialização estrutural foi introduzida. **Satisfeito** — T-063, T-124 testam isso explicitamente.
3. O parser está decidido, com a correção de F-01/F-02 incorporada (Seção 10). **Satisfeito.**
4. Os quatro modelos de domínio (agora incluindo o relatório de inspeção como objeto persistido) estão completamente especificados, incluindo validadores, imutabilidade e serialização (Seções 13–22). **Satisfeito.**
5. A persistência está completamente definida para os três registros create-once (Seção 24). **Satisfeito.**
6. A CLI está completamente definida, incluindo o comando novo (Seção 29). **Satisfeito.**
7. A taxonomia de erros está completa, sem as lacunas de cobertura que F-06/F-07 identificaram (Seção 30). **Satisfeito.**
8. A matriz normativa está reconciliada mecanicamente (soma de subtotais == total == contagem de ids únicos == 137, Seção 35.8) — **verificada explicitamente, corrigindo o erro aritmético de F-05.**
9. A allowlist está definida, sem novos arquivos além dos já previstos (Seção 37). **Satisfeito.**
10. Os checkpoints estão definidos e suas contagens reconciliam mecanicamente contra a matriz (Seção 38). **Satisfeito.**
11. Os quatro achados MAJOR estão RESOLVED (Seção 41), os seis MINOR originais estão RESOLVED (Seção 42), e as dez NOTES estão RECONCILED (Seção 43), sem nenhum achado omitido ou suavizado sem justificativa.
12. Nenhum TBD normativo permanece — toda decisão condicional (Seção 12.4, REMARK 465/470) está completamente especificada para ambos os desfechos possíveis, com apenas o desfecho concreto dependente de confirmação de biblioteca no Checkpoint 1, exatamente como a versão exata do pin do Gemmi já era.
13. As sete correções autorizadas pela Seção 19 da Corrected Revised Draft Confirmation (`10-correction-confirmation`) — m-02, m-04, m-05, m-06, n-01, n-02, n-03 — estão todas aplicadas, cada uma localizada em sua seção normativa final e reconciliada na tabela da Seção 45.1 desta especificação, sem ampliação para temas adjacentes e sem reabertura de arquitetura, modelo, identidade, parser ou escopo.

Todos os treze critérios estão satisfeitos por este documento, conforme as seções citadas.

---

## 37. Allowlist

**Inalterada em contagem de arquivos** — nenhum módulo novo foi necessário para incorporar as quatro correções MAJOR; todas foram absorvidas pelos sete módulos já previstos pelo Draft original, com conteúdo atualizado.

| Caminho | Natureza | Conteúdo atualizado por esta revisão |
|---|---|---|
| `src/molecular/receptor_parsing.py` | Novo | Único módulo que importa `gemmi`; **adiciona** o fluxo seguro de leitura (Seção 11.3), a rejeição de compressão (Seção 11.2), e a proibição explícita de `setup_entities()`/métodos mutantes (Seção 10.3) |
| `src/molecular/receptor_inspection.py` | Novo | `ReceptorInspectionReport` (agora com `selection_capability`), `EntityInventoryEntry`/`ChainInventoryEntry` (renomeados, com `identity_origin`), `StructConnEndpoint`/`StructureConnection` (Seção 18), vocabulário de warnings estendido (Seção 19), **e** o algoritmo de `inspection_id` (Seção 15) |
| `src/molecular/receptor_selection.py` | Novo | `ReceptorSelectionPolicy` (campos novos `inspection_id`/`raw_checksum_observed`, Seção 21), `ChainSelector`, `ComponentDisposition` |
| `src/molecular/receptor_resolution.py` | Novo | `ResolvedReceptorSelection` (campo `inspection_snapshot` retirado, campo `inspection_id` adicionado, Seção 22), `ResolvedChainSelection` (simplificado), `ResolvedComponentDisposition` |
| `src/molecular/receptor_registry.py` | Novo | Persistência estendida: `receptor_inspections/` passa de cache opcional a registry create-once de primeira classe (Seção 24) |
| `src/molecular/receptor_service.py` | Novo | Application Service — adiciona `load_receptor_inspection`; `inspect_receptor` passa a persistir; `declare_receptor_selection`/`resolve_receptor_selection` redesenhados (Seção 25) |
| `src/molecular/cli.py` | Existente, aditivo apenas | Adiciona `receptor inspection show`; demais comandos com saída atualizada (Seção 29) |
| `pyproject.toml` | Existente, aditivo apenas | **Inalterado em conteúdo** — ainda apenas `structure = ["gemmi==<versão travada>"]`; nenhuma nova dependência é necessária para magic-byte detection (assinaturas públicas, stdlib apenas) |
| `tests/test_receptor_parsing.py` | Novo | T-001–012, T-095–105 |
| `tests/test_receptor_inspection.py` | Novo | T-013–042, T-106–122 |
| `tests/test_receptor_selection.py` | Novo | T-043–056, T-123 |
| `tests/test_receptor_resolution.py` | Novo | T-057–068, T-124 |
| `tests/test_receptor_registry.py` | Novo | T-069–080, T-125–130 |
| `tests/test_receptor_service.py` | Novo | T-081–090, T-131–135 |
| `tests/test_cli.py` | Existente, aditivo apenas | T-091–094, T-136–137 |

Nenhum nome acima é adotado automaticamente se colidir com código real já presente no momento da implementação — herdado sem alteração.

---

## 38. Checkpoints

Redistribuídos para incorporar os cenários novos, com aritmética verificada explicitamente em cada passo (corrige F-05 por construção e documenta a verificação para impedir recorrência).

### Checkpoint 1 — Domínio + fronteira do parser + inspeção (agora incluindo persistência de inspeção e correções F-01/F-02/F-03)
- **Arquivos autorizados:** `receptor_parsing.py`, `receptor_inspection.py`, `receptor_registry.py` (apenas a parte de `receptor_inspections/`), `pyproject.toml` (extra `structure`, inalterado), `tests/test_receptor_parsing.py`, `tests/test_receptor_inspection.py`.
- **Contratos:** `parse_receptor_raw` completo, incluindo o fluxo seguro de leitura e a rejeição de compressão; `ReceptorInspectionReport` e todos os submodelos completos, incluindo `identity_origin`/`selection_capability`/`StructureConnection`; persistência create-once de `ReceptorInspectionReport` via `inspection_id`.
- **Cenários normativos:** grupo Parser/formato (23: T-001–012, T-095–105) + grupo Inventário (47: T-013–042, T-106–122) = **70 cenários**.
- **Testes direcionados:** os 70 cenários acima.
- **Suíte completa:** reexecução integral da baseline herdada (1.315 + os novos) sem nenhuma regressão.
- **Restore point:** commit isolado, revertível independentemente.
- **Microrrevisão obrigatória:** confirmar que nenhum tipo `gemmi.*` escapou de `receptor_parsing.py` (T-011); confirmar que `setup_entities()` e os métodos mutantes nunca são chamados (T-095); confirmar que toda entrada comprimida é rejeitada por extensão e por magic bytes (T-096–105); confirmar o vetor golden de `inspection_id` (T-122) byte a byte.
- Nenhuma preparação química ou estrutura derivada é produzida neste checkpoint.

### Checkpoint 2 — Seleção + resolução + persistência completa (incorpora F-04)
- **Arquivos autorizados:** `receptor_selection.py`, `receptor_resolution.py`, `receptor_registry.py` (completo), `tests/test_receptor_selection.py`, `tests/test_receptor_resolution.py`, `tests/test_receptor_registry.py`.
- **Contratos:** `ReceptorSelectionPolicy` referenciando `inspection_id`/`raw_checksum_observed`; `ResolvedReceptorSelection` referenciando `inspection_id` sem embutir o relatório; persistência completa dos três registros create-once.
- **Cenários normativos:** grupo `ReceptorSelectionPolicy` (15: T-043–056, T-123) + grupo `ResolvedReceptorSelection` (13: T-057–068, T-124) + grupo Persistência (18: T-069–080, T-125–130) = **46 cenários**.
- **Testes direcionados:** os 46 cenários acima.
- **Suíte completa:** reexecução integral acumulada (Checkpoint 1 + 2) = 70 + 46 = 116 cenários novos, mais a baseline herdada.
- **Restore point:** commit isolado.
- **Microrrevisão obrigatória:** confirmar ausência de `inspection_snapshot`/`label_asym_id_is_auth_equivalent` em `ResolvedReceptorSelection` (T-124); confirmar que nenhuma `ResolvedReceptorSelection`/`ReceptorSelectionPolicy` existe sob uma inspeção `"inspection-only"` (T-123, verificado indiretamente); confirmar que uma inspeção persistida nunca é duplicada por múltiplas resoluções (T-130).
- Nenhuma preparação química ou estrutura derivada é produzida neste checkpoint.

### Checkpoint 3 — Application Service + CLI + activity (incorpora F-01 na fronteira de serviço, F-06/F-07 na taxonomia)
- **Arquivos autorizados:** `receptor_service.py`, `cli.py` (aditivo), `tests/test_receptor_service.py`, `tests/test_cli.py` (aditivo).
- **Contratos:** as sete funções públicas da Seção 25.1; os sete comandos de CLI da Seção 29.1; logging de atividade completo com `inspection_id`.
- **Cenários normativos:** grupo Application Service (15: T-081–090, T-131–135) + grupo CLI (6: T-091–094, T-136–137) = **21 cenários**.
- **Testes direcionados:** os 21 cenários acima.
- **Suíte completa:** reexecução integral acumulada (Checkpoints 1–3) = 70 + 46 + 21 = 137 cenários novos, mais a baseline herdada.
- **Restore point:** commit isolado.
- **Microrrevisão obrigatória:** confirmar que `declare_receptor_selection` recusa `"inspection-only"` antes de qualquer validação de cadeia (T-131); confirmar que `ReceptorResolutionParserVersionConflictError` não existe mais em nenhuma parte do código (busca textual); confirmar que todo erro CLI passa por `_sanitize_cli_error_text` (T-093).
- Nenhuma preparação química ou estrutura derivada é produzida neste checkpoint.

### Checkpoint 4 — Validação cumulativa e handoff para o 021
- **Arquivos autorizados:** nenhum arquivo novo — apenas verificação.
- **Contratos:** confirmar que o contrato de leitura da Seção 34.1 é exercitável de ponta a ponta, incluindo `load_receptor_inspection` por `inspection_id`.
- **Cenários normativos:** nenhum novo — os 137 cenários anteriores são reexecutados integralmente.
- **Suíte completa:** reexecução integral de toda a baseline do repositório (herdada + os 137 novos), confirmando 0 falhas.
- **Restore point:** commit final deste incremento, antes de qualquer trabalho do 021.
- **Microrrevisão obrigatória:** checklist completo da Seção 36 (Critérios de Aceite) reexecutado contra o código real.
- Nenhuma preparação química ou estrutura derivada é produzida neste checkpoint — este é o último checkpoint do 020.

**Verificação aritmética explícita (corrige F-05permanentemente):** 70 (Checkpoint 1) + 46 (Checkpoint 2) + 21 (Checkpoint 3) + 0 (Checkpoint 4) = **137**, idêntico ao total da Seção 35.8. Cada subtotal de checkpoint foi recalculado nesta seção a partir de suas próprias faixas citadas, nunca copiado de um valor anterior sem reverificação — a causa raiz de F-05 (um número reaproveitado sem recontagem) é endereçada pelo próprio método de apresentação desta seção, não apenas pelo valor corrigido.

---

## 39. Riscos

Herdados da Seção 36 do Draft original, com dois riscos resolvidos (rebaixados a histórico) e nenhum risco novo introduzido pelas correções desta revisão:

- Confundir "decisão lógica" com "materialização física" — mitigado, inalterado (T-063, T-124).
- Tratar `ResolvedReceptorSelection` como uma representação molecular — mitigado, inalterado.
- Tratar qualquer engine de preparo como referência de design do core — proibido, inalterado.
- A tabela fechada de códigos CCD de íons metálicos pode ficar desatualizada — **mitigação reforçada nesta revisão**: o fallback para `"unknown"` em componentes monoatômicos não listados (Seção 17.1) já torna uma eventual incompletude da tabela honesta e visível, em vez de silenciosamente absorvida em `"other-non-polymer"`; uma revisão futura da tabela é expressa como incremento de `INSPECTION_PROFILE_VERSION` (Seção 15.1), sem ambiguidade.
- **Resolvido por esta revisão (histórico):** "ausência de um mecanismo de re-resolução sob uma nova versão de parser" (Seção 36 do Draft original) — este risco não existe mais: a arquitetura de pinagem por `inspection_id` (Seção 14) torna explícito, e correto, que uma resolução nunca migra silenciosamente para uma inspeção diferente; uma nova versão de parser produz uma nova inspeção independente, nunca um conflito a resolver.
- **Resolvido por esta revisão (histórico):** "risco de sobre-engenharia do `ReceptorInspectionReport` como um registry pleno" (Seção 36 do Draft original) — este risco é superado pela decisão explícita de persisti-lo create-once (Seção 14.1): o registro é simples (sem máquina de estados, Seção 26), e sua identidade determinística (Seção 15) é precisamente o nível de peso arquitetural proporcional à necessidade real que o risco original temia que fosse excedido.
- **Novo, próprio desta revisão:** a dependência de uma capacidade do Gemmi ainda não confirmada por teste de integração real (exposição estruturada de `SSBOND`/`LINK`/`CONECT`/`REMARK 465`/`470` para PDB legado, Seção 12.3/12.4) é uma decisão condicional explícita, não um TBD — mas seu desfecho concreto só será conhecido no Checkpoint 1. Mitigado por especificar completamente ambos os desfechos possíveis (Seção 12.4), de modo que, qualquer que seja o resultado, nenhuma decisão de implementação fica sem cobertura normativa.

---

## 40. Questões Abertas Não Bloqueantes

Herdadas da Seção 37 do Draft original, com uma questão resolvida (retirada) e nenhuma questão nova bloqueante introduzida:

1. Identidade secundária derivada de conteúdo (`semantic_key`-like) para `ResolvedReceptorSelection` — permanece não adotada (Seção 23.1), distinta do `inspection_id` desta revisão; aberta para um incremento futuro caso um caso de uso real surja.
2. **Retirada (resolvida por esta revisão):** "mecanismo de re-resolução sob uma nova versão de parser" — não existe mais como questão aberta; a arquitetura de pinagem por `inspection_id` torna a pergunta sem objeto (Seção 39).
3. Consolidação de proveniência documental das cópias do roadmap — herdada, não bloqueante, não decidida por este documento.
4. Possível extensão futura da tabela fechada de códigos CCD de íons metálicos — gerida por versionamento de `INSPECTION_PROFILE_VERSION` (Seção 15.1/17.2), não bloqueante.
5. Se e quando `ReceptorSelectionPolicy` deveria referenciar `ScientificConditionsDeclaration` — explicitamente adiada (Seção 28.1), não bloqueante.
6. Nomenclatura `kind="proteins"` vs. um futuro `kind="receptor"` dedicado — permanece como decidida por este incremento especificamente (reutiliza `kind="proteins"`), questão filosófica mais ampla não reaberta.
7. Mecanismo de revisão/supersedes para `ReceptorSelectionPolicy` — não necessário no 020, permanece uma possível melhoria futura.
8. **Nova nesta revisão:** confirmação, no Checkpoint 1, de qual dos dois desfechos da Seção 12.4 (`REMARK 465`/`470` estruturalmente exposto ou não) efetivamente se aplica ao Gemmi na versão travada — ambos os desfechos já estão completamente especificados (Seção 12.4), portanto esta não é uma lacuna normativa, apenas um fato de implementação a confirmar.

Nenhuma destas questões impede a declaração `READY FOR FINAL SHORT REVIEW: YES` (Seção 45) — nenhuma delas é uma lacuna normativa necessária à implementação do 020 como especificado.

---

## 41. Reconciliação dos 4 MAJORs

| ID | Problema (Adversarial Review) | Correção aplicada | Seção(ões) | Status |
|---|---|---|---|---|
| **F-01** | `label_entity_id` obrigatório (não opcional) em três modelos, sem caminho de derivação para PDB legado; risco de inferência geométrica silenciosa via `setup_entities()` | `label_asym_id`/`label_entity_id` tornam-se `Optional`, cada um com `*_origin: IdentityOrigin`; `selection_capability` bloqueia seleção/resolução sob identidade insuficiente; `setup_entities()`/heurísticas geométricas explicitamente proibidas | 10.3, 12, 15.4–15.6, 16.1–16.2, 17.4, 20, 21.4, 25.3 | **RESOLVED** |
| **F-02** | Gemmi descomprime `.gz` transparentemente; teto de 1 GiB verificado sobre tamanho em disco, nunca sobre conteúdo descomprimido | Rejeição integral de entrada comprimida, por extensão e por magic bytes, antes de qualquer chamada ao Gemmi; fluxo seguro de dez passos (Passo 0–9) | 10.5, 11.2, 11.3, 32.2–32.3 | **RESOLVED** |
| **F-03** | `StructConnEndpoint` de quatro campos, sem altloc nem operador de simetria; perda silenciosa de informação declarada pelo formato | `StructConnEndpoint` de treze campos, incluindo `label_alt_id`/`symmetry`; modelo unificado `StructureConnection` preservando distância, ordem de valor, papel, detalhes, flag de átomo que sai | 18 | **RESOLVED** |
| **F-04** | `ResolvedReceptorSelection` embute o `ReceptorInspectionReport` completo a cada resolução, sem deduplicação, sem reconhecimento de custo | `ReceptorInspectionReport` persistido create-once, identificado por `inspection_id` determinístico; `ReceptorSelectionPolicy`/`ResolvedReceptorSelection` referenciam por id, nunca embutem; elimina `ReceptorResolutionParserVersionConflictError` por construção | 14, 15, 21.2, 22.2, 23, 24, 25.2–25.4, 27.1, 34.1 | **RESOLVED** |

**Confirmação de completude:** 4 MAJOR listados na Seção 31 da Adversarial Review (`06-draft-review`). Todos os 4 aparecem na tabela acima, cada um corrigido por redesenho direto de modelo/mecanismo — nenhum por suavização de texto, nenhum por reclassificação de severidade.

---

## 42. Reconciliação dos 6 MINORs

| ID | Problema | Correção | Seção | Status |
|---|---|---|---|---|
| **F-05** | Checkpoint 1 declarava "56 cenários" para a faixa T-001–T-042 (soma real 42) | Checkpoints inteiramente redistribuídos com aritmética verificada explicitamente em cada passo (70+46+21+0=137); o próprio método de apresentação da Seção 38 recalcula cada subtotal a partir de suas faixas citadas, nunca copia um número sem reverificação | 38 | **RESOLVED** |
| **F-06** | `RawArtifactTooLargeError` ausente da tabela central de erros; `RawArtifactUnavailableError`/`InspectionFailureError` ausentes do mapeamento de banners; nenhum dos cinco limites de segurança tinha cenário de teste correspondente | As três classes têm linha completa na taxonomia (Seção 30.1); `InspectionFailureError` agora também aparece explicitamente na linha `PARSE ERROR` da tabela de banners, com contrato completo (classe, banner, exit code, sanitização, ausência de caminho absoluto, preservação de `KeyboardInterrupt`/`SystemExit`, impossibilidade de falso sucesso) imediatamente após a tabela — fechando a lacuna que a Short Adversarial Review (`08-revised-draft-review`, m-01) encontrou entre a prosa e a tabela real; T-104 testa o teto de tamanho explicitamente; os quatro tetos de contagem permanecem cobertos pelo comportamento de falha honesta já especificado, agora com `StructureConnection` também sob teto (Seção 32.2) | 29.3 (tabela de banners e contrato completo), 30.1, 32.2, 35.1 (T-104) | **RESOLVED** |
| **F-07** | `load_protein` propaga `yaml.YAMLError`/`pydantic.ValidationError` sem tradução; `inspect_receptor` não tinha classe de erro para um `ProteinInput` corrompido | Nova classe `ReceptorInputRecordInvalidError`, traduzida explicitamente em `inspect_receptor` (passo 2, Seção 25.2), com banner `RECORD INVALID` mapeado | 25.2, 29.3, 30.1 | **RESOLVED** |
| **F-08** | Gemmi expõe `remove_hydrogens()`/`remove_waters()`/`remove_ligands_and_waters()`/`remove_alternative_conformations()` sem proibição explícita de uso dentro do adapter | Proibição explícita adicionada à fronteira Gemmi | 10.3 | **RESOLVED** |
| **F-09** | Comportamento de activity logging indefinido para falhas de sintaxe de `--chain`/`--component` pré-Service | **Decisão explícita adotada e agora transcrita ao corpo normativo da Seção 29:** falhas de sintaxe puramente da CLI (antes de qualquer chamada à Application Service) seguem o mesmo padrão já estabelecido por `_validate_id_or_exit` — logam uma entrada `error` quando `project_dir`/`command` já são conhecidos no ponto da falha (ambos sempre conhecidos aqui, já que a resolução do experimento precede a análise de `--chain`/`--component`); a regra de propriedade dos eventos operacionais (Service como único proprietário de `started`/`succeeded`/`error`, CLI apenas apresentando o resultado) também está agora explícita no mesmo local — fechando a lacuna que a Short Adversarial Review (`08-revised-draft-review`, m-03) encontrou entre a tabela de reconciliação e o texto real da Seção 29 | 29.6 | **RESOLVED** |
| **F-10** | Divergência `raw_format_declared`/`structure_format` (T-012) corrigida silenciosamente, sem warning no vocabulário fechado | Vocabulário estendido de 14 para 15 códigos; novo `declared-format-mismatch` | 11.5, 19.1, 35.1 (T-012 reescrito) | **RESOLVED** |

**Confirmação de completude:** 6 MINOR listados na Seção 31 da Adversarial Review. Todos os 6 aparecem na tabela acima, cada um corrigido individualmente — nenhum tratado apenas como efeito colateral de uma correção MAJOR sem verificação própria.

---

## 43. Reconciliação das 10 NOTES

| ID | Observação da Adversarial Review | Evidência confirmada | Exigiu mudança normativa? | Seção afetada | Status |
|---|---|---|---|---|---|
| **N-01** | `ReceptorSelectionPolicy` não referenciava nenhum checksum/inspeção no momento da declaração; inofensivo porque o RAW é imutável | Confirmada como observação correta sobre o Draft original | **Sim, parcialmente** — não porque N-01 por si só exigisse, mas porque a correção de F-04 (Seção 14) naturalmente introduz `inspection_id`/`raw_checksum_observed` na política (Seção 21.2), fechando a lacuna de rastreabilidade que N-01 descrevia como inofensiva mas real | 21.2 | **RECONCILED** |
| **N-02** | Ausência de `semantic_key` em `ResolvedReceptorSelection` é decisão correta e bem fundamentada, não uma lacuna | Reconfirmada integralmente; o `inspection_id` desta revisão resolve um problema estrutural diferente (Seção 15.7) e não reabre N-02 | Não | 23.1 | **RECONCILED** |
| **N-03** | A frase "nunca sobrescrito" do cache de inspeção era ligeiramente mais forte que a garantia real sob concorrência multi-processo, mas sem contradição real dado o escopo de processo único já aceito | Superada: `receptor_inspections/` deixou de ser um "cache" informal e passou a ser um registry create-once guardado por `check_storage_identity_conflict` (Seção 24.2), com a mesma disciplina de identidade de armazenamento do resto do repositório — a imprecisão textual que N-03 apontava não existe mais, porque o mecanismo mudou | 24.2 | **RECONCILED** |
| **N-04** | Nenhum caminho indireto para materialização estrutural ou química foi encontrado em nenhuma parte do Draft original | Reconfirmada — nenhuma das quatro correções MAJOR herdadas, nem as sete correções mecânicas desta promoção, abre tal caminho (Seção 7) | Não | 7 (Fora de Escopo) | **RECONCILED** |
| **N-05** | Disponibilidade de wheels Windows do Gemmi 0.7.5 confirmada diretamente contra o PyPI | Reconfirmada, decisão do parser preservada (Seção 10.1) | Não | 10.1 | **RECONCILED** |
| **N-06/N-07** | Acesso de baixo nível a categorias mmCIF e ausência de conversão automática para PDB, ambos confirmados contra documentação oficial | Reconfirmadas, ambas preservadas sem alteração | Não | 10.1, 11.1 | **RECONCILED** |
| **N-08** | Rejeição do PDBFixer como parser central é tecnicamente sólida | Reconfirmada, preservada sem alteração | Não | 10.1 (herda Seção 10.3 do Draft original) | **RECONCILED** |
| **N-09** | Todos os seis comandos de CLI do Draft original eram implementáveis 1:1 pelas seis funções de Application Service especificadas | Reconfirmada e estendida: os sete comandos desta revisão permanecem implementáveis 1:1 pelas sete funções de Application Service (Seção 29.1 mapeia `receptor inspection show` → `load_receptor_inspection`) | Não (extensão proporcional, não uma correção) | 25.1, 29.1 | **RECONCILED** |
| **N-10** | `SSBOND`/`LINK`/`CONECT` e `REMARK 465`/`470` do PDB legado provavelmente desapareceriam do inventário sob leitura literal do Draft original; recomendação de decidir explicitamente | **Sim** — a observação identificava uma ambiguidade real que esta revisão decide explicitamente, em vez de deixar implícita | Sim | 12.3, 12.4 | **RECONCILED** |

**Confirmação de completude:** 10 NOTES listadas na Seção 31 da Adversarial Review. Todas as 10 aparecem na tabela acima. Nenhuma NOTE foi promovida a achado corretivo sem evidência concreta e distinta de uma simples preferência estilística (N-01 e N-10 são as únicas que motivaram mudança normativa, e ambas por razão explícita e rastreável, nunca por reclassificação arbitrária de severidade).

---

## 44. Critérios para a Revisão Final Curta

A Final Specification Candidate esteve pronta para, e foi efetivamente submetida a, uma **revisão final curta e focada** — não um novo ciclo de revisão adversarial completo — pelas razões abaixo, confirmadas pela Final Short Review (`12-final-review`):

1. A arquitetura central (Opção B, ausência de materialização, ausência de química) não foi tocada por nenhuma correção em nenhum estágio da linhagem; apenas corrigida em pontos específicos e nomeados.
2. Cada um dos quatro MAJOR herdados tem uma correção direta, rastreável e verificável contra o texto (Seção 41) — uma revisão final pode confirmar cada correção seção por seção, exatamente como as revisões anteriores já confirmaram.
3. Cada uma das sete correções mecânicas da candidata (m-02, m-04, m-05, m-06, n-01, n-02, n-03) é localizada, rastreável e verificável contra a Seção 19 da Corrected Revised Draft Confirmation e contra a tabela de reconciliação da Seção 45.1 desta especificação.
4. Nenhuma correção, em nenhum estágio, introduziu uma nova superfície de risco não examinada — a Seção 39 (Riscos) documenta explicitamente que nenhum risco novo surge, exceto uma dependência de capacidade de biblioteca já tratada como decisão condicional completa (não um TBD).
5. A matriz normativa, os checkpoints, e a allowlist permanecem mecanicamente verificáveis (Seções 35.8, 38, 37) — 137 cenários, contíguos, sem lacuna, sem duplicata — uma revisão final pode reexecutar essa verificação independentemente.

A Final Short Review confirmou, especificamente: (a) que F-01–F-04, F-05–F-10 e N-01–N-10 permanecem RESOLVED/RECONCILED sem reabertura; (b) a aritmética da Seção 35.8/38 (137 cenários, inalterada); (c) que cada uma das sete correções da candidata está localizada exatamente onde a Seção 19 do documento 10 autorizou, sem ampliação para temas adjacentes; (d) que a etiqueta de T-061 (n-02) é a única mudança dentro da matriz normativa, e que nenhum cenário foi renumerado, removido ou consolidado; (e) que o vetor golden da Seção 15.3 permanece corretamente especificado — e identificou três achados MINOR adicionais, puramente textuais e mecânicos (MINOR-01, MINOR-02, MINOR-03), corrigidos por este congelamento (Seção 45.5).

---

## 45. Bloco Terminal

### Verificação Final

- **Caminho deste documento:** `C:\Users\Pichau\Documents\MolecularGovernance\increments\020\13-final-specification\INCREMENT_020_FINAL_SPECIFICATION.md`.
- **Linhas, bytes UTF-8, SHA-256:** calculados e reportados após a escrita (ver resposta final) — um documento nunca pode conter seu próprio hash, pela mesma razão lógica já aceita nos documentos 09/10/11/12 desta linhagem.
- **Final Specification Candidate (`11-final-specification-candidate`):** verificada intacta — 1.943 linhas, 203.710 bytes UTF-8, SHA-256 `c25690681ac1a3a194c8645d0c44479b321b1c3881b2238e0c4c784f18a8dd23`, idêntico ao confirmado na Seção 3; não modificada por este trabalho.
- **Final Short Review (`12-final-review`):** verificada intacta — 214 linhas, 22.762 bytes UTF-8, SHA-256 `7f0096f5340fec04c375cc819871346b5a2d38e25fc0665d01c4b8490175dcbd`, idêntico ao confirmado na Seção 3; não modificada por este trabalho.
- **Corrected Revised Draft Specification (`09-corrected-revised-draft`):** verificado intacto — 1.884 linhas, 189.242 bytes UTF-8, SHA-256 `4db4836fbf9c1315dc742e99aa96844642068a6aac3b0d8863ee4164b7d74862`, idêntico ao confirmado na Seção 3; não modificado por este trabalho.
- **Corrected Revised Draft Confirmation (`10-correction-confirmation`):** verificada intacta — 326 linhas, 32.063 bytes UTF-8, SHA-256 `11875eecbe11ce683586d779dffe2cf3c3a96eb0a1ec12f7052745ad0123532c`, idêntico ao confirmado na Seção 3; não modificada por este trabalho.
- **Short Adversarial Review do Revised Draft (`08-revised-draft-review`):** verificada intacta — SHA-256 idêntico ao confirmado na Seção 3; não modificada por este trabalho.
- **Revised Draft Specification (`07-revised-draft-specification`):** verificado intacto — SHA-256 idêntico ao confirmado na Seção 3; não modificado por este trabalho.
- **Draft Specification (`05-draft-specification`):** verificado intacto — SHA-256 idêntico ao confirmado na Seção 3.
- **Adversarial Review do Draft (`06-draft-review`):** verificada intacta — SHA-256 idêntico ao confirmado na Seção 3.
- **Revised Discovery (`03-revised-discovery`):** verificado intacto.
- **Short Adversarial Review (`04-revised-discovery-review`):** verificada intacta.
- **Discovery original (`01-discovery`) e revisão adversarial original (`02-discovery-review`):** não foram reabertos nem modificados.
- **`increment-009-review.txt`** e **`_figura_curcumina/`:** intocados, não lidos, não movidos, não adicionados ao Git.
- **Repositório:** inalterado — `git status --short` permanece apenas `?? _figura_curcumina/` e `?? increment-009-review.txt`. Nenhum commit, branch, push, PR ou merge foi criado. Nenhum código foi alterado. Nenhum teste foi escrito ou executado.
- **Gemmi:** não instalado — confirmado antes e depois da escrita deste documento.
- **Nenhum spike foi executado.**
- **Único documento criado por este trabalho:** esta Final Specification, em `13-final-specification/`. Nenhum documento existente (01–12) foi alterado.

### Resumo para o leitor

- **MAJORs resolvidos (herdados):** 4/4 (Seção 41).
- **MINORs originais resolvidos (herdados):** 6/6 (Seção 42).
- **NOTES reconciliadas (herdadas):** 10/10 (Seção 43).
- **Achados residuais da Short Adversarial Review do Revised Draft, corrigidos pela candidata:** 4 MINOR residuais (m-02, m-04, m-05, m-06) + 3 NOTE residuais (n-01, n-02, n-03) = 7/7 (Seção 45.1 abaixo).
- **Achados residuais da Final Short Review, corrigidos por este congelamento:** 3 MINOR residuais, puramente textuais (MINOR-01, MINOR-02, MINOR-03) = 3/3 (Seção 45.5 abaixo).
- **Cenários normativos totais:** 137 (T-001–T-137), inalterado por este congelamento — 94 preservados/reescritos na linhagem 05→09 + 43 novos (T-095–T-137) na mesma linhagem; nenhum cenário `T-138+` foi acrescentado (via recomendada de m-02); a única mudança dentro da matriz é a etiqueta de T-061 (n-02, Seção 35.4), sem alteração de texto.
- **Allowlist:** inalterada em contagem de arquivos (7 módulos novos + `cli.py`/`pyproject.toml` aditivos + 7 arquivos de teste).
- **Checkpoints:** 4, com aritmética 70+46+21+0=137 verificada explicitamente (Seção 38), inalterada por este congelamento.
- **Questões abertas:** 8, todas não bloqueantes (Seção 40), inalteradas por este congelamento.

### 45.1 Reconciliação desta Promoção — Sete Correções Autorizadas pela Seção 19 da Corrected Revised Draft Confirmation (`10-correction-confirmation`)

A Final Specification Candidate (`11-final-specification-candidate`) aplicou **exclusivamente** as sete correções que a Seção 19 daquele parecer autorizou sobre os sete achados residuais declarados pela Short Adversarial Review do Revised Draft (`08-revised-draft-review`) como fora do escopo de correção do documento 09, e confirmados pelo documento 10 como mecânicos, localizados e seguros para aquela promoção:

| Achado | Natureza | Correção aplicada na candidata (`11`) | Seção normativa final | Status |
|---|---|---|---|---|
| **m-02** | MINOR — dos cinco tetos de contagem da Seção 32.2, apenas o teto de tamanho de arquivo (T-104) tinha cenário de teste dedicado | Via recomendada pela Seção 19.1 do documento 10: justificativa textual explícita adicionada à Seção 32.2, explicando por que o comportamento idêntico e inequívoco (warning `parser-limitation`, enumeração interrompida) já cobre os quatro tetos restantes sem exigir cenário dedicado por teto. **Nenhum cenário `T-138+` foi acrescentado** — a matriz permanece em 137 | 32.2 | **RESOLVED** |
| **m-04** | MINOR — a enumeração do fluxo seguro de leitura (Seção 11.3) não listava explicitamente a rejeição por extensão (Seção 11.2) como um de seus passos | Passo 0 explícito inserido na Seção 11.3, nomeando a rejeição por extensão como a primeira verificação do fluxo, executada antes do Passo 1 (abertura do arquivo) e de qualquer outra verificação | 11.3 | **RESOLVED** |
| **m-05** | MINOR — a Seção 11.2 não especificava normalização de case (`casefold()`/`.lower()`) na comparação da extensão declarada contra a lista fechada de extensões rejeitadas | Frase normativa explícita adicionada à Seção 11.2 determinando comparação via `Path.suffix.casefold()`; `.GZ`/`.Gz`/`.gZ` e variações equivalentes de `.bz2`/`.xz`/`.zip` não escapam da rejeição. Nenhuma normalização de conteúdo científico é introduzida — apenas comparação de sufixo de nome de arquivo | 11.2 | **RESOLVED** |
| **m-06** | MINOR — as tabelas das Seções 12.3/18.3 não cobriam o caso de ambos os parceiros de um `LINK`/`CONECT` legado classificados `"metal-ion"` (ponte metal-metal) | "Um parceiro classificado `metal-ion`" substituído por "pelo menos um parceiro classificado `metal-ion`" nas duas tabelas espelhadas (12.3 e 18.3); o caso de dois parceiros metálicos é agora classificado `metal_coordinations` de forma determinística, pela mesma regra que já classificava o caso de um único parceiro metálico. Nenhum balde de destino novo, nenhum redesenho de modelo | 12.3, 18.3 | **RESOLVED** |
| **n-01** | NOTE — `NonPolymerComponent` (Seção 17.4) não exibia o validador `_validate_origin_consistency` presente em `EntityInventoryEntry`/`ChainInventoryEntry` | Método `_validate_origin_consistency` adicionado a `NonPolymerComponent`, replicando literalmente o padrão já presente nos dois modelos análogos, com os mesmos nomes de campo | 17.4 | **RECONCILED** |
| **n-02** | NOTE — T-061 era etiquetado `[PRESERVADO]`, mas o texto do cenário descreve uma migração de mecanismo (de validador de modelo para comportamento de Service) | Etiqueta de T-061 corrigida de `[PRESERVADO]` para `[REESCRITO — mecanismo]`; texto do cenário inalterado | 35.4 | **RECONCILED** |
| **n-03** | NOTE — a Seção 15.6 usava "pelo menos uma", enquanto as Seções 12.3/18.3 usavam "um parceiro classificado" em contexto semanticamente análogo | Terminologia padronizada para "pelo menos um" nas Seções 12.3/18.3, aplicada na mesma passagem de edição que resolve m-06 — a mesma expressão normativa ("pelo menos um") agora é usada em toda ocorrência análoga desta especificação | 12.3, 15.6, 18.3 | **RECONCILED** |

**Mudanças técnicas no contrato introduzidas por esta promoção:** um validador de consistência campo↔origem em `NonPolymerComponent` (n-01, não observável externamente — apenas rejeita uma construção já logicamente inconsistente); nenhuma outra mudança de modelo, campo, classe de erro, fluxo de serviço, comando de CLI ou regra de persistência. As demais seis correções (m-02, m-04, m-05, m-06, n-02, n-03) são redação normativa mais precisa sobre comportamento já vinculante — nenhuma delas altera o resultado observável de nenhum caminho de código já especificado.

**Cenários normativos: 137 (T-001–T-137), inalterados em contagem.** Nenhum cenário foi adicionado, removido, renumerado ou consolidado por esta promoção. A única mudança dentro da matriz normativa é a etiqueta de T-061 (n-02) — texto do cenário inalterado. A Seção 37 (Allowlist) e a Seção 38 (Checkpoints) permanecem com as mesmas contagens de arquivos e de cenários do documento 09.

**Achados confirmados pelo documento 10 como já resolvidos antes desta promoção (histórico, não reabertos aqui):** M-01 (referências cruzadas), F-06 (banner de `InspectionFailureError`), F-09 (propriedade de activity logging) — ver Seção 45.2 abaixo.

### 45.2 Reconciliação Histórica — Short Adversarial Review do Revised Draft (`08-revised-draft-review`), corrigida pelo Corrected Revised Draft Specification (`09-corrected-revised-draft`)

O documento 09 corrigiu **exclusivamente** os três achados que aquela revisão autorizou corrigir sobre o Revised Draft Specification (`07-revised-draft-specification`) — preservados sem reabertura por esta promoção:

| Achado | Natureza | Correção aplicada no documento 09 | Local normativo | Status |
|---|---|---|---|---|
| **M-01** (novo MAJOR) | Cinco referências cruzadas internas citavam "Seção 30" como se fosse "Escopo Negativo"; a Seção 30 real é "Erros" | Cinco citações corrigidas: (1) linha do Resumo Executivo (Seção 4) → `(Seção 7)`; (2) linha da Seção 13 (visão geral dos modelos) → `(Seção 27.2)`; (3) linha da Seção 22.3 (o que `ResolvedReceptorSelection` prova) → `(Seção 7)`; (4) Critério de Aceite 1 (Seção 36) → `(Seção 7)`; (5) reconciliação de N-04 (Seção 43) → `(Seção 7)` na evidência e `7 (Fora de Escopo)` na coluna "Seção afetada". Nenhum contrato técnico tocado | Seções 4, 13, 22.3, 36, 43 | **RESOLVED** |
| **F-06** (MINOR, parcialmente resolvido) | `InspectionFailureError` ausente da linha `PARSE ERROR` da tabela de banners (Seção 29.3), apesar de a prosa já alegar o mapeamento | `InspectionFailureError` adicionada explicitamente à linha `PARSE ERROR`; contrato completo acrescentado imediatamente após a tabela | Seção 29.3 | **RESOLVED** |
| **F-09** (MINOR, não efetivamente resolvido no corpo normativo) | A decisão de propriedade de activity logging para falhas de sintaxe CLI pré-Service existia apenas na tabela de reconciliação (Seção 42), não no texto da Seção 29 | Nova Seção 29.6 transcreve a decisão já formulada, com a regra completa de propriedade dos eventos operacionais | Seção 29.6 | **RESOLVED** |

Confirmado pelo documento 10 (Seções 5–7) e reconfirmado aqui por herança: nenhuma mudança técnica adicional nessas três correções; a Seção 35 (Matriz Normativa), a Seção 37 (Allowlist) e a Seção 38 (Checkpoints) do documento 09 permanecem byte a byte idênticas às do documento 07 **nessas passagens** — a única mudança dentro da matriz normativa em toda a linhagem 07→09→11 é a etiqueta de T-061 introduzida por esta promoção (n-02, Seção 45.1).

### 45.3 Diff Conceitual 09 → 11

Nenhuma outra linha do documento 09 foi tocada além das listadas abaixo. As sete correções da Seção 45.1, mais o framing documental de promoção (título, Natureza, Seções 1–3, 36, 44, 45), são as únicas mudanças:

1. **m-02** — Seção 32.2: parágrafo de justificativa textual acrescentado após a tabela de limites.
2. **m-04** — Seção 11.3: "Passo 0" acrescentado antes do Passo 1 (passos 1–9 inalterados em texto e numeração).
3. **m-05** — Seção 11.2: frase normativa de `casefold()` acrescentada ao bullet de extensões rejeitadas.
4. **m-06** — Seções 12.3 e 18.3: "um parceiro" → "pelo menos um parceiro" em quatro linhas de tabela (duas por seção), mais nota explicativa em 12.3.
5. **n-01** — Seção 17.4: método `_validate_origin_consistency` acrescentado a `NonPolymerComponent`, mais nota explicativa.
6. **n-02** — Seção 35.4: etiqueta de T-061 corrigida de `[PRESERVADO]` para `[REESCRITO — mecanismo]`; texto do cenário inalterado.
7. **n-03** — mesmas Seções 12.3/18.3 do item 4 (correção conjunta, conforme autorizado pela Seção 19.7 do documento 10).

**Confirmado:** nenhuma outra seção, modelo, classe de erro, comando de CLI, regra de persistência, cenário normativo, checkpoint ou entrada de allowlist foi tocada por esta promoção.

### 45.4 Tabela Final de Promoção

| Item | Estado nesta especificação |
|---|---|
| Novo MAJOR de referências cruzadas (M-01) | **Resolvido** (herdado do documento 09, Seção 45.2) |
| F-01–F-04 (MAJOR originais) | **4/4 Resolvidos** (herdados, Seção 41) |
| F-05–F-10 (MINOR originais) | **6/6 Resolvidos** (herdados, Seção 42; inclui F-06/F-09 reconfirmados pelo documento 10, Seção 45.2) |
| N-01–N-10 (NOTES) | **10/10 Reconciliadas** (herdadas, Seção 43) |
| m-02, m-04, m-05, m-06 (MINOR residuais) | **4/4 Resolvidos na candidata** (Seção 45.1) |
| n-01, n-02, n-03 (NOTE residuais) | **3/3 Reconciliadas na candidata** (Seção 45.1) |
| MINOR-01, MINOR-02, MINOR-03 (MINOR da Final Short Review) | **3/3 Corrigidos neste congelamento** (Seção 45.5) |
| Mudanças técnicas introduzidas pela candidata | Um validador não-observável (`NonPolymerComponent._validate_origin_consistency`, n-01); demais seis correções são redação normativa, sem mudança de comportamento |
| Mudanças técnicas introduzidas por este congelamento | Nenhuma — as três correções MINOR deste congelamento são exclusivamente textuais/aritméticas (referência cruzada e duas contagens de prosa), sem alterar modelo, validador, classe de erro, fluxo de serviço, comando de CLI, regra de persistência, cenário normativo ou checkpoint |
| Impacto na matriz normativa | Nenhum cenário novo; nenhuma remoção; nenhuma renumeração; 137 cenários (T-001–T-137) preservados; única mudança em toda a linhagem: etiqueta de T-061 (n-02) |

### 45.5 Reconciliação da Revisão Final Curta — Três Correções Autorizadas pela Seção 19 da Final Short Review (`12-final-review`)

Esta especificação aplica **exclusivamente** as três correções que a Seção 19 da Final Short Review autorizou sobre os três achados MINOR que aquela revisão identificou — todos efeitos colaterais textuais/aritméticos das próprias correções m-04 e m-02 da candidata, nunca regressões em território não tocado pela promoção 09→11:

| Achado | Natureza | Correção aplicada neste congelamento | Seção normativa final | Status |
|---|---|---|---|---|
| **MINOR-01** | Referência cruzada obsoleta na Seção 40: citava `READY FOR SHORT REVISED DRAFT REVIEW: YES` como o campo ativo do bloco terminal (Seção 45), nome de campo que não existe em nenhum bloco terminal desta linhagem desde o documento 09 | `READY FOR SHORT REVISED DRAFT REVIEW: YES` substituído por `READY FOR FINAL SHORT REVIEW: YES` | 40 | **RESOLVED** |
| **MINOR-02** | A Seção 11.3, após a correção m-04 da candidata, enumera Passos 0–9 (dez passos no total), mas duas passagens herdadas (Seção 4, bullet F-02; Seção 41, linha F-02) ainda diziam "fluxo seguro de nove passos" | As duas ocorrências de "fluxo seguro de nove passos" substituídas por "fluxo seguro de dez passos (Passo 0–9)"; os Passos 0–9 em si (texto e numeração) permanecem inalterados | 4, 41 | **RESOLVED** |
| **MINOR-03** | O parágrafo de justificativa textual acrescentado à Seção 32.2 pela correção m-02 da candidata continha um erro de contagem interno: a tabela de limites daquela seção lista seis linhas, mas o parágrafo dizia "cinco limites"/"cinco tetos" (3 ocorrências) e "quatro tetos restantes" (2 ocorrências) — 6 − 1 = 5, não 4 | "Cinco limites"/"cinco tetos" substituído por "seis limites" (3 ocorrências); "quatro tetos restantes" substituído por "cinco tetos restantes" (2 ocorrências); nenhuma outra alteração no parágrafo; nenhum valor de limite ou cenário alterado | 32.2 | **RESOLVED** |

**Mudanças técnicas no contrato introduzidas por este congelamento: nenhuma.** As três correções são, respectivamente, uma referência cruzada corrigida e duas contagens de prosa corrigidas — nenhuma toca modelo, validador, classe de erro, fluxo de serviço, comando de CLI, regra de persistência, cenário normativo (`T-xxx`), checkpoint ou entrada de allowlist.

**Cenários normativos: 137 (T-001–T-137), inalterados em contagem.** Nenhum cenário foi adicionado, removido, renumerado ou consolidado por este congelamento. A única mudança dentro da matriz normativa, em toda a linhagem, permanece a etiqueta de T-061 (n-02), já aplicada pela candidata.

### 45.6 Diff Conceitual 11 → 13

Nenhuma outra linha da Final Specification Candidate foi tocada além das listadas abaixo. As três correções da Seção 45.5, mais o framing documental de congelamento (título, Natureza, Seções 1–3, 36, 44, 45), são as únicas mudanças:

1. **MINOR-01** — Seção 40: referência cruzada corrigida (uma ocorrência).
2. **MINOR-02** — Seções 4 e 41: contagem de passos corrigida (duas ocorrências, mesma frase exata em cada local).
3. **MINOR-03** — Seção 32.2: aritmética do parágrafo de justificativa corrigida (cinco ocorrências no total: três de "cinco limites/tetos", duas de "quatro tetos restantes").

**Confirmado:** nenhuma outra seção, modelo, classe de erro, comando de CLI, regra de persistência, cenário normativo, checkpoint ou entrada de allowlist foi tocada por este congelamento.

```
INCREMENT 020 FINAL SPECIFICATION COMPLETE: YES
HEAD VERIFIED: YES
INPUT DOCUMENTS PRESERVED: YES
FINAL REVIEW RECONCILED: YES
FINAL REVIEW MINORS CORRECTED: 3/3
AUTHORIZED CORRECTIONS ONLY: YES
F-01-F-04 RESOLVED: 4/4
F-05-F-10 RESOLVED: 6/6
N-01-N-10 RECONCILED: 10/10
RESIDUAL MINORS RESOLVED: 4/4
RESIDUAL NOTES RECONCILED: 3/3
OPTION B PRESERVED: YES
GEMMI DECISION PRESERVED: YES
PDB LEGACY IDENTITY PRESERVED: YES
COMPRESSED INPUT POLICY COMPLETE: YES
STRUCT_CONN FIDELITY PRESERVED: YES
INSPECTION CREATE-ONCE PRESERVED: YES
STRUCTURAL MATERIALIZATION IN 020: NO
NEW ATTEMPT STATE MACHINE: NO
NORMATIVE MATRIX RECONCILED: YES
NORMATIVE SCENARIOS: 137
CHECKPOINTS: 4
MANDATORY SPIKES FOR 020: NO
READY FOR IMPLEMENTATION: YES
FINAL SPECIFICATION FROZEN: YES
IMPLEMENTATION PERFORMED: NO
REPOSITORY MODIFIED: NO
```








