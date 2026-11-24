# Recebimento de R-1 e encaminhamento focal — Incremento 021, CP1

Data: 24/11/2026, America/Sao_Paulo. Autor: Codex arquiteto. Natureza: recebimento técnico e preparação da reverificação independente; não é fechamento independente nem aprovação de CP1.

## 1. Snapshots confirmados

| Objeto | Snapshot remoto observado |
|---|---|
| Coordenação de entrada | docs/020-a-candidate1-review-20261020 @ 771ae24f6289e41a2f8c7e17906bf294925bd375 |
| Código corrigido | feature/increment-021-receptor-materialization @ ea8dac9cdc203c337d7f3f9947b54042291f7484 |
| Pai direto do código | bbd491e1a0b3fcb913c3549b004120693212df62 |
| Entrega do implementador | claude/021-cp1-r1-test-correction-20261124 @ b35bb8e9d32e6fb4bc95e903f786fa0c1240e2d2 |
| Main código | 08b797e0985e123ffd4d7ca7e5a5e8f040e63851, preservada |
| Main governance | a47183dfec8213c765ed43ae482c8c227760a3d5, preservada |
| Parecer que originou R-1 | edb8764b4d4ee56e49ff849b65b950e5e430fae0 |

As refs foram consultadas diretamente no GitHub. A entrega do governance tem dois commits próprios sobre a coordenação de entrada, apenas dez arquivos adicionados sob `increments/021/29-checkpoint1-r1-test-correction/`. Nenhum STATUS/tarefa central foi alterado pelo implementador. A árvore local Windows não é observável por esta sessão; seu diagnóstico limpo é informação fornecida pelo implementador.

## 2. Identidades e escopo observados

O relatório do implementador tem 133 linhas, 10.445 bytes e SHA-256 `a275e1634808c4c0386d52ff90f8bf733e39894d140ccd7c262bf3bdca7c17e6`. Seu manifesto tem 98 linhas, 4.613 bytes e SHA-256 `fb2e1960efebddcbea8ee499bdf638726148202d17f5783ba62cc2830d11a87d`. As onze entradas do manifesto (dois arquivos de código e nove documentos/evidências) conferem em linhas, bytes e SHA-256; os blobs Git foram confrontados com as árvores remotas. O manifesto também foi verificado pelo próprio blob Git.

O delta `bbd491e..ea8dac9` altera exclusivamente `tests/test_receptor_materialization.py`: 31 inserções e zero exclusões. Produção permanece byte-idêntica: 1.724 linhas, 78.807 bytes, SHA-256 `d8fc55db900f761f0debe4cea29f05cade1502ea1299937f123c6c883e30431d`. O arquivo de testes final tem 1.676 linhas, 83.570 bytes, SHA-256 `9f72301ece6e55ef11d78d589f20822673887af10eeee1365d209099c3658ada`.

A comparação AST própria remove apenas a função adicionada e reproduz toda a AST anterior: nenhum import, helper, constante, teste anterior ou outro enunciado mudou. São 91 → 92 funções de teste. O diff cumulativo `08b797e..ea8dac9` continua restrito aos dois arquivos originais do CP1. Não houve modificação em contrato, módulos do 020, CLI, dependências ou lógica científica por este delta.

## 3. Verificação própria restrita a R-1

O teste novo usa `(ordinal=3, atom_id="a")`, depois `(ordinal=1, atom_id="Z")`, com bytes manuais e os dois SHA-256 literais já fornecidos pelo arquiteto. A ordem difere tanto da ordenação crescente de ordinal quanto da ordenação ASCII de ID. Os treze goldens e os 91 testes anteriores foram preservados.

Executei em Linux/Python 3.12.14 somente a função nova e seus dois helpers locais, extraídos da AST sem reescrever seus corpos, sobre o arquivo exato de produção remoto. Gemmi e RDKit foram bloqueados, sem sentinela/stub. A função passou na produção. Substituindo sua referência global por wrappers que ordenam por ordinal ou por atom_id antes de chamar a produção, a mesma função gerou AssertionError em ambos os controles. Isso prova a discriminação das asserções; não é execução pytest do módulo inteiro nem execução de arquivo de produção mutado. Nenhuma fonte foi alterada, inclusive na cópia desta verificação.

O script fornecido pelo implementador carrega produção e dois arquivos mutados externos e compara seus digests; sua saída indica que ambos são discriminados. Ele não executa diretamente a função pytest nova e os dois arquivos mutados não foram publicados. Isso é uma limitação de reexecução dessa evidência, não demonstra falha da correção. A revisão focal deverá confirmar diretamente a discriminação pela função nova, por pytest em cópia descartável se o ambiente permitir ou por extração AST explícita com limites declarados.

## 4. Testes fornecidos e contagem

Comparei os logs completos de coleta: 1.572 → 1.573 node IDs, exatamente a função nova adicionada, nenhum removido. O log focal informa 92 passed. O log completo informa 1.568 passed e 5 skipped; total 1.573, consistente com +1. Os cinco skips continuam identificados: application:1809/1847 e cli:4250/4303 exigem ausência de RDKit; atomic:1046 depende de privilégio de symlink no Windows. Os logs de execução são evidência fornecida, não pytest próprio.

O ambiente fornecido é Windows/Python 3.14.7/Pydantic 2.13.5/Gemmi 0.7.5/RDKit 2026.3.6/pytest 9.1.1. Não instalei dependências nem executei pytest, Gemmi nativo, RDKit, Windows, concorrência ou suíte completa. Os checks Git limpos são informados no log do implementador; observei diretamente o diff aditivo e ausência de whitespace final no arquivo testado, não alego execução local de `git diff --check` sobre o repositório original.

## 5. Disposição e próximo gate

Recebimento: conforme à tarefa de correção de teste, apto a reverificação independente restrita a R-1. R-1 permanece aberto até parecer independente; não há autorização de CP2. Os doze fechamentos funcionais do parecer anterior e as três NOTES são preservados, assim como os 43 cenários (40 provados/3 parciais por desenho/zero lacunas). Não se autoriza repetir revisão integral por preferência nem ampliar escopo.

A tarefa `tasks/021-CHECKPOINT1-R1-FOCAL-REVIEW.json` identifica todas as entradas e saídas. O revisor deve atuar em sessão separada do implementador, publicar parecer próprio em `increments/021/31-checkpoint1-r1-focal-review/` e não editar coordenação central. Nenhum Claude foi acionado automaticamente. Parecer favorável retorna ao arquiteto/responsável para o próximo gate; não aprova CP1 ou autoriza CP2 automaticamente.

R1 CORRECTION RECEIVED: YES
R1 INDEPENDENTLY CLOSED: NO
CHECKPOINT1 APPROVED: NO
CHECKPOINT2 IMPLEMENTATION AUTHORIZED: NO
FINAL SPECIFICATION FROZEN: YES
INCREMENT020A: STAND-BY
CODE REPOSITORY MODIFIED BY ARCHITECT: NO
AUTOMATED DISPATCH: NO
