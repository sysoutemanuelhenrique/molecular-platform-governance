# Incremento 021 — Revisão final curta das correções residuais do Checkpoint 1

Revisor: Claude, numa sessão de revisão independente, separada do arquiteto e de todas as sessões implementadoras. Data: 2026-11-24. Tarefa: `tasks/021-CHECKPOINT1-FINAL-FOCAL-REVIEW.json`.

**Veredito: REQUEST CHANGES**, por uma única regressão de teste introduzida pelo delta (R-1). A correção é somente de teste e cabe em uma linha de vetor mais um literal.

- As três correções residuais estão fechadas em código.
- Este parecer não aprova o CP1 e não autoriza o CP2.
- 020-A permanece em STAND-BY.

## 1. Snapshots e identidades

Conferidos com `git ls-remote` antes e depois da revisão, sem deriva:

| Referência | Esperado = observado |
|---|---|
| Coordenação `docs/020-a-candidate1-review-20261020` | `fcad8561b53b924ad2d04844c460fabd8489f866` |
| Governance `main` | `a47183dfec8213c765ed43ae482c8c227760a3d5` |
| Código `feature/increment-021-receptor-materialization` | `bbd491e1a0b3fcb913c3549b004120693212df62`, pai direto `42b4804` |
| Código `main` | `08b797e0985e123ffd4d7ca7e5a5e8f040e63851` |
| Entrega `claude/021-cp1-residual-corrections-20261124` | `74fb0c39fbf3f56b43936491aa2c0789a53ecf31`, cadeia `b9d9592 → 1bf4d4d` |
| Revisão focal anterior | `854ae336621116f7047033b5146c7c4834ebf9c2` |

O delta `42b4804..bbd491e` toca só os dois arquivos da allowlist. O delta cumulativo desde `08b797e` também fica nesses dois arquivos. A branch de entrega adiciona 13 arquivos próprios, todos sob `increments/021/25-…`.

| Arquivo | Linhas | Bytes | SHA-256 |
|---|---|---|---|
| `src/molecular/receptor_materialization.py` | 1724 | 78807 | `d8fc55db900f761f0debe4cea29f05cade1502ea1299937f123c6c883e30431d` |
| `tests/test_receptor_materialization.py` | 1645 | 81362 | `e67539e76be9d174e7ef2c93cf971faa6bfba3316ef996f5e4a55c9345a90d69` |

Conferências adicionais, por linhas, bytes, SHA-256 e blob:

- relatório (`6d3b254b…`, blob `d63b1547`), manifesto (`c2fc0ba6…`), handoff (`428b1b64…`), reconciliação residual (`06a7887a…`) e vetores documentais (`fe2ae073…`, blob `06f1ef6a`);
- especificação congelada e os quatro anexos;
- a revisão anterior (`61865d46…`).

O log da suíte completa foi lido pelos bytes do blob `d8b45ed5` (3003 bytes, SHA-256 `400a6979…`), não por uma visão de texto recodificada.

## 2. Método e limites

Ambiente: Linux, Python 3 do sandbox, sem rede, sem Gemmi, RDKit ou Windows. Trabalhei sobre uma cópia externa de `bbd491e`. Nada foi gravado no fonte: a contagem de bytecode e cache foi 0 depois de cada execução.

- **Processo nativo bloqueado:** `sys.modules["gemmi"/"rdkit"] = None`, sem stub, nos modos normal e `-O`. Nele chamei as funções de produção sobre os insumos documentais do MINOR-7 e o caminho puro da conferência de formato. Nenhum módulo nativo ou parser do 020 foi carregado. Evidência: `claude-blocked-native-golden-and-format.*`.
- **Recomputação independente dos 13 envelopes:** feita só com a biblioteca padrão, a partir da tabela de envelopes de §13 e SCHEMAS (linhas 23, 27, 45, 47 e 53–60; especificação 227, 229 e 231). Não importei produção nem o gerador do arquiteto. Evidência: `claude-independent-vectors.*`.
- **Sondas com DTOs reais do 020:** usam o sentinela inerte de `gemmi`, cujo `__getattr__` lança erro. Ele serve só para importar as classes; não prova importação nativa.
  - 49 sondas residuais: `claude-residual-probes.*`.
  - Reexecução das 59 sondas da revisão anterior contra `bbd491e`: `claude-previous59-*`.
- **Testes e mutação:** os 91 testes passam aqui com o sentinela (`claude-pytest-91-with-sentinel.txt`). A mutação de ordem em `compute_atom_ids_key` foi feita em cópia scratch: `claude-atom-ids-order-mutation.*`.
- **Fornecido, não reexecutado:** 91 passed no arquivo e 1567 passed + 5 skipped na suíte completa, em Windows. Os cinco skips nomeados no log atual (test_application:1809/1847, test_atomic:1046, test_cli:4250/4303) coincidem, arquivo:linha, com os do log da rodada anterior.

## 3. Disposição dos três residuais

### MAJOR-A residual: FECHADO

`build_source_context` passa a normalizar `acquisition.raw_artifact.format` e `inspection.raw_format_declared` com `strip().lower()` e o mapa de quatro aliases do 020 (`cif`, `mmcif`, `pdb`, `ent`). O mapa é projetado localmente, sem import de `receptor_inspection`, o que preserva ARCH-01. O resultado precisa ser reconhecido, concordante e igual a `mmcif`; caso contrário, sai `INVALID_RECORD`.

Sondas com DTOs reais:

- Recusados com `INVALID_RECORD`:
  - pdb/pdb com detecção mmcif, mesmo com o aviso `declared-format-mismatch` presente;
  - mmcif/pdb e pdb/mmcif;
  - xyz/xyz, xyz/mmcif e mmcif/xyz;
  - ent/pdb;
  - `"mm cif"`;
  - rótulo só de espaços.
- Aceitos: cif/mmcif, mmcif/cif, cif/cif, mmcif/mmcif, e `" MMCIF "`/`"Cif\t"`, conforme a regra strip/lower do 020.
- As strings de origem permanecem intactas.
- `ENGINE_VERSION` continua precedendo a checagem de formato.
- O mesmo comportamento se repete no processo bloqueado, nos modos normal e `-O`.

Nota não bloqueante: a checagem de formato fica entre as checagens de engine/schema/formato detectado e as de capacidade, ids e checksums. Um registro com formato e id divergentes ao mesmo tempo responde `INVALID_RECORD`, e não `IDENTITY_MISMATCH`. Isso é coerente com a precedência já existente da checagem de `structure_format`, e as duas causas são de configuração da fonte.

### MINOR-3 residual: FECHADO

Unicidade dentro de cada tupla:

- recusados: `(0,0)` em kept, `(0,0)` em omitted e o duplicado não adjacente `(0,1,0)`;
- continuam recusados: sobreposição entre as tuplas, ordinal negativo e `bool` (estrito).

Gramática das famílias por `re.fullmatch(r"(?:_pdbx_validate_|_pdbx_nmr_|_em_)[a-z0-9_]+")`:

- recusados: LF final e LF inicial, os três prefixos nus, espaço, nome de item com ponto, maiúsculas no prefixo e no sufixo, NUL, TAB e `é`;
- aceitos: `_em_3d_fitting`, `_pdbx_validate_close_contact`, `_pdbx_nmr_spectrometer` e `_em_x_`;
- família com `filter` e nome fora do catálogo continuam recusados.

Preservados:

- os 94 nomes do catálogo, aceitos e idênticos ao conjunto `categories` do anexo `CATALOG_021.json` (0 de diferença em cada sentido);
- nenhum nome do catálogo cai na gramática de família;
- os controles de omissão vazia, `_cell` filter+generate e generate com fonte nula.

### MINOR-7 residual: FECHADO em literais e envelopes, com regressão R-1 em ordem

Há 13 literais SHA-256 fixos no arquivo de teste. A minha recomputação independente, sem produção e sem o gerador do arquiteto, coincide com **todos os 13**. As funções de produção correspondentes, chamadas no processo bloqueado (normal e `-O`), também coincidem com os 13. Os insumos derivados (`atom_ids_key` de w1 e as `occurrence_key` de A e B) coincidem com os valores escritos no teste.

O teste legado passa a chamar **diretamente o helper novo** `_compute_legacy_inspection_id` e o compara com o literal independente `1c217d99…`. O helper antigo fica apenas como controle adicional.

Não há dependência de fixture ou governance em tempo de teste, e o algoritmo não mudou: `compute_*` e `compute_materialization_hash` não aparecem no diff de fonte.

Os vetores são documentais: não são RAW científico nem saída de adaptador nativo. `policy_file_sha256` foi tomado como insumo dado.

## 4. Regressões concretas do delta

**R-1 (MINOR, bloqueante, somente teste): a prova de ordem do `atom_ids_key` foi enfraquecida.**

Em `42b4804`, `test_minor7_golden_atom_ids_key_preserves_given_order_independent_of_production` usava dois átomos fora de ordem, `(ordinal=3,"Z")` e `(ordinal=1,"a")`. Em `bbd491e`, o mesmo teste usa um único átomo, `(1,"b1")`. Com isso:

- o nome do teste continua afirmando preservação da ordem dada, mas a propriedade deixou de ser exercida;
- nenhum outro teste chama `compute_atom_ids_key` com mais de um átomo fora de ordem.

Mutação em cópia scratch, reordenando o vetor dentro de `compute_atom_ids_key`:

| Mutante | Testes de `42b4804` (75) | Testes de `bbd491e` (91) |
|---|---|---|
| ordena por ordinal | **1 falha** (o teste acima) | 91 passam |
| ordena por `atom_id` | 75 passam | 91 passam |

O mutante por ordinal era detectado antes e deixou de ser. O mutante por `atom_id` já não era detectado, porque `"Z" < "a"` em ASCII.

Isso contraria o critério da tarefa ("confirm no … assertion weakened") e o critério original do MINOR-7 ("ordem de listas"). Uma reordenação silenciosa mudaria a identidade de auditoria de X/O.

**Correção pedida, sem mudança de fonte:** restaurar um vetor `atom_ids` com pelo menos dois átomos, cuja ordem dada não seja ordenada nem por ordinal nem por id. Por exemplo, `(3,"a")` seguido de `(1,"Z")`, com bytes escritos à mão e um literal SHA-256 fixo. Pode ser um teste adicional, mantendo o vetor atual.

Fora isso:

- as 59 sondas da revisão anterior, reexecutadas em `bbd491e`, mudam **exatamente nas 9** que correspondiam aos residuais (3 de formato, 2 de duplicata, 4 de família), de aceito para recusado;
- as outras 50 têm desfecho idêntico, inclusive ARCH-02, MAJOR-B e MINOR-1/2/4/5;
- MINOR-6 se mantém no processo bloqueado.

Nenhuma outra regressão foi observada.

## 5. Fechamentos anteriores e NOTES

- **Os nove fechamentos anteriores continuam preservados**, conforme as sondas de controle e o processo bloqueado: ARCH-01, ARCH-02, ARCH-03, MAJOR-B, MINOR-1, MINOR-2, MINOR-4, MINOR-5 e MINOR-6.
- **NOTE-1:** sem persistência ou reutilização de plano parcial e sem CP2.
- **NOTE-2:** estritez mantida; `bool` como ordinal é recusado e não há exceção ampla.
- **NOTE-3:** CLI e 020 inalterados.

## 6. Testes nominais e contagens

Contagens:

- arquivo de teste: 75 → 91 funções, 0 parametrizações;
- coleta completa: 1556 → 1572;
- node IDs: 17 adicionados e 1 removido, todos no arquivo de teste.

O node ID removido corresponde ao teste legado tautológico, renomeado para `…_calls_the_new_helper_against_independent_literal`. A coleta "antes" desta rodada tem exatamente os mesmos 1556 node IDs da coleta "depois" da rodada anterior. Os 91 nomes coletados aqui coincidem com a coleta fornecida.

Os 43 IDs normativos (T021-001…040 e 159…161) continuam presentes; nenhum cenário foi removido. A classificação 40 provados / 3 parciais por desenho / 0 lacunas permanece.

Quatro testes golden existentes foram modificados. Três foram reforçados com literal; os vetores de ocorrência e de conexões vazias foram trocados por outros de cobertura equivalente. O quarto é o caso R-1.

Os 91 testes nominais passam, mas não bastam: não detectam a mutação de ordem descrita em R-1.

## 7. Veredito

**REQUEST CHANGES**, limitado a R-1: restaurar a prova golden literal de preservação de ordem do `atom_ids_key`, somente no arquivo de teste.

- MAJOR-A, MINOR-3 e MINOR-7 estão fechados quanto ao que foi pedido.
- Os nove fechamentos e as três NOTES estão preservados.
- Após a correção de R-1, a expectativa é **APPROVE WITH NON-BLOCKING NOTES**, a partir da nota de ordem de checagem em MAJOR-A e das observações não bloqueantes já registradas.
- Este parecer não aprova o CP1 e não autoriza o CP2. Não há PR, merge, tag, release nem alteração de `main`.

## 8. Evidências

Em `increments/021/27-checkpoint1-final-focal-review/evidence/`:

- `claude-residual-probes.py` e `.output.json`: 49 sondas residuais.
- `claude-independent-vectors.py` e `.output.json`: 13 de 13 coincidem.
- `claude-blocked-native-golden-and-format.py` e `.output.txt`: modos normal e `-O`.
- `claude-previous59-probes.py` e `claude-previous59-regression-diff.json`: 9 mudanças esperadas, 0 regressões.
- `claude-atom-ids-order-mutation.sh` e `.output.txt`: R-1.
- `claude-pytest-91-with-sentinel.txt`.
- `claude-inert-gemmi-sentinel.py`: serve só para construir os DTOs; não é prova de importação.
- `claude-evidence-identities.json`.
