# Use a imagem base do Python
FROM python:3.9

# Defina o diretório de trabalho
WORKDIR /code

# Copie o arquivo requirements.txt
COPY requirements.txt /code/

# Instale as dependências
RUN pip install -r requirements.txt

# Copie o restante do código
COPY . /code/

# Defina a variável de ambiente SECRET_KEY
ENV SECRET_KEY "_*(ko-j_4x-pfkh+u_4gm0inget@1&m$ybd3@o8v)ad=o9%!@v"

# Coleta os arquivos estáticos
RUN python manage.py collectstatic --noinput

# Exponha a porta 8000
EXPOSE 8000

# Comando para iniciar o servidor
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "--worker-class", "uvicorn.workers.UvicornWorker", "hackathon.asgi:application"]