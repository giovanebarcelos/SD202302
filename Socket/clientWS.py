import asyncio
import websockets


async def send_messages():
  # Configuração do cliente WebSocket
  uri = "ws://127.0.0.1:8765"
  async with websockets.connect(uri) as websocket:
    while True:
      # Solicita que o cliente insira uma mensagem
      message = input(
          "Digite uma mensagem para o servidor (ou digite 'exit' para sair): ")
      if message.lower() == 'exit':
        break  # Sai do loop se o cliente digitar 'exit'

      # Envia a mensagem para o servidor
      await websocket.send(message)

      # Recebe a resposta do servidor
      response = await websocket.recv()
      print(f"Servidor diz: {response}")


# Inicia o loop de eventos do cliente
asyncio.get_event_loop().run_until_complete(send_messages())
