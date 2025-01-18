import os
import PyPDF2
import spacy
from pathlib import Path
from collections import defaultdict
import json
from tqdm import tqdm

def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        print(f"Erro ao processar {pdf_path}: {str(e)}")
        return ""

def save_text_file(text, output_path):
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(text)
        return True
    except Exception as e:
        print(f"Erro ao salvar {output_path}: {str(e)}")
        return False

def analyze_text(text, nlp):
    try:
        doc = nlp(text[:1000000])  # Limitar o tamanho do texto para evitar problemas de memória
        
        # Análise básica
        analysis = {
            'num_sentences': len(list(doc.sents)),
            'num_tokens': len(doc),
            'key_entities': defaultdict(int),
            'main_concepts': [],
        }
        
        # Entidades nomeadas
        for ent in doc.ents:
            if len(ent.text) > 3:  # Filtrar entidades muito curtas
                analysis['key_entities'][f"{ent.text} ({ent.label_})"] += 1
        
        # Ordenar entidades por frequência
        analysis['key_entities'] = dict(sorted(
            analysis['key_entities'].items(), 
            key=lambda x: x[1], 
            reverse=True
        )[:20])
        
        return analysis
    except Exception as e:
        print(f"Erro na análise do texto: {str(e)}")
        return {
            'num_sentences': 0,
            'num_tokens': 0,
            'key_entities': {},
            'main_concepts': [],
            'error': str(e)
        }

def main():
    # Carregar modelo spaCy
    try:
        nlp = spacy.load('pt_core_news_sm')
    except Exception as e:
        print(f"Erro ao carregar modelo spaCy: {str(e)}")
        return
    
    # Criar diretórios de saída
    Path('txt_output').mkdir(exist_ok=True)
    Path('analysis_output').mkdir(exist_ok=True)
    
    # Processar PDFs
    pdf_dir = 'pdfs_germinal'
    all_analyses = {}
    
    pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
    
    for pdf_file in tqdm(pdf_files):
        try:
            pdf_path = os.path.join(pdf_dir, pdf_file)
            base_name = os.path.splitext(pdf_file)[0]
            
            # Extrair texto
            text = extract_text_from_pdf(pdf_path)
            if not text:
                continue
            
            # Salvar texto
            txt_path = os.path.join('txt_output', f"{base_name}.txt")
            if not save_text_file(text, txt_path):
                continue
            
            # Analisar texto
            analysis = analyze_text(text, nlp)
            all_analyses[base_name] = analysis
            
            # Salvar análise individual
            analysis_path = os.path.join('analysis_output', f"{base_name}_analysis.json")
            with open(analysis_path, 'w', encoding='utf-8') as f:
                json.dump(analysis, f, ensure_ascii=False, indent=2)
        
        except Exception as e:
            print(f"Erro ao processar {pdf_file}: {str(e)}")
            continue
    
    # Salvar análise global
    try:
        with open('analysis_output/global_analysis.json', 'w', encoding='utf-8') as f:
            json.dump(all_analyses, f, ensure_ascii=False, indent=2)
        print("Análise global salva com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar análise global: {str(e)}")

if __name__ == "__main__":
    main() 