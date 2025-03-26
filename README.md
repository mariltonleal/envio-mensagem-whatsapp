# Servidor MCP para WhatsApp

Este projeto implementa um servidor MCP (Multi-Cloud Protocol) para envio de mensagens e arquivos via WhatsApp utilizando a Evolution API.

## Funcionalidades

- Envio de mensagens de texto para números individuais
- Envio de mensagens de texto em lote com intervalo configurável
- Envio de arquivos de mídia (imagem, vídeo, documento, áudio)
- Envio de arquivos de mídia em lote com intervalo configurável
- Verificação de status de instâncias do WhatsApp

## Uso no Smithery

Este servidor está disponível no Smithery, permitindo que você utilize-o sem precisar instalar ou configurar nada localmente. Para usar através do Smithery:

1. Acesse a página do servidor no Smithery
2. Configure as seguintes opções:
   - **URL da API Evolution**: URL da sua instância da Evolution API
   - **Chave da API**: Sua chave de API da Evolution
   - **Nome da Instância**: (Opcional) Nome da instância do WhatsApp que você deseja usar

Todas as chamadas de API serão processadas com segurança no ambiente do Smithery.

## Instalação Local

### Requisitos

- Python 3.8+
- Biblioteca `httpx`
- Biblioteca `asyncio`
- Framework `fastmcp`
- Uma instância do Evolution API em execução

### Passo a Passo

1. Clone este repositório:
```bash
git clone https://github.com/mariltonleal/envio-mensagem-whatsapp.git
cd envio-mensagem-whatsapp
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Configuração

1. Configure a URL da API e sua chave de API usando variáveis de ambiente:
```bash
export BASE_API_URL="https://sua-instancia-evolution-api.com"
export API_KEY="sua-chave-api"
export DEFAULT_INSTANCE="nome-da-instancia"
```

2. Ou modifique diretamente no arquivo `envio_mensagem.py`:
```python
BASE_API_URL = "https://sua-instancia-evolution-api.com"
API_KEY = "sua-chave-api"
DEFAULT_INSTANCE = "nome-da-instancia"
```

3. Certifique-se de que sua instância do Evolution API esteja configurada e em execução.

## Uso Local

### Iniciar o servidor

```bash
python envio_mensagem.py
```

### Exemplos de uso

#### Enviar mensagem de texto

```python
await send_whatsapp_message("5511999999999", "Olá, esta é uma mensagem de teste!")
```

#### Enviar mensagens em lote

```python
numeros = ["5511999999999", "5521888888888", "5531777777777"]
await send_whatsapp_with_interval(numeros, "Mensagem em lote de teste", interval_seconds=5)
```

#### Enviar mídia

```python
await send_whatsapp_media("5511999999999", "https://exemplo.com/imagem.jpg", "image")
```

#### Verificar status da instância

```python
status = await check_instance_status()
print(status)
```

## Funções disponíveis

- `send_whatsapp_message`: Envia uma mensagem de texto para um número
- `send_whatsapp_with_interval`: Envia mensagens para múltiplos números com intervalo
- `send_whatsapp_media`: Envia mídia para um número
- `send_whatsapp_media_with_interval`: Envia mídia para múltiplos números com intervalo
- `check_instance_status`: Verifica o status de uma instância WhatsApp

## Deployment no Smithery

Este servidor pode ser facilmente implantado no Smithery para permitir que outros usuários utilizem-no através de WebSockets. Para configurar o deployment:

1. Certifique-se de que o repositório contenha os arquivos `Dockerfile` e `smithery.yaml`
2. Adicione seu servidor ao Smithery ou reivindique-o se já estiver listado
3. Clique em "Deploy" na aba Smithery Deployments na página do seu servidor

O Smithery criará um playground para seu servidor, permitindo que usuários o testem online sem instalar dependências.

## Segurança

⚠️ **Importante:** Não compartilhe sua chave API ou credenciais em repositórios públicos.

## Licença

Este projeto é distribuído sob a licença MIT.