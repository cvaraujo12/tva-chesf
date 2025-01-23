# Comandos Disponíveis

## /update-resume
**Descrição**: Atualiza o resumo geral de todas as fontes consultadas na sessão atual.

### Funcionalidades
- Gera/atualiza arquivo `resumo_geral_pesquisa.md`
- Incorpora novas fontes identificadas
- Atualiza status de análises
- Registra novas conexões descobertas
- Mantém histórico de alterações

### Estrutura do Resumo
1. **Fontes Analisadas**
   - Nome e localização
   - Status da análise
   - Descobertas principais
   - Relevância para pesquisa

2. **Fontes Pendentes**
   - Identificação
   - Prioridade
   - Prazo estimado
   - Requisitos de acesso

3. **Conexões Estabelecidas**
   - Entre documentos
   - Entre instituições
   - Validações cruzadas

4. **Próximos Passos**
   - Análises prioritárias
   - Documentos pendentes
   - Cruzamentos necessários

5. **Recomendações**
   - Ações imediatas
   - Preparação documental
   - Expansão da pesquisa

### Uso
```bash
/update-resume                    # Atualização básica
/update-resume --full            # Atualização completa com metadados
/update-resume --section=fontes  # Atualiza seção específica
```

### Metadados Incluídos
- Data da última atualização
- Número de fontes analisadas
- Estatísticas de progresso
- Validações pendentes

### Observações
- Executa backup automático antes da atualização
- Mantém histórico de versões
- Notifica sobre alterações significativas
- Preserva formatação markdown

### Integração
- Respeita regras do .cursorrules
- Mantém padrões de documentação
- Permite exportação em múltiplos formatos
- Facilita citações e referências

# Comandos de Produção e Revisão

## Comandos de Análise e Verificação

### /check-consistency
Verifica a consistência do conteúdo em diferentes níveis (volume, capítulo, seção).
- **Escopo**: Define o nível de análise (volume, capítulo ou seção)
- **Verificações**: Cronologia, referências cruzadas, citações e narrativa
- **Saída**: Relatório em formato markdown com inconsistências encontradas

### /generate-timeline
Gera linha do tempo visual dos eventos documentados.
- **Formatos**: Mermaid, markdown ou visual
- **Ordenação**: Automática por data
- **Detecção**: Identifica lacunas temporais na narrativa

### /review-citations
Analisa e valida as citações utilizadas.
- **Estilos**: Chicago, APA ou personalizado
- **Verificações**: Formato, completude e duplicatas
- **Correções**: Sugestões de ajustes necessários

### /analyze-gaps
Identifica lacunas na documentação e narrativa.
- **Tipos**: Documentação, linha do tempo, evidências e narrativa
- **Sugestões**: Fontes potenciais para preencher lacunas
- **Relatório**: Lista detalhada de áreas que precisam complementação

## Comandos de Geração e Exportação

### /generate-summary
Gera resumos automáticos em diferentes níveis.
- **Níveis**: Capítulo, seção ou descobertas
- **Metadados**: Inclui informações sobre fontes e classificação
- **Formato**: Markdown estruturado com seções definidas

### /validate-sources
Valida as fontes utilizadas na pesquisa.
- **Validação**: Autenticidade, referências cruzadas e classificação
- **Rastreamento**: Mantém histórico de alterações
- **Relatório**: Status de validação de cada fonte

### /track-revisions
Gerencia versões e alterações no conteúdo.
- **Rastreamento**: Mudanças, versões e conflitos
- **Backup**: Mantém cópias de segurança automáticas
- **Histórico**: Log detalhado de alterações

### /export-findings
Exporta descobertas em diferentes formatos.
- **Formatos**: PDF, markdown, HTML e DOCX
- **Evidências**: Inclui documentação comprobatória
- **Personalização**: Opções de formatação por formato

## Comandos de Análise Avançada

### /check-narrative
Analisa a qualidade e coerência da narrativa.
- **Aspectos**: Fluxo, consistência, lógica e transições
- **Sugestões**: Melhorias na estrutura narrativa
- **Relatório**: Pontos fortes e áreas para melhoria

### /generate-visualization
Cria visualizações das conexões e relacionamentos.
- **Tipos**: Redes, linhas do tempo, hierarquias e conexões
- **Formatos**: Mermaid, DOT e SVG
- **Interativo**: Permite exploração visual dos dados

### /semantic-analysis
Realiza análise semântica do conteúdo.
- **Análises**: Temas, padrões, contextos e relacionamentos
- **Conexões**: Sugere ligações entre diferentes elementos
- **Insights**: Identifica padrões e tendências

### /quality-check
Verifica a qualidade geral do conteúdo.
- **Verificações**: Linguagem, estrutura, referências e formatação
- **Correções**: Sugestões de melhorias
- **Relatório**: Avaliação detalhada da qualidade

## Notas de Uso
1. Todos os comandos podem ser executados em qualquer nível do projeto
2. Os relatórios são gerados em markdown por padrão
3. As configurações podem ser ajustadas no arquivo .cursorrules
4. Backups automáticos são realizados antes de alterações significativas
5. Logs detalhados são mantidos para todas as operações 