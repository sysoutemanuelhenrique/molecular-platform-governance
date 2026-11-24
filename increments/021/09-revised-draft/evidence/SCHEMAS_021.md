# Schemas propostos — Incremento 021 draft-2

Anexo do rascunho, não código nem contrato congelado. Todos os objetos abaixo são fechados: campo desconhecido é erro. Campos sem indicação nullable são obrigatórios e não null. Nenhum número é aceito como string, nenhum bool como int e nenhum bytes como str. JSON/YAML pode representar tuplas como arrays; somente as posições de array declaradas são convertidas explicitamente em tupla, com elementos validados sem coerção. Não admitir set, generator ou string como array.

## 1. Tipos e serialização

- Hex64: str real de 64 caracteres [0-9a-f]; sem uppercase, espaços ou prefixos.
- Id020: str validada pelo validador existente e comparação interna exata; eligibility Windows é verificação de storage adicional, não outra identidade científica.
- NativeId: str decodificada CIF não vazia, preservando caixa; até 256 caracteres, sem controles C0/C1. Não é nome de arquivo. Colisões na correspondência NFC são recusadas.
- Token: str bruta do DOM CIF, inclusive quoting e marcadores, até o limite de célula. Ausência de coluna é null; '?' e '.' citados não viram null.
- Count/Ordinal: int real >=0; Model: int real >=1; bytes e tamanhos também Count. Sem float JSON.
- TimeUTC: str de data real no formato YYYY-MM-DDTHH:MM:SS.ffffffZ. Generated at pelo service, nunca interpretado como geometria experimental.
- Enum: str real de vocabulário fechado. Engine={name:'gemmi',version:'0.7.5'}. Profile/algorithm/schema dos records novos='1.0'.
- application_version/runtime_python: str não vazia, até 128 caracteres sem controles, obtida da distribuição/runtime observados; sem coerção nem Git SHA inventado.
- Arquivos JSON novos: UTF-8, objetos com chaves ordenadas, sem floats/NaN, separadores compactos e um LF final. O hash de payload usa a mesma forma, **sem** LF. YAML novo: safe_dump de primitivas validadas, sort_keys=true, Unicode preservado; integridade é dos bytes realmente gravados. Nenhuma serialização usa pickle ou tags YAML construtoras.

## 2. RecordSnapshot e SourceContext

RecordSnapshot={kind, id, sha256, size_bytes, schema_version}. kind é protein|inspection|selection|resolution; id Id020, exceto inspection Hex64; schema_version é null para ProteinInput (não possui esse campo), '1.0' nos demais. São obrigatórios exatamente quatro snapshots, em ordem protein/inspection/selection/resolution, sem repetir kind.

SourceContext={protein_input_id:Id020, selection_id:Id020, inspection_id:Hex64, model:Model, records:tuple[RecordSnapshot], raw_sha256:Hex64, raw_size_bytes:Count, raw_format:'mmcif', inspection_schema:'1.0', inspection_profile:'1.0', parser:Engine}.

Os ids dos snapshots, os campos de referência e os ids internos dos registros capturados devem concordar exatamente. SourceContext é uma representação do snapshot documental; não inclui raw_artifact.path como autoridade de saída nem altera os registros antigos. source_context_key é H desse objeto com envelope {kind:'receptor-materialization-sources',version:'1.0',sources:SourceContext}.

## 3. OccurrenceIdentity, XEntry e OutsideEntry

OccurrenceIdentity={model:Model, label_asym_id:NativeId, entity_id:NativeId, ccd:NativeId, label_seq_id:NativeId|null, auth_asym_id:NativeId|null, auth_seq_id:NativeId|null, insertion_token:Token|null}. Pelo menos label_seq_id ou auth_seq_id informado e contexto inequívoco são necessários. Occurrence key é H({kind:'receptor-materialization-occurrence',version:'1.0',identity:OccurrenceIdentity}).

XEntry={model:Model, label_asym_id:NativeId, entity_id:NativeId, atom_count:Count, atom_ids_key:Hex64}; representa um asym polymer inteiro excluído do complemento de S. atom_ids_key é hash envelopado do vetor [{ordinal:Ordinal,id:NativeId}] em ordem fonte. X não contém asyms de outro modelo.

OutsideEntry={identity:OccurrenceIdentity, occurrence_key:Hex64, decision_source:'disposition-keep'|'unaddressed-preserve', atom_count:Count, atom_ids_key:Hex64, author_id_coincidence:'retained-polymer'|'excluded-polymer'|'multiple'|'none'|'unavailable'}. A classificação multiple vale quando há mais de um asym polymer com o mesmo auth id, ou coincidências com retido e excluído; não implica ligação física. O descreve todas as ocorrências retidas de asyms fora de S, não um resumo por CCD. Coincidência é calculada em M.

X/O são ordenados conforme o corpo. As listas exatas alimentam os hashes; X vazio e O vazio têm hashes canônicos mesmo que os acknowledgements correspondentes devam ser null.

## 4. Decisões internas do plano

AtomDecision={ordinal:Ordinal, atom_id:NativeId, occurrence_key:Hex64, retained:bool, reason:AtomReason}. AtomReason=model-filter|selected-asym|disposition-keep|disposition-remove|unaddressed-preserve|chain-complement. Cobrir exatamente uma vez todo ordinal atom_site fonte; retained equivale à máscara e aos motivos válidos. chain-complement descreve o motivo estrutural proposto; os acknowledgements no record/audit comprovam separadamente que o cientista o reconheceu.

ConnectionDecision={ordinal:Ordinal, id:NativeId, row_key:Hex64, conn_type_token:Token, endpoint_atom_ids:tuple[tuple[NativeId],tuple[NativeId]],identity_basis:tuple[IdentityBasis,IdentityBasis], retained_endpoints:Count, symmetry_class:SymmetryClass, action:'preserve'|'omit', reason:ConnectionReason}. Cada conjunto endpoint_atom_ids é não vazio, sem ids repetidos e ordenado por ordinal fonte; seus membros pertencem à mesma ocorrência/label_atom_id e têm destino uniforme. retained_endpoints só 0/1/2, contando conjuntos, não variantes. IdentityBasis=pdbx-1_555-convention|source-operator|not-applicable; o último só em K=0 para contexto sem prova e sem referência preservada. SymmetryClass=both-identity|same-nonidentity|different|one-null|both-null|unsupported-discarded. unsupported-discarded só aparece em K=0; recusas não geram um plano aceito.

ConnectionReason=both-retained|both-removed|whole-partner-removed-metalc|whole-partner-removed-hydrog. A linha está no mesmo RAW/M e seus endpoints foram resolvidos antes; cannot match nunca é uma ação omit válida. row_key é hash envelopado do vetor ordenado tag/token fonte; os ids da conexão não são transformados em paths.

CategoryDecision={category:str canônica do catálogo, action:'filter'|'omit'|'generate'|'guard_then_omit', kept_row_ordinals:tuple[Ordinal], omitted_row_ordinals:tuple[Ordinal], preserved_tags:tuple[str], omitted_tags:tuple[str], generated_tags:tuple[str], source_rows_key:Hex64|null}. source_rows_key é null somente para categoria ausente/gerada sem fonte. Arrays de linhas não se sobrepõem e cobrem as linhas presentes; categorias ausentes opcionais entram em unavailable_categories do plano, não numa linha fictícia. Quando a categoria é omitida, nenhuma tag/linha sobrevive.

PlanBinding={kind:'receptor-materialization-plan',version:'1.0',profile:'1.0',algorithm:'1.0',catalogue_sha256:Hex64,engine:Engine,sources:SourceContext,source_context_key:Hex64,selected_asym_ids:tuple[NativeId],unaddressed_components:'preserve'|'require-disposition',exclusions:tuple[XEntry],outside:tuple[OutsideEntry],exclusions_key:Hex64,outside_key:Hex64,atom_decisions_key:Hex64,connection_decisions_key:Hex64,category_decisions_key:Hex64,unavailable_categories:tuple[str],warnings:tuple[WarningCode]}.

Cada decisions_key é H de {kind específico,version:'1.0',source_context_key,decisions:vetor completo na ordem definida}. O plano interno inclui PlanBinding e os três vetores completos de decisões, preservando bytes/DTOs suficientes para serializar sem reabrir RAW. plan_key=H(PlanBinding). Não há persistência pública obrigatória de preview nem campo de aprovação preenchido pelo planner.

Envelopes exatos dos demais hashes (H é a canonicalização do corpo):

| Hash | Payload exato |
|---|---|
| atom_ids_key | {kind:'receptor-materialization-atom-ids',version:'1.0',atoms:[{ordinal,id},...]} |
| exclusions_key | {kind:'receptor-materialization-exclusions',version:'1.0',source_context_key,model,entries:X} |
| outside_key | {kind:'receptor-materialization-outside',version:'1.0',source_context_key,model,entries:O} |
| atom_decisions_key | {kind:'receptor-materialization-atom-decisions',version:'1.0',source_context_key,decisions:AtomDecision[]} |
| connection_decisions_key | {kind:'receptor-materialization-connection-decisions',version:'1.0',source_context_key,decisions:ConnectionDecision[]} |
| category_decisions_key | {kind:'receptor-materialization-category-decisions',version:'1.0',source_context_key,decisions:CategoryDecision[]} |
| row_key | {kind:'receptor-materialization-source-row',version:'1.0',source_context_key,category,ordinal,tokens:[{tag,token},...]} |
| source_rows_key | {kind:'receptor-materialization-source-category',version:'1.0',source_context_key,category,rows:[row_key,...]} |

tokens ordena tags canônicas; rows e decisions seguem ordinal fonte/categoria canônica conforme o corpo. Nenhuma dessas chaves é identidade química universal. Exemplos de hash devem ser vetores documentais de teste, não resultado científico alegado.

WarningCode=all-altlocs-retained|outside-selected-asym-retained|declared-connections-unavailable|source-annotations-omitted|coordination-connections-omitted|hydrogen-bonds-omitted|source-symmetry-context-only|other-models-excluded|source-ncs-annotations-omitted|special-position-annotations-omitted. O vetor ordena códigos lexicalmente, sem repetição. Contagens e detalhes permanecem nos vetores estruturados, não em texto livre de exceção.

## 5. PreviewOutcome

PreviewOutcome={plan:PlanBinding,plan_key:Hex64,counts:Summary,commit_state:'not-published'}. Contém X/O completos e os hashes para reconhecimento; o service pode devolver o plano interno por canal privado ao declarante, mas a CLI não ganha objeto Gemmi. Serialização de preview limitada a 32 MiB; excesso é LIMIT_EXCEEDED, sem truncamento.

## 6. ReceptorMaterializationPolicy

PolicyRecord={kind:'receptor-materialization-policy',schema_version:'1.0',profile_version:'1.0',algorithm_version:'1.0',catalogue_sha256:Hex64,engine:Engine,policy_id:Hex64,sources:SourceContext,source_context_key:Hex64,plan_key:Hex64,unaddressed_components:'preserve'|'require-disposition',exclusions_key:Hex64,outside_key:Hex64,excluded_polymer_asym_count:Count,outside_occurrence_count:Count,acknowledge_plan_key:Hex64,acknowledge_exclusions_key:Hex64|null,acknowledge_outside_key:Hex64|null,declared_by:str,declared_at:TimeUTC}.

Validar: acknowledge_plan_key=plan_key; se excluded_polymer_asym_count>0, acknowledge_exclusions_key=exclusions_key, senão null; regra análoga para O. As contagens/keys vêm do plano calculado, mas os valores acknowledge vêm dos argumentos explícitos do cientista. Não copiar campos calculados como se fossem reconhecimento recebido. policy_id é calculado exclusivamente pelo payload declarado no corpo; o resto deve concordar com o plano e com as fontes capturadas.

PolicyOutcome={policy:PolicyRecord,reused:bool,commit_state:'published',relative_path:str controlada}. Reused mantém o record original e seu timestamp; verificar id semântico e integridade. O checksum dos bytes da policy é obtido pelo leitor e só entra no request/artifact, não no próprio policy_id.

## 7. Summary e payloads do manifesto

Summary={source_atom_count:Count,selected_model_atom_count:Count,retained_atom_count:Count,removed_atom_count:Count,retained_asym_count:Count,excluded_polymer_asym_count:Count,outside_occurrence_count:Count,source_connection_count:Count,preserved_connection_count:Count,omitted_connection_count:Count,omitted_metalc_count:Count,omitted_hydrog_count:Count,omitted_category_count:Count,omitted_tag_count:Count}.

source_atom_count=retained_atom_count+removed_atom_count. source_connection_count=preserved_connection_count+omitted_connection_count no modelo/contexto resolvido; arquivo com conexão não resolvível já recusou antes. Remoção de átomos de outros modelos integra removed_atom_count com motivo model-filter. Nenhuma contagem significa hidrogênios adicionados ou valência corrigida.

PayloadDescriptor={filename:str constante,sha256:Hex64,size_bytes:Count}. ManifestRecord={kind:'receptor-materialization-artifact',schema_version:'1.0',profile_version:'1.0',algorithm_version:'1.0',catalogue_sha256:Hex64,engine:Engine,application_version:str,runtime_python:str,artifact_id:Hex64,request_key:Hex64,policy_id:Hex64,policy_file_sha256:Hex64,sources:SourceContext,source_context_key:Hex64,plan_key:Hex64,structure:PayloadDescriptor,audit:PayloadDescriptor,summary:Summary,warnings:tuple[WarningCode],created_at:TimeUTC}.

artifact_id=request_key; structure.filename='receptor.cif'; audit.filename='audit.json'. Sem URL, caminho arbitrário, checksum de si mesmo ou estado em execução. Os três arquivos são a lista fechada do bundle. Não confundir presença de um manifesto ainda no work com commit: a localização final e a validação do bundle determinam publicação.

## 8. AuditRecord

AuditRecord={kind:'receptor-materialization-audit',schema_version:'1.0',profile_version:'1.0',catalogue_sha256:Hex64,plan_key:Hex64,source_context_key:Hex64,source_entry_id:Token|null,source_symmetry_only:bool,special_positions:SpecialPositionSummary,atoms:tuple[AtomDecision],occurrences:tuple[OccurrenceAudit],connections:tuple[ConnectionDecision],categories:tuple[CategoryDecision],unavailable_categories:tuple[str],exclusions:tuple[XEntry],outside:tuple[OutsideEntry],acknowledge_plan_key:Hex64,acknowledge_exclusions_key:Hex64|null,acknowledge_outside_key:Hex64|null,summary:Summary,warnings:tuple[WarningCode]}.

SpecialPositionSummary={source_annotation_count:Count,retained_annotation_count:Count,retained_unique_atom_count:Count}. Zero counts when category absent; counts are source-annotation matches, not a computed site multiplicity.

OccurrenceAudit={identity:OccurrenceIdentity,occurrence_key:Hex64,retained:bool,decision_source:AtomReason,atom_ids_key:Hex64,atom_count:Count}. Cobrir cada ocorrência em todos os modelos, com reason model-filter fora de M. As listas atoms e occurrences são auditáveis em relação ao mesmo RAW. Para o perfil de preservação de contexto, source_symmetry_only=true, ainda que a categoria de simetria esteja ausente (nenhuma nova simetria foi afirmada).

O audit não inclui UUID operacional, data de execução ou erro nativo livre; o manifesto liga os bytes da auditoria à requisição e ao timestamp. Vetores de linha/categoria removidos têm hashes e ordinais; valores completos dos metadados omitidos ficam no RAW, não são duplicados integralmente no JSON.

## 9. Outcomes e erros

ArtifactOutcome={manifest:ManifestRecord,reused:bool,commit_state:'published',structure_relative_path:str controlada,audit_relative_path:str controlada}. Readers show/show-policy devolvem os records íntegros, sem rerun, com esse mesmo vocabulário. O DTO não apresenta running como sucesso.

MaterializationErrorDetails={code:enum fechado da taxonomia do corpo,phase:'preflight'|'metadata'|'raw'|'parse'|'plan'|'acknowledgement'|'serialize'|'verify'|'reserve'|'publish'|'activity'|'presentation'|'cleanup',protein_input_id:Id020|null,selection_id:Id020|null,policy_id:Hex64|null,artifact_id:Hex64|null,committed:bool|null,unconfirmed_removals:tuple[str relativo controlado],secondary_activity_error:bool,source_row_ordinal:Ordinal|null}.

committed=true só se publicação confirmada; false só antes do commit comprovado; null para resultado indeterminado. O erro preserva original_error/cause em memória, sem serializá-lo nem imprimi-lo como texto. Falha de cleanup/log não troca a instância de KeyboardInterrupt/SystemExit. Os detalhes não são um registro universal persistido de ExecutionAttempt.

Draft-2: application_version não integra PlanBinding nem PolicyRecord. Continua obrigatório no ManifestRecord e payload request_key; profile/algorithm/catalogue/engine e hashes das decisões controlam a semântica do plano. As novas regras pertencem a um contrato ainda não congelado; manter versões propostas 1.0 não é migração de dado implementado.
