# Checkpoint 1 implementation report — Increment 020-A

Autor: Claude (Sonnet 5), sessão implementadora separada. Data: 2026-10-20.
Natureza: relatório de execução real do Checkpoint 1 ("DTOs/perfis/adaptador") do
Incremento 020-A, conforme autorização registrada em `tasks/020-A-CHECKPOINT1.json`
(status `AUTHORIZED`) e `increments/020-A/08-final-specification/
OWNER_FREEZE_AND_CP1_AUTHORIZATION.md`. Não é revisão independente; aguarda revisão
independente antes de qualquer liberação do Checkpoint 2.

## 1. Identidade e autorização confirmadas antes da implementação

Lido integralmente, byte a byte, no snapshot de governance
`85ce45ce5cc635d75035664dd612ca6c0a839dac` (branch
`docs/020-a-candidate1-review-20261020`), antes de qualquer código:

- `AGENTS.md`, `CLAUDE.md`, `STATUS.md` desse snapshot.
- `tasks/020-A-CHECKPOINT1.json`: `status="AUTHORIZED"`, `authorization_scope=
  "CHECKPOINT_1_ONLY"`, `allowed_code_paths` = exatamente os quatro caminhos abaixo,
  `execution_started=false` no momento da leitura.
- `increments/020-A/08-final-specification/INCREMENT_020_A_FINAL_SPECIFICATION.md`,
  lido integralmente (586 linhas). SHA-256 recalculado localmente sobre o blob lido
  via `git show <commit>:<path>`:
  `cfbc6ea4bbb58f987deb3f73e45fc39d5b79d0cfaa2de8e0a7870a9937386e9c`; 71.904 bytes;
  586 linhas — **idêntico** ao publicado na tarefa e no `STATUS.md`.
- `increments/020-A/08-final-specification/OWNER_FREEZE_AND_CP1_AUTHORIZATION.md`,
  lido integralmente no mesmo snapshot — confirma a aprovação "aprovado" do
  responsável e o escopo delimitado a quatro arquivos, sem Checkpoints 2/3, sem
  PR/merge.

Nenhuma dessas leituras foi repetida como "novo estudo"; a revisão documental já
encerrada (fechamento Claude, commit `7f1f75219203eb1a691e454db170900ca81536e8`) não
foi refeita.

## 2. Repositório de código — preflight

- Remoto confirmado: `https://github.com/sysoutemanuelhenrique/molecular-platform.git`
  (único remoto, `origin`).
- `origin/main` após `git fetch`: **`08b797e0985e123ffd4d7ca7e5a5e8f040e63851`** —
  idêntico à baseline exigida pela tarefa. (A branch `main` local do checkout
  principal do usuário estava desatualizada em `23a3a8e...`, um ancestral de
  `08b797e...` por `pull --ff-only` histórico; isso não é avanço de `main`, apenas
  cache local defasado, confirmado por `git merge-base --is-ancestor`.)
- `feature/increment-020-a-molecular-characterization`: **inexistente** em
  `origin` no preflight, confirmado por `git rev-parse --verify
  origin/feature/increment-020-a-molecular-characterization` (falhou).
- Nenhum trabalho inesperado encontrado na branch pretendida; nenhuma interrupção
  foi necessária.
- **Worktree isolado**: `git worktree add ../molecular-platform-020a-cp1 -b
  feature/increment-020-a-molecular-characterization
  08b797e0985e123ffd4d7ca7e5a5e8f040e63851`, preservando sem alteração o checkout
  anterior do usuário (`C:\Users\Pichau\molecular-platform`, branch
  `feature/increment-020-receptor-preparation-foundation`, com seus próprios
  untracked `_figura_curcumina/` e `increment-009-review.txt` — nenhum dos dois foi
  tocado nesta sessão, em nenhum momento).

## 3. Escopo implementado — exatamente quatro arquivos

| Caminho | Natureza | Linhas | Bytes |
|---|---|---:|---:|
| `src/molecular/characterization.py` | novo | 1054 | 39.713 |
| `src/molecular/rdkit_tautomer.py` | modificado (só adições + 1 linha de import ampliada) | +680 inserções, −1 | — |
| `tests/test_characterization.py` | novo | 718 | 23.916 |
| `tests/test_rdkit_tautomer.py` | modificado (só adições) | +643 inserções, 0 remoções | — |

`git diff --stat` completo contra a baseline: `4 files changed, 3094 insertions(+), 1
deletion(-)`. A única linha removida é a própria linha de import ampliada em
`rdkit_tautomer.py` (`from rdkit.Chem import rdMolDescriptors` →
`from rdkit.Chem import Descriptors, rdMolDescriptors`) — nenhuma função, classe ou
comportamento pré-existente foi removido, renomeado ou alterado. Confirmado por
inspeção linha a linha do diff (nenhuma outra linha começando com `-` em nenhum dos
dois arquivos modificados).

Nenhum outro arquivo foi tocado. `increment-009-review.txt` e `_figura_curcumina/`
não foram tocados (não existem no worktree isolado, que parte de um clone limpo da
baseline — a verificação é vácua por construção, mas confirmada: `git status`
no worktree, antes e depois, nunca listou esses caminhos).

### 3.1 `characterization.py` — o que foi implementado

DTOs frozen/`extra=forbid` para os dez valores (`CharacterizationValues`), os blocos
`effective_parameters` de caracterização e desenho (Seção 11), `DrawingResult`,
`CharacterizationProvenance` e `MolecularCharacterizationResult` completos (Seção 11
— construídos nesta etapa apenas a partir de valores sintéticos de teste, nunca de um
`MolecularState` real: leitores/serviço são Checkpoint 2, não implementados). A
taxonomia de erros completa da Seção 13: `CharacterizationError` e as quatro
subclasses de categoria, cada uma com vocabulário fechado de `reason` validado no
próprio construtor (decisão de design: um `reason` fechado por categoria, em vez de
uma subclasse Python por `reason`, diferente do estilo anterior de
`rdkit_tautomer.py` — mais fiel à Seção 13's própria descrição "cada uma possui
reason do vocabulário fechado"). O validador/vinculador fechado de SVG (Seção
10/10.1/10.2) via `xml.parsers.expat` puro — **sem nenhum import de rdkit**,
confirmado por teste estático (`ast`) que verifica a ausência de qualquer `import
rdkit`/`from rdkit...` no código-fonte do módulo.

Não implementados nesta etapa (fora do escopo autorizado): leitores verificados
(`VerifiedBytes`/`atomic.py`), `characterization_service.py`, `cli.py` — nenhum
desses arquivos foi tocado ou criado.

### 3.2 `rdkit_tautomer.py` — o que foi adicionado

`characterize_molecule_rdkit(representation_bytes, *, input_format, input_state_id,
representation_sha256, include_svg=False) -> RDKitCharacterizationOutcome`, mais suas
funções privadas de apoio: gramática SDF/SMILES (Seção 7.1/7.2), elegibilidade do
grafo (Seção 7.3), limites de tamanho (Seção 6, somente átomos/ligações — os limites
de bytes de registro/representação pertencem aos leitores do Checkpoint 2 e não foram
duplicados aqui), os dez valores (Seção 8), e o pipeline opcional de desenho/SVG
(Seções 9/10), delegando a validação/vinculação do SVG para
`characterization.validate_and_bind_depiction_svg`.

A separação de disponibilidade de cálculo versus desenho da Seção 15 foi respeitada:
um segundo bloco `try/except ImportError` próprio
(`_RDKIT_DRAWING_IMPORT_ERROR`) para `RDConfig`/`rdDepictor`/`rdMolDraw2D`, nunca
sobrescrevendo o `_RDKIT_IMPORT_ERROR` legado. `Descriptors` (necessário para
`molar_mass_g_mol`) foi adicionado ao bloco de import **de cálculo** existente, não
ao de desenho, porque é uma dependência de cálculo, não de desenho.

A função pública usa exatamente uma chamada ao motor de parsing (Seção 12, passo
4/5: "uma vez") e suprime logs nativos do RDKit com `rdBase.BlockLogs()` em escopos
mínimos, restaurados em sucesso e em falha (Seção 13) — verificado por teste com
`capfd` (Seção 7 abaixo).

## 4. Ambiente de validação

```
Python: 3.11.9 (CPython, Windows, MSC v.1938 64 bit AMD64)
rdkit (pip):      2026.3.6
rdkit.rdBase.rdkitVersion (observado em runtime): 2026.03.6
pydantic:         2.14.1
pytest:           9.1.1
typer:            0.27.3
PyYAML:           6.0.3
gemmi:            0.7.5
xml.parsers.expat (EXPAT_VERSION): expat_2.6.0
SO: Windows-10-10.0.26200-SP0 (Windows 11 Pro, build 26200)
```

RDKit, gemmi e as demais dependências foram instaladas em um ambiente virtual novo
(`python -m venv`) dedicado a este checkpoint, a partir de
`pip install -e ".[dev,rdkit]"` seguido de `pip install "gemmi==0.7.5"` — nenhuma
alteração a `pyproject.toml` ou a qualquer arquivo de dependência. RDKit real e
produtivo, não mock, executado localmente nesta sessão (não é reaproveitamento de
sondagem/pesquisa anterior).

Um segundo ambiente virtual, deliberadamente **sem** o extra `rdkit`, foi usado para
confirmar a fronteira opcional (Seção 15, T-020A-006) de forma independente.

## 5. Comandos executados e resultados — coleta reconciliada

### 5.1 Suíte focal — `tests/test_characterization.py` (novo arquivo)

```
pytest tests/test_characterization.py -q
→ 111 passed in 0.23s
```

Não requer RDKit (confirmado: os mesmos 111 testes passam, idênticos, no ambiente
virtual sem o extra `rdkit` instalado).

### 5.2 Suíte focal — `tests/test_rdkit_tautomer.py` (arquivo existente, ampliado)

```
pytest tests/test_rdkit_tautomer.py -q
→ 142 passed in 3.33s
```

62 testes pré-existentes (idênticos byte a byte à baseline — nenhuma linha removida
do arquivo) + 80 testes novos desta etapa. No ambiente sem o extra `rdkit`, o arquivo
inteiro é pulado via o `pytest.importorskip("rdkit")` de escopo de módulo
pré-existente (`1 skipped` — comportamento inalterado).

### 5.3 Suíte completa do projeto

```
pytest tests/ -q
→ 1667 passed, 5 skipped in 63.88s
```

Baseline (mesma suíte, mesmo ambiente, antes de qualquer alteração desta sessão, na
baseline `08b797e...`): **1476 passed, 5 skipped**. Delta: **+191 testes aprovados**,
**0 regressões**, **0 skips novos**. 191 = 111 (novos em `test_characterization.py`)
+ 80 (novos em `test_rdkit_tautomer.py`), reconciliado exatamente.

No ambiente sem o extra `rdkit` (com `gemmi` instalado, mas sem `rdkit`): 1489
passed, 8 skipped (os testes que dependem de RDKit ficam skip/falham de forma já
pré-existente e não relacionada a este checkpoint — ver Seção 6.4, limitação
registrada, não uma regressão introduzida aqui).

### 5.4 Higiene de diff e árvore de trabalho

```
git diff --check   → saída vazia, exit code 0 (sem erros de whitespace)
git status (antes) → working tree limpa na baseline, após git worktree add
git status (depois, antes do commit) → exatamente os 4 arquivos autorizados
                       modificados/novos; nenhum outro caminho tocado
```

Staging explícito por caminho (`git add src/molecular/characterization.py
src/molecular/rdkit_tautomer.py tests/test_characterization.py
tests/test_rdkit_tautomer.py`) — nunca `git add .` nem `-A`.

## 6. Reconciliação cenário → função/teste → resultado

A matriz da Seção 16 da especificação final contém 80 cenários contratuais que
cobrem todos os três checkpoints. O Checkpoint 1 autoriza apenas DTOs/perfis/
adaptador — a tabela abaixo reconcilia os cenários efetivamente aplicáveis a este
checkpoint. Cenários de leitores verificados, plataforma Windows/NTFS, serviço e CLI
(Checkpoints 2/3) **não são exercitados aqui** e estão marcados como tal; nenhum
deles foi implementado ou testado nesta etapa.

| Cenário(s) | Função/arquivo | Testes (itens coletados) | Resultado |
|---|---|---|---|
| T-020A-001 a 005 | `CharacterizationValues`, `CharacterizationProvenance`, `MolecularCharacterizationResult`, `RDKitCharacterizationOutcome`, `DrawingResult` (characterization.py) | `test_characterization.py`: 1 (`test_module_never_imports_rdkit`) + 7 (`test_extra_field_is_rejected_on_every_dto`, parametrizado) + 1 + 3 (frozen) + 2 + 5 + 2 + 2 + 3 (não-finito/bool/negativo) + 1 + 6 (consistência svg/drawing e hash/tamanho) = 33 itens | Todos passaram; recusa tipada, imutabilidade, NaN/inf/bool/contagem negativa, consistência svg/drawing e hash/tamanho confirmadas |
| T-020A-006 (parcial — só a parte de import, não `--help`, que é CLI/Checkpoint 3) | módulo `characterization.py` | `test_module_never_imports_rdkit` (AST) + execução completa da suíte focal em venv sem `rdkit` | characterization.py nunca importa rdkit; importável e 100% testável sem o extra |
| T-020A-007 | `_resolve_characterization_engine` | `test_characterization_engine_unavailable_on_missing_import`, `test_characterization_engine_unavailable_on_version_mismatch` | CONFIGURATION ERROR/`engine-unavailable`, sem parse/cálculo/fallback |
| T-020A-008 (parcial — sem a parte "enumeração preservada" de CLI) | `_RDKIT_DRAWING_IMPORT_ERROR` | `test_drawing_unavailable_does_not_affect_calculation_only_requests`, `test_enumeration_still_works_after_characterization_additions` | Cálculo sem figura funciona com desenho indisponível; figura falha configuração; enumeração existente intacta |
| T-020A-009/010 (defensivo, não é o validador de ID do serviço do Checkpoint 2) | validação de `input_state_id` dentro do adaptador | `test_input_state_id_rejected_before_engine_access` (parametrizado, 7 casos), `test_input_state_id_is_preserved_verbatim_case_sensitive` | ID malformado recusado como `invalid-request` antes de qualquer acesso ao motor; ID válido preservado verbatim no SVG |
| T-020A-011 a 026 | — | — | **Fora de escopo do Checkpoint 1** (leitores/plataforma/caminho — Checkpoint 2); nenhuma linha de código correspondente existe nesta etapa |
| T-020A-026 (só a parte "formato desconhecido", a normalização de `representation.format` é do serviço) | `_parse_molecule_rdkit` | `test_unsupported_format_is_configuration_error` | `unsupported-format` sem sniffing |
| T-020A-027 a 033 | `_validate_sdf_grammar`, `_parse_molecule_rdkit` | 12 testes (`test_sdf_*`) | Gramática física SDF exata — um registro, delimitador exato, CRLF/LF, substring `$$$$` não é delimitador, NUL/BOM recusados |
| T-020A-034 a 037 | `_validate_smiles_grammar` | 1 (child real da enumeração) + 2 (terminadores) + 10 (parametrizado, violações) + 1 (não-ASCII) + 1 (NUL/DEL) = 15 testes | Gramática física SMILES exata |
| T-020A-038/039 | `_validate_graph_eligibility` | `test_disconnected_salt_is_rejected`, `test_dummy_atom_is_rejected`, `test_sgroup_is_rejected_by_eligibility_check`, `test_enhanced_stereo_groups_are_rejected_by_eligibility_check` (×2), `test_absolute_stereo_group_is_not_rejected_by_eligibility_check`, `test_empty_molecule_is_rejected` | `unsupported-structure` correto; SGroup e stereo AND/OR testados contra objetos RDKit reais construídos via API pública (`CreateMolSubstanceGroup`/`CreateStereoGroup`), não mockados — ver limitação na Seção 6.4 |
| T-020A-040 | `_validate_size_limits` | `test_atom_count_over_limit_is_rejected`, `test_atom_count_at_exact_limit_is_accepted` | Teto/teto+1 corretos (4096 átomos real, molécula de cadeia linear real) |
| T-020A-041 | `_compute_characterization_values` | `test_caffeine_reference_vector` | Os dez valores da cafeína batem exatamente com o vetor de referência da Seção 17 (tolerância 1e-8) |
| T-020A-042 | idem | `test_real_production_fixtures_characterize_without_tautomer_enumeration` (4 fixtures: ácido acético, diclofenaco, atrazina, estrutura tipo paratião) | Fórmula/carga corretas; nenhuma tautomerização ocorre |
| T-020A-043 | idem | `test_isotope_and_charge_preservation` | `[13C]H4`, amônio (+1), acetato (−1) |
| T-020A-044 | idem | idem | Carga formal preservada, sem neutralização |
| T-020A-045 | idem | `test_hbd_hba_use_the_pinned_api_not_nhoh_nocount` | HBD = 1/1/2 para metilamina/amônia/diamina, via `CalcNumHBD` real |
| T-020A-046 | idem | `test_rotatable_bonds_strict_discriminant_against_nonstrict` | `Strict` ≠ `NonStrict` comprovado numericamente (N-metilacetamida: 0 vs 1), resultado do adaptador bate com `Strict` |
| T-020A-047 | idem | `test_tpsa_sp_discriminant_against_include_s_and_p` | Dimetilsulfona: `includeSandP=False` (34.14) ≠ `True` (42.52); adaptador usa o perfil `False` |
| T-020A-048 | idem | `test_descriptor_failure_is_execution_error`, `test_descriptor_returning_non_finite_is_rejected` | Falha de descritor → `descriptor-failure`, cadeia de causa preservada; NaN → mesma categoria, sem zero/null |
| T-020A-049 | idem | `test_stereo_centers_are_preserved_not_enumerated` | Centro definido/indefinido preservados, nenhuma nova estereoquímica atribuída |
| T-020A-050 | idem | `test_representation_bytes_are_never_mutated` | Buffer de entrada bit a bit inalterado após a chamada |
| T-020A-051 | `_build_drawing_result` | `test_depiction_produces_a_validated_svg_for_each_probe` (cafeína, **antraceno canário obrigatório**, aspirina, alanina, isótopo+carga) | SVG válido no perfil fechado para todos; **ver achado/limitação registrado na Seção 6.4** sobre um caso que falha |
| T-020A-052 | idem + `_graph_signature` | `test_depiction_preserves_explicit_hydrogens_and_isotopes` | H explícitos/isotópicos preservados; invariantes do grafo comparados antes/depois da preparação |
| T-020A-053 | idem | `test_force_rdkit_remains_effective_regardless_of_global_coordgen_preference` | `forceRDKit=True` efetivo mesmo com `SetPreferCoordGen(True)` global |
| T-020A-054 | `_resolve_font_path_and_hash` | `test_font_evidence_is_real_and_matches_the_documented_hash` | **Evidência real do Windows**: hash do arquivo de fonte instalado neste wheel Windows é byte-idêntico ao hash observado em Linux na especificação (`eeaa2d17...`) |
| T-020A-055 | `_clear_drawing_annotation_properties` | `test_hostile_annotation_properties_are_stripped_from_the_svg` | `_Name`/`atomNote` hostis nunca aparecem no SVG final |
| T-020A-056 | adaptador completo | `test_drawer_is_never_invoked_when_svg_not_requested` | Desenhador nunca chamado quando `include_svg=False`; cálculo independente |
| T-020A-057 a 062 | `characterization.validate_and_bind_depiction_svg` | 27 testes (`test_doctype_is_rejected`, `test_external_entity_reference_is_rejected`, `test_predefined_entity_is_resolved_and_still_subject_to_grammar`, `test_disallowed_elements_are_rejected` ×6, `test_processing_instruction_is_rejected`, `test_non_whitespace_text_content_is_rejected`, `test_grandchild_element_is_rejected`, `test_root_attribute_violations_are_rejected` ×5, `test_unknown_root_attribute_is_rejected`, classe/estilo/`d` ×26, limite de bytes ×2) | DOCTYPE/entidade externa recusados sem abrir recurso; entidade predefinida ainda sujeita à gramática do atributo; elementos/atributos/estilo/`d` fechados; limite de bytes respeitado no limite exato e limite+1 |
| T-020A-063 | `_serialize_validated_svg`/vínculo | `test_svg_binding_links_state_id_hash_and_engine_to_the_entry`, `test_binding_preserves_exact_state_id_without_normalization`, `test_binding_escapes_special_characters_in_state_id` | IDs/hash/engine/perfil conferem com a entrada; escaping correto, sem path absoluto |
| T-020A-064 | adaptador completo | `test_depiction_failure_never_returns_a_partial_outcome` | Falha de desenho nunca retorna ficha parcial |
| T-020A-065 | validador SVG | `test_minimal_valid_svg_is_accepted_and_bound` (`.encode("utf-8").decode("utf-8") == final`) | Serialização UTF-8 coerente |
| T-020A-066 a 077 | — | — | **Fora de escopo** (serviço real com registro/leitores, e CLI — Checkpoints 2/3) |
| T-020A-069 (só vocabulário, não a decisão do serviço) | `RDKitCharacterizationOutcome`/`MolecularCharacterizationResult` | `test_warnings_must_match_fixed_order_exactly`, `test_generated_2d_warning_required_when_svg_present` | Vocabulário fechado de warnings validado nos dois DTOs |
| T-020A-076/077 | — | — | Não exercitado: `KeyboardInterrupt`/`SystemExit` durante cada fase do adaptador não foram testados individualmente nesta etapa — ver limitação Seção 6.4 |
| T-020A-078 | suppressão de logs nativos | `test_native_rdkit_logs_are_suppressed_and_restored` (via `capfd`) | Log nativo de erro suprimido no caminho de falha; chamada subsequente bem-sucedida confirma restauração (sem `DisableLog` permanente) |
| T-020A-079 | fronteiras opcionais | execução completa da suíte em venv sem `rdkit`; `test_characterization_imports_do_not_shadow_legacy_rdkit_import_error` | Fronteiras/legado preservados com e sem o extra |
| T-020A-080 | suíte completa | `pytest tests/ -q` (ambos os ambientes) | 1667 passed/5 skipped (com rdkit+gemmi); sem mudança científica, de handler legado, attempt/status ou contrato antigo — nenhum outro arquivo tocado |

### 6.4 Achados e limitações registrados explicitamente (não corrigidos silenciosamente)

1. **Achado real de incompatibilidade de gramática `d` (Seção 10.1)** — confirmado por
   execução real, não hipotético. Um centro quiral cuja ligação em cunha é desenhada
   como **triângulo preenchido** (por exemplo `C[C@@H](C(=O)O)Nc1ccc(Cl)cc1`,
   confirmado também com outras moléculas quirais com substituintes volumosos) produz
   um atributo `d` terminado em um comando absoluto `Z` (closepath) para fechar o
   triângulo. A gramática fechada da especificação (Seção 10.1: apenas `M, L, Q`),
   confrontada pela especificação apenas contra cinco desenhos empacotados e o
   canário obrigatório de antraceno (T-020A-051) — nenhum dos quais precisa de um
   triângulo de cunha preenchido — **não cobre esse comando**. Seguindo a instrução
   explícita da própria Seção 10.1 ("saída que exija comando não coberto falha
   explicitamente, sem ampliar o perfil silenciosamente... Qualquer incompatibilidade
   deve ser relatada"), **o validador não foi alterado** para aceitar `Z`; o
   adaptador corretamente recusa esse desenho com `depiction-failure`. Teste
   dedicado: `test_filled_wedge_triangle_z_command_is_an_unresolved_profile_gap`.
   Isso significa que, nesta implementação, **desenhos de centros quirais que exigem
   cunha preenchida falham com CONFIGURATION/EXECUTION ERROR em vez de produzir um
   SVG** — uma limitação real de cobertura do perfil congelado, não um bug do
   adaptador, que fica para decisão explícita de revisão (ampliar a gramática `d`
   para incluir `Z`, ou aceitar essa limitação).
2. **SGroup e grupos estéreo AND/OR (T-020A-038/039)** não puderam ser produzidos por
   um arquivo SDF/SMILES de texto real neste corpo de testes dentro do tempo desta
   etapa (um bloco V3000 funcional com `COLLECTION`/`STEAND` manuscrito não foi
   trivial de construir corretamente). Em vez disso, esses dois testes constroem o
   objeto RDKit real via a própria API pública do RDKit
   (`Chem.CreateMolSubstanceGroup`, `Chem.CreateStereoGroup`) e chamam
   `_validate_graph_eligibility(mol)` diretamente — exercitando a função de produção
   real contra um objeto RDKit real, mas não através do caminho completo de bytes→
   parsing→elegibilidade. É um teste de unidade legítimo da função de decisão (mesmo
   padrão já usado pela base de código em `_classify_record_counts`), mas não é
   evidência de que um arquivo SDF/SMILES real e hostil com SGroup/estereogrupo
   enhanced chegaria ao RDKit exatamente dessa forma — essa lacuna fica registrada
   para o Checkpoint 2, quando fixtures reais de arquivo puderem ser obtidas/
   construídas com mais tempo.
3. **T-020A-076/077 (`KeyboardInterrupt`/`SystemExit` durante cada fase)** não foram
   exercitados por teste automatizado nesta etapa — o código já usa `except
   Exception` (nunca `except BaseException`) em todos os pontos de tratamento do
   adaptador, o que estruturalmente garante que `KeyboardInterrupt`/`SystemExit`
   nunca são capturados e sempre se propagam sem conversão — mas essa garantia não
   foi comprovada por um teste de injeção dedicado por fase, diferente do padrão já
   existente em `test_sdf_source_raises_keyboard_interrupt_when_iteration_is_interrupted`
   para a enumeração de tautômeros. Registrado como item pendente de reforço de teste,
   não como comportamento duvidoso.
4. **Dois testes pré-existentes de `tests/test_cli.py`**
   (`test_tautomer_cli_17_invalid_sdf_is_execution_error`,
   `test_tautomer_cli_18_multiple_molecules_is_execution_error`) falham num ambiente
   sem o extra `rdkit` instalado, porque usam um helper de fixture que importa
   `rdkit` diretamente sem guarda `importorskip`. **Confirmado, lendo
   `tests/test_cli.py` na própria baseline `08b797e...`, que essa condição já existia
   antes desta sessão e é inteiramente independente dela** — `cli.py`/`test_cli.py`
   não fazem parte do escopo autorizado e não foram tocados.
5. O vetor de desenho `drawing.effective_parameters` retornado pelo adaptador usa os
   valores fixos/literais declarados na Seção 11 diretamente (DTOs com `Literal` e
   defaults fixos), e não lê de volta cada parâmetro efetivo do objeto `drawOptions`
   do RDKit após a configuração — como a Seção 11 já declara esses valores como
   constantes fechadas do perfil (não lidos de volta em nenhum ponto da própria
   especificação), isso é consistente com o texto, mas registrado aqui para
   transparência total.

## 7. Identidade do relatório e commits publicados

- **Commit de código publicado** (branch `feature/increment-020-a-molecular-
  characterization`, em `sysoutemanuelhenrique/molecular-platform`):
  **`f8416b845efe93f9e47deca97f01a355e4e679ba`**, parent direto
  `08b797e0985e123ffd4d7ca7e5a5e8f040e63851` (a baseline exata exigida — nenhum commit
  intermediário, nenhum merge). `origin/feature/increment-020-a-molecular-
  characterization` após `git push -u` aponta para o mesmo SHA, confirmado por
  `git rev-parse`.
- `origin/main` permanece em `08b797e0985e123ffd4d7ca7e5a5e8f040e63851` após este
  trabalho — confirmado por novo `git fetch` + `git rev-parse` ao final da sessão.
  Nenhum PR, merge, force push, amend, reset ou rebase foi executado; nenhuma
  configuração ou visibilidade foi alterada.
- **Este relatório** é publicado no repositório de governance
  `sysoutemanuelhenrique/molecular-platform-governance`, branch própria
  `claude/020-a-checkpoint1-report-20261020` (ramificada de `origin/main` do
  governance, SHA `a47183dfec8213c765ed43ae482c8c227760a3d5`, preservando esse SHA
  intacto), no caminho exato
  `increments/020-A/09-checkpoint-1/CLAUDE_CHECKPOINT1_IMPLEMENTATION_REPORT.md`
  exigido pela tarefa. Nenhuma edição a `STATUS.md` ou a tarefas centrais do
  governance foi feita nesta sessão.

## 8. Não realizado nesta etapa (lembrete explícito dos limites da autorização)

Checkpoints 2 e 3 **não foram implementados nem iniciados**: nenhum leitor
verificado, nenhum `characterization_service.py`, nenhum subcomando de CLI. Nenhuma
evidência de plataforma Windows11/NTFS para leitores foi produzida (não é exigida
neste checkpoint). Nenhum PR foi aberto; nenhum merge foi solicitado ou executado.

## 9. Pedido de revisão independente

Este checkpoint está pronto para revisão independente, conforme o próprio gate da
tarefa ("Independente review of Checkpoint 1; no automatic release of Checkpoint
2"). Nenhum Checkpoint subsequente foi iniciado por esta sessão.
