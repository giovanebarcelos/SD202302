# pip install websockets
import asyncio
import websockets

# Configuração do servidor WebSocket
host = '127.0.0.1'
port = 8765


# Função que trata as mens recebidas do cliente
async def handle_client(websocket, path):
  async for message in websocket:
    print(f"Cliente diz: {message}")
    await websocket.send(f"Servidor recebeu: {message}")


# Inicia o servidor WebSocket
start_server = websockets.serve(handle_client, host, port)
print(f"Servidor WebSocket iniciado em ws://{host}:{port}")

# Inicia o loop de eventos do servidor
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
