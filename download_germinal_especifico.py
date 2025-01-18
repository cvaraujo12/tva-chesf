import requests
from bs4 import BeautifulSoup
import os
import time

def baixar_artigos():
    # URL da revista
    url = "https://periodicos.ufba.br/index.php/revistagerminal/issue/view/2576"

    # Criar diretório para salvar os PDFs
    if not os.path.exists("pdfs_germinal"):
        os.makedirs("pdfs_germinal")

    # Configurar headers para simular um navegador
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
    }

    # Fazer requisição para a página
    print("Acessando a página da revista...")
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()  # Verificar se a resposta foi bem sucedida
        print("Página acessada com sucesso!")
    except Exception as e:
        print(f"Erro ao acessar a página: {str(e)}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar todos os artigos (procurando na estrutura específica da página)
    artigos = {}
    for section in soup.find_all('div', class_='section'):
        for item in section.find_all('div', class_='title'):
            link = item.find('a')
            if link:
                titulo = link.get_text().strip()
                href = link.get('href', '')
                if href:
                    artigos[titulo] = href

    total_artigos = len(artigos)
    print(f"\nEncontrados {total_artigos} artigos para download\n")

    if total_artigos == 0:
        print("Nenhum artigo encontrado. Verifique se o site está acessível.")
        # Salvar o HTML para debug
        with open('debug_page.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
        print("HTML da página salvo em 'debug_page.html' para análise.")
        return

    # Baixar todos os artigos
    for i, (titulo, pdf_url) in enumerate(artigos.items(), 1):
        try:
            # Criar nome do arquivo baseado no título
            filename = titulo.replace(" ", "_").replace("/", "-").replace(":", "")[:100] + ".pdf"
            filepath = os.path.join("pdfs_germinal", filename)
            
            print(f"\nBaixando {i}/{total_artigos}: {titulo}")
            print(f"URL: {pdf_url}")
            
            # Fazer download do PDF
            pdf_response = requests.get(pdf_url, headers=headers, timeout=30)
            
            # Verificar se é realmente um PDF
            if 'application/pdf' in pdf_response.headers.get('content-type', '').lower():
                # Salvar o PDF
                with open(filepath, 'wb') as f:
                    f.write(pdf_response.content)
                print(f"✓ Download concluído!")
            else:
                print(f"❌ O link não é um PDF válido")
            
            # Esperar um pouco entre downloads
            time.sleep(2)
                
        except Exception as e:
            print(f"❌ Erro ao baixar {titulo}: {str(e)}")

print("Iniciando downloads...")
baixar_artigos()
print("\nProcesso concluído! Os PDFs foram salvos na pasta 'pdfs_germinal'") 