# Reconciliação arquitetural da revisão independente — Incremento 021 CP2

Codex arquiteto;25/11/2026,America/Sao_Paulo. Parecer recebido: **REQUEST CHANGES —0BLOCKERS,7MAJORS,6MINORS,4NOTES**. O resultado permanece. Esta resposta não fecha achados independentemente e não aprovaCP2/CP3.

## 1. Snapshot, identidades e autoridade

Coordenação:`c9e02f0290cd522c8b94b0ade3998ca59976b048`; código feature/increment-021-receptor-materialization:`a807b03f44089eb3cbacc14f871b63689a21aec9`; parecer claude/021-cp2-adversarial-review-20261125:`85c605e04ae61b2dad39f7d65d4531db860f71d4`. Main código:`08b797e0985e123ffd4d7ca7e5a5e8f040e63851`;main governance:`a47183dfec8213c765ed43ae482c8c227760a3d5`. Todos consultados no remoto e idênticos antes desta reconciliação.

Li o parecer integral, a matriz79, o log nativo completo, o registro de execução e as sondas pertinentes. Conferi21blobs da pasta40 contra árvore Git (bytes/SHA1) e os20outputs do manifesto contra linhas/bytes/SHA256/GitSHA. São20saídas mais o próprio manifesto, não20arquivos totais; isso explica a contagem da mensagem, sem criar impedimento. Os21arquivos e parecer ficam preservados.

Código/contrato usados são os mesmos snapshots da tarefa39. Os cinco normativos e o pacote permanecem congelados; a correção cabe na allowlistCP2 de quatro fontes/testes e raiz de fixtures. Nenhuma preferência arquitetural será transformada em requisito novo.

## 2. Evidência observada versus fornecida

O revisor executou Gemmi0.7.5nativo/Linux e214focais,121de regressão020 e controles em trêsSHAs. Seus67fails ambientais não são regressões, pois reproduzem na baseline/CP1. A conta1569+95=1664 é coerente; não substitui1659passed/5skipped do Windows. Os64COVERED/15PARTIAL/0GAP são classificação independente recebida, não execução minha nem aprovação.

Aqui executei funções reais puras/importações em cópia externa pinada a807b03, Python3.12.14/Pydantic2.13.4, normal e-O, sem Gemmi/RDKit/pytest e sem instalação. Corroborei aceitação de coordenada de visão decodificada apesar de token cru citado/carga inválida, recollapse de literal?em simetria, duplicataCCD, fonte_entry sem guarda/auditoria, endpoint6/7indistinguível e altlocinexistente→zero. A guarda pré-parse aceita save_ indentado/maiúsculo; sua aceitação nativa é prova do revisor, não desta sonda. Não tenho acesso ao checkoutWindows do responsável.

## 3. Ressalvas factuais e interpretação, sem alterar o contrato

**Inteiros:** o§6 exige inteiro decimal não citado e modelo positivo; não exige grafia canônica sem sinal/zeros iniciais. As páginas oficiais wwPDB de [model_num](https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_atom_site.pdbx_PDB_model_num.html) e [formal_charge](https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_atom_site.pdbx_formal_charge.html) declaram tipo int com regex `[+-]?[0-9]+`, consultadas em25/11. Portanto+1/01não são erros apenas por sua escrita; devem ser controles positivos quando representamM=1. Isso não autoriza números citados, non-ASCII, floats oucargascalculadas. Não importar a faixa química do dicionário, pois não está no contrato021. Não generalizar essa interpretação a IDs/operadores:01_555e ids1/01 de tabela de simetria continuam sujeitos à grafia/igualdade textual exata do§10.1.

Consequência: MAJOR-2 é aceito quanto aos números citados/validação de carga/gramática crua, mas contestado no subexemplo+1. MINOR-5 é aceito quanto a contexto/altloc inválido;01não deve ser simplesmente recusado por grafia. A comparação textual str(model) que perde correspondência numérica precisa ser corrigida. Essa disposição interpretativa será confrontada no fechamento focal pelo revisor, não registrada como concordância dele.

**Gemmi:** conferi no pin5cc1c23 os arquivos cif.hpp e python/cif.cpp contra sua árvore Git. A gramática do keyword save_ usa comparação case-insensitive; o binding expõeItem.frame. É viável recusar frames pelo DOM nativo antes da enumeração de categorias, sem criar um parser próprio.

**NOTE-2/inventário:** o log p_real registra5I55original60/derivado57;1PFE76/73;3DG155/50. A prosa NOTE-2 usa57/73/50 como se fossem downloadsoriginais: são os números dos derivados no próprio log. Registar origem/versão/filelabel corretamente; não fazer código/dados baterem artificialmente com inventário antigo. Os dois falsos positivos já reconhecidos pelo revisor (duplicação de operador e expressãoCIFmalformada) não geram correção de produção.

## 4. Disposição individual

| Achado | Disposição arquitetural | Objeto |
|---|---|---|
| MAJOR-1 | ACCEPTED | Save-frame detection |
| MAJOR-2 | PARTIALLY_ACCEPTED | Raw numeric grammar and integer fields |
| MAJOR-3 | ACCEPTED | Quoted-null symmetry identity |
| MAJOR-4 | ACCEPTED | chem_comp and source entry guards/audit |
| MAJOR-5 | ACCEPTED | Branched compound references |
| MAJOR-6 | ACCEPTED | Indistinguishable occurrences/endpoints |
| MAJOR-7 | ACCEPTED | 021 error taxonomy/cause at public adapter boundary |
| MINOR-1 | ACCEPTED | Canonical output tag ordering |
| MINOR-2 | ACCEPTED | Real four-document snapshot identities in integrations |
| MINOR-3 | ACCEPTED | Permanent separate interruption tests |
| MINOR-4 | ACCEPTED | Permanent native IdentityBasis/hash oracles |
| MINOR-5 | PARTIALLY_ACCEPTED | Special-position invalid context vs zero overlap |
| MINOR-6 | ACCEPTED | Real-source NCS full-pipeline evidence |
| NOTE-1 | ACCEPTED_CARRIED | Deposited whitespace |
| NOTE-2 | ACCEPTED_WITH_FACTUAL_CLARIFICATION | Versioned fixture inventory/lineage |
| NOTE-3 | ACCEPTED_CARRIED_TO_CP3_GATE | Preflight/connection/catalogue error precedence |
| NOTE-4 | ACCEPTED_PRESERVE | Nonconventional identity operator conservatism |

### MAJOR-1 — ACCEPTED

**Objeto:** Save-frame detection. **Fundamento:** Frozen§6/11; actual regex is case/column-sensitive; peer native probes accept frames omitted by category enumeration. Pinned Gemmi grammar is case-insensitive and Python Item.frame exists.

**Solução concreta:** Inspect real Gemmi block items for frame content before category extraction (or equivalent supported native DOM operation). Refuse any frame, including indentation/case variants; no handmade CIF parser. Keep quoted/multiline save_ literals valid.

**Aceitação/prova:** Native end-to-end lower/uppercase/indented frames refuse with021typedparseerror andcause; genuine literal controls retain tokens. Do not merely broaden the regex and claim complete grammar coverage.

### MAJOR-2 — PARTIALLY_ACCEPTED

**Objeto:** Raw numeric grammar and integer fields. **Fundamento:** Quoted coordinates/occupancy/B/NCS/tensors and absent formal_charge validation violate§6. The isolated expectation that unquoted+1is invalid is not supported by frozenbody and contradicts officialint lexicaltype [+-]?[0-9]+.

**Solução concreta:** Validate true raw tokens before Gemmi dequoting: numeric regex+finiteDecimal; model_num unquotedASCIIdecimalinteger and >0; formal_charge null-real or signedASCIIdecimalinteger. Do not calculatecharges or impose dictionarycharge ranges not frozen. Preserve all written tokens.

**Aceitação/prova:** Refuse quoted/multiline numericstrings, malformeddecimal/su/exponent/underscores/non-ASCIIint/floatcharge; preserve validnull,zerooccupancy,signedfinitevalues. Keep+1and01as validunquotedinteger spellings for numericmodel context; no broader identifier normalization.

### MAJOR-3 — ACCEPTED

**Objeto:** Quoted-null symmetry identity. **Fundamento:** §10.1/T021-173 explicitly distinguish realnull from quoted?/.; actualresolver collapses already-decoded literals again.

**Solução concreta:** Maintain Optional semantics once at raw boundary or explicitraw/literaltype throughresolver. OnlyNone denotes realnull after decoding; literal?/. must remain malformed strings. Keep source rowrawtokens/hash distinct.

**Aceitação/prova:** Native K0quoted?/.→not-applicable/unsupported-discarded, realnull retainsone/both-null semantics; K>0refusals correct. Verify decision/payload/oracles without claiming crossRAWplanhash equality or ignoring unchangedRAWchecksum binding.

### MAJOR-4 — ACCEPTED

**Objeto:** chem_comp and source entry guards/audit. **Fundamento:** §11,SCHEMAS§4; sourcecode skips bothspecialcases before genericguards. Purecorroboration confirms duplicatechem_comp retained and sourceentryunknown tags/audit lost.

**Solução concreta:** Run correspondingcatalogue key/nonnull/unknown-tag/singleton checks before deferred/generatehandling. For source_entry, hash originalrow and cover it as replaced/omitted; transport originalentryid forprovenance. Generateddecision can carrysource_rows_key andomittedsourceordinal whilegenerated_tags=[id]; no invented source forabsententry.

**Aceitação/prova:** Refuse duplicate/nullchem_compkeys, malformed/unknown/duplicatedsourceentry. Presententry hasnon-nullsource_rows_key andsource-rowcoverage; absententrymayhaveNone. Originalentryprovenance andnewtbmpid/block remain distinct; outputverificationclosure remains intact.

### MAJOR-5 — ACCEPTED

**Objeto:** Branched compound references. **Fundamento:** §11 explicitly requires fullentity/num/comp keys; specificpolymerlogic exists but analogous branch logic ismissing. Reviewer native corruptlinks/list-schemeaccepted.

**Solução concreta:** Validate branchlist/entity/CCD, bothlinkendpoints and schemes withfullcompoundkeys; establish unambiguousretainedatom-occurrence mapping using supportedsourcecolumns. Do not invent branchnum fromauthseq,fillnull label_seq, choosefirstmatch or use numalone.

**Aceitação/prova:** Native wrongentity/num/comp andswappedlist-vs-scheme refuseINVALID_CIF; validwholebranch inclunobservedmonomers and declaredleavingatomwithoutcoordinates stays valid. UniformityP3 preserved; no graphrepair, chemistryinference or obligatoryabsentlinkfabrication.

### MAJOR-6 — ACCEPTED

**Objeto:** Indistinguishable occurrences/endpoints. **Fundamento:** §6/9/T021-157; pureproductionresolver returnsIDs6and7for duplicatewaterO withsameoccurrence+altloc; nativepeer reproduces acceptance.

**Solução concreta:** At newCP2source/resolver boundary reject repeated physicalidentity (model,occurrence,label_atom_id,altloc) and ambiguousoccurrences before buildingendpointsets. DistinctA/Baltlocs withinoneoccurrence remain valid; othermodels/insertions/CCDs remain distinct.

**Aceitação/prova:** Nativeduplicate-null-altloc andduplicatesame-altloc refuseINVALID_CIF/AMBIGUOUS_ENDPOINT as appropriate; endpoints never merge twoindistinguishable physicalatoms. Preserve T021-043/156, CP1tests and genuinevariations; no silentdeduplication/firstmatch.

### MAJOR-7 — ACCEPTED

**Objeto:** 021 error taxonomy/cause at public adapter boundary. **Fundamento:** §16/SCHEMASerrorfields/brief§5; peer actualproduction raises legacy/rawValueErrors withoutcode/phase. Reader020mustremainunchanged.

**Solução concreta:** Translate enumeratedraw/nativeparse/helper errors at the021public boundary into existingtyped021errors with correctphase and fromcause. Keep existing021typederrors andKI/SystemExit untouched; narrow catches only. Installedwrongversion→ENGINE_VERSION; sourceparsermetadata mismatch→IDENTITY_MISMATCH/ENGINE_VERSION as documented, never absentenginewhenpresent.

**Aceitação/prova:** Rawsize→ExecutionLIMIT_EXCEEDED/raw; compression/BOM/encoding→ExecutionINVALID_CIF/raw; malformedCIF/multipleblocks/frames/duplicate tags→ExecutionINVALID_CIF/parse; invalidatom/entitymapping→ExecutionINVALID_CIF/plan; outputerrorsremainINVALID_OUTPUT/verify. Causes preserved, no newcodes/CLIhandlers, no changeparse_receptor_raw020exceptions.

### MINOR-1 — ACCEPTED

**Objeto:** Canonical output tag ordering. **Fundamento:** §11andbriefrequirealphabeticalcategories ANDtags; currentwriterusescatalogue/sourcecolumnorder.

**Solução concreta:** Sort canonical tagkeys at serialization/outputconstruction withoutreordering survivingrows orrewritingtokens.

**Aceitação/prova:** Nativeoutputcategory/tagorder assertions anddeterministicbytes; scientificroworder/goldens/canonicalhashenvelopes preserved.

### MINOR-2 — ACCEPTED

**Objeto:** Real four-document snapshot identities in integrations. **Fundamento:** Brief§8/C04 explicitly require realdocumenthashes/sizes; currentnativefixturecontext uses1..4repeatedhex/size1.

**Solução concreta:** Build valid concrete020document bytefixtures/models in testsetup; hashactualUTF8/YAMLbytes and sizes, match IDs/RAW/parser relations. Theadapter receives capturedSourceContext, not newCP3readers; no actualproductionfilesystemcapture claimed.

**Aceitação/prova:** Integratedtests bind allfour actualdocuments+RAW; changedbyte/size alters/refuses expectedcontext. Unit-onlyDTOdocumentarygoldens may remainfixedliterals if clearly labelled; no fakecapture or runtimecalls to futureCP3service.

### MINOR-3 — ACCEPTED

**Objeto:** Permanent separate interruption tests. **Fundamento:** §20/brief§9; peer demonstratedcorrectbehavior in14class×boundaryprobes but repositoryproof absent.

**Solução concreta:** Add pytest cases for KI andSystemExit separately on seven realparse/planning/serialize/verifyboundaries; monkeypatch owningnamespace onlytoinjectfailure,nevertofabricatesuccess.

**Aceitação/prova:** Everycombination asserts sameexceptioninstance/SystemExitcode, no retry/reparse/persistence. Preserve correctbehavior; no broadBaseExceptionhandler added.

### MINOR-4 — ACCEPTED

**Objeto:** Permanent native IdentityBasis/hash oracles. **Fundamento:** §10.1/annex; nativepeerproved7pairs/hashseeds, repositoryusesfixedDTOcontext/repeatedsameconstruction.

**Solução concreta:** Add productionnativecases for7reachablepairs with genuinefixedRAWandfourdocumentidentities, literalindependentexpectedhashes anddifferentin-memorycategoryvisitorders/hashseeds. Keep2impossiblepairsrefused.

**Aceitação/prova:** Compare sameRAWbytes/context acrossvisits; do notchangeRAWrow/filebytes thenexpectsameplan_key (RAWchecksumisbound). Do notuseannexdocumentaryprojectionhashesasproductionplanhashes or deriveexpectedusingfunctionundertest.

### MINOR-5 — PARTIALLY_ACCEPTED

**Objeto:** Special-position invalid context vs zero overlap. **Fundamento:** Unknownaltloc/context mustnotbe silentlyzero; however01isnot malformedmerelybyspelling underfrozenintegersemantics/officialtype. Currentstr(model)comparison misclassifies anumericallymatchingmodel.

**Solução concreta:** Validate rawintegermodel token andcompareits numericvalue tosource/resolvedmodel whilepreservingtoken. Refuse genuinelyinvalid/unresolvablecontext/altloc; keep legitimateknownothermodel/removedcontexts withzero overlap. Do notadd canonical1-onlyinteger rule.

**Aceitação/prova:** 01/+1model1context matches asinteger; quoted/noninteger/nonpositive modelsrefuse. Nonexistentaltloc refuses; validothermodel/removedandcurrentoverlap/1-1-3controls preserved. Explain source-modelavailabilityratherthan assumingzerooverlapimpliesinvalidity.

### MINOR-6 — ACCEPTED

**Objeto:** Real-source NCS full-pipeline evidence. **Fundamento:** §23requiresNCSoutcome fromreal-sourceentry; 1A2Pfullpipeline fails earlieronsymmetry, so isolatedguardproof alone insufficient.

**Solução concreta:** Prefer a qualifiedrealdeposition whoseNCS reachesfull021entry. Alternatively useanexplicitNCS-isolationderivative ofpinned1A2P under§23lineageallowance: retain original/operatorbytes, enumerate everyremovedblockingconnection/category, testoriginalexpectednegative and labelderivativehonestly. No productionruleexemption orfabricatedoperators.

**Aceitação/prova:** RealNCSoperatorbytes reachfullmaterialize pipeline andproduce expectedNCSrefusal or auditablegiven/identityomission. Keep original1A2Pnegative/isolatedguardreference. Ifqualificationcannotbeproved, report preciseblocker; never labelaneditedfileintact or downgrade the case toanapprovedskip.

### NOTE-1 — ACCEPTED_CARRIED

**Objeto:** Deposited whitespace. **Fundamento:** Peerwhitespacewarnings exclusively12CIF originals/derivatives; originalscientificbytesmustremainpinned.

**Solução concreta:** Preserve alloriginalbytes; report source/testdiffchecks separately fromdepositiontrailingwhitespace.

**Aceitação/prova:** No RAWwhitespace rewrite forgreencheck; newsource/testpatches clean.

### NOTE-2 — ACCEPTED_WITH_FACTUAL_CLARIFICATION

**Objeto:** Versioned fixture inventory/lineage. **Fundamento:** Lineage/tokenidentity checkedbyreviewer. NOTE2prose calls57/73/50currentdownloads; nativep_reallog gives original60/76/55andtrimmed57/73/50for5I55/1PFE/3DG1 respectively.

**Solução concreta:** Keep exactfixtures/checksums and distinguish original,trimmedandhistoricalGemmiinventory. Do notchangefrozencataloguetoacceptnewdepositionmetadata.

**Aceitação/prova:** Newreport usesexplicitversion/filelabels,not conflatedcounts; legitimateUNSUPPORTED_CATEGORYand1PFEnegativepreserved.

### NOTE-3 — ACCEPTED_CARRIED_TO_CP3_GATE

**Objeto:** Preflight/connection/catalogue error precedence. **Fundamento:** Peerobserves1PFEoriginal COVALENT_CUTbeforecatalogue, no explicitCP2violation; §16statesvalidationstageorder.

**Solução concreta:** Preserve existingCP2orderunlessrequiredbyafix; carrydetailedserviceprecedence checktoCP3planning/review, withoutimplementingCP3now.

**Aceitação/prova:** Do notassertalloriginals failbyunknowncategory; reportactualfirsterror. FutureCP3requiresseparateauthorization.

### NOTE-4 — ACCEPTED_PRESERVE

**Objeto:** Nonconventional identity operator conservatism. **Fundamento:** 2_555operator2identityexpressionstillnonidentityunderthefrozenprofile, consistentwithmatrix.

**Solução concreta:** Preserve rule; do notgeneralizegeometricidentity equivalence orrelaxretained-image profile.

**Aceitação/prova:** Matrix15cellsandbasiscontrolsremainunchanged exceptspecificquotednullfix.

## 5. Orientações de implementação que evitam outra correção incompleta

- Validar tipos numéricos no token cru, decodificar identificadores pela API Gemmi e colapsar null real exatamente uma vez. Preservar grafia/token para escrita/hashes; interpretação numérica de model_num não autoriza renumerarIDs ou normalizar identificadores químicos.
- As guardas comuns também alcançam_chem_comp e_entry antes da lógica especial. A entrada original gera source_rows_key e cobertura de linha; a novaentrycontinua sótbmp_plan_key. O fato de a saída ter umaentryválida não prova integridade daentryfonte.
- Para branch, conferir chaves compostas e ligação coerente à ocorrência com dados fonte suficientes; label_seqnull não pode virar um número inventado. Não reconstruir grafo/leavingatom/coordenadas.
- Traduzir somente exceções conhecidas na fronteira021. Não mudar o leitor020, capturar Exception/BaseException genericamente, reembalar erros021já tipados ou perder a instância de KeyboardInterrupt/SystemExit.
- Testes permanentes devem executar produção; os scripts do revisor têm paths Linux de harness e precisam de adaptação externa documentada, nunca serem copiados cegamente como testes ou usados como sucesso constante. Ler antes de executar. O helper de manifesto Git já fornecido continua válido.
- As quatro fontes/testes e novas fixtures são a allowlist completa. Sem reader/storage/service/CLI, outro motor, protonação ou novo schema. Não tocar em fixturesRAWoriginais só para limpar whitespace.

## 6. Correções autorizadas e critério de entrega

Nova tarefa: tasks/021-CHECKPOINT2-REVIEW-CORRECTIONS.json. Mesma autorização humanaCP2registrada no commit399bbbc, mesma feature, entradaa807b03. Não é novo incremento/checkpoint nem exige nova aprovação para consertar esse escopo. Publicar código/testes/fixtures permitidos e relatório aditivo no globoriginal35/evidence/claude-*, em branch própria do governance a partir do novo despacho. O parecer40e todos os documentos históricos ficam intocados.

Executar foco após mudanças que o justifiquem; no fim, regressão020 e suíte completa uma vez, com Gemmi0.7.5real disponível. Relatar comandos, ambiente, erros/skips e coleta sem vender contagens antigas como atuais. Entregar disposição dos13achados de correção+4NOTES, matriz79atualizada (prioridade aos15parciais e controles dos64já comprovados), testes nativos por grupo, hashesGit de todaallowlist/fixtures e confirmação remota.

MINOR-6 é qualificação de dados/teste com engine real; não pesquisa arquitetural terceirizada. Como downloadsRCSBtestados neste ambiente não foram acessíveis pela ferramentaweb, não declaro uma novaentrada qualificada. O conjunto1A2Ppinado permite a alternativa de isolamento explicitamente rastreada acima sob§23, sem mascarar a recusa do original ou mudar regra de produção; o revisor deverá verificar se o caso derivado satisfaz a prova exigida.

Após entrega concreta, arquiteto faz recebimento e prepara revisão focal separada; sem acionamento automático. A revisão focal fecha os achados/ressalvas e verifica regressões, sem repetir decisões aprovadas por preferência. CP2 só será apresentado para sua decisão após esse gate; CP3depende de autorização futura.

## 7. Decisões e estado

Decisão nova exigida do responsável agora: **nenhuma**, pois o trabalho permanece na autorizaçãoCP2e no contrato congelado. Interpretação dos inteiros e suficiência da prova NCS devem receber fechamento independente; se surgir contradição contratual real que exija mudar o contrato, parar e trazer a decisão, sem implementar uma exceção.

RECONCILIATION COMPLETE: YES
REVIEW VERDICT PRESERVED: REQUEST CHANGES
REVIEW FINDING GROUPS: 7 MAJORS /6 MINORS /4 NOTES
IMPLEMENTATION CORRECTIONS WITHIN EXISTING CP2 AUTHORIZATION: YES
INDEPENDENT FINDINGS CLOSED BY ARCHITECT: NO
READY FOR OWNER CP2 DECISION: NO
CHECKPOINT2 APPROVED: NO
CHECKPOINT3 IMPLEMENTATION AUTHORIZED: NO
FINAL SPECIFICATION FROZEN: YES
INCREMENT020A: STAND-BY
CODE REPOSITORY MODIFIED: NO
AUTOMATED DISPATCH: NO
