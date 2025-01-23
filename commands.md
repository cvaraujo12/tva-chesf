# Comandos do Sistema Integrado de Pesquisa e Produção Acadêmica

## Visão Geral
Este documento descreve os comandos disponíveis no Sistema Integrado de Pesquisa e Produção Acadêmica, que segue as regras definidas no arquivo .cursorrules. O sistema combina gestão documental, produção de conteúdo e validação acadêmica.

## Configuração do Sistema
- **Versão**: 2.0
- **Formato Padrão**: Markdown
- **Validação**: ABNT
- **Backup**: Automático
- **Controle de Versão**: Ativo

## 1. Comandos de Gestão de Fontes e Documentos

### /adicionar-fonte
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

### /update-resume
- **Descrição**: Atualiza o resumo geral de todas as fontes consultadas
- **Funcionalidades**:
  - Gera/atualiza arquivo `resumo_geral_pesquisa.md`
  - Incorpora novas fontes identificadas
  - Atualiza status de análises
  - Registra novas conexões descobertas
- **Uso**:
  ```bash
  /update-resume                    # Atualização básica
  /update-resume --full            # Atualização completa com metadados
  /update-resume --section=fontes  # Atualiza seção específica
  ```

### /buscar-fontes
- **Dificuldade**: Fácil
- **Descrição**: Busca fontes por termo específico
- **Parâmetros**:
  - termo_busca: Termo para busca
  - tipo_fonte: Tipo de fonte
  - periodo: Período de busca

## 2. Comandos de Validação e Qualidade

### /validar-citacoes
- **Dificuldade**: Difícil
- **Descrição**: Valida citações conforme ABNT NBR 10520
- **Parâmetros**:
  - citation_style: Estilo de citação
  - document_type: Tipo de documento
  - fix_suggestions: Sugestões de correção

### /check-consistency
- **Descrição**: Verifica consistência do conteúdo
- **Escopo**: Define o nível de análise (volume, capítulo ou seção)
- **Verificações**:
  - Cronologia
  - Referências cruzadas
  - Citações
  - Narrativa

### /quality-check
- **Verificações**:
  - Linguagem
  - Estrutura
  - Referências
  - Formatação
- **Saída**: Relatório detalhado com sugestões

### /validate-evidence
- **Dificuldade**: Alta
- **Descrição**: Valida evidências documentais conforme regras estabelecidas
- **Níveis de Validação**:
  - primary_source
  - secondary_source
  - cross_reference
  - contextual
- **Tipos de Conexão**:
  - direct
  - indirect
  - contextual
  - comparative
- **Saída**: Relatório de validação com ranking de prioridade

### /analyze-structure
- **Dificuldade**: Média
- **Componentes**:
  - contexto_historico
  - evidencia_documental
  - analise_critica
  - implicacoes
  - conclusoes
- **Elementos Obrigatórios**:
  - fonte_primaria
  - metodologia
  - argumentacao
  - conclusao

## 3. Comandos de Análise e Visualização

### /generate-timeline
- **Formatos**: Mermaid, markdown, visual
- **Funcionalidades**:
  - Ordenação automática por data
  - Detecção de lacunas temporais
  - Visualização interativa

### /semantic-analysis
- **Análises**:
  - Temas e padrões
  - Contextos
  - Relacionamentos
  - Tendências
- **Saída**: Relatório de insights e conexões

### /generate-visualization
- **Tipos**:
  - Redes
  - Linhas do tempo
  - Hierarquias
  - Conexões
- **Formatos**: Mermaid, DOT, SVG

### /research-automation
- **Dificuldade**: Alta
- **Bases de Dados**:
  - CIA_FOIA
  - NARA_Archives
  - Wilson_Center
  - Digital_Archives
- **Funcionalidades**:
  - Atualização diária
  - Alertas de novos documentos
  - Rastreamento de fontes

### /knowledge-management
- **Dificuldade**: Média
- **Categorização**:
  - militar
  - tecnico
  - diplomatico
  - estrategico
- **Funcionalidades**:
  - Rastreamento de relações
  - Visualização de conexões
  - Gestão taxonômica

## 4. Comandos de Integração

### /sincronizar-referencias
- **Dificuldade**: Difícil
- **Plataformas**:
  - Mendeley
  - Zotero
- **Parâmetros**:
  - api_key: Chave API
  - sync_options: Opções de sincronização
  - collection_id: ID da coleção

### /exportar-bibliografia
- **Formatos**:
  - PDF
  - Markdown
  - HTML
  - DOCX
- **Opções**:
  - Incluir anotações
  - Preservar metadados
  - Manter formatação

## 5. Comandos de Produção Textual

### /produzir-introducao
- **Dificuldade**: Média
- **Parâmetros**:
  - topic: Tópico
  - scope: Escopo
  - goal: Objetivo
  - context_files: Arquivos de contexto

### /produzir-conclusao
- **Dificuldade**: Média
- **Parâmetros**:
  - main_arguments: Argumentos principais
  - implications: Implicações
  - final_thoughts: Pensamentos finais
  - context_files: Arquivos de contexto

### /revisar-texto
- **Dificuldade**: Média
- **Verificações**:
  - Coesão textual
  - Fluidez argumentativa
  - Padronização
  - Formatação ABNT

## 6. Comandos de Segurança e Backup

### /gerenciar-credenciais
- **Dificuldade**: Difícil
- **Funcionalidades**:
  - Gerenciamento de acessos
  - Criptografia de dados
  - Backup de credenciais

### /track-revisions
- **Rastreamento**:
  - Mudanças
  - Versões
  - Conflitos
- **Backup**: Automático e manual

## 7. Comandos de Resumo e Atualização

### /auto-summary
- **Dificuldade**: Média
- **Arquivo de Saída**: resumo_geral_pesquisa.md
- **Seções**:
  - fontes_analisadas
  - fontes_pendentes
  - conexoes_estabelecidas
  - proximos_passos
  - recomendacoes
- **Campos Obrigatórios**:
  - status
  - relevancia
  - descobertas_principais
  - pendencias
- **Metadados**:
  - track_dates: true
  - track_progress: true
  - track_connections: true
- **Gatilhos de Atualização**:
  - nova_fonte
  - nova_analise
  - nova_conexao
  - novo_documento

### /update-rules
- **Dificuldade**: Média
- **Frequência**: on_demand
- **Funcionalidades**:
  - Backup automático
  - Controle de versão
  - Notificações
- **Seções de Resumo**:
  - Fontes Analisadas
    - nome_arquivo
    - tipo_documento
    - data_analise
    - descobertas_principais
  - Fontes Pendentes
    - nome_arquivo
    - status
    - prioridade
    - prazo_estimado
  - Conexões
    - fonte_origem
    - fonte_destino
    - tipo_conexao
    - relevancia

## Notas de Uso
1. Todos os comandos respeitam as regras definidas no .cursorrules
2. Backups automáticos são realizados antes de alterações significativas
3. Logs detalhados são mantidos para todas as operações
4. A formatação markdown é preservada em todas as operações
5. Metadados são mantidos em todas as exportações
6. Validações ABNT são aplicadas automaticamente
7. Integrações com ferramentas externas requerem configuração prévia
8. Comandos podem ser executados em qualquer nível do projeto
9. Evidências devem ser validadas por múltiplas fontes
10. Referências cruzadas são obrigatórias 