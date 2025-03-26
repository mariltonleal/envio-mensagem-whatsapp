FROM python:3.10-slim

WORKDIR /app

# Instalar ferramentas de diagnóstico
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copiar arquivo de requisitos
COPY requirements.txt .

# Instalar dependências com diagnóstico
RUN pip install --no-cache-dir --upgrade pip && \
    echo "Python version:" && python --version && \
    echo "Pip version:" && pip --version && \
    pip install --no-cache-dir -r requirements.txt

# Copiar o código do servidor
COPY envio_mensagem.py .

# Comando para iniciar o servidor MCP
CMD ["python", "envio_mensagem.py"]