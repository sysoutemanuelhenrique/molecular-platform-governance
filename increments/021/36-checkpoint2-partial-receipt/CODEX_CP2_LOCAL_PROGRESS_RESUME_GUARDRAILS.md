# CP2 — orientação de retomada após progresso local informado

Autor: Codex arquiteto. Data do registro: 24/11/2026, America/Sao_Paulo. Origem: relato de progresso fornecido pelo responsável, interrompido por limite da sessão implementadora. Este é um adendo operacional à tarefa de conclusão já autorizada; não revisão independente ou nova aprovação.

## 1. Snapshot observado e limite da evidência

Na consulta remota, coordenação continua em 7cd8ab3c5c2ec53e4630a41a6e7362e30fbe5edd; feature de código em 0d06ebd4c46c90e5446fec6f0eb72b4a8d2855db; relatório parcial em 9aa07628f2db61e68fc57b47d6e0e8e3dbeac80c. Main código permanece 08b797e0985e123ffd4d7ca7e5a5e8f040e63851 e main governance a47183dfec8213c765ed43ae482c8c227760a3d5. Não observei novo commit remoto da continuação.

O relato mostra edições e execução local em andamento, inclusive aquisição/recorte de fixtures. Não tenho acesso ao checkout Windows, seus diffs atuais ou bytes dessas fixtures. Portanto não declaro trabalho intacto, correções fechadas, novas contagens aprovadas ou cobertura dos79 concluída. O estado informado é progresso local não entregue; todas as provas finais da tarefa continuam exigidas. Nenhum código, documento normativo ou relatório histórico foi alterado pelo arquiteto.

## 2. Retomada preservando o trabalho

Retomar a mesma sessão implementadora e inspecionar somente leitura o estado local antes de novas edições: diretório/origin/branch/HEAD/index/diff e untracked. Não reiniciar do zero nem descartar diffs autorizados. Se HEAD ainda for0d06ebd e houver alterações locais reconhecidas como esta continuação CP2, preservá-las e continuar na mesma feature; esse dirty state esperado não é motivo para reset/stash/clean ou duplicação da implementação. Se houver commit novo, outra tarefa, alteração não reconhecida ou deriva remota, registrar o snapshot e interromper para reconciliação.

A coordenação avançará apenas por este adendo: usar o novo SHA de despacho fornecido pelo arquiteto, em vez de tratar o avanço documental conhecido como alteração do código. Continuam válidos o contrato congelado, a autorização humana original, a mesma allowlist, os79 cenários e os caminhos de saída35/evidence/claude-* já definidos. A mudança da ref de coordenação não autoriza main/PR/merge/CP3 ou outra branch de código.

## 3. Pontos contratuais que não podem ser dispensados

### 3.1 parent_comp_id preservado exige fechamento CCD

O relato acrescenta uma exceção incondicional em `_validate_simple_references` para `_pdbx_struct_mod_residue.parent_comp_id`, justificando que o pai pode não ter linha em chem_comp num depósito real. O contrato §11, regra REFERENCED_CCD_CLOSURE, exige a união dos CCDs de átomos/seq/branch e **parent_comp_id preservados**, com linhas chem_comp correspondentes, sem nova busca CCD.

Essa exigência é um limite do perfil021, não afirmação de que todo depósito real deva conter todos os pais. **Não aceitar silenciosamente uma referência preservada sem a linha exigida.** Substituir a exceção irrestrita pela validação do fechamento relevante ao que será preservado: se o parent_comp_id entrar no fechamento e faltar sua linha, recusar conforme a taxonomia vigente; não baixar/inventar CCD, apagar a anotação sem política ou reinterpretar o requisito como meramente descritivo. Referências que não sobrevivem/não entram no fechamento não devem ser confundidas com pais preservados.

Testar pai preservado com linha presente, pai preservado ausente e anotação não preservada, com produção e expectativas explícitas. Um arquivo real fora do perfil pode e deve ter recusa esperada. Modificar o contrato para aceitar esse caso exige outro processo e não está autorizado nesta tarefa.

### 3.2 Teto RAW021 é16MiB, separado do legado020

O trecho de preflight usa `MAX_RAW_ARTIFACT_SIZE_BYTES`, que no código parcial publicado é o teto1GiB do leitor020. Não há prova neste relato de sua adequação ao021. A especificação §4 fixa **16MiB inclusivos para os bytes capturados021**. Usar limite próprio021 e testar fronteira/excesso antes de Gemmi; não reaproveitar1GiB nem mudar o teto legado, o que alteraria comportamento020. Extensão/path seguro e captura Windows permanecem CP3; não inventar caminho no SourceContext para esse teste de bytes.

### 3.3 Import Gemmi tardio e ausência do engine

A docstring local passou a reconhecer explicitamente que o import continua global e a alegar que ARCH-01 o permite no adapter. ARCH-01 prova apenas import puro do domínio; **não substitui §3**, que exige import tardio e erro de configuração para engine ausente/versão divergente. Não fechar C-04 apenas com docstring ou checagem de versão após import global já bem-sucedido. Cumprir essa fronteira no arquivo permitido, preservar os resultados/API do parser020 e provar os casos ausente/versão errada sem falso engine de sucesso. Não editar CLI ou ampliar escopo para solucionar o caso.

### 3.4 Visão decodificada não é apenas colapso de nulos

Preservar raw_columns é necessário, mas o trecho ainda chama `raw_cif_null_to_optional_str` na visão usada em lookup. Nessa versão, isso não prova decodificação Gemmi de strings citadas. Identificar null real pelo token bruto; para os demais tokens, usar a decodificação do Gemmi na fronteira, mantendo '?' e '.' citados como strings literais, nunca None. Testar identificadores/expressões de operador citados e multiline, além de ?/. reais. O domínio não deve interpretar quoting como parte da identidade nem importar Gemmi. Os hashes/escrita continuam usando tokens brutos.

### 3.5 Fixtures recortadas e detector de frames

O relato diz que seis arquivos foram trimmed e que estão sendo exercitados. Isso não é prova recebida dos bytes ou do lineage. Preservar originais, origem/data/hash, lista exata de mudanças e os resultados da versão original quando suportada. Não retirar categorias/conexões/anotações apenas para apresentar um depósito incompatível como aceito intacto. Recortes/edições de isolamento permitidos no §23 devem ser identificados como derivados e ter oráculos próprios; as recusas esperadas do perfil, inclusive1pfe, permanecem.

O scanner por linhas/alternância de ponto-e-vírgula mostrado no relato não fecha por si C-06. Provar com Gemmi real frames efetivos, texto multiline, strings citadas e whitespace pertinentes, sem escrever outro parser CIF. Os demais critérios C-01–C-07, inclusive verificações independentes da saída e phase=verify, auditoria/contagens, anisotrop, referências compostas, testes/identidades e79 cenários, continuam vigentes; este adendo não afirma que foram atendidos.

## 4. Encaminhamento

Continuar dentro da autorização original, corrigindo os pontos acima e o restante da tarefa. Usar commits aditivos normais na allowlist, identificando explicitamente qualquer checkpoint parcial; não alegar conclusão antes das provas. Preservar o relato/commit parcial e todos os itens locais protegidos. Publicar novo relatório/evidências nos caminhos da tarefa, sem editar STATUS/tarefas centrais. Não apresentar redução do contrato como substituto das provas faltantes.

LOCAL PROGRESS REPORTED: YES
LOCAL DIFF INDEPENDENTLY OBSERVED: NO
NEW CODE DELIVERY VERIFIED: NO
CP2 CONTINUATION AUTHORIZED WITHIN ORIGINAL SCOPE: YES
READY FOR INDEPENDENT FINAL CP2 REVIEW: NO
CHECKPOINT2 APPROVED: NO
CHECKPOINT3 IMPLEMENTATION AUTHORIZED: NO
FINAL SPECIFICATION FROZEN: YES
CODE REPOSITORY MODIFIED BY ARCHITECT: NO
AUTOMATED DISPATCH: NO
