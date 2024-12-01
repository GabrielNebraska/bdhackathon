#!/usr/bin/env bash
# Sai do script se houver algum erro
set -o errexit

# Atualiza o pip
pip install --upgrade pip

pip install pdm

# Instala as dependências
pip install -r requirements.txt

# Coleta os arquivos estáticos
python manage.py collectstatic --no-input

# Aplica as migrações
python manage.py migrate

pip install pdm

pdm self update

pdm install

pdm run python manage.py collectstatic --no-input

pdm run python manage.py migrate
