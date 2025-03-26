FROM python:3.10-slim

WORKDIR /app

# Copiar arquivo de requisitos
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código do servidor
COPY envio_mensagem.py .

# Comando para iniciar o servidor MCP
CMD ["python", "envio_mensagem.py"]