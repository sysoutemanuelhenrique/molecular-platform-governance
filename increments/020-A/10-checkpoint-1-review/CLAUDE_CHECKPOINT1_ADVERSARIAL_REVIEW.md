# Revisão adversarial independente — Checkpoint 1, Incremento 020-A

Revisor: Claude, sessão separada da implementação, papel `claude-independent-reviewer-separate-from-implementer` (tarefa `020-A-CHECKPOINT1-REVIEW`, status `READY_FOR_REVIEW` confirmado antes de iniciar). Código, testes e especificação permanecem estritamente read-only nesta sessão; nenhum arquivo do repositório de código ou documento congelado foi alterado.

## 1. Identidades e snapshots conferidos

Todas as identidades abaixo foram verificadas por esta sessão, por hash/SHA, antes de qualquer leitura de conteúdo — não apenas aceitas por afirmação do arquiteto ou do implementador.

| Item | Esperado | Observado por este revisor | Resultado |
|---|---|---|---|
| Governance, branch `docs/020-a-candidate1-review-20261020` | `6bd9a5fdb30f8d75dd6dde05d4eafab9e86382e1` | Idêntico (clone raso anônimo) | OK |
| Governance `main` preservada | `a47183dfec8213c765ed43ae482c8c227760a3d5` | Idêntico, não tocado | OK |
| `tasks/020-A-CHECKPOINT1-REVIEW.json` | SHA-256 `2ab2a155...7161` | Idêntico | OK |
| Especificação congelada | SHA-256 `cfbc6ea4...6e9c`; 586 linhas; 71.904 bytes | Idêntico | OK |
| Triagem do arquiteto | SHA-256 `11f4ffed...37f80` | Idêntico | OK |
| Sonda do arquiteto (`architect-dto-strictness-probe.json`) | SHA-256 `651ee70e...6ad0` | Idêntico | OK |
| Relatório do implementador | SHA-256 `76f7403c...4dc82`; 343 linhas; 26.859 bytes | Idêntico (lido do commit `0dac01f2f51efe1ed1600eafac88eb8f750d41b1`, branch `claude/020-a-checkpoint1-report-20261020`) | OK |
| Código, branch `feature/increment-020-a-molecular-characterization` | HEAD `f8416b845efe93f9e47deca97f01a355e4e679ba` | Idêntico (clone raso anônimo) | OK |
| Parent direto do HEAD de código | `08b797e0985e123ffd4d7ca7e5a5e8f040e63851` | Idêntico — `git log -1 --format='%H %P'` confirma commit único sobre a baseline, sem merge intermediário | OK |
| `main` do código | `08b797e0985e123ffd4d7ca7e5a5e8f040e63851` | Idêntico, não tocado | OK |

Nenhum gate divergiu; a revisão prosseguiu. Acesso: leitura anônima via protocolo Git funcionou para ambos os repositórios nesta sessão (sem credenciais); a API REST do GitHub permanece bloqueada para esta sessão por política própria do sandbox, sem efeito sobre a verificação acima, feita inteiramente por `git ls-remote`/`git clone`/`git show` diretos.

Diff completo confirmado independentemente: `git diff --stat` entre a baseline e o HEAD mostra exatamente os quatro arquivos autorizados (`src/molecular/characterization.py`, `src/molecular/rdkit_tautomer.py`, `tests/test_characterization.py`, `tests/test_rdkit_tautomer.py`), `3094 insertions(+), 1 deletion(-)`; `git diff --check` limpo; nenhum caminho fora da allowlist tocado; `increment-009-review.txt` e `_figura_curcumina/` não aparecem no diff.

## 2. Ambiente e execução desta revisão — comandos, resultados e limitações

Esta sessão **não tem RDKit instalável** (sem resolução DNS para pypi.org mesmo pelo proxy configurado — limitação idêntica à de todas as rodadas anteriores desta linha de revisão) e **não tem `pytest` instalado**, e a tentativa de `pip install pytest` falhou pelo mesmo motivo (comando e erro registrados abaixo). Portanto, não foi possível executar a suíte real nem coletar os 191 itens adicionais por mim mesmo.

```
$ pip install --break-system-packages pytest
ERROR: Could not find a version that satisfies the requirement pytest ...
ERROR: No matching distribution found for pytest
```

O que **foi** executado de forma independente, com Python 3.13.16 e Pydantic 2.13.5 (ambos já presentes neste ambiente, sem instalação) contra o código exato do HEAD publicado, sem pytest:

```python
import sys; sys.path.insert(0, "src")
from molecular import characterization as c

c.CharacterizationValues(formula="C2H6O", molar_mass_g_mol="46.069", exact_mass_da=46.0419,
    formal_charge_e="0", heavy_atom_count="3", hbd_count=1, hba_count=1,
    rotatable_bond_count=0, tpsa_a2=20.2, clogp_wildman_crippen=-0.3)
c.CharacterizationValues(..., heavy_atom_count=3.0, ...)
c.SdfParserParameters(sanitize=1)
```

Resultado (evidência completa publicada em `evidence/claude-dto-coercion-reproduction.json`): todas as três chamadas **foram aceitas sem erro**. `heavy_atom_count="3"` (str) e `heavy_atom_count=3.0` (float) tornam-se `int` 3; `formal_charge_e="0"` torna-se `int` 0; `molar_mass_g_mol="46.069"` torna-se `float`; `SdfParserParameters(sanitize=1)` (int) torna-se `bool True` no campo `Literal[True]`. Isto **reproduz de forma totalmente independente**, numa terceira versão de Pydantic distinta tanto da sonda do arquiteto (2.14.0) quanto do ambiente do implementador (2.14.1), a mesma falha já apontada pela sonda do arquiteto — a convergência em três ambientes diferentes torna implausível que seja uma peculiaridade de versão. Ver §4, MAJOR-1.

Toda leitura estática de código (`grep`/leitura direta dos quatro arquivos no HEAD pinado) foi feita diretamente sobre os bytes do commit publicado, não sobre o relatório do implementador ou a triagem do arquiteto. Onde a verificação dependeria de RDKit real, Windows real ou pytest real (os dez valores de referência da cafeína, a evidência Windows da fonte Telex, a contagem exata de itens coletados, os resultados reportados "111/142/1667 passed"), este revisor **declara explicitamente não ter executado essa verificação** e trata o número correspondente como relatado pelo implementador, não como observado por mim — distinção exigida pela tarefa e preservada em cada item abaixo.

## 3. Reconciliação dos itens coletados (+191)

Verificação estrutural independente, por contagem textual direta no código-fonte do diff (não por execução de pytest, que não está disponível):

| Verificação | Comando | Resultado observado por mim |
|---|---|---|
| Funções `def test_` em `tests/test_characterization.py` | `grep -c "^def test_"` | 51 |
| `@pytest.mark.parametrize` em `tests/test_characterization.py` | `grep -c` | 14 |
| Funções `def test_` **adicionadas** pelo diff em `tests/test_rdkit_tautomer.py` | `git diff ... | grep -c "^\+def test_"` | 54 |
| `@pytest.mark.parametrize` **adicionados** pelo diff em `tests/test_rdkit_tautomer.py` | idem | 6 |

Isso é consistente com a afirmação do relatório de que 111 e 80 são contagens de **itens coletados** (funções × expansão de parametrização), não de funções — 51 e 54 funções, respectivamente, com 14 e 6 delas parametrizadas, são uma base plausível para 111 e 80 itens coletados, mas **não pude confirmar a aritmética exata de expansão** sem `pytest --collect-only`, que não pude executar. Esta é uma reconciliação estrutural parcial, não uma contagem independente completa — declaro o limite em vez de presumir.

Os resultados "111 passed", "142 passed (62+80)", "1667 passed, 5 skipped" (suíte completa) e "1476 passed, 5 skipped" (baseline) são **relatados pelo implementador**, não observados por mim. O próprio arquiteto também não os reexecutou (confirmado em sua triagem, §"Evidência fornecida versus observada"). Nenhuma autoridade adicional é emprestada a esses números por esta revisão; eles permanecem no estado de evidência fornecida.

## 4. BLOCKERS

Nenhum. Nenhum achado desta rodada invalida a arquitetura, quebra a baseline, introduz ciência incorreta no caminho real de execução (todos os valores que efetivamente atravessam `characterize_molecule_rdkit` em produção vêm de chamadas RDKit reais, já nos tipos nativos corretos) ou exige reabertura de decisão congelada.

## 5. MAJORS

**MAJOR-1 — DTOs não implementam a "validação estrita" exigida pela Seção 11, apesar de `frozen=True, extra="forbid"`.**

Evidência normativa: Seção 11, abertura — "DTOs públicos frozen, extra=forbid, com validação estrita, sem dict científico irrestrito e sem objetos do motor." A própria tarefa desta rodada instrui explicitamente: "não tratar frozen/extra=forbid como validação estrita suficiente."

Evidência de código: `src/molecular/characterization.py`, linhas 209–260 (`CharacterizationValues`) e 268–274 (`SdfParserParameters`). `model_config = ConfigDict(frozen=True, extra="forbid")` não ativa o modo estrito do Pydantic v2; os campos `molar_mass_g_mol: float`, `exact_mass_da: float`, `formal_charge_e: int`, `heavy_atom_count: int`, etc. usam tipos simples sem `strict=True` em `Field()` nem `model_config=ConfigDict(strict=True)`. Os `field_validator`s existentes (linhas 222–260) cobrem exatamente três coisas — bool-mascarado-de-int/float, não-finito, positividade — e nada além disso.

Reproduzido de forma totalmente independente por mim (§2, evidência completa em `evidence/claude-dto-coercion-reproduction.json`), numa terceira versão de Pydantic (2.13.5) distinta das duas já usadas pelo arquiteto (2.14.0) e pelo implementador (2.14.1): `heavy_atom_count` aceita `"3"` (str) e `3.0` (float), coercionando para `int`; `formal_charge_e` aceita `"0"` (str); `molar_mass_g_mol` aceita `"46.069"` (str); `SdfParserParameters(sanitize=1)` (int) é aceito e coercionado para o campo `Literal[True]`. Todas essas chamadas deveriam, pela própria redação da Seção 11, ser recusadas por tipo.

Classificação: **MAJOR, não BLOCKER**. No caminho real de produção (`characterize_molecule_rdkit` → RDKit real → `CharacterizationValues(...)`), todo valor chega já no tipo nativo correto (float/int reais vindos de chamadas RDKit), então este gap não corrompe nenhum resultado científico observado nos testes atuais. Mas é uma lacuna real e reproduzível entre o texto do contrato e a implementação, no próprio objeto que esta etapa existe para entregar (DTOs/perfis — primeiro item do `review_scope` desta tarefa), e representa um risco de silêncio: uma futura chamada manual, um teste mal escrito ou uma integração do Checkpoint 2 que monte esses DTOs a partir de dados menos controlados (por exemplo, de um YAML) passaria por este contrato sem o fail-closed que a Seção 11 promete.

Correção proposta (sem exigir mudança de forma do JSON público nem de nomes de campo — mecânica, dentro da allowlist já autorizada): adicionar `strict=True` a cada `Field()` numérico afetado em `CharacterizationValues` e aos literais booleanos/numéricos dos blocos de `effective_parameters` (`SdfParserParameters.sanitize`, etc.), ou `model_config=ConfigDict(frozen=True, extra="forbid", strict=True)` nessas classes especificamente, revalidando que os `field_validator`s de bool-rejeitado continuam necessários sob modo estrito (Pydantic estrito já rejeita bool→int por padrão, então essa parte pode simplificar).

**MAJOR-2 — T-020A-076/077 (KeyboardInterrupt/SystemExit por fase) não têm teste dedicado, apesar de exigidos expressamente para este checkpoint.**

Evidência normativa: a matriz da Seção 16 lista T-020A-076 ("Interrupção preservada; handles/logs restaurados; sem compensação/persistência") e T-020A-077 ("Mesma garantia verificada por teste separado/parametrização real") como cenários contratuais da especificação congelada. A triagem do arquiteto cita explicitamente que a solicitação aprovada de CP1 os exigia separadamente e instrui "não postergar automaticamente o adaptador para CP2, cujo escopo são leitores/serviço" — ou seja, o próprio arquiteto já descartou a hipótese de que isso seria adiável.

Evidência de código: o próprio relatório do implementador (Seção 6.4, item 3) concede a ausência: "não foram exercitados por teste automatizado nesta etapa". Confirmei por leitura direta e por `grep -n "except "` em todo o arquivo `src/molecular/rdkit_tautomer.py` que **nenhuma cláusula `except BaseException` existe** — apenas `except Exception` e exceções específicas (`OSError`, `UnicodeDecodeError`, `Chem.MolSanitizeException`, `ValueError`, `CharacterizationError`/subclasses) — o que estruturalmente garante que `KeyboardInterrupt`/`SystemExit` sempre se propagam sem conversão. O uso de `with rdBase.BlockLogs():` como gerenciador de contexto (confirmado nas dez ocorrências do arquivo) também garante restauração do estado de log mesmo quando uma exceção (incluindo `KeyboardInterrupt`) atravessa o bloco, porque `__exit__` do gerenciador de contexto executa no desenrolamento normal do Python para essas exceções.

Classificação: **MAJOR, não BLOCKER**, pela mesma razão que o próprio relatório já documenta honestamente em vez de ocultar: a garantia estrutural existe e é verificável estaticamente (nenhum `except BaseException`, uso correto de context manager), mas a obrigação contratual explícita desta etapa — um teste dedicado, por fase, como já existe no padrão legado (`test_sdf_source_raises_keyboard_interrupt_when_iteration_is_interrupted`, Incremento 017) — está ausente, não parcialmente coberta. Isso é uma lacuna de evidência exigida, não um defeito de comportamento observado, mas a tarefa desta rodada é explícita que uma lacuna de teste requerida para o CP1 não deve ser tratada como cosmética.

## 6. MINORS

**MINOR-1 — Teste de restauração de log (T-020A-078) não segue o padrão de prova já estabelecido no projeto.**

`tests/test_rdkit_tautomer.py`, linhas 1572–1585 (`test_native_rdkit_logs_are_suppressed_and_restored`): o teste verifica que `"ERROR"` não aparece em `captured.err` após uma falha, e então executa um **segundo cálculo bem-sucedido** como evidência indireta de restauração. Isso contrasta com o padrão já existente no mesmo arquivo para a enumeração de tautômeros (linhas 282–318: `test_enumeration_logs_are_suppressed_and_restored_after_incomplete_status` e `test_successful_enumeration_restores_rdkit_logs`), que chamam `rdBase.LogWarningMsg(marker)` depois da operação e verificam `marker in captured.err` — uma prova direta e explícita de que o supressor foi desarmado, exatamente o que T-020A-078 pede ("emissão após sucesso, exceção e interrupção com capfd/subprocesso").

Um segundo cálculo bem-sucedido é evidência indireta razoável (se os logs estivessem permanentemente suprimidos, isso não impediria um cálculo de dar certo), mas não é a mesma prova. Como a implementação usa corretamente `with rdBase.BlockLogs():` (gerenciador de contexto, restauração garantida em sucesso/exceção/interrupção por construção da própria API RDKit), a confiança na correção do comportamento é alta independentemente deste teste — mas a obrigação de T-020A-078 como escrita não está plenamente satisfeita. Recomendo adicionar a emissão do marcador explícito, replicando o padrão já estabelecido, nos três casos (sucesso, exceção, interrupção).

**MINOR-2 — Testes de SGroup/estereogrupo (parte de T-020A-038/039) exercitam a função de decisão diretamente com objetos RDKit construídos via API, não por bytes de arquivo real.**

`tests/test_rdkit_tautomer.py`, linhas 1234–1267. O próprio relatório (Seção 6.4, item 2) descreve honestamente essa limitação: construir um SDF V3000 real com `COLLECTION`/`STEAND` manuscrito não foi trivial no tempo desta etapa, e os testes chamam `_validate_graph_eligibility(mol)` diretamente sobre um `Mol` construído via `Chem.CreateMolSubstanceGroup`/`Chem.CreateStereoGroup` (API pública real, não mock). Isso é um teste de unidade legítimo da função de decisão, no mesmo padrão já usado em `_classify_record_counts` da base de código existente — mas não comprova que um arquivo SDF/SMILES hostil real chegaria ao RDKit exatamente nessa forma pelo caminho completo `_parse_molecule_rdkit` → elegibilidade. Diferente do MAJOR-2, aqui a lacuna é de integração (bytes→parsing→elegibilidade), não de comportamento de interrupção, e o relatório já a registra como pendência explícita para completar — ainda dentro do escopo nominal de CP1, visto que T-020A-038/039 aparecem na própria matriz do CP1 na reconciliação do relatório.

## 7. NOTES

**NOTE-1 — Disposição do comando `Z` do SVG: correta, sem alteração de contrato.**

`tests/test_rdkit_tautomer.py`, linhas 1452–1474 (`test_filled_wedge_triangle_z_command_is_an_unresolved_profile_gap`); `src/molecular/characterization.py`, linha 650 (`_D_COMMAND_ARITY = {"M": 2, "L": 2, "Q": 4}`). Confirmei por leitura direta que a gramática aceita apenas M/L/Q — `Z` cairia no ramo de recusa (`command not in _D_COMMAND_ARITY`). O implementador relata, reproduz e documenta esse gap exatamente como a Seção 10.1 exige ("saída que exija comando não coberto falha explicitamente, sem ampliar o perfil silenciosamente... Qualquer incompatibilidade deve ser relatada"): a especificação já antecipava esse risco (confrontada contra cinco desenhos mais o canário obrigatório de antraceno, nenhum deles exigindo cunha preenchida) e instrui explicitamente a não ampliação silenciosa. Este revisor concorda com a disposição do arquiteto: não é defeito de implementação, é uma limitação de cobertura do perfil já disclosed e corretamente tratada (`depiction-failure`, sem resultado parcial, sem expansão da gramática `d`). Fica para decisão explícita do responsável/arquiteto, fora desta revisão, se vale ampliar a gramática para incluir `Z` num incremento futuro — não antes do Checkpoint2/3, e não por preferência deste revisor.

**NOTE-2 — Alocação do validador de SVG em `characterization.py`, e não em `rdkit_tautomer.py` como a Seção 4 descreve textualmente, é aceitável.**

A Seção 4 atribui "desenho e validação do SVG" a `rdkit_tautomer.py`. O implementador colocou `validate_and_bind_depiction_svg` em `characterization.py`, delegando a chamada a partir de `rdkit_tautomer.py`. Verifiquei que isso não viola os invariantes que de fato importam: `characterization.py` não contém nenhum import de `rdkit` (confirmado por leitura e também coberto pelo próprio teste `test_module_never_imports_rdkit`, baseado em `ast`), e todo import RDKit novo permanece confinado a `rdkit_tautomer.py` (confirmado por leitura das linhas 57–87 desse arquivo). A própria Seção 4 permite ajuste de "nomes internos de estruturas auxiliares" na revisão, desde que responsabilidades/JSON público/invariantes não mudem silenciosamente — nenhum deles mudou. Tratado como preferência de organização, não achado, conforme instrução explícita da triagem do arquiteto.

**NOTE-3 — Pequena imprecisão aritmética no relatório do implementador (não um defeito de código).**

O relatório (Seção 3, tabela) declara "+680 inserções, −1" para `rdkit_tautomer.py`. `git diff --numstat` entre a baseline e o HEAD mostra, de forma independente e reprodutível, `679 1 src/molecular/rdkit_tautomer.py` — ou seja, +679/−1, consistente com a contagem de 679 que o próprio arquiteto já havia citado via API do GitHub. O total do `git diff --stat` completo (3094 inserções, 1 remoção) está correto; apenas a célula individual dessa linha da tabela está com um erro de contagem de um. Classificado como precisão de relatório, sem efeito sobre o código ou os testes.

**NOTE-4 — Limites desta revisão quanto a evidência RDKit/Windows.**

Confirmo, por leitura direta e correta do código-fonte, que a estrutura dos dez valores científicos, dos blocos de `effective_parameters`, da taxonomia de erros e das fronteiras de import está fielmente alinhada com as Seções 8/9/11/13/15 da especificação congelada. Não pude, nesta sessão, executar RDKit real nem pytest (§2) — portanto, os resultados numéricos específicos (vetor de referência da cafeína, discriminantes Strict/TPSA, hash da fonte Telex no wheel Windows, as contagens "111/142/1667/1476 passed") permanecem como evidência relatada pelo implementador, examinada quanto à plausibilidade e à estrutura do código que a produz, mas não reexecutada por mim. Isso é consistente com o próprio limite que o arquiteto já declarou em sua triagem.

**NOTE-5 — Confirmações positivas.**

Verificação direta de código confirma: as 16 chaves de `CharacterizationProvenance` e as 6 chaves de `MolecularCharacterizationResult` correspondem exatamente à Seção 11; os invariantes cruzados (svg/drawing ambos presentes ou ambos ausentes, hash/tamanho do SVG final, checksum case-insensitive, bloco `parser` correspondendo ao formato resolvido, vocabulário fixo de `warnings`) estão implementados como `model_validator`s reais, não como comentário ou promessa; as constantes `MAX_TOTAL_ATOM_COUNT=4096`, `MAX_BOND_COUNT=8192` e `REQUIRED_ENGINE_VERSION="2026.03.6"` batem exatamente com a Seção 6/8; a fronteira opcional de import (`_RDKIT_IMPORT_ERROR` vs. `_RDKIT_DRAWING_IMPORT_ERROR`, dois blocos `try/except ImportError` distintos, nunca um sobrescrevendo o outro) está implementada exatamente como a Seção 15 exige; a taxonomia de erros usa um `_allowed_reasons: frozenset[str]` por categoria, verificado no construtor da classe-base — ou seja, falha-fechado por construção, não por convenção; os testes científicos (cafeína, HBD/HBA, Strict/NonStrict, TPSA S/P) chamam genuinamente a API RDKit real para gerar o valor de comparação dentro do próprio teste, em vez de apenas repetir um número mágico — bom padrão de teste discriminante, já usado no projeto.

## 8. Conformidade e regressões dentro do escopo do CP1

Nenhuma regressão identificada: `rdkit_tautomer.py` e `test_rdkit_tautomer.py` só recebem adições (uma linha de import ampliada, zero remoções de comportamento); `tests/test_cli.py`, fora da allowlist, não foi tocado, e a falha pré-existente ali (dependência direta de `rdkit` sem `importorskip`, citada no relatório, Seção 6.4 item 4) é estrutural da baseline — não decorre deste diff, confirmado trivialmente pelo fato de `cli.py`/`test_cli.py` não aparecerem em `git diff --name-only`. Não encontrei nenhuma exigência especulativa de Checkpoint2/3 sendo cobrada aqui; os itens que o próprio relatório marca "fora de escopo do Checkpoint1" (T-020A-011 a 026, 066 a 077 exceto 069/076/077, leitores/serviço/CLI) foram conferidos como de fato ausentes do diff, consistente com a allowlist de quatro arquivos.

## 9. Veredito

**BLOCKER: 0 / MAJOR: 2 / MINOR: 2 / NOTE: 5**

Os dois MAJORS são defeitos reais e reproduzidos de forma independente (não apenas aceitos por autoridade do arquiteto ou do implementador), ambos no escopo nuclear desta etapa (DTOs/perfis — primeiro item do `review_scope`; interrupções exigidas explicitamente para CP1). Nenhum exige mudança de arquitetura, de forma do contrato JSON público ou de arquivo fora da allowlist já autorizada — ambos são corrigíveis dentro dos quatro arquivos já liberados, sem nova decisão arquitetural. A disposição do comando SVG `Z` está correta e não constitui achado. As confirmações positivas (§7, NOTE-5) e a ausência de regressão (§8) indicam uma implementação estruturalmente sólida e fiel ao contrato na grande maioria de sua superfície.

**Verdict: REQUEST CHANGES.**

Não por falta de qualidade geral — a implementação é extensa, bem organizada e, na maior parte, fiel ao contrato — mas porque os dois MAJORS são exatamente o tipo de lacuna que este checkpoint existe para pegar antes de autorizar o próximo. Recomendo uma rodada de correção focal, restrita aos quatro arquivos já autorizados: (a) tornar estritos os campos numéricos/literais de `CharacterizationValues` e dos blocos de `effective_parameters` (MAJOR-1); (b) adicionar testes dedicados de injeção de `KeyboardInterrupt`/`SystemExit` por fase do adaptador, no padrão já estabelecido pelo Incremento017 (MAJOR-2); e, se o tempo permitir na mesma rodada, os dois MINORS (marcador explícito de restauração de log; integração real de bytes para os casos de SGroup/estereogrupo).

READY FOR CHECKPOINT 2 REVIEW GATE: **NO** — pendente da correção e reverificação dos dois MAJORS. Isto não é uma declaração sobre a qualidade do Checkpoint 2 em si, apenas sobre a prontidão do CP1 para ser considerado encerrado.
READY FOR IMPLEMENTATION (CP2/CP3): NO
CHECKPOINT 1 APPROVED BY THIS INDEPENDENT REVIEW: NO
CHECKPOINT 2 AUTHORIZED: NO
CHECKPOINT 3 AUTHORIZED: NO
FINAL SPECIFICATION FROZEN: YES (inalterado por esta revisão)
FROZEN SVG GRAMMAR AMENDED: NO
CONTRACT OR SCOPE CHANGED BY THIS REVIEW: NO
CODE REPOSITORY MODIFIED: NO
GOVERNANCE CENTRAL STATUS/TASKS EDITED BY THIS REVIEWER: NO
PR/MERGE/FORCE-PUSH/AMEND/RESET/REBASE PERFORMED: NO
TESTS INDEPENDENTLY EXECUTED BY THIS REVIEWER: PARTIAL — one isolated reproduction of the DTO-coercion finding (Pydantic only, no pytest, no RDKit); full suite execution (pytest, RDKit-dependent tests, Windows evidence) not possible in this sandbox and not claimed
