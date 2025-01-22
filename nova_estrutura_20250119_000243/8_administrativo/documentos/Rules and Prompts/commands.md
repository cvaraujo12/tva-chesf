# Comandos do Agente de Escrita Contextualizada

## Comandos de Gestão de Fontes

### `adicionar nova fonte`
- **Dificuldade**: Média
- **Descrição**: Adiciona uma nova fonte bibliográfica ao sistema
- **Parâmetros**:
  - titulo: Título da fonte
  - autores: Lista de autores
  - data_publicacao: Data de publicação
  - palavras_chave: Palavras-chave
  - resumo: Resumo do conteúdo
  - localizacao_arquivo: Localização do arquivo
  - citacao: Citação formatada
  - link_fonte: Link para a fonte
  - anotacoes: Anotações sobre a fonte

### `listar fontes`
- **Dificuldade**: Fácil
- **Descrição**: Lista todas as fontes disponíveis
- **Parâmetros**:
  - tipo_lista: Tipo de listagem desejada

### `buscar fontes`
- **Dificuldade**: Fácil
- **Descrição**: Busca fontes por termo específico
- **Parâmetros**:
  - termo_busca: Termo para busca

### `resumir fonte`
- **Dificuldade**: Fácil
- **Descrição**: Cria um resumo de uma fonte específica
- **Parâmetros**:
  - nome_fonte: Nome da fonte a ser resumida

### `analisar fonte`
- **Dificuldade**: Média
- **Descrição**: Realiza análise detalhada de uma fonte
- **Parâmetros**:
  - nome_fonte: Nome da fonte a ser analisada

### `anexar fonte`
- **Dificuldade**: Fácil
- **Descrição**: Anexa uma fonte para uso em outras operações
- **Parâmetros**:
  - nome_fonte: Nome da fonte a ser anexada

## Comandos de Validação ABNT

### `validar citacoes`
- **Dificuldade**: Difícil
- **Descrição**: Valida citações conforme ABNT NBR 10520
- **Parâmetros**:
  - citation_style: Estilo de citação
  - document_type: Tipo de documento
  - fix_suggestions: Sugestões de correção

### `validar referencias cruzadas`
- **Dificuldade**: Difícil
- **Descrição**: Valida referências cruzadas no documento
- **Parâmetros**:
  - ref_types: Tipos de referências
  - validation_level: Nível de validação
  - fix_broken: Corrigir referências quebradas

### `validar elementos textuais`
- **Dificuldade**: Difícil
- **Descrição**: Valida elementos textuais conforme ABNT
- **Parâmetros**:
  - element_types: Tipos de elementos
  - document_section: Seção do documento
  - fix_suggestions: Sugestões de correção

### `validar elementos graficos`
- **Dificuldade**: Difícil
- **Descrição**: Valida elementos gráficos conforme ABNT
- **Parâmetros**:
  - element_types: Tipos de elementos
  - document_type: Tipo de documento
  - fix_suggestions: Sugestões de correção

### `validar abnt avancado`
- **Dificuldade**: Difícil
- **Descrição**: Realiza validação avançada de normas ABNT
- **Parâmetros**:
  - document_type: Tipo de documento
  - validation_level: Nível de validação
  - fix_suggestions: Sugestões de correção

## Comandos de Integração

### `sincronizar mendeley`
- **Dificuldade**: Difícil
- **Descrição**: Sincroniza referências com Mendeley
- **Parâmetros**:
  - api_key: Chave API do Mendeley
  - sync_options: Opções de sincronização
  - collection_id: ID da coleção

### `sincronizar zotero`
- **Dificuldade**: Difícil
- **Descrição**: Sincroniza referências com Zotero
- **Parâmetros**:
  - api_key: Chave API do Zotero
  - library_id: ID da biblioteca
  - sync_options: Opções de sincronização

### `sincronizar dados`
- **Dificuldade**: Média
- **Descrição**: Sincroniza dados locais e remotos
- **Parâmetros**:
  - sync_type: Tipo de sincronização
  - sync_rules: Regras de sincronização
  - backup_options: Opções de backup

## Comandos de Segurança

### `gerenciar credenciais`
- **Dificuldade**: Difícil
- **Descrição**: Gerencia credenciais de acesso
- **Parâmetros**:
  - credential_type: Tipo de credencial
  - action: Ação a ser realizada
  - credential_data: Dados da credencial
  - encryption_key: Chave de criptografia

## Comandos de Processamento

### `processar lote`
- **Dificuldade**: Difícil
- **Descrição**: Processa múltiplos arquivos em lote
- **Parâmetros**:
  - batch_files: Lista de arquivos
  - action_type: Tipo de ação
  - processing_options: Opções de processamento

### `exportar bibliografia`
- **Dificuldade**: Média
- **Descrição**: Exporta bibliografia em diferentes formatos
- **Parâmetros**:
  - export_style: Estilo de exportação
  - sort_criteria: Critérios de ordenação
  - export_format: Formato de exportação
  - include_annotations: Incluir anotações

### `importar referencias`
- **Dificuldade**: Média
- **Descrição**: Importa referências de diferentes fontes
- **Parâmetros**:
  - source_file: Arquivo fonte
  - import_format: Formato de importação
  - duplicate_handling: Tratamento de duplicatas

### `organizar referencias`
- **Dificuldade**: Média
- **Descrição**: Organiza referências por diferentes critérios
- **Parâmetros**:
  - organization_criteria: Critérios de organização
  - group_by: Agrupar por
  - sort_order: Ordem de classificação

## Comandos de Produção de Texto

### `produzir conclusao`
- **Dificuldade**: Média
- **Descrição**: Auxilia na produção de conclusões
- **Parâmetros**:
  - main_arguments: Argumentos principais
  - implications: Implicações
  - final_thoughts: Pensamentos finais
  - context_files: Arquivos de contexto

### `criar template`
- **Dificuldade**: Média
- **Descrição**: Cria templates de documentos
- **Parâmetros**:
  - template_type: Tipo de template
  - sections: Seções
  - formatting_rules: Regras de formatação

### `verificar plagio`
- **Dificuldade**: Difícil
- **Descrição**: Verifica similaridade com outras fontes
- **Parâmetros**:
  - text: Texto a ser verificado
  - min_similarity: Similaridade mínima
  - databases: Bases de dados para verificação
