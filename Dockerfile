FROM python:3.9-slim

WORKDIR /app

# Copiar arquivos de requisitos
COPY requirements.txt .
COPY requirements_whatsapp.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements_whatsapp.txt

# Copiar o código do servidor
COPY envio_mensagem.py .

# Comando para iniciar o servidor MCP
CMD ["python", "envio_mensagem.py"]