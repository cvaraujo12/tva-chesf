#!/usr/bin/env python3
import os
import yaml
from datetime import datetime
import shutil

class Catalogador:
    def __init__(self):
        self.tipos = {
            'DOC': 'Documentos Técnicos e Relatórios',
            'BIB': 'Bibliografia Acadêmica',
            'LEG': 'Legislação e Normas',
            'IMG': 'Imagens e Fotografias',
            'VID': 'Vídeos e Documentários',
            'AUD': 'Áudios e Entrevistas',
            'MAP': 'Mapas e Plantas'
        }
        
        self.categorias = {
            'GER': 'Geral',
            'TEC': 'Técnico',
            'ADM': 'Administrativo',
            'HIS': 'Histórico',
            'POL': 'Político',
            'ECO': 'Econômico',
            'SOC': 'Social',
            'AMB': 'Ambiental'
        }
        
        self.tags_tematicas = [
            'Imperialismo', 'Desenvolvimento', 'Territorio',
            'SetorEletrico', 'Tecnologia', 'Politica',
            'Economia', 'Sociedade', 'MeioAmbiente'
        ]
        
        self.tags_temporais = [
            'PeriodoImperial', 'PeriodoDesenvolvimentista',
            'PeriodoTecnicoMilitar', 'PeriodoGrandesProjetos',
            'PeriodoTransicao'
        ]
        
        self.tags_geograficas = [
            'Nordeste', 'SaoFrancisco', 'PauloAfonso',
            'Chesf', 'Brasil'
        ]

    def gerar_codigo(self, tipo, ano, categoria, numero):
        return f"{tipo}-{ano}-{categoria}-{numero:03d}"

    def criar_metadados(self):
        print("\n=== Catalogação de Documento ===\n")
        
        # Tipo
        print("Tipos disponíveis:")
        for k, v in self.tipos.items():
            print(f"{k}: {v}")
        tipo = input("Digite o tipo do documento: ").upper()
        
        # Ano
        ano = input("Digite o ano do documento (AAAA ou 0000 se desconhecido): ")
        
        # Categoria
        print("\nCategorias disponíveis:")
        for k, v in self.categorias.items():
            print(f"{k}: {v}")
        categoria = input("Digite a categoria do documento: ").upper()
        
        # Número sequencial
        numero = int(input("Digite o número sequencial (1-999): "))
        
        codigo = self.gerar_codigo(tipo, ano, categoria, numero)
        
        metadados = {
            'codigo': codigo,
            'titulo': input("Título do documento: "),
            'data': input("Data do documento (AAAA-MM-DD): "),
            'autor': input("Autor/Instituição: "),
            'tipo': self.tipos.get(tipo, "Não especificado"),
            'categoria': self.categorias.get(categoria, "Não especificada"),
            'localizacao': input("Localização do arquivo: "),
            'palavras_chave': input("Palavras-chave (separadas por vírgula): ").split(','),
            'descricao': input("Breve descrição: "),
            'relacionados': input("Códigos relacionados (separados por vírgula): ").split(',')
        }
        
        return metadados

    def salvar_metadados(self, metadados, pasta_destino):
        codigo = metadados['codigo']
        arquivo_yaml = os.path.join(pasta_destino, f"{codigo}_metadata.yaml")
        
        with open(arquivo_yaml, 'w', encoding='utf-8') as f:
            yaml.dump(metadados, f, allow_unicode=True, sort_keys=False)
        
        print(f"\nMetadados salvos em: {arquivo_yaml}")

    def mover_arquivo(self, arquivo_origem, pasta_destino, codigo):
        nome_arquivo = os.path.basename(arquivo_origem)
        extensao = os.path.splitext(nome_arquivo)[1]
        novo_nome = f"{codigo}_{nome_arquivo}"
        destino = os.path.join(pasta_destino, novo_nome)
        
        shutil.copy2(arquivo_origem, destino)
        print(f"\nArquivo copiado para: {destino}")

def main():
    catalogador = Catalogador()
    
    print("=== Sistema de Catalogação de Documentos ===")
    
    while True:
        print("\nOpções:")
        print("1. Catalogar novo documento")
        print("2. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            metadados = catalogador.criar_metadados()
            
            pasta_destino = input("\nDigite o caminho da pasta de destino: ")
            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)
            
            catalogador.salvar_metadados(metadados, pasta_destino)
            
            arquivo_origem = input("\nDigite o caminho do arquivo a ser catalogado (ou Enter para pular): ")
            if arquivo_origem and os.path.exists(arquivo_origem):
                catalogador.mover_arquivo(arquivo_origem, pasta_destino, metadados['codigo'])
            
            print("\nDocumento catalogado com sucesso!")
            
        elif opcao == "2":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main() 