# Instruções para testar o build do Docker localmente

Antes de fazer o deploy no Smithery, é importante garantir que a imagem Docker está construindo corretamente. Siga estas instruções para testar localmente:

## Pré-requisitos

- Ter o Docker instalado em sua máquina. [Guia de instalação do Docker](https://docs.docker.com/get-docker/)
- Ter clonado o repositório em sua máquina local

## Passos para testar o build

1. Navegue até o diretório do projeto onde está o Dockerfile:

```bash
cd envio-mensagem-whatsapp
```

2. Execute o comando para construir a imagem Docker:

```bash
docker build -t whatsapp-mcp .
```

Se a construção for bem-sucedida, você verá uma mensagem semelhante a:
```
Successfully built [ID_DA_IMAGEM]
Successfully tagged whatsapp-mcp:latest
```

3. (Opcional) Execute a imagem para testar se o servidor inicia corretamente:

```bash
docker run -p 8080:8080 -e BASE_API_URL=https://sua-api.exemple.com -e API_KEY=sua-chave-api whatsapp-mcp
```

## Explicação das alterações recentes

### Instalação do fastmcp diretamente do GitHub

Devido a problemas de compatibilidade com o pacote publicado no PyPI, modificamos a instalação do fastmcp para usar diretamente o repositório GitHub oficial:

```
git+https://github.com/AnthropicMmcpSdk/fastmcp.git
```

Esta abordagem garante que estamos usando a versão mais recente e compatível com nosso ambiente Python.

### Adição de ferramentas de diagnóstico

Atualizamos o Dockerfile para:
- Instalar o git (necessário para instalar pacotes diretamente do GitHub)
- Atualizar o pip para a versão mais recente
- Adicionar diagnósticos para mostrar a versão do Python e do pip durante o build

## Solução de problemas comuns

### Erro: Could not find a version that satisfies the requirement fastmcp>=0.1.0

Este erro foi resolvido instalando o fastmcp diretamente do GitHub em vez de usar o PyPI.

### Erro: Could not find a version that satisfies the requirement asyncio

Este erro ocorre porque `asyncio` é um módulo built-in do Python 3.4+ e não deve ser instalado via pip. Foi corrigido removendo esta dependência do arquivo `requirements.txt`.

### Erro: No such file or directory: requirements_whatsapp.txt

Este erro ocorre porque o Dockerfile estava referenciando um arquivo que não existe. Isso foi corrigido consolidando todas as dependências em um único arquivo `requirements.txt`.

## Depois do teste bem-sucedido

Após confirmar que a imagem Docker constrói corretamente em sua máquina local:

1. Volte ao Smithery e tente o deployment novamente.