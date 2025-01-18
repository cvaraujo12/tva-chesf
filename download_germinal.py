import requests
from bs4 import BeautifulSoup
import os
import time

# URL da revista
url = "https://periodicos.ufba.br/index.php/revistagerminal/issue/view/2576"

# Criar diretório para salvar os PDFs
if not os.path.exists("pdfs_germinal"):
    os.makedirs("pdfs_germinal")

# Fazer requisição para a página
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar todos os links PDF
pdf_links = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href and 'pdf' in href:
        pdf_links.append(href)

# Baixar cada PDF
for i, pdf_url in enumerate(pdf_links, 1):
    try:
        # Extrair nome do arquivo do URL
        filename = pdf_url.split('/')[-1]
        if not filename.endswith('.pdf'):
            filename += '.pdf'
        
        # Caminho completo para salvar
        filepath = os.path.join("pdfs_germinal", filename)
        
        print(f"Baixando {i}/{len(pdf_links)}: {filename}")
        
        # Fazer download do PDF
        pdf_response = requests.get(pdf_url)
        
        # Salvar o PDF
        with open(filepath, 'wb') as f:
            f.write(pdf_response.content)
        
        # Esperar um pouco entre downloads para não sobrecarregar o servidor
        time.sleep(2)
        
    except Exception as e:
        print(f"Erro ao baixar {pdf_url}: {str(e)}")

print("\nDownload concluído! Os PDFs foram salvos na pasta 'pdfs_germinal'") 