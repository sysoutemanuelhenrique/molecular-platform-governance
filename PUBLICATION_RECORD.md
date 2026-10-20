# Carga inicial pública — plano e registro de preparação

Emanuel decidiu em20/10/2026 manter este governance público. A inicialização documental está autorizada no contexto da comunicação entre agentes; não há autorização de implementação ou mudança da visibilidade do código.

Carga preparada a partir do bootstrap anterior. Os documentos científicos, parecer original, dados de evidência e pacotes de contexto mantêm seus bytes e hashes. Apenas os arquivos de coordenação foram adaptados à decisão pública. O bootstrap privado anteriormente preparado permanece preservado separadamente, sem sobrescrita.

A checagem local examinou22arquivos da carga anterior e seus ZIPs recursivamente:133entradas,3arquivos ZIP e cerca de2,8milhões de caracteres de texto. Não foram encontrados os padrões procurados de tokens GitHub/API/AWS, cabeçalho de chave privada, URL com credencial, endereço de email ou filename comum de segredo. Isso é verificação limitada por padrões; não é garantia universal nem auditoria do histórico do repositório de código. Não executar scripts do pacote durante a publicação.

Procedimento de inicialização: confirmar repositório público e sem refs; criar README inicial; publicar a árvore documental restante em commit filho; atualizar main documental por fast-forward sem force; ler snapshot publicado e verificar arquivos/hashes. Se surgir conteúdo remoto, interromper para reconciliação. O SHA final deve ser informado no comando de entrada do revisor, sem hash autorreferente nos próprios arquivos.

Esta carga não contém workflow, segredo, instalação de integração ou automação ativa. Não altera o repositório de código. O revisor ainda precisa comprovar acesso autenticado para publicar seu parecer em branch própria. PR/merge e aprovação formal não decorrem da permissão de publicar um arquivo de parecer.

## Resultado da tentativa

A criação inicial de README.md pela API conectada foi recusada com HTTP403, Resource not accessible by integration. A checagem posterior de refs retornou HTTP409, Git Repository is empty. Nenhum arquivo, branch ou commit foi publicado. Não se tentou contornar a restrição por outro endpoint ou credencial. A carga permanece preparada, aguardando um canal de escrita autorizado.

## Retomada com ambiente e acessos recuperados

A escrita do arquiteto foi demonstrada no commit inicial a47183dfec8213c765ed43ae482c8c227760a3d5. A escrita do Claude foi demonstrada e lida independentemente no commit befdc444fe015286b1508b60c107c7e9f5c23dd3. O bloqueio403 anterior é histórico.

Com o ambiente de execução recuperado, o arquiteto prepara a publicação da carga diretamente em docs/020-a-candidate1-review-20261020, partindo da main documental a47183dfec8213c765ed43ae482c8c227760a3d5. A branch do Claude e a main do governance não serão movidas por essa publicação. Originais científicos/pareceres e pacotes históricos permanecem byte-idênticos; apenas o protocolo operacional foi atualizado para refletir fatos observados. O resultado remoto e o SHA final são confirmados fora deste arquivo após atualizar a ref da branch própria.
