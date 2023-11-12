# Use a imagem oficial do Python como base
FROM python:3.8-slim

# Configurar o ambiente
WORKDIR /app
COPY . /app

# Instalar as dependências
RUN pip install --upgrade pip
RUN pip install flask pandas scikit-learn flask-cors joblib zipfile os shutil

# Expor a porta
EXPOSE 3030

# Comando para executar a aplicação quando o contêiner for iniciado
CMD ["python", "api.py"]