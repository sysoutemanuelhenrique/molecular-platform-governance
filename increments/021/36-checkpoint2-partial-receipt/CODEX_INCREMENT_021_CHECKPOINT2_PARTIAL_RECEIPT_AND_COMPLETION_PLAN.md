# Incremento 021, CP2 — recebimento parcial e plano de conclusão

Autor: Codex arquiteto. Data: 24/11/2026, America/Sao_Paulo. Natureza: recebimento/triagem pontual e instrução de continuidade dentro do CP2 já autorizado. Não é parecer independente, revisão integral, aprovação de CP2 ou execução de Gemmi/pytest pelo arquiteto.

## 1. Identidades e escopo verificados

| Objeto | Snapshot |
|---|---|
| Coordenação de entrada | docs/020-a-candidate1-review-20261020 @ 399bbbc7bea95fa4eafcc6757bf2d8d8a166df30 |
| Código parcial | feature/increment-021-receptor-materialization @ 0d06ebd4c46c90e5446fec6f0eb72b4a8d2855db |
| Pai direto | ea8dac9cdc203c337d7f3f9947b54042291f7484, CP1 aprovado |
| Relatório do implementador | claude/021-cp2-implementation-report @ 9aa07628f2db61e68fc57b47d6e0e8e3dbeac80c |
| Main código | 08b797e0985e123ffd4d7ca7e5a5e8f040e63851, preservada |
| Main governance | a47183dfec8213c765ed43ae482c8c227760a3d5, preservada |

O relatório foi lido integralmente no remoto: 181 linhas, 23.706 bytes, SHA-256 `5f9e23e632db9dfd7908a61c683f86650aa9eea88dd2eb32dfab9345205fb139`. Sua publicação adiciona somente dez arquivos nos caminhos autorizados, sem STATUS/tarefas centrais. Verifiquei os quatorze blobs (quatro código e dez governance) por identidade Git/tamanho; as quatro entradas do manifesto de código também conferem em SHA-256/linhas. Uma cópia externa de todos os 68 arquivos do snapshot foi confrontada com a árvore remota para as sondas; nenhum repositório foi alterado.

O commit de código é filho direto do CP1 aceito e altera apenas os quatro arquivos autorizados: +3.833/−38. Nenhuma fixture foi publicada. O diff cumulativo continua restrito aos mesmos quatro caminhos. A comparação AST preserva os corpos de funções anteriores do teste de domínio CP1. Isso não prova equivalência de todos os comportamentos do domínio sob os novos dados.

## 2. Decisão arquitetural de encaminhamento

**Completar o CP2 antes de encaminhar uma revisão independente final.** A autorização humana já cobre implementação/testes/commit/push dos quatro arquivos e fixtures definidos, além de relatório próprio. Continuar esse mesmo escopo não exige nova autorização de checkpoint. O código de entrada da continuação passa a ser o commit parcial acima, sem reset/rebase/amend ou retorno destrutivo à baseline.

O relatório declara 53 cenários mapeados e 26 pendentes. Conferi mecanicamente que os dois conjuntos são disjuntos e cobrem os 79 IDs, e que os node IDs citados existem no log de coleta. **Mapeamento não equivale a fechamento independente nem a prova integral de cada requisito.** A frase “cenários não são funções pytest” não permite omitir cenários obrigatórios. A honestidade do relato preserva a utilidade da entrega parcial; não altera os critérios de aceite.

## 3. Pendências declaradas

Os 26 IDs permanecem exigidos: T021-041, 042, 043, 065, 066, 068, 069, 070, 071, 072, 073, 074, 080, 081, 086, 088, 089, 145, 146, 147, 148, 149, 155, 156, 157 e 162. A matriz derivada anexa preserva os 79 cenários e identifica o status apenas informado pelo implementador.

Não se trata apenas de adicionar testes. O próprio relatório admite contexto best-effort, conferência anisotrop parcial e ausência de contagens de posições especiais. As entradas reais 5i55/1pfe/3dg1_final, NMR multi-modelo, EM e NCS, mais o lineage dos positivos D-01(b), são escopo obrigatório CP2 (§23), não funcionalidades futuras nem itens fora de escopo. O mmCIF escrito à mão usado com Gemmi real é integração nativa sintética, não entrada de depósito real.

## 4. Correções contratuais concretas para a continuação

**C-01 — numéricos e NCS exato (MAJOR na triagem).** Em receptor_materialization.py:3486–3613, `_finite_numeric_token` usa float e `_guard_ncs_row` adota tolerância 1e-6. Executei a função real sem nativos: translação 0.0000001 com code=generate foi aceita como identidade, contrariando §11 (identidade Decimal exata; não identidade generate/null deve recusar UNSUPPORTED_NCS). O helper rejeita 1.2e3(4) e aceita 1_000; a gramática congelada exige o inverso nesses casos aplicáveis. Implementar a gramática/cálculo central Decimal e a identidade exata, sem converter tokens para serialização; acrescentar controles de quase identidade, su/expoente e todos os campos numéricos exigidos no RAW, não somente NCS/tensor.

**C-02 — hashes e duas visões do token (MAJOR).** Em receptor_materialization.py:3425–3443, `compute_source_rows_key` usa kind=receptor-materialization-source-rows e linhas cruas por coluna. SCHEMAS §4 exige source-category com vetor de row_key; cada row_key usa envelope source-row e tag/token fonte em ordem. A sonda documental recalcula o envelope congelado e diverge da função. `_build_category_tables` (receptor_parsing.py:1388–1396) ainda converte tanto ? quanto . em None, perdendo os tokens brutos necessários à auditoria. Com contexto documental constante, as duas entradas transcritas geram o mesmo resultado; isso demonstra perda de token nessa fronteira, não uma alegação de colisão de plano entre RAWs reais (cujos hashes de contexto mudariam). Manter separadas a visão bruta usada em hashes/escrita e a decodificada pelo Gemmi usada em identidades/lookup; testar quoted/unquoted, multiline e expressões de operador citadas. Não implementar outro parser CIF em Python. Conservar os envelopes CP1 já aprovados e criar goldens independentes dos novos envelopes.

**C-03 — verificação independente da saída (MAJOR).** receptor_parsing.py:1424–1465 verifica essencialmente contagem/presença de tags, sem receber os vetores de tokens/IDs esperados. A execução do helper exato extraído por AST aceitou uma tabela com id=CHANGED_ID e coordenada=NaN desde que a forma coincidisse. Isso é prova do helper, não execução de materialização CIF nativa. Passar as expectativas completas do plano/fonte e comparar ids/ordem/tokens/coordenadas/conexões/relações/categorias/tags e contagens, inclusive rejeição de extras. Testar mutações de saída preservando formato e exigir INVALID_OUTPUT/phase=verify; reparse pela mesma biblioteca sozinho não basta (§18).

**C-04 — RAW/pin/proveniência do teste integrado (MAJOR).** A função `materialize_receptor_cif021` (1468–1541) entra direto no parse; não confronta bytes/tamanho com SourceContext nem verifica o pin observado. O import Gemmi ainda é global (linha 35); a docstring o chama de tardio sem fazer a mudança. O teste integrado usa `_CP2_RAW_SHA="a"*64`, raw_size=10 e snapshots com hashes/tamanhos fictícios (test_receptor_parsing.py:576–619), embora entregue outro RAW. Completar o preflight CP2 de bytes/pin/limites/compressão da tarefa, sem implementar o leitor Windows do CP3, e usar hashes/tamanhos reais das fixtures e dos quatro documentos em integrações. Testar ausência/versão divergente sem stub de sucesso. Preservar comportamento/API do 020 e import puro do domínio.

**C-05 — integridade de catálogo, contextos e auditoria (MAJOR).** Executei `compute_category_decisions` com um polímero retido e sem entity_poly/entity_poly_seq/pdbx_poly_seq_scheme: o motor aceitou. As categorias são condicionais obrigatórias no catálogo. Completar chaves únicas/não nulas, vínculos asym/entity/seq/branch/CCD, correspondência anisotrop de todos os campos informados, contexto por modelo/resíduo/inserção/altloc e dados/contagens necessários à auditoria. Não chamar um filtro genérico de membership de validação referencial completa. As 94 categorias e os campos copiados do literal coincidem com a projeção correspondente do catálogo; os campos nonnull_key/unknown_tag_action/scenario_ids não estão no literal. Essa redução do literal não é por si um defeito: a prova exigida é execução equivalente das regras, não preferência por duplicar metadados documentais. Posições especiais hoje só testam label/auth de cadeia e emitem aviso por presença de categoria; devem resolver o contexto correto, contar interseção retida/átomos únicos e emitir aviso somente quando exigido. Entregar esses dados no adapter/DTOs CP2, sem antecipar persistência/service CP3. Os novos DTOs devem continuar fechados/estritos/imutáveis, inclusive suas estruturas internas.

**C-06 — identidade gerada e save frames (MINORs na triagem).** A linha 1528 gera `_entry.id` com TBMP_ maiúsculo, enquanto §11 exige tbmp_<plan_key> para entry e block. O teste novo copia a expectativa incorreta (linha 815), portanto deve ser corrigido junto da produção, preservando os testes CP1. `_reject_save_frames` usa regex de início de linha e recusa save_literal_inside_text em valor multilinha; reproduzi o comportamento exato do helper, sem Gemmi. A correção deve distinguir frames reais de texto e provar os dois com Gemmi 0.7.5 real, sem criar parser CIF artesanal. A prova nativa desse exemplo permanece responsabilidade da continuação.

**C-07 — reavaliar a comprovação, não apenas os 26 (obrigatório).** Os testes T021-164/166/168/169/170/171/172 usam DTOs e repetem o mesmo hash duas vezes, sem os RAWs/checksums/plan_key completos exigidos; T021-141 e 144 não usam as entradas reais previstas; T021-158 só cobre a guarda de contexto. Reclassificar essas provas como parciais onde necessário e fechar o requisito completo. Não tratar os 53 mapeados como aprovação herdada. Ajustar apenas oráculos CP2 errados com justificativa; não enfraquecer R-1, os treze goldens ou os 92 testes CP1. Separar casos/itens/funções e execução real por ambiente.

## 5. Execução, contagem e limites

Os logs fornecidos mostram 1.573 → 1.622 coletados (+49), 172 passed nos dois arquivos focais, 121 passed na regressão receptor 020 e 1.617 passed/5 skipped na suíte Windows. Comparei os node IDs com o log CP1 anterior: +49 e zero removidos. Os cinco skips continuam explicados no log. Não executei pytest, Windows, Gemmi nativo ou RDKit, nem instalei dependências. Estes números são evidência do implementador, não teste independente meu.

Minhas execuções foram sondas puras do domínio exato, e helpers exatos do adapter extraídos por AST, com Gemmi/RDKit bloqueados e sem sentinela nativa. O script anexo exige os SHA-256 dos dois fontes parciais antes de rodar, não grava na fonte e declara seus limites. Isso não certifica parsing/serialização nativa nem audita as 4.060 linhas integralmente. As classificações acima são triagem do arquiteto para completar o contrato, não fechamento pelo revisor independente.

## 6. Tarefa e saída autorizada

`tasks/021-CHECKPOINT2-COMPLETION.json` detalha a continuação. Mesma feature, commit aditivo sobre 0d06ebd, quatro arquivos e raiz de fixtures originais; nenhuma autorização nova de escopo é inferida. Relatório novo sob `increments/021/35-checkpoint2-implementation/evidence/claude-cp2-completion-report.md` e evidências `claude-completion-*`, dentro do glob já autorizado. Branch própria a partir do novo despacho, preservando relatório/branch parcial e os documentos históricos; sem editar STATUS/tarefas centrais. Não sobrescrever o relatório parcial nem prometer CP3.

Critério para encaminhar à revisão independente: contrato CP2 integralmente implementado, 79 cenários efetivamente comprovados com limites declarados, fixtures reais/lineage presentes, C-01–C-07 atendidos e regressão preservada. Impedimento genuíno deve apontar requisito/arquivo/evidência e manter o gate bloqueado; não autoriza reduzir a especificação ou pedir aprovação de um substituto sintético. O arquiteto receberá a nova entrega antes de preparar a revisão.

PARTIAL DELIVERY RECEIVED: YES
CONTINUE EXISTING AUTHORIZED CP2: YES
READY FOR INDEPENDENT FINAL CP2 REVIEW: NO
CHECKPOINT2 APPROVED: NO
CHECKPOINT3 IMPLEMENTATION AUTHORIZED: NO
FINAL SPECIFICATION FROZEN: YES
INCREMENT020A: STAND-BY
CODE REPOSITORY MODIFIED BY ARCHITECT: NO
AUTOMATED DISPATCH: NO
