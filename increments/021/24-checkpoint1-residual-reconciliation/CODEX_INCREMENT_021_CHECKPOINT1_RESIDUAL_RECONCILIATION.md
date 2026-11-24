# Reconciliação focal e instruções de correção residual — Incremento 021, CP1

Data: 24/11/2026, America/Sao_Paulo. Codex arquiteto. Resposta executável dentro do CP1 autorizado, sem novo estudo, implementação ou mudança de contrato. Nenhum agente foi acionado automaticamente.

## 1. Parecer recebido e snapshots

Coordenação de entrada: `docs/020-a-candidate1-review-20261020 @ 155661115851c2a5fb70f5d905425baeb4d23c9f`. Código: `feature/increment-021-receptor-materialization @ 42b4804b5f4ea01ddf320c45473d8b4f980ea67e`; main/baseline `08b797e0985e123ffd4d7ca7e5a5e8f040e63851`. Main governance `a47183dfec8213c765ed43ae482c8c227760a3d5`. HEADs remotos coincidiram antes do trabalho.

[Parecer focal](https://github.com/sysoutemanuelhenrique/molecular-platform-governance/blob/854ae336621116f7047033b5146c7c4834ebf9c2/increments/021/23-checkpoint1-focal-review/CLAUDE_INCREMENT_021_CHECKPOINT1_FOCAL_REVIEW.md): branch `claude/021-cp1-focal-review-20261124`, commit `854ae336621116f7047033b5146c7c4834ebf9c2`, pai único 1556611. Identidade: 251 linhas / 17.535 bytes / SHA-256 `61865d461b72e318e52209f202b5f44288971dc1f8255360b697236e2ea71ed5`. Manifesto de oito entradas confere; os nove blobs próprios (parecer + oito evidências) foram verificados. A branch não alterou STATUS/tarefas/contratos/históricos. Não a mesclei.

Normativos congelados e anexos permanecem no commit b0e60f6528f6fcb828aa6dd5577824e08c7c9fac, principal SHA-256 5de705d609eaf158b0b29a99a0d02e24be4ed0b19d8e127c7e8d70c93aca1bd8. INPUT_IDENTITIES.json identifica os materiais. Os dois arquivos de código continuam com os hashes da entrega 42b4804; nenhuma edição do código foi feita pelo arquiteto.

## 2. Disposição adotada, sem reabertura

Fechados independentemente por Claude: **ARCH-01, ARCH-02, ARCH-03, MAJOR-B, MINOR-1, MINOR-2, MINOR-4, MINOR-5 e MINOR-6**. Preservar as nove disposições; reexaminar somente se a nova correção produzir regressão concreta. As três NOTES permanecem preservadas. As observações de cruzamento entity_id no futuro adapter, abrangência NFC atual e duck typing não viram novos bloqueios do CP1.

Restam **MAJOR-A (rótulo histórico, severidade residual MINOR), MINOR-3 e MINOR-7**. Contagem residual do parecer: **0 BLOCKER / 0 MAJOR / 3 MINOR**, os três impedem a aprovação por critérios contratuais pendentes. REQUEST CHANGES permanece. Isso não altera a contagem histórica de quatro MAJORs/oito MINORs do parecer inicial.

Os 43 cenários já têm fechamento independente de 40 provados/3 parciais por desenho/0 lacunas, sem fechar automaticamente esses três achados. A correção preserva T021-018/024/038 no limite CP1 e não exige conexão/adapter antecipado.

## 3. MAJOR-A residual — regra concreta de formato

**Aceito o resíduo e determino, como orientação de conformidade ao §5, recusa da contradição declarado/detectado.** Não usar o aviso `declared-format-mismatch` como autorização para materializar com proveniência contraditória. Não alterar o relatório antigo nem executar inspect/resolve para corrigi-lo.

Fonte primária: [receptor_inspection.py na baseline](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/src/molecular/receptor_inspection.py) define `_DECLARED_FORMAT_ALIASES = {'cif':'mmcif','mmcif':'mmcif','pdb':'pdb','ent':'pdb'}` e usa `raw_format_declared.strip().lower()` antes de comparar ao detectado. Essa normalização vale apenas para **rótulos de formato**, nunca IDs/tokens científicos/checksums.

No caminho puro novo: normalizar acquisition.raw_artifact.format e inspection.raw_format_declared por esse mesmo mapa e regra. Ambos precisam ser reconhecidos e equivalentes entre si e ao formato detectado mmcif; inspection.structure_format e resolution.structure_format continuam exigidos como mmcif. `cif` e `mmcif` (inclusive a normalização strip/lower já usada pelo 020) são equivalentes aceitos; `pdb`/`ent`, `xyz` e outros desconhecidos são recusados neste perfil. Usar MaterializationConfigurationError com código existente `INVALID_RECORD`. Preservar a ordem engine→fontes→seleção, as verificações de checksum/IDs já fechadas e todos os valores originais dos registros.

O mapa pequeno pode ser projetado no novo módulo puro; não importar receptor_inspection em runtime, nem editar o 020. Não há novo formato suportado, fallback ou escolha científica dependente de aprovação adicional. É a verificação antes omitida do perfil mmCIF já congelado, escolhendo a recusa entre as duas soluções que o revisor explicitou.

Testes mínimos: acquisition=pdb/declarado=pdb/detectado=mmcif, inclusive com declared-format-mismatch; acquisition=mmcif/declarado=pdb; acquisition=xyz/declarado=xyz; contradição reversa; formato desconhecido numa fonte; aliases cif/mmcif cruzados nas duas direções e rótulos normalizados pela regra 020; controle coerente mmcif. Nada regrava ou reclassifica a fonte.

## 4. MINOR-3 residual — unicidade e gramática

**Aceito.** Em cada tupla kept_row_ordinals e omitted_row_ordinals, exigir unicidade antes de aceitar; manter não negatividade/estritez e disjunção entre tuplas. Recusar, nunca deduplicar silenciosamente nem ordenar para reparar, pois isso mudaria o payload aceito.

Categorias explícitas continuam sendo os 94 nomes canônicos já incorporados. Para famílias de omissão, exigir `re.fullmatch(r'(?:_pdbx_validate_|_pdbx_nmr_|_em_)[a-z0-9_]+', category)` e action=omit. Não usar startswith sozinho nem `$` que admita LF final; não aplicar strip/lower para fazer nome inválido parecer válido. Essa é a gramática delimitada solicitada pelo revisor, não um parser CIF genérico, campo novo ou alteração do catálogo.

Testar duplicatas em ambas as tuplas, sobreposição entre tuplas, ordinais únicos válidos; LF, prefixo nu, espaço, ponto/nome de item, uppercase e controle em famílias; positivos de cada uma das três famílias com letras/dígitos/underscore. Manter válidos omit com arrays vazios + fonte, filter com tag gerada permitida e generate sem fonte. Sem adaptar DOM/filtrar arquivos ou inferir cobertura de linhas fonte nesta fase.

## 5. MINOR-7 residual — prova regressiva literal pronta

**Aceito.** Forneço `evidence/DOCUMENTARY_GOLDEN_VECTORS.json`, com treze vetores de bytes canônicos e SHA-256 literais: JSON básico; inspection_id legado; SourceContext; OccurrenceIdentity; atom_ids; X; O; decisões atômicas; conexão vazia CP1; decisões de categoria; PlanBinding; policy_id; request_key. Os envelopes seguem §13/SCHEMAS; os valores foram gerados por script separado usando só hashlib/json, sem importar produção. O generator permanece disponível para auditoria, não para ser chamado pelos testes para gerar seus próprios valores esperados.

Uma verificação separada sobre a produção intacta 42b4804 confirmou 13/13 digests pelas funções correspondentes, com Gemmi/RDKit bloqueados, sem stub. Isso demonstra que o resíduo é de **prova regressiva nos testes**, não requer mudar algoritmos de hash. São fixtures documentais: bytes declarados de teste, não RAW científico, geometria ou resultado nativo. Os registros artificiais e o JSON de policy usado como bytes de entrada não são prova do serializer/persistência YAML CP3.

Copiar os vetores necessários como literais para o único arquivo de testes autorizado; não adicionar JSON/fixture externa ao código, runtime download ou leitura do governance. Cada teste deve chamar a função de produção correspondente e comparar com o digest literal, usando o DTO adequado. Só comparar H(payload) genericamente para todos os casos não prova os builders de envelopes. hashlib pode conferir o literal contra os bytes, mas **não** produzir o expected dentro do teste. Manter Unicode/ordem de arrays e envelopes, não atualizar um literal apenas porque a produção falhou.

O teste legado precisa chamar `_compute_legacy_inspection_id` novo, com os inputs exatos do vetor (protein-1, parser gemmi/0.7.5, raw_checksum='a'*64, raw_format=mmcif), e comparar ao literal `1c217d99e7b2b09d9c31a0c8f9daf056c48aa916bdf957cae83df449ad68e80c`. Comparar opcionalmente com o helper antigo é um terceiro controle, não substituto da chamada nova/literal. Seu antigo teste old_helper==constante_old_helper não constitui essa prova.

Os vetores são auxílio de teste não normativo; o contrato congelado prevalece. Se houver erro no vetor, registrar e confrontar bytes/envelope, sem mudar o contrato para fazê-lo passar. Não criar funções CP2 de source-row hashing por causa dos seeds documentais presentes na fixture.

## 6. Evidência própria e limites

Li o parecer completo e os trechos de código/contrato pertinentes, conferi manifesto/blobs e refiz a sonda pura já publicada no recibo 22 sobre 42b4804. Os resíduos de formato/ordinais/nomes continuam observáveis. Gerei os vetores sem produção e depois os comparei separadamente com as funções reais; 13/13 coincidem. Os scripts e outputs estão neste diretório. Essa comparação não é fechamento independente das futuras correções.

Não executei pytest, suíte completa, Gemmi nativo, RAW, Windows ou concorrência. O revisor executou 75 testes com sentinela inerte para montar DTOs 020, prova diferente do import sem opcionais. Os 1551 passed/5 skipped Windows continuam evidência fornecida do implementador. Nenhum resultado histórico vira teste executado nesta etapa. Cópias e scripts auxiliares são externos ao código, sem bytecode.

## 7. Execução e próximo gate

Tarefa preparada: `tasks/021-CHECKPOINT1-RESIDUAL-CORRECTIONS.json`, para Claude implementador separado do revisor, dentro da autorização humana original de CP1, mesmos dois arquivos e mesma branch. Continuar a partir de 42b4804 por commit(s) aditivo(s) e push normal. Não reeditar históricos ou relatórios recebidos. Publicar relatório próprio em `increments/021/25-checkpoint1-residual-corrections/CLAUDE_INCREMENT_021_CHECKPOINT1_RESIDUAL_CORRECTIONS_REPORT.md` e evidence/claude-* em branch própria do governance.

Executar testes focais, import bloqueado normal/-O, suíte completa e coleta no ambiente disponível, nomear skips e medir a diferença real contra 1556/75 antes desta rodada; não fixar contagem futura artificial. Preservar os nove fechamentos, os 43 cenários e as três NOTES por regressão, sem reabertura. Corrigir apenas os três resíduos, sem nova pesquisa arquitetural ou implementação de CP2. Não é necessário pedir nova decisão científica ao responsável para essas correções de conformidade.

Depois da entrega exata, arquiteto recebe código/relatório e prepara revisão final curta dos três resíduos e regressões no delta. Não há disparo automático nem aprovação antecipada. Não assegurar que o próximo parecer será favorável só porque estas instruções existem.

FOCAL REVIEW RECEIVED AND VERIFIED: YES
ARCHITECT RESIDUAL RECONCILIATION COMPLETE: YES
INDEPENDENTLY CLOSED FINDINGS PRESERVED: 9
OPEN RESIDUAL BLOCKERS: 0
OPEN RESIDUAL MAJORS: 0
OPEN RESIDUAL MINORS: 3
CHECKPOINT1 APPROVED: NO
CHECKPOINT2 IMPLEMENTATION AUTHORIZED: NO
FINAL SPECIFICATION FROZEN: YES
CODE REPOSITORY MODIFIED BY ARCHITECT: NO
AUTOMATED DISPATCH: NO
