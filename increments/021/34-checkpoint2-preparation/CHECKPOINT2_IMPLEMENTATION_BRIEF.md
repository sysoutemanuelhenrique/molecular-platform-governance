# Brief de implementação — Incremento 021, Checkpoint 2

Preparação por Codex arquiteto em 24/11/2026, America/Sao_Paulo. **Tarefa preparada, implementação NÃO autorizada.** Este brief executa requisitos já congelados; não modifica contrato, schemas ou critérios científicos. Em divergência, parar e reportar o ponto exato ao arquiteto, sem escolher regra alternativa.

## 1. Entradas, autorização e baseline

- Repositório: sysoutemanuelhenrique/molecular-platform; mesma branch feature/increment-021-receptor-materialization, continuando de **ea8dac9cdc203c337d7f3f9947b54042291f7484**, CP1 aprovado pelo responsável.
- Main do código permanece 08b797e0985e123ffd4d7ca7e5a5e8f040e63851; não implementar em main nem criar outro ramo científico sem reconciliação.
- Governance de preparação: docs/020-a-candidate1-review-20261020 @ fceadfe20ba7d3d63081e4d4a0682bffcd197374. Executar somente após autorização própria publicada pelo arquiteto: o SHA desse despacho autorizado será a entrada, não este snapshot histórico de preparação.
- Especificação: increments/021/15-final-specification/INCREMENT_021_FINAL_SPECIFICATION.md, 377 linhas/64.746 bytes, SHA-256 5de705d609eaf158b0b29a99a0d02e24be4ed0b19d8e127c7e8d70c93aca1bd8. Ler integralmente os quatro anexos e conferir as identidades da tarefa/FROZEN_PACKAGE. Cabeçalhos históricos de draft nos anexos não anulam o congelamento.
- Aprovação do CP1 e permissão de preparar CP2 estão em ../33-checkpoint1-acceptance/OWNER_CHECKPOINT1_ACCEPTANCE.md. **Não autorizam implementação CP2.**

## 2. Entrega e allowlist do CP2

CP2 entrega o adapter DOM real, transcrição de tokens, endpoints/simetria, aplicação do catálogo, serialização e verificação dos bytes derivados. Não publica bundle científico, não implementa leitores Windows, reserva, registry, service ou CLI.

| Caminho permitido após autorização | Alteração delimitada |
|---|---|
| src/molecular/receptor_parsing.py | Entradas aditivas 021; única fronteira de Gemmi; preservar API/DTOs/resultados de parse_receptor_raw e helpers do 020 |
| src/molecular/receptor_materialization.py | DTOs estritos próprios e extensões puras necessárias ao adapter/plano completo; conservar semântica CP1 e hashes dos mesmos payloads |
| tests/test_receptor_parsing.py | Testes do adapter 021; preservar testes/oráculos 020 |
| tests/test_receptor_materialization.py | Testes de decisões/hashes/regras novas; preservar 92 testes CP1 e R-1 |
| tests/fixtures/receptor_materialization/** | Somente fixtures científicas públicas/sintéticas e seus manifestos/oráculos de teste; sem código executável ou arquivos pessoais |

Esta é a projeção do §19 congelado: quatro arquivos editáveis mais uma raiz de fixtures. Não criar outro módulo fonte/teste fora desses caminhos, nem copiar relatórios de execução para fixtures. atomic.py, activity.py, pyproject.toml, receptor_inspection/selection/resolution/registry/service, CLI e módulos de ligantes permanecem inalterados. Testes fora da allowlist podem ser executados, nunca editados. Ajustes nos dois arquivos CP1 são somente os requeridos pelo CP2, não refatoração geral.

## 3. Pontos concretos do código de entrada

1. O domínio aprovado importa os tipos 020 apenas sob TYPE_CHECKING e reproduz a identidade legada por helper puro. Preservar a importação sem Gemmi/RDKit em processo novo, inclusive python -O. Não reintroduzir import de receptor_inspection/receptor_parsing em runtime no domínio.
2. compute_connection_decisions_key ainda hasheia decisões vazias; MaterializationPlan ainda só carrega átomos/categorias. São limites declarados do CP1, não implementação de conexões. CP2 precisa carregar ConnectionDecision completo e usar o vetor real nos hashes/plano, preservando o envelope e o resultado do caso vazio. Novos parâmetros internos podem ter default vazio para preservar chamadas CP1; o fluxo real CP2 nunca substitui conexões presentes por esse default.
3. build_materialization_plan hoje projeta S/D/U/X/O e recebe CategoryDecision já construído; unavailable_categories e warnings ainda são parciais. Integrar decisões reais de categorias/conexões/avisos antes de emitir um plano CP2 completo; não apresentar o plano parcial como resultado materializável. Não copiar reconhecimentos calculados para fingir consentimento.
4. parse_receptor_raw do 020 recebe Path e relê o arquivo; os DTOs antigos não contêm todos os tokens/coordenadas e usam a grafia antiga de inserção. **Não reutilizá-lo como leitor materializador, não corrigir suas colunas antigas e não alterar seus DTOs.** O 021 recebe bytes capturados e mantém sua proveniência separada.
5. receptor_parsing.py possui import Gemmi em nível de módulo no código de entrada. O novo caminho deve cumprir o import tardio/checagem do pin exigidos pelo §3. É permitida a organização mecânica necessária dentro desse arquivo, com prova de não regressão da API e resultados antigos; não transferir Gemmi para outro módulo nem alterar a CLI como atalho.

## 4. Fluxo técnico e separação de responsabilidades

As assinaturas privadas são escolha de implementação, documentadas no relatório; não criar novas APIs públicas de service neste checkpoint. A sequência obrigatória, independentemente desses nomes, é:

1. Receber bytes RAW imutáveis e contexto/seleção já validados, conferir hash/tamanho contra SourceContext, pin Gemmi 0.7.5 e limites aplicáveis. Não abrir arquivo científico, seguir URL ou refazer inspect/resolve a partir de dentro do novo caminho. Na execução futura, captura única e segura dos quatro YAMLs/RAW pertence ao CP3; em CP2 testar a fronteira de bytes sem alegar leitor Windows pronto.
2. Parsear esses bytes uma vez em DOM Gemmi na fronteira, validar estrutura/limites e extrair DTOs próprios com tokens/ordinais/índices suficientes para planejar e serializar sem reabrir RAW. Nenhum Document/Block/Loop/Structure ou objeto nativo atravessa a fronteira pública. Dentro do adapter, é permitido reconstruir DOM a partir dos DTOs/tokens, sem novo parsing do RAW. O reparse obrigatório dos bytes de saída é uma verificação diferente, não segunda leitura da fonte.
3. Aplicar as projeções S/D/U/X/O aprovadas, resolver conexões em M e calcular todas as decisões de categorias/linhas/tags. Só o plano completo tem seus vetores e hashes finais. A geração de entry/block tbmp_<plan_key> usa esse hash final; não inserir o próprio plan_key nos payloads-fonte e criar ciclo de identidade.
4. Serializar receptor.cif em bytes UTF-8 determinísticos e produzir os DTOs/dados completos da auditoria do adapter. Os reconhecimentos públicos e sua persistência pertencem à declaração/service CP3: o adapter não inventa declared_by, tempo ou ack automático. Se construir AuditRecord completo num teste, usar os acknowledgements explícitos do teste validados pela produção CP1. Não inventar um audit completo com consentimento implícito.
5. Reparsear a saída com Gemmi real e comparar independentemente aos vetores esperados do plano, tokens, contagens e fechamento referencial. Falha produz INVALID_OUTPUT; aceitação pelo writer/reader da mesma biblioteca sozinha não é oráculo suficiente. Nenhum arquivo final é publicado neste CP.

É permitido usar um estágio interno de máscara atômica para resolver dependências de conexões/categorias, mas ele nunca é exposto/persistido como plano final aceito. Não criar novo algoritmo científico ou alterar precedência S/D/U. Preview pode propor omissões condicionais; a exigência de acknowledgements em declare/run continua integral e será integrada no CP3.

## 5. RAW, tokens e integridade estrutural (§§4–7)

- Gemmi 0.7.5 real; ausente/versão diferente → erro de configuração ENGINE_UNAVAILABLE/ENGINE_VERSION, sem substituto silencioso. Falha de parsing → taxonomia 021, causa preservada. Não usar parser CIF escrito em Python; regex/Decimal só validam campos segundo o perfil depois do DOM.
- 16 MiB RAW; um block; sem BOM UTF-8 estrutural, compressão, save frames, duplicação de tags canônicas ou categorias malformadas. Comparação de tags ASCII case-insensitive; valores/identificadores preservam caixa e tokens. Respeitar os demais tetos do §4 antes de duplicar/planejar/serializar: 100.000 átomos, 50.000 conexões, 256 categorias, 128 tags/categoria, 500.000 linhas, 4.000.000 células, 1 MiB/célula e 32 MiB/saída/auditoria. Não declarar teto rígido de memória nativa.
- atom_site.id único global; modelo positivo explícito; usar M escolhido, nunca primeiro modelo/or 1. Vínculos atom_site→struct_asym→entity inequívocos; NFC só para correspondência injetiva, nunca como normalização de identidade/hashing.
- Preservar coordenadas, precisão, null real vs '?' / '.' citados, ocupância 0/parcial/null, B-factor, altlocs, H/D e microheterogeneidade. Numéricos seguem regex fechada/Decimal do §6: 1.2e3(4) válido, 1.2(4)e3 inválido; nenhuma conversão numérica para escrever tokens. Todas as variantes de um asym seguem a mesma decisão.
- Preservar D ausente em M como não aplicável auditado; entity.type fonte, sem classificar por HETATM/report.chains. Nenhuma preparação química, expansão, reparo, adição/remoção conveniente de H, renumeração ou escolha de ocupância/altloc.

## 6. Conexões, simetria e IdentityBasis (§§9–10.1)

- Ler inserção canônica pdbx_ptnr{1,2}_PDB_ins_code diretamente dos tokens RAW. Não usar ParsedConnection do 020 como autoridade. Endpoints devem resolver em M para uma ocorrência/atom name, eventualmente conjunto de altlocs uniforme, em ordem fonte; sem escolher primeiro match, produto cartesiano ou heurística de namespace.
- Todos os campos ptnr3 preenchidos/literais citados são recusados; só ausência/null CIF real é aceita. IDs de conexão únicos e tipo literal preservado. Resolver endpoints antes de decidir K; incompatibilidade não vira omissão inocente.
- Implementar as quinze células K=0/1/2 × simetria conforme o corpo: K=1 covalente sempre recusa; metalc/hydrog só omite se parceiro removido for asym inteiro excluído por D/X reconhecível; K=2 só preserva identidade provada; K=0 omite auditado. Não aplicar exceção a falha de match, outro modelo ou remoção parcial. saltbr/mismat/unknown recusam K>0; K=0 pode omitir com token auditado.
- 1_555 sem nenhuma tabela tem base de convenção; tabela presente impede fallback. Mesmo id uma vez em cada tabela concordante não é duplicação. Para identidade 1_555 em K>0, operador 1 precisa estar confirmado como identidade em todas as tabelas presentes. Não usar operadores de assembly, nome de grupo espacial ou equivalência matemática fora da gramática para fabricar prova.
- IdentityBasis por endpoint é independente de K e segue a precedência fechada §10.1; não sortear bases. K=0 com prova de identidade insuficiente usa unsupported-discarded conforme a candidata 2 congelada, inclusive operador 1 só em uma de duas tabelas. Os sete pares alcançáveis e os dois impossíveis devem ter provas reais; os hashes documentais do anexo não substituem connection_decisions_key/plan_key completos de produção.

## 7. Catálogo, serialização e auditoria (§§11–13/18)

Incorporar as regras dos bytes exatos do catálogo, constante SHA-256 8561039fd15137811b60316336dff04539df3732710dca6ec4009f23150d6d03; não criar catálogo configurável, lookup por diretório corrente ou dependência externa. São 94 categorias: 24 filter, 1 generate, 67 omit, 2 guard_then_omit; omissões de famílias _pdbx_validate_/_pdbx_nmr_/_em_ seguem a gramática já corrigida no CP1. Categoria/tag desconhecida fora das permissões recusa.

Executar cada regra, sem confundir omit com filter vazio ou pular guardas: ATOM_MASK; ANISOTROP_ATOM_ID; RETAINED_ASYM/ENTITY; sequência inteira declarada e branch inteiro; fechamento CCD incluindo parent; CONNECTION_ACTIONS/tipos usados/elementos; contexto cell/symmetry/operadores; resíduos modificados/anotações de ausências; omissões auditadas; NCS e posições especiais; DERIVED_ENTRY.

NCS não identidade com generate/null recusa UNSUPPORTED_NCS antes de omitir; given/identidade podem ser omitidos auditados, sem aplicar transformações. Código/matriz incompletos inválidos recusam INVALID_CIF. Posições especiais exigem contexto inequívoco e contagens/aviso corretos; não recalcular ocupância. Tensor anisotrop U ou B completo e finito é obrigatório quando a categoria existe; não converter U↔B nem inventar leaving atoms/átomos ausentes.

Preservar tags como tokens brutos e referências suportadas; não quote sobre token já citado. Tags/categorias de saída canônicas ordenadas; linhas sobreviventes na ordem fonte. Gerar somente entry/block novos; simetria é contexto fonte e source_symmetry_only=true. Registar toda linha/tag/categoria removida, indisponibilidades, motivos, conjuntos endpoints, hashes e ordinais, sem duplicar integralmente valores de metadados omitidos. Receptor.cif não precisa ser byte-idêntico ao RAW; os tokens científicos preservados precisam corresponder. JSON de auditoria usa primitivos fechados, sem float, chaves ordenadas e LF; hashes de payload continuam sem LF. Sem timestamp/UUID operacional nativo na auditoria para mascarar não determinismo.

ConnectionDecision, row_key/source_rows_key, Summary e dados de auditoria necessários devem seguir SCHEMAS; não novos formatos improvisados. Os DTOs adicionais são closed/frozen/strict com arrays explicitamente convertidos somente na fronteira, sem coerção de elementos. Preservar __cause__ e a mesma instância de KeyboardInterrupt/SystemExit; não converter BaseException em erro científico nem introduzir validações por assert removíveis com -O.

## 8. Fixtures reais e oráculos (§23)

- Fixtures sintéticas mínimas precisam conter categorias/coordenadas/referências suficientes; a fixture 020 mínima não atende automaticamente. Checksums de RAW/snapshots usados em integração devem vir dos bytes realmente fornecidos, não 'a'*64 ou hash documental tratado como científico. DTOs isolados podem continuar usando constantes nos testes puros antigos; não enfraquecê-los por essa orientação.
- T021-162 e positivos D-01(b) exigem lineage de entrada real, incluindo casos metal–água e hydrog pertinentes. Manifesto de fixture: origem exata (URL oficial RCSB/wwPDB ou arquivo de fonte pública identificado), data/versão quando disponível, SHA-256/tamanho do original, M/S/D/U, transformações enumeradas e hashes dos derivados, oráculos esperados de átomos/conexões/recusas. Preservar o original e testar a versão não editada quando suportada; derivado editado não é depósito intacto. Não acrescentar artificialmente tabelas de operadores para fazer um caso passar.
- Exigir cobertura de inventários 5i55, 1pfe e 3dg1_final. Reobter ou localizar bytes de origem identificável, não presumir igualdade entre uma URL atual e o inventário histórico. 1pfe passa cobertura de categorias/tags, mas deve recusar no gate 1_555/9_555; não convertê-lo em caso positivo. 5i55/3dg1_final só contam como positivos quando realmente executados com expectativas verificadas.
- Incluir ao menos uma entrada real NMR multi-modelo, uma EM e uma com struct_ncs_oper, com checksums/lineage. Para NCS, a recusa esperada é resultado válido quando os bytes exigem. NMR/EM demonstram M explícito e perda de metadados auditada, sem afirmar conformer representativo/qualidade experimental do recorte. Selecionar entradas dentro dos limites do perfil; impossibilidade de localizar fixture verificável é impedimento explícito, não omissão silenciosa.
- Downloads de fixture, se necessários depois da autorização, são aquisição controlada de evidência de teste pública; não rede durante pytest nem recurso novo de aquisição da aplicação. Não instalar ferramenta extra/global. Não copiar ZIP do governance, arquivos privados ou executáveis para fixtures. Metadados públicos de autoria dos depósitos permanecem atribuídos na proveniência, sem confundir com autoria do software.

## 9. Prova, execução e critérios de aceite

São **79 cenários normativos**, não promessa de 79 funções pytest: T021-041–090 (50), 141–158 (18), 162 (1), 164–173 (10). A cópia extraída em evidence/CP2_SCENARIO_SCOPE.csv preserva exatamente os campos do anexo congelado, sem alterar resultados. Mapear cada ID a teste de produção/asserção, fixture, limite e execução real. Parametrizações ampliam itens; não contar um helper/sonda textual como prova do cenário.

Gemmi 0.7.5 nativo é obrigatório para aceitar CP2. Sentinela, monkeypatch que fabrica parsing, teste só de DTO ou 'import disponível' não provam integração. Mocks servem para falhas na fronteira certa. Usar comparação independente de vetores/tokens/fechamento contra saída, golden envelopes literais e fonte/versão real; ausência de ciência duplicada no teste não autoriza oráculo tautológico. Não pytest.raises(Exception), não snapshot/diff de attempts.

Após autorização, executar no ambiente existente: coleta antes/depois; `python -B -m pytest -p no:cacheprovider tests/test_receptor_parsing.py tests/test_receptor_materialization.py -q -rs`; regressão receptor 020 pertinente; suíte completa uma vez; `git diff --check`, diff da rodada e cumulativo. Enumerar nós/skips, funções/parametrizações/itens e explicar qualquer remoção/mudança. A referência recebida de CP1 é 1.573 coletados / 1.568 passed / 5 skipped, fornecida pelo implementador; a coleta inicial real deve confirmá-la ou explicar o ambiente, sem fingir reexecução histórica. Nenhuma contagem de CP2 é prevista/fabricada neste brief.

Cobrir adicionalmente limites e falhas das fases CP2 (parse/plan/serialize/verify), pin/ausência do engine, interrupções separadas por classe e preservação do RAW; fases de storage/reserva/publicação/apresentação ficam em CP3/CP4. Testar domínio sem opcionais em processo limpo, preservar o vetor R-1 e os treze goldens existentes. Hashes de saída repetidos devem coincidir para mesmo payload/pin/perfil; mudança da ordem de visita de categorias não pode mudar decisões científicas ordenadas conforme contrato.

Adapter pode ser testado em Linux com nativos reais, conforme §4/§19. Registrar sistema e versões reais. Validação de produção Windows 11/NTFS, reparse points e concorrência entre dois processos são gate CP3, não prova obtida pelo CP2. Se executar em Windows existente, registrar evidência sem generalizar para outros hosts. Qualquer cenário não executado deve permanecer explicitamente pendente, nunca convertido em skip aprovado.

## 10. Entrega e limites de publicação

Após autorização expressa da tarefa, staging/commit/push normais apenas dos caminhos permitidos na mesma feature, mantendo ea8dac9 como ancestral e sem reescrever histórico. Confirmar remoto e main inalterada. Relatório próprio em `increments/021/35-checkpoint2-implementation/CLAUDE_INCREMENT_021_CHECKPOINT2_IMPLEMENTATION_REPORT.md` e `evidence/claude-*`, em branch Claude própria do governance a partir do snapshot autorizado. Não editar STATUS/tarefas centrais nem pareceres.

Relatório deve identificar fontes/versões/manifestos, código completo/pai/branch, diff exato, 79 cenários mapeados, resultados reais/limitações e identidades de todos os outputs. Registrar alteração necessária dos pontos parciais CP1 sem reabrir os doze fechamentos/R-1 por preferência. O materializador não pode ser anunciado como receptor quimicamente preparado ou pronto para docking. Sem PR/merge/main/tag/release/CP3/CP4, automação ou retomada do 020-A. Preservar Claude outputs/, _figura_curcumina/, increment-009-review.txt e itens pessoais do governance.

Próximo gate: responsável autoriza tarefa CP2 exata; implementador executa; arquiteto recebe evidência e prepara revisão independente. Nenhum agente foi acionado e nenhuma execução está autorizada pela existência deste arquivo.

CHECKPOINT1 APPROVED BY OWNER: YES
CHECKPOINT2 TASK PREPARED: YES
CHECKPOINT2 IMPLEMENTATION AUTHORIZED: NO
CHECKPOINT3 IMPLEMENTATION AUTHORIZED: NO
FINAL SPECIFICATION FROZEN: YES
CODE REPOSITORY MODIFIED BY ARCHITECT: NO
AUTOMATED DISPATCH: NO
