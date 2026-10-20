# Incremento 020-A — Candidata final e fechamento focal do draft1

20/10/2026. Este pacote preserva o rascunho e o parecer recebidos. Contém uma candidata nova, a resposta do arquiteto, diff integral e evidência adicional executada no RDKit2026.03.6. Não contém autorização de implementação.

## Ordem de leitura

1. `INCREMENT_020_A_DRAFT_REVIEW_RESPONSE.md`.
2. `changes/draft1-to-candidate1.diff` e as seções alteradas da candidata.
3. `evidence/draft-review-verification.json` e `evidence/verify_draft_review.py`.
4. Originais em `prior/`, conforme necessário. O contexto arquitetural anterior está no ZIP preservado em `context/`.

Conferir identidades em `FILE_IDENTITIES.json`. O manifesto não inclui hash de si mesmo. Nenhum hash de arquivo foi atribuído a conteúdo apenas alegado.

## Comando para o Claude revisor

```text
Atue como o revisor independente designado para fechar as correções do
draft1 do Incremento020-A. Leia o pacote anexado. Não implemente código,
não altere originais nem faça commit/push/PR ou configure automações.

Confronte a candidate1 e a resposta ao seu parecer anterior, com foco em:
1. MINOR-1: construtor, MolDrawOptions e DrawMolecule separados, inclusive DTO;
2. MINOR-2: defaults e desvios identificados nas tabelas científicas/gráficas;
3. MINOR-3: coordMap/bondLength explícitos e a ressalva de versão:
   usePathAngleExpansion aparece na documentação2026.09.1, mas a docstring
   e a chamada real do binding2026.03.6 no pacote mostram sua ausência/recusa.
   Examine essa evidência; não aceite a correção apenas por autoridade.
4. Disposição das seis NOTES e ausência de regressão concreta no contrato.

Não repetir A-01–A-14/C-01–C-03 nem os 80 cenários por preferência.
Não exigir os leitores Windows implementados antes de aprovar o texto.
Declare limites de acesso e de execução.

Entregue fechamento focal em Markdown: itens encerrados/pendentes,
BLOCKERS/MAJORS/MINORS/NOTES e READY FOR OWNER FREEZE DECISION: YES/NO.
Isso significa apenas prontidão para eu decidir o congelamento.
Mantenha READY FOR IMPLEMENTATION: NO, FINAL SPECIFICATION FROZEN: NO
e IMPLEMENTATION AUTHORIZED: NO.
```

## Comunicação futura pelo GitHub

O desenho da automação permanece separado. O repositório de governance foi encontrado público; nenhum material deste pacote foi enviado a ele. Antes de utilizá-lo como espaço privado compartilhado, confirmar sua visibilidade e o acesso de ambos os lados. Não enviar tokens por chat nem gravá-los no repositório.

Um comando curto do responsável deverá sempre se vincular à versão e ação pendentes identificadas. O fluxo automático só estará ativo quando configurado e testado; este pacote não cria tarefas, workflows ou gatilhos.
