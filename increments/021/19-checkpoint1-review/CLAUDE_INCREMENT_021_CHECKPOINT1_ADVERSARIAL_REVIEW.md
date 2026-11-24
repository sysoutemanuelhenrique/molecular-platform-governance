# Revisão adversarial independente — Incremento 021, Checkpoint 1

Tarefa: `021-CHECKPOINT1-ADVERSARIAL-REVIEW`. Papel: Claude, revisor independente, separado do implementador. Data: 24/11/2026, America/Sao_Paulo.

Escopo: o código do CP1 (`711f307`) contra o contrato congelado (`b0e60f6`), os 43 cenários, o relatório do implementador e a triagem do arquiteto. A triagem não foi aceita como prova; cada ponto foi reproduzido sobre o código de produção intocado. Este parecer não autoriza o CP2, não corrige código e não altera contrato. O 020-A segue em STAND-BY.

**Veredito: REQUEST CHANGES.**

- ARCH-01 e ARCH-02 foram confirmados como MAJOR; ARCH-03, como MINOR.
- Encontrei de forma independente mais dois MAJORs: cruzamentos de fonte incompletos, com proveniência de parser falsificável, e integridade da política existente não verificada.
- Há 7 MINORs.
- Não há BLOCKER. A canonicalização, a estritez dos DTOs, a lógica S/D/U/X/O de modelo único e os reconhecimentos P-1/P-2 estão corretos e bem testados.
- Todas as correções cabem nos dois arquivos da allowlist, sem mudar o contrato.

## 1. Gates, identidades e materiais

**HEADs remotos antes de revisar:**

| Ref | HEAD |
|---|---|
| coordenação governance | `d577b0dfddd3c71f9287b4c9cdcc783ea0865654` |
| main do governance | `a47183df…` |
| branch do relatório | `51752b4ce7603d1f14677b0b030edc176b9df13f` |
| feature do código | `711f3070765efe67a5799f939f1a18306ed8afdd` |
| main do código | `08b797e0985e123ffd4d7ca7e5a5e8f040e63851` |

- O código tem pai único, a baseline, e o diff traz exatamente dois arquivos novos (A/A).
- A branch do relatório tem base `3cda329` e acrescenta só os 8 arquivos próprios.

**Identidades conferidas:**

| Item | Linhas | Bytes | SHA-256 |
|---|---|---|---|
| `receptor_materialization.py` | 1.418 | 60.988 | `b4a59696…` |
| `test_receptor_materialization.py` | 791 | 38.057 | `ae8af3f9…` |
| especificação congelada | 377 | 64.746 | `5de705d6…` |
| autorização do responsável | 55 | 4.625 | `589eb029…` |
| relatório do implementador | 160 | 15.963 | `135a4460…` |
| triagem do arquiteto | 67 | 8.807 | `540d6aed…` |

Também conferem os quatro anexos normativos e as quatro evidências da triagem.

**Ambiente próprio:** Linux, Python 3.13.18, Pydantic 2.13.5 (a mesma do implementador), pytest 9.1.1, sem Gemmi e sem rdkit; nada instalado. O código veio de um `git archive` do `711f307` para scratch externo. Nenhum bytecode ou cache foi gravado na cópia (contagem: 0).

## 2. Execução própria e limites

1. **Import em processo novo, sem Gemmi e sem stub** (`claude-import-probe.*`). `inputs` e `receptor_selection` importam; `receptor_resolution`, `receptor_inspection`, `receptor_parsing` e `receptor_materialization` falham com `ModuleNotFoundError: gemmi`.
2. **Sentinela inerte** (`claude-inert-gemmi-sentinel.py`): qualquer atributo levanta exceção. Fica fora da árvore e só deixa o import avançar até a lógica pura. Não prova nada sobre o comportamento nativo nem sobre importar sem Gemmi.
3. **Testes do implementador com o sentinela:** 43 coletados, 43 passam, 0 parametrizações (`claude-pytest-new-tests-with-sentinel.txt`).
4. **Sondas de domínio próprias** (`claude-domain-probes.*`): 23 casos, cada um com o esperado pelo contrato e o observado.
5. **Canonicalização e estritez** (`claude-canonical-and-strict.*`): bytes canônicos escritos à mão comparados ao hash de produção, e varredura de configuração e coerção.
6. **`python -O`**: sonda do conjunto fechado de códigos de erro.

**Não executado:** suíte completa (depende de Gemmi e rdkit reais), Gemmi real, Windows e concorrência. Os números 1.481, 1.524 e 1.519/5 vêm dos logs do implementador; conferi só a aritmética: 1.481 + 43 = 1.524 = 1.519 + 5. O log `-q` não identifica quais são os 5 skips, então não posso confirmar que já existiam na baseline.

## 3. Disposição individual de ARCH-01/02/03

### ARCH-01 — import transitivo de Gemmi no domínio puro: **CONFIRMADO, MAJOR**

**Cadeia reproduzida:** `receptor_materialization.py:53` → `receptor_inspection.py:28` → `receptor_parsing.py:33` (`import gemmi`). Isso viola o §3 do contrato: "Import tardio no adapter; falta/versão divergente gera erro de configuração, sem impedir --help/import de módulos puros", com Gemmi como extra opcional `structure` no `pyproject.toml`. Viola também o §20 ("imports/help sem opcionais") e o T021-040.

**O T021-040 não detecta o problema:** faz busca textual e `hasattr` (`test_receptor_materialization.py:733–743`). O próprio arquivo de testes importa `receptor_inspection` e `receptor_resolution` no topo, então nem roda sem Gemmi.

**Conflito entre o brief e o contrato, resolvido sem ampliar a allowlist:** no módulo, os nomes do 020 só aparecem em anotações, que são strings por causa de `from __future__ import annotations` (linhas 370, 374 e 913), e numa chamada a `compute_inspection_id` (443). Reuso e pureza de import são compatíveis:
- mover os imports de `ReceptorInspectionReport` e `ResolvedReceptorSelection` para um bloco `TYPE_CHECKING`;
- importar `compute_inspection_id` tardiamente dentro de `build_source_context`, preservando exatamente o payload e o hash antigos.

O contrato tem precedência sobre a frase do brief. Não é preciso reimplementar o helper.

**Teste exigido:** subprocesso novo com Gemmi bloqueado (por exemplo `sys.modules['gemmi'] = None`), importando o módulo de domínio sem stub.

A falha *pré-existente* do 020 não é atribuída a este checkpoint: na baseline, `cli.py` já importa `receptor_parsing` no topo. Fica como NOTE para o CP4.

### ARCH-02 — disposição com chave ausente em M afeta polímero em M: **CONFIRMADO, MAJOR**

Em `receptor_materialization.py:928–938`, `disposition_remove_asyms` e `disposition_keep_asyms` são agregados por asym sobre **todas** as chaves, antes da projeção em M. O ramo polimérico (967–985) só consulta o asym. O ramo não polimérico está correto, porque consulta `(asym, ccd)` por ocorrência em M.

**Sondas** (`claude-domain-probes.output.json`):

| Caso | Esperado (§7) | Observado |
|---|---|---|
| controle sem D (A/ALA em M=1, A/GLY em M=2) | ALA retido | aceito, retido |
| S=A, D remove (A,GLY), GLY só em M=2 | sem efeito | **SELECTION_CONFLICT** |
| S=A, D remove (A,ALA) presente em M | SELECTION_CONFLICT | SELECTION_CONFLICT |
| B fora de S, D keep (B,MSE), MSE só em M=2 | B excluído por complemento | **SELECTION_CONFLICT** |
| B fora de S, D keep (B,ALA) presente em M | SELECTION_CONFLICT | SELECTION_CONFLICT |
| D keep sobre asym ausente de M | sem efeito | aceito |

O erro é fail-closed: recusa entradas válidas e não aceita inválidas. Ainda assim, contraria diretamente o §7 ("chave ausente em M não tem efeito"). O T021-019 não fornece nenhuma disposição, então não cobre o cenário.

**Correção:** decidir os conflitos poliméricos só com as chaves `(asym, ccd)` que ocorrem em M. Estender o T021-019 aos dois sentidos (remove em S e keep fora de S).

### ARCH-03 — `CategoryDecision` proíbe tag gerada em `filter`: **CONFIRMADO, MINOR**

O catálogo congelado declara `_cell` e `_symmetry` como `action=filter`, com `generate_tags=['entry_id']`; o §11 manda derivar `entry_id` (DERIVED_ENTRY/SOURCE_FRAME_SINGLETON). O validador (`:785–787`) rejeita: "filter must not generate tags". Nas duas categorias reais, a sonda dá `ValidationError`; `_entry` com `generate` é aceito.

Classifico como MINOR porque é fail-closed, o CP1 não constrói decisões a partir do catálogo e o erro apareceria de imediato no CP2. Mesmo assim, é uma restrição implementada que contradiz um anexo normativo, e a correção deve entrar no ajuste deste checkpoint, com cenário para filter+generate.

## 4. Achados independentes

### MAJOR-A — `build_source_context` não faz os cruzamentos de fonte exigidos pelo §5

O §5 exige "parser gemmi 0.7.5" da inspeção e manda "conferir protein_input_id, inspection_id, checksums acquisition/raw_checksum_observed/raw_checksum, formato e parser". O código (`:390–480`) faz menos:

- **Parser da inspeção nunca é conferido.** Só `resolved_selection.parser` é. Uma inspeção feita por **gemmi 0.7.4**, com `inspection_id` coerente, é **aceita**, e o `SourceContext` registra `parser=gemmi/0.7.5` (sonda `IND_inspection_parser_0.7.4_resolution_0.7.5`). A proveniência sai falsificada no `source_context_key` e no `plan_key`.
- **`resolved_selection.structure_format` não é comparado** com o da inspeção: resolução `pdb` com inspeção `mmcif` é aceita.
- **Checksum de `acquisition` do `ProteinInput` não é conferido.** A função recebe só `protein_input_id`, sem o `ProteinInput`.
- **`protein_input_id` da política não é conferido.** A função recebe três escalares da política e omite esse campo.

O T021-005 e o T021-006 não cobrem esses casos.

**Correção:** receber os registros tipados necessários (ou os escalares faltantes), exigir a igualdade dos parsers e a igualdade gemmi/0.7.5 em ambos, comparar formatos e checksum de acquisition, e testar cada divergência.

### MAJOR-B — a política existente é aceita sem verificar integridade nem equivalência (§13; T021-030)

O §13 diz que a "declaração repetida retorna a política existente depois de verificar integridade e equivalência". O brief do CP1 coloca essa prova no CP1 ("CP1 prova identidade/equivalência de política e preservação do record/timestamp por funções puras").

O código (`:1361–1363`) só compara `existing.policy_id == policy_id` e então constrói um record **novo** com o `declared_at` antigo. Não verifica o resto do `existing`, e `PolicyRecord` não valida o próprio `policy_id`.

**Sonda:** um `existing` adulterado (mesmo `policy_id`, `unaddressed_components` trocado) é aceito em silêncio; um `PolicyRecord` com `policy_id` arbitrário (`eeee…`) é construído sem erro.

**Correção:** recalcular o `policy_id` do `existing` a partir do próprio payload e exigir igualdade campo a campo com o record que seria produzido (exceto `declared_at`); devolver o existente. Divergência é erro tipado, nunca sobrescrita. Validar o `policy_id` no `PolicyRecord`. Testar com o existente adulterado.

### MINORs

- **MINOR-1 — cobertura de `AtomDecision` e vínculos de M.** O SCHEMAS §4 manda "cobrir exatamente uma vez todo ordinal" e o §6 exige `atom_site.id` único e vínculo inequívoco. Sondas: ordinal duplicado gera 2 decisões; `atom_id` duplicado é aceito; `entity_id` contraditório no mesmo asym é aceito, e `XEntry` usa o primeiro visto (`setdefault`, `:961`); asym de S ausente em M é aceito em silêncio. O adapter do CP2 deveria garantir isso, mas o planner é a guarda declarada. Recusar com código do conjunto fechado.
- **MINOR-2 — NFC não injetivo entre os tokens envolvidos (§6).** A injetividade só é verificada entre auth ids de polímeros (`:989–994`). Um auth id de água NFD, igual por NFC ao auth id NFC de um polímero, é classificado como `retained-polymer`, ou seja, fundido, quando o §6 exige recusa. Não muda a retenção.
- **MINOR-3 — invariantes de `CategoryDecision`** (SCHEMAS §4: "quando a categoria é omitida, nenhuma tag/linha sobrevive"; Ordinal ≥ 0):
  - `omit` e `guard_then_omit` aceitam `kept_row_ordinals` não vazio, um fail-open;
  - ordinais negativos são aceitos;
  - `category` não é validada como canônica nem como membro do catálogo;
  - a regra de `source_rows_key` nulo não é imposta.

  Corrigir junto com o ARCH-03.
- **MINOR-4 — catálogo não fixado nos DTOs e estímulos parciais.** `PlanBinding` e `PolicyRecord` aceitam qualquer `catalogue_sha256` (a sonda aceita `ffff…`), embora o T021-005 peça "catalogue divergente → erro de configuração". O T021-035 só varia `application_version` e `policy_file_sha256`, sem profile, catalogue nem engine. O T021-160 só varia decisões.
- **MINOR-5 — código `UNSUPPORTED_PLATFORM` para inspeção que não é mmCIF** (`:403–407`). Pelo §4, "plataforma" é o perfil de host; o próprio docstring (`:115–123`) diz que esse código nunca é emitido pelo módulo. Usar `INVALID_RECORD` ou `INCOMPLETE_INSPECTION`. As demais escolhas declaradas pelo implementador (`SELECTION_CONFLICT` para U=require, `UNSUPPORTED_REQUEST` para NFC e tipos) cabem no conjunto fechado e não as contesto.
- **MINOR-6 — conjunto fechado de códigos via `assert`** (`:109`, `:133`). Sob `python -O`, `MaterializationInputError('NOT_A_CODE')` é aceito. Usar `raise` explícito.
- **MINOR-7 — testes sem golden values.** O brief exige "golden values independentes" para hashes, mas os testes só comparam igualdade e desigualdade. Calculei bytes canônicos à mão (ordem de chaves, compactação, UTF-8 sem escape, listas preservadas, envelopes de ocorrência, de ids atômicos e de conexão vazia) e todos coincidem com a produção. A implementação está correta, mas falta prova regressiva disso nos testes.

### NOTES

- **NOTE-1:** `connection_decisions_key` vazio, a ausência de `ConnectionDecision` e a ausência dos records futuros (Summary, Manifest, Audit) são recortes declarados e aceitáveis no CP1. O plano do CP1 não é materialização, e um `plan_key` do CP1 não deve ser reutilizado nem persistido como plano final no CP2.
- **NOTE-2:** a estritez está verificada nos 12 modelos novos; o substituto UTF-16 isolado é recusado pelo `str` estrito; a ordem de validação segue o §16 (engine → vínculos → seleção); não há `except` amplo; o encadeamento `from` é usado em TimeUTC.
- **NOTE-3:** a importação do CLI já exigia Gemmi na baseline 020 (`cli.py:79–80`). Isso é tema do gate do CP4 ("imports/help sem opcionais"), não defeito do CP1.

## 5. Reconciliação dos 43 cenários

Os 43 IDs (T021-001–040 e 159–161) estão mapeados 1:1 a 43 funções reais, sem parametrização, todas chamando produção. Classificação da prova:

- **Provados (31):** T021-001, 002, 003, 004, 007, 008, 009, 010, 011, 012, 013, 014, 015, 016, 017, 020, 021, 022, 023, 025, 026, 027, 028, 031, 032, 033, 034, 036, 037, 039 e 159.
- **Parciais (10):** T021-005 e 006 (MAJOR-A, MINOR-4); 018 (sem altloc/H/D no DTO; uniformidade estrutural aceitável no CP1); 024 e 038 (`hydrog`/`metalc` são CP2; aceitável); 029 (bytes não exercitados em `declared_by`, embora a estritez cubra); 030 (MAJOR-B); 035 e 160 (MINOR-4); 161 (ARCH-03, MINOR-3).
- **Lacunas (2):** T021-019 (ARCH-02) e T021-040 (ARCH-01).

## 6. Mudanças exigidas para reapresentação (somente nos dois arquivos)

1. **ARCH-01:** imports tardios ou `TYPE_CHECKING`, mais um teste de import em subprocesso com Gemmi bloqueado.
2. **ARCH-02:** projeção das chaves D em M no ramo polimérico; T021-019 com disposições nos dois sentidos.
3. **MAJOR-A:** todos os cruzamentos do §5, com um teste por divergência.
4. **MAJOR-B:** verificação de integridade e equivalência do `existing`, `policy_id` autovalidado e teste de adulteração.
5. **ARCH-03 e MINOR-1–7.**

Feito isso, uma revisão focal do diff basta. Esses itens não exigem tocar o contrato, o 020 nem o CP2.

## 7. Veredito

**REQUEST CHANGES.** O CP1 não está aprovado e o próximo gate é a correção do implementador. Este parecer não autoriza o CP2.

VERDICT: REQUEST CHANGES
ARCH-01: CONFIRMED MAJOR; ARCH-02: CONFIRMED MAJOR; ARCH-03: CONFIRMED MINOR
INDEPENDENT: 0 BLOCKER, 2 MAJOR, 7 MINOR, 3 NOTE
SCENARIOS: 31 PROVED / 10 PARTIAL / 2 GAP OF 43
CHECKPOINT1 APPROVED: NO
CP2 IMPLEMENTATION AUTHORIZED: NO
CODE REPOSITORY MODIFIED: NO
ARCHITECT DOCUMENTS MODIFIED: NO
INCREMENT 020-A: STAND-BY
