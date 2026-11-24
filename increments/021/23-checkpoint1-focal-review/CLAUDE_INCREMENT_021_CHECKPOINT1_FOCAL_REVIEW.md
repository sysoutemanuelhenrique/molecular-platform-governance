# Incremento 021 — Revisão focal independente das correções do Checkpoint 1

Revisor: Claude (sessão de revisão independente, separada do arquiteto e das duas sessões implementadoras). Data: 2026-11-24. Tarefa: `tasks/021-CHECKPOINT1-FOCAL-REVIEW.json`.

**Veredito: REQUEST CHANGES** (correções focais e pequenas; nenhuma reabertura arquitetural). CP1 não aprovado por este parecer; CP2 não autorizado. 020-A permanece em STAND-BY.

## 1. Snapshots e identidades fixadas

Verificado por `git ls-remote` antes e depois da revisão, sem deriva:

| Referência | Esperado | Observado |
|---|---|---|
| governance `docs/020-a-candidate1-review-20261020` | `155661115851c2a5fb70f5d905425baeb4d23c9f` | igual |
| governance `main` | `a47183dfec8213c765ed43ae482c8c227760a3d5` | igual |
| código `feature/increment-021-receptor-materialization` | `42b4804b5f4ea01ddf320c45473d8b4f980ea67e` | igual |
| código `main` | `08b797e0985e123ffd4d7ca7e5a5e8f040e63851` | igual |
| relatório de correções `claude/021-cp1-corrections-20261124` | `010ee93aedf31bdcdfee513164b84aa40f3fbde4` | igual |
| revisão anterior `claude/021-cp1-adversarial-review-20261124` | `2e36222b087134f9ba725bc2ad96c3ba39fb8801` | igual |

Cadeia do código confirmada: `08b797e → 711f307 → 3ba2fa9 → 42b4804`, duas correções aditivas, cumulativamente apenas os dois arquivos da allowlist. A branch do relatório tem dois commits (`452f12e` com pai `521500c`, depois `010ee93`) e adiciona somente os onze arquivos próprios.

Identidades conferidas (linhas / bytes / SHA-256):

- `src/molecular/receptor_materialization.py` @42b4804: 1669 / 75461 / `ef38b524adbbe7432e83171d63c675856e3b21777322faec001efab530704fb1` (blob `f6e130c1…`).
- `tests/test_receptor_materialization.py` @42b4804: 1421 / 67030 / `7064aa8d7e36902f9e85a3ae4e075b118f8b5dd391029bf9652a53cbdd883eb8` (blob `55aa9a46…`).
- Especificação congelada (`b0e60f6`): 377 / 64746 / `5de705d6…`. Anexos SCHEMAS `649b4334…`, CATALOG `8561039f…`, SCENARIOS `ca5c8830…` e IDENTITY_BASIS `14636992…` coincidem.
- Reconciliação: 90 / 16130 / `8b1c19f8…`. Recibo do arquiteto: 73 / 10422 / `09796cbe…`. Relatório de correções: 154 / 14940 / `5e03d83a…`. Manifesto das correções: 108 / 4903 / `70e516de…`. Revisão anterior: 176 / 15726 / `2af4f188…`. Os dois manifestos têm todas as entradas OK.
- O log da suíte completa foi lido pelos bytes do blob (`67f5d86a…`, 3003 bytes, SHA-256 `15c40b93…`), não por texto recodificado.

## 2. Método e limites de execução

- O código ficou somente leitura e foi copiado para scratch externo. Nada foi gravado no fonte: nenhum bytecode, `__pycache__` ou `.pytest_cache` (contagem 0, verificada após cada execução). Ambiente Linux, Python 3 do sandbox, sem rede, sem Gemmi nem RDKit instalados.
- **Prova de importação (ARCH-01):** processo novo `python3 -I -B`, com `sys.modules["gemmi"] = None` e `sys.modules["rdkit"] = None`, sem stub. A prova correu nos modos normal e `-O`. Evidência: `claude-blocked-import-probe.*`.
- **Sondas de domínio:** usam um sentinela inerte de `gemmi` (o `__getattr__` lança erro), para importar as classes DTO reais do 020 (`ReceptorInspectionReport`, `ResolvedReceptorSelection`). O sentinela **não** é prova de importação; serve apenas para construir objetos tipados reais. As 59 sondas registram o esperado e o observado. Evidência: `claude-domain-probes.*` e `claude-inert-gemmi-sentinel.py`.
- Os 75 testes focais correram com o sentinela (`pytest -p no:cacheprovider`): **75 passed**. Isso prova que os testes passam aqui, não que os módulos nativos funcionam.
- **Não executado:** Windows, Gemmi 0.7.5 nativo, RDKit e a suíte completa. Os números 1551 passed + 5 skipped (Python 3.14.7, Windows) são **fornecidos**, não reexecutados. Os cinco skips atuais estão nomeados no log, mas a alegação histórica de que "são os mesmos cinco" não pode ser estabelecida pelo log `-q` antigo.
- Contagens de coleta reconciliadas a partir dos arquivos de coleta: 1524 antes, 1556 depois, +32, 0 removidos, sem duplicatas. A diferença é composta inteiramente por itens de `test_receptor_materialization.py`. São 43 → 75 funções e 0 parametrizações.

## 3. Disposição individual das doze correções funcionais

| ID | Disposição | Severidade residual |
|---|---|---|
| ARCH-01 | **FECHADO** (código); a prova dedicada do legado fica em MINOR-7 | — |
| ARCH-02 | **FECHADO** | — |
| ARCH-03 | **FECHADO** | — |
| MAJOR-A | **PARCIAL** | MINOR (bloqueante para a aprovação do CP1) |
| MAJOR-B | **FECHADO** | — |
| MINOR-1 | **FECHADO** (com observação) | — |
| MINOR-2 | **FECHADO** (com observação) | — |
| MINOR-3 | **PARCIAL** | MINOR (bloqueante) |
| MINOR-4 | **FECHADO** | — |
| MINOR-5 | **FECHADO** | — |
| MINOR-6 | **FECHADO** | — |
| MINOR-7 | **PARCIAL** | MINOR (bloqueante) |

### ARCH-01 — fechado

Processo limpo com Gemmi e RDKit bloqueados, sem stub, nos modos normal e `-O`:

- Nenhum módulo nativo, nem `molecular.receptor_inspection` ou `receptor_resolution` do 020, é carregado antes ou depois da execução.
- O pipeline puro funciona de ponta a ponta: `build_source_context` → planner → `build_policy_record`, com `source_context_key` `5ea39c48dd36…`, `plan_key` `b6c596d7e6c8…` e `policy_id` `874a82fb01a6…`.
- Os tipos antigos ficam só sob `TYPE_CHECKING`.
- `_compute_legacy_inspection_id` reconstrói os sete campos e usa `compute_semantic_key` puro.
- Um golden calculado à mão, de forma independente (`1c217d99e7b2b09d9c31a0c8f9daf056c48aa916bdf957cae83df449ad68e80c`), coincide com o helper novo no processo bloqueado e com o helper antigo do 020 no processo com sentinela.
- O código do 020 não foi alterado.

O teste dedicado `test_minor7_golden_legacy_inspection_id_matches_the_020_production_helper` é tautológico: compara o helper antigo com uma constante derivada do próprio helper antigo e nunca chama o helper novo. Essa lacuna de evidência é tratada em MINOR-7; não invalida o fechamento em código.

### ARCH-02 — fechado

Os dois sentidos foram reproduzidos com objetos reais:

- `remove (A,GLY)` com GLY só em M=2 mantém A/ALA em M=1 (`selected-asym`).
- `keep (B,MSE)` com MSE só fora de M deixa B não selecionado como `chain-complement`.
- Os controles com os mesmos pares presentes em M continuam recusando com `SELECTION_CONFLICT`.
- A máscara `model-filter` é preservada.

Nenhuma retenção ou remoção mudou fora da tabela S/D/U.

### ARCH-03 — fechado

`_cell` e `_symmetry` com `filter` + `generated_tags=("entry_id",)` e tags disjuntas são aceitos. `omit` e `guard_then_omit` com linha retida continuam recusados, assim como a sobreposição kept/omitted. Nenhum serializer CP2 foi introduzido.

### MAJOR-A — parcial

O que fecha:

- Ambos os parsers são exigidos em gemmi/0.7.5 (`ENGINE_VERSION`), e essa verificação vem antes da de identidade.
- Formato de resolução divergente e formato pdb coerente em todos os registros dão `INVALID_RECORD`.
- Checksum de acquisition divergente dá `CHECKSUM_MISMATCH`.
- `protein_input_id` divergente, tanto no ProteinInput quanto na policy, dá `IDENTITY_MISMATCH`.
- `ProteinInput` e `ReceptorSelectionPolicy` tipados são recebidos.
- Não há fallback de inspect/resolve nem leitura de YAML/RAW.

O que não fecha. A §5 manda "Conferir … formato" entre os registros carregados, e o escopo da tarefa inclui explicitamente "acquisition and declared-versus-observed formats". `build_source_context` nunca lê `acquisition.raw_artifact.format` nem `inspection.raw_format_declared`. Três casos são aceitos:

1. `acquisition.format = "pdb"` e `raw_format_declared = "pdb"`, conteúdo detectado `mmcif`, com o próprio aviso `declared-format-mismatch` do 020 presente no relatório: **aceito**.
2. `acquisition.format = "mmcif"` contra `inspection.raw_format_declared = "pdb"` (os registros discordam entre si): **aceito**.
3. `acquisition.format = raw_format_declared = "xyz"`: **aceito**.

O alias `cif → mmcif` é aceito, mas apenas porque nada é comparado, não por suporte explícito ao alias do código primário (`_DECLARED_FORMAT_ALIASES` do 020).

**Correção pedida:**

- Comparar `acquisition.raw_artifact.format` com `inspection.raw_format_declared`, por igualdade exata ou pelo mapa de aliases do 020, sem reclassificar a proveniência.
- Decidir de forma explícita a divergência entre declarado e detectado: recusar com o código de configuração existente adequado (`INVALID_RECORD`), ou documentar e testar a aceitação apoiada no aviso `declared-format-mismatch`.
- Adicionar um controle negativo para cada caso.

O impacto científico direto é baixo, porque o RAW é vinculado por checksum e o formato detectado é exigido como mmcif. Ainda assim, é um critério contratual explícito não atendido.

### MAJOR-B — fechado

- Um `policy_id` arbitrário é recusado no próprio DTO (`policy_id does not match H() of its own declared payload`).
- Um `existing` adulterado em U ou em `source_context_key` é recusado com `SOURCE_CHANGED`, sem sobrescrita.
- A adulteração de contagens é recusada já na validação do DTO.
- A repetição legítima devolve **o mesmo objeto** existente com o `declared_at` original (2026-01-01), ignorando o novo (2099).

`SOURCE_CHANGED` pertence ao conjunto fechado existente. Não confundo isso com integridade de bytes de arquivo, que é CP3.

### MINOR-1 — fechado

Cada guarda recusa com `INVALID_ID`:

- ordinal duplicado;
- `atom_id` duplicado entre modelos;
- `entity_id` contraditório dentro do mesmo asym;
- asym de S ausente em M, inclusive quando existe só em outro modelo.

O controle multimodelo válido conserva os ordinais de origem (3, 7), sem renumeração. Observação não bloqueante: o `label_entity_id` da cadeia resolvida (`E7`) não é cruzado com o `entity_id` dos átomos (`E1`) e é aceito. Hoje a fonte de ambos é a mesma inspeção; convém cruzar no CP2, quando o adaptador DOM existir.

### MINOR-2 — fechado

Recusam com `UNSUPPORTED_REQUEST`:

- água NFD contra polímero NFC;
- ligante NFD contra polímero NFC.

Um token idêntico em asyms distintos continua `multiple`, e a combinação `retained-polymer`/`excluded-polymer` continua correta. Observação não bloqueante: o índice NFC cobre todos os tokens de M, inclusive um ligante **selecionado** sem entrada em O. Isso é mais amplo do que o exigido e pode recusar uma entrada legítima rara; é aceitável no CP1, mas deve ficar registrado como decisão.

### MINOR-3 — parcial

O que fecha:

- omissão vazia com `source_rows_key`;
- `filter` + `generate` com fonte;
- `generate` sem fonte com chave nula;
- recusa de ordinal negativo e de sobreposição;
- recusa de categoria fora do catálogo e de maiúsculas;
- recusa de família com `filter`;
- recusa de `filter` sem fonte e de linhas sem fonte.

O que não fecha, apesar dos critérios explícitos ("ordinais … únicos"; "nomes inválidos recusam"):

1. `kept_row_ordinals=(0,0)` e `omitted_row_ordinals=(0,0)` são **aceitos**. O validador só verifica sobreposição entre as duas tuplas, não duplicatas dentro de cada uma.
2. A validação das famílias é um `startswith` simples. São **aceitos**:
   - `"_em_example\n"` (LF);
   - `"_em_"` (prefixo nu, sem categoria);
   - `"_pdbx_nmr_ x"` (espaço);
   - `"_em_entity.id"` (nome de item, não de categoria).

**Correção pedida:**

- Exigir unicidade dentro de cada tupla.
- Exigir que o nome de família seja prefixo aprovado seguido de pelo menos um caractere de uma gramática canônica de nome de categoria: minúsculas, dígitos e `_`, sem ponto, espaço ou controle.
- Adicionar um controle negativo para cada caso.

Sem campo novo e sem adaptador DOM.

### MINOR-4 — fechado

- `catalogue_sha256` divergente é recusado em `PlanBinding` e em `PolicyRecord` (`Literal`).
- `Engine` 0.7.4 e 0.7.6 são recusados.
- `profile` e `algorithm` fora do vigente são recusados.
- Variações documentais do dicionário (rotuladas como tal) mudam o hash para `profile`, `algorithm`, `catalogue`, `engine` e `atom_decisions_key`, e `plan_key = H(dump)`.
- O teste do `request_key` cobre as quatro dimensões.
- `application_version` participa apenas do `request_key`.

### MINOR-5 — fechado

Formato pdb coerente em todas as fontes dá `INVALID_RECORD` (configuração), não `UNSUPPORTED_PLATFORM`. A ordem de validação foi preservada.

### MINOR-6 — fechado

Nos modos normal e `-O`, um código desconhecido é recusado nas duas classes de erro (`ValueError` explícito, sem `assert`). Os códigos válidos conservam `code`/`phase` (`plan`/`metadata`). Não há `except` amplo nem `assert` de validação no módulo.

### MINOR-7 — parcial

Os testes golden usam bytes canônicos escritos à mão (bom) para JSON canônico, `atom_ids`, ocorrência e chave de conexão vazia. Mas:

1. O SHA-256 esperado é calculado em tempo de execução com `hashlib` sobre esses bytes, não fixado como literal independente, como pedido ("bytes e SHA-256 literais independentes").
2. Faltam envelopes representativos de contexto, X/O, decisões, policy e request.
3. A prova do `inspection_id` legado é tautológica (ver ARCH-01).

**Correção pedida:**

- Fixar literais SHA-256 para cada vetor.
- Adicionar ao menos um golden literal por envelope listado.
- Fazer o teste legado comparar o helper **novo** com o literal independente `1c217d99…`, calculado aqui sem chamar código de produção, e opcionalmente também o helper antigo.

## 4. NOTES

- **NOTE-1 — preservada.** A estrutura parcial do CP1 não é persistida nem reutilizada como plano final. Não há conexão real, catálogo físico, armazenamento ou materialização.
- **NOTE-2 — preservada.** Todos os doze DTOs são `strict`/`frozen`/`forbid`. São recusados: surrogate em id nativo, `bool` como contagem e `float` como tamanho. Não há `except` amplo; a ordem e o encadeamento foram mantidos. Evidência: `claude-note2-strictness.output.json`.
- **NOTE-3 — preservada.** CLI e módulos 020/017/018/019 inalterados (diff restrito à allowlist). O gate de import/help sem opcionais fica para CP4.

Observação adicional não bloqueante: `build_source_context` recebe inspection/resolution por duck typing, sem verificação de tipo em runtime (as anotações são strings sob `TYPE_CHECKING`). É coerente com ARCH-01; o chamador CP2 deve passar os DTOs reais carregados.

## 5. Pontos residuais do recibo do arquiteto, confrontados de forma independente

| Candidato do recibo | Resultado independente |
|---|---|
| Ordinais duplicados em `CategoryDecision` aceitos | **Confirmado** (MINOR-3) |
| Nome malformado de família de omissão aceito | **Confirmado**, e é mais amplo: LF, prefixo nu, espaço e nome de item |
| Contradições acquisition/`raw_format_declared` aceitas | **Confirmado** (MAJOR-A), mais a divergência declarado/detectado |
| Completude da prova de regressão de hash | **Incompleta** (MINOR-7): SHA não literal, envelopes ausentes, teste legado tautológico |

Nenhum desses resultados foi aceito por autoridade: cada um tem uma sonda com esperado e observado em `claude-domain-probes.output.json`.

## 6. Testes nominais e reconciliação dos 43 cenários

- Os 75 testes passam aqui com o sentinela. **Testes nominais não equivalem a suficiência:** todos os resíduos acima passam despercebidos pelos 75 testes.
- Os 43 IDs normativos `T021-001…040` e `159…161` continuam presentes. Os 43 nomes originais foram preservados, e nenhum foi excluído ou enfraquecido.
- Classificação independente por cenário: **40 provados / 3 parciais por desenho (T021-018, T021-024, T021-038, restritos ao CP1) / 0 lacunas**, o que confirma a alegação no nível de cenário.
- Ressalva: os resíduos de MAJOR-A e MINOR-3 ficam fora do enunciado literal de T021-006 (ids/hashes) e T021-161 (omissão vazia). Por isso o fechamento dos cenários não implica o fechamento dos achados.

## 7. Correções de apresentação (sem editar o relatório do implementador)

- São doze mudanças funcionais (4 MAJOR + 8 MINOR), não onze.
- O JSON de disposições tem quinze registros (incluindo as três NOTES), não treze.
- O `code_commit_parent` do manifesto aponta o baseline `08b797e`. O pai direto de `42b4804` é `3ba2fa9`.

## 8. Escopo, regressão e veredito

- Escopo respeitado: sem parser nativo, materialização, storage, registry ou CLI. Os módulos 020/017/018/019 estão inalterados. Não houve regressão observada nas sondas de controle.
- **REQUEST CHANGES**, limitado a três correções focais no mesmo par de arquivos:
  1. MAJOR-A: conferência de formato acquisition/declarado/detectado.
  2. MINOR-3: unicidade intra-tupla e gramática canônica dos nomes de família.
  3. MINOR-7: SHA literais, envelopes golden e teste legado não tautológico.
- Depois delas, espera-se aprovação com notas não bloqueantes, numa revisão focal curta.
- Este parecer não aprova o CP1, não autoriza o CP2 e não altera `main`, PR, merge, tag ou release.

## 9. Evidências publicadas

Em `increments/021/23-checkpoint1-focal-review/evidence/`:

- `claude-blocked-import-probe.py` e `.output.txt` (normal e `-O`)
- `claude-domain-probes.py` e `.output.json` (59 sondas)
- `claude-note2-strictness.output.json`
- `claude-inert-gemmi-sentinel.py` (somente para construir DTOs; não é prova de importação)
- `claude-pytest-75-with-sentinel.txt`
- `claude-evidence-identities.json`
