# Recebimento focal das correções residuais — Incremento 021, CP2

Codex arquiteto; 25/11/2026, America/Sao_Paulo. Tarefa 021-CHECKPOINT2-COMPLETION. Este registro recebe a nova entrega e define a continuação concreta; não é parecer independente nem aprovação do checkpoint.

## 1. Identidade e procedência

- Coordenação de entrada: `1c7906d748a544b26b007faad4d08062008d7fcd`. Main do código: `08b797e0985e123ffd4d7ca7e5a5e8f040e63851`; main do governance: `a47183dfec8213c765ed43ae482c8c227760a3d5`, ambas consultadas e preservadas.
- Código: feature/increment-021-receptor-materialization @ `a8d46675e1d1bab83c9f7824225699afae57bd4a`, filho direto de 5be1e443200cedddac0f97707963500a2edc6da6.
- Relatório: claude/021-cp2-residual-correction-report-20261125 @ `2c50be1ec30fa49b85cc3d269b7af2fe365b5e8f`, filho direto da coordenação de entrada. Somente dois arquivos novos próprios: relatório residual e log de suíte completa. Relatos anteriores permanecem intactos.
- O texto enviado pelo responsável termina no meio de um teste; ele não é a entrega final. Localizei e li integralmente o relatório já publicado em 2c50be1, conferi o commit de código posterior e os bytes dos seis inputs relevantes contra suas árvores Git. A nova árvore do código difere de 5be1e44 somente nos quatro arquivos permitidos; fixtures/manifests não mudaram. O acumulado mantém os 22 caminhos previamente conferidos. Nenhuma escrita em código/main/contrato.

## 2. Verificações e melhorias observadas

Sondas próprias, fontes fixadas por SHA256, Python 3.12.14/Pydantic 2.13.4, processos normal e -O, importações Gemmi/RDKit bloqueadas por finder real, sem stub. Mesmos resultados nos dois modos. Não executei pytest, Gemmi nativo, Windows/NTFS ou concorrência e não instalei dependências. Não tenho acesso ao working tree Windows do responsável.

- Importação do domínio/adapter sem tentativa nativa; primeira entrada exige engine e retorna ENGINE_UNAVAILABLE quando bloqueado.
- R-CP2-01 avançou: assim inexistente agora recusa INVALID_CIF; caso válido gera contagens 1/1/1; transporte SpecialPositionSummary e aviso condicionado constam do código e dos testes novos.
- Os três contraexemplos originais de R-CP2-02 agora recusam: sequência anisotrópica divergente, elemento O contra C, e U parcial mesmo com B completo. Recebida a correção; o fechamento científico/nativo independente continua pertencendo ao revisor final, não a este recebimento.
- R-CP2-03 avançou: categoria extra agora recusa INVALID_OUTPUT com phase=verify. A comparação de tokens de lineage foi acrescentada ao teste existente; sua execução nativa é evidência fornecida.

## 3. Residuais que ainda precisam ser completados

### R-CP2-01 — MAJOR parcial: componente informado ignorado

O resolver novo compara cadeia e sequência, mas não lê label_comp_id/auth_comp_id da anotação. Com átomo fonte A/seq1/ALA, a função real compute_special_position_summary aceita anotação A/seq1/GLY e conta o átomo como afetado (1/1/1). Não é um caso de outro modelo/átomo removido com interseção zero: o componente explicitamente informado contradiz o átomo contado. O ramo por label_seq também ignora contexto auth/inserção contraditório quando informado. Isso permanece dentro da resolução inequívoca exigida por §11/T021-158 e da correção já pedida, sem novo motor ou preparação química.

Completar a resolução com os campos científicos suportados e informados de modo coerente; não exigir campo opcional ausente quando o contexto já é inequívoco. Recusar contradição/ambiguidade em vez de casar somente asym+seq ou unir ocorrências distintas sem prova. Preservar as novas contagens, sobreposições, avisos, casos removidos/outro modelo e controles válidos. Acrescentar negativo do componente contraditório e positivos em função de produção, incluindo prova nativa pertinente.

### R-CP2-03 — MAJOR parcial: _entry e bloco ainda não verificados

O verificador real aceita _entry.unplanned ao lado de um id correto. A checagem especial de _entry encerra esse ramo após conferir apenas contagem/id; não aplica a comparação de tags/células do restante. ParsedCifDom021 não transporta o nome do bloco, então nenhum confronto pós-reparse do block contra tbmp_<plan_key> ocorre. Ambos os requisitos já constavam expressamente da aceitação R-CP2-03 no recebimento anterior.

Aplicar fechamento exato dos campos de _entry e conferir nome do bloco e id gerado contra a identidade esperada após reparse nativo. Corrupção de block, id e tag extra deve recusar INVALID_OUTPUT/verify; preservar os negativos novos de categoria extra e token alterado. A forma interna de transporte é escolha de implementação; sem mudar schema público congelado nem antecipar persistência CP3.

### R-CP2-04 — MINOR documental: causa LF/CRLF confirmada

Todos os quatro tamanhos/hashes declarados no relatório correspondem exatamente aos arquivos locais reconstruídos em CRLF. Os blobs Git estão em LF. Confirmei os dois conjuntos de bytes mecanicamente; não é corrupção inexplicada nem falha científica. O texto do relatório os chama identidades de blob e também diz que os calculou no working tree, que são superfícies diferentes. Preservar o relatório histórico e publicar manifestação correta dos bytes Git finais.

| Arquivo em a8d4667 | Linhas LF | Bytes Git | SHA256 Git |
|---|---:|---:|---|
| `src/molecular/receptor_materialization.py` | 4547 | 217908 | `5f25769da6f0798d2c0d1c84e0b64016ce7e2c471fc454cd035b66703d8a4e8c` |
| `src/molecular/receptor_parsing.py` | 1759 | 72234 | `158950130610d71061e59c180da578ce52452836523074e7690077a060a7570c` |
| `tests/test_receptor_materialization.py` | 2970 | 157371 | `4d8e9812d56e0094ca49a9cfc411d3d851e3ff2c3ef2fdaa428ee3f9c295f6fb` |
| `tests/test_receptor_parsing.py` | 1486 | 63537 | `335aafdd88351d5b3fe5ca1e706e82984a625a07f52d1fc3bfb0e196378f20ee` |

Forneço evidence/GENERATE_GIT_BLOB_IDENTITIES.py, somente leitura, para gerar por subprocess git show o manifesto dos quatro arquivos e de toda a raiz de fixtures no commit final. Executar fora da árvore de código, com caminho do repositório e SHA completo final como argumentos; redirecionar stdout somente para o caminho próprio autorizado do governance. O helper verifica HEAD, restringe paths e confirma SHA1 do blob antes de calcular SHA256. Não usar Get-Content/text mode/bytes do checkout como se fossem bytes do commit. O helper foi inspecionado e compilado por AST aqui; não foi executado contra um checkout Git local completo nesta sessão.

## 4. Testes e evidências

O diff acrescenta quatro funções de teste, sem remoção de funções: duas no domínio e duas no adapter. A conta fornecida 1658→1662 coletados e 1653→1657 passed, com cinco skips, é coerente com +4. O foco 212 e a regressão 020 com 121 passed são fornecidos; não reexecutei pytest. O log final existe no novo commit; os cinco skips continuam discriminados. O log retorna texto pelo conector; a cópia temporária foi reconstruída em CP1252 apenas após reproduzir exatamente tamanho e SHA do blob remoto, como nos recebimentos anteriores.

R-CP2-02 não gera nova demanda de implementação neste recebimento. Não reabrir decisões por preferência. R-CP2-01/R-CP2-03 ainda parciais não podem ser chamados fechados apenas porque seus testes específicos anteriores passaram. Preservar a matriz de 79 cenários e publicar disposição/mapeamento final honesto, sem confundir função mapeada com prova integral. Os demais C-01–C-07, CP1 e regressões seguem os requisitos originais; esta triagem não é nova revisão integral.

## 5. Continuação autorizada e gate

Continua a mesma tarefa/autorização CP2: usar a8d4667 como input atual, sem retornar a 5be1e44 ou reiniciar o trabalho. Corrigir somente R-CP2-01 e R-CP2-03 remanescentes; completar R-CP2-04 documental com o helper fornecido e nova evidência real. Manter os quatro arquivos/raiz permitidos, publicar normalmente na feature existente e relatório próprio novo no glob35/evidence/claude-*. Não editar relatórios anteriores, descartar diffs reconhecidos, resetar, amendar, rebasear ou forçar refs.

Após correção/testes e entrega documental consistente, preparar a revisão independente final do CP2 em sessão separada. Não acionei nenhum agente. CP2 não aprovado, CP3/CP4 não autorizados, 020-A STAND-BY. A organização de estudos mais amplos começa somente no 022, sem afetar o contrato congelado do 021.

ARCHITECT FOCAL RECEIPT COMPLETE: YES
BLOCKERS: 0
REMAINING MAJORS: 2
REMAINING MINORS: 1
READY FOR INDEPENDENT FINAL CP2 REVIEW: NO
CHECKPOINT2 APPROVED: NO
CHECKPOINT3 IMPLEMENTATION AUTHORIZED: NO
FINAL SPECIFICATION FROZEN: YES
CODE REPOSITORY MODIFIED: NO
AUTOMATED DISPATCH: NO
