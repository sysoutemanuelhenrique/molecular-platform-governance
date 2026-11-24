# Incremento 021 — Revisão focal independente do R-1 (Checkpoint 1)

Revisor: Claude, em sessão de revisão independente, separada do arquiteto e da sessão implementadora. Data: 2026-11-24. Tarefa: `tasks/021-CHECKPOINT1-R1-FOCAL-REVIEW.json`.

O escopo é somente o R-1 (delta de teste `bbd491e..ea8dac9`) e a preservação dos testes anteriores. Não é uma revisão científica, nativa ou de checkpoint integral.

**Veredito R-1: APPROVE.**

| Item | Estado |
|---|---|
| READY FOR OWNER CP1 DECISION | YES |
| CHECKPOINT1 APPROVED | NO |
| CP2 AUTHORIZED | NO |
| 020-A | STAND-BY |

## 1. Snapshots e identidades

Todos os refs abaixo foram conferidos com `git ls-remote` antes e depois da revisão. Não houve deriva.

| Referência | Esperado = observado |
|---|---|
| Coordenação `docs/020-a-candidate1-review-20261020` | `828bf806e2f16ae9fee5896ae6f9719a9e1dc5cf` |
| Governance `main` | `a47183dfec8213c765ed43ae482c8c227760a3d5` |
| Código `feature/increment-021-receptor-materialization` | `ea8dac9cdc203c337d7f3f9947b54042291f7484` |
| Pai direto do código | `bbd491e` |
| Código `main` | `08b797e0985e123ffd4d7ca7e5a5e8f040e63851` |
| Entrega `claude/021-cp1-r1-test-correction-20261124` | `b35bb8e9d32e6fb4bc95e903f786fa0c1240e2d2`, cadeia `066af33 → 771ae24` |
| Revisão anterior `claude/021-cp1-final-focal-review-20261124` | `edb8764b4d4ee56e49ff849b65b950e5e430fae0` |

A entrega acrescenta somente os dez arquivos próprios sob `increments/021/29-…`.

Identidades conferidas, com linhas, bytes, SHA-256 e blob. Todas coincidem com a tarefa:

- relatório (`a275e163…`), manifesto (`fb2e1960…`, blob `3ed1a9e7`), handoff (`e50b5bcd…`), verificação do arquiteto (`3a60eeb9…`), resposta R-1 (`c079d09a…`), vetor documental (`19f14197…`, blob `03875e79`);
- especificação congelada (`5de705d6…`), SCHEMAS (`649b4334…`) e a revisão anterior (`61b3f0b6…`, blob `bbd7c5ec`).

| Arquivo em `ea8dac9` | Linhas | Bytes | SHA-256 |
|---|---|---|---|
| `src/molecular/receptor_materialization.py` | 1724 | 78807 | `d8fc55db900f761f0debe4cea29f05cade1502ea1299937f123c6c883e30431d` |
| `tests/test_receptor_materialization.py` | 1676 | 83570 | `9f72301ece6e55ef11d78d589f20822673887af10eeee1365d209099c3658ada` |

O SHA-256 do fonte é idêntico ao de `bbd491e`. O delta `bbd491e..ea8dac9` toca apenas o arquivo de teste, com `+31/-0`. O delta cumulativo desde `08b797e` continua restrito aos dois caminhos do CP1.

## 2. Disposição do R-1: FECHADO

O teste novo é `test_atom_ids_key_preserves_given_order_against_ordinal_and_id_sorting`.

1. **Literais independentes.** Recalculei os dois envelopes só com a biblioteca padrão, a partir do envelope `atom_ids` de SCHEMAS §4, sem importar produção nem o vetor do arquiteto:
   - ordem dada `(3,"a"),(1,"Z")` → `96fd3eacd89d16753dbdc5ec22bb79db0740e9f355e6322cb0c4641bc0f3106a`;
   - ordem invertida → `bf820fe14730b4b8ede9d8e007e4c3d32f71def5d8a4747c657d6d76dac562d1`.

   Os dois coincidem com a tarefa e com o teste. Os bytes escritos à mão no teste são exatamente os bytes canônicos que recalculei.
2. **Vetor discriminante.** A ordem dada difere da ordenação por ordinal e da ordenação ASCII por id. As duas ordenações coincidem com a ordem invertida.
3. **Teste executado contra produção.** O teste chama o `compute_atom_ids_key` real com `_atom(...)`, por meio do helper `_assert_hand_bytes_hash_to_literal` (`hashlib` sobre os bytes escritos à mão). O literal esperado não é gerado por produção.
4. **Mutação com o nó pytest exato, em cópia descartável.** O `compute_atom_ids_key` foi mutado, e o nó novo e o arquivo inteiro rodaram contra cada versão:

   | Versão | Nó novo | Arquivo inteiro |
   |---|---|---|
   | original | 1 passed | 92 passed |
   | ordena por ordinal | **falha** | 1 falha (só o nó novo) |
   | ordena por `atom_id` | **falha** | 1 falha (só o nó novo) |
   | inverte | **falha** | 1 falha (só o nó novo) |
   | ordena por ordinal decrescente | **falha** | 1 falha (só o nó novo) |

   O mutante decrescente preserva a ordem do vetor dado. Ele só é detectado pela segunda asserção, a do vetor invertido, o que mostra que ela não é redundante. Na revisão anterior, os mutantes por ordinal e por id passavam pelos 91 testes; agora são detectados.

## 3. Preservação dos testes anteriores

Comparação AST entre `bbd491e` e `ea8dac9`:

- 91 → 92 funções de teste;
- 0 funções removidas e 0 modificadas;
- imports e atribuições de módulo idênticos;
- os 13 literais `_GOLDEN_*` mantidos;
- 0 parametrizações;
- os 43 IDs T021 presentes;
- o texto antigo é reconstituído exatamente quando se remove a função nova.

Nenhuma asserção, import, helper ou golden foi enfraquecido ou removido. O teste golden de um átomo continua presente: o teste novo foi acrescentado, não substituiu o anterior.

Os logs de coleta fornecidos mostram 1572 → 1573 node IDs: exatamente +1, que é o nó novo, e 0 removidos. A coleta "antes" desta rodada tem os mesmos node IDs da coleta "depois" da rodada anterior.

Os 12 achados fechados, as 3 NOTES e a classificação 40/3/0 dos 43 cenários ficam preservados. Não há mudança de fonte, então nenhum fechamento é afetado. Nenhuma regressão concreta foi encontrada.

## 4. Separação entre a minha execução e as evidências fornecidas

**Executado por mim.** Ambiente Linux, Python 3 do sandbox, sem rede, sem instalações e sem Gemmi, RDKit ou Windows. As execuções rodaram em cópia externa, com o sentinela inerte de `gemmi` apenas para importar os DTOs do 020; ele não prova importação nativa. Não foi gravado bytecode nem cache no fonte (contagem 0). Execuções:

- pytest do nó exato e dos 92 testes;
- mutações;
- recomputação dos literais;
- comparação AST.

**Fornecido, não reexecutado.** A suíte completa no Windows deu 1568 passed + 5 skipped. Esse log foi lido pelos bytes do blob `0afc49e6` (3003 bytes, SHA-256 `d7f62c14…`). Os cinco skips (test_application:1809/1847, test_atomic:1046, test_cli:4250/4303) são os mesmos, arquivo:linha, da rodada anterior. A aritmética 1568 + 5 = 1573 confere com a coleta.

**Limite da evidência do implementador.** O `claude-r1-mutation-check.py` carrega o módulo por `importlib` e compara diretamente a saída da função. Ele não executa o pytest exato e por isso não foi tratado como execução do teste novo. A detecção pelo nó pytest exato foi demonstrada de forma independente na tabela da seção 2.

## 5. Veredito

**APPROVE** para o R-1.

- R-1 fechado; nenhuma nota bloqueante ou nova.
- READY FOR OWNER CP1 DECISION: **YES**.
- CHECKPOINT1 APPROVED: **NO**. CP2 AUTHORIZED: **NO**.

Este parecer não aprova o CP1, não autoriza o CP2 e não cria PR, merge, tag ou release. Também não altera `main`, STATUS ou tarefas.

## 6. Evidências

Em `increments/021/31-checkpoint1-r1-focal-review/evidence/`:

- `claude-r1-independent-literals.py` e `.output.json`
- `claude-r1-mutation-exact-pytest.sh` e `.output.txt`
- `claude-r1-test-preservation.py` e `.output.json`
- `claude-inert-gemmi-sentinel.py` (usado só para construir os DTOs; não prova importação)
- `claude-evidence-identities.json`
