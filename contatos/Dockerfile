# Imagem base mínima com Python 3.14
FROM python:3.14-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Evita buffers no stdout/stderr e garante encoding UTF-8
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DJANGO_SETTINGS_MODULE=contatos.settings

# Instala dependências do sistema necessárias para conectar ao MariaDB/MySQL
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia arquivo de dependências e instala via pip
COPY requirements.txt ./
RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copia o restante do código do projeto
COPY . .

# Porta padrão do Django
EXPOSE 8000

# Comando padrão ao iniciar o container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
