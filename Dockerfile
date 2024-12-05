# Use a imagem base do Python
FROM python:3.12-slim

# Instale as dependências do psycopg2 e libmagic
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    libmagic1 \
    && rm -rf /var/lib/apt/lists/*

# Crie o diretório de trabalho
RUN mkdir -p /code

# Defina o diretório de trabalho
WORKDIR /code

# Copie o arquivo requirements.txt
COPY requirements.txt /code/

# Instale as dependências
RUN pip install -r requirements.txt

# Copie o restante do código
COPY . /code

# Defina a variável de ambiente SECRET_KEY
ENV SECRET_KEY "t9AMMJtdgqa7kiQOM8YNMb4790BZp4CY9biOU7jqK5feornSoT"

# Coleta os arquivos estáticos
RUN python manage.py collectstatic --noinput

# Exponha a porta 8000
EXPOSE 8000

# Comando para iniciar o servidor
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "--worker-class", "uvicorn.workers.UvicornWorker", "config.asgi:application"]
