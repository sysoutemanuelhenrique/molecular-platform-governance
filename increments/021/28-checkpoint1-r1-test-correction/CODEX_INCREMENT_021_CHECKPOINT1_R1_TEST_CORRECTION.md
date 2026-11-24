# Correção pontual R-1 — Incremento 021, Checkpoint 1

Data: 24/11/2026, America/Sao_Paulo. Codex arquiteto. Encaminhamento direto de uma regressão de teste; nenhuma mudança de arquitetura ou produção autorizada por este documento.

## 1. Parecer e estado verificados

Coordenação: docs/020-a-candidate1-review-20261020 @ fcad8561b53b924ad2d04844c460fabd8489f866. Código: feature/increment-021-receptor-materialization @ bbd491e1a0b3fcb913c3549b004120693212df62. Main código: 08b797e0985e123ffd4d7ca7e5a5e8f040e63851; main governance: a47183dfec8213c765ed43ae482c8c227760a3d5. HEADs remotos coincidiram.

[Parecer final focal](https://github.com/sysoutemanuelhenrique/molecular-platform-governance/blob/edb8764b4d4ee56e49ff849b65b950e5e430fae0/increments/021/27-checkpoint1-final-focal-review/CLAUDE_INCREMENT_021_CHECKPOINT1_FINAL_FOCAL_REVIEW.md): branch claude/021-cp1-final-focal-review-20261124, commit edb8764b4d4ee56e49ff849b65b950e5e430fae0, pai único fcad8561. Identidade:175 linhas/12.045 bytes/SHA-256 61b3f0b6773e100ede55211ededec585710caff515a672b995dd52a38d2244a7. Os14 arquivos adicionados pertencem somente ao caminho do parecer/evidências; nenhum histórico/STATUS/task editado na branch do revisor. Os13 itens do manifesto conferem em bytes/SHA-256 e blobs; o manifesto também confere com o blob. Um JSON tem100 LF e101 segmentos splitlines, sem LF final: é diferença de convenção de linhas, não de conteúdo/hash.

O revisor fechou MAJOR-A residual, MINOR-3 e MINOR-7; os nove fechamentos anteriores e as três NOTES permanecem preservados. Resta **R-1: um MINOR bloqueante para a aprovação**, somente teste. REQUEST CHANGES permanece, sem BLOCKER ou MAJOR aberto. Não reabrir os doze fechamentos funcionais por preferência ou refazer o estudo. CP1 não aprovado; CP2 não autorizado;020-A STAND-BY.

## 2. Disposição de R-1

**Aceito.** O teste de ordem passou de dois átomos fora de ordem para um único átomo, enquanto seu nome continuou alegando preservação da ordem. O revisor publicou que ordenar por ordinal fazia falhar o teste antigo e não é detectado pelos91 testes atuais. Isso é regressão concreta de prova, não defeito científico observado na função atual nem escolha estética.

Correção escolhida: **adicionar um único teste** no arquivo permitido, mantendo o teste de um átomo e todos os13 goldens atuais. Novo vetor, cuja ordem dada difere tanto da ordenação por ordinal quanto por id: `(ordinal=3, atom_id='a')`, depois `(ordinal=1, atom_id='Z')`. Não modificar compute_atom_ids_key nem outros trechos de produção.

Bytes canônicos escritos à mão, sem LF final:

```text
{"atoms":[{"id":"a","ordinal":3},{"id":"Z","ordinal":1}],"kind":"receptor-materialization-atom-ids","version":"1.0"}
```

SHA-256 literal: `96fd3eacd89d16753dbdc5ec22bb79db0740e9f355e6322cb0c4641bc0f3106a`.

Ordem reversa, também resultado das duas ordenações indevidas: SHA-256 `bf820fe14730b4b8ede9d8e007e4c3d32f71def5d8a4747c657d6d76dac562d1`.

O teste novo deve construir esses dois AtomObservation usando o helper existente, chamar a função real com o vetor **nessa ordem** e comparar ao primeiro literal. Pode conferir também que o vetor reverso produz o segundo literal. Incluir os bytes à mão e, opcionalmente, validar sua consistência com hashlib; o expected principal é o literal, nunca uma chamada de produção ou hash calculado dentro do teste. Não ordenar a entrada antes de chamar a função.

## 3. Evidência própria e limites

Calculei os dois digests apenas com hashlib sobre os bytes literais, antes de importar produção. Depois, em processo -I -B com Gemmi/RDKit bloqueados, sem stub, construí DTOs reais e chamei compute_atom_ids_key da cópia externa exata de bbd491e. A ordem original corresponde ao primeiro digest e os dois controles ordenados ao segundo: o vetor discrimina ambas as reordenações. O source SHA-256 permaneceu d8fc55db900f761f0debe4cea29f05cade1502ea1299937f123c6c883e30431d.

Não executei pytest, os mutantes sobre um futuro teste ainda inexistente, Gemmi nativo, Windows ou suíte completa. As execuções91 testes/mutantes são evidência do revisor;1567 passed/5 skipped Windows são evidência fornecida. O JSON em evidence separa tudo isso; os dados são documentais, não RAW científico. Não alterei código/testes.

## 4. Execução autorizada e entrega

Tarefa: tasks/021-CHECKPOINT1-R1-TEST-CORRECTION.json, dentro da autorização original de CP1 e reduzida a **tests/test_receptor_materialization.py somente**. Continuar a branch existente a partir de bbd491e por commit aditivo e push normal. A identidade de src/molecular/receptor_materialization.py deve permanecer exatamente a mesma. Não alterar contratos, helpers, dependências, fixtures externas ou testes existentes para esconder falha.

Executar o teste novo e o arquivo completo; comprovar, em cópia descartável externa, que ordenar por ordinal ou id faz o novo teste falhar. Nenhuma mutação entra no código commitado. Registrar coleta e resultados reais; previsão simples é91→92 funções e1572→1573 itens se adicionar apenas um teste, mas conferir em execução. Rodar a suíte completa uma vez no ambiente disponível aprovado, identificando skips; não inventar resultado se houver limitação.

Relatório próprio: increments/021/29-checkpoint1-r1-test-correction/CLAUDE_INCREMENT_021_CHECKPOINT1_R1_TEST_CORRECTION_REPORT.md e evidence/claude-*, em branch própria do governance baseada na publicação desta tarefa. Depois, a reverificação independente se limita a R-1 e ao delta somente teste, com produção byte-idêntica; não será nova revisão integral dos doze fechamentos. Nenhum agente foi acionado automaticamente.

R1 CORRECTION TASK PREPARED: YES
PRIOR TWELVE FUNCTIONAL CLOSURES PRESERVED: YES
OPEN BLOCKERS: 0
OPEN MAJORS: 0
OPEN MINORS: 1
CHECKPOINT1 APPROVED: NO
CHECKPOINT2 IMPLEMENTATION AUTHORIZED: NO
FINAL SPECIFICATION FROZEN: YES
CODE REPOSITORY MODIFIED BY ARCHITECT: NO
AUTOMATED DISPATCH: NO
