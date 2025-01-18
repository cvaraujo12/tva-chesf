from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import requests

def baixar_artigos():
    # URL da revista
    url = "https://periodicos.ufba.br/index.php/revistagerminal/issue/view/2576"

    # Criar diretório para salvar os PDFs
    if not os.path.exists("pdfs_germinal"):
        os.makedirs("pdfs_germinal")

    # Configurar o Firefox em modo headless
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    
    print("Iniciando navegador...")
    driver = webdriver.Firefox(options=options)
    
    try:
        print("Acessando a página da revista...")
        driver.get(url)
        
        # Esperar a página carregar
        time.sleep(5)
        
        # Encontrar todos os links de artigos
        artigos = []
        sections = driver.find_elements(By.CLASS_NAME, "obj_article_summary")
        
        for section in sections:
            try:
                titulo = section.find_element(By.CLASS_NAME, "title").text.strip()
                pdf_link = section.find_element(By.PARTIAL_LINK_TEXT, "PDF").get_attribute("href")
                if pdf_link and titulo:
                    artigos.append((titulo, pdf_link))
            except:
                continue

        total_artigos = len(artigos)
        print(f"\nEncontrados {total_artigos} artigos para download\n")

        # Headers para o download
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Firefox/91.0',
            'Accept': 'application/pdf,application/octet-stream',
        }

        # Baixar cada PDF
        for i, (titulo, pdf_url) in enumerate(artigos, 1):
            try:
                # Criar nome do arquivo
                filename = titulo.replace(" ", "_").replace("/", "-").replace(":", "")[:100] + ".pdf"
                filepath = os.path.join("pdfs_germinal", filename)
                
                print(f"\nBaixando {i}/{total_artigos}: {titulo}")
                print(f"URL: {pdf_url}")
                
                # Fazer download do PDF
                pdf_response = requests.get(pdf_url, headers=headers, timeout=30)
                
                if pdf_response.status_code == 200:
                    with open(filepath, 'wb') as f:
                        f.write(pdf_response.content)
                    print(f"✓ Download concluído!")
                else:
                    print(f"❌ Erro no download: Status {pdf_response.status_code}")
                
                # Esperar entre downloads
                time.sleep(2)
                    
            except Exception as e:
                print(f"❌ Erro ao baixar {titulo}: {str(e)}")
                
    except Exception as e:
        print(f"Erro ao acessar a página: {str(e)}")
    
    finally:
        print("\nFechando o navegador...")
        driver.quit()

if __name__ == "__main__":
    print("Iniciando downloads...")
    baixar_artigos()
    print("\nProcesso concluído! Os PDFs foram salvos na pasta 'pdfs_germinal'") 