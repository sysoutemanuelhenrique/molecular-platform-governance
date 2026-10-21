# Recepção e encaminhamento — Checkpoint 1 do Incremento 020-A

Codex, arquiteto; 20/10/2026, data local do responsável. Triagem de entrega, não parecer independente de aprovação. Fonte principal: relatório publicado pelo implementador; o transcript anexado foi lido como contexto, sem ser publicado no governance.

## Snapshot conferido diretamente no GitHub

- Código: sysoutemanuelhenrique/molecular-platform; branch feature/increment-020-a-molecular-characterization em f8416b845efe93f9e47deca97f01a355e4e679ba.
- Parent único do commit: 08b797e0985e123ffd4d7ca7e5a5e8f040e63851, igual à baseline e à main remota observada.
- Diff: um commit, exatamente os quatro arquivos autorizados; 3.094 inserções e uma exclusão. A exclusão amplia o import existente de rdMolDescriptors para Descriptors/rdMolDescriptors. Em testes legados, o diff acrescenta imports e testes; não exclui linhas.
- Governance: main a47183dfec8213c765ed43ae482c8c227760a3d5; branch do arquiteto docs/020-a-candidate1-review-20261020 em 85ce45ce5cc635d75035664dd612ca6c0a839dac antes desta atualização; branch do revisor preservada em 7f1f75219203eb1a691e454db170900ca81536e8.
- Relatório: branch claude/020-a-checkpoint1-report-20261020, commit 0dac01f2f51efe1ed1600eafac88eb8f750d41b1, caminho increments/020-A/09-checkpoint-1/CLAUDE_CHECKPOINT1_IMPLEMENTATION_REPORT.md. Lido integralmente: 343 linhas, 26.859 bytes; SHA-256 76f7403c22e2f0462841de43f53f752791d670ad9e290d56fda755bb23e4dc82.

Contrato congelado: increments/020-A/08-final-specification/INCREMENT_020_A_FINAL_SPECIFICATION.md no commit 665fb8b9cb4e1c7e0d0b9f1db98ec2adaa63bfed; SHA-256 cfbc6ea4bbb58f987deb3f73e45fc39d5b79d0cfaa2de8e0a7870a9937386e9c; 586 linhas; 71.904 bytes. Permanece inalterado.

## Identidades do código lido

| Caminho | Linhas | Bytes | SHA-256 |
|---|---:|---:|---|
| src/molecular/characterization.py | 1054 | 39713 | 83a9d0e2d32b73f37188d1596816d2e727716c8eb47f038924d221af88bb32a9 |
| src/molecular/rdkit_tautomer.py | 1304 | 53277 | 5c6bf758c9e451f71815c3af3f0e917b9cc22c4434b93e5e8d0cfe165e1612ed |
| tests/test_characterization.py | 718 | 23916 | 4d6a8a66787f766fe841e240d0088b0e656ecbcaf8260fdbdb614f98a9962685 |
| tests/test_rdkit_tautomer.py | 1599 | 59937 | fdcaf50cf1b3aca0e24c8f05ab94dc1f5b58d0768248f44b77f04602ec067b8e |

A triagem leu o relatório inteiro, o diff e trechos pertinentes de DTOs, adaptação/desenho e testes; não constitui revisão exaustiva dos quatro arquivos. O revisor deverá ler o código completo pertinente no snapshot fixado.

## Evidência fornecida versus observada

Fornecido pelo implementador, não reexecutado pelo arquiteto:

- Windows 11/build 26200, Python 3.11.9, RDKit runtime 2026.03.6, Pydantic 2.14.1.
- tests/test_characterization.py: 111 passed.
- tests/test_rdkit_tautomer.py: 142 passed, dos quais 62 anteriores e 80 novos.
- Suíte completa: 1667 passed, 5 skipped; baseline 1476 passed, 5 skipped. Aritmética: 111 + 80 = 191 adicionais. Não confundir com número de funções nem afirmar coleta independente.
- git diff --check limpo e preservação dos checkouts/untracked locais, segundo o relatório. O arquiteto não tem acesso à máquina Windows para confirmar esses estados locais.

Observado pelo arquiteto: refs/parent/diff, leitura e identidade dos arquivos públicos, análise estática dos trechos abaixo e uma sonda de DTO sobre o código exato publicado, sem alteração de fonte. Pytest não está instalado neste ambiente; não foi executado nem foram instaladas dependências para esta triagem. A sonda usou Python 3.12.14/Pydantic 2.14.0, diferente do ambiente informado pelo implementador. Resultado em evidence/architect-dto-strictness-probe.json.

## Pontos concretos para a revisão, sem adjudicação independente antecipada

1. **Validação estrita dos DTOs.** Seção 11, especialmente a abertura e a regra de tipos estritos. CharacterizationValues, linhas 209–253, usa frozen/extra=forbid e recusa bool, mas aceita coerção: heavy_atom_count="3" e 3.0 tornam-se int 3; formal_charge_e="0" torna-se int; molar_mass_g_mol="46.069" torna-se float. SdfParserParameters(sanitize=1) aceita e converte para bool True. Reproduzido isoladamente. Confrontar todos os blocos/constantes com o contrato e classificar a causa; não tratar frozen/extra=forbid como validação estrita suficiente. Revisor deve reproduzir independentemente.
2. **Interrupções exigidas neste checkpoint.** O próprio relatório, seção 6.4 item 3, declara ausência de testes dedicados de KeyboardInterrupt/SystemExit no adaptador. A solicitação aprovada de CP1, item “Verificação exigida ao implementador”, os exigia separadamente; T-020A-076/077 também os cobre. Ter except Exception preserva normalmente essas interrupções, mas não prova restauração de recursos/logs por fase nem dispensa o teste contratado. Não postergar automaticamente o adaptador para CP2, cujo escopo são leitores/serviço.
3. **Restauração de logs.** tests/test_rdkit_tautomer.py, linhas 1572–1585, testa supressão no parse inválido e em seguida calcula etanol com sucesso. Não emite LogWarningMsg depois nem verifica um marcador em stderr. Isso não comprova restauração. T-020A-078 exige emissão após sucesso, exceção e interrupção com capfd/subprocesso. Os testes legados que emitem marcadores exercitam enumeração/promoção, não este novo fluxo. Avaliar cobertura real, sem afirmar que a ausência do teste demonstra um bug já reproduzido no logger.
4. **Comando SVG Z.** O implementador relata recusa de cunha preenchida na molécula C[C@@H](C(=O)O)Nc1ccc(Cl)cc1. A seção 10.1 fecha a gramática em M/L/Q e manda recusar e relatar outros comandos. O arquiteto não autoriza incluir Z nem ampliar o perfil. O revisor deve separar limitação declarada do contrato, implementação da recusa e eventual regressão concreta. Reproduzir causa real e all-or-nothing; não exigir mudança contratual só para aumentar cobertura gráfica. O exemplo do professor ainda não foi ensaiado com a CLI nova, que não existe neste checkpoint.
5. **Suficiência das demais evidências.** Conferir DTOs/JSON, parsing real, invariantes científicas, opcionais, taxonomia de erros e testes discriminantes; unidade com Mol real não é o mesmo que bytes SDF/SMILES reais. Verificar os casos de SGroup/estéreo declarados como limitação, teto de ligações, fonte/desenho indisponíveis, coerência de vínculo/hash e ausência de resultado parcial, nos limites de CP1. Julgar a alocação do helper SVG pela responsabilidade contratada na seção 4, sem transformar preferência de organização em achado.
6. **Precisão do relatório.** A API GitHub conta 679 adições no adaptador; a tabela declara +680, enquanto o total de 3.094 está correto. A seção 5.3 informa resultado do ambiente sem RDKit sem listar failed, mas a seção 6.4 menciona duas falhas anteriores. Pedir clareza se pertinente, preservando a distinção entre lacuna documental e regressão nova. Não corrigir os testes CLI preexistentes fora da allowlist para limpar um ambiente opcional.

## Próximo gate

Tarefa: tasks/020-A-CHECKPOINT1-REVIEW.json. Destinatário: Claude revisor em sessão separada da implementação. Código read-only; apenas parecer/evidência próprios no governance. Não refazer a revisão documental nem exigir leitores Windows de CP2 agora. Não reabrir decisões aprovadas sem violação contratual ou regressão concreta.

O Checkpoint 1 está recebido e encaminhado, **não aprovado**. Checkpoints 2/3 continuam não autorizados. O relatório favorável do implementador e sua contagem de testes não equivalem a fechamento independente. Nenhum código ou documento congelado foi alterado pelo arquiteto.

IMPLEMENTATION RECEIVED: YES
REMOTE CODE SNAPSHOT VERIFIED: YES
INDEPENDENT PYTEST RUN BY ARCHITECT: NO
INDEPENDENT REVIEW COMPLETE: NO
CHECKPOINT 1 APPROVED: NO
CHECKPOINT 2 AUTHORIZED: NO
CHECKPOINT 3 AUTHORIZED: NO
CODE REPOSITORY MODIFIED BY ARCHITECT: NO
