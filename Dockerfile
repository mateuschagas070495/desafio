# Use uma imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos requirements.txt e app.py para o contêiner
COPY requirements.txt requirements.txt
COPY app.py app.py

# Instale as dependências
RUN pip install -r requirements.txt

# Exponha a porta que o Flask usa
EXPOSE 5000

# Defina o comando padrão para executar o aplicativo
CMD ["python", "app.py"]
