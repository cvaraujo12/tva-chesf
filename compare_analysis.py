import json
import os
from pathlib import Path
import spacy
from collections import defaultdict

def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def analyze_connections(text, nlp):
    doc = nlp(text)
    
    # Extrair temas e conceitos principais
    themes = defaultdict(int)
    for ent in doc.ents:
        if len(ent.text) > 3:
            themes[ent.text.lower()] += 1
    
    return dict(sorted(themes.items(), key=lambda x: x[1], reverse=True))

def compare_with_analysis(connections_themes, analysis_data):
    comparisons = {}
    
    for doc_name, doc_analysis in analysis_data.items():
        doc_entities = set(k.lower() for k in doc_analysis['key_entities'].keys())
        
        # Encontrar interseções temáticas
        common_themes = []
        for theme in connections_themes:
            if any(theme.lower() in entity for entity in doc_entities):
                common_themes.append(theme)
        
        comparisons[doc_name] = {
            'common_themes': common_themes,
            'unique_themes': list(doc_entities - set(t.lower() for t in connections_themes)),
            'relevance_score': len(common_themes) / len(connections_themes) if connections_themes else 0
        }
    
    return comparisons

def main():
    # Carregar modelo spaCy
    nlp = spacy.load('pt_core_news_sm')
    
    # Ler arquivo de conexões temáticas
    connections_text = read_markdown_file('documentos_apoio/conexoes_tematicas.md')
    connections_themes = analyze_connections(connections_text, nlp)
    
    # Ler análises dos documentos
    with open('analysis_output/global_analysis.json', 'r', encoding='utf-8') as f:
        analysis_data = json.load(f)
    
    # Realizar comparação
    comparisons = compare_with_analysis(connections_themes, analysis_data)
    
    # Criar diretório para sínteses
    Path('sinteses').mkdir(exist_ok=True)
    
    # Gerar sínteses individuais e comparativas
    for doc_name, comparison in comparisons.items():
        synthesis = {
            'documento': doc_name,
            'temas_em_comum': comparison['common_themes'],
            'temas_unicos': comparison['unique_themes'][:10],  # Limitar a 10 temas únicos
            'score_relevancia': comparison['relevance_score'],
            'analise_original': analysis_data[doc_name]
        }
        
        # Salvar síntese
        synthesis_path = os.path.join('sinteses', f"{doc_name}_sintese.json")
        with open(synthesis_path, 'w', encoding='utf-8') as f:
            json.dump(synthesis, f, ensure_ascii=False, indent=2)
    
    # Gerar síntese global
    global_synthesis = {
        'total_documentos': len(comparisons),
        'media_relevancia': sum(c['relevance_score'] for c in comparisons.values()) / len(comparisons),
        'documentos_mais_relevantes': sorted(
            [(k, v['relevance_score']) for k, v in comparisons.items()],
            key=lambda x: x[1],
            reverse=True
        )[:5]
    }
    
    with open('sinteses/sintese_global.json', 'w', encoding='utf-8') as f:
        json.dump(global_synthesis, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main() 