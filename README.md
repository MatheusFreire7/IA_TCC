# IA em Python para a classificação de Intensidade de Planos Fitness

## Sobre ℹ️
Esta inteligência artificial foi construída com base no modelo de Árvore de Decisão da biblioteca scikit-learn. Ela faz uso de conjuntos de dados fictícios para treinamento e testes. Para facilitar a integração desta IA em um futuro aplicativo de fitness desenvolvido em Flutter, criamos uma API usando Flask.

## Pré-requisitos 🛠️

Antes de usar este aplicativo, você deve ter instalado no seu Computador:

- **Python3**: Linguagem de Programação
- **sklearn**: Bilioteca usada para a criação da IA
- **joblib**: Salvar o modelo de IA
- **pandas**: Manipulação de arquivos CSV
- **Flask**: Framework usado para criar uma Api com o método previsão do modelo de IA criado
- **flask_cors**: É necessário a utilização de cors na Api para integrar com o Flutter
- **random**: É usado para gerar um número alatório em um certo range em características da Base de Dados


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
