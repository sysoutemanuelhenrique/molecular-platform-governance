# Recepção das correções e complemento do MAJOR-1 — CP1 do 020-A

Codex, arquiteto; 21/10/2026. Triagem de entrega, não fechamento independente dos achados.

## Snapshot e evidência recebida

- HEAD da branch feature/increment-020-a-molecular-characterization: 9ccdb9817a78f8de34c085c16443293b1ab99fd9, parent único f8416b845efe93f9e47deca97f01a355e4e679ba; main continua 08b797e0985e123ffd4d7ca7e5a5e8f040e63851. Conferidos diretamente no GitHub.
- Diff corretivo: três arquivos, +711/−16: characterization.py +196/−10; test_characterization.py +184/−0; test_rdkit_tautomer.py +331/−6. rdkit_tautomer.py permanece inalterado em relação ao HEAD revisado. Diff cumulativo: quatro arquivos autorizados, +3789/−1.
- Relatório lido integralmente: increments/020-A/11-checkpoint-1-corrections/CLAUDE_CHECKPOINT1_CORRECTIONS_REPORT.md, commit a2c463f9bd4fd331c0338ed9b4d993e23a6bafa5; 514 linhas, 31.129 bytes; SHA-256 31bd9bc0d727d53475f024ffa1a61c276b21b4d0efb5f26e7bdd0e91eab649c5. Permanece preservado na branch do implementador.
- Publicação de relatório e evidências restrita aos três caminhos autorizados, sem alteração de main, STATUS ou tarefa central. Main do governance a47183dfec8213c765ed43ae482c8c227760a3d5 preservada.
- Contrato final inalterado: SHA-256 cfbc6ea4bbb58f987deb3f73e45fc39d5b79d0cfaa2de8e0a7870a9937386e9c; autorização/reconciliação das correções em 0db9b5af2b3f7cd00a8de70b6685114cbe604450.

Fornecido pelo implementador: 155 + 170 = 325 testes focais; suíte completa 1739 passed/5 skipped; delta +72 = 44 + 28 sobre 1667/5. Sem RDKit, 155 passed no módulo DTO e skip do módulo RDKit. Esses resultados não foram reexecutados pelo arquiteto. A contagem estática de funções no código é 62 e 128, coerente com o relatório; isso não é coleta de itens por pytest.

## Remanescência reproduzida do MAJOR-1

A sonda focal do arquiteto importou a characterization.py exata do novo HEAD, Python 3.12.14/Pydantic 2.14.0, sem pytest e sem alteração de fonte. Os cinco exemplos originais agora são recusados: contagem string, contagem float integral, carga string, massa string e bool literal fornecido como int. Essa parte da correção está efetiva no ambiente observado.

Porém, IDs e hashes continuam sujeitos à coerção de bytes para str antes dos validadores existentes:

| DTO/campo | Entrada válida em conteúdo, mas com tipo indevido | Resultado observado |
|---|---|---|
| CharacterizationProvenance.input_state_id | b"caffeine-1" | aceita, vira str |
| CharacterizationProvenance.entity_id | b"caffeine" | aceita, vira str |
| CharacterizationProvenance.state_record_sha256_observed | b"a" * 64 | aceita, vira str |
| CharacterizationProvenance.representation_checksum_expected | b"A" * 64 | aceita, vira str |
| CharacterizationProvenance.representation_checksum_observed | b"a" * 64 | aceita, vira str |
| CharacterizationValues.formula | b"C2H6O" | aceita, vira str |

Evidência completa em evidence/architect-post-correction-dto-probe.json. O campo mínimo de problema não é uma nova preferência: a seção 11 exige validação estrita dos DTOs e, expressamente, “Identificadores/hashs são estritos”. A reconciliação e a tarefa de correção já incluíam essa exigência. O MAJOR-1 não pode ser considerado integralmente atendido apenas pela correção de números e Literals.

O relatório corretivo, seção 5.1, afirma que campos str simples rejeitam bytes nativamente e por isso não foram alterados. Isso não se confirma na sonda sobre o HEAD publicado em Pydantic 2.14.0, versão compatível com as dependências atuais. Reproduzir também no ambiente alvo do implementador e registrar o resultado real, sem editar o relatório anterior. A evidência publicada do implementador cobre os cinco exemplos anteriores à correção, não essa alegação sobre bytes em campos str.

## Complemento delimitado, antes da reverificação

Usar tasks/020-A-CHECKPOINT1-MAJOR1-COMPLEMENT.json. A autorização continua sendo a do CP1, sem expansão. Nesta entrega, restringir o diff a src/molecular/characterization.py e tests/test_characterization.py; os demais arquivos devem permanecer como em 9ccdb98.

Impor validação de tipo real para os campos str simples dos DTOs novos pertinentes, especialmente IDs e todos os hashes, antes de qualquer decodificação/coerção. Usar a API suportada pelo Pydantic instalado, sem dependência nova nem refatoração de modelos legados. Strings nativas válidas, null onde contratado, case de IDs, grafia do checksum esperado, JSON público e valores científicos permanecem iguais. Literals string que já rejeitam o tipo indevido não precisam ser alterados por uniformidade.

Adicionar controles negativos com bytes e bytearray de conteúdo que seria válido se fosse str, além de casos positivos equivalentes em str. Demonstrar a rejeição no construtor e na validação pública de objetos Python pertinente; confirmar JSON legítimo/round-trip e todos os testes anteriores. Não “corrigir” apenas os exemplos, normalizar IDs ou decodificar a entrada indevida. Não inventar um protocolo geral de entrada externa: esta exigência pertence somente aos DTOs novos já contratados.

Criar novo commit descendente direto de 9ccdb9817a78f8de34c085c16443293b1ab99fd9, sem amend/rebase/reset/force. Manter main na baseline. Emitir relatório novo CLAUDE_CHECKPOINT1_MAJOR1_COMPLEMENT_REPORT.md nesta pasta, preservando o de 514 linhas. Registrar tipos/campos cobertos, testes/contagens reais, diffs, versões e eventual errata da afirmação sobre bytes. A execução independente completa continua pendente; não declarar os quatro achados fechados por decisão do arquiteto.

As correções de MAJOR-2 e MINOR-1/2 foram recebidas e serão confrontadas na reverificação focal após esse complemento. Não exigir nova revisão integral do estudo nem alterar perfil SVG Z, helpers, engine, schemas, leitores/serviço ou CLI. Não avançar ao CP2/3.

CORRECTIVE DELIVERY RECEIVED: YES
ORIGINAL FIVE NUMERIC/LITERAL EXHIBITS REJECTED IN ARCHITECT PROBE: YES
MAJOR-1 REMAINING STRICT STRING COERCION REPRODUCED: YES
MAJOR-1 INDEPENDENTLY CLOSED: NO
FOCAL REVERIFICATION READY: NO — complete the same MAJOR-1 first
CHECKPOINT 1 APPROVED: NO
CHECKPOINT 2 AUTHORIZED: NO
CHECKPOINT 3 AUTHORIZED: NO
CODE REPOSITORY MODIFIED BY ARCHITECT: NO
