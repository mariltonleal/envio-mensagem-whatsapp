# Servidor MCP para WhatsApp

Este projeto implementa um servidor MCP (Multi-Cloud Protocol) para envio de mensagens e arquivos via WhatsApp utilizando a Evolution API.

## Funcionalidades

- Envio de mensagens de texto para números individuais
- Envio de mensagens de texto em lote com intervalo configurável
- Envio de arquivos de mídia (imagem, vídeo, documento, áudio)
- Envio de arquivos de mídia em lote com intervalo configurável
- Verificação de status de instâncias do WhatsApp

## Requisitos

- Python 3.8+
- Biblioteca `httpx`
- Biblioteca `asyncio`
- Framework `fastmcp`
- Uma instância do Evolution API em execução

## Instalação

1. Clone este repositório:
```bash
git clone https://github.com/mariltonleal/envio-mensagem-whatsapp.git
cd envio-mensagem-whatsapp
```

2. Instale as dependências:
```bash
pip install httpx fastmcp
```

## Configuração

1. Configure a URL da API e sua chave de API no arquivo `envio_mensagem.py`:
```python
BASE_API_URL = "https://sua-instancia-evolution-api.com"
API_KEY = "sua-chave-api"
```

2. Certifique-se de que sua instância do Evolution API esteja configurada e em execução.

## Uso

### Iniciar o servidor

```bash
python envio_mensagem.py
```

### Exemplos de uso

#### Enviar mensagem de texto

```python
await send_whatsapp_message("5511999999999", "Olá, esta é uma mensagem de teste!", "minha-instancia")
```

#### Enviar mensagens em lote

```python
numeros = ["5511999999999", "5521888888888", "5531777777777"]
await send_whatsapp_with_interval(numeros, "Mensagem em lote de teste", "minha-instancia", interval_seconds=5)
```

#### Enviar mídia

```python
await send_whatsapp_media("5511999999999", "https://exemplo.com/imagem.jpg", "image", "minha-instancia")
```

#### Verificar status da instância

```python
status = await check_instance_status("minha-instancia")
print(status)
```

## Funções disponíveis

- `send_whatsapp_message`: Envia uma mensagem de texto para um número
- `send_whatsapp_with_interval`: Envia mensagens para múltiplos números com intervalo
- `send_whatsapp_media`: Envia mídia para um número
- `send_whatsapp_media_with_interval`: Envia mídia para múltiplos números com intervalo
- `check_instance_status`: Verifica o status de uma instância WhatsApp

## Segurança

⚠️ **Importante:** Não compartilhe sua chave API ou credenciais em repositórios públicos.

## Licença

Este projeto é distribuído sob a licença MIT.