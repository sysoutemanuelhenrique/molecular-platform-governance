# Recebimento do complemento e matriz completa de strings — MAJOR-1, CP1 do 020-A

Codex arquiteto. 21/10/2026. Triagem de entrega, sem implementação e sem fechamento independente dos achados.

## Snapshot e materiais recebidos

- Código: `feature/increment-020-a-molecular-characterization` em `36682074b55596d5632800bea98aff778eee885f`, parent direto `9ccdb9817a78f8de34c085c16443293b1ab99fd9`; main preservada em `08b797e0985e123ffd4d7ca7e5a5e8f040e63851`. Refs e parent consultados no GitHub nesta sessão.
- Governance de entrada: branch `docs/020-a-candidate1-review-20261020` em `2d0cd56378b76e9c64ce88afa8a78544e5d322cc`; main em `a47183dfec8213c765ed43ae482c8c227760a3d5`.
- Relatório do implementador lido integralmente: `increments/020-A/11-checkpoint-1-corrections/CLAUDE_CHECKPOINT1_MAJOR1_COMPLEMENT_REPORT.md`, commit `07185ab3738f279a4536419fde37a079988e8ed4`, 332 linhas/17.224 bytes, SHA-256 `cc9d9ada7c4df4a230c5940cd0a6e66e7b83949efda3fe16d1c9ed6c6d2ce1fb`. Preservado na branch do autor, sem copiar ou editar o original.
- As duas mensagens anexadas pelo responsável são duplicatas byte a byte (17.095 bytes, SHA-256 `e938c7b54863710cd33af41eda539a99da73d64af7360d2cd11a9ba25ddd6ce8`); constituem uma entrega, não duas rodadas.
- Diff do complemento observado: dois arquivos autorizados, +141/−0. Cumulativo observado desde main: quatro arquivos autorizados, +3.930/−1. Adaptador e seus testes não mudaram neste complemento.
- Fonte examinada: `src/molecular/characterization.py`, 1.281 linhas/48.908 bytes, SHA-256 `135f4a34a0a4fa775f191ca1c9fc5180e38239298d38df6fad01da625eed62f8`; blob Git `703f238431dc1fc90ee5676b39609d200a63cad3`, igual ao blob retornado pelo GitHub para esse commit.

## Disposição da entrega e do escopo

Os seis campos demonstrados na sonda anterior foram corrigidos. A errata publicada pelo implementador também retira corretamente a afirmação anterior de que o Pydantic rejeitaria bytes nativamente nesses campos.

A seção 4 do novo relatório considera que tocar os dois hashes de DrawingResult seria inventar um achado fora da autorização. Essa leitura não procede: a tarefa anterior, publicada em `2d0cd56378b76e9c64ce88afa8a78544e5d322cc`, exige literalmente “applicable ordinary-str fields in the new DTOs, particularly IDs and all hashes” e testes para “other applicable ordinary-string DTO fields”. Os seis exemplos não eram uma allowlist de campos; a allowlist de escrita continha os dois arquivos. A especificação congelada, §11, já exige DTOs públicos estritos e identificadores/hashs estritos. A repetição da mesma coerção nos hashes de desenho mantém aberto o mesmo MAJOR-1.

Para remover a ambiguidade prática, esta tarefa substitui o complemento anterior como tarefa ativa e enumera todo o conjunto finito de strings comuns dos novos DTOs. Não altera a especificação nem cria um achado separado por campo. Não autoriza endurecimento dos modelos legados, novos critérios científicos, regras de conteúdo textual ou refatoração geral. O DTO auxiliar do adaptador também integra a mesma implementação nova e recebe os mesmos controles de tipo; isso não o transforma em JSON público.

## Reprodução própria sobre o código exato do HEAD

Python 3.12.14/Pydantic 2.14.0, cópia isolada do módulo de produção e dependência inputs inalterada da baseline. O hash do arquivo e seu blob Git foram conferidos. Não executei pytest, RDKit ou validação Windows. O SVG mínimo usado serve apenas para satisfazer invariantes dos construtores; não é evidência da gramática/segurança gráfica nem de resultado científico.

Inventário mecânico dos BaseModel definidos no módulo: **17 campos com anotação str ou str|None**, sem os Literal/enum já tratados. Para cada campo, quatro chamadas: bytes e bytearray com conteúdo válido, por construtor e por model_validate. Resultado: seis campos recusam os quatro ensaios; **11 convertem silenciosamente nos quatro ensaios**. Todos os 17 controles de str nativa e round-trip JSON válido passaram; três controles de null contratado passaram.

| Campo | Resultado observado |
|---|---|
| `CharacterizationValues.formula` | Recusa os quatro ensaios |
| `DrawingResult.font_name` | **Converte nos quatro ensaios** |
| `DrawingResult.font_sha256_observed` | **Converte nos quatro ensaios** |
| `DrawingResult.svg_sha256` | **Converte nos quatro ensaios** |
| `DrawingResult.xml_parser_version_observed` | **Converte nos quatro ensaios** |
| `CharacterizationProvenance.input_state_id` | Recusa os quatro ensaios |
| `CharacterizationProvenance.entity_id` | Recusa os quatro ensaios |
| `CharacterizationProvenance.state_record_sha256_observed` | Recusa os quatro ensaios |
| `CharacterizationProvenance.representation_path` | **Converte nos quatro ensaios** |
| `CharacterizationProvenance.representation_format_declared` | **Converte nos quatro ensaios** |
| `CharacterizationProvenance.representation_checksum_expected` | Recusa os quatro ensaios |
| `CharacterizationProvenance.representation_checksum_observed` | Recusa os quatro ensaios |
| `CharacterizationProvenance.engine_version` | **Converte nos quatro ensaios** |
| `CharacterizationProvenance.application_version` | **Converte nos quatro ensaios** |
| `MolecularCharacterizationResult.svg` | **Converte nos quatro ensaios** |
| `RDKitCharacterizationOutcome.engine_version` | **Converte nos quatro ensaios** |
| `RDKitCharacterizationOutcome.svg` | **Converte nos quatro ensaios** |

Evidência completa: `evidence/architect-complete-string-matrix.json`; programa diagnóstico: `evidence/architect-complete-string-matrix-probe.py`. O programa pressupõe as cópias locais descritas nele; não precisa ser executado pelo implementador. Sua reprodução própria deve importar o módulo real do checkout-alvo, sem monkeypatch dos validadores, sem model_construct e sem copiar a lógica de validação para testes.

## Correção autorizada e critérios de aceite

Tarefa ativa: `tasks/020-A-CHECKPOINT1-MAJOR1-STRING-CLOSURE.json`. A autorização existente cobre somente completar o MAJOR-1 no CP1, nos mesmos dois caminhos: characterization.py e test_characterization.py. A matriz de 17 campos é o escopo fechado desta rodada: corrigir os 11 remanescentes e preservar os seis já corrigidos.

Exigir recusa de bytes e bytearray antes de conversão nos pontos normais de validação Python, com erro localizado no campo. Preservar str válida, grafia/case dos IDs e checksum esperado, os três null contratados, JSON válido, valores científicos e todas as correções anteriores. Nenhuma regra nova sobre vazio, semântica de versão, paths, conteúdo do SVG ou subclasses de str decorre desta tarefa. Não modificar Literal/numéricos já corretos nem introduzir strict global em modelos legados. Não fixar quantidade de testes antecipadamente: reconciliar a coleta efetiva, sem remover/enfraquecer testes anteriores.

Após a entrega, haverá reverificação independente focal dos quatro achados originais e regressões concretas. O arquiteto não declara MAJOR-2/MINOR-1/MINOR-2 fechados por esta triagem. CP1 não aprovado; CP2/CP3 não autorizados. Não abrir PR, fazer merge ou alterar main.

## Evidência fornecida e limitações

O implementador informa 173 testes DTO com e sem RDKit, suíte completa 1.757 passed/5 skipped e +18 itens desde 1.739/5. Isso é evidência fornecida, não pytest executado pelo arquiteto. A revisão dos testes novos confirma a estrutura declarada: 1+1+10+5+1=18 itens. A sonda própria só prova os resultados de tipos descritos acima. A entrega tem progresso real, mas é parcial para o MAJOR-1.

MAJOR-1 STATUS: OPEN — SAME ORIGINAL FINDING
CHECKPOINT 1 APPROVED: NO
CHECKPOINT 2 AUTHORIZED: NO
CHECKPOINT 3 AUTHORIZED: NO
CODE REPOSITORY MODIFIED BY ARCHITECT: NO
