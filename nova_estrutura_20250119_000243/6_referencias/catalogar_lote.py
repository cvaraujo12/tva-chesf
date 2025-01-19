#!/usr/bin/env python3
import os
import yaml
from datetime import datetime
import shutil
import re
from catalogar import Catalogador

class CatalogadorLote(Catalogador):
    def __init__(self):
        super().__init__()
        self.contadores = {}
        
    def detectar_tipo(self, arquivo):
        ext = os.path.splitext(arquivo)[1].lower()
        if ext in ['.pdf', '.doc', '.docx']:
            return 'DOC'
        elif ext in ['.txt', '.md']:
            return 'BIB'
        elif ext in ['.jpg', '.jpeg', '.png', '.gif']:
            return 'IMG'
        elif ext in ['.mp4', '.avi', '.mov']:
            return 'VID'
        elif ext in ['.mp3', '.wav']:
            return 'AUD'
        else:
            return 'DOC'
            
    def extrair_data_do_nome(self, nome):
        # Procura por padrão de data no nome do arquivo (YYYYMMDD)
        match = re.search(r'(\d{8})', nome)
        if match:
            data_str = match.group(1)
            try:
                return datetime.strptime(data_str, '%Y%m%d')
            except ValueError:
                pass
        return None
            
    def detectar_categoria(self, caminho, nome):
        nome_lower = nome.lower()
        caminho_lower = caminho.lower()
        
        if 'artigo' in nome_lower or 'resenha' in nome_lower:
            return 'BIB'
        elif 'texto' in nome_lower and 'artigo' in nome_lower:
            return 'BIB'
        elif 'chesf' in nome_lower or 'chesf' in caminho_lower:
            return 'HIS'
        elif 'estudo' in nome_lower or '/estudos/' in caminho_lower:
            return 'TEC'
        elif 'relatorio' in nome_lower or '/relatorios/' in caminho_lower:
            return 'TEC'
        elif 'bibliografica' in nome_lower or '/bases_bibliograficas/' in caminho_lower:
            return 'BIB'
        elif 'projeto' in nome_lower:
            return 'ADM'
        else:
            return 'BIB'  # Default para pasta txt_output
            
    def extrair_id_artigo(self, nome):
        # Extrai o ID do artigo do nome do arquivo
        match = re.search(r'^(\d+)', nome)
        if match:
            return match.group(1)
        return None
            
    def gerar_numero_sequencial(self, tipo, ano, categoria):
        chave = f"{tipo}-{ano}-{categoria}"
        if chave not in self.contadores:
            self.contadores[chave] = 0
        self.contadores[chave] += 1
        return self.contadores[chave]
        
    def criar_metadados_automatico(self, arquivo, pasta_origem):
        nome_base = os.path.splitext(os.path.basename(arquivo))[0]
        
        # Tenta extrair data do nome do arquivo, senão usa data de modificação
        data_arquivo = self.extrair_data_do_nome(nome_base)
        if data_arquivo:
            data_mod = data_arquivo
            ano = str(data_mod.year)
        else:
            data_mod = datetime.fromtimestamp(os.path.getmtime(arquivo))
            ano = str(data_mod.year)
        
        tipo = self.detectar_tipo(arquivo)
        categoria = self.detectar_categoria(arquivo, nome_base)
        numero = self.gerar_numero_sequencial(tipo, ano, categoria)
        
        codigo = self.gerar_codigo(tipo, ano, categoria, numero)
        
        # Define a pasta de destino baseada no tipo
        if tipo == 'DOC':
            subpasta = 'documentos/tecnicos'
        elif tipo == 'BIB':
            subpasta = 'bibliografia/primaria'
        elif tipo in ['IMG', 'VID', 'AUD']:
            subpasta = f'midiateca/{tipo.lower()}s'
        else:
            subpasta = 'documentos/tecnicos'
            
        # Extrai palavras-chave mais significativas
        palavras_chave = []
        partes = nome_base.replace('_', ' ').replace('-', ' ').split()
        for palavra in partes:
            if len(palavra) > 2 and not palavra.isdigit():
                palavras_chave.append(palavra.lower())
        
        # Extrai ID do artigo se disponível
        id_artigo = self.extrair_id_artigo(nome_base)
        if id_artigo:
            palavras_chave.append(f"ID:{id_artigo}")
        
        metadados = {
            'codigo': codigo,
            'titulo': nome_base.replace('_', ' ').replace('-', ' ').title(),
            'data': data_mod.strftime('%Y-%m-%d'),
            'autor': 'Não especificado',
            'tipo': self.tipos.get(tipo, "Não especificado"),
            'categoria': self.categorias.get(categoria, "Não especificada"),
            'localizacao': subpasta,
            'palavras_chave': palavras_chave,
            'descricao': f"Artigo acadêmico ID:{id_artigo if id_artigo else 'N/A'} encontrado em {os.path.dirname(arquivo)}",
            'relacionados': []
        }
        
        return metadados, subpasta
        
    def catalogar_pasta(self, pasta_origem):
        print(f"\nCatalogando pasta: {pasta_origem}")
        
        arquivos_processados = 0
        
        for root, dirs, files in os.walk(pasta_origem):
            for arquivo in files:
                if arquivo.startswith('.') or arquivo.endswith('.yaml'):
                    continue
                    
                caminho_completo = os.path.join(root, arquivo)
                print(f"\nProcessando: {caminho_completo}")
                
                try:
                    metadados, subpasta = self.criar_metadados_automatico(caminho_completo, pasta_origem)
                    pasta_destino = os.path.join('referencias', subpasta)
                    
                    if not os.path.exists(pasta_destino):
                        os.makedirs(pasta_destino)
                        
                    self.salvar_metadados(metadados, pasta_destino)
                    self.mover_arquivo(caminho_completo, pasta_destino, metadados['codigo'])
                    arquivos_processados += 1
                    print(f"Catalogado com sucesso: {metadados['codigo']} em {subpasta}")
                except Exception as e:
                    print(f"Erro ao processar {arquivo}: {str(e)}")
                    
        return arquivos_processados

def main():
    catalogador = CatalogadorLote()
    
    pasta_origem = "../txt_output"
    
    print("=== Catalogação em Lote de Documentos ===")
    print(f"\nPasta de origem: {pasta_origem}")
    print("Os arquivos serão organizados automaticamente nas pastas apropriadas")
    
    confirmacao = input("\nDeseja prosseguir com a catalogação? (s/n): ")
    if confirmacao.lower() != 's':
        print("Operação cancelada.")
        return
        
    total_processado = catalogador.catalogar_pasta(pasta_origem)
    print(f"\nProcessamento concluído!")
    print(f"Total de arquivos processados: {total_processado}")

if __name__ == "__main__":
    main() 