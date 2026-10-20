# INCREMENTO 020-A — Resposta à revisão adversarial do draft1

Autor: Codex, arquiteto. Data: 20/10/2026. Natureza: reconciliação documental e evidência de pesquisa, para fechamento focal pelo Claude. Não é parecer independente sobre o próprio texto e não autoriza implementação.

## 1. Entradas e limite de autoridade

Parecer recebido: `Texto colado(20261020-160803).txt`, preservado integralmente como `prior/CLAUDE_DRAFT_REVIEW_ORIGINAL.txt`. Identidade dos bytes originais: **126 linhas; 20.981 bytes; SHA-256 f2215080d4dc091db31cf4c7583ab915918da382388058700e1a0b17e2e56a8b**. CRLF do original preservado na cópia; o nome de transporte não é uma nova autoria.

Draft1 confrontado: `INCREMENT_020_A_DRAFT_SPECIFICATION.md`, **542 linhas; 62.532 bytes; SHA-256 b0c8532282ac90cf41c9958b8af06ef3aea142777794af6b058e3ba558c6397d**. Original não alterado.

Contagem do parecer: 0 BLOCKERS, 0 MAJORS, 3 MINORS, 6 NOTES. Veredito recebido: avanço para candidata final condicionado às três correções. Não converter esse parecer em aprovação independente incondicional. Claude continua sendo o único revisor designado nesta etapa.

Candidata nova: `INCREMENT_020_A_FINAL_SPECIFICATION_CANDIDATE.md`, candidate1. **575 linhas; 70.346 bytes; SHA-256 123596d03947f89321e6e623e3f0e7a2b88f38de42cd510a59f31cfd16d67ad4**. Identidades complementares estão em `FILE_IDENTITIES.json`, sem hash circular desse manifesto dentro de si.

## 2. MINOR-1 — Superfícies de desenho e DTO

**Aceito e endereçado.** A linha compacta do draft1 permitia confundir três superfícies reais. A candidata §9 separa:

1. `MolDraw2DSVG`: construtor, dimensões e opcionais próprios de painel/FreeType;
2. `drawer.drawOptions()`: atribuição posterior de atributos de `MolDrawOptions`, incluindo a política de fonte;
3. `drawer.DrawMolecule(mol, legend="")`: chamada de renderização, após configurar o drawer.

A §11 registra blocos fechados `compute2d`, `prepare`, `drawer`, `draw_options`, `draw_molecule` e `svg_validation_profile`. Não mistura opções gráficas com kwargs do construtor. A fonte é identificada por política, nome e hash observado; o caminho absoluto interno de fontFile não integra o JSON público.

O probe executou as chamadas reais do construtor com seus kwargs suportados, as atribuições de opções e a chamada de DrawMolecule. Esse script de pesquisa não implementa o DTO ou o adaptador de produção.

## 3. MINOR-2 — Default versus desvio explícito

**Aceito e endereçado.** As tabelas §8/§9 agora distinguem parâmetros obrigatórios, parâmetros opcionais coincidentes com defaults, desvios deliberados e métodos sem kwargs fornecidos. A referência é o binding Python2026.03.6, não a classe C++ nem a documentação posterior.

Desvios explicitados, sem mudar os valores já selecionados no draft1:

- fórmula: separateIsotopes=True e abbreviateHIsotopes=False;
- TPSA e Crippen: force=True, distinguindo recálculo/cache de preparação química;
- coordenadas: forceRDKit=True;
- preparação gráfica: kekulize=False e addChiralHs=False;
- drawOptions: prepareMolsBeforeDrawing=False e includeMetadata=False;
- fontFile: asset explícito da instalação em vez da string vazia observada como default.

Strict continua seleção explícita do overload enum de rotatable bonds; não se afirma que o resultado diverge de Default no pin. Os defaults já declarados no parsing SDF/SMILES permanecem intactos. Nenhuma alteração de política científica foi feita.

## 4. MINOR-3 — Parâmetros omitidos e diferença real de versão

**Aceito quanto à lacuna; uma premissa do parecer exige correção de versão.**

`coordMap={}` e `bondLength=-1.0` existem no binding Python2026.03.6. A candidata fixa ambos explicitamente nos defaults e os registra no bloco `compute2d`. coordMap é objeto vazio fechado no DTO e mapa vazio novo na chamada; não admite ancoragem livre de usuário nem mapa mutável compartilhado.

**`usePathAngleExpansion` não existe na assinatura exposta do pin observado.** A docstring completa capturada em `evidence/draft-review-verification.json` termina em `useRingTemplates=False`. Uma chamada isolada com `usePathAngleExpansion=True` é recusada com `ArgumentError`, cuja mensagem e assinatura estão preservadas na mesma evidência.

O nome aparece na documentação primária atual, identificada como **RDKit2026.09.1**, em <https://www.rdkit.org/docs/source/rdkit.Chem.rdDepictor.html>. Isso explica a diferença com a consulta do revisor, que declarou não conseguir confirmar nela o pin. A evidência não estabelece em qual versão intermediária o parâmetro foi introduzido; nenhuma data de introdução é inferida.

Portanto, a candidata §9/§11 **proíbe passar ou declarar esse kwarg como efetivo no pin**. Não se instala outra versão, não se introduz fallback por tentativa/erro e não se aumenta o escopo para suportar duas APIs. Fixar um kwarg inexistente produziria incompatibilidade concreta; documentar sua ausência é a disposição adequada.

Pede-se ao revisor conferir os dados brutos, sem aceitar a correção apenas por autoridade do arquiteto. O site atual é fonte primária para2026.09.1; a docstring e a chamada real são evidência primária do binding instalado2026.03.6 usado no estudo.

## 5. Disposição das seis NOTES

| Item | Disposição |
|---|---|
| NOTE-1 — detecção de Windows11 | Pergunta preservada em §6. Fonte/API, distinção cliente/Server, critério de build e provas positivas/negativas devem constar do checkpoint2. Não se aprova agora um limiar universal da Microsoft nem se exige implementar leitores antes do contrato. |
| NOTE-2 — Descriptors.MolWt | §8 explica a escolha da API pública e o encaminhamento observado ao helper privado. Não se exige namespace único: GetFormalCharge já pertence a Chem e GetNumHeavyAtoms ao Mol. O helper privado não é autorizado ao adaptador novo. |
| NOTE-3 — canário aromático fundido | Incorporado a T-020A-051/§10.1: antraceno, SMILES fixado. A sonda Linux observou apenas M/L; mantém-se exigência de evidência Windows e fail-closed do validador futuro. Não se amplia a gramática SVG. |
| NOTE-4 — grafia de versão | Encerrada pelo próprio parecer; grafias de dependência e runtime continuam separadas. |
| NOTE-5 — vetor cafeína não executado pelo revisor | Limitação dele preservada. O arquiteto reproduziu os dez valores no pin, com RAW identificado por hash e tolerância1e-8. Isso adiciona evidência e não finge execução pelo revisor nem substitui T-020A-041 de produção. |
| NOTE-6 — confirmações positivas | Preservadas; a ressalva factual sobre usePathAngleExpansion não reabre A-01–A-14 ou C-01–C-03. |

## 6. Evidência nova executada independentemente pelo arquiteto

Ambiente: Python3.12.14; Linux; RDKit2026.03.6 já instalado. Nenhuma instalação de dependência foi feita nesta rodada. A sonda ficou fora do clone e usou RAWs do pacote anterior como entradas somente de leitura.

Comando relativo reproduzível no pacote, após disponibilizar o RDKit pinado por meio do ambiente local já autorizado:

```sh
python evidence/verify_draft_review.py --raw-root evidence-context/evidence/raw --output research-output.json
```

Antes desse comando, extrair `context/INCREMENT_020_A_V2_REVIEW_RESPONSE_PACKAGE.zip` na pasta `evidence-context`; a saída é arquivo de pesquisa escolhido pelo operador, fora do repositório de código. O script não instala pacote, faz download ou implementa funções da plataforma. Não exige manipular o ambiente global.

Resultados mecânicos:

- docstrings de coordenadas, construtor, preparação, DrawMolecule e descritores capturadas;
- defaults das opções de desenho capturados de objeto real;
- source Python de MolWt e assinatura interna observados;
- usePathAngleExpansion ausente da assinatura e recusado na chamada real;
- cinco comparações de desenho, antes/depois da explicitação de parâmetros: **5/5 byte-idênticas no mesmo ambiente**;
- dez valores de referência da cafeína: **todos coincidentes** com §17, sob a tolerância declarada;
- antraceno: fórmula C14H10, comandos de path observados L/M, dentro do conjunto M/L/Q;
- fonte Telex: 38.940 bytes, SHA-256 eeaa2d17d105b6b46e5368ecd990f5b19c50131ff922dbf79bfb9bb45c249871.

Não se executou pytest nesta rodada. Não há leitores, serviço, CLI, DTO ou validador SVG020-A de produção implementados. O probe não demonstra esses contratos nem o funcionamento Windows. Inspeção de XML confiável produzido localmente para contar comandos não é o parser de segurança que o contrato exige implementar.

## 7. Baseline, preservação e escopo

`main` remota reconfirmada por `git ls-remote` e consulta autenticada ao commit da ref main: **08b797e0985e123ffd4d7ca7e5a5e8f040e63851**. Clone local no mesmo SHA; `git status --porcelain=v1` vazio; `git diff --check` sem saída/exit0. Nenhum arquivo do clone foi editado.

Diff documental draft1→candidate1 limitado a: identificação/histórico de etapa; resposta às tabelas §8/§9/§11; pergunta Windows preservada em §6; canário em §10.1/T-020A-051; registro de evidência em §17; critérios/pedido de fechamento/estado documental em §§19/21/22. O diff integral está em `changes/draft1-to-candidate1.diff`.

Continuam **22 seções e 80 cenários únicos** T-020A-001–080. Nenhum cenário foi removido/renumerado; T-020A-051 recebeu o canário e a verificação das superfícies. Isso não é contagem de funções ou itens pytest. A allowlist de dez caminhos da §18 foi preservada integralmente.

Arquitetura, valores científicos selecionados, parsing, gramática SVG, limites, taxonomia de falhas, CLI, exclusões, ausência de persistência e três checkpoints permanecem. Não se alega prova de toda regressão por uma comparação de arquivos; as execuções futuras continuam exigidas pelo contrato.

O repositório `sysoutemanuelhenrique/molecular-platform-governance` foi consultado sem escrita e continua **público**. Não se publicou material, alterou visibilidade, criou branch/PR ou ativou automação. A preparação da comunicação entre agentes é trabalho separado; não faz parte da allowlist020-A nem concede autorização científica.

## 8. Próximo gate e comando focal ao revisor

Enviar este pacote ao Claude revisor para **fechamento das três correções**, não repetição da revisão integral e não implementação. O pedido exato está em `00_START_HERE.md` e §21 da candidata.

Após fechamento independente, apresentar a identidade exata da candidata ao responsável para decisão explícita de aprovação/congelamento. Não congelar automaticamente por esta resposta. A autorização de implementação deve indicar especificação final identificada e checkpoint autorizado; o desejo de automatizar o processo não substitui esse gate.

## 9. Estado desta resposta

DRAFT REVIEW RESPONSE COMPLETE: YES
ORIGINAL DRAFT PRESERVED: YES
ORIGINAL REVIEW PRESERVED: YES
MINOR-1 ADDRESSED BY ARCHITECT: YES
MINOR-2 ADDRESSED BY ARCHITECT: YES
MINOR-3 ADDRESSED WITH PINNED-API CORRECTION: YES
REVIEWER INDEPENDENT CLOSURE OF CORRECTIONS: PENDING
FINAL CANDIDATE PREPARED: YES
READY FOR FINAL CANDIDATE CLOSURE REVIEW: YES
READY FOR IMPLEMENTATION: NO
FINAL SPECIFICATION FROZEN: NO
WINDOWS PRODUCTION READERS VALIDATED: NO
CODE OR TESTS IMPLEMENTED: NO — bounded research probe only
REPOSITORY MODIFIED: NO
IMPLEMENTATION AUTHORIZED: NO
