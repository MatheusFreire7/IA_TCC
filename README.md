# IA em Python para a classificação de Intensidade de Planos Fitness

## Sobre ℹ️
Esta **Inteligência Artificial** foi desenvolvida utilizando o modelo de **Árvore de Decisão** da biblioteca scikit-learn. Utilizando conjuntos de dados fictícios para treinamento e testes, a IA é capaz de classificar a intensidade de planos fitness com precisão. Para facilitar a integração desta IA em um Aplicativo de fitness desenvolvido em Flutter, uma API foi criada usando **Flask**.

## Pré-requisitos 🛠️

Antes de usar este aplicativo, você deve ter instalado no seu Computador:

- **Python3**: Linguagem de programação utilizada.
- **sklearn**: Biblioteca fundamental para a construção do modelo de IA.
- **joblib**: Necessário para salvar o modelo de IA.
- **pandas**: Utilizada para a manipulação de arquivos CSV.
- **Flask**: Framework utilizado para criar a API, com o método de previsão do modelo de IA.
- **flask_cors**: Essencial para a utilização de CORS na API, permitindo a integração com o Flutter.
- **random**: Utilizado para gerar números aleatórios em um determinado intervalo para características da Base de Dados.

Esteja pronto para explorar o poder desta IA e integrá-la aos seus projetos fitness! 🏋️‍♂️✨

## Como Usar  ▶️
1. **Clone o repositório**:
``` bash
   git clone https://github.com/MatheusFreire7/IA_TCC.git
```

2. **Instalar as Dependências do Projeto**:
 ``` bash
   pip install scikit-learn joblib pandas flask flask_cors random csv
```
3. **Extraia o Arquivo "base_dados.csv.zip"**
 
4. **Execute a Api**:
 ``` bash
   python api.py
```

## **Autores**
   **Luiz Henrique Parolim Domingues**     [Github](https://github.com/LuizHPDomingues2005)<br>
   **Matheus Henrique de Oliveira Freire** [Github](https://github.com/MatheusFreire7)
