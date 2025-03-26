import httpx
import asyncio
import os
from mcp.server.fastmcp import FastMCP, Context
from typing import Union, List

# Create an MCP server
mcp = FastMCP("WhatsApp Sender")

# API configuration from environment variables
BASE_API_URL = os.environ.get("BASE_API_URL", "https://evodesent2.gorgolead.com.br")
API_KEY = os.environ.get("API_KEY", "429683C4C97741ACAS1DAS4A9SJS72")
DEFAULT_INSTANCE = os.environ.get("DEFAULT_INSTANCE", "default")

@mcp.tool()
async def send_whatsapp_message(phone_number: Union[str, int], message: str, instance_name: str = None, ctx: Context = None) -> str:
    """Sends a WhatsApp message to the specified number.
    
    Args:
        phone_number: The phone number to send the message to (include country code, no spaces or symbols). Can be string or integer.
        message: The text message to send.
        instance_name: The WhatsApp instance name to use (optional, uses default if not specified).
    
    Returns:
        A string indicating success or failure of the message send attempt.
    """
    # Use default instance if none provided
    if instance_name is None:
        instance_name = DEFAULT_INSTANCE
    
    # Converter explicitamente para string logo no início para garantir compatibilidade
    phone_number = str(phone_number)
    
    # Log the request attempt
    if ctx:
        ctx.info(f"Attempting to send message to {phone_number} using instance {instance_name}")
    
    # Format phone number if needed (removing spaces, +, etc.)
    cleaned_number = ''.join(filter(str.isdigit, phone_number))
    
    # Validar se o número está em um formato válido
    if not cleaned_number or len(cleaned_number) < 10:
        return "❌ Número de telefone inválido. Certifique-se de incluir código do país e DDD."
    
    # Build the complete API URL with the instance name
    api_url = f"{BASE_API_URL}/message/sendText/{instance_name}"
    
    # Prepare the request
    headers = {
        "Content-Type": "application/json",
        "apikey": API_KEY
    }
    
    payload = {
        "number": cleaned_number,
        "text": message
    }
    
    try:
        # Send the request
        async with httpx.AsyncClient() as client:
            response = await client.post(api_url, json=payload, headers=headers)
            
        # Check if the request was successful
        if 200 <= response.status_code < 300:
            return f"✅ Message sent successfully to {phone_number}."
        else:
            error_info = response.text
            return f"❌ Failed to send message. Status code: {response.status_code}. Error: {error_info}"
    
    except Exception as e:
        # Handle any exceptions
        return f"❌ Error sending message: {str(e)}"

@mcp.tool()
async def send_whatsapp_with_interval(phone_numbers: List[Union[str, int]], message: str, instance_name: str = None, interval_seconds: int = 0, ctx: Context = None) -> str:
    """
    Sends a WhatsApp message to multiple numbers with a specified interval between each message.
    
    Args:
        phone_numbers: List of phone numbers (string or integer) to send the message to.
        message: The text message to send to all numbers.
        instance_name: The WhatsApp instance name to use (optional, uses default if not specified).
        interval_seconds: Time to wait between each message in seconds (default: 0).
        
    Returns:
        A string summarizing the results of all message send attempts.
    """
    # Use default instance if none provided
    if instance_name is None:
        instance_name = DEFAULT_INSTANCE
        
    results = []
    success_count = 0
    failure_count = 0
    
    for i, phone in enumerate(phone_numbers):
        if ctx:
            ctx.info(f"Sending message to {phone} ({i+1}/{len(phone_numbers)})")
        
        # Converter explicitamente para string
        phone_str = str(phone)
        result = await send_whatsapp_message(phone_str, message, instance_name, ctx)
        results.append(result)
        
        if "✅" in result:
            success_count += 1
        else:
            failure_count += 1
        
        # Wait for the specified interval before sending the next message
        if i < len(phone_numbers) - 1 and interval_seconds > 0:
            if ctx:
                ctx.info(f"Waiting for {interval_seconds} seconds before next message...")
            await asyncio.sleep(interval_seconds)
    
    summary = f"Sent {success_count} messages successfully, {failure_count} failed."
    return summary + "\n" + "\n".join(results)

@mcp.tool()
async def send_whatsapp_media(phone_number: Union[str, int], media_url: str, media_type: str, instance_name: str = None, ctx: Context = None) -> str:
    """
    Sends a media message (image, video, document, or audio) via WhatsApp to the specified number.
    
    Args:
        phone_number: The phone number to send the message to (include country code, no spaces or symbols). Can be string or integer.
        media_url: URL of the media to be sent.
        media_type: Type of media ('image', 'video', 'document', or 'audio').
        instance_name: The WhatsApp instance name to use (optional, uses default if not specified).
    
    Returns:
        A string indicating success or failure of the media send attempt.
    """
    # Use default instance if none provided
    if instance_name is None:
        instance_name = DEFAULT_INSTANCE
        
    if ctx:
        ctx.info(f"Attempting to send {media_type} to {phone_number} using instance {instance_name}")
    
    phone_number = str(phone_number)
    cleaned_number = ''.join(filter(str.isdigit, phone_number))
    
    if not cleaned_number or len(cleaned_number) < 10:
        return "❌ Número de telefone inválido. Certifique-se de incluir código do país e DDD."
    
    valid_media_types = ['image', 'video', 'document', 'audio']
    if media_type.lower() not in valid_media_types:
        return f"❌ Tipo de mídia inválido. Deve ser um dos seguintes: {', '.join(valid_media_types)}"
    
    api_url = f"{BASE_API_URL}/message/sendMedia/{instance_name}"
    
    headers = {
        "Content-Type": "application/json",
        "apikey": API_KEY
    }
    
    payload = {
        "number": cleaned_number,
        "mediatype": media_type.lower(),
        "media": media_url
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(api_url, json=payload, headers=headers)
            
        if 200 <= response.status_code < 300:
            return f"✅ {media_type.capitalize()} sent successfully to {phone_number}."
        else:
            error_info = response.text
            return f"❌ Failed to send {media_type}. Status code: {response.status_code}. Error: {error_info}"
    
    except Exception as e:
        return f"❌ Error sending {media_type}: {str(e)}"

@mcp.tool()
async def send_whatsapp_media_with_interval(phone_numbers: List[Union[str, int]], media_url: str, media_type: str, instance_name: str = None, interval_seconds: int = 0, ctx: Context = None) -> str:
    """
    Sends a media message (image, video, document, or audio) to multiple numbers with a specified interval.
    
    Args:
        phone_numbers: List of phone numbers (string or integer) to send the media to.
        media_url: URL of the media to be sent.
        media_type: Type of media ('image', 'video', 'document', or 'audio').
        instance_name: The WhatsApp instance name to use (optional, uses default if not specified).
        interval_seconds: Time to wait between each message in seconds (default: 0).
        
    Returns:
        A string summarizing the results of all media send attempts.
    """
    # Use default instance if none provided
    if instance_name is None:
        instance_name = DEFAULT_INSTANCE
        
    results = []
    success_count = 0
    failure_count = 0
    
    for i, phone in enumerate(phone_numbers):
        if ctx:
            ctx.info(f"Sending {media_type} to {phone} ({i+1}/{len(phone_numbers)})")
        
        phone_str = str(phone)
        result = await send_whatsapp_media(phone_str, media_url, media_type, instance_name, ctx)
        results.append(result)
        
        if "✅" in result:
            success_count += 1
        else:
            failure_count += 1
        
        if i < len(phone_numbers) - 1 and interval_seconds > 0:
            if ctx:
                ctx.info(f"Waiting for {interval_seconds} seconds before next message...")
            await asyncio.sleep(interval_seconds)
    
    summary = f"Sent {success_count} media messages successfully, {failure_count} failed."
    return summary + "\n" + "\n".join(results)

@mcp.tool()
async def check_instance_status(instance_name: str = None, ctx: Context = None) -> str:
    """
    Verifica se uma instância específica está funcionando.
    
    Args:
        instance_name: Nome da instância do WhatsApp a ser verificada (opcional, usa a padrão se não especificada).
    
    Returns:
        Uma string indicando o status da instância e informações adicionais.
    """
    # Use default instance if none provided
    if instance_name is None:
        instance_name = DEFAULT_INSTANCE
        
    if ctx:
        ctx.info(f"Verificando status da instância {instance_name}")
    
    api_url = f"{BASE_API_URL}/instance/connectionState/{instance_name}"
    
    headers = {
        "apikey": API_KEY
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(api_url, headers=headers)
        
        if 200 <= response.status_code < 300:
            data = response.json()
            status = data.get("state", "Desconhecido")
            connected = "Conectada" if status == "CONNECTED" else "Desconectada"
            
            status_info = f"Instância: {instance_name}\n"
            status_info += f"Status: {connected} ({status})\n"
            
            if "qrcode" in data:
                status_info += "QR Code disponível para conexão\n"
            
            return status_info
        else:
            error_info = response.text
            return f"Falha ao verificar o status da instância. Código de status: {response.status_code}. Erro: {error_info}"
    
    except Exception as e:
        return f"Erro ao verificar o status da instância: {str(e)}"

if __name__ == "__main__":
    # Run the server
    mcp.run()