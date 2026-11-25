# Recebimento arquitetural da conclusão declarada — Incremento021 CP2

Codex arquiteto;25/11/2026;America/Sao_Paulo. Tarefa021-CHECKPOINT2-COMPLETION. Este é recebimento/triagem de contrato, não revisão independente nem aprovação. **A entrega avançou, mas CP2 ainda exige correções dentro da autorização original. Não está pronto para revisão independente final.**

## 1. Snapshot e escopo verificados

- Coordenação de entrada: `625e538a01335829ee3f29ebf0e04758aa8f5fab`; código: feature/increment-021-receptor-materialization@`5be1e443200cedddac0f97707963500a2edc6da6`, filho direto de60f9e0da5c67c3820747242a033db2f5d49b1817.
- Relatório próprio: claude/021-cp2-completion-report@`17e594d28e13f7b0214fbb25de21a8d410b3ba2d`; dois commits aditivos desde7cd8ab3. A branch de relatório não contém o adendo625e538 na sua ancestralidade, mas o cita como input lido. É registrado como procedência real; não se exige rebase/merge para reescrever a origem histórica.
- Main código:`08b797e0985e123ffd4d7ca7e5a5e8f040e63851`;main governance:`a47183dfec8213c765ed43ae482c8c227760a3d5`. Ambas consultadas diretamente e inalteradas. A coordenação ainda está no SHA esperado antes desta publicação.
- DiffCP1ea8dac9..5be1e44, parcial0d06ebd..5be1e44 e baseline08b797e..5be1e44:22 arquivos, somente os quatro arquivos permitidos mais18 fixtures/manifests sob a raiz autorizada. O último commit altera somente receptor_parsing.py e seu teste(+178/-27). Sem evidência de CP3/CLI/outro módulo no diff.
- Especificação e quatro anexos congelados: hashes locais recalculados e comparados aos blobs da árvore remota625e538, sem alteração. Contrato/pacote preservados. Os commits0d06ebd→b096af7→60f9e0d→5be1e44 foram confirmados no comparativo remoto.

## 2. O que foi observado e o que foi fornecido

Li integralmente o relatório de conclusão70f7a14 e o adendo17e594d, a tarefa/guardrails e os trechos efetivos de produção/teste referentes aos residuais.27 arquivos necessários de código,relatórios,manifests e coordenação foram conferidos em tamanho/SHA de blob Git; os cinco normativos foram conferidos separadamente. Os12 arquivosCIF não foram baixados nesta triagem; os manifests existem no código e o diff contém os originais/recortes. Não certifico a origem externa dos seus bytes.

Dois logs retornaram como texto Unicode pelo conector e estavam originalmente emCP1252. Reconstruí somente a cópia temporária quando a conversão reproduziu exatamente tamanho eSHA1 de blob publicados; a evidência registra o método. Isso não é divergência no log remoto nem edição de documento histórico.

No ambiente disponível(Python3.12.14/Pydantic2.13.4), executei sondas próprias em cópia temporária com fontes fixadas porSHA256 e dependências-base existentes. Gemmi/RDKit foram bloqueados por um finder real, sem stub. Não executei pytest, Gemmi nativo,Windows/NTFS,concorrência nem git diff--check num checkout completo. Não instalei nada. Os resultados de testes do implementador continuam evidência fornecida.

## 3. Melhorias comprovadas nesta triagem

- Importar domínio e adapter, num processo limpo, não tentou carregar Gemmi/RDKit. A primeira chamada parse_receptor_cif_dom021 tentou Gemmi e retornou ENGINE_UNAVAILABLE com o motor bloqueado. Mesma prova emPython normal e-O; não certifica uso nativo, pin instalado ou ausência de regressão completa020.
- O código usa o teto próprio021 de16MiB, e separa valores Gemmi-decodificados de tokens crus; o novo teste dedicado consta do diff. A validação Decimal pura aceita1.2e3(4) e recusa1.2(4)e3/1_000/NaN.
- O fechamento de parent_comp_id preservado não possui a dispensa geral anterior; o código verifica membros ausentes em_chem_comp. Não transformar recusas honestas5I55/1PFE em positivos artificiais.
- O verificador já recusa alteração de atom_id; isso preserva parte da correçãoC-03, sem resolver toda a verificação fechada.
- A matriz tem os79IDs normativos e todas as funções de teste referidas existem porAST. Isso comprova mapeamento, não prova integral dos resultados esperados.

## 4. Residuais concretos — três MAJORs e um MINOR de evidência

### R-CP2-01 — MAJOR/C-05: contexto e auditoria de posições especiais

O contrato§11/T021-158 exige resolver modelo,label ou auth/inserção ealtloc, recusar contexto inválido/ambíguo, contar linhas fonte/interseção retida/átomos retidos únicos e avisar somente quando há interseção. A função real_guard_special_position_row(l3821–3844) retorna imediatamente para qualquerlabel_asym_id não nulo. A sonda, inclusive pela função públicacompute_category_decisions, aceitouNO_SUCH_ASYM/seq999 e omitiu a anotação. Não há contagenspecial_positions nos resultadosCP2; o warning do planner(l1453–1454) depende apenas da presença da categoria. O próprio relatório§4.1.3 admite a contagem não implementada. Falta uma capacidade contratual, não um refinamento opcional nem uma exigência de persistênciaCP3.

Correção: resolver o contexto completo emM; calcular e transportar dados imutáveis suficientes para os três camposSpecialPositionSummary deSCHEMAS§8, sem publicarAuditRecord/bundle. Testar anotações sobrepostas, somente removidas, categoria vazia/ausente, outro modelo, inserção/altloc e ambiguidade, além da amostra real3DG1. Uma cadeia existente sozinha não prova o contexto da anotação.

### R-CP2-02 — MAJOR/C-05: coerência anisotrópica e família parcial

O contrato§11/T021-062 exige que os campos informados concordem com o átomo referido, e recusa uma famíliaU/B populada mas incompleta. O mapping real(l3656–3660) cobre sóatom/asym/comp label, omitindo por exemploseq,type_symbol,modelo,auth/altloc/inserção correspondentes quando presentes. A função pública do catálogo preservou id=a1 comlabel_seq=99, enquanto o átomo éseq1; o helper também aceitouO contraC. Além disso,_tensor_family_state considera a família ausente quando falta qualquer coluna:U[1][1] informado+demaisU ausentes+B completo foi aceito pelo helper real. Não é validação física de tensor; é integridade exigida pelo perfil.

Correção: mapping explícito das identidades suportadas/informadas, sem inventar campos ausentes, e estado de família que distinga ausência integral de preenchimento parcial, mesmo se o outro tensor estiver completo. PreservarU/B/esd/tokens sem conversão/normalização; acrescentar provas positivas e negativas, inclusive integraçãoGemmi real.

### R-CP2-03 — MAJOR/C-03: verificação fechada da saída

O helper_verify_output_reparse(l1524–1595) compara células esperadas, mas só percorre decisões conhecidas; a sonda adicionou uma categoriaunplanned aoDOM e foi aceita. A rejeição deatom_id alterado usa phase=plan, nãoverify. O contrato§18 e o critérioC-03 já exigem confronto independente de vetores,relações e saída efetiva; não se propõe um sanitizador/validadorCIF universal.

Correção: confrontar o universo completo de categorias/tags esperado,inclusive_entry/bloco,recusar categorias extras e identidades geradas divergentes, e manter as verificações de tokens/ordem/contagens/referências exigidas. INVALID_OUTPUT emphase=verify; não trocar os oráculos fonte/plano por uma comparação do writer consigo mesmo. Acrescentar mutações de saída sem mudar sua forma principal e teste nativo.

### R-CP2-04 — MINOR/C-07: identidades e reconciliação de evidência

O adendo§3 declara1729linhas/72413bytes/SHA17f428... para o parser e1383/59027/SHA c87aa9... para seu teste. As linhas conferem, mas os bytes/hashes não correspondem aos blobs finais verificados abaixo. O manifesto antigo identifica60f9e0d expressamente: é histórico,não manifesto final. Publicar novo manifesto/adendo,sem sobrescrever material anterior.

| Arquivo em5be1e44 | LinhasLF | Bytes | SHA256 observado |
|---|---:|---:|---|
| `src/molecular/receptor_materialization.py` | 4381 | 209266 | `3ec96abf14c05ce29e285d389e386a189b6b69f9244e307756003260ca8f9ba3` |
| `src/molecular/receptor_parsing.py` | 1729 | 70684 | `54abf400cb500dd18fc825d616c8faf22e637db7d1cdcec396329d06244471f7` |
| `tests/test_receptor_materialization.py` | 2787 | 146902 | `67104670202d4887bb2f76287448604c8d4a81fc7c3913ec80c3ef3e1c47a286` |
| `tests/test_receptor_parsing.py` | 1383 | 57644 | `625ac29a5bf395cdc91d360d990cf5212d79cc9e8ecd6dc0f2d3f4862ffd4ff5` |

O diff final adiciona exatamente três funções de teste não parametrizadas e não remove funções. Os logs anteriores dizem205focais e1650passed+5skipped=1655; o final informa208focais e1653+5=1658. A aritmética+3 é coerente; as frases antes206/1651 e+2 no adendo não são. Não apresento essa conta como execução minha. Cada nova execução deve ter seu próprio ambiente/comando/HEAD/log e cinco skips discriminados. Corrigir a matriz para refletir o comportamento efetivamente provado:79funções mapeadas não fechamR01–R03.

A prova nova de lineage compara categorias e contagens de linhas entre originais e recortes. É útil, mas uma contagem igual não prova conteúdo intocado: se afirmar que só foram feitas as remoções listadas, comparar também os tokens/conteúdo das categorias não removidas contra o original. Não se exige identidade de whitespace comRAW nem ampliação do catálogo.

## 5. Continuação e próximo gate

Mantém-se021-CHECKPOINT2-COMPLETION, dentro da autorização literal já registrada; o input agora é5be1e44, não0d06ebd. Não reiniciar,descartar diffs,rebasear,amendar ou forçar refs. CorrigirR01–R04 dentro dos mesmos quatro arquivos/raiz de fixtures e preservar92testesCP1/vetores/fechamentos/notas e regressão020. Relatório novo aditivo no glob35/evidence/claude-*; nova branch própria a partir do despacho documental,sem modificar os relatos históricos17e594d/9aa0762.

Executar foco/regressão020/suíte comGemmi0.7.5 real, mapear os79cenários às asserções exigidas e declarar pendências com honestidade. Sem alegar que estudo mais amplo autorizou redução doCP2: o responsável limitou a nova organização dos estudos aoIncremento022. O021 preserva contrato/checkpoints. Nenhuma nova funcionalidade ou móduloCP3 foi autorizado.

Após entrega consistente, o arquiteto fará recebimento e preparará a revisão independente final em sessão separada. Não acioneiClaude. Não há necessidade de nova autorização para completar os requisitosCP2 já autorizados. CP3 depende de outro gate e decisão própria.

## 6. Evidência e decisão

Sonda publicável:evidence/ARCHITECT_CP2_COMPLETION_PROBES.py, com resultados normais e-O; manifesto factual:evidence/ARCHITECT_CP2_COMPLETION_RECEIPT_VERIFICATION.json. Os contraexemplos usamDTOs documentais e funções reais,não parsingCIF nativo nem materialização completa. Não os confundir com fixtures públicas ou com testespytest. Não houve alteração no código,contrato,main,relatórios do implementador ou itens locais protegidos.

DELIVERY RECEIVED: YES
ARCHITECT RECEIPT COMPLETE: YES
INDEPENDENT CHECKPOINT APPROVAL: NO
BLOCKERS: 0
MAJORS: 3
MINORS: 1
READY FOR INDEPENDENT FINAL CP2 REVIEW: NO
CHECKPOINT2 APPROVED: NO
CHECKPOINT3 IMPLEMENTATION AUTHORIZED: NO
INCREMENT020A: STAND-BY
FINAL SPECIFICATION FROZEN: YES
CODE REPOSITORY MODIFIED: NO
AUTOMATED DISPATCH: NO
