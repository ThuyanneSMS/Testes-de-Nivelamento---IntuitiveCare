# server.py
from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS
from io import StringIO

app = Flask(__name__)
CORS(app)

# Carrega o CSV (ajuste o caminho conforme necessário)
with open(r'C:/Users/Thuya/OneDrive/Área de Trabalho/TESTE DE API/operadoras.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    # Tenta encontrar o número correto de colunas na primeira linha
    n_cols = len(lines[0].split(','))
    # Filtra linhas com número errado de colunas
    cleaned_lines = [line for line in lines if len(line.split(',')) == n_cols]
    df = pd.read_csv(StringIO(''.join(cleaned_lines)))

@app.route('/api/search', methods=['GET'])
def search_operadoras():
    query = request.args.get('q', '').lower()
    if not query:
        return jsonify({'results': df.to_dict('records')})
    
    # Busca textual simples
    filtered_df = df[df.apply(lambda row: any(query in str(value).lower() 
                           for value in row), axis=1)]
    
    # Ordena por relevância (contagem de ocorrências da query)
    filtered_df = filtered_df.assign(
        relevance=lambda x: x.apply(
            lambda row: sum(str(value).lower().count(query) 
                          for value in row), axis=1)
    ).sort_values('relevance', ascending=False)
    
    return jsonify({
        'results': filtered_df.drop('relevance', axis=1).to_dict('records')
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)