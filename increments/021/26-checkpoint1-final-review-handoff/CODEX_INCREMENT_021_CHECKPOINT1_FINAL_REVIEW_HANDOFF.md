# Recebimento residual e encaminhamento à revisão final curta — Incremento 021, CP1

Data: 24/11/2026, America/Sao_Paulo. Codex arquiteto. Natureza: recibo e triagem, sem aprovação de CP1 nem fechamento independente.

## 1. Snapshots e escopo

Governance de entrada: docs/020-a-candidate1-review-20261020 @ 1bf4d4d1eefad1aa0ce3c693bf8738ab32344f54. Código recebido: feature/increment-021-receptor-materialization @ bbd491e1a0b3fcb913c3549b004120693212df62, pai único 42b4804b5f4ea01ddf320c45473d8b4f980ea67e. Main código permanece 08b797e0985e123ffd4d7ca7e5a5e8f040e63851; main governance permanece a47183dfec8213c765ed43ae482c8c227760a3d5. Nenhum código foi alterado pelo arquiteto.

Entrega: claude/021-cp1-residual-corrections-20261124 @ 74fb0c39fbf3f56b43936491aa2c0789a53ecf31, pai b9d9592dc6b08bc05e9c848c44057f33d229df7f, cujo pai é o snapshot de coordenação 1bf4d4d. Só treze arquivos próprios adicionados (relatório + doze evidências); nenhum STATUS/task/histórico alterado nessa branch. Não fiz merge dela.

Delta 42b4804..bbd491e: apenas os dois arquivos permitidos, módulo +60/−5, testes +265/−41. Acumulado baseline..bbd491e: os mesmos dois arquivos A/A. O código não foi rebaseado contra a baseline: a cadeia aditiva anterior está preservada.

## 2. Identidades conferidas

| Material | Linhas | Bytes | SHA-256 |
|---|---:|---:|---|
| src/molecular/receptor_materialization.py | 1.724 | 78.807 | d8fc55db900f761f0debe4cea29f05cade1502ea1299937f123c6c883e30431d |
| tests/test_receptor_materialization.py | 1.645 | 81.362 | e67539e76be9d174e7ef2c93cf971faa6bfba3316ef996f5e4a55c9345a90d69 |
| CLAUDE_INCREMENT_021_CHECKPOINT1_RESIDUAL_CORRECTIONS_REPORT.md | 136 | 14.088 | 6d3b254bd6854076180600d2e5114a7838e5ca44f3bdaea00568c7b181941e7d |

As quatorze entradas do manifesto (dois arquivos de código + doze arquivos de relatório/evidências, excluindo o próprio manifesto) conferem em linhas/bytes/SHA-256 e blob Git; o próprio manifesto também confere com o blob. A cópia externa dos 68 arquivos do snapshot foi verificada por Git SHA. Contrato congelado e quatro anexos permanecem byte-idênticos, identificados na tarefa. O log de suíte usa CP1252; sua vista textual foi reconvertida apenas depois de coincidirem Git SHA e SHA-256, como no recibo anterior. Não confundir recodificação do conector com alteração do manifesto.

## 3. Resultados fornecidos versus observação própria

Implementador informa Windows/Python 3.14.7, 91 passed no arquivo e 1567 passed/5 skipped na suíte completa, 1572 coletados. Não executei pytest, suíte completa, Windows, Gemmi nativo, RAW ou concorrência. Os cinco skips estão nomeados no log do implementador; nenhuma contagem histórica foi apresentada como execução minha.

Conferência mecânica: antes 1556, depois 1572; 75→91 funções, zero parametrizações; diferença líquida +16. Há **17 node IDs novos e um antigo removido por renomeação** do teste legado: test_minor7_golden_legacy_inspection_id_matches_the_020_production_helper foi substituído por test_minor7_golden_legacy_inspection_id_calls_the_new_helper_against_independent_literal. Isso corresponde à remoção da prova tautológica explicitamente pedida, não à exclusão de um cenário normativo. O revisor deve confirmar que a nova prova é mais forte; não exigir nome antigo apenas por preferência. Os 43 cenários normativos continuam sendo o conjunto a preservar, não uma contagem de funções novas.

Executei em Linux/Python 3.12.14/Pydantic 2.13.4 dois subprocessos (-I -B normal e -O), bloqueando Gemmi/RDKit sem stub. Reusei a sonda documental pura do recibo 22 com os mesmos limites: ProteinInput/policy reais e namespaces documentais de inspection/resolution, sem prova de parsing ou validação 020. As duplicatas/nomes inválidos e contradições de formato antes aceitas agora recusam; controles válidos continuam aceitos. Os treze vetores independentes da reconciliação 24 foram comparados separadamente às funções reais do novo snapshot e coincidem. Whitespace dos dois deltas foi verificado em cópia externa, limpo.

evidence/ARCHITECT_FINAL_RECEIPT_VERIFICATION.json identifica blobs, contagens, sondas, os treze hashes e limitações. As sondas não constituem revisão independente nem autorização de publicação científica. Não pude observar a working tree Windows/itens locais protegidos; sua preservação é declaração do implementador.

## 4. Próximo gate: revisão final curta

Preparada tasks/021-CHECKPOINT1-FINAL-FOCAL-REVIEW.json, para Claude revisor separado de todas as sessões implementadoras. Escopo: MAJOR-A residual (severidade MINOR) formatos; MINOR-3 unicidade intra-tupla/gramática; MINOR-7 hashes literais/envelopes/helper novo. Os nove fechamentos independentes e três NOTES permanecem preservados; só regressão concreta no delta permite reexame.

O revisor deve confirmar aliases020 e recusa INVALID_RECORD sem modificar proveniência; aceitar/refusar os nomes/ordinais do perfil; comparar literais independentes e as chamadas de produção, inclusive helper novo legado. Conferir a renomeação e a cobertura de regressão, sem exigir adapter/storage/CLI/CP2, novo estudo ou hardening fora do contrato. Não tratar como fechado porque a triagem é positiva. Classificações documentais de 40 provados/3 parciais por desenho/0 lacunas permanecem respeitadas no nível CP1.

Saída: increments/021/27-checkpoint1-final-focal-review/CLAUDE_INCREMENT_021_CHECKPOINT1_FINAL_FOCAL_REVIEW.md e evidence/claude-*, em branch própria do governance baseada na publicação desta tarefa. Nenhum agente foi acionado automaticamente. Depois do parecer, caberá a decisão de aprovação do CP1 e autorização separada de qualquer checkpoint posterior.

RESIDUAL DELIVERY RECEIVED AND VERIFIED: YES
READY FOR SHORT INDEPENDENT FINAL FOCAL REVIEW: YES
RESIDUALS INDEPENDENTLY CLOSED: NO
CHECKPOINT1 APPROVED: NO
CHECKPOINT2 IMPLEMENTATION AUTHORIZED: NO
FINAL SPECIFICATION FROZEN: YES
CODE REPOSITORY MODIFIED BY ARCHITECT: NO
AUTOMATED DISPATCH: NO
