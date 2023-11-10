from flask import Flask, request, jsonify
import joblib
import pandas as pd
import zipfile
import os
import shutil  # Importe o módulo shutil

from flask_cors import CORS

app = Flask(__name__)

# Carregue o modelo treinado
modelo = joblib.load("modelo_decision_tree.pkl")

# Função para descompactar o arquivo ZIP e carregar os dados em um DataFrame
def carregar_base_dados():
    with zipfile.ZipFile('base_dados.zip', 'r') as zip_ref:
        # Crie um diretório temporário para extrair os arquivos
        temp_dir = 'temp_extracted_data'
        os.makedirs(temp_dir, exist_ok=True)
        zip_ref.extractall(temp_dir)

    # Suponha que há apenas um arquivo CSV no diretório extraído
    csv_file = os.path.join(temp_dir, os.listdir(temp_dir)[0])
    
    # Carregue o CSV em um DataFrame Pandas
    df = pd.read_csv(csv_file)

    # Remova o diretório temporário e todo o seu conteúdo
    shutil.rmtree(temp_dir)

    return df

# Carregue a base de dados uma vez no início
base_dados = carregar_base_dados()

@app.route('/previsao', methods=['POST'])
def fazer_previsao():
    try:
        print("Recebeu uma solicitação POST")
        data = request.get_json()
        genero = data['genero']
        idade = data['idade']
        peso = data['peso']
        altura = data['altura']
        meta = data['meta']
        restricao = data['restricao']

        # Use a base de dados carregada
        df_encoded = pd.get_dummies(base_dados, columns=['gênero','meta','restricao'])
        
        # Mapeia os níveis de classificação
        class_mapping = {
            'intensivo': 2,
            'intermediário': 1,
            'menos_intensivo': 0
        }
        # Convertermos as classificações conforme o class_mapping
        df_encoded['classificação'] = df_encoded['classificação'].map(class_mapping)
        
        # Separar features e alvo
        X = df_encoded.drop('classificação', axis=1) #Features
        y = df_encoded['classificação']  #Alvo
        
        # Treinar o modelo com os dados disponíveis
        modelo.fit(X, y)

        # Fazer a previsão usando o modelo
        X_pred = pd.DataFrame({
            'idade': [idade],
            'peso': [peso],
            'altura': [altura],
            'gênero_feminino': [1 if genero == 'feminino' else 0],
            'gênero_masculino': [1 if genero == 'masculino' else 0],
            'meta_emagrecimento': [1 if meta == 'emagrecimento' else 0],
            'meta_hipertrofia': [1 if meta == 'hipertrofia' else 0],
            'restricao_diabetes': [1 if restricao == 'diabetes' else 0],
            'restricao_doenca_respiratoria': [1 if restricao == 'doenca_respiratoria' else 0],
            'restricao_nenhuma': [1 if restricao == 'nenhuma' else 0],
            'restricao_outro': [1 if restricao == 'outro' else 0],
            'restricao_problema_fisico': [1 if restricao == 'problema_fisico' else 0]
        })

        previsao = modelo.predict(X_pred)

        # Mapear a classificação de volta para o texto
        class_mapping_inverso = {
            2: 'intensivo',
            1: 'intermediário',
            0: 'menos_intensivo'
        }
        texto_previsao = class_mapping_inverso[previsao[0]]

        return jsonify({'previsao': texto_previsao})
    except Exception as e:
        return jsonify({'erro': str(e)})

if __name__ == '__main__':
    CORS(app)
    app.run(debug=True, port=3030)
