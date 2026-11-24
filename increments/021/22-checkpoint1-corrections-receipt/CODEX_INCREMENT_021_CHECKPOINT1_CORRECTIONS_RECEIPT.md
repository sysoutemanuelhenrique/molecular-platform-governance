# Recebimento das correções e encaminhamento focal — Incremento 021, CP1

Data: 24/11/2026, America/Sao_Paulo. Papel: Codex arquiteto. Recebimento e triagem de evidências; não é fechamento independente dos achados nem aprovação de CP1. Código somente lido, nenhuma alteração científica ou contratual.

## 1. Snapshots remotos e cadeia

Coordenação: `docs/020-a-candidate1-review-20261020 @ 521500c18272a379dc4fa2557754d9fa30d60cb7`. Código: `feature/increment-021-receptor-materialization @ 42b4804b5f4ea01ddf320c45473d8b4f980ea67e`. Cadeia aditiva real: `08b797e0985e123ffd4d7ca7e5a5e8f040e63851 → 711f3070765efe67a5799f939f1a18306ed8afdd → 3ba2fa91eaa95cae070d0aea7dba0d1918d9fd33 → 42b4804b5f4ea01ddf320c45473d8b4f980ea67e`. Main código permanece em 08b797e; main governance permanece `a47183dfec8213c765ed43ae482c8c227760a3d5`.

Entrega: branch `claude/021-cp1-corrections-20261124 @ 010ee93aedf31bdcdfee513164b84aa40f3fbde4`, pai `452f12e8aede26038ba85726f16def94a1acd08c`, cujo pai é a coordenação 521500c. Acrescenta exatamente onze arquivos próprios (relatório + dez evidências), sem editar STATUS, tarefas, contratos ou históricos. Nenhuma branch do implementador/revisor foi mesclada.

O anexo de conversa recebido termina durante a edição dos testes e não contém entrega final. O recebimento efetivo usa os snapshots imutáveis publicados acima, conferidos no remoto antes de confrontar conteúdo e novamente antes de publicação desta resposta; não uso o texto incompleto como prova de conclusão.

## 2. Identidades e escopo

| Arquivo | Linhas | Bytes | SHA-256 |
|---|---:|---:|---|
| src/molecular/receptor_materialization.py | 1.669 | 75.461 | ef38b524adbbe7432e83171d63c675856e3b21777322faec001efab530704fb1 |
| tests/test_receptor_materialization.py | 1.421 | 67.030 | 7064aa8d7e36902f9e85a3ae4e075b118f8b5dd391029bf9652a53cbdd883eb8 |
| CLAUDE_INCREMENT_021_CHECKPOINT1_CORRECTIONS_REPORT.md | 154 | 14.940 | 5e03d83a35154c52330a6a5f420d17a2e426947ef5d0041cf2fb9ee29fc96875 |

As doze entradas do manifesto (dois arquivos de código + dez arquivos do relatório/evidências, excluindo o próprio manifesto) conferem em linhas/bytes/SHA-256 e contra os blobs Git. O manifesto também foi confrontado com o blob remoto. Toda a cópia externa usada nos ensaios confere com os 68 blobs do snapshot 42b4804. Cinco documentos normativos foram verificados contra os blobs preservados da coordenação e suas identidades congeladas.

Diff 711f307..42b4804: apenas M/M nos dois arquivos permitidos; módulo +304/−53, testes +644/−14. Diff baseline..42b4804: apenas A/A nesses arquivos. A cadeia contém dois commits de correção, não um novo filho direto da baseline. whitespace verificado nas cópias externas com git diff --no-index --check, sem saída de erro. A árvore Windows e os três itens locais protegidos não estão acessíveis a mim; sua preservação permanece declaração do implementador.

**Transporte do log:** o log da suíte tem 3.003 bytes, SHA-256 `15c40b9336b5e007557c9ba28fe6c52b7b5ae99663fb67455a854ba9f1d2b611`, blob `67f5d86a1fb48d0d44e6afd95fdb2af5a06c61aa`. A leitura textual do conector o recodifica para UTF-8 (3.006 bytes); a rota direta de blob acusou byte 0xe3 inválido para UTF-8. Reconstruí a representação original pela codificação CP1252 do texto recebido e aceitei os bytes **somente** depois de coincidirem tanto com o Git SHA remoto quanto com o SHA-256 do manifesto. Não é divergência documental; a reconstrução e a vista de transporte são identificadas em LOG_ENCODING_RECONSTRUCTION.json. O revisor deve usar bytes do blob, não hashear texto recodificado. Não republico o log nem seus caminhos pessoais.

## 3. Testes fornecidos e reconciliação observada

Relatório do implementador: Windows 11 x64, Python 3.14.7, pytest 9.1.1, Pydantic 2.13.5, Gemmi 0.7.5/RDKit 2026.3.6. Resultados fornecidos: 75 passed no arquivo novo e 1551 passed/5 skipped na suíte completa. Isso não é pytest executado pelo arquiteto.

Conferência mecânica própria: 1.524 IDs antes e 1.556 depois, todos únicos; 32 itens adicionais e nenhum ID anterior removido. AST: 43 funções antigas preservadas, 75 funções atuais, 32 funções adicionais, nenhuma parametrização declarada; os 43 cenários normativos continuam sendo a mesma matriz, não 75 cenários novos. A aritmética 1524+32=1556=1551+5 confere com os logs publicados. Isso não prova suficiência das asserções ou fecha achados.

Os skips atuais estão nomeados no log: application.py:1809/1847 e cli.py:4250/4303 requerem instalação sem RDKit; atomic.py:1046 depende de privilégio de symlink neste Windows. Que sejam exatamente os mesmos cinco skips históricos é alegação do implementador: o log histórico não nomeava os cinco. Os testes antigos correspondentes não foram modificados, mas não invento uma execução retrospectiva.

## 4. Triagem própria das correções

Ambiente próprio: Linux/Python 3.12.14/Pydantic 2.13.4. Não instalei dependências; não executei pytest, Gemmi real, RAW, Windows ou concorrência. Dois subprocessos novos (-I -B, com e sem -O) bloquearam Gemmi/RDKit por sys.modules=None, **sem sentinela nativa**. O módulo novo importou e executou DTO/hash/planner/contexto puro. Os registros ProteinInput/policy são DTOs reais; inspection/resolution são namespaces documentais sintéticos para ensaiar a fronteira pura, não prova de parsing nem da validação 020. O script portátil e o output registram essa limitação.

Observado: filter+entry_id gerado é aceito em _cell/_symmetry; disposição remove de GLY só fora de M deixa ALA retido, enquanto remove de ALA presente continua recusado; hash legado puro confere com hash documental independente; código inválido é recusado com e sem -O. Essas observações apoiam correções pontuais, mas não constituem revisão independente de todos os quatro MAJORs/oito MINORs.

**Pontos para exame focal, sem novo alargamento de escopo:**

| Referência já existente | Observação arquitetural no snapshot recebido | Ação do revisor |
|---|---|---|
| MINOR-3, invariantes locais | CategoryDecision ainda aceita kept_row_ordinals=(0,0) e omitted_row_ordinals=(0,0). | Confirmar contra a exigência já despachada de unicidade/disjunção; classificar disposição individual, sem deduplicar silenciosamente. |
| MINOR-3, nome canônico/famílias | `_em_example` omit é aceito, mas `_em_example` seguido de LF também passa pelo startswith. | Examinar a guarda de categoria canônica e o limite da família aprovada. Não inventar um sanitizador genérico ou implementar DOM. |
| MAJOR-A, cruzamento de formatos | Contexto aceita acquisition.raw_artifact.format=pdb e inspection.raw_format_declared=pdb quando inspection/resolution.structure_format=mmcif. | Confrontar com §5 e o comportamento real do 020; distinguir aliases oficialmente aceitos de contradição PDB/mmCIF. Não escolher uma interpretação silenciosa nem tratar o ensaio sintético como depósito real. |
| MINOR-7/ARCH-01, prova de compatibilidade | O teste dedicado “golden_legacy...matches_the_020_production_helper” chama compute_inspection_id antigo e compara com INSPECTION_ID, também calculado pelo helper antigo no topo. Não chama o helper 021 novo. | Avaliar prova dedicada versus cobertura indireta de build_source_context, e os golden independentes restantes; não afirmar alteração do algoritmo, que conferiu na sonda própria. |
| MINOR-4/7, cobertura | Novo teste de request_key varia campos, mas o relatório declara T021-160 e toda prova de hash resolvidos. | Conferir especificamente plan_key/policy, golden dos envelopes exigidos e estímulos reais; não aceitar a autoavaliação por autoridade nem abrir os Literals do perfil. |

O parecer focal é o lugar para confirmar/classificar esses resíduos; não emito correção adicional ao implementador em paralelo nem declaro os achados fechados. P-1/P-2/P-3 e as decisões científicas aprovadas não são reabertas por preferência. A recusa/aceitação de seleções continua sendo objeto do CP1, não autorização de materialização científica.

## 5. Precisões de recibo, sem editar históricos

O relatório usa “13 entradas” e “ALL_11_REQUIRED_CHANGES”, mas existem doze mudanças funcionais (4 MAJOR+8 MINOR) e quinze registros no JSON de disposições incluindo três NOTES. Todos os IDs esperados estão presentes; são rótulos/contagens de apresentação, não achados ausentes por si. A mesma entrega diz ter lido “cinco evidências” do parecer; o snapshot do revisor tem nove, e este recibo não presume que todas foram lidas só pelo resumo. O revisor focal acessa o conjunto completo pinado.

O manifesto chama `code_commit_parent` de 08b797e, que é a baseline. O pai direto de 42b4804 é 3ba2fa9; a cadeia correta foi observada no Git e já consta no corpo do próprio relatório. A identidade dos arquivos não diverge. Não usar esse nome de campo como prova de parent único incorreto. O relatório classifica 40 provados/3 parciais por desenho/0 lacunas: isso é avaliação do implementador pendente de fechamento, não nova classificação independente.

## 6. Encaminhamento

Preparada `tasks/021-CHECKPOINT1-FOCAL-REVIEW.json`, para Claude revisor em sessão separada dos implementadores. Inputs incluem código 42b4804, entrega 010ee93, parecer original 2e36222, reconciliação 521500c e contrato congelado b0e60f6. Examinar o delta e a integração com os contratos já revisados; não repetir estudo nem exigir CP2. Registrar separadamente correções implementadas, achados fechados, resíduos e limites de execução.

Saída própria do revisor: `increments/021/23-checkpoint1-focal-review/CLAUDE_INCREMENT_021_CHECKPOINT1_FOCAL_REVIEW.md` e `evidence/claude-*`, em branch própria baseada na publicação desta tarefa. A tarefa fica pronta para encaminhamento manual; não alego acionamento automático. STATUS e tarefas centrais refletem recebimento, não aprovação. Nenhuma implementação nova está autorizada pelo recebimento.

CORRECTION DELIVERY IDENTITIES VERIFIED: YES
ARCHITECT RECEIPT COMPLETE: YES
READY FOR INDEPENDENT FOCAL REVIEW: YES
INDEPENDENT CORRECTION CLOSURE COMPLETE: NO
CHECKPOINT1 APPROVED: NO
CHECKPOINT2 IMPLEMENTATION AUTHORIZED: NO
FINAL SPECIFICATION FROZEN: YES
CODE REPOSITORY MODIFIED BY ARCHITECT: NO
AUTOMATED DISPATCH: NO
