#!/usr/bin/env bash
# Sai do script se houver algum erro
set -o errexit

# Instala o PDM
pip install pdm

# Atualiza o PDM
pdm self update

# Instala as dependências
pdm install

# Coleta os arquivos estáticos
pdm run python manage.py collectstatic --no-input

# Aplica as migrações
pdm run python manage.py migrate