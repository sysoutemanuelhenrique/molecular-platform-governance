# Correção ao relatório de conclusão — Incremento 021, Checkpoint 2

Autor: Claude implementador (sessão separada da revisão independente). Data: 25/11/2026, America/Sao_Paulo.

Este documento **corrige** um ponto específico do relatório já publicado nesta mesma branch
(`claude-cp2-completion-report.md`, commit `70f7a14`, 25/11/2026 00:41) - não o substitui nem
reescreve a história; é aditivo, como a própria política da tarefa exige ("Own branch from exact
new dispatch"; relatórios próprios não são sobrescritos). O relatório anterior permanece intacto.

## 1. O que estava errado no relatório anterior

A seção 3-bis daquele relatório, item **§3.3 (import tardio e engine ausente)**, descrevia a
correção como: `import gemmi` no topo do módulo dentro de `try/except ImportError`, com
`_require_engine_available()` convertendo a ausência num erro limpo. A seção 4.1/C-04 do mesmo
relatório ia além e afirmava explicitamente: *"A docstring não afirma mais um import 'tardio' que
nunca existiu - documenta explicitamente que este é o módulo adapter dedicado com import eager,
e que o pin acontece nesta função, não no import do módulo."*

Essa é exatamente a leitura que o próprio adendo de governance
(`CODEX_CP2_LOCAL_PROGRESS_RESUME_GUARDRAILS.md`, §3.3) antecipa e rejeita: *"A docstring local
passou a reconhecer explicitamente que o import continua global e a alegar que ARCH-01 o permite
no adapter. ARCH-01 prova apenas import puro do domínio; não substitui §3, que exige import
tardio e erro de configuração para engine ausente/versão divergente."* O relatório anterior, ao
escrever essa justificativa, reproduziu precisamente o raciocínio que o adendo já havia
descartado como insuficiente - uma inconsistência que só se tornou visível ao reler o adendo
integralmente lado a lado com o código publicado, em vez de confiar na mensagem do commit
anterior (`60f9e0d`) que also reivindicava o ponto como corrigido.

O import permanecia, de fato, **eager** (avaliado no momento em que `molecular.receptor_parsing`
é importado, não no momento em que uma função de entrada é efetivamente chamada) - o
`try/except` apenas tornava essa falha tolerável, nunca tardia. Nenhum teste anterior distinguia
as duas coisas: o teste de subprocesso existente (`test_materialize_receptor_cif021_engine_absent_
raises_clean_configuration_error`) bloqueia `gemmi` **antes** de importar o módulo, o que prova
que uma falha de import é tolerada, mas não prova *quando* o import real acontece.

## 2. Correção aplicada

Commit `5be1e443200cedddac0f97707963500a2edc6da6` (filho direto de `60f9e0d`, mesma branch
`feature/increment-021-receptor-materialization`, allowlist inalterada: `src/molecular/
receptor_parsing.py` e `tests/test_receptor_parsing.py`, nenhum outro caminho tocado):

- `_ensure_gemmi_imported()` substitui o `try/except` de nível de módulo: o `import gemmi` real
  só acontece dentro desta função, na primeira chamada, armazenado em cache (`_GEMMI_IMPORT_
  ATTEMPTED`) para toda chamada seguinte. Meramente importar `molecular.receptor_parsing` não
  toca `gemmi` nenhuma vez.
- `_require_engine_available()` (toda entrada pública 021: `parse_receptor_cif_dom021`,
  `serialize_cif_document021`, `materialize_receptor_cif021`) chama `_ensure_gemmi_imported()`
  primeiro - o import real acontece ali, não antes.
- `parse_receptor_raw` (020) chama `_ensure_gemmi_imported()` no seu próprio primeiro passo -
  comportamento/API inalterados no único caso já testado (Gemmi presente); o caso ausente nunca
  foi exercido pela suíte 020 antes ou depois desta correção.
- As duas docstrings que racionalizavam o import eager como permitido por ARCH-01 foram
  reescritas para descrever o comportamento real (import tardio, cacheado, nunca de módulo).
- Novo teste de regressão, por subprocesso fresco (nunca um processo com `gemmi` já importado
  com sucesso ou já bloqueado): confirma `rp._GEMMI_IMPORT_ATTEMPTED is False` e `rp.gemmi is
  None` imediatamente após `import molecular.receptor_parsing`, e `True`/não-`None` somente após
  a primeira chamada real a uma função de entrada - a ordem em si, não apenas a tolerância a uma
  falha.

Na mesma correção, aproveitei para fechar duas lacunas de prova que o adendo também pedia e que
o relatório anterior não havia fechado com teste dedicado (ambos os pontos já estavam
corretamente implementados em código antes desta sessão - apenas sem a prova explícita que o
adendo exige):

- **§3.4** (visão decodificada vs. colapso de nulos): novo teste exercitando `_build_category_
  tables`/`_build_entity_type_lookup`/`_build_symmetry_operator_tables` através do adaptador real
  com um identificador citado (`_entity.type`), uma expressão de operador citada em uma linha e
  uma expressão de operador genuinamente multilinha (campo delimitado por `;`) em outra, ao lado
  de um `.` real e um `'.'` citado - provando que a visão decodificada é realmente cozida pelo
  Gemmi (aspas/delimitadores removidos), nunca apenas colapso de nulos, enquanto a visão crua
  preserva o token literal exato.
- **§3.5** (recorte de fixtures e lineage): novo teste que verifica, para as seis fixtures reais,
  que cada categoria em `categories_removed` (i) está genuinamente presente no arquivo original
  intocado, (ii) está genuinamente ausente do derivado `_trimmed.cif`, (iii) está genuinamente
  fora do catálogo congelado de 94 categorias (`_cat_def_for(...) is None` - a razão real, não
  apenas descrita em prosa, para a rejeição exigida), e que toda categoria *não* removida mantém
  exatamente a mesma contagem de linhas entre original e recortado - contra os bytes reais dos
  dois arquivos, não apenas contra o que o `PROVENANCE.json` afirma.

Os pontos §3.1 (fechamento CCD de `parent_comp_id`) e §3.2 (teto de 16 MiB) do relatório anterior
foram reconferidos nesta sessão e permanecem corretos como descritos - nenhuma mudança adicional
foi necessária neles.

## 3. Evidência real desta correção

```
Python 3.14.7 / gemmi 0.7.5 / pytest, mesmo ambiente do relatório anterior (venv do projeto)

tests/test_receptor_parsing.py + tests/test_receptor_materialization.py:
  python -B -m pytest -p no:cacheprovider tests/test_receptor_parsing.py tests/test_receptor_materialization.py -q -rs
  -> 208 passed (antes desta correção: 206; +2 testes novos, mais o teste de ordenação do import)

regressão 020 (inspection/selection/resolution/registry/service):
  python -B -m pytest -p no:cacheprovider tests/test_receptor_inspection.py tests/test_receptor_selection.py tests/test_receptor_resolution.py tests/test_receptor_registry.py tests/test_receptor_service.py -q -rs
  -> 121 passed (inalterado)

coleta completa:
  python -B -m pytest --collect-only -q
  -> 1658 coletados (antes: 1655)

suíte completa:
  python -B -m pytest -p no:cacheprovider -q -rs
  -> 1653 passed, 5 skipped (antes desta correção: 1651 passed, 5 skipped)
```

`git diff --check` e `git show --check 5be1e44...` limpos. `git diff --name-status 60f9e0d..5be1e44`
mostra exatamente os dois caminhos da allowlist tocados (`src/molecular/receptor_parsing.py`,
`tests/test_receptor_parsing.py`) - nenhuma fixture nova ou modificada, nenhum outro arquivo.
`origin/main` do código permanece `08b797e0985e123ffd4d7ca7e5a5e8f040e63851`; `origin/main` do
governance permanece `a47183dfec8213c765ed43ae482c8c227760a3d5` - ambos reconferidos depois desta
publicação.

| Caminho | Linhas | Bytes | SHA-256 |
|---|---:|---:|---|
| `src/molecular/receptor_parsing.py` | 1729 | 72.413 | `17f42823060a67efb600818745a61df41cbab82e79e8dc4a8f6a7ed03451bf8b` |
| `tests/test_receptor_parsing.py` | 1383 | 59.027 | `c87aa96a0233d6471a9f4578b1e7475c1079008c2e0cca988a4035f2a98b430b` |

## 4. Commit e publicação remota

```
commit 5be1e443200cedddac0f97707963500a2edc6da6
parent  60f9e0da5c67c3820747242a033db2f5d49b1817
branch  feature/increment-021-receptor-materialization
2 files changed, 178 insertions(+), 27 deletions(-)
```

Push confirmado: `git rev-parse origin/feature/increment-021-receptor-materialization` devolve
`5be1e44...`. Nenhum PR, merge, tag ou alteração de `main` em nenhum dos dois repositórios.

## 5. Disposição final

Com esta correção, os cinco pontos do adendo (§3.1-§3.5) estão corrigidos e com prova de produção
dedicada para cada um, reconferidos contra o código real publicado - não apenas contra a
mensagem do commit anterior. Isso não é uma segunda alegação de fechamento independente de CP2:
as limitações já declaradas no relatório anterior (§4.1/§6 daquele documento) permanecem válidas
e não foram reexaminadas nesta correção, que tem escopo deliberadamente estreito (o ponto §3.3
mal corrigido, mais prova explícita para §3.4/§3.5 que já estavam corretos em código).

Não declaro CP2 aprovado. Não solicito avanço a CP3. Recomendo que o arquiteto confira esta
correção especificamente (o diff `60f9e0d..5be1e44` é pequeno e isolado) antes de decidir se o
critério de conclusão do CP2 está agora satisfeito para a revisão independente final.

```
TASK_ID: 021-CHECKPOINT2-COMPLETION
ROLE: claude-implementer-separate-from-independent-reviewer
SCOPE_EXECUTED: CHECKPOINT2_COMPLETION_ADDENDUM_CORRECTION
CODE_BRANCH: feature/increment-021-receptor-materialization
CODE_COMMIT: 5be1e443200cedddac0f97707963500a2edc6da6
READY FOR INDEPENDENT FINAL CP2 REVIEW: NO
CHECKPOINT2 APPROVED: NO
CHECKPOINT3 IMPLEMENTATION AUTHORIZED: NO
```
