# Sistema de Catalogação de Referências

## 1. Estrutura do Código de Catalogação

Cada documento receberá um código único no formato:
`[TIPO]-[ANO]-[CATEGORIA]-[NÚMERO]`

### 1.1 Tipos de Documento [TIPO]
- DOC: Documentos Técnicos e Relatórios
- BIB: Bibliografia Acadêmica
- LEG: Legislação e Normas
- IMG: Imagens e Fotografias
- VID: Vídeos e Documentários
- AUD: Áudios e Entrevistas
- MAP: Mapas e Plantas

### 1.2 Ano [ANO]
- Formato: AAAA (ano de produção do documento)
- Para documentos sem data precisa: 0000

### 1.3 Categorias [CATEGORIA]
- GER: Geral
- TEC: Técnico
- ADM: Administrativo
- HIS: Histórico
- POL: Político
- ECO: Econômico
- SOC: Social
- AMB: Ambiental

### 1.4 Número Sequencial [NÚMERO]
- Formato: 001-999

Exemplo: `DOC-1942-TEC-001` (Primeiro documento técnico de 1942)

## 2. Metadados Obrigatórios

Cada documento deve conter os seguintes metadados:

```yaml
codigo: DOC-1942-TEC-001
titulo: "Título do Documento"
data: 1942-01-01
autor: "Nome do Autor/Instituição"
tipo: "Documento Técnico"
categoria: "Técnico"
localizacao: "referencias/documentos/tecnicos/"
palavras_chave: ["palavra1", "palavra2"]
descricao: "Breve descrição do conteúdo"
relacionados: ["códigos de documentos relacionados"]
```

## 3. Sistema de Tags

### 3.1 Tags Temáticas
- #Imperialismo
- #Desenvolvimento
- #Territorio
- #SetorEletrico
- #Tecnologia
- #Politica
- #Economia
- #Sociedade
- #MeioAmbiente

### 3.2 Tags Temporais
- #PeriodoImperial
- #PeriodoDesenvolvimentista
- #PeriodoTecnicoMilitar
- #PeriodoGrandesProjetos
- #PeriodoTransicao

### 3.3 Tags Geográficas
- #Nordeste
- #SaoFrancisco
- #PauloAfonso
- #Chesf
- #Brasil

## 4. Organização Física dos Arquivos

### 4.1 Estrutura de Pastas
```
referencias/
├── bibliografia/
│   ├── primaria/      # Documentos históricos originais
│   ├── secundaria/    # Livros e artigos acadêmicos
│   └── terciaria/     # Índices e catálogos
├── midiateca/
│   ├── imagens/       # Fotos e ilustrações
│   ├── videos/        # Vídeos e documentários
│   └── audio/         # Entrevistas e gravações
├── documentos/
│   ├── tecnicos/      # Relatórios e estudos
│   ├── institucionais/# Documentos oficiais
│   └── legislacao/    # Leis e normas
└── indices/
    ├── tematico/      # Organização por tema
    ├── cronologico/   # Linha do tempo
    └── geografico/    # Organização espacial
```

### 4.2 Nomenclatura de Arquivos
- Formato: `[CÓDIGO]_titulo-resumido.extensao`
- Exemplo: `DOC-1942-TEC-001_relatorio-missao-cooke.pdf`

## 5. Processo de Catalogação

1. **Identificação**
   - Analisar o documento
   - Determinar tipo e categoria
   - Atribuir código único

2. **Registro**
   - Preencher metadados
   - Adicionar tags relevantes
   - Criar links com documentos relacionados

3. **Arquivamento**
   - Salvar na pasta apropriada
   - Nomear arquivo conforme padrão
   - Atualizar índices

4. **Indexação**
   - Adicionar ao índice temático
   - Incluir na linha do tempo
   - Registrar no índice geográfico

## 6. Manutenção do Sistema

1. **Atualizações Regulares**
   - Verificar consistência dos códigos
   - Atualizar links relacionados
   - Revisar tags e metadados

2. **Backup**
   - Manter cópia de segurança
   - Versionar documentos importantes
   - Registrar alterações

3. **Revisão Periódica**
   - Validar organização
   - Atualizar índices
   - Verificar integridade 