# Recebimento arquitetural do parecer do estudo 021

Data: 23/11/2026. Autor: Codex arquiteto. Natureza: recibo de leitura e verificação documental; não é reconciliação técnica, aprovação do responsável ou fechamento dos achados.

## Snapshot lido

- Governance de coordenação: e6848903b1d0b342470fed59e43d39e4482a471a.
- Branch do revisor: claude/021-study-review-v2-20261123.
- Commit do parecer: debeba6f4370c6f5dd77d2273420abf8a828e9f8, confirmado no remoto.
- Parent único do parecer: e6848903b1d0b342470fed59e43d39e4482a471a.
- Código main observado: 08b797e0985e123ffd4d7ca7e5a5e8f040e63851.
- Main do governance observada: a47183dfec8213c765ed43ae482c8c227760a3d5.

O diff da branch do revisor contra sua base contém quatro adições: parecer e três evidências, sem alteração ou remoção de arquivos preexistentes. Os caminhos de evidência estão dentro de increments/021/02-study-review/evidence/; a forma abreviada evidence/... no aviso do chat não é um caminho na raiz do repositório.

## Identidades conferidas

| Arquivo | Linhas | Bytes | SHA-256 |
|---|---:|---:|---|
| increments/021/02-study-review/CLAUDE_INCREMENT_021_STUDY_WITH_CONTINUATION_REVIEW.md | 198 | 20580 | 649c67b0f72186504a083d6041b53d7f5becf8d4f27ac89c1885c5a32843708e |
| increments/021/02-study-review/evidence/claude-021-study-review-verification.json | 86 | 5221 | 36380b1582199aecf1d91fa7d80e3be1208a04b859ec5ee4ffd4f8ac563c3036 |
| increments/021/02-study-review/evidence/claude-gemmi-cif-token-probe.cpp | 32 | 1593 | 08fbe986b5b3b9ec9bff79814868e05ab4a5f4b0a2aea410c56cb1d4ca834949 |
| increments/021/02-study-review/evidence/claude-gemmi-cif-token-probe.output.txt | 35 | 743 | 5fc27870af5ad3b0030fcdff07d5efff80e55fe29fc1100cf1eb73108402e1a9 |

O SHA-256 do parecer, suas linhas e bytes coincidem com os valores completos informados pelo revisor. Os hashes da sonda e da saída também coincidem com os valores registrados na evidência JSON. A evidência JSON foi lida e recebeu hash completo neste recibo. A contagem de linhas é de linhas separadas por LF, preservando a quebra final observada.

O arquiteto leu integralmente o parecer e os três arquivos de evidência pelo commit identificado. A verificação de hash usou os bytes UTF-8 do conteúdo remoto e um controle conhecido SHA-256 de abc. Não houve execução da sonda C++, pytest, Gemmi Python, Windows ou ensaio concorrente por este recibo.

## Estado dos achados: recebidos, não reconciliados

| Item | Conteúdo recebido do revisor | Estado |
|---|---|---|
| MAJOR-1 | Cortes de conexão versus disposições amplas de água/metal; opções a/b | Aberto para confronto e recomendação arquitetural; decisão de escopo do responsável pendente |
| MAJOR-2 | Universo de ocorrências e precedência cadeia/disposição/complemento | Aberto; tabela implementável ainda necessária |
| MAJOR-3 | Colunas de inserção e correspondência de endpoints; ptnr3/simetria/modelos | Aberto; conferir fontes pinadas, sem corrigir o 020 por esta tarefa |
| MAJOR-4 | Leitores públicos versus hash da mesma leitura; identidade exata de id | Aberto; escolher mecanismo coerente com allowlist |
| MINOR-1 | Remoção de resíduo polimérico modificado | Aberto |
| MINOR-2 | Tratamento tudo-ou-nada de branched/glicanos | Aberto |
| MINOR-3 | Catálogo adicional de categorias referenciadas | Aberto |
| MINOR-4 | Gate de parser-limitation | Aberto |
| MINOR-5 | Matriz individual de cenários | Aberto |
| C-1/C-2/C-3 | Ambiente Gemmi inconsistente; nomes de colunas; abrangência de report.chains | Recebidas para verificação, sem edição retroativa do estudo/evidências |
| NOTE-1/2/3 | Limites da sonda; precedente de criação exclusiva; declaração/execução | Recebidas para disposição na reconciliação |

Contagem do parecer recebido: 0 BLOCKERS, 4 MAJORS, 5 MINORS, 3 NOTES. O arquiteto não converteu correções factuais C-1 a C-3 em contagem adicional, nem declarou qualquer achado fechado por ter lido o parecer.

O veredito do revisor é APPROVE FOR DRAFT SPECIFICATION, condicionado à absorção dos quatro MAJORs antes ou dentro do rascunho. Isso permite discutir o rascunho como próximo estágio; não significa recorte fechado ou pronto para implementação. A prontidão arquitetural/decisão do responsável será registrada após a reconciliação, sem inferi-la do título favorável.

A execução C++ em Linux é evidência fornecida pelo revisor, cujo código/saída foram lidos, não execução reproduzida pelo arquiteto. Os limites declarados de Python/Windows/concorrência e de consulta web permanecem explícitos. Não se confirma frequência de casos no arquivo PDB por esta leitura.

## Próximo passo e comunicação

A próxima tarefa do arquiteto é tasks/021-STUDY-RECONCILIATION.json. A orientação de entregas é communications/GOVERNANCE_DELIVERY_INSTRUCTIONS_20261123.md. O responsável pode indicar apenas branch/commit/path; o arquiteto consulta a fonte remota sem exigir colagem do parecer no chat.

Não houve merge da branch do revisor nem cópia/modificação de seu parecer. O apontamento por SHA é suficiente. O estudo v1, complemento, tarefas antigas e documentos do 020-A permanecem intactos.

REVIEW RECEIVED AND READ: YES
REVIEW IDENTITY VERIFIED: YES
RECONCILIATION COMPLETE: NO
FINDINGS CLOSED BY THIS RECEIPT: NO
READY FOR IMPLEMENTATION: NO
FINAL SPECIFICATION FROZEN: NO
CODE REPOSITORY MODIFIED: NO
