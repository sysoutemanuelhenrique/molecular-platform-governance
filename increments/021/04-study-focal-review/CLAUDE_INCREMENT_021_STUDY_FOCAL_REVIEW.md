# Revisão focal — reconciliação do estudo do Incremento 021

Tarefa: `021-STUDY-FOCAL-REVIEW`. Papel: Claude, revisor independente, separado do implementador. Data: 23/11/2026, America/Sao_Paulo.

Escopo: só a resposta arquitetural (`d5580b1`) e suas consequências sob as escolhas D-01(b) e D-02 aprovadas. Não é revisão integral repetida, não retoma o 020-A, não congela contrato e não autoriza implementação.

**Resultado: o estudo, com a reconciliação e as escolhas aprovadas, está pronto para a fase de rascunho.** Fecho 11 dos 15 itens originais. MAJOR-1, MAJOR-2, MAJOR-3 e MINOR-3 ficam parcialmente resolvidos, com cinco pendências concretas (P-1 a P-5, §5) que o rascunho deve fechar. Não há BLOCKER.

## 1. Gates e identidades

- Branch de coordenação: HEAD remoto `771d1aa2e6218188113aad4e54849c103219a25c` antes do trabalho, igual ao snapshot despachado. Pai imediato é `d5580b16…`.
- Código: `main` remoto `08b797e0985e123ffd4d7ca7e5a5e8f040e63851`.
- Parecer original: `claude/021-study-review-v2-20261123` em `debeba6f…`, inalterado.
- Manifesto atual (`dispatch-20261123/FILE_IDENTITIES.json`): STATUS 46/3.980/`30d13cbb…`; aprovação 47/3.446/`8b5cc011…`; tarefa focal 119/6.790/`7bf41072…`; tarefa de reconciliação 115/6.127/`d8e5036c…`. Todos conferem.
- Manifesto histórico da reconciliação: conferido **no commit `d5580b16…`**, como a tarefa exige. Os 9 itens conferem ali, incluindo STATUS e tarefas antigos. Não os comparei às versões atuais.
- Reconciliação (266/37.217/`77b677fb…`) e as cinco evidências da tarefa: idênticas às identidades declaradas.
- Blobs Gemmi citados (`src/mmcif.cpp` `1da0854c…`; `tests/5i55.cif` `c75212ea…`, SHA-256 `cae93774…`): conferem.

**Aprovação do responsável.** Li o registro `OWNER_SCOPE_DECISIONS_D01_D02_20261123.md`. Ele cita a mensagem literal, a reconciliação exata por commit e hash, e limita a aprovação a D-01(b) e a D-02 com alcance amplo explícito e auditado no modelo fonte escolhido, sem inferir pertencimento biológico. É coerente com o comando que recebi. Tratei as duas escolhas como entrada e não as reabri por preferência.

## 2. Execução própria e evidência fornecida

**Próprio:**
- conferência de refs, blobs e hashes (incluindo o manifesto histórico no commit pinado);
- releitura dirigida do código em `08b797e` (campos de id, validador `policy_selection_id`, mapeamento de categoria de conexão, `registry._load_input`, `atomic.py:868,966`);
- **reprodução da sonda de namespace do arquiteto**, executada de scratch externo com `python3 -I`. Saída byte-idêntica à fornecida (`1cefea88…`).

**Fornecido e não reexecutado:** consultas web ao dicionário wwPDB feitas pelo arquiteto (não tive acesso web; aceito a enumeração de `conn_type` como evidência dele).

**Não houve:** pytest, Gemmi em Python, Windows, concorrência ou nova sonda C++.

## 3. Disposição por achado

| Achado | Disposição | Base |
|---|---|---|
| MAJOR-1 | **Parcialmente resolvido** | (b) aprovada. Lista covalente fechada (sem regex), recusa de corte covalente e exceção condicionada estão corretas. Usar o `conn_type` literal é necessário: confirmei que o 020 classifica como `covalent` tudo que não é `disulf`/`metalc`, inclusive `hydrog`. Resta P-1. |
| MAJOR-2 | **Parcialmente resolvido** | A tabela de precedência é coerente com o código e com D-02. Resta P-2 (mecanismo do "explícito") e P-3 (unidade não polimérica). |
| MAJOR-3 | **Parcialmente resolvido** | Fechados: leitura do RAW pelo DOM, colunas canônicas, nulos ≠ wildcard, `pdbx_ptnr3_*` só nulo, avaliação no modelo M. Simetria com pendência P-4. |
| MAJOR-4 | **Fechado** | Campos reais conferidos: `ProteinInput.id`, `inspection_id`, `ReceptorSelectionPolicy.selection_id`, `resolved_selection_id`/`policy_selection_id` (igualdade já imposta por validador), `protein_input_id`. O regex de id aceita maiúsculas, então a comparação exata é necessária. O leitor próprio com captura única + hash + validação schema 1.0 resolve a incoerência sem tocar o 020. Ver NOTE-F1. |
| MINOR-1 | Fechado | Recusa em cadeia mantida, inclusive terminal; exclusão conjunta quando a cadeia sai inteira. |
| MINOR-2 | Fechado | Branched tudo-ou-nada por modelo/asym, independente de `struct_conn`. |
| MINOR-3 | Parcialmente resolvido (esperado) | Famílias e critérios adequados; catálogo por tag é condição do writer e item de rascunho. |
| MINOR-4 | Fechado | Qualquer `parser-limitation` bloqueia; `full` não certifica completude. |
| MINOR-5 | Fechado como disposição | Enumeração individual fica para o rascunho. |
| NOTE-1/2/3 | Fechadas | NOTE-2 confere: `xb` e `os.link` existem só no helper de ligantes; registry 020 é check-then-write. |
| C-1 | Fechada | Errata limitada ao mecanismo de falso positivo de namespace, reproduzido por mim. Não fabrica estado histórico de wheel nem execução: declara a versão histórica não comprovada e preserva o JSON. |
| C-2 | Fechada | Aceito o refinamento: `5i55` prova a grafia, não frequência nem valor preenchido. A perda só ocorre quando há código de inserção informado. |
| C-3 | Fechada | A tabela usa `atom_site → struct_asym → entity.type`, não a lista `chains` do 020. |

## 4. Confronto com as escolhas aprovadas

**D-01(b) com parceiros inteiros.**

- *Parceiro não polimérico removido por D:* água por balde ou chave, metal, ligante por chave `(asym, ccd)`. A unidade "inteiro" é bem definida, porque a disposição é por chave e todos os altlocs são preservados ou removidos juntos. Os exemplos da §3/§10 (água removida/metal mantido; ligante removido inteiro → omite `metalc`, mas `covale` recusa) são corretos.
- *Parceiro polimérico:* o resíduo só sai como parte da cadeia inteira, porque remoção de resíduo é recusada. A integridade está garantida. A inconsistência está na *origem* da decisão (P-1).

**D-02 e projeção no modelo.**

- *Projeção:* a decisão vem do inventário sem `model_number` e é projetada sobre as ocorrências de M. Isso é correto, porque uma chave ausente em M não tem efeito e os outros modelos são excluídos.
- *Modelo:* recusar `pdbx_PDB_model_num` ausente, nulo, zero ou misturado é restrição de consumidor legítima, e necessária. O 020 converte ausente e 0 em 1 (`or 1`), então o consumidor precisa conferir RAW contra `resolved_model` e recusar a divergência.
- *Autor × pertencimento biológico:* resolvido. `auth_asym_id` é só comparado e reportado (coincide com retido, excluído, vários ou nenhum), sem atribuir propriedade.

## 5. Pendências técnicas para o rascunho

**P-1 (MAJOR-1) — o que conta como "decisão explícita".**

A tabela da §3 e o registro do responsável exigem que o parceiro saia "por decisão explícita suportada". A §4 define S como cadeia *listada*; a exclusão de uma cadeia polimérica decorre da sua *não* listagem. Mesmo assim, o exemplo da §4 aplica a exceção quando "B sai integralmente por seleção explícita". O rascunho deve declarar se a não seleção de uma cadeia polimérica conta como decisão explícita para a exceção `metalc`/`hydrog`.

- Se contar: auditar por linha. Isso inclui o caso de fitas de ácido nucleico, em que selecionar uma fita omite todas as pontes `hydrog` de pareamento com a outra.
- Se não contar: o metal mantido pelo balde e coordenado pela cadeia excluída volta a ser recusa.

**P-2 (MAJOR-2/D-02) — mecanismo do "reconhecimento explícito".**

A reconciliação define auditoria e enumeração das retenções fora de S, mas não um ato de reconhecimento. Para cumprir o "explícito" aprovado, o rascunho deve definir um campo da declaração (operação de declaração, Q-04) com estas propriedades:

- é exigido sempre que existirem retenções fora de S em M;
- fica vinculado ao conjunto enumerado (por exemplo, por hash da lista label_asym/entity/CCD/origem);
- recusa a execução se estiver ausente ou se o conjunto mudar.

Um aviso apenas informativo não satisfaz D-02.

**P-3 (MAJOR-2) — unidade não polimérica.**

As linhas não poliméricas operam por componente `(asym, ccd)`, mas S opera por asym. Só branched recebeu a regra de uniformidade. Um asym não polimérico com mais de uma chave (micro-heterogeneidade de ligante, por exemplo) poderia sair parcialmente. Recomendo exigir resultado uniforme por asym também para não polímeros no perfil mínimo, ou justificar a exceção.

**P-4 (MAJOR-3) — matriz de simetria incompleta e justificativa a corrigir.**

- *Justificativa:* recusar dois códigos iguais não identidade é aceitável como restrição conservadora do perfil. O argumento de que a igualdade "não demonstra que a representação contém os parceiros" está, porém, incorreto. Com o mesmo operador (uma isometria) aplicado aos dois endpoints, a relação entre os átomos do referencial fonte é a mesma. Os átomos estão em M sempre que os endpoints se resolvem nele. A recusa deve ser justificada por ausência de fixture e cautela, não por falta de suporte geométrico.
- *Linhas com os dois extremos retidos:* a expressão "conexão que afetará o recorte" deixa indefinido o tratamento de linhas cujos dois extremos são retidos e cuja simetria é distinta ou nula. O rascunho deve fechar a matriz extremos retidos {2, 1, 0} × simetria {identidade nos dois lados, iguais não identidade, distintas, nula em um, nula em ambos}, dizendo para cada célula se preserva literal, omite com auditoria ou recusa.
- *Identidade:* se o rascunho não presume que o índice 1 é identidade, precisa dizer como a identidade é estabelecida. Por exemplo, aceitar só `n_555` cujo operador `n` conste como `x,y,z` na lista de operadores da própria fonte, recusando o resto. Sem isso, toda linha `1_555` fica com estado indefinido.

**P-5 (MINOR-3)** — catálogo por tag, chave, filtro e teste. Já reconhecido pelo arquiteto como condição do writer.

**NOTE-F1 (MAJOR-4, não pendente).** Para que "mesma validação" seja literal, o leitor próprio deve decodificar os bytes como `read_text(encoding="utf-8")` + `yaml.safe_load` fazem no 020: UTF-8 estrito, com newline universal sem efeito semântico em YAML. A derivação de caminho também deve seguir `inputs/proteins/<id>.yaml` e os diretórios dos registries 020, sem alterar seus loaders.

## 6. Escopo aprovado × questões técnicas abertas

**Aprovado pelo responsável e não reaberto:**
- D-01(b): exceção auditada `metalc`/`hydrog` com parceiro inteiro; cortes covalentes recusados.
- D-02: alcance amplo no modelo fonte escolhido, explícito e auditado, sem inferência por `auth_asym_id`.

**Abertas tecnicamente:**
- P-1: definição de "decisão explícita".
- P-2: mecanismo do reconhecimento explícito.
- P-3: uniformidade não polimérica.
- P-4: matriz e critério de simetria.
- P-5: catálogo.

Nenhuma delas contradiz as escolhas aprovadas. Todas cabem no rascunho e o impedem de ser congelado até serem fechadas.

## 7. Prontidão

Somente a fase de rascunho: o estudo, a reconciliação e o registro de aprovação são base suficiente para iniciar o rascunho de especificação, desde que P-1 a P-5 sejam seções obrigatórias dele. Não há especificação final nem autorização de implementação.

READY FOR DRAFT SPECIFICATION: YES, with P-1–P-5 as mandatory draft items
INDEPENDENT FINDING CLOSURE: 11 closed / 4 partially resolved / 0 open without path
READY FOR IMPLEMENTATION: NO
FINAL SPECIFICATION FROZEN: NO
INCREMENT 020-A: STAND-BY
CODE REPOSITORY MODIFIED: NO
ARCHITECT DOCUMENTS MODIFIED: NO
