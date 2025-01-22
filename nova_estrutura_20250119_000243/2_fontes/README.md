# Sistema de Gestão de Fontes

## Estrutura de Diretórios

```
2_fontes/
├── primarias/
│   ├── documentos/      # Documentos originais
│   ├── entrevistas/     # Transcrições e gravações
│   └── dados_brutos/    # Dados não processados
├── secundarias/
│   ├── artigos/         # Artigos científicos
│   ├── livros/          # Livros e ebooks
│   └── websites/        # Conteúdo web
└── metadados/
    ├── indices/         # Índices de busca
    └── catalogos/       # Catálogos organizados
```

## Sistema de Catalogação

### Formato de Metadados
```json
{
  "id": "FONTE-YYYYMMDD-XXX",
  "tipo": "artigo|livro|documento|entrevista|website",
  "titulo": "Título da Fonte",
  "autores": ["Autor 1", "Autor 2"],
  "data": {
    "publicacao": "YYYY-MM-DD",
    "acesso": "YYYY-MM-DD"
  },
  "localizacao": {
    "fisica": "path/to/file",
    "digital": "url/doi"
  },
  "tags": ["tag1", "tag2"],
  "status": "ativo|arquivado|removido",
  "citacoes": {
    "abnt": "Formato ABNT",
    "apa": "Formato APA"
  }
}
```

## Processos de Gestão

### 1. Adição de Novas Fontes
1. Verificar duplicidade
2. Gerar ID único
3. Preencher metadados
4. Armazenar arquivo
5. Indexar conteúdo

### 2. Organização
- Classificação por tipo
- Indexação por palavras-chave
- Categorização temática
- Vinculação entre fontes relacionadas

### 3. Backup
- Backup diário incremental
- Backup semanal completo
- Verificação mensal de integridade
- Rotação de backups (90 dias)

### 4. Validação
- Verificação de links
- Validação de DOIs
- Checagem de integridade de arquivos
- Atualização de referências

## Integração com Gestores Bibliográficos

### Mendeley
- Sincronização automática
- Importação de metadados
- Exportação de citações
- Gestão de PDFs

### Zotero
- Sincronização de biblioteca
- Tags e coleções
- Notas e anotações
- Backup na nuvem

## Políticas de Uso

### Acesso
- Controle por níveis de permissão
- Registro de acessos
- Proteção de dados sensíveis
- Compartilhamento controlado

### Manutenção
- Verificação mensal de links
- Atualização de metadados
- Limpeza de fontes obsoletas
- Consolidação de duplicatas 