# Triagem do arquiteto — Incremento 021, Checkpoint 1

Data: 24/11/2026, America/Sao_Paulo. Autor: Codex arquiteto. Natureza: recebimento, confronto de evidências e triagem técnica; não é aprovação do checkpoint nem substitui a revisão independente.

## 1. Snapshot e escopo observados

Código: feature/increment-021-receptor-materialization @ 711f3070765efe67a5799f939f1a18306ed8afdd, pai único 08b797e0985e123ffd4d7ca7e5a5e8f040e63851. Main remota permanece nessa baseline. O diff remoto tem exatamente dois arquivos novos: src/molecular/receptor_materialization.py (1.418 linhas) e tests/test_receptor_materialization.py (791 linhas), 2.209 inserções/0 remoções. Os 68 blobs do snapshot completo foram comparados por Git hash ao conteúdo da cópia externa usada na triagem; nenhum código remoto foi modificado pelo arquiteto.

Governance de coordenação: docs/020-a-candidate1-review-20261020 @ 3cda329b0e19a972d9858e26b58052873655ac07. Entrega do implementador: claude/021-cp1-implementation-report-20261124 @ 51752b4ce7603d1f14677b0b030edc176b9df13f. Cadeia: 363478df… → f7253077… → 51752b4c…, baseada na coordenação autorizada. Só oito arquivos próprios da entrega foram adicionados; nenhum STATUS/task/contrato existente foi editado na branch do implementador. Main do governance permanece a47183dfec8213c765ed43ae482c8c227760a3d5.

Contrato: especificação final e quatro anexos do commit b0e60f6528f6fcb828aa6dd5577824e08c7c9fac, SHA-256 principal 5de705d609eaf158b0b29a99a0d02e24be4ed0b19d8e127c7e8d70c93aca1bd8. Autorização de CP1 preservada; CP2 não autorizado e 020-A em STAND-BY.

## 2. Identidades e contagem

Relatório final recebido: increments/021/17-checkpoint1-implementation/CLAUDE_INCREMENT_021_CHECKPOINT1_IMPLEMENTATION_REPORT.md, 160 linhas, 15.963 bytes, SHA-256 135a44606d76515e25b2bde042bb41e87f4698ce61b9780040c5dd8262fff934. As sete entradas do manifesto do implementador conferem em linhas/bytes/SHA-256 com os arquivos do snapshot recebido. As identidades dos dois arquivos de código também conferem com o manifesto.

A correção pública CRLF/LF do relatório foi conferida: o hash final do teste é ae8af3f9f6120a258ad7bd569d32a707337d3e6e69cc87f566760bbfd2bf86fb, 38.057 bytes. Não trato a errata histórica já corrigida como defeito atual.

Conferência mecânica: 1.481 IDs de coleta no log da baseline; 43 funções novas de teste; nenhuma parametrização declarada nessas funções; matriz de 43 IDs únicos correspondente à tarefa e aos nomes reais dos testes; 1.481+43=1.524. O log fornecido registra 1.519 passed/5 skipped, e o log direcionado registra os 43 novos testes. Isso reconcilia a aritmética, não prova a suficiência das asserções nem representa pytest executado por mim.

## 3. Execução própria e limitações

Ambiente próprio: Linux, Python 3.12.14, Pydantic 2.13.4. O Python disponível para esta triagem não possui pytest nem Gemmi. Não instalei pacotes. Li os dois arquivos do diff, compilei sua AST, verifiquei hashes e git diff --no-index --check dos novos arquivos na cópia externa, sem problemas de whitespace.

A importação limpa, em processo novo, sem stub e sem alterar fonte, falhou com ModuleNotFoundError: No module named 'gemmi'. Para isolar mais duas regras de domínio, executei quatro casos condicionais sobre os mesmos arquivos intactos com um módulo sentinela de importação Gemmi: nenhum atributo nativo pode ser acessado, qualquer acesso falha. Isso não prova importação sem Gemmi, parsing, execução química nem integração nativa. O script, o JSON e a verificação separados permitem reproduzir com Gemmi real instalado, sem a opção sentinela.

Não executei pytest, suíte completa, Gemmi real, parsing RAW, materialização, Windows ou concorrência. Os resultados Windows/Python 3.14.7/Pydantic 2.13.5 permanecem evidência do implementador, não execução minha. Não observei a working tree Windows nem os itens locais protegidos.

## 4. Pontos contratuais encontrados — confirmar independentemente

São candidatos a achados significativos, não encerramento independente nem ordem de correção já executada. O revisor deve reproduzir e classificar por seu próprio confronto com o contrato.

### ARCH-01 — o domínio puro importa Gemmi transitivamente

Cadeia real: receptor_materialization.py:53 importa receptor_inspection; receptor_inspection.py:28 importa receptor_parsing; receptor_parsing.py:33 executa import gemmi. A importação limpa do módulo novo falhou antes de qualquer chamada de domínio. O teste T021-040 só procura imports diretos/nomes de open/Path no texto e atributos do módulo, portanto não detecta essa dependência transitiva.

Referências: contrato §3, §19/CP1, T021-040 e brief de domínio sem Gemmi. Não se trata de exigir mudança científica no 020: o problema é a fronteira do módulo novo. Minha instrução preparatória de reutilizar compute_inspection_id não identificou esse acoplamento do helper antigo; isso é uma limitação da preparação arquitetural que precisa de reconciliação. O contrato congelado de domínio puro tem precedência. Não usar minha preferência de reutilização para justificar o import transitivo, alterar o contrato ou ampliar a allowlist. A revisão deve apontar a solução admissível dentro dos dois arquivos, preservando compatibilidade exata com o payload/hash antigo; nenhuma correção está autorizada ao revisor nesta tarefa.

### ARCH-02 — disposição de CCD ausente em M afeta cadeia polimérica em M

build_materialization_plan constrói disposition_remove_asyms/disposition_keep_asyms sobre todas as chaves antes de filtrar atoms_in_model e verifica o polímero só por asym. Reprodução condicional: M=1 tem A/ALA; M=2 tem A/GLY; S seleciona A; D remove A/GLY. Esperado pelo §7: a chave A/GLY está ausente de M=1 e não deve afetá-lo. Observado: SELECTION_CONFLICT e recusa da cadeia selecionada A/ALA. Controle sem disposição retém ALA de M=1 e exclui GLY de M=2; controle remove A/ALA recusa corretamente.

O teste nominal T021-019 não fornece nenhuma disposição: testa apenas model-filter, portanto não prova esse caso. O revisor deve verificar também D=keep sobre polímero fora de S e chaves que só existem fora de M, sem confundir retenção por cadeia e disposição por (asym,CCD).

### ARCH-03 — CategoryDecision proíbe geração de tag em action=filter

O validator de CategoryDecision rejeita generated_tags não vazio em action=filter. Porém o catálogo congelado define _cell e _symmetry como filter, com generate_tags=['entry_id']; o §11 determina entry_id derivado. Reprodução condicional nos dois casos: generated_tags=('entry_id',) produz ValidationError “filter must not generate tags”; controles sem generated_tags são aceitos.

A aplicação física do catálogo é CP2, mas o DTO/restrição já foi implementado no CP1 e não representa um caso exigido pelo contrato. Não se trata de pedir o serializer antecipadamente nem de preferência de implementação. T021-161 cobre omit e guard_then_omit, mas não essa combinação filter+generate. O revisor deve confrontar SCHEMAS/CategoryDecision e o catálogo real, além de verificar outras invariantes de linhas/tags antes de concluir.

## 5. Outros focos da revisão

Rever cobertura real dos 43 cenários, strictness em todos os campos/coleções novos, vínculos sources/resolution/model, identidade/equivalência de policy existente, ordenação determinística e limites da prova CP1. Avaliar a decisão de connection_decisions_key sempre vazio como recorte explicitamente declarado, sem exigir CP2 antecipadamente nem aceitar que o plano parcial seja apresentado como materialização concluída. Classificar a escolha de códigos de erro por violação contratual demonstrável, não por preferência de nome.

Não reabrir decisões fechadas do estudo/candidatos por preferência. Não refazer estudo, não mexer em contrato congelado nem solicitar CP2 para contornar falha de CP1. Novos problemas encontrados devem receber evidência precisa e escopo de correção, não implementação pelo revisor.

## 6. Próximo gate

Tarefa preparada: 021-CHECKPOINT1-ADVERSARIAL-REVIEW, em sessão Claude revisor independente e separada do implementador. Os inputs são os commits exatos de código/relatório/especificação e esta triagem. O arquiteto não afirma que o agente foi acionado nem que o checkpoint foi aprovado. Após o parecer, haverá reconciliação; CP2 permanece não autorizado.

IMPLEMENTATION RECEIPT VERIFIED: YES
ARCHITECT TRIAGE COMPLETE: YES
INDEPENDENT CHECKPOINT1 REVIEW COMPLETE: NO
CHECKPOINT1 APPROVED: NO
CHECKPOINT2 IMPLEMENTATION AUTHORIZED: NO
FINAL SPECIFICATION FROZEN: YES
CODE REPOSITORY MODIFIED BY ARCHITECT: NO
