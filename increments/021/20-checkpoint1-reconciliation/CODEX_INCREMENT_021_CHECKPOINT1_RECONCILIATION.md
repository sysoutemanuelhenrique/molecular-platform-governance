# Reconciliação arquitetural — Incremento 021, Checkpoint 1

Data: 24/11/2026, America/Sao_Paulo. Papel: Codex arquiteto. Esta resposta confronta o parecer independente e prepara correções do CP1 já autorizado. Não implementa, não aprova o checkpoint e não encerra achados independentemente.

## 1. Snapshots e materiais verificados

Coordenação de entrada: `docs/020-a-candidate1-review-20261020 @ d577b0dfddd3c71f9287b4c9cdcc783ea0865654`. Código: `feature/increment-021-receptor-materialization @ 711f3070765efe67a5799f939f1a18306ed8afdd`, pai direto/main `08b797e0985e123ffd4d7ca7e5a5e8f040e63851`. Main do governance: `a47183dfec8213c765ed43ae482c8c227760a3d5`. Refs remotas conferidas antes de trabalhar, sem divergência.

[Parecer independente](https://github.com/sysoutemanuelhenrique/molecular-platform-governance/blob/2e36222b087134f9ba725bc2ad96c3ba39fb8801/increments/021/19-checkpoint1-review/CLAUDE_INCREMENT_021_CHECKPOINT1_ADVERSARIAL_REVIEW.md): branch `claude/021-cp1-adversarial-review-20261124`, commit `2e36222b087134f9ba725bc2ad96c3ba39fb8801`; 176 linhas, 15.726 bytes, SHA-256 `2af4f1880e6c1e086204ae12b298419eaf61809de8bf5e2a7f29f30ad7d4fdc4`. Seu pai é o snapshot de coordenação. A branch adiciona exatamente dez arquivos: parecer + nove evidências, sem modificação de STATUS/tarefas/históricos. A mensagem entregue diz dez evidências; a árvore real contém nove. É uma precisão de recibo, não defeito do código.

Contrato congelado e quatro anexos no commit `b0e60f6528f6fcb828aa6dd5577824e08c7c9fac`, SHA-256 principal `5de705d609eaf158b0b29a99a0d02e24be4ed0b19d8e127c7e8d70c93aca1bd8`. Os bytes locais usados foram comparados aos blobs remotos desses commits, incluindo os dois arquivos de código. Relatório do implementador permanece no snapshot `51752b4ce7603d1f14677b0b030edc176b9df13f`; não foi mesclado, nem os documentos do revisor. INPUT_IDENTITIES.json registra a evidência por arquivo. A especificação e todos os materiais históricos permanecem intactos.

## 2. Contagem e decisão arquitetural

O parecer distingue os achados confirmados da triagem dos achados independentes novos. Contagem cumulativa desta resposta: **0 BLOCKER, 4 MAJOR, 8 MINOR, 3 NOTE**. São ARCH-01/02 (dois MAJORs) + MAJOR-A/B (dois novos); ARCH-03 (um MINOR) + MINOR-1–7 (sete novos). As nove linhas informais da mensagem são agrupadas pelos sete MINORs do relatório, especialmente MINOR-1. Não edito nem reinterpreto retroativamente o bloco de contagem “INDEPENDENT” do autor.

**REQUEST CHANGES mantido.** Aceito os defeitos apontados, com delimitações de solução abaixo. Nenhum está fechado pela minha aceitação. Os 43 cenários seguem 31 provados/10 parciais/2 lacunas conforme classificação do revisor; as correções devem ampliar asserções e controles sem transformar essa classificação em aprovação automática. Não há alteração contratual, expansão científica ou necessidade de CP2 para corrigir os DTOs/planner atuais.

## 3. Evidência própria desta reconciliação

Ambiente: Linux, Python 3.12.14/Pydantic 2.13.4, sem Gemmi/pytest disponíveis. Nenhum pacote instalado. Reconfirmei fonte/contrato, importação limpa em subprocesso e executei os dois scripts publicados do revisor depois de inspecionar seus bytes e conferir seus Git hashes. Sobre o mesmo código intacto, os 23 resultados de domínio coincidiram com o JSON publicado; golden hashes canônicos e controles de estritez também coincidiram. Comprovei adicionalmente omit retendo linha, ordinal negativo e linhas sem source_rows_key; `NOT_A_CODE` é recusado normalmente e aceito sob `python -O` nos dois tipos de erro.

As sondas de lógica usam sentinela inerte de importação, explicitamente diagnosticada: nenhum atributo nativo pode ser chamado. Isso não prova Gemmi, parsing ou importação sem Gemmi; o processo limpo, sem sentinela, é que prova a falha de import. A assinatura confirma a falta dos escalares acquisition checksum/policy protein_input_id; esses dois casos precisam de novos testes depois da correção da API. Não executei pytest, suíte completa, Windows, Gemmi real ou concorrência. Os 43 testes passando com sentinela são execução do revisor, não minha. Os 1.519 passed/5 skipped são resultados fornecidos pelo implementador, não reexecutados por mim, e a identidade dos cinco skips ainda precisa ser exposta no novo relatório.

O script de reconciliação e seu output ficam em evidence/. Reexecução externa: `python -I -B ARCHITECT_RECONCILIATION_CHECKS.py --code-root <snapshot-711f307> --review-evidence-dir <evidencias-do-revisor-2e36222> --output <arquivo-externo>`. Esse script é para o snapshot defeituoso identificado, não uma suíte de aceitação da correção futura.

## 4. Disposições dos MAJORs e ARCH-03

| Item | Disposição | Correção delimitada e prova de fechamento |
|---|---|---|
| ARCH-01, MAJOR | Aceito | Tipos inspection/resolution sob TYPE_CHECKING; caminho puro não carrega biblioteca nativa. Processo novo com Gemmi/RDKit bloqueados, sem stub. Preservar exatamente a identidade de inspeção antiga. |
| ARCH-02, MAJOR | Aceito | Projetar D em M antes da agregação polimérica. Testar remove fora de M em S e keep fora de M fora de S, além dos controles presentes que continuam recusados. |
| MAJOR-A | Aceito | Completar fontes/escalares obrigatórios; conferir ambos parsers, formatos, acquisition checksum, todos IDs, schema/profile e inspection_id recalculado. Não atribuir 0.7.5 a fonte 0.7.4. |
| MAJOR-B | Aceito | Autovalidação do policy_id; integridade e equivalência de todos campos do existente contra candidato, exceto declared_at. Retornar o record existente íntegro; adulteração recusa sem overwrite. |
| ARCH-03, MINOR | Aceito | filter permite generated_tags quando o catálogo assim manda (_cell/_symmetry entry_id), sem permitir tags sobrepostas. Não adiantar serializer. |

**ARCH-01 — ressalva à solução sugerida, não contestação do achado:** mover compute_inspection_id para dentro de build_source_context resolve o import inicial, mas ainda faz a função de domínio carregar inspection→parsing→Gemmi quando chamada. A restrição congelada é fronteira nativa única no adapter (§3), além do T021-040. Minha instrução histórica de reutilizar o helper acoplado estava incompleta; esta reconciliação a substitui apenas como orientação de implementação, sem editar o brief/histórico ou contrato.

Solução concreta recomendada dentro do módulo novo: projetar os mesmos sete campos (inspection_schema_version, inspection_profile_version, parser_name, parser_version, protein_input_id, raw_checksum, raw_format) e reutilizar o backend puro `promotion.compute_semantic_key`, que é o mesmo usado por `receptor_inspection.compute_inspection_id` na baseline. A canonicalização antiga faz NFC; não trocá-la pela canonicalização 021 que preserva tokens. Tipos antigos ficam somente em anotações. Isso duplica apenas a projeção estreita de um payload versionado, não parsing nem inferência científica; fixar compatibilidade por bytes/hashes independentes. Uma alternativa igualmente pura e byte-compatível cabe ao implementador justificar. Import tardio sozinho não é suficiente para esse caminho; modificar o 020/pyproject está proibido.

**MAJOR-A — fronteira:** preferir receber ProteinInput e ReceptorSelectionPolicy já carregados/validados junto com inspection/resolution, em vez de inferir campos faltantes dos próprios registros comparados. Campos escalares explícitos obrigatórios também são admissíveis se todos os vínculos forem testados. A API interna nova pode ser corrigida dentro dos dois arquivos; schemas públicos congelados não mudam. Captura de bytes, paths e releitura pertencem CP2/CP3; aqui só comparação pura de registros. Formatos e ids são comparados conforme o perfil mmCIF, sem recuperação por inspeção nova ou normalização silenciosa de identidade.

**MAJOR-B — fronteira:** policy_id identifica o payload restrito do §13; não acrescentar U/fontes/tempo ao algoritmo para “consertar” o hash. Esses campos derivados concordam com o plano por comparação de integridade/equivalência do registro. Timestamp original permanece; timestamp novo não justifica sobrescrita. O pure builder valida o objeto existente recebido; a validação dos bytes do arquivo e create-once real permanecem CP3.

## 5. Disposições dos sete MINORs independentes

| Item | Disposição | Correção e limite |
|---|---|---|
| MINOR-1 | Aceito | Recusar ordinais/atom_id duplicados; garantir cobertura de cada observação uma vez, vínculo inequívoco asym/entity e existência de cada asym selecionado em M. Não renumerar, escolher o primeiro ou aceitar seleção fantasma. |
| MINOR-2 | Aceito | Injetividade NFC de todos auth tokens usados na correspondência em M, incluindo água/ligante. Tokens literais idênticos em várias cadeias continuam múltiplas coincidências válidas; preservar identidade/hash fonte e não comparar namespaces não relacionados. |
| MINOR-3 | Aceito, delimitado | Enforce invariantes locais das decisões, sem implementar filtro DOM. omit/guard sem linhas/tags mantidas; ordinais não negativos, únicos/disjuntos; categoria canônica pertencente ao catálogo/famílias aprovadas; source_rows_key obrigatório quando há fonte. |
| MINOR-4 | Aceito | Pin do catálogo nos DTOs do perfil atual e testes de vinculação profile/algorithm/catalogue/engine/decisões. Não aceitar versões novas como produção válida para poder testar sensibilidade documental. |
| MINOR-5 | Aceito | Formato inadequado usa código de configuração do conjunto existente (INVALID_RECORD no caso de fonte incompatível), não UNSUPPORTED_PLATFORM de host. |
| MINOR-6 | Aceito | Validação explícita do conjunto de códigos, também com python -O. Sem assert como guarda de produção. |
| MINOR-7 | Aceito | Golden bytes/digests literais independentes para canonicalização e envelopes; igualdade/desigualdade apenas não basta. A matemática atual confere; corrigir a prova regressiva. |

**MINOR-3 — sem alterar schema para preencher informação inexistente:** CategoryDecision não transporta o DOM nem total de linhas. CP1 deve validar o que o DTO já representa; CP2 provará cobertura de todas as linhas/tag reais e o cálculo do source_rows_key. Havendo ordinais fonte, null é incoerente; fonte presente vazia também tem hash não nulo. Uma categoria opcional ausente pertence a unavailable_categories, não a uma decisão fictícia; geração sem fonte pode ter null. O teste “omit arrays vazios válido” deve continuar válido usando a identidade da fonte apropriada, sem sentinela all. Categorias das famílias _pdbx_validate_/_pdbx_nmr_/_em_ explicitamente permitidas não devem ser recusadas como desconhecidas por uma lista incompleta. A guarda pura de categoria/ação não autoriza implementação física do catálogo no CP1.

**MINOR-4/7 — perfis fixos e testes de identidade:** manter literais de perfil/engine correntes fechados. Para provar que um campo integra o hash, usar bytes/payloads documentais com variantes explicitamente não aceitas como execução do perfil; não burlar os DTOs em produção. Adicionar controles reais de rejeição para catálogo/engine divergentes. Não reclassificar hash documental como checksum de RAW real.

## 6. NOTES e preservação de limites

- NOTE-1 incorporada: vetor de conexões vazio e ausência dos records futuros continuam recorte CP1. Plano parcial não será persistido/reutilizado como plano final CP2; CP1 não materializa receptor.
- NOTE-2 incorporada: preservar strict/frozen/extra=forbid, Unicode válido, ordem engine→fontes→seleção, __cause__ quando aplicável e interrupções sem captura ampla. A correção não pode enfraquecer testes válidos para acomodar erro.
- NOTE-3 registrada para CP4: importação CLI preexistente com Gemmi não será corrigida nos dois arquivos do CP1. O gate futuro import/help sem opcionais continua obrigatório no seu escopo.

## 7. Plano de correção e autorização existente

Tarefa nova: `tasks/021-CHECKPOINT1-CORRECTIONS.json`, em sessão Claude implementador separada do revisor. Usa a autorização humana de CP1 registrada em `increments/021/16-checkpoint1-preparation/OWNER_CHECKPOINT1_IMPLEMENTATION_AUTHORIZATION.md` no snapshot `3cda329b0e19a972d9858e26b58052873655ac07`. Não há nova aprovação humana alegada: as correções de conformidade permanecem no mesmo CP1/branch/dois arquivos. A tarefa define nova pasta própria de relatório, preservando a entrega original.

Código continua na mesma branch a partir de 711f307, por commits aditivos normais. Baseline científica é 08b797e; não recomeçar nem reescrever o commit original. Allowlist permanece receptor_materialization.py e test_receptor_materialization.py. Não tocar parsing/inspection/resolution/CLI/pyproject nem implementar native adapter, storage, registry ou service. Novos testes/parametrizações são permitidos no arquivo já autorizado e sua contagem real precisa ser reconciliada; 43 é a quantidade de cenários CP1, não teto artificial de coleta.

Antes/depois: registrar coleta, executar testes do arquivo novo e suíte completa com dependências reais já disponíveis; comandos precisos/ambiente/saídas/5 skips nominados; git diff --check; diff 711f307..HEAD e baseline..HEAD; hashes LF dos blobs commitados. Processo de import sem opcionais e códigos sob -O precisam ser provas reais, sem sentinela. Se faltar dependência/ambiente, declarar e não inventar sucesso. Instalações globais não autorizadas. Não exigir Windows para provar apenas domínio puro; não chamar Linux de validação Windows de publicação.

Relatório novo do implementador: `increments/021/21-checkpoint1-corrections/CLAUDE_INCREMENT_021_CHECKPOINT1_CORRECTIONS_REPORT.md` e `evidence/claude-*`, em branch própria do governance baseada no snapshot de publicação desta reconciliação. Somente o arquiteto atualiza coordenação central. Sem disparo automático. Depois de receber código/relatório reais, o arquiteto preparará revisão focal independente com hashes exatos; não há snapshot de correção antecipadamente inventado nem parecer já fechado.

## 8. Fontes primárias e questões pendentes

[Implementação confrontada](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/711f3070765efe67a5799f939f1a18306ed8afdd/src/molecular/receptor_materialization.py), [testes confrontados](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/711f3070765efe67a5799f939f1a18306ed8afdd/tests/test_receptor_materialization.py), [contrato congelado](https://github.com/sysoutemanuelhenrique/molecular-platform-governance/blob/b0e60f6528f6fcb828aa6dd5577824e08c7c9fac/increments/021/15-final-specification/INCREMENT_021_FINAL_SPECIFICATION.md), [helper 020](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/src/molecular/receptor_inspection.py) e [backend canônico antigo](https://github.com/sysoutemanuelhenrique/molecular-platform/blob/08b797e0985e123ffd4d7ca7e5a5e8f040e63851/src/molecular/promotion.py). Fonte primária desta reconciliação é o código/contrato/outputs pinados; não foram necessárias alegações externas sobre capacidades nativas novas.

Não há decisão científica nova pendente do responsável para corrigir esses pontos; não foi proposta troca de escopo/engine/schema. Permanecem pendentes: implementação das correções pelo ator autorizado, evidência real, revisão focal independente e decisão de aprovação do CP1. Toda ambiguidade contratual nova deve retornar ao arquiteto, sem escolha silenciosa. O 020-A permanece STAND-BY.

ARCHITECT RECONCILIATION COMPLETE: YES
INDEPENDENT CHECKPOINT1 REVIEW RECEIVED: YES
FINDINGS INDEPENDENTLY CLOSED AFTER CORRECTION: NO
CHECKPOINT1 APPROVED: NO
CHECKPOINT2 IMPLEMENTATION AUTHORIZED: NO
FINAL SPECIFICATION FROZEN: YES
CODE REPOSITORY MODIFIED BY ARCHITECT: NO
AUTOMATED DISPATCH: NO
